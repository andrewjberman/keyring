# IRPT_BCKEND -- project sweep 10 remediations

<sweep_watermark>2026-10-07T09:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07. Graduated at sweep 10's L9 (ADJUDICATION_v25.md), round label v62. 6 rows, all OPEN:
S348, S357 and W136-S1 close with the round-61 directory release; S352 (BLOCKING, ARMED) and S356 are the FWD-5 replay's, which no dell2
principal can run; W137-S1 is FWD-2's gated arms. W127-S1 (REMEDIATION_v20) is not moved: IB-pr-332's build passes the parity gate, but
no disarm row is filed yet.

```json
[
  {
    "id": "IRPT_BCKEND-S348",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The directory refresh writes its day manifest under the artifact's business date and rewrites it only on a completion it sees, so the 10-06 fires left 49F and INF at RUNNING and filed COT's result under _refresh/2026-09-22/.",
    "evidence": [
      "investigation row IRPT_BCKEND-S348",
      "IRPT_BCKEND_ROUND_61_P_DRAIN_END_20261007.md @0c3d443030: IB-pr-333 (E-P5, refresh manifest by dispatch date) drained @f2fa74df85, code only; the release and a driven fire wait on the directory release packet and its CTO half"
    ],
    "remedy": "Release IB-pr-333 and read one driven fire: each firm's _refresh/<dispatch date>/manifest.json ends READY (or FAILED with its reason), never under an older date.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v62"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S352",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The dell2 identity is refused on irpt/<firm>/platinum/holdings/current/manifest.json at all three firm buckets, so E-M1 (the FWD-5 replay on the served publication) cannot run from dell2.",
    "evidence": [
      "investigation row IRPT_BCKEND-S352",
      "row S352's reads, 08:4xZ: HeadObject 403 at 3 of 3 firm buckets; ListBucket explicit deny on opal-data-49financial; sts positive control"
    ],
    "remedy": "Either a permitted principal (a laptop seat) runs the read and delivers a FILE that 2.0.0_SA_COO~M2 files as a row, or the dell2 identity is admitted read-only: an access change, the laptop CTO's under NFRA_CTLPLN v0.12 C-ROLES, through the cross-firm guard.",
    "owner": "2.0.0_SA_COO~M2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M2",
      "round": "v62"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S356",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The laptop CVO's E-M1 reader run (@e9993e95fa) is not a FWD-5 grade: c2 asked for one Cottonwood account holding both SPYI and PSLV (0 exist; 29 hold either), and c3 looked for custody_totals in the dated manifest, which never carries them.",
    "evidence": [
      "investigation row IRPT_BCKEND-S356",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_20261007.md @e9993e95fa"
    ],
    "remedy": "The issuer's amended reader (c2 over every account holding either, each tied, denominator printed; c3 reads the platinum header and fails an absent field as ABSENT) is run once by a permitted principal; FWD-5 is graded on that run.",
    "owner": "2.0.0_SA_COO~M2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M2",
      "round": "v62"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W136-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "_authz/served.py BOUNDARY_REASONS has no DIRECTORY_OVER_AGE, so status_envelope (served.py:285) refuses it; the search's over-age answer is built by directory/expiry.fallback_answer instead (state STALE, actions RETRY and WAIT), and a caller branching on public_reason_code sees the expiry envelope's code, not the boundary's.",
    "evidence": [
      "investigation row IRPT_BCKEND-W136-S1",
      "infra/aws/lambda/investor-reporting/_authz/served.py:285-286 @da25f92f4c; directory/expiry.py REASON_CODES and fallback_answer"
    ],
    "remedy": "Before the directory release: the portal search consumer is read for how it branches on the over-age answer, or DIRECTORY_OVER_AGE joins BOUNDARY_REASONS in an _authz cell.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v62"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W137-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The FWD-2 replay over 21 live routes drives the advisor, revoked-grant and no-protected-field arms through the route on only 6; 15, 15 and 17 arms are GATED for want of an operation-shaped fixture per route (a server-issued selection, a receipt with an artifact, a jobs-store item).",
    "evidence": [
      "investigation row IRPT_BCKEND-W137-S1",
      "deliverables/0.9.0_WK_IRPT_BCKEND~137/IB61-7_replay_output.json: advisor_principal DRIVEN-PASS 6 / GATED 15; revoked_grant_warm_cache 6 / 15; negative_no_protected_field 4 / 17",
      "IRPT_BCKEND_ROUND_61_P_DRAIN_END_20261007.md @0c3d443030: authenticated and advisor arms are GATED (no test principal; Andrew's to name, analysis section 6 item 2); FWD-2 NOT realized by this run"
    ],
    "remedy": "One fixture per gated route, and the test principal Andrew names; FWD-2 is graded on the run that drives every arm.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v62"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S357",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "irpt-directory-refresh runs a handler.py older than its recorded deploy commit (live blob 48313e9c0e of 2026-09-11; map says daed4433b4), so the next refresh release also ships the two 09-26 UIR-07 handler commits as riders.",
    "evidence": [
      "investigation row IRPT_BCKEND-S357",
      "row S357's release census at b9411881a0: handler.py built 3865775e75f8, live e46922a00379; changed_members 2"
    ],
    "remedy": "The round-61 directory release packet names the UIR-07 riders for its CTO half and corrects the deploy record at its close.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v62"
    },
    "closed": false
  }
]
```
