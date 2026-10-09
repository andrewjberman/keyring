# ADVI_COTBKF: remediations, round 27

<sweep_watermark>2026-10-09T04:44Z</sweep_watermark>

Graduated at round 27's L9 (ADJUDICATION_v21.md), round label v28: 5 rows, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W50-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The closes the chain reads are split-adjusted over their whole history while the quantity rebuilt from the rows is as traded, so a month before a split values the position at 1/k and a split day shows a ghost return (B3S605610 2025-11-17 +274.9% against a reported -2.67)",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W50-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/diff_trace.md section 'One traced month per cause': B3S605610 2025-11, NFLX 64110L106: 68 shares and a stored close of 111.22 on 2025-11-14 (10 times that, 1,112, as traded, if the 10-for-1 ratio holds), a QA row of +612 shares on 2025-11-17 (10-for-1), the stored close continuous across the day (115.42 -> 111.22 -> 110.29); the account value goes 24,498 -> 91,844; with the closes before the split scaled x10 the month is -2.5150 against reported -2.67 (D was +279.4650)"
  ],
  "remedy": "Value positions with as-traded closes from the store's own split history (or blank the day with its reason); re-grade the 59 split months.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v28",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v28"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W50-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "An li row that delivers shares can carry the cost basis as its Amount, so the flow the chain subtracts is below the value the shares add to the account and the day returns the difference (B3S793726 2025-11-20 +8.30%)",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W50-S2",
   "transactions cache (silver with Amount): B3S793726 2025-11-20 li GOOGL 02079K305 Quantity 50 Amount 5302.475; the day's close x 50 = 14,452.87; the day's value steps 99,206 -> 112,741 with flow 5,302.48 recorded, return +8.2991%"
  ],
  "remedy": "Value an in-kind li at the shares' value, not the booked cost basis, or blank the day with its reason.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v28",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v28"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W50-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On a dvr day the position's value steps twice, once by the reinvested shares and once by a close that rises by about the distribution per share instead of falling by it (RGY004120 2025-12-05 FCNTX +5.04% close, +42.5 shares)",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W50-S3",
   "transactions cache: RGY004120 2025-12-05 dvlt 1019.65 and dvr Quantity 42.539 of 316071109; the stored close 22.7407 (2025-12-04) -> 23.8867 (2025-12-05), 1.1460 a share against a distribution of about 1.09 a share; the day returns +9.74% (price +5.00, shares +4.74) and the month is 11.2855 against reported 1.65"
  ],
  "remedy": "On a dvr day, take the close that falls by the distribution, or blank the day with its reason; re-grade the 13 months.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v28",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v28"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W51-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-aa-2 weight rule has no stated value for a security with no purchase row (1,540 of 4,372 listed): this worker used the largest inbound amount (1,428), else weight 1.0 (112), with weight_basis printed per row; and the list holds 4,372 securities where the CRO's section 6 tier counts sum to 3,226",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W51-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.md (weight_basis: BUY 2832, INBOUND 1428, NONE 112; P1 2155, P2 195, P3 2022)"
  ],
  "remedy": "State the weight rule for a security with no purchase as the CRO's (or a ruled) rule, and reconcile 4,372 against the CRO's 3,226 by population; say whether money-market funds (e.g. FZAXX) belong on a price-need list.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v28",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v28"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S40",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 CB27aa1-AC3 NOT MET as written; CB27aa2-AC3 MET; CB27aa3-AC3 MET. CB27aa1-AC3 fails on 'nothing forced': REACH_CAP_PCT was moved 0.5 -> 1.0 after exploratory runs on the same 512 months (traced 70 -> 73, the worker's own disclosure), and the three months it admits include the ONLY flow_value month, so one of the three classes exists by a constant tuned on the outcome. The other two clauses hold (rule commit 4624627872 precedes the run; each class shown on a traced month's day values; 439 left untraced with what each cause leaves).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S40",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/ADVI_COTBKF.TO-CB-aa-1.trace-512.proof_of_spec.json controls.determinism ('the exploratory run before the reach cap moved from 0.5 to 1.0 gave traced=70')"
  ],
  "remedy": "CB27aa1-AC3: re-run the trace at the pre-registered 0.5 cap, or label the three months between 0.5 and 1.0 as traced at a post-hoc cap; flow_value counts as a class only on a month that reaches under a cap fixed before it was seen.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v28",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v28"
  },
  "closed": false
 }
]
```
