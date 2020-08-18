arr = [1,2,3,4,5]
def numThree(arr):
  for i in arr:
    num = str(i/3)
    if num[-1] == '0':
      print(i)
numThree(arr)