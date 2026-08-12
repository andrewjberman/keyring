# 49F overlay Units 1+2: firm_leaderboard + firm_ownership_map -- 1820-1910Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

## Window

Base DS dispatch 182003Z (Unit-1 firm_leaderboard, Unit-2 ownership_map) through both units
complete + CVO validation of Unit-1. Surfaced to Andrew before starting that this dispatch moves
me onto the 49F/Schwab side (his open question about my Inflection focus); proceeded on no
redirect.

## Delivered

- `data/assets/scripts/gold/runners_49f/d07_firm_leaderboard.py` + V19-LB-SUMMARY-AUA band row
  @fd72adf7d2 (registry BEFORE evidence); slug-grammar fix @b790aaca3e.
  Instance PROOF_OF_SPEC_49F_OVERLAY_FIRM_LEADERBOARD_20260811.json @5c9c3b1c0f VALID rc=0.
  **CVO VALIDATED @e56275ef45.**
- `data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py` @b790aaca3e.
  Instance PROOF_OF_SPEC_49F_OVERLAY_FIRM_OWNERSHIP_MAP_20260811.json @fe9ffd6f30 VALID rc=0.
- Frame finding ADOPTED: ShapeFrozenPublisher open_key_paths (base landed @82ba36381b from my
  183926Z finding -- KEYS-AS-DATA map nodes; fee_efficiency had passed on fixed-key luck).
- Census run-4 coverage gap MEASURED (platinum/49financial/ absent from the prefix enumeration,
  family row structurally impossible); base landed run-5 @2685dd34f1.

## Evidence (all rc UNPIPED)

- d07: SHAPE PASS diffs=0 unmapped=0; 146 advisors; firm_total 1,789,058,516.82 ties the pinned
  canonical exactly; shape mutant rc=1; monetary mutant +1M -> fit FAIL rc=1 with EXACTLY the 5
  V19 pin paths (off_by 1,000,000.0 each); clean fit PASS rc=0 FAIL 0 DESIGN 45,666/72,170.
- d08: SHAPE PASS (open-key /advisors); tamper guard PASS 146 advisors both planes; id mutant
  rc=1 naming the corrupted entity; shape mutant rc=1; fit PASS FAIL=0 DESIGN 24,649/31,735
  (whole value plane = V8 identity-spine under D6 -- the fit non-discrimination is measured and
  stated in the instance, which is WHY the tamper guard exists).
- Slug grammar MEASURED against served keys (jackson_o_brien / neil_tjon_hing / curry_pajcic_jr):
  non-alnum runs -> one underscore; both emitters fixed; d07 re-verified end-to-end at final
  state; overlap 145/146 (chad_crabill genuine universe member).

## Corrections on the record (mine)

- Near-claim "jd2 has no local_ops" REFUTED by grounding on the dim before shipping (d03's
  4-role ROLES list is that family's choice; jd2 carries local_ops + manager). In the instance's
  SURPRISES row; CVO credited the disclosure.
- Initial plan to emit total_implied_revenue live INVERTED by measurement (served value is
  WINDOW-ACCRUED: QTD 1.99M vs YTD 10.65M) -> typed zero V2.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-system | regen x2 (post-instance lands) | PASS -- both regens grounded at land HEAD; lands routed to COO (exec lane, 7f5a958bdf precedent) |

Native Grep/Read stage-2 drills on known runners_49f files + operational `aws s3 cp` (legacy leg,
the same read fit_harness does); zero estate-scoped raw greps -- the census gap was found by
reading the artifact's own prefix enumeration (denominator beside the absence verdict).

## Blockers

None open for me. Two routed-and-resolved this window (open-key frame @82ba36381b; census run-5
@2685dd34f1) -- both base-owned, both landed same-hour.

## Current State (zero-context reader)

- Both 49F units COMPLETE, committed, instances VALID; Unit-1 CVO-validated. Serving ports NOT
  done (base sequences; emitters are QA-emission only, artifact writes gated on shape PASS).
- Pending at COO: exec-lane land of my in-tree comp-system regen (HEAD=fe9ffd6f30 stamp;
  re-verify-or-re-run at land time). STRUCTURAL-TWOPHASE recurrence #3 flagged to CTO via COO.
- Next natural unit: d07 window-column re-arm post-fill-2 (real nna -> real ordering -> V2
  narrowing + re-pin) -- on base's word [0.4.0_DS_ClientPlatform].
- Standing INF watches unchanged: billing silver (~$209.48M book) + D_04 serve (fee $202.84M /
  non-fee $6.29M pins) on SCHEDULED fires; DIVERGE-SOVEREIGN total_aua universe ruling at Andrew.

## Next Steps

- [0.4.0_DS_ClientPlatform] fill-consumption re-arm dispatch (or continued honest idle).
- [2.0.0_SA_COO] regen land + the enumeration-vs-route-to-exec question at CTO.
