# NFRA_OPLGTW -- adjudication v17 (site Z): the L8 of rounds 25 and 26 (OG-al-2, OG-up-2, the r26 release OG-rl-12; OG-au-2, OG-sd-1)

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T15:00:00Z. Trigger: `2.0.0_SA_COO~O` msg 31057 (rounds 25 and 26 TERMINAL,
5 of 5 complete). This seat compiles on `1.0.0_SA_CTO~Z`'s ruling msg 30783; the slug's one send goes to
`1.0.0_SA_CTO~Z`.

**Terminality.** All 5 orders read `<status>complete</status>` (round 25: 3; round 26: 2). Neither round carries a
judgment criterion, so there is no L9 grade. This seat re-ran the 9 checks at CLOUD @c14b3240e1, 14:5xZ:
- PASS, 8 of 9: al2.AC1 (4 of 4), al2.AC2 (1 row added, 0 removed), al2.AC3 (2 of 2), up2.AC1 (4 of 4), up2.AC2 (5 of
  5 files), rl12.AC2 (the concierge admitted for the status tool on the served release, ssm Success), au2.AC1 (4 of
  4), sd1.AC1 (3 of 3).
- FAIL on re-run, 1 of 9: rl12.AC1, on its live..CLOUD conjunct alone ("gateway files differing 5"). Every other
  conjunct holds: deployed feddb37244 descends from 240ac2fe5a; host shipped files equal the release bytes 5 of 5;
  ledger entry 1, sentinel gone; floor yes/yes. The 5 files are round 26's two cells, built and not released
  (`git diff --name-only feddb37244 HEAD`: 6 with the runbook). Same instrument property as v16's C-S46.

**The r26 release against the CVO half** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_NEVER_WIDEN_OG-rl-12_HALF_20261007.md`
@d293c39967). Condition 2 named six post-act reads from the installed code. `RL12_ALLOW.json` and `RL12_FLOOR.json`
(served_release feddb37244, `installed_code` true), read by this seat:

| condition | read |
|---|---|
| the concierge admitted for the status tool | `status_tool_allowed_for_scoped` true |
| 0 unnamed tools admitted | `unnamed_tool_allowed_for_scoped` false |
| consent 9, tools 66 | 9 and 66; overlay rows 1 to 2; grants written 0 |
| a refused id makes 0 requests | a slash id and a dot id each refused, `http_requests` 0; the known execution read SUCCEEDED |
| the four route arms | chart_404 with its body, chart_400, day page 200, audit page 200, each `ok` true |
| nothing else | real holder 2150 / 2150 / 2150 / 0 on both paths; portal login OK |

All met. The day page's size in the post-act record (1,298,076 bytes) differs from the rehearsal's (1,279,784); the
arm compares before and after the act, so I read that as the page having been re-published in between, and did not
verify it.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 393 investigation items, 90 remediation rows; 7
OPEN, 2 ARMED. This file adjudicates the 7:
- **GRADUATED (6), C-S47:** Z-W28-S17, Z-W28-S18, Z-W28-S16, Z-S66 (to the CTO); Z-W28-S14, Z-W28-S19 (to the issuer).
- **DISMISSED_WITH_REASON (1), C-S48:** Z-W28-S15.
- **C-S49** records the in-place advance of Z-S65 to REMEDIATED and the state of the v11 rows.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S47",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T15:00:00Z",
  "one_line": "Rounds 25-26 L8: 6 rows GRADUATE OPEN -- a Schwab master account id sits in 52 committed files of this project's deliverables (Z-W28-S17) and the AWS account id in saved deploy output (Z-W28-S18); a forced head move in a linked worktree leaves no audit record (Z-W28-S16); two drains raced in the shared tree and one commit took one seat's message and the other seat's tree (Z-S66, ARMED); the rehearsal runner stages only app/ and deploy/ files (Z-W28-S14); the manifest's release note outgrew the naming gate's argument length (Z-W28-S19, ARMED).",
  "class": "OBSERVATION",
  "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
  "world_is": "Z-W28-S17: the host's real-holder body prints a Schwab master account id; the worker counted 254 matches in 52 files under this project's deliverables, 21 of them its own older files, and redacted only the r26 outputs. Those files are in git history, and site-Z's commits to fad25b1527 were pushed to origin today. Z-W28-S18: the deploy scripts echo the artifact bucket name, which embeds the 12-digit AWS account id; r25's saved output carries it 4 times. Z-W28-S16: FORCE_HEADMOVE=1 in a linked worktree under /c/tmp printed that it could not resolve the audit log, so the override is unrecorded while the guard's text says it is logged. Z-S66: commit 9f146f853a carries 2.0.0_SA_COO~X's subject and branch parent, 2.0.0_SA_COO~O as author and OG-au-2's tree; safe-merge detected it after the commit and printed the repair to the seat whose content landed. Z-W28-S14: a release that ships a gateway-root file other than the allowlist is rehearsed on the installed copy of it. Z-W28-S19: the cumulative release_note passed 32,000 characters and the naming gate's `git cat-file -e HEAD:<value>` failed with WinError 206; three old segments were trimmed by hand, so r27 hits it again.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-W28-S17",
   "NFRA_OPLGTW-Z-W28-S18",
   "NFRA_OPLGTW-Z-W28-S16",
   "NFRA_OPLGTW-Z-S66",
   "NFRA_OPLGTW-Z-W28-S14",
   "NFRA_OPLGTW-Z-W28-S19"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md, the 6 rows named in adjudicates (each read by this seat: one-line, spec, world, notes and evidence)",
    "this seat's own commits today met index.lock collisions twice in the shared tree (14:22Z and 14:27Z, rc=128), consistent with several seats committing at once; it did not observe Z-S66's race itself",
    "1.0.0_SA_CTO~O's open row Z-S61 (remediations/REMEDIATION_v10.md): an earlier drain that left the shared index at the pre-drain tree"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S48",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T15:00:00Z",
  "one_line": "Rounds 25-26 L8: Z-W28-S15 is DISMISSED_WITH_REASON -- the bare ref CLOUD reading a different commit than refs/heads/CLOUD was not reproduced, no second ref of that name exists, and no release proof uses the bare name.",
  "class": "OBSERVATION",
  "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
  "world_is": "The worker's re-read gave the same commit for both names twice and found 0 other refs named CLOUD. Its candidate cause, the branch advancing between two reads, is unmeasured. Every r26 measurement names refs/heads/CLOUD.",
  "adjudicates": [
   "NFRA_OPLGTW-Z-W28-S15"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S15 (read whole by this seat)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Not reproduced, with a control (no second ref) and no proof depending on it. The row's advice, to name refs/heads/CLOUD inside a long script, is already what the release form's checks do."
 },
 {
  "id": "NFRA_OPLGTW-Z-C-S49",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T15:00:00Z",
  "one_line": "Rounds 25-26 L8: Z-S65 advanced in place to REMEDIATED -- r26 @feddb37244 is live and the installed code refuses a slash id and a dot id with 0 requests; every condition of this seat's r26 half reads met; Z-S64 and Z-W28-S13 stay OPEN because their cells (OG-au-2, OG-sd-1) are built and not released.",
  "class": "OBSERVATION",
  "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read. Z-S65's remedy: REMEDIATED when r26 is live and a host read shows the status tool refusing a malformed id before any GET.",
  "world_is": "rl12.AC2 re-run by this seat: PASS, ssm Success, digest yes. RL12_FLOOR.json (installed_code true, served_release feddb37244): status_id_refused http_requests 0 on a slash id and on a dot id; the known execution read SUCCEEDED. The allowlist row and the check landed in one release, as the remediation row required. Z-S64: OG-au-2 admits rivalfunds_view's args to the audit allowlist (au2.AC1 PASS, 4 of 4) and is on CLOUD, not on the host. Z-W28-S13: OG-sd-1 reads the manifest's date (sd1.AC1 PASS, 3 of 3), likewise unreleased. Z-W28-S11 (the concierge's token scopes) is unchanged and at the CTO.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/2.0.0_SA_COO~O/r26/checks/rl12.AC2.sh re-run by this seat 2026-10-07 14:5xZ: RESULT: PASS exit=0",
    "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL12_FLOOR.json and RL12_ALLOW.json (read whole by this seat)",
    "git diff --name-only feddb37244 HEAD -- infra/aws/ec2/opal-gateway: audit.py, integration.py, rivalfunds_view.py, two test files, and the runbook",
    "org/critical_paths/change_management/20261007T1358Z_nfra-oplgtw-gateway-release-r26_deploy_completion.md present; 0 NFRA_OPLGTW entries in org/critical_paths/.open_deploys/ at HEAD of the shared tree",
    "remediations/REMEDIATION_v11.md#NFRA_OPLGTW-Z-S65"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```

-- 3.0.0_SA_CVO~Z
