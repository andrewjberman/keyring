"""Prepare concrete Peers/crosswalk bytes; all AWS access is read-only.

Run from the repository root. Inputs are the retained snapshots previously
downloaded under --inputs. This does not publish a crosswalk or a peer object.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import sys
from unittest.mock import patch

import boto3

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from lib.research.identity import crosswalk
from lib.research.peers import engine, universe


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--stamp", required=True)
    args = parser.parse_args()
    inputs, out = Path(args.inputs), Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    client = boto3.client("s3", region_name="us-east-1")

    class ReadOnlyS3:
        def __getattr__(self, name):
            if name not in {"get_object", "head_object", "list_objects_v2", "get_paginator"}:
                raise RuntimeError("Preparation forbids AWS operation: " + name)
            return getattr(client, name)

    readonly = ReadOnlyS3()
    retained = json.loads((inputs / "union.json").read_bytes())
    live_union, union_source = crosswalk.load_identity_universe(client=readonly)
    assert live_union == retained, "retained identity input moved; prepare again on an explicit basis"
    document = crosswalk.build_crosswalk(args.stamp[:10], identity_universe=retained, identity_source=union_source)
    crosswalk._validate_document_against_schema(document)
    crosswalk_raw = crosswalk.serialise(document)
    crosswalk_path = out / "crosswalk.json"
    crosswalk_path.write_bytes(crosswalk_raw)
    measured = {r["security_key"] for r in document["records"] if r["resolution"] == "MEASURED"}
    prior_keys = [k[len("peers/v1/"):].rsplit("/", 1)[0]
                  for k in json.loads((inputs / "prior-peer-keys.json").read_bytes())]
    refusals = [{"key": k, "result": crosswalk.resolve(k, path=str(crosswalk_path))}
                for k in prior_keys if crosswalk.resolve(k, path=str(crosswalk_path))["resolution"] != "MEASURED"]
    candidates = universe.hydrate_csc_values(json.loads((inputs / "candidate-universe.json").read_bytes()), readonly)
    candidate_path = out / "candidate-universe.json"
    candidate_path.write_text(json.dumps(candidates), encoding="utf-8")
    captured = {}
    original = engine.peers

    def observe(key, **kwargs):
        result = original(key, **kwargs)
        captured[key] = result
        return result

    def s3_only(service, **kwargs):
        assert service == "s3", "Preparation permits only S3 reads"
        return readonly

    stdout = io.BytesIO()
    with patch.dict(os.environ, {"AMGT_CROSSWALK_PATH": str(crosswalk_path),
                                "AMGT_PEER_UNIVERSE_CACHE": str(candidate_path)}), \
            patch("boto3.client", side_effect=s3_only), patch.object(engine, "peers", side_effect=observe):
        summary = engine.run_batch(args.stamp, write_pool=False, out=stdout)
    assert set(captured) == measured, "batch and crosswalk key sets differ"
    files = []
    for key, result in sorted(captured.items()):
        raw = engine.serialise(result).encode("utf-8")
        filename = digest(key.encode()) + ".json"
        (out / filename).write_bytes(raw)
        files.append({"security_key": key, "file": filename, "sha256": digest(raw),
                      "size": len(raw), "pool_key": engine.pool_key(key, args.stamp),
                      "basis": result["basis"], "members": len(result["members"])})
    manifest = {"cloud_writes": 0, "stamp": args.stamp,
        "crosswalk": {"file": "crosswalk.json", "sha256": digest(crosswalk_raw),
                      "pool_key": crosswalk.CROSSWALK_PREFIX + args.stamp[:10] + ".json",
                      "denominators": document["denominators"]},
        "prior_keys": len(prior_keys), "prior_keys_measured": len(prior_keys) - len(refusals), "refusals": refusals,
        "crosswalk_measured_keys": len(measured), "batch_keys": len(captured), "key_sets_equal": True,
        "shared_defect": summary["shared_defect"], "files": files,
        "inputs": {name: digest((inputs / name).read_bytes())
                   for name in ("union.json", "candidate-universe.json", "crosswalk.json", "prior-peer-keys.json")},
        "csc_value_sources": candidates.get("csc_value_sources"), "universe_vintage": candidates.get("vintage")}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (out / "batch.log").write_bytes(stdout.getvalue())
    print(json.dumps({k: v for k, v in manifest.items() if k not in {"files", "inputs", "csc_value_sources"}}, indent=2))
    print("Prepared artifact directory:", out)


if __name__ == "__main__":
    main()
