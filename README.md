# ML-Based Compiler Flag Selector

## Overview

This project builds a machine learning system to automatically select the best compiler optimization flags for a given program. Instead of using fixed optimization levels such as -O2 or -O3, the model predicts which subset of flags will yield better performance.

This is formulated as a multi-label classification problem where each program can benefit from multiple optimization flags.

---

## Problem Statement

Modern compilers apply a fixed set of optimizations (e.g., -O2, -O3) regardless of program characteristics. However:

* Different programs benefit from different optimizations
* Applying all optimizations may degrade performance
* Manual tuning is time-consuming

This project solves the problem by predicting the most beneficial flags based on program features.

---

## Objective

* Predict optimal compiler flags for a program
* Improve performance over fixed optimization levels
* Model optimization as a multi-label classification problem
* Analyze performance using ML metrics

---

## Project Structure

flag-selector/
│
├── data/                  # Dataset generation
├── features/              # Feature processing
├── models/                # ML model training
├── evaluation/            # Model evaluation
├── utils/                 # Metrics and plotting
├── inference/             # Prediction logic
│
├── main.py                # Entry point
├── requirements.txt
└── README.md

---

## Dataset

A synthetic dataset is generated where each row represents a program.

### Features

* num_loops: number of loops
* loop_depth_avg: average loop depth
* num_functions: number of functions
* avg_func_size: average function size
* total_instrs: total instructions
* alu_pct: arithmetic instruction percentage
* mem_pct: memory instruction percentage
* branch_pct: branch instruction percentage
* num_constants: number of constants
* tail_call_sites: number of tail calls
* mul_div_pct: multiplication/division usage
* dead_code_frac: fraction of dead code

### Labels

Each program is assigned multiple flags:

* loop_unroll
* vectorize
* inline_small
* licm
* strength_reduce
* tail_call
* const_prop
* dead_code_elim

---

## Model

A MultiOutputClassifier is used with Random Forest as the base model.

* Handles multi-label classification
* Learns one classifier per flag
* Captures feature interactions

---

## Evaluation Metrics

* Hamming Loss (lower is better)
* F1 Score (micro and macro)
* Jaccard Similarity
* Per-flag accuracy

---

## Results

Typical results:

* High per-flag accuracy (>80%)
* Improved flag selection compared to static optimization
* Better average speedup than fixed optimization levels

---

## Output

Running the project produces:

* Model performance metrics
* Per-flag accuracy
* Speedup comparison
* Plot saved as:
  flag_selector_results.png

---

## How to Run

### 1. Clone repository

git clone https://github.com/jyotipatthak/flag-selector.git
cd flag-selector

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the project

python main.py

---

## Inference Example

Input:
Program features (loops, instruction mix, etc.)

Output:
Recommended flags:
['loop_unroll', 'vectorize', 'licm']

---

## Applications

* Compiler optimization (LLVM, GCC)
* Auto-tuning systems
* Performance engineering
* Code optimization tools

---

## Future Improvements

* Use real benchmark datasets
* Integrate with compiler pipelines
* Add hardware-aware features
* Build API for real-time recommendations

---

## Conclusion

This project demonstrates how machine learning can improve compiler optimization by replacing static optimization levels with adaptive, program-specific decisions.
