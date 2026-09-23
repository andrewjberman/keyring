"""Independent receipt persistence, restart, binding, and release controls."""
import copy

import pytest
from test_retention import (world as candidate_world, reserve, RetentionPolicy,
                            RetentionExpired, RetentionRefused, ReportDenied)

world = candidate_world


def fresh(world):
    old = world.policy
    return RetentionPolicy(old.index, old.reporting_policy, old.authorize,
                           clock=lambda: world.state.now)


@pytest.mark.parametrize("persisted", [False, True])
def test_lost_receipt_response_has_only_proven_acceptance(world, persisted):
    ref = reserve(world)
    deadline = world.policy.require_live(world.principal, ref)["expires_at"]
    world.state.now = deadline - 1
    original = world.table.put_item

    def fail_receipt(**kwargs):
        if "#PROMOTION#" in kwargs["Item"]["request_revision"]:
            with pytest.raises(RetentionRefused):
                fresh(world).require_live(world.principal, ref, accepted=True)
            if persisted:
                original(**kwargs)
            raise OSError("receipt transport interrupted")
        return original(**kwargs)

    world.table.put_item = fail_receipt
    with pytest.raises(OSError):
        world.policy.promote(world.principal, ref)
    world.table.put_item = original
    world.state.now = deadline + 1
    world.policy = fresh(world)
    if persisted:
        assert world.policy.require_live(world.principal, ref, accepted=True)["state"] == "ACCEPTED"
        assert world.policy.promote(world.principal, ref) == ref
    else:
        for action in (lambda: reserve(world), lambda: world.policy.promote(world.principal, ref),
                       lambda: world.policy.require_live(world.principal, ref, accepted=True)):
            with pytest.raises(RetentionRefused):
                action()
        assert len(world.table.rows) == 1


def test_delayed_receipt_certifies_timely_intent_without_renewal(world):
    ref = reserve(world)
    first = world.policy.require_live(world.principal, ref)
    world.state.now = first["expires_at"] - 1
    original = world.table.put_item

    def delay_receipt(**kwargs):
        if "#PROMOTION#" in kwargs["Item"]["request_revision"]:
            world.state.now = first["expires_at"] + 1
        return original(**kwargs)

    world.table.put_item = delay_receipt
    assert world.policy.promote(world.principal, ref) == ref
    row = fresh(world).require_live(world.principal, ref, accepted=True)
    assert row["expires_at"] == first["ceiling_at"]
    receipt = next(r for k, r in world.table.rows.items() if "#PROMOTION#" in k[1])
    assert receipt["verified_at"] == first["expires_at"] - 1


@pytest.mark.parametrize("mutation", ["intent_generation", "receipt_hash", "receipt_tenant",
                                      "receipt_key", "receipt_boolean_time", "direct_accepted"])
def test_receipt_or_intent_corruption_refuses(world, mutation):
    ref = reserve(world)
    world.policy.promote(world.principal, ref)
    intent = next(r for k, r in world.table.rows.items() if "#PROMOTION#" not in k[1])
    receipt = next(r for k, r in world.table.rows.items() if "#PROMOTION#" in k[1])
    if mutation == "intent_generation":
        intent["generation"] += 1
    elif mutation == "receipt_hash":
        receipt["intent_sha256"] = "0" * 64
    elif mutation == "receipt_tenant":
        receipt["tenant"] = "cottonwood"
    elif mutation == "receipt_key":
        receipt["request_revision"] += "-alias"
    elif mutation == "receipt_boolean_time":
        receipt["verified_at"] = True
    else:
        intent["state"] = "ACCEPTED"
    with pytest.raises(RetentionRefused):
        fresh(world).require_live(world.principal, ref, accepted=True)


def test_receipt_cannot_be_transplanted_to_different_identity(world):
    one = reserve(world, logical="one")
    two = reserve(world, logical="two")
    world.policy.promote(world.principal, one)
    world.policy.promote(world.principal, two)
    rows = [(k, r) for k, r in world.table.rows.items() if "#PROMOTION#" in k[1]]
    world.table.rows[rows[1][0]] = copy.deepcopy(rows[0][1])
    with pytest.raises(RetentionRefused):
        fresh(world).require_live(world.principal, two, accepted=True)


def test_access_revoked_after_intent_never_mints_receipt(world):
    ref = reserve(world)
    original = world.table.put_item

    def revoke(**kwargs):
        result = original(**kwargs)
        if "ExpressionAttributeValues" in kwargs:
            world.state.access = False
        return result

    world.table.put_item = revoke
    with pytest.raises(ReportDenied):
        world.policy.promote(world.principal, ref)
    world.state.access = True
    assert len(world.table.rows) == 1
    with pytest.raises(RetentionRefused):
        fresh(world).require_live(world.principal, ref, accepted=True)


def test_receipt_delay_cannot_outlive_accepted_ceiling(world):
    ref = reserve(world)
    ceiling = world.policy.require_live(world.principal, ref)["ceiling_at"]
    original = world.table.put_item

    def delay(**kwargs):
        if "#PROMOTION#" in kwargs["Item"]["request_revision"]:
            world.state.now = ceiling
        return original(**kwargs)

    world.table.put_item = delay
    with pytest.raises(RetentionExpired):
        world.policy.promote(world.principal, ref)
    with pytest.raises(RetentionExpired):
        fresh(world).require_live(world.principal, ref, accepted=True)
