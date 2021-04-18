#!/bin/bash

cd ~/boca/algochallenger

docker stack deploy -c docker-compose-swarm.yml boca-new
