"""Rows 8-11 -- frontier coordinates, run consistency, admissible publication, single HEADs.

Row 8's collision is the one the CONTRACT CANNOT SEE: two raw strings that differ, normalising to
one canonical coordinate with different versions. Any check that compares raw keys passes it.

Row 11's three accept arms are doing more work than they look like. `L-11-two-heads` proves the
ledger refuses an ambiguous HEAD; the two tie arms prove it still ANSWERS when a tie is real --
once on commit_seq, once on the id when even that is shared. A head selector that returned "no
answer" whenever two versions shared a publication instant would pass the reject arm and be useless.
"""
from . import arm
from . import fixtures as fx

SURFACE = "ent:logical-surface"


def _seed(store):
    fx.open_authority(store)
    for i, serial in enumerate(("ent:alpha", SURFACE)):
        store.admit(fx.minted_pair(serial, receipt="mr:%d" % i), actor=fx.ROOT)
    store.admit([fx.materializer("mat:1")])
    store.admit([{"record_type": "materializer_version", "version_id": "matv:1",
                  "materializer_serial": "mat:1"}])
    return store


def _frontier(fid, entries, version="v1"):
    return {"record_type": "source_frontier", "source_frontier_id": fid,
            "normalization_version": version, "entries": entries}


def _entry(key, entry_version, observed_at=None, serial="ent:alpha"):
    e = {"source_serial": serial, "source_native_key": key, "entry_version": entry_version}
    if observed_at:
        e["observed_at"] = observed_at
    return e


def _run(rid, frontier="sf:1", result="succeeded", completed="2026-02-02T00:00:00Z",
         started="2026-02-01T00:00:00Z", outputs=None):
    rec = {"record_type": "materialization_run", "run_id": rid, "materializer_serial": "mat:1",
           "materializer_version_id": "matv:1", "source_frontier_id": frontier,
           "started_at": started, "run_result": result}
    if completed:
        rec["completed_at"] = completed
    if outputs:
        rec["output_surface_version_ids"] = outputs
    return rec


def _surface(sid, run="run:1", frontier="sf:1", state="draft", published_at=None,
             promoter="1.0.0_SA_CTO", version="matv:1"):
    rec = {"record_type": "surface_version", "surface_version_id": sid,
           "logical_surface_serial": SURFACE, "producing_run_id": run,
           "source_frontier_id": frontier, "materializer_version_id": version,
           "publication_state": state}
    if published_at:
        rec["published_at"] = published_at
    if promoter and state == "published":
        rec["promoted_by"] = promoter
    return rec


# -- row 8 -------------------------------------------------------------------------------------

@arm("L-08-distinct-normalized-keys-accepted")
def distinct_normalized_keys(store):
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1"), _entry("beta/two", "v1")])])


@arm("L-08-normalized-collision")
def normalized_collision(store):
    """Two RAW strings that differ; one canonical coordinate; two versions."""
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("Alpha/One", "v1"), _entry("  alpha/one ", "v2")])])


@arm("L-08-observed-before-start-accepted")
def observed_before_start(store):
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1",
                                           observed_at="2026-01-01T00:00:00Z")])])
    store.admit([_run("run:1")])


@arm("L-08-observed-after-start")
def observed_after_start(store):
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1",
                                           observed_at="2026-03-01T00:00:00Z")])])
    store.admit([_run("run:1")])


# -- row 9 -------------------------------------------------------------------------------------

@arm("L-09-consistent-triple-accepted")
def consistent_triple(store):
    """The run and its outputs land in ONE batch.

    They have to: a run's `output_surface_version_ids` is STRICT, so a run that declares an output
    admitted in a LATER batch has a reference that does not resolve at ITS final state. The mutual
    reference between a run and its surface is the same shape as the sec 2c bootstrap pair.
    """
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1")])])
    store.admit([_run("run:1", outputs=["sv:1"]), _surface("sv:1")])


@arm("L-09-membership")
def membership(store):
    """sv:1 names run:1 as producer; run:1's outputs list a DIFFERENT surface."""
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1")])])
    store.admit([_run("run:1", outputs=["sv:other"]), _surface("sv:other"), _surface("sv:1")])


@arm("L-09-frontier-disagree")
def frontier_disagree(store):
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1")]),
                 _frontier("sf:2", [_entry("beta/two", "v1")])])
    store.admit([_run("run:1", frontier="sf:1", outputs=["sv:1"]),
                 _surface("sv:1", frontier="sf:2")])


@arm("L-09-version-disagree")
def version_disagree(store):
    _seed(store)
    store.admit([{"record_type": "materializer_version", "version_id": "matv:2",
                  "materializer_serial": "mat:1", "supersedes": "matv:1"}])
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1")])])
    store.admit([_run("run:1", outputs=["sv:1"]), _surface("sv:1", version="matv:2")])


# -- row 10 ------------------------------------------------------------------------------------

def _publishable(store, run_result="succeeded", completed="2026-02-02T00:00:00Z"):
    """A run with NO declared outputs -- so each arm below admits its own surfaces freely.

    Row 9's membership rule only bites when a run DECLARES outputs (sec 2d: "items when present"),
    which is what lets rows 10 and 11 vary publication without also restating run membership.
    """
    _seed(store)
    store.admit([_frontier("sf:1", [_entry("alpha/one", "v1")])])
    store.admit([_run("run:1", result=run_result, completed=completed)])


@arm("L-10-unpublished-accepted")
def unpublished_accepted(store):
    _publishable(store)
    store.admit([_surface("sv:1")])


@arm("L-10-publish-after-succeeded-accepted")
def publish_after_succeeded(store):
    _publishable(store)
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z")])


@arm("L-10-publish-from-failed")
def publish_from_failed(store):
    _publishable(store, run_result="failed")
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z")])


@arm("L-10-publish-before-complete")
def publish_before_complete(store):
    _publishable(store, completed=None)
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z")])


@arm("L-10-no-promoter")
def no_promoter(store):
    _publishable(store)
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z",
                          promoter=None)])


# -- row 11 ------------------------------------------------------------------------------------

@arm("L-11-projection-with-basis-accepted")
def projection_with_basis(store):
    from ledger import surfaces
    _seed(store)
    proj = surfaces.projection(store.estate(), "entity.current_status", ["ent:alpha"], {1: 1})
    assert proj["basis"] == ["ent:alpha"], proj


@arm("L-11-projection-without-basis")
def projection_without_basis(store):
    """A derived value that cannot show WHAT it was derived from is refused at construction."""
    from ledger import engine, surfaces
    _seed(store)
    try:
        surfaces.projection(store.estate(), "entity.current_status", [], {})
    except ValueError as exc:
        raise engine.Rejected(str(exc), "a projection must carry the admitted records it was "
                                        "derived from (sec 2, sec 5.4)")


@arm("L-11-two-heads")
def two_heads(store):
    """Two published versions that tie on EVERY ordering field would be two heads.

    Constructed as the same publication instant, the same batch (so one commit_seq) AND the same
    id -- which the store refuses earlier as a duplicate primary id. That refusal IS the reason a
    two-head state is unreachable, and the arm records it rather than inventing a second mechanism.
    """
    _publishable(store)
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z")])
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z",
                          frontier="sf:1", version="matv:1", promoter="0.0.0_AB_MSTR")])


@arm("L-11-tied-publication-head-deterministic")
def tied_publication_head(store):
    """Same published_at, DIFFERENT batches: commit_seq breaks the tie, and it says so."""
    _publishable(store)
    store.admit([_run("run:2")])
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z")])
    store.admit([_surface("sv:2", run="run:2", state="published",
                          published_at="2026-02-03T00:00:00Z")])
    head, tie = store.head(SURFACE)
    assert head is not None and tie == "commit_seq", (head, tie)


@arm("L-11-same-batch-tie-broken-by-id")
def same_batch_tie_broken_by_id(store):
    """Same instant AND same commit_seq: the id is the last resort that keeps the answer TOTAL."""
    _publishable(store)
    store.admit([_run("run:2")])
    store.admit([_surface("sv:1", state="published", published_at="2026-02-03T00:00:00Z"),
                 _surface("sv:2", run="run:2", state="published",
                          published_at="2026-02-03T00:00:00Z")])
    head, tie = store.head(SURFACE)
    assert tie == "surface_version_id", (head, tie)
    assert head["surface_version_id"] == "sv:2", head
