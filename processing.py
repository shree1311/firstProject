import csv
#find the largest value associated with
#a key in a list of dictionaries
def max_value (lod,k):
  retval = ''
  for dict in lod:
    for key in dict.keys():
      if key == k:
        a = dict.get(key)
        if a > retval:
          retval = a
  return retval


def init_dictionary (lod,k):
  retVal={}
  for dict in lod:
    for key in dict.keys():
      if key == k:
        v = dict[key]
        retVal[v]=0
  return retVal

def sum_matches(lod, k, v, tgt):
  acc = 0
  for dict in lod:
    for key in dict.keys():
      if key == k:
        c = dict.get(k,None)
        if c == v:
          a = dict.get(tgt,None)
          acc=acc+float(a)
  return acc

def copy_matching (lod, k, v):
  retval=[]
  for dict in lod:
    for key in dict.keys():
      if key == k:
        if dict.get(k) == v:
          retval.append(dict)
  return retval
