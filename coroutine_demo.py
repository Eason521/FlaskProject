"""协程复习、、

并发：同时出发，不一定同时执行。
  	     多进程 multiprocessing
异步并发“执行时间片，在效果上神似并发的效果，
        Threading
        Threading.Thread
        _thread 是threading模块的父类
        Twisted(扭曲)框架，tornado框架的核心框架
并行：同时执行，不强调同时出发
多线程：异步问题
协程：单线程，在单个线程内，自由的在两个不同函数，执行到一部分的时候，	 切换。协程解决了IO等待问题，在python当中协程最原始是由yeild生成器实现
gevent 协程框架。解决多IO问题。

"""

#
# def coroutine():
#     for i in (1,2,10):
#         yield i
#         print("***********************")
#         print(i)
# d=coroutine()
# print(d.__next__())
# print("+++++++++++++++++++++++++++++++++")
# print(d.__next__())
# print("+++++++++++++++++++++++++++++++++")
# print(next(d))


#  send方法
# def coroutine():
#     for i in (1,2,10):
#         key = yield i
#         print("***********************")
#         print(key)
#         print(i)
# d=coroutine()
# print(d.__next__())
# print(d.send(3))
# print(d.send(100))


def getContent():
    while True:
        url = yield "hello world"
        print("+++++++++++++++++++++++++++")
        print("hello,%s"%url)
        print("+++++++++++++++++++++++++++")

def getUrl(g):
    url_list = ["url1", "url2", "url3", "url4", "url5"]
    for url in url_list:
        print("==================")
        g.send(url)
        print("==================")

if __name__ == '__main__':
    g=getContent()
    next(g)
    getUrl(g)





# def getContent():
#     """
#     获取内容的方法
#     """
#     while True:
#         for i in (1,2,3,4,5,6,7,8,9):
#             n = yield i
#             print("get content from url:%s"%i)
#             print(n)
#
#
# def getUrl(g):
#     url_list = ["url1","url2","url3","url4","url5"]
#     for i in url_list:
#          print("+++++++++++++++++++++++++++++++++++++")
#          g.send(i)
#          print("+++++++++++++++++++++++++++++++++++++")
#
# if __name__ == "__main__":
#     g = getContent()
#     next(g)
#     getUrl(g)