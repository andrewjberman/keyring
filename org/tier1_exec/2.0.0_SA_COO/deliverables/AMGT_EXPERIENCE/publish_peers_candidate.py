"""Publish the EXACT signed Peers candidate bytes to the pool -- the one act both never-widen halves cover.

Run from the repository root:
  python org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/publish_peers_candidate.py \
      --candidate <dir with manifest.json, crosswalk.json, <sha>.json objects> --receipt <path>

WHAT IT DOES, IN ORDER, AND WHY THE ORDER IS THE MECHANISM:
  1. Verifies every candidate file's sha256 against manifest.json (the halves bind BYTES, not a rebuild).
  2. CTO-half CONDITION (msg 25202): head_object on the crosswalk key IMMEDIATELY before the put. 404 = the
     additive branch (IfNoneMatch: *); 200 = STOP AND REPORT, nothing put -- write_pool's IfMatch branch would
     OVERWRITE a key another writer landed first, and that rollback is a restore the producer captured nowhere.
  3. Puts the crosswalk through crosswalk.write_pool (schema-validated BEFORE the put; read-back of digest and
     length), then each peer object through engine.write_pool_object (read-back per object). The peers writer
     is an unconditional put, so this script REFUSES any peer key that already exists (measured 0 pre-flight).
  4. Writes a receipt naming every key written -- the rollback denominator -- and the read-back result.
No vendor call, no delete, no deploy. A refusal at any step puts nothing further.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from lib.research.identity import crosswalk  # noqa: E402
from lib.research.peers import engine  # noqa: E402

BUCKET = "opal-data-harvest"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def head(client, key):
    try:
        return client.head_object(Bucket=BUCKET, Key=key)
    except ClientError as exc:
        if exc.response["Error"]["Code"] in {"404", "NoSuchKey", "NotFound"}:
            return None
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--receipt", required=True)
    args = parser.parse_args()
    cand = Path(args.candidate)
    manifest = json.loads((cand / "manifest.json").read_bytes())
    receipt = {"candidate": str(cand), "stamp": manifest["stamp"], "steps": [], "written": [], "read_back_ok": 0}

    def fail(msg):
        receipt["refused"] = msg
        Path(args.receipt).write_text(json.dumps(receipt, indent=2) + "\n")
        print("REFUSED: " + msg)
        sys.exit(3)

    # 1. bytes == manifest
    cw_raw = (cand / "crosswalk.json").read_bytes()
    if sha(cw_raw) != manifest["crosswalk"]["sha256"]:
        fail("crosswalk.json sha256 differs from manifest")
    objects = []
    for entry in manifest["files"]:
        raw = (cand / entry["file"]).read_bytes()
        if sha(raw) != entry["sha256"]:
            fail("object %s sha256 differs from manifest" % entry["security_key"])
        objects.append((entry, raw))
    receipt["steps"].append("bytes verified: crosswalk + %d objects match manifest sha256" % len(objects))

    client = boto3.client("s3", region_name="us-east-1")
    cw_key = manifest["crosswalk"]["pool_key"]

    # peers keys must be ABSENT (unconditional put in the producer)
    present = [e["pool_key"] for e, _ in objects if head(client, e["pool_key"]) is not None]
    if present:
        fail("%d peer key(s) already exist at this stamp, e.g. %s" % (len(present), present[:3]))
    receipt["steps"].append("peer keys absent: 0 of %d present" % len(objects))

    # 2. CTO condition: head immediately before the put
    control = head(client, "crosswalk/v1/2026-09-22.json")
    if control is None:
        fail("positive control crosswalk/v1/2026-09-22.json not visible to the instrument")
    existing = head(client, cw_key)
    if existing is not None:
        fail("STOP: %s already exists (ContentLength %s, document-sha256 %s) -- IfMatch branch, not covered"
             % (cw_key, existing.get("ContentLength"), existing.get("Metadata", {}).get("document-sha256")))
    receipt["steps"].append("pre-put head_object %s -> 404 (control 2026-09-22 -> 200 len %s): additive branch"
                            % (cw_key, control["ContentLength"]))

    # 3a. crosswalk put (schema-validated inside write_pool)
    document = json.loads(cw_raw.decode("utf-8"))
    rec = crosswalk.write_pool(cw_key, cw_raw, client=client, document=document)
    receipt["written"].append({"key": cw_key, "sha256": rec["sha256"], "put_performed": rec["put_performed"],
                               "content_length": rec["content_length"]})
    if rec["sha256"] != manifest["crosswalk"]["sha256"] or rec["content_length"] != len(cw_raw):
        fail("crosswalk read-back mismatch")
    receipt["read_back_ok"] += 1
    print("OK: crosswalk %s put=%s len=%d" % (cw_key, rec["put_performed"], rec["content_length"]))

    # 3b. peer objects
    for entry, raw in objects:
        peer_set = json.loads(raw.decode("utf-8"))
        if engine.serialise(peer_set).encode("utf-8") != raw:
            fail("re-serialisation of %s is not byte-identical to the signed file" % entry["security_key"])
        out = engine.write_pool_object(client, peer_set, manifest["stamp"])
        ok = out["read_back_ok"] and out["sha256"] == entry["sha256"] and out["key"] == entry["pool_key"]
        receipt["written"].append({"key": out["key"], "sha256": out["sha256"], "read_back_ok": bool(ok)})
        if not ok:
            Path(args.receipt).write_text(json.dumps(receipt, indent=2) + "\n")
            print("ERROR: read-back failed on %s -- stopping; %d written so far" % (out["key"], len(receipt["written"])))
            sys.exit(4)
        receipt["read_back_ok"] += 1
    receipt["summary"] = "UPLOADED %d of %d peer objects + 1 crosswalk, read-back ok %d of %d" % (
        len(objects), len(objects), receipt["read_back_ok"], len(objects) + 1)
    Path(args.receipt).write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["summary"])


if __name__ == "__main__":
    main()
