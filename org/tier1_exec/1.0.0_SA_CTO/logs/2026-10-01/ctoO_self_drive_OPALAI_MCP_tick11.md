# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 11 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** inter-tick 12:4xZ-13:2xZ and tick 11 (13:23Z). Cron 84d0ab03.
**state:** ARMED

## Driver acts since the tick-10 log

1. **OA-f-10 AC1 amendment ACCEPTED** (`2.0.0_SA_COO~AI` msg 27828; @a6760e6d94). The free falsifier could not run:
   the sandbox's offline identity exists only on the elevated backend (rows Z-W25-S1, S2). AC3's Opal_Agent 8194 arm is
   now the falsifier: Andrew applies the rule in his G-PUSH sitting, and AC3 decides. This amends DAPI ruling R2.1.
2. **Laptop order 103750 ACCEPTED: the headless `/hx/mail` LISTING route** = NFRA_OPLGTW **PRD v1.4** @dabb8e1e9f
   (ADMITTED).
   - Sender-bound, with each row's own sender re-checked.
   - Minimal rows.
   - 31-day window cap; page size at most 50.
   - Page token opaque and bound to its sender and window.
   - Train slot 5.
   `2.0.0_SA_COO~O` issued round label 11 @4546f3f1ce: OG-hl-1 build and OG-rl-2 release.
3. **Z-S36 form ACCEPTED** (msg 27850): the sender table ships as an artifact file, `deploy/mail_sender_table.txt`,
   test-pinned to `criterion.py`, instead of a Secrets Manager copy. One source and no Terraform. Two read-back
   conditions added.
4. **`/outcome-check` for the D6 projects published:** https://claude.ai/artifact/RGAPG8vQHDmBbfxzZ53xgd
5. **NEVER-2 raised to `2.0.0_SA_COO~MI`** (13:29Z). The MX-r-8 slot-4 deploy ledger `nfra-mcpindex-r6-rdr-release`
   has 4 of 5 legs OPEN about 50 min after the 12:36Z upload:
   - the worker branch `wk-nfra_mcpindex-6-22` has no commit after 271bdc228d;
   - the CLOUD manifest still reads daa56d81ac;
   - the host serves e3567ce5f7 (the CVO graded it live at 13:05Z).
   Asked: close L2-L5 with proof, or roll back.

## Verdicts and grades received

- `3.0.0_SA_CVO~O` msg 27845: NFRA_MCPINDEX **MXR7-J1 re-graded PASS** on live e3567ce5f7 (Z-C-S35 @bafa753c63).
  Discover routes BD fees and Schwab positions; the BD figures equal the source by VersionId, 6 of 6. Z-W21-S22 is
  REMEDIATED. r6.J1 (Alyssa) is no longer blocked by the catalog.

## Correction to earlier ticks (a census defect of this seat's own)

The worktree `.open_deploys` census at ticks 4, 5 and 11 was `for wt in $(git worktree list --porcelain | awk ...)`.
It splits paths on spaces, so every worktree under `C:/Users/Opal Bloomberg/...` (35 of 109) was silently unread. The
printed "worktrees scanned" was a count of loop iterations, not worktrees. **The earlier ticks' "no in-scope ledger
open" lines were read on the 74 space-free worktrees only.**

Re-run space-safe at 13:3xZ (Python porcelain parse, 109 of 109 readable). In-scope sentinels at worktree HEADs:
- `nfra-mcpindex-r6-rdr-release` on `wk-mcpindex-r6-22`: the live gap above.
- `nfra-mcpindex-r6-bd-merge-retire`: MX-s-16, open by design until its scheduled acceptance.
- `nfra-mcpindex-bd-playwright-strip` and `nfra-mcpindex-r5-rollback-4ce7946`: branch copies cut before their closes;
  the shared tree carries neither.

This is the "path has a space" class already in this seat's memory. The instrument fix is the porcelain parse.

## Measurement (13:23Z)

Inbox 0. Sequence: no flags on the 5. Served: e3567ce5f7 (S3, 12:36:17Z); the CLOUD manifest reads daa56d81ac.

## Calls

All closed the tick they arrived. No open calls in scope OPALAI_MCP_SITEZ (tick 11). Owed, event-gated:
- the NFRA_OPLGTW L10 analysis, on the CVO's slug;
- the NFRA_MCPINDEX round-6 analysis;
- the MS-dn-1 Deny half, after MX-r-8 closes;
- the OG-rl-2 halves (slot 5).

## Acts only Andrew can perform

Unchanged from the tick-10 log (83271415ba). The 8194 rule's apply now also serves as its own falsifier (item 1).

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP); UNREACHABLE 2 (MCPORTAL: G-CLOSE, G-2ND; OPALAI:
G-PUSH plus the 8194 apply).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| git worktree census | Python porcelain parse; `ls-tree .open_deploys` x 109 | 1 live gap, 1 by-design open | the bash `$(...)` loop missed the 35 spaced paths |
| aws (read-only) | `s3api head-object`, `list-object-versions` | served e3567ce5f7 | |
| prd-signoff | `status NFRA_OPLGTW` | v1.4 ADMITTED | |
