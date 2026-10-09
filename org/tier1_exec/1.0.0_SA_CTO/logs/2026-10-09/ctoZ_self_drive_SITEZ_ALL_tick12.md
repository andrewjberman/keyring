# `/self-drive 30m` every site-Z project -- ticks 11-12 (2026-10-09 ~12:4xZ to ~13:36Z), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md` @4752d8dfcc.
Cron `fff05062`. Previous log: `ctoZ_self_drive_SITEZ_ALL_tick10.md` @e0266a0aa4. **state: ARMED.**

## Scope

7 non-terminal SITEZ-placed projects; 2 of 9 closed. **Completion test: NOT DONE.** REACHABLE 6, UNREACHABLE 1 (NFRA_MCPMSP: G-MSPID).
**r29 is LIVE:** `NFRA_OPLGTW.TO-OG-ap-3` complete @fab015fa54 (AC1, AC2 PASS) at 13:00:53Z; its ledger was closed on `box/sitez` at 12:46Z
(@5f1400c4a2). OG-rl-15 still reads `pending` (its issuer's drain). Inbox at tick 12: 0 unread. Open calls: 1. A new unblock case
UB-20261009T133624Z-e1ca (NFRA_OPALAI) opened 13:36Z, awaiting the CRO.

## Acts and rulings

| item | ruling / act | carrier |
|---|---|---|
| UB-fafc r29 trigger | AMENDED: a worktree's ledger copy counts as open only if that branch's own commits touched it. Two worker branches cut at 12:18Z carried inherited copies (0 own commits), so the first-written union read could never fire. Trigger read TRUE at 13:1xZ. MSTR asked to apply the same test in `unblock.py --owed-ledger` | @7cca94207d |
| OPALAI arms refused `asker_message_stale` (COO~AI 32764, row Z-S70) | r29's 900s replay bound is KEPT; the arms re-fold onto FRESH messages (Andrew for arm b, Alyssa's sitting for arm a), message ids and send times recorded beside results | @4e2f00c9fa |
| dell2 FWD-6 `.pptx` generalisation of `copy_site_file_to_s3` (dell2 CTO @1e0c6f1455; COO~O 32762) | TAKE: parameterise root and filter, admit `.pptx` to the `market_update` address from `address()`; ships WITH E2 under one pair naming both admitted pairs | @4e2f00c9fa |

## Acts only Andrew can do (cited)

- **One Teams message to the Opal Bloomberg account** for arm (b), at the COO's timing (his account; ruling @4e2f00c9fa).
- **Barron's sign-in** (AMGT_HARVST). **COMM_ASSIST fallback sender** (only if nothing is texted by 19:30Z). **G-MSPID**. **Forced worktree
  removal** (HELD).

## Compiler Tools

| tool | result | note |
|---|---|---|
| `git worktree list --porcelain` + `ls-tree` per tree, then `git log <merge-base>..<branch> -- <ledger>` | PASS | the own-commits test separated 2 inherited copies from real open entries across 49 trees |
| last-`<status>`-tag read of OG-ap-3 / OG-rl-15 | PASS | the order's last tag, not the first |

-- 1.0.0_SA_CTO~Z
