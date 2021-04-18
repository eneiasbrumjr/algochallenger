# encoding=utf8

import dateparser
import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xNjUuMjI3LjYwLjE5Mzo4MDAxXC9hcGlcL2xvZ2luIiwiaWF0IjoxNjEyMjczODQ3LCJleHAiOjE2MTIzMzM4NDcsIm5iZiI6MTYxMjI3Mzg0NywianRpIjoib0tNanZRN1dDTXRNSmpxZSIsInN1YiI6MSwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.CodOkZXcmuCKBtKFdt_NFUoTnYhmumJHbMTuciOa8kU"


response = requests.get(
        "http://165.227.60.193:8001/api/problem/1/run",
        headers={"Authorization": "Bearer "+TOKEN}
)
response.raise_for_status()

max_date = None
min_date = None


process_jail_list = []
queue_wait_time_list = []
process_jail_download_list = []
jail_ex_download_list = []

for r in response.json():
         
        if r.get("jail_finished_at"):

        #a = dateparser.parse(r["created_at"]) #colocado no banco -> tempo de chegada do run no banco
        #b = dateparser.parse(r["updated_at"]) #tempo da ultima atualização de qualquer lugar ->não vai ser usado nos calculos
        # d = dataparser.parse(r[""]) # jail started_at -> inicio do processamento no jail (com download do banco)
        
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

                #d = dateparser.parse(r["jail_work_started_at"]) # if r["jail_started_at"] is not 'null' else r["jail_started_at"].pop() # jail started_at -> inicio do processamento no jail (com download do banco)
                if min_date is None or min_date > jail_work_started_at:
                        min_date = jail_work_started_at  
                # d = dateparser.parse(r["jail_work_started_at"]) # jail started_at -> inicio do processamento no jail (com download do banco)
             #   e = dateparser.parse(r["jail_finished_at"]) #tempo final do processamento no jail onde ele terminou de trabalhar
                if max_date is None or max_date < jail_finished_at:
                        max_date = jail_finished_at

                process_jail = jail_finished_at - jail_work_started_at #Tempo gasto no processamento do run no jail
                ##########################################################################################################################          

                # f = true started_at ----> sem download 
                # c = b - a
                #e=d

		#------>>>>> tempo de espera do run na fila do jail c = created_at - jail_started_at                   
                #criar runs com loops infinitos -> aumentar o timelimit                

                #grafico com tempo na fila, grafico do tempo processamento, processamento com download finished_jail - start_jail, download "puro" work_started - started_jail

                #c = b - a #Tempo gasto no processamento do run

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
n, bins, patches = plt.hist(process_jail_list, weights=np.ones(len(process_jail_list)) / len(process_jail_list),alpha=0.5)
#n, bins, patches = plt.hist(queue_wait_time_list, 10, density=True)
#n, bins, patches = plt.hist(process_jail_download_list, 10, alpha=0.5, label='Tempo de processamento com download', density=True)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Processamento dos exercicios sem executar download")
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(0, 13)
#plt.ylim(0, 0.3)
plt.legend()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()


n, bins, patches = plt.hist(process_jail_download_list,weights=np.ones(len(process_jail_download_list)) / len(process_jail_download_list),alpha=0.5)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Processamento dos exercicios com download")
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(0, 13)
#plt.ylim(0, 0.3)
plt.legend()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

# the histogram of the data
#n, bins, patches = plt.hist(queue_wait_time_list, weights=np.ones(len(queue_wait_time_list)) / len(queue_wait_time_list), alpha=0.5, label='Tempo de espera na fila')
#weights=np.ones(len(queue_wait_time_list)) / len(queue_wait_time_list)

#print("---------------------> "+str(len(weights)))
#print(np.ones(len(queue_wait_time_list)))
#print("---------------------> "+str((weights)))
#print("---------------------> "+str((np.ones(len(queue_wait_time_list)) / len(queue_wait_time_list))))
n, bins, patches = plt.hist(queue_wait_time_list,weights=np.ones(len(queue_wait_time_list)) / len(queue_wait_time_list))
#n, bins, patches = plt.hist(queue_wait_time_list, 10, density=True)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Espera dos exercicios na fila")
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(0, np.max(queue_wait_time_list))
#plt.ylim(0, 0.003)
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

# the histogram of the data
#n, bins, patches = plt.hist(jail_ex_download_list, weights=np.ones(len(jail_ex_download_list)) / len(jail_ex_download_list), alpha=0.5, label='Tempo de download do exercicio no jail')
n, bins, patches = plt.hist(jail_ex_download_list, weights=np.ones(len(jail_ex_download_list)) / len(jail_ex_download_list), alpha=0.5)
#n, bins, patches = plt.hist(queue_wait_time_list, 10, density=True)

plt.xlabel("Agrupamento amostral por segundo")
plt.ylabel("Frequencia")
plt.title("Downloads do exercicio no jail")
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(0, 600)
#plt.ylim(0, 0.003)
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
