#!/usr/bin/python3
import urllib.request
import urllib.error
# 用来解决ssl验证
import ssl

##这个版本的问题是，当下载的网址有问题的时候，会直接报错
'''
报错信息
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1026, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 964, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/socket.py", line 724, in create_connection
    raise err
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/socket.py", line 713, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 61] Connection refused

'''
def first_download(url):
    return urllib.request.urlopen(url).read()

#print(first_download("http://127.0.0.1:8000/places/default/index"))

'''
这个改进的版本是当出现报错的时候，把报错信息捕获
如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类
'''
def second_download(url):
    """Download function that catches errors"""
    print( 'Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as e:
        print('Download httperror:', e.reason)
        html = None
    except urllib.error.URLError as e:
        print('Download urlerror:', e.reason)
        html = None
    return html
#print(second_download("http://127.0.0.1:8000/places/default/index2"))

'''
下载重试版本
'''
def three_download(url,num_retries=2):
    print('Downloading:',url)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as e:
        '''
        当网页找不到时，就不重试了，即4**的时候不重试
        '''
        print('Download httperror:',e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = three_download(url, num_retries - 1)
    except urllib.error.URLError as e:
        print('Download urlerror:', e.reason)
        html = None
    return html
'''
http://httpstat.us/500  可以返回500错误
'''
#print(three_download("http://httpstat.us/500"))


'''
下载重试版本
'''
def four_download(url,context,num_retries=2):
    print('Downloading:',url)
    try:
        if(context):
            html = urllib.request.urlopen(url,context=context).read()
        else:
            html = urllib.request.urlopen(url).read()

    except urllib.error.HTTPError as e:
        '''
        当网页找不到时，就不重试了，即4**的时候不重试
        '''
        print('Download httperror:',e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = three_download(url, num_retries - 1)
    except urllib.error.URLError as e:
        print('Download urlerror:', e.reason)
        html = None
    return html

'''
http://www.meetup.com
python3 CERTIFICATE_VERIFY_FAILED错误 certificate verify failed
下面是两种解决问题的方案
'''
# 全局取消证书验证，引入如下：
ssl._create_default_https_context = ssl._create_unverified_context
#print(four_download("http://www.meetup.com",""))

#生成证书上下文(unverified 就是不验证https证书)
#print(four_download("https://www.meetup.com",ssl._create_unverified_context()))


'''
添加headers的版本
'''
def five_download(url,context,user_agent='awg',num_retries=2):
    print('Downloading:',url)
    try:
        headers={'User-agent':user_agent}
        req = urllib.request.Request(url=url,headers=headers)
        if(context):
            html = urllib.request.urlopen(req,context=context,).read()
        else:
            html = urllib.request.urlopen(req).read()

    except urllib.error.HTTPError as e:
        '''
        当网页找不到时，就不重试了，即4**的时候不重试
        '''
        print('Download httperror:',e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = three_download(url, num_retries - 1)
    except urllib.error.URLError as e:
        print('Download urlerror:', e.reason)
        html = None
    # python3 已经严格区分byte和str了。所以这里需要把byte转成str
    return html.decode(encoding='utf-8');

#print(five_download("https://www.meetup.com",ssl._create_unverified_context()))