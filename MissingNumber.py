def find_missing(a,b):
  '''
  You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77
'''
 
  a,b = set(a),set(b)
  if  (len(a) == len (b) or len(a) == 0 or len(b)==0):
    return 0
  else:
    for num in a:
      if num not in b:
        return num
    for num in b:
      if num not in a:
        return num
      
    