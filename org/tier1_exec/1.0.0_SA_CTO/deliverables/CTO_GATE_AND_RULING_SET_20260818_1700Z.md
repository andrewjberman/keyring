# CTO GATE + RULING SET -- queue drain before compaction (2026-08-18 ~1700Z)

**Context:** 17 messages queued at the CTO seat during the reset window (Andrew: "drain the queue and clear the gates, then I'll compact"). Three gates cleared, five rulings, four concurs. Each item cites its ask.

## GATES CLEARED

**G-A · P2-FLOOR-49F TF draft (AE 161446Z, `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/P2_FLOOR_49F_TF_DRAFT_20260818.md`) -- READ DONE, both decision rows ruled:**
1. **DEDICATED `advi_49f_floor_dlq` -- APPROVED.** The mdpf shared DLQ is itself a K3 KEEP-UNTIL-REHOMED residual that retires with the mdpf floor's own DLQ; cross-pipeline coupling on a queue we intend to delete would re-manufacture the two-homes class. A DLQ is a route (the floor pattern's own shape), not an alarm -- moratorium untouched.
2. **12:45Z cron -- APPROVED AS CANDIDATE**, final pin lands with DS~A's P2D-3 measured chain duration; must stay inside the ratified window (post-12:18Z Schwab silver landing, <= the 13:30Z CRO retarget). The apply remains gated behind tonight's fixture + P2D-4; my per-apply plan read happens at the apply as usual.

**G-B · TO-4 (AE 162536Z) -- CTO NEVER#3 HALF SIGNED** against the 10-row sha256 manifest (9 json/mdpf keys + `cache/custody_crosswalk.json`; `json/mdpf/49financial/aggregate-aua-timeseries.json` stays HELD behind T-B half 1). **bmkaud-evidence EXCLUDE -- CONCUR:** a frozen verification-evidence snapshot cited by `verify_channel_BMKAUD_WS5_FINAL` as its verification surface is a DECLARED exception (the closed-period-immutable kind), not "unused" under Andrew's word. Conditions carried (all already in AE's plan): fixture PASS first · ledger opens before the first delete · live principal census at exec with denominator · rollback copies verified present. Execute tonight after the 23:01Z fixture passes.

**G-C · TIGHTENING_ENUMERATION_SPEC @1dceb7d61d (CRO~A 163151Z) -- RATIFIED, all four joints.** Routing (COO decomposes; the J-hooks banked at COO release):
- **J2** (comp-state cp1252 -- the sharpest: reader-thread death yields stdout=None with rc==0, one caller-guard from a silent all-QUIET corpus): the one-line `state_scan.py:68` fix (`encoding="utf-8", errors="replace"`, the in-estate `comp_missions.py:36` pattern) + the planted-byte self-test leg. Comp lane, dated 08-19. The 33-of-184 unencoded-subprocess census stays SURFACED, no sweep in push week.
- **J1**: `to-check.py --proof-board` (ladder rung 2) approved; the additive schema `firm` field APPROVED (additive act, UNPARSED rendered never guessed).
- **J3**: the 5-of-9 atom runner + the **per-family lineage-declaration JSON landing WITH each P4-EMIT family (DS~B)** approved; the A1 acceptance is exactly right -- atom-5 must read VIOLATES on 49F today and flip at P2 (a conformance runner that cannot see today's true violation is broken).
- **J4**: the `P4_FLIP_ORACLES_49F` per-key table (fe_surface / must_change / must_not_change / mutant / discriminates-0v1), runnable 08-21 so non-discrimination is caught the day BEFORE flip day; COO folds row references into P4R-3/P4X-4. DELTA=0 keys carry read-path discriminators.

## RULINGS (COO items 1/2/5/6/8)

**R-1 · role_aua basis (COO item 1 -- un-gates the DECLARED-GATED d13/leaderboard families): PORT FIDELITY FIRST.** The P4-EMIT emitters **CONSUME the canonical role_aua ARTIFACT** (`gold/canonical/role_aua/{date}.parquet`) as a DECLARED input (lineage-declared per J3 atom-8) -- **never a re-derivation on a different basis inside an emitter**: a 15->9 population change is a served-CONTENT change, exactly the class the never-widen check caught on 08-12, and P4 moves routes, not content. Companion act, named now so the dependency is honest: **re-home the role_aua PRODUCER (`C_01c.role_aua_flow_join.py`) into the canonical scheduled path as a dim-family member** -- the TO-2 dim re-home pattern verbatim (wire the existing module, exercise unattended, value-tie); dated P3-residual, COO staffs (DS~A post-P1 or DS~B post-EMIT); **P5 teardown of C_01c gates on it.** The jd2 x canonical_valuation BASIS question is a separate content decision -- parked, goes to Andrew only if he wants the population definition changed; not folded into the flip.

**R-2 · bd merge-daily-incremental two-homes #4 (COO item 2 / census finding): COO's rec ADOPTED exactly.** (a) NOTHING tonight (7 weeks stale; tonight is not different; fixture contamination risk is real). (b) Convergence refresh of the S3 staging copy to HEAD -- **DS~A, dated 08-21** (post P1/P3-close; DS base is full through 08-21), one ledgered act, Rule 13 lane. (c) The leg-retirement question stays in P5-TEARDOWN where it lives.

**R-3 · comp-pipescript BD-gold registry blind to runners_49f (COO item 5): DEFECT accepted at my desk** (comp-tooling is foundational). Registry addition routed to **0.8.0_AE_CloudComp beside PREFIX-READS, dated 08-19, landing before the P4/P5 io clauses lean on it (08-20)**. Build note: the registry entry DERIVES from the corpus (a predicate over `data/assets/scripts/gold/runners_49f/`), never a hand list -- a predicate is not a roster. DS~A's census-JSON degraded path stands meanwhile.

**R-4 · DEPLOYCENSUS routing (COO item 6):** (a) **shared-advisor-router + public-data-router currency read = a P4 FLIP PRECONDITION** -- AE 0.7.0, dated 08-20: Rule-22a bytes-vs-built-from read; if divergence touches the flip path, the refresh lands + verifies before 08-22 or the flip re-dates (COO folds into the P4R preconditions). (b) yang-generate-cma committed-never-deployed: COO post-push allocation (not 49F). (c) the 14 bundled-vs-canonical declarations: owner-by-owner at P5, as COO staged. (d) EC2 manifest hygiene (2 nonexistent instance ids, Rule-8 rows): AE 0.7.0, small dated fix 08-20. (e) deployed member-sha comp-tool: the banked residual candidate, now census-evidenced -- 0.8.0 post-PREFIX-READS, COO staffs.

**R-5 · INF as_of label convention (COO item 8a): RULED -- `data_as_of` means the VALUATION AS-OF (T-1 basis), never the producer's run date.** Run metadata lives under its own names (`run_date` / `pulled_at`). INF_E_00's stamp is therefore a DEFECT of the label class (a name asserting a property the computation does not carry), fixed at ORIGIN per COO's post-push allocation -- the convention binds NOW so no new code copies it. (b) the inf-etf next-deploy checklist arm: concur, stays banked on that deploy's checklist. (c) the "W1 fixed the chain's end, links 1-3 still stamp run-dates" frame: kept.

## CONCURS (no change)

- **Enumeration over digit** (COO item 3): the frozen joint DS~B+CVO key list (P4E-1) is the 4a/4b/4c denominator; the plan's "15" is superseded by reference.
- **Backfill determination-then-price-or-discharge** (COO item 4): concur; DS~A's determination either prices the remainder (card to Andrew) or discharges with evidence and the plan line corrects.
- **DE's absent-flat point_class-first reading** (T-A): CONCUR -- source-grounded on the one law (`_flat_point_class` :2065-2087); stands, no overrule. My P4 attestation read = DE's one-command live exercise (`paired-provenance-read-exercise.mjs` on the four live artifacts).
- **deploy_ledger reader fixes A+B @0ae9d71ef5** (COO item 7): validated at the instrument owner's desk both directions; noted, nothing further.

FYI-class (W-29 close, seat cc's, RP-F2/DEPLOYCENSUS cc duplicates): read, no action. Queue empty at 1700Z.
