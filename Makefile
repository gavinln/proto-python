ifeq ($(OS),Windows_NT)
    SHELL='c:/Program Files/Git/usr/bin/sh.exe'
endif

SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: help tmux
.DEFAULT_GOAL=help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

tmux:  ## start tmux
	tmuxp load tmux.yaml

SRC_DIR=$(SCRIPT_DIR)/example1

protoc_example1:  ## generate Python code for example1
	# ./protobuf/bin/protoc -I $(SRC_DIR) --python_out=$(SRC_DIR) $(SRC_DIR)/addressbook.proto
	./protobuf/bin/protoc -I $(SRC_DIR) --python_out=$(SRC_DIR) $(SRC_DIR)/addressbook.proto

python_example1:  ## run Python code for example1
	python $(SCRIPT_DIR)/example1/proto-python-example1.py
