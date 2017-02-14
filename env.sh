#!/bin/sh

ENV_BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export PYTHONPATH=$PYTHONPATH:$ENV_BASE_DIR

echo $ENV_BASE_DIR
echo $PYTHONPATH

unset ENV_BASE_DIR
