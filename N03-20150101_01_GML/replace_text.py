#coding:utf-8
'''
Created on 2014/03/27
@author: hitsuji
'''
import csv

# 置換リストをCSVファイルで読み込む
words_filename = 'hokkaido_id'
document_in = 'hokkaido_topo.json'
document_out = 'hokkaido_topo_out.json'
words = []

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line

with open(words_filename + '.csv', 'rU') as csvfile:
    spamreader = unicode_csv_reader(csvfile, dialect=csv.excel)
    for row in spamreader:
        words.append(row)

text = u""
with open(document_in, 'rU') as docfile:
    tmpdoc = docfile.read()
    docfile.close()
    text = tmpdoc.decode('utf-8')

for pair in words:
    text = text.replace(pair[0], pair[1])

with open(document_out, 'w') as f:
    f.write(text.encode('utf-8'))
    f.close() 