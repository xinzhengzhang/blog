---
layout: post
title: 定制 UIPageControl
categories:
- program
tags: []
published: true
comments: true
---
<p>pagecontrol 就是iphone上面比如scrollview翻图片时候下面那个小点点<br />
其实我个人觉得还是挺美观的……可是需求就是要自己的图片替掉……然后死人苹果又不给api、所以也就只能自己复写实现了<br />
先说下ios7之前 那些点点的实现非常简单 就是UIPageControl.subviews 就是一个个点的UIImageView 所以只需简单的替换掉就好了代码如下

```

@property(nonatomic,strong)UIImage *_activeImage;
@property(nonatomic,strong)UIImage *_inactiveImage;
//在init的时候把你自己定义的两张图片搞进去
- (void)updateDots
{
    for (int i = 0; i

        if (i == self.currentPage) {
            if ([dot respondsToSelector:@selector(setImage:)]) {
                dot.image=_activeImage;
            }

        } else {
            if ([dot respondsToSelector:@selector(setImage:)]) {
                dot.image=_inactiveImage;
            }
        }
    }
}
//然后自己重载一下setNumber就好了

- (void)setNumberOfPages:(NSInteger)numberOfPages
{
    [super setNumberOfPages:numberOfPages];
    [self updateDots];
}

但是呢万恶的ios7改掉了尼玛……连底层实现都改啊混蛋……可以对self.subviews 标红一下就明白了……整个pagecontrol的uivew乱七八糟……而且都是view根本就没了image属性、换句话说现在的那些小点点都是代码写出来的了、而不是简单图了
实现起来就要重写UIView的绘画函数了代码大致如下

#import "ZDPageControll.h"
#import

@interface ZDPageControll()
{
    UIImage *_activeImage;
    UIImage *_inactiveImage;
    NSArray *_usedToRetainOriginalSubview;
}

@end

@implementation ZDPageControll
@synthesize kSpacing=_kSpacing;
- (id)initWithFrame:(CGRect)frame currentImageName:(NSString *)current commonImageName:(NSString *)common
{
    self= [super initWithFrame:frame];
    if ([self respondsToSelector:@selector(setCurrentPageIndicatorTintColor:)] && [self respondsToSelector:@selector(setPageIndicatorTintColor:)]) {
        [self setCurrentPageIndicatorTintColor:[UIColor clearColor]];
        [self setPageIndicatorTintColor:[UIColor clearColor]];
    }

    [self setBackgroundColor:[UIColor clearColor]];
    _activeImage= [UIImage imageNamed:current];
    _inactiveImage= [UIImage imageNamed:common];
    _kSpacing=10.0f;
    //hold住原来pagecontroll的subview
    _usedToRetainOriginalSubview=[NSArray arrayWithArray:self.subviews];
    for (UIView *su in self.subviews) {
        [su removeFromSuperview];
    }
    self.contentMode=UIViewContentModeRedraw;
    return self;
}
-(void)dealloc
{
    //释放原来hold住的那些subview
    _usedToRetainOriginalSubview=nil;
    _activeImage=nil;
    _inactiveImage=nil;
}
- (void)updateDots
{

    for (int i = 0; i
        UIImageView* dot =[self.subviews objectAtIndex:i];

        if (i == self.currentPage) {
            if ([dot respondsToSelector:@selector(setImage:)]) {
                dot.image=_activeImage;
            }

        } else {
            if ([dot respondsToSelector:@selector(setImage:)]) {
                dot.image=_inactiveImage;
            }
        }
    }

}

- (void)setCurrentPage:(NSInteger)currentPage
{
    [super setCurrentPage:currentPage];
    if ([[[UIDevice currentDevice]systemVersion]floatValue]
        [self updateDots];
    }
//    [self updateDots];
    [self setNeedsDisplay];
}
- (void)setNumberOfPages:(NSInteger)numberOfPages
{
    [super setNumberOfPages:numberOfPages];
    if ([[[UIDevice currentDevice]systemVersion]floatValue]
        [self updateDots];
    }
//    [self updateDots];
    [self setNeedsDisplay];

}
-(void)drawRect:(CGRect)iRect
{
    int i;
    CGRect rect;

    UIImage *image;
    iRect = self.bounds;

    if ( self.opaque ) {
        [self.backgroundColor set];
        UIRectFill( iRect );
    }

    if ( self.hidesForSinglePage && self.numberOfPages == 1 ) return;

    rect.size.height = _activeImage.size.height;
    rect.size.width = self.numberOfPages * _activeImage.size.width + ( self.numberOfPages - 1 ) * _kSpacing;
    rect.origin.x = floorf( ( iRect.size.width - rect.size.width ) / 2.0 );
    rect.origin.y = floorf( ( iRect.size.height - rect.size.height ) / 2.0 );
    rect.size.width = _activeImage.size.width;

    for ( i = 0; i
        image = i == self.currentPage ? _activeImage : _inactiveImage;

        [image drawInRect: rect];

        rect.origin.x += _activeImage.size.width + _kSpacing;
    }
}
@end


>

```
