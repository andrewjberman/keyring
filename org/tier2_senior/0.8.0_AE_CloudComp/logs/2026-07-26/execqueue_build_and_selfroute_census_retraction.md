# Exec commit queue + the self-route census I had to RETRACT — 0.8.0_AE_CloudComp~C

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Date:** 2026-07-26 (window close; log written 2026-07-28T1239Z)
**Task Order:** CTO~Z dispatches 181813Z (exec-path commit queue) and 203028Z (self-route, Andrew-direct GO)
**Status:** queue COMPLETE; self-route census RETRACTED, awaiting CTO~Z direction on the corrected basis
**Window:** 2026-07-25T1838Z (`@7856093dc`) -> 2026-07-26T0738Z

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-grep` / `comp-glob` | locate refusal path, `sovereign_held` consumers | PASS | the `sovereign_held` census returned **200 matches / 50 files [TRUNCATED]** — reported as a CEILING, never a count |
| `commit-gate.sh` | `exec-commit-queue.py` x2 | PASS | |
| `exec-commit-queue.py` | `--days 3`, `--days 5`, `--all` | PASS after a **self-caught wrong predicate** | see below |
| `comp-which` | tie-case render check | PASS | printed the near-tie banner — evidence that option (b) was already implemented |
| `comp_route` / `comp_which_signals` (in-process) | 69-tool self-route census, twice | **FIRST RUN INVALID** | wrong query string; second run authoritative |
| `git log --date=format-local` | window scoping for this log | **CAUGHT MID-COMMAND** | used it without `TZ=UTC` — my own documented false form. Redone; 1500 local was really 1900Z |

**What worked:** reading the refusal branch of `owned-paths-check.sh` before building a logging
change — it was already there, already fail-safe, which killed a scope-bound lift CTO~Z had
granted on my premise.

**What failed (mine, both disclosed):** (1) the queue's first predicate asked *"is this path
currently dirty?"*, conflating NEVER-LANDED with LANDED-THEN-TOUCHED-AGAIN, producing two live
false positives. (2) **The self-route census — 100% of it measured on the wrong query string.**

**Gap found:** `owned-paths-check.sh:115` logs only the FIRST 3 violations per refusal, so 55
BLOCK events under-report **at source** and no reader can recover the rest. Stated by the tool,
not hidden; the fix belongs in the hook.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. **Exec commit queue `@db0e4bc78`** — a PURE READER over the gate's own 615 logged refusals.
   No hook change: `owned-paths-check.sh:122` had been appending `<ISO_TS> BLOCK <AGENT>
   <N_FILES> (VIOLATION: <path> -- lane=<LANE>)` all along, already `2>/dev/null || true`.
   CTO~Z withdrew the scope-bound lift once I found it. **The signal was never missing; it was
   unread, 615 events deep.**
   - Predicate corrected before landing, and **exercised both directions**: known-resolved -> 0
     rows, genuinely-pending -> 1 row, `--all` resurfaces 30 suppressed.
   - Prints every denominator each run + the source truncation + what it structurally cannot see.
2. **Andrew-direct governance ruling recorded `@c64f00e59`** — verbatim, in the tool's own
   docstring rather than only in a message. No comp-tool may carry a governance predicate.
   Compliance verified by grep over my own artifacts; `sovereign_held.py` NOT touched.
3. **Self-route census — RETRACTED.** See below.

## THE RETRACTION (the substantive item)

Reported to CTO~Z: 47/69 TOP-1, 61/69 co-equal-top-set, 22 failures, "14 of 22 are an
alphabetical tie-break = 64% of failures", "two instruments disagree by ~17".

**All of it void.** `.tools/comp-which-routing-test.py:439-447`:
```
self_route_query(manifest, tool) -> manifest entries[].use_case IF present, ELSE tools_index.does
```
**All 69 tools have a `use_case` entry**, so the authoritative probe never reads `does`. I used
longest-sentence-of-`does` for all 69 — **the query strings differ for 69/69.**

```
                        RANK1   TIED-TOP   MISS
authoritative (use_case)   63        3        3
what I reported (does)     47       14        8
```

**Voided:** the 22-failure population · the alphabetical-tie-break-is-64%-of-failures finding
(3 ties, all already `kind=disambiguation`) · the ~17 instrument disagreement (**the disagreement
was mine**; 3 MISS + 3 NEARTIE = 6 vs manifest-check's 5 WARNs is a reconciliation) · my claim
that the predicates differ (**they don't** — same RANK1/NEARTIE/MISS split; they differ by
QUERY SOURCE) · the comp-debris changelog finding (`does` is not a routing input).

> **Same class as the kuzu wrong-population near-miss: rigorous, internally consistent, freshly
> measured, WRONG AXIS. The difference is that this one did not stop at my terminal — CTO~Z
> issued a ruling and amended a reporting instruction on the strength of it.**

Root cause: I inherited CTO~Z's stated method and never checked it against the instrument's
source. I read `comp_route.py`, `comp_which_signals.py` and the manifest — **not the harness
whose method I was reproducing.** That is the load-bearing-unverified-premise failure I had
flagged to CTO~Z six hours earlier on the audit log and said I would not repeat.

**Damage bound:** 0 of my 25 commits since 07-25 contain 61/69 or 47/69 — measured, not assumed.
The numbers existed only in MCP messages, so nothing durable needed retracting.

## Files Modified

See commit messages: `db0e4bc78`, `c64f00e59`. No estate file touched by the census (read-only).

## Blockers

None blocking. **BLOCKED-ON-RULING** for next work: CTO~Z to direct whether I take the 3 real
MISSes or re-run the census himself first on the corrected basis.

## Current State

- `deliverables/exec-commit-queue.py` — live, read-only, reads `org/git-author-override-audit.log`.
  Pending = blocked AND no commit touching that path since the refusal (`git log --since`).
  Placement (exec startup + `safe-commit` output) is AGREED but **NOT wired** — separate change.
  Promotion to a registered `.tools/comp-*` is a separate NFRA_COMPREG step, COO SoD.
- **Real self-route failures, authoritative query, all `kind=decision` (confidently wrong, not
  ties):** `comp-denytest` -> `comp-iam`, `comp-firmsep-sweep` -> `comp-iam`, `comp-keys` ->
  `comp-freshness`. Untouched.
- Self-route numbers are a **SELF-CONSISTENCY check over each tool's own use_case text — NOT a
  coverage measurement and NOT a routing-quality score** (CTO~Z 073515Z; harness says so
  in-source at `:468-470`). Never publish either number without that scope line.
- HALTGT `@2002dcdca7` stands. Qualifier: **it does NOT make lane `[STOP]`s hard-block** — it
  binds a lane that is DEAF or between watchers.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Direct the corrected self-route work — the 3 MISSes, or re-measure first.
2. **[1.0.0_SA_CTO]** Exec-queue placement wiring, if wanted, as its own change.
3. **[0.8.0_AE_CloudComp~C]** Reachable, event-driven.
