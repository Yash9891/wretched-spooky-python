#map--------------------
# def sqru(num):
#     return num*num

# seq=[1,2,3,4,5]
# lst=list(map(sqru, seq))
# print(lst)


#lambda expression
# mul=list(map(lambda x:x*3, [1,2,3,4,5]))
# print(mul)


#filter: filter out even num---------------------
# evenNum=list(filter(lambda num:num%2==0, [1,2,3,4,5,6]))
# print(evenNum)


#filter out thouse who does not start with s---------
seq=['soup','dog','salad','cat']
fil_seq=list(filter(lambda word:word[0]!="s", seq))
print(fil_seq)