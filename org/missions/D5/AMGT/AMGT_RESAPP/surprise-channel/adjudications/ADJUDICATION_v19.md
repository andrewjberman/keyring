# AMGT_RESAPP round 18: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T18:0xZ at HEAD `212afaa4f3`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND18_L8_PACKET_20260921.md` @`212afaa4f3`; the two orders; the channel census;
the adapter source at HEAD; one live read and one pair read from this seat.

## Round state

**2 of 2 terminal** (`rk-74` @`1dc7089050`, `rk-72` @`c1fdd952e1`). Acceptance **PASS 12 / FAIL 0 / UNVERIFIABLE 0 of
12 over 2 orders**; the order files carry 12 criterion ids (6 + 6); **judgment census 0 of 2.** No grade is owed.

## Checks the drain did not run

**`rk-74` (R18-A), the vintage on the served answer.** Source at HEAD: `scoped_amgt.py:1782` takes
`crosswalk.loaded_from()` and `:1720` serves it as `crosswalk_source` on the block, beside the document (`:1713-1714`),
so the module's byte-faithful invariant holds. Live read on the one key shape nobody sampled, the slash key,
both encodings: `BP%2F_LN_Equity` and `BP/_LN_Equity` each return 200 with `crosswalk_source =
s3://opal-data-harvest/crosswalk/v1/2026-09-19.json`; deployed CodeSha256 `P4n1bVaa...`, equal to the COO's read.
**`W54-S2` is now fully remedied** -- the key-shape filter (rk-68) and the vintage on the served answer (rk-74) -- so its
owed remediation row reads REMEDIATED, not the PARTIAL the round-16 analysis named.

**`rk-72` (R18-C), CSL's second seed.** Its one live write overwrote `UNRESOLVED-SOURCE.source.json` with a new version.
The signed pair names exactly that branch and its rollback (`ledger/NEVER_WIDEN_ROUND18_R18C_CSL_POOL_HALVES.md` :23,
:59, :120: `copy_object` from VersionId `OGe4GT77...`). **The write stayed inside its radius -- the census lesson from
`S192` held in the first round after it.** `W40-S1`'s remedy is executed: UNRESOLVED by design, every attempt carried
(seed 1 connection reset; seed 2, the ASX listing page, returned 200 and the crawl spent its 40-page cap on ASX's own
pages). Its owed remediation row reads REMEDIATED.

## Rows

`S193` set `DISMISSED_WITH_REASON` on its own row -- the round-16 disarm contract working; no supersession needed.
`S192` was dispositioned at ADJUDICATION_v17 C-S349. `W72-S1` is dispositioned below. Channel after this document:
**1 open, `W37-S1`** (the laptop CRO lane); `_graduated_without_row` 24, unchanged.

**PRD v0.15 is ADMITTED** (both halves SIGNED, `prd-signoff.py status` at HEAD), so round 19's hold on the PRD
halves is already lifted; the round-18 packet's line saying the halves are owed predates the stamps.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S354",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T18:05Z",
    "one_line": "L9 GRADE RECORD for round 18: 2 of 2 terminal, acceptance 12/0/0 of 12, no judgment criterion; rk-74's vintage read live on the slash key in both encodings; rk-72's one live write inside its signed radius.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 212afaa4f3: rk-72 6 and rk-74 6 criterion ids, parser reads the same, judgment=\"true\" in 0 of 2; --acceptance --round 18: PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 over 2 order(s).",
        "scoped_amgt.py:1782 loaded_from(), :1720 crosswalk_source; live invoke of /thesis for BP%2F_LN_Equity and BP/_LN_Equity: 200 and crosswalk_source s3://opal-data-harvest/crosswalk/v1/2026-09-19.json each; CodeSha256 P4n1bVaa.",
        "NEVER_WIDEN_ROUND18_R18C_CSL_POOL_HALVES.md :23, :59, :120 name the UNRESOLVED-branch overwrite and its copy_object rollback from OGe4GT77."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells pass on their criteria and on reads the drain did not run; W54-S2 and W40-S1 are remedied in full.",
    "notes": "Grade carrier only. The owed remediation rows for W54-S2 (C-S326) and W40-S1 (C-S330) now read REMEDIATED at the true L10 close.",
    "dismissal_reason": "Grade record: this row carries the round-18 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S355",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T18:05Z",
    "one_line": "DISMISSED onto W42-S5: rk-72's criterion script never extracts domicile, so step 5 prints 'jurisdiction UNKNOWN' where the rk-38 record reads 'AU' -- the outcome, no adapter, is the same either way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W72-S1: the order's own section-5 derivation script omits a domicile key; the live step 5 reads 'no adapter for jurisdiction UNKNOWN', the rk-38 record 'no adapter for jurisdiction AU'.",
        "Both read 'no adapter', so the crawl's behaviour and CSL's UNRESOLVED outcome do not depend on which string the step prints."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "AC4: steps 1-3 and 5 match the rk-38 record verbatim.",
    "world_is": "Step 5's wording differs because the criterion's own script dropped a field; the act and its outcome match.",
    "notes": "Instance of the bar-authored-without-measuring class carried at C-S335.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W72-S1"
    ],
    "dismissal_reason": "A criterion-script defect; the act's outcome is identical under either jurisdiction string."
  }
]
```
