import wikipedia
import json
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

while True:
    que = input('請輸入你的問題:')
    if que == '/back':
        os.system("cls")
        os.system('python run.py')
    else:
        wikipedia.set_lang(jdata['wiki_lang'])
        print(wikipedia.summary((que), sentences=(jdata['sentence'])))