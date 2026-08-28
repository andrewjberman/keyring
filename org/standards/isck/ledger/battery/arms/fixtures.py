"""Fixture builders. FIXTURES ONLY (WP3-mech-5): every record here is minted by this file.

No fixture reads a production substrate, and none is copied from one. A fixture names its own
`record_type`, which is what makes AC7's carrier promote-or-kill measurable from the fixtures
rather than inferred from prose.
"""


def mint_receipt(receipt_id, entity_serial, authority="0.0.0_AB_MSTR", minted_at="2026-01-01T00:00:00Z"):
    return {"record_type": "mint_receipt", "receipt_id": receipt_id,
            "entity_serial": entity_serial, "minting_authority": authority,
            "minted_at": minted_at}


def entity(entity_serial, authority="0.0.0_AB_MSTR", minted_at="2026-01-01T00:00:00Z", **extra):
    rec = {"record_type": "entity", "entity_serial": entity_serial,
           "minting_authority": authority, "minted_at": minted_at}
    rec.update(extra)
    return rec


def minted_pair(serial, receipt="mr:1", **extra):
    """The bootstrap pair of sec 2c -- ONE batch whose two references resolve against each other."""
    return [mint_receipt(receipt, serial), entity(serial, **extra)]


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
