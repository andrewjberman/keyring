# AMGT_RESAPP ROUND 40 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-25 ~01:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `DRAIN_END_PACKET.md` @`cc1a74568e` (read to EOF), msg 25825.
**L7 state, RE-MEASURED not adopted:** 7 of 7 `ro-*` orders terminal on the LAST `<status>` tag; **18
acceptance criteria, EXACTLY 2 carrying `judgment="true"`** -- `ro-1` AC4 and `ro-3` AC3, matching the
packet, against that attribute's 258 uses elsewhere in this project as the positive control.

⭐ **BOTH JUDGMENT CRITERIA EXIST BECAUSE OF THE ROUND-39 RULING**, and each says so in its own `<expect>`:
*"the round-39 ruling requires a judgment criterion on a cell that touches served figures."* The pattern
this seat reported over rounds 38-39 -- a fully green mechanical grid over a correctness defect -- is now
generating the criteria that grade its own class.

---

## 1. L8 -- THE CHANNEL COMPILE

Denominator **6**, the packet's s.4 list; all six filed OBSERVATION / INERT.

| row | surfaced by | disposition here |
|---|---|---|
| `W152-S1` | `~152` | **GRADUATED** -- the `description=` hookup was outside the cell's paths; wired at `f3de463222` |
| `Z-S271` | `0.7.0_AE_CloudOps~A` | **GRADUATED** -- 16 of 17 on the served plane; fixed at `f3de463222`, and `ro-7.AC2` now reads absences **17 of 17, extras 0**, re-run by the issuer and confirmed in the export read below |
| `Z-S269` | `1.0.0_SA_CTO~Z` | **CARRIED** -- the authenticated deployed render at 20:35Z carried no P/E. Its SUBJECT has not been re-measured: the deployed frontend is not promoted this round, so this row remains the **last measurement of the deployed page** |
| `Z-S270` | `1.0.0_SA_CTO~Z` | **CARRIED** -- the deployed P/E reads `BEST_PE_RATIO`, three of five members outside the 89. It is the GROUND of the three-valued ruling @`0d568cdf51`, whose surface is still to be named |
| `Z-S272` | `2.0.0_SA_COO~Z` | **CARRIED** -- posture packs are served verbatim from the stored 2026-09-15 snapshot, so `ro-5`'s producer fix reaches the page only on a posture re-run, which needs its own authorisation. Not remedied |
| `Z-S273` | `2.0.0_SA_COO~Z` | **CARRIED** -- served Peers carries P/E for 12 of 12; feeds the same open ruling as `Z-S270` |

**6 = 2 graduated + 4 carried**, and every carry names why: one subject unmeasured, two feeding an open
ruling, one needing an authorisation this round did not hold.

## 2. L9 -- BOTH JUDGMENT CRITERIA, GRADED ON THE SERVED SET

⚠ **The packet warns that `real-run/` (the fixture set) is STALE against the served plane** -- no verdict
field, an older peers partition. **Both criteria were graded on `real-run-served/` only.** The worker's own
judgment file for `ro-1` was likewise built on the fixture, before the join and the `Z-S271` fix, so it was
read as context and not as evidence.

### `ro-3` AC3 -- **PASS**

*"whether the Thesis section now says only what its sentences are."* This is the remedy for this seat's own
round-39 finding, and it was fixed the way the round-39 analysis ruled -- **the section, not the header.**

Served `thesis.png` now renders, in order: the absence line `Description: ABSENT -- no served D-1
company_description sentence passing the describes-the-business test`, then the heading **"FILED DETAIL
(DOES NOT DESCRIBE THE BUSINESS)"**, then the three backlog sentences, kept reachable.

**The one thing that could still have made the page contradict itself was checked and does not.** The three
sentences carry `PASS` badges while the header says no sentence passes the describes-the-business test.
**They are different axes:** `description_verdict_state` is the describes-the-business verdict that gates
which FACE renders (`ThesisTab.tsx:238`); the per-sentence PASS/REFUSE face is `AMGT-rj-2`'s evidence face,
"KEPT BY CONSTRUCTION" (`:15`). No collision.

⭐ **And the load-bearing claim -- one verdict, not two implementations -- VERIFIES at the bytes:**

```
lib/research/api/scoped_amgt.py:2510   def company_description_verdict(...)   <- ONE definition
  :1705-1707  writes description_verdict_state / _reason onto the section entry
portal/.../ThesisTab.tsx:238           reads that field to pick the face
lib/research/print/render_pack.py:465  the EXPORT reads the same field and the same reason
portal/.../types.ts:629                "never a second implementation"
lib/research/api/tests/test_thesis_description_verdict.py  asserts the verdict is MECE over its domain
```

**Header, section and export cannot drift, because all three read one field.** That is the strongest form
of the fix: round 39's defect was two carriers of one claim, and the remedy removed the second carrier
rather than re-synchronising it. Two further properties worth naming: an **absent** verdict is treated as
NOT passed -- *"never claimed a pass this render cannot see measured"*, i.e. fail-closed on an unmeasured
verdict -- and the sentences are **kept reachable, never dropped**, so a labelling defect was not fixed by
hiding data.

### `ro-1` AC4 -- **PASS**

*"the rich export written beside the page's renders for a person to read."* Read `BA_US_Equity.rich.served.md`
(55,609 bytes) beside the served PNGs.

- It carries **the same two faces** as the tab: `## Company Description` -> the absence line -> `### Filed
  detail (does not describe the business)` -> the three sentences. That is the `ro-1` x `ro-3` join
  (`8f3f1c25df`) landing, and the reason appears at the **right grain in each place** -- the short reason in
  the section, the long composed reason in the header region, exactly as the page does.
- ⭐ **The refused series is carried AS A REFUSAL:** `IS_DIV_PER_SHR: REFUSED -- unit/sign convention is
  'SIGN-UNRESOLVED', not MEASURED`. **That is round 39's `Z-S268` closed at the artifact** -- the export
  that published 10 figures the page refuses now prints the page's own refusal instead.
- Every drafted sentence carries its passage id, accession, section path, paragraph number and the full
  source paragraph. That is MORE TRACEABLE than the page without being MORE CLAIMED: it expands the page's
  own `cites N passages` disclosure, and `ro-7.AC2` measures **extras 0**.

## 3. BOUNDS ON THIS VERDICT

1. **PLANE.** The served set pairs the **deployed DATA** with the **LOCAL DEV frontend**. The round's portal
   changes (`ro-2`, `ro-3`, `ro-4`) are on DEV only and no promote was in scope, so **what the deployed page
   shows after `ro-7` is NOT measured**, by anyone, this round. `Z-S269` at 20:35Z remains its last reading.
2. **The grading narrowing was applied.** Per the CTO's adjudication @`0d568cdf51` and `6baf45575c` s.6.3,
   an act is graded against the rows it GOVERNS, not against every row the surface displays -- grading
   `ro-7`'s act C against all five deployed members would fail a correct act on three rows outside its
   universe. A wrong-domain grade produces a false FAIL as readily as a false pass.
3. **Not graded here:** the three-valued P/E rendering is an ENRICHMENT item on the CTO's list, not a defect
   fix, and it does not re-open this round.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 7 of 7. **MET**
2. **Every round-40 row dispositioned** -- 6 of 6; 2 graduated, 4 carried with named reasons. **MET**
3. **Every judgment criterion graded** -- **2 of 2, both on the served set.** **MET, and not vacuously for
   the first time in three rounds.**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S418",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-25T01:45:00Z",
    "one_line": "L9 round 40: BOTH judgment criteria PASS on the SERVED set -- ro-3 AC3 fixed this seat's own round-39 thesis finding the way the analysis ruled (the section, not the header), with the one-verdict-two-carriers claim verified at the bytes; and ro-1 AC4's export now prints the page's own REFUSAL for the series round 39's Z-S268 caught it publishing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": ["AMGT_RESAPP-W152-S1", "AMGT_RESAPP-Z-S271"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: 7 of 7 ro-* orders terminal on the LAST <status> tag; 18 acceptance criteria; EXACTLY 2 carrying judgment=\"true\" (ro-1 AC4, ro-3 AC3), matching the packet, against that attribute's 258 uses elsewhere in this project as the positive control.",
        "BOTH JUDGMENT CRITERIA EXIST BECAUSE OF THE ROUND-39 RULING and each says so in its own <expect>: 'the round-39 ruling requires a judgment criterion on a cell that touches served figures'. The pattern this seat reported over rounds 38-39 is now generating the criteria that grade its own class.",
        "GRADED ON THE SERVED SET ONLY. The packet warns real-run/ (the fixture set) is STALE against the served plane -- no verdict field, an older peers partition -- and that the worker's own ro-1 judgment file was built on that fixture before the join and the Z-S271 fix. Both were read as context, never as evidence; every grade below rests on real-run-served/.",
        "ro-3 AC3 PASS. Served thesis.png renders the absence line, then the heading 'FILED DETAIL (DOES NOT DESCRIBE THE BUSINESS)', then the three backlog sentences kept reachable. This is the remedy this seat argued for in round 39 and the analysis ruled -- the SECTION was the defect, not the header, and fixing the header would have made the page lie to agree with itself.",
        "THE ONE REMAINING WAY IT COULD HAVE CONTRADICTED ITSELF WAS CHECKED AND DOES NOT: the three sentences carry PASS badges while the header says no sentence passes the describes-the-business test. Different axes -- description_verdict_state gates which FACE renders (ThesisTab.tsx:238), while the per-sentence PASS/REFUSE face is AMGT-rj-2's evidence face, 'KEPT BY CONSTRUCTION' (:15).",
        "AND THE LOAD-BEARING CLAIM VERIFIES AT THE BYTES -- ONE VERDICT, NOT TWO IMPLEMENTATIONS: scoped_amgt.py:2510 is the single definition of company_description_verdict; :1705-1707 write description_verdict_state/_reason onto the section entry; ThesisTab.tsx:238 reads that field; render_pack.py:465 has the EXPORT read the same field and reason; types.ts:629 states 'never a second implementation'; and test_thesis_description_verdict.py asserts the verdict is MECE over its own domain. Header, section and export cannot drift because all three read ONE field -- round 39's defect was two carriers of one claim, and the remedy REMOVED the second carrier rather than re-synchronising it.",
        "TWO FURTHER PROPERTIES OF THAT FIX WORTH NAMING: an ABSENT verdict is treated as NOT passed ('never claimed a pass this render cannot see measured'), so it fails closed on an unmeasured verdict rather than defaulting to a claim; and the sentences are KEPT REACHABLE, never dropped, so a labelling defect was not resolved by hiding data.",
        "ro-1 AC4 PASS. BA_US_Equity.rich.served.md (55,609 bytes) carries the SAME TWO FACES as the tab -- '## Company Description' -> absence line -> '### Filed detail (does not describe the business)' -> the three sentences -- with the reason at the RIGHT GRAIN in each place, the short one in the section and the long composed one in the header region, exactly as the page does. That is the ro-1 x ro-3 join at 8f3f1c25df landing.",
        "AND THE REFUSED SERIES IS CARRIED AS A REFUSAL: 'IS_DIV_PER_SHR: REFUSED -- unit/sign convention is SIGN-UNRESOLVED, not MEASURED'. That is round 39's Z-S268 closed AT THE ARTIFACT -- the export that published 10 figures the page refuses now prints the page's own refusal instead. Every drafted sentence additionally carries its passage id, accession, section path, paragraph number and full source paragraph: MORE TRACEABLE than the page without being MORE CLAIMED, and ro-7.AC2 measures extras 0.",
        "BOUNDS. (1) The served set pairs the DEPLOYED DATA with the LOCAL DEV frontend; the round's portal changes are on DEV only and no promote was in scope, so what the deployed page shows after ro-7 is NOT measured by anyone this round, and Z-S269 at 20:35Z remains its last reading. (2) The CTO's grading narrowing @0d568cdf51 / 6baf45575c s.6.3 was APPLIED: an act is graded against the rows it GOVERNS, never against every row the surface displays, because a wrong-domain grade produces a false FAIL as readily as a false pass. (3) The three-valued P/E rendering is an ENRICHMENT item, not a defect fix, and does not re-open this round."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @cc1a74568e asserts seven of seven orders terminal with every proof instance re-graded VALID, two judgment criteria owed to the CVO (ro-1 AC4, ro-3 AC3), that they be graded on the SERVED set because the fixture set is stale, and six new rows all OBSERVATION and INERT.",
    "world_is": "Every one of those claims is TRUE as re-measured here. Both judgment criteria PASS on the served set, and both fixes close defects this seat raised in earlier rounds -- the thesis section's mislabelling and the export's publication of refused figures. The fixture-set staleness warning was material and was honoured: the fixture carries no verdict field at all, so grading ro-3 there would have read an UNMEASURED verdict as the absence of a fix.",
    "notes": "FOUR ROWS CARRIED, EACH WITH A NAMED REASON RATHER THAN A STANDING: Z-S269's subject is unmeasured (the deployed frontend is not promoted, so that row is the last reading of the deployed page); Z-S270 and Z-S273 feed the three-valued ruling whose surface is not yet named; Z-S272 needs a posture re-run carrying its own authorisation. ⭐ THE CLOSED LOOP IS WORTH THE ANALYSIS'S EYE: this seat reported in round 39 that two consecutive rounds had shown a fully green mechanical grid over a correctness defect, both caught only by a person reading an artifact. That became a rule -- a round touching served figures carries at least one judgment criterion. Round 40 carried two, BOTH graded here, and both confirm fixes to the very defects that motivated the rule. The instrument that found the class is now the instrument that certifies its remedies."
  }
]
```
