# AMGT_CORPUS ROUND 23 -- L8 COMPILE (no judgment criterion; one WORLD act under two pairs)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND23_DRAIN_END_PACKET.md` @`44b762332a`, msg 27095. The packet was read to EOF (5,700 B).
**L7 re-measured:** `y-1`, `y-2` (which carries y-5 as AMENDMENTs 1 and 2) and `y-3` read `complete` on their LAST `<status>` tag.
There are 0 judgment criteria.

---

## 1. THE SERVED STATE, RE-READ BY THIS SEAT

**Census over the newest `derived/model_block/<key>/<stamp>/model_block.json` per key.**
- `opal-data-harvest` lists 98 slash-free keys, plus 2 keys whose security_key carries a slash (`BP/_LN_Equity`, `NG/_LN_Equity`).
  The 2 slash keys are excluded under `Z-S64`, and this census skipped them.
- **Signs:** 35,678 figures carry a plain sign label, and **0 contradict their own value.** The packet's "1,569 -> 0" holds on the
  served state.
- **Units:** 36,280 numeric figures, UNRESOLVED **602**, POINTER **0**, not-measured **1.7%**. The packet's 612 UNRESOLVED and 375
  POINTER over 100 keys (2.6%) include the two slash keys. The difference sits exactly on the excluded names, so the two agree.

**Other re-reads:**
- **Dossiers:** `amgt/harvest/gold/research_dossier/` holds **380** objects (287 + 93, leg d).
- **VERDICT-B condition 1 (the formula text):** `lib/research/api/case_rule.py:73` reads "Bloomberg consensus EPS (FY1, BEST_EPS) x
  adjusted trailing-median P/E ...", and `:162` selects `BEST_EPS` FY1. The text kept on the 67 blocks is the true one. **MET.**
- **VERDICT-B condition 2 (the test plants):** y-5 AC3 reads `plain_disagree 0 convention_disagree 0` against a base of 1,568 plain
  and 1 convention case. The convention path is exercised, not only the loss-year path. **MET.**
- **The bound:** leg s landed at 09:40Z, before 12:00Z, so A was never executed.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S68` (the per-security sign mislabels loss years; the act widened them from 886 to 1,568) | **GRADUATED** | This seat's census reads 0 contradictions over 35,678 plain-signed served figures, and y-5 classifies each figure from its own value. |
| `Z-W2-S17` (a superseded test assertion) | **CARRIED**, ruled by AMENDMENT 2 | as the packet |
| `Z-W2-S16` (TSM has no stored same-currency anchor) | **CARRIED** | the mechanism is landed; the anchor is still absent |
| `Z-S64` (BP/_LN and NG/_LN) | **CARRIED**, widened | now excluded from the unit pass too; their raw-freshness read is untrusted |

## 3. FOR THE ROUND-23 ANALYSIS

1. **The issuer's corrected census.** The round-22 "25%" counted only the UNRESOLVED prefix; with the pointer class it was 42.5%.
   This seat carried the 25% figure into ADJUDICATION_v25 section 3 as stated, so that sentence is superseded by 42.5%.
2. **The two slash-bearing security keys** (`BP/_LN`, `NG/_LN`) break any census that splits on `/`. Before their pass lands, a key
   form without the slash should be decided, or every reader must parse them positionally.
3. The 602 remaining UNRESOLVED figures by class; the dossier `/5` objects wait on RESAPP's r52 redeploy; r-1's acceptance reads at
   the 13:00Z fire.
4. **The y-4 writer census traced unit paths only** (the issuer's own item). This is the same class as the HARVST o-5 cut-time
   misses: before signing, a pair should list every INPUT of the derive it runs, not only the path it intends to move.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 order files, 4 cells, all complete. The y-4 ledger is CLOSED. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S68` GRADUATED; the rest CARRIED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S26",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T10:50:00Z",
    "one_line": "L8 round 23: served census over 98 newest model blocks -- 0 of 35,678 plain sign labels contradict their value, 602 UNRESOLVED / 0 POINTER (1.7%; the packet's 2.6% includes BP/_LN and NG/_LN, excluded under Z-S64); 380 dossiers; both VERDICT-B conditions met (case_rule reads BEST_EPS; convention plant exercised); Z-S68 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-y-1, y-2 (with y-5 AMENDMENT 1+2), y-3 read 'complete' on their LAST <status> tag.",
        "S3 opal-data-harvest derived/model_block/: newest object per key for 98 slash-free keys; numeric figures 36280, UNRESOLVED 602, POINTER 0; plain-signed 35678, contradicting own value 0; 12 objects under the two slash keys BP/_LN_Equity and NG/_LN_Equity not parsed.",
        "S3 amgt/harvest/gold/research_dossier/: 380 objects.",
        "lib/research/api/case_rule.py:73 formula text 'Bloomberg consensus EPS (FY1, BEST_EPS) x adjusted trailing-median P/E (PX_LAST / IS_COMP_EPS_ADJUSTED)'; :162 selects BEST_EPS FY1."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S68"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @44b762332a asserts y-4 closed under two pairs, sign contradictions 1,569 -> 0 and not-measured units 42.5% -> 2.6% over the newest 100 keys, dossiers 287 -> 380, and the formula text kept as true.",
    "world_is": "True as read: 0 contradictions, 380 dossiers, BEST_EPS in case_rule. The unit share reads 1.7% on the 98 slash-free keys, and the remainder sits on the two Z-S64 names.",
    "notes": "FOR THE ROUND-23 ANALYSIS: v25's '25%' is superseded by 42.5%; decide a slash-free key form for BP/_LN and NG/_LN; a pair lists every input of the derive it runs."
  }
]
```
