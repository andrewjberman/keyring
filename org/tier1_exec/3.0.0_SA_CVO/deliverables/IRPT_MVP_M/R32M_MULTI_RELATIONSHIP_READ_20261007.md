# IRPT_BCKEND cell IB-mr-321 (E-M3, row S368) -- one true multi-relationship account, run from the laptop for 2.0.0_SA_COO~M2

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~12:3xZ, read-only, on `1.0.0_SA_CTO` msg 106211. A FILE, not a row.
Result JSON beside this file: `R32M_MULTI_RELATIONSHIP_READ.json`.

## The caution in the ask, and how it was met

The script calls the producer's own `build_snapshot("cottonwood", s3, "2026-10-05")`. Two controls:

1. **Read.** `r32m_multi_relationship_read.py` (blob 48829801c9, 169 lines) read in full: its own AWS calls are the
   imported `read_firm` (S3 `get_object`) and STS `get_caller_identity`. The producer
   `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (blob 98d4ae8218, equal at HEAD, in the tree and at
   `a533959eae`) was scanned for every write-shaped call: the S3 writes are in `land()` (line 2825 on: `write_bytes`
   2849, `publisher.publish` 2854) and `publish_client` (2874), none of them called by `build_snapshot` (2653). One
   local temp file is written at 1265-1268. The builder imports eleven other modules that were NOT read to the end.
2. **Guard, because the read was not complete.** The script ran unchanged under
   `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/run_read_only_guarded.py`, which wraps botocore's one call path
   and refuses, before any request is sent, every operation whose name does not start with Get, List, Head, Describe,
   BatchGet, Query, Scan or Select, for every client of every service in the process. Negative control run first: an
   S3 `PutObject` and a Lambda `Invoke` were both refused, and a `HeadBucket` passed.

**What the process did, counted by the guard:** dynamodb GetItem 2,026; dynamodb Scan 3; s3 GetObject 16; s3
ListObjectsV2 6; sts GetCallerIdentity 1. **Refused: none.** No put, copy, delete or invoke was attempted.

## What was run

- The script and `r30m_fwd5_replay_read.py` (blob cb2de9d266) from commit `a533959eae` by `git show`; the producer from
  the laptop tree at HEAD `5f131dfa8b` (sha256 `55a5ac985aa2...`, as the script records).
- `--self-test`: "SELF-TEST OK: 3 arms (an account in two relationships named, tied, and the 2x2 overlap printed; a
  served value that double-counts FAILs m2; no multi-relationship account reads as a stated absence)".
- Served publication compared: cottonwood 2026-10-05, revision bb51912332f6.

## Result: exit code 0 -- m1 PASS, m2 PASS, m3 PASS

- **m1.** Account `acc_0f1e215e521798954f80f291` belongs to two relationships; 3 accounts in total hold more than one
  Relationship ID.
- **m2.** That account: 58 raw custody rows collapse to 29 unique positions (29 duplicate relationship rows
  collapsed); its rebuilt subtree ties over 4 partitions, 0 unbalanced; rebuilt value 462,857.7422 equals the served
  value 462,857.7422.
- **m3.** Of 860 accounts: 1 is both multi-model and multi-relationship; 180 multi-model only; 2 multi-relationship
  only; 677 neither. The round-31 proxy (more than one model) finds 181 accounts; the case has 3; they share 1.

## Notes

- m2 was tested on one of the three multi-relationship accounts; the other two were not tied.
- The build printed "Classification not found for ticker" lines for at least eight tickers (BDCASHIN, FCASH, CQP and
  five manual or private holdings). They did not stop the build; whether they matter is the producer owner's.
- The JSON carries the two raw Relationship IDs of the named account, as the script writes them.

-- 3.0.0_SA_CVO
