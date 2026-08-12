# Overlay sweep window close — 15:18Z-17:32Z (0.4.0_DS_ClientPlatform)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

## Window
From the CPR-6 close (15:18Z, prior log window_chain_1424-1518Z.md) to the fee_efficiency
amendment commit @07e9226a5d (~17:31Z). Drive loop under COO cycles 17-23 + CVO verdicts.

## What landed (commits, all local on CLOUD; MSTR pushes)
- @45399c9ef8  V7 pinned_delta on fee_efficiency advisors[0].aua (pre-evidence)
- @60cc0e1c0f  fit_harness SHADOWED-PIN FIX + self-test control 5 + D5 dashboard pin
- @3b945255c2  dashboard + fee_efficiency PROOF_OF_SPEC overlay instances (VALID x2) + frozen reports
- @(bands)     V8-V13 declared pre-evidence for the apigw pair (6 new narrow kind-coherent rows + 3 pins)
- @b6aa49e701  d04_clients_tab.py emitter + clients_tab instance (VALID) + frozen report + V11 note amendment
- @d99e4eda59  d03 placeholder refinement + V7 re-pin (name-aligned)
- @07e9226a5d  fee_efficiency instance AMENDED re-VALID + report re-frozen

## The load-bearing findings of the window
1. SHADOWED-PIN INSTRUMENT DEFECT (found by the CVO-required monetary mutant): classify_divergence
   returns the FIRST matching registry row, so any pinned_delta on a LATER row was silently
   unreachable -- D6 'advisors*' swallowed V7's pin and the first monetary mutant routed DESIGN
   rc=0. Every prior PIN-dependent PASS (incl. CVO's own 10:53Z header_metrics verdict) was
   row-order luck. Fix: global pin_index across ALL rows (dup keys refuse loudly); control 5
   (a later-row pin must fire through an earlier broad band); self-test 5/5. CVO: "caught a
   defect in a prior CVO verdict -- that's the loop at its best."
2. S3 GOLD HELD ZERO P1 ARTIFACTS until the timing sample -- every evidence run had been
   --local-out; gold/canonical/ had only pre-P1 nna_atomic. The A-group dims are STILL not
   uploaded (fill prerequisite, reported). My earlier "grants already proven by the runner path"
   claim was wrong as applied to P1; the sample's own writes are the first grant proof.
3. IDENTITY-SPINE GAP (V8): served clients surfaces ride the BD household z-spine; canonical
   has NO household-grain identity (A_06 = SmartX-ACCOUNT grain, A_01 = rel_ hashes). Per-row
   alignment impossible BY INPUT. The crosswalk is HARVESTABLE read-only from the served detail
   family's own accounts[] lists (declared, not run -- offered to COO for sequencing).
4. DETAIL FAMILY WHOLLY STALE: gold/clients/{id} (2,948 instances) all mtime 2026-04-07,
   data_as_of 2026-03-31, behind a live lambda proxy, while clients_tab refreshes daily.
   Routed as a routing/freshness QUESTION with evidence (a REFERENCE is not a FAILURE).
5. PLACEHOLDER CONVERGENCE: excluding jd2's 'Unassigned' from the d03 universe (145->144)
   flipped the top row to the SAME NAMED ADVISOR served shows (Travis Penfield), shrank the
   pinned delta 35x (+899.3M -> -25.8M), moved 225 fields banded->clean. The attribution
   planes were nearly aligned; one placeholder made them look foreign.

## Measurements delivered
- UNASSIGNED FRAME to COO (161021Z): per-role denominators over 5,336 rows/$1,458,753,836.84;
  discriminator 2,355/2,498 architect-Unassigned carry a named advisor elsewhere; truly
  unattributed 143 accounts/$11,966,345.57 (0.8%); served carries zero Unassigned rows;
  the $1.286B was my emitter's union artifact (stated plainly).
- BACKFILL SCOPE to COO (163847Z): 3 chains, inputs fully exist (526 silver partitions each),
  P2 label INHERITED, executable-now, risk additive-reversible.
- TIMING SAMPLE (COO-authorized, 20 dates 2025-05-05..2025-06-02, 59/59 rc=0): B_00 cold
  2.59s/warm 0.93s; C_00 2.46/0.66; C_02 0.69/0.07 (local-read caveat). Extrapolation
  (stated as such): 525-date three-chain fill ~15 min warm / ~50 min cold-serial. Wrote 40
  QA partitions (canonical_valuation + flow_ledger, 2025-05-05..2025-06-02) -- ad-hoc QA
  artifacts, never production evidence.
- STOP-CONDITION REPORT to COO (172613Z): pair majority-banded, but gate TAXONOMY is the
  content -- backfill-gated ~10 / spine-gated 2 (cheap harvest) / input-blocked 1 / CLEARED 2.

## Verdicts received
- CVO 170538Z: dashboard CLEARS technical parity; fee_efficiency IN-FLIGHT affirmed, held on
  the Unassigned emitter defect (discharged this window, awaiting re-read).
- Banding ruling (CVO): fraction is a KIND not a THRESHOLD; two-part test (structural
  value-exemption + failing monetary mutant on a live core field). Applied to all instances.

## Boundary/regime changes ACKed
- Window fix RE-HOMED to ~A (CTO 165825Z / COO 165919Z): BOTH silver billing files
  (orion_billing_dim.py + build_billing_dim.py) under stand-off until ~A's window+flag acts
  close. My armed notify-~A instruction DISSOLVED.
- LEG (d) (COO 171037Z): INF_D_02 repoint off the silver flag -- READY declared (171222Z)
  with the consumption census (load_billing_dim:360 one ingress, ~8 read sites, loader-level
  swap); HOLDING for COO's window; (b) never fires before (d); D_04 second-derivation-site
  scope question surfaced.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| fit_harness | --self-test x2 (4/4 then 5/5); 8 surface runs (baselines+mutants), rc unpiped | PASS/FAIL exactly as designed; 1 instrument defect found+fixed |
| proof-of-spec-check | 4 instance validations (2 initial INVALID -> fixed -> VALID; 2 VALID) | artifact-coverage + schema violations caught and corrected |
| comp-estate | --resource clients_tab / bd-client-detail | thread owners resolved (advi-bd) |
| comp-find/raw | rail-checked s3 ls (unregistered new tree, existence census + positive control) | control FAILED first (empty gold tree) -> layout discovery -> finding 2 above |
What worked: the mutant battery as an instrument-grade control (it caught the harness itself).
What failed: my first mutant run piped rc through tee (masked rc), and an MSYS path reached
python open() -- both caught in-window, evidence discarded and re-run.
Gap found: no comp-tool models the new canonical tree (accepted until P2/P3 registration).

## Blockers
None assumption-grade. Held items are dispatch-owned: leg (d) window (COO), crosswalk harvest
go (COO), backfill decision (Andrew), CVO re-read of the amended instance.

## Current State (zero-context handoff)
- Repo runners_49f/: d00-d04 emitters committed; fit_harness.py with global pin_index +
  5-control self-test; predeclared_divergences_49f.json rows D1-D10, V1-V13, 7 pins across
  D5/V3/V7/V13; fit_reports/ carries frozen dashboard/fee_efficiency/clients_tab reports.
- Instances (org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/): HEADER_METRICS (cleared),
  FIRM_DASHBOARD (cleared), FEE_EFFICIENCY (amended @07e9226a5d, awaiting CVO re-read),
  CLIENTS_TAB (@b6aa49e701, awaiting CVO).
- S3: 40 QA partitions under schwab/08335338/gold/canonical/{canonical_valuation,flow_ledger}/
  date=2025-05-05..2025-06-02 + the asof evidence NOT uploaded (A-group dims still local-only
  at scratchpad p1_evidence/artifacts/).
- Stand-off: both data/inf/scripts/silver/*billing_dim*.py files are ~A's until their acts close.
- Kill-condition state: compile clause DISCHARGED (33/33); overlay numerator 2 CLEARED +
  2 awaiting CVO + ~10 backfill-gated + 2 spine-gated + 1 input-blocked.

## Next Steps
- [2.0.0_SA_COO] names the leg-(d) window -> I execute the INF_D_02 loader repoint WITH ~A's (b).
- [2.0.0_SA_COO] go/no-go on the crosswalk harvest (2,948 read-only GETs) -> un-gates the spine class.
- [3.0.0_SA_CVO] re-read of fee_efficiency @07e9226a5d + clients_tab @b6aa49e701.
- [0.4.0_DS_ClientPlatform] CPR-4 step 4 ticks on the next scheduled INF serve carrying both fields.
