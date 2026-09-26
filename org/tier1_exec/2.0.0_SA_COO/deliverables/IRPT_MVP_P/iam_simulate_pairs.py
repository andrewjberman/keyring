#!/usr/bin/env python3
"""iam simulate-principal-policy over an explicit (action, resource) list, printed with its denominator.

    python iam_simulate_pairs.py <role-name> <pairs.json> [--policy-input <policy.json>]

--policy-input adds a CANDIDATE identity policy to the role's own for the simulation (a pre-apply check).

<pairs.json> is a JSON list of [action, resource_arn] (or {"action":..,"resource":..,"expect":"allowed"|"denied",
"context": [<IAM ContextEntries>]} -- context for a conditioned grant, e.g. kms:ViaService + an EncryptionContext).
Prints one line per pair and the totals "N of M allowed". Exit 0 when every pair meets its expectation (default
expectation: allowed); exit 1 otherwise. Identity policies only (the role's attached and inline policies) -- a bucket
policy or KMS key policy is a separate plane, named where it applies.
"""
from __future__ import annotations

import json
import sys

import boto3


def main(argv):
    role, path = argv[1], argv[2]
    extra = []
    if "--policy-input" in argv:
        extra = [open(argv[argv.index("--policy-input") + 1], encoding="utf-8").read()]
    raw = json.load(open(path, encoding="utf-8"))
    pairs = []
    for item in raw:
        if isinstance(item, dict):
            pairs.append((item["action"], item["resource"], item.get("expect", "allowed"), item.get("context")))
        else:
            pairs.append((item[0], item[1], "allowed", None))
    iam = boto3.client("iam")
    arn = iam.get_role(RoleName=role)["Role"]["Arn"]
    met = allowed = 0
    for action, resource, expect, context in pairs:
        kw = {"ContextEntries": context} if context else {}
        if extra:
            kw["PolicyInputList"] = extra
        r = iam.simulate_principal_policy(PolicySourceArn=arn, ActionNames=[action], ResourceArns=[resource], **kw)
        decision = r["EvaluationResults"][0]["EvalDecision"]
        is_allowed = decision == "allowed"
        allowed += is_allowed
        ok = is_allowed == (expect == "allowed")
        met += ok
        print("%s %-9s %-24s %s (expect %s)%s" % ("OK  " if ok else "MISS", decision, action, resource, expect,
                                                  " [context]" if context else ""))
    print("%s: %d of %d allowed; %d of %d met their expectation" % (role, allowed, len(pairs), met, len(pairs)))
    return 0 if met == len(pairs) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
