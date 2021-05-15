# encoding=utf8

from flask import Flask
from flask import request

from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import dateparser
import requests
import numpy as np


np.set_printoptions(precision=2, suppress=True)

app = Flask(__name__)
api = Api(app)
CORS(app)


class Calc(Resource):
    # methods go here
    @cross_origin()
    def get(self):
        TOKEN = request.headers.get('token')
        
        print(request.headers.get('token'))

        response = requests.get(
                "http://backend/api/problem/1/run",
                headers={"Authorization": "Bearer "+TOKEN}
        )
        response.raise_for_status()
        
        max_date = None
        min_date = None


        process_jail_list = []
        queue_wait_time_list = []
        process_jail_download_list = []
        jail_ex_download_list = []
        media_list = []
        media_list_general = []
        media_list_100v = []
        i=1

        #client = docker.from_env()
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        #client = client.json()
        

        for container in (client.tasks(filters={'name': 'boca-new_boca-jail'})):
                #filters={'name': 'boca-new_boca-jail'}
        #yaml.safe_load(container)    
                if (container["Status"]["State"]) == "running":
                        i=i+1

        print(i)

        

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

                        media_list.append((np.mean(queue_wait_time_list)))
                        media_list_general.append(np.mean(media_list))
                        #media_list_100v.append(np.mean(queue_wait_time_list[-100:]))
                        
                        
                        





        #print("Numero total de amostras "+str(len(process_jail_list)))
        print(i)
        c = max_date - min_date #[-10:]        
        #alow = "2"
        foo = {
            "total":str(len(process_jail_list)),
            "num_jails": str(i),
            "time_process":str(c),
            "list_twq": str(queue_wait_time_list),
            "list_tpd": str(process_jail_list),
            "list_tpdwd": str(process_jail_download_list),
            "list_td": str(jail_ex_download_list),
            "media_list": str(media_list),
            "media_list_general": str(media_list_general),
            "media_list_100v": str(media_list[-101:]),
            "metrics": [
        {
                "name": "Tempo de processamento sem download",
                "soma":str(np.round(np.sum(process_jail_list),2)),
                "media":str(np.round(np.mean(process_jail_list),2)),
                "standard_desviation": str(np.round(np.std(process_jail_list),2)),
                "min": str(np.round(np.min(process_jail_list),2)),
                "max": str(np.round(np.max(process_jail_list),2)),
                "95%": str(np.round(np.percentile(process_jail_list,95),2)),
                "99%": str(np.round(np.percentile(process_jail_list,99),2))               
            },
            {
                "name": "Tempo de processamento com download",
                "soma":str(np.round(np.sum(process_jail_download_list),2)),
                "media": str(np.round(np.mean(process_jail_download_list),2)),
                "standard_desviation": str(np.round(np.std(process_jail_download_list),2)),
                "min": str(np.round(np.min(process_jail_download_list),2)),
                "max": str(np.round(np.max(process_jail_download_list),2)),
                "95%": str(np.round(np.percentile(process_jail_download_list,95),2)),
                "99%": str(np.round(np.percentile(process_jail_download_list,99),2))

            },
            {
                "name": "Tempo de download de exercícios",
                "soma":str(np.round(np.sum(jail_ex_download_list),2)),
                "media":str(np.round(np.mean(jail_ex_download_list),2)),
                "standard_desviation": str(np.round(np.std(jail_ex_download_list),2)),
                "min": str(np.round(np.min(jail_ex_download_list),2)),
                "max": str(np.round(np.max(jail_ex_download_list),2)),
                "95%": str(np.round(np.percentile(jail_ex_download_list,95),2)),
                "99%": str(np.round(np.percentile(jail_ex_download_list,99),2)),                
            },
            {
                "name": "Tempo de espera na fila",
                "soma":str(np.round(np.sum(queue_wait_time_list),2)),
                "media":str(np.round(np.mean(queue_wait_time_list),2)),
                "standard_desviation": str(np.round(np.std(queue_wait_time_list),2)),
                "min": str(np.round(np.min(queue_wait_time_list),2)),
                "max": str(np.round(np.max(queue_wait_time_list),2)),
                "95%": str(np.round(np.percentile(queue_wait_time_list,95),2)),
                "99%": str(np.round(np.percentile(queue_wait_time_list,99),2)) 
            },
            ]
        }
      
        return foo

api.add_resource(Calc, '/calc')  # '/users' is our entry point


if __name__ == '__main__':
    app.run()  # run our Flask app