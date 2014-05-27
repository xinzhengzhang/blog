---
layout: post
title: 开源库AsyncSocket实现socket通信的基本用法
categories:
- program
tags: []
published: true
comments: true
---
<p><a href="https://snorlax.sinaapp.com/Document_Code/AsyncSocket.h">AsyncSocket.h</a>
<a href="https://snorlax.sinaapp.com/Document_Code/AsyncSocket.m">AsyncSocket.m</a></p>

<p>
```

- (BOOL)connectToHost:(NSString*)hostname onPort:(UInt16)port error:(NSError **)errPtr //connect to the server

- (void)writeData:(NSData *)data withTimeout:(NSTimeInterval)timeout tag:(long)tag //send data

- (void)onSocket:(AsyncSocket *)sock didReadData:(NSData *)data withTag:(long)tag //be called when the data was received

- (void)onSocketDidDisconnect:(AsyncSocket *)sock //be called when the socket disconnect

- (void)onSocketDidSecure:(AsyncSocket *)sock // be called when TLS is unstable


Example client

AsyncSocket *client;
NSSError *err=nil;
NSString *hel=@"hello AsyncSocket!"; 
NSData *data = [hel dataUsingEncoding:NSISOLatin1StringEncoding];
[client connectToHost:@"127.0.0.1" onPort:51423 error:&err];
[client writeData:data withTimeout:-1 tag:0];
- (void)onSocket:(AsyncSocket *)sock didReadData:(NSData *)data withTag:(long)tag{  
    
    NSString* aStr = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];  
    NSLog(@"Hava received datas is :%@",aStr);  
    [aStr release];  
    [client readDataWithTimeout:-1 tag:0];  
} 

Example server

import socket
host=''
port=51423
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

print "server is running on port %d;press ctrl-c to terminate"
while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        print "Got connection from", clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()


>

```
