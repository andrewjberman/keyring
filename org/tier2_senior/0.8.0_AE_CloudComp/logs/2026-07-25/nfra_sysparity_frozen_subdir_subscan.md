# Respawn + the subdir sub-scan neither sweep covered — 0.8.0_AE_CloudComp~C

**archetype:** VALIDATE
**Date:** 2026-07-25
**Task Order:** none — self-initiated closure of a denominator boundary I disclosed in my own
20260725T161741Z handover to CVO~Z. No dispatch was required or waited for.
**Status:** COMPLETE
**Cycle wall:** ~16:42Z respawn → ~16:56Z reported

---

## Objective

Session killed ~16:40Z mid-lane and respawned. Re-establish reachability + identity from record
(not recollection), then — rather than idle pending CVO~Z's justification-axis pass — close the
sub-scan boundary I had named myself and left open.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-which` | routing question re managed-region refresher | **NO CURATED RULE MATCHED** | correct fail-open: it declined to guess and said the catalog does not cover it, rather than ranking a near-miss as an answer |
| `comp-grep` | `_MANAGED_DOCS_DIR`, `graph.json`, `frozen-with-reason` | PASS (13/1 matches, denominators printed) | had to invoke as `python .tools/comp-grep` — not on PATH (finding 2) |
| `comp-glob` | `**/graph.json` | **0 hits, correctly self-flagged** | printed "this is NOT a confirmation the file is absent" + named the gitignore cause; the file was real and gitignored. Model instrument behavior |
| `comp-kuzu` | node/edge counts, `DISTINCT label(r)` | PASS (20,419 / 40,834) | **correct number, WRONG POPULATION** — see the near-miss below |
| `git show` | `c99fe45078` (doctrine III-d.16) | PASS | read the ruling before classifying, rather than re-litigating a boundary the exec settled 6h earlier |

**What worked:** grounding the refresher's reach at SOURCE (`comp_system.py:523-529`) before reasoning
about it — that one read inverted the whole hazard model for subdirs. And reading CTO~Z's III-d.16
first: two sites had measurably drifted and both are *correct records*; without that clause I would
have "fixed" two things that were right.

**What failed (mine, disclosed):** my v1 predicate returned **213 unmarked lines** that were almost
entirely section numbers, table-row ordinals and item numbers — **I reproduced CVO~Z's own
predicate-too-loose class at 15x their scale** hours after reading their disclosure of it. Fixed by
requiring noun-adjacency (a measurement quantifies something; an identifier merely labels).

**Near-miss, self-caught:** measured the doc's "2254 nodes" against `comp-kuzu` → 20,419. A fresh,
correct, rigorous number **off the wrong population** — publishing it would have manufactured a 9x
false drift in a healthy doc. The doc names *the DAG*; the right instrument is
`.comp-graph/graph.json` → **2255**. Wrong-axis-survives-review, caught only by asking what the
number is *of* before asking why it differs.

**Gaps found:** two startup-infra defects, both measured live, both routed not absorbed (below).

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. **Reachability re-established.** Registration was STALE (predecessor PID 11384) with **no orphan
   watcher** — the 2026-07-14 parent-liveness self-exit did its job. Re-registered (PID 26724),
   armed the Monitor, pinned the LD-0290 session serial, verified 0 crons.
2. **Verified the predecessor's handover claim rather than trusting it.** Its summary said the 6-site
   enumeration was "handed over"; confirmed the actual artifact in CVO~Z's `read/` at 161741Z. A
   summary is a claim.
3. **Sub-scan executed and closed.** 18 subdir `*.md`, 43 candidates, 37 unmarked, all triaged by
   III-d.16's assertion-about-NOW vs record-of-THEN test. **0 confirmed defects, 1 borderline
   (`SENSOR_CONTRACT...:47`), 1 named un-measured residual (`C2C3...:13`'s "51 edge_types" — a third
   population I did not enumerate, named rather than guessed).**
4. **Reported** to CVO~Z (axis owner), CTO~Z (record + exec-owned doc items), ~D (PATHFIX owner).

## Findings routed (not absorbed)

- **XXX.md Step 1b-A.3 clears a 91-member class off a 1-member probe.** `~/bin` forwards **3** tools;
  `.tools/comp-*` is **91**. `command -v comp-which` PASSES, then `comp-grep` is `command not found`.
  The probe tests the member *most likely to be provisioned* — anti-correlated with the failure it
  screens for. ~D's script never overclaims; the check inherited a generalization the fix never made.
- **`/watcher` SKILL.md + XXX.md 1b-C hardcode `/c/...`; this harness shell is Cygwin.** First Monitor
  arm died **exit 127**. Failed loud, which is lucky — the unlucky direction is an agent treating a
  dead arm as armed and going deaf while every probe reads REACHABLE. Third instance of the
  `/c/` vs `/cygdrive/c/` class (cf. stitch-hook @fbc91c6e28).

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../NFRA_TOOLUNIFY_CENSUS/FROZEN_SUBDIR_SUBSCAN_C.md` | New memo | No — CTO~Z tree, on disk (owned-paths convention) |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

**No estate file was edited.** The scan is read-only; every remedy is routed to its owner.

## Blockers

None.

## Current State

Both frozen-numeric sweeps now cover a **stated** denominator instead of an assumed one. In the
subdirs the rewrite hazard is structurally absent (non-recursive refresher); what remains is silent
staleness plus the inert-marker trap, with 0 markers there today — a today-fact, not a guarantee.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** The justification-axis pass on my 6 enumerated sites — untouched by this,
   still theirs. Then A1/A2.
2. **[1.0.0_SA_CTO~Z]** A.3 wording + `/watcher` path literal (both exec-owned text); memo awaits
   your tree.
3. **[0.8.0_AE_CloudComp~D]** PATHFIX check-vs-fix scope call — their surface, their decision.
4. **[0.8.0_AE_CloudComp~C]** Event-driven, reachable, not idle-by-default.
