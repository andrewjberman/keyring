# /self-drive dell2-box -- ticks 181-182 (2026-10-20 ~17:27Z-18:27Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 181 and 182, since the tick 180 log (@c5fb6c1830). state: ARMED.

## Never-widen halves signed

| grant | CTO half | packet bound | state |
|---|---|---|---|
| Resident role reads the model series and positioning (C-MODEL-SOURCE; `~G2`) | @a08bb1c202 | blob 0834df2dd4, sha256 a5200ee7 | IB2 STOPPED at step 3 (`fmt -check` rc 3 at pin 50f7c709af, whitespace); nothing applied. `~G2` re-pins and re-posts; this seat re-signs. |
| irpt-status-role reads `ycharts_opal_reports` (run 7b's R stop; `~Y2`) | @8461e95c62 | blob d6011af96e, sha256 262f55be | `~Y2` GO to IB2 at 18:13Z, at the drained commit 9b614db42a1. Run 7c follows the apply. |

## IRPT_ANLREQ PRD text changes

- **v0.27** @cd00de4ecb: C-AUDIT-RECORD becomes the platinum family ANALYSIS_AUDIT (table `analysis_audit`), written by the
  packager at attach (`~Y2` AR-y-462 REC).
  - CVO re-signed @c30a9c69d0, with grading notes: a null pdf/commentary pointer at attach, and a replace attach supersedes.
    Both were relayed to `~Y2`.
- **v0.28** @ea3014a892: the audit record's address is `opal-data-irpt/irpt/<firm>/platinum/analysis_audit/` (the IRPT product
  bucket under the firm prefix), not "each firm's bucket" (`~Y2` 18:21Z: the firm buckets are fenced against the resident role).
  - The difference from Andrew's words was stated to him at the terminal ~18:2xZ.
  - Re-reads were asked of the CVO and the CRO.

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
