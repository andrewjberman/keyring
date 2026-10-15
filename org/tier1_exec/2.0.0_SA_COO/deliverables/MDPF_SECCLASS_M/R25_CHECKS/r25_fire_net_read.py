"""R25 fire read, NETTED: grade the served objects against REBASE_BASELINE_20261014.json treating the
cash / fixed_income pair as one transfer (the FDRXX -> cash release of IRPT_DASHBD.TO-DB-b-183 first ran on the
2026-10-14 23:00Z fire). Read-only. Run from the workspace root:

    python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_fire_net_read.py

A STRICT date (abs AUA move <= TOL_AUA): the pair's net and every other class within TOL_ROUND of the baseline.
A MOVED date: the sum of all class deltas equals the AUA move within TOL_ROUND (conserved).
The raw instrument stays r25_rebase_read.py; this file imports its served readers and constants.
"""
import importlib.util
import json
from pathlib import Path

D = Path("org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS")
PAIR = ("cash", "fixed_income")


def load_raw():
    spec = importlib.util.spec_from_file_location("r25", D / "r25_rebase_read.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def net(m, live_classes, base_classes):
    """Per-class deltas, the pair's net, and the deltas of every class outside the pair."""
    keys = sorted(set(live_classes) | set(base_classes))
    dl = {k: live_classes.get(k, 0.0) - base_classes.get(k, 0.0) for k in keys}
    pair_net = dl.get("cash", 0.0) + dl.get("fixed_income", 0.0)
    rest = {k: v for k, v in dl.items() if k not in PAIR}
    return dl, pair_net, rest


def grade(m, mv, pair_net, rest):
    if abs(mv) <= m.TOL_AUA:
        return abs(pair_net) <= m.TOL_ROUND and all(abs(v) <= m.TOL_ROUND for v in rest.values())
    return abs(pair_net + sum(rest.values()) - mv) <= m.TOL_ROUND


def other_max(rest):
    return max([abs(v) for v in rest.values()] or [0.0])


def main():
    m = load_raw()
    r24 = m.load_r24()
    mode = r24.resolve_mode(None)
    b = json.loads((D / "baseline/REBASE_BASELINE_20261014.json").read_text(encoding="utf-8"))
    mds, e1, s1 = m.served_json(r24.K_MDS, mode)
    fmv, e2, s2 = m.served_json(r24.K_FMV, mode)
    aua, _e3, s3 = m.served_aua(mode)
    print("NETREAD served mds=%s fmv=%s stable=%s" % (e1["VersionId"], e2["VersionId"], s1 and s2 and s3))
    bad = []
    for d in sorted(b["firm"]):
        mv = aua[d] - b["aua_by_date"][d]
        dl, pair_net, rest = net(m, m.numeric_classes(mds["firm"][d]), m.numeric_classes(b["firm"][d]))
        ok = grade(m, mv, pair_net, rest)
        if not ok:
            bad.append(d)
        print("NET firm %s %s aua_move=%.2f transfer_cash=%.2f pair_residual=%.2f other_max=%.2f ok=%s" % (
            d, "STRICT" if abs(mv) <= m.TOL_AUA else "MOVED", mv, dl.get("cash", 0.0), pair_net,
            other_max(rest), ok))
    for lb in m.bar_labels():
        live = m.read_bar(fmv["views"], lb)
        base = b["bars"][lb]
        dl, pair_net, rest = net(m, live["classes"], base["classes"])
        mv = aua[live["end"]] - b["aua_by_date"][live["end"]]
        ok = grade(m, mv, pair_net, rest) and live["end"] == base["end"]
        if not ok:
            bad.append(lb)
        print("NET bar %s end=%s transfer_cash=%.2f pair_residual=%.2f other_max=%.2f ok=%s" % (
            lb, live["end"], dl.get("cash", 0.0), pair_net, other_max(rest), ok))
    print("NETREAD ok=%s bad=%s" % (not bad, bad))
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
