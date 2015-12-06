#coding:utf-8
'''
Created on 2014/03/27
@author: Tae Matsumoto
CSVファイルを読み込み、同名のJSONファイルを出力します。
'''

import csv, json

filename = 'hokkaido_codes_16331removed'

header = []
data = []

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield row

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line

with open(filename + '.csv', 'rU') as csvfile:
    spamreader = unicode_csv_reader(csvfile, dialect=csv.excel)
    is_first = True
    
    for row in spamreader:
        if is_first:
            header = row[:]
            is_first = False
            continue
        items = {}
        for i in range(0, len(row)):
            item = row[i]
            items[header[i]] = item
        data.append(items)

with open(filename+'.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2, encoding='utf-8')
    f.close()