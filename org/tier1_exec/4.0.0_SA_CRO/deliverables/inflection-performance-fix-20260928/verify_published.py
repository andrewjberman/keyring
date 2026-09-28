"""Verify downloaded post-deploy objects against the pinned upstream total returns.

Arguments: original audit snapshot directory, fix snapshot directory, output JSON.
Loads only trusted internally generated PKLs captured for this investigation.
"""
import gzip
import hashlib
import json
import math
import pickle
import sys
from pathlib import Path

import pandas as pd

from test_period_contract import expected


def read_json(path):
    raw = path.read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw)


def diff(before, after, path=""):
    if type(before) is not type(after):
        return [dict(path=path, before=before, after=after)]
    if isinstance(before, dict):
        rows = []
        for key in sorted(set(before) | set(after)):
            rows.extend(diff(before.get(key), after.get(key), path + "/" + key))
        return rows
    if isinstance(before, list):
        if len(before) != len(after):
            return [dict(path=path, before_length=len(before), after_length=len(after))]
        rows = []
        for i, (b, a) in enumerate(zip(before, after)):
            rows.extend(diff(b, a, path + "/" + str(i)))
        return rows
    return [] if before == after else [dict(path=path, before=before, after=after)]


def main():
    audit_root, fix_root, output = map(Path, sys.argv[1:])
    model_path = audit_root / "model_20260925_v1.pkl"
    data_path = audit_root / "data_20260925_v1.pkl"
    model = pickle.loads(model_path.read_bytes())
    data = pickle.loads(data_path.read_bytes())
    etfs = model["etf_returns"]
    report = {"inputs": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in [model_path, data_path]}, "checks": [], "changes": {}, "summary": {}}

    def check(surface, identity, period, published, want):
        report["checks"].append(dict(surface=surface, identity=identity, period=period,
                                     published=published, expected=want, matches=published == want))

    for filename, surface in [("positioning_data.json", "Positioning"),
                              ("opal_aggregate.json", "Opal aggregate")]:
        after = read_json(fix_root / ("after_" + filename))
        before = read_json(fix_root / ("before_" + filename))
        end = pd.Timestamp(after["data_as_of"])
        assert str(end.date()) == "2026-09-25"
        for collection in ["current_holdings", "portfolios"]:
            for code, group in after.get(collection, {}).items():
                for holding in group["holdings"]:
                    ticker = holding["ticker"]
                    series = etfs[etfs.ticker == ticker].set_index("date")["return"].sort_index()
                    for period, value in holding["returns"].items():
                        check(surface, collection + "/" + code + "/" + ticker, period, value,
                              expected(series, end, period, full_window=True))
        report["changes"][surface] = diff(before, after)
        input_changes = [r for r in report["changes"][surface]
                      if "/returns/" not in r["path"] and r["path"] != "/generated_at"]
        report["summary"][surface + " non_return_changes_since_previous_run"] = input_changes
        # AUM is read live by the unchanged producer. Replay the OLD handler with
        # the exact NEW AUM version and intercept its writes: every non-return
        # field must then equal production, proving the delta is input-driven.
        control = read_json(fix_root / ("control_" + filename))
        control_changes = diff(control, after)
        unexpected = [r for r in control_changes
                      if "/returns/" not in r["path"] and r["path"] != "/generated_at"]
        report["summary"][surface + " non_return_mismatches_against_control"] = unexpected

    filename = "etf_returns.json"
    after = read_json(fix_root / ("after_" + filename))
    before = read_json(fix_root / ("before_" + filename))
    end = pd.Timestamp(after["data_as_of"])
    assert str(end.date()) == "2026-09-25"
    for ticker, row in after["etfs"].items():
        series = etfs[etfs.ticker == ticker].set_index("date")["return"].sort_index()
        for period, value in row["returns"].items():
            if period == "Since Inception":
                selected = series.loc[pd.Timestamp(after["inception_date"]):end].dropna()
                want = round(100 * (math.prod(1 + float(r) / 100 for r in selected) - 1), 2)
            else:
                want = expected(series, end, period)
            check("ETF Performance", ticker, period, value, want)
    report["changes"]["ETF Performance"] = diff(before, after)

    benchmark = read_json(fix_root / "after_model_portfolio_benchmarks.json")
    end = pd.Timestamp(benchmark["data_as_of"])
    inception = pd.Timestamp(benchmark["inception_date"])
    frame = data["return_daily"]
    frame = frame[frame.index_name.str.contains("Term") & (frame.date.dt.weekday < 5)]
    pivot = frame.pivot(index="date", columns="index_name", values="return").sort_index()
    pivot = pivot[(pivot.fillna(0) != 0).any(axis=1)]
    names = dict(UST="Ultra Short Term", ST="Short Term", INT="Intermediate Term",
                 LT="Long Term", ULT="Ultra Long Term")
    for row in benchmark["models"]:
        code = row["code"]
        benchmark_name = names["LT" if code == "ULT" else code]
        fields = {"model": names[code], "index_benchmark": benchmark_name + " Benchmark",
                  "etf_benchmark": benchmark_name + " ETF"}
        for period, values in row["returns"].items():
            for field, name in fields.items():
                series = pivot[name].loc[:end]
                if period in {"TTW", "Since Inception"}:
                    selected = (series.tail(10) if period == "TTW" else series.loc[inception:]).dropna()
                    want = round(100 * (math.prod(1 + float(r) / 100 for r in selected) - 1), 2)
                    if period == "Since Inception":
                        want = round(((1 + want / 100) ** (365 / (end - inception).days) - 1) * 100, 2)
                else:
                    want = expected(series, end, period)
                check("Benchmark", code + "/" + field, period, values[field], want)
    report["summary"]["benchmark_bytes_unchanged"] = (
        (fix_root / "before_model_portfolio_benchmarks.json").read_bytes() ==
        (fix_root / "after_model_portfolio_benchmarks.json").read_bytes())
    for surface in ["Positioning", "Opal aggregate", "ETF Performance", "Benchmark"]:
        rows = [r for r in report["checks"] if r["surface"] == surface]
        report["summary"][surface] = dict(tested=len(rows), matched=sum(r["matches"] for r in rows),
                                           changed=len(report["changes"].get(surface, [])))
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf8")
    print(json.dumps(report["summary"], indent=2))
    assert all(r["matches"] for r in report["checks"]), "Published return mismatch"
    assert report["summary"]["benchmark_bytes_unchanged"]
    assert not report["summary"]["Positioning non_return_mismatches_against_control"]
    assert not report["summary"]["Opal aggregate non_return_mismatches_against_control"]


if __name__ == "__main__":
    main()
