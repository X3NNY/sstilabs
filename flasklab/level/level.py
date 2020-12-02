# -*- coding: utf-8 -*-

"""
@Author   : Xenny
@Email    : xennyxd1@gmail.com
@Time     : 2020/12/2 11:14
@File     : 111
"""

from flask import render_template_string


def level1(code):
    return code


def level2(code):
    def waf(s):
        return "WAF" if "{{" in s else s
    return waf(code)


def level3(code):
    try:
        render_template_string(code)
        return "correct"
    except Exception:
        return "wrong"


def level4(code):
    def waf(s):
        bl = ['[', ']']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level5(code):
    def waf(s):
        bl = ['\'', '"']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level6(code):
    def waf(s):
        bl = ['_']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level7(code):
    def waf(s):
        bl = ['.']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level8(code):
    def waf(s):
        bl = ["class", "arg", "form", "value", "data", "request", "init", "global", "open", "mro", "base", "attr"]
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level9(code):
    def waf(s):
        bl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level10(code):
    def waf(s):
        return "{% set config=None%}{% set self=None%}" + s
    return waf(code)


def level11(code):
    def waf(s):
        bl = ['\'', '"', '+', 'request', '.', '[', ']']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level12(code):
    def waf(s):
        bl = ['_', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\\', '\'', '"', '[', ']']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)


def level13(code):
    def waf(s):
        bl = ['_', '.', '\\', '\'', '"', 'request', '+', 'class', 'init', 'arg', 'config', 'app', 'self', '[', ']']
        for i in bl:
            if i in s:
                return "WAF"
        return s
    return waf(code)
