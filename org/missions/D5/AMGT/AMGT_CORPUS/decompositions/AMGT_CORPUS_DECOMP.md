# AMGT_CORPUS -- L5 decomposition v45.0 -- ROUND 45 (the round-44 analysis's enrichment list: FWD-1 ingest, FWD-12 and FWD-20 rendered reads, FWD-11, FWD-14, the graded reads)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-11 ~09:3xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-44 analysis `ledger/ROUND_ANALYSIS.round44.md` @599a7cee43 (msg 3693), over
`3.0.0_SA_CVO` ADJUDICATION_v56 @1eec531da8 (MAY-CLOSE; D1-W1-S6 dismissed). REALIZED 13 of 22; FWD-12 served at the dossier with the
rendered read owed; FWD-1 MEASURED short (store 356 objects, drive 378 files). PRD v0.9, no ENDPOINT change. Round 44's decomposition
kept as `AMGT_CORPUS_DECOMP.round44.md`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | FWD-1: ingest the resolved-folder files the store lacks, then account for the drive: census files F = files in resolved folders R + files in named unresolved folders K, objects = R, mismatch 0, the unresolved files named with reasons | `CRPS-au-1` | site-Z order to `0.7.0_AE_CloudOps~ZC` under a crossbox file (round 40's ap10u precedent), under the never-widen pair `NEVER_WIDEN_ROUND45_AU1_BRONZE_INGEST.md` (COO half signed; CTO half owed) | WORLD |
| 2 | FWD-14: the four-count line, read fresh at site Z in the same order as item 1 | `CRPS-au-2` | the same order, `fence14 ... sum S folders_read S` before and after | WORLD (rides au-1's order) |
| 3 | FWD-12, the rendered read: the ap-9 row compare on the RENDERED Model tab over every served name, the page's rows equal `model.team_sheet.rows`, denominator printed, the three-class census sums to the served names | `CRPS-au-3` | the issuer's walk of the DEV build (`/ui-walk`, the dormant walker account, local dev build on 5174) against the live function at /11 `l8egBo` | LOCAL (read) |
| 4 | FWD-20, read from the rendered page after au-3: shown / refused / absent / unmapped with unmapped 0, every absent row worded for a PM | `CRPS-au-4` | the issuer's read of the same walk (depends on au-3) | LOCAL (read) |
| 5 | FWD-11: name-by-name officer comparison on SAP GY and BABA US against the persisted filing roster | `CRPS-au-5` | the issuer's read (served `read_management` against the roster, by content) | LOCAL (read) |
| 6 | the graded reads to L9: FWD-10, 15, 16, 18, 21 from `ROUND44_GRADED_READS_PACKET.md`, refreshed with au-7 and au-8 | `CRPS-au-6` | the issuer's packet to `3.0.0_SA_CVO` (depends on au-7, au-8) | -- |
| 7 | FWD-10's missing read: IMB LN's Thesis tab walked, one pillar opened to its passage | `CRPS-au-7` | the issuer's walk, same session as au-3 | LOCAL (read) |
| 8 | FWD-16's missing read: the fwd16 census line on the written /10, and on the served /11 beside it | `CRPS-au-8` | the issuer's re-run of `checks/round44` census over the stored dossiers (S3 reads) | LOCAL (read) |

**Chains:** `au-1 + au-2` (one order); `au-3 -> au-4`; `au-5`; `au-7`, `au-8` `-> au-6`.
`fanout: 0 of 1 worker chains (issuer acts only; one site-Z executor order), cap 8`.

## 1. Two measured facts the analysis did not carry (issuer's rulings inside this decomposition)

- **The at-2 portal build is already on DEV.** `26f621d5` (CRPS-at-2 amendment 1) is an ancestor of live `origin/DEV` `ff418947`
  (fetched 2026-10-11 ~09:2xZ). The analysis's "lands on DEV, candidate to the CTO first" has no act left: the owed act is au-3's
  rendered read. No portal candidate is cut this round.
- **`ingest --write` stores only RESOLVED-folder files** (`lib/research/corpus/ingest.py:124-132`: unresolved and ambiguous folders and
  loose root files are printed with a reason, never stored, no key guessed). The fence14 line read 6 unresolved-with-reason folders of
  102. So "objects = the drive's 378" can hold only if K = 0. au-1 prints all three numbers (F, R, K) and the identity F = R + K; the PRD's
  DONE WHEN ("for every file the library's own folder list resolves to ... objects equals files scanned") reads on R. The CTO/CVO grade
  with K beside it; the 22 split is measured by the order's `--write` output, not assumed.

## 2. The cells (every check dry-run at the base before the cut)

**CRPS-au-1 / au-2** `checks/round45/au1_accounting.py <evidence>` and two greps on the order's evidence file.
Base (the round-44 at-4 evidence, no write section): AC1 grep 0 (expect 1) FAIL; AC2 `NOT-DERIVABLE missing write,unresolved` FAIL;
AC3 grep 1 (expect 2, before and after) FAIL. Green arm: `--selftest` prints `identity OK` then `identity BROKEN` on the mutant.
**CRPS-au-3 .. au-8** issuer reads; their instruments are named in the packet that carries each read.

## 3. Not in round 45: the six unresolved folders' identities (a `crosswalk/v1` matter); vocabulary growth (ruling F); anything that
changes the 13:00Z fire's call, field list or address; the PROD promote of the portal (the push law).
