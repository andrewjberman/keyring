"""Fixture builders. FIXTURES ONLY (WP3-mech-5): every record here is minted by this file.

No fixture reads a production substrate, and none is copied from one. A fixture names its own
`record_type`, which is what makes AC7's carrier promote-or-kill measurable from the fixtures
rather than inferred from prose.
"""


ROOT = "0.0.0_AB_MSTR"
CTO = "1.0.0_SA_CTO"


def epoch_event(event_id, authority=ROOT, kind="opened", actor=ROOT,
                occurred_at="2020-01-01T00:00:00Z"):
    """An authority epoch transition. `actor` is bound to the submitting principal at admission."""
    return {"record_type": "authority_epoch_event", "event_id": event_id,
            "authority_id": authority, "event_kind": kind, "actor": actor,
            "occurred_at": occurred_at}


def open_authority(store, authority=ROOT, actor=ROOT, event_id=None,
                   occurred_at="2020-01-01T00:00:00Z"):
    """Register a minting authority by OPENING its epoch -- the precondition for any mint.

    Every fixture that mints needs this: sec 3 row 6 refuses a receipt whose minting_authority is
    not OPEN at `minted_at`. Before row 6 was built, every arm minted against an authority that had
    never been registered -- and every one of them was ADMITTED, because the rule did not exist yet.
    """
    eid = event_id or ("aep:open-" + authority.replace(".", "-"))
    if store.get(eid) is None:
        store.admit([epoch_event(eid, authority, "opened", actor, occurred_at)], actor=actor)
    return eid


def bootstrap(store, serial, receipt="mr:1", authority=ROOT, actor=ROOT, **extra):
    """The legal minimum: register the authority, then mint the bootstrap pair."""
    open_authority(store, authority, actor)
    store.admit(minted_pair(serial, receipt, authority=authority, **extra), actor=actor)
    return store


def mint_receipt(receipt_id, entity_serial, authority=ROOT, minted_at="2026-01-01T00:00:00Z"):
    return {"record_type": "mint_receipt", "receipt_id": receipt_id,
            "entity_serial": entity_serial, "minting_authority": authority,
            "minted_at": minted_at}


def entity(entity_serial, authority=ROOT, minted_at="2026-01-01T00:00:00Z", **extra):
    rec = {"record_type": "entity", "entity_serial": entity_serial,
           "minting_authority": authority, "minted_at": minted_at}
    rec.update(extra)
    return rec


def minted_pair(serial, receipt="mr:1", authority=ROOT, **extra):
    """The bootstrap pair of sec 2c -- ONE batch whose two references resolve against each other."""
    return [mint_receipt(receipt, serial, authority=authority),
            entity(serial, authority=authority, **extra)]


def materializer(serial, **extra):
    rec = {"record_type": "materializer", "materializer_serial": serial,
           "current_status": "active"}
    rec.update(extra)
    return rec


def materializer_version(version_id, materializer_serial, **extra):
    rec = {"record_type": "materializer_version", "version_id": version_id,
           "materializer_serial": materializer_serial}
    rec.update(extra)
    return rec


def source_frontier(frontier_id, **extra):
    rec = {"record_type": "source_frontier", "source_frontier_id": frontier_id, "entries": []}
    rec.update(extra)
    return rec


def state_observation(observation_id, entity_serial, observed_at, **extra):
    rec = {"record_type": "state_observation", "observation_id": observation_id,
           "entity_serial": entity_serial, "observed_at": observed_at,
           "producer_serial": "probe:fixture"}
    rec.update(extra)
    return rec
