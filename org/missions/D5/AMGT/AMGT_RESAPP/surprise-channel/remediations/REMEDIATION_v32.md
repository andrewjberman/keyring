# AMGT_RESAPP -- round 86 remediations (dell1)

<sweep_watermark>2026-10-09T18:31Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T18:31:00Z. Graduated at ADJUDICATION_v104: 8 rows, all INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S29",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NU's served company_description is one Item 4.B sentence that reports Colombia launch results rather than describing the business, and the served section's own description_verdict_state is FAILED ('no served D-1 company_description sentence passing the describes-the-business test') while it still serves that sentence.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S29"
    ],
    "remedy": "Serve only sentences that pass the describes-the-business test (empty with the stated reason otherwise), or have the page withhold a FAILED section as a description. Close when: NU's served card is a sentence that says what Nu does or the honest empty state, and no served section reads FAILED while showing a sentence",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W345-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "drafting/schema.json pins sentence.generated to const true, so a served sentence that is the filing's own text still reads generated true (NU's description sentence serves generated true with verbatim_check PASS); the substitution is marked only by quote_method/served_from.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W345-S2",
      "3.0.0_SA_CVO served read of NU's section: generated true on a verbatim filing sentence"
    ],
    "remedy": "Let the schema carry generated false (or a distinct value) for a filing sentence served as written. Close when: a served filing sentence reads not-generated and the schema test pins it",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-S2",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "owned-paths-validate.py's 'task order is the grant' clause is keyed to the worker serial pattern, so a non-worker seat (0.7.0_AE_CloudOps~AMG) whose order declares lib/ paths is refused as BASE_EXEC.",
    "evidence": [
      "investigation row AMGT_RESAPP-S2"
    ],
    "remedy": "Give a non-worker seat's declared order paths a route, or rule that such acts go through a worker. Close when: an AE order's declared lib/ path commits through the gate, or the ruling is recorded",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S18",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GET /api/scoped/amgt/watchlist never reads selected_tenant (scoped_amgt.py takes the firm from the edge header only), so an off-list selector is answered rather than refused as the other scoped routes do. Not a leak: the answer is the caller's own firm's data.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S18",
      "3.0.0_SA_CVO direct invoke (no authorizer context, x-firm-id opal): /watchlist with an off-list selected_tenant 200 '[]', and /security/NU_US_Equity/thesis also 200 -- a direct invoke cannot reproduce the refusal path, so the row's code reading stands as the evidence"
    ],
    "remedy": "The watchlist route refuses an off-list selected_tenant like the other scoped routes. Close when: an off-list selector through the edge reads the refusal on /watchlist and the caller's own list without one",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND88_MM4_CTO_HALF.md@c2b5454449 ADDENDUM 1 and 1.0.0_SA_CTO~DELL1 msg 3185 (D1-S18 dismissed at the round-88 analysis): the watchlist selector has one branch by spec; mm-3 (a) stopped under its STOP clause (row D1-W350-S1); closed at ADJUDICATION_v108"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-S3",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/research/corpus/library.py _resolve_root returns the FIRST candidate that is a directory, so a SET but nonexistent OPAL_RESEARCH_LIBRARY_ROOT is skipped silently and the next candidate (OneDrive) is read.",
    "evidence": [
      "investigation row AMGT_RESAPP-S3",
      "3.0.0_SA_CVO read library.py:41-72 (_candidates puts the env root first; _resolve_root skips any non-directory)"
    ],
    "remedy": "A set override that is not a directory refuses with its path named. Close when: a bogus OPAL_RESEARCH_LIBRARY_ROOT raises and the unset case still derives",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S14",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Peer-set prices (and 992 HK's subject EV) are served with no price_currency, so the Security Analysis peer table prints 'currency not stated' on most peer rows.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S14",
      "DSGN_AMGTV1 round-68 walk shots 011/042 (tmp/ui-walk/20261009T164047Z): 'currency not stated' on 10-11 of 12 peer price cells"
    ],
    "remedy": "Serve price_currency for each peer price. Close when: the peer table's price cells carry a currency on a walked name",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S15",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The peer set serves the subject's market_cap_musd 541,932 as of 2026-09-19 for ASML_NA_Equity, stale and on a different basis against the header's CUR_MKT_CAP; the page no longer shows it (the subject row reads the header).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S15"
    ],
    "remedy": "Refresh or drop the peer set's own subject cap. Close when: the served subject cap matches the header's vintage or is absent",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S16",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Most served peers are identity UNRESOLVED and non-US listings carry a SEDOL or an exchange number in ticker where an exchange ticker exists (Tencent 'BMMV2K' vs 700 HK).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S16"
    ],
    "remedy": "Serve resolved identity with exchange tickers for peers. Close when: Tencent and SK hynix serve their exchange tickers",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v87",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v87"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```
