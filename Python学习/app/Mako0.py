# -*-coding:utf-8-*-

# from  mako.template import Template
#
# t = Template("hello world")
#
# print(t.render())

from mako.template import Template

from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['/docs'])

t = Template('<%include file="header.txt" /> hello word!', lookup=lookup)
# 上面创建的模板中包含文件header.txt。为了查找header.txt，传了一个 TemplateLookup 对象给它。
# 通常，应用会以文本文件形式在文件系统上存储大部分或全部的模板。一个真正的应用会直接从 TemplateLookup 取得它的模板，使用 get_template() 方法，它接受需要的模板的URI作为参数：

from mako.template import Template

from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['/docs'], module_directory='/tmp/mako_modules')


def serve_template(t_name, **kwargs):
    t = lookup.get_template(t_name)

    print
    t.render(**kwargs)