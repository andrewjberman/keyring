# IRPT_BCKEND -- project sweep 3 remediations

<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-29. Graduated at sweep 3's L9 (ADJUDICATION_v17.md).

```json
[
  {
    "id": "IRPT_BCKEND-S216",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Inflection's Orion positions stopped landing after 2026-09-27. The producer lands every calendar day at 13:05Z, so two landings (09-28, 09-29) are missing; this is a count of landings, not a trading-day staleness call. It blocks the INF performance producer's first fire and the INF adapter switch.",
    "evidence": [
      "aws s3api list-objects-v2 opal-data-assets orion/inflection/bronze/positions/2026-09-2*, read by this seat 2026-09-29 19:0xZ: 6 keys, 09-22 through 09-27, each LastModified 13:05Z; none for 09-28 or 09-29",
      "row S216",
      "TO-IB-pr-241 pending (the raw-writer diagnosis)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P0: TO-IB-pr-241 names why opal-assets-silver-orion logs START and nothing else; 1.0.0_SA_CTO places the owner of the Orion positions pull. Disarm when date=2026-09-28 and later partitions exist in silver fact_positions.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S218",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "No Analysis report can be produced: on generate build inrij6hL both jobs that reached the vendor died SESSION_REFRESH_ALREADY_USED, because the job's first act spent the one admitted session refresh.",
    "evidence": [
      "row S218 (2.0.0_SA_COO~Y); proof commit e146a80a3d",
      "not re-read live by this seat",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P0: 2.0.0_SA_COO~P reads why the resident holds no usable vendor session at job start; 1.0.0_SA_CTO rules whether one refresh per request is the right allowance. Disarm when a job on the live build reaches READY without spending its refresh at fence 1.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S217",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The directory bundle's member list lacks schwab_account_codes.py and .json, which directory_runner.py imports at load (line 121); a bundle minted as defined fails every directory fire. The live bundle predates the import, so nothing served is broken yet.",
    "evidence": [
      ".tools/safe_deploy_core.py at HEAD: schwab_account_codes appears only at lines 423-437 (the Holdings closure), after the directory bundle's key at line 370",
      "data/assets/scripts/gold/investor_reporting/directory_runner.py:121 import schwab_account_codes as _sac",
      "row S217",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: a ~M cell adds both files to the directory bundle's members and proves import directory_runner from a locally built bundle. Interim control: 0.0.0_AB_MSTR skips investor-reporting.tar.gz at every push.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S213",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A READY report's sections route serves public_reason_code UNEXPECTED when the rendered bundle is absent; the ROUND_ANALYSIS.sweep2 rule is a figure or a named refusal, never UNEXPECTED.",
    "evidence": [
      "row S213 (2.0.0_SA_COO~P, read at W24 K10 on RPT-2e21b52e)",
      "not re-read live by this seat",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: render the bundle for READY reports, or map the absent bundle to a named refusal; read back on RPT-2e21b52e.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W80-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The shared handler's day selection assumes next-morning landing; Inflection's silver lands the same day, so every INF fire computes one trading day staler than its data supports. The INF producer is plan-only and held on S216, so nothing served carries this yet.",
    "evidence": [
      "row W80-S1",
      "TO-IB-er-501 drained d110bee556 (plan only)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: a follow-on cell makes _target_day source-aware, or 1.0.0_SA_CTO accepts the extra day as INF's designed lag; decided before the INF producer's first served fire.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S215",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A normalization dispatched while another resolve or generation is in flight on the same principal dies RESOLVE_RETRY_EXHAUSTED; reproduced three times across two generate builds. Carries S206.",
    "evidence": [
      "rows S206, S215 (2.0.0_SA_COO~Y); the third reproduction was unplanned and is stated as such by its author",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: 1.0.0_SA_CTO rules whether the resident's provider read is single-flight per host and whether a receive that never reached the provider counts against the four-receive bound.",
    "owner": "1.0.0_SA_CTO",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v24"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S214",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A holdings-basis press's time is its partition gets: frame_ms p50 6.7 s and max 14.9 s over 95 served reads, while the account-map sweep costs 59-259 ms. Carries S212.",
    "evidence": [
      "rows S212, S214 (4.0.0_SA_CRO)",
      "D1 closed d39ef96d92: 154 invocations, max 17.2 s (2.0.0_SA_COO~P drain-end 102978)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P3: enrichment candidate for the next analysis; no remedy is owed while the r3 rollback trigger (SI at or over 48 s) is not approached.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v24"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  }
]
```
