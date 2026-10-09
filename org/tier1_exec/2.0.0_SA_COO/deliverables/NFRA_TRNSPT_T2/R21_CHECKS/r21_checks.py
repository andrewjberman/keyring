"""NFRA_TRNSPT round 21 -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  m21   TR21-m21-AC1  D2-S12: every aws_lambda_function in infra/aws/terraform/transcripts/ has a lambda-source-map.json entry
                      (tf_file in that root, tf_resource matching); every entry for a LIVE function carries artifact_sha256 and a
                      40-hex last_deployed_commit; an entry for a function not yet applied says so in _artifact_note

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root). Local only: no AWS call.
"""
import json
import re
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


if __name__ == "__main__":
    if sys.argv[1:] != ["m21"]:
        print("usage: r21_checks.py m21")
        sys.exit(2)
    ok, why = m21()
    print("R21-M21-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
