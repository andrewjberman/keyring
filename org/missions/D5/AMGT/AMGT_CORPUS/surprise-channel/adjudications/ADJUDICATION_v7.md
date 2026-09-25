# AMGT_CORPUS ROUND 4 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-25 ~15:2xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND4_DRAIN_END_PACKET.md` @`e44d6ff5c2` (read to EOF), msg 25885.
**L7 state, RE-MEASURED not adopted:** 3 of 3 `CRPS-f-*` orders terminal on the LAST `<status>` tag; 10
acceptance criteria, **exactly 1 carrying `judgment="true"`** (`f-2` AC4), matching the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Denominator **12**.

| row | disposition here |
|---|---|
| `Z-S33` | **GRADUATED** -- the carrier; 89 of 89 served blocks non-empty, verified below on 5 keys |
| `Z-S26` | **GRADUATED** through `Z-S33` -- the 31 served-empty incident; blocks now serve content |
| `Z-S29` | **GRADUATED** through `Z-S33` -- history `{}`; the chunked request returns rows where the 39-field one returned nothing |
| `Z-S35` | **GRADUATED** -- the carrier for the disclosure re-mint |
| `Z-S34` | **GRADUATED** through `Z-S35` -- `crosswalk.main`'s write path lacked the live list |
| `Z-W1-S7`, `Z-W1-S8` | **GRADUATED** through `Z-S35` -- the issuer's own cut defects |
| `Z-S37` | **GRADUATED** -- the carrier for `Z-S30` |
| `Z-S30` | **GRADUATED** through `Z-S37` -- extract stored 353 of 353 report_ids, the CPA duplicate a NAMED skip |
| `Z-W2-S7`, `Z-W2-S8` | **GRADUATED** -- worker rows, INERT |
| `Z-S36` | **CARRIED** -- 9,471 `model_rows`, **0 values**, and every row cites a hard-coded `not authorized` reason **that is now false**. Unremedied |

**12 = 11 graduated + 1 carried.**

## 2. ⭐ MY DENOMINATOR FINDING IS CLOSED, AND CLOSED BETTER THAN I ASKED

Round 3's adjudication filed that the served crosswalk **carried 94 folders while disclosing 89**, from a
2026-09-10 snapshot -- "a claim a reader cannot verify from the object that carries it". `f-1` fixed it:
`folders_in_records 94 == research_folders_live 94 == the records' own folder count`.

⭐ **And it added a field I did not ask for: `snapshot_stale_against_live: True`.** Rather than silently
replacing the stale vintage, the artifact now **carries the fact that its snapshot is stale** as data. That
is `A_VALUE_MUST_CARRY_ITS_CLAIM` applied to the disclosure itself, and it is the stronger fix -- a reader
who relied on the old field learns why it moved instead of finding it quietly changed.

## 3. L9 -- `f-2` AC4, GRADED

**The criterion:** for three named keys, the derived Model block's added history fields **beside the team's
own model workbook**: do the figures agree in **sign, scale and fiscal year**, and is every absent field
**absent WITH a reason**?

### ⚠ I CHANGED THE SAMPLE, AND THE CRITERION INVITED ME TO

The suggested keys were `ASML_NA` and `ADBE_US` -- **the probe batch the chunked-request fix was developed
on** -- plus `2317_TT`. A fix is weakest where it was not developed, so I kept the suggested keys and added
`8306_JP_Equity` and `IMB_LN_Equity` from the 86 that followed.

⛔ **AND ONE SUGGESTED KEY CANNOT ANSWER THE CRITERION AT ALL: `Adobe ADBE US` HOLDS ONE FILE, A RESEARCH
PACK PDF, AND NO WORKBOOK.** There is nothing to compare the served block against. Measured at the library
root, not inferred.

### (a) Absent WITH a reason -- **PASS, 163 of 163**

| key | FY rows | figures | unresolved | carrying a reason | empty |
|---|---|---|---|---|---|
| `ASML_NA` | 10 | 419 | 2 | 2 | **0** |
| `ADBE_US` | 10 | 359 | 52 | 52 | **0** |
| `2317_TT` | 10 | 420 | 0 | 0 | **0** |
| `8306_JP` *(mine)* | 11 | 291 | 46 | 46 | **0** |
| `IMB_LN` *(mine)* | 10 | 358 | 63 | 63 | **0** |

⭐ **The sample change is what gave this half its power.** `ASML` -- the suggested probe key -- carries
**2** unresolved entries. The two keys I added carry **109 between them**. Grading the reason requirement
on the suggested set alone would have tested it on 2 absences; it is now tested on 163.

### (b) Sign, scale and fiscal year -- **PASS**

Compared against the team's own workbooks (`Overview!Financial Summary`), read directly:

```
ASML_NA   EPS / BVPS / DPS x FY2016-2021 = 18 comparisons
          sign      18 of 18 correct   (all POSITIVE)
          scale     18 of 18 correct   (PER SHARE, same magnitude -- no 100x-class error)
          fiscal yr 18 of 18 aligned   (each served FY matches the workbook column)
          value     15 of 18 within 2%
2317_TT   EPS x FY2016-2020 = 5 comparisons, 5 of 5 within 2% (four exact to 4 d.p.)
          currencies: quote TWD == reporting TWD, mixed False, converted False
```

**The three exceptions are all `IS_EPS`** (2016, 2018, 2021), 2.4-3.8%, **in both directions**. BVPS agrees
to four decimal places on 6 of 6 and DPS is exact on 6 of 6. A one-sided or order-of-magnitude error would
be a defect; **a small bidirectional spread on one row while its neighbours are exact is a provider
DEFINITION difference** -- the block's own figure description says "Bloomberg's reported earnings-per-share
figure, Bloomberg's own definition", and the workbook computes EPS on its own average-diluted-share basis.
**Named, not waved through**, and the block discloses its definition, which is what makes the difference
legible rather than alarming.

⭐ **This is the test that would have caught `AMGT_RESAPP-Z-S265` (a P/E served 100x wrong). It did not
fire.** Scale is right, including on a non-USD name where a currency mix would surface.

### One reader trap confirmed at the bytes, and it is already known

`ASML`'s workbook `CSC` sheet lists **KPN / VOD / BT / ORA / TEL / TKA / RCI / T / SCMN / VZ / TEF** --
telecoms, in a semiconductor company's file. That is the FactSet ONE PAGER **template boilerplate** the
round-3 packet warned reads as tickers to a naive search. Confirmed here independently; **it is not ASML's
peer set and must not be read as one.**

## 4. BOUNDS

1. **`Z-S36` is the round's open defect and it is the same class as the one this estate keeps paying for:**
   9,471 `model_rows` carry 0 values while every row states `not authorized` -- **a hard-coded reason that
   was true when written and is false now that the figures have arrived.** The packet's own enrichment says
   it best: *"reasons belong to the data."* An absent-reason that cannot go stale is the fix.
2. **AC4 is graded on 5 keys of 89.** Sign/scale/FY agreement is established on the two names with
   workbooks; it is not a population claim.
3. **AXIS AND VINTAGE, per the round-41 ruling:** FWD-12 is served across **89** (the superseded snapshot);
   the disclosure is **94** (live). Those are different populations and both are stated as such.

## 5. L10 PRECONDITION

1. **Every task order terminal** -- 3 of 3. **MET**
2. **Every round-4 row dispositioned** -- 12 of 12. **MET**
3. **Every judgment criterion graded** -- 1 of 1, on 5 keys including 2 outside the suggested set. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S7",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-25T15:25:00Z",
    "one_line": "L9 round 4: f-2 AC4 PASSES on both halves -- 163 of 163 absent fields carry a reason and sign/scale/fiscal-year agree with the team's own workbooks on 23 comparisons -- graded on a sample I CHANGED, because two of the three suggested keys were the probe batch the fix was developed on and a third holds no workbook at all. My round-3 denominator finding is closed, and closed better than I asked: the artifact now carries snapshot_stale_against_live as data.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": ["AMGT_CORPUS-Z-S33", "AMGT_CORPUS-Z-S26", "AMGT_CORPUS-Z-S29", "AMGT_CORPUS-Z-S35", "AMGT_CORPUS-Z-S34", "AMGT_CORPUS-Z-W1-S7", "AMGT_CORPUS-Z-W1-S8", "AMGT_CORPUS-Z-S37", "AMGT_CORPUS-Z-S30", "AMGT_CORPUS-Z-W2-S7", "AMGT_CORPUS-Z-W2-S8"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: 3 of 3 CRPS-f-* orders terminal on the LAST <status> tag; 10 acceptance criteria, exactly 1 carrying judgment=\"true\" (f-2 AC4), matching the packet.",
        "I CHANGED THE SAMPLE AND THE REASON IS THE ROUND-41 LESSON. The suggested keys ASML_NA and ADBE_US ARE THE PROBE BATCH the chunked-request fix was developed on, and a fix is weakest where it was not developed. Kept them, added 8306_JP_Equity and IMB_LN_Equity from the 86 that followed.",
        "AND ONE SUGGESTED KEY CANNOT ANSWER THE CRITERION: the research folder 'Adobe ADBE US' holds ONE file, a research pack PDF, and NO workbook of any kind. Measured at the library root (library.library_root(), 94 folders), not inferred. AC4's first half is unexercisable on it.",
        "HALF (a), ABSENT WITH A REASON -- PASS, 163 of 163 across five keys: ASML_NA 2 unresolved / 2 with reasons; ADBE_US 52 / 52; 2317_TT 0 / 0; 8306_JP 46 / 46; IMB_LN 63 / 63. ZERO empty reasons. THE SAMPLE CHANGE IS WHAT GAVE THIS HALF ITS POWER -- the suggested probe key carries 2 unresolved entries and the two keys added carry 109 between them, so the requirement is tested on 163 absences rather than on 2.",
        "HALF (b), SIGN / SCALE / FISCAL YEAR -- PASS, compared against the team's OWN workbooks read directly from the research library. ASML_NA: EPS, BVPS and DPS across FY2016-2021, 18 comparisons -- sign 18 of 18 POSITIVE and correct, scale 18 of 18 PER SHARE and same magnitude, fiscal year 18 of 18 aligned to the workbook's own columns, value 15 of 18 within 2%. 2317_TT: IS_EPS across FY2016-2020, 5 of 5 within 2% with four exact to four decimal places, and currencies quote TWD == reporting TWD, mixed False, converted False.",
        "THE THREE EXCEPTIONS ARE NAMED AND ATTRIBUTED RATHER THAN WAVED THROUGH: all three are IS_EPS (FY2016, FY2018, FY2021), 2.4 to 3.8 percent, and IN BOTH DIRECTIONS, while BVPS agrees to four decimals on 6 of 6 and DPS is exact on 6 of 6. A one-sided or order-of-magnitude error would be a defect; a small bidirectional spread on ONE row whose neighbours are exact is a provider DEFINITION difference -- the block's own description reads 'Bloomberg's reported earnings-per-share figure, Bloomberg's own definition' while the workbook computes EPS on its own average-diluted-share basis. The block DISCLOSING its definition is what makes the difference legible.",
        "THIS IS THE TEST THAT WOULD HAVE CAUGHT AMGT_RESAPP-Z-S265, THE P/E SERVED 100x WRONG, AND IT DID NOT FIRE. Scale is correct on every comparison including a non-USD name, which is where a currency mix would surface.",
        "MY ROUND-3 DENOMINATOR FINDING IS CLOSED AND CLOSED BETTER THAN ASKED. f-1 brings folders_in_records 94 == research_folders_live 94 == the records' own folder count, AND ADDS snapshot_stale_against_live: True -- the artifact now CARRIES the fact that its snapshot is stale as data rather than silently replacing the vintage. That is A_VALUE_MUST_CARRY_ITS_CLAIM applied to the disclosure itself, and a reader who relied on the old field learns why it moved.",
        "A READER TRAP CONFIRMED AT THE BYTES: ASML's workbook CSC sheet lists KPN, VOD, BT, ORA, TEL, TKA, RCI, T, SCMN, VZ and TEF -- telecoms in a semiconductor company's file. That is the FactSet ONE PAGER template boilerplate the round-3 packet flagged as reading like tickers to a naive search. Confirmed independently here; it is NOT ASML's peer set."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @e44d6ff5c2 asserts 3 of 3 orders complete and drained, FWD-12 REALIZED with 89 of 89 served blocks non-empty, the disclosure re-mint at 94 of 94, the production sequence 10 of 10, one judgment criterion owed to the CVO with three suggested keys, and the dossier's Model rows NOT realized.",
    "world_is": "All of that holds as re-measured. f-2 AC4 passes on both halves. Two departures from the packet's own framing are recorded: one of its three suggested keys has no workbook and so cannot answer the criterion's first half at all, and two of the three are the batch the fix was developed on -- so the sample was changed rather than accepted.",
    "notes": "ONE ROW CARRIED: Z-S36, and it is the round's open defect. 9,471 model_rows carry 0 values while EVERY row states 'not authorized' -- a hard-coded reason that was TRUE when written and is FALSE now that the figures have arrived. ⭐ THE PACKET'S OWN ENRICHMENT SAYS IT BEST AND IT GENERALISES FAR PAST THIS ROW: 'reasons belong to the data'. A constant absent-reason cannot go stale loudly; it goes stale silently, and it reads as authoritative the whole time. That is the same family as a stale disclosed denominator and a stale line citation -- a value that was correct when written, carried forward by something that cannot know it has moved."
  }
]
```
