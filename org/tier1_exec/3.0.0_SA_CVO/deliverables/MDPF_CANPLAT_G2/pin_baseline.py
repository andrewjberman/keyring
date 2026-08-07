"""MDPF_CANPLAT.G2 -- R7 limb 3: pin the served platinum surface to explicit S3 VersionIds.

Writes baseline_manifest_<UTCSTAMP>.json beside this script. Re-pins are NEW manifests,
never edits (TO @f123fbf6e acceptance criterion 3).

READ-ONLY on the served surface. NEVER#3 binds absolutely.

Timestamps are s3api/boto3 true UTC ISO-8601 (+00:00), never `aws s3 ls` columns.
Denominators printed on every scan (acceptance criterion 8).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import pathlib
import sys

import boto3

BUCKET = "opal-data-portal-v2"
SCOPES = ["global", "49financial", "inflection", "cottonwood"]
ARTIFACT_TYPES = ["aggregate-aua-timeseries", "aum-metrics", "account-distribution"]

CANONICAL_KEYS = [
    ("platinum/mdpf/{s}/{t}.json".format(s=s, t=t), "canonical")
    for s in SCOPES
    for t in ARTIFACT_TYPES
]
# R12: the two standalone extras -- pinned so their continued presence is verifiable
# until their fold passes R2+R7. Retirement is Andrew's act, never this program's.
EXTRA_KEYS = [
    ("platinum/mdpf/cottonwood/account-units.json", "standalone_extra_R12"),
    ("platinum/mdpf/global/non-model-assets.json", "standalone_extra_R12"),
]


def latest_version(s3, key: str):
    """Return the IsLatest version entry for an exact key, or None."""
    paginator = s3.get_paginator("list_object_versions")
    for page in paginator.paginate(Bucket=BUCKET, Prefix=key):
        for v in page.get("Versions", []):
            if v["Key"] == key and v.get("IsLatest"):
                return v
    return None


def main() -> int:
    s3 = boto3.client("s3")
    pin_instant = dt.datetime.now(dt.timezone.utc)
    stamp = pin_instant.strftime("%Y%m%dT%H%M%SZ")
    targets = CANONICAL_KEYS + EXTRA_KEYS

    entries = []
    missing = []
    for key, role in targets:
        v = latest_version(s3, key)
        if v is None:
            missing.append(key)
            print("ERROR: no latest version found for s3://{b}/{k}".format(b=BUCKET, k=key))
            continue
        body = s3.get_object(Bucket=BUCKET, Key=key, VersionId=v["VersionId"])["Body"].read()
        entries.append(
            {
                "key": key,
                "role": role,
                "version_id": v["VersionId"],
                "etag": v["ETag"].strip('"'),
                "size": v["Size"],
                "last_modified_utc": v["LastModified"].astimezone(dt.timezone.utc).isoformat(),
                "sha256": hashlib.sha256(body).hexdigest(),
            }
        )
        print(
            "OK: {k}  VersionId={vid}  sha256={h}...".format(
                k=key, vid=v["VersionId"][:16], h=entries[-1]["sha256"][:12]
            )
        )

    manifest = {
        "_meta": {
            "artifact": "R7 baseline manifest -- pinned served platinum surface",
            "to": "MDPF_CANPLAT.G2 @f123fbf6e",
            "pinned_by": "3.0.0_SA_CVO~Z",
            "pin_instant_utc": pin_instant.isoformat(),
            "bucket": BUCKET,
            "rule": "Re-pins are NEW manifests, never edits.",
        },
        "denominator": {
            "targets": len(targets),
            "pinned": len(entries),
            "missing": missing,
        },
        "entries": entries,
    }
    out = pathlib.Path(__file__).parent / "baseline_manifest_{s}.json".format(s=stamp)
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="ascii")
    print(
        "DENOMINATOR: {p} of {t} target keys pinned ({c} canonical + {e} extras); missing: {m}".format(
            p=len(entries), t=len(targets), c=len(CANONICAL_KEYS), e=len(EXTRA_KEYS),
            m=missing if missing else "none",
        )
    )
    print("MANIFEST: {o}".format(o=out.name))
    print("PIN INSTANT (UTC): {i}".format(i=pin_instant.isoformat()))
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
