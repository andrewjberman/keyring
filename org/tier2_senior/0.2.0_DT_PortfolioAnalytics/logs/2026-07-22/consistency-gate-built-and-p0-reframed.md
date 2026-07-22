# Internal-consistency gate built + mutant-exercised; the Global P0 reframed on three points

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-22 (~0344Z -> 0405Z)
**Window:** fresh session (MSTR spawn for the MDPF FE promote) -> mission SUPERSEDED mid-startup -> gate built, committed, reported

## Summary
Spawned to promote the stranded MDPF FE (DEV->PROD). Mission was superseded during startup by COO+MSTR:
CTO had grounded a P0 -- live Global's `opal_aggregate_aua` != `model_aua + non_model_aua` -- and the
direction flipped from promote-forward to ROLLBACK. I ACKed the corrected mission (no promote, stay
reachable, 0159Z co-sign VOID for the re-flip) and flagged, unprompted, that my own 3/3 parity leg was
structurally incapable of catching this: **parity is not consistency.** COO routed the gate to me on that
basis. Built it, mutant-gated it, ran it against live -- and it corrected the incident's framing on three
points, one of which lands on the rollback rationale itself.

## What happened
1. **Startup:** /watcher (Monitor bdfd71vli), registered PID 24148, LD-0290 serial file, audit-archive
   (rc=0, snapshot not-due), owned-paths hook, comp-graph context. Identity CLEAN -- NOT REGISTERED at
   start, no `inbox-watch.sh` process for my serial, so no orphan and no kill needed (the whose-PID
   discriminator never had to fire).
2. **Mission superseded mid-startup:** COO 034403Z + MSTR 034450Z, both consistent. ACKed both same-turn
   with an explicit read-back of what I am bound to, including the one I judged most likely to arrive by
   accident: a "go" citing the 0159Z co-sign, which is VOID (it pinned the buggy coherent-9 ETags).
3. **Grounded the FE state anyway** (read-only, so the re-land is a known quantity): workspace CLOUD,
   portal main tree on DEV (Rule 19 satisfied), origin/DEV = aa8c0420, origin/PROD = 99fed48f, DEV exactly
   4 commits ahead. Named that the re-land is a 4-commit forward merge, not the 1 commit "promote
   @aa8c0420" implies.
4. **Flagged the gap in my own instrument** before being asked: a served-vs-published compare cannot see a
   defect present on both sides, which is exactly why 3/3 was honestly CLEAN while Global was wrong.
5. **COO routed the gate to me** (034839Z) on that flag. Started immediately rather than waiting out the
   CTO/CVO speak-now window.
6. **Grounded the field shape on live S3 BEFORE writing the invariant** -- and it was not what the brief
   assumed. `opal_aggregate_aua` exists ONLY on global; 49financial and inflection carry
   `partner_custody_total`. A gate hard-coded to the named field would have silently no-opped on 2 of 3
   firms while printing a clean sweep.
7. **Measured all three candidate invariants** across every firm and date, both sides, before coding.
8. **Built + mutant-gated + committed** @3e557741e, pushed CLOUD. Reported CTO (URGENT, non-blocking),
   COO, DS, CVO.

## The gate (`--consistency`, @3e557741e)
| Property | Decision | Why |
|---|---|---|
| Invariant | `total == model_aua + non_model_aua`, per firm, per date | the invariant the 3-pass structurally lacked |
| Total field | resolved BY PRESENCE from `(opal_aggregate_aua, partner_custody_total)` | MEASURED; global-only hard-code covers 1 of 3 firms and reports clean |
| Nulls | all-None -> honest-None skip+count; partial-None -> `PARTIAL_NULL` FAIL | absent is NOT zero -- zero-filling makes the exact live hole tie perfectly |
| Tolerance | $1.00 abs floor; **measured floor $1.01 printed by the test** | USD ~1e9 in float64 carries ~1e-6 real FP noise; floor sits ~6 orders above it |
| Uncheckable | absent artifact / absent total field -> rc=1 | **UNCHECKABLE IS NOT A PASS** |
| Cross-firm | companion check, flagged as BEYOND the routed ask | LD-0292 dropped-firm class; separately acceptable/rejectable |
| Exercise | 13 mutant clauses + a coherent control | a gate that never failed a seeded defect has never been tested; one that cannot pass is equally broken |

`--served` runs the same invariant against the legacy live artifacts, so "is what we serve today correct?"
is answerable by the instrument rather than an ad-hoc script.

## Verification (actual output)
```
SELF-TEST consistency CONTROL (coherent artifact PASSES, gate not stuck-red)=True
SELF-TEST consistency MUTANT-1 (live bug shape: total omits $153M component) -> RED=True
SELF-TEST consistency MUTANT-2 sensitivity: caught holes [1000000.0, 1000.0, 10.0, 2.0, 1.01]
                                            -> measured floor $1.01; sub-cent ignored=True
SELF-TEST consistency MUTANT-3 missing-is-NOT-zero: explicit None -> PARTIAL_NULL=True;
                                            truncated array -> PARTIAL_NULL=True
SELF-TEST consistency MUTANT-4 total field absent -> UNCHECKABLE (not a clean sweep)=True
SELF-TEST consistency PARTNER shape (partner_custody_total resolves)=True; partner defect caught=True
SELF-TEST consistency honest-None row (all 3 None) skipped+counted, not a violation=True
SELF-TEST crossfirm: clean rollup PASS=True; dropped firm CAUGHT=True;
                     partner-missing-at-date CAUGHT=True; date-joined (reordered partner ties)=True
SELF-TEST PASS
```
Live, rc=1 both sides:

| firm | SERVED (legacy live = rollback target) | STAGED (gold/mdpf_revamp) |
|---|---|---|
| global | **FAIL 429/429**, hole $64.4M-$203.8M | **FAIL 421/427**, hole $64.5M-$203.2M |
| 49financial | **FAIL 1 date** 2025-12-26, -$43,157,544.80 | **PASS 427/427** (revamp fixes it) |
| inflection | PASS 429/429 | **FAIL 3 PARTIAL_NULL** (05-21, 06-01, 07-01) |
| crossfirm | PASS | PASS |

## Findings that CORRECT the incident framing (all grounded, reported to CTO/COO/DS/CVO)
1. **ROLLBACK DOES NOT CLEAR THE DATA BUG.** Served global fails 429/429 with the same hole, back to
   2024-11-01. The revamp did not introduce it. Rollback clears the FE-mismatch; Global stays internally
   wrong, the old FE just doesn't show components beside the total. "Known-good" is true of the FE and not
   of Global's numbers.
2. **THE FIRM-SUM IS CORRECT -- the defect is the total-field COMPOSITION.** CROSSFIRM_PASS both sides;
   `(model+non_model) - opal_aggregate_aua == inflection.non_model_aua` at 421/421 dates, exactly. The
   circulating "DS fixes the Global firm-sum" would send DS into a component that never broke.
3. **The hole is not a flat ~$153M.** $64,478,099.34 (frontier) to $203,203,649.06, median
   $163,093,838.09. $153M matches early history (~2024-11 to mid-2025, 159 dates in [145M,161M]), not the
   frontier a user sees today.
4. **NEW, unowned:** staged inflection 2026-05-21 / 06-01 / 07-01 carry a populated
   `partner_custody_total` (~$202.0M/$206.2M/$202.6M) with BOTH components None -- a total with no
   components. Grounded fact; cause NOT asserted (Rule 22), routed to DS.
5. **The revamp fixes a legacy defect:** served 49f 2025-12-26 (-$43.16M); staged 49f clean 427/427.

## Blockers
None. Mission-bound to a HOLD, which is not a blocker. The re-land gate is external to me: DS's fix +
the exercised consistency gate + a FRESH never-widen co-sign + Andrew re-eyeball + CTO's go.

## Current State (zero-context handoff)
- **Mission:** NO promote of current state under any circumstance. NOT winding down. Holding REACHABLE
  for the clean FE-FIRST re-land. **The 0159Z co-sign is VOID for the re-flip** -- a "go" citing it is
  NOT a go, and I will route it back rather than act on it.
- **FE:** portal main tree on DEV. origin/DEV = aa8c0420, origin/PROD = 99fed48f, DEV +4 commits
  (aa8c0420, 1508d183, 5b1e44dc, 2f603319). The re-land is a 4-commit forward merge.
- **Gate:** `mdpf_parity_check.py` @3e557741e on CLOUD (HEAD==origin). self-test PASS.
  `--consistency [--published-prefix ...] [--served]`, rc=1 on violation.
- **rc CHANGE flagged to CTO:** `--all` now returns 1 when the consistency gate fails (previously always
  0). Parity verdicts still do not affect rc. Offered to revert to --consistency-only if it breaks usage.
- **Untracked cruft in the portal tree** (.runtmp/, org/, screenshots, catch404_final.png) -- noted for
  the promote's Step-1 cleanup; NOT deleted (recursive deletion needs human confirmation).

## Next Steps
- **[1.0.0_SA_CTO]** rules on (a) whether this becomes the STANDING pre-serve gate and who runs it,
  (b) the rc change on `--all`, (c) the corrected rollback rationale before it reaches Andrew.
- **[0.4.0_DS_ClientPlatform]** fix the `opal_aggregate_aua` composition (NOT the firm-sum); rule on the
  3 inflection PARTIAL_NULL dates -- honest -> I add a NAMED exemption, else they need fixing. Verify
  with `--consistency --published-prefix gold/mdpf_revamp` (rc=0 == clean).
- **[3.0.0_SA_CVO]** adversarial check of the gate itself -- I built it, so I cannot certify it. Four
  specific refutation targets sent at 040424Z (tolerance floor, undiscriminating-instrument test,
  cross-firm scope, PARTIAL_NULL over-fire).
- **[0.2.0_DT]** re-arm the date-joined parity harness against corrected data on DS's re-stage; run the
  consistency gate on the corrected set; on CTO's go WITH the FRESH co-sign confirmed, run /prod-deploy.
  Event-driven, reachable (Monitor bdfd71vli). No crons.

## MCP traffic
6 handled. IN: COO corrected mission (034403Z), MSTR spawn-hint correction (034450Z), COO gate routing
(034839Z). OUT: ACK to COO (034504Z), ACK to MSTR (034631Z), ACK+start to COO (034957Z), delivery reports
to CTO (040258Z), COO (040327Z), DS (040354Z), CVO (040424Z). RAVC: COO's routing request opened and
closed with evidence (commit + mutant output + live results), not a claim.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `mdpf_parity_check.py --self-test` | PASS | 13 new mutant clauses + control; measured floor $1.01 printed |
| `mdpf_parity_check.py --consistency --published-prefix gold/mdpf_revamp` | rc=1 (FAIL, correct) | global 421/427, inflection 3 PARTIAL_NULL, 49f clean, crossfirm PASS |
| `mdpf_parity_check.py --consistency --served` | rc=1 (FAIL, correct) | global 429/429, 49f 1 date; established rollback does NOT clear it |
| `commit-gate.sh` | PASS | py_compile + ruff py39 + Rule-15 future-annotations |
| `safe-commit.sh` (surface-check + risk-reflex) | PASS | @3e557741e; no critical surface; reflex CLEAN, denominator 1/1239 printed, map STALE 189.6h (measured) |
| boto3 S3 reads (data-access, off-rail per graph-presence) | PASS | field-shape + 3-invariant measurement across 3 firms x 2 sides x ~430 dates |

**What worked:** grounding the field shape on live S3 BEFORE writing the invariant. The brief named one
field; the estate had two, and only one firm carried the named one. Writing the obvious gate would have
produced a green sweep covering a third of the firms -- the `comp-iam`-fails-GREEN shape, in my own code.
**What worked (2):** measuring all three candidate invariants before coding, which is what separated
"the firm-sum is broken" (false) from "the total-field composition is broken" (true) and prevented DS
being pointed at the wrong component.
**What failed:** nothing functionally. One process error: I read an exit code from a piped command
(`... | grep`) and briefly had rc=0 for a gate that returns 1 -- the exact put-the-control-on-the-
RETRIEVAL trap in CLAUDE.md Git section. Caught it by re-running unpiped before reporting anything.
**Gap found:** the 3-pass had no consistency axis at all -- three independent instruments, one shared
blind spot. Three methods do not help when all three compare the same two sides. Now closed, mutant-locked.
