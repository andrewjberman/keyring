#!/usr/bin/env python3
"""old_list_reader_census_bd.py -- MDPF_SECCLASS SC-e-41 (FWD-5, row W25-S5): the widened reader census of the old list
(DynamoDB `bd-securities`, us-east-1) over the three places round 8's trace excluded.

READ-ONLY. No write, no install, no download. Prints, in order, with its denominator:
  1. BD TREE: `git grep -l -E "bd-securities|BD_SECURITIES_TABLE" -- data/black_diamond/` minus test files (the census the
     issuer's check recomputes), and per file the call sites (table handle, scan, get_item, batch_get, query, write verbs);
  2. RUN-TIME NAMES: every builder of the table name assembled at run time ('%s-securities', the naming registry's
     `serving-route` alias) and every module that imports a builder module;
  3. ROLE GRANTS: every IAM role, user and group scanned; each principal that can READ the table by any policy
     (explicit table ARN, a wildcard that matches it, `*`, or an AWS-managed DynamoDB policy), the Deny statements that
     could cut it, and the functions / instance profiles / task definitions that assume each such role;
  4. the canonical table's `updated_by` write census (the CANONICAL-PRODUCER count);
  5. the old list's own 14-day request counts by operation (CloudWatch), so a live reader is told from a silent one.
Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_reader_census_bd.py
"""
import collections
import fnmatch
import json
import re
import subprocess
import sys

PAT = "bd-securities|BD_SECURITIES_TABLE"
REGION = "us-east-1"
TABLE = "bd-securities"
READ_ACTIONS = ["dynamodb:scan", "dynamodb:getitem", "dynamodb:query", "dynamodb:batchgetitem", "dynamodb:partiqlselect"]
CALL_RE = re.compile(r"\.Table\(|\.scan\(|get_item\(|batch_get_item|\.query\(|put_item\(|update_item\(|batch_writer|delete_item\(")
WRITE_RE = re.compile(r"put_item\(|update_item\(|batch_writer|delete_item\(")


def run(cmd, timeout=120):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)


def bd_census():
    r = run(["git", "grep", "-l", "-E", PAT, "--", "data/black_diamond/"])
    return [f for f in r.stdout.splitlines() if "/tests/" not in f and "/test_" not in f]


def part1():
    files = bd_census()
    print(f"[1] BD TREE CENSUS: {len(files)} files (git grep -l -E '{PAT}' -- data/black_diamond/, minus test files)")
    total_hits = total_calls = 0
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
        hits = [i + 1 for i, ln in enumerate(lines) if re.search(PAT, ln)]
        calls = [(i + 1, ln.strip()[:90]) for i, ln in enumerate(lines) if CALL_RE.search(ln)]
        writes = [n for n, ln in calls if WRITE_RE.search(ln)]
        total_hits += len(hits)
        total_calls += len(calls)
        print(f"  {f}: {len(hits)} naming lines, {len(calls)} table-call lines ({len(writes)} write verbs)")
        for n, ln in calls:
            print(f"      call {n}: {ln}")
    print(f"  TOTAL: {len(files)} files, {total_hits} naming lines, {total_calls} table-call lines swept")
    return len(files), total_hits, total_calls


def part2():
    print("[2] RUN-TIME NAMES: builders of a table name assembled at run time")
    pats = r"%s-securities|\{[^}]*\}-securities|\+ *['\"]-securities|format\([^)]*\).*-securities|['\"]-securities['\"]"
    r = run(["git", "grep", "-n", "-E", pats, "--", "*.py", "*.sh", "*.ts", "*.tsx", "*.tf", "*.yaml", "*.yml"])
    builders = [ln for ln in r.stdout.splitlines()
                if not ln.startswith(("org/", "docs/", "rcg/")) and "/tests/" not in ln and "/test_" not in ln]
    for b in builders:
        print("  builder:", b[:200])
    mods = sorted({b.split(":")[0] for b in builders})
    callers = []
    for m in mods:
        stem = m.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        rr = run(["git", "grep", "-n", "-E", rf"(import|from) +{re.escape(stem)}\b", "--", "*.py"])
        for ln in rr.stdout.splitlines():
            if not ln.startswith(("org/", "docs/")) and "/tests/" not in ln and "/test_" not in ln:
                callers.append(ln[:200])
                print("  importer of", stem + ":", ln[:200])
    r2 = run(["git", "grep", "-n", "-E", r"default_bd_securities_lookup\(|--legacy-fork-table|args\.legacy_fork_table", "--", "*.py", "*.sh", "*.json", "*.yaml", "*.tf"])
    supplied = [ln for ln in r2.stdout.splitlines()
                if not ln.startswith(("org/", "docs/", "rcg/")) and "/tests/" not in ln and "/test_" not in ln]
    for b in supplied:
        print("  caller-supplied name:", b[:200])
    builders = builders + supplied
    mods = sorted(set(mods) | {b.split(":")[0] for b in supplied})
    try:
        sys.path.insert(0, "lib")
        from opal_naming import lookup  # noqa: PLC0415
        slot = next(a["spelling"] for a in lookup("49financial")["aliases"] if "serving-route" in a.get("planes", []))
        print(f"  registry resolution: lookup('49financial') serving-route alias = '{slot}' -> '%s-securities' = '{slot}-securities'")
    except Exception as e:  # noqa: BLE001 -- report, never swallow
        print(f"  registry resolution UNREAD: {type(e).__name__}: {e}")
    print(f"  TOTAL: {len(builders)} builder lines in {len(mods)} files, {len(callers)} importer lines")
    return len(builders), len(mods), len(callers)


def _arn_match(res, table_arn):
    resl = [res] if isinstance(res, str) else list(res)
    return any(x == "*" or fnmatch.fnmatchcase(table_arn, x) for x in resl)


def _matched_actions(act):
    acts = [act] if isinstance(act, str) else list(act or [])
    return [a for a in acts if a.lower() == "*" or a.lower() == "dynamodb:*"
            or any(fnmatch.fnmatchcase(r, a.lower()) for r in READ_ACTIONS)]


def _action_match(act, notact=None):
    return bool(_matched_actions(act))


def _stmts(doc):
    s = doc.get("Statement", [])
    return [s] if isinstance(s, dict) else s


def grants_read(doc, table_arn):
    """Return (allow_reads, denies): the statements that Allow / Deny a read on the table (Condition noted)."""
    allow, deny = [], []
    for st in _stmts(doc):
        eff = st.get("Effect")
        if "NotAction" in st or "NotResource" in st:
            note = "NotAction/NotResource statement (conservatively counted)"
            res_ok = ("NotResource" in st) or _arn_match(st.get("Resource", "*"), table_arn)
            act_ok = ("NotAction" in st) or _action_match(st.get("Action"))
            if res_ok and act_ok:
                (allow if eff == "Allow" else deny).append(note)
            continue
        if _action_match(st.get("Action")) and _arn_match(st.get("Resource", []), table_arn):
            tag = json.dumps(_matched_actions(st.get("Action"))) + " on " + json.dumps(st.get("Resource"))[:100]
            if "Condition" in st:
                tag += " WITH-CONDITION " + json.dumps(st["Condition"])[:100]
            (allow if eff == "Allow" else deny).append(tag)
    return allow, deny


def part3():
    import boto3  # noqa: PLC0415
    print("[3] ROLE GRANTS: live IAM read (list/get only)")
    sts = boto3.client("sts")
    acct = sts.get_caller_identity()["Account"]
    table_arn = f"arn:aws:dynamodb:{REGION}:{acct}:table/{TABLE}"
    iam = boto3.client("iam")
    cache = {}

    def managed_doc(arn):
        if arn not in cache:
            p = iam.get_policy(PolicyArn=arn)["Policy"]
            cache[arn] = iam.get_policy_version(PolicyArn=arn, VersionId=p["DefaultVersionId"])["PolicyVersion"]["Document"]
        return cache[arn]

    findings = {}
    nprinc = {"roles": 0, "users": 0, "groups": 0}
    npol = 0

    def scan_principal(kind, name, attached, inline_names, get_inline):
        nonlocal npol
        res = {"allow": [], "deny": []}
        for pol in attached:
            npol += 1
            a, d = grants_read(managed_doc(pol["PolicyArn"]), table_arn)
            res["allow"] += [f"managed {pol['PolicyName']}: {x}" for x in a]
            res["deny"] += [f"managed {pol['PolicyName']}: {x}" for x in d]
        for pn in inline_names:
            npol += 1
            a, d = grants_read(get_inline(pn), table_arn)
            res["allow"] += [f"inline {pn}: {x}" for x in a]
            res["deny"] += [f"inline {pn}: {x}" for x in d]
        if res["allow"]:
            findings[(kind, name)] = res

    role_meta = {}
    for page in iam.get_paginator("list_roles").paginate():
        for r in page["Roles"]:
            nprinc["roles"] += 1
            n = r["RoleName"]
            role_meta[n] = r
            att = [p for pg in iam.get_paginator("list_attached_role_policies").paginate(RoleName=n) for p in pg["AttachedPolicies"]]
            inl = [x for pg in iam.get_paginator("list_role_policies").paginate(RoleName=n) for x in pg["PolicyNames"]]
            scan_principal("role", n, att, inl, lambda pn, n=n: iam.get_role_policy(RoleName=n, PolicyName=pn)["PolicyDocument"])
    for page in iam.get_paginator("list_users").paginate():
        for u in page["Users"]:
            nprinc["users"] += 1
            n = u["UserName"]
            att = [p for pg in iam.get_paginator("list_attached_user_policies").paginate(UserName=n) for p in pg["AttachedPolicies"]]
            inl = [x for pg in iam.get_paginator("list_user_policies").paginate(UserName=n) for x in pg["PolicyNames"]]
            scan_principal("user", n, att, inl, lambda pn, n=n: iam.get_user_policy(UserName=n, PolicyName=pn)["PolicyDocument"])
    for page in iam.get_paginator("list_groups").paginate():
        for g in page["Groups"]:
            nprinc["groups"] += 1
            n = g["GroupName"]
            att = [p for pg in iam.get_paginator("list_attached_group_policies").paginate(GroupName=n) for p in pg["AttachedPolicies"]]
            inl = [x for pg in iam.get_paginator("list_group_policies").paginate(GroupName=n) for x in pg["PolicyNames"]]
            scan_principal("group", n, att, inl, lambda pn, n=n: iam.get_group_policy(GroupName=n, PolicyName=pn)["PolicyDocument"])
    print(f"  scanned {nprinc['roles']} roles, {nprinc['users']} users, {nprinc['groups']} groups, {npol} policy attachments/inlines "
          f"({len(cache)} distinct managed documents); table ARN {table_arn}")
    reach_roles = sorted(n for (k, n) in findings if k == "role")
    for (kind, name), res in sorted(findings.items()):
        boundary = (role_meta[name].get("PermissionsBoundary") or {}).get("PermissionsBoundaryArn") if kind == "role" else None
        print(f"  CAN-READ {kind} {name}" + (f" [permissions boundary {boundary}]" if boundary else ""))
        for x in res["allow"]:
            print("      allow:", x)
        for x in res["deny"]:
            print("      DENY:", x)
    print(f"  PRINCIPALS THAT CAN READ THE TABLE: {len(findings)} ({len(reach_roles)} roles)")

    # group membership (who is behind a group grant)
    for (kind, name) in sorted(findings):
        if kind == "group":
            mem = [u["UserName"] for pg in iam.get_paginator("get_group").paginate(GroupName=name) for u in pg["Users"]]
            print(f"  MEMBERS of group {name}: {mem}")

    # assumers -- each limb guarded: an AccessDenied is reported as UNREAD for that limb, never as zero
    arn_by_role = {n: role_meta[n]["Arn"] for n in reach_roles}
    funcs = collections.defaultdict(list)
    nfun = None
    try:
        lam = boto3.client("lambda", region_name=REGION)
        nfun = 0
        for page in lam.get_paginator("list_functions").paginate():
            for f in page["Functions"]:
                nfun += 1
                funcs[f["Role"]].append(f["FunctionName"])
    except Exception as e:  # noqa: BLE001
        print(f"  ASSUMERS lambda UNREAD: {type(e).__name__}: {str(e)[:120]}")
    profiles = {}
    inst_by_profile = collections.defaultdict(list)
    ninst = None
    try:
        for page in iam.get_paginator("list_instance_profiles").paginate():
            for ip in page["InstanceProfiles"]:
                for r in ip["Roles"]:
                    profiles.setdefault(r["RoleName"], []).append((ip["InstanceProfileName"], ip["Arn"]))
        ec2 = boto3.client("ec2", region_name=REGION)
        ninst = 0
        for page in ec2.get_paginator("describe_instances").paginate():
            for rsv in page["Reservations"]:
                for i in rsv["Instances"]:
                    ninst += 1
                    a = (i.get("IamInstanceProfile") or {}).get("Arn")
                    if a:
                        tag = next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), "")
                        inst_by_profile[a].append(f"{i['InstanceId']}({i['State']['Name']},{tag},last-launch {i['LaunchTime'].strftime('%Y-%m-%dT%H:%MZ')})")
    except Exception as e:  # noqa: BLE001
        print(f"  ASSUMERS ec2/instance-profile UNREAD: {type(e).__name__}: {str(e)[:120]}")
    ecs_by_role = collections.defaultdict(list)
    nfam = None
    try:
        ecs = boto3.client("ecs", region_name=REGION)
        nfam = 0
        for page in ecs.get_paginator("list_task_definition_families").paginate(status="ACTIVE"):
            for fam in page["families"]:
                nfam += 1
                td = ecs.describe_task_definition(taskDefinition=fam)["taskDefinition"]
                for k in ("taskRoleArn", "executionRoleArn"):
                    if td.get(k):
                        ecs_by_role[td[k]].append(f"{fam}:{k}")
    except Exception as e:  # noqa: BLE001
        print(f"  ASSUMERS ecs UNREAD: {type(e).__name__}: {str(e)[:120]}")
    glue_by_role = collections.defaultdict(list)
    nglue = None
    try:
        glue = boto3.client("glue", region_name=REGION)
        nglue = 0
        for page in glue.get_paginator("get_jobs").paginate():
            for j in page["Jobs"]:
                nglue += 1
                glue_by_role[j["Role"]].append(j["Name"])
    except Exception as e:  # noqa: BLE001
        print(f"  ASSUMERS glue UNREAD: {type(e).__name__}: {str(e)[:120]}")
    cb_by_role = collections.defaultdict(list)
    ncb = None
    try:
        cb = boto3.client("codebuild", region_name=REGION)
        names = [n for pg in cb.get_paginator("list_projects").paginate() for n in pg["projects"]]
        ncb = len(names)
        for i in range(0, len(names), 100):
            for p in cb.batch_get_projects(names=names[i:i + 100])["projects"]:
                cb_by_role[p["serviceRole"]].append(p["name"])
    except Exception as e:  # noqa: BLE001
        print(f"  ASSUMERS codebuild UNREAD: {type(e).__name__}: {str(e)[:120]}")
    print(f"  ASSUMERS scanned (None = UNREAD): lambda functions {nfun}, EC2 instances {ninst}, "
          f"roles-in-instance-profiles {len(profiles)}, active ECS families {nfam}, Glue jobs {nglue}, CodeBuild projects {ncb}")
    for n in reach_roles:
        a = arn_by_role[n]
        flat = []
        for st in _stmts(role_meta[n]["AssumeRolePolicyDocument"]):
            pr = st.get("Principal") or {}
            v = pr.get("Service") or json.dumps(pr.get("AWS"))[:80]
            flat += v if isinstance(v, list) else [v]
        insts = [i for _, pa in profiles.get(n, []) for i in inst_by_profile.get(pa, [])]
        for t in flat:  # a role trusted by another role: that role's instances are the ones that can assume it
            m = re.search(r"role/([\w+=,.@-]+)", str(t))
            if m:
                insts += [f"via {m.group(1)}: {i}" for _, pa in profiles.get(m.group(1), []) for i in inst_by_profile.get(pa, [])]
        print(f"  ASSUMED-BY role {n}: trust={flat}; lambda={funcs.get(a, [])}; instance-profiles={[p for p, _ in profiles.get(n, [])]}; "
              f"instances={insts}; ecs={ecs_by_role.get(a, [])}; glue={glue_by_role.get(a, [])}; codebuild={cb_by_role.get(a, [])}")
    return nprinc, len(findings), len(reach_roles), nfun


def part4():
    import boto3  # noqa: PLC0415
    ddb = boto3.client("dynamodb", region_name=REGION)
    cnt, n = collections.Counter(), 0
    for page in ddb.get_paginator("scan").paginate(TableName="etf-classifications", ProjectionExpression="ticker, updated_by"):
        for it in page["Items"]:
            n += 1
            cnt[it.get("updated_by", {}).get("S", "<none>")] += 1
    d = ddb.describe_table(TableName=TABLE)["Table"]
    print(f"[4] CANONICAL WRITE CENSUS: etf-classifications {n} rows scanned; updated_by = {json.dumps(dict(cnt.most_common()))}")
    print(f"    old list {TABLE}: {d['ItemCount']} items (describe_table), status {d['TableStatus']}")
    return n


def part5():
    import datetime  # noqa: PLC0415
    import boto3  # noqa: PLC0415
    cw = boto3.client("cloudwatch", region_name=REGION)
    end = datetime.datetime.now(datetime.timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = end - datetime.timedelta(days=14)
    print(f"[5] TABLE ACTIVITY (CloudWatch AWS/DynamoDB, table {TABLE}, daily, {start.date()}..{end.date()} UTC): request counts by operation")
    for op in ("Scan", "GetItem", "BatchGetItem", "Query", "PutItem", "UpdateItem"):
        r = cw.get_metric_statistics(Namespace="AWS/DynamoDB", MetricName="SuccessfulRequestLatency",
                                     Dimensions=[{"Name": "TableName", "Value": TABLE}, {"Name": "Operation", "Value": op}],
                                     StartTime=start, EndTime=end, Period=86400, Statistics=["SampleCount"])
        pts = [(d["Timestamp"].strftime("%m-%d"), int(d["SampleCount"])) for d in sorted(r["Datapoints"], key=lambda x: x["Timestamp"])]
        print(f"    {op}: {pts if pts else 'no datapoint in the window'}")
    return 0


def main():
    nfiles, nhits, ncalls = part1()
    nb, nm, nc = part2()
    try:
        nprinc, nfind, nroles, nfun = part3()
        live = (f"roles read: {nprinc['roles']} roles + {nprinc['users']} users + {nprinc['groups']} groups scanned, "
                f"{nfind} principals can read the table ({nroles} roles), {nfun} Lambda functions mapped")
        part4()
        part5()
    except Exception as e:  # noqa: BLE001 -- report, never swallow
        live = f"live plane UNREAD ({type(e).__name__}: {e})"
        print("[3/4] LIVE PLANE UNREAD --", live)
    print(f"DENOMINATOR: {nfiles} BD-tree census files, {nhits} naming lines and {ncalls} table-call lines swept; "
          f"{nb} run-time-name builder lines in {nm} files, {nc} importer lines; {live}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
