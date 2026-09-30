"""MDPF_SECCLASS round 6 SC-e-14: run both seed scripts with --dry-run against the LIVE table (read only) and
print `SEED-PREREAD seed=<n> excluded_cusip=<n> constituents=<n> excluded_cusip=<n>` parsed from their own output.
Exit 1 (and print each script's tail) if either script's count line is absent or a script exits non-zero."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
YANG = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "yang_pipeline"
SEED_RE = re.compile(r"^PRE-READ: (\d+) existing row\(s\) excluded_cusip=(\d+)", re.M)
CONS_RE = re.compile(r"^EXISTING rows in \S+: (\d+) excluded_cusip=(\d+)", re.M)


def run(script: str):
    p = subprocess.run([sys.executable, script, "--dry-run"], cwd=str(YANG), capture_output=True,
                       text=True, timeout=300)
    return p.returncode, p.stdout + p.stderr


def main() -> int:
    rc1, out1 = run("seed-etf-classifications.py")
    rc2, out2 = run("seed-etf-constituents.py")
    m1, m2 = SEED_RE.search(out1), CONS_RE.search(out2)
    if rc1 or rc2 or not m1 or not m2:
        print("SEED-PREREAD-FAIL rc_seed=%s rc_constituents=%s" % (rc1, rc2))
        print(out1[-800:])
        print(out2[-800:])
        return 1
    print(m1.group(0))
    print(m2.group(0))
    print("SEED-PREREAD seed=%s excluded_cusip=%s constituents=%s excluded_cusip=%s"
          % (m1.group(1), m1.group(2), m2.group(1), m2.group(2)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
