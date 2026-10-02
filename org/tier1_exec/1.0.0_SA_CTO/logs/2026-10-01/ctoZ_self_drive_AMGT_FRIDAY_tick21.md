# /self-drive AMGT_FRIDAY -- tick 21, `1.0.0_SA_CTO~Z`, 2026-10-01 22:51Z-23:46Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 23:45Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
- **The demo freeze holds** at portal DEV `3c37a01c`.
- **AMGT_HARVST:**
  - Round 36 amendment 1 issued repair cell HVST-ai-4 (50ca06792c, Z-S57: a bbg HTML branch in silver).
  - The ft worker was stopped after 4 failed renewals to protect the account (Z-S56).
- **ETFS_RIVALS:**
  - PRD v0.9 is SIGNED by CVO~Z (ac93507a8d, msg 28089); Addendum B stays PROPOSED until Andrew.
  - Round 5 is issued as ONE issuance of 8 orders (cd11d6edea).
  - The per-fund floor carrier row Z-S13 is filed (1d9af9180c).
- **Inbox:** 0 unread. Acked: 28079, 28083, 28085, 28089.
- **Push state (ls-remote):**
  - origin CLOUD `a3866c3dfb`;
  - origin portal DEV `d79b9934`, PROD `f2731ad3`;
  - local DEV `3c37a01c`.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

## Calls closed and acts taken

| item | ruling or act | hash |
|---|---|---|
| COO~H 28083: a mid-round repair for Z-S57 (772 of 779 bbg articles stuck on JSONDecodeError) | **YES, one bounded cell.** A bbg HTML branch in silver, with the JSON path untouched. Plants: one real bbg body, plus a JSON-publisher control. Drain the outbox with before and after counts. Gold #4 runs after the cell drains, with a census of 0 gone and 0 changed outside the new bbg rows. Otherwise #4 runs without it, before 13:00Z. | msg 28084, issued 50ca06792c |
| MSTR~Z 28079: confirm that W5-S14 is closed by MX-x-4 | **CONFIRMED.** The wrapper writes through `json.dumps` while keeping the escape style, and its test passes 8 of 8. | msg |
| MSTRZ-GL-1: the gitlink hook tested a portal commit against `ajb_workspace.git` | **FIXED twice.** The first fix (2925367d6e) covered only an uninitialized submodule and missed the hook environment. MSTR~Z reopened it (28085): a commit hook exports `GIT_DIR`, which overrides `-C`. Every submodule query now runs with `GIT_*` unset. Reproduced with the leaked variable: the bare call read the wrong remote and missed `d79b9934`; the fixed call reads `portal.git` and finds it. | `2925367d6e`, `be815d264f` |

## Acts only Andrew can do

1. **PROD for the demo** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word).
   - The act: pull-merge origin portal DEV `d79b9934` into `3c37a01c`, push, and promote.
   - The CLOUD pull that MSTR~Z holds for Andrew's merge needs `be815d264f`.
2. **The ETFS_RIVALS FWD-1 signed-in read, and confirmation of Addendum B** (two answers owed).
3. **Vendor per-use words, if wanted:** the HARVST residential arm, and web search for the rivalfunds AI.

## Compiler Tools

`git ls-remote`, `git log`, `pytest` (`test_safe_ec2_deploy_manifest.py`), `bash -n`, a hook-environment reproduction with `GIT_DIR` exported, broker `send_message`/`ack_messages`.
