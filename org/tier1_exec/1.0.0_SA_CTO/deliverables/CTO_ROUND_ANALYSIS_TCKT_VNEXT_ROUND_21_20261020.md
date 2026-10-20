# CTO round-N analysis: TCKT_VNEXT round 21 (2026-10-20 ~16:2xZ, 1.0.0_SA_CTO~DELL2)

**Answers:** the L10 slug from `3.0.0_SA_CVO~DELL2` (msg 16:04Z), ADJUDICATION_v18 @baafaf8ebf.
- R21RB1-AC2J is MET.
- Round 21 reads MAY-CLOSE.
- Its two notes are answered below.

## Grades read (not re-derived)

- TO-R21-RB1, `0.7.0_AE_CloudOps~TV2`, RUN-OK at 15:45-15:48Z (record
  `org/tier2_senior/0.7.0_AE_CloudOps~TV2/logs/2026-10-20/r21_rb1b_trade_readback.md`):
  - a synthetic Trade Request on https://opalinvest.dev: door 200, PUT 200, ticket 201, Open 200;
  - the uploaded sha256 equals the read-back;
  - the ticket and its row read ABSENT afterwards.
- The CVO fetched the stored object at its VersionId and found the same sha256.

## Note 1: Trade is FWD-10, and the status of its DEV leg

**FWD-10:** "on DEV, then PROD by 2026-10-24".
- There was no separate DEV-leg run.
- Read here at 16:2xZ: `git diff --name-only origin/PROD origin/DEV -- src/pages/TicketCenter` lists 12 files, all of the
  Analysis Request walk set (rows 4664 and 37f6). None of them is a Trade file, so the Trade page code is the same on DEV and
  PROD.
- DEV's `/api` proxies to the same CloudFront, ticket service and trade-form prefix as PROD (TV2 msg 11051, `vite.config.ts`
  lines 64 to 104).
- A DEV-leg run would therefore exercise the same page code against the same backend, with one more residue object.

**Ruling:**
- The DEV leg is satisfied by identity and is not run.
- FWD-10's grade rests on the PROD leg (RB1) together with the round-18 to round-20 PROD filings.
- The grade itself is the CVO's (L9). This seat states the DEV-leg fact, and records that the round-20 analysis named the
  read-back without naming FWD-10 (its omission).

## Note 2: the residue delete

- Andrew's standing word of 2026-10-16 ("you can delete synthetic and test files any time") covers the four trade-form
  objects.
- Row 6e7c is closed on it. `2.0.0_SA_COO~V2` deletes them by key and VersionId, with a read-back showing ABSENT, through a
  principal that holds DeleteObject. If none does, a one-key-list grant goes under a never-widen pair (msg 11428).

## Enrichment list for round 22

1. **The four residue objects:** delete and read back (owner `~V2`).
2. **D2-S53:** the outside-domain users row with all-firm access, on Andrew's word only (row a331). Nothing is cut before it.

No other enrichment. Andrew opening a real Trade attachment stays the organic arm.

## Close state

- Round 21: CLOSED.
- TCKT_VNEXT closes when the CVO grades FWD-10 REALIZED and the round-22 items are dispositioned.

-- 1.0.0_SA_CTO~DELL2
