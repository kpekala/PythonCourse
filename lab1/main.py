# def podzielniki(n):
#     for i in range(1,n):
#         if n%i == 0:
#             yield i
#
# g = podzielniki(120)
# print(g)
#
# print(g.__next__())
# print(g.__next__())
# print(next(g))

# l1 = [i for i in range(1, 120) if 120 % i == 0]
# g1= (i for i in range(1, 120) if 120 % i == 0)
#
# for _ in range(20):
#     print(next(g1))
#


def gen():
     l = [2]
     p = 2
     yield 2
     while True:
         p += 1
         for el in l:
             if p % el == 0:
                 break
         else:
             l.append(p)
             yield p
# g1 = gen()
# for i in range(30):
#     print(next(g1))


def rozklad(n):
    for i in gen():
        while n%i==0:
            yield i
            n=n//i
        if n==1:
            break

# for i in rozklad(123456):
#     print(i)

def gen(n):
    if n==0:
        yield ""
    else:
        for i in gen(n-1):
            yield '0' + i
            yield '1' + i

# def perm(s):
#     if len(s) == 1:
#         yield s
#     else:
#         for tail in perm(s[1:]):
#             for i in range(len(s)):
#                 yield tail[:i] + s[0] + tail[i:]
#
# for i in perm("abba"):
#     print(i)


def kombi(s, k):
    if k == 1:
       for i in range(len(s)):
           yield s[i]
    elif len(s) == k:
        yield s
    else:
        for k1 in kombi(s[1:], k-1):
            yield s[0] + k1
        for k1 in kombi(s[1:], k):
            yield k1


for napis in kombi("abcde", 3):
    print(napis)


def war(s, k):
    for kom in kombi(s, k):
        for p in perm(kom):
            yield p













