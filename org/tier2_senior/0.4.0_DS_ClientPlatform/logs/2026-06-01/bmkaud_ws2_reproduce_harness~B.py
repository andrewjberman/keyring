"""BMKAUD WS-2 independent reproduction harness (DS~B, 2026-06-01).
Loads the local data PKL, runs the DOCUMENTED transform (the deployed pure-yang
lambda's own functions) over every model x period, and diffs the result against
the SERVED model_portfolio_benchmarks.json. Any mismatch = a number the served
output does NOT reproduce from the PKL via the documented transform.
Read-only; no S3 writes."""
from __future__ import annotations
import json, pickle, sys
import pandas as pd

LAMBDA_DIR = ("infra/aws/lambda/v2_portal/yang_pipeline/portfolios/"
              "yang-model-portfolio-benchmarks")
sys.path.insert(0, LAMBDA_DIR)
import lambda_function as lf  # noqa: E402

PKL = ".runtmp/bmkaud/data_20260531_v1.pkl"
SERVED = ".runtmp/bmkaud/served_model_portfolio_benchmarks.json"

with open(PKL, "rb") as fh:
    data_pkl = pickle.load(fh)
served = json.load(open(SERVED))

term = lf.get_term_returns(data_pkl)
end_date = term.index.max()
print(f"REPRO end_date={end_date.date()}  served data_as_of={served['data_as_of']}")
print(f"return_daily index_names w/ 'Term': {sorted(term.columns)}")

periods = served["periods"]
served_models = {m["code"]: m["returns"] for m in served["models"]}

# fields in the comprehensive output produced per (model, period)
FIELDS = ["model", "index_benchmark", "etf_benchmark",
          "index_spread", "etf_spread",
          "model_volatility", "index_benchmark_volatility",
          "etf_benchmark_volatility"]

mismatches = []
checked = 0
for code in lf.MODEL_CODES:
    mp = lf.INDEX_NAME_MAP[code]
    ms = term.get(mp["model"])
    ix = term.get(mp["index_benchmark"])
    et = term.get(mp["etf_benchmark"])
    for period in periods:
        mr = lf.calculate_period_returns(ms, end_date, period)
        ir = lf.calculate_period_returns(ix, end_date, period)
        er = lf.calculate_period_returns(et, end_date, period)
        model_ret, index_ret, etf_ret = mr["return"], ir["return"], er["return"]
        repro = {
            "model": model_ret,
            "index_benchmark": index_ret,
            "etf_benchmark": etf_ret,
            "index_spread": (round(model_ret - index_ret, 2)
                             if model_ret is not None and index_ret is not None else None),
            "etf_spread": (round(model_ret - etf_ret, 2)
                           if model_ret is not None and etf_ret is not None else None),
            "model_volatility": mr["volatility"],
            "index_benchmark_volatility": ir["volatility"],
            "etf_benchmark_volatility": er["volatility"],
        }
        srv = served_models.get(code, {}).get(period, {})
        for f in FIELDS:
            checked += 1
            a, b = repro[f], srv.get(f)
            # tolerance: exact (both rounded to 2dp) or both-None
            if a is None and b is None:
                continue
            if a is None or b is None or abs(a - b) > 0.001:
                mismatches.append((code, period, f, b, a))  # served, repro

print(f"\nCHECKED {checked} cells | MISMATCHES {len(mismatches)}")
if mismatches:
    print(f"{'model':4} {'period':16} {'field':28} {'SERVED':>14} {'REPRO(PKL)':>14}")
    for code, period, f, srv_v, rep_v in mismatches:
        print(f"{code:4} {period:16} {f:28} {str(srv_v):>14} {str(rep_v):>14}")
else:
    print("ALL CELLS REPRODUCE EXACTLY from the PKL via the documented transform.")

# Spotlight the Andrew symptom periods regardless of match
print("\n--- SYMPTOM SPOTLIGHT (served values) ---")
for code in lf.MODEL_CODES:
    for period in ["1M", "1Q"]:
        srv = served_models.get(code, {}).get(period, {})
        print(f"{code:4} {period:4} model={srv.get('model')} index={srv.get('index_benchmark')} "
              f"etf={srv.get('etf_benchmark')} idx_spread={srv.get('index_spread')}")
