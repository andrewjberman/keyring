# IRPT_BCKEND -- round 34 ~M L8 packet (2.0.0_SA_COO~M2, 2026-10-09 ~02:2xZ)

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 2127 (release 6, port 2). Decomposition `decompositions/IRPT_BCKEND_DECOMP_R34_M.md`; issuance
@76dae59dce; drained @772cc0a4d2 (box/dell2, LOCAL).

| order | worker | status | criteria (issuer re-grade on the worker branch, then AC1 again on the drained tree) |
|---|---|---|---|
| TO-IB-m34-341 | 0.9.0_WK_IRPT_BCKEND~201 | complete | IBM34-341-AC1 PASS, IBM34-341-AC2 PASS (holdings 182, _scope 223 + 67 subtests), IBM34-G-201 PASS; proof VALID |

**Product change:** `infra/aws/lambda/investor-reporting/holdings/snapshot.py` +9 -- `holdings_publication_for(s3_client=None)` returns
`publication_for(firm_id) -> _publication_reader(firm_id, DEFAULT_PREFIX, s3_client)`; plus `holdings/tests/test_publication_port.py`
(+42). No existing function changed.

**The one real run (issuer):** AC1 on the drained tree -- the factory fences 3 of 3 canonical firms in the production namespace with no
S3 call at construction, refuses 5 of 5 bad firms ("ALL", "", None, 7, unknown), and a capture -> load_pinned round trip over the
in-memory versioned S3 meets the reader's shape rules with an equal pinned reload. Nothing deployed: the port ships in `~Y2`'s release 6.

**Judgment criteria:** 0. **Rows:** 0 filed.

**Worker note:** AC2 failed on the worker's first run -- its own new test matched `PublicationRefused` by class identity, and another
suite in the same pytest session loads a second `publication` module object; fixed in its own test (47f9c3b27a) to match by name.
Existing tests untouched.

**S3 read set of the port** (code read, for the release-6 pair's grant): buckets `opal-data-<firm>` (49financial, cottonwood,
inflection; from the address builder, product irpt, table holdings); keys under `irpt/<firm>/platinum/holdings/`:
`current/manifest.json` (capture reads current; load_pinned reads the receipt's pinned VersionId), `date=YYYY-MM-DD/<rev>.manifest.json`,
`<rev>.json` (v1 body), `<rev>.header.json` and `<rev>.part%05d.json` (v2), each with VersionId; actions `s3:GetObject` and
`s3:GetObjectVersion`; no List, no Put.
