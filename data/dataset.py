import numpy as np
import pandas as pd

FLAGS = [
    'loop_unroll','vectorize','inline_small','licm',
    'strength_reduce','tail_call','const_prop','dead_code_elim'
]

def generate_dataset(n=2500):
    rows = []

    for _ in range(n):
        num_loops = np.random.randint(0, 30)
        loop_depth_avg = np.random.uniform(1, 4)
        num_functions = np.random.randint(1, 100)
        avg_func_size = np.random.randint(5, 200)
        total_instrs = num_functions * avg_func_size
        alu_pct = np.random.uniform(0.2, 0.7)
        mem_pct = np.random.uniform(0.1, 0.5)
        branch_pct = 1 - alu_pct - mem_pct
        num_constants = np.random.randint(0, 50)
        tail_call_sites = np.random.randint(0, 10)
        mul_div_pct = np.random.uniform(0, 0.2)
        dead_code_frac = np.random.uniform(0, 0.15)

        labels = [0]*len(FLAGS)

        if num_loops > 5 and loop_depth_avg < 3: labels[0]=1
        if alu_pct > 0.4 and num_loops > 3 and branch_pct < 0.2: labels[1]=1
        if avg_func_size < 20 and num_functions > 10: labels[2]=1
        if num_loops > 8 and alu_pct > 0.3: labels[3]=1
        if mul_div_pct > 0.1: labels[4]=1
        if tail_call_sites > 2: labels[5]=1
        if num_constants > 20: labels[6]=1
        if dead_code_frac > 0.05: labels[7]=1

        rows.append([
            num_loops, loop_depth_avg, num_functions, avg_func_size,
            total_instrs, alu_pct, mem_pct, branch_pct,
            num_constants, tail_call_sites, mul_div_pct, dead_code_frac
        ] + labels)

    cols = [
        'num_loops','loop_depth_avg','num_functions','avg_func_size',
        'total_instrs','alu_pct','mem_pct','branch_pct',
        'num_constants','tail_call_sites','mul_div_pct','dead_code_frac'
    ]

    return pd.DataFrame(rows, columns=cols + FLAGS)