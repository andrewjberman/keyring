"""Reviewer controls loaded beside the exact candidate's boundary fixture."""
import copy
import json

from test_entry_selection import boundary as candidate_boundary, entry, fx

boundary = candidate_boundary


def test_unknown_retained_reference_refuses_before_provider(boundary):
    boundary.event["pathParameters"]["accountSetId"] = "sel_" + "f" * 64
    answer = entry.lambda_handler(boundary.event)
    assert answer["ok"] is False and "data" not in answer
    assert answer["status"]["public_reason_code"] == "OBJECT_NOT_COVERED"
    assert boundary.calls == []


def test_modified_members_cannot_reuse_retained_reference(boundary):
    row = next(iter(boundary.rows.values()))
    row["account_ids"] = [fx.A1, fx.A2]
    answer = entry.lambda_handler(boundary.event)
    assert answer["ok"] is False and "data" not in answer
    assert boundary.calls == []


def test_cross_firm_retained_row_refuses_before_provider(boundary):
    next(iter(boundary.rows.values()))["firm_id"] = "other-firm"
    answer = entry.lambda_handler(boundary.event)
    assert answer["ok"] is False and "data" not in answer
    assert boundary.calls == []


def test_changed_date_window_is_not_previous_invocation_payload(boundary):
    original_scope = copy.deepcopy(boundary.scope)
    for start, end in (("2024-02-29", "2024-02-29"), ("2025-01-01", "2025-12-31")):
        boundary.event["queryStringParameters"] = {"start": start, "end": end}
        answer = entry.lambda_handler(boundary.event)
        assert answer["data"]["dates"]["requested_start"] == start
        assert answer["data"]["dates"]["requested_end"] == end
        assert "report" not in answer["data"] and "_status" not in answer["data"]
        assert boundary.calls[-1][1] == {"requested_start": start, "requested_end": end}
        assert boundary.calls[-1][0]["resolved_scope"]["scope_ids"] == [fx.A1]
    assert len(boundary.calls) == 2 and boundary.scope == original_scope


def test_revocation_during_provider_prevents_release(boundary, monkeypatch):
    provider = entry._handler.run

    def revoke_then_return(scope, **kwargs):
        result = provider(scope, **kwargs)
        boundary.deps.ownership["advisors"][fx.ADVISOR_A]["accounts"] = [fx.A2, fx.A3]
        boundary.deps.entitlement_revision = "ent-review-revoked"
        return result

    monkeypatch.setattr(entry._handler, "run", revoke_then_return)
    answer = entry.lambda_handler(boundary.event)
    assert len(boundary.calls) == 1
    enforcer, _ = entry.ENTRY.enforcer_for(fx.TENANT)
    current, refusal = enforcer.resolve_now(entry._entry._enforce.Request(
        boundary.event["headers"], "performance_report"))
    assert refusal is None and fx.A1 not in current["permitted_account_set"]
    next_answer = entry.lambda_handler(boundary.event)
    assert next_answer["ok"] is False and "data" not in next_answer
    assert len(boundary.calls) == 1
    print(json.dumps({"returned_data": "data" in answer,
                      "returned_state": answer["status"]["state"],
                      "current_selected_account_permitted": False,
                      "current_entitlement_revision": current["entitlement_revision"],
                      "next_request_refused": True, "provider_calls": len(boundary.calls)}))
    assert answer.get("ok") is False and "data" not in answer


def test_invalid_end_and_nonstring_query_refuse(boundary):
    for query in ({"start": "2026-01-01", "end": "2026-02-29"},
                  {"start": ["2026-01-01"], "end": "2026-09-09"}):
        boundary.event["queryStringParameters"] = query
        answer = entry.lambda_handler(boundary.event)
        assert answer["ok"] is False and "data" not in answer
        assert answer["status"]["public_reason_code"] == "INVALID_INPUT"
    assert boundary.calls == []
