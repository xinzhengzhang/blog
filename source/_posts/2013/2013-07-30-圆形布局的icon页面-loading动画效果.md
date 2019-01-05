---
layout: post
title: 圆形布局的icon页面 loading动画效果
categories:
- program
tags: []
published: true
comments: true
---
<p><a href="http://snorlax-wordpress.stor.sinaapp.com/uploads/2013/07/700BAD52-7C3F-4500-8B52-69C13291528D.jpg"><img src="http://snorlax-wordpress.stor.sinaapp.com/uploads/2013/07/700BAD52-7C3F-4500-8B52-69C13291528D.jpg" alt="" title="700BAD52-7C3F-4500-8B52-69C13291528D" width="314" height="470" class="alignnone size-full wp-image-397" /></a>
大致效果就是3个元素根据不同时间间隔开始沿着圆进行无限追逐，每次一圈后进行一个小停顿然后继续、比较类似wp7的那种小的loading、主要用到的还是CAKeyframeAnimation其中为了让无限循环中加上停顿用了个小trick
</p>

```objective-c
#import <QuartzCore/QuartzCore.h>
#define PI 3.14159265358979323846
@interface canvas ()
{
    UIButton *red;
    UIButton *green;
    UIButton *yellow;
}

@end

@implementation canvas

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
        red=[[UIButton alloc]initWithFrame:CGRectMake(117.55-10, 38.1-10, 10, 10)];
        green=[[UIButton alloc]initWithFrame:CGRectMake(141.42-10, 58.57-10, 10, 10)];
        yellow=[[UIButton alloc]initWithFrame:CGRectMake(173.2-10, 100-10, 10, 10)];
        [red setBackgroundColor:[UIColor redColor]];
        [green setBackgroundColor:[UIColor greenColor]];
        [yellow setBackgroundColor:[UIColor yellowColor]];
        [red addTarget:self action:@selector(end) forControlEvents:UIControlEventTouchUpInside];
        [yellow addTarget:self action:@selector(start) forControlEvents:UIControlEventTouchUpInside];

        [self start];
        [self addSubview:red];
        [self addSubview:green];
        [self addSubview:yellow];
    }
    return self;
}
-(void)end{
    [red.layer removeAllAnimations];
    [green.layer removeAllAnimations];
    [yellow.layer removeAllAnimations];
}
-(void)start{
    CGMutablePathRef path=CGPathCreateMutable();
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.8424, -0.8424+2*PI, NO);//用cgpath画出运动轨迹
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.8424, -0.9424, YES);
    CAKeyframeAnimation *animation=[CAKeyframeAnimation animationWithKeyPath:@"position"];
    [animation setCalculationMode:kCAAnimationPaced];
    [animation setPath:path];
    [animation setDuration:2.0f];
    [animation setTimingFunction:[CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseInEaseOut]];
//    [animation setBeginTime:CACurrentMediaTime()+0.7];
//    [animation setRepeatCount:HUGE_VALF];
    CFRelease(path);
    CAAnimationGroup *animationGroup = [CAAnimationGroup animation];//利用动画组的间隔做到小动画的无限间隔之间的停顿
    animationGroup.duration = 3;
    animationGroup.repeatCount = INFINITY;
    animationGroup.animations=@[animation];
    [animationGroup setBeginTime:CACurrentMediaTime()+0.5];//让三个元素起始时间区分开
    [red.layer addAnimation:animationGroup forKey:NULL];
    path=CGPathCreateMutable();
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.683, -0.683+2*PI, NO);
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.683, -0.783, YES);
    animation=[CAKeyframeAnimation animationWithKeyPath:@"position"];
    [animation setCalculationMode:kCAAnimationPaced];
    [animation setPath:path];
    [animation setDuration:2.0f];
    [animation setTimingFunction:[CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseInEaseOut]];
//    [animation setBeginTime:CACurrentMediaTime()+0.5];
//    [animation setRepeatCount:HUGE_VALF];

    CFRelease(path);
    animationGroup = [CAAnimationGroup animation];<br />
    animationGroup.duration = 3;<br />
    animationGroup.repeatCount = INFINITY;<br />
    animationGroup.animations=@[animation];<br />
    [animationGroup setBeginTime:CACurrentMediaTime()+0.2];<br />
    [green.layer addAnimation:animationGroup forKey:NULL];<br />
    <br />
    path=CGPathCreateMutable();<br />
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.425, -0.425+2*PI, NO);<br />
    CGPathAddArc(path, NULL, 0.0f, 200.0f, 200, -0.425, -0.525, YES);<br />
    animation=[CAKeyframeAnimation animationWithKeyPath:@"position"];<br />
    [animation setCalculationMode:kCAAnimationPaced];<br />
    [animation setPath:path];<br />
    [animation setDuration:2.0f];<br />
//    [animation setRepeatCount:HUGE_VALF];</p>

    [animation setTimingFunction:[CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseInEaseOut]];

    CFRelease(path);
    animationGroup = [CAAnimationGroup animation];
    animationGroup.duration = 3;
    animationGroup.repeatCount = INFINITY;
    animationGroup.animations=@[animation];
    [yellow.layer addAnimation:animationGroup forKey:NULL];
}

// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    CGContextRef context = UIGraphicsGetCurrentContext();
    CGContextSetStrokeColor(context, [UIColor blueColor].CGColor);
    CGContextAddArc(context, 0.0, 200.0f, 200, 0, 2*PI, YES);

    [[UIColor orangeColor] setFill];
    [[UIColor blueColor] setStroke];
    CGContextDrawPath (context, kCGPathStroke);
}

@end
```
