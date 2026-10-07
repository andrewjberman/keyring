# NFRA_OPLGTW -- surprise channel, REMEDIATION v5 -- THE SLUG (round 17)

Author: 3.0.0_SA_CVO~O. Round: v5. Fabric: site-z. Recorded: 2026-10-06T00:55:00Z. **Reader:** `1.0.0_SA_CTO~O`.

5 rows, graduated by `adjudications/ADJUDICATION_v9.Z.md` C-S26. Round 17 has no L9 grade (no judgment criterion).
- **OPEN, for the CTO (4):**
  - Z-W27-S3: the p95 regression, +71 % over the cap on every served release.
  - Z-W15-S41: FWD-4 is unexercised by any real principal; the grant change is Andrew's word.
  - Z-W15-S47: CLOUD's gateway source and live have diverged in both directions.
  - Z-S55: the onboarding kit still installs the June local setup.
- **OPEN, for the issuer (1):** Z-W15-S51, checks graded against anchors they cannot read (seven rows in two rounds).

Standing, not new: Z-W15-S37 (OPEN, the one-process test isolation; three more sightings this round). Z-W13-S5 (ARMED,
moot, waits on the issuer's disarm). Z-W16-S5's re-measure ran (Z-W27-S3) and confirmed the regression.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W27-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The full-day 2026-10-05 ALB TargetResponseTime p95 of the opal-gateway target is 0.9473 s over 3,328 requests (no 5xx datapoint), +71.1 % against OG-p-1's 0.5535 s and above the 0.6642 s cap. The segment p95s are 0.73 / 1.02 / 0.97 s across the three releases served that day, and the hourly profile sits near 1 s in the low-volume hours. This is the full-trading-day re-measure Z-W16-S5 asked for; it confirms the regression rather than clearing it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W27-S3",
      "remediations/REMEDIATION_v3.md#NFRA_OPLGTW-Z-W16-S5",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W27-S2 (day-level reads 09-30 to 10-02)"
    ],
    "remedy": "OPEN: the CTO cuts a cause read (per-route or per-integration latency on live; whether the low-volume hours are cold-path cost or a code change since OG-p-1), then a fix cell or a ruling on the cap. Until then FWD performance claims read against a breached cap.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round18.md R19 @b397c851c0 (the latency cap is per route: OG-p-1's routes keep 0.6642 s; a route added since takes its own first-full-day reference +20 %, GET /hx/teams/chats 1.224 s; the aggregate ALB p95 is retired as a grade), on OG-pm-2's MIX finding; clock written by 3.0.0_SA_CVO~O on the owner's word, 1.0.0_SA_CTO~O msg 29926 / R23 @98c25ed40e"
      }
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S41",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The one live grant naming dim_asset carries list/describe/query and not download_filtered, so the r17 dim_asset download (FWD-4) opens for no real principal; the verify run exercised it only through a synthetic in-memory grant. The release added no authorization and wrote no grant.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S41",
      "deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6_20261005.md section 3(d)"
    ],
    "remedy": "OPEN: the CTO puts one call to Andrew: grant download_filtered to the dim_asset grant holder (a grant write, which PRD v1.7 reserves to his word), or accept FWD-4 as served-but-unexercised. A grant write, if given, takes the post-act read of a real download under C3.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S47",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Gateway releases are cut on live and their branches are not drained back, so CLOUD's gateway source and live have diverged in both directions: CLOUD's app/server.py carries OA-e-10's /login change (18 lines) that live lacks, and live's deploy-to-ec2.sh .env template carries lines CLOUD's lacks. A release cut from CLOUD would ship OA-e-10 unreviewed and drop live template lines; every release must re-prove its diff against two bases (Z-W15-S44, Z-W15-S47).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S47",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S44"
    ],
    "remedy": "OPEN: the CTO rules the lineage: either drain each release branch back to CLOUD after its deploy (and decide whether OA-e-10's /login change ships or reverts), or name CLOUD as not the gateway's source of record. Until then a CLOUD-based release can regress live.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S51",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer checks keep grading against an anchor they cannot read at the moment they run: rl6.AC1 reads the manifest at HEAD before step 21 commits it (S51); rl6.AC1's 'before' arm names a state that no longer exists after a later release (S45); q7.AC1 needs '::<test> PASSED' on one line, which a capsys print splits (W22-S6); q7.AC2 counts textual call sites, which a single helper defeats (W22-S7). With the issuer's own S38 (stale expect), S42 (kit files absent from the tarball) and S50 (hard-coded 50 .env names), that makes seven rows in two rounds. Each was caught, but each cost a FAIL, an amendment or a re-grade.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S51",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S45",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S7",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S38 / -S42 / -S50 (issuer-dispositioned)"
    ],
    "remedy": "OPEN: the issuer runs each new or reused check once against the release tree BEFORE GO (a pre-GO exercise with its expected PASS and one negative control), and re-runs it whenever the order is amended or the .env shape or step order changes; a check whose anchor appears only after a later step is moved to after that step.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S55",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The in-repo colleague onboarding kit .tools/m365-mcp-kit/ (last touched 2026-06-12, @8b0e7d2412) still installs a LOCAL Lokka server ('Lokka-Microsoft', npx @merill/lokka) under the old 'm365' name. The correct reconnect to the hosted gateway (https://mcp.opalinvest.dev/mcp, as opalgateway, work-account sign-in) is written nowhere a colleague would find it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S55"
    ],
    "remedy": "OPEN: the kit is rewritten (or retired with a pointer) to the hosted-gateway reconnect: remove the old entry, add opalgateway over HTTP, authenticate with the work account.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~O
