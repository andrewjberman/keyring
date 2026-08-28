"""Row 5 -- event-to-status projection, with authoritative records staying `authored`.

The frozen +38 requires `status_basis: authored` on all five status-bearing records and +38 is
immutable. So the ledger does NOT introduce a `derived` value -- that was a contract change dressed
as a ledger rule, and the design withdrew it. What it adds is a REJECTED WRITE: an authored value on
a derivable axis that DISAGREES with the fold over the admitted records is refused.

INTERPRETATION, declared here for a reviewer to contest rather than buried. Sec 4's
verification_standing table says a SUPERSEDED assertion "keeps its own authored standing, never
rewritten" -- so an already-admitted record is never re-judged, and a disagreement is only
constructible WITHIN ONE BATCH: {A standing X, B supersedes A standing Y} with X != Y. At that
batch's final state the chain's head is B, so A's authored standing contradicts the chain it is
part of. Across batches there is no disagreement to find, by design. The accept sibling is the
identical batch with X == Y.
"""
from . import arm
from . import fixtures as fx


def _entities(store, *serials):
    fx.open_authority(store)
    for i, serial in enumerate(serials):
        store.admit(fx.minted_pair(serial, receipt="mr:%d" % i), actor=fx.ROOT)
    return store


def _assertion(bid, standing, supersedes=None):
    rec = {"record_type": "bridge_assertion", "bridge_id": bid,
           "subject_entity_serial": "ent:alpha", "object_entity_serial": "ent:beta",
           "verification_standing": standing}
    if supersedes:
        rec["supersedes"] = supersedes
    return rec


def _relation(rid, standing, supersedes=None):
    rec = {"record_type": "identity_relation", "relation_id": rid,
           "subject_serial": "ent:alpha", "object_serial": "ent:beta",
           "relation_type": "candidate_equivalence", "verification_standing": standing}
    if supersedes:
        rec["supersedes"] = supersedes
    return rec


# -- entity.current_status ----------------------------------------------------------------------

@arm("L-05-entity.current_status-authored-agrees-accepted")
def entity_status_agrees(store):
    fx.open_authority(store)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha"),
                 fx.entity("ent:alpha", current_status="active")], actor=fx.ROOT)


@arm("L-05-entity.current_status-authored-vs-derived")
def entity_status_disagrees(store):
    """Authors `retired` with no retirement relation anywhere: the fold derives `active`."""
    fx.open_authority(store)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha"),
                 fx.entity("ent:alpha", current_status="retired")], actor=fx.ROOT)


# -- entity_binding.status ----------------------------------------------------------------------

def _binding(status, **extra):
    rec = {"record_type": "entity_binding", "binding_id": "bind:1",
           "entity_serial": "ent:alpha", "valid_from": "2026-01-01T00:00:00Z", "status": status}
    rec.update(extra)
    return rec


@arm("L-05-entity_binding.status-authored-agrees-accepted")
def binding_status_agrees(store):
    _entities(store, "ent:alpha")
    store.admit([_binding("open"),
                 {"record_type": "binding_event", "event_id": "bev:1", "binding_id": "bind:1",
                  "event_kind": "opened", "occurred_at": "2026-02-01T00:00:00Z"}])


@arm("L-05-entity_binding.status-authored-vs-derived")
def binding_status_disagrees(store):
    """Authors `closed` with no effective `closed` event: the fold derives `open`."""
    _entities(store, "ent:alpha")
    store.admit([_binding("closed"),
                 {"record_type": "binding_event", "event_id": "bev:1", "binding_id": "bind:1",
                  "event_kind": "opened", "occurred_at": "2026-02-01T00:00:00Z"}])


# -- materializer.current_status ------------------------------------------------------------------

@arm("L-05-materializer.current_status-authored-agrees-accepted")
def materializer_status_agrees(store):
    store.admit([fx.materializer("mat:1", current_status="active"),
                 {"record_type": "materializer_version", "version_id": "matv:1",
                  "materializer_serial": "mat:1"}])


@arm("L-05-materializer.current_status-authored-vs-derived")
def materializer_status_disagrees(store):
    """Authors `active` with ZERO versions: the fold's total-coverage default is `unknown`."""
    store.admit([fx.materializer("mat:1", current_status="active")])


# -- the two verification_standing axes -----------------------------------------------------------

@arm("L-05-bridge_assertion.verification_standing-authored-agrees-accepted")
def bridge_standing_agrees(store):
    _entities(store, "ent:alpha", "ent:beta")
    store.admit([_assertion("br:1", "corroborated"),
                 _assertion("br:2", "corroborated", supersedes="br:1")])


@arm("L-05-bridge_assertion.verification_standing-authored-vs-derived")
def bridge_standing_disagrees(store):
    _entities(store, "ent:alpha", "ent:beta")
    store.admit([_assertion("br:1", "contradicted"),
                 _assertion("br:2", "corroborated", supersedes="br:1")])


@arm("L-05-identity_relation.verification_standing-authored-agrees-accepted")
def relation_standing_agrees(store):
    _entities(store, "ent:alpha", "ent:beta")
    store.admit([_relation("rel:1", "corroborated"),
                 _relation("rel:2", "corroborated", supersedes="rel:1")])


@arm("L-05-identity_relation.verification_standing-authored-vs-derived")
def relation_standing_disagrees(store):
    _entities(store, "ent:alpha", "ent:beta")
    store.admit([_relation("rel:1", "unverified"),
                 _relation("rel:2", "corroborated", supersedes="rel:1")])


# -- the projection is NOT a record ----------------------------------------------------------------

@arm("L-05-projection-submitted-as-record-rejected")
def projection_submitted_as_record(store):
    from ledger import surfaces
    _entities(store, "ent:alpha")
    store.admit([surfaces.projection(store.estate(), "entity.current_status", ["ent:alpha"],
                                     {1: 1})])


@arm("L-05-projection-not-mistakable-for-record")
def projection_not_mistakable(store):
    """A projection fails +38 BY CONSTRUCTION -- it has no record_type at all, not a wrong one."""
    from ledger import surfaces
    _entities(store, "ent:alpha")
    proj = surfaces.projection(store.estate(), "entity.current_status", ["ent:alpha"], {1: 1})
    assert "record_type" not in proj, proj
    assert set(proj) == {"axis", "value", "basis", "derived_at_commit_seq"}, proj


@arm("L-05-frozen-authored-record-validates")
def frozen_authored_record_validates(store):
    """A +38-valid record whose authored value AGREES is admitted UNCHANGED -- bytes compared."""
    from ledger import engine
    fx.open_authority(store)
    record = fx.entity("ent:alpha", current_status="active", status_basis="authored")
    store.admit([fx.mint_receipt("mr:1", "ent:alpha"), record], actor=fx.ROOT)
    stored = store.get("ent:alpha")
    assert engine.canonical(stored) == engine.canonical(record), (stored, record)


@arm("L-05-voided-decommission-does-not-retire-accepted")
def voided_decommission_does_not_retire(store):
    """R4-CVO-3, and the arm rows 5 and 13 SHARE.

    A NULLIFIED contest voids the decommission and carries no replacement (R4-CRO-7), so the fold
    falls through to row 3 and reads `active` from the surviving version -- never `retired` from a
    voided event. Queried rather than re-written: an admitted record is never re-judged, so the
    observable is the FOLD, not a second write.
    """
    from ledger import folds
    store.admit([fx.materializer("mat:1"),
                 {"record_type": "materializer_version", "version_id": "matv:1",
                  "materializer_serial": "mat:1"}])
    store.admit([{"record_type": "lifecycle_event", "event_id": "lce:1",
                  "materializer_serial": "mat:1",
                  "event_kind": "materializer_decommissioned",
                  "occurred_at": "2026-02-01T00:00:00Z"}])
    estate = [r for r, _s in store.estate()]
    assert folds.materializer_current_status(estate, "mat:1", store._primary_of, {})[0] == "retired"
    store.admit([{"record_type": "contest_event", "event_id": "ctev:1", "contest_id": "ctev:1",
                  "event_kind": "opened", "target_kind": "lifecycle_event",
                  "target_event_id": "lce:1", "occurred_at": "2026-02-02T00:00:00Z"},
                 {"record_type": "contest_event", "event_id": "ctev:2", "contest_id": "ctev:1",
                  "event_kind": "resolved", "outcome": "nullified",
                  "target_kind": "lifecycle_event", "target_event_id": "lce:1",
                  "occurred_at": "2026-02-03T00:00:00Z"}])
    estate = [r for r, _s in store.estate()]
    derived, basis = folds.materializer_current_status(estate, "mat:1", store._primary_of, {})
    assert derived == "active", (derived, basis)
