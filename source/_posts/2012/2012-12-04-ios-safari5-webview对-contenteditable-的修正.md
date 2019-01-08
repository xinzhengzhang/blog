---
date: 2012-12-04
layout: post
title: ios safari5 webview对 contenteditable 的修正
categories:
- program
tags: []
published: true
comments: true
---
<p>自从上次发现了html5的神器标签contenteditable后一直忽视了一个问题、因为一直跑的机器都是ios6（六毫无问题）、当放到5时出一个很大的问题、每次进入编辑时焦点会被放到整个body的最上面、毫无疑问这个糟糕的体验是不可能让用户自己去解决的所以需要解决。</p>

<p>首先先是native和js交互的问题、也许js太过庞大、webview完全没有做任何关于js callback的api、唯一只有一个<br />
- (NSString *)stringByEvaluatingJavaScriptFromString:(NSString *)script;<br />
只能往里插js却获不得回调、这样没人性的行为绝对是无法容忍的、竟然phonegap什么的可以就一定有解决途径。<br />
既然js无法获得回调、就从webview的回调入手、查了他的三个delegate后办法有了、就是更改document.location加一个?xx=xx相当于一个get请求、然后通过回调去拿到xx然后做native<br />
可是这样我马上就发现了不适宜contenteditable的一个问题、就是一个点击事件同时触发了编辑以及跳转事件后、后者覆盖了前者、网上主流说的也是这个方法、找了半天终于找到了替代法<a href="http://blog.devtang.com/blog/2012/03/24/talk-about-uiwebview-and-phonegap/"></a>详见最后的这段js代码、最后需要做的就是给需要编辑的标签绑定上事件 通过鼠标的点击拿到pageY的偏移量 通过uiwebview.uiscrollview setContentOffset来调整偏移量即可修复safari5对contenteditable这极不友好的支持、代码如下</p>

<p>
```

var edit = document.getElementById(\"editable\");edit.addEventListener(\"click\",function(e){var iFrame;iFrame = document.createElement(\"iframe\");iFrame.setAttribute(\"src\", \"noteOffset:\"+e.pageY);iFrame.setAttribute(\"style\", \"display:none;\");iFrame.setAttribute(\"height\", \"0px\");iFrame.setAttribute(\"width\", \"0px\");iFrame.setAttribute(\"frameborder\", \"0\");document.body.appendChild(iFrame);iFrame.parentNode.removeChild(iFrame);iFrame = null;}, false);

然后在回调中写

#pragma UIWebViewDelegate
-(BOOL)webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType
{
    NSLog(@"------");
    NSLog(@"%@",[[request URL]absoluteString]);
    if ([[[request URL]absoluteString]judgeNoteBodyEditMode] && [[request URL]absoluteString].length>>3) {
        
        NSLog(@"%d",[[[[request URL]absoluteString]substringFromIndex:[[request URL]absoluteString].length-3]integerValue]);
        [showRichText.scrollView setContentOffset:CGPointMake(showRichText.scrollView.contentOffset.x,[[[[request URL]absoluteString]substringFromIndex:[[request URL]absoluteString].length-3]integerValue])];
    }
    return YES;
}
</pre></p>

```
