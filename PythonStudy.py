#encoding:utf-8
import re

file = open('/home/zbw/桌面/homework/太空旅客.txt', 'r')
bigfile=file.read()
# 读取评论的txt文件

dict_keyword = {}
# 字典初始化

def getFile(path): # 定义读取评论关键字的方法
    with open(path,'r') as file:
        for keyword in file.readlines():
            lines = keyword.strip('\n') # 删除换行符
            match = re.findall(lines,bigfile) # 利用正则表达式找到匹配的字符串
            count = match.__len__() # 计算符合的匹配出的字符串的个数
            dict_keyword[lines] = count # 将个数放入字典中

    with open(r'/home/zbw/桌面/homework/result.txt','a') as fileInput: # 新建一个文件放入结果,'a'表示在原结果之后继续输出
        for lines in dict_keyword:
            fileInput.write('(')
            fileInput.write(lines) # 字符串
            fileInput.write(')')
            fileInput.write('出现了')
            fileInput.write(str(dict_keyword[lines])) # 强制转换成String类型
            fileInput.write('次')
            fileInput.write('\n')
        dict_keyword.clear() # 避免重复

getFile('/home/zbw/桌面/homework/角色/反派.txt')
getFile('/home/zbw/桌面/homework/角色/角色.txt')
getFile('/home/zbw/桌面/homework/角色/角色中的其他.txt')
getFile('/home/zbw/桌面/homework/角色/男主角.txt')
getFile('/home/zbw/桌面/homework/角色/女主角.txt')
getFile('/home/zbw/桌面/homework/角色/配角.txt')
getFile('/home/zbw/桌面/homework/剧情/发展.txt')
getFile('/home/zbw/桌面/homework/剧情/结局.txt')
getFile('/home/zbw/桌面/homework/剧情/剧情.txt')
getFile('/home/zbw/桌面/homework/剧情/开头.txt')
getFile('/home/zbw/桌面/homework/剧情/泪点.txt')
getFile('/home/zbw/桌面/homework/剧情/笑点.txt')
getFile('/home/zbw/桌面/homework/剧情/发展.txt')
getFile('/home/zbw/桌面/homework/视听/动作.txt')
getFile('/home/zbw/桌面/homework/视听/画面.txt')
getFile('/home/zbw/桌面/homework/视听/镜头.txt')
getFile('/home/zbw/桌面/homework/视听/视听.txt')
getFile('/home/zbw/桌面/homework/视听/试听效果中的其他')
getFile('/home/zbw/桌面/homework/视听/音乐.txt')
getFile('/home/zbw/桌面/homework/制作/编剧.txt')
getFile('/home/zbw/桌面/homework/制作/出品公司.txt')
getFile('/home/zbw/桌面/homework/制作/导演.txt')
getFile('/home/zbw/桌面/homework/制作/选景.txt')
getFile('/home/zbw/桌面/homework/制作/制作.txt')
getFile('/home/zbw/桌面/homework/主题/风格.txt')
getFile('/home/zbw/桌面/homework/主题/主题.txt')
getFile('/home/zbw/桌面/homework/主题/题材内容.txt')