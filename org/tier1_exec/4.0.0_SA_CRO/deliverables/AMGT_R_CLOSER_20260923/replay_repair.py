"""Read twelve exact retained S3 versions; replay locally without AWS writes."""

import hashlib
import json
import os
from pathlib import Path
import tempfile

import boto3

from lib.research.api.scoped_amgt import read_drafted_sections


def main():
    home = Path(__file__).parent
    census = json.loads((home / "HELD_CENSUS.json").read_bytes())
    client = boto3.client("s3", region_name="us-east-1")
    result = {"plane": "local candidate reader, exact retained S3 versions", "cases": []}
    with tempfile.TemporaryDirectory(prefix="amgt-r-replay-") as directory:
        previous = os.environ.get("AMGT_DRAFTING_ROOT")
        os.environ["AMGT_DRAFTING_ROOT"] = directory
        try:
            for obj in census["objects"]:
                raw = client.get_object(Bucket="opal-data-harvest", Key=obj["key"],
                                        VersionId=obj["version_id"])["Body"].read()
                before = hashlib.sha256(raw).hexdigest()
                assert before == obj["historical_sha256"]
                path = Path(directory) / (obj["security_key"] + ".json")
                path.write_bytes(raw)
                output = read_drafted_sections(obj["security_key"])
                served = [s for section in output["drafted_sections"] for s in section["sentences"]]
                after = hashlib.sha256(path.read_bytes()).hexdigest()
                no_span = sum(not any(q.strip() for q in s["quoted_spans"]) for s in served)
                assert before == after
                assert output["drafting_status"] == "SERVED"
                assert no_span == 0
                assert output["held_no_span_at_read"] == obj["historical_held"]
                source = json.loads(raw)
                anchored = [s["text"] for sec in source["sections"] for s in sec["sentences"]
                            if any(q.strip() for q in s.get("quoted_spans", []))]
                assert [s["text"] for s in served] == anchored
                result["cases"].append({
                    "security_key": obj["security_key"], "source_sha256": before,
                    "source_unchanged": before == after, "served": len(served),
                    "served_no_span": no_span, "held_at_read": output["held_no_span_at_read"],
                    "held_on_object": output["held_no_span_on_object"],
                    "anchored_siblings_exact": True,
                })
        finally:
            if previous is None:
                os.environ.pop("AMGT_DRAFTING_ROOT", None)
            else:
                os.environ["AMGT_DRAFTING_ROOT"] = previous
    result.update(documents=len(result["cases"]),
                  served=sum(c["served"] for c in result["cases"]),
                  held_at_read=sum(c["held_at_read"] for c in result["cases"]),
                  served_no_span=sum(c["served_no_span"] for c in result["cases"]))
    (home / "REPAIR_REPLAY.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}))


if __name__ == "__main__":
    main()
