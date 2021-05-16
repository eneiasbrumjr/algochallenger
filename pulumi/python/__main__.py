
import pulumi_digitalocean as do
"""
importação de bibliotecas para o funcionamento do código, aqui vale destacar que deve-se importar bibliotecas 
específicas para o funcionamento do Pulumi para DigitalOcean
"""
from pulumi import export, get_stack

region = "nyc3" #Definição da região e zona de disponibilidade que o recurso será alocado na nuvem

user_data = """#!/bin/bash

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" -y
    sudo apt update
    apt-cache policy docker-ce
    sudo apt install docker-ce -y 

    sleep 10

    systemctl start docker 
    systemctl enable docker

    sleep 3

    private_ip=$(hostname -I | awk '{print $3}') 

    docker swarm init --advertise-addr ${private_ip}

    sleep 3

    output_worker_token=$(docker swarm join-token worker)
    worker_token=%{output_worker_token#*:}

    apt-get install -y git 

    sleep 3

    mkdir ~/boca

    cd ~/boca

    git clone https://github.com/eneiasbrumjr/algochallenger.git 

    sleep 3

    cd ~/boca/algochallenger

    mkdir boca-volume 

    cd boca-volume

    mkdir {app,framework,logs} 
    
    cd framework

    mkdir {cache,sessions,views} 

    sleep 3

    cd ~/boca/algochallenger

    export EXTERNAL_IP=$(curl ipinfo.io/ip)

    sleep 3

    docker build -t api-mon ./api

    docker build -t dash-mon ./dashboard

    sleep 3


    docker stack deploy -c docker-compose-swarm.yml boca-new
"""

droplet_type = "algochallenger-app-%s" %get_stack() #extração de tag para associar a instância
droplet_type_tag = do.Tag(droplet_type)


def createDroplet(): #definição de função para criação de instância
    droplet = do.Droplet( #modulo de criação da instância, netes podemos definir os parâmetros da mesma
        instance_name,
        image="ubuntu-18-04-x64",
        region=region,
        size="s-1vcpu-1gb",
        tags=[name_tag.id, droplet_type_tag.id],
        user_data=user_data #atribuição do user_data na instância
    )

    export("ip privado",droplet.ipv4_address_private) #exibi ip privado da instância
    export("ip publico",droplet.ipv4_address) #exibi ip publico da instância
    
    global instance_public_ip
    instance_public_ip=droplet.ipv4_address #armazena ip publico da instância em uma variável global


instance_name = "algochallenger"
name_tag = do.Tag(instance_name)

createDroplet() #chama a função de criação da instância

domain = do.Domain("algochallenger", #criar uma zona de domínio do projeto na DigitalOcean
  name='algochallenger.com',
  ip_address=instance_public_ip #Associa ip publico da instância extraído anteriormente
)

cnameRecord = do.DnsRecord('algochallenger-cname', #cria CNAME e insere no domino da DigitalOcean 
    domain=domain.name,
    type='CNAME',
    name='www',
    value='@',
)

export("domain name", domain.name) #exibi domínio na tela do terminal
