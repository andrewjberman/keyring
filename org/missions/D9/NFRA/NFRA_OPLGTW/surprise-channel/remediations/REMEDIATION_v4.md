# NFRA_OPLGTW -- surprise channel, REMEDIATION v4 -- THE SLUG (round 16)

Author: 3.0.0_SA_CVO~O. Round: v4. Fabric: site-z. Recorded: 2026-10-04T23:55:00Z. **Reader:** `1.0.0_SA_CTO~O`.

3 rows, graduated by `adjudications/ADJUDICATION_v8.Z.md` C-S23. Round 16 has no L9 grade (no judgment criterion).
- **REMEDIATED (1):** Z-S50, safe-commit's surprise-gate refusal now unstages the whole staged set (@f2c150d420).
- **OPEN, for the CTO (1):** Z-W15-S36, a release order cannot be committed on its release branch without the override
  its Bounds forbid.
- **OPEN, for the issuer (1):** Z-W15-S37, the schwab test set is order-dependent in one pytest process.

Standing, not new (ADJUDICATION_v8.Z C-S24): Z-W13-S5 reads moot and waits on the issuer's disarm. Z-W16-S5's re-measure
now takes the first full trading day on live 4b6b823fae (Monday 2026-10-05).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S50",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S46's remedy was met only for gate files after @bee7c817d7: a surprise-gate refusal unstaged and post-checked SRGATE_FILES only, so a non-gate path declared in the same commit stayed staged while the refusal printed 'none remains staged'.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S50",
      "f2c150d420 (1.0.0_SA_CTO~O): the refusal unstages and post-checks everything this call staged (staged-now minus the lock-entry baseline)",
      "re-read at HEAD 2026-10-04 ~23:4xZ: .tools/safe-commit.sh elif SRGATE_RC branch, comment citing Z-S46 / Z-S50"
    ],
    "remedy": "Met: every refusal branch of the surprise gate unstages the whole set the call staged and prints what remains staged.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S36",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A gateway release order has its worker commit a release branch cut from live, which predates the order. The owned-paths gate reads the order at that tree's HEAD, finds none, and refuses. OG-rl-4 and OG-rl-5 (4b6b823fae) both landed their release commits under the audited GIT_COMMIT_AUTHOR_OVERRIDE, against the order's Bounds ('never override a gate'). The org/standards contract twin is also outside the order's <paths>.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S36",
      "org/git-author-override-audit.log line 20557 (BLOCK, 0.9.0_WK_NFRA_OPLGTW~15, 21:37:06Z)"
    ],
    "remedy": "OPEN: the CTO rules one of two: (a) the release-order form names the audited override as a sanctioned step for release-branch commits, bounded to the order's listed paths; or (b) the owned-paths gate admits a release branch whose base is the order's live pin. Until then each release order contradicts its own Bounds.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S37",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "tests/test_schwab_*.py run in ONE pytest process errors at setup on every acceptance-fixture file after the first (RuntimeError: StreamableHTTPSessionManager .run() can only be called once per instance): 9 errors at CLOUD HEAD, 11 with OG-rl-5's new file. Each file passes alone. Third sighting (INVESTIGATION_v1.md:4015, :5752), never graduated, so every 'full set' criterion is graded per file or against a baseline of errors.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S37",
      "investigations/INVESTIGATION_v1.md:4015 (OG-t-1, test_ogz1_ac05 / ac08 in isolation)",
      "investigations/INVESTIGATION_v1.md:5752 (35 StreamableHTTP errors on live and release whole-suite runs)"
    ],
    "remedy": "OPEN: the issuer cuts a cell giving each acceptance-fixture module its own session manager (or app instance), so the whole schwab set passes in one process with 0 setup errors; a 'full set' criterion then grades one run.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v4"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~O
