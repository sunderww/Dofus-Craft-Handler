# Dofus-Craft-Handler
An API that allows you to handle your craft list for the MMORPG Dofus

### Prerequisites
Dofus-Craft-Handler runs in a [docker](https://www.docker.com) container. You need to have it installed.

The database is filled for demo purposes only. If you want to use this project, please fill the database with your own data.

## Build
    docker build -t sunderww/dofuscrafthandler-api .
    
## Run
    docker run -d --name dofuscrafthandler_api sunderww/dofuscrafthandler-api
    
You'll be able to access the api at localhost:5005/v1
