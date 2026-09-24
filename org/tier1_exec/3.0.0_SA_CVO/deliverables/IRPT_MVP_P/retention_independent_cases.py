"""Independent retention race and finite-lifetime controls."""
import json

import pytest
from test_retention import (world as candidate_world, reserve, DAY, RetentionPolicy,
                            RetentionExpired, RetentionRefused)

world = candidate_world


def test_successful_write_crossing_reserved_expiry_cannot_resurrect(world):
    ref = reserve(world)
    expires = world.policy.require_live(world.principal, ref)["expires_at"]
    world.state.now = expires - 1
    original_put = world.table.put_item

    def delayed_put(*args, **kwargs):
        if "ExpressionAttributeValues" in kwargs:
            world.state.now = expires  # condition still receives the previously sampled :now
        return original_put(*args, **kwargs)

    world.table.put_item = delayed_put
    promoted = live = False
    try:
        world.policy.promote(world.principal, ref)
        promoted = True
    except (RetentionExpired, RetentionRefused):
        pass
    try:
        world.policy.require_live(world.principal, ref, accepted=True)
        live = True
    except (RetentionExpired, RetentionRefused):
        pass
    row = next(iter(world.table.rows.values()))
    print(json.dumps({"promotion_returned_success": promoted, "accepted_read_succeeds": live,
                      "old_reserved_expiry": expires, "now": world.state.now,
                      "stored_state": row["state"], "stored_expiry": row["expires_at"]}))
    assert not promoted and not live


def test_before_deadline_promotion_and_retry_keep_creation_ceiling(world):
    ref = reserve(world)
    first = world.policy.require_live(world.principal, ref)
    world.state.now = first["expires_at"] - 1
    assert world.policy.promote(world.principal, ref) == ref
    accepted = world.policy.require_live(world.principal, ref, accepted=True)
    assert accepted["expires_at"] == first["ceiling_at"]
    world.state.now += 100 * DAY
    assert reserve(world) == ref and world.policy.promote(world.principal, ref) == ref
    assert world.policy.require_live(world.principal, ref) == accepted


def test_restart_at_expiry_cannot_reserve_same_identity(world):
    ref = reserve(world)
    world.state.now = world.policy.require_live(world.principal, ref)["expires_at"]
    original = world.policy
    world.policy = RetentionPolicy(original.index, original.reporting_policy,
                                   original.authorize, clock=lambda: world.state.now)
    with pytest.raises(RetentionExpired):
        reserve(world)
    with pytest.raises(RetentionExpired):
        world.policy.promote(world.principal, ref)
    assert len(world.table.rows) == 1


def test_dependency_minimum_and_expiry_survive_later_output_creation(world):
    short = reserve(world, "SELECTED_ACCOUNTS", "short")
    long = reserve(world, "PERFORMANCE_SOURCE_EVIDENCE", "long")
    world.policy.promote(world.principal, short)
    world.policy.promote(world.principal, long)
    earliest = world.policy.require_live(world.principal, short)["expires_at"]
    world.state.now += DAY
    output = world.policy.reserve(world.principal, world.owner, "PERFORMANCE", "combined",
                                  dependencies=[long, short])
    assert world.policy.require_live(world.principal, output)["expires_at"] == earliest
    world.state.now = earliest
    with pytest.raises(RetentionExpired):
        world.policy.require_live(world.principal, output)


def test_repeated_conditional_conflicts_never_report_acceptance(world):
    ref = reserve(world)
    calls = []
    world.table.conflict = lambda: calls.append(True)
    with pytest.raises(RetentionRefused):
        world.policy.promote(world.principal, ref)
    assert len(calls) == 4
    assert next(iter(world.table.rows.values()))["state"] == "RESERVED"


@pytest.mark.parametrize("value", [True, -1, float("nan"), float("inf")])
def test_invalid_server_clock_never_creates_record(world, value):
    world.state.now = value
    with pytest.raises(RetentionRefused):
        reserve(world)
    assert not world.table.rows
