# IRPT_BCKEND round 76 -- workstream ~Y decomposition (release 6, part 1: install the custody factory in irpt-ycharts-generate)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~02:4xZ. Inputs:
- `1.0.0_SA_CTO~DELL2` msgs 2124 (Y wires the custody factory into `generate_installed`, release 6), 2129 (port owners) and 2162 (two
  pair conditions from the CVO);
- `~K2` row `IRPT_CUSTDY-W18-S1`;
- the port contract `deliverables/2.0.0_SA_COO~Y2/release6_custody/CUSTODY_PORT_CONTRACT.md` @859ae01405.

**Both port halves are drained:**
- ~M2 port 2: `holdings/holdings_publication_port.py`, @49cecd310d (round 35; the publication.py name collision is cleared);
- ~P2 ports 1, 3 and 4: `_scope/custody_ports.py`, @3998906069 (IB-pr-382). Its read set and staging list are in
  `deliverables/0.9.0_WK_IRPT_BCKEND~190/IB94-1_custody_ports_read_set.json`.

Row `IRPT_BCKEND-D2-S19` disarms the pyarrow hazard (`D2-W190-S3`) by the AWSSDKPandas layer. ONE issuance, one cell, no edges.

| item | cell | cut? |
|---|---|---|
| Install the custody factory: `reports/generate_installed.py` routes a no-`input_id` body to `build_accepted_custody_entry(AcceptedCustodyReader(...))` instead of raising `CUSTODY_FACTORY_REQUIRED`; stage every module the path needs; attach the pandas layer; declare the read/write grants in `ycharts/generate.tf` | `IB-yr-761` | **CUT** |
| Release 6 itself (pair + apply) | -- | NOT CUT: follows this cell's drain, under a fresh pair |

| criterion | invocation | base reading |
|---|---|---|
| Y76-1-AC1 (a statement submission reaches the custody factory; an `input_id` submission still reaches the prospect factory) | `python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed_custody.py` | FAIL: the file does not exist |
| Y76-1-AC2 (no staged commit ships split) | `python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r73/cochange_closure.py irpt-ycharts-generate` | PASS at base (split=0); must stay PASS after the new rows |
| Y76-1-AC3 (every imported name resolves in the built zip) | `bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh` | PASS at base (missing=0); must stay PASS after the new rows |

Risk WORLD (the L6 gate floor; served code and IAM declarations). Nothing deploys here.

## Four-postulate record

(i) Domain: one route branch, the modules it needs, one layer and its grants. (ii) One install. (iii) One intent: a Performance client
statement submission is accepted instead of refused. (iv) PERFORMANCE, ANALYSIS, the prospect path and every other function do not
move.

fanout: 1 of 1 chains, cap 8, reason: one item. Worker slot `~223`.
