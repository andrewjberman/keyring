# /self-drive dell2-box tick 22 (2026-10-15 22:2xZ, 1.0.0_SA_CTO~DELL2)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`. This log covers
the time since tick 21 (@ba140a5cae).

## Andrew's words this tick
- **~21:3xZ (@cf8764df23):**
  - 90ef: a placeholder for now (row CLOSED; `~D2` told);
  - 2106: MSTR recommends it to the laptop box (routed);
  - 4608: stop the runner (STOPPED, read stopped; row CLOSED);
  - J4: being checked.
- **~21:4xZ:** the PROD firm chooser works, so J4 is DONE. The ticker swap is missing: the door asked the filer for a proxy (PRD v0.17
  @ab6de45efb, then v0.18 @c0993a9bbe).
- **~21:5xZ (via CVO~DELL2):** the unmatched-ticker decision tree, Yes / Replace / No. PRD v0.19 @70a3edb0eb; the CVO signed it.

## Acts since tick 21
- **CTO halves:**
  - the chain-cap code update @38966dc091;
  - r32 resident @803ea45ca3 (applier AQ2, `opal_pricing` OFF);
  - exemption ADDENDUM 1 @6112647190.
- **Rulings:**
  - 4255 (the cause read, LOCAL) @b11f73087f, with its xadj RULED and CLOSED;
  - 49F publishing does not wait on the evidence key @594e598878 (an erratum on my SmartX premise);
  - r33 by `~G2` @fb11003a1b;
  - the swap compose, then r34, then run 3 @ebfa463c5b;
  - the swap pool as a dated snapshot, with no IAM @b77453b2dd;
  - an unclassified holding takes the not-analysed branch, with the classifier afterwards and agent-curated classes refused @d35053237f.
- **Analyses:**
  - B-IN r124 @e5c8b143fe and r125 @3743d3d5ba (r124 closes; round 127 lands with 0.4.2, which itself landed @6ac152c83a);
  - B-49F r138-141 @7fdfe4f6e6 (reporting-gold live with 65 days; `VENDOR_REPORTED` out of `return_basis`).

## Open calls
3 open: 2106 (with the laptop via MSTR), c02c, e260.

## ACTS ONLY ANDREW CAN DO
- **c02c:** send `C:\Users\Test\Desktop\DRAFT_Inflection_Orion_account_start_dates.txt`, or not. It is outward-facing to a client firm.
- **e260:** the Opal_Terminal key. His hold: "let's not discuss the Opal_Terminal key further i will handle it".
- **2106:** now routed to the laptop box on his word. It is no longer an act listed for him at this seat; the row closes on the
  read-back.

## Completion test
NOT DONE. IRPT_DASHBD, IRPT_BCKEND and IRPT_ANLREQ are EXECUTING.

state: ARMED

## Compiler Tools
open-calls.py list, close, hold and add; xadj.py open and show; `aws ec2 describe-instances` and `stop-instances` (on his word); `aws ssm
list-command-invocations`; safe-commit.sh; MCP send_message and ack_messages.
