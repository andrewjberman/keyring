# AMGT_CORPUS ROUND 26 -- L8 COMPILE (no judgment criterion; one WORLD act)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~01:0xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND26_DRAIN_END_PACKET.md` @`aa35ffcdca`, msg 27458. The packet was read to EOF (6,319 B).
**L7 re-measured:** `ab-1`, `ab-2`, `ab-3` and `ab-5` read `complete` on their LAST `<status>` tag. The ab-4 ledger is CLOSED. There are 0
judgment criteria.

---

## 1. THE SERVED STATE, RE-READ BY THIS SEAT

- **Census over the newest `derived/model_block/<key>/<stamp>` for 100 keys:** **UNRESOLVED 11** (BBSE3_BZ 10, TSM_US 1), and **0 sign
  contradictions**.
  - This equals the packet's 31 -> 11 over 100 keys.
  - BP's 20 from v30 (`PE_RATIO` 10, `PROF_MARGIN` 10) are resolved.
- **BP's market cap.** The deployed `/thesis` for `BP/_LN_Equity` serves `CUR_MKT_CAP` 89,798,586,794.73 with **currency None**, basis
  "UNMEASURED: the value is measured in GBP, which neither the quote label (GBp) nor the reporting currency states". That is an
  honest absence where a USD label was before. The negative arm, BA `CUR_MKT_CAP`, stays USD (reporting).
- **`Z-S71` end to end:**
  - BP's newest `research_dossier` object (`as_of=2026-09-30.3ea88471c4c27e6f`, written 09-30 23:44:57Z) references
    `derived/model_block/BP-SLASH-_LN_Equity/20260930T231718Z/model_block.json`;
  - NG's newest (`as_of=2026-10-01.2c6210ddb8afb8c5`, written 10-01 00:25:05Z) references
    `NG-SLASH-_LN_Equity/20260930T190147Z`.
  - Both read the encoded current blocks, no longer the kept 09-25 copies.
  - This seat's first read sorted the dossier keys lexically, which orders by hash, not time, and returned a 09-30 05:26Z object
    that still read the 09-25 block. Re-read by `LastModified`, the newest are as above.
- **The correction the packet owns** (section 3 item 1): the round-25 "375 measured" was 365 measured plus 10 to UNRESOLVED. That
  confirms this seat's v30 section 1 finding.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S71` (ARMED: `dossier.py` read model blocks on the RAW key) | **GRADUATED** | ab-1 routes both paths through `slash_safe_key`, and ab-4 leg d wrote BP and NG through the fixed reader. The newest dossiers reference the encoded blocks (section 1). |
| `Z-S70` (proof-of-spec-check accepts an older pin) | **CARRIED**, DISARMED by the CTO @`1730652e13` | the battery patch is parked with `0.8.0_AE_CloudComp` |
| `Z-W2-S18`, `Z-W2-S19` | **CARRIED**, ruled | as the packet |
| `Z-W5-S7` | **CARRIED**, INERT | basis text cites the round-25 census on round-26 figures |

## 3. FOR THE ROUND-26 ANALYSIS

1. **AMGT_RESAPP's redeploy carrying ab-3.**
   - The scoped API recomputes cases per request from its deployed `case_rule` (`scoped_amgt.py:3195`), so BP's mixed-currency 778.57
     input stays in `/thesis` until that redeploy.
   - The fix is in the block and not on the page. Read the live payload after the redeploy.
2. **The issuer's defect 2, a ledger sentinel's working copy that reverted two leg closes, cause not found.**
   - This is the "shared tree loses uncommitted work" class.
   - The remedy the issuer names (commit the sentinel after each leg close) is the right one. An uncommitted sentinel is evidence
     only on the plane that wrote it.
3. The 11 remaining figures: BBSE3 `CAPITAL_EXPEND` (6 zeros in 10 years; series median out of band) and TSM `CURR_ENTP_VAL`.
4. The 2 pre-existing test failures at the round-26 base (`test_readonly_proof_bound`, `test_harvest_prefixes`) should be routed to
   their owners rather than carried in every drain's hygiene line.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4, plus the issuer act. The ledger is CLOSED. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S71` GRADUATED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S32",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T01:00:00Z",
    "one_line": "L8 round 26: census over 100 keys reads 11 UNRESOLVED (BBSE3 10, TSM 1), 0 sign contradictions; BP CUR_MKT_CAP now prints no currency with an honest UNMEASURED reason (BA stays USD); Z-S71 graduates -- BP's and NG's newest dossiers reference the encoded current blocks; the mixed-currency case input stays in /thesis until RESAPP redeploys.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-ab-1, ab-2, ab-3, ab-5 read 'complete' on their LAST <status> tag.",
        "S3 opal-data-harvest derived/model_block/ newest per key, 100 keys: UNRESOLVED/POINTER 11 (BBSE3_BZ 10, TSM_US 1); sign contradictions 0.",
        "Invoke /thesis BP/_LN_Equity: CUR_MKT_CAP 89798586794.73 currency None basis 'UNMEASURED: the value is measured in GBP ...'; BA_US_Equity CUR_MKT_CAP USD reporting.",
        "research_dossier BP-SLASH-_LN_Equity newest by LastModified (09-30 23:44:57Z) refs derived/model_block/BP-SLASH-_LN_Equity/20260930T231718Z; NG-SLASH-_LN_Equity newest (10-01 00:25:05Z) refs NG-SLASH-_LN_Equity/20260930T190147Z."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S71"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @aa35ffcdca asserts UNRESOLVED 31 -> 11 over 100 keys, BP/NG dossiers read the encoded blocks, BP's market cap no longer labelled USD, and the case fix riding RESAPP's redeploy.",
    "world_is": "True as read on S3 and the deployed route.",
    "notes": "FOR THE ROUND-26 ANALYSIS: read /thesis BP's case inputs after RESAPP's redeploy; commit a ledger sentinel after each leg close; route the 2 pre-existing test failures."
  }
]
```
