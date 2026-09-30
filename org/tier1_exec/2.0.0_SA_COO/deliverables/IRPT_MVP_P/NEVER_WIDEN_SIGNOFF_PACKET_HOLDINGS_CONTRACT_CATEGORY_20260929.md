# Never-widen sign-off packet -- the HoldingsSnapshot contract's CATEGORY revision in the two served validators

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~11:3xZ.
**Asked by:** `2.0.0_SA_COO~M` 102599 (step 1 of the release order in
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md`; CTO
ruling 102475 on AD-01). **Order:** TO-IB-pr-212, drained @dc1fc92e4e (P21-2-AC1 PASS). **Ledger:**
`irpt-holdings-contract-category-20260929` (U1 closed).

## 1. What ships

The docs contract `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` at a69fe8e33e adds, additively:
- `node_kind` CATEGORY;
- a top-level `source_vendor_keys`;
- an ACCOUNT `assigned_strategy`.

Every prior enum member stays. The act stages that revision in the two functions that validate against it:

| function | live -> new | S3 version | census vs live |
|---|---|---|---|
| irpt-holdings | `kZygK57y..` -> `U4/P5Bh3..` | vN9Fiykn | 33 -> 33; ONLY `contracts/HoldingsSnapshot.schema.json` differs |
| irpt-ycharts-generate | `AdE17rT6..` -> `wnt7hjAB..` | GP__8T1n | 111 -> 111; ONLY `contracts/HoldingsSnapshot.schema.json` differs |

**One build fact the halves should know:** the first generate build from HEAD also moved `recipe.py`,
`resident_main.py` and `resident_worker.py`. These are resident-side modules that HEAD carries at newer bytes. They are
now PINNED in the source map to their LIVE blobs (03ea5980cc / 4ed7edaaa8 / bb1eb7f92b, blob-equal to the served
bytes), so this act moves the contract only.

- Cold start, live vs new, both functions (/var/task mapped): import OK, the same named envelope.
- Plans: holdings root 0/1/0 and ycharts root 0/1/0, each the Lambda's code fields only.
- The lambda-tree copy `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` is byte-equal to
  the same revision (pr-212). It is what ~M's holdings runner validates against at its re-mint, which is ~M's step 2
  and not in this act.

## 2. Blast radius -- both branches

- **Moves:** each validator ADMITS a document carrying CATEGORY nodes, `source_vendor_keys` or `assigned_strategy`.
  Today it would refuse such a document.
- **Unchanged:** every document served today still validates. WK~68 validated the latest served snapshot of all
  three firms against a69fe8e33e: 49F 151,697 nodes, COT 16,749, INF 33,328, all VALID. No served document changes
  in this act, because the served shape moves only when ~M re-mints (step 2, its own halves). No IAM, route, table or
  schedule moves.
- **Reachable:** the Holdings card and the Analysis generate path's holdings validation.

## 3. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. BEFORE: one served Holdings snapshot per firm validates under the live contract (the same read WK~68 made).
3. Fresh plans equal section 1; safe-apply the holdings root, then the ycharts root (halt gate; HALT_ACK=1 only on 0
   STOP items). The S3 latest version of each key is confirmed equal to the section-1 version before each apply.
4. Read back CodeSha256 per function; a real cold-start invoke of each; re-plan both roots: No changes.
5. AFTER: the same three snapshots validate; an unchanged Holdings card read on one firm.

**Rollback per key:** irpt-holdings -> S3 version of `kZygK57y` restored as latest, then re-apply; irpt-ycharts-generate
-> S3 version `BIEsyaNn` (`AdE17rT6`) restored as latest, then re-apply.

## What the halves sign against

This file's committed blob; dc1fc92e4e; the two artifacts of section 1; the apply protocol of section 3.
