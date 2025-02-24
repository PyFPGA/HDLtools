#!/bin/bash

set -e

DOCKER="docker run --rm -v $PWD:$PWD -w $PWD --user $(id -u):$(id -g)"
IMAGE="ghcr.io/pyfpga/langutils"

$DOCKER $IMAGE surelog -parse -nonote -noinfo -nowarning -sv modules.sv && rm -fr slpp_all
$DOCKER $IMAGE verible-verilog-lint --rules=-module-filename,-explicit-parameter-storage-type modules.sv
