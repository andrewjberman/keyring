# /self-drive NFRA four -- ticks 20-22 + NFRA_MCPMSP L3/L4 (1.0.0_SA_CTO~O, site Z, 2026-09-30 04:50Z-05:5xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4

## Measured (the four projects)

- **Inbox:** 0 unread at each tick. The messages in between (26933, 26939) are acked.
- **Open TOs:** 12 of 180 (last-tag read). OG 4, OA 4, MP 2, MX 2.
- **Scope commits by other seats since 04:45Z:** none in the four projects.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE (acts per the tick-11 log).

## NFRA_MCPMSP (outside the four-project scope, on Andrew's own word)

1. **Andrew confirmed the DONE WHEN lines**, verbatim "yes aggreed for all of these". Record
   `ANDREW_DIRECT_20260930_05xxZ_NFRA_MCPMSP_ENDPOINT_CONFIRMED.md`.
2. **L3 registered @7c7848d589** under D6/NFRA: tree row, generated index, D6 members line; missions-tree-index 0
   violations.
3. **L4 PRD v0.1 @b90b97652f:** C1-C12, S1-S14, A0-A11, and 29 of 29 brief headings covered.
   - This seat ruled the five L2 open items: pilot scope and guest addresses (C3), the refusal log and its approver (C4),
     the FWD-1 data (A1), and the audit gap (to L5).
4. **COO seated:** 2.0.0_SA_COO~MS (0.0.0_AB_MSTR~Z msg 26933), recorded @5f29f92546.
5. **L4-R:** 3.0.0_SA_CVO~O SIGNED the ratified-text half, stamp @8647b72584 and review @8d6851f97c (msg 26939).
   - Verbatim grounding: "ENDPOINT is verbatim to @64617f8afa (33 of 33 records). C1-C12 agree with the record and with
     the MCPORTAL/OPALAI counterparts. I contest none of your four L4 rulings."
   - `prd-signoff status`: ADMITTED.
   - The CVO's non-blocking notes N1 (the tenant-registry writer inside MCPORTAL C4's single-writer edge) and N2 (the
     queue view's sibling sequencing) go to L5.
6. **L5 handed to 2.0.0_SA_COO~MS** (msg 05:52Z). project.json now reads blocking NOT BLOCKED -- L5 next.

## Calls

No open calls in the four projects (ticks 20-22).

## Acts only Andrew can do (each cited)

- NFRA_MCPMSP's live pilot: G-USER (an Opal Analyst M365 user, with Opal IT), G-IT-INF (Inflection's IT), G-ADVISOR (a
  named advisor), G-FIRM (his go-live word), and later G-KEY (per-firm API keys and caps; his spend).
- Unchanged for the four projects: G-ACCT step 5 (his login or spend), MCPORTAL G-2ND and G-CLOSE, OPLGTW G-D and
  Part D, and MX-t-11 (his widening word). G-C is external at Opal IT.

## Compiler Tools

- `.tools/missions-tree-index.py derive --write` and `check` (0 violations).
- `.tools/prd-signoff.py status NFRA_MCPMSP` (WITHHELD, then ADMITTED).
