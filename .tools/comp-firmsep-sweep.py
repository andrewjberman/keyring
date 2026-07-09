#!/usr/bin/env python3
"""comp-firmsep-sweep -- prove the universe: who can reach a firm's credentials?

DETECT pillar, leg 2, of the firm-sep-DATA credential-plane program.
  PREVENT = the cross-firm belts (bucket + secret)
  DETECT  = leg 1: a grant-shape lint (cheap; catches what we AUTHOR)
            leg 2: THIS (expensive; catches what we INHERIT)
  VERIFY  = comp-denytest

WHY LEG 2 IS NOT OPTIONAL
-------------------------
On 2026-07-09 the credential belt was scoped by grepping our own Terraform for
`secret:opal/*` wildcards.  That found 4 roles.  The real universe was 6: two more
reached the BD firm's credentials through the **AWS-managed `SecretsManagerReadWrite`**
policy (`secretsmanager:*` on `Resource: "*"`).

That policy is not in our Terraform.  No grep of our repo can ever find it.  A
grant-shape enumeration produced a complete-LOOKING universe that was 60% of the real
one, and the remediation shipped against it.

So: **enumerate by simulating the actual secret against every principal**, never by the
shape of the grant.  A filter silently passes what is outside it.

WHAT IT ASSERTS
---------------
  * every role in the account is simulated (rows == roles; duplicates are a bug)
  * a blank/errored verdict is NEVER a pass -- it is a failure to have checked
  * only the firm's own declared roles may be `allowed`
  * optionally the WRITE reach too (`PutSecretValue`), which is how you find a role that
    cannot read a secret but can OVERWRITE it -- the hole a read-only sweep misses

SHELL COUNTERS ARE BANNED HERE, ON PURPOSE
------------------------------------------
The first version of this sweep was a shell loop that did
`echo $allowed | grep -vc bd-exporter`.  On an EMPTY allowed-set that feeds `grep` a
blank line, which counts as **1** -- reporting "1 non-firm role still allowed" when the
truth was zero.  `grep -vc` also exits non-zero on a 0 count, firing a `|| echo 0`
fallback.  A cosmetic-looking counter that INVERTS a security verdict.
Counting happens in python, against asserted row counts.  A verdict from a counter you do
not trust is not a verdict.

USAGE
-----
  comp-firmsep-sweep --secret opal/bd/credentials --owner bd-exporter-ec2-role
  comp-firmsep-sweep --secret blackdiamond/cot/session --owner cot-exporter-ec2-role --write
  comp-firmsep-sweep --secret orion/credentials --owner inf-exporter-ec2-role --json report.json

Exit 0 = the universe is closed.  Exit 1 = a non-owner can reach it, or the sweep was
incomplete (which is the same thing: you did not prove closure).
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

AWS = shutil.which("aws") or shutil.which("aws.cmd")
if not AWS:
    sys.exit("comp-firmsep-sweep: cannot locate the `aws` executable on PATH.")

READ = "secretsmanager:GetSecretValue"
WRITE = "secretsmanager:PutSecretValue"


def _aws(*args: str) -> tuple[int, str, str]:
    p = subprocess.run([AWS, *args], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    return p.returncode, p.stdout.replace("\r", "").strip(), p.stderr.strip()


def all_roles() -> list[str]:
    rc, out, err = _aws("iam", "list-roles", "--max-items", "1000",
                        "--query", "Roles[].RoleName", "--output", "text")
    if rc != 0:
        sys.exit(f"comp-firmsep-sweep: list-roles failed: {err[:160]}")
    names = sorted({n for n in out.replace("\t", "\n").split("\n") if n.strip()})
    if not names:
        sys.exit("comp-firmsep-sweep: list-roles returned nothing. An empty universe is not a clean sweep.")
    return names


def secret_arn(name: str) -> str:
    rc, out, err = _aws("secretsmanager", "describe-secret", "--secret-id", name,
                        "--query", "ARN", "--output", "text")
    if rc != 0 or not out:
        sys.exit(f"comp-firmsep-sweep: cannot resolve secret {name!r}: {err[:160]}")
    return out


def simulate(account: str, role: str, arn: str, action: str) -> str:
    """One principal, ONE resource, one action. Multi-ARN batching returns false verdicts."""
    rc, out, err = _aws("iam", "simulate-principal-policy",
                        "--policy-source-arn", f"arn:aws:iam::{account}:role/{role}",
                        "--action-names", action,
                        "--resource-arns", arn,
                        "--query", "EvaluationResults[].EvalDecision", "--output", "text")
    if rc != 0 or not out:
        # NOT a pass. Not having checked is a failure to prove closure.
        return f"NO_VERDICT({err[:60] or 'empty'})"
    return out


def main() -> int:
    p = argparse.ArgumentParser(prog="comp-firmsep-sweep")
    p.add_argument("--secret", required=True, help="the firm credential to prove closure on")
    p.add_argument("--owner", action="append", default=[],
                   help="repeatable; role(s) legitimately permitted (the firm's own). Anything else is a finding.")
    p.add_argument("--write", action="store_true",
                   help="also sweep PutSecretValue -- finds roles that cannot READ it but can OVERWRITE it")
    p.add_argument("--write-only", action="store_true",
                   help="sweep PutSecretValue ONLY (half the API calls). Use when the READ universe is already "
                        "proven closed and you are isolating the WRITE dimension -- a role can be explicitDeny "
                        "on read and still overwrite the secret.")
    p.add_argument("--account", default="313476888478")
    p.add_argument("--json", metavar="PATH", help="write the full per-role verdict table")
    a = p.parse_args()

    arn = secret_arn(a.secret)
    roles = all_roles()
    owners = set(a.owner)
    if a.write_only:
        actions = [WRITE]
    else:
        actions = [READ] + ([WRITE] if a.write else [])
    print(f"secret : {a.secret}\n         {arn}")
    print(f"roles  : {len(roles)} in account   owners: {sorted(owners) or 'NONE DECLARED'}")
    print(f"actions: {actions}\n")

    table: dict[str, dict[str, str]] = {}
    for i, r in enumerate(roles, 1):
        table[r] = {act: simulate(a.account, r, arn, act) for act in actions}
        if i % 40 == 0:
            print(f"  ... {i}/{len(roles)}")

    # Assert the sweep is COMPLETE before believing any conclusion from it.
    assert len(table) == len(roles), f"swept {len(table)} of {len(roles)} roles -- a partial sweep proves nothing"

    failures: list[str] = []
    for act in actions:
        blanks = sorted(r for r, v in table.items() if v[act].startswith("NO_VERDICT"))
        allowed = sorted(r for r, v in table.items() if v[act] == "allowed")
        trespass = sorted(set(allowed) - owners)
        print(f"=== {act}")
        print(f"  simulated : {len(table)}/{len(roles)}")
        print(f"  no-verdict: {len(blanks)} {blanks or ''}   (a blank is never a pass)")
        print(f"  allowed   : {allowed or 'NONE'}")
        print(f"  NON-OWNER : {trespass or 'NONE'}   <- must be empty\n")
        if blanks:
            failures.append(f"{act}: {len(blanks)} role(s) returned no verdict -- closure NOT proven")
        if trespass:
            failures.append(f"{act}: non-owner roles can reach {a.secret}: {trespass}")

    if a.json:
        with open(a.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"secret": a.secret, "arn": arn, "owners": sorted(owners),
                       "roles_swept": len(table), "verdicts": table}, fh, indent=1)
        print(f"  full verdict table -> {a.json}\n")

    if failures:
        print("RESULT: FAIL")
        for f in failures:
            print(f"  !! {f}")
        print("\n  NOTE: a WRITE trespass with no READ trespass still means a foreign role can OVERWRITE this")
        print("  firm's credential. A read-only sweep would have called that clean.")
        return 1
    print(f"RESULT: PASS -- universe closed on {a.secret}: only its owner(s) can reach it.")
    print("  NOTE: this proves CAPABILITY as IAM evaluates it today. It says nothing about whether a")
    print("  consumer would fail loud or silent if a grant were later removed -- see comp-denytest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
