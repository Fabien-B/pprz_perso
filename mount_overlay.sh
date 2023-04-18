#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

mkdir -p $SCRIPT_DIR/workdir
sudo mount -t overlay overlay -o lowerdir=$HOME/paparazzi_base,upperdir=$SCRIPT_DIR/paparazzi_diff,workdir=$SCRIPT_DIR/workdir $PAPARAZZI_SRC

