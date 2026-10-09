# IRPT_BCKEND -- round 35 ~M L8 packet (2.0.0_SA_COO~M2, 2026-10-09 ~02:5xZ)

**Cut on:** `2.0.0_SA_COO~Y2` msg 2202 (release-6 blocker: `irpt-ycharts-generate` packages `ycharts/extract/publication.py`, so the
round-34 port in `holdings/snapshot.py`, which imports `publication`, collides). Decomposition `decompositions/IRPT_BCKEND_DECOMP_R35_M.md`;
issuance @5f32410b6e; drained @49cecd310d (box/dell2, LOCAL).

| order | worker | status | criteria (issuer re-grade on the worker branch, then AC1 again on the drained tree) |
|---|---|---|---|
| TO-IB-m35-351 | 0.9.0_WK_IRPT_BCKEND~202 | complete | IBM35-351-AC1 PASS, IBM35-351-AC2 PASS (holdings 182, _scope 234 + 67 subtests), IBM35-G-202 PASS; proof VALID |

**Product change:** new `infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py` (+21): imports `holdings_publication`
(the name `~Y2` stages holdings/publication.py under) and falls back to `publication`; `holdings_publication_for(s3_client=None)`, same
signature and read set as round 34, boto3 client built lazily. `snapshot.holdings_publication_for` removed (-9, no consumers);
`tests/test_publication_port.py` repointed. No other function changed.

**The one real run (issuer):** AC1 on the drained tree -- in a fresh isolated interpreter staged as `irpt-ycharts-generate` stages it
(the port, holdings/publication.py as holdings_publication.py, ycharts' publication.py and its siblings, lib/), the port imports,
binds `holdings_publication.HoldingsPublication` in the production namespace, makes no S3 call at construction, and refuses ALL.
Nothing deployed: `~Y2` stages it in release 6.

**Judgment criteria:** 0. **Rows:** 0 filed. **S3 read set:** unchanged (round-34 packet @36b0cbb93f).
