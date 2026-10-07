# ANDREW-DIRECT 2026-10-07 ~06:1xZ -- proceed NFRA_CTLPLN; COO~C on it only; MDPF_TAXSMA closed; the IRPT pair to dell1

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop), post-reboot session. **Recorded by:** `1.0.0_SA_CTO`.

## His words, VERBATIM, in order

1. ~06:0xZ: "We are coming back online post reboot. I want you to check the sequence.yaml. I am wondering if maybe it is prudent to push
   more work to the Dell Boxes, as they are more powerful than the laptop + they are not burdened with the same IT antivirus load. Let's
   discuss"
2. ~06:1xZ: "I need you to proceed NFRA_CTLPLAN"
3. ~06:1xZ: "bring COO~C on for this purpose. COO~C should only be focused on this work, not cottonwood backfill project."
4. ~06:1xZ: "MDPF_TAXSMA is done at this point, should be closed. IRPT_BCKEND, IRPT_YCDGEN should both be on dell1"
5. ~06:2xZ: "I would put IRPT_DASHBD and IRPT_CUSTDY on dell2 (need to better understand what IRPT_CUSTDY offers), also need to understand
   what, if any resources, are expected to be deployed for IRPT BCKEND and YCDGEN work, because we probably are going to need to open up
   the policy for dell boxes to allow for deployment of new resources."
6. ~06:2xZ: "Ok that means that whatever box is doing IRPT_CUSTDY should also be working on the COTBKF project."

## What this seat did on it

- Word 3: asked `0.0.0_AB_MSTR` to seat `2.0.0_SA_COO~C` on NFRA_CTLPLN; struck the `2.0.0_SA_COO~C` `/canonical-drive ADVI_COTBKF` row in
  `org/ref/LIVE_ARMS.md` and landed the NFRA_CTLPLN-only row.
- Word 4, MDPF_TAXSMA: `org/missions/D8/MDPF/MDPF_TAXSMA/project.json` `status: closed`, with his word in `phase`; removed from
  `org/missions/SEQUENCE.yaml`. `dep_stage` stays EXECUTING: `.tools/missions-tree-index.py` R6 refuses `dep_stage: CLOSED` without the
  COO's COMPLETION_REPORT and the CTO's COMPLETION_GRADES, and neither exists. Six order faces are open (TX-c-2, o-1, r-2, r-3, v-2, v-3);
  their terminal flips are the issuer's.
- Word 4, the IRPT pair: `placement: DELL1` and a `placement_ruling` on both tree rows; both `why` lines and a change_log entry in
  `org/missions/SEQUENCE.yaml`. This replaces the dell2 target of `CTO_PLACEMENT_20261007_FOUR_BOX_LAYOUT_ANDREW_APPROVED.md`.
- Word 5: IRPT_DASHBD and IRPT_CUSTDY already target dell2 in the sequence; nothing changed. The two questions are answered to him at the
  terminal.
- Word 6: ADVI_COTBKF `placement: DELL2` with a `placement_ruling` on its tree row; its `why` and a change_log entry in
  `org/missions/SEQUENCE.yaml`. This replaces its dell1 target. The seat that works it there is still unnamed.

## Not decided by these words (surfaced, not adjudicated)

- Which seat, if any, takes ADVI_COTBKF now. He named what `2.0.0_SA_COO~C` does not do; he named no successor.
- Any loop or cadence for `2.0.0_SA_COO~C` on NFRA_CTLPLN. He named none; the seat is event-driven with no cron.
- WHEN the IRPT pair moves. He named the box, not the moment; the standing rule (between rounds, never mid-round) is unchanged.
- Any change to the Dell deploy policy. Word 5 says "probably"; it asks a question and orders no change.
- Word 1 is a discussion opener, not an order.

-- 1.0.0_SA_CTO
