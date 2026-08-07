"""MDPF_CANPLAT.G2 -- R7 REGRESSION COMPARATOR, all five limbs (CONTRACT @a3106d585 section E row R7).

R7, quoted as the row: "REGRESSION TEST -- all five limbs. PASS iff value-identical per JSON
path . declared canonicalisation . mutation shown to FAIL and LOCALISE . baseline pinned to
VersionIds at a stamped instant . absent!=null!=zero."

- Limb 1: value-identical PER JSON PATH under the DECLARED canonicalisation (README.md,
  confirmed jointly with 0.4.0_DS_ClientPlatform~Z msg 20260807T000529Z). Never byte-over-file.
- Limb 2: no PASS is citable without --mutation-record pointing at an existing record file;
  reports without it are stamped PASS-NOT-CITABLE.
- Limb 3: baseline is fetched by explicit VersionId from a pinned manifest (pin_baseline.py);
  re-pins are new manifests, never edits.
- Limb 4: ABSENT / NULL / ZERO are three distinct states with distinct verdicts
  (selftest-three-state exercises them on the record).
- Limb 5: the exemption set is sectionB_field_paths.json, consumed AS DATA. A diff not excused
  by a named exemption is a REGRESSION. decision_pending / path_pending entries excuse NOTHING.

Role boundary: a REGRESSION here is a report to 2.0.0_SA_COO~Z -- never a fix at this seat.
Run-and-read per verification event. No standing service.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import subprocess
import sys
from decimal import Decimal

HERE = pathlib.Path(__file__).parent
R7_ROW = (
    "REGRESSION TEST -- all five limbs. PASS iff value-identical per JSON path . "
    "declared canonicalisation . mutation shown to FAIL and LOCALISE . baseline pinned "
    "to VersionIds at a stamped instant . absent!=null!=zero."
)

_ABSENT = object()


def _reject_const(name: str):
    raise ValueError("non-JSON constant rejected by declared canonicalisation: " + name)


def parse_canonical(text: str):
    """Declared canonicalisation rules 1+3: strict parse, numbers as Decimal, NaN/Inf rejected."""
    return json.loads(text, parse_float=Decimal, parse_int=Decimal, parse_constant=_reject_const)


def state_of(v) -> str:
    if v is _ABSENT:
        return "ABSENT"
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "BOOL"
    if isinstance(v, Decimal):
        return "ZERO" if v == 0 else "NUMBER"
    if isinstance(v, str):
        return "STRING"
    if isinstance(v, list):
        return "ARRAY"
    if isinstance(v, dict):
        return "OBJECT"
    return "OTHER"


def _esc(key: str) -> str:
    return key.replace(".", "\\.")


def _leaf_equal(a, b) -> bool:
    if isinstance(a, Decimal) and isinstance(b, Decimal):
        return a == b  # mathematical value: 5 == 5.0, 0.1 == 0.10 (rule 3)
    if type(a) is not type(b):
        return False
    return a == b


def _short(v) -> str:
    if v is _ABSENT:
        return "<absent>"
    s = json.dumps(v, default=str)
    return s if len(s) <= 60 else s[:57] + "..."


def walk(base, cand, path: str, diffs: list, denom: list) -> None:
    """Structural walk. Containers with a one-sided change collapse to ONE localised diff."""
    if isinstance(base, dict) and isinstance(cand, dict):
        for k in sorted(set(base) | set(cand)):
            sub = (path + "." if path else "") + _esc(k)
            walk(base.get(k, _ABSENT), cand.get(k, _ABSENT), sub, diffs, denom)
        return
    if isinstance(base, list) and isinstance(cand, list):
        n = max(len(base), len(cand))
        for i in range(n):
            b = base[i] if i < len(base) else _ABSENT
            c = cand[i] if i < len(cand) else _ABSENT
            walk(b, c, "{p}[{i}]".format(p=path, i=i), diffs, denom)
        return
    denom[0] += 1
    sb, sc = state_of(base), state_of(cand)
    if sb in ("OBJECT", "ARRAY") or sc in ("OBJECT", "ARRAY"):
        # container vs leaf/absent/null: one localised diff at this path
        if sb == sc:
            return  # unreachable: same container types recurse above
        diffs.append({"path": path, "from": sb, "to": sc,
                      "baseline": _short(base), "candidate": _short(cand)})
        return
    if sb == sc == "ABSENT":
        return
    if sb == sc and _leaf_equal(base, cand):
        return
    diffs.append({"path": path, "from": sb, "to": sc,
                  "baseline": _short(base), "candidate": _short(cand)})


def _path_covers(ex_path: str, diff_path: str) -> bool:
    return (
        diff_path == ex_path
        or diff_path.startswith(ex_path + ".")
        or diff_path.startswith(ex_path + "[")
    )


def classify(diff: dict, scope: str, exemptions: list) -> dict:
    """Return the diff annotated: excused-by (exemption authority) or REGRESSION."""
    for ex in exemptions:
        if scope not in ex["scopes"]:
            continue
        if not _path_covers(ex["path"], diff["path"]):
            continue
        cls, fr, to = ex["class"], diff["from"], diff["to"]
        if cls in ("absent_to_present", "fold_in_new") and fr == "ABSENT" and to != "ABSENT":
            return dict(diff, verdict="EXCUSED", exemption=ex["path"], cls=cls)
        if cls == "null_to_composite" and fr == "NULL" and to in ("STRING", "OBJECT", "ARRAY", "NUMBER", "BOOL"):
            return dict(diff, verdict="EXCUSED", exemption=ex["path"], cls=cls)
        if cls == "absent_to_null_only" and fr == "ABSENT" and to == "NULL":
            # CONTRACT @6c50710af: the named transition is absent->null (honest absence under one
            # schema); ABSENT -> any VALUE at such a path is NOT excused -- off-contract emission.
            return dict(diff, verdict="EXCUSED", exemption=ex["path"], cls=cls)
        if cls == "null_to_nonzero_value_only" and fr == "NULL" and to == "NUMBER":
            return dict(diff, verdict="EXCUSED", exemption=ex["path"], cls=cls)
        # matched path but wrong transition (e.g. NULL->ZERO under null_to_nonzero_value_only):
        # NOT excused -- fall through so a stricter-matching exemption may still apply.
    return dict(diff, verdict="REGRESSION")


def _git_head_of(relpath: str) -> str:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%h", "--", relpath],
            capture_output=True, text=True, cwd=str(HERE), timeout=30,
        )
        h = out.stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain", "--", relpath],
            capture_output=True, text=True, cwd=str(HERE), timeout=30,
        ).stdout.strip()
        if not h:
            return "UNCOMMITTED"
        return h + ("+DIRTY" if dirty else "")
    except Exception:
        return "UNRESOLVED"


def _vintage(doc) -> dict:
    out = {}
    if isinstance(doc, dict):
        for f in ("as_of_last", "n_dates", "last_updated", "generated_at"):
            if f in doc:
                out[f] = json.dumps(doc[f], default=str)
    return out


def cmd_compare(args) -> int:
    manifest = json.loads(pathlib.Path(args.manifest).read_text(encoding="ascii"))
    sectionb_path = HERE / "sectionB_field_paths.json"
    sectionb = json.loads(sectionb_path.read_text(encoding="ascii"))
    sectionb_commit = _git_head_of("sectionB_field_paths.json")

    mutation_ok = bool(args.mutation_record) and pathlib.Path(args.mutation_record).exists()
    citability = "CITABLE" if mutation_ok else "PASS-NOT-CITABLE (mutation exercise not on record)"

    import boto3  # deferred: selftest needs no AWS

    s3 = boto3.client("s3")
    bucket = manifest["_meta"]["bucket"]

    pairs = []
    for e in manifest["entries"]:
        if e["role"] != "canonical":
            continue
        parts = e["key"].split("/")  # platinum/mdpf/{scope}/{type}.json
        scope, atype = parts[2], parts[3][: -len(".json")]
        if args.scope and scope != args.scope:
            continue
        if args.type and atype != args.type:
            continue
        pairs.append((scope, atype, e))

    report_pairs = []
    total_regressions = 0
    for scope, atype, e in pairs:
        base_text = s3.get_object(Bucket=bucket, Key=e["key"], VersionId=e["version_id"])["Body"].read().decode("utf-8")
        if args.live:
            cand_text = s3.get_object(Bucket=bucket, Key=e["key"])["Body"].read().decode("utf-8")
            cand_src = "live:s3://{b}/{k}".format(b=bucket, k=e["key"])
        else:
            cpath = pathlib.Path(args.candidate_dir) / scope / (atype + ".json")
            if not cpath.exists():
                report_pairs.append({"scope": scope, "type": atype, "verdict": "COULD-NOT-VERIFY",
                                     "reason": "candidate file missing: " + str(cpath)})
                print("COULD-NOT-VERIFY {s}/{t}: candidate missing {p}".format(s=scope, t=atype, p=cpath))
                continue
            cand_text = cpath.read_text(encoding="utf-8")
            cand_src = str(cpath)
        base = parse_canonical(base_text)
        cand = parse_canonical(cand_text)
        diffs, denom = [], [0]
        walk(base, cand, "", diffs, denom)
        exemptions = sectionb["artifact_types"][atype]["exemptions"]
        classified = [classify(d, scope, exemptions) for d in diffs]
        regressions = [d for d in classified if d["verdict"] == "REGRESSION"]
        excused = [d for d in classified if d["verdict"] == "EXCUSED"]
        total_regressions += len(regressions)
        verdict = "TIE" if not diffs else ("REGRESSIONS({n})".format(n=len(regressions)) if regressions else "EXCUSED-ONLY")
        report_pairs.append({
            "scope": scope, "type": atype, "key": e["key"], "baseline_version_id": e["version_id"],
            "candidate_source": cand_src,
            "baseline_vintage": _vintage(base), "candidate_vintage": _vintage(cand),
            "paths_compared": denom[0], "diffs": len(diffs),
            "excused": excused, "regressions": regressions, "verdict": verdict,
        })
        print("{v}: {s}/{t}  paths_compared={n} diffs={d} excused={x} regressions={r}".format(
            v=verdict, s=scope, t=atype, n=denom[0], d=len(diffs), x=len(excused), r=len(regressions)))
        for r in regressions[: args.max_print]:
            print("  REGRESSION {p}: {f} -> {t}  baseline={b} candidate={c}".format(
                p=r["path"], f=r["from"], t=r["to"], b=r["baseline"], c=r["candidate"]))

    now = dt.datetime.now(dt.timezone.utc)
    report = {
        "_meta": {
            "r7_row": R7_ROW,
            "to": "MDPF_CANPLAT.G2 @f123fbf6e",
            "run_by": "3.0.0_SA_CVO~Z",
            "run_instant_utc": now.isoformat(),
            "citability": citability,
            "mutation_record": args.mutation_record or None,
            "sectionB_artifact": "sectionB_field_paths.json",
            "sectionB_derivation_commit": sectionb_commit,
            "canonicalisation": "README.md 'THE DECLARED CANONICALISATION' (joint w/ 0.4.0_DS_ClientPlatform~Z msg 20260807T000529Z)",
            "baseline_manifest": pathlib.Path(args.manifest).name,
            "baseline_pin_instant_utc": manifest["_meta"]["pin_instant_utc"],
        },
        "denominator": {
            "pairs_targeted": len(pairs),
            "pairs_compared": len([p for p in report_pairs if p.get("verdict") != "COULD-NOT-VERIFY"]),
            "could_not_verify": len([p for p in report_pairs if p.get("verdict") == "COULD-NOT-VERIFY"]),
            "total_regressions": total_regressions,
        },
        "pairs": report_pairs,
    }
    runs = HERE / "runs"
    runs.mkdir(exist_ok=True)
    out = runs / "R7_{s}.json".format(s=now.strftime("%Y%m%dT%H%M%SZ"))
    out.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="ascii")
    print("DENOMINATOR: {c} of {t} pairs compared; total regressions={r}; {ci}".format(
        c=report["denominator"]["pairs_compared"], t=len(pairs), r=total_regressions, ci=citability))
    print("REPORT: " + str(out.relative_to(HERE)))
    print("SECTION-B DERIVATION COMMIT: " + sectionb_commit)
    if report["denominator"]["could_not_verify"]:
        # a COULD-NOT-VERIFY pair must never read as a clean exit -- rc 3 keeps it loud
        return 3
    return 0 if total_regressions == 0 else 2


def cmd_three_state(args) -> int:
    """Limb 4 exercised, not asserted: absent / null / zero produce distinct verdicts."""
    fx = HERE / "fixtures" / "three_state"
    base = parse_canonical((fx / "baseline.json").read_text(encoding="ascii"))
    cand = parse_canonical((fx / "candidate.json").read_text(encoding="ascii"))
    diffs, denom = [], [0]
    walk(base, cand, "", diffs, denom)
    expected = {
        "a": ("ZERO", "NULL"),
        "b": ("NULL", "ABSENT"),
        "c": ("NUMBER", "ZERO"),
        "e": ("ABSENT", "NULL"),
    }
    got = {d["path"]: (d["from"], d["to"]) for d in diffs}
    ok = got == expected
    lines = []
    lines.append("THREE-STATE SELFTEST -- paths_compared={n}".format(n=denom[0]))
    for p in sorted(set(expected) | set(got)):
        lines.append("  {p}: expected {e}  got {g}  {v}".format(
            p=p, e=expected.get(p), g=got.get(p), v="OK" if expected.get(p) == got.get(p) else "MISMATCH"))
    verdict = "PASS: three states produce distinct verdicts (and d 2 vs 2.0 produced no diff -- rule 3)" if ok \
        else "FAIL: verdict set does not match expected three-state matrix"
    lines.append(verdict)
    print("\n".join(lines))
    if args.record:
        now = dt.datetime.now(dt.timezone.utc)
        rec = HERE / "records" / "THREE_STATE_{d}.md".format(d=now.strftime("%Y%m%d"))
        rec.parent.mkdir(exist_ok=True)
        rec.write_text(
            "# Three-state fixture record (R7 limb 4) -- exercised, not asserted\n\n"
            "**Run:** {i} by 3.0.0_SA_CVO~Z -- TO MDPF_CANPLAT.G2 @f123fbf6e\n"
            "**Fixtures:** fixtures/three_state/baseline.json vs candidate.json\n\n```\n"
            .format(i=now.isoformat())
            + "\n".join(lines) + "\n```\n\n-- 3.0.0_SA_CVO\n",
            encoding="ascii",
        )
        print("RECORD: " + str(rec.relative_to(HERE)))
    return 0 if ok else 2


def main() -> int:
    ap = argparse.ArgumentParser(description="R7 regression comparator (all five limbs)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("compare")
    c.add_argument("--manifest", required=True)
    src = c.add_mutually_exclusive_group(required=True)
    src.add_argument("--candidate-dir")
    src.add_argument("--live", action="store_true")
    c.add_argument("--scope")
    c.add_argument("--type")
    c.add_argument("--mutation-record")
    c.add_argument("--max-print", type=int, default=20)
    c.set_defaults(fn=cmd_compare)
    t = sub.add_parser("selftest-three-state")
    t.add_argument("--record", action="store_true")
    t.set_defaults(fn=cmd_three_state)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
