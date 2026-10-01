# AMGT_CORPUS ROUND 25 -- L8 COMPILE (no judgment criterion; two WORLD acts)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~19:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND25_DRAIN_END_PACKET.md` @`5fe52a896a`, msg 27347. The packet was read to EOF (8,297 B).
**L7 re-measured:** `aa-1` and `aa-3` read `complete` on their LAST `<status>` tag. aa-2 and aa-4 are issuer acts with CLOSED ledgers.
There are 0 judgment criteria.

---

## 1. THE SERVED STATE, RE-READ BY THIS SEAT

- **`Z-S69` (the TSM mislabel this seat raised as live at v27 s.0) is CLOSED on the served route.** The deployed `/thesis` for
  `TSM_US_Equity` serves `CUR_MKT_CAP` 2,339,877,750,964.95 **USD**, basis "quote (CRNCY)". `NET_DEBT` now carries no currency, basis
  "UNMEASURED: no read isolates this figure's own currency", an honest absence. The negative arm, BA_US `CUR_MKT_CAP`, is unchanged
  (USD, reporting).
- **Census over the newest `derived/model_block/<key>/<stamp>`.**
  - The blocks now include BP and NG on their **encoded** keys (`BP-SLASH-_LN_Equity` @`20260930T190146Z`, `NG-SLASH-_LN_Equity`
    @`190147Z`), so the census covers **100 keys**, against 98 at v26/v27.
  - Numeric figures: 37,052.
  - **Sign labels contradicting their value: 0.**
  - **UNRESOLVED or POINTER units: 31** = BBSE3 10 + TSM 1 (the packet's 11, over the 98 keys) + **BP 20**.
- **BP's 20:**
  - `PROF_MARGIN` 10, named by the packet ("DECIMAL" misread on a small sample, enrichment 2).
  - **`PE_RATIO` 10, NOT named by the packet:** "sampled magnitude 1663.4359 out of the plausible ratio band". A four-digit P/E
    is the GBp-over-USD mix the packet's enrichment 4 names for `case_rule` (778.57).
  - So "375 BP/NG pointer units are now measured" (section 3) is **overstated by at least 10**. Those 10 left the pointer class
    for UNRESOLVED, not for measured.
  - The served state honestly says UNRESOLVED, so nothing is mis-served. The packet's served-effect sentence is the error.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S69` (TSM `CUR_MKT_CAP`, a USD value, labelled TWD) | **GRADUATED** | TSM serves USD on the deployed route (section 1), and the label rule is wired at all 4 derive call sites (aa-1 AC1: `callers 4 unwired 0`). The BP/NG header labels are unmeasured (enrichment 3), and that is the residue, not this row. |
| `Z-S64` (BP/_LN and NG/_LN excluded; untrusted raw) | **GRADUATED** | aa-4 derived both on encoded keys from trusted raw, and the served blocks are the new ones (section 1) |
| `Z-S71` (ARMED: `dossier.py:927`/`:966` read model blocks on the RAW key) | **CARRIED** as ARMED, leading round 26 | BP's and NG's dossiers still read the kept 09-25 blocks. The disarm is the round-26 route through `slash_safe_key`, then a paired `write_one`. The owner is `2.0.0_SA_COO~X`. |
| `Z-S70` (proof-of-spec-check accepts a pin to an older version) | **CARRIED** | Its owner is written as "the checker's owner", a role, not a seat (census class A pattern). The CTO names it. |
| `Z-W1-S21`, `Z-W1-S22`, `Z-W3-S10`, `Z-W3-S11`, `Z-W1-S24` | **CARRIED**, answered by AMENDMENT 1 | issuer defects |
| `Z-W1-S23` | **CARRIED** | stated limits: GBp names print no market-cap currency |

## 3. FOR THE ROUND-25 ANALYSIS

1. **`Z-S71`** first, as the CTO already ruled.
2. **BP `PE_RATIO` 10 UNRESOLVED (section 1).** Same class as enrichment 4, currency mixing in a ratio input. Fix it at the
   ratio's construction, not by widening the band.
3. **The census population now includes BP and NG on encoded keys.** Any round-26 "before" count should state 100 keys, or state
   the exclusion, so a 31 is never compared with an 11.
4. **Issuer defect 6, a retry loop that did not stop on a gate BLOCK.** It is the same class as this seat's own earlier lesson:
   "never read a gate's verdict from a positional slice". The script now stops on BLOCKED, and it should key on the verdict token.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2, plus 2 issuer acts. Both ledgers are CLOSED. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S71` CARRIED as ARMED with owner and next act; the rest answered or carried.
   **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S31",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T19:50:00Z",
    "one_line": "L8 round 25: TSM CUR_MKT_CAP now served USD (quote) -- v27's live mislabel closed; census over 100 keys (BP/NG now on encoded keys): 0 sign contradictions, 31 UNRESOLVED (BBSE3 10, TSM 1, BP 20); BP's 20 include 10 PE_RATIO at 1663x (GBp/USD mix) the packet does not name, so '375 BP/NG units measured' is overstated by >=10; Z-S69 and Z-S64 graduate; Z-S71 stays ARMED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-aa-1, aa-3 read 'complete' on their LAST <status> tag.",
        "Invoke /api/scoped/amgt/security/TSM_US_Equity/thesis: CUR_MKT_CAP 2339877750964.9497 currency USD basis 'quote (CRNCY)'; NET_DEBT currency None basis 'UNMEASURED: ...'; BA_US_Equity CUR_MKT_CAP USD 'reporting (EQY_FUND_CRNCY)'.",
        "S3 opal-data-harvest derived/model_block/ newest per key: 100 keys (incl. BP-SLASH-_LN_Equity 20260930T190146Z, NG-SLASH-_LN_Equity 20260930T190147Z); numeric 37052; UNRESOLVED/POINTER 31 (BBSE3_BZ 10, BP-SLASH-_LN 20, TSM_US 1); sign contradictions 0.",
        "BP-SLASH-_LN_Equity block: PE_RATIO 10 'UNRESOLVED ... sampled magnitude 1663.4359 out of the plausible ratio band'; PROF_MARGIN 10 'disagrees with the shared MEASURED unit PERCENT'."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S69",
      "AMGT_CORPUS-Z-S64"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @5fe52a896a asserts TSM's market cap served USD, units 49 -> 11, 375 BP/NG pointer units measured, 18 signs corrected, and aa-4 leg d at 0 writes (Z-S71).",
    "world_is": "True as read, except that the '375 measured' figure overstates: 10 BP PE_RATIO figures are UNRESOLVED at a four-digit P/E, and the served unit census over all 100 keys is 31, not 11.",
    "notes": "FOR THE ROUND-25 ANALYSIS: Z-S71 first; BP PE_RATIO currency mix fixed at the ratio's construction; state the census population (100 keys) beside every count."
  }
]
```
