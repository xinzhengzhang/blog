---
date: 2013-01-07
layout: post
title: 关于嵌套与UIScrollView中的UITableVIew的冲突解决
categories:
- program
tags: []
published: true
comments: true
---
<p>周知tableview是继承自scrollview的、一旦如果在scrollview上add上子的table那么双方的滚动就冲突了、只能选择其一、apple的文档里也讲了两者是冲突的不要加子table到scroll上、但是发现其实还是有解决方法的<br />
首先的关键点就是禁掉两方的任意一个ScrollEnabled另一方就可以滚动了、所以就从这下手其实思路也非常简单、就是给table加一个gesture、捕捉提前捕捉事件然后禁掉背的scroll的滚动话不多讲上代码

```

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    scr=[[UIScrollView alloc]initWithFrame:CGRectMake(0, 0, 320, 440)];
    scr.delegate=self;
    [scr setContentSize:CGSizeMake(320, 800)];
    [scr setDelaysContentTouches:YES];//记得这里要把延迟触摸设成yes
    UIView *pand=[[UIView alloc]initWithFrame:CGRectMake(0, 0, 320, 800)];
    [pand setBackgroundColor:[UIColor redColor]];
    tableView=[[UITableView alloc]initWithFrame:CGRectMake(0, 0, 320, 440)];
    tableView.dataSource=self;
    tableView.delegate=self;
    UILongPressGestureRecognizer *ge=[[UILongPressGestureRecognizer alloc]initWithTarget:self action:@selector(cancelScroll:)];
    [ge setDelegate:self];
    [ge setMinimumPressDuration:0.1];//这里为了让他在tableview还是能够进行整个scroll的拖动所以用了0.1给用户一个快速拖动
    [tableView addGestureRecognizer:ge];
    [self.view addSubview:scr];
    [scr addSubview:pand];
    [scr addSubview:tableView];
}

然后是回调

-(BOOL)gestureRecognizer:(UIGestureRecognizer *)gestureRecognizer shouldRecognizeSimultaneouslyWithGestureRecognizer:(UIGestureRecognizer *)otherGestureRecognizer
{
    //切记这个代理必须要设置、因为scroll的拖动说白了也是一个gesture、为了流畅性必须要两个触碰事件同时触发
    return YES;
}
-(void)cancelScroll:(UIGestureRecognizer*)gesture
{
    //这里就是让背景的拖动定死这样就不冲突了
    if ([gesture state]==UIGestureRecognizerStateBegan) {
        [scr setScrollEnabled:NO];
    }

}
-(void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate
{
    //拖动完再恢复
    [scr setScrollEnabled:YES];
}

>

```
