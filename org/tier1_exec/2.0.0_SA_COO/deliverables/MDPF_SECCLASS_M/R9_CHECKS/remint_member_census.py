#!/usr/bin/env python3
"""remint_member_census.py -- batch 183's ONE packet: every member the producer re-mint would move, and who changed it.

For each irpt_holdings_* bundle (.tools/safe_deploy_core.py STANDALONE_BUNDLES) the SERVED tar is downloaded (current S3
version), and each member is compared with CLOUD's bytes (CRLF-normalized). For a member that differs, the commit whose blob
equals the served bytes is found by walking that path's history (newest first), and every commit after it touching the path is
listed with its author and subject -- the changes the re-mint would carry, attributed. A served member found at no commit is
reported as such. Read-only (S3 get, git); writes R9_CHECKS/REMINT_MEMBER_CENSUS_<date>.json.

Run from the repo root: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/remint_member_census.py
"""
from __future__ import annotations

import datetime
import importlib.util
import io
import json
import subprocess
import sys
import tarfile
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
s3 = boto3.client("s3", region_name="us-east-1")


def git(*args) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def norm(b: bytes) -> bytes:
    return b.replace(b"\r\n", b"\n")


def blob_at(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    spec = importlib.util.spec_from_file_location("sdc", ".tools/safe_deploy_core.py")
    sdc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sdc)
    out = {"generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "cloud": git("rev-parse", "CLOUD").strip(),
           "bundles": {}}
    for name, b in sdc.STANDALONE_BUNDLES.items():
        head = s3.head_object(Bucket=b["bucket"], Key=b["s3_key"])
        data = s3.get_object(Bucket=b["bucket"], Key=b["s3_key"], VersionId=head["VersionId"])["Body"].read()
        tf = tarfile.open(fileobj=io.BytesIO(data))
        names = tf.getnames()
        rows = []
        for member in map(str, b["members"]):
            cand = [n for n in names if n == member or n.endswith("/" + member) or member.endswith("/" + n)]
            if not cand:
                rows.append({"member": member, "state": "not-in-served-tar"})
                continue
            served = norm(tf.extractfile(cand[0]).read())
            cloud = blob_at("CLOUD", member)
            if cloud is not None and norm(cloud) == served:
                continue
            commits = git("log", "--format=%H\t%an\t%ad\t%s", "--date=format:%m-%d", "CLOUD", "--", member).splitlines()
            base, after = None, []
            for line in commits:
                sha = line.split("\t", 1)[0]
                b_ = blob_at(sha, member)
                if b_ is not None and norm(b_) == served:
                    base = sha
                    break
                after.append(line.split("\t"))
            rows.append({"member": member, "state": "differs", "served_equals_commit": base,
                         "changes_riding": [{"commit": c[0][:10], "author": c[1], "date": c[2], "subject": c[3][:160]}
                                            for c in after] if base else None})
        out["bundles"][name] = {"bucket": b["bucket"], "key": b["s3_key"], "served_version": head["VersionId"],
                                "served_last_modified": head["LastModified"].isoformat(), "members": len(b["members"]),
                                "differing": rows}
        print(name, head["VersionId"], "members", len(b["members"]), "differing", len(rows), flush=True)
    dest = HERE / ("REMINT_MEMBER_CENSUS_%s.json" % datetime.date.today().strftime("%Y%m%d"))
    dest.write_text(json.dumps(out, indent=1), encoding="utf-8")
    authors = {}
    for bdl in out["bundles"].values():
        for r in bdl["differing"]:
            for c in (r.get("changes_riding") or []):
                authors.setdefault(c["author"], set()).add(r["member"])
    print("AUTHORS OF RIDING CHANGES:", {a: len(m) for a, m in sorted(authors.items())})
    print("WROTE", dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
