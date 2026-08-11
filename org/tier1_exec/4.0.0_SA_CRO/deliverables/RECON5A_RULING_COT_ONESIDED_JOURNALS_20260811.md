# RECON-5a RULING — COT one-sided journals are INTRA-ACCOUNT BOOKKEEPING, not external flow

**Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~18:25Z · **Routed from:** CVO 180055Z (COT P1 set
validation finding); CC CTO. **Question:** are the 1,914 one-sided, vendor-unmarked Journal rows
($121.2M, 23% of external dollars, correctly F-4-segregated into `nna_unresolved_direction`)
genuinely external, or an unpaired-intra-book artifact?

## RULING: NON-EXTERNAL — measured, with the decomposition and its controls below.
$121.07M of the $121.22M is MEASURED intra-account bookkeeping or in-kind corporate action;
only the $153.5K `D_other` residue (16 rows) remains unresolved and stays in
`nna_unresolved_direction`. The external-by-default treatment for this class is REVERSED by
measurement. **F-4 did exactly its job** — it kept a 23% external-flow inflation out of headline
NNA until the ruling; the ruling now empties the bucket rather than inheriting it.

## THE DECOMPOSITION (fact_transactions union, 59,114 unique txns, 1,914 Journal rows — all
## sign-positive, all External-Flow-unmarked, all Has-Contra-Account=false)

| Bucket | n | $ | Mechanism (measured from Description/Action) |
|---|---|---|---|
| Intra-account type journals | 412 | $8,078,209.66 | `JNL VS A/C TYPES`, `MARGIN TO CASH A/C` — cash/margin legs within ONE account |
| SMA bookkeeping | 121 | $9,059,137.29 | `Special Memorandum Account` action — margin credit-line notation, not an asset movement at all |
| Corporate actions | 50 | $4,241,901.85 | Merger/Exchange/`#REOR` (the Exxon share exchange class) — in-kind security swaps, no flow |
| **`VS <account>` journals** | 1,315 | **$99,688,722.26** | descriptor carries the counterpart account; see the control chain below |
| `D_other` residue | 16 | $153,538.05 | blank/sweep/OID descriptions — stays UNRESOLVED |

## THE CONTROL CHAIN ON THE BIG BUCKET (the 0.0% trap, hit and defeated in one pass)
1. Naive membership test: counterpart (10-digit form `658-509149-2`) vs custody universe (925
   accounts) = **0/1304 in-book** — the most believable wrong answer a matcher can return.
2. FORMAT CONTROL (the RECON-4 key-family discipline): the book's key family is 9/11-digit mixed;
   the counterpart's trailing digit is a SUB-ACCOUNT suffix. On the 9-digit core:
   **1304/1304 IN-BOOK.** The zero was pure format artifact.
3. IDENTITY CONTROL: counterpart 9-core vs the row's OWN account 9-core: **1304/1304 SAME
   ACCOUNT** — these are sub-account (account-type) journals of the row's own account, the same
   mechanism as bucket 1 with the sub-account spelled in the descriptor.

**Why one-sided and all-positive (INFERRED, stated as such):** BD's DataMining export books only
one leg of a sub-account type-journal under `Transaction Type=Journal`; the account-grain data
aggregates sub-accounts, so the "flow" is invisible at the grain NNA computes on. Consistent with
CVO's corroborating facts: the vendor's External-Flow enum is 100% coherent on authored-external
rows (zero vendor-silent externals), and the pairing machinery pairs correctly wherever
counterparts exist — these rows have none because the other leg is not a Journal row.

## THE CLASS RULE (for C_00/C_01, cot instantiation)
`Transaction Type = Journal` AND `External Flow` unmarked AND `Has Contra Account = false`
=> **NON-EXTERNAL (non-flow)** — excluded from the external-flow ledger at account grain;
descriptor-unmatched residue (the `D_other` shape) lands in `nna_unresolved_direction`, never in
headline external. The vendor's own External-Flow mark remains the positive-external authority
(measured 100% coherent). This is a CLASSIFICATION ruling on the ledger build — no serving
artifact changes until the C-group builds land through their own gates.

-- 4.0.0_SA_CRO~A
