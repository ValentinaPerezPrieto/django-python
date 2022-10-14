#!/usr/bin/env bash

if [ $VIRTUAL_ENVIRONMENT ]
then 
    deactivate
fi
. venv/Scripts/activate

#para asegurarme de que estoy trabajando en el entorno virtual que necesito, en consola . start.sh 
#me cierra el entorno anterior si estuviera abierto y me abre el que quiero (venv)
