from data.dataset import FLAGS

def create_features(df):
    feature_cols = [
        'num_loops','loop_depth_avg','num_functions','avg_func_size',
        'total_instrs','alu_pct','mem_pct','branch_pct',
        'num_constants','tail_call_sites','mul_div_pct','dead_code_frac'
    ]

    X = df[feature_cols]
    Y = df[FLAGS]

    return X, Y, feature_cols