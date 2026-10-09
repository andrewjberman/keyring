# ADVI_BILLING -- round 2 remediations

<sweep_watermark>2026-10-09T09:29Z</sweep_watermark>

Graduated at round 2's L8 (ADJUDICATION_v2.md), round label v3: 5 rows, OPEN. Round 1's W1-S6 closed in place (the edge book check, measured).

```json
[
  {
    "id": "ADVI_BILLING-D2-S4",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-3 graded NOT REALIZED on the real render (E4): of its ACCEPT, the value charged on, the schedule (flat, so no tiers), days, per-account and household steps, and the 'why' are shown on real data; but 'any adjustment for money moved in or out during the quarter' and 'anything left out' are shown only on the invented-data render. For household z08219260 the panel neither shows a flow or exclusion nor states there was none, and the one flow-like mechanism -- SMArtX's prior-quarter true-up under advance billing -- is printed as 'method not known to this round'. ABSENT is not EXERCISED-AGAINST.",
    "evidence": [
      "investigation row ADVI_BILLING-D2-S4",
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef"
    ],
    "remedy": "One real household's panel shows the flow adjustment (or states none) and what is left out (or states nothing), with the true-up read from a landed SMArtX statement; then FWD-3 is re-graded.",
    "owner": "2.0.0_SA_COO~B2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B2",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "ADVI_BILLING-D2-W4-S2",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served map is produced by the legacy D_00.portal_aggregates (z-id grammar, 191 advisors, generated today), not by d08; the d08 fix reaches the served map only at the cutover, and D_00 has the same universe law",
    "evidence": [
      "investigation row ADVI_BILLING-D2-W4-S2",
      "live map generated_at 2026-10-09T05:27Z, 191 advisors, relationship ids z-form; d08 produces rel_ hash ids and 149 advisors on the same day's inputs"
    ],
    "remedy": "Rule whether the served ownership map is regenerated now under a pair, or the d08 fix waits for its cutover from the legacy D_00 writer (the issuer recommends the latter).",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "ADVI_BILLING-D2-S3",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "other_firm (firmId mockadv, role user, firmRole user, and no advisorId, exactly as the order specifies the class) returned 403 'Advisor scoping: missing identity claims' -- index.mjs:478-492, failure mode 1, which runs BEFORE getOwnershipMap resolves a firm to a bucket. The status met the stated expectation (401 or 403) while exercising the identity-gap arm, not cross-firm containment.",
    "evidence": [
      "investigation row ADVI_BILLING-D2-S3",
      "AB_E1_PROBES.json probes[3]: status 403, error_head {\"error\":\"Advisor scoping: missing identity claims\"}"
    ],
    "remedy": "Exercise the CROSS-FIRM arm: a probe with complete claims for another firm's mapped advisor, refused at firm resolution (today's 403 is at 'missing identity claims', before it).",
    "owner": "2.0.0_SA_COO~B2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B2",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "ADVI_BILLING-D2-W3-S2",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AB-e-6 item 3 saves the dry-run object (client figures) to .scratch/advi_billing/AB_E6_DRYRUN.json 'in the worktree root (gitignored)', but git check-ignore on that path prints nothing and git status lists .scratch/ as untracked, so only the explicit-path commits keep it out of history.",
    "evidence": [
      "investigation row ADVI_BILLING-D2-W3-S2",
      "git check-ignore -v .scratch/advi_billing/AB_E6_DRYRUN.json -> no output (rc 1) in C:/dev/wk-advi-billing-3"
    ],
    "remedy": "Make .scratch/ ignored (gitignore) or move client-figure scratch outside the checkout, so no broad add can stage client data.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "ADVI_BILLING-D2-W3-S3",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AB-e-6 says each account's ADVISOR and PLATFORM rates come from the silver statement 'summed over the account's allocations'; rates are fractions that do not add across sleeves, so fee_quarter.smartx_by_account value-weights rates by Current Period Estimate Valuation and sums only the true-ups, and it defines the PLATFORM rate as UMA + APM + Model rate (Client Fee Rate unused) -- neither is tested against a real statement.",
    "evidence": [
      "investigation row ADVI_BILLING-D2-W3-S3",
      "data/assets/scripts/gold/advi_billing/fee_quarter.py @9492f23e7d smartx_by_account(); org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json 0.2.0 scope_note says the composition is an assumption"
    ],
    "remedy": "Test the value-weighted per-account rate (fee_quarter.smartx_by_account) against a real SMArtX statement before v2 is served.",
    "owner": "2.0.0_SA_COO~B2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B2",
      "round": "v3"
    },
    "closed": false
  }
]
```
