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

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-D1-S8`: RE-OWNED to `0.7.0_AE_CloudOps~SC1`. Next act: SC1 redeploys the HEAD handler under its own pair, makes one non-internal invoke and reads the refusal line naming the tier from the CloudWatch group; un-parks on that line. Basis: Not met: the handler line exists at HEAD (git show HEAD:infra/aws/lambda/research/pull_enqueue/lambda_function.py:118 logs DENIED tier=), but the close needs a deployed non-internal invoke whose refusal line appears in /aws/lambda/opal-research-pull-enqueue, which this seat cannot read.
- `AMGT_HARVST-D1-S9`: RE-OWNED to `1.0.0_SA_CTO~DELL1`. Next act: 1.0.0_SA_CTO~DELL1 rules whether a Dev login of another tier is refused; un-parks when the ruling is on record and, if the rule changes, the fence's tests carry the Dev case. Basis: Not met: a comp-find of 'unless exactly internal' finds the ruling text only in the population file, the REMEDIATION_v15 row and the bx-2 order; no CTO ruling on whether a Dev login of another tier is refused is on record.

-- 3.0.0_SA_CVO
