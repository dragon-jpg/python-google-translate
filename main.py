import googletrans
from pprint import pprint
import json
import os


#開啓json設定檔
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


while True:
    #定義參數
    translator = googletrans.Translator()

    #翻譯顯示以及處理
    lan = input('請輸入要翻譯的文字:')
    if lan == '/back':
        os.system("cls")
        os.system('python run.py')
    else:
        results = translator.translate(f'{lan}', dest=(jdata['lan']))
        print(results.text)
        print('=======================================')