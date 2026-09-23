"""Independent flat-package producer/consumer controls; synthetic dependencies."""
import copy
import json
import os
from pathlib import Path
import socket
import sys
from types import SimpleNamespace


def forbidden_network(*args, **kwargs):
    raise AssertionError("network forbidden by independent package review")


socket.create_connection = forbidden_network
socket.socket.connect = forbidden_network
flat = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(flat))
import entry  # noqa: E402
import enforce  # noqa: E402
import ids  # noqa: E402
import loaders  # noqa: E402
import selection  # noqa: E402
import selection_store  # noqa: E402

for module in (entry, enforce, ids, loaders, selection, selection_store):
    assert Path(module.__file__).resolve().is_relative_to(flat)

firm = "49financial"
opaque = ids.opaque_firm(firm)
a, b, c = [ids.opaque_account(firm, raw) for raw in ("1000000001", "1000000002", "1000000003")]
directory = {"firm_id_opaque": opaque, "as_of_business_date": "2026-09-22",
             "entries": [{"ids": {"firm_id": opaque, "account_ids": [a, b, c],
                                   "client_id": "client-review"}}]}
ownership = {"schema_version": 1,
             "advisors": {"advisor": {"accounts": [a, b], "relationships": []}}}
entry.ENTRY.deps = lambda tenant: loaders.fixture_deps(directory, ownership)
entry.ENTRY.opaque_firm_for = lambda tenant: opaque
headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-firm-id": firm,
           "x-user-email": "test@example.invalid", "x-user-role": "advisor", "x-advisor-id": "advisor"}
exchange = Path(sys.argv[3])
checks = []


def refused(answer):
    assert answer.get("ok") is False and "data" not in answer, answer


if sys.argv[2] == "irpt-directory-search":
    rows = {}

    def save(tenant, reference, record):
        rows[(tenant, reference)] = copy.deepcopy(record)

    selection_store.configured_store = lambda: SimpleNamespace(save=save)
    event = {"version": "2.0", "headers": headers,
             "routeKey": "POST /api/scoped/investor-reporting/selections",
             "body": json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [a]})}
    answer = entry.lambda_handler(event)
    assert answer["data"]["selected_account_ids"] == [a]
    ref = answer["data"]["account_set_id"]
    assert rows[(firm, ref)]["account_ids"] == [a]
    exchange.write_text(json.dumps(rows[(firm, ref)]), encoding="utf-8")
    checks.append("producer persisted exact subset for separate consumer process")
    for query in ({"scope_kind": "ACCOUNT", "scope_ids": []},
                  {"scope_kind": "ACCOUNT", "scope_ids": [c]},
                  {"scope_kind": "CLIENT", "scope_ids": ["client-review"]},
                  {"scope_kind": "ACCOUNT", "scope_ids": [a], "account_ids": [b]}):
        event["body"] = json.dumps(query)
        refused(entry.lambda_handler(event))
    assert len(rows) == 1
    checks.append("empty, unentitled, partially permitted whole group and extra field refused without save")
    event["body"] = json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [b]})

    def fail_save(*args):
        raise RuntimeError("synthetic conditional store failure")

    selection_store.configured_store = lambda: SimpleNamespace(save=fail_save)
    refused(entry.lambda_handler(event))
    checks.append("persistence failure cannot issue selection success")
else:
    record = json.loads(exchange.read_text(encoding="utf-8"))
    assert record["account_ids"] == [a]
    selection_store.configured_store = lambda: SimpleNamespace(load=lambda tenant, ref:
        copy.deepcopy(record) if tenant == firm and ref == record["account_set_id"] else None)
    calls = []

    def provider(scope, **kwargs):
        assert scope["resolved_scope"]["scope_ids"] == [a]
        calls.append(copy.deepcopy(kwargs))
        return {"report": {"lineage": {"source_revision": "synthetic-review"},
                           "dates": {"actual_end": "2026-09-22"}}, "contract_validated": True}

    entry._handler.run = provider
    event = {"version": "2.0", "headers": headers, "routeKey": next(iter(entry.ROUTES)),
             "pathParameters": {"accountSetId": record["account_set_id"]},
             "queryStringParameters": {"start": "2026-01-01", "end": "2026-09-22"}}
    answer = entry.lambda_handler(event)
    assert answer["status"]["state"] == "READY" and "report" not in answer["data"]
    assert calls == [{"requested_start": "2026-01-01", "requested_end": "2026-09-22"}]
    checks.append("consumer resolves producer-issued subset and exact dates in separate process")
    for reference in (a, "sel_" + "0" * 64):
        bad = copy.deepcopy(event)
        bad["pathParameters"]["accountSetId"] = reference
        refused(entry.lambda_handler(bad))
    bad = copy.deepcopy(event)
    del bad["queryStringParameters"]["end"]
    refused(entry.lambda_handler(bad))
    assert len(calls) == 1
    checks.append("literal/unknown reference and incomplete dates refused before provider")

    def revoke(scope, **kwargs):
        answer = provider(scope, **kwargs)
        ownership["advisors"]["advisor"]["accounts"] = [b]
        return answer

    entry._handler.run = revoke
    refused(entry.lambda_handler(event))
    refused(entry.lambda_handler(event))
    assert len(calls) == 2
    checks.append("in-flight revocation and subsequent request refuse without protected payload")

print(json.dumps({"function": sys.argv[2], "checks": checks,
                  "network_forbidden": True, "isolated_python": sys.flags.isolated == 1,
                  "IRPT_environment_keys": sorted(k for k in os.environ if k.startswith("IRPT_"))}))
