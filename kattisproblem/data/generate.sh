#!/bin/bash
USE_SCORING=0
. ./gen.sh

use_solution solve_crit_analytic.py            # Use ../submissions/accepted/js_100.cpp to generate answer files

compile gen_dag.py
compile gen_long.py

# Generate answers to sample cases
sample 1


tc  random1 gen_dag 1000 10000 100 10 1
tc  random2 gen_dag 1000 10000 100 10 2
tc  random3 gen_dag 1000 10000 100 10 3
tc  random4 gen_dag 100 1000 70 5 4
tc  long1 gen_long 1000 10000 100 5
