#!/bin/sh

ENV_BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export PYTHONPATH=$PYTHONPATH:$ENV_BASE_DIR

export PATH=$PATH:$ENV_BASE_DIR"/bin"


echo $ENV_BASE_DIR


unset ENV_BASE_DIR
