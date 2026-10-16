"""SOC2_MSLOGS round 1, cell SM-x-1 checks (the cosmetic scrub of the Ticket Center name). Run from the repo root.

  python s1_check_x1.py scrub -> X1-SCRUB-OK (no TCKT in the listed files; their behaviour is byte-for-byte what it was)

A file passes only if (a) it names TCKT nowhere and (b) its behaviour fingerprint equals the one recorded at the cut:
Python by its AST without docstrings; Terraform by its non-comment lines with the project name TCKT_MTADTA read as
SOC2_MSLOGS (so the two non-comment strings, a tag and a description, must be re-worded to exactly that and no other change).
"""
import os
import sys

ROOT = os.getcwd()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fp_lib  # noqa: E402

FINGERPRINTS = {
    "infra/aws/terraform/trino/main.tf": ("tf", "09635b6c5c7d96c2"),
    "infra/aws/terraform/trino/identity.tf": ("tf", "3f14f9021c25728a"),
    "infra/aws/terraform/trino/collector.tf": ("tf", "4b526a7d08890958"),
    "data/m365_metadata/scripts/app/register_app.py": ("py", "08509d5a7e7562cb"),
}
TEXT_ONLY = ["data/m365_metadata/README.md", "data/m365_metadata/scripts/app/RUNBOOK.md"]


def scrub():
    bad = []
    for rel, (kind, want) in FINGERPRINTS.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            bad.append("missing %s" % rel)
            continue
        t = open(p, encoding="utf-8").read()
        if "TCKT" in t:
            bad.append("%s still mentions TCKT" % rel)
        got = fp_lib.py_fp(t) if kind == "py" else fp_lib.tf_fp(t)
        if got != want:
            bad.append("%s changed behaviour (fingerprint %s, recorded %s)" % (rel, got, want))
    for rel in TEXT_ONLY:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            bad.append("missing %s" % rel)
        elif "TCKT" in open(p, encoding="utf-8").read():
            bad.append("%s still mentions TCKT" % rel)
    if bad:
        print("X1-SCRUB-REFUSED " + "; ".join(bad))
        return 1
    print("X1-SCRUB-OK files=%d" % (len(FINGERPRINTS) + len(TEXT_ONLY)))
    return 0


if __name__ == "__main__":
    sys.exit(scrub() if (sys.argv[1:2] == ["scrub"]) else 2)
