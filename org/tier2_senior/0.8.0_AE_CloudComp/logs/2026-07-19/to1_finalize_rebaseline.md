# NFRA_COMPASSURANCE.TO-1 -- FINALIZE the preserved WIP baseline (re-measure at current HEAD)

**archetype:** VALIDATE (with a scoped IMPLEMENT: the conditional-provenance harness fix)

**Session:** `0.8.0_AE_CloudComp~Z` respawn 2026-07-19 (MSTR SPAWN-DIRECT 180318Z, Andrew
proceed-all-NFRA via CTO). PRIORITY = NFRA_COMPASSURANCE PRD-2. FIRST ACTION = finalize-or-discard
WIP `@a2e31bc3c` (the routing-quality harness artifacts COO preserved on-behalf during the crash;
UNVERIFIED / UNLOGGED / owner=None). This log is TO-1's AC9 deliverable.

## Disposition: FINALIZE (not discard)

The WIP is my own pre-crash work. Grounding it end-to-end:

- **The harness (`.tools/comp-which-routing-test.py`) is sound + AC-complete.** Both mutation tests
  PASS (all-zero collapses the positive control; all-nine fires gibberish) -- AC4: it CAN fail.
  Methodology satisfies all 15 ACs (vintage-pinned binary, non-polluting scratch mirror, four-signal
  live routing, v4 alibi pollution check, full row-tag tally before filtering, bracket + two-named-
  metrics, frozen cohort measured -- not re-derived).
- **The frozen cohort (`comp-which-routing-cohort.frozen.json`, n=562 R_raw, frozen 2026-07-14T05:41,
  snapshot 12074 lines) is legitimately pinned** and is the exact population TO-2 measured against
  (26.441% -> 25.050%, n=562). KEPT FROZEN (AC8) -- not touched, not re-derived.
- **The one real defect was VINTAGE DRIFT.** The WIP baseline measured comp-which blob `ee543c83`
  (= commit `e7fec72ec`, the pinned HEAD at capture, deliberately avoiding a then-mid-edit working
  tree). That working-tree version has since become committed HEAD (`4aeed452`), and the sole
  comp-which commit between them is `59b37efea` (comp-genesis registration). So the WIP baseline
  measured a binary **that no longer runs** -- a stale-vintage record, not a wrong measurement.

FINALIZE = re-measure the baseline against **current HEAD** on the **same frozen cohort**, commit the
refreshed artifact, log, close. No re-freeze, no comp-which (binary) edit. (COO + CTO accepted this
disposition; review-on-land, no pre-commit gate; CVO verifies per PRD-2 ACs.)

## The baseline delta (old ee543c83 -> new HEAD 4aeed452), and WHY it did not move

Re-ran the harness at HEAD (`4aeed452`) against the frozen n=562 cohort. Structured leaf-diff vs the
committed WIP baseline -- **every coverage/routing number is IDENTICAL:**

| metric | WIP (ee543c83) | FRESH (HEAD 4aeed452) |
|---|---|---|
| R_raw zero-rate (everything asked) | 30.1% | **30.1%** |
| R_strict zero-rate | 29.3% | **29.3%** |
| headline NL-questions (coverage hole proper) | 25.05% | **25.05%** |
| cohort C self-consistency | 13.8% | **13.8%** |
| cohort G gibberish gate | 100% zero, 0 unguarded misroutes | **100% zero, 0 unguarded** |
| recall@3 (multi-label, cohort C) | 87.4% | **87.4%** |
| RULES score distributions (all 4 cohorts) | -- | **byte-identical** |
| VERDICT | PASS (exit 0) | **PASS (exit 0)** |

**The ONLY substantive non-vintage change:** the r[1] anti-control `poisoned_r1` moved 33 -> 42. That
is the harness deliberately reproducing the r[1] space-count bug over comp-which's RULES; it scores
higher because the RULES set GREW (comp-genesis added curated rules). It is a **confirmation the
harness is bound to the current scorer**, and it still PASSES (poisoned>0, clean==0). Everything else
that differs is the intended vintage stamp (blob, `working_tree_differs` True->False on a clean tree,
`measured_at`) or run-to-run concurrent-traffic volatility in the reported-only pollution fields
(`live_log_new_rows` 11->3, `training_delta` 11->0 -- non-convicting by design).

**WHY the headline did not move despite the intervening commit:** comp-genesis's added vocabulary is
tenant-provisioning ("provision a tenant", "atomic bundle") -- it intersects ZERO questions in the
frozen organic-agent cohort, so no frozen probe's score changed. The refresh moved the *vintage*, not
the *finding*.

## Scoped harness fix: conditional provenance (the artifact must not contradict itself)

The harness baked a `provenance_note` describing the ORIGINAL 07-18 capture ("captured minutes before
another lane began editing... sound by luck"). On a CLEAN-tree re-baseline that prose CONTRADICTS the
artifact's own `subject.working_tree_differs: False`. A baseline whose provenance note fights its own
subject fields is map-vs-territory drift. Fixed `provenance_note` to be **conditional on the actual
capture state** (dirty-tree vs clean-tree), keeping the earned lesson ("a provenance record that
captures WHAT but not WHEN is not provenance") in BOTH branches as HISTORY, never asserted as this
run's condition. This fixes every future re-baseline, not just this one. `commit-gate.sh` PASS
(py_compile + ds-precommit + ruff + manifest registration-invariant 78 accounted). Re-ran to produce a
byte-reproducible artifact carrying the clean-tree note.

## Compiler Tools (AC9 -- every compiler_tools_mandate <run> reproduced, observed vs <expect>)

| Phase | run | observed | vs expect |
|---|---|---|---|
| 0 discovery | `wc -l comp-which-rail.log` | **15262** (was 12074 at freeze; ROUTE-POSTERIOR 7535->9908) | PASS w/ NOTE: log GREW ~3200 lines / 5d -> a re-derived cohort today would be a DIFFERENT population. **This VINDICATES AC8** (freeze, don't re-derive). Frozen cohort kept. |
| 1 before-write | `python -c "...manifest counts"` | entries **97**, use_case **97/97**, distinct tools **65**, tools_index 60 | CHANGED from 66/66/38 -- catalog GREW via the registration flow. Cohort C construction still valid (use_case present on all). Reported, not reconciled (TO-4). |
| 1 before-write | `comp-blast comp-which` | NOT-FOUND in the 1427-node TRACE graph (structural, COMPRAIL F-5) **BUT** now reports `comp-pydeps DOES model it: 21 code consumers` | MATERIAL CHANGE vs PRD F-5 / Q3: `comp-pydeps` (cf22d5a75) closed F-5 for the CODE-reference layer since the WIP. comp-blast (trace graph) still NOT-FOUND; the reference graph now RESOLVES. Surfacing (below). |
| 1 before-write | live-binary Phase-1 probe | NOT RUN (harness mandate RETRACTED it -- it destroys cohort R's singletons). Measured via the scratch mirror instead. | PASS -- did the non-destructive thing. |
| 2 before-commit | `python comp-which-routing-test.py` | VERDICT **PASS** (exit 0); controls held; G 100% zero, 0 unguarded; recall@3 87.4% | PASS |
| 2 before-commit | `--mutate zero` / `--mutate nine` | both "harness DETECTED the mutant: YES" (exit 0) | PASS -- the harness CAN fail (AC4). |
| 2 before-commit | positive + gibberish controls (isolated) | positive score=5 PASS; gibberish n=40 nonzero=0 PASS; r[1] anti-control poisoned=42 clean=0 PASS | PASS |
| 2 before-commit | pollution (v4 alibi) | 776 routes issued; mirror sweep 0 rows (silent); positive-control 1 row (capture proven); live-log rows matching a probe **0** | PASS -- zero pollution, proven not assumed. |
| 3 after-commit | re-run + commit refreshed baseline | (this commit) | -- |

`comp-which` on itself: exercised via the mirror throughout (the instrument under test IS the tool);
not run live for the log (a live probe pollutes the very rail log it measures -- the RETRACTED-probe
lesson). `org/compiler-tools-log.md` row appended in the same commit.

## Findings surfaced (not acted on -- out of TO-1 measurement scope)

- **PRD Q3 / F-5 partially resolved:** `comp-pydeps` now models the compiler-tool CODE-reference graph
  (`comp-which` has 21 consumers, incl. the fail-closed `commit_gate_runner.py`). The PRD's "blast
  radius is not graph-derivable / the compiler tools are outside the compiler graph" is now partially
  stale. -> routes to COMPASSURANCE / TO-4 owner; noted for the COMPROUTE-reopen framing.
- **Cohort C = 13.8% zero (not near-ceiling):** "the catalog cannot retrieve itself" finding persists
  at current HEAD -> TO-4 (catalog truth), as the harness already routes it.
- **TO-2/TO-3 confirmed live at current HEAD:** the abstain (rc/no-route) + top-k machinery is in the
  binary; the G gate PASSES (comp-which abstains on 100% of gibberish) -- the defect the original
  07-13 baseline reported (exit 1, gibberish routed) is FIXED. TO-2/TO-3 shipped via NFRA_COMPCLOSE
  Phase B (`c52f83612` abstain/rc=1 + `7215ee75c` distribution-derived floor; `f64e5f5b1`/`b68237ad5`/
  `be738b2d1`/`8bd21d667` top-k).

## Outcome

TO-1 FINALIZED: harness verified sound at current HEAD, baseline refreshed to the live vintage on the
frozen cohort, provenance made self-consistent, logged. `<status>` remains complete (evidenced here).
Deliverables: refreshed `comp-which-routing-baseline.json` + the conditional-provenance harness fix +
this log. Frozen cohort unchanged. Next: TO-2..5 ground-truth + surface the COMPROUTE-reopen question
to COO + CTO.
