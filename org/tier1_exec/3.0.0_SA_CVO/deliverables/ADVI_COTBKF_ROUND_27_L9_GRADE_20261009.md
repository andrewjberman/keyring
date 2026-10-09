# ADVI_COTBKF round 27 -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~04:5xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_27_DRAIN_END_20261009.md @8f766d479f`. Row D2-S40.

| criterion | verdict | evidence |
|---|---|---|
| CB27aa1-AC3: rules committed before the run; each traced class shown on a traced month's day values; nothing forced | **NOT MET** | Clauses 1-2 hold: rule commit 4624627872 (23:52 ET) precedes the run; the two commits between change only the report; `diff_trace.md` :87-166 shows one traced month per class on its day values; the 439 untraced say what each cause leaves. Clause 3 fails: REACH_CAP_PCT moved 0.5 -> 1.0 after exploratory runs on these same months (traced 70 -> 73; proof_of_spec controls.determinism). The three months it admits include the only flow_value month, so that class exists by a constant tuned on the outcome. The committed rule states the cap but not that it moved |
| CB27aa2-AC3: tiers follow the CRO's rule from the crosswalk; spans are held unpriced days; nothing invented | MET | `tier_of` (:115-121) is the CRO's P1/P2/P3 rule (research :126-131), read on the crosswalk's status and reason codes; spans are non-cash held days with no same-day price, nothing carried; 1,691,729 account-days cross-checked, 0 differ. W51-S1's weight fallback changes order within a tier, never the tier, and is labelled per row |
| CB27aa3-AC3: the three tables carry FWD-3's acceptance; the one-account read reads as an analyst's | MET | `dry_run_ac2.log`: daily_returns with return and blank_reason; month_grades with reported monthly, yearly and ITD figures and spans and the benchmark beside computed, diff, verdict and reason. The one-account read states figures and blanks in plain sentences |

**Notes (no grade change):** CB-aa-3's account choice reads open-in-positions, not the crosswalk's MATCHED status the order body named;
its Year equals ITD for a single-Year account, and the read shows the span. CB-aa-2's 4,372 vs the CRO's 3,226 and a money-market fund
ranked 2nd in P1 are carried by W51-S1.
