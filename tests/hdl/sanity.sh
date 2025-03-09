#!/bin/bash

set -e

DOCKER="docker run --rm -v $PWD:$PWD -w $PWD --user $(id -u):$(id -g)"

IMAGE="ghcr.io/pyfpga/langutils"
for file in modules.sv memory1.sv memory2.sv; do
  $DOCKER $IMAGE surelog -parse -nonote -noinfo -nowarning -sv "$file" && rm -fr slpp_all
  $DOCKER $IMAGE verible-verilog-lint --rules=-module-filename,-explicit-parameter-storage-type "$file"
done

IMAGE="ghcr.io/pyfpga/simulation"
for file in memory1.sv memory2.sv; do
  $DOCKER $IMAGE verilator --lint-only "$file"
done
