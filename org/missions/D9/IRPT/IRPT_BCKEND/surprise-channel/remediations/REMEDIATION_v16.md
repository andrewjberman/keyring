# IRPT_BCKEND -- project sweep 6 remediations

<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01. Graduated at sweep 6's L9 (ADJUDICATION_v20.md). Three rows arrive REMEDIATED on a disarm their owner or the CTO recorded in the channel during the FAST interval (S244, S245, S247); S245 is not closed.

```json
[
  {
    "id": "IRPT_BCKEND-W99-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "opal-assets-ingest-mirror raises MirrorRaise ALIEN SURPLUS on its eclipse row on every Inflection invocation, after the orion row has copied. The function therefore reports failure every day, and a real orion-row failure would look the same.",
    "evidence": [
      "investigation row IRPT_BCKEND-W99-S3",
      "the function's log streams of 2026-10-01 and 2026-09-30 (this seat, ~15:1xZ): the same raise on the same two keys under eclipse/inflection/bronze/eclipse_membership_map/date=2026-09-24/",
      "1.0.0_SA_CTO RULINGS batch 88 item 6: the mirror's three files granted to 2.0.0_SA_COO~P, code only (lane IRPT_BCKEND_FAST_P_MIRROR)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Under the batch 88 grant: an unknown key under a mirrored prefix is skipped and named, not raised on, or the two keys are given an owner. Accept: one scheduled Inflection fire ends without the raise and its log names what it skipped. The silver sweep's standing FAIL on one alien fact_assets key (W99-S4) is the same class and is read at the same time.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-04T23:19:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W100-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A perfrp performance leaf for 49 Financial sits on the serve origin with Since-inception figures that include the inflated 2025-01-10 day (the S237 error), while the portal's comments say no perfrp key is served.",
    "evidence": [
      "investigation row IRPT_BCKEND-W100-S2",
      "s3api head-object on opal-data-portal-v2 platinum/advi/49financial/perfrp_performance_account.json (this seat, ~15:1xZ): LastModified 2026-09-01T03:16:07Z, 1,923,593 bytes, unchanged since the row",
      "not read by this seat: whether any portal route fetches the key today",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The issuer's choice, as the row says: correct the figures at their emitter, or withdraw the leaf from the serve origin under a never-widen sign-off. Until then the portal's comment and the origin disagree, and anything that starts reading the key serves the error.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-05T04:58:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S241",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "served.py's service-principal firm reader wraps its lazy import of canonical_profile_reads in a catch-all that returns an empty list, so a bundle missing that module refuses every service principal with FIRM_BINDING and no log line naming the cause.",
    "evidence": [
      "investigation row IRPT_BCKEND-S241",
      "infra/aws/lambda/investor-reporting/_authz/served.py:930-953 at HEAD (this seat): the import at :935 is inside the try whose handler at :952-953 is `except Exception: return []`",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Let an ImportError propagate (or log the missing module by name) while every read failure still restricts everything. The build-time check that proves the import in each bundle stays.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S244",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The service principal's firm limit was enforced nowhere on deployed bytes: the resident ran a root without allowedFirmIds and the served boundary was not moved.",
    "evidence": [
      "investigation row IRPT_BCKEND-S244",
      "resident host, this seat's read-only Systems Manager read 2026-10-01 13:07Z: root 9ac9b56d3c-st8, current_authority.py sha256 5291b3be7e0006ad equal to the pin and CLOUD HEAD",
      "the sections route as the service principal with another firm selected: UNAVAILABLE, FIRM_BINDING (this seat, 13:05Z)",
      "investigation rows IRPT_BCKEND-S246 and S248 (1.0.0_SA_CTO): the resident half closed on the st6 install, the API half on six functions read live",
      "limit carried from S248: the resident's own refusal of a foreign-firm JOB has not been exercised live",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Done on both deployed planes. The one arm not exercised (a foreign-firm job reaching the resident) needs a job the API now refuses to accept.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-01T07:18:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S245",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Inflection's holdings-basis gold was dated one trading day late since early May 2026 because the producer paired date=t with the prior trading day's partition for every source, while Inflection's partition dated D holds the close before D.",
    "evidence": [
      "investigation row IRPT_BCKEND-S245",
      "sources.json 1.2 and holdings_performance.py at CLOUD HEAD (032eed278a): which close a partition holds is data per source; this seat's run of the producer's suite, 55 passed",
      "investigation row IRPT_BCKEND-S254 (2.0.0_SA_COO~P, on 1.0.0_SA_CTO's read 103769): the gold is rebuilt on the measured basis; one account reproduced by hand at three places, 6 of 6 rows equal",
      "lambda list-functions (this seat, ~15:1xZ): irpt-holdings-performance-lambda LastModified 2026-09-29T14:42:51Z, so the DEPLOYED producer is still the earlier build; the hand reproductions were not re-run by this seat",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The gold and the source are right. What remains before this closes: the producer that runs on a schedule for Inflection is the 1.2 code, with a fire time after the partition lands (row S257 carries the timing).",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-01T13:12:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S247",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Three retained Performance reports carrying a vendor's calculated return (one Inflection, two Cottonwood) were within the reopen path's reach, against FWD-3.",
    "evidence": [
      "investigation row IRPT_BCKEND-S247",
      "investigation row IRPT_BCKEND-S249 (2.0.0_SA_COO~P): before and after on the deployed bytes; the adapter live until 08:20:26Z returned all three, the adapter live since refuses all three with OBJECT_NOT_COVERED",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md third wave @2858785e52: the released zip hashes to the live CodeSha256; 4 of 4 refused vendor uses answered OBJECT_NOT_COVERED in the live log",
      "lambda get-function-configuration today: the adapter is unchanged since 08:20:26Z (cdbFZDJA..)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Done: a retained report reopens only when its lineage provider is the holdings basis. The three reports remain retained and unreachable; whether they are kept is a retention question, not this row's.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-01T08:33:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S250",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The coerced Inflection positions file for 2026-07-02 differs from its raw file in four attribute columns on 9 of 33,618 rows; no price, share or value column differs; nobody has read why.",
    "evidence": [
      "investigation row IRPT_BCKEND-S250",
      "the row's own measurement (2.0.0_SA_COO~P); 1.0.0_SA_CTO RULINGS batch 81: a coerced date is admitted only if equal row for row on its neighbours; 2026-07-01 is not admitted",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A placement, not a repair: who reads why the coercing step and the raw pull disagree on that date. Un-parks if 2026-07-01 is ever wanted in the gold.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S251",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ETF ownership producer's source says it writes a per-date staleness determination under orion/inflection/meta/dedup/ on every run; the prefix holds no object.",
    "evidence": [
      "investigation row IRPT_BCKEND-S251",
      "s3api list-objects-v2 on opal-data-assets orion/inflection/meta/dedup/ (this seat, ~15:1xZ): no keys",
      "not read: whether the deployed function is the version that writes determinations",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A placement: compare the deployed function with its source and decide whether the determinations are wanted. It belongs with the ETF ownership pipeline's owner, not with this project.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S252",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On five of ten Cottonwood holdings partitions read, 3.4 to 5.9 percent of the securities that moved carry the prior day's close, so their holdings return is dated a day late on those days; the declared basis is one close per partition.",
    "evidence": [
      "investigation row IRPT_BCKEND-S252",
      "the row's own measurement on 10 of 81 partitions (2.0.0_SA_COO~P)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Parked by its owner with a stated condition: read which securities, and the other 71 partitions, when Cottonwood's holdings basis is served.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S253",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The READY receipt of a resident job carries no vendor_requests ledger: the ledger of IB-yr-291 is written in a module the resident's worker does not use for its receipt.",
    "evidence": [
      "investigation row IRPT_BCKEND-S253",
      "irpt-jobs row of REQ-a69e5751d42c374f1d2354f9 (this seat's consistent read, 13:0xZ): job_detail holds three keys, certification_sha256, report_id and revision, and no ledger",
      "1.0.0_SA_CTO RULINGS batch 86 item 13: a row for the round with 2.0.0_SA_COO~Y as owner",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The resident's worker writes the vendor-request ledger onto its receipt, or the order's claim is restated to the path that does. Accept: the next READY receipt carries it.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S257",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Inflection holdings-producer function and schedule declared in Terraform (unapplied) fire at 07:30 America/New_York, before the partition that holds the prior day's close lands at 13:05Z; under the measured close basis every row would become a two-day linked row dated a day late.",
    "evidence": [
      "investigation row IRPT_BCKEND-S257",
      "the row's own read of the declaration (2.0.0_SA_COO~P, 15:02Z); not applied, so nothing does this today",
      "the row names the trigger: an untargeted apply in the holdings-performance root would create both as declared",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Re-time the entry in the serving packet before anything applies it, as the row's owner states. Until then an untargeted apply in that root is the hazard: the root should not be applied untargeted.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-04T23:19:00Z"
    }
  }
]
```
