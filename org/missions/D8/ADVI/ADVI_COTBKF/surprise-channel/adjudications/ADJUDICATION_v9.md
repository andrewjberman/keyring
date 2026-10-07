# ADVI_COTBKF: CVO adjudication, round 11

<sweep_watermark>2026-10-07T13:1xZ</sweep_watermark>

Round 11 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~13:1xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_11_DRAIN_END_20261007.md @db0f34670c` (msg 577). 1 of 1 order (CB-k-1) complete and
VALID @50a35d3ada under AMENDMENT 1. 2 rows, both dismissed below; no row graduates. ARMED: 0. No price was fetched; the FILE goes to
MDPF_SECHIST through 1.0.0_SA_CTO~DELL2, and the pull is Andrew's per-use word.

```json
[
 {
  "id": "ADVI_COTBKF-C-S16",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T13:15Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-W27-S1 (CB-k-1's AC2 expected 2,914 securities with 8,091,310 days, two different sets; resolved by AMENDMENT 1) and D2-S21 (the correction of S19's wording) are dismissed; the price-need FILE recounts exactly.",
  "adjudicates": [
   "ADVI_COTBKF-D2-W27-S1",
   "ADVI_COTBKF-D2-S21"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "2,914 securities are never priced (6,259,410 days) and the 8,091,310 uncovered days span 4,545 securities (the 2,914 plus 1,631 partly priced). The worker stopped on the mismatch under its refusal clause; the issuer amended AC2 to the 4,545 the pull needs. This seat recounted the FILE: 4,545 rows, 4,545 distinct ids, YAHOO 3,226 securities / 5,773,776 days and BLOOMBERG_SITE_Z 1,319 / 2,317,534, summing to 8,091,310. The same conflation is in this seat's ADJUDICATION_v8 and round-10 grade text ('2,914 of 4,634 securities, 8,091,310 of 9,388,961 security-days' read as one gap): both figures are true, and they are two sets, not one; D2-S21 is the correction of record.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-D2-W27-S1, ADVI_COTBKF-D2-S21",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_11_DRAIN_END_20261007.md @db0f34670c",
    "deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv recounted: 4,545 rows; days_needed by source YAHOO 5,773,776 + BLOOMBERG_SITE_Z 2,317,534 = 8,091,310 (this compile's read, dell2 CLOUD, 2026-10-07 ~13:1xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An order-scope block resolved by the issuer's amendment, and a wording correction; the FILE recounts exactly."
 }
]
```
