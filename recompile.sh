#!/bin/bash

# Set up CLASSPATH for ANTLR
export CLASSPATH=".:/home/miguel/Documents/antlr/antlr-4.13.1-complete.jar:$CLASSPATH"

# Run ANTLR tool to generate Python code from Hello.g4 grammar file
java org.antlr.v4.Tool Hello.g4 -Dlanguage=Python3 -o files

# Change directory to the generated files directory
cd files/

# Run the generated Python code with pygrun to display parse trees
java org.antlr.v4.runtime.gui.TestRig Hello r --tree

# Navigate back to the original directory
cd ..
