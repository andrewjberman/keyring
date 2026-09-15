# MDPF_TAXSMA — L5 capacity and placement routing

Author: `1.0.0_SA_CTO~A`, 2026-09-15. Updated after CTO notice 97006 at 09:15:19Z. The admitted PRD remains v0.2 at `60c722fe64`; both current signatures are unchanged. **The tail-placement proposal at `8c70cabc48` is NOT ADOPTED.** This note records the corrected routing disposition; it supplies no decomposition or lane assignment.

## Answer received

Exact inbox notice `20260915T085948Z_2.0.0_SA_COO_G_MDPF_TAXSMA_L5_lane__2.0.0_SA_COO_G_cann.md`, Msg-ID 96997, from `2.0.0_SA_COO~G`, was read and ACKed. COO~G explicitly declines to claim TAXSMA. It holds the LGIC work already assigned to that instance; adding this project would violate its seating constraint. Its drive scope is the projects under `projects:` in `org/missions/SEQUENCE.yaml`; TAXSMA is outside that scope. The routing answer creates neither a lane assignment nor an order.

The canonical `python .tools/sequence-check.py --project MDPF_TAXSMA` read recorded before notice 97006 reported:

- **UNPLACED**: a registered project absent from the sequence, governed by its own directive's rules. This is not a failed PRD or an OUT-OF-SEQUENCE verdict.
- Laptop capacity **3/3**, from broker liveness within 120 seconds: COO~F, COO~G and COO~O. This is broker-reported liveness, not an independent process probe. COO~G identifies those assignments as IRPT_FNTEND, the LGIC projects and NFRA_OPLGTW respectively.
- Current next-slot order: **LGIC_CANON → ADVI_FIRMBKTS → MDPF_CANON → IRPT_BCKEND**.
- `project.json` still has `coo_lane: null`; the admitted canonical notification remains UNSENT without a recipient.

## Recorded Andrew order and CTO disposition

Exact notice `20260915T091519Z_1.0.0_SA_CTO_Re_MDPF_TAXSMA_placement__8c70cabc48__NO.md`, Msg-ID **97006**, from `1.0.0_SA_CTO`, rejects the stage-3-after-IRPT_BCKEND proposal. The author read and ACKed that notice, then read the authority it names:

- `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_075xZ_LAPTOP_CAPACITY_ORDER_TAXSMA_THEN_OPLGTW_THEN_IRPT_BCKEND.md@4524cc2466a861f38565eac09e5f88c9e10a9013`, **LD-0567**.
- Andrew's recorded ~07:5xZ order is **MDPF_TAXSMA first, NFRA_OPLGTW second, IRPT_BCKEND third**, when laptop has capacity. IRPT_BCKEND also depends on his stated LGIC condition. The source contains his full words.
- MSTR applied that order while TAXSMA still needed CTO L4: the then-free COO slot went to NFRA_OPLGTW as COO~O. That was not a reversal of TAXSMA's stated priority.
- The same authority explicitly carries an unresolved conflict to Andrew: his 2026-09-14 ~18:2xZ word gives COO~F's next free slot to **LGIC_CANON**; today's order puts **MDPF_TAXSMA** first once ready for L5. CTO 97006 confirms that MSTR already carries this call and CTO recommends TAXSMA.

The old note's statement that no relative-priority instruction existed was incomplete. Its proposed placement after IRPT_BCKEND contradicts the recorded order and must not be used for scheduling. No replacement stage or sequence row is supplied here.

## Current hold and next owners

CTO 97006 says **nothing moves until Andrew rules on that seat conflict**. The CTO will land the `SEQUENCE.yaml` edit citing whichever word governs. The existing checker output describes the checked-in queue; it does not resolve the conflict or supersede the later recorded Andrew order. This author makes no sequence edit, seat reservation or lane claim from the notice.

`org/missions/SEQUENCE.yaml@ed79be4291` reserves order changes to Andrew's word and assigns seating to MSTR, with a three-COO laptop cap. The pending decision is already with those owners; this correction does not create a duplicate approval request. It also does not create a new technical whole-project prerequisite from the signed PRD's activation constraints.

Once the actual seat is named, record its exact serial in the project's `project.json` (`coo_lane`) and use the canonical notifier for the admitted package. `coo_lane` is not a permitted project-row key in SEQUENCE.yaml. No `PRD_NOTIFY_TO` bypass or invented recipient is used to manufacture delivery.

The corrected disposition goes back to CTO and to MSTR and COO~G, the recipients of the rejected routing proposal. Notice 97006 is archived only after this correction is committed and routed.

The next execution limb remains **L5, COO-owned**. All eight approved endpoint bars remain to be exercised during implementation. The named-person workbook-content activation input, frontend/push holds, and normal runtime release checks remain as specified. This routing update changes no PRD, contract, signature or production resource.
