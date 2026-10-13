# IRPT_ANLREQ -- decomposition, round 21 READER r19.3 RELEASE PREPARATION, workstream YR round 14 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO round-21 analysis, section 3 items 1 and 4 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md`): reader r19.3 is built and drained (@d20800082a, `AR-y-221`); the r19.3 release pair (two legs) follows. MEASURED by this seat at HEAD: `intake/uploads.py` sha256 `176682cb1545...` is the SAME bytes both legs carry since release 19; `intake/template_reader.py` is `a61cd0c622f8...` against the live r18.1 `83ab9b45d590...` (history: r19.1 `920cdf69ca`, r19.2 `77f804b5e2`, r19.3 `55d1755d39`). So the release moves ONE member in each leg. The live state to move from: resident root `0485393f3a-r19` (tarball `irpt-resident-0485393f3a-r19.tar.gz`, sha256 `84df6479...`), Lambda `irpt-ycharts-generate` live at `hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=` (release 20; built at base `4067c2dd5b` with its release diff).

The three cells prepare the pair's numbers; none uploads, installs or applies anything. The pair itself and the apply orders follow their records.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-226` | the re-open matrix of the r18.1 pair against the r19.3 pair (stored by each, re-opened by each, run in process) and the effect table: the one-account and two-account header cases (the 16 negatives, the 5 positives of `AR-y-221`) read by both | scratch only, one record | LOCAL |
| `AR-y-227` | the resident leg: the release-19 tarball with ONLY `template_reader.py` moved (plus the bindings and the sums), its delta, determinism control, new root name, host script, and the reader's tests on the extracted package | scratch only, one record, one script copy | LOCAL |
| `AR-y-228` | the Lambda leg: the live `irpt-ycharts-generate` package read from AWS now, the release build (live plus `template_reader.py` only) and a no-move control that reproduces the live CodeSha256 | scratch only, one record, one map patch | LOCAL |

## Edges and chains

- None between the cells: M = 3 chains. `AR-y-226` decides the ORDER of the legs in the pair; `AR-y-227` and `AR-y-228` do not depend on it.

fanout: 3 of 3 chains, cap 8, reason: three independent preparation reads with disjoint scratch and records.
