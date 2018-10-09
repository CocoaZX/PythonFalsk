# -*-coding:utf-8-*-

# from  mako.template import Template
#
# t = Template("hello world")
#
# print(t.render())

#lookup相当于前缀
from mako.template import Template

t = Template(filename='/Users/zhangxin/Desktop/PythonFalskGit/Python学习/app/header.txt')

# t = Template(filename='/docs/tpl.txt')

print (t.render())



#lookup相当于前缀
from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['/docs'])
t = Template('<%include file="header.txt" /> hello word!', lookup=lookup)


#储存模块文件到/tmp/mako_modules目录下
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['/docs'], module_directory='/tmp/mako_modules')
def serve_template(t_name, **kwargs):
    t = lookup.get_template(t_name)
    print t.render(**kwargs)

# 上面的例子中我们创建了一个 TemplateLookup ，它从/docs目录中查找模板，并把所有的模块文件存储到/tmp/mako_modules目录中。通过将传入的URI附加到每个查找目录来定位模板，如传递/etc/beans/info.txt，将查找文件/docs/etc/beans/info.txt，如果没找到将抛出 TopLevelNotFound 异常。
# 当定位到模板的时候，传给 get_template() 调用的URI也会作为 Template 的 uri 属性。 Template 使用这个URI来得到模块文件的名字，因此上面的例子中对/etc/beans/info.txt会创建模块文件/tmp/mako_modules/etc/beans/info.txt.py。
