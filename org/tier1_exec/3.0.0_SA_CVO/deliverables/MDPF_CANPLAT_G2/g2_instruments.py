"""MDPF_CANPLAT.G2 -- R1 / R2 / R12 instruments (CONTRACT @a3106d585 section E).

r1  : EXISTENCE of the 12 canonical platinum keys. This is an EXISTENCE verdict and is
      NEVER reported as freshness -- 12 files at 12 known paths is identical whether fresh
      or frozen (PRD section 5.1; TO acceptance criterion 5).
r2  : key-set identity per artifact type across all four scopes. PASS iff set-diff = empty
      for each of the 3 types; any non-empty diff reported with the exact paths.
r12 : both standalone extras still present. Their retirement is Andrew's act, never this
      program's (PRD section 4 sequencing; TO acceptance criterion 7).

READ-ONLY on served surfaces. Denominators printed on every scan.
Key-set extraction convention (r2): dict keys walked recursively; array indices collapse
to []. DATA-KEYED maps are DATA, not schema: their keys collapse to path.<map> and ONE
representative child is descended as path.<*> so the map's VALUE schema is still compared.
A dict is data-keyed iff it is non-empty and EVERY key is data-like (date-shaped, all
digits, len>12, a scope name, or a composite id containing '/'), OR its field name is in
the explicit list (by_model, account_count_by_model_key -- model names can be short).
(Convention adapted from the adopted P0-1 schema baseline @db5f37b11 shape(): "a
date-keyed or id-keyed map explodes; sample ONE representative child".)
First exercised 2026-08-07: the narrow first-cut convention (explicit list only) exploded
date-keyed meta maps into 452 divergent paths for aggregate-aua-timeseries; this revision
collapses them while preserving every genuine schema divergence (W-1 et al).
"""
from __future__ import annotations

import datetime as dt
import json
import sys

import boto3

BUCKET = "opal-data-portal-v2"
SCOPES = ["global", "49financial", "inflection", "cottonwood"]
ARTIFACT_TYPES = ["aggregate-aua-timeseries", "aum-metrics", "account-distribution"]
EXTRAS = [
    "platinum/mdpf/cottonwood/account-units.json",
    "platinum/mdpf/global/non-model-assets.json",
]
DATA_KEYED_MAPS = {"by_model", "account_count_by_model_key"}


def key_of(scope: str, atype: str) -> str:
    return "platinum/mdpf/{s}/{t}.json".format(s=scope, t=atype)


def _data_like(k: str) -> bool:
    if k in SCOPES or "/" in k:
        return True
    if len(k) == 10 and k[4] == "-" and k[7] == "-":
        return True
    return k.isdigit() or len(k) > 12


def key_paths(obj, prefix: str = "", out=None, field_name: str = ""):
    """Schema-grain key-path set: recursive dict keys, [] for arrays, <map>+<*> for data-keyed maps."""
    if out is None:
        out = set()
    if isinstance(obj, dict):
        keys = list(obj.keys())
        is_data_keyed = field_name in DATA_KEYED_MAPS or (
            bool(keys) and all(_data_like(str(k)) for k in keys)
        )
        if is_data_keyed and prefix:
            out.add(prefix + ".<map>")
            rep = obj[sorted(keys, key=str)[0]]
            key_paths(rep, prefix + ".<*>", out, "")
            return out
        for k, v in obj.items():
            path = (prefix + "." if prefix else "") + str(k).replace(".", "\\.")
            out.add(path)
            key_paths(v, path, out, str(k))
    elif isinstance(obj, list):
        for el in obj:
            key_paths(el, prefix + "[]", out, field_name)
    return out


def cmd_r1() -> int:
    s3 = boto3.client("s3")
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    present, absent = [], []
    for scope in SCOPES:
        for atype in ARTIFACT_TYPES:
            key = key_of(scope, atype)
            try:
                s3.head_object(Bucket=BUCKET, Key=key)
                present.append(key)
            except Exception:
                absent.append(key)
    print("R1 EXISTENCE verdict at {t} (EXISTENCE ONLY -- says NOTHING about freshness):".format(t=now))
    print("DENOMINATOR: {p} of {d} canonical keys EXIST".format(p=len(present), d=len(SCOPES) * len(ARTIFACT_TYPES)))
    for k in absent:
        print("  ABSENT: s3://{b}/{k}".format(b=BUCKET, k=k))
    if not absent:
        print("  all 12 canonical keys exist. This verdict is identical whether fresh or frozen.")
    return 0 if not absent else 2


def cmd_r2() -> int:
    import pathlib

    s3 = boto3.client("s3")
    now_dt = dt.datetime.now(dt.timezone.utc)
    now = now_dt.isoformat()
    print("R2 KEY-SET IDENTITY at {t} -- per artifact type, set-diff across the 4 scopes:".format(t=now))
    rc = 0
    full_record = {"run_instant_utc": now, "run_by": "3.0.0_SA_CVO~Z", "types": {}}
    for atype in ARTIFACT_TYPES:
        sets = {}
        for scope in SCOPES:
            key = key_of(scope, atype)
            body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read().decode("utf-8")
            sets[scope] = key_paths(json.loads(body))
        union = set().union(*sets.values())
        inter = set.intersection(*sets.values())
        diff = union - inter
        print("  {t}: union={u} paths, intersection={i}, divergent={d}  -> {v}".format(
            t=atype, u=len(union), i=len(inter), d=len(diff),
            v="PASS (set-diff empty)" if not diff else "FAIL (non-empty set-diff)"))
        shown = sorted(diff)[:60]
        for p in shown:
            holders = [s for s in SCOPES if p in sets[s]]
            missing = [s for s in SCOPES if p not in sets[s]]
            print("    {p}: present={h} absent={m}".format(p=p, h=",".join(holders), m=",".join(missing)))
        if len(diff) > len(shown):
            print("    ... and {n} more divergent paths (full set in the run record)".format(
                n=len(diff) - len(shown)))
        if diff:
            rc = 2
        full_record["types"][atype] = {
            "union": len(union), "intersection": len(inter), "divergent": len(diff),
            "divergent_paths": {
                p: {"present": [s for s in SCOPES if p in sets[s]],
                    "absent": [s for s in SCOPES if p not in sets[s]]}
                for p in sorted(diff)
            },
        }
    runs = pathlib.Path(__file__).parent / "runs"
    runs.mkdir(exist_ok=True)
    out = runs / "R2_{s}.json".format(s=now_dt.strftime("%Y%m%dT%H%M%SZ"))
    out.write_text(json.dumps(full_record, indent=2) + "\n", encoding="ascii")
    print("DENOMINATOR: {n} scope-bodies read per type x {t} types = {tot} served bodies".format(
        n=len(SCOPES), t=len(ARTIFACT_TYPES), tot=len(SCOPES) * len(ARTIFACT_TYPES)))
    print("FULL RECORD: runs/{o}".format(o=out.name))
    return rc


def cmd_r12() -> int:
    s3 = boto3.client("s3")
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    print("R12 NOTHING-RETIRES-EARLY at {t}:".format(t=now))
    rc = 0
    for key in EXTRAS:
        try:
            h = s3.head_object(Bucket=BUCKET, Key=key)
            print("  PRESENT: s3://{b}/{k}  VersionId={v}".format(
                b=BUCKET, k=key, v=h.get("VersionId", "null")))
        except Exception:
            print("  *** ABSENT ***: s3://{b}/{k} -- a standalone extra is GONE before its fold "
                  "passed R2+R7. REGRESSION REPORT to 2.0.0_SA_COO~Z; retirement is Andrew's act.".format(
                      b=BUCKET, k=key))
            rc = 2
    print("DENOMINATOR: {n} of {d} standalone extras checked".format(n=len(EXTRAS), d=len(EXTRAS)))
    return rc


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("r1", "r2", "r12"):
        print("usage: g2_instruments.py {r1|r2|r12}")
        return 1
    return {"r1": cmd_r1, "r2": cmd_r2, "r12": cmd_r12}[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
