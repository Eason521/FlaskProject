
# 'capitalize','casefold','center','count','encode','endswith','expandtabs',
# 'find','format','format_map','index', 'isalnum', 'isalpha', 'isascii',\
# 'isdecimal', 'isdigit', 'isidentifier','islower', 'isnumeric', 'isprintable',\
# 'isspace','istitle','isupper', 'join', 'ljust','lower', 'lstrip','maketrans',\
# 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition','rsplit',\
# 'rstrip', 'split', 'splitlines','startswith', 'strip', 'swapcase', \
# 'title', 'translate', 'upper', 'zfill'


def capitalize_demo(): #首字母大写其他小写
    a="abblaHYCDsdj"
    print(a.capitalize())
    print(a)
# capitalize_demo()
def casefold_demo(): #将所有大写字符转换为小写
    a="jdsOYTHjlkA叁肆一"
    print(a.casefold())
# casefold_demo()

def center_demo(): #返回字符串居中且两边用空格填充至指定的字符串长度
    a="jdsOYTHjlkA"
    print(a.center(50))
# center_demo()

def count_demo(): #返回字符在字符串里出现的次数
    a="abcdeabca"
    print(a.count("a",3,9)) #参数分别是待搜索字符，开始位置，结束位置
# count_demo()

def encode_decode_demo():
    a="abcdeabca"
    b=a.encode(encoding="utf-8") #编码
    print(b)
    c=b.decode(encoding="utf-8") #解码
    print(c)
# encode_decode_demo()


def endswith_demo(): #检查字符串是否以指定字符结尾
    a="abcdeabca"
    print(a.endswith("a")) #参数分别是待搜索字符，开始位置，结束位置
# endswith_demo()

def expandtabs_demo(): #将tab转换为空格
    a="ab       cdea bca"
    print(a.split(" "))
    b=a.expandtabs()
    print(b.split(" "))
# expandtabs_demo()
def find_demo():  #指定范围内查找字符串，若存在返回索引，若无返回-1
    a="kahduiqhfbsd"
    print(a.find("a",0,1)) #参数分别是待查找字符，开始位置，结束位置
# find_demo()

def format_demo(): #格式化输出字符串
    name = "小邓"
    msg="吃饭了么？"
    print("Hello,%s,%s"%(name,msg))
    print(name,msg.format())
# format_demo()

def format_map_demo(): #格式化输出字符串
    name="小邓"
    print(name.format_map(name))
# format_map_demo()

def index_demo(): #查找字符串，若有返回索引，若无报错
    a = "abcdefg"
    print(a.index("c"))
    # print(a.index("k"))
    try:
        print(a.index("k"))
    except Exception as e:
        print(e)
# index_demo()

def isalnum_demo():#如果 string 至少有一个字符并且所有字符都是字母或数字或中文则返回 True,否则返回 False
    a = "<,"
    b="我"
    c="lsdj1234"
    print(a.isalnum())
    print(b.isalnum())
    print(c.isalnum())
# isalnum_demo()

def isalpha():#如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
    a = "123jasoijo"
    b = "jasoijo"
    print(a.isalpha())
    print(b.isalpha())
# isalpha()

# def isascii_demo():  #判断是否是ascii码，若是返回True.否则返回False
#     a = "ksjdijnsa"
#     # print(isascii(a))
# isascii_demo()

def isdecimal_demo(): #只包含十进制数字，若是返回True,否则返回False
    a="010101"
    print(a.isdecimal())
# isdecimal_demo()

def isdigit_demo():#判断是否全是数字，若是返回True,否则返回False
    a="2324t"
    print(a.isdigit())
# isdigit_demo()

def isidentifier_demo(): #判断变量名是否合法(不包含内置变量)
    a="def"
    print(a.isidentifier())
# isidentifier_demo()

def islower_demo():  #判断字母是否全是小写
    a="ejwoee"
    print(a.islower())
# islower_demo()

def isnumeric_demo():#判断是否全是数字，若是返回True,否则返回False
    a="23"
    print(a.isnumeric())
# isnumeric_demo()

def isprintable_demo(): #若字符串都是可打印的或为空返回True 否则返回False
    a="jweoif\nwfr" #含有转义符
    b="skj"
    print(a.isprintable())
    print(b.isprintable())
# isprintable_demo()

def isspace_demo(): #判断字符串是否全是空格
    # a="dso lj"
    a=" "
    print(a.isspace())
# isspace_demo()

def istitle_demo(): #判断字符串是否是标题化的
    a="Demo"
    b="demo"
    print(a.istitle())
    print(b.istitle())
# istitle_demo()


def isupper_demo():  #字符串包含至少一个区分大小写的字符，且这些字符全部大写返回True 否则返回False
    a = "32134"
    b = "923uLheiu"
    c = "KKHK"
    print(a.isupper())
    print(b.isupper())
    print(c.isupper())
# isupper_demo()

def join_demo(): #合并字符串
    a="$$"
    seq=["a","","b","c",""]
    print(a.join(seq))  #以a为分隔符合并seq中的元素
# join_demo()

def ljust_demo():  #返回一个原字符串，左对齐，右边用空格填充至指定长度
    a = "abc"
    b= a.ljust(10)
    print(b,len(b))
# ljust_demo()

def lower_demo(): #将所有大写字符转换为小写
    a = "abcABC"
    print(a.lower())
# lower_demo()

def lstrip_demo():  #截取掉首字符左边的空格
    a = "  a    bcd    abbb"
    b=a.lstrip()
    print(b,"a:",len(a),"b:",len(b))
# lstrip_demo()

def maketrans_demo():  #创建字符映射转换表，第一个参数是待转换字符，第二个参数是目标字符 返回的是ASCII码
    a = "abcdefg"       #暂时看不懂
    b = a.maketrans("h","H")
    print(a)
    print(b)
# maketrans_demo()

def partition_demo():  #根据指定参数将字符分割为三部分，若指定字符串不存在则返回的第一个参数为原字符串，其他为空
    a = "abcdef"
    b=a.partition("c")
    c=a.partition("h")
    print(b,c)
# partition_demo()

def replace_demo(): #替换字符串 若num指定(第三个参数)，则替换次数不超过num次
    a="abcdefgcccc"
    b=a.replace("c","H",3)
    print(b)
# replace_demo()

def rfind_demo(): #从右边查找字符,返回索引，若无返回-1
    a = "abcdefg"
    print(a.rfind("d"))
# rfind_demo()

def rindex_demo(): #从右边查找字符,返回索引，若无报错
    a = "abcdefg"
    print(a.rindex("d"))
# rindex_demo()

def rjust_demo(): #返回一个原字符串，右对齐，左边用空格填充至指定长度
    a = "abcdefg"
    print(a.rjust(10))
# rjust_demo()
#
def rpartition_demo(): #根据指定参数从右边搜索分隔符，将字符分割为三部分，若指定字符串不存在则返回的第一个参数为原字符串，其他为空
    a = "abcdefg"
    print(a.rpartition("d"))
rpartition_demo()

# rsplit',\
# 'rstrip',
# 'split',
# 'splitlines','
# startswith', '
# strip',
# 'swapcase', \
# 'title',
# 'translate',
# 'upper',
# 'zfill'

"""
maketrans_demo

"""


#  4    10 11 13  20


