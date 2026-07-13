#!/usr/bin/env python3
"""G6 validation fixtures -- generator for the 4 synthetic mdpf partition variants (CVO~A, validator).

Co-authored to 0.7.0_AE_CloudOps~A's landed schema (46d8be80d): the checker reads ONLY
  as_of_by_partner{partner->date} / rolled_forward_partners{partner->date} /
  source_vintage.by_feeder.etf_net_assets{TICKER->date} / source_masters[list-or-dict of masters]
from the partition; everything else in a real partition is ignored. Fixtures are SYNTHETIC (no firm
data -- dates + the two public master ids only). Exercise: upload a variant to
s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/<variant>.json and point the REAL checker at it
via AGGREGATE_PARTITION_KEY (the seam). Protocol: CVO_G6_percohort_freshness_alarm_validation_protocol_20260712.md.

Dates are computed RELATIVE TO THE RUN DAY so the variants stay valid whenever the exercise runs:
  fresh   = the expected last trading day (the checker's own semantics)
  stale   = fresh - 3 trading days  (>= threshold 1, unambiguous)
SHARED-PREDICATE CAVEAT (disclosed, NFRA_TOOLPASS sec.6): the trading-day calendar here is imported
FROM THE CHECKER (one home, no fork) -- fine for INPUT GENERATION, but the exercise verdict must
hand-verify the run-day's expected trading date independently (a fixture generated and judged by the
same wrong calendar would false-pass A2). The verdict doc records the hand-check.

Usage:
  python g6_fixture_generator.py --out <dir>        # write the 4 variants locally
  # then upload (exercise-time):  aws s3 cp <dir>/<v>.json s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/<v>.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import sys

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
_CHECKER = os.path.join(_WS, "infra", "aws", "lambda", "mdpf-pipeline", "mdpf-freshness-checker",
                        "lambda_function.py")

ETF_TICKERS = ("DIVZ", "IDVZ", "PFOE", "PFDE")
SMARTX_MASTER = "08242234"
BD_MASTER = "08335338"


def _load_checker():
    """Import the REAL checker module for its trading-day calendar (one home; caveat in docstring)."""
    spec = importlib.util.spec_from_file_location("mdpf_freshness_checker", _CHECKER)
    m = importlib.util.module_from_spec(spec)
    sys.modules["mdpf_freshness_checker"] = m
    spec.loader.exec_module(m)
    return m


def _dates(m):
    now = dt.datetime.now(dt.timezone.utc)
    fresh = m.expected_last_trading_day(now)
    stale = fresh
    for _ in range(3):
        stale = m.prev_trading_day(stale)
    return fresh.isoformat(), stale.isoformat()


def _base(fresh, with_bd_master=True):
    """A fresh-everything partition skeleton in the exact field shapes the checker reads."""
    body = {
        "_g6_fixture": True,   # loud marker: synthetic, never production data
        "as_of_date": fresh,
        "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of_by_partner": {"49financial": fresh, "inflection": fresh},
        "rolled_forward_partners": {},
        "source_vintage": {"by_feeder": {"etf_net_assets": {t: fresh for t in ETF_TICKERS}}},
        "source_masters": [SMARTX_MASTER] + ([BD_MASTER] if with_bd_master else []),
    }
    return body


def variants():
    m = _load_checker()
    fresh, stale = _dates(m)
    v = {}
    # A2 -- fresh-all (incl 08335338 present): every cohort staleness 0, every alarm silent.
    v["fresh-all"] = _base(fresh, with_bd_master=True)
    # A1 -- one-stale: ONE feeder behind (etf DIVZ), everything else fresh -> only etf_divz moves.
    one = _base(fresh, with_bd_master=True)
    one["source_vintage"]["by_feeder"]["etf_net_assets"]["DIVZ"] = stale
    v["one-stale"] = one
    # A3+A4 -- mixed: 49financial rolled-forward on a stale as_of, inflection fresh -> the 49F
    # partner cohorts age on the OLD as_of (A4) while inflection_models stays 0 (A3 discrimination).
    mixed = _base(fresh, with_bd_master=True)
    mixed["as_of_by_partner"]["49financial"] = stale
    mixed["rolled_forward_partners"] = {"49financial": stale}
    v["mixed"] = mixed
    # A5 -- one-missing: inflection absent from as_of_by_partner entirely -> inflection_models =
    # MISSING -> the EXPLICIT 99 emit (never no-datapoint). ALSO drop 08335338 from source_masters
    # -> cohort-8 (49f_schwab_custody) INCOMPLETE 99 (the standing prod expectation until G2 wires
    # the pull -- COO ruling (a)).
    missing = _base(fresh, with_bd_master=False)
    del missing["as_of_by_partner"]["inflection"]
    v["one-missing"] = missing
    return fresh, stale, v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="local output dir for the 4 variant JSONs")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    fresh, stale, v = variants()
    for name, body in v.items():
        p = os.path.join(a.out, name + ".json")
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(body, fh, indent=2)
        print("wrote %-14s fresh=%s stale=%s -> %s" % (name, fresh, stale, p))
    print("\nexercise-time upload (per variant):")
    print("  aws s3 cp <dir>/<v>.json s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/<v>.json")
    print("  then invoke the checker with AGGREGATE_PARTITION_KEY=platinum/mdpf/_g6_fixture/<v>.json")
    print("HAND-CHECK for the verdict: expected trading day computed above = %s -- verify by hand "
          "(NYSE calendar) before trusting A2." % fresh)
    return 0


if __name__ == "__main__":
    sys.exit(main())
