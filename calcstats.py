# encoding=utf8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

np.set_printoptions(suppress=True)

ar1 = input("Array para T1:\n")
ar2 = input("Array para T2:\n")
ar3 = input("Array para T3:\n")
ar4 = input("Array para T4:\n")
ar5 = input("Array para T5:\n")

ar = []


def calc_array(ar1,ar2,ar3,ar4,ar5):
	ar = [(np.array(ar1)+np.array(ar2)+np.array(ar3)+np.array(ar4)+np.array(ar5))/5.0]
        print("Media do array: \n")
        print(ar)
        print
        ar_min = np.min(ar)
        print("Valor minimo: \n"+str(ar_min))
        print
        ar_max = np.max(ar)
        print("Valor maximo: \n"+str(ar_max))
        print
        ar_mean = np.mean(ar)
        print("Valor medio: \n"+str(ar_mean))
        print
        ar_std = np.std(ar)
        print("Desvio Padrao: \n"+str(ar_std))
        print
        ar_sum = np.sum(ar)
        print("Valor da soma: \n"+str(ar_sum))
        print
        ar95 = np.percentile(ar,0.95)
        print("95 percentil: \n"+str(ar95))
        print
        ar99 = np.percentile(ar,0.99)
        print("99 percentil: \n"+str(ar99))
        print
        

calc_array(ar1,ar2,ar3,ar4,ar5)


