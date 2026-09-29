# DSGN_AMGTV1 ROUND 1 -- L10 CLOSE ADDENDUM (AV-t-4 terminal)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~07:0xZ - **Extends:** `ADJUDICATION_v1.md` @`357640b526`, whose L10
limb 1 was held on `AV-t-4`.

`AV-t-4` now reads `complete` on its LAST `<status>` tag. Round 1 is **4 of 4 terminal**, and the held limb is MET.

**`Z-W3-S1` (ARMED) and `Z-W2-S2` -- GRADUATED, measured by this seat:** the HeroGraphic stub is at portal HEAD
(`tabs.harness.cjs:90`, `'@/ui/components/graphic/HeroGraphic'`, portal `30f69ad0`, then `36485a07`), and this seat ran the
harness: **`CHECKS-OK 20 of 20`, rc=0.**

**L10 PRECONDITION: all three limbs MET** (4 of 4 terminal; every ARMED row dispositioned; 3 of 3 judgments graded in v1).

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T07:00:00Z",
    "one_line": "L10 close for round 1: AV-t-4 is terminal, so the round is 4 of 4; the tabs harness loads the merged page again -- this seat's run reads CHECKS-OK 20 of 20, rc=0, with the HeroGraphic stub at tabs.harness.cjs:90. Z-W3-S1 and Z-W2-S2 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-AV-t-4 reads '<status>complete</status>' as its LAST status tag at HEAD.",
        "git -C portal show HEAD:src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs, line 90: '@/ui/components/graphic/HeroGraphic': { ... }; portal commits 30f69ad0 and 36485a07 (AV-t-4).",
        "This seat ran 'node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs' in portal/: 'CHECKS-OK 20 of 20', rc=0."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W3-S1",
      "DSGN_AMGTV1-Z-W2-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "ADDENDUM 1 asserts AV-t-4 stubs HeroGraphic so the tabs harness loads the merged page, 20 of 20 again.",
    "world_is": "True as run by this seat: 20 of 20, rc=0.",
    "notes": ""
  }
]
```
