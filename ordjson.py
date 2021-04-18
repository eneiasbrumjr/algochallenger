#!/bin/env python
#coding: utf8

import sys
#import os
import json
#import operator

import dateparser
import numpy as np
from collections import OrderedDict

max_date = None
min_date = None



json_name = raw_input("")

data = json.load(open(json_name), object_pairs_hook=OrderedDict)

data = sorted(data, key=lambda k: k['id'], reverse=False)

process_jail_list = []
queue_wait_time_list = []
process_jail_download_list = []
jail_ex_download_list = []

for r in data:
        if r.get("jail_finished_at"):

                ########################################### Tempo de espera na fila ######################################################

                jail_started_at = dateparser.parse(r["jail_started_at"])
                created_at = dateparser.parse(r["created_at"])
                queue_wait_time = jail_started_at - created_at

                ##########################################################################################################################          
                ##################### Tempo de processamento do exercício no jail com download  ##########################################

                jail_finished_at = dateparser.parse(r["jail_finished_at"])
                process_jail_download = jail_finished_at - jail_started_at

                ##########################################################################################################################          
                #################################### Tempo de download do exercício no jail  #############################################

                jail_work_started_at = dateparser.parse(r["jail_work_started_at"])
                jail_ex_download = jail_work_started_at - jail_started_at

                ##########################################################################################################################          
                ################################# Tempo de processamento do exercicio no jail  ###########################################

                if min_date is None or min_date > jail_work_started_at:
                        min_date = jail_work_started_at
                if max_date is None or max_date < jail_finished_at:
                        max_date = jail_finished_at


                process_jail = jail_finished_at - jail_work_started_at #Tempo gasto no processamento do run no jail
                ##########################################################################################################################          

                process_jail_download_list.append(process_jail_download.seconds) #tempo de processamento do jail com download
                jail_ex_download_list.append(jail_ex_download.seconds) #tempo de download do exercicio no jail

                #millis = queue_wait_time.days * 24 * 60 * 60 * 1000
                #millis += queue_wait_time.seconds * 1000
                #millis += queue_wait_time.microseconds / 1000

                #queue_wait_time_list.append(millis) #Lista de tempos de espera na fila
                queue_wait_time_list.append(queue_wait_time.seconds) #Lista de tempos de espera na fila

                #millis = c.days * 24 * 60 * 60 * 1000
                #millis += c.seconds * 1000
                #millis += c.microseconds / 1000

                #diffs_in_milliseconds.append(millis)
                process_jail_list.append(process_jail.seconds)


print("Numero total de amostras "+str(len(process_jail_list)))

c = max_date - min_date

#final_value = c.days * 24 * 60 * 60 * 1000
#final_value += c.seconds * 1000
#final_value += c.microseconds / 1000

print("\nTempo total de processamento: "+str(c)+"\n")

print("############## TEMPOS DE PROCESSAMENTO DO EXERCICIO NO JAIL  ####################")
#print(diffs_in_milliseconds)
print("Soma "+ str(np.sum(process_jail_list))+" segundos")
print("Media " + str(np.mean(process_jail_list))+" segundos")
print("Desvio padrão " + str(np.std(process_jail_list))+" segundos")
print("Minimo " + str(np.min(process_jail_list))+" segundos")
print("Maximo " + str(np.max(process_jail_list))+" segundos")

print

print("95% "+ str(np.percentile(process_jail_list,0.95))+" segundos")
print("99% "+ str(np.percentile(process_jail_list,0.99))+" segundos")
print
print("############## TEMPOS DE PROCESSAMENTO DO EXERCICIO NO JAIL COM DOWNLOAD  ################")
#print(diffs_in_milliseconds)
print("Soma "+ str(np.sum(process_jail_download_list))+" segundos")
print("Media " + str(np.mean(process_jail_download_list))+" segundos")
print("Desvio padrão " + str(np.std(process_jail_download_list))+" segundos")
print("Minimo " + str(np.min(process_jail_download_list))+" segundos")
print("Maximo " + str(np.max(process_jail_download_list))+" segundos")
print
print("95% "+ str(np.percentile(process_jail_download_list,0.95))+" segundos")
print("99% "+ str(np.percentile(process_jail_download_list,0.99))+" segundos")
print
print("################### TEMPOS DE DOWNLOAD DO EXERCICIO NO JAIL #######################")
#print(diffs_in_milliseconds)
print("Soma "+ str(np.sum(jail_ex_download_list))+" segundos")
print("Media " + str(np.mean(jail_ex_download_list))+" segundos")
print("Desvio padrão " + str(np.std(jail_ex_download_list))+" segundos")
print("Minimo " + str(np.min(jail_ex_download_list))+" segundos")
print("Maximo " + str(np.max(jail_ex_download_list))+" segundos")
print
print("95% "+ str(np.percentile(jail_ex_download_list,0.95))+" segundos")
print("99% "+ str(np.percentile(jail_ex_download_list,0.99))+" segundos")
print

print("############################ TEMPOS DE ESPERA NA FILA ############################")
print("Soma "+ str(np.sum(queue_wait_time_list)))
print("Media " + str(np.mean(queue_wait_time_list))+" segundos")
print("Desvio padrão " + str(np.std(queue_wait_time_list))+" segundos")
print("Minimo " + str(np.min(queue_wait_time_list))+" segundos")
print("Maximo " + str(np.max(queue_wait_time_list))+" segundos")
print
print("95% "+ str(np.percentile(queue_wait_time_list,0.95))+" segundos")
print("99% "+ str(np.percentile(queue_wait_time_list,0.99))+" segundos")
print

print("################### queue_wait_time_list: ######################")
print
print(queue_wait_time_list)
print
print("################################################################")
print("################### jail_ex_download_list: ######################")
print
print(jail_ex_download_list)
print
print("################################################################")

print("################################################################")
print("################### process_jail_download_list: ######################")
print
print(process_jail_download_list)
print
print("################################################################")

print("################################################################")
print("################### process_jail_list: ######################")
print
print(process_jail_list)
print
print("################################################################")

# the histogram of the data
"""
n, bins, patches = plt.hist(process_jail_list, weights=np.ones(len(process_jail_list)) / len(process_jail_list),alpha=0.5)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Processamento dos exercicios sem executar download")
plt.legend()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()


n, bins, patches = plt.hist(process_jail_download_list,weights=np.ones(len(process_jail_download_list)) / len(process_jail_download_list),alpha=0.5)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Processamento dos exercicios com download")
plt.legend()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

n, bins, patches = plt.hist(queue_wait_time_list,weights=np.ones(len(queue_wait_time_list)) / len(queue_wait_time_list))

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Espera dos exercicios na fila")
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

# the histogram of the data
n, bins, patches = plt.hist(jail_ex_download_list, weights=np.ones(len(jail_ex_download_list)) / len(jail_ex_download_list), alpha=0.5)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Downloads do exercicio no jail")
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
"""
#print(json.dumps(data, indent=4))
