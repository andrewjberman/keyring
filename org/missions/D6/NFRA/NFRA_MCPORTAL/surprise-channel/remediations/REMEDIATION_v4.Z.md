# NFRA_MCPORTAL -- surprise channel, REMEDIATION v4 (site Z) -- THE C17 ROUND-2 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-14 ~02:4xZ. **Reader:** `1.0.0_SA_CTO~Z`.

C17 round 2 has 4 of 4 orders terminal and reads MAY-CLOSE (re-run by this seat), with 0 judgment criteria. It is served
at b0c75d24f1. L8 is at `adjudications/ADJUDICATION_v4.Z.md`.

- **C17 is REALIZED.** The bound holds: one pointer get per box, and a cold read of 1.3 s on the host and 2.2 s from this
  box against the 5 s bar (Z-C-S30). This seat re-read the pointer census: laptop present, the other three 404.
- **A display defect graduates (Z-C-S31).** `integration_refused` reads "not recorded" both for a box whose clean
  integrate pass IS recorded (laptop) and for a box with no pointer. The basis text shown is false for the first.
- **The backlog is cleared.** No CVO compile had been written since v3 (10-09), so 39 rows were undispositioned, four of
  them ARMED since 09-25.
  - 30 are dismissed as resolved by later rows or acts.
  - 5 recipe rows go to the cut template; they are the same class as NFRA_MCPINDEX Z-S92.
  - 3 graduate, below.
  - Three REMEDIATION_v1 rows that Z-S20 disarmed are flipped to REMEDIATED in place: Z-W3-S3, Z-C-S10 and Z-W3-S2.

**For the analysis:**
1. **Z-S47 is Andrew's word with no outcome:** account and usage per box on /control-plane. It lands at the GW round's
   analysis.
2. **Z-C-S31:** show `no` (measured, with `at`) for rc 0, and `not recorded` only for a missing pointer.
3. **Z-W2-S8:** the rollback-time bound has not been re-measured since 09-25.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S31",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "app/admin_fabric_gitstate.py _refused returns 'not recorded' for a pointer with rc 0 as well as for no pointer, and the basis shown says 'no integrate pass has been recorded'; laptop's recorded clean pass (02:37:22Z) displays as not recorded",
    "evidence": [
      "3.0.0_SA_CVO~Z read of admin_fabric_gitstate.py:15-16, :59-61, :173-182 and the four head-objects, ~02:4xZ 2026-10-14"
    ],
    "remedy": "Three states, three displays: rc != 0 shows {at, note} (refused); rc == 0 shows 'no' with the pass's at (measured); no pointer shows 'not recorded'. The basis text names which one applies. Closes when the served page reads 'no' for laptop and 'not recorded' for a box with no pointer.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~MP", "round": "v4"},
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S8",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a triggered gateway rollback through safe-ec2-deploy.sh spent about 12 minutes in its HALT-GATE scan before reaching the host (09-25), so the outage it bounds is 12-15 minutes while release orders state rollback triggers in seconds; not re-measured since",
    "evidence": [
      "NFRA_MCPORTAL-Z-W2-S8 (0.9.0_WK_NFRA_MCPORTAL~2)"
    ],
    "remedy": "Re-measure the named rollback path's time-to-host on today's wrapper, or name the rollback as a direct deploy-to-ec2.sh redeploy of previous_deployed_commit with its measured time. The release template states the measured bound.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v4"},
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-S23",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "an untargeted plan of infra/aws/terraform/opal-gateway reads 1 to change (aws_lambda_function.mcportal_grant_writer in place) and errors on a data source for the absent secret gateway/mail/commassist-bearer; left as found, a hazard for the next untargeted actor",
    "evidence": [
      "NFRA_MCPORTAL-Z-S23 (0.7.0_AE_CloudOps~MP); not re-planned by 3.0.0_SA_CVO~Z"
    ],
    "remedy": "Re-plan untargeted. Reconcile the grant-writer drift, or adopt it in code. Make the secret's data source match what exists, now that commassist is a named bearer holder (NFRA_OPLGTW v2.4 C7). Closes on an untargeted plan reading 0 to change with no error.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~MP", "round": "v4"},
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-S47",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Andrew-direct ~20:4xZ 2026-10-13 (XB-20261013T202846Z-111f): /control-plane shows, per box, the logged-in Claude account and usage remaining on the 5-hour and weekly windows; no PRD outcome carries it yet",
    "evidence": [
      "NFRA_MCPORTAL-Z-S47 (1.0.0_SA_CTO~Z); org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_204xZ_CONTROL_PLANE_SHOWS_CLAUDE_ACCOUNT_AND_USAGE (cited in the row)"
    ],
    "remedy": "A PRD addendum at the GW round's analysis adds the outcome: account (email, plan, organization, never a token) and 5-hour and weekly usage with reset times and claim words, per box. It is then cut.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~Z", "round": "v4"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
