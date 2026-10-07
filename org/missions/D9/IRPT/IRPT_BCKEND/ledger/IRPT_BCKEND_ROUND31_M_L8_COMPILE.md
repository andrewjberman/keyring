# IRPT_BCKEND round 31, workstream ~M -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~M2` (the issuer for L6 and L7, on dell2), **for** `3.0.0_SA_CVO` (L8 channel compile, L9 adjudication,
and the slug to the CTO), 2026-10-07 ~11:5xZ. The round is SERVED.
- Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R31_M.md`, with AMENDMENT 1.
- Issuance @6b1578f2d0, cut on the CTO round-30 M analysis @e252251fbe, item E-M2.

## Terminality

- **1 of 1** ~M round-31 orders is terminal: `IRPT_BCKEND.TO-IB-m31-311`, status complete.
- Its proof instance (`deliverables/0.9.0_WK_IRPT_BCKEND~153/...proof_of_spec.json`) was re-checked by the issuer
  before the drain: VALID, rc 0.
- Drained @5eea584574 by `.tools/safe-merge.sh`:
  - 3 paths needed, 0 dropped, 0 foreign;
  - the index check shows 0 of 3 differ;
  - the worktree and both branches are removed.

## The cell and the real runs

**IB-mr-311 (FWD-5's four PROOF cases, 2026-10-05 served publication).** Two reads, each pinned by commit and sha256:

| read | file | run by | scope |
|---|---|---|---|
| CASES | `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R31M_FWD5_PROOF_CASES_READ.json` @471da6f0b0, sha256 `2b61c5a833c7...` | laptop `3.0.0_SA_CVO`, identity Andrew_Berman | 3 of 3 firms |
| RECHECK | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31M_UNASSIGNED_RECHECK_20261007.json` @6458a5a9d3, sha256 `9eb9cff78f77...` | dell2, `cloudops-dell2-agent-user`, `--date 2026-10-05` | the unassigned case, 49F and INF (COT lists 0) |

| criterion | the issuer's re-run at dell2 HEAD after the drain |
|---|---|
| IBM31-311-AC1 | `E1-CASES-NAMED`. 4 of 4 cases found: unassigned (49F, 1,876 instances), unmatched join (49F; 3 firms), blended model (COT acc_000c147a49a4d234b37dab66, 366), multi-relationship membership (49F acc_1c312e69da7efca76d0f17d3, 1,487) |
| IBM31-311-AC2 | `E2-CASES-RECONCILE`. Unassigned: 1,876 of 1,876 pass over every instance (49F 1,645 incl. 888 zero-value; INF 231 incl. 56 zero-value): served as an ACCOUNT, subtree ties, no model node beneath. Unmatched join: 49F reconciles on all three arms, with a visible remainder of 168,525,497.37 USD ("1645 of 7597 custody account(s) carried in Client with membership unattributed"). Blended and multi-membership instances tie. |
| IBM31-311-AC3 | `E3-COVERAGE-DENOMINATED`. 49F 5,952 resolved of 7,597 attempted, 19 assigned without custody. INF 627 of 858, 35. COT 475 of 860, 0. |

**Difference control:** AC2 with a wrong pinned RECHECK hash prints `NOT-E2-CASES-RECONCILE`.

**Not graded on the CASES file's own e2:** it tested one zero-value account against a rule the L0 category shape makes
impossible (row S366). AMENDMENT 1 is the issuer's ruling on that.

**No judgment criteria.** All three are mechanical.

**One limit stated for L9:** the multi-relationship case is defined on the served data as an account whose subtree
references more than one MODEL. The producer's relationship-collapse evidence sits in its private `_manifest`, which
is not served.

## Rows

| row | what it records |
|---|---|
| S363 | BLOCKING, the fenced read; disarmed by S367. |
| S366 | the e2 instrument defect and the issuer's re-check. |
| S367 | the disarm. |

Worker rows: none. Armed rows owned by ~M with no seated owner: none.
