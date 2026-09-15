# MDPF_TAXSMA - L5 seat priority and routing

Author: `1.0.0_SA_CTO~A`. Updated after **CTO97073 at2026-09-15T12:55:50Z**. PRD **v0.2 ADMITTED at60c722fe64**; both current signatures remain unchanged.

## Current disposition

**The wait for Andrew to resolve the seat-order conflict is RELEASED. MDPF_TAXSMA takes the next free COO slot.** MSTR owns naming that exact seat; `project.json` still has `coo_lane: null`, so canonical L4 delivery remains held solely for an actual recipient. No lane assignment or L5 decomposition is represented as complete by this routing update.

Exact unread notice handled: `20260915T125550Z_1.0.0_SA_CTO_ANDREW_RULED_the_seat_order__MDPF_TAXSMA.md`, Msg-ID97073, sender `1.0.0_SA_CTO`. It relays Andrew's ~12:5xZ words verbatim:

> If push mdpf_taxsma as the next one followed by nfra_oplgtw

The CTO landed that order in **`org/missions/SEQUENCE.yaml` v4 at `8f0c4fa2bf1538031561ed60993976956e974efa`**. This author read the committed YAML: new stage0 contains MDPF_TAXSMA first and NFRA_OPLGTW second, both without waits_on gates. Stages1-3 remain as in the CTO's ruling. This resolves LD-0567's conflict with the earlier LGIC_CANON claim on COO~F's next free slot; it also confirms Andrew's earlier ~07:5xZ word at4524cc2466. The rejected tail-placement proposal8c70cabc48 remains **NOT ADOPTED**.

NFRA_OPLGTW keeps **`2.0.0_SA_COO~O`**. It needs no new slot while that lane remains active; it is next if the lane goes dark. IRPT_FNTEND round9 is not in Andrew's stated seat order and waits for a seat after these. COO~F is only a possible available seat if MSTR verifies its instance has no open orders; this notice does not assign COO~F to TAXSMA.

## Current sequence measurement

`python .tools/sequence-check.py --project MDPF_TAXSMA`, read after97073, reports:

- **PLACED, stage0**, PRD v0.2 ADMITTED with both current halves SIGNED; `dep_stage=PRD`, flag **NEEDS-SLOT**.
- **Next COO slot:** MDPF_TAXSMA -> LGIC_CANON -> ADVI_FIRMBKTS -> MDPF_CANON -> IRPT_BCKEND. NFRA_OPLGTW is already staffed, which is why it does not consume the next-slot queue entry.
- Laptop capacity **3/3**, lanes COO~F, COO~G and COO~O, from `org/mcp/liveness.json` registrations seen within120 seconds. This is the checker's broker-liveness observation, not an independent process or open-order audit.

The priority decision is settled. Remaining routing work is operational seating by MSTR and delivery to the named lane, not another Andrew approval.

## Next owners and exact handoff

1. **[0.0.0_AB_MSTR]** Name the next free COO seat for MDPF_TAXSMA within the three-session cap, checking the instance's open orders before treating it as available.
2. **[1.0.0_SA_CTO~A]** After that assignment, record the exact full serial in this project's `project.json` `coo_lane`. Do not put that key in SEQUENCE.yaml or infer a recipient from liveness alone.
3. **[1.0.0_SA_CTO~A]** Fire the repository's canonical L4 notifier for the unchanged admitted v0.2 package (`60c722fe64`) to the named round holder, and record actual delivery evidence. `.tools/prd-header-notify.py` intentionally holds a release without `coo_lane`; no `PRD_NOTIFY_TO` bypass is used. Delivery/READ demonstrates transport or intake, not L5 completion.
4. **[named COO lane]** Own L5 decomposition and the downstream canonical flow after receiving the admitted package. This note issues no task orders or implementation GO.

The named-person workbook-content authorization remains a capability-activation input under the signed PRD; it is not a new whole-project precondition on L5 priority. All eight approved endpoint bars still require deliberate walkthrough or controlled-test EXERCISED proof at delivery. This update changes no PRD, contract, signature, workbook or production resource.

## Superseded routing history

COO~G notice96997 declined the project under its assigned scope and capacity; that refusal did not select another lane. The earlier checker read TAXSMA as UNPLACED. CTO97006 then rejected the proposed placement after IRPT_BCKEND and kept movement held until Andrew resolved the competing LGIC_CANON next-slot claim. That decision hold is now superseded by97073 and SEQUENCE v4; the historical checker output is not the current queue.

Prior authority: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_075xZ_LAPTOP_CAPACITY_ORDER_TAXSMA_THEN_OPLGTW_THEN_IRPT_BCKEND.md@4524cc2466a861f38565eac09e5f88c9e10a9013`, LD-0567. No new sequence edit is made by this seat.
