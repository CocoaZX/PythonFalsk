#Flask 在程序文件夹中的 templates 子文件夹中寻找模板。

# import flask
# from flask import Flask,render_template,session,redirect,url_for
from flask import Flask, render_template, session, redirect, url_for, flash

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    session['name'] = form.name
    return render_template('index.html')

