# IRPT_ANLREQ -- decomposition, round 19 RESIDENT LEG round 2, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-19 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 4 (@1cda6cc12a): before any pair is written, (1) prove whether a resident release REPLACES or OVERLAYS the package (116 live members the builder does not produce); (2) the reads: `2.0.0_SA_COO~Y2` reads its own three members and IRPT_YCDGEN's one, `2.0.0_SA_COO~P2` reads IRPT_BCKEND's eight, `2.0.0_SA_COO~D2` reads DSGN_IRPTV1's one; (3) the cross-box members (ADVI_FIRMBKTS 3, NFRA_CTLPLN 1) are shown EQUAL to a version their owner already released, or go to their owner through MSTR before the pair is signed.

**Why its own round:** workstream `YR` round 1 holds the delta cell (`AR-y-195`, drained @f1c4389a54); this round holds the three reads that ruling asks for, each a cell of one chain.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-196` | the install semantics read from the installer(s) with a SCRATCH install proof (live-shaped package + the new tarball, member lists before and after, denominators printed): OVERLAY, REPLACE or NEW_ROOT_COPY | the worker's deliverables | LOCAL (scratch folders outside the tree; nothing installed on a host) |
| `AR-y-197` | the issuer's four members read: `_authz/served.py`, `infra/logic/registry/name_rulings.json`, `ops/status.py` (IRPT_ANLREQ) and `ycharts/generate/resident_worker.py` (IRPT_YCDGEN): old and new blob, the commits, whether and how the resident uses it, and what changes in behaviour | the worker's deliverables | LOCAL |
| `AR-y-198` | the five cross-box members (`_authz/loaders.py`, `infra/logic/registry/exemptions.json`, `scopes.json`, `lib/opal_naming.py`, `infra/logic/registry/firm_pages.json`) each compared to the version its owner released (act 4's eight Lambda artifacts for ADVI_FIRMBKTS, the CTLPLN release): EQUAL, NOT_EQUAL or CANNOT_TELL | the worker's deliverables | LOCAL |

## Edges and chains

- None. M = 3 chains: {196}, {197}, {198}.

fanout: 3 of 3 chains, cap 8, reason: three independent read cells.
