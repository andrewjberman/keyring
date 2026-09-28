"""Audit published return periods independently of the production functions.

Usage: python audit_periods.py <snapshot-directory> <output-json>
To-date windows INCLUDE the first day's close-to-close return. Trailing windows
exclude their opening boundary. Only trusted local audit PKLs are loaded.
"""
import gzip
import json
import pickle
import sys
from pathlib import Path

import pandas as pd

root, output = map(Path, sys.argv[1:])
audit = {"benchmark_checks": [], "positioning_checks": [], "summary": []}
names = dict(UST="Ultra Short Term", ST="Short Term", INT="Intermediate Term",
             LT="Long Term", ULT="Ultra Long Term")


def compound(values):
    values = values.dropna()
    return round(float(((1 + values / 100).prod() - 1) * 100), 2) if len(values) else None


def window(series, end, period, quarter_days=91, inception=None):
    series = series[series.index <= end]
    if period == "1D":
        return series.tail(1)
    if period == "TTW":
        return series.tail(10)
    if period in {"1M", "1Q", "1Y"}:
        days = {"1M": 30, "1Q": quarter_days, "1Y": 365}[period]
        return series[series.index > end - pd.Timedelta(days=days)]
    starts = {"WTD": end - pd.Timedelta(days=end.weekday()),
              "MTD": end.replace(day=1),
              "QTD": end.replace(month=(end.month - 1) // 3 * 3 + 1, day=1),
              "YTD": end.replace(month=1, day=1), "Since Inception": inception}
    return series[series.index >= starts[period]]


for day, bf, pf in [("20260921", "benchmark_seen_sept22.json", "positioning_seen_sept22.json"),
                    ("20260925", "model_portfolio_benchmarks.json", "positioning_data.json")]:
    data = pickle.loads((root / f"data_{day}_v1.pkl").read_bytes())
    model = pickle.loads((root / f"model_{day}_v1.pkl").read_bytes())
    benchmark = json.loads((root / bf).read_bytes())
    positioning = json.loads(gzip.decompress((root / pf).read_bytes()))
    end = pd.Timestamp(benchmark["data_as_of"])
    inception = pd.Timestamp(benchmark["inception_date"])
    frame = data["return_daily"]
    frame = frame[frame.index_name.str.contains("Term") & (frame.date.dt.weekday < 5)]
    pivot = frame.pivot(index="date", columns="index_name", values="return").sort_index()
    pivot = pivot[(pivot.fillna(0) != 0).any(axis=1)]
    for row in benchmark["models"]:
        code = row["code"]
        benchmark_name = names["LT" if code == "ULT" else code]
        fields = {"model": names[code], "index_benchmark": benchmark_name + " Benchmark",
                  "etf_benchmark": benchmark_name + " ETF"}
        for period, values in row["returns"].items():
            for field, name in fields.items():
                selected = window(pivot[name], end, period, inception=inception)
                expected = compound(selected)
                if period == "Since Inception" and expected is not None:
                    # This explicitly reproduces the producer's rounding before annualization.
                    expected = round(((1 + expected / 100) ** (365 / (end-inception).days) - 1) * 100, 2)
                audit["benchmark_checks"].append({
                    "as_of": str(end.date()), "model": code, "field": field, "period": period,
                    "source_series": name, "published": values[field], "expected": expected,
                    "matches": values[field] == expected, "observations": len(selected),
                    "missing_returns": int(selected.isna().sum())})
    etfs = model["etf_returns"]
    for code, group in positioning["current_holdings"].items():
        for holding in group["holdings"]:
            series = etfs[etfs.ticker == holding["ticker"]].set_index("date")["return"].sort_index()
            for period, published in holding["returns"].items():
                selected = window(series, end, period, quarter_days=90)
                expected = compound(selected)
                if period in {"1M", "1Q", "1Y"}:
                    start = end - pd.Timedelta(days={"1M": 30, "1Q": 90, "1Y": 365}[period])
                    if series.index.min() > start:
                        expected = None
                audit["positioning_checks"].append({
                    "as_of": str(end.date()), "model": code, "ticker": holding["ticker"],
                    "period": period, "published": published, "expected": expected,
                    "matches": published == expected, "observations": len(selected),
                    "missing_returns": int(selected.isna().sum())})
    bc = [r for r in audit["benchmark_checks"] if r["as_of"] == str(end.date())]
    pc = [r for r in audit["positioning_checks"] if r["as_of"] == str(end.date())]
    summary = {"as_of": str(end.date()), "benchmark_tested": len(bc),
               "benchmark_matched": sum(r["matches"] for r in bc),
               "positioning_tested": len(pc), "positioning_matched": sum(r["matches"] for r in pc),
               "positioning_mismatch_by_period": {period: sum(not r["matches"] for r in pc if r["period"] == period)
                                                   for period in ["1D", "WTD", "MTD", "1M", "QTD", "1Q", "YTD", "1Y"]}}
    audit["summary"].append(summary)
output.write_text(json.dumps(audit, indent=2, allow_nan=False) + "\n", encoding="utf8")
print(json.dumps(audit["summary"], indent=2))
