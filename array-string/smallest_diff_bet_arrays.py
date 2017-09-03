def smallest_diff(a,b):
  a.sort()
  b.sort()
  last_j=0
  global_diff=float("inf")
  i,j=0,0
  while i<len(a) and j<len(b):
    diff = abs(a[i]-b[j])
    if diff == 0:
      return 0
    if diff<global_diff:
      global_diff=diff
    if a[i]<b[j]:
      i+=1
    else:
      j+=1
  return global_diff    
      
  
print(smallest_diff([1, 3, 15, 11, 2],[23, 127, 235, 19, 8]))
