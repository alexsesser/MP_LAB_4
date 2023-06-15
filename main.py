import time
import numpy as np
import scipy.stats
import random

def lsd(seed= int(time.time()), m=2**32, a=72782623, c=7):
    while(True):
        seed=(((seed * a) + c) % m)
        yield seed

def XORSHIFT(seed= int(time.time())):
    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123
    while (True):
        t = x ^ ((x << 11) & 0xFFFFFFFF)  # 32bit
        x, y, z = y, z, w
        w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
        yield w

a=(lsd())
b=XORSHIFT()
masLsd=[]
masXor=[]
for i in range(10):
    masLsd.append([])
    for z in range(10000):
        masLsd[i].append(next(a))
for i in range(10):
    masXor.append([])
    for z in range(10000):
        masXor[i].append(next(a))

# print(masLsd)
# print(masXor)

# for i in range(10):
#     print(f"Выборка №{i} метоом LSD: среднее {np.mean(masLsd[i])}, стандартное отклонение {np.std(masLsd[i])} коэффициент вариации {np.std(masLsd[i])/np.mean(masLsd[i])}")
#
# for i in range(10):
#     print(f"Выборка №{i} метоом XOR: среднее {np.mean(masXor[i])}, стандартное отклонение {np.std(masXor[i])} коэффициент вариации {np.std(masXor[i])/np.mean(masXor[i])}")
#
# for i in range(10):
#     n = sum(masLsd[i])
#     k = len(masLsd[i])
#     f = [n / k] * k
#     print(f"Выборка №{i} метоом LSD: xi^2 {scipy.stats.chisquare(masLsd[i])[1]}")

# for i in range(10):
#     n = sum(masXor[i])
#     k = len(masXor[i])
#     f = [n / k] * k
#     print(f"Выборка №{i} метоом XOR: xi^2 {scipy.stats.chisquare(masXor[i])[1]}")
#
#
# for i in [1000,10000,100000,1000000]:
#     tic = time.perf_counter()
#     for z in range(i):
#         lsd()
#     toc = time.perf_counter()
#     print(f"Время генирации методом lsd для выборки размера {i}: {toc - tic}")
print(f"Время генирации методом XORSHIFT\tДля выборки размера ")
for i in [1000,10000,100000,1000000]:
    tic = time.perf_counter()
    for z in range(i):
        XORSHIFT()
    toc = time.perf_counter()
    print(f"{i}\t{toc - tic}")
print(f"Время генирации методом randint\tДля выборки размера ")
for i in [1000,10000,100000,1000000]:
    tic = time.perf_counter()
    for z in range(i):
        random.randint(0,1000000)
    toc = time.perf_counter()
    print(f"{i}\t{toc - tic}")
