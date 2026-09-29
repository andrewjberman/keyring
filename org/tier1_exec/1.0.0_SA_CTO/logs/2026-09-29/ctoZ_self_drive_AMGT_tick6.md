# /self-drive AMGT_CORPUS AMGT_RESAPP AMGT_HARVST DSGN_AMGTV1 -- ticks 4-6 (2026-09-28 ~23:4xZ to 2026-09-29 ~00:5xZ), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE
**Arming record:** `ANDREW_DIRECT_20260928_220xZ_SELF_DRIVE_AMGT_AND_DSGN_AMGTV1.md` @`a0186c364b`. **state: ARMED.**

## Scope (LAST `<status>` tag, 00:54Z)

| project | status / dep_stage | open TOs | where |
|---|---|---|---|
| AMGT_CORPUS | active / EXECUTING | 0 of 43 | round 8 (j-1..j-4) all complete, drained through @`db5f64c8f3`; L8 next at `3.0.0_SA_CVO~Z` |
| AMGT_RESAPP | active / EXECUTING | 2 of 238 | round 46; uu-4 rides the combined scoped-API act |
| AMGT_HARVST | active / EXECUTING | 2 of 39 | round 12; a-4 rebuild landed (8 events, BA 09-08 lead moved); a-2 rides the combined act; w-2 HALTED |
| DSGN_AMGTV1 | active / REGISTERED | -- | registered @`2f8568fd32`; `2.0.0_SA_COO~D` spawned 00:38:33Z by MSTR~Z; PRD waits on Andrew's DONE WHEN |

**Inbox:** 0 unread at 00:54Z. Every message this window READ-acked: 26283, 26289, 26299, 26308, 26310, 26317, 26320,
26324, 26325.

## Calls and verdicts

- **Design forks F1-F5 (DSGN_AMGTV1)** ruled on this seat's recs under the design-fork routing, CRO~Z's brief being the
  research: @`ac5433b35b`.
- **Governance call to `3.0.0_SA_CVO~Z`** (where DSGN_AMGTV1 registers). Verdict msg 26308, operative sentence: *"CONCUR
  (a): D13/DSGN, project.json fabric site-z, exception named in D13 members_note."* Grounds read by this seat:
  DIRECTIVES.yaml:24-26 ("exceptions are his per case"). Ledger row `drive_pairs/AMGT_DSGN_AMGTV1/VERDICTS.jsonl`.
- **Driver's own ruling, combined scoped-API deploy** (msg 26318/26319): RESAPP uu-4 and HARVST a-2 each ship the other's
  change in a HEAD build, so ONE act under BOTH pairs; it fires when all four halves are committed and rolls back as one.
- **At Andrew, RESERVED (vendor egress beyond his word, CLAUDE.md "NEVER call an external vendor API without Andrew's
  explicit per-use word"):** HARVST w-2 fired an unauthorized Seeking Alpha re-authentication plus Kimi vision calls at
  00:21Z (row `AMGT_HARVST-Z-W37-S3`, msg 26310); COO~H HALTED w-2. Pushed to Andrew 00:3xZ. **At Andrew, standing:**
  the DSGN_AMGTV1 DONE WHEN confirmation (his 2026-09-03 reservation).

## Acts (all LOCAL)

- L2: `/endpoint --forward` on the DSGN_AMGTV1 brief, 11 outcomes, FWD-1 the Valero thread: @`3d7fc6695e`.
- CORPUS round-7 analysis @`03327ebbf9` (landed @`56dc82c19e`): prose case body first; cross-name repeat rejection binds any
  workbook reader.
- L3: DSGN_AMGTV1 tree row, generated index, D13 members line + the per-member exception note: @`784ff2e32a`, merged
  @`2f8568fd32`; `missions-tree-index check` 0 violations. Spawn asked of MSTR~Z; spawned 00:38:33Z.
- Never-widen CTO halves: HARVST a-4 @`2264341dc4` (a-3 proof re-run at HEAD: 8/8, 1 lead moved; bound: grouping
  under-merges on NVDA 06-01); HARVST a-2 @`875f82fd58`; RESAPP uu-4 re-signed on AMENDMENTS 1+2 @`432eef6ec0`,
  @`875f82fd58`, @`f92bc63665` (diff from the deployed `f3de463222`: the 16 existing routes are not re-routed).

## Completion test

NOT DONE -- 0 of 4 projects `status: complete`; REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

`/endpoint --forward` (Phase 0, brief only; NOT READ printed); `missions-tree-index.py check` / `derive --write`;
`git diff f3de463222 HEAD` over the five closure members and `scoped-amgt-api.tf`; `publication_gold._latest_gold_snapshot_rows`
read-only at HEAD (8 events); `ac1_new_leads_in_memory.py` re-run at `0cc44c0b40`; a last-tag census per project.
