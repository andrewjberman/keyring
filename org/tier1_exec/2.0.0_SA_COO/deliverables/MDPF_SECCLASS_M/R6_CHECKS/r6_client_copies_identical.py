"""MDPF_SECCLASS round 6 SC-e-14: the one ETF classifications client and its two copies stay byte-identical.
Prints `COPIES-IDENTICAL 3 of 3 <sha>` when all match, else each path's hash (exit 1)."""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
V = "infra/aws/lambda/v2_portal"
PATHS = [
    V + "/_shared/etf_classifications_dynamodb.py",
    V + "/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py",
    V + "/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py",
]


def main() -> int:
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in PATHS}
    if len(set(hashes.values())) == 1:
        print("COPIES-IDENTICAL %d of %d %s" % (len(PATHS), len(PATHS), next(iter(hashes.values()))))
        return 0
    for p, h in hashes.items():
        print("%s  %s" % (h, p))
    print("COPIES-DIFFER")
    return 1


if __name__ == "__main__":
    sys.exit(main())
