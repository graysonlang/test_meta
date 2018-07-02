#!/usr/bin/env python

import inspect
import os
import subprocess
import sys

sys.dont_write_bytecode = True

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "shared", "gyp", "pylib"))
import gyp

DIR_ROOT = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
DIR_GYPI = os.path.abspath(os.path.join(DIR_ROOT, "shared", "gypi"))

def generate_projects(gyp_file = None):
    gyp_path = os.path.relpath(gyp_file, os.getcwd())
    print("Generating project files for \"" + gyp_path + "\".")
    gyp.gyp_main([ gyp_file, "--depth=.", "--no-duplicate-basename-check" ])

if __name__ == "__main__":
    subprocess.call(["git", "submodule", "update", "--init", "--recursive"])
    generate_projects("apps/test_png/test_png.gyp")
