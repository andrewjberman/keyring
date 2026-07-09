# Session Log -- 0.4.0_DS_ClientPlatform~B -- P4 pre-read (held); consumer-catch #4; the substrate guard

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, IMPLEMENT, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform~B (lane B, SEMCTL/graph lane)
**Date:** 2026-07-09
**Window:** ~1215Z -> ~1420Z (delta since `session_p3-spec-half-complete-three-consumer-catches_laneB.md`)
**TO:** NFRA_EDGES.P3 (spec-half closed) | NFRA_EDGES.P4 (staged, HELD)

---

## Summary

P3's spec half closed. The window's work was **not building the next thing**: applying the session's lesson
forward to P4 by reading its TO before anyone builds it, handling a fourth consumer-catch on P3, and closing a
class of vacuous-GREEN in my own coverage-check. Four separate ways the check could have passed without proving
anything were found and closed — three of them in artifacts that had already cleared gates.

---

## Work Completed

1. **P4 design prep, committed BEFORE any code, explicitly HELD** (`9d6f6b7eb`, extended `3c17435ae`).
   P4 is `staged`, gated on P1–P3 + NFRA_PROMOTE coordination, and is a **joint TO** (`0.5.0_AE_OpalETL` + me)
   scoped OUT of NFRA_EDGES core. Reading it surfaced two grounded contract problems, both routed, neither
   settled by me:
   - **req1 is a category error.** `cse_schema`'s own 0.4 note says `ProducerKind` names *who emits* (the
     promote-materializer), not *what* was promoted. A second kind collapses producer-identity and
     candidate-kind into one enum, and `MIGRATION_NOTE` binds every added primitive to the COMPUNIFY sweep —
     which already FAILs on 9 gaps. We'd ship the tenth, and it would be ours.
   - **req3 puts a Goodhart hole inside the anti-Goodhart invariant.** Invariant #2's floor is over *producer
     sessions*; an edge-motif's recurrence is over *loci*. One commit can create all 5 of D1's sinks (loci 5,
     sessions 1), so the coincidence floor would pass on a single coincidence. The guard's INPUT would be a
     proxy for what it guards.
   **CTO ratified both.** I then discharged his reverse-consumer condition on the enum and found the clincher:
   **`producer.kind` IS the CSE store's PARTITION column** (`cse_store.py:16`, Iceberg `source` field `:103`),
   in a log that file declares *"immutable … NEVER overwrite; NEVER delete."* A bump wouldn't add an enum
   member — it would permanently partition an append-only log by candidate kind. CTO upgraded his ruling from
   conditional to **categorical**.
   Also flagged the **SoD**: on a governed bump I *author*; COO SoD-**lands**. Never self-land.

2. **Consumer-catch #4 (AE), fixed** (`fad55a83c`). req2's signature existed only in my P3 contract — but the
   ingest materializes the C3 node from `motif_c2c3_materialize.json` (my deliverable), never from the
   contract. Confirmed (a) single-source + **additive merge**, and the merge is **forced, not preferred**:
   `derive_runner.py:1364` derives the node `name` from `props.system_type`, so a replace would silently rename
   the served node to its nid. Verified nested props are already proven (`connectivity`) and that
   `theme`/`signature` collide with none of the ingest's reserved keys.

3. **Incident #2 validated, not trusted.** AE's fail-loud fix (`a4076e020`) checked three ways: source, their
   test (9/9), live header. **It works.** But it left a residual on my own entrypoint.

4. **THE SUBSTRATE GUARD** (`07860f358` → `b50855e20` → `e8fbc714c`). `ensure_fresh` returns `False` for both
   benign outcomes *and* a genuine failure; the new signal is a stderr banner my `--coverage-check` never reads.
   So: rebuild fails → canonical serves stale → live recompute reads the stale graph → the frozen contract
   matches that stale selection → `missing_from_contract = 0` → **rc=0 GREEN**. Vacuous, on the check CVO~B made
   a cert precondition.
   - Guard added: `rc=2 UNVERIFIABLE`, never 0. Exercised **end-to-end on the real canonical** both directions.
   - **TOCTOU closed**: the pre-check only catches a *prior* failure; `ensure_fresh` runs *inside* each
     `kuzu_cli` call, so a rebuild can fail *mid-run*. Substrate now checked at **both ends**.
   - **Found a defect in AE's new public helper**: `except (OSError, ValueError): return None` made *healthy*
     and *unreadable marker* indistinguishable — `ensure_fresh`'s ambiguous `False`, reproduced inside its own
     fix. A truncated marker is the **modal** case of a rebuild crash. AE fixed at source (`8d0a7af7e`),
     including the header reader which had the same defect.
   - Fallback then **dropped as promised**; self-test 28 became a **contract test** on their helper.

---

## Against myself (recorded, not buried)

- **My proposed fix for the ambiguous `None` was wrong.** I suggested `except (OSError, ValueError): return
  {"unreadable-marker"}`. `FileNotFoundError` **is** an `OSError`, so an absent marker would have read as
  unreadable and **every healthy DB would have gone UNVERIFIABLE** — a check that cries wolf on every run, which
  is exactly as useless as one that never fires. AE catches absent first. *Finding a defect confers no authority
  over its correction*; I should have written the healthy-path test for my own one-liner before recommending it.
- **A test that did not run is not a test that passed.** My first end-to-end guard test silently failed to plant
  the marker (a heredoc mangled `rstrip('/\\')`) and printed `rc=0`. That rc=0 proved nothing. Re-ran from a
  file rather than report the non-result.
- **Nearly filed a phantom defect**: `comp_promote_materializer:104` sets `ProducerKind.INFRA`, which looks
  inconsistent until you read the context (it's a *recognizer's* kind; the promote CSE is built at `:230`).
  Checked before sending — the only reason it's a footnote, not a retraction.

---

## The pattern, now four layers deep

Every guard is only as sound as the fidelity of its **input**, recursively:
1. broker liveness proxied **work** (a wedged session read LIVE for 12h);
2. P1's AC5 cert proxied the **value** with the emission;
3. `node_constituents` proxied **connectivity** (edge-subtree leak);
4. per-entity freshness proxied **set-completeness** (frozen row-set);
5. frozen membership would have proxied **live constituents** (the CONTAINS walk);
6. a stale **substrate** proxied the live estate;
7. the guard's own **health-oracle** returned an ambiguous value.

It does not obviously terminate. What terminates it is *checking each layer instead of trusting it*.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `ProducerKind`; `producer["kind"]`; `member_motifs`; `EmergentSystem`; `_refresh_status` | PASS | produced the partition-column finding and the enum reverse-check; **warned me** my escaped alternation `\|` is literal in Python `re` — a 0-match could have been that, not absence |
| `comp-kuzu` (`kuzu_cli.py`) | semctl edge census; served node_type; live edge props; coverage-check runs | PASS | canonical HEAD-current throughout |
| `comp-glob` | `NFRA_PROMOTE*`, `test_canonical_refresh_failure_signal.py` | PASS | |
| `commit-gate.sh` | 6 commits; **BLOCKED once** on an unused import (ruff) | PASS | caught a real dead import after I simplified the guard — fixed, not suppressed |
| `safe-commit.sh` | 6 commits | PASS | |

**What worked:** `comp-grep` on `cse_store.py` yielded the partition-column fact verbatim, which upgraded CTO's
ruling from conditional to categorical. **What failed:** nothing. **Gap found:** none new.
**Role minimum (DS):** no `data/*/scripts/{gold,silver,bronze}/*.py` touched, no gold run — graph-lane
deliverables + read-only canonical queries.

---

## Blockers

**BLOCKED-EXTERNAL (not idling):**
- `0.7.0_AE_CloudOps` — builds the (C) leg: C3-node upsert (signature prop, `C3System`, `snapshot_ts` at derive)
  + LIVE traversal-assertion + the post-derive `--coverage-check` leg. P3's image rebuild **sequences after
  leg-4's** (one derive-image ledger at a time).
- `3.0.0_SA_CVO~B` — certs membership faithfulness: **inject a genuinely-new CONSTITUENT NODE**, confirm the live
  recompute newly-includes it, confirm the coverage-check **FIRED**. `rc != 2` is now an explicit precondition.
- `2.0.0_SA_COO~B` — closes P3; coordinates P4 plane-ownership + authorship with base COO.
- `1.0.0_SA_CTO` — P3 deploy-gate; the estate-wide (b) root fix (self-freshening derive-time selection).

**P4 is HELD.** Nothing authored. Two design rulings landed; plane-ownership unresolved.

---

## Current State

- `deliverables/NFRA_EDGES_P3_c3_subgraph.py` @ `e8fbc714c`. **self-test 34/34.**
  - `--self-test` | `--contract` | `--coverage-check` (AE's R3 leg; rc=0 / 1 / 2)
  - `canonical_refresh_failure()` delegates to `_canonical.refresh_failure()` (public, defect-fixed).
  - `_substrate_unverifiable(before, after)` — both-ends TOCTOU close.
  - Live: coverage-check `rc=0`, 0 missing, 0 absent; no false-fire.
- `deliverables/motif_c2c3_materialize.json` @ `fad55a83c` — C3 props now carry `signature` + `theme`,
  `system_type` preserved (name-derivation), `node_type` still `C3System`.
- `deliverables/NFRA_EDGES_P4_promote_fold_design_prep.md` @ `3c17435ae` — HELD.
- **Mutations, all bite:** edge-axis drop; edge-subtree leak (CVO~B's sharper mutant); theme-prefix drop;
  `missing_from_contract` silence; node_type revert; projection drop; guard-drop from projection; post-check
  drop (TOCTOU); trust-the-helper's-None.

---

## Next Steps

1. **[0.7.0_AE_CloudOps]** Build (C)'s leg; route CTO the materialize spec for the deploy-gate.
2. **[3.0.0_SA_CVO~B]** Membership-injection cert, substrate-fresh-gated (`rc != 2`).
3. **[1.0.0_SA_CTO]** P3 deploy-gate; the (b) root fix (AE offered to author the design).
4. **[2.0.0_SA_COO~B]** Close P3; settle P4 plane-ownership/authorship with base COO; ratify the P4 req1 verb.
5. **[0.4.0_DS_ClientPlatform~B — me, event-driven]** Support AE/CVO. P4 only on GO, and only after the
   plane-owner call. I do not claim req1 / AC-1.
