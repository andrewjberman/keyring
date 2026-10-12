"""NFRA_TRNSPT round 23 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  tt23  TR23-tt23-AC1  read_refused is in pull.totals and the PULL-DRY line; test_eod_voice.py collects; the pull's suites stay green
  tv23  TR23-tv23-AC1  LIVE read-only: a TRACKED readers.auto.tfvars holds exactly the second-reader role's live trust principals;
                       the variable keeps no default; the header no longer says the readers are not applied
  cl23  TR23-cl23-AC1  the drafter's prompt carries only closed-list values: five named tests pass with the commentary suites
  ca23  TR23-ca23-AC1  LIVE read-only: the three functions run ONE digest, the built dist zip's, and not the pre-act zip
  sw23  TR23-sw23-AC1  the drafter posts its draft to the request's ticket and leaves a census: six named tests pass with every commentary test file
  sa23  TR23-sa23-AC1  LIVE read-only: three functions on ONE digest (the built zip's, not the pre-act zip) and the drafter's
                       ticket base is the front door
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


CL_FILE = TESTS / "test_commentary_drafter.py"
CL_NAMES = ["test_account_type_off_list_is_not_sent", "test_account_type_on_list_is_sent",
            "test_category_off_list_is_dropped_and_counted", "test_themes_are_never_sent",
            "test_allowed_sets_come_from_the_estate"]
CL_SUITE = [CL_FILE, TESTS / "test_commentary_seam.py", TESTS / "test_commentary_entry.py"]


def cl23():
    if not CL_FILE.exists():
        return False, "absent: %s" % CL_FILE.as_posix()
    text = CL_FILE.read_text(encoding="utf-8")
    missing = [n for n in CL_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    rc, passed, tail = _pytest(CL_SUITE)
    return (rc == 0 and passed >= len(CL_NAMES)), tail


SW_FILE = TESTS / "test_commentary_route_switch.py"
SW_NAMES = ["test_persist_answer_carries_ticket_id_when_the_store_names_one",
            "test_post_goes_to_the_named_ticket_with_exactly_two_body_keys", "test_no_ticket_id_means_no_post",
            "test_refused_post_is_logged_and_not_handed_back_to_the_queue", "test_replay_of_a_stored_draft_posts_nothing",
            "test_census_counts_unposted_drafts"]


def sw23():
    if not SW_FILE.exists():
        return False, "absent: %s" % SW_FILE.as_posix()
    text = SW_FILE.read_text(encoding="utf-8")
    missing = [n for n in SW_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    suite = sorted(TESTS.glob("test_commentary_*.py"))
    rc, passed, tail = _pytest(suite)
    return (rc == 0 and passed >= len(SW_NAMES)), "%s (%d commentary test files)" % (tail, len(suite))


def mp23():
    import boto3

    lam = boto3.client("lambda", region_name="us-east-1")
    shas = {f: lam.get_function_configuration(FunctionName=f)["CodeSha256"] for f in (PULL_FN, MAIL_FN, COMMENTARY_FN)}
    facts = " ".join("%s=%s" % (f.split("-")[0] + "-" + f.split("-")[2], s[:8]) for f, s in shas.items())
    if len(set(shas.values())) != 1:
        return False, "%d distinct digests across 3 functions; %s" % (len(set(shas.values())), facts)
    return True, "one digest across 3 functions; " + facts


PRE_CA23_SHA = "AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I="
DIST_ZIP = Path("infra/aws/lambda/transcripts-pull/dist/transcripts-pull.zip")


def ca23():
    """Live read-only: all three functions run ONE digest, it is the built dist zip's, and it is not the pre-act zip."""
    import base64
    import hashlib

    import boto3

    if not DIST_ZIP.exists():
        return False, "absent: %s" % DIST_ZIP.as_posix()
    local = base64.b64encode(hashlib.sha256(DIST_ZIP.read_bytes()).digest()).decode()
    lam = boto3.client("lambda", region_name="us-east-1")
    shas = {f: lam.get_function_configuration(FunctionName=f)["CodeSha256"] for f in (PULL_FN, MAIL_FN, COMMENTARY_FN)}
    facts = "digests=%d live=%s local_zip=%s" % (len(set(shas.values())), sorted({s[:8] for s in shas.values()}), local[:8])
    if set(shas.values()) == {PRE_CA23_SHA}:
        return False, "the functions still run the pre-act zip; " + facts
    if len(set(shas.values())) != 1:
        return False, "the three functions are not on one digest; " + facts
    if next(iter(shas.values())) != local:
        return False, "the live digest is not the local dist zip's; " + facts
    return True, facts


PRE_SA23_SHA = "auyn4IvltKLLl6yw+SsMWGi3VVlYZKnmJKFssjJaVNY="
RUNNER_CONFIG = Path("integrations/ticketing/intake/runner_config.json")


def sa23():
    """Live read-only: three functions on ONE digest, the built dist zip's, not the pre-act zip; the commentary function's
    ticket base is the front door named by the ticketing intake's own config."""
    import base64
    import hashlib
    import json

    import boto3

    if not DIST_ZIP.exists():
        return False, "absent: %s" % DIST_ZIP.as_posix()
    local = base64.b64encode(hashlib.sha256(DIST_ZIP.read_bytes()).digest()).decode()
    front = json.loads(RUNNER_CONFIG.read_text(encoding="utf-8"))["portal_base"]
    lam = boto3.client("lambda", region_name="us-east-1")
    cfg = {f: lam.get_function_configuration(FunctionName=f) for f in (PULL_FN, MAIL_FN, COMMENTARY_FN)}
    shas = {f: c["CodeSha256"] for f, c in cfg.items()}
    base = cfg[COMMENTARY_FN].get("Environment", {}).get("Variables", {}).get("TICKET_API_BASE")
    facts = "digests=%d live=%s local_zip=%s base_is_front_door=%s" % (
        len(set(shas.values())), sorted({s[:8] for s in shas.values()}), local[:8], base == front)
    if PRE_SA23_SHA in shas.values():
        return False, "a function still runs the pre-act zip; " + facts
    if len(set(shas.values())) != 1:
        return False, "the three functions are not on one digest; " + facts
    if next(iter(shas.values())) != local:
        return False, "the live digest is not the local dist zip's; " + facts
    if base != front:
        return False, "the commentary function's ticket base is not the front door; " + facts
    return True, facts


if __name__ == "__main__":
    fns = {"tt23": tt23, "tv23": tv23, "mp23": mp23, "cl23": cl23, "ca23": ca23, "sw23": sw23, "sa23": sa23}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("usage: r23_checks.py {tt23|tv23|mp23|cl23|ca23|sw23|sa23}")
        sys.exit(2)
    ok, why = fns[sys.argv[1]]()
    print("R23-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
