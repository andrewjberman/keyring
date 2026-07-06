#!/usr/bin/env python3
"""reap_lib.py -- shared reap-on-cadence CONTRACT for a delivered/consumed backlog.

ONE implementation of the reap POLICY, consumed by BOTH:
  - org/mcp/archive_messages.py  (broker: delivered SQLite `messages` rows -> weekly
    JSONL archive -> DELETE -> VACUUM)
  - .tools/commit_queue_gc.py    (NFRA_CMTQUE: consumed/orphaned result + poison dlq
    files under <gitdir>/commit-queue/ -> archive -> unlink)

WHY shared: both are the SAME failure-class -- an already-delivered/consumed backlog
that piles up and (SQLite) bloats the file + spins CPU, or (fs) grows unbounded. The
POLICY that must NEVER drift between them lives here in exactly one place (the same
no-copy-drift principle as .tools/commit_gate_lib.sh for the security gate). The
SUBSTRATE-specific mechanics (SQL vs filesystem) are injected as callbacks.

THE POLICY (enforced by reap(), invariant across substrates):
  1. NEVER touch in-flight. The substrate's select_eligible() returns ONLY terminal/
     consumed candidates older than a retention floor. Undelivered / in-flight /
     newer-than-floor items are never candidates (the substrate query owns this).
  2. ARCHIVE-then-DELETE, verified. Archive durably FIRST; VERIFY archived == eligible;
     DELETE only what was archived. A crash between leaves the hot copy -> never a
     lost record (fail-closed: a short archive ABORTS before any delete).
  3. RECLAIM is the real fix. Deleting rows/files that don't reclaim space (SQLite
     pages) leaves the bloat + CPU spin -- the substrate's reclaim() (VACUUM / compact)
     is what actually shrinks. Optional (fs unlink reclaims immediately -> no reclaim()).
  4. NO SILENT TRUNCATION. Every run logs eligible / archived / deleted / reclaimed.
  5. MODES (safety-graded): dry_run (report only, no writes); archive_only (copy,
     live-safe, no delete/reclaim); full (archive + delete + reclaim).

A SUBSTRATE is a ReapSubstrate of callbacks; reap() orchestrates the policy over it.
"""
from __future__ import annotations

from typing import Any, Callable, Optional


class ReapSubstrate:
    """The substrate-specific callbacks reap() drives. Each consumer builds one."""

    def __init__(
        self,
        name: str,
        select_eligible: Callable[[], list],
        archive: Callable[[list], int],
        delete: Callable[[list], int],
        total_count: Optional[Callable[[], int]] = None,
        reclaim: Optional[Callable[[], Any]] = None,
    ) -> None:
        self.name = name
        # -> list of eligible candidates (terminal + older-than-floor; NEVER in-flight)
        self.select_eligible = select_eligible
        # (candidates) -> count durably archived (must fsync/flush). archive_only-safe.
        self.archive = archive
        # (candidates) -> count deleted from the hot store
        self.delete = delete
        # () -> total item count, for the "keeping N" log (optional)
        self.total_count = total_count
        # () -> reclaim result string, e.g. "89.0MB -> 0.5MB" (optional; VACUUM/compact)
        self.reclaim = reclaim


def reap(
    substrate: ReapSubstrate,
    *,
    dry_run: bool = False,
    archive_only: bool = False,
    do_reclaim: bool = True,
    log: Callable[[str], Any] = print,
) -> dict:
    """Run the reap policy over `substrate`. Returns a result dict. Raises
    RuntimeError (fail-closed) if the archive count does not match eligible -- never
    deletes on a short archive."""
    name = substrate.name
    eligible = list(substrate.select_eligible())
    n = len(eligible)
    total = substrate.total_count() if substrate.total_count else None
    if total is not None:
        log(f"[reap:{name}] eligible={n} of {total} (keeping {total - n})")
    else:
        log(f"[reap:{name}] eligible={n}")

    if dry_run:
        return {"substrate": name, "eligible": n, "archived": 0, "deleted": 0,
                "reclaimed": None, "dry_run": True}
    if n == 0:
        log(f"[reap:{name}] nothing to reap.")
        return {"substrate": name, "eligible": 0, "archived": 0, "deleted": 0,
                "reclaimed": None}

    # 1. ARCHIVE (durable) -- verified before any delete (fail-closed).
    written = substrate.archive(eligible)
    if written != n:
        raise RuntimeError(
            f"[reap:{name}] archived {written} != eligible {n}; NOT deleting "
            f"(fail-closed -- the hot copy is preserved, re-run)."
        )
    log(f"[reap:{name}] archived {written}")

    if archive_only:
        log(f"[reap:{name}] archive-only: hot store untouched.")
        return {"substrate": name, "eligible": n, "archived": written, "deleted": 0,
                "reclaimed": None}

    # 2. DELETE only what was archived.
    deleted = substrate.delete(eligible)
    log(f"[reap:{name}] deleted {deleted}")

    # 3. RECLAIM (the real space/CPU fix; optional).
    reclaimed = None
    if do_reclaim and substrate.reclaim is not None:
        reclaimed = substrate.reclaim()
        if reclaimed:
            log(f"[reap:{name}] reclaim: {reclaimed}")

    return {"substrate": name, "eligible": n, "archived": written, "deleted": deleted,
            "reclaimed": reclaimed}


# --------------------------------------------------------------------------
# Self-test: a fake in-memory substrate exercises the policy (dry-run makes no
# writes; a short archive fail-closes before delete; full run archives->deletes->
# reclaims; in-flight items are never candidates). No SQLite, no filesystem, no git.
# --------------------------------------------------------------------------
def _selftest() -> int:
    store = {1: "delivered-old", 2: "delivered-old", 3: "IN-FLIGHT"}  # 3 must never be touched
    archived: list = []

    def select_eligible():
        # policy: only terminal (delivered-old), never in-flight
        return [k for k, v in store.items() if v == "delivered-old"]

    def total_count():
        return len(store)

    def archive(cands):
        archived.extend(cands)
        return len(cands)

    def delete(cands):
        d = 0
        for k in cands:
            if k in store:
                del store[k]
                d += 1
        return d

    reclaimed_flag = {"done": False}

    def reclaim():
        reclaimed_flag["done"] = True
        return "compacted"

    logs: list = []
    lg = logs.append

    # dry-run: no writes
    sub = ReapSubstrate("faketest", select_eligible, archive, delete, total_count, reclaim)
    r = reap(sub, dry_run=True, log=lg)
    assert r["eligible"] == 2 and r["archived"] == 0, f"dry-run wrote: {r}"
    assert len(store) == 3 and not archived, "dry-run mutated state"

    # full run: archive -> delete -> reclaim; in-flight (3) untouched
    r = reap(sub, log=lg)
    assert r["archived"] == 2 and r["deleted"] == 2, f"full run: {r}"
    assert sorted(archived) == [1, 2], f"archived wrong set: {archived}"
    assert list(store.keys()) == [3], f"in-flight touched or delete wrong: {store}"
    assert reclaimed_flag["done"], "reclaim not called"

    # fail-closed: a short archive must raise BEFORE deleting
    store2 = {10: "delivered-old", 11: "delivered-old"}

    def bad_archive(cands):
        return len(cands) - 1  # under-count

    sub2 = ReapSubstrate("failclosed", lambda: list(store2.keys()), bad_archive,
                         lambda c: [store2.pop(k) for k in c] and len(c))
    try:
        reap(sub2, log=lg)
        print("FAIL: short archive did not raise")
        return 1
    except RuntimeError:
        assert len(store2) == 2, "fail-closed still deleted!"

    print("PASS: reap_lib selftest (dry-run inert / full archive->delete->reclaim / "
          "in-flight untouched / short-archive fail-closed)")
    return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        sys.exit(_selftest())
    print(__doc__)
