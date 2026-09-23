"""Read exactly the twelve historical drafting objects; never write to AWS.

Outputs a local report, including whether the historic 179 denominator was
actually recovered. Uses only GetObject with retries disabled. It does not
reinterpret old prose as typed figures or infer a numeric check verdict.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

import boto3
from botocore.config import Config

from lib.research.reports.claims import gate_claim
from lib.research.reports.inputs import InputRef


class ReadOnlyObjects:
    def __init__(self):
        self.__client = boto3.client(
            "s3",
            region_name="us-east-1",
            config=Config(retries={"total_max_attempts": 1}),
        )

    def read(self, key):
        return self.__client.get_object(Bucket="opal-data-harvest", Key=key)


def main():
    ledger = Path(
        "org/critical_paths/change_management/amgt-rk-41-verbatim-gate-hold-rebuild-20260919.md"
    )
    raw_ledger = ledger.read_bytes()
    rows = re.findall(
        r"^\| (\S+_Equity) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| `([0-9a-f]{64})` \|$",
        raw_ledger.decode("utf-8"),
        re.MULTILINE,
    )
    if len(rows) != 12 or sum(int(row[2]) for row in rows) != 179:
        raise ValueError(
            "historical ledger denominator is not exactly 12 objects / 179 held"
        )
    reader = ReadOnlyObjects()
    result = {
        "evidence_level": "retained-data read; offline discriminator",
        "ledger_sha256": hashlib.sha256(raw_ledger).hexdigest(),
        "historical_objects": 12,
        "historical_held": 179,
        "objects": [],
        "limitation": "No legacy prose is converted to a checked I2 figure without an actual typed source mapping.",
    }
    for security, _, historical_held, _, _, expected_hash in rows:
        # Exact legacy path grammar documented by the ledger, not a new address.
        key = f"drafting/v1/{security}.json"
        item = {
            "security_key": security,
            "key": key,
            "historical_sha256": expected_hash,
            "historical_held": int(historical_held),
        }
        try:
            response = reader.read(key)
            raw = response["Body"].read()
            doc = json.loads(raw)
            digest = hashlib.sha256(raw).hexdigest()
            item.update(
                sha256=digest,
                exact_historical_bytes=(digest == expected_hash),
                version_id=response.get("VersionId"),
                metadata_sha256=response.get("Metadata", {}).get("document-sha256"),
            )
            source = InputRef.from_bytes("retained_drafting", key, raw)
            # Adapter for this offline REPLAY only: the evidence passages are
            # retained inside this exact drafting document, not freshly fetched.
            passages = {
                record["id"]: dict(record, security_key=security, input_ref=source)
                for record in doc.get("evidence_records", [])
                if record.get("id")
            }
            candidates = []
            for section in doc.get("sections", []):
                for sentence in section.get("sentences", []):
                    if not sentence.get("quoted_spans"):
                        candidates.append((section.get("section"), sentence))
            # Post-HOLD objects may already carry the rows outside sections.
            for sentence in doc.get("held_no_span", []):
                candidates.append((sentence.get("section"), sentence))
            counts = {"PASS": 0, "HOLD": 0, "REFUSE": 0}
            cases = []
            for index, (section, sentence) in enumerate(candidates):
                candidate = {
                    "kind": "prose",
                    "text": sentence.get("text"),
                    "evidence": sentence.get("evidence", []),
                    "quoted_spans": [],
                }
                verdict = gate_claim(
                    candidate,
                    security_key=security,
                    figures={},
                    passages=passages,
                    manifest={source.input_id: source},
                )
                counts[verdict["status"]] += 1
                cases.append(
                    {
                        "index": index,
                        "section": section,
                        "text_sha256": hashlib.sha256(
                            (sentence.get("text") or "").encode()
                        ).hexdigest(),
                        "has_figure_id": bool(sentence.get("figure_id")),
                        "status": verdict["status"],
                        "reason": verdict["reason"],
                    }
                )
            item.update(
                current_no_span=len(candidates), discriminator=counts, cases=cases
            )
        except Exception as error:
            item["read_error"] = type(error).__name__
            item["exact_historical_bytes"] = False
        result["objects"].append(item)
    result["exact_historical_matches"] = sum(
        x["exact_historical_bytes"] for x in result["objects"]
    )
    result["observed_no_span"] = sum(
        x.get("current_no_span", 0) for x in result["objects"]
    )
    result["historical_denominator_recovered"] = (
        result["exact_historical_matches"] == 12 and result["observed_no_span"] == 179
    )
    result["counts"] = {
        status: sum(
            x.get("discriminator", {}).get(status, 0) for x in result["objects"]
        )
        for status in ("PASS", "HOLD", "REFUSE")
    }
    destination = Path(__file__).with_name("HELD_CENSUS.json")
    destination.write_bytes((json.dumps(result, indent=2) + "\n").encode())
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "objects"}, indent=2
        )
    )
    print(
        json.dumps(
            [
                {key: value for key, value in item.items() if key != "cases"}
                for item in result["objects"]
            ],
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
