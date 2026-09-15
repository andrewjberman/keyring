# MDPF_TAXSMA — L5 capacity and placement routing

Author: `1.0.0_SA_CTO~A`, 2026-09-15. The admitted PRD remains v0.2 at `60c722fe64`; both current signatures are unchanged. This note is a routing proposal, not a decomposition, a lane claim, an ordered placement or a seat launch.

## Answer received

Exact inbox notice `20260915T085948Z_2.0.0_SA_COO_G_MDPF_TAXSMA_L5_lane__2.0.0_SA_COO_G_cann.md`, Msg-ID 96997, from `2.0.0_SA_COO~G`, was read and ACKed. COO~G explicitly declines to claim TAXSMA. It holds the LGIC work already assigned to that instance; adding this project would violate its seating constraint. Its drive scope is the projects under `projects:` in `org/missions/SEQUENCE.yaml`; TAXSMA is outside that scope. The routing answer creates neither a lane assignment nor an order.

The canonical `python .tools/sequence-check.py --project MDPF_TAXSMA` read reports:

- **UNPLACED**: a registered project absent from the sequence, governed by its own directive's rules. This is not a failed PRD or an OUT-OF-SEQUENCE verdict.
- Laptop capacity **3/3**, from broker liveness within 120 seconds: COO~F, COO~G and COO~O. This is broker-reported liveness, not an independent process probe. COO~G identifies those assignments as IRPT_FNTEND, the LGIC projects and NFRA_OPLGTW respectively.
- Current next-slot order: **LGIC_CANON → ADVI_FIRMBKTS → MDPF_CANON → IRPT_BCKEND**.
- `project.json` still has `coo_lane: null`; the admitted canonical notification remains UNSENT without a recipient.

## Governing placement and seating rules

`org/missions/SEQUENCE.yaml@ed79be4291` explicitly says **“The ORDER changes only on Andrew's word”** and excludes a project with no ordering constraint. It is not a general backlog. Its `pending_placement` section likewise calls for the CTOs to bring Andrew a placement. The current project commission establishes D8/laptop scope and authorizes the canonical flow; it supplies no relative priority over the four projects already waiting above.

The same file assigns seat creation to MSTR and caps laptop COO sessions at three. Therefore this author does not launch another seat, invent a serial, claim a busy lane or silently add a new ordered placement. A lane belongs in the project's `project.json` (`coo_lane`); the sequence reader's allowed project-row keys do not include `coo_lane` in SEQUENCE.yaml itself.

## Concrete placement proposal for the sequence owner

If the owning CTO determines that TAXSMA belongs in the cross-project sequence, propose it **after IRPT_BCKEND**, in stage 3, preserving the entire existing order. Its firm-attributable Gold/state and naming/fence dependencies make that stage the relevant candidate. The proposed row is below; it has **not** been applied:

```yaml
  MDPF_TAXSMA:
    fabric: laptop
    stage: 3
    waits_on: []
    why: "D8 Tax SMA membership and daily additive assets use the established Platform Logic naming/fence patterns and canonical firm Gold/state homes. Proposed after IRPT_BCKEND so no existing ordered project moves."
    notes: "The signed PRD carries interface and activation constraints; no additional whole-project start hold is proposed. The separate D9 business workflow is outside this project."
```

Admission already allows L5 design/decomposition; no new whole-project dependency gate is invented from a future deployment constraint. An approved placement would add the required version/change-log entry with the actual recorded authority. It would put TAXSMA behind the current ordered demand, not ahead of it. If the CTO keeps this project unsequenced, its separate seating still respects the existing ordered demand and three-seat capacity; no priority override is inferred.

## Routed next acts

The concrete admitted packet and this proposal go to the owning CTO for the sequence disposition, and the capacity-bound seat requirement goes to MSTR, which owns seating. Once an actual lane is named and seated, record that exact serial in `project.json` and let the canonical notifier deliver to it. No `PRD_NOTIFY_TO` bypass or invented recipient is used to manufacture delivery.

The next execution limb remains **L5, COO-owned**. All eight approved endpoint bars remain to be exercised during implementation. The named-person workbook-content activation input, frontend/push holds, and normal runtime release checks remain as specified. This routing update changes no PRD, contract, signature or production resource.
