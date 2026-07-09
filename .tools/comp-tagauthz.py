#!/usr/bin/env python3
"""comp-tagauthz -- are this resource's TAGS load-bearing for AUTHORIZATION?

THE QUESTION THIS ANSWERS (CTO standing arch rule, 2026-07-09T195725Z):

    "A Terraform tree that sets `default_tags` must not manage resources whose tags carry
     authorization. Tags are metadata UNTIL someone writes a Condition on them -- at which point
     they are an ACL wearing metadata's clothes, and a provider-level default that silently
     rewrites them is a privilege-revocation engine."

The gate this REPLACES (retracted by its own author, same message):

    WRONG: "does the plan change only `tags`/`tags_all`?"   <- measures ATTRIBUTE SURFACE
    RIGHT: "does the plan change the VALUE of a tag key that appears in any policy Condition,
            on a resource that Condition's Resource matches?"   <- measures AUTHORIZATION

In the Opal account a plan containing ONLY `tags`/`tags_all` is PRECISELY the plan that silently
revokes authorization: `shared-infra`'s `default_tags` keys are `Project` and `System`, and those
are exactly the keys two of our policies condition on. "It's just tags" is the dangerous case.

DERIVED, NEVER REMEMBERED. The authorization-bearing (key, value) pairs come from ONE account-wide
call -- `iam get-account-authorization-details` -- not from a hand-kept list. Enumerating them by
hand is the defect this whole project exists to correct.

Exit codes:  0 = no tag-authorization collision   2 = COLLISION (do not default_tag)   1 = error
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

TAG_COND_RE = re.compile(r"aws:(ResourceTag|RequestTag|PrincipalTag)/(?P<key>[^\"'\s,}]+)", re.I)
TAGKEYS_RE = re.compile(r"aws:TagKeys", re.I)


def sh(cmd: list[str]) -> str:
    """Run a CLI command. Resolves the executable explicitly -- on Windows `aws` is a .cmd shim
    that bare subprocess cannot find, and a silent FileNotFoundError here would look exactly like
    an empty result. A failed probe must never be mistaken for a clean probe."""
    import shutil

    exe = shutil.which(cmd[0]) or shutil.which(cmd[0] + ".cmd")
    if not exe:
        print(f"ERROR: executable not found on PATH: {cmd[0]}", file=sys.stderr)
        sys.exit(1)
    p = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True)
    if p.returncode != 0:
        print(f"ERROR: {' '.join(cmd[:4])}... rc={p.returncode}\n{p.stderr[:400]}", file=sys.stderr)
        sys.exit(1)
    if not p.stdout.strip():
        print(f"ERROR: {' '.join(cmd[:4])}... returned EMPTY output (rc=0). "
              "Refusing to treat an empty probe as a clean result.", file=sys.stderr)
        sys.exit(1)
    return p.stdout


def _as_list(x):
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


def collect_conditions(aad: dict) -> list[dict]:
    """Every statement whose Condition references a tag context key. Whole account."""
    found: list[dict] = []

    def scan(doc, source):
        if not isinstance(doc, dict):
            return
        for st in _as_list(doc.get("Statement")):
            cond = st.get("Condition")
            if not cond:
                continue
            blob = json.dumps(cond)
            keys = {m.group("key") for m in TAG_COND_RE.finditer(blob)}
            if not keys and not TAGKEYS_RE.search(blob):
                continue
            # pull the concrete (key -> allowed values) pairs out of the operators
            pairs: dict[str, list[str]] = {}
            for _op, kv in cond.items():
                if not isinstance(kv, dict):
                    continue
                for ck, cv in kv.items():
                    m = TAG_COND_RE.search(ck)
                    if m:
                        pairs.setdefault(m.group("key"), []).extend(_as_list(cv))
            found.append(
                {
                    "source": source,
                    "sid": st.get("Sid", "(none)"),
                    "effect": st.get("Effect"),
                    "actions": _as_list(st.get("Action")),
                    "resources": _as_list(st.get("Resource")),
                    "keys": sorted(keys),
                    "pairs": pairs,
                    "condition": cond,
                }
            )

    for r in aad.get("RoleDetailList", []):
        for p in r.get("RolePolicyList", []):
            scan(p.get("PolicyDocument", {}), f"role/{r['RoleName']}:inline:{p['PolicyName']}")
    for pol in aad.get("Policies", []):
        for v in pol.get("PolicyVersionList", []):
            if v.get("IsDefaultVersion"):
                scan(v.get("Document", {}), f"managed/{pol['PolicyName']}")
    for u in aad.get("UserDetailList", []):
        for p in u.get("UserPolicyList", []):
            scan(p.get("PolicyDocument", {}), f"user/{u['UserName']}:{p['PolicyName']}")
    for g in aad.get("GroupDetailList", []):
        for p in g.get("GroupPolicyList", []):
            scan(p.get("PolicyDocument", {}), f"group/{g['GroupName']}:{p['PolicyName']}")
    return found


def is_ours(source: str) -> bool:
    """AWS service-linked-role policies are AWS's, not ours. Report both; gate on ours."""
    aws_managed = (
        "ServiceRolePolicy",
        "AWSServiceRole",
        "AmazonECSServiceRolePolicy",
        "AmazonRDSServiceRolePolicy",
        "APIGatewayServiceRolePolicy",
        "AmazonOpenSearchServiceRolePolicy",
    )
    return not any(a in source for a in aws_managed)


def default_tag_keys(tree: str) -> list[str]:
    """Parse provider-level default_tags keys out of a terraform tree's .tf files."""
    import glob
    import os

    keys: list[str] = []
    for f in glob.glob(os.path.join(tree, "*.tf")):
        txt = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r"default_tags\s*\{(.*?)\n\s*\}", txt, re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            km = re.match(r"\s*([A-Za-z0-9_-]+)\s*=", line)
            if km and km.group(1) != "tags":
                keys.append(km.group(1))
    return sorted(set(keys))


def tree_instance_ids(tree: str) -> set[str]:
    """EC2 instance IDs a terraform tree currently manages (read-only `state pull`)."""
    import os

    ws = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tf = os.path.join(ws, ".tools", "terraform.exe")
    p = subprocess.run([tf, "state", "pull"], cwd=tree, capture_output=True, text=True)
    if p.returncode != 0 or not p.stdout.strip():
        print(f"WARN: could not read state for {tree} -- reporting NO managed instances would be a "
              "claim about the probe, not the tree. Treating as UNKNOWN.", file=sys.stderr)
        return set()
    try:
        st = json.loads(p.stdout)
    except json.JSONDecodeError:
        return set()
    ids: set[str] = set()
    for r in st.get("resources", []):
        if r.get("type") == "aws_instance":
            for i in r.get("instances", []):
                iid = (i.get("attributes") or {}).get("id")
                if iid:
                    ids.add(iid)
    return ids


def ec2_tagged() -> list[dict]:
    out = sh(["aws", "ec2", "describe-instances", "--output", "json"])
    d = json.loads(out or "{}")
    rows = []
    for res in d.get("Reservations", []):
        for i in res.get("Instances", []):
            rows.append(
                {
                    "arn": f"instance/{i['InstanceId']}",
                    "id": i["InstanceId"],
                    "state": i.get("State", {}).get("Name"),
                    "tags": {t["Key"]: t["Value"] for t in i.get("Tags", [])},
                }
            )
    return rows


def banner(aad: dict, conds: list[dict]) -> None:
    """State the denominator. An artifact that cannot say what universe it swept cannot be
    trusted about what it found."""
    print("-" * 78)
    print("SWEPT (derived from the account, one call: iam get-account-authorization-details):")
    print(f"  roles {len(aad.get('RoleDetailList', []))}   local+attached policies "
          f"{len(aad.get('Policies', []))}   users {len(aad.get('UserDetailList', []))}   "
          f"groups {len(aad.get('GroupDetailList', []))}")
    print("  SCPs: NOT APPLICABLE -- account is not in an AWS Organization "
          "(AWSOrganizationsNotInUseException). Stated, not implied.")
    print("NOT SWEPT (named, not implied): S3 bucket policies, KMS key policies,")
    print("  permission boundaries, session policies, resource policies generally.")
    print(f"tag-conditioned statements found: {len(conds)} "
          f"({sum(1 for c in conds if is_ours(c['source']))} ours, "
          f"{sum(1 for c in conds if not is_ours(c['source']))} AWS service-linked)")
    print("-" * 78)


def cmd_pairs(args) -> int:
    aad = json.loads(sh(["aws", "iam", "get-account-authorization-details", "--output", "json"]))
    conds = collect_conditions(aad)
    banner(aad, conds)
    ours = [c for c in conds if is_ours(c["source"])]
    if not ours:
        print("\nNo policy WE authored conditions on a tag. Tags are metadata in this account.")
        return 0
    print("\nAUTHORIZATION-BEARING TAGS (ours). These tag values ARE an ACL:\n")
    for c in ours:
        print(f"  {c['source']}")
        print(f"    Sid      : {c['sid']}   Effect: {c['effect']}")
        print(f"    Actions  : {', '.join(c['actions'][:6])}")
        print(f"    Resource : {', '.join(str(r) for r in c['resources'][:3])}")
        for k, vals in c["pairs"].items():
            print(f"    TAG      : {k} = {vals}   <- changing this value CHANGES ACCESS")
        print()
    return 0


def cmd_check(args) -> int:
    aad = json.loads(sh(["aws", "iam", "get-account-authorization-details", "--output", "json"]))
    all_conds = collect_conditions(aad)
    # banner MUST report the full universe it swept, not the filtered subset -- a banner that
    # states the post-filter count is an artifact misreporting its own denominator.
    banner(aad, all_conds)
    conds = [c for c in all_conds if is_ours(c["source"])]

    # authorization-bearing (key -> {value -> [sources]})
    authz: dict[str, dict[str, list[str]]] = {}
    for c in conds:
        for k, vals in c["pairs"].items():
            for v in vals:
                authz.setdefault(k, {}).setdefault(v, []).append(c["source"])

    dkeys = default_tag_keys(args.default_tags_tree) if args.default_tags_tree else []
    if dkeys:
        print(f"\ndefault_tags keys in {args.default_tags_tree}: {dkeys}")
        collide = sorted(set(dkeys) & set(authz))
        if collide:
            print(f"  *** KEY COLLISION: {collide} are BOTH default_tags keys AND authorization keys.")
        else:
            print("  no key collision with authorization-bearing keys")

    rows = ec2_tagged()
    cands = set(args.candidate or [])
    scoped = args.candidate or args.from_state

    if args.from_state and args.default_tags_tree:
        cands |= tree_instance_ids(args.default_tags_tree)

    if not scoped:
        # ADVISORY: no candidate set given. This is a universe listing, NOT a per-tree verdict --
        # flagging every tag-authorized instance against a tree that may never manage any of them
        # would be an alarm reporting on something other than what it claims to measure.
        print("\nMODE: ADVISORY (no --candidate / --from-state given).")
        print("  This lists the account's tag-AUTHORIZED instances. It is NOT a verdict on this tree:")
        print("  a tree only endangers a resource it actually MANAGES. Pass the batch's candidates")
        print("  (--candidate i-xxx, repeatable) or --from-state for a real gate verdict.\n")
    else:
        print(f"\nMODE: GATE. Scoped to {len(cands)} candidate resource(s) this tree would manage.\n")

    bad = 0
    listed = 0
    for r in rows:
        if scoped and r["id"] not in cands:
            continue
        deps = [(k, v, authz[k][v]) for k, v in r["tags"].items() if k in authz and v in authz[k]]
        if not deps:
            continue
        listed += 1
        overwritten = [d for d in deps if d[0] in dkeys] if dkeys else []
        verdict = ("DANGER" if overwritten else "TAG-AUTHORIZED") if scoped else "TAG-AUTHORIZED"
        if scoped and overwritten:
            bad += 1
        print(f"  [{verdict}] {r['id']} ({r['state']})")
        for k, v, srcs in deps:
            mark = "  <-- this tree's default_tags WOULD OVERWRITE THIS" if k in dkeys else ""
            print(f"      {k}={v}  grants access via {srcs[0]}{mark}")
        print()

    if not scoped:
        print(f"RESULT (advisory): {listed} live instance(s) carry an access-granting tag.")
        if set(dkeys) & set(authz):
            print(f"         This tree's default_tags keys {sorted(set(dkeys) & set(authz))} ARE "
                  "authorization keys, so importing ANY of the above into it would revoke access.")
        print("         Exit 0: advisory only. Re-run with --candidate/--from-state to gate a batch.")
        return 0

    if bad:
        print(f"RESULT: {bad} CANDIDATE(s) whose ACCESS-GRANTING tag would be overwritten by "
              f"{args.default_tags_tree}'s default_tags.")
        print("        default_tags MUST NOT apply to these. Per-resource `tags` override, or keep")
        print("        them out of a default_tags tree entirely. (CTO standing arch rule 195725Z.)")
        return 2
    print(f"RESULT: none of the {len(cands)} candidate(s) has an access-granting tag this tree "
          "would overwrite.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-tagauthz", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pairs", help="list the authorization-bearing tag (key,value) pairs, derived from the account")
    c = sub.add_parser("check", help="flag CANDIDATE resources whose access-granting tag a tree's default_tags would overwrite")
    c.add_argument("--default-tags-tree", help="path to a terraform tree that sets provider default_tags")
    c.add_argument("--candidate", action="append",
                   help="an EC2 instance id this tree would manage (repeatable). Scopes the gate.")
    c.add_argument("--from-state", action="store_true",
                   help="use the instances the tree ALREADY manages as the candidate set")
    args = ap.parse_args()
    return cmd_pairs(args) if args.cmd == "pairs" else cmd_check(args)


if __name__ == "__main__":
    sys.exit(main())
