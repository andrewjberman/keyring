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
to []; the children of DATA-KEYED maps (by_model, account_count_by_model_key) are DATA,
not schema, and collapse to path.<map> -- model names legitimately differ per scope.
(Convention adapted from the adopted P0-1 schema baseline @db5f37b11, which samples map
children rather than exploding them.)
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


def key_paths(obj, prefix: str = "", out=None):
    """Schema-grain key-path set: recursive dict keys, [] for arrays, <map> for data-keyed maps."""
    if out is None:
        out = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            path = (prefix + "." if prefix else "") + str(k).replace(".", "\\.")
            if str(k) in DATA_KEYED_MAPS and isinstance(v, dict):
                out.add(path + ".<map>")
                continue
            out.add(path)
            key_paths(v, path, out)
    elif isinstance(obj, list):
        for el in obj:
            key_paths(el, prefix + "[]", out)
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
    s3 = boto3.client("s3")
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    print("R2 KEY-SET IDENTITY at {t} -- per artifact type, set-diff across the 4 scopes:".format(t=now))
    rc = 0
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
        for p in sorted(diff):
            holders = [s for s in SCOPES if p in sets[s]]
            missing = [s for s in SCOPES if p not in sets[s]]
            print("    {p}: present={h} absent={m}".format(p=p, h=",".join(holders), m=",".join(missing)))
            rc = 2
    print("DENOMINATOR: {n} scope-bodies read per type x {t} types = {tot} served bodies".format(
        n=len(SCOPES), t=len(ARTIFACT_TYPES), tot=len(SCOPES) * len(ARTIFACT_TYPES)))
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
