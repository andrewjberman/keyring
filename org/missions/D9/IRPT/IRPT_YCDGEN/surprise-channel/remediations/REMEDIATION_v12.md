# IRPT_YCDGEN: remediations, round 14

<sweep_watermark>2026-10-11T19:40Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:40:12Z. Input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/ROUND14_DRAIN_END_READ_20261011.md @8e099e4110 (msg 5670)`.
Graduated, round label v15: 2 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **FWD-1 is not met and nothing this project can build stands in front of it** (the issuer's reading). The fifth run's one sign-in
   was answered by a firewall challenge on its probe; the vendor path is stopped and the question is with Andrew.
2. **Row D2-W7-S1 is closed:** the builder's filter takes the logo's ending. Read by this seat in the code; its 31 tests pass on this
   seat's run. Not run by this seat: a research build.
3. **Three rows stay ARMED, owner `2.0.0_SA_COO~G2`:** S16 (waits on one accepted submission made by a browser), D2-S38, D2-S45.
4. **Row D2-S60** is the finding NFRA_OPSWKF FWD-8 now carries for one of the five functions. The other four have no owner yet.
5. The source map is stale for the generate function (the issuer's note; not filed as a row by it or by this seat).
6. st32's stamp on a job that fails five deliveries is unexercised; the rollback has run on copies only.

```json
[
 {
  "id": "IRPT_YCDGEN-D2-S60",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Five functions behind the portal authorizer serve any verified token without examining the caller, one of them creating a trade submission: a service token opens more than the one door its pair named",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S60",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/ROUND14_DRAIN_END_READ_20261011.md @8e099e4110 (msg 5670)"
  ],
  "remedy": "The trade dashboard service's eight routes are fixed under NFRA_OPSWKF FWD-8 (PRD v0.6, signed). The four other functions are read and each gets its own line or owner, as that PRD's addendum says.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v15"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S61",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The receipt check's CHECK VERDICT reads FOUND on 33 KEY-NAME matches of which 8 are FALSE POSITIVES -- its token pattern hits the probe pair's own with_token_/without_token_ arms -- so the count overstates the concern AND hides 8 diagnostic values; the three counts that would have meant a real leak all read 0",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S61",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/ROUND14_DRAIN_END_READ_20261011.md @8e099e4110 (msg 5670)"
  ],
  "remedy": "The receipt check's token pattern is narrowed so the probe pair's own two arm names do not match, and its verdict reads on values, not on key names alone.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v15"
  },
  "closed": false
 }
]
```
