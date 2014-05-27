---
layout: post
title: 分享一个webview和js交互的封装
categories:
- program
tags: []
published: true
comments: true
---
<p><a href="https://github.com/marcuswestin/WebViewJavascriptBridge">marcuswestin / WebViewJavascriptBridge</a>
<strong>1) Copy Classes/WebViewJavascriptBridge.h and Classes/WebViewJavascriptBridge.m into your Xcode project</strong></p>

<p><strong>2) Instantiate a UIWebView, a WebViewJavascriptBridge, and set yourself as the bridge's delegate</strong>

```

   #import 
#import "WebViewJavascriptBridge.h"

@interface ExampleAppDelegate : UIResponder 

@end

@implementation ExampleAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];

    self.webView = [[UIWebView alloc] initWithFrame:self.window.bounds];
    [self.window addSubview:webView];
    self.javascriptBridge = [WebViewJavascriptBridge javascriptBridgeWithDelegate:self];
    self.webView.delegate = javascriptBridge;

    [self.window makeKeyAndVisible];
    return YES;
}

- (void)javascriptBridge:(WebViewJavascriptBridge *)bridge receivedMessage:(NSString *)message fromWebView:(UIWebView *)webView 
{
    NSLog(@"MyJavascriptBridgeDelegate received message: %@", message);
}

@end

3) Go ahead and send some messages from Objc to javascript


[self.javascriptBridge sendMessage:@"Well hello there" toWebView:self.webView];


4) Finally, set up the javascript side of things

document.addEventListener('WebViewJavascriptBridgeReady', function onBridgeReady() {
    WebViewJavascriptBridge.setMessageHandler(function(message) {
        alert('Received message: ' + message)
    })
    WebViewJavascriptBridge.sendMessage('Hello from the javascript')
}, false)

>

```
