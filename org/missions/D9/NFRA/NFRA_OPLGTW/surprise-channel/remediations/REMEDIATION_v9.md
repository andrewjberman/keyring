# NFRA_OPLGTW -- surprise channel, REMEDIATION v9 -- THE SLUG (round 22)

Author: 3.0.0_SA_CVO~O. Round: v9. Fabric: site-z. Recorded: 2026-10-06T19:23:00Z. **Reader:** `1.0.0_SA_CTO~O`.

2 rows, graduated by `adjudications/ADJUDICATION_v14.Z.md` C-S38. Round 22 has no L9 grade. OG-ga-1 closed FAILED on
AC2, with AC1 and AC3 PASS.
- **OPEN, for the CTO (1):** Z-W28-S1 (+ issuer row Z-S59). The held set admits a blank cusip, so 23 blank-cusip
  dim_asset rows pass C3 on the query and download paths. The act's hazard is DISARMED; the served rows are not.
- **OPEN, for the issuer (1):** Z-W28-S2. An operator-command order prints master ids on stdout.

**Advanced in place this slug (C-S40), REMEDIATED:** Z-W15-S41 (`REMEDIATION_v5.md`). FWD-4 is exercised by the real
holder.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W28-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "integration.py:341 builds the held set as frozenset(row[0] for row in pos_rows) with no blank filter. A held position with a blank cusip therefore puts the blank into the set, and every dim_asset row whose cusip is blank passes qualify_asset_plan. The query path (:656-660) and the download/export path (:939-946) share the one helper, so the real holder's query has admitted the same 23 rows since OG-q-7, and the S41 download now does too: 2173 returned = 2150 held + 23 blank, 0 non-blank unheld.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S1",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S59",
      "adjudications/ADJUDICATION_v14.Z.md#NFRA_OPLGTW-Z-C-S38"
    ],
    "remedy": "OPEN: the CTO rules whether a blank cusip may qualify a dim_asset row. If not (C3 reads 'only the CUSIPs the grant's accounts hold'), the issuer's fix candidate is one line at :341 dropping blank and null from position_cusips, plus a test with a blank-cusip held position, then a release under the usual halves; ga1.AC2 then re-runs unamended as the post-release read. If yes, the ruling amends C3's text and AC2.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v9",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v9"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-06T19:11:00Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W28-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ops/schwab_entitlement_admin.py prepare() and activate print the scope diff keyed by master id, and the order said only 'never print an account id'. The worker saw two account-number-shaped ids on its stdout once, before it redirected. The operator role also cannot dynamodb:Scan the state table, so the holder's pk was found under the caller's own read-only identity.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S2"
    ],
    "remedy": "OPEN: the next operator-command order redirects prepare()/activate output to the off-repo directory and prints only the operations line, and names how the holder's pk is resolved (the instrument's read-only Scan, or a GetItem on a known key).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v9"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
