"""Row 12 -- historical replay, anchored by commit_seq (design sec 2e + sec 3 row 12).

Nothing in the frozen +38 carries INGESTION order, and append-only permits a later batch to carry
an earlier-dated record. Two replays that disagree about whether to include that backfill are both
"as of" the same anchor unless the anchor names an ingestion point -- so every anchor binds to a
commit_seq, and all three forms reduce to `commit_seq <= N`.

The rejects prove an anchor that cannot be bound is REFUSED rather than answered; the accepts prove
the same machinery returns the recorded state, places a later-admitted backfill at its EVENT-TIME
position, and hands back the anchor's commit_seq so a reader can see what it could not know about.
"""
from . import arm
from . import fixtures as fx


def _seeded(store):
    store.admit(fx.minted_pair("ent:alpha", receipt="mr:1"))
    return store.head_commit_seq()


@arm("L-12-replay-frontier")
def replay_frontier_unbindable(store):
    _seeded(store)
    store.replay("frontier", "sf:never-admitted")


@arm("L-12-replay-publication")
def replay_publication_unbindable(store):
    _seeded(store)
    store.admit([fx.source_frontier("sf:1")])
    store.admit([{"record_type": "surface_version", "surface_version_id": "sv:1",
                  "logical_surface_serial": "ent:alpha", "source_frontier_id": "sf:1",
                  "publication_state": "draft", "published_at": "2026-03-01T00:00:00Z"}])
    store.replay("publication", "sv:1")          # bound only by a PUBLISHED version


@arm("L-12-backfill-before-anchor-excluded")
def backfill_before_anchor_excluded(store):
    """The backfill is admitted AFTER the anchor, so a claim that it is inside is refused."""
    _seeded(store)
    store.admit([fx.source_frontier("sf:1")])
    anchor = store.head_commit_seq()
    store.admit([fx.state_observation("obs:backfill", "ent:alpha", "2020-01-01T00:00:00Z")])
    store.replay_expecting("commit_seq", anchor, ["obs:backfill"])


@arm("L-12-replay-matches-recorded-accepted")
def replay_matches_recorded(store):
    seq = _seeded(store)
    result = store.replay_expecting("commit_seq", seq, ["ent:alpha", "mr:1"])
    assert result["anchor_commit_seq"] == seq


@arm("L-12-backfill-after-anchor-included-at-event-time")
def backfill_after_anchor_included(store):
    _seeded(store)
    store.admit([fx.state_observation("obs:late", "ent:alpha", "2026-06-01T00:00:00Z")])
    store.admit([fx.state_observation("obs:backfill", "ent:alpha", "2020-01-01T00:00:00Z")])
    after = store.head_commit_seq()
    result = store.replay_expecting("commit_seq", after, ["obs:backfill", "obs:late"])
    order = [r.get("observation_id") for r in result["estate"] if r.get("observation_id")]
    assert order == ["obs:backfill", "obs:late"], (
        "a backfill included after its anchor takes its EVENT-TIME position, not its "
        "admission position; got %r" % (order,))


@arm("L-12-anchor-commit-seq-printed")
def anchor_commit_seq_printed(store):
    seq = _seeded(store)
    result = store.replay("commit_seq", seq)
    assert result["anchor_commit_seq"] == seq
    assert "counted" in result and result["counted"] == len(result["estate"])
