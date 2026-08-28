"""Row 3 -- append-only retention (design sec 3 row 3).

Four refusals: delete; a write carrying an existing primary id with DIFFERENT bytes; and
`superseded_by` / `materializer.superseded_by_version` populated on any write after creation
(they are DERIVED projections, sec 2b -- never client-authored state).

The accept siblings are the discriminating half: appending a NEW record is admitted, and a rewrite
with the SAME id and the SAME bytes is idempotent, not a mutation. Without those two, "reject a
second write of an existing id" and "reject every second write" are indistinguishable.
"""
from . import arm
from . import fixtures as fx


@arm("L-03-delete")
def delete_refused(store):
    store.admit(fx.minted_pair("ent:alpha"))
    store.delete("ent:alpha")


@arm("L-03-inplace-mutation")
def inplace_mutation(store):
    store.admit(fx.minted_pair("ent:alpha"))
    store.admit([fx.entity("ent:alpha", minted_at="2099-12-31T00:00:00Z")])   # same id, new bytes


@arm("L-03-superseded-by-written")
def superseded_by_written(store):
    store.admit(fx.minted_pair("ent:alpha", receipt="mr:1"))
    store.admit(fx.minted_pair("ent:beta", receipt="mr:2"))
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_kind": "canonicalization"}])
    store.admit([{"record_type": "identity_relation", "relation_id": "rel:1",
                  "subject_serial": "ent:alpha", "object_serial": "ent:beta",
                  "relation_kind": "canonicalization", "superseded_by": "rel:1"}])


@arm("L-03-superseded-by-version-written")
def superseded_by_version_written(store):
    store.admit([fx.materializer("mat:1")])
    store.admit([fx.materializer_version("matv:1", "mat:1")])
    store.admit([fx.materializer("mat:1", superseded_by_version="matv:1")])


@arm("L-03-append-accepted")
def append_accepted(store):
    store.admit(fx.minted_pair("ent:alpha", receipt="mr:1"))
    store.admit(fx.minted_pair("ent:beta", receipt="mr:2"))


@arm("L-03-idempotent-rewrite-accepted")
def idempotent_rewrite(store):
    """SAME id, SAME bytes -- a repeat delivery is not a mutation and must not be refused."""
    pair = fx.minted_pair("ent:alpha")
    store.admit(pair)
    store.admit([dict(r) for r in pair])
