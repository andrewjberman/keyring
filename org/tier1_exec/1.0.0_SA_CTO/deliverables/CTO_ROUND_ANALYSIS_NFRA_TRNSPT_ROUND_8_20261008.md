# NFRA_TRNSPT -- ROUND ANALYSIS, round 8

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~20:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1544) and ADJUDICATION_v6 @5cc74b5157. MAY-CLOSE, 0 rows undispositioned, ARMED 0.

## 1. State

- **E1:** the `ENCRYPTED_UNVERIFIED` revert is verified byte-equal to 8394179dec, and the bundle imports. Internal encrypted mail does not
  land. The proof pins 603cbf62e4 by content.
- **E2 (FWD-5's first slice):**
  - 29 of 29 Research transcripts gave 20,473 rows, with 0 failures.
  - Speaker is kept and text is wiped: 14,153 name hits; 2,716 rows carry a residual flag.
  - The rows are held locally.
  - One transcript reads back as 207 speaker turns.

## 2. Ruling -- where the rows live (PRD :154), and the residual rows

- **Home: `opal-data-transcripts`, silver tier** (C-BUCKET, C-TIERS), the project's one store. The key comes from
  `lib/opal_naming.py address()`, never hand-typed (CLAUDE.md rule 30). A builder refusal means a missing registry row, which the cell
  adds.
- **The 2,716 residual-flag rows are held out,** exactly as mail silver does: they are stored with `held_out=true` and never reach gold
  or any reader of the wiped copy. This is the CVO's recommendation.

## 3. ENRICHMENT -- round 9, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Land the 20,473 Research rows in transcripts silver** at the builder's address | (1) the address printed from `address()` (or the registry row added, then the address); (2) read-back from S3: 20,473 rows, of which 2,716 are `held_out` and 17,757 are not; (3) the planted-token wipe test passes on the stored bytes, not the local copy | SERVED (a new silver partition in the project's own bucket, which no consumer reads yet) |

The write sits under FWD-8's reader set: the bucket's existing key and policy, with no new principal.

-- 1.0.0_SA_CTO~DELL2
