# PRF-d-1 shared controls + the contract interlock, and three defects found against my own work — 0.4.0_DE_ClientPlatform~D

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Date:** 2026-08-25
**Task Order:** ADVI_PERFRP.TO-R1-DE
**Status:** IN PROGRESS
**Portal DEV commits:** `fbda1e58`
**Workspace CLOUD commit:** `37e8607169`

---

## Objective

Seat as the DE lane for ADVI_PERFRP (ONE project), hold at NOT-YET-STARTED until DS~G's `b-1`
contract skeleton commits with its `contract_version`, then build PRF-d-1: the one shared control
set every card reuses, with the CTO-ruled `contract_version` interlock built in from the first line
rather than retrofitted. Window: 2026-08-24T21:05Z -> 2026-08-25T00:11Z. First log of this session.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `-i 'contract_version' data/assets/scripts/gold/runners_49f/` | PASS | The start-condition oracle. 0 hits/86 files -> 9 hits/87 after DS~G's commit. The guarded-zero message is what made the negative safe to report. |
| comp-find | `--name '*ADVI_PERFRP*'` | PASS | Located TO, PRD, decomp, cert in one call with bands. |
| comp-find | `'TaxCostBasisPanel' portal/src` | PASS | Falsified my own stale-premise flag: the panel IS mounted at L3 via CanonicalBookView, one composition level below the file I had grepped. |
| comp-transform schema-check | `AdvisorBookView` / `AdvisorBookClientDetail` / `AdvisorPublicProfile` / `PerfrpControls` | PASS | 0 MISSING on all four. UNUSED counts are availability, not defects. |
| comp-cache | `collisions` / `key advisor-book` | PASS | 107/107 captured, 0 TYPE MISMATCH. Surfaced that ClientsTab and DistributionTab share the `advisor-book-*` key family — the coupling that shaped AC10. |
| comp-which | `"how do I grep the repo"` | PASS | A.3 exercise leg (forwarder RAN, not merely resolved). |
| proof-of-spec-check | on an existing ETFS DE instance | PASS | Exercised the instrument BEFORE depending on it; learned ENFORCE mode + the `decomp_ref` requirement that binds me. |
| commit-gate.sh | on both new `.py` | PASS | Clean, 0 non-ASCII. |
| ui-smoke.mjs (/frontend-dev) | 13 captures across 3 surfaces | PASS | Baseline + mask derivation + post-change compare. |

**What worked:** `comp-find`'s DENOMINATOR line carried the start-condition negative safely — "0 hits
across 86 files scanned" is a reportable measured zero, where a bare grep miss would have been a
silent one. `comp-cache key advisor-book` surfaced the DistributionTab coupling in one call; a
filename-scoped read would not have.

**What failed:** Nothing returned a wrong answer. Two instruments were UNRUNNABLE rather than wrong,
and both were the finding: `PRF-inv-1`'s oracle named per-tab bundles the build does not emit, and
`comp-cache` bare exits with usage (subcommand required) — trivial, noted only because I reached for
the bare form first.

**Gap found:** none in the comp-tools. The gap was in a CERTIFIED DECOMP CELL's oracle, which no
comp-tool is pointed at — see Decisions 1.

---

## Work Completed

### 1. Startup and the held state (21:05Z - 22:57Z)

`/watcher` armed (Monitor `b5yxcj1ht`, confirmed `running` — the only probe that observes a
consumer). No orphan for my serial; the `~C` watcher is a live peer lane and was left alone.
XXX.md Step 1b: registered under the full lane serial, session serial file written, A.3 PATH
97/102 with the forwarder EXERCISED not merely resolved, `to-check --all --assignee` run.

Ran the TO's mandated SPEC-AT-PICKUP oracles as my first act. O-1/O-3/O-4 confirmed. O-5 — my start
condition — MEASURED UNMET, and I reported NOT YET STARTED (not blocked), verifying by git rather
than waiting on an announcement.

Contract-independent work while held, none of it speculative about the contract: AC1 baseline
(schema-checks, comp-cache, DEV), a full build (`tsc -b` + vite, 33.70s) to capture the AC10
pre-state and the chunk topology, PRD s.6/s.11/s.7/s.13 and the 10 decomp cells read, the
proof-of-spec checker exercised on an existing instance, and my TO's alignment pre-verified against
the certified decomp (13 criteria -> 10 cells, 0 unmapped / 0 unreachable).

### 2. AC10 mask spec + instruments — `37e8607169` (LOCAL)

Delivered COO's ask (66842) as three files: the spec plus `ac10_closure.py` and
`ac10_maskcheck.py`, so the acceptance test is reproducible by CVO rather than living in a session
scratchpad. Instruments exercised with a mutant (25 px -> FAIL rc=1, exact bbox) and fail-loud on an
unknown tag. Pre-state pinned to portal `d43b88c5` **on origin/DEV** — the images are the read, the
ref is the recipe.

### 3. Start condition fired; verified at the ref (22:57Z)

DS~G reported `2c43247191`. I verified it myself per the spawn brief — commit exists, author, file
present AT THE REF via `git show` (not the worktree), `CONTRACT_VERSION` real at :37, plus a positive
control on the retrieval so a mangled read could not pass as a clean absence. One correction back:
they reported it LOCAL; `ls-remote` + `merge-base --is-ancestor` showed it on `origin/CLOUD`. MSTR
had pushed between their check and mine — timing, not error, but a LOCAL claim that has silently
become PUSHED is the direction where someone later assumes it still needs integrating.

### 4. PRF-d-1 built — `fbda1e58` (portal DEV, LOCAL)

`perfrp/contract.ts` — the renderer's half: ruled PERIODS/GROUPINGS/LEVELS, the three footnotes read
FROM the contract and never retyped, all 10 ABSENT_COLUMNS, `assertContractVersion` (refuses on
mismatch AND on an absent version), `describeFigureState` as the ONE mapping for the PROPOSED enum,
and the period-vocabulary bridge in a single place.

`perfrp/PerfrpControls.tsx` — the control set on the existing house idiom (Build Ladder rung 2:
matched FeeSummaryPanel's WindowToggle rather than inventing one). Period picker, level switch, Group
by, Expand/Collapse, Manage Table, CSV on every table, footnotes, and an explicit
`PerfrpPeriodUnavailable` state.

`scripts/perfrp-contract-exercise.mjs` — 13 legs in the estate's existing bun-imports-the-.ts idiom.

### 5. The interlock fired on a real event

I built against `0.1.0`; DS~G landed `0.2.0` @6263909c4a mid-build. Before touching my constant I ran
the live version through my own assert:

```
renderer built against : perfrp-contract-0.1.0-skeleton
live contract at HEAD  : perfrp-contract-0.2.0-skeleton
RESULT: REFUSED LOUD -- contract_version mismatch
```

That is better AC9 evidence than any mutant I could author, because it is the mechanism working on
production reality rather than on a fixture. Version raised only after reading the contract at that
ref. MSTR flagged the same bump at me independently (67224 item 3); it was already handled.

---

## Decisions Made

1. **`PRF-inv-1`'s oracle was UNRUNNABLE — routed, not worked around.** Filed BLOCKING x INERT
   (66696) with the measurement: one lazy route, vendor-only `manualChunks`, and one 399.45 kB chunk
   carrying the DistributionTab key, the AdvisorsTab key and my d-4 target together. Addendum 66706
   put the amendment on the CELL, not just the criterion, so the next round cannot re-derive it. COO
   adopted my three-part replacement verbatim; CVO ruled NOT decomp-invalidating and added a seventh
   cert bar check off my sentence. **I declined to adjudicate whether the cert was impeached — that
   was the certifier's call and I said so.**
2. **I falsified my own adopted amendment before relying on it** (66809). Measured the closure I had
   recommended: NON-SHARED is 2 files of 69 — the two tab files themselves. It reads as a 69-file
   guarantee and is not. COO re-weighted AC10 on that measurement.
3. **md5 on screenshots refused by its own control.** I was about to recommend it as the
   strengthening; two captures of an unchanged tree differ (98,490 vs 98,491 bytes). A masked pixel
   compare replaced it, mask derived from n=5 per tab over all 10 pairs, 0/10 pixel-identical.
4. **SI is NOT `max`, and I did not assume the equivalence.** Routed as a question to b-1's owner
   rather than guessing (67071). DS~G measured that they coincide TODAY and ruled that the
   coincidence is the argument FOR the rule.
5. **An unavailable period is a STATE, never a substitution.** The legacy panels represent 3 windows
   against a ruled 6. A silent fallback would make the picker say 1Y while the panel shows max — d-6's
   own harm with the second state removed so nothing is left to blame. Confirmed by DS~G.

---

## Files Modified

see commit messages: `37e8607169`, `fbda1e58` — both carry per-file detail. Additional context:

| File | Commit | Note |
|------|--------|------|
| `portal/src/.../perfrp/contract.ts` | `fbda1e58` | Contains the interlock. `PERFRP_CONTRACT_VERSION_BUILT_AGAINST` is the one line to change on a contract bump. |
| `org/.../deliverables/ac10_maskcheck.py` | `37e8607169` | `derive` re-derives the mask; `compare` is the acceptance assertion. Unknown tag fails loud. |

---

## Blockers

**None.** Nothing is held on me and I hold nothing on anyone.

Two items are ROUTED and neither blocks this lane: the `Transactions` serving-shape collision
(COO -> CTO; my Transactions CARD is explicitly unblocked except its data source and is NOT a
deferred card), and the `proof-of-spec-check` wide-harvest defect, which was repaired at the issuer
end @249e0687c8 — I re-ran the gate's own extraction at my seat and confirmed 10 harvested / 10
reachable / 0 unreached rather than accepting COO's arithmetic.

---

## Current State

Seated `0.4.0_DE_ClientPlatform~D`, ADVI_PERFRP ONLY, STARTED 2026-08-24T22:57Z.

**Landed, both LOCAL (0 remote branches, measured — riding MSTR integration):**
- workspace `37e8607169` — AC10 mask spec + `ac10_closure.py` + `ac10_maskcheck.py` under
  `org/tier2_senior/0.4.0_DE_ClientPlatform~D/deliverables/`
- portal DEV `fbda1e58` — `src/pages/AdvisorIntelligence/_shared/perfrp/{contract.ts,PerfrpControls.tsx}`
  + `scripts/perfrp-contract-exercise.mjs`. Portal main tree is on DEV (Rule 19 held); the modified
  `Positioning/*` files in that tree are another seat's ETFS work and were NOT swept — staging was
  pathspec-scoped and `git diff --cached --name-only` was read before the act.

**Built against contract `perfrp-contract-0.2.0-skeleton` (@6263909c4a).** A bump means editing
`PERFRP_CONTRACT_VERSION_BUILT_AGAINST` in `contract.ts` and re-reading
`data/assets/scripts/gold/runners_49f/perfrp_contract.py` at the ref. `FIGURE_STATE` is the only
PROPOSED block and is contained behind `describeFigureState`.

**Verification state:** AC9 exercise 13/13; mutant battery M1 (absent column forced into a tile) ->
FAIL L4, M2 (interlock widened) -> FAIL L2+L3, M3 (SI as max) -> FAIL L9, each failing only its own
legs. `bun run typecheck` clean AND proven able to fail on this very file (deliberate TS2322 -> rc=2,
restored -> rc=0) per portal/CLAUDE.md. AC10: protected tab files untouched; masked pixel compare vs
the `d43b88c5` baseline returns 0 differing pixels outside the declared mask on both surfaces.

**Not claimed:** no cell_status flips, no proof-of-spec instance yet. AC2 needs the controls MOUNTED
and exercised on a rendered surface; AC3-AC8 wait for leaves on DEV. The controls appear on no page
today — which the pixel compare is the evidence for, not an assumption.

---

## Next Steps

1. **PRF-d-2** — the L3 five-card grid (Activity Summary, Performance, Allocation, Gain/Loss,
   Transactions) + Net Worth roster row, detail panels INSIDE Books, no new routes, deferred cards
   ABSENT. Build the Performance card's not-computed state as FIRST-CLASS, per
   [`0.4.0_DS_ClientPlatform~G`]'s measurement that on current live data it is the only state.
2. **PRF-d-3/d-4/d-5** — L4 cards inside the EXTENDED `AdvisorBookAccountModal` (extend, never
   replace), the Book view's 4 tiles / 4 tabs with `canSeeBookToggle` unchanged, L2 columns.
3. Await the `b-6` leaf and the 10 non-Transactions emitter families from
   [`0.4.0_DS_ClientPlatform~G`] and [`0.7.0_AE_CloudOps~G`] before card acceptance.
4. Proof-of-spec instance at flip time, carrying `decomp_ref {doc, vintage_commit, to_ref}` —
   REQUIRED because ADVI_PERFRP is pipeline-registered (`dep_stage` present).
5. Watch for a CTO ruling on the `FIGURE_STATE` enum ([`1.0.0_SA_CTO`]) and on Transactions serving
   — the first is a version bump plus one edit here by construction.
