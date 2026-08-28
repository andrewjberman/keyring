#!/usr/bin/env python
"""Rows 8-11 -- frontier coordinates, run/surface consistency, admissible publication, single HEADs.

THE NORMALIZER IS THE POINT OF ROW 8. The contract's shape check sees two DIFFERENT strings and is
satisfied; the ledger normalises per `normalization_version` and sees ONE coordinate claimed twice
with different versions. That collision is invisible to any check that compares raw keys, which is
why the design calls it "the case the contract's shape check cannot see".

A HEAD IS SINGLE-VALUED OR IT IS NOT A HEAD (row 11). Surface authority orders by
`(published_at DESC, commit_seq DESC, surface_version_id DESC)`. All three are needed and each
covers what the one before it cannot: two versions can share a publication instant, and two
admitted in ONE batch share a commit_seq too -- so the id is the last resort that makes the answer
TOTAL. A tie left unbroken does not return two heads; it returns a different head per query, which
is worse because it looks like an answer.
"""

DEFAULT_NORMALIZATION = "v1"


def normalize(key, version=DEFAULT_NORMALIZATION):
    """The canonical form of a frontier coordinate, per normalization_version."""
    if version == DEFAULT_NORMALIZATION:
        return " ".join(str(key).strip().lower().split())
    return str(key)


def check_frontier(records, batch_records, primary, reject):
    """Row 8 -- one canonical coordinate per frontier, and no observation after its consumer starts."""
    for rec in batch_records:
        if rec.get("record_type") != "source_frontier":
            continue
        version = rec.get("normalization_version", DEFAULT_NORMALIZATION)
        seen = {}
        for entry in rec.get("entries") or []:
            key = normalize(entry.get("source_native_key") or entry.get("source_serial"), version)
            claimed = entry.get("entry_version")
            if key in seen and seen[key] != claimed:
                reject("L-08-normalized-collision",
                       "frontier %s has two entries normalising to the canonical key %r under "
                       "normalization_version %r with different versions (%r, %r): the contract's "
                       "shape check sees two distinct strings and cannot see this (sec 3 row 8)"
                       % (primary(rec), key, version, seen[key], claimed))
            seen[key] = claimed

    runs = [r for r in records if r.get("record_type") == "materialization_run"]
    frontiers = dict((primary(r), r) for r in records
                     if r.get("record_type") == "source_frontier")
    for run in runs:
        started = run.get("started_at")
        frontier = frontiers.get(run.get("source_frontier_id"))
        if not started or frontier is None:
            continue
        for entry in frontier.get("entries") or []:
            observed = entry.get("observed_at")
            if observed and observed > started:
                reject("L-08-observed-after-start",
                       "run %s started at %s but consumes a frontier entry observed at %s: a run "
                       "cannot consume a state that did not exist when it began (sec 3 row 8)"
                       % (primary(run), started, observed))


def check_run_consistency(records, batch_records, primary, reject):
    """Row 9 -- the run / frontier / version / surface quadruple must agree with itself."""
    by_id = dict((primary(r), r) for r in records)
    for rec in batch_records:
        if rec.get("record_type") != "surface_version":
            continue
        run = by_id.get(rec.get("producing_run_id"))
        if run is None:
            continue
        outputs = run.get("output_surface_version_ids") or []
        if outputs and primary(rec) not in outputs:
            reject("L-09-membership",
                   "surface_version %s names run %s as its producer, but that run does not list it "
                   "in output_surface_version_ids (sec 3 row 9)"
                   % (primary(rec), primary(run)))
        if rec.get("source_frontier_id") != run.get("source_frontier_id"):
            reject("L-09-frontier-disagree",
                   "surface_version %s consumed frontier %s but its producing run consumed %s "
                   "(sec 3 row 9)"
                   % (primary(rec), rec.get("source_frontier_id"), run.get("source_frontier_id")))
        if rec.get("materializer_version_id") and \
                rec.get("materializer_version_id") != run.get("materializer_version_id"):
            reject("L-09-version-disagree",
                   "surface_version %s claims materializer_version %s but its producing run used "
                   "%s (sec 3 row 9)" % (primary(rec), rec.get("materializer_version_id"),
                                         run.get("materializer_version_id")))


def check_publication(records, batch_records, primary, reject):
    """Row 10 -- publication is ADMISSIBLE only from a succeeded, completed run, with a promoter."""
    by_id = dict((primary(r), r) for r in records)
    for rec in batch_records:
        if rec.get("record_type") != "surface_version":
            continue
        if rec.get("publication_state") != "published":
            continue                                  # unpublished needs none of this
        run = by_id.get(rec.get("producing_run_id"))
        if run is not None:
            if run.get("run_result") not in ("succeeded", None):
                reject("L-10-publish-from-failed",
                       "surface_version %s is published from run %s whose result is %r "
                       "(sec 3 row 10)"
                       % (primary(rec), primary(run), run.get("run_result")))
            if not run.get("completed_at"):
                reject("L-10-publish-before-complete",
                       "surface_version %s is published from run %s which has no completed_at: a "
                       "run that has not finished has not produced what is being published "
                       "(sec 3 row 10)" % (primary(rec), primary(run)))
        if not rec.get("promoted_by"):
            reject("L-10-no-promoter",
                   "surface_version %s is published with no promoter: publication is an ACT and "
                   "an act has an actor (sec 3 row 10)" % primary(rec))


def surface_authority_head(records, logical_surface, primary, seqs):
    """The single authoritative published version, by (published_at, commit_seq, id) DESC.

    Returns (head, tie_broken_by) so a caller can PRINT which field decided -- a head whose tie
    was broken silently is indistinguishable from one that was never tied.
    """
    candidates = [r for r in records
                  if r.get("record_type") == "surface_version"
                  and r.get("logical_surface_serial") == logical_surface
                  and r.get("publication_state") == "published"]
    if not candidates:
        return None, "no_versions"
    ordered = sorted(candidates,
                     key=lambda r: (r.get("published_at") or "", seqs.get(id(r), 0), primary(r)),
                     reverse=True)
    head = ordered[0]
    tie = "published_at"
    if len(ordered) > 1:
        nxt = ordered[1]
        if (head.get("published_at") or "") == (nxt.get("published_at") or ""):
            tie = ("commit_seq" if seqs.get(id(head), 0) != seqs.get(id(nxt), 0)
                   else "surface_version_id")
    return head, tie


def projection(records, axis, basis_ids, seqs):
    """A DERIVED value carrying the admitted records it was derived from (sec 2, sec 5.4).

    It is NOT a contract record: no record_type in the frozen catalog, never admissible as a write.
    A projection that cannot show its basis is refused at construction rather than served, because
    the whole reason the derived value is trustworthy is that its basis is inspectable.
    """
    if not basis_ids:
        raise ValueError("L-11-projection-without-basis")
    return {"axis": axis, "value": None, "basis": sorted(basis_ids),
            "derived_at_commit_seq": max(seqs.values()) if seqs else 0}
