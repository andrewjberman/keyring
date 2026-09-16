"""Analyze saved research responses, never make network calls."""

import ast
import collections
import json
import math
import statistics
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]


def load(name):
    return json.loads((OUT / name).read_text(encoding="utf-8"))


def reference(name):
    return {
        r["security"]: r
        for msg in load(name)["responses"]
        for r in msg.get("securityData", [])
    }


def val(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def pct(values, q):
    values = sorted(values)
    pos = (len(values) - 1) * q
    low = int(pos)
    high = min(low + 1, len(values) - 1)
    return values[low] + (values[high] - values[low]) * (pos - low)


ns = {}
instrument = (
    ROOT
    / "org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/instruments/peers_v_feasibility_grain.py"
)
tree = ast.parse(instrument.read_text())
module = ast.Module(
    body=[
        n
        for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name in ("inv", "measures")
    ],
    type_ignores=[],
)
exec(compile(module, str(instrument), "exec"), ns)
measures = ns["measures"]

result = {
    "vintage": load("pool_1FY.json")["as_of"],
    "populations": {},
    "coverage": {},
    "five_name_scaling": {},
    "peers": {},
}
pool = load("pool_inventory.json")
reqs = load("peer_requests.json")
bf = reference("peers_BF.json")
result["populations"] = {
    "pool": len(pool),
    "peer_nonempty_subjects": len(reqs["subjects"]),
    "peer_unique_requests": len(reqs["members"]),
    "peer_unique_companies": len(
        {bf[s]["fieldData"].get("ID_BB_GLOBAL_COMPANY", s) for s in reqs["members"]}
    ),
    "sectors": dict(
        collections.Counter(
            r["fieldData"].get("GICS_SECTOR_NAME")
            for r in reference("pool_1FY.json").values()
        )
    ),
}
result["empty_peers"] = {
    s: {"class": "NOT_REACHED", "reason": r["document"].get("reason"), "key": r["key"]}
    for s, r in pool.items()
    if not r["document"].get("members")
}
for pop, stem in (("pool", "pool"), ("peer_members", "peer_members")):
    for period in ("1FY", "2FY"):
        rows = reference(f"{stem}_{period}.json")
        cov = {"n": len(rows), "per_security": {}}
        for prefix in ("BEST_CPS", "BEST_EPS"):
            usable = [
                s
                for s, r in rows.items()
                if val(r["fieldData"].get(prefix + "_STDDEV"))
            ]
            ge4 = [
                s
                for s in usable
                if rows[s]["fieldData"].get(prefix + "_NUMEST", 0) >= 4
            ]
            cov[prefix] = {
                "spread_n": len(usable),
                "spread_and_count_ge4_n": len(ge4),
                "eligible": ge4,
            }
        for s, row in rows.items():
            cov["per_security"][s] = {
                "values": row["fieldData"],
                "field_exceptions": row.get("fieldExceptions", []),
                "security_error": row.get("securityError"),
            }
        result["coverage"][f"{pop}_{period}"] = cov
        if pop == "pool":
            for s in (
                "BA US Equity",
                "COST US Equity",
                "HD US Equity",
                "SAP GY Equity",
                "BABA US Equity",
            ):
                r = rows[s]["fieldData"]
                fcf = r.get("BEST_ESTIMATE_FCF")
                record = {
                    "period_end": r.get("BEST_PERIOD_END_DATE"),
                    "fundamental_currency": r.get("EQY_FUND_CRNCY"),
                    "listing_currency": r.get("CRNCY"),
                    "fcf_consensus": fcf,
                }
                for pre in ("CPS", "EPS"):
                    mean, sd = r.get("BEST_" + pre), r.get("BEST_" + pre + "_STDDEV")
                    record[pre] = {
                        "mean": mean,
                        "sd": sd,
                        "count": r.get("BEST_" + pre + "_NUMEST"),
                        "relative_scaled_fcf": abs(fcf) * sd / abs(mean)
                        if val(fcf) and val(sd) and mean
                        else None,
                        "sd_times_reported_shares": sd * r["IS_AVG_NUM_SH_FOR_EPS"]
                        if val(sd) and val(r.get("IS_AVG_NUM_SH_FOR_EPS"))
                        else None,
                    }
                result["five_name_scaling"][s + " " + period] = record

fixes = reqs["candidate_fixes_require_name_validation"]
result["identity_checks"] = {
    s: {
        **expected,
        "returned_name": bf[s]["fieldData"].get("NAME"),
        "company_id": bf[s]["fieldData"].get("ID_BB_GLOBAL_COMPANY"),
        "security_id": bf[s]["fieldData"].get("ID_BB_GLOBAL"),
        "security_error": bf[s].get("securityError"),
    }
    for s, expected in reqs["members"].items()
}
for sub, doc in reqs["subjects"].items():
    ks = [
        fixes.get(
            m["ticker"],
            m["ticker"] if m["ticker"].endswith(" Equity") else m["ticker"] + " Equity",
        )
        for m in doc["members"]
    ]
    sub_id = bf[sub]["fieldData"]["ID_BB_GLOBAL_COMPANY"]
    seen = {sub_id}
    unique = []
    for k in ks:
        identity = bf[k]["fieldData"]["ID_BB_GLOBAL_COMPANY"]
        if identity not in seen:
            unique.append(k)
            seen.add(identity)
    ys = measures(bf[sub]["fieldData"])
    detail = {}
    for m in range(1, 7):
        vv = [measures(bf[k]["fieldData"]).get(m) for k in unique]
        vv = [v for v in vv if val(v)]
        if m not in ys or len(vv) < 6:
            detail[m] = {
                "state": "SUPPRESSED",
                "subject_present": m in ys,
                "peer_n": len(vv),
            }
            continue
        lo, hi = pct(vv, 0.05), pct(vv, 0.95)
        w = [min(max(v, lo), hi) for v in vv]
        med, sd = statistics.median(w), statistics.stdev(w)
        if sd == 0:
            detail[m] = {"state": "SUPPRESSED", "reason": "zero_dispersion"}
            continue
        clamped = min(max(ys[m], lo), hi)
        detail[m] = {
            "raw": ys[m],
            "capped": clamped,
            "lo": lo,
            "hi": hi,
            "median": med,
            "sd": sd,
            "peer_n": len(vv),
            "uncapped_z": (ys[m] - med) / sd,
            "capped_z": (clamped - med) / sd,
        }
    z = [r["capped_z"] for r in detail.values() if "capped_z" in r]
    u = [r["uncapped_z"] for r in detail.values() if "uncapped_z" in r]
    eligible = len(unique) >= 8 and len(z) >= 3
    total_abs = sum(abs(v) for v in z)
    for r in detail.values():
        if "capped_z" in r:
            r["absolute_contribution_share"] = (
                abs(r["capped_z"]) / total_abs if total_abs else None
            )
            r["leave_one_out_V"] = (
                (sum(z) - r["capped_z"]) / (len(z) - 1) if len(z) > 1 else None
            )
    result["peers"][sub] = {
        "K_before_company_dedup": len(ks),
        "K": len(unique),
        "M": len(z),
        "uncapped_V": statistics.mean(u) if eligible else None,
        "capped_V": statistics.mean(z) if eligible else None,
        "measure_details": detail,
        "max_abs_contribution_share": max([abs(v) / total_abs for v in z])
        if total_abs
        else None,
        "qualification": "CTO measure proxies retained to isolate subject-clamp effect; not a contract-correct production V",
    }


def hist(name):
    return {
        x["securityData"]["security"]: x["securityData"]
        for x in load(name)["responses"]
        if "securityData" in x
    }


cons = {
    "x1_flow_inputs": (["EBIT", "IS_INT_EXPENSE"], 11),
    "x2": (["NET_DEBT", "TRAIL_12M_EBITDA"], 8),
    "x3_principal_proxy": (
        [
            "BS_CASH_NEAR_CASH_ITEM",
            "BS_TOTAL_AVAIL_LINE_OF_CREDIT",
            "BS_YEAR_1_PRINCIPAL",
            "BS_YEAR_2_PRINCIPAL",
        ],
        8,
    ),
    "x4": (
        ["BS_YEAR_1_PRINCIPAL", "BS_YEAR_2_PRINCIPAL", "BS_TOTL_DEBT_DEBT_SCHEDULE"],
        8,
    ),
    "x5": (["TRAIL_12M_FREE_CASH_FLOW", "TRAIL_12M_NET_SALES"], 8),
    "x6_top_disclosed_customer_proxy": (["SUPPLY_CHAIN_SUM_TOP_REVENUES"], 8),
}
result["history_window_coverage"] = {
    "not_score_eligibility": True,
    "last_completed_quarter": "2026Q2",
    "constraints": {},
}
quarterly = hist("history_quarterly.json")
for label, (fields, n) in cons.items():
    eligible = []
    for sec, obj in quarterly.items():
        byquarter = {}
        for r in obj.get("fieldData", []):
            y, m = map(int, r["date"].split("-")[:2])
            byquarter[(y, (m - 1) // 3 + 1)] = r
        periods = [
            (ix // 4, ix % 4 + 1) for ix in range(2026 * 4 + 1 - n + 1, 2026 * 4 + 2)
        ]
        if all(all(val(byquarter.get(q, {}).get(f)) for f in fields) for q in periods):
            eligible.append(sec)
    result["history_window_coverage"]["constraints"][label] = {
        "n": len(eligible),
        "securities": eligible,
    }
result["history_window_coverage"]["raw_count_distribution"] = dict(
    collections.Counter(
        sum(
            s in r["securities"]
            for r in result["history_window_coverage"]["constraints"].values()
        )
        for s in pool
    )
)
result["annual_field_coverage_2018_2025"] = {}
annual = hist("history_annual.json")
for f in load("history_annual.json")["fields"]:
    got = []
    for sec, obj in annual.items():
        yy = {int(r["date"][:4]) for r in obj.get("fieldData", []) if val(r.get(f))}
        if set(range(2018, 2026)) <= yy:
            got.append(sec)
    result["annual_field_coverage_2018_2025"][f] = {"n": len(got), "securities": got}

result["supply_chain"] = {
    "top_one_scalar_n": sum(
        val(r["fieldData"].get("SUPPLY_CHAIN_SUM_TOP_REVENUES"))
        for r in reference("supply_chain.json").values()
    ),
    "scope": "top disclosed customer; count override one also limits the bulk; relationship dates and coverage are not full-customer TTM proof",
}
result["broker_detail"] = {}
for sec, obj in reference("broker_detail.json").items():
    result["broker_detail"][sec] = {}
    for field in ("BEST_CPS_BRK_GRID", "BEST_CAPEX_BROKER_GRID"):
        rows = obj["fieldData"].get(field, [])[1:]
        numeric = 0
        for row in rows:
            try:
                float(row.get("Current Value"))
                numeric += 1
            except (TypeError, ValueError):
                pass
        result["broker_detail"][sec][field] = {
            "broker_rows_excluding_header": len(rows),
            "numeric_current": numeric,
            "current_perm_denied": sum(
                row.get("Current Value") == "PERM DENIED" for row in rows
            ),
        }

result["corrected_fundamental_history"] = {}
for fp, fname in (("Q", "history_fund_Q.json"), ("Y", "history_fund_Y.json")):
    bysec = hist(fname)
    output = {}
    for label, (fields, n) in cons.items():
        eligible = []
        for sec, obj in bysec.items():
            if fp == "Q":
                byperiod = {
                    (int(r["date"][:4]), (int(r["date"][5:7]) - 1) // 3 + 1): r
                    for r in obj.get("fieldData", [])
                }
                periods = [
                    (ix // 4, ix % 4 + 1)
                    for ix in range(2026 * 4 + 2 - n, 2026 * 4 + 2)
                ]
            else:
                byperiod = {int(r["date"][:4]): r for r in obj.get("fieldData", [])}
                periods = list(range(2018, 2026))
            if all(
                all(val(byperiod.get(q, {}).get(f)) for f in fields) for q in periods
            ):
                eligible.append(sec)
        output[label] = {"n": len(eligible), "securities": eligible}
    counts = {
        sec: sum(sec in row["securities"] for row in output.values()) for sec in pool
    }
    result["corrected_fundamental_history"][fp] = {
        "input_windows_only_not_S": True,
        "constraints": output,
        "count_distribution": dict(collections.Counter(counts.values())),
        "ge5_count": sum(x >= 5 for x in counts.values()),
        "ge4_count": sum(x >= 4 for x in counts.values()),
        "ge3_count": sum(x >= 3 for x in counts.values()),
    }

mgmt = reference("management_and_obligations.json")
result["management_bulk"] = {
    "population": len(mgmt),
    "officer_lists": sum(
        bool(r["fieldData"].get("COMPANY_EXEC_OFFICERS")) for r in mgmt.values()
    ),
    "columns": sorted(
        {
            k
            for row in mgmt.values()
            for officer in row["fieldData"].get("COMPANY_EXEC_OFFICERS", [])
            for k in officer
        }
    ),
    "cfo_start_count": sum(
        bool(r["fieldData"].get("LAST_CFO_START_DATE")) for r in mgmt.values()
    ),
    "coo_start_count": sum(
        bool(r["fieldData"].get("LAST_COO_START_DATE")) for r in mgmt.values()
    ),
}

result["matched_broker_reconstruction"] = {}
for sec, obj in reference("broker_detail.json").items():

    def numeric_rows(field):
        output = {}
        for row in obj["fieldData"].get(field, [])[1:]:
            try:
                value = float(row.get("Current Value"))
            except (TypeError, ValueError):
                continue
            output[row["Broker"]] = {"value": value, "date": row["Date"]}
        return output

    cps = numeric_rows("BEST_CPS_BRK_GRID")
    capex = numeric_rows("BEST_CAPEX_BROKER_GRID")
    common = sorted(set(cps) & set(capex))
    current = reference("pool_1FY.json")[sec]["fieldData"]
    shares = current.get("IS_AVG_NUM_SH_FOR_EPS")
    paired = (
        [
            {
                "broker": b,
                "cps": cps[b],
                "capex": capex[b],
                "reconstructed_fcf": cps[b]["value"] * shares + capex[b]["value"],
            }
            for b in common
        ]
        if val(shares)
        else []
    )
    values = [r["reconstructed_fcf"] for r in paired]
    result["matched_broker_reconstruction"][sec] = {
        "matched_numeric_count": len(paired),
        "reported_share_count": shares,
        "sample_sd": statistics.stdev(values) if len(values) > 1 else None,
        "pairs": paired,
        "qualification": "hypothesis using reported average shares; forecast shares, freshness and contributor eligibility not validated",
    }

(OUT / "analysis.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(
    json.dumps(
        {
            "populations": result["populations"],
            "coverage": {
                k: {
                    m: {f: n for f, n in v[m].items() if f != "eligible"}
                    for m in ("BEST_CPS", "BEST_EPS")
                }
                for k, v in result["coverage"].items()
            },
            "peers": {
                s: {k: v for k, v in r.items() if k != "measure_details"}
                for s, r in result["peers"].items()
            },
            "history": result["history_window_coverage"],
            "annual": result["annual_field_coverage_2018_2025"],
            "supply_chain": result["supply_chain"],
            "broker_detail": result["broker_detail"],
            "corrected_history": result["corrected_fundamental_history"],
            "management_bulk": result["management_bulk"],
            "broker_reconstruction": {
                s: {k: v for k, v in r.items() if k != "pairs"}
                for s, r in result["matched_broker_reconstruction"].items()
            },
        },
        indent=2,
    )
)
