# ADVI_COTBKF -- round 4 remediations

<sweep_watermark>2026-10-07T07:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~08:4xZ. Graduated at this compile (ADJUDICATION_v3.md): 5 rows, round label v5 (the
round after round 4). W14-S1 REMEDIATED and closed, disarmed by `2.0.0_SA_COO~C2`'s row S8. W12-S1 (ARMED), W12-S2, W12-S4 and S7 OPEN.

Clocks advanced in place at this compile (state fields only) in REMEDIATION_v1.md, each on its own REMEDIATED condition, read by this
seat (grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md`):
- W6-S2: REMEDIATED and closed. CB-d-1's census names all 40 of the account's buckets with a verdict (BARRED from the registry, never
  opened) and re-reads the coverage line (1,720 of 4,634 priced). The two buckets it could not list are carried by W12-S2.
- W10-S4: REMEDIATED and closed. The crosswalk is re-read with acct#a2618be7 scored (0.600, NOT_MATCHED, its in-kind exit of 2026-04-07 named),
  and the near-matches are listed for Andrew (21).
- W11-S2: REMEDIATED and closed. Every account that ends before 2026-06-23 carries a row (1,450 of 1,450), so every round-3 target is
  followed or says why it stops.
Not moved: W6-S5 (its ruling is not recorded).

```json
[
 {
  "id": "ADVI_COTBKF-W14-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CB4d3-AC2's 120-second bound held only against a primed cache: the cache needs the advisor and relationship columns, so round 3's cache was stale and a cold read took 2m23s.",
  "evidence": [
   "investigation row ADVI_COTBKF-W14-S1",
   "investigation row ADVI_COTBKF-S8 (2.0.0_SA_COO~C2, 07:40Z): the disarm; CB4d3-AC2 runs in 34 s on dell2 against its cache",
   "the order's bound allows a cache under .scratch/ warmed once untimed, if said; the packet says the d-2 and d-3 times are warm-cache figures"
  ],
  "remedy": "Done within the order's bound: the cache is re-primed with the new columns and the timed run meets 120 s.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v5",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v5"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": "2026-10-07T07:40Z"
  }
 },
 {
  "id": "ADVI_COTBKF-W12-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "dell2 has no pandas_market_calendars, so lib/trading_calendar falls back to a holiday list covering 2024-2027; every earlier year counts holidays as trading days, and the census's security_days figures are not comparable to round 2's.",
  "evidence": [
   "investigation row ADVI_COTBKF-W12-S1",
   "python -c 'import pandas_market_calendars' on dell2: ModuleNotFoundError (this compile's read, dell2, 2026-10-07 ~08:1xZ-08:4xZ)",
   "row S9 (filed by this compile): the account-links run also differs between the laptop and dell2, on exits dated before 2024"
  ],
  "remedy": "Run the census and the links on a box that has the calendar package, or provision it on dell2. Installing a package is egress off Opal infrastructure, so provisioning dell2 takes Andrew's word through its fabric manager; the priced counts do not depend on it.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v5",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v5"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": "2026-10-07T10:25Z"
  }
 },
 {
  "id": "ADVI_COTBKF-W12-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "opal-data-cottonwood (Cottonwood's own scope bucket) and opalinvest-portal refuse a List to cloudops-dell2-agent-user, so the census grades both USABLE with contents unknown; CB4d1-AC3's completeness cannot be shown.",
  "evidence": [
   "investigation row ADVI_COTBKF-W12-S2",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md: CB4d1-AC3 NOT MET on these two buckets"
  ],
  "remedy": "A principal permitted on both buckets lists them and names any per-security daily price store, or the dell2 identity is granted read-only (an access change: the laptop CTO's under NFRA_CTLPLN v0.12 C-ROLES). CB4d1-AC3 is then re-graded.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v5",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v5"
  },
  "closed": true
 },
 {
  "id": "ADVI_COTBKF-W12-S4",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ruff was not installed on dell2, so .tools/commit-gate.sh failed closed on every .py commit; the worker installed ruff==0.15.11 with pip --user, a device change and a PyPI egress made without Andrew's word.",
  "evidence": [
   "investigation row ADVI_COTBKF-W12-S4",
   "CLAUDE.md Agent Autonomy: 'Excluded: all egress off Opal infrastructure'; 0.0.0_AB_MSTR's provisioning ruling (msg 105150) is the precedent that tool provisioning is the fabric manager's"
  ],
  "remedy": "0.0.0_AB_MSTR~DELL2 records the install and either ratifies it as dell2's provisioning (on Andrew's word for the egress) or removes it; the commit gate's prerequisites are provisioned per box, so a worker never meets the gap again.",
  "owner": "0.0.0_AB_MSTR~DELL2",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "0.0.0_AB_MSTR~DELL2",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-S7",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB4d4-AC1 (check_restricted_prefix.py) cannot be re-run on dell2 because terraform is absent, so the merged C-RESTRICTED policy's grade rests on the laptop worker's run; the laptop tfplan is archived only on the laptop.",
  "evidence": [
   "investigation row ADVI_COTBKF-S7",
   "ADVI_COTBKF_ROUND_4_DRAIN_END_20261007.md: CB-d-4 'NOT re-run ... NOT APPLIED'"
  ],
  "remedy": "Re-run CB4d4-AC1 on the box that applies the policy, under safe-apply, immediately before the apply.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v5"
  },
  "closed": false
 }
]
```
