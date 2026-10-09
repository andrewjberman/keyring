"""NFRA_TRNSPT round 21 -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  m21   TR21-m21-AC1  D2-S12: every aws_lambda_function in infra/aws/terraform/transcripts/ has a lambda-source-map.json entry
                      (tf_file in that root, tf_resource matching); every entry for a LIVE function carries artifact_sha256 and a
                      40-hex last_deployed_commit; an entry for a function not yet applied says so in _artifact_note

  r21   TR21-r21-AC1  ADDENDUM 12.1: FWD-5's silver-only reader role in readers.tf (plan-only build): names from NAMES.json, GetObject on
                      silver prefixes only, never bronze, a trust of exactly the raw-tier readers (CTO ruling @374553467d)

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root). Local only: no AWS call.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = "infra/aws/terraform/transcripts/"
MAP = Path("infra/aws/lambda/ci/lambda-source-map.json")


def m21():
    resources = []
    for tf in sorted(Path(ROOT).glob("*.tf")):
        for m in re.finditer(r'^resource\s+"aws_lambda_function"\s+"([A-Za-z0-9_]+)"', tf.read_text(encoding="utf-8"), re.M):
            resources.append((tf.as_posix(), "aws_lambda_function." + m.group(1)))
    if not resources:
        return False, "denominator 0 resources under %s" % ROOT
    fns = json.loads(MAP.read_text(encoding="utf-8")).get("functions", {})
    bad = []
    for tf_file, res in resources:
        hits = [(k, v) for k, v in fns.items() if v.get("tf_file") == tf_file and v.get("tf_resource") == res]
        if len(hits) != 1:
            bad.append("%s %s entries=%d" % (tf_file, res, len(hits)))
            continue
        _, v = hits[0]
        live = bool(v.get("artifact_sha256")) or bool(v.get("last_deployed_commit"))
        if live:
            if not re.fullmatch(r"[0-9a-f]{40}", v.get("last_deployed_commit", "")) or len(v.get("artifact_sha256", "")) != 44:
                bad.append("%s sha/commit malformed" % res)
        elif "not yet applied" not in v.get("_artifact_note", ""):
            bad.append("%s neither live fields nor a not-yet-applied note" % res)
    if bad:
        return False, "; ".join(bad)
    return True, "%d of %d resources mapped" % (len(resources), len(resources))


K21_TEST = Path("data/transcripts/scripts/tests/test_gateway_key_write.py")
K21_NAMES = ["test_gateway_write_statement_shape", "test_gateway_write_scoped_to_s3_and_bucket", "test_no_other_key_statement_changed"]


def k21():
    if not K21_TEST.exists():
        return False, "absent: %s" % K21_TEST.as_posix()
    text = K21_TEST.read_text(encoding="utf-8")
    missing = [n for n in K21_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(K21_TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(K21_NAMES)), tail


R21_TEST = Path("data/transcripts/scripts/tests/test_silver_reader_role.py")
R21_NAMES = ["test_policy_reads_silver_only", "test_no_bronze_prefix_granted", "test_trust_is_the_raw_tier_readers",
            "test_research_meeting_prefix_denied"]


def r21():
    if not R21_TEST.exists():
        return False, "absent: %s" % R21_TEST.as_posix()
    text = R21_TEST.read_text(encoding="utf-8")
    missing = [n for n in R21_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(R21_TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(R21_NAMES)), tail


if __name__ == "__main__":
    fns = {"m21": m21, "r21": r21, "k21": k21}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("usage: r21_checks.py {m21|r21|k21}")
        sys.exit(2)
    ok, why = fns[sys.argv[1]]()
    print("R21-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
