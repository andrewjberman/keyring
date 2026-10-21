# L4-R re-review -- ADVI_COTBOOKS PRD v0.3 @05143c53b0, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-21 ~16:3xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 9138 (acked). Half hash `64c7ee61baba`.
That is the same hash the base 3.0.0_SA_CVO refused at v0.2 (`L4R_REVIEW_ADVI_COTBOOKS_v0.2_RATIFIED_TEXT_20261017.md` @8f584cb1a3), so
the ENDPOINT and CONTRACTS bytes are unchanged since v0.2.

**Read:** the PRD at 05143c53b0 (the ENDPOINT block and its status lines); `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md`
and `..._20261020.md`; `ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md`; `python .tools/open-calls.py list`.

## Verdict: REFUSE (two grounds)

- **Ground 1 -- the ENDPOINT carries a SUPERSEDED endpoint.**
  - The PRD's block is FWD-1 to FWD-6, from `ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md`. Its status line still cites call
    `dell1-20261017T030813Z-0cf5`.
  - The live L2 record is `ENDPOINT_FORWARD_ADVI_COTBOOKS_20261020.md`, endpoint v2, with 8 outcomes, on Andrew's 2026-10-20 ~13:xZ
    word: "we cannot rely on Black Diamond for any critical function". It states: "**Supersedes:** `ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md`
    (FWD-1..6). Those ids are retired and never reused."
  - A PRD whose ENDPOINT is the retired text cannot be verbatim to the ratified pins, whatever Andrew does with v2.
  - Call `0cf5` reads `[CLOSED]` as "escalated to andrew", not as his confirmation.
- **Ground 2 -- endpoint v2 is unconfirmed.** Call `dell1-20261020T135705Z-ea86` ("confirm ADVI_COTBOOKS v2's 8 DONE WHEN lines ...") reads
  `[OPEN]`. The spine binds this half to the ratified pins (`CANONICAL_FABRIC_WORKFLOW_20260901.md` :120-121, :191). The CTO accepted that
  reading for NFRA_FIDSLVR today (msg 9134).

## Re-delivery

Re-paste the v2 block, FWD-1 to FWD-8 from the 2026-10-20 record, into ENDPOINT. Re-point the status line at ea86, and re-read CONTRACTS
against v2's no-Black-Diamond rule ("a Black Diamond read is allowed only in a column labelled as the comparison"). Then deliver after
Andrew answers ea86. That delivery is a full read, because the ENDPOINT and probably CONTRACTS change.

-- 3.0.0_SA_CVO~DELL1
