#!/bin/python3
# Run init phase

import subprocess

subprocess.check_output(["coreos-assembler", "build"])
subprocess.check_output(["coreos-assembler", "kola", "run"])
