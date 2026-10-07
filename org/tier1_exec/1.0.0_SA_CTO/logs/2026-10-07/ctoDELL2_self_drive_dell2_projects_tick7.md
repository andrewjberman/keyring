# /self-drive dell2 projects -- tick 7 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 6 (@ac6608a044), plus tick 7 (12:45Z). **state: ARMED**

## Scope state (12:45Z)

All 5 are `active` / `EXECUTING`. Inbox: 0 unread.

## Outcomes

- ADVI_COTBKF **5 of 9** (FWD-6 REALIZED this window). FWD-3's gap is sized: 2,914 of 4,634 securities and 8,091,310 of 9,388,961
  security-days. The pull is MDPF_SECHIST's, under Andrew's per-use word (PRD v0.4 ADDENDUM 2 fixed the source).
- IRPT_BCKEND FWD-5 (this project's share): 3 of 4 PROOF cases MET; the multi-relationship case is in flight (E-M3).
- IRPT_CUSTDY FWD-1: hops 1-4 run on real data; hop 5 waits on IRPT_BCKEND E-P9's release (terraform kit).
- IRPT_DASHBD FWD-8: held on Andrew's split-pull word.

## Driver acts (dell2 LOCAL)

| act | hash |
|---|---|
| IRPT_BCKEND PRD v0.30: ExportReceipt names its accounts; reads fail closed (W142-S4) | f20371eb03 |
| ADVI_COTBKF round 8 L10 | 31b26bff2d |
| IRPT_DASHBD round 21 L10, plus CORRECTION (read the etf-classifications TABLE, not the seed module) | 214a0ef324, f172f8c7b0 |
| IRPT_BCKEND round 31 M L10 | 8306f3a88b |
| ADVI_COTBKF round 9 L10, plus CORRECTION (the 49F/INF half struck as cross-firm) | 9b8dcec304, 283b15713f |
| IRPT_CUSTDY round 4 L10 | 16d9b128c0 |
| ADVI_COTBKF round 10 L10 | ec46d09305 |
| ADVI_COTBKF CB-d-4 CTO half AMENDMENT 1 | b4073b7bf2 |

## Security finding (IRPT_BCKEND W142-S4 / W146-S1)

`export/entry.py:151-152` admitted any export whose receipt named no account, and the receipt schema named none. It has been
fail-open since 2026-09-11 and is still live. Exposure cannot be proven absent: admitted reads write no log line, and part of the
window is past retention. **RULED (msg 513):** measure who can reach it now. If no principal outside Opal admin/internal/dev can,
the fix waits for the terraform kit AND opening PROD to any advisor is blocked until it ships. If any can, a laptop applies the fix
by hash as a security exception. The fix logs every admitted read.

## Self-findings

Three rulings this window were corrected by the COO lanes on their citations: the C-SILVER count (round 7), the seed module versus
the table (DASHBD round 21), and cross-firm stores (round 9). All three have one cause: ruling before reading the project's own
CONTRACTS and prior rulings. Each was corrected in the record the same tick. A memory write recording the lesson was refused by
hook (Andrew-direct 2026-09-24: seats do not write lessons to memory); the stray index line was removed.

## Laptop changes received

- Portal toolchain LIVE on dell2 (typecheck rc=0). PyMuPDF has no cp314 wheel, so those test legs run on the laptop. Terraform
  goes into the kit (accepted).
- bun auto-installs from npm. Rules 106215 and 106221: no `bun install`; bun only in a portal tree with node_modules, with
  `--no-install`. Relayed to all 7 lanes.
- 2.0.0_SA_COO~G2 disclosed one npm egress (~08:0xZ, worktree-only). RULED: file a row, re-prove on the shared node_modules, no delete.

## Acts only Andrew can do

1. The IRPT_YCDGEN F1 retry (his login).
2. One IRPT_BCKEND export (his per-use vendor word).
3. Opening PROD `/investor-reporting` to an advisor, or naming an advisor test principal. **HOLD: not before W142-S4's fix ships.**
4. The IRPT_DASHBD split BD pull: 2,299 calls (his per-use vendor word).
5. **NEW:** the ADVI_COTBKF price pulls, through MDPF_SECHIST: Yahoo for equity/ETF/fund and Bloomberg for fixed income/other,
   sized from the need FILE (his per-use vendor word). MDPF_SECHIST's issuer puts the sized ask.
6. Landing the IRPT_BCKEND print-page branches on portal DEV (laptop 106221: waits on his word).
7. Handing IRPT_CUSTDY reports to the advisor (egress), when hop 5 serves.
8. Offered: confirming IRPT_YCDGEN FWD-17 to FWD-23.

## Completion test

NOT DONE: 0 of 5 complete. 5 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- Reads only. Commits retried through MSTR's merges on `.git/MERGE_HEAD` in the background.
