#!/usr/bin/env python3
"""NFRA_INFRPT.P1 increment-2b -- drift producer.

Runs the repo/infra drift checks the opal-infrastructure-monitor Lambda CANNOT run in-AWS
(comp-* CLIs + `terraform plan`) and writes per-leg drift_state to S3 for the Lambda to
render. Two legs, two S3 keys (no read-merge-write race between the GH-Action push leg and
the EventBridge->CodeBuild nightly leg):

  --mode comp       (GH-Action push, CLOUD): comp-manifest-check check + comp-surface-check
                    scan  -> s3://opal-data-portal-v2/infrastructure/drift_state_comp.json
  --mode terraform  (CodeBuild nightly):     terraform plan across modules (-lock=false,
                    read-only) -> s3://.../infrastructure/drift_state_tf.json (+ source_zip_age)

NO-SECRET-ECHO (CTO security cond 1): drift_state lands in the SERVED opal-data-portal-v2
bucket. Findings carry resource IDENTITY + drift STATUS + a NON-sensitive reason/pointer ONLY
-- NEVER a plan/state-surfaced value (no secret/key/password/ARN-embedded-secret). The
terraform leg reads `terraform show -json` change ADDRESSES + ACTIONS only, never `.after`/
`.before` attribute values.

2-IN-TF-LAMBDAS CAVEAT (CTO): infrastructure-daily-snapshot + opal-infrastructure-monitor are
legitimately TF-managed now -- the manifest/terraform legs must NOT flag them as drift.

Plain ASCII, no emoji (runs in CodeBuild/GH-Action logs).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

DRIFT_BUCKET = "opal-data-portal-v2"
DRIFT_PREFIX = "infrastructure/"
TF_ROOT = "infra/aws/terraform"
# Legitimately-in-TF now -- never flag as drift (the WAS-orphan-NOW-in-TF case).
TF_ONBOARDED_ALLOWLIST = {"infrastructure-daily-snapshot", "opal-infrastructure-monitor"}
# Modules to skip in the terraform leg (non-deployable scaffolding / decom holding).
TF_MODULE_SKIP = {"modules", "_decom-snapshots"}

# GATED (CTO floor-semantics ruling 202255Z): cannot-assess because the deploy is in a KNOWN
# in-flight gated state (committed-before-apply, artifact uploads at apply) -- transient, not a gap.
# EXPLICIT allowlist = operator-vouched grounding (never inferred). Remove an entry when its gate
# clears (re-includes it in the floor). A gated-allowlisted module whose error is NOT the expected
# missing-artifact falls through to ERROR (fail-toward-gap; a NEW error cannot hide behind the gate).
GATED_ALLOWLIST = {
    "bd-pipeline": "SS4c TIER-1 canary apply gated on RAVC1 chain (0.6.0_AE; gldinc-ss4c-canary.zip uploads at apply)",
}

# DENY-BLOCKED grounding (CTO Guard 2): a cannot-assess counts as deny-blocked ONLY when the error
# is an ACTUAL AccessDenied for a Deny'd action (drift-producer.tf least-priv Denies) -- never
# inferred. A denial we cannot attribute to a Deny'd action = ERROR (a missing Allow / real perm gap).
_DENY_GROUND = [
    ("secretsmanager:getsecretvalue", "secretsmanager:GetSecretValue (module reads a secret VERSION at plan time)"),
    ("ssm:getparameter", "ssm:GetParameter (account param)"),
    ("kms:decrypt", "kms:Decrypt"),
    ("dynamodb:getitem", "dynamodb:GetItem (item read at plan time)"),
    ("dynamodb:batchgetitem", "dynamodb:BatchGetItem (item read at plan time)"),
    ("dynamodb:query", "dynamodb:Query (item read at plan time)"),
    ("dynamodb:scan", "dynamodb:Scan (item read at plan time)"),
]
_MISSING_ARTIFACT = re.compile(r"couldn't find resource|reading s3 bucket.*object", re.I)


def _classify_cannot_assess(name: str, err: str):
    """(cls, cause): classify a cannot-assess by CAUSE, grounded on the actual error text.
    deny-blocked = the least-priv Deny correctly refused a secret/firm-data read (EXCLUDED from the
    floor); gated = a known in-flight gated deploy (EXCLUDED-but-tracked); error = a real gap (floor
    RED). Fails TOWARD error: anything not POSITIVELY grounded as deny-blocked/gated = error, so a
    real gap can never masquerade as excused (CTO Guard 2)."""
    low = err.lower()
    denied = "accessdenied" in low or "explicit deny" in low or "not authorized to perform" in low
    if denied:
        for needle, cause in _DENY_GROUND:
            if needle in low:
                return "deny-blocked", cause
        # firm-data S3: my Deny blocks s3:GetObject ONLY on opal-data-*/* -> a denied s3:GetObject is
        # necessarily the firm-data Deny (ReadOnly allows GetObject elsewhere).
        if "s3:getobject" in low or ("opal-data-" in low and ("reading s3" in low or "headobject" in low)):
            return "deny-blocked", "s3:GetObject on opal-data-* (firm-data read at plan time)"
        return "error", "AccessDenied on a non-Deny'd action (missing Allow / real perm gap -- add the read perm)"
    # S3 HeadObject 403: S3 returns a BODYLESS 403 'Forbidden' for HeadObject -> the SDK error names
    # NO action (unlike GetObject's detailed AccessDenied), so the action-grounded branch above misses
    # it. The drift role's ONLY S3-read Deny is firm-data (opal-data-*/*) and ReadOnly allows
    # s3:GetObject everywhere else -> a 403 on an S3 read is NECESSARILY that firm-data Deny (grounded
    # on the role's policy STRUCTURE, not a loose inference). data.aws_s3_object reads do HeadObject.
    if ("statuscode: 403" in low or "api error forbidden" in low or "403 forbidden" in low) and \
            ("headobject" in low or "getobject" in low or "reading s3 object" in low):
        return "deny-blocked", "s3 403 on read (firm-data Deny; HeadObject masks the action -- role's only S3-read Deny is opal-data-*/*)"
    if name in GATED_ALLOWLIST and _MISSING_ARTIFACT.search(err):
        return "gated", GATED_ALLOWLIST[name]
    return "error", err.strip()[:140]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _run(cmd, cwd=None, timeout=600):
    """Run a command, capture (rc, stdout, stderr). Never raises on non-zero."""
    try:
        p = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, shell=False
        )
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s"
    except Exception as e:  # noqa: BLE001 -- producer must never crash a leg
        return 125, "", str(e)[:200]


def _put_s3(key: str, body: dict) -> None:
    """Write a drift_state leg to S3. Uses boto3 if present, else the aws CLI."""
    payload = json.dumps(body, indent=2, default=str)
    full_key = DRIFT_PREFIX + key
    try:
        import boto3  # type: ignore

        boto3.client("s3").put_object(
            Bucket=DRIFT_BUCKET, Key=full_key, Body=payload.encode("utf-8"),
            ContentType="application/json",
        )
    except Exception:
        tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), key)
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(payload)
        rc, _, err = _run(["aws", "s3", "cp", tmp, f"s3://{DRIFT_BUCKET}/{full_key}",
                           "--content-type", "application/json"])
        if rc != 0:
            raise RuntimeError(f"s3 put failed for {full_key}: {err[:200]}")
    print(f"OK: wrote s3://{DRIFT_BUCKET}/{full_key} ({len(payload)} bytes)")


def _git_head() -> str:
    rc, out, _ = _run(["git", "rev-parse", "HEAD"])
    return out.strip()[:12] if rc == 0 else "unknown"


# =============================================================================
# COMP leg -- comp-manifest-check + comp-surface-check (repo/code-surface drift)
# =============================================================================

_SURFACE_RE = re.compile(r"(SEV\d)\b.*?\bCHANGED\b\s+(.*)")


def run_comp_leg() -> dict:
    findings = []
    tools_run = 0
    tools_failed = 0

    # comp-manifest-check check -- non-canonical graph-access drift (advisory). Output lines
    # (when present) name the offending file; clean = no output. Identity-only -> no-secret-safe.
    rc, out, err = _run(["bash", ".tools/comp-manifest-check", "check"])
    tools_run += 1
    if rc != 0:
        # could-not-assess: NEVER silent-clean -- a tool that can't RUN is a VISIBLE gap.
        tools_failed += 1
        findings.append({
            "source": "manifest", "status": "watch",
            "reason": f"comp-manifest-check could not run (cannot assess): rc={rc} {err.strip()[:120]}",
            "pointer": "org/modules/graph/graph-call-manifest.yaml",
        })
    else:
        for line in out.splitlines():
            s = line.strip()
            if not s or s.startswith("comp-manifest-check"):
                continue
            if any(a in s for a in TF_ONBOARDED_ALLOWLIST):
                continue
            findings.append({
                "source": "manifest", "status": "watch",
                "reason": f"non-canonical graph-access pattern (advisory): {s[:160]}",
                "pointer": "org/modules/graph/graph-call-manifest.yaml",
            })

    # comp-surface-check scan -- critical-surface drift (SEV1/SEV2 CHANGED). Identity-only.
    # NB: scan reads the .comp-graph baseline; if absent (fresh CI checkout -- .comp-graph is
    # gitignored) it exits rc=0 but NO-OPS (0 findings). rc=0 != actually-assessed -> a no-op scan
    # MUST NOT read clean (the false-clean class we kill). Require a loaded baseline (>0 nodes);
    # else could-not-assess WATCH (VISIBLE, not a silent 0-findings clean).
    rc, out, err = _run(["bash", ".tools/comp-surface-check", "scan"])
    tools_run += 1
    baseline_ok = bool(re.search(r"baseline:.*\(\s*([1-9]\d*)\s*nodes?\)", out))
    if rc != 0:
        tools_failed += 1
        findings.append({
            "source": "surface", "status": "watch",
            "reason": f"comp-surface-check could not run (cannot assess): rc={rc} {err.strip()[:120]}",
            "pointer": "org/modules/graph/critical-surfaces.yaml",
        })
    elif not baseline_ok:
        tools_failed += 1
        findings.append({
            "source": "surface", "status": "watch",
            "reason": "comp-surface-check scan loaded NO baseline (.comp-graph absent in CI?) -> NO-OP; cannot assess critical-surface drift (no silent-clean)",
            "pointer": "org/modules/graph/critical-surfaces.yaml",
        })
    else:
        for line in out.splitlines():
            m = _SURFACE_RE.search(line)
            if not m:
                continue
            sev, what = m.group(1), m.group(2).strip()
            if any(a in what for a in TF_ONBOARDED_ALLOWLIST):
                continue
            # SEV1 critical-surface change = RED-tier; SEV2 = WATCH. (The Lambda applies the
            # state-change-since-last-report filter; here we report the current scan.)
            findings.append({
                "source": "surface", "status": "red" if sev == "SEV1" else "watch",
                "reason": f"{sev} critical-surface CHANGED: {what[:200]}",
                "pointer": "org/modules/graph/critical-surfaces.yaml",
            })

    return {
        "leg": "comp",
        "generated_at": _now(),
        "source_commit": _git_head(),
        "tools_run": tools_run,
        "tools_failed": tools_failed,
        "findings": findings,
        "note": None if findings else f"no comp drift ({tools_run} tools ran clean)",
    }


# =============================================================================
# TERRAFORM leg -- `terraform plan` across modules (real infra drift, out-of-band)
# =============================================================================

def _module_dirs() -> list:
    base = TF_ROOT
    out = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        d = os.path.join(base, name)
        if not os.path.isdir(d) or name in TF_MODULE_SKIP:
            continue
        if any(f.endswith(".tf") for f in os.listdir(d)):
            out.append((name, d))
    return out


def _plan_module(name: str, d: str, terraform: str):
    """init + plan -detailed-exitcode -lock=false (READ-ONLY).
    Returns (assessed: bool, finding: dict|None). assessed=False means init/plan could not
    run (systemic-blind input -- feeds the leg-level coverage guard); assessed=True means the
    module was actually evaluated (clean OR drift)."""
    rc, _, err = _run([terraform, f"-chdir={d}", "init", "-input=false", "-no-color",
                       "-lock=false", "-upgrade=false"], timeout=600)
    if rc != 0:
        cls, cause = _classify_cannot_assess(name, err)
        return False, {"source": "terraform", "module": name, "status": "watch", "class": cls,
                       "cause": cause,
                       "reason": f"terraform init failed [{cls}]: {cause}",
                       "pointer": f"{TF_ROOT}/{name}/"}
    rc, _, err = _run([terraform, f"-chdir={d}", "plan", "-input=false", "-no-color",
                       "-lock=false", "-detailed-exitcode", "-out=/tmp/tfplan.bin"], timeout=900)
    if rc == 0:
        return True, None  # assessed, no drift
    if rc == 1:
        cls, cause = _classify_cannot_assess(name, err)
        return False, {"source": "terraform", "module": name, "status": "watch", "class": cls,
                       "cause": cause,
                       "reason": f"terraform plan cannot-assess [{cls}]: {cause}",
                       "pointer": f"{TF_ROOT}/{name}/"}
    # rc == 2 -> assessed + drift. Read addresses + actions ONLY (no-secret-echo: never values).
    addrs = []
    sc, sout, _ = _run([terraform, f"-chdir={d}", "show", "-json", "/tmp/tfplan.bin"], timeout=120)
    if sc == 0:
        try:
            plan = json.loads(sout)
            for ch in plan.get("resource_changes", []):
                chg = ch.get("change", {})
                acts = [a for a in chg.get("actions", []) if a != "no-op"]
                if not acts:
                    continue
                addr = ch.get("address", "?")
                if any(a in addr for a in TF_ONBOARDED_ALLOWLIST):
                    continue  # the 2-in-TF Lambdas caveat
                # Suppress benign aws_lambda_function s3_object_version churn: when an artifact is
                # re-uploaded with IDENTICAL content (build-and-upload makes a new S3 version even
                # for byte-identical code), terraform sees a version-id diff but source_code_hash is
                # UNCHANGED -> the deployed code == the artifact (the deploy-drift sha-check confirms
                # current). That is cosmetic version-pointer churn, not a real config-drift -> skip.
                if ch.get("type") == "aws_lambda_function" and acts == ["update"]:
                    before = chg.get("before") or {}
                    after = chg.get("after") or {}
                    bsh = before.get("source_code_hash")
                    if bsh and bsh == after.get("source_code_hash"):
                        continue  # identical code -> benign s3_object_version churn
                addrs.append(f"{addr} [{'/'.join(acts)}]")
        except Exception:
            addrs = ["<plan parse failed -- drift present, detail unavailable>"]
    if not addrs:
        return True, None  # assessed; only allowlisted/no-op changes
    return True, {"source": "terraform", "module": name, "status": "red",
                  "reason": f"infra drift -- {len(addrs)} resource(s) differ from code: " + "; ".join(addrs[:12]),
                  "pointer": f"{TF_ROOT}/{name}/"}


def run_terraform_leg() -> dict:
    terraform = os.environ.get("TERRAFORM_BIN", "terraform")
    findings = []
    checked = 0
    assessed = 0
    for name, d in _module_dirs():
        checked += 1
        was_assessed, f = _plan_module(name, d, terraform)
        if was_assessed:
            assessed += 1
        if f:
            findings.append(f)
    # source_zip_age: how stale is the build source (the globgrph footgun guard). The build env
    # exports DRIFT_SOURCE_ZIP_MTIME (epoch seconds of the S3 source zip) when built from S3.
    src_mtime = os.environ.get("DRIFT_SOURCE_ZIP_MTIME")
    src_age_h = None
    if src_mtime:
        try:
            src_age_h = round((datetime.now(timezone.utc).timestamp() - float(src_mtime)) / 3600, 1)
        except ValueError:
            src_age_h = None
    # Cause-classification of cannot-assess (CTO floor-semantics ruling). assessable = checked minus
    # the EXCLUDED-from-floor classes (deny-blocked-by-design + gated-transient). The Lambda floor
    # reads RED on ERROR-class >=1 OR assessable-coverage < 0.8; deny-blocked/gated are honest +
    # ENUMERATED (never silently dropped) but excused. assessed/deny/gated/error sum to checked.
    deny_blocked = sum(1 for f in findings if f.get("class") == "deny-blocked")
    gated = sum(1 for f in findings if f.get("class") == "gated")
    errored = sum(1 for f in findings if f.get("class") == "error")
    assessable = checked - deny_blocked - gated
    return {
        "leg": "terraform",
        "generated_at": _now(),
        "terraform_checked_at": _now(),
        "source_commit": _git_head(),
        "source_zip_age_hours": src_age_h,
        "modules_checked": checked,
        "modules_assessed": assessed,
        "modules_assessable": assessable,
        "modules_deny_blocked": deny_blocked,
        "modules_gated": gated,
        "modules_error": errored,
        "findings": findings,
        "note": None if findings else f"no terraform drift across {assessed}/{checked} assessed module(s)",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="NFRA_INFRPT.P1 inc-2b drift producer")
    ap.add_argument("--mode", required=True, choices=["comp", "terraform"])
    args = ap.parse_args()
    if args.mode == "comp":
        _put_s3("drift_state_comp.json", run_comp_leg())
    else:
        _put_s3("drift_state_tf.json", run_terraform_leg())
    return 0


if __name__ == "__main__":
    sys.exit(main())
