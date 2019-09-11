#!/bin/python3
# Run init phase

import subprocess

#TODO: make ref and src config urls configurable
subprocess.check_output(
  ["coreos-assembler", "init", "--force",
   "--branch", "master", "https://github.com/coreos/fedora-coreos-config"])

#TODO: add buildprep
subprocess.check_output(["coreos-assembler", "fetch"])
