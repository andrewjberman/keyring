"""Reconcile trusted, read-only Portal S3 snapshots downloaded for this audit.

Usage: python reconcile.py <snapshot-directory> <output-json>
No network access; no source or production data is changed.
"""
import gzip
import hashlib
import json
import pickle
import sys
from pathlib import Path

import pandas as pd


def read_json(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def compound(series):
    return float(((1 + series / 100).prod() - 1) * 100)


root, output = map(Path, sys.argv[1:])
result = {"method": "Compound daily percent returns; compare published rounded YTD cells.",
          "snapshots": [], "sha256": {}}
inputs = []
for day, bench_file, positioning_file in [
    ("20260921", "benchmark_seen_sept22.json", "positioning_seen_sept22.json"),
    ("20260925", "model_portfolio_benchmarks.json", "positioning_data.json"),
]:
    files = [f"data_{day}_v1.pkl", f"model_{day}_v1.pkl", bench_file, positioning_file]
    inputs.extend(files)
    data, model = [pickle.loads((root / name).read_bytes()) for name in files[:2]]
    benchmark, positioning = [read_json(root / name) for name in files[2:]]
    end = pd.Timestamp(benchmark["data_as_of"])
    start = pd.Timestamp(year=end.year, month=1, day=1)

    def ytd(frame):
        dates = pd.to_datetime(frame["date"])
        return frame[(dates >= start) & (dates <= end)].copy()

    daily = ytd(data["return_daily"])
    etf = ytd(model["etf_returns"])
    model_checks = []
    for row in benchmark["models"]:
        values = daily.loc[daily["bbg_ticker"] == f'.{row["code"]} Index', "return"]
        assert len(values), row["code"]
        actual = compound(values)
        published = row["returns"]["YTD"]["model"]
        model_checks.append({"code": row["code"], "calculated_pct": actual,
                             "published_pct": published, "matches_2dp": round(actual, 2) == published})
    holding_checks = []
    for code, portfolio in positioning["current_holdings"].items():
        for holding in portfolio["holdings"]:
            values = etf.loc[etf["ticker"] == holding["ticker"]]
            if values.empty:
                holding_checks.append({"model": code, "ticker": holding["ticker"], "missing": True})
                continue
            actual = compound(values["return"])
            published = holding["returns"]["YTD"]
            holding_checks.append({"model": code, "ticker": holding["ticker"],
                                   "calculated_pct": actual, "published_pct": published,
                                   "price_only_pct": compound(values["price_return"]),
                                   "matches_2dp": round(actual, 2) == published})
    holdings = positioning["current_holdings"]["UST"]["holdings"]
    valid_yield = [h for h in holdings if h["yield"] is not None]
    weighted_yield = sum(h["weight"] * h["yield"] for h in valid_yield) / sum(h["weight"] for h in valid_yield)
    valid_duration = [h for h in holdings if h["duration"] is not None]
    weighted_duration = sum(h["weight"] * h["duration"] for h in valid_duration) / sum(h["weight"] for h in holdings)
    mr = ytd(model["model_returns"])
    mr = mr.loc[mr["model"] == "UST"].set_index("date")
    tickers = [c[:-7] for c in mr.columns if c.endswith("_return") and c[:-7] in mr.columns]
    weighted_total = pd.Series(0.0, index=mr.index)
    weighted_price = pd.Series(0.0, index=mr.index)
    missing_active_prices = 0
    for ticker in tickers:
        weight = mr[ticker].fillna(0)
        weighted_total += weight * mr[ticker + "_return"].fillna(0)
        prices = etf.loc[etf["ticker"] == ticker].set_index("date")["price_return"].reindex(mr.index)
        missing_active_prices += int(((weight != 0) & prices.isna()).sum())
        weighted_price += weight * prices.fillna(0)
    # These are the stored daily weights, not normalized by the "total" column.
    # The price-only result is a diagnostic, not a complete causal attribution.
    ust = next(c for c in model_checks if c["code"] == "UST")
    business_days = len(pd.bdate_range(start, end))
    chars = positioning["portfolios"]["UST"]["characteristics"]
    snapshot = {
        "as_of": str(end.date()), "benchmark_generated_at": benchmark["generated_at"],
        "positioning_generated_at": positioning["generated_at"],
        "benchmark_model_ytd_checks": model_checks,
        "holding_ytd_checks": holding_checks,
        "holding_checks_total": len(holding_checks),
        "holding_checks_matched": sum(h.get("matches_2dp", False) for h in holding_checks),
        "ust_characteristics": chars,
        "ust_weighted_yield_pct": weighted_yield,
        "ust_weighted_duration_years_using_generator_denominator": weighted_duration,
        "ust_missing_yield": [h["ticker"] for h in holdings if h["yield"] is None],
        "ust_missing_duration": [h["ticker"] for h in holdings if h["duration"] is None],
        "ust_missing_duration_weight": sum(h["weight"] for h in holdings if h["duration"] is None),
        "ust_model_returns_weighted_ytd_pct": compound(weighted_total),
        "ust_model_returns_stored_ytd_pct": compound(mr["return"]),
        "ust_model_returns_daily_max_abs_reconstruction_error_pct": float((weighted_total - mr["return"]).abs().max()),
        "ust_same_weights_price_only_diagnostic_pct": compound(weighted_price),
        "ust_diagnostic_missing_active_prices": missing_active_prices,
        "ust_model_returns_minus_benchmark_source_bps": (compound(weighted_total) - ust["calculated_pct"]) * 100,
        "net_toggle_business_days": business_days,
        "net_toggle_ytd_fee_percentage_points": 0.36 * business_days / 252,
        "net_toggle_ust_ytd_pct": round(ust["published_pct"] - 0.36 * business_days / 252, 2),
        "fdrxx_present_in_etf_returns": bool((etf["ticker"] == "FDRXX").any()),
    }
    assert all(c["matches_2dp"] for c in model_checks)
    assert snapshot["holding_checks_matched"] == snapshot["holding_checks_total"]
    assert round(weighted_yield, 2) == chars["yield"]
    assert round(weighted_duration, 2) == chars["duration"]
    assert snapshot["ust_model_returns_daily_max_abs_reconstruction_error_pct"] < 1e-12
    assert missing_active_prices == 0
    result["snapshots"].append(snapshot)
for name in inputs + ["benchmark_live.py", "positioning_live.py", "router_live.mjs",
                      "index-BSJ0dYHG.js", "ModelPortfolios-DKBKUb7w.js", "index-C5iNecJJ.js"]:
    result["sha256"][name] = hashlib.sha256((root / name).read_bytes()).hexdigest()
output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
print(json.dumps({"output": str(output), "snapshots": [
    {k: v for k, v in s.items() if k not in ("holding_ytd_checks", "benchmark_model_ytd_checks")}
    for s in result["snapshots"]]}, indent=2))
