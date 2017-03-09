def find_missing(a,b):
 
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
      
    