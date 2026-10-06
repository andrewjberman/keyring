# ETFS_RIVALS -- round 2 remediations (site-Z fabric): the L10 slug

<sweep_watermark>2026-10-01T05:09Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01. Graduated at round 2's L9 (`adjudications/ADJUDICATION_v2.Z.md`). Eight items. One is still ARMED (W2-S4). Round 1's eight (REMEDIATION_v1.Z.md) stay OPEN beside these. The slug goes to 1.0.0_SA_CTO~Z for the round-2 analysis.

```json
[
  {
    "id": "ETFS_RIVALS-Z-W2-S4",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "silver_issuer._capture_id compares capture ids as strings. The issuer collector's key now starts with the requested date ('2026-...-<ts>-<sha>'), and '-' sorts below '0'-'9', so a new-format capture loses to any old-format ('<ts>-<sha>') silver of the same report date. A re-capture of a landed BASG report date keeps the OLD rows silently.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W2-S4 (0.9.0_WK_ETFS_RIVALS~2)",
      "this seat's list-objects-v2 of opal-data-etfs issuer-site/etfs/silver/holdings/ ~05:4xZ: 325 objects, 325 report dates, 325 old-format, 0 new-format (matches the packet's 05:1xZ measure)",
      "DRAIN_END_READ_ROUND2.md:58 and :67: not disarmed; the remedy is a live-Lambda code change, the first cell of round 3",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Order issuer silver by the capture's embedded UTC timestamp (strip the requested-date segment in _capture_id), shipped to the live build-silver Lambda under a never-widen pair, with a re-capture of one landed date as the positive control.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~RV",
      "at": "2026-10-01T04:10:00Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S8",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "G1 has no home-producer reader: no silver address or schema exists for the home funds' own holdings, so IDVZ and PFOE read ABSENT on the served page while both are mapped home_producer (Andrew '1b').",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S8 (0.9.0_WK_ETFS_RIVALS~1)",
      "DRAIN_END_READ_ROUND2.md:28 (IDVZ is the home fund and is not read this round) and :70",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A home-producer reader cell: the address and schema of the home funds' holdings, read by G1, so each group shows its own fund beside its rivals.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S28",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "report_date_freshness has a PROVISIONAL threshold of 0 trading days. A one-day Bloomberg report lag marks WCMG, TSEL, ETFT and PCLG not-updated and withholds the batch's publish marker, so the served page reads 'not-updated' with 6 of 13 funds updated.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S28 (0.9.0_WK_ETFS_RIVALS~5)",
      "DRAIN_END_READ_ROUND2.md:30-31: manifest status not-updated, funds_total 13, funds_updated 6",
      "this seat's list of state/publish_page/: import-r2-00..07 present, import-r2-08 absent",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "FWD-9's cell sets report_date_freshness from measured per-source lag (Bloomberg-fallback funds report one trading day later by construction), together with round 1's W1-S5 contract line.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Gateway deploys from different seats have no mutual exclusion, and nothing checks that a release preserves the routes other projects serve. On 2026-09-30 a release cut on a stale base removed /rivalfunds for 42 minutes. The 2026-10-01 01:38Z NFRA_OPLGTW release kept it, but only because its tree carried the files by content: 4ce7946426 is not its ancestor.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S2 (2.0.0_SA_COO~RV); the mitigation today is a messaged instruction (msgs 27202/27203, 27333), not a mechanism",
      "this seat's SSM cbe1a6ef-1cfc-473b-a539-097ebb8e9f03: host server.py == d61fde4693, /rivalfunds 401; `git merge-base --is-ancestor 4ce7946426 d61fde4693` false",
      "round-1 rows W5-S16/S17 (the 42-minute loss and its repair)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (what you should have asked)"
    ],
    "remedy": "The CTO decides the mechanism: a deploy lease on opal-gateway (safe-ec2-deploy.sh, or the ledger's open entry as the lock), and/or a pre-deploy route diff that refuses a release removing a route a project outside the release serves. Proposal only; no gate is built without the CTO's ruling.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S11",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A G1 object's revision is '<greatest capture ts>-<hash of the input set>'. A later input set that adds a capture OLDER than the greatest ties on the timestamp, so 'greatest revision' is decided by hash order, not completeness.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S11 (0.9.0_WK_ETFS_RIVALS~1): 'it would need a revision scheme that orders by input-set completeness, which is a contract change for G1 and trade_schedule'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A revision contract for G1 and trade_schedule that orders by input-set completeness (or a generation counter). It is exercised before FWD-8's rebuild, which is the first act that can produce the tie.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S11",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Neither G3 nor G1 carries a dividend currency (G1 reads 'USD' on all 3260 rows, including JP and FP lines), and LN amounts come in mixed pence and dollars. G5 converts by exchange suffix and a 25% sanity bound, so income_funded rests on a heuristic.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W3-S11 (0.9.0_WK_ETFS_RIVALS~3): 'What closes it is a per-record currency in G3 (Bloomberg DVD_CRNCY beside DVD_HIST_ALL), a change to RIV-e-1's pull'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Add DVD_CRNCY to the pull-enrichment request, scripted under R-21, so G3 carries a per-record currency and G5 drops the suffix heuristic.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S12",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "G3 names only the parent of a spinoff, rights issue or warrant, so the child line a corporate action creates reads as a discretionary 'entry' trade, against the issuer's ruling that it is not a trade (16 of 4780 records).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W3-S12 (0.9.0_WK_ETFS_RIVALS~3)",
      "issuer amendment ef6e9eb88d (TO-RIV-g-4 amendment 1) rules spinoff/rights/Warrant SHARE-CHANGING: 'a new line from an entitlement is not a trade' -- the ruling the build cannot honour without a child identity",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A child-identity source for spinoff, rights and warrant actions (a Bloomberg field beyond DVD_HIST_ALL, or a maintained map), so G5 labels the child line CORP-ACTION rather than entry.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S21",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "collector_bloomberg.land_capture deduplicates by listing the acquisition partition and GETting every sidecar once per capture, so the product S3 sink is quadratic in the partition's object count. The import ran through a memoising sink object; the daily leg (one capture a day) is unaffected.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S21 (0.9.0_WK_ETFS_RIVALS~5): 'A future backfill mode over many days on the product sink has the same shape'",
      "DRAIN_END_READ_ROUND2.md:74",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Move the memoised sidecar index into the product sink (or key the dedup check on the sha) before any backfill or FWD-8 rebuild runs on the product path.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true
  }
]
```
