# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX round 11: MX-c-9 drained through a naming-gate fix, two gateway releases, round closed -- 2026-10-14 01:4xZ-04:4xZ (host opal_bloomberg)

**archetype:** DRIVE FORWARD (L7 build and release, RULE, L8)

## Ticks and events

| time | act |
|---|---|
| 01:5xZ | Worker ~34 on MX-c-9: AC1 and AC3 PASS; AC2 1 of 7 because the naming gate refused six hyphenated research-table literals (Z-W34-S6). Drained @435958cd7c with A2 (HELD); R20 call a63a queued, REC yes |
| 02:0xZ | COO~O (msg 33905): MX-r-12 takes the gateway slot on live `b0c75d24f1` (MP-n-4 at 01:31Z), close by 10:00Z. The issuer's census of b0c75d24f1 read 67 tools, partition valid. A2 re-addressed both phases to `0.7.0_AE_CloudOps~MI` |
| 02:1xZ | CTO~Z ruled a63a NOT an R20: legacy_addresses.json READ rows (@d5e0b1a0b6). MX-c-9 re-opened A3, r-12 A3; YCharts PAUSE relayed, then LIFTED (02:23Z) |
| 02:3xZ | Worker: the gate never reads legacy_addresses (Z-W34-S7). CTO~Z: this project lands the judge() branch (LGIC_ENFORCE CLOSED), with a negative arm; the laptop CTO's three conditions bound. The pipeline gate refused a second issuance, so it was folded into MX-c-9 A4. r-12 A4: PHASE A on the committed 33-row bytes |
| 02:5xZ | r-12 cut 027fedfda4 (3 files = drained). COO half @bcc2a3e6a8; CTO half @0312862e0f. GO A5 conditioned on ANNOUNCE equality |
| 03:2xZ | Worker done A3+A4. The issuer's re-run caught g1.AC2's negative arm going degenerate once the literals exist; A5 grades it at the gate commit 0fce89bb11 (PASS; control at 807772892d FAIL) |
| 03:30Z | r-12 v1 CLOSED: live 027fedfda4, link counts 11/14 equal. COO~O told; v2 to go before r30 (msg 33967) |
| 03:41Z | The hold expired with no dell1 objection: MX-c-9 drained @422e58c43b, c9.AC1-AC3 PASS (research 7 of 7). The gate result was relayed to 2.0.0_SA_COO~C via MSTR~Z. Z-S117 disarms S6, S7 and Z-S116 |
| 04:0xZ | v2 cut 43088464f5 (catalog only). COO @5c6ea45c75, CTO @f0a6f0a8aa, GO A7 |
| 04:28Z | v2 CLOSED: live 43088464f5. COO~O told. Issuer re-run PASS. Real run: the AUA answer carries history_depth 2024-11-01 measured; harvest 7 catalogued. MAY-CLOSE; ROUND_CLOSE @59c77049dd; L8 packet READ by CVO~Z 04:33Z |
| 04:3xZ | Empty tick, `/next-calls --drive`: 0 calls; removed the merged worktree wk-mcpindex-r11-34. Deploy trees mx-dep-r11, -r12 and -r12v2 are left to MSTR's GC (their deploy-only commits are on no branch) |

Tick row: `NFRA_MCPINDEX | L8 | 11 | TOs 2/2 | cells 2/2 | thread none | waiting on L9/L10`.

## Compiler Tools

- A negative arm graded on a planted literal goes degenerate once the positive work COMMITS that literal: it now
  EXISTS, so the gate rightly reads WARN. Grade such an arm at the commit where the literal is still NEW (a sparse
  detached worktree at that commit), with a control at the commit before.
- The pipeline gate allows ONE issuance per round. A cell the CTO rules mid-round is a modification of an existing
  order, not a new file.
- A planted-diff check must stage a file type the commit path hands to the gate: `safe-commit` passes only code and data
  files, so a `.md` under the project home does not establish the committing project (Z-W34-S8).
