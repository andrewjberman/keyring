"""NFRA_TRNSPT round 23 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  tt23  TR23-tt23-AC1  read_refused is in pull.totals and the PULL-DRY line; test_eod_voice.py collects; the pull's suites stay green
  tv23  TR23-tv23-AC1  LIVE read-only: a TRACKED readers.auto.tfvars holds exactly the second-reader role's live trust principals;
                       the variable keeps no default; the header no longer says the readers are not applied
  mp23  TR23-mp23-AC1  LIVE read-only: all three functions of the transcripts root read ONE CodeSha256, the Teams pull's

Prints R23-<TOKEN>-OK or R23-<TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
PULL_SUITE = [TESTS / "test_teams_pull.py", TESTS / "test_pull_handler.py", TESTS / "test_pull_read_refused.py",
              TESTS / "test_monday_skip_replay.py", TESTS / "test_eod_voice.py"]
TT_NAMES = ["test_totals_carry_read_refused", "test_dry_line_prints_read_refused"]
TT_FILE = TESTS / "test_pull_read_refused.py"

ROOT_TF = Path("infra/aws/terraform/transcripts")
TFVARS = ROOT_TF / "readers.auto.tfvars"
READERS = ROOT_TF / "readers.tf"
SECOND_READER_ROLE = "teams-global-transcripts-second-reader-role"

PULL_FN = "teams-global-transcripts-pull-lambda"
MAIL_FN = "outlook-global-transcripts-pull-lambda"
COMMENTARY_FN = "outlook-global-commentary-draft-lambda"
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _pytest(paths):
    r = subprocess.run([sys.executable, "-m", "pytest"] + [str(p) for p in paths] + ["-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=300)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    return r.returncode, (int(m.group(1)) if m else 0), tail


def tt23():
    if not TT_FILE.exists():
        return False, "absent: %s" % TT_FILE.as_posix()
    text = TT_FILE.read_text(encoding="utf-8")
    missing = [n for n in TT_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    rc, passed, tail = _pytest(PULL_SUITE)
    return (rc == 0 and passed >= len(TT_NAMES)), tail


def tv23():
    import boto3

    if not TFVARS.exists():
        return False, "absent: %s" % TFVARS.as_posix()
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", TFVARS.as_posix()], capture_output=True, text=True)
    if tracked.returncode != 0:
        return False, "not tracked by git: %s" % TFVARS.as_posix()
    text = TFVARS.read_text(encoding="utf-8")
    m = re.search(r"second_reader_trust_principal_arns\s*=\s*\[(.*?)\]", text, re.S)
    if not m:
        return False, "no second_reader_trust_principal_arns list in the tfvars"
    declared = sorted(re.findall(r'"([^"]+)"', m.group(1)))
    doc = boto3.client("iam").get_role(RoleName=SECOND_READER_ROLE)["Role"]["AssumeRolePolicyDocument"]
    live = []
    for st in doc["Statement"]:
        p = st.get("Principal", {}).get("AWS", [])
        live += [p] if isinstance(p, str) else list(p)
    live = sorted(live)
    facts = "declared=%d live=%d" % (len(declared), len(live))
    if declared != live:
        return False, "the tfvars value is not the role's live trust; " + facts
    rtext = READERS.read_text(encoding="utf-8")
    block = re.search(r'variable\s+"second_reader_trust_principal_arns"\s*\{(.*?)\n\}', rtext, re.S)
    if not block:
        return False, "the variable block is gone from readers.tf"
    if re.search(r"^\s*default\s*=", block.group(1), re.M):
        return False, "the variable has a default in readers.tf"
    if "NOT APPLIED -- plan only" in rtext:
        return False, "readers.tf's header still says NOT APPLIED -- plan only"
    return True, facts + " equal; no default; header states the applied state"


def mp23():
    import boto3

    lam = boto3.client("lambda", region_name="us-east-1")
    shas = {f: lam.get_function_configuration(FunctionName=f)["CodeSha256"] for f in (PULL_FN, MAIL_FN, COMMENTARY_FN)}
    facts = " ".join("%s=%s" % (f.split("-")[0] + "-" + f.split("-")[2], s[:8]) for f, s in shas.items())
    if len(set(shas.values())) != 1:
        return False, "%d distinct digests across 3 functions; %s" % (len(set(shas.values())), facts)
    return True, "one digest across 3 functions; " + facts


if __name__ == "__main__":
    fns = {"tt23": tt23, "tv23": tv23, "mp23": mp23}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("usage: r23_checks.py {tt23|tv23|mp23}")
        sys.exit(2)
    ok, why = fns[sys.argv[1]]()
    print("R23-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
