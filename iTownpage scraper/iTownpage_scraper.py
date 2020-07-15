
# coding: utf-8

import requests
import json

# \が入っているので、raw文字列として保存
#searchJSON = r'C:\Users\tkuji\Desktop\search.json'
result = r'C:\Users\tkuji\Desktop\result.txt'

# とりあえず見たやつ
#with open(searchJSON, 'r', encoding='utf-8') as f:
#    data = json.load(f)

#print(json.dumps(data, ensure_ascii=False, indent=4))

# パースしたやつをファイルに書いたやつ
#data = open(searchJSON, 'r', encoding='utf-8')
#outfile = open(result, 'w')

#json.dump(json.load(data),outfile,ensure_ascii=False,indent=4)

#outfile.close()

urlBase = 'https://itp.ne.jp/search?size=20&sortby=01&media=pc&kw=病院'
area = '青森県三戸郡階上町'
getPoint = 0

# 最初のリスト取得
url = urlBase + '&from=' + str(getPoint) + '&area=' + area
print('fetching ' + url)
jsonDict = json.loads( requests.get(url).content )

hitsTotal = jsonDict['hits']['total']
print('hit total = ' + str(hitsTotal))
bufferList = []

while True:
    for i in jsonDict['hits']['hits']:
        dataStr = i['_source']['ki']['name'] + ','
        dataStr += i['_source']['ki']['jusyo'] + i['_source']['ki']['jyusyo_banti']

        for j in i['_source']['ki']['sginfo']:
            dataStr += ',' + j

        bufferList.append(dataStr)

    getPoint += 20
    
    if getPoint > hitsTotal:
        break

    url = urlBase + '&from=' + str(getPoint) + '&area=' + area
    print('fetching ' + url)
    jsonDict = jsonDict = json.loads( requests.get(url).content )

print('fetch done. bufferWriting...')
buffer = "\n".join(bufferList)

with open(result, 'w', encoding='utf-8') as outf:
    outf.writelines(buffer)

print('ALL DONE!')

