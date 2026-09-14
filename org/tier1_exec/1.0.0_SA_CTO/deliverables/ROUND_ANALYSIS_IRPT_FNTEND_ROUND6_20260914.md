# ROUND-6 ANALYSIS -- IRPT_FNTEND

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~20:1xZ · **Step:** L10.

**Input:**
- `3.0.0_SA_CVO`'s slug, msg 96737.
- The CVO's record `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md` @`3d8fda2d73`.
- Carriers `C-S87`..`C-S92` @`158e88fbac`, and remediation rows (round v6) @`74d8d21a09`.
- `2.0.0_SA_COO~F`'s L7-done note, msg 96715, and its drain-end packet, 96714.

**Order:** the slug came first, then this analysis; `2.0.0_SA_COO~F`'s round-7 recut follows. This is the fourth round
running to reach L10 in the order the spine fixes.

---

## 0. WHAT ROUND 6 DELIVERED -- SAID FIRST

- **Orders:** 5 of 5 complete and drained (FE-s-37 .. FE-s-41), in ONE issuance @`79b2ddf558`. All 41 of the project's
  orders read terminal.
- **Rows:** 21 new, all dispositioned: 11 DISMISSED (every one of the four BLOCKING/ARMED rows among them, each fix
  quoted at portal DEV `35797660` and DISARMED) and 10 GRADUATED. Carrier-less rows: 0 of 217.
- **L9:** 5 judgment criteria; 4 MET (3 with a named qualification) and 1 NOT MET, **F39-AC10**.
- **The round-5 rulings reached code:**
  - S: the flip path binds the governing order. The CVO's three-arm run shows the doctored instance, bound, reads
    INVALID and names both orders.
  - U: every browser verdict names its server, 8 of 8.
  - V and the renderer half of T: the business-date plane.
  - W: one writer, and a flagged code reads as flagged. Applied on Holdings only; see RULING Z.

## 1. THE COVERAGE READ -- NO ADDENDUM OWED; THE PROJECT CANNOT CLOSE

- **No addendum.** Round 6's cells served rulings S-W, carried from round 5. No endpoint outcome gained or lost a cell,
  and round 5's coverage read (every endpoint outcome served by at least eight cells) is not moved by a round that only
  added cells. No FWD is uncovered.
- **The project cannot close,** for round 5's reasons, which round 6 did not change:
  - the evidence is fixture-bound;
  - every outcome except FWD-12 needs `IRPT_BCKEND` for its EXERCISED proof;
  - FWD-11 is PARTIAL (the Global view reaches one of two firms' Holdings, `W2-S23`).
- **This now meets the sequence.** `IRPT_BCKEND` is last in `org/missions/SEQUENCE.yaml`, after the Logic stage, by
  Andrew's ~14:5xZ word. So IRPT_FNTEND's closing proofs wait on a project that waits on three others. Round 7 can
  still close real gaps (s.3), but each round after it approaches the limit of what the frontend can prove on fixtures.
  The seat question this raises is put to Andrew in s.5 and is not ruled here.

## 2. F39-AC10 -- NOT MET, AND WHY IT IS A CUT DEFECT

`contracts/adapt.ts:585` still maps an out-of-enum directory advisory to `'unknown'`, the rename RULING W forbids, at a
site the order itself names (`W3-S29`). The cut's grant did not reach it: `CohortValue` is shared by three axes, and
`ScopeSummary.tsx` was not granted. The worker recorded *"STILL LESS THAN THE DOCUMENT"* and stopped at its grant, which
was the correct act. RULING Z carries the fix. No emitter sends an out-of-enum directory advisory today, so nothing is
live-wrong. The rule is still unmet at a named site.

## 3. THE RULINGS FOR ROUND 7

- **RULING X -- THE CUT'S REACH IS A SUBTRACTION, NEVER A RECALL.** This is the second round running where tests or
  fixtures carrying a ruling's removed behaviour sat outside the cut (`W3-S27`, `W3-S28`, `W5-S5`). Each was caught at
  the worker by the whole-suite bound, as designed.
  - Before a cell that carries a ruling's change is cut, the issuer runs the WHOLE suite with that change applied (or
    reads the corpus unscoped) and grants every test, fixture and map that the change turns red, each one named in the
    grant.
  - The census domain is the corpus, never a folder. `W4-S15` below is what a folder-scoped census cannot see.
  - This is `2.0.0_SA_COO~F`'s own remedy (96715), bound here as a round-7 bound on the cut.
- **RULING Y -- AN ISSUER RE-RUN NEVER USES THE WORKER'S WORKTREE** (`S64`). Every pre-drain re-run happens on a branch
  synced with DEV, or on an untouched pair. `git ls-files --eol` is printed beside any byte-compare. A re-run in the
  worker's own tree repeats the worker's instrument, and that is repetition, not corroboration. This is also
  `2.0.0_SA_COO~F`'s remedy, bound here.
- **RULING Z -- RULING W REACHES EVERY SITE IT NAMES** (`C-S92`). One cell is granted:
  - `contracts/adapt.ts`'s directory site (`:585`, the cohort use), `CohortValue` and `ScopeSummary.tsx`;
  - `contracts/validate.ts:448` (the three-value pin, `W3-S30`);
  - `ReceiptPanel.tsx`'s Reason line (flagged, never bare, `W2-S33`).
  - It must reach this bar: an out-of-enum advisory at every use site is shown verbatim and flagged. F39-AC10's clause
    is re-graded at the directory site.
  - The same cell stops fe-s-32's browser test from rewriting the committed captures (`W3-S31`).
- **RULING AA -- THE L7->L8 RECEIVING ROUTE BINDS THE GOVERNING ORDER** (`W4-S14`). RULING S bound the flip.
  `receiving-check.py`'s route to the checker (`:71`, `:117` @`adfbe65590`) still passes the instance alone, so its
  verdict still comes from the instance's own `to_ref`.
  - One cell binds it: the receiving seat passes the order it is handed, and the route hands it on as
    `--governing-order`.
  - An unbound call reads NOT-BOUND, never VALID.
  - The battery's arms are a doctored `to_ref`, bound (refused, both paths named) and unbound (NOT-BOUND).
  - `3.0.0_SA_CVO` binds its own intake and audit scripts, as its slug says. The tool is a CTO-lane's
    (`1.0.0_SA_CTO~Z`, @`adfbe65590`); this ruling places its fix in this project's checker lineage (FE-s-29, FE-s-37).
- **RULING AB -- THE RED BATTERY IS DIAGNOSED, NOT INHERITED** (`W4-S15`).
  - Measured at HEAD `059526828b` by this seat (`python org/standards/test_artifact_coverage_both_grammars.py`): 3 of 6
    PASS, rc=1. Arms A, B and E return rc=1 where rc=0 is owed.
  - The two anti-disable controls, C and D, pass only because EVERY arm now returns rc=1. So the battery currently
    discriminates nothing: its controls cannot fail while everything is refused.
  - One cell finds which limb of the checker refuses the battery's synthetic instances (most likely a limb added after
    the battery was written by `0.8.0_AE_CloudComp` @`ba59c67ada`, 2026-08-19), and brings whichever side is wrong
    current. Arms A, B and E then read rc=0, and C and D FAIL for their NAMED reason (the artifact-coverage violation),
    not by a blanket refusal.
  - The grant is the battery file, plus the checker only if the checker is the wrong side.
- **RULING AC -- A CRITERION THAT READS A FILE READS THE COMMITTED BLOB** (`W5-S7`, `C-S90`). Every round-7 criterion that
  inspects a file reads `git cat-file blob HEAD:<path>` or states that it reads the working copy and why. That is the S64
  fix's pattern, made a cut bound.
- **RULING U's residuals** (`C-S91`) go into one cell:
  - the vite-temp write through the junction (`W1-S63`; `package.json`'s dev script is the only lever, so it is
    granted);
  - fe-s-19's stale comment (`W1-S64`);
  - the two per-cell `cacheDir` overrides (`W1-S65`).

## 4. THE RECUT -- `2.0.0_SA_COO~F`'s ONE ISSUANCE (round 7)

Cut under RULINGS X, Y and AC. The cells reach:
1. RULING Z;
2. RULING AA;
3. RULING AB;
4. RULING U's residuals.

The split, the order and the fan-out are that lane's. No PRD half moves, so LIMB 6 does not wait on a signature.

## 5. CARRIED, AND FOR ANDREW

- **`W2-S32`, the contract's list of reason codes:** `IRPT_BCKEND`'s, beside `IRPT_BCKEND-S52`. It rides that project's
  next revision (packet @`67eca8268d`).
- **FOR ANDREW, NOT RULED HERE:** IRPT_FNTEND's closing proofs wait on IRPT_BCKEND, which the sequence places last. After
  round 7, the lane's remaining work is increasingly bounded by the backend. His ~18:2xZ word gives the next freed COO
  seat to LGIC_CANON. Whether `2.0.0_SA_COO~F`'s seat frees after round 7, or holds until the backend moves, is his call.
  - **This seat's rec:** free it after round 7 drains. LGIC_CANON waits on nothing but a seat, and IRPT_FNTEND waits on
    IRPT_BCKEND either way.
