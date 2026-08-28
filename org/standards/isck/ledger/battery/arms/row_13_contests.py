"""Row 13 -- contest integrity. The three limit-11 promises, enforced as REJECTED WRITES.

Convention throughout: a contest's `contest_id` IS the event_id of its own `opened` event, which is
what makes the STRICT-CONDITIONAL reference in sec 2d resolve.

The eleven accepts are not padding. `L-13-dismissed-then-new-challenge-accepted` and
`L-13-merge-survivor-resolves-later-accepted` exist because `dismissed` and `merged` consume NO
corrective slot (R4-CVO-4) -- without them, "one corrective outcome per event" would be
indistinguishable from "one contest per event ever", and a ledger that refused every second
challenge would pass the reject arm.
"""
from . import arm
from . import fixtures as fx

MAT = "mat:1"
BINDING = "bind:1"


def _seed(store):
    fx.open_authority(store)
    for i, serial in enumerate(("ent:alpha", "ent:beta")):
        store.admit(fx.minted_pair(serial, receipt="mr:%d" % i), actor=fx.ROOT)
    store.admit([fx.materializer(MAT),
                 {"record_type": "materializer_version", "version_id": "matv:1",
                  "materializer_serial": MAT}])
    store.admit([{"record_type": "entity_binding", "binding_id": BINDING,
                  "entity_serial": "ent:alpha", "valid_from": "2026-01-01T00:00:00Z"},
                 _bev("bev:1", "opened")])
    return store


def _bev(eid, kind, binding=BINDING, at="2026-02-01T00:00:00Z"):
    return {"record_type": "binding_event", "event_id": eid, "binding_id": binding,
            "event_kind": kind, "occurred_at": at}


def _lce(eid, kind="materializer_decommissioned", serial=MAT, at="2026-02-01T00:00:00Z"):
    return {"record_type": "lifecycle_event", "event_id": eid, "materializer_serial": serial,
            "event_kind": kind, "occurred_at": at}


def _open(eid, kind="entity", at="2026-02-02T00:00:00Z", **target):
    rec = {"record_type": "contest_event", "event_id": eid, "contest_id": eid,
           "event_kind": "opened", "target_kind": kind, "occurred_at": at}
    rec.update(target)
    return rec


def _resolve(eid, contest_id, outcome, kind="entity", at="2026-02-05T00:00:00Z", **extra):
    rec = {"record_type": "contest_event", "event_id": eid, "contest_id": contest_id,
           "event_kind": "resolved", "outcome": outcome, "target_kind": kind, "occurred_at": at}
    rec.update(extra)
    return rec


def _entity_open(eid="ctev:1", serial="ent:alpha", at="2026-02-02T00:00:00Z"):
    return _open(eid, "entity", at, target_entity_serial=serial)


def _entity_resolve(eid, contest_id="ctev:1", outcome="dismissed", serial="ent:alpha", **extra):
    return _resolve(eid, contest_id, outcome, "entity", target_entity_serial=serial, **extra)


# -- opening / resolution pairing --------------------------------------------------------------

@arm("L-13-opened-then-resolved-accepted")
def opened_then_resolved(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2")])


@arm("L-13-resolved-without-opened")
def resolved_without_opened(store):
    """The contest_id RESOLVES -- to a record that is not an opening.

    Pointing it at a never-admitted id would be refused by row 2 first, and the arm would carry a
    row-13 name over a row-2 test. Found by mutating row 13 off and watching which arms failed to
    turn.
    """
    _seed(store)
    store.admit([_entity_open("ctev:a")])
    store.admit([_resolve("ctev:2", "ctev:a", "dismissed", "entity", at="2026-02-05T00:00:00Z",
                          target_entity_serial="ent:alpha")])
    store.admit([_resolve("ctev:3", "ctev:2", "dismissed", "entity", at="2026-02-06T00:00:00Z",
                          target_entity_serial="ent:alpha")])


@arm("L-13-duplicate-opened")
def duplicate_opened(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([dict(_entity_open("ctev:2"), contest_id="ctev:1")])


@arm("L-13-duplicate-resolved")
def duplicate_resolved(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2")])
    store.admit([_entity_resolve("ctev:3", at="2026-02-06T00:00:00Z")])


@arm("L-13-resolved-target-differs")
def resolved_target_differs(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2", serial="ent:beta")])


@arm("L-13-resolved-before-opened-rejected")
def resolved_before_opened(store):
    _seed(store)
    store.admit([_entity_open(at="2026-03-01T00:00:00Z")])
    store.admit([_entity_resolve("ctev:2", at="2026-02-01T00:00:00Z")])


@arm("L-13-same-instant-pair-ordered-by-id-accepted")
def same_instant_pair(store):
    """Opened and resolved share an instant AND a batch; the ID makes the order total."""
    _seed(store)
    store.admit([_entity_open(at="2026-02-02T00:00:00Z"),
                 _entity_resolve("ctev:2", at="2026-02-02T00:00:00Z")])


@arm("L-13-dismissed-accepted")
def dismissed(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2", outcome="dismissed")])


@arm("L-13-dismissed-then-new-challenge-accepted")
def dismissed_then_new_challenge(store):
    """A dismissal consumes no corrective slot, so the same target may be challenged again."""
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_resolve("ctev:2", "ctev:1", "dismissed", "lifecycle_event",
                          target_event_id="lce:1")])
    store.admit([_open("ctev:3", "lifecycle_event", "2026-02-06T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_resolve("ctev:4", "ctev:3", "dismissed", "lifecycle_event",
                          at="2026-02-07T00:00:00Z", target_event_id="lce:1")])


# -- upheld consequences -------------------------------------------------------------------------

@arm("L-13-upheld-with-later-same-target-consequence-accepted")
def upheld_with_later_consequence(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_type": "retirement", "occurred_at": "2026-02-04T00:00:00Z"},
                 _entity_resolve("ctev:2", outcome="upheld", consequence_refs=["rel:1"])])


@arm("L-13-consequence-unparsable")
def consequence_unparsable(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2", outcome="upheld",
                                 consequence_refs=["not-a-record-id"])])


@arm("L-13-consequence-unresolved")
def consequence_unresolved(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2", outcome="upheld",
                                 consequence_refs=["rel:never-admitted"])])


@arm("L-13-consequence-wrong-target")
def consequence_wrong_target(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:beta", "object_serial": "ent:alpha",
                  "relation_type": "retirement", "occurred_at": "2026-02-04T00:00:00Z"},
                 _entity_resolve("ctev:2", outcome="upheld", consequence_refs=["rel:1"])])


@arm("L-13-consequence-predates-opening")
def consequence_predates_opening(store):
    _seed(store)
    store.admit([_entity_open(at="2026-02-10T00:00:00Z")])
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_type": "retirement", "occurred_at": "2026-01-01T00:00:00Z"},
                 _entity_resolve("ctev:2", outcome="upheld", at="2026-02-11T00:00:00Z",
                                 consequence_refs=["rel:1"])])


# -- event corrections ----------------------------------------------------------------------------

@arm("L-13-event-upheld-with-single-replacement-accepted")
def event_upheld_single_replacement(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_lce("lce:2", at="2026-02-05T00:00:00Z"),
                 _resolve("ctev:2", "ctev:1", "upheld", "lifecycle_event",
                          target_event_id="lce:1", consequence_refs=["lce:2"])])


@arm("L-13-event-upheld-without-single-replacement-rejected")
def event_upheld_without_single_replacement(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_lce("lce:2", at="2026-02-05T00:00:00Z"),
                 {"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_type": "candidate_equivalence",
                  "occurred_at": "2026-02-05T00:00:00Z"},
                 _resolve("ctev:2", "ctev:1", "upheld", "lifecycle_event",
                          target_event_id="lce:1", consequence_refs=["lce:2", "rel:1"])])


@arm("L-13-event-replacement-kind-or-key-differs-rejected")
def event_replacement_kind_differs(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_lce("lce:2", kind="materializer_superseded", at="2026-02-05T00:00:00Z"),
                 _resolve("ctev:2", "ctev:1", "upheld", "lifecycle_event",
                          target_event_id="lce:1", consequence_refs=["lce:2"])])


@arm("L-13-event-nullified-accepted")
def event_nullified(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_resolve("ctev:2", "ctev:1", "nullified", "lifecycle_event",
                          target_event_id="lce:1")])


@arm("L-13-nullified-on-non-event-rejected")
def nullified_on_non_event(store):
    _seed(store)
    store.admit([_entity_open()])
    store.admit([_entity_resolve("ctev:2", outcome="nullified")])


@arm("L-13-nullified-with-consequence-rejected")
def nullified_with_consequence(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_type": "candidate_equivalence",
                  "occurred_at": "2026-02-05T00:00:00Z"},
                 _resolve("ctev:2", "ctev:1", "nullified", "lifecycle_event",
                          target_event_id="lce:1", consequence_refs=["rel:1"])])


@arm("L-13-second-corrective-outcome-rejected")
def second_corrective_outcome(store):
    _seed(store)
    store.admit([_lce("lce:1")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-02T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_resolve("ctev:2", "ctev:1", "nullified", "lifecycle_event",
                          target_event_id="lce:1")])
    store.admit([_open("ctev:3", "lifecycle_event", "2026-02-06T00:00:00Z",
                       target_event_id="lce:1")])
    store.admit([_resolve("ctev:4", "ctev:3", "nullified", "lifecycle_event",
                          at="2026-02-07T00:00:00Z", target_event_id="lce:1")])


@arm("L-13-opened-before-target-event-rejected")
def opened_before_target_event(store):
    _seed(store)
    store.admit([_lce("lce:1", at="2026-03-01T00:00:00Z")])
    store.admit([_open("ctev:1", "lifecycle_event", "2026-02-01T00:00:00Z",
                       target_event_id="lce:1")])


# -- merges ---------------------------------------------------------------------------------------

def _merge_pair(store, survivor_at="2026-02-02T00:00:00Z"):
    store.admit([_entity_open("ctev:s", at=survivor_at)])
    store.admit([_entity_open("ctev:1", at="2026-02-03T00:00:00Z")])


@arm("L-13-merged-into-open-same-target-accepted")
def merged_into_open_same_target(store):
    _seed(store)
    _merge_pair(store)
    store.admit([_entity_resolve("ctev:2", outcome="merged", surviving_contest_id="ctev:s")])


@arm("L-13-merge-survivor-resolves-later-accepted")
def merge_survivor_resolves_later(store):
    """The survivor of a merge resolves later on the same target -- a merge consumes no slot."""
    _seed(store)
    _merge_pair(store)
    store.admit([_entity_resolve("ctev:2", outcome="merged", surviving_contest_id="ctev:s")])
    store.admit([_resolve("ctev:3", "ctev:s", "dismissed", "entity",
                          at="2026-02-08T00:00:00Z", target_entity_serial="ent:alpha")])


@arm("L-13-merged-into-unopened")
def merged_into_unopened(store):
    _seed(store)
    store.admit([_entity_open("ctev:a")])
    store.admit([_resolve("ctev:r", "ctev:a", "dismissed", "entity", at="2026-02-04T00:00:00Z",
                          target_entity_serial="ent:alpha")])
    store.admit([_entity_open("ctev:1", at="2026-02-05T00:00:00Z")])
    store.admit([_entity_resolve("ctev:2", at="2026-02-06T00:00:00Z", outcome="merged",
                                 surviving_contest_id="ctev:r")])


@arm("L-13-merged-into-self")
def merged_into_self(store):
    _seed(store)
    store.admit([_entity_open("ctev:1", at="2026-02-03T00:00:00Z")])
    store.admit([_entity_resolve("ctev:2", outcome="merged", surviving_contest_id="ctev:1")])


@arm("L-13-merged-into-resolved-rejected")
def merged_into_resolved(store):
    _seed(store)
    _merge_pair(store)
    store.admit([_resolve("ctev:9", "ctev:s", "dismissed", "entity",
                          at="2026-02-04T00:00:00Z", target_entity_serial="ent:alpha")])
    store.admit([_entity_resolve("ctev:2", outcome="merged", at="2026-02-06T00:00:00Z",
                                 surviving_contest_id="ctev:s")])


@arm("L-13-merged-cross-target-rejected")
def merged_cross_target(store):
    _seed(store)
    store.admit([_entity_open("ctev:s", serial="ent:beta", at="2026-02-02T00:00:00Z")])
    store.admit([_entity_open("ctev:1", at="2026-02-03T00:00:00Z")])
    store.admit([_entity_resolve("ctev:2", outcome="merged", surviving_contest_id="ctev:s")])


@arm("L-13-merge-cycle-rejected")
def merge_cycle(store):
    """A into B and B into A leaves NO survivor -- and every reference resolves."""
    _seed(store)
    store.admit([_entity_open("ctev:a", at="2026-02-02T00:00:00Z")])
    store.admit([_entity_open("ctev:b", at="2026-02-03T00:00:00Z")])
    store.admit([_resolve("ctev:r1", "ctev:a", "merged", "entity", at="2026-02-05T00:00:00Z",
                          target_entity_serial="ent:alpha", surviving_contest_id="ctev:b")])
    store.admit([_resolve("ctev:r2", "ctev:b", "merged", "entity", at="2026-02-06T00:00:00Z",
                          target_entity_serial="ent:alpha", surviving_contest_id="ctev:a")])
