#!/usr/bin/env bash

source /etc/bashrc

module load python vistrails

PYTHONPATH=${PYTHONPATH}:/opt/vistrails
./vt_execute.py "$[@]"
