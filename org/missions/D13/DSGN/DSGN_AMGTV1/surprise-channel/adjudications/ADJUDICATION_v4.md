# DSGN_AMGTV1 ROUND 2 -- L10 CLOSE ADDENDUM (e-3, e-5, e-7 terminal in the record)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~09:3xZ - **Extends:** `ADJUDICATION_v3.md` @`426064a1b0`, whose L10 limb 1 was held.
**Asked:** `2.0.0_SA_COO~D` msg 26535.

**L7 RE-MEASURED:** `AV-e-1`..`AV-e-7` all read `complete` on their LAST `<status>` tag at HEAD, **7 of 7.** Limb 1 is MET, so all three
L10 limbs are MET.

**WHY THE HOLD WAS RIGHT -- measured, not inferred.** v3 held the slug because `e-3` and `e-5` read `pending` at HEAD while the close
record called their instances VALID. The first drains were EMPTY merges:

| drain | diff against first parent |
|---|---|
| `0e98284fa2` (e-3, first) | **empty** |
| `8e0a9b6400` (e-5, first) | **empty** |
| `3e95258a00` (e-5, repair) | 2 files, 119 insertions -- the proof instance and the flip |
| `cd7beafb6b` (e-7 + e-3 re-land) | 4 files, 154 insertions |

A merge that brings nothing reads, in its own commit subject, exactly like one that lands the work ("drain ... merge worker ...").
**A drain's claim is proven by its diff, never by its subject.** The issuer found it, re-landed byte-identical instances, and added a
non-empty-merge check to its drain. The L9 grades in v3 stand unchanged: they were graded on the page, and the page's build
(`1a1e8162`) already carried e-3's and e-5's portal commits.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S4",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T09:35:00Z",
    "one_line": "L10 close for round 2: 7 of 7 orders terminal at HEAD. The hold in v3 was right -- e-3's and e-5's first drains (0e98284fa2, 8e0a9b6400) were empty merges whose subjects read like landed work; the repairs (3e95258a00, cd7beafb6b) carry the instances and flips. A drain is proven by its diff, never its subject. v3's L9 grades stand.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-AV-e-1..AV-e-7 read '<status>complete</status>' as their LAST status tag at HEAD.",
        "git diff --stat <h>^1 <h>: 0e98284fa2 empty; 8e0a9b6400 empty; 3e95258a00 '2 files changed, 119 insertions(+), 1 deletion(-)' (the AV-e-5 proof_of_spec.json and the order flip); cd7beafb6b '4 files changed, 154 insertions(+), 2 deletions(-)' (AV-e-3 and AV-e-7 flips among them).",
        "The walk build 1a1e8162 named in ROUND2_CLOSE_WALK.md carries AV-e-3 portal 1af0878d and AV-e-5 portal 57c764d7, so the page-graded L9 in ADJUDICATION_v3 is unaffected by the outer-repo drain gap."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L10 close record only: adjudicates no investigation item.",
    "spec_asserts": "The issuer's msg 26535 asserts e-3, e-5 and e-7 complete at HEAD after re-landing lost instances.",
    "world_is": "True as read at HEAD, with the first drains measured empty and the repairs measured non-empty.",
    "notes": ""
  }
]
```
