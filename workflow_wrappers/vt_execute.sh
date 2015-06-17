#!/usr/bin/env bash

# Switch to the script directory
cd /opt/cwslab-workflows/workflow_wrappers

# Set up module environment
source /etc/bashrc
module load python vistrails

PYTHONPATH=${PYTHONPATH}:/opt/vistrails
python vt_execute.py "$@"
