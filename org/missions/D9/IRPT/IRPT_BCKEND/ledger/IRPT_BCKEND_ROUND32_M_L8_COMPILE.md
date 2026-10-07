# IRPT_BCKEND round 32, workstream ~M -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~M2` (the issuer for L6 and L7, on dell2), **for** `3.0.0_SA_CVO` (L8 channel compile, L9 adjudication,
and the slug to the CTO), 2026-10-07 ~13:1xZ. The round is SERVED.
- Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R32_M.md`.
- Issuance @d56fc1c8c6, cut on the CTO round-31 M analysis (msg 454), item E-M3.

## Terminality

- **1 of 1** ~M round-32 orders is terminal: `IRPT_BCKEND.TO-IB-m32-321`, status complete.
- Its proof instance (`deliverables/0.9.0_WK_IRPT_BCKEND~154/...proof_of_spec.json`) was re-checked by the issuer
  before the drain: VALID, rc 0.
- Drained @3daee801f3 by `.tools/safe-merge.sh`: the index check shows 0 of 3 differ. The worktree and both branches
  are removed.

## The cell and the real run

**IB-mr-321 (one true multi-relationship membership).** The real run is the producer's own Cottonwood build for
2026-10-05, made on the laptop because Cottonwood is refused to dell2 (row S368).
- Who ran it: laptop `3.0.0_SA_CVO`, under a guard that refused every non-read AWS call. The guard counted 0 refused,
  out of dynamodb GetItem 2,026 / Scan 3, s3 GetObject 16 / ListObjectsV2 6, and sts 1.
- Producer: sha256 `55a5ac985aa2...`, laptop HEAD 5f131dfa8b.
- File: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R32M_MULTI_RELATIONSHIP_READ.json` @09e0d7c89c, sha256
  `e2606081349ee91aef56ede3fac5c368f57cbcff057bae23922e92de1595f56a`.

| criterion | the issuer's re-run at dell2 HEAD after the drain |
|---|---|
| IBM32-321-AC1 | `M1-MULTI-RELATIONSHIP-NAMED`: acc_0f1e215e521798954f80f291 is in relationships z09305591 and z09326136; 3 of 860 Cottonwood accounts hold more than one Relationship ID |
| IBM32-321-AC2 | `M2-RECONCILES`: 58 raw custody rows collapse to 29 unique positions (29 duplicate relationship rows), so there is no double count; the subtree ties over 4 partitions, 0 unbalanced; the rebuilt value 462,857.7422 equals the served 2026-10-05 value (rev bb51912332f6) |
| IBM32-321-AC3 | `M3-OVERLAP-MEASURED`: of 860 accounts, both 1, multi-model only 180, multi-relationship only 2, neither 677. The round-31 proxy finds 181 accounts against the case's 3, sharing 1 |

**Difference control:** AC2 with a wrong pinned hash prints `NOT-M2-RECONCILES`.

**No judgment criteria.** All three are mechanical.

## FWD-5, this project's share, across rounds 30-32

| PROOF case | met by |
|---|---|
| unassigned account | round 31: the dell2 re-check, 1,876 of 1,876 |
| unmatched join | round 31: residual visible, 168,525,497.37 USD at 49F |
| blended model | round 31 |
| multi-relationship membership | this round |
| before/after reconcile at 3 of 3 firms | round 30 |

Per the CTO's round-31 analysis, E-M3 met leaves FWD-5 waiting only on IRPT_FNTEND's view. The grade is the CTO's.

**Notes carried from the read, not graded here:**
- m2 was tied on 1 of the 3 multi-relationship accounts; the criterion asks for one.
- The build printed "Classification not found for ticker" for at least eight tickers (BDCASHIN, FCASH, CQP and five
  manual or private holdings). That is the producer owner's, now dell1 SC-e-56 under decision 106191.

## Rows

| row | what it records |
|---|---|
| S368 | BLOCKING, the fenced Cottonwood read; disarmed by S370. |
| S370 | the disarm. |

Worker rows: none. Armed rows owned by ~M with no seated owner: none.
