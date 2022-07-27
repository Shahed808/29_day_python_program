'''sort()'''

# a =[1,2,3,4,5,6]
# a.sort()
# print(a)                                  # [1,2,3,4,5,6]
# a.sort(reverse=True)
# print(a)                                  # [6,5,4,3,2,1]
# print(*sorted([58,56,12,36,.2,12,20]))       # 0.2, 12, 12, 20, 36, 56, 58


''' all()'''

# print(all(['str',25,23.6,True,(25+36.5)]))           # True
# print(all(['code',0.23,0.56,230,]))                  # True
# print(all(['','kdmkekf','4845465',23.0]))            # False
# print(all(['   ','None',False,0.52,'0']))            # False
# print(all(['ntr','mtr',None,NoneType]))              # False


''' any()'''

# print(any([True,False,0,1]))                            # True
# print(any([23.6,'',0,1]))                               # True
# print(any(['   ',0,1]))                                 # True
# print(any([False,False,0]))                             # False


''' bool()'''

# print(bool(False))                          # False
# print(bool(True))                           # True
# print(bool(0))                              # False
# print(bool(1))                              # True
# print(bool('str'))                          # True
# print(bool(None))                           # False
# print(bool('0'))                            # True
# print(bool(''))                             # False


''' eval()'''

# print('eval= ',eval('5**5'))                  # 3125
# print('eval= ',eval('5*6-1+6'))               # 35
# a = eval('23*89-6936')
# b = eval('23*89-6936+985/2')
# print(a)                                      # -4889
# print(b)                                      # -4396.5

''' sum() '''
# s = ('sum of s = ',sum([10,20,30,40]))         
# f = ('sum of f = ',sum([10*20*30*40]))
# g = ('sum of g =',sum([895/36.2]))
# print(*s)                                       #  # sum of s =  100
# print(*f)                                       # sum of f =  240000
# print(*g)                                       # sum of g = 24.723756906077345


''' reversed() -list'''

# for n in reversed([10,52,56,3.6,120.2,589]):
#     print(n)

''' reversed()- tuple'''
# for w in reversed((25,78,96,14,782,123,56.3)):
#     print(w,end='')                             # 56.312378214967825


''' enumerate() '''

d = (['code','python','SQL'])
# a = enumerate(d)
# print(type(a))
# print(dict(a))                              # {0: 'code', 1: 'python', 2: 'SQL'}
# print(tuple(a))                             # ((0, 'code'), (1, 'python'), (2, 'SQL'))
# print(list(a))                              # [(0, 'code'), (1, 'python'), (2, 'SQL')]

f = enumerate(d,5)                            # (iterable,start)
# print((dict(f)))                          # {5: 'code', 6: 'python', 7: 'SQL'}
print((list(f)))                                # [(5, 'code'), (6, 'python'), (7, 'SQL')]