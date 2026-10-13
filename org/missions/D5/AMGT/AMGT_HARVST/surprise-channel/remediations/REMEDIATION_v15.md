# AMGT_HARVST -- round 80 remediations (dell1)

<sweep_watermark>2026-10-12T14:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T14:15:00Z. Graduated at ADJUDICATION_v72: 3 rows (D1-W135-S2 ARMED; D1-S8, D1-S9 INERT).

```json
[
  {
    "id": "AMGT_HARVST-D1-S8",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal-research-pull-enqueue logs only a successful enqueue and the portal API stage has no access log, so the CTO half's post-act read (Branch B: an internal 403 in the first trading day) cannot be seen; the issuer restated it as START count minus OK lines, which counts refusals plus errors without the caller's tier.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S8",
      "order bx-2 COMPLETE record"
    ],
    "remedy": "One handler line that logs a refusal with the tier string (never the ticker or body), then one redeploy under its own pair. Close when: a deployed non-internal invoke leaves a refusal line naming its tier in /aws/lambda/opal-research-pull-enqueue.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-S9",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The portal authorizer grants ALL access to userType 'Dev' whatever its tier, while the fenced handler admits only tier 'internal', so a Dev login whose tier is not 'internal' passes the authorizer and gets 403 here. Not measured: whether any Dev login carries another tier or uses the research page.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S9"
    ],
    "remedy": "The CTO rules whether a Dev login of another tier should be refused (the ruling's text is '403 unless exactly internal'). Close when: the ruling is on record and, if it changes the rule, the fence's tests carry the Dev case.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-W135-S2",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A failed pair's reason was lost at three hops (Collector.run_job dropped the job's detail when a run record existed; run-record jobs carried no detail; the cycle record copied the status). bx-3 fixes all three in code @1c69fa35a3, but site Z's runner still runs b5a7a3a4b6, so cycle records keep writing detail == status until a re-pin.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W135-S2",
      "merge @1c69fa35a3 (bx-3 AC1 11 passed, AC2 63 passed on 3.0.0_SA_CVO's run)",
      "ledger/ROUND_ANALYSIS.round79.md item (2): the re-pin is planned as a crossbox order, not yet cut"
    ],
    "remedy": "Re-pin site Z's runner to a commit carrying @1c69fa35a3 (a crossbox order to site Z's runner owner, under its own pair). Close when: the first cycle record after the re-pin carries failures whose detail differs from the status; disarm on the same read.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v80",
      "closure": {
        "reason": "CARRIED_BY",
        "pointer": "org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md:3855 (HVST-bz-1, STAGED for round 82, owner 0.7.0_AE_CloudOps~ZW, CTO msg 4476)"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": "2026-10-13T18:05:00Z"
    },
    "closed": true
  }
]
```
