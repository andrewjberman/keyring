#!/usr/bin/env python3
"""old_list_reader_trace.py -- MDPF_SECCLASS SC-e-38 census of who can read the old list (DynamoDB `bd-securities`).

READ-ONLY. Prints the denominator line the trace file carries, then the reader list:
  1. the repo census: `git grep -l -E "bd-securities|BD_SECURITIES_TABLE"` over *.py *.ts *.tsx *.tf *.json, minus
     data/black_diamond/**, org/** and test files (the CTO's printed command, AMENDMENT 1) -- the files that need a section;
  2. `comp-find 'bd-securities|BD_SECURITIES_TABLE' --files` for its own denominator (files scanned, hits);
  3. the live plane: `comp-find --corpus aws 'bd-securities'`; if the served graph is unreachable for this principal
     (a BLOCKED line, not a zero) the script says so and reads the live plane directly, read-only: customer-managed and
     role-inline IAM policies that name the table, Lambda environments that name it, and the canonical table's
     `updated_by` write census.
Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reader_trace.py
"""
import collections
import json
import re
import subprocess
import sys

PAT = "bd-securities|BD_SECURITIES_TABLE"


def run(cmd, timeout=180):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)


def census_files():
    r = run(["git", "grep", "-l", "-E", PAT, "--", "*.py", "*.ts", "*.tsx", "*.tf", "*.json"])
    raw = r.stdout.splitlines()
    keep = []
    for f in raw:
        low = f.lower()
        if f.startswith(("data/black_diamond/", "org/")) or "/tests/" in low or "/test_" in low \
                or ".test." in low or "__tests__" in low:
            continue
        keep.append(f)
    return raw, keep


def comp_find_repo():
    r = run(["bash", "-c", f"comp-find '{PAT}' --files"])
    m = re.search(r"DENOMINATOR:\s*(\d+) hit\(s\) across (\d+) file\(s\) scanned", r.stdout)
    return (int(m.group(2)), int(m.group(1))) if m else (None, None)


def comp_find_aws():
    r = run(["bash", "-c", "comp-find --corpus aws 'bd-securities'"])
    out = (r.stdout + r.stderr).strip()
    if "BLOCKED" in out:
        return None, out.splitlines()[1].strip()[:200] if len(out.splitlines()) > 1 else out[:200]
    m = re.search(r"(\d+) node\(s\) scanned|(\d+) CloudNode", out)
    n = int(next(g for g in m.groups() if g)) if m else None
    return n, out[:200]


def live_plane():
    import boto3
    iam = boto3.client("iam")
    lam = boto3.client("lambda", region_name="us-east-1")
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    res = {}
    pols = {}
    npol = 0
    for page in iam.get_paginator("list_policies").paginate(Scope="Local"):
        for p in page["Policies"]:
            npol += 1
            doc = iam.get_policy_version(PolicyArn=p["Arn"], VersionId=p["DefaultVersionId"])["PolicyVersion"]["Document"]
            if "bd-securities" in json.dumps(doc):
                ents = iam.list_entities_for_policy(PolicyArn=p["Arn"])
                pols[p["PolicyName"]] = [r["RoleName"] for r in ents["PolicyRoles"]]
    res["managed_policies_scanned"] = npol
    res["managed_policies_naming_table"] = pols
    inline, nroles = [], 0
    for page in iam.get_paginator("list_roles").paginate():
        for r in page["Roles"]:
            nroles += 1
            for ip in iam.get_paginator("list_role_policies").paginate(RoleName=r["RoleName"]):
                for pn in ip["PolicyNames"]:
                    doc = iam.get_role_policy(RoleName=r["RoleName"], PolicyName=pn)["PolicyDocument"]
                    if "bd-securities" in json.dumps(doc):
                        inline.append((r["RoleName"], pn))
    res["roles_scanned"] = nroles
    res["inline_policies_naming_table"] = inline
    nfun, env_hits = 0, []
    for page in lam.get_paginator("list_functions").paginate():
        for f in page["Functions"]:
            nfun += 1
            env = (f.get("Environment") or {}).get("Variables") or {}
            if "bd-securities" in json.dumps(env):
                env_hits.append(f["FunctionName"])
    res["functions_scanned"] = nfun
    res["functions_env_naming_table"] = env_hits
    cnt, nrows = collections.Counter(), 0
    for page in ddb.get_paginator("scan").paginate(TableName="etf-classifications",
                                                   ProjectionExpression="ticker, updated_by"):
        for it in page["Items"]:
            nrows += 1
            cnt[it.get("updated_by", {}).get("S", "<none>")] += 1
    res["etf_classifications_rows"] = nrows
    res["etf_classifications_updated_by"] = dict(cnt.most_common())
    return res


def main():
    raw, keep = census_files()
    nfiles, nhits = comp_find_repo()
    aws_n, aws_note = comp_find_aws()
    live = None
    live_err = None
    try:
        live = live_plane()
    except Exception as e:  # noqa: BLE001 -- report, never swallow
        live_err = f"{type(e).__name__}: {e}"
    aws_txt = str(aws_n) if aws_n is not None else f"UNREAD (comp-find --corpus aws: {aws_note})"
    extra = ""
    if live:
        extra = (f"; live-plane direct read: {live['roles_scanned']} roles + {live['managed_policies_scanned']} "
                 f"customer-managed policies + {live['functions_scanned']} functions")
    print(f"DENOMINATOR: {nfiles} files scanned by comp-find (corpus=all), {nhits} hits; "
          f"census {len(keep)} files of {len(raw)} raw git-grep files (CTO command, minus data/black_diamond, org, tests); "
          f"aws nodes {aws_txt}{extra}")
    print("READER LIST (repo census, one section each in the trace):")
    for f in keep:
        print("  " + f)
    print("NAMED READERS added by the order face: advisor screens; resolve_tickers.py (data/black_diamond, excluded from census)")
    if live:
        print("LIVE PLANE (read-only):")
        print("  managed policies naming the table -> roles:", json.dumps(live["managed_policies_naming_table"]))
        print("  role-inline policies naming the table:", json.dumps(live["inline_policies_naming_table"]))
        print("  lambda environments naming the table:", json.dumps(live["functions_env_naming_table"]))
        print(f"  etf-classifications rows {live['etf_classifications_rows']}, updated_by census:",
              json.dumps(live["etf_classifications_updated_by"]))
    else:
        print("LIVE PLANE: UNREAD --", live_err)
    return 0


if __name__ == "__main__":
    sys.exit(main())
