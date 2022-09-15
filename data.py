def dic_list_gen (los,lis):
  lod = []
  for string in lis:
    dict = {}
    count = -1
    for key in los:
      count +=1
      value = (string[count])
      dict[key] = value
    lod.append(dict)
  return lod

import csv
def read_values(filename):
  retval = []
  with open (filename) as f:
    reader = csv.reader(f)
    next (reader)
    for line in reader:
      retval.append(line)
  return retval

def make_lists (los, lod):
  retval = []
  for dict in lod:
    acc=[]
    for string in los:
      a = dict.get(string)
      acc.append(a)
    retval.append(acc)
  return retval

import csv
def write_values(filename,lol):
  with open (filename,'a') as f:
    writer = csv.writer(f)
    for list in lol:
      writer.writerow(list)

import urllib.request
import json

def json_loader(url):
  response = urllib.request.urlopen(url)
  content_string = response.read().decode()
  content = json.loads(content_string)
  return content

def make_values_numeric (los, dict):
  for string in los:
    a = float(dict[string])
    dict[string] = a
  return dict
  
import csv
def save_data(los,lod,filename):
  lists = make_lists(los,lod)
  with open(filename,'w') as f:
    writer = csv.writer(f)
    writer.writerow(los)
    for list in lists:
      writer.writerow(list)

def load_data(filename):
  with open (filename) as f:
    acc = []
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
      dict = {}
      for head in range(len(header)):
       dict[header[head]] = line[head]
      acc.append(dict)
  return acc

