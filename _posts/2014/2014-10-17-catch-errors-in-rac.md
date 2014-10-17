---
layout: post
title: "ReactiveCocoa中RAC绑定时Error的处理"
description: ""
category: program
tags: ["ReactiveCocoa", "objective-c"]
---
{% include JB/setup %}

### 背景
  * 大致情况是bind了一个`NSData`到一个由`NSURLConnection`拓展出来的signal中、当网络请求超时时一定发生crash

#### 关键代码
  * `RACSignal+Operations.m` line 629-643 
	* 查看RAC宏定义发现入口时下面
	* `- (RACDisposable *)setKeyPath:(NSString *)keyPath onObject:(NSObject *)object nilValue:(id)nilValue;`
	* 如下代码中可以发现其实在当error时候直接assert掉了关于这里作者是这么说的
	  * Errors that occur in a property binding are generally not corrupting. You're more likely to see weird UI glitches than a completely broken document, so crashing may be an unreasonable response.
	  * But, of course, we really have no way of knowing. Maybe we should just fail fast.
	* 不过个人认为这也只是在可控制状态下这样强硬的要求也的确不错、可是在比如网络请求下就出大坑了……


	```objective-c
		RACDisposable *subscriptionDisposable = [self subscribeNext:^(id x) {
		NSObject *object = (__bridge id)objectPtr;
		[object setValue:x ?: nilValue forKeyPath:keyPath];
	} error:^(NSError *error) {
		NSObject *object = (__bridge id)objectPtr;

		NSCAssert(NO, @"Received error from %@ in binding for key path \"%@\" on %@: %@", self, keyPath, object, error);

		// Log the error if we're running with assertions disabled.
		NSLog(@"Received error from %@ in binding for key path \"%@\" on %@: %@", self, keyPath, object, error);

		[disposable dispose];
	} completed:^{
		[disposable dispose];
	}];
	```
  * 继续看`NSURLConnection+RACSupport.m`中的对NSURLConnection中的拓展
  * 其中最致命的问题也就是当在一个request回来时判定了当data为空时直接向signal send error了、这也就导致了为什么仅仅只是在超时的时候发送了error、而没有在别的网络错误时crash、因为那个时候data虽然不是你想要的但至少不是空

	```objective-c
	+ (RACSignal *)rac_sendAsynchronousRequest:(NSURLRequest *)request {
	NSCParameterAssert(request != nil);

	return [[RACSignal
		createSignal:^ RACDisposable * (id<RACSubscriber> subscriber) {
			NSOperationQueue *queue = [[NSOperationQueue alloc] init];
			queue.name = @"com.github.ReactiveCocoa.NSURLConnectionRACSupport";

			[NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse *response, NSData *data, NSError *error) {
				if (data == nil) {
					[subscriber sendError:error];
				} else {
					[subscriber sendNext:RACTuplePack(response, data)];
					[subscriber sendCompleted];
				}
			}];

			return [RACDisposable disposableWithBlock:^{
				// It's not clear if this will actually cancel the connection,
				// but we can at least prevent _some_ unnecessary work --
				// without writing all the code for a proper delegate, which
				// doesn't really belong in RAC.
				queue.suspended = YES;
				[queue cancelAllOperations];
			}];
		}]
		setNameWithFormat:@"+rac_sendAsynchronousRequest: %@", request];
	}
	```

#### 问题代码
  * `RAC(photoModel, fullsizedData) = [self download:photoModel.fullsizedURL];` 其中fullsizeData为一个NSData

	```objective-c
	+(RACSignal *)download:(NSString *)urlString {
    NSAssert(urlString, @"URL must not be nil");
    
    NSURLRequest *request = [NSURLRequest requestWithURL:[NSURL URLWithString:urlString]];
    return [[[NSURLConnection rac_sendAsynchronousRequest:request] reduceEach:^id(NSURLResponse *response, NSData *data){
        return data;
    }] deliverOn:[RACScheduler mainThreadScheduler]];
	}
	```

#### 发生原因梳理
  * RAC 绑定了一个由 NSURLConnection 的 rac_sendAsynchronousRequest生成出的signal
  * 在网络超时时候发出了error信号、导致rac绑定crash

#### 问题解决方法
  * 在subscribe那个网络信号的时候进行catch error操作

	```objective-c
	[[[[NSURLConnection rac_sendAsynchronousRequest:request] reduceEach:^id(NSURLResponse *response, NSData *data){
        return data;
    }] deliverOn:[RACScheduler mainThreadScheduler]] catch:^RACSignal*(NSError *error){
        NSLog(@"error =%@", error);
        return [RACSignal empty];
    }];
    ```

  * 在 [传送门](https://github.com/ReactiveCocoa/ReactiveCocoa/commit/37bbe0d5340e5180db111694f584f927df474824)这个pull request之中……当然这是个针对swift的branch中加入了`errorHandler`[传送门](https://github.com/ReactiveCocoa/ReactiveCocoa/commit/09c3d739579abfc51df5d56ed0c7e09c20a8fac8)解决了这个问题