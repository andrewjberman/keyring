"""BMKAUD WS-2 follow-on (DS~B): 1M/1Q window-definition BOTH-WAYS evidence +
end_date edge check. Window is the ONLY variable; aggregation (geometric
compound of daily %) is held constant via the lambda's compound_returns. Evidence
for Andrew's window ruling -- NOT a methodology verdict (CVO/WS-3 own that)."""
from __future__ import annotations
import pickle, sys
import pandas as pd
from datetime import timedelta

LAMBDA_DIR = ("infra/aws/lambda/v2_portal/yang_pipeline/portfolios/"
              "yang-model-portfolio-benchmarks")
sys.path.insert(0, LAMBDA_DIR)
import lambda_function as lf  # noqa: E402

data_pkl = pickle.load(open(".runtmp/bmkaud/data_20260531_v1.pkl", "rb"))
term = lf.get_term_returns(data_pkl)
end_date = term.index.max()

# ---- end_date edge check ----
print("=== END_DATE EDGE CHECK ===")
raw = data_pkl['return_daily'].copy()
raw = raw[raw['index_name'].str.contains('Term', na=False)].copy()
raw['date'] = pd.to_datetime(raw['date'])
wk = raw[raw['date'].dt.weekday < 5].pivot(index='date', columns='index_name', values='return').sort_index()
print(f"weekday-filtered max date (BEFORE all-zero drop): {wk.index.max().date()}")
print(f"term_returns max date (AFTER all-zero drop) = lambda end_date: {end_date.date()} ({end_date.strftime('%A')})")
tail = term.tail(4)
print("last 4 term_returns rows (UST model col) :")
for dt_, v in tail['Ultra Short Term'].items():
    print(f"   {dt_.date()} {dt_.strftime('%a')}: UST_model_daily={v}")
# would a different drop change end_date?
dropped_tail = wk.loc[(wk.fillna(0) != 0).any(axis=1) == False].index
dropped_after = [d for d in dropped_tail if d > end_date]
print(f"all-zero (dropped) rows AFTER end_date: {[d.date() for d in dropped_after] or 'NONE'}  "
      f"(if any -> end_date could be a real later trading day that was all-zero; investigate)")

# ---- 1M / 1Q both-ways ----
def comp(series, lo, hi_inclusive):
    if series is None:
        return None
    pd_ = series[(series.index > lo) & (series.index <= hi_inclusive)] if lo is not None \
        else series[series.index <= hi_inclusive]
    return lf.compound_returns(pd_)

def comp_range(series, start, end):
    if series is None:
        return None
    return lf.compound_returns(series[(series.index >= start) & (series.index <= end)])

month_start = end_date.replace(day=1)
prev_month_end = month_start - timedelta(days=1)
prev_month_start = prev_month_end.replace(day=1)
qmonth = ((end_date.month - 1)//3)*3 + 1
q_start = end_date.replace(month=qmonth, day=1)
prev_q_end = q_start - timedelta(days=1)
prev_q_start = prev_q_end.replace(month=((prev_q_end.month-1)//3)*3+1, day=1)

print(f"\n=== 1M / 1Q WINDOW BOTH-WAYS (end_date={end_date.date()}) ===")
print(f"windows: 1M trailing30d=({(end_date-timedelta(days=30)).date()},{end_date.date()}] | "
      f"MTD=[{month_start.date()},{end_date.date()}] | lastCalMonth=[{prev_month_start.date()},{prev_month_end.date()}]")
print(f"         1Q trailing91d=({(end_date-timedelta(days=91)).date()},{end_date.date()}] | "
      f"QTD=[{q_start.date()},{end_date.date()}] | lastCalQtr=[{prev_q_start.date()},{prev_q_end.date()}]")
hdr = f"{'model':4} {'series':9} {'1M_trail30':>11} {'1M_MTD':>9} {'1M_lastMo':>10} | {'1Q_trail91':>11} {'1Q_QTD':>9} {'1Q_lastQ':>9}"
print(hdr)
for code in lf.MODEL_CODES:
    mp = lf.INDEX_NAME_MAP[code]
    for tag, key in [("model", "model"), ("index", "index_benchmark"), ("etf", "etf_benchmark")]:
        s = term.get(mp[key])
        row = [
            comp(s, end_date - timedelta(days=30), end_date),
            comp_range(s, month_start, end_date),
            comp_range(s, prev_month_start, prev_month_end),
            comp(s, end_date - timedelta(days=91), end_date),
            comp_range(s, q_start, end_date),
            comp_range(s, prev_q_start, prev_q_end),
        ]
        print(f"{code:4} {tag:9} " + " ".join(f"{('' if v is None else v):>11}" if i in (0,) else f"{('' if v is None else v):>9}" for i,v in enumerate(row[:3])) +
              " | " + " ".join(f"{('' if v is None else v):>11}" if i==0 else f"{('' if v is None else v):>9}" for i,v in enumerate(row[3:])))
