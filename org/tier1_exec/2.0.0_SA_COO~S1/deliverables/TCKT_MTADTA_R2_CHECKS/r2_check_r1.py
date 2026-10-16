"""TCKT_MTADTA round 2, cell MD-r-1 checks (the apply and FWD-8's first half). LIVE reads: AWS get/describe/simulate only.
Run from the repo root by the CloudOps seat, after the apply, under the box's own identity (a non-member of the access group).

  python r2_check_r1.py applied  -> R1-APPLIED-OK  (bucket policy, key policy, aliases, group read back as built)
  python r2_check_r1.py refusals -> R1-REFUSALS-OK (the no-MFA box identity is refused on both aliases; the collector role keeps only its own alias)
  python r2_check_r1.py getobject -> R1-GETOBJECT-OK (run after the first clean fire: an admin GetObject on the existing cursor key reads AccessDenied)
  python r2_check_r1.py plan     -> R1-PLAN-OK     (a plan of the trino root after the policy lands exits 0: no lock-out, no drift)
  python r2_check_r1.py mfa      -> R1-MFA-OK      (the group's invoke needs MFA; the group holds Andrew_Berman alone, who has an MFA device)

No object body, secret or event is printed. Only counts, names and error codes.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
BUCKET = "opal-data-trino"
FN = "globgrph-trino-access-lambda"
GROUP = "globgrph-trino-access-group"
ROLE = "globgrph-trino-access-role"
CROLE = "m365-metadata-trino-collector-role"
CURSOR = "m365-metadata/trino/state/subscription_cursor/current/cursor.json"
TF = os.path.join(ROOT, "infra", "aws", "terraform", "trino")


def aws(*args, timeout=90):
    exe = shutil.which("aws") or "aws"
    p = subprocess.run([exe] + list(args) + ["--output", "json"], capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def j(s):
    try:
        return json.loads(s)
    except ValueError:
        return None


def applied():
    bad = []
    rc, out, err = aws("s3api", "get-bucket-policy", "--bucket", BUCKET)
    if rc != 0:
        print("R1-APPLIED-REFUSED no bucket policy (%s)" % err.strip().splitlines()[-1][:120])
        return 1
    pol = json.loads(j(out)["Policy"])
    acts = set()
    admitted = set()
    for st in pol["Statement"]:
        if st.get("Effect") == "Deny":
            a = st.get("Action")
            acts |= set(a if isinstance(a, list) else [a])
            np = (st.get("NotPrincipal") or {}).get("AWS")
            admitted |= set(np if isinstance(np, list) else ([np] if np else []))
    if any("ListBucket" in a for a in acts):
        bad.append("ListBucket is in the bucket Deny")
    if not any("GetObject" in a for a in acts):
        bad.append("GetObject is not denied")
    if len(admitted) != 1 or not next(iter(admitted)).endswith(":role/" + ROLE):
        bad.append("the admitted principal is not the access role alone: %r" % sorted(admitted))
    rc, out, err = aws("s3api", "get-bucket-encryption", "--bucket", BUCKET)
    if rc != 0 or "aws:kms" not in out:
        bad.append("no SSE-KMS default")
    rc, out, err = aws("lambda", "list-aliases", "--function-name", FN)
    names = sorted(a["Name"] for a in (j(out) or {}).get("Aliases", [])) if rc == 0 else []
    if names != ["collector", "member"]:
        bad.append("aliases %r" % names)
    rc, out, err = aws("iam", "get-group", "--group-name", GROUP)
    if rc != 0:
        bad.append("no IAM group")
    rc, out, err = aws("s3api", "get-bucket-location", "--bucket", BUCKET)
    key = None
    rc2, out2, _ = aws("s3api", "get-bucket-encryption", "--bucket", BUCKET)
    if rc2 == 0:
        key = j(out2)["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"].get("KMSMasterKeyID")
    if key:
        rc, out, err = aws("kms", "get-key-policy", "--key-id", key, "--policy-name", "default")
        if rc != 0:
            bad.append("key policy unreadable")
        else:
            kp = json.loads(j(out)["Policy"])
            princ = set()
            for st in kp["Statement"]:
                p = (st.get("Principal") or {}).get("AWS")
                princ |= set(p if isinstance(p, list) else [p])
            users = sorted(x for x in princ if not x.endswith(":root") and not x.endswith(":role/" + ROLE))
            if users:
                bad.append("the key policy admits more than root and the access role: %r" % users)
    if bad:
        print("R1-APPLIED-REFUSED " + "; ".join(bad))
        return 1
    print("R1-APPLIED-OK aliases=%s" % ",".join(names))
    return 0


def refusals():
    bad = []
    probe = os.path.join(tempfile.gettempdir(), "r1_invoke.out")
    for alias in ("member", "collector"):
        rc, out, err = aws("lambda", "invoke", "--function-name", FN, "--qualifier", alias, "--payload", "e30=", probe)
        if rc == 0 or "AccessDenied" not in err:
            bad.append("the box identity (no MFA) invoked the %s alias or was not refused with AccessDenied (rc=%d)" % (alias, rc))
    rc, out, err = aws("iam", "get-role", "--role-name", CROLE)
    if rc != 0:
        bad.append("collector role missing")
        arn = None
    else:
        arn = j(out)["Role"]["Arn"]
    acct = (arn or "arn:aws:iam::313476888478:role/x").split(":")[4]
    fn_arn = "arn:aws:lambda:us-east-1:%s:function:%s" % (acct, FN)
    if arn:
        def sim(action, resource, alias=None):
            args = ["iam", "simulate-principal-policy", "--policy-source-arn", arn, "--action-names", action, "--resource-arns", resource]
            if alias:
                rc, o, e = aws("lambda", "get-policy", "--function-name", FN, "--qualifier", alias)
                if rc == 0:
                    args += ["--resource-policy", json.loads(o)["Policy"],
                             "--context-entries", "ContextKeyName=aws:MultiFactorAuthPresent,ContextKeyValues=false,ContextKeyType=boolean"]
            rc, o, e = aws(*args)
            d = j(o) or {}
            return [r["EvalDecision"] for r in d.get("EvaluationResults", [])]
        if sim("lambda:InvokeFunction", fn_arn + ":collector", "collector") != ["allowed"]:
            bad.append("the collector role cannot invoke its own alias under the MFA-absent Deny (carve-out missing)")
        if sim("lambda:InvokeFunction", fn_arn + ":member") == ["allowed"]:
            bad.append("the collector role can invoke the member alias")
        if sim("s3:GetObject", "arn:aws:s3:::%s/%s" % (BUCKET, CURSOR)) == ["allowed"]:
            bad.append("the collector role can read the bucket directly")
        if sim("kms:Decrypt", "*") == ["allowed"]:
            bad.append("the collector role holds a KMS action")
    if bad:
        print("R1-REFUSALS-REFUSED " + "; ".join(bad))
        return 1
    print("R1-REFUSALS-OK")
    return 0


def getobject():
    """Run after the first clean fire: the cursor exists, so an explicit Deny reads AccessDenied (a missing key reads NoSuchKey)."""
    out_file = os.path.join(tempfile.gettempdir(), "r1_probe.out")
    rc, out, err = aws("s3api", "head-object", "--bucket", BUCKET, "--key", CURSOR)
    if "Not Found" in err or "NoSuchKey" in err or "404" in err:
        print("R1-GETOBJECT-REFUSED the cursor does not exist yet; run after the first clean fire")
        return 1
    rc, out, err = aws("s3api", "get-object", "--bucket", BUCKET, "--key", CURSOR, out_file)
    if rc == 0 or "AccessDenied" not in err:
        print("R1-GETOBJECT-REFUSED an admin GetObject on an existing key was not refused (rc=%d)" % rc)
        return 1
    print("R1-GETOBJECT-OK")
    return 0


def plan():
    if not os.path.isdir(TF):
        print("R1-PLAN-REFUSED no trino root")
        return 1
    p = subprocess.run(["terraform", "plan", "-detailed-exitcode", "-input=false", "-lock=false", "-no-color"], cwd=TF,
                       capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        tail = (p.stdout + p.stderr).strip().splitlines()[-3:]
        print("R1-PLAN-REFUSED exit=%d %s" % (p.returncode, " | ".join(t[:100] for t in tail)))
        return 1
    print("R1-PLAN-OK exit=0")
    return 0


def mfa():
    bad = []
    rc, out, err = aws("iam", "list-group-policies", "--group-name", GROUP)
    names = (j(out) or {}).get("PolicyNames", []) if rc == 0 else []
    if not names:
        print("R1-MFA-REFUSED no group policy (%s)" % (err.strip().splitlines()[-1][:100] if err.strip() else "none listed"))
        return 1
    gated = 0
    for n in names:
        rc, out, err = aws("iam", "get-group-policy", "--group-name", GROUP, "--policy-name", n)
        doc = (j(out) or {}).get("PolicyDocument", {})
        for st in doc.get("Statement", []):
            acts = st.get("Action")
            acts = acts if isinstance(acts, list) else [acts]
            if "lambda:InvokeFunction" in acts and st.get("Effect") == "Allow":
                cond = json.dumps(st.get("Condition", {}))
                if "MultiFactorAuthPresent" in cond and "true" in cond.lower():
                    gated += 1
                else:
                    bad.append("an invoke Allow without the MFA condition")
    if gated < 1:
        bad.append("no invoke Allow carries aws:MultiFactorAuthPresent")
    rc, out, err = aws("iam", "get-group", "--group-name", GROUP)
    members = sorted(u["UserName"] for u in (j(out) or {}).get("Users", [])) if rc == 0 else []
    if members != ["Andrew_Berman"]:
        bad.append("group members %r, ruled: Andrew_Berman alone" % members)
    rc, out, err = aws("iam", "list-mfa-devices", "--user-name", "Andrew_Berman")
    if rc != 0 or not (j(out) or {}).get("MFADevices"):
        bad.append("Andrew_Berman has no MFA device")
    if bad:
        print("R1-MFA-REFUSED " + "; ".join(bad))
        return 1
    print("R1-MFA-OK members=1 mfa_devices>=1")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"applied": applied, "refusals": refusals, "plan": plan, "mfa": mfa, "getobject": getobject}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except Exception as e:  # noqa: BLE001
        print("R1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:160]))
        sys.exit(1)
