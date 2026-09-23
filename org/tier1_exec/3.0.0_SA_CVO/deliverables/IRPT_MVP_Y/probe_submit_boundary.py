"""Independent synthetic baseline probe; no vendor, queue, or cloud calls.

Runs the actual submit compute function with injected send and already-resolved
synthetic scope. This does not exercise authentication or the HTTP guard.
"""

import hashlib
import importlib.util
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[5]
    source = root / "infra/aws/lambda/investor-reporting/ycharts/generate/entry.py"
    spec = importlib.util.spec_from_file_location("cvo_y_generation_entry", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    scope = {
        "_census": {"tenant": "49financial", "opaque_firm_id": "F-SYNTHETIC"},
        "permitted_account_set_fingerprint": "synthetic-permitted-ab",
        "permitted_account_set": ["A-SYNTHETIC", "B-SYNTHETIC"],
        "principal_class": "ADVISOR",
        "entitlement_revision": "synthetic-1",
    }
    first = {
        "request_id": "areq-synthetic-a", "client_id": "C-SYNTHETIC",
        "account_ids": ["A-SYNTHETIC"], "snapshot_id": "snapshot-a",
        "variant": "overview", "comparison_keys": [], "report_title": "First",
    }
    second = dict(first, request_id="areq-synthetic-b",
                  account_ids=["B-SYNTHETIC"], snapshot_id="snapshot-b",
                  report_title="Second")
    sends = []

    def send(url, message):
        sends.append(json.loads(message))
        return {"MessageId": "synthetic-only"}

    answers = [module.submit_analysis({}, scope, {"body": json.dumps(body)}, None,
                                     send=send, queue_url="synthetic-no-network")
               for body in (first, second, first)]
    result = {
        "boundary": "actual submit_analysis; injected send; synthetic resolved scope",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "browser_fields": list(module.BROWSER_FIELDS),
        "submitted_keys": list(first),
        "retained_keys": sorted(set(first).intersection(module.BROWSER_FIELDS)),
        "discarded_keys": sorted(set(first).difference(module.BROWSER_FIELDS)),
        "issued_ids": [answer["identity"]["request_id"] for answer in answers],
        "changed_input_same_id": answers[0]["identity"] == answers[1]["identity"],
        "send_count_for_three_calls": len(sends),
        "changed_input_same_enqueued_message": sends[0] == sends[1],
        "queued_request_halves": [message["request"] for message in sends],
        "limits": ["Not an HTTP/auth test", "No persistent adapter exercised",
                   "No vendor/cloud calls", "No new candidate or deployed verdict"],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
