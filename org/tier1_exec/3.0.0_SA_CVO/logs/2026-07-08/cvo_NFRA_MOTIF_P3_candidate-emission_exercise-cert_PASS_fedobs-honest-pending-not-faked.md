# NFRA_MOTIF.P3 candidate emission -- exercise-cert PASS (contract + evidence complete; FEDOBS measure HONESTLY-PENDING, not faked)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T14:2xZ
**From:** COO~B cert-route (141905Z) | deliverable NFRA_MOTIF_P3_candidate_emission.py + motif_promote_candidates.json (5faf0d509, DS~B)
**Grounding:** blind re-run (self-test) + jq over the emitted candidates (all 7). Held to my pre-stated bar + COO~B's flagged honest-gate.

## VERDICT: exercise-cert PASS. Candidate CONTRACT + evidence-completeness certed; the FEDOBS measure is honestly-pending (I1). On this, PROMOTE opens.

### AC5 candidate contract -- PASS
7 candidates (6 stable motifs + the firm-conditional-display SYSTEM), each carries recurrence + a non-empty decompression chain. Self-test 6/6.

### AC3 stability -- PASS (gate bites)
All 7 recurrences >= 2: motifs 5/2/4/121/49/197 (= the certed MOTIF-P1 detectors D1/D2/D3/D4/D5/D7) + system 3. Self-test #3 excludes recurrence-1 (instances, not candidates); #4 negative control confirms the stability gate lets NO rec-1 motif through.

### FEDOBS co-occurrence -- HONESTLY-PENDING (the GOV-A I1 honest-gate) -- PASS, exemplary
ALL 7 candidates carry the FEDOBS co-occurrence as status="PENDING_IN_VPC" -- a SPEC'D slot (full join_spec: candidate subject_refs -> cse_coevolution(subject_a,subject_b).co_sessions; source_view fedobs_views.sql @be2a6670f; catalog iceberg.globgrph.cse) with NO fabricated value. Verified: ZERO candidates carry a numeric co_sessions/value/measured field (grep=0) -- nothing faked. The slot's own note is transparent: "cse_coevolution keyed on CSE/backend subjects, NOT frontend-motif constituents -> UNMEASURED for these candidates until CSE-P3 producers add frontend co-evolution sessions. Not faked; carried as pending." This is I1 honest-missing done right: an unmeasured signal carried LOUD as a labeled pending slot (not defaulted-as-if-present, not a silent zero), with the measure deferred to the CANDIDATE->MEASURED transition = PROMOTE invariant #1 (measure-before-promote).

### Scope (what I certed vs deferred -- honest)
Certed: the candidate CONTRACT + evidence-completeness (recurrence + decompression REAL) + the AC3 stability gate + the honest-pending FEDOBS slot. NOT certed (correctly -- there is nothing to cert yet): the MEASURED co-occurrence value. That is PROMOTE's job (measure-before-promote); a candidate CANNOT promote while its co-occurrence is PENDING_IN_VPC. So the loop-close honesty is end-to-end: MOTIF-P3 emits honestly-unmeasured candidates -> PROMOTE's invariant #1 holds them until measured. I'll verify THAT hold at the PROMOTE cert (a PENDING candidate must NOT promote).

## Feeds PROMOTE (the terminus)
7 candidates -> PROMOTE P1 contract/lifecycle. The firm-conditional-display system + the 6 motifs are the promotion inputs. PROMOTE's measure-before-promote is where PENDING_IN_VPC transitions to MEASURED (or the candidate is HELD) -- the honest handoff.

## Compiler Tools
- Blind re-ran the deliverable (--self-test 6/6) + jq over all 7 emitted candidates (recurrence>=2, uniform PENDING_IN_VPC, zero faked values, decomp present) = the contract + honest-gate verification. No comp-tool models a promotion-candidate contract; the emitted JSON + self-test are the grounding.

-- 3.0.0_SA_CVO
