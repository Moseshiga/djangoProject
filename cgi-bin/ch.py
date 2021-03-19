#!/usr/bin/env python3
import cgi, time, os, http.cookies
import random, base64, sqlite3

from _wall import Wall
wall = Wall()


wall.register("123", "22")
wall.register("44", "55")
wall.prall()

print(wall.find('1234'))