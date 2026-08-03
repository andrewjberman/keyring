# T4.A exemplar verdicts (4 tranches) + ADHOC LAG/shell-trace (outcome B) + 07-22 anchor correction

**archetype:** VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-03 ~22:00Z - 23:25Z (follows the WS-1 census log, same day)

## MDPF_GLOBAL.T4A -- 4 tranches landed, consumer enumeration executed

Commits: T1 Orion/Eclipse @a356870e40 (8 tables) -> T2 SmartX @248166c902 (3 MDPF feeds;
fact_model_aum_daily CLEAN) -> T3 BD-cottonwood @bd9a298559 (relationship-inclusive grains)
-> T4 Schwab RPS pair + consumer enumeration @387fa87c90. Every key pos+neg-exercised in
separate invocations (16 tables total), dup rate 0.0 on every measured partition; evidence
doc deliverables/MDPF_T4A/T4A_orion_eclipse_family_verdicts.md. Residue enumerated (smartx
10, BD siblings, 49f dims, schwab 17) -- the TO stays open on residue; the exemplar spine
is done.

**The night's findings (each routed, none adjudicated cross-seat):**
- SERVED-NUMBER DEFECT: 3 naive summers over the BD relationship grain + the DDB cohort
  tie-implied; served cottonwood Total-AUA overstates +$205,070.77 (~0.045%) on
  value-carrying dual-relationship days (>=07-22). THE 07-22 DDB PARITY TIE
  ($458,189,558.77) IS THE DOUBLE-COUNTED FIGURE (collapsed truth $457,984,488.00) --
  both legs shared the naive derivation; shared-derivation parity is not an instrument.
  Repair = 0.2.0's DC1 (already implemented in-tree by session end).
- Eclipse gap ledger short by one (05-21); docstring corrected @bb030199b8 (COO dispatch).
- cot LAG=0 latent risk MEASURED live (allocations full/near-empty alternation).
- partner_roster s2 disclaimer-sheet feeds: adjudicated DECLARATION-ONLY dead config by
  0.2.0; roster-content defect routes on the C1 spec.
- R-1 named risk (dual-writer bronze keys unattributable-by-construction) @95e1f062f2;
  BR1 TO staged for post-T4.A.
- Schwab RPS pair: the first genuinely CLEAN full-serve-window exemplars (436/436 both).

## ADHOC.cot-snapshot-lag1-parity-and-shell-trace -- OUTCOME (B), OPEN at the STOP

- FIX DEPLOYED: BD_SNAPSHOT_ASOF_LAG_BDAYS default 0->1 @bf4c0aabbe; cot plane s3 cp
  MATCH-verified (ETag==md5 94744092f0ffb9e61d9d286b215bd563); ledger
  change_management/20260803T231854Z @f72b94a07e. Mechanism precision: BD returns 1-3-row
  PARTIALS (~5KB xlsx) for incomplete as-ofs -- passes the has_data==0 guard by design.
- TRACE = OUTCOME (B): documented historical served propagation (cash_coverage_summary
  $0.00 off the 07-09 zero-row freeze, cottonwood_aua.py:17-31) + current latest-snapshot
  selection (A_00:327, A_01:29) over a plane carrying near-empty partitions
  (silver/allocations 07-27/07-29 at ~44KB vs ~122KB). STOPPED per pre-registration;
  scope call at CTO/COO (recommended fold into the Andrew disclosure package).
- Mirror diagnosis: mirror CURRENT (monolith cot bronze through 08-03-labeled); the 07-31
  silver frontier stop is the CONVERTER leg. Report-only.
- NEW: the bd plane's deployed copy of the shared script is 6 WEEKS diverged (07-09 vs
  07-24) -- deployed cot-only rather than smuggle the delta into the 49f runner; routed.

## ADHOC.0722-tie-known-wrong-anchor-correction -- EXECUTED

14-hit repo denominator classified: 2 superseded in place (slice docstring -- rides
0.2.0's DC1 commit per shared-tree coordination; my 07-23 log @c4259acec8), 2
note-to-owner with exact text (COO source map + DT trace -- the owned-paths lane gate
correctly REFUSED my author on both), 4 data snapshots enumerated-not-mutated (mock
fixtures + restore snapshots document served history), finding-records already the
correction, DDB rows noted to the emitter owner.

## Compiler Tools (T4.A + ADHOC mandates, observed vs expect)

| Run | Observed | Verdict |
|---|---|---|
| comp-estate per family (T4.A phase 1) | smartx vertical read T2 (census gap: the C5 monolith producer absent from its chains -- noted, grounded live); other families grounded via WS-1's comp-estate work same-session (cross-cited, not re-run) | PASS with drift noted per if_mismatch |
| comp-pipescript io per converter | assets-tree blindness confirmed (rc=2 --pipeline refusal, WS-1 gap note stands); hand-derivations labeled throughout (schema scans + source reads with file:line) | if_mismatch path: tool-gap notes accumulated to the 0.8.0~B coverage build |
| Key exercises (T4.A phase 2) | 16 tables x pos+neg controls, SEPARATE invocations, verbatim outputs in the evidence doc + registry rows | PASS -- zero asserted keys |
| Tranche reports (phase 3) | 4 tranche reports + the enumeration report, each with measured rates + exercised-key evidence + registry commit | PASS -- none REWORKed |
| ADHOC phase 1 (configs at source) | cot_bronze_ingest.py:94(->100) + bd-49f-interim.tf:310 both cited; gold consumption mechanism identified (latest-snapshot selection, file:line) | PASS |
| ADHOC phase 2 (trace) | outcome (b) with mechanism cite + served-value evidence (the documented $0.00 cash-coverage instance + current exposure) | (b) -> STOP executed, fix deployed as pre-authorized |
| ADHOC phase 3 (deploy verify) | head-object baseline BEFORE firing (caught the bd-plane drift), post-deploy ETag==md5, ledger, reports to COO+CTO | PASS |
| comp-grep denominator (0722-tie) | 14 hits repo-wide, every hit classified, variants stated | PASS |

## Open at session end (owners named)

- ADHOC LAG TO: OPEN at outcome-B (CTO/COO historical-impact scope call).
- T4.A residue (mine, next session); BR1 activates on T4.A completion.
- COO + DT record supersessions (note-to-owner text delivered 232457Z).
- bd-plane code refresh; converter-leg lag; LAG=1 first-fire verify (next nightly ~02:0xZ
  = the natural check that the fix landed behavior-grade -- whoever reads it: expect the
  snapshot primaries to request T-1 and land FULL, with T-day partials gone).

## Do NOT (successors)

- Do NOT commit build_cottonwood_mdpf_slice.py wholesale -- 0.2.0's uncommitted DC1 work
  + my docstring rider share the tree; their commit carries both.
- Do NOT cite $458,189,558.77 as a verified anchor anywhere, ever.
- Do NOT read the ADHOC LAG TO as closed -- outcome-B holds it open by its own terms.

## Addendum ~23:40Z -- shell-serve census (new GO @337aea9aeb) + Leg-2 self-correction

- Census @a6d1dc1797: 90 partitions row-counted, 222 surviving serve-writes, 26 near-empty
  marked; DAY-LIST = 07-28..07-31 x all 12 platinum artifacts consumed near-empty
  latest-snapshots; exposure closed 08-01; pre-07-19 serve moments UNKNOWN (no surviving
  versions). Routed to CTO cc COO as the Andrew-package input.
- Leg 2: my 232021Z converter-lag diagnosis was WRONG -- corrected on instrument evidence
  (set-identity PASS 732/732 frontier 08-03; snapshot as-of vs period run-date label
  frontiers). NO fix deployed to the working converter. Closure = tonight's scheduled
  advance, read not hand-run.
- Window precision folded from 0.2.0's convergent census @47f7c82dc1 (July onset 07-21;
  served June episode 06-15..06-18).
- Anchor TO closed at my seat (COO landed their record @0a17ddf3be; DT queued).
- Compiler Tools for the census TO: reproduced in the deliverable doc s.'Compiler Tools'.
