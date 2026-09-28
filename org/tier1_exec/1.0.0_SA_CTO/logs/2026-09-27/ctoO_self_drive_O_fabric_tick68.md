# /self-drive ~O fabric -- ticks 66-68 (13:05Z-13:5xZ), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** the first acts this seat takes as OPLGTW's CTO -- a ruling, a contract amendment and a PRD version.

## C6 (MCPORTAL): both gates hold (@0aaf865219)

G-OPLGTW (Andrew, 09-26) and the OPLGTW re-seat (@6fba157e76) are both met. C6 is still cut at MCPORTAL's L10, because the
spec is frozen mid-round.

## R2-k (OPLGTW's email-keyed deny cell for row W3-S22): five calls RULED @2ae58221ab

`2.0.0_SA_COO~O`'s design @500aac7e4d executes the 09-15 ruling 97251. Rulings:
- (1) revoke KEEPS the deny record; a lift is a later, separate act;
- (2) the 5 routes FAIL CLOSED (503) on an unreadable table, matching C2 and the MCP path;
- (3) one deny record per email alias, AND the post-validation check in `redeem_consent` stays;
- (4) the release base is live `110d93fb73` + this change only (TX-g-1 stays out);
- (5) this seat AMENDED `NFRA_OPLGTW_CONTRACT.json` 1.2 -> **1.3** (`email_deny` in `record_types`; the POLICY namespace
  names it) and the PRD v0.9 -> **v1.0** (one clause each in C2 and C6; header `fabric` site-z).

`prd-signoff status` reads both halves SIGNED and current at @2ae58221ab. That is BY DESIGN, not a defect: since v3.19 both
halves bind to the ENDPOINT hash alone (`prd_signoff_lib.py:117-118`), so a CONTRACTS edit re-opens nothing. CVO~O is asked
for a review anyway (file same tick).

**One served step waits on Andrew:** `deny-backfill` for Alyssa Keith (SERVED step 2) adds denial to her. His open card asks
whether her portal-only grant should restrict her own access at all. Steps 0 (build), 1 (narrow release) and 3 (the
grant-writer Lambda) go ahead; step 3 before any dashboard grant.

## Calls at Andrew

One card: should Alyssa's portal-only grant also remove her own gateway tools (REC (a) keep as is). It now also decides
R2-k's SERVED step 2.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE. Open orders: MX-s-4, MX-s-6 (MCPINDEX); OA-t-1, OA-t-3 (OPALAI);
OPLGTW OG-v-4 and OG-v-5 held behind R2-k (their assignee, laptop worker ~6, is unreachable).

state: ARMED

## Compiler Tools

`prd-signoff.py status`; a read of `prd_signoff_lib.py`'s half binding.
