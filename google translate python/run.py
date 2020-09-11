import json
import os


with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)



print('請選擇功能:')
print('====================')
print('1.google翻譯(google)')
print('2.wiki搜尋(wiki)')

while True:
    features = input()

    if features == 'google':
        if jdata['installed'] == 'true':
            os.system("cls")
            os.system('python main.py')
        else:
            print(f"請修改在setting.json中的  installed : unll 把null改成true ")
    elif features == 'wiki':
        if (jdata['installed']) == 'true':
            os.system("cls")
            os.system('python main2.py')
        else:
            print(f"請修改在setting.json中的  installed : unll 把null改成true ")