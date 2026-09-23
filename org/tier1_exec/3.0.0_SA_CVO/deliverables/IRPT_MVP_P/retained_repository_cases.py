"""Independent final history-release and repository/lineage controls."""
import json

import pytest
from test_retained_repository import (world as candidate_world, retention_world as candidate_retention_world,
                                      put, publish, DAY, RetentionExpired, RetentionRefused)
from test_repository import report
from repository import ReportDenied, ReportRefused, ReportRepository

world = candidate_world
retention_world = candidate_retention_world


@pytest.mark.parametrize("boundary", ["expiry", "revocation"])
def test_history_rechecks_earlier_items_at_final_release(world, boundary):
    source = put(world)
    world.stores.retention.promote(world.principal, source["retention_ref"])
    refs = []
    for name in ("REQ-one", "REQ-two"):
        value = report(name)
        refs.append(world.stores.reports.persist(world.principal, world.owner, "ANALYSIS",
                    value["request_ref"], value, {"fixture": "independent-review"},
                    retention_dependencies=[source["retention_ref"]]))
    assert len(world.stores.reports.list(world.principal)["items"]) == 2
    deadline = world.state.now + 2555 * DAY
    reads = []

    def change_during_second_blob():
        reads.append(True)
        if len(reads) == 2:
            if boundary == "expiry":
                world.state.now = deadline
            else:
                world.state.access = False

    world.s3.on_get = change_during_second_blob
    try:
        result = world.stores.reports.list(world.principal)
    except ReportDenied:
        result = {"items": []}
    world.s3.on_get = None
    unreadable = 0
    for ref in refs:
        with pytest.raises(ReportDenied):
            world.stores.reports.get(world.principal, ref["report_id"], ref["revision"])
        unreadable += 1
    print(json.dumps({"boundary": boundary, "blob_reads": len(reads), "returned_items": result["items"],
                      "now": world.state.now, "access": world.state.access, "fresh_gets_refused": unreadable}))
    assert result["items"] == []


def test_bare_report_reader_cannot_read_retained_report(world):
    source = put(world)
    world.stores.retention.promote(world.principal, source["retention_ref"])
    ref = publish(world, [source["retention_ref"]])
    bound = world.stores.reports
    bare = ReportRepository(bound.index, bound.blobs, bound.authorize, bound.validate)
    with pytest.raises(ReportRefused, match="retention service"):
        bare.get(world.principal, ref["report_id"], ref["revision"])


def test_missing_report_retention_reference_refuses(world):
    source = put(world)
    world.stores.retention.promote(world.principal, source["retention_ref"])
    ref = publish(world, [source["retention_ref"]])
    row = next(row for key, row in world.table.rows.items() if key[1].startswith("REPORT#"))
    del row["retention_ref"]
    with pytest.raises(ReportRefused, match="binding"):
        world.stores.reports.get(world.principal, ref["report_id"], ref["revision"])


def test_parent_acceptance_cannot_renew_child_original_deadline(world):
    old = put(world)
    world.state.now += 20 * DAY
    child = put(world, "child", [old["retention_ref"]])
    before = world.stores.retention.require_live(world.principal, child["retention_ref"])
    world.stores.retention.promote(world.principal, old["retention_ref"])
    assert world.stores.retention.require_live(world.principal, child["retention_ref"])["expires_at"] == before["expires_at"]
    world.state.now = before["expires_at"]
    with pytest.raises(RetentionExpired):
        world.stores.retention.promote(world.principal, child["retention_ref"])


def test_accepted_lineage_cannot_drop_parent_on_retry(world):
    old = put(world)
    child = put(world, "child", [old["retention_ref"]])
    world.stores.retention.promote(world.principal, old["retention_ref"])
    world.stores.retention.promote(world.principal, child["retention_ref"], [])
    accepted = world.stores.retention.require_live(world.principal, child["retention_ref"], accepted=True)
    assert accepted["dependencies"] == [old["retention_ref"]]
    with pytest.raises(RetentionRefused):
        world.stores.retention.promote(world.principal, child["retention_ref"], [])


def test_blob_write_crossing_expiry_cannot_publish_artifact(world):
    original = world.s3.put_object
    deadline = world.state.now + 30 * DAY

    def late(**kwargs):
        result = original(**kwargs)
        world.state.now = deadline
        return result

    world.s3.put_object = late
    with pytest.raises(RetentionExpired):
        put(world)
    assert not any(key[1].startswith("ARTIFACT#") for key in world.table.rows)
    assert world.s3.put_count == 1  # orphan bytes are not a visible accepted artifact


def test_report_publication_crossing_expiry_cannot_return_or_serve(world):
    source = put(world)
    world.stores.retention.promote(world.principal, source["retention_ref"])
    original = world.stores.reports.index.publish
    deadline = world.state.now + 2555 * DAY

    def late(item):
        accepted = original(item)
        world.state.now = deadline
        return accepted

    world.stores.reports.index.publish = late
    with pytest.raises(RetentionExpired):
        publish(world, [source["retention_ref"]])
    assert world.stores.reports.list(world.principal)["items"] == []
