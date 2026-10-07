# NFRA_OPLGTW -- adjudication v19 (site Z): round 27 L8 -- r27 meets the CVO half's four conditions; 7 rows dispositioned (4 graduated, 3 dismissed); three clocks advanced

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T17:49:35Z. Trigger: `2.0.0_SA_COO~O` msg 31227 (r27 `510c8cfed2` live since 16:57:30Z,
round 27 terminal, drained @1b0575f0ba).

## The half's four conditions, read from the post-act records

| # | condition | read | result |
|---|---|---|---|
| 1 | live re-read first | `r27_phaseB_before_read.out`: MODE=before_feddb372443 | MET |
| 2 | audit keys, status date, refused id, tools, consent | page `day, route`; chart `day, fund, route`; other args kept 0; bytes 1,286,540 = page served; `displayed_date` filled; refused id 0 requests; tools 66; scopes 9 | MET |
| 3 | `LastModified` at both reads | four page objects, equal at 16:54Z and 16:58Z | MET |
| 4 | no second cache read | principal `source=issuer-off-repo-file` | MET |

**Not observed:** a rivalfunds record in the S3 audit lake. 53 objects were read at 17:05Z and none is a
rivalfunds view yet. The new keys are shown from installed code, which is what the half asked; the first stored
record is still to be read.

## Clocks advanced in place

- **Z-S64** (the audit record could not say which page was served): REMEDIATED.
- **Z-W28-S13** (the status tool's date read null): REMEDIATED.
- **Z-W28-S19** (the manifest note outgrew the naming gate): DISARMED and REMEDIATED. The note is 2,038 characters.

## New this round

- **Z-W28-S24, to the CTO:** the deploy script runs `bun install` on every gateway deploy. The issuer recommends no
  further gateway deploy from site Z until that line is ruled; I agree.
- **Z-W28-S21 stays ARMED** at the issuer until the release form carries the page-time read.
- **Z-W28-S20:** the form should name where the wrapper exercise's principal key comes from, and that it is never
  the sign-in cache.
- **Z-W28-S26:** one audit-lake key with an empty timestamp; cause unread.

`comp-surprise --armed --project NFRA_OPLGTW` after this file should read 1 (Z-W28-S21).

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S51",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T17:49:35Z",
  "one_line": "Round 27 L8: 4 rows GRADUATE OPEN -- the gateway deploy script runs bun install (77 packages) on every deploy, after Andrew's no-fetch word (Z-W28-S24); the route arms cannot tell a page republish from a route change and the release form does not yet carry the page-time read r27 used (Z-W28-S21, ARMED); the wrapper exercise's principal key has no named source in the form (Z-W28-S20); one audit-lake object has an empty timestamp in its key (Z-W28-S26).",
  "class": "OBSERVATION",
  "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
  "world_is": "Z-W28-S24: r27_phaseB_deploy.out shows deploy-to-ec2.sh building the dashboard bundle with bun and reporting 77 packages installed; whether they came from the registry or a local cache is unmeasured; r25 and r26 did the same. Z-W28-S21: r27 printed each page object's LastModified at BEFORE (16:54Z) and AFTER (16:58Z) and they are equal, so no republish crossed this deploy; RELEASE_ORDER_FORM.md @0f1f16a511 carries no such step, so r28 inherits the hazard. Z-W28-S20: Phase A learned the concierge's key by decrypting three principals' sign-in caches in memory; Phase B read it from an issuer off-repo file (R27_PRINCIPAL source=issuer-off-repo-file) and did not open the cache; the form names neither source. Z-W28-S26: audit/dt=2026-10-07/-321b3117.jsonl, written 13:31:24Z, cause not read, object not opened.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-W28-S24",
   "NFRA_OPLGTW-Z-W28-S21",
   "NFRA_OPLGTW-Z-W28-S20",
   "NFRA_OPLGTW-Z-W28-S26"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md rows Z-W28-S20, S21, S24, S26 (read whole by this seat)",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r27_phaseB_read.out lines 8-12",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r27_pagetime_before_2.out and r27_pagetime_after_1.out",
    "deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md @0f1f16a511 (no LastModified step, no principal source)"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S52",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T17:49:35Z",
  "one_line": "Round 27 L8: 3 rows DISMISSED_WITH_REASON -- the r26 BEFORE arm asserted the pre-r26 state and was adapted (Z-W28-S22); the worker worktree's sparse cone lacked org/devices and the worker added it (Z-W28-S23); a bare '/' argument and one --query form fail through bash on this device and the worker's scripts avoid both (Z-W28-S25).",
  "class": "OBSERVATION",
  "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
  "world_is": "Each of the three was met and worked past inside the worker's own files with no served-output consequence; none names a defect in a shipped file.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-W28-S22",
   "NFRA_OPLGTW-Z-W28-S23",
   "NFRA_OPLGTW-Z-W28-S25"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S22 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S23 (read whole by this seat)",
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S25 (read whole by this seat)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Mechanical and fixed in place by the worker. Z-W28-S23's advice (cut worker worktrees with org/devices in the sparse cone) and Z-W28-S25's (rc 3221225477 with empty stderr is a crash of the shim, not a list failure) are carried to the issuer in the slug; neither needs a remediation clock."
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S53",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T17:49:35Z",
  "one_line": "Round 27: the CVO half's four conditions for r27 (510c8cfed2 on feddb37244) are MET on the post-act records, and three clocks advance in place -- Z-S64 REMEDIATED, Z-W28-S13 REMEDIATED, Z-W28-S19 DISARMED and REMEDIATED.",
  "class": "OBSERVATION",
  "spec_asserts": "The CVO advances remediation clocks in place only on its own read of the post-act record.",
  "world_is": "RL13_READ.json (installed code, served_release 510c8cfed2): page records keep day and route, the chart record day, fund and route, audit_other_args_kept 0, bytes on the record 1,286,540 equal to the page served; displayed_date 2026-10-07T11:08:40Z equals the manifest's generated_at; tools 66; scoped scopes 9. RL13_FLOOR.json: a refused id makes 0 requests (slash and dot); day and audit pages unchanged with equal LastModified at both reads; floor_ok and route_ok true. The sign-in cache was not opened in Phase B. EC2_MANIFEST.json release_note is 2,038 characters and holds r27's note only, and the form carries that rule. NOT observed: a rivalfunds record in the S3 audit lake (53 objects read at 17:05Z, none yet), so the new keys are shown from installed code and not yet from a stored lake object.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL13_READ.json",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL13_FLOOR.json",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r27_phaseB_read.out",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r27_lake_read.out",
    "infra/aws/ec2/EC2_MANIFEST.json services/opal-gateway/release_note (2,038 characters, measured by this seat)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_NEVER_WIDEN_OG-rl-13_HALF_20261007.md conditions 1-4"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```
