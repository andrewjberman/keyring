"""SC-e-79 deploy check: the served BD gold lib equals the repo bytes, and it is not the SC-e-76 rollback object.

Read-only. Prints one line:
  E79-SHIPPED ok=<bool> repo=<md5> served=<etag> version=<VersionId> rollback=<etag> control=<MATCH|MISMATCH>
ok is True when the served ETag equals the repo md5 AND differs from the SC-e-76 rollback ETag.
control is the positive control: the repo md5 must differ from the rollback ETag (else the check cannot discriminate).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REPO_FILE = ROOT / "data/black_diamond/scripts/gold/lib/etf_classifier.py"
BUCKET = "opal-data-bd"
KEY = "code/gold/lib/etf_classifier.py"
ROLLBACK_ETAG = "535378b5e0b01891c3cf685faf1ed653"  # SC-e-76 lib, VersionId yPda0uV6nypDdrdFVi.0ZW86Mdxk_cI2


def main() -> int:
    repo = hashlib.md5(REPO_FILE.read_bytes()).hexdigest()
    aws = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    out = subprocess.run([aws, "s3api", "head-object", "--bucket", BUCKET, "--key", KEY, "--output", "json"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        print(f"E79-SHIPPED ok=False error=head-object rc={out.returncode} {out.stderr.strip()[:200]}")
        return 1
    head = json.loads(out.stdout)
    served = head["ETag"].strip('"')
    control = "MATCH" if repo != ROLLBACK_ETAG else "MISMATCH"
    ok = served == repo and served != ROLLBACK_ETAG and control == "MATCH"
    print(f"E79-SHIPPED ok={ok} repo={repo} served={served} version={head.get('VersionId')} "
          f"rollback={ROLLBACK_ETAG} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
