#!/bin/bash
USE_SCORING=0
. ./gen.sh

use_solution solve_crit_analytic.py            # Use ../submissions/accepted/js_100.cpp to generate answer files

compile gen_dag.py
compile gen_long.py

# Generate answers to sample cases
sample 1
sample 2


tc  long1 gen_long 1000 10000 100 8
tc  random1 gen_dag 1000 10000 100 10 1
tc  random2 gen_dag 1000 10000 100 10 2
tc  random3 gen_dag 1000 10000 100 10 3
tc  random4 gen_dag 1000 10000 100 10 4
tc  random5 gen_dag 1000 10000 100 10 5
tc  random6 gen_dag 1000 10000 100 10 6
tc  random7 gen_dag 100 10000 10 5 7
