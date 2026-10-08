# NFRA_OPLGTW -- adjudication v21 (site Z): round 29 L8 -- r28 meets the CVO half's five conditions; 8 rows dispositioned (2 graduated, 6 dismissed)

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T22:29:59Z. Trigger: `2.0.0_SA_COO~O` msg 31438 (r28 `aa75078e1b` live since 21:49:10Z,
round 29 terminal, drained @5db4581baf).

## The half's five conditions, read from the post-act records

| # | condition | read | result |
|---|---|---|---|
| 1 | live re-read first | the issuer's record; not re-read by me | taken |
| 2 | R45 before any criterion, with byte totals | 0 of 6,441 entries touched; 1,882,231,173 bytes and 115,217 files before and after | MET |
| 3 | the post-act record from installed code | no-`ts` key stamped; `ts` key shape unchanged; tools 66; scopes 9; refused id 0 requests | MET |
| 4 | host pip output kept whole | my own count in the kept output: 47 already satisfied, 0 Collecting, 0 Downloading | MET |
| 5 | no sign-in cache opened | the principal came from the issuer's off-repo file | MET |

**Not observed:** a real audit-lake key written by r28 for a record with no `ts`. The check called the key builder on
installed code and wrote nothing. Row Z-W28-S26 stays OPEN until such a key is read on the lake.

## Open after this round

- **Z-W28-S33, at the CTO:** whether a fully cached frozen install sends a metadata request. The cache control cannot
  see it; only a network-side read would decide it.
- **Z-W28-S26:** as above.
- **Z-S67, ARMED, at the issuer:** the r28 restart signed out the scoped concierge, the identity the 07:00
  America/New_York Bloomberg send depends on. It needs a sign-in by hand. The release form now names that cost; no
  code is changed.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S55",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T22:29:59Z",
  "one_line": "Round 29 L8: 2 rows GRADUATE OPEN -- the r28 restart revoked the scoped concierge's whole gateway session by the token-reuse rule, so a gateway deploy can sign out a connected client by timing (Z-S67, ARMED); and a clean R45 shows no package was written to bun's cache; it cannot show that no request left the box, so whether a fully cached frozen install sends a metadata request stays UNDETERMINED (Z-W28-S33).",
  "class": "OBSERVATION",
  "spec_asserts": "A real open question found in the round is graduated with a remediation row.",
  "world_is": "RL14_BUN_CACHE.json: 0 of 6,441 entries touched, 1,882,231,173 bytes and 115,217 files before and after, 0 download lines in the build span. The deploy output shows bun install ran after the pre-check passed. The control reads cache writes only. Andrew's word is about fetching from the internet; a metadata request is a request to the registry that fetches no package. Z-S67: the issuer's read-only scan of the refresh-token records shows 1 family revoked in the hour of r28 (reason refresh_token_reuse), 0 in the hours of r26 and r27, and another identity refreshing in the same minute left signed in; the opal-gateway-bbg connection refuses whoami and needs a sign-in by hand. The cause (a rotation committed while its answer was lost across the restart) is the issuer's INFERENCE; the records show the revocation, its reason and its minute. This seat did not re-run the scan.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-S67",
   "NFRA_OPLGTW-Z-W28-S33"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md rows Z-S67 and Z-W28-S33 (read whole by this seat)",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL14_BUN_CACHE.json"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S56",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T22:29:59Z",
  "one_line": "Round 29 L8: 6 rows DISMISSED_WITH_REASON -- three base-guard tests went red on the first release cut and pass on the re-cut (Z-W28-S27); rl14.AC1 counted two files that never reach the host and was amended before the GO (Z-W28-S28); the order's two sentences on the principal identifier (Z-W28-S29); the audit-lake read took 1,087 seconds (Z-W28-S30); the rehearsal record named the superseded sha (Z-W28-S31); a repo-root requirements.txt in a whole-repo diff (Z-W28-S32).",
  "class": "OBSERVATION",
  "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
  "world_is": "Z-W28-S27: fixed by OG-bi-4 in the re-cut aa75078e1b; test_deploy_base_guard.py passes in this seat's own run of the five files (25 passed). Z-W28-S28: the issuer re-grades rl14.AC1 PASS at 1 of 1 host file. Z-W28-S29: Phase B read the issuer's off-repo holder file, the source the release form's R41 names; no sign-in cache was opened. Z-W28-S30: the read it slowed is the rivalfunds acceptance, already read in Phase A (a record written 18:55:34Z keeps day and route with bytes); no later order repeats it. Z-W28-S31 and Z-W28-S32: worked past in the worker's own files; the gateway's requirements.txt is the same blob on both sides.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-W28-S27",
   "NFRA_OPLGTW-Z-W28-S28",
   "NFRA_OPLGTW-Z-W28-S29",
   "NFRA_OPLGTW-Z-W28-S30",
   "NFRA_OPLGTW-Z-W28-S31",
   "NFRA_OPLGTW-Z-W28-S32"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S27 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S28 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S29 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S30 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S31 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S32 (read whole by this seat)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each was resolved before the GO or inside the worker's own files, with no served consequence on r28. The four filed ARMED were check or order defects whose trigger was this release's own run, which has completed."
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S57",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T22:29:59Z",
  "one_line": "Round 29: the CVO half's five conditions for r28 (aa75078e1b on 510c8cfed2) are MET on the post-act records. Z-W28-S26 stays OPEN: no lake object has yet been written by installed r28 for a record with no ts.",
  "class": "OBSERVATION",
  "spec_asserts": "The CVO advances a remediation clock in place only on its own read of the post-act record.",
  "world_is": "RL14_READ.json (installed code, served_release aa75078e1b): a no-ts record's key has a non-empty time part and its day matches; a record with ts keeps its key shape; 0 records changed; tools 66; scoped scopes 9; 0 lake objects written by the check. RL14_FLOOR.json: refused ids make 0 requests (slash and dot); pages unchanged with equal LastModified; floor_ok and route_ok true. RL14_BUN_CACHE.json as in Z-C-S55. Host pip, counted by this seat in the kept deploy output: 47 lines already satisfied, 0 Collecting or Downloading. NOT observed: a real lake key from r28 for a no-ts record (the builder was called, nothing was written), and the rivalfunds lake record was not re-read in Phase B. A separate finding is at the issuer on the CTO's ask (msg 31440): the opal-gateway-bbg session lost its token at 21:49Z, the minute r28 went live.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL14_READ.json",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL14_FLOOR.json",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL14_BUN_CACHE.json",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r28c_phaseB_deploy.out (pip lines counted by this seat)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_NEVER_WIDEN_OG-rl-14_HALF_20261007.md conditions 1-5"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```
