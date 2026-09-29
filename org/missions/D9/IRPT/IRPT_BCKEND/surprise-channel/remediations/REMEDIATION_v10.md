# IRPT_BCKEND -- round 19 remediations

Author: 3.0.0_SA_CVO, 2026-09-29. Graduated from INVESTIGATION_v1.md at round 19's L9 (ADJUDICATION_v14.md). Priority is in each remedy (P0/P1/P2). Evidence detail: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md.

```json
[
  {
    "id": "IRPT_BCKEND-S176",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "NEW-01: the page reopens RETAINED Performance reports, so an invested 49F account still reads -100.00% YTD after the compute guard (S186, the same account); near-miss accounts just above r_net <= -1 also serve about -100% (S184).",
    "evidence": [
      "STATUS~P.md:34 (CRO D1 NOT MET)",
      "walks 20260928T220437Z shot 011 and 20260929T000244Z shot 010: -100.00% on ****9079 / IRA",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P0: serve IB-pr-194 (the retained reopen guard, built @90c4b596f3) and show the named refusal on a walk of this account (D1). Then retire the 49F engine read when FWD-3 turns REALIZED for 49F (v0.19 item 12); until then S184's near-misses need the class predicate or an accepted residual stated in STATUS~P.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S173",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The COT gold host cannot read bd-securities, so served COT classification is name patterns plus a ticker-shape heuristic; every COT classification act (cash, other, NEOS/CSHI) is moot on served output until the classifier reads the canonical table.",
    "evidence": [
      "row S173",
      "row S188 (ruling: one act, gated on the etf-classifications fill; coverage COT 39.7%, BD 68.1%)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: the canonical-classifier re-point to etf-classifications as ONE act with halves (S188), then the R1 read-backs of cot-cash-admission and bd-securities-cot-new-p1 on served output.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S155",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "COT lib/mix_views MIX_ASSET_CLASSES lacks cash and other, so the period bars will disagree with mix_daily_summary once classification is live.",
    "evidence": [
      "row S155",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: decide before S173's re-point lands: widen COT mix_views under the same half, or state in the read-back that the period bars keep the residual.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S182",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Every account of the COT eleven-account client reads one identity ('****8774 / UTMA') in OVER WHAT, the pie legend and the table.",
    "evidence": [
      "row S182",
      "DSGN_IRPTV1 walk 20260928T182319Z shot 017 (3.0.0_SA_CVO grade record @43d796a418)",
      "CRO brief docs/briefs/irpt-ui-remaining-brief-20260928.md:61 UIR-26 (owner ~M)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: read the served holdings snapshot for this client and name whether the eleven nodes carry one display.label; if so, the producer emits a distinguishing tail and type per account; if not, it returns to 2.0.0_SA_COO~D.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S147",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A served 49F Performance read took 30.19 s, past API Gateway's 30 s cap, so a first open fails.",
    "evidence": [
      "row S147",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: measure the same account after the pool fix (bb09a3467c) rides the adapter; the engine read retires with FWD-3 for 49F, so no lever is owed beyond that measurement.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S149",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Every EC2 role with AmazonSSMManagedInstanceCore can ssm:GetParameter* any parameter; only the IRPT render host is fenced.",
    "evidence": [
      "row S149",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: census the roles carrying the managed policy and their real GetParameter reads, then a per-role Deny NotResource or a customer-managed replacement. Estate-wide; routed through 1.0.0_SA_CTO to the cloud-ops owner.",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S151",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The host YCharts session capture failed silently at window-6 receive 1 and spent the one-use session_refresh intent.",
    "evidence": [
      "row S151",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: parked on Andrew's word for ONE wrapper run (a live YCharts call); un-parks when he gives it. Keep the wrapper's output on that run.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S152",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "INF holdings lagged the INF directory by 3 trading days (09-22 vs 09-25).",
    "evidence": [
      "row S152",
      "STATUS~M.md:65 (R4 QA fire SUCCESS at all three firms; ENABLE half sent)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: closes on the first SCHEDULED INF holdings publication at T-1 after the R4 enable, read from its manifest.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S165",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The cot box has no in-run login retry, so one transient login failure freezes the COT chain for a day, silently; FWD-12 reads COT silver daily from that chain.",
    "evidence": [
      "row S165",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1 (raised by v0.19: FWD-12 reads COT silver daily): the CTO rules the retry deploy (the newer .js, CTO-gated) or an alternative that surfaces a failed login the same day.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S166",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The login script the cot box runs has no build input in the cot tree; a redeploy from that tree would not reproduce it.",
    "evidence": [
      "row S166",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: name the cot login script's source of truth and the tree it is built from, before any cot redeploy.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W62-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A pre-existing export test fails: a bare import of handler binds whichever same-named Lambda handler module was cached first.",
    "evidence": [
      "row W62-S1",
      "row S183 (carried to the next ~P round)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: the next ~P round isolates the handler import (module path per Lambda) and makes the export suite green.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W42-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A task order's proof_of_spec names an instance keyed off its to_id while check_complete_flip globs the order FILE's stem; four occurrences this round (W41-S3, W61-S1, W63-S1, W42-S4) and W21-S1 before.",
    "evidence": [
      "rows W41-S3, W61-S1, W63-S1, W42-S4",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: either check_complete_flip also tries the to_id-derived name, or L6 keeps every order's file slug equal to its to_id. One rule, the gate owner's.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S187",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Worker slot ids have no allocator across workstreams (~63 issued by ~Y and by ~P).",
    "evidence": [
      "row S187",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: a per-workstream slot band, or a gate limb refusing an order whose issued_to holds another workstream's non-terminal order.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S132",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Lambda@Edge role can read both PRIVATE signing keys (opal/auth/*), though it needs only the public keys.",
    "evidence": [
      "row S132",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1 (security): narrow lambda-edge-secrets-logs to the two public-key ARNs; routed through 1.0.0_SA_CTO to the portal-auth IAM lane.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S145",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A READY 49F snapshot states 0.0 for three accounts without saying whether they are empty or unvalued.",
    "evidence": [
      "row S145",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: read the three accounts' custody rows for the business date and state which; if unvalued, READY over it is the defect.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S174",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bd-securities carries firm provenance (222 inflection-origin, 941 COT-derived rows) that BD, 49F and INF gold load whole.",
    "evidence": [
      "row S174",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: leaves the path with the etf-classifications re-point (S173) and the disposal of the held COT-new write; stop writing firm_origin (classify_assets.py:353).",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S191",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Workstream ~E round 1: acceptance check E1-AC1 reads the source declaration by a bare firm key, and the commit-time naming gate (LGIC_ENFORCE DEC-6) refuses a bare registered firm token in a new authored JSON; the cell's S3 work is complete and only its commit is blocked.",
    "evidence": [
      "row S191",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1 (blocks the v0.19 thread's first commit): the naming limb admits a registered firm token as a KEY in an authored declaration, or lib/opal_naming.py generates sources.json, or an R20 entry Andrew acknowledges. Dispositioned here, ahead of ~E's own L8, because the row gate holds every new remediation row until this BLOCKING item is dispositioned.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S175",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A refused unknown Comparison key answers UNEXPECTED (MaintainedSourceRefused has no classifier mapping).",
    "evidence": [
      "row S175",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: map it to a named refusal code in generate.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S178",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lambda-source-map.json lags live on 5 IRPT functions; the intake poller serves a 07-22 firm registry.",
    "evidence": [
      "row S178",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: reconcile the map fields; decide whether the poller carries the current registry.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S180",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "One selection create answered HTTP 500 for a valid eleven-account scope.",
    "evidence": [
      "row S180",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: read the directory-search log group around 17:55Z for the stack.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S144",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The generate closure check walked first-party imports only.",
    "evidence": [
      "row S144",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: record CTO 101230's condition 3 (every generate module imports on the deployed function) as met, or state what fails.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S119",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The JS session bundle and the Python resident's bundle contract differ (schema_version, capture_origin, generation, identity).",
    "evidence": [
      "row S119",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: confirm the contract gap is closed on the served resident, or cut it; S151's silent capture failure may be this seam.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S121",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The YCharts runner's offline suite is offline only when preloaded; unguarded, its control reached the vendor once.",
    "evidence": [
      "row S121",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: the suite refuses to start without the net guard.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S120",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The SSM deploy document installs Playwright browsers for root while the resident runs as ec2-user.",
    "evidence": [
      "row S120",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: fix the document (PLAYWRIGHT_BROWSERS_PATH=0 or an ec2-user install step) so a redeploy does not reintroduce it.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S118",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "record-terraform-deploy.sh hands a .js CHANGELOG file to python3 wherever its hardcoded bun path is absent, silently skipping the CHANGELOG.",
    "evidence": [
      "row S118",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: pick the interpreter per consumer; the device path breaches CLAUDE.md's derive-do-not-hardcode rule.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S124",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The bundle mint reads working-tree bytes while loose deploys read the index, so an autocrlf checkout mints CRLF copies.",
    "evidence": [
      "row S124",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: build_bundle_payload reads the index blob, or the members carry eol=lf.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S141",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The push-time deploy gate deploys every changed gold script, so a code-only grant holds only until the next CLOUD push.",
    "evidence": [
      "row S141",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: the deploy gate honours a declared code-only grant, or grants stop being scoped code-only.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W42-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two top-level lib packages collide in the investor_reporting test run (14 INF tests fail on lib.silver_ids).",
    "evidence": [
      "row W42-S3",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: pop the sys.path insert in test_bundle_manifest_stamp.py, or import by file path.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S129",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S125's directory refresh fix, remedied and exercised: the 09-25 13:30Z fire dispatched at all three firms and the served directories moved off 2026-09-17.",
    "evidence": [
      "row S129 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S136",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S135 disarmed: ~P's schedule fix (86a3d27224) is on CLOUD at afefa09d7e; a plan of the directory root from CLOUD no longer changes the refresh (read again by this seat: schedule.tf cron(30 9 ...)).",
    "evidence": [
      "row S136 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S137",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S131/S134 remedied: a full-firm COT build screens each account (holdings_snapshot.cot_screen_accounts, ce64116275, on CLOUD since de042e1e4b) and refuses the account, never the firm.",
    "evidence": [
      "row S137 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S150",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Window-6 branch (e) was false; graduated into CTO ruling 101673 as a standing rule: a window's delete leg runs only after every job it started reads terminal.",
    "evidence": [
      "row S150 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "1.0.0_SA_CTO",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S159",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The first READY Analysis report's level basis (custom_date, Sunday-dated sections) is closed by CTO 102024 (S163): the vendor's printed 'Data as of' line is R10's label.",
    "evidence": [
      "row S159 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S160",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Recipe-side diagnosis of S159, graduated under CTO 102021 (S162).",
    "evidence": [
      "row S160 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S161",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The CTO 101971 discriminator answered from the advisor's own HAR, no vendor call; graduated under CTO 102021 (S162).",
    "evidence": [
      "row S161 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S162",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CTO 102021 recorded: W15-3 stays Static-only as built (Y @36837771d6); the approved vendor GET withdrawn unspent.",
    "evidence": [
      "row S162 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S163",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CTO 102024 closes S159: R10 applied to Analysis sections (labelled, never silent); no certifier change.",
    "evidence": [
      "row S163 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S164",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-IB-s158's false premise (the box keeps no session-fetch logs): SSM document version 5 uploads the wrapper log on the failure branch. Its failure branch is not yet exercised (S168).",
    "evidence": [
      "row S164 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "0.6.2_AE_PartnerETL~S",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.6.2_AE_PartnerETL~S",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S167",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A tree order's flat proof_of_spec path cannot satisfy the complete-flip gate; this instance was moved to the gate's path. The class is carried open by W42-S4.",
    "evidence": [
      "row S167 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "0.6.2_AE_PartnerETL~S",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.6.2_AE_PartnerETL~S",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S168",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seat corrected its own record: the 09-28 scheduled run does not exercise the log-on-failure branch (Lever A skips a young capture).",
    "evidence": [
      "row S168 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "0.6.2_AE_PartnerETL~S",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.6.2_AE_PartnerETL~S",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S169",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S158 disarmed: the refreshed COT session (AWSCURRENT 9da4e781) served a signed use's 2 BD requests and retained a report.",
    "evidence": [
      "row S169 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S170",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S157 resolved on real data: corrected COT report RPT-12b885b8 states 2026-07-21..2026-09-21, its series starting 07-21.",
    "evidence": [
      "row S170 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S171",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The one-use plan tool's default approval_ref cited a spent word; cot_one_use_plan.py now requires --approval-ref (measured).",
    "evidence": [
      "row S171 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S172",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A Git-Bash aws ssm delete-parameter with a slashed name was path-converted, so K1-CRED lived until 21:12:46Z; the seat deletes and proves absence through boto3 from now.",
    "evidence": [
      "row S172 (GRADUATED by its author; no remediation row existed)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "Applied as the row records; written closed at round 19's L9 so the graduated item carries its remediation row.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v19",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v19"
    },
    "closed": true
  }
]
```
