#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def normalize(s):
    a=''
    for i in range(0,len(s)):
        if i ==0: a+=s[i].upper()
        else: a+=s[i].lower()
    return a
