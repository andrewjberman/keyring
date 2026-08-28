"""Row 7 -- relation direction, cycles and forks on EVERY chain, and the lifecycle machine.

Every reject here RESOLVES EVERY REFERENCE. {A supersedes B, B supersedes A} is an atomic batch
that dangles nothing and has ZERO heads; two roots dangle nothing and have TWO. A referential
checker passes both. What they break is "which one is current?", and that question ends up with no
answer rather than a wrong one -- which is why it is refused at the write instead of resolved at the
read.

The eight accepts are the other half of every one of those: a LINEAR chain is admitted, a SINGLE
root is admitted, `superseded -> decommissioned` is admitted. Without them "no cycles" and "no
chains at all" are the same ledger.
"""
from . import arm
from . import fixtures as fx

MAT = "mat:1"


def _relation(rid, subject, obj, rtype="canonicalized_as"):
    return {"record_type": "identity_relation", "relation_id": rid,
            "subject_serial": subject, "object_serial": obj, "relation_type": rtype}


def _version(vid, supersedes=None, serial=MAT):
    rec = {"record_type": "materializer_version", "version_id": vid,
           "materializer_serial": serial}
    if supersedes:
        rec["supersedes"] = supersedes
    return rec


def _assertion(bid, supersedes=None):
    rec = {"record_type": "bridge_assertion", "bridge_id": bid,
           "subject_entity_serial": "ent:alpha", "object_entity_serial": "ent:beta"}
    if supersedes:
        rec["supersedes"] = supersedes
    return rec


def _lifecycle(eid, kind, serial=MAT, occurred_at="2026-02-01T00:00:00Z"):
    return {"record_type": "lifecycle_event", "event_id": eid, "materializer_serial": serial,
            "event_kind": kind, "occurred_at": occurred_at}


def _seed(store, entities=("ent:alpha", "ent:beta", "ent:gamma")):
    fx.open_authority(store)
    for i, serial in enumerate(entities):
        store.admit(fx.minted_pair(serial, receipt="mr:%d" % i), actor=fx.ROOT)
    store.admit([fx.materializer(MAT)])
    return store


# -- relation chains ---------------------------------------------------------------------------

@arm("L-07-acyclic-chain-accepted")
def acyclic_chain(store):
    _seed(store)
    store.admit([_relation("rel:1", "ent:alpha", "ent:beta"),
                 _relation("rel:2", "ent:beta", "ent:gamma")])


@arm("L-07-retirement-accepted")
def retirement(store):
    _seed(store)
    store.admit([_relation("rel:1", "ent:alpha", "ent:beta", "retirement")])


@arm("L-07-cycle-canonicalize")
def cycle_canonicalize(store):
    _seed(store)
    store.admit([_relation("rel:1", "ent:alpha", "ent:beta"),
                 _relation("rel:2", "ent:beta", "ent:alpha")])


@arm("L-07-cycle-merge")
def cycle_merge(store):
    _seed(store)
    store.admit([_relation("rel:1", "ent:alpha", "ent:beta", "merged_into"),
                 _relation("rel:2", "ent:beta", "ent:alpha", "merged_into")])


@arm("L-07-unknown-kind")
def unknown_kind(store):
    _seed(store)
    store.admit([_relation("rel:1", "ent:alpha", "ent:beta", "absorbed_by")])


# -- assertion supersedes chains ---------------------------------------------------------------

@arm("L-07-linear-assertion-chain-in-one-batch-accepted")
def linear_assertion_chain(store):
    """A whole chain in ONE batch: legal precisely because sec 2c resolves at final state."""
    _seed(store)
    store.admit([_assertion("br:1"), _assertion("br:2", "br:1"), _assertion("br:3", "br:2")])


@arm("L-07-branching-supersession-rejected")
def branching_supersession(store):
    _seed(store)
    store.admit([_assertion("br:1")])
    store.admit([_assertion("br:2", "br:1"), _assertion("br:3", "br:1")])


@arm("L-07-cycle-assertion-supersedes-rejected")
def cycle_assertion_supersedes(store):
    """The atomic batch that resolves every reference and has ZERO heads."""
    _seed(store)
    store.admit([_assertion("br:1", "br:2"), _assertion("br:2", "br:1")])


# -- materializer_version chains ---------------------------------------------------------------

@arm("L-07-single-root-accepted")
def single_root(store):
    _seed(store)
    store.admit([_version("matv:1")])


@arm("L-07-linear-version-chain-accepted")
def linear_version_chain(store):
    _seed(store)
    store.admit([_version("matv:1")])
    store.admit([_version("matv:2", "matv:1")])
    store.admit([_version("matv:3", "matv:2")])


@arm("L-07-second-root-rejected")
def second_root(store):
    _seed(store)
    store.admit([_version("matv:1")])
    store.admit([_version("matv:2")])            # no supersedes, and a version already exists


@arm("L-07-fork-materializer-version-rejected")
def fork_version(store):
    _seed(store)
    store.admit([_version("matv:1")])
    store.admit([_version("matv:2", "matv:1"), _version("matv:3", "matv:1")])


@arm("L-07-cycle-version-supersedes-rejected")
def cycle_version_supersedes(store):
    _seed(store)
    store.admit([_version("matv:1", "matv:2"), _version("matv:2", "matv:1")])


@arm("L-07-cross-materializer-supersedes-rejected")
def cross_materializer_supersedes(store):
    _seed(store)
    store.admit([fx.materializer("mat:2")])
    store.admit([_version("matv:1")])
    store.admit([_version("matv:9", serial="mat:2", supersedes="matv:1")])


# -- the lifecycle machine ----------------------------------------------------------------------

@arm("L-07-single-process-supersession-accepted")
def single_process_supersession(store):
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_superseded")])


@arm("L-07-superseded-then-decommissioned-accepted")
def superseded_then_decommissioned(store):
    """The legal order. Decommission is terminal, not exclusive."""
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_superseded")])
    store.admit([_lifecycle("lce:2", "materializer_decommissioned",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-second-process-supersession-rejected")
def second_process_supersession(store):
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_superseded")])
    store.admit([_lifecycle("lce:2", "materializer_superseded",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-two-effective-successors-same-batch-rejected")
def two_successors_same_batch(store):
    """Both arrive together, so neither is 'second' by arrival -- only a final-state machine sees it."""
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_superseded"),
                 _lifecycle("lce:2", "materializer_superseded",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-second-decommission-rejected")
def second_decommission(store):
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_decommissioned")])
    store.admit([_lifecycle("lce:2", "materializer_decommissioned",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-transition-after-decommission-rejected")
def transition_after_decommission(store):
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_decommissioned")])
    store.admit([_lifecycle("lce:2", "materializer_superseded",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-replacement-without-upheld-contest-rejected")
def replacement_without_upheld_contest(store):
    """A voided decommission and a stand-in that no upheld contest names.

    The voiding here is a `nullified` contest, which by R4-CRO-7 carries NO consequence. So the
    replacement cannot be anyone's consequence, and appending one anyway is exactly "correcting an
    event by adding another".
    """
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_decommissioned")])
    store.admit([{"record_type": "contest_event", "event_id": "ctev:1", "contest_id": "ctev:1",
                  "event_kind": "opened", "target_kind": "lifecycle_event",
                  "target_event_id": "lce:1", "occurred_at": "2026-02-02T00:00:00Z"},
                 {"record_type": "contest_event", "event_id": "ctev:2", "contest_id": "ctev:1",
                  "event_kind": "resolved", "outcome": "nullified",
                  "target_kind": "lifecycle_event", "target_event_id": "lce:1",
                  "occurred_at": "2026-02-03T00:00:00Z"}])
    store.admit([_lifecycle("lce:2", "materializer_decommissioned",
                            occurred_at="2026-03-01T00:00:00Z")])


@arm("L-07-voided-then-replacement-accepted")
def voided_then_replacement(store):
    """The legal correction: an UPHELD contest whose single consequence IS the replacement."""
    _seed(store)
    store.admit([_lifecycle("lce:1", "materializer_decommissioned")])
    store.admit([{"record_type": "contest_event", "event_id": "ctev:1", "contest_id": "ctev:1",
                  "event_kind": "opened", "target_kind": "lifecycle_event",
                  "target_event_id": "lce:1", "occurred_at": "2026-02-02T00:00:00Z"}])
    store.admit([_lifecycle("lce:2", "materializer_decommissioned",
                            occurred_at="2026-03-01T00:00:00Z"),
                 {"record_type": "contest_event", "event_id": "ctev:2", "contest_id": "ctev:1",
                  "event_kind": "resolved", "outcome": "upheld",
                  "target_kind": "lifecycle_event", "target_event_id": "lce:1",
                  "consequence_refs": ["lce:2"], "occurred_at": "2026-03-01T00:00:00Z"}])
