#!python3
#Launches a map in the browser using an address from the # command line or clipboard
#命令行或剪贴板中的地址在浏览器中启动映射

import webbrowser,sys,requests

if len(sys.argv) > 1:
    #从命令行拿url地址
    address = ''.join(sys.argv[1:])
#Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，关键就是要明白这参数是从程序外部输入的，
# 而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数.此处argv[1:]就是输入的所有参数
#因为0为程序文件名

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)

