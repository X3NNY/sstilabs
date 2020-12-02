# -*- coding: utf-8 -*-

"""
@Author   : Xenny
@Email    : xennyxd1@gmail.com
@Time     : 2020/12/2 10:11
@File     : 111
"""

from flask import Flask, request, render_template, render_template_string
import os
from level import level

'''
level1 -> no waf
level2 -> bl['{{']
level3 -> blind
level4 -> bl['[', ']']
level5 -> bl['\'', '"']
level6 -> bl['_']
level7 -> bl['.']
level8 -> bl["class", "arg", "form", "value", "data", "request", "init", "global", "open", "mro", "base", "attr"]
level9 -> bl['0-9']
level10 -> config


level11 -> bl['\'', '"', '+', 'request', '.', '[', ']']
level12 -> bl['_', '.', '0-9', '\\', '\'', '"', '[', ']']
level13 -> bl['_', '.', '\\', '\'', '"', 'request', '+', 'class', 'init', 'arg', 'config', 'app', 'self', '[', ']']
'''

app = Flask(import_name=__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/level/<int:lev>', methods=['GET', 'POST'])
def level1(lev):
    if request.method == "GET":
        return render_template("level.html", level=lev)
    try:
        code = request.form.get('code')
        level_func = 'level' + str(lev)
        call_obj = getattr(level, level_func)
        res = call_obj(code)
        return render_template_string("Hello %s" % res)
    except Exception:
        return "No this level"


app.run()
