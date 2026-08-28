"""Row 6 -- mint-receipt authentication, mint-fact equality, and the TOTAL authority-epoch machine.

Nineteen arms, and the eight accepts are what stop this row from being "refuse every mint". The
sharpest pair is `L-06-epoch-actor-spoof-rejected` against
`L-06-cto-close-reopen-as-authenticated-writer-accepted`: the SAME transition, by the SAME named
actor, refused in one and admitted in the other. The only difference is whether the seat that
submitted the batch IS the actor it claims. If the spoof arm passed and that accept arm did not
exist, the ledger could be "secure" by refusing every epoch transition -- and nobody could tell.

AUTHORIZATION IS AN ADMISSION-TIME FACT (R3-CRO-34), which is what
`L-06-backfilled-close-leaves-admitted-mint-accepted` exists to pin down. A `closed` backfilled with
an earlier date does NOT retroactively invalidate a mint that was authorised when it was admitted.
Two different questions live here and collapsing them is the defect: "was this mint authorised?" is
answered at the mint's own commit_seq and never re-asked; "which authorities were open at t?" is
answered by event time on the replay surface.
"""
from . import arm
from . import fixtures as fx

OTHER = "0.4.0_DT_ClientPlatform"          # a real seat, deliberately NOT a root family


def _epoch(event_id, authority, kind="opened", actor=fx.ROOT, occurred_at="2020-01-01T00:00:00Z"):
    return fx.epoch_event(event_id, authority, kind, actor, occurred_at)


# -- the mint half ---------------------------------------------------------------------------

@arm("L-06-entity-without-receipt")
def entity_without_receipt(store):
    fx.open_authority(store)
    store.admit([fx.entity("ent:orphan")])


@arm("L-06-receipted-mint-accepted")
def receipted_mint(store):
    fx.bootstrap(store, "ent:alpha")


@arm("L-06-mint-facts-equal-accepted")
def mint_facts_equal(store):
    """The entity's mint facts EQUAL the receipt's -- the sibling both mismatch arms need."""
    fx.open_authority(store)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha", minted_at="2026-05-05T00:00:00Z"),
                 fx.entity("ent:alpha", minted_at="2026-05-05T00:00:00Z")], actor=fx.ROOT)


@arm("L-06-minted-at-mismatch")
def minted_at_mismatch(store):
    fx.open_authority(store)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha", minted_at="2026-05-05T00:00:00Z"),
                 fx.entity("ent:alpha", minted_at="2026-06-06T00:00:00Z")], actor=fx.ROOT)


@arm("L-06-authority-mismatch")
def authority_mismatch(store):
    fx.open_authority(store)
    fx.open_authority(store, fx.CTO, actor=fx.CTO)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha", authority=fx.ROOT),
                 fx.entity("ent:alpha", authority=fx.CTO)], actor=fx.ROOT)


@arm("L-06-second-receipt-for-serial")
def second_receipt_for_serial(store):
    """TWO receipts for one serial in ONE batch.

    Same batch deliberately: row 1's cross-batch rule compares against the STORE and would fire
    first, and then this arm would be green for row 1's reason rather than row 6's. Row 1 is about a
    serial minted twice across batches and fabrics; row 6 is about one entity carrying two receipts.
    """
    fx.open_authority(store)
    store.admit([fx.mint_receipt("mr:1", "ent:alpha"),
                 fx.mint_receipt("mr:2", "ent:alpha"),
                 fx.entity("ent:alpha")], actor=fx.ROOT)


@arm("L-06-authority-unregistered")
def authority_unregistered(store):
    store.admit(fx.minted_pair("ent:alpha", authority="9.9.9_NEVER_REGISTERED"))


@arm("L-06-authority-closed-before-mint")
def authority_closed_before_mint(store):
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "closed", occurred_at="2025-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit(fx.minted_pair("ent:alpha", authority="auth:x"), actor=fx.ROOT)


@arm("L-06-authority-in-epoch-accepted")
def authority_in_epoch(store):
    """The same shape as the arm above, minted INSIDE the open interval."""
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit(fx.minted_pair("ent:alpha", authority="auth:x"), actor=fx.ROOT)


@arm("L-06-backfilled-close-leaves-admitted-mint-accepted")
def backfilled_close_leaves_mint(store):
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit(fx.minted_pair("ent:alpha", authority="auth:x"), actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "closed", occurred_at="2025-01-01T00:00:00Z")],
                actor=fx.ROOT)


# -- the epoch machine -----------------------------------------------------------------------

@arm("L-06-mstr-genesis-open-accepted")
def mstr_genesis_open(store):
    store.admit([_epoch("aep:1", "auth:x", "opened", actor=fx.ROOT)], actor=fx.ROOT)


@arm("L-06-cto-close-reopen-as-authenticated-writer-accepted")
def cto_close_reopen(store):
    """CTO closes and reopens, submitting as itself -- the legal twin of the spoof arm."""
    store.admit([_epoch("aep:1", "auth:x", "opened", actor=fx.ROOT)], actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "closed", actor=fx.CTO,
                        occurred_at="2021-01-01T00:00:00Z")], actor=fx.CTO)
    store.admit([_epoch("aep:3", "auth:x", "opened", actor=fx.CTO,
                        occurred_at="2022-01-01T00:00:00Z")], actor=fx.CTO)


@arm("L-06-reopened-authority-accepted")
def reopened_authority(store):
    """Closed then opened again: two intervals, no overlap."""
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "closed", occurred_at="2021-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:3", "auth:x", "opened", occurred_at="2022-01-01T00:00:00Z")],
                actor=fx.ROOT)


@arm("L-06-same-time-open-close-ordered-accepted")
def same_time_open_close(store):
    """Identical occurred_at: the tie breaks on commit_seq then id, so open precedes close."""
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z"),
                 _epoch("aep:2", "auth:x", "closed", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)


@arm("L-06-overlapping-epoch-rejected")
def overlapping_epoch(store):
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "opened", occurred_at="2021-01-01T00:00:00Z")],
                actor=fx.ROOT)


@arm("L-06-close-without-open-rejected")
def close_without_open(store):
    store.admit([_epoch("aep:1", "auth:x", "closed", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)


@arm("L-06-duplicate-close-rejected")
def duplicate_close(store):
    store.admit([_epoch("aep:1", "auth:x", "opened", occurred_at="2020-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:2", "auth:x", "closed", occurred_at="2021-01-01T00:00:00Z")],
                actor=fx.ROOT)
    store.admit([_epoch("aep:3", "auth:x", "closed", occurred_at="2022-01-01T00:00:00Z")],
                actor=fx.ROOT)


@arm("L-06-unauthorized-epoch-transition-rejected")
def unauthorized_epoch_transition(store):
    """A non-root seat opening an epoch AS ITSELF: the actor binding passes, the family fails."""
    store.admit([_epoch("aep:1", "auth:x", "opened", actor=OTHER)], actor=OTHER)


@arm("L-06-epoch-actor-spoof-rejected")
def epoch_actor_spoof(store):
    """A trusted-looking `actor` string written by another writer.

    The refusal must come from the BINDING, not the family predicate -- a spoofed actor passes the
    family test by construction, because it was chosen to.
    """
    store.admit([_epoch("aep:1", "auth:x", "opened", actor=fx.ROOT)], actor=OTHER)
