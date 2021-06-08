# -*- coding: utf-8 -*-
"""
Time    : 2020-03-06 15:19
Author  : Yaodi
Object  : 
"""
from zhangdama.start import get_geetest_challenge
import json

if __name__ == '__main__':
    with open("user.json") as f:
        userList = json.load(f)
    # print(userList["users"])
    it = iter(userList["users"])
    for i in it:
        # print(i)
        get_geetest_challenge(username=i["username"], password=i["password"])