# AMGT_HARVST -- round 84 remediations (dell1)

<sweep_watermark>2026-10-13T21:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T21:20:00Z. Graduated at ADJUDICATION_v79: 2 rows, INERT.

```json
[
  {
    "id": "AMGT_HARVST-Z-S119",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "bz-6's saved sessions read VALID=True (a local predicate) yet both publishers' next cycle ended STOPPED=sign_in_refused: wsj after 35 pairs in 69 min, barrons after 0 pairs in 21 s.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S119",
      "order bz-7 CANCELLED record",
      "adjudication row AMGT_HARVST-D1-C-S41"
    ],
    "remedy": "The CTO's (A) cell (msg 5143): the runner refreshes once per publisher per cycle through the existing SessionManager, printing Barron's refusal class (expired, entitlement or blocked) first. Close when: one wsj and one barrons cycle each end completed=true unattended, read from their cycle records.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v84",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v84"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-S15",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The astn-pipeline Terraform root carries a pending aws_instance.astn user_data diff, so an apply of that root (even one signed for a schedule flip) starts the stopped instance i-059405dfefcb4b44a; bz-8's apply did at 20:48:11Z, and it was stopped again at 21:04:03Z on Andrew's relayed word.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S15",
      "3.0.0_SA_CVO describe-instances i-059405dfefcb4b44a: stopped, 'User initiated (2026-10-13 21:04:03 GMT)'"
    ],
    "remedy": "Reconcile or ignore the pending user_data diff under its own pair so a plan of the astn-pipeline root no longer touches aws_instance.astn. Close when: a plan of that root reads 0 changes to aws_instance.astn.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v84",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v84"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  }
]
```

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-Z-S119`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the row until the round-86 reading the CTO orders on Z-S121, then re-runs one wsj and one barrons cycle; un-parks when both cycle records end completed=true unattended. Basis: Not met: the bz-7 read in the row's grounding shows wsj and barrons each still ending STOPPED=sign_in_refused, with no completed=true cycle record for either publisher, and the later Z-S121 read shows a single refresh does not cure the expiry.
- `AMGT_HARVST-D1-S15`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 reconciles or ignores the pending user_data diff under its own pair; 0.7.0_AE_CloudOps~SC1 then runs the plan of that root; un-parks when the plan reads 0 changes to aws_instance.astn. Basis: Not met: the pending aws_instance.astn user_data diff is still on the astn-pipeline root (row D1-S15, bz8_apply.out), and the close is a plan of that root reading 0 changes to aws_instance.astn, which needs an AWS plan this worker may not run.

-- 3.0.0_SA_CVO
