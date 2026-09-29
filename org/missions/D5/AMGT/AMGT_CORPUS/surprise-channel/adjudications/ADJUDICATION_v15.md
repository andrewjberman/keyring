# AMGT_CORPUS ROUND 12 -- L8 COMPILE (no judgment criterion this round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~11:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND12_DRAIN_END_PACKET.md` @`4f52b3f69d` (read to EOF, 4,991 B), msg 26579.
**L7 RE-MEASURED not adopted:** `n-1` reads `complete` on its LAST `<status>` tag; 0 judgment criteria.

---

## 1. THE SERVED ACT, READ BY THIS SEAT ON THE LIVE BUCKET

This is the R19 path the `vv-4` rollback required (AMGT_RESAPP `Z-S298`, and this seat's corrected verdict `Z-S299`). It is the
dossier store's own migration to the builder's canonical address, landed as its own project cell.

| read | result |
|---|---|
| `list_objects_v2` (paginated) `amgt/harvest/gold/research_dossier/` | **95 objects, 95 partitions** |
| same, legacy `amgt/harvest/gold/research-dossier/` | **846 objects, 95 partitions** -- untouched, no delete |
| `read_dossier("HEI_US_Equity")` through the trunk entry point | serves `s3://.../research_dossier/security_key=HEI_US_Equity/as_of=2026-09-29...`, method `/4`, Base EPS `6.03 / 6.80 / 7.73 / 8.99 / null` -- **identical** to this seat's round-11 read of the legacy `/4` object |
| `git grep -l research-dossier HEAD -- lib` | **0 files**; the control `research-` in `lib/research/corpus` finds 18 (the other five `research-*` stores stay legacy, as ruled) |

**Every after-state line the COO half named is reproduced here independently.** The held merge (code not landed at HEAD until both
halves were signed, so HEAD never read an empty prefix) is the right sequencing and is recorded as such.

## 2. L8 -- ROWS

`_latest_dispositions`: **97 items, 30 UNDER_INVESTIGATION.** That is 2 fewer than round 11's 32, exactly the two this seat graduated
in v14 (`Z-W1-S14`, `Z-S57`). **No new row this round**, which reproduces the packet's zero. The carried set (`Z-W2-S11`, `Z-S3`,
`Z-S6`..`Z-S9`) is unchanged.

## 3. WHAT IT UNBLOCKS, AND WHAT IT DOES NOT

- **It unblocks AMGT_RESAPP's `vv-4` re-land.** The grant line can now be written against `lib/opal_naming.py address()` output, which
  the naming gate grades as canonical, not NEW-and-out-of-pattern. That redeploy is RESAPP's order.
- **It does not change what users see yet.** The deployed scoped-API Lambda still reads the legacy prefix, which is whole. The page
  serves the same dossiers until RESAPP redeploys onto this code. The INTU "not in this pack yet" sentence (DSGN_AMGTV1 round 2) waits
  on that redeploy too.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 1 of 1. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- no new row; the carried set unchanged. **MET**
3. **Every judgment criterion graded** -- 0 in the round. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S15",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T11:35:00Z",
    "one_line": "L8 round 12: the dossier store moved to the builder's canonical research_dossier/ prefix, read by this seat on the live bucket -- 95 objects over 95 partitions, legacy research-dossier/ 846 untouched, the trunk read_dossier serving HEI from the new prefix with content identical to round 11's legacy read, and 0 hyphen literals left in lib (control 18). This is the R19 path the vv-4 rollback required; it unblocks RESAPP's re-land but changes nothing users see until that redeploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-n-1 reads 'complete' on its LAST <status> tag; 0 criteria carry judgment=\"true\".",
        "LIVE BUCKET, boto3 list_objects_v2 paginated over opal-data-harvest: 'amgt/harvest/gold/research_dossier/ objects 95 partitions 95'; 'amgt/harvest/gold/research-dossier/ objects 846 partitions 95'.",
        "read_dossier('HEI_US_Equity') uri 's3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=HEI_US_Equity/as_of=2026-09-29.90c55da8', method 'amgt-corpus-dossier/4', Base EPS ['6.03','6.80','7.73','8.99',None], equal to ADJUDICATION_v14's read of the legacy /4 object.",
        "git grep -l 'research-dossier' HEAD -- lib: 0 files; control git grep -l 'research-' HEAD -- lib/research/corpus: 18 files.",
        "L8: _latest_dispositions('.', 'AMGT_CORPUS') 97 items, 30 UNDER_INVESTIGATION (round 11: 32, less Z-W1-S14 and Z-S57 graduated in v14); no new row."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: adjudicates no investigation item; the round filed none.",
    "spec_asserts": "The packet @4f52b3f69d asserts n-1 terminal and VALID, 95 of 95 served at research_dossier/, legacy 846 untouched, and all five after-state lines equal the signed COO half.",
    "world_is": "True as read by this seat on the live bucket and through the trunk entry point. The deployed Lambda still reads the legacy prefix until AMGT_RESAPP redeploys.",
    "notes": "FOR THE ROUND-12 ANALYSIS: the vv-4 re-land can now write its grant at the canonical address; it is RESAPP's order. The legacy 846 objects are unread by trunk code, and their deletion needs the operator's word."
  }
]
```
