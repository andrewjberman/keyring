# OPAL_BBGTML -- Surprise-channel investigation doc v1

Opened 2026-10-06 by 0.0.0_AB_MSTR~Z at this project's first channel item, on 1.0.0_SA_CTO~Z msg 30002.
Append-only. `integrations/bloomberg/` is under Andrew's no-modify order, so any remedy is his word.

---

### OPAL_BBGTML-Z-S1 -- the sign-in fallback writes the OCR'd Terminal username to the pull log in plain text

```json
{
  "id": "OPAL_BBGTML-Z-S1",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-10-06T11:30Z",
  "one_line": "The DAPI sign-in fallback's verify step prints the OCR'd Bloomberg Terminal username in plain text into the scheduled pull log: 3 lines in today's log, and 15 of the 31 logs in %USERPROFILE%\\opal_bbg_logs carry the line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:\\Users\\Opal Bloomberg\\opal_bbg_logs\\bbg_tplus1_20261006_070001.log lines 27, 43, 59: \"username OCR (observation only): '<username>' similarity 100%\" (value not reproduced here).",
      "Emitter: integrations/bloomberg/auth/bbg_verify.ps1:192-193 @598b791b19 (Write-Output of $ocr).",
      "Census: grep -l 'username OCR (observation only)' over %USERPROFILE%\\opal_bbg_logs\\*.log = 15 of 31 files, read 2026-10-06 ~11:28Z."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The fallback never prints credential values: its own fill line says 'user_len=12 pw_len=9 (values never printed)'.",
  "world_is": "The password stays masked, but the username is OCR'd from the screenshot and printed verbatim by the verify step, so the login identity sits in plain text in local pull logs.",
  "notes": "Local disk only; no upload of these logs was measured. No file was edited or redacted (no-modify zone, 1.0.0_SA_CTO~Z msg 30002). A remedy prints the similarity score alone and leaves the existing logs to Andrew's word."
}
```

### OPAL_BBGTML-Z-S2 -- bbg_signin.ps1's three absolute click constants miss the live login dialog (root cause of the 2026-10-06 outage)

Filed by 0.0.0_AB_MSTR~Z on 0.0.3_BG_BBGTerminal msg 30037 (BG's fence cannot write this channel). Finding is BG's.

```json
{
  "id": "OPAL_BBGTML-Z-S2",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.3_BG_BBGTerminal",
  "surfaced_at": "2026-10-06T12:41Z",
  "one_line": "bbg_signin.ps1 clicks three absolute screen constants that sit about (+204,+68) off the live 'BLOOMBERG: Login' dialog's controls, so every unattended click lands on dialog background and the fallback can never log in; one click at the recomputed Login centre (386,414) signed in at once.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "integrations/bloomberg/auth/bbg_signin.ps1:46-48 @598b791b19: COORD_USER=(659,348), COORD_PASS=(659,426), COORD_LOGIN=(590,482).",
      "0.0.3_BG_BBGTerminal log org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-06/stale_summons_step1_step2_terminal_recovered_1130-1245Z.md (untracked at filing), section R1: live dialog L=275 T=64; true centres username (455,279), password (455,360), Login (386,414); all three constants sample RGB(0,0,0); control: the password interior samples RGB(255,160,40).",
      "Same log: a single click at (386,414) gave 1 listener on 8194, the dialog closed, bloomberg_health ok=true at 12:22Z."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The sign-in fallback clicks the username field, the password field and the Login button of the live dialog.",
  "world_is": "It clicks fixed screen points measured against an older dialog position; on 2026-10-06 all three missed by about (+204,+68), so submits never reached Bloomberg and reported 'still no listener'.",
  "notes": "integrations/bloomberg/ is under Andrew's no-modify order, so the fix is his word. BG's proposed remedy: derive the three points at call time from GetWindowRect plus the field box bbg_verify.ps1 already locates. Until fixed, every unattended sign-in fails."
}
```

### OPAL_BBGTML-Z-S3 -- bbg_verify.ps1's glyph-run band rejects every fill of the credential in use

Filed by 0.0.0_AB_MSTR~Z on 0.0.3_BG_BBGTerminal msg 30037. Finding is BG's.

```json
{
  "id": "OPAL_BBGTML-Z-S3",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.3_BG_BBGTerminal",
  "surfaced_at": "2026-10-06T12:41Z",
  "one_line": "bbg_verify.ps1 accepts a username fill only if it renders len-1..len glyph runs (11..12 for 12 characters), a band built on a fixture with ONE touching glyph pair; the username in use has two such pairs, renders 10, and fails verification every time even when its own OCR scores the fill 100%.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "integrations/bloomberg/auth/bbg_verify.ps1:189 and :196 @598b791b19: uLo = len-1, uHi = len; okUser = runs within [uLo,uHi].",
      "C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261006_070001.log: 3 of 3 fills read 'username glyph-runs: 10 (expect 11..12)' with OCR similarity 100% and 9 of 9 password dots, then 'VERIFY: FAIL'.",
      "0.0.3_BG_BBGTerminal log (path in Z-S2), section R2."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The verify gate fails only a wrong fill; its own comment calls a correct fill rendering 10 runs fail-safe-rare.",
  "world_is": "For the credential in use, a correct fill always renders 10 runs, so the gate refuses 100% of correct fills and the fallback aborts before submit every day it runs.",
  "notes": "No-modify zone; the fix is Andrew's word. BG's proposed remedies: derive the band from the credential's doubled-letter count, or make the glyph check advisory beside the OCR similarity. The username value is deliberately not reproduced here (see Z-S1)."
}
```

### OPAL_BBGTML-Z-S4 -- Caps Lock was on during the automated fills, and nothing in the fill path checks or clears it

Filed by 0.0.0_AB_MSTR~Z from 0.0.3_BG_BBGTerminal's session log (R3 there; msg 30037 listed three rows, and its log carries this fourth).

```json
{
  "id": "OPAL_BBGTML-Z-S4",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.3_BG_BBGTerminal",
  "surfaced_at": "2026-10-06T12:41Z",
  "one_line": "The 07:04 local fallback screenshot shows Bloomberg's own 'Caps Lock is on' warning, the machine read CapsLock True, and the typer is SendKeys.SendWait, which is Caps-Lock-sensitive, so the masked password may have been typed case-inverted; the dot-count check cannot see case.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "0.0.3_BG_BBGTerminal log (path in Z-S2), section R3: Bloomberg's Caps Lock warning in the 07:04 local screenshot; CapsLock True; warning absent after BG cleared it before its own fill.",
      "integrations/bloomberg/auth/bbg_signin.ps1:148-149 @598b791b19: input via [System.Windows.Forms.SendKeys]::SendWait."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The fill types the stored credential exactly.",
  "world_is": "With Caps Lock on, SendWait inverts the case of alphabetic characters, and no step checks or clears Caps Lock; whether this contributed to the submitted-but-still-down days 2026-09-23 and 2026-09-27 is NOT established.",
  "notes": "No-modify zone; the fix is Andrew's word. BG's proposed remedy: clear Caps Lock in the fill path before typing and log its state."
}
```

### OPAL_BBGTML-Z-S5 -- 7 of 13 custom CIX series stop at 2026-09-29 while the rest reach 2026-10-05 (pre-existing)

Filed by 0.0.0_AB_MSTR~Z on 0.0.3_BG_BBGTerminal msg 30037 (its log calls this R4). Finding is BG's.

```json
{
  "id": "OPAL_BBGTML-Z-S5",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.3_BG_BBGTerminal",
  "surfaced_at": "2026-10-06T12:41Z",
  "one_line": "In the published 2026-10-05 PKL, 7 of 13 custom CIX series (.INT_BMK .LT_BMK .LT_ETF .ST_BMK .ST_ETF .UST_BMK .UST_ETF) last carry 2026-09-29, while the other 6 and the SPX control reach 2026-10-05; they already sat at 718 rows in the 10-02 pull, so this predates today's outage, and the tripwire passes regardless.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "0.0.3_BG_BBGTerminal log (path in Z-S2), sections '.ST CIX content check' and R4: .ST 721 -> 722 rows, last 2026-10-05 @ 111.1831; SPX 1445 -> 1446; ZZZZ Index 0 rows (negative control); the 7 named series stop at 2026-09-29."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Every custom CIX series in the daily PKL advances to the as-of date, and the as-of-scoped tripwire would catch one that does not.",
  "world_is": "Seven series have been frozen at 2026-09-29 since at least the 2026-10-02 pull, and the tripwire passes, so it does not grade per-series recency.",
  "notes": "Surfaced, not chased. Owner of the CIX definitions and the tripwire not yet named."
}
```

### OPAL_BBGTML-Z-S6 -- the untargeted yang-pipeline plan moves a SECOND resource (the Step Function definition, CRLF->LF only), which CTO condition 2 grades as a STOP

Filed by 0.7.0_AE_CloudOps~RV while executing OPAL_BBGTML.TO-GUARD-1 @416573eac2, leg 2.
ARMED: it blocks the deploy leg. This seat cannot disarm it -- the condition is the CTO's and
only its author can read its scope ("surface, do not adjudicate").

```json
{
  "id": "OPAL_BBGTML-Z-S6",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-06T16:07:26Z",
  "one_line": "An UNTARGETED terraform plan on infra/aws/terraform/yang-pipeline moves 2 of 69 resources, not 1: module.model_portfolio_benchmarks.aws_lambda_function.this (the signed act) AND aws_sfn_state_machine.yang_pipeline, whose definition differs from the deployed one by line endings ALONE -- 1012 CR bytes removed, 481 leaf values compared, 0 differ, parsed JSON identical. Pre-existing drift, unrelated to this act, but CTO section 4 condition 2 says any other resource is a STOP.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform -chdir=infra/aws/terraform/yang-pipeline plan -out=tfplan.bin -> 'Plan: 0 to add, 2 to change, 0 to destroy'; terraform show -json graded by address: 69 resource_changes, 2 NOT no-op.",
      "module.model_portfolio_benchmarks.aws_lambda_function.this changes exactly 3 attributes: source_code_hash dHTjheKzauUziiPc6Jkwn7Ys+C36Xb5KS0aAWPh7Th8= -> FLFjTpvIDptT+YqJGG9w3XaWN/Cwq4WJkNlmPd4p0tg=, s3_object_version Pzl.iT8IkhL0_Ob8sE6NQBzZ43BUyw5K -> g0NaQztkPzEyQXXiV2a4utvW1Er0V5dS, last_modified known-after-apply. That is the signed blast radius exactly.",
      "aws_sfn_state_machine.yang_pipeline changes exactly 1 attribute, definition: before 35730 chars with 1012 CR and 1012 LF; after 34718 chars with 0 CR and 1012 LF; identical with CR stripped; identical as parsed JSON; a per-leaf walk compared 481 leaf values and found 0 differing.",
      "infra/aws/terraform/yang-pipeline/yang-pipeline-definition.json carries LF; the deployed definition carries CRLF -- so ANY apply of this root from ANY device normalizes it. It is not produced by this act."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO section 4 condition 2: the plan is graded UNTARGETED, and only this function's code (or the archive/hash feeding it) may change; any other resource is a STOP.",
  "world_is": "A second resource moves. Its semantic delta is zero by measurement, but an apply still writes a new Step Function definition revision -- a state write the never-widen pair's blast radius does not name. Reading condition 2 as satisfied would be this seat adjudicating the CTO's own condition wider than its words.",
  "notes": "Deploy HELD at leg 2; nothing is half-landed. The artifact is uploaded to s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-model-portfolio-benchmarks.zip (new version g0NaQztk...), but the live function still points at the base version Pzl.iT8... and still reads CodeSha256 dHTjheKz..., so the deployed bytes are unchanged and the served keys are untouched. Three routes for the CTO: (a) an addendum naming the SFN definition CRLF->LF normalization as in-radius with DELTA=0 verified, then one untargeted apply; (b) authorize a TARGETED apply on module.model_portfolio_benchmarks.aws_lambda_function.this only, leaving the drift standing; (c) a separate act for the drift first. This seat recommends (a): the drift is measured at DELTA=0, CLAUDE.md NEVER-1 already says a verified DELTA=0 needs no hold, and (b) leaves the next operator the same STOP."
}
```

### OPAL_BBGTML-Z-S7 -- record-terraform-deploy.sh cannot run on site Z, so deployment Rule 4's last_deployed_commit is silently stale for every yang-pipeline deploy from this device

Filed by 0.7.0_AE_CloudOps~RV after TO-GUARD-1's apply, running the post-deploy hygiene the
/cloud-ops profile makes canonical. Not a TO-GUARD-1 acceptance criterion; surfaced, not chased.

```json
{
  "id": "OPAL_BBGTML-Z-S7",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-06T17:38:38Z",
  "one_line": "infra/aws/lambda/ci/record-terraform-deploy.sh dies 'line 463: /c/Users/Opal: Is a directory' on site Z: line 218 prefers bun and stores its RESOLVED PATH, which contains a space here, and four invocation sites pass it unquoted (250, 348, 448, 463). The python fallback can never fire because lines 249 and 446 gate it on $JSON_TOOL being the literal string 'python3' or 'python', which a resolved bun path never equals. Consequence: deployment Rule 4's last_deployed_commit stays at 0ce5aa5ada (2026-08-18) for yang-model-portfolio-benchmarks while the deployed bytes are 513b25f522 -- the source map now MISREPRESENTS the deployed commit, which is the exact code-currency trap Rule 4's own text warns about.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Invocation: bash infra/aws/lambda/ci/record-terraform-deploy.sh yang-pipeline --function yang-model-portfolio-benchmarks --version yang-pipeline-v1.5.9 --author '0.7.0_AE_CloudOps~RV <...>'. Output: 'Using: /c/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_.../bun' then 'record-terraform-deploy.sh: line 463: /c/Users/Opal: Is a directory'.",
      "Line 218-225 detection order: bun FIRST (JSON_TOOL=\"$(command -v bun)\", a full path), then python3, then python, then node. Lines 249 and 446 test [ \"$JSON_TOOL\" = \"python3\" ] -- false for a resolved path, so the python heredocs at 250 and 448 are unreachable on this device.",
      "Unquoted invocation sites: 250, 348, 448, 463 (grep over the file). Four, not one.",
      "The sibling builder infra/aws/lambda/ci/build-and-upload.sh ALREADY carries the fix in its own comment: 'Prefer node over bun on Windows -- bun cannot resolve MSYS2 /tmp/ paths', and it selected node cleanly in the same session.",
      "Line 787 of the recorder already names 'the $JSON_TOOL hazard' in a comment, and line 796 works around it with JS_RUNTIME=\"$(command -v node || command -v bun || true)\" -- so the defect is known in one half of the file and unfixed in the other.",
      "No partial write: git status --porcelain infra/aws/lambda/ci/ is clean after the failure, so it died before touching the source map. Nothing to reset.",
      "lambda-source-map.json for yang-model-portfolio-benchmarks still reads last_deployed_commit 0ce5aa5ada0aead068225a8e8d1551b1849358e2, last_deployed_at 2026-08-18T16:43:32Z. artifact_sha256 IS current (FLFjTpv...) because build-and-upload.sh wrote it on the working path."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Deployment Rule 4 (/cloud-ops canonical): every Lambda carries a source-map entry, and record-terraform-deploy.sh closes the parity loop after every apply by setting last_deployed_commit to the last commit touching that function's source_dir.",
  "world_is": "On site Z the recorder cannot run at all, so the loop never closes and the staleness is SILENT -- the apply succeeds, the 0-diff plan passes, and nothing reads the source map's commit field at deploy time. Rule 4's own text already disclaims being a byte-currency control; this makes its commit field actively wrong rather than merely uninformative.",
  "notes": "NOT fixed by this seat. Shared CI tooling for 7 pipelines across 2 devices, outside any open task order, and the /cloud-ops profile names this tool a known failure to 'surface in RAVC'. Two candidate fixes, both small: (a) quote all four $JSON_TOOL sites -- minimal, but may trade the space failure for the MSYS /tmp failure the sibling script documents for bun; (b) reorder detection to prefer node as build-and-upload.sh already does, which is the fix the sibling arrived at by measurement. This seat recommends (b) plus (a) together: (b) removes the space from the common path and (a) makes the remaining paths space-safe. Owner: an AE/DT seat holding infra/aws/lambda/ci/ under an authoring order. SEPARATE AND UNTAKEN: deployment Rule 6's post-deploy tag. yang-pipeline-v1.5.9 was NOT created -- 11 of 11 yang-pipeline tags and 256 of 264 pipeline tags across the repo were created by Andrew Berman (7 by 0.0.0_AB_MSTR, 1 by 0.7.0_AE_CloudOps~V), so tagging is not this seat's measured practice, and the Rule 6 'push --follow-tags' half is barred to every seat but the integrator anyway."
}
```

### OPAL_BBGTML-Z-S8 -- record-terraform-deploy.sh writes the pipeline CHANGELOG outside any task order's <paths>, and the criterion written to bound it is path-scoped so it cannot see the overrun

Filed by 0.7.0_AE_CloudOps~RV while grading TO-GUARD-2's AC3. Not caused by the Z-S7 fix; the fix
is what made it reachable, because the script previously died before either writer.

```json
{
  "id": "OPAL_BBGTML-Z-S8",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-06T18:06:48Z",
  "one_line": "record-terraform-deploy.sh commits infra/aws/terraform/<pipeline>/CHANGELOG.json alongside the source map -- 48 insertions here -- which is outside TO-GUARD-2's <paths> and outside infra/aws/lambda/ci/ entirely; and TO-GUARD-2's AC3 proof invocation is path-scoped to the very directory the write escaped, so it returns a clean one-file answer and the criterion PASSES while the overrun stands.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "AC3 LITERAL invocation, git show --stat 4ddd25eee8 -- infra/aws/lambda/ci/ -> '1 file changed, 5 insertions(+), 4 deletions(-)', lambda-source-map.json only. READS CLEAN.",
      "The SAME commit unscoped, git show --stat 4ddd25eee8 -> '2 files changed, 53 insertions(+), 4 deletions(-)': lambda-source-map.json AND infra/aws/terraform/yang-pipeline/CHANGELOG.json (+48).",
      "TO-GUARD-2 @304b05698f <paths> names three files: the recorder, lambda-source-map.json, and this channel. The pipeline CHANGELOG is not among them, and the owned-paths hook did not refuse the commit.",
      "The source-map diff ALSO added a per-function key recorded_by that AC3 does not name. AC3 named _updated and _last_deploy_recorded; _last_deploy_recorded did move, _updated did not.",
      "The CHANGELOG entry records agent=devops_technician, a hardcoded label, not the --author serial that was passed and that the git commit correctly carries (0.7.0_AE_CloudOps~RV).",
      "That entry's deployed_commit is 8555ce7e1255d8d0af58fd8280bd8cd184b55a71 -- HEAD at run time, an unrelated record commit -- NOT the deployed code commit 513b25f522 that the source map correctly carries. Two fields named for the same idea disagree by design across the two files."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A task order's <paths> is the write surface of the act (owned-paths-validate), and an acceptance criterion's invocation measures the thing the criterion claims to bound.",
  "world_is": "A seat running the recorder under ANY order whose <paths> omit infra/aws/terraform/<pipeline>/CHANGELOG.json overruns its write surface, under its own author line, in a commit the tool makes for it. And the criterion written to bound the diff is scoped to a directory the overrun is not in, so it certifies nothing about it -- a census scoped to where the question is filed, missing the answer filed elsewhere.",
  "notes": "Surfaced, not chased. No fix attempted and none wanted from this seat without an order: changing where the recorder writes touches 7 pipelines on 2 devices. Three candidate scopes for an owner, cheapest first: (i) add the pipeline CHANGELOG to the <paths> of any order that runs the recorder -- a template fix, not a code fix; (ii) re-word the AC3 pattern to grade an UNSCOPED git show --stat, since a path-scoped proof of a path-containment claim is circular; (iii) decide whether agent and deployed_commit in that file should carry the real serial and the real code commit, which is a semantics question about what the file is FOR, not a bug report. Owner: an AE/DT seat holding infra/aws/lambda/ci/. Cites OPAL_BBGTML-Z-S7 (the defect that hid this) and ETFS_RIVALS-Z-S40 (same class: a granted path a seat could not actually write)."
}
```

### OPAL_BBGTML-Z-S9 -- Z-S7's fix has LANDED, but its disposition is not this seat's to move: RESOLVED is not in the gate's closed enum and GRADUATED is the CVO's

Filed by 0.7.0_AE_CloudOps~RV as a NEW row citing OPAL_BBGTML-Z-S7, because the channel is
APPEND-ONLY. I first tried to mark Z-S7 RESOLVED in place, as TO-GUARD-2 directs, and the gate
refused twice -- correctly, and on two different grounds. Both refusals are recorded below, because
the second is a rule this seat had exactly backwards.

```json
{
  "id": "OPAL_BBGTML-Z-S9",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-06T18:06:48Z",
  "one_line": "The Z-S7 defect is FIXED @8be38c9dec and verified (AC1 exit 0 with no 'Is a directory'; AC2 last_deployed_commit now 513b25f52259dcfe10500cdffd564c025d08afda), but Z-S7's disposition still reads UNDER_INVESTIGATION because TO-GUARD-2's instruction to mark Z-S7 RESOLVED is not executable by this seat: RESOLVED is not a member of the closed disposition enum, and the terminal value GRADUATED is resolved from a REMEDIATION row, which stays the CVO's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE FIX: @8be38c9dec. Detection reordered to node FIRST (node resolves as a bare name, so no device path enters the invocation); all four JSON_TOOL invocation sites quoted, with the census asserted before any byte was written (4 unquoted before, 0 after, 4 quoted after); both python gates now compare the basename, so a resolved path still selects the python branch; and the comment at line 217 corrected, which had claimed bun was 'derived with command -v, no device path' -- the opposite of what command -v bun returns, and the sentence that made the original choice look safe.",
      "VERIFIED: bash -n exits 0, with a live negative control -- a copy with a truncated if appended is REJECTED by the same bash -n, so the pass discriminates. commit-gate clean 1 of 1.",
      "AC1 PASS: the recorder ran to exit 0, no 'Is a directory', committing @4ddd25eee8.",
      "AC2 PASS: lambda-source-map.json last_deployed_commit 0ce5aa5ada (2026-08-18) -> 513b25f52259dcfe10500cdffd564c025d08afda, last_deployed_at -> 2026-10-06T17:47:56Z. Deployment Rule 4's parity loop is closed for the guard deploy.",
      "REFUSAL 1, on the enum: the gate blocked the commit at /disposition. surprise-row-gate.py:174 defines UNDISPOSITIONED as ('UNDER_INVESTIGATION', None, ''); :164-166 resolves the terminal value GRADUATED from a REMEDIATION row bearing the id, else a row whose adjudicates list names it. RESOLVED is in neither set. CLAUDE.md section 2: REMEDIATION rows stay the CVO's.",
      "REFUSAL 2, on append-only, after the enum value was reverted but the row left edited: 'EXISTING row OPAL_BBGTML-Z-S7 was MUTATED in place (content hash 775ec48bffef -> 48ecd6b0ea3f). Corrections are NEW items citing the old id; an edited history is a history nobody can audit.' The rule was inverted here: supersede-in-place is for STATE carriers, while a surprise row is corrected by a NEW row. Z-S7 was restored to its committed bytes (17757) and this row carries the correction instead."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-GUARD-2's gates: Mark Z-S7 RESOLVED in its own row, citing the fix commit.",
  "world_is": "That step cannot be performed as written by any non-CVO seat. The word RESOLVED does not exist in the grammar, and the two mechanisms that CAN terminate an item -- a remediation row, or a CVO L9 adjudication -- are both the CVO's. A seat following the instruction literally either gets refused, as this one did, or forces an out-of-enum string past an override and leaves the corpus carrying a value no consumer can read.",
  "notes": "Two asks, neither taken unilaterally. (1) For 3.0.0_SA_CVO~RV or whoever holds L9 on this project: graduate Z-S7, whose fix is landed and verified. (2) For 2.0.0_SA_COO~Z: the order template's wording. 'Mark <row> RESOLVED' should read 'record the fix in a new row citing <row>, and hand the disposition to the CVO', or the next order repeats this. No override was used for either refusal; the gate was right both times."
}
```

### OPAL_BBGTML-Z-S10 -- the Teams watcher's documented arm line `--identity opalbloomberg` cannot match: self_id() never reads the `email` claim

Filed by 2.0.0_SA_COO~Z as the carrier for a finding of 0.0.3_BG_BBGTerminal (its msg 30741, carried by
0.0.0_AB_MSTR~Z msg 30742), which cannot write this channel. The named owner of the engine,
0.5.0_AE_OpalETL~Z, had no live session at filing.

```json
{
  "id": "OPAL_BBGTML-Z-S10",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~Z",
  "surfaced_at": "2026-10-07T09:08:37Z",
  "one_line": "teams-watch.py --identity opalbloomberg dies [TEAMS-IDENTITY-FAIL] no-token-for-identity (exit 2): self_id() reads sub, then preferred_username, then upn, and the terminal seat reports the gateway tokens carry the readable identity only in email. The same arm line is the documented one in two places.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ BY THIS SEAT: .claude/skills/teams-assist/teams-watch.py:283 -- sub = claims.get(\"sub\") or claims.get(\"preferred_username\") or claims.get(\"upn\"). The email claim is not read. 1 file of that name in the repo.",
      "READ BY THIS SEAT: the arm line `--identity opalbloomberg` is in .claude/skills/bbg-teams-assist/SKILL.md (1 skill file of the skills folder names it). The seat also names its own prompt.md step 3; that file was not read here.",
      "REPORTED BY 0.0.3_BG_BBGTerminal, NOT re-measured here (no token was decoded by this seat): on all three token records preferred_username and upn are null, sub is an opaque pairwise GUID, and the true identity is in email. Its record: org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-07/startup_0818-0900Z_post_reboot_launch_teams_replay_sweep.md lines 32-57 and 174-178.",
      "REPORTED BY THE SAME SEAT: it armed instead on --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f with the --server pin intact, so its watcher is identity-pinned today. That is why the hazard reads INERT."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The documented arm line pins the Teams watcher to the terminal's own identity by a readable name, and a seat following its prompt or the skill arms a working, identity-pinned watcher.",
  "world_is": "The documented line exits 2 before arming. A seat that reacts by dropping --identity arms a watcher that is not pinned; the terminal seat did not do that and pinned on the GUID instead. The fix is the engine owner's choice of two: self_id() falls through to email, or the two documents name the GUID.",
  "notes": "Surfaced, not chased. No edit made to teams-watch.py, the skill or the prompt. Owner of the engine per the terminal seat: 0.5.0_AE_OpalETL~Z, not live at filing. Placement: 2.0.0_SA_COO~Z cuts an order to that seat when it is seated, or the CTO re-homes the row if the Teams concierge belongs to another project; this channel was chosen because 2.0.0_SA_COO~Z holds the Bloomberg terminal cells."
}
```

### OPAL_BBGTML-Z-S11 -- the 2026-10-06 07:00 ET vehicle reads LastTaskResult 267014: the task was ended at its 30-minute limit while a leg retried a dead DAPI connection

Filed by 2.0.0_SA_COO~Z on the ask of 1.0.0_SA_CTO~Z (msg 30747, the read owed outside the ba-21 CTO half).

```json
{
  "id": "OPAL_BBGTML-Z-S11",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~Z",
  "surfaced_at": "2026-10-07T09:23:59Z",
  "one_line": "Scheduled task OPAL_BBGTML_daily_pull: LastRunTime 2026-10-06 07:00:01 local, LastTaskResult 267014 (0x41306, the scheduler's code for a task that was terminated). Its log ends at 07:30:01 with ^C, and the task's ExecutionTimeLimit is PT30M: the run was ended by the limit, it did not exit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Get-ScheduledTaskInfo at 05:20 local 2026-10-07: OPAL_BBGTML_daily_pull LastRunTime 2026-10-06 07:00:01, LastTaskResult 267014 (0x41306), State Ready, NextRunTime 2026-10-07 07:00:00, MissedRuns 0. Settings: ExecutionTimeLimit PT30M, MultipleInstances IgnoreNew. Control on the same read: OPAL_BBGTML_freshness_check LastRunTime 2026-10-06 07:30:01, LastTaskResult 2.",
      "The run's own log, bbg_tplus1_20261006_070001.log (last write 07:30:01 local): line 7 DAPI DOWN; line 63 DAPI FALLBACK EXIT 2; line 81 PRECONDITION FAILED, PULL NOT ATTEMPTED; line 88 RIVALFUNDS BLOOMBERG LEG EXIT CODE 93, nothing written; line 89 starts the RIVALFUNDS ENRICHMENT STEP; then 68 of the log's 71 'Failed to connect to 127.0.0.1:8194' lines follow that start, from 07:08:01 to 07:29:40 (the other 3 are in the precondition block); the last line is ^C. No enrichment exit code and no final exit line were written.",
      "A second log, bbg_tplus1_20261006_082454.log (last write 08:33:57 local), ends RIVALFUNDS BLOOMBERG LEG EXIT CODE 90 landed and RIVALFUNDS ENRICHMENT EXIT CODE 94 landed. The task's LastRunTime still reads 07:00:01, so that recovery run was not started through the scheduler and left no result in it.",
      "NOT measured: the Task Scheduler operational event log returned no events for this task (the read found none in the last 4000 events), so 'ended by the time limit' rests on the limit, the log's last-write time and the ^C, not on a scheduler event.",
      "Today, for C1 of the ba-21 CTO half: at 09:22Z one process (bbcomm, started 04:26:40 local) listens on 127.0.0.1:8194. That is a port read only; no Bloomberg request was made, and a listener is not proof the Terminal is signed in (READ_HERE section 2)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The vehicle exits with its own code (0, or a named non-zero from its disjoint leg ranges), every leg is isolated, and a reader of the task's result or its log can tell which leg spoke.",
  "world_is": "On 2026-10-06 the vehicle did not exit: with the DAPI down, the rival-funds enrichment step kept retrying the connection for about 22 minutes and the scheduler ended the whole task at 30 minutes. The result is the scheduler's 267014, not a code of the launcher, and no leg after the enrichment step ran. A gate that reads only the last run DATE and 'not Running' (research_pulls.vehicle_ran_today) passes on such a day.",
  "notes": "Surfaced, not chased. No file, task or schedule was changed. Three things an owner may decide, none taken here: (1) the enrichment step has no bound of its own on a dead DAPI, unlike the collector leg, which exited 93 at once; (2) the 30-minute limit ends the task without a launcher exit line, so the day's log has no verdict; (3) the research-pull gate does not read the result. For the ba-21 act, (3) is covered by condition C1 of CTO_HALF_AMGT_RESAPP_BA21_SEGMENTS_PULL_20261007.md: this seat reads the result and the log before the probe. The enrichment step is ETFS_RIVALS code (2.0.0_SA_COO~RV's project); the launcher is under Andrew's no-modify order for integrations/bloomberg/."
}
```

### OPAL_BBGTML-Z-S12 -- GUARD-3b closes the per-series CIX check on the SCHEDULED path only: a hand-run publish_to_portal.py re-runs the TZERO tripwire, which the order forbids touching and which carries no per-series check

Filed by 0.7.0_AE_CloudOps~RV while executing OPAL_BBGTML.TO-GUARD-3 cell GUARD-3b, which
names the tplus1 copy and says of the tzero copy "Do not touch it. Say in your report whether
anything scheduled runs it." It does -- this row is that read, placed where it survives the
report.

```json
{
  "id": "OPAL_BBGTML-Z-S12",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-07T09:48:00Z",
  "one_line": "There are TWO copies of bbg_pkl_tripwire.py and they are reached by different consumers. GUARD-3b adds the per-series custom-CIX recency check to the tplus1 copy, which the scheduled pull leg runs. The SEND gate -- publish_to_portal.py line 64 -- deliberately runs the TZERO copy instead, and that copy is out of the order's bounds, so it does not get the check. The scheduled path is still closed, because the vehicle gates the send leg on the pull rc; a HAND-run publish_to_portal.py is not.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ BY THIS SEAT: integrations/bloomberg/pipeline/publish_to_portal.py:62-64 -- 'The as-of-scoped tripwire lives in the tzero variant; tplus1's copy is deliberately byte-verbatim with production and does NOT carry the check. Use tzero's regardless of which variant produced the files -- we want the STRICTER instrument on the send path.' TRIPWIRE = os.path.join(HERE, 'tzero', 'tools', 'bbg_pkl_tripwire.py').",
      "READ BY THIS SEAT: integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:180 sets PUBLISH to publish_to_portal.py and runs it as the SEND LEG, so the tzero copy IS on a scheduled path -- the answer to the order's question is YES, indirectly, via the publisher.",
      "READ BY THIS SEAT: the scheduled path is nonetheless CLOSED by the tplus1 edit alone. scheduled_daily_pull.cmd runs the pull leg as %RUNNER% (line 39, tplus1/tools/run_daily_pull.py) and then branches: 'if not \"%RC%\"==\"0\" ( echo RESULT: PULL FAILED rc=%RC% -- nothing sent, publish NOT attempted ... goto :etf_leg / goto :prune )'. The SEND LEG is only reached on RC==0. And run_daily_pull.py:246-256 runs the tripwire from its OWN TOOLS_DIR (the tplus1 copy) and returns its rc: 'STOP: tripwire FAILED -- do not send.' So a frozen custom CIX series now fails the tplus1 tripwire, the runner returns non-zero, and the cmd never reaches the publisher.",
      "READ BY THIS SEAT: the residual is the MANUAL path, and two documents instruct it. run_daily_pull.py:261 prints 'NEXT: ... publish on the SAME channel the scheduled run uses: <PY_AWS python> -u integrations/bloomberg/pipeline/publish_to_portal.py -- No args needed -- the publisher derives the vintage itself, re-runs the as-of-scoped tripwire'; and integrations/bloomberg/pipeline/README.md:299 names the tzero tripwire directly. Either route re-runs tzero only, which after this order still has no per-series CIX limb.",
      "MEASURED, bounding the hazard today: on the current served vintage all 13 custom CIX series reach the as-of 2026-10-05 (benchmarks/data_20261007_v1.pkl VersionId F2HhLHRpKgZ18hIWMRJr3p3t4T52RfBW), and the served body's benchmark_last_date reads 2026-10-05 on all 5 models both sides. There is no frozen series to send right now, which is why this reads INERT rather than ARMED.",
      "NOT MEASURED by this seat: whether the tzero copy's own as-of-scoped presence check (its lines 133-152, absent from tplus1) would independently catch a frozen BENCHMARK series. It checks that the five MODEL index_names have a bar ON the as-of; the four _BMK and four _ETF benchmark series are not in MODEL_INDEX_NAMES, so on its face it would not -- but that is a reading of the code, not an exercise of it, and the order's bounds put exercising it out of scope."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ADDENDUM 6's gap 2 is closed when a pull carrying a frozen custom CIX series cannot reach the portal: 'For every custom CIX series in the data PKL, the last non-null date equals the as-of date. A series behind FAILS the tripwire.'",
  "world_is": "It is closed on the scheduled vehicle, which is the path ADDENDUM 6's proof and first-live-read are written against. It is NOT closed on the hand-run send: publish_to_portal.py re-runs the tzero copy, the order forbids editing that copy, and so the stricter instrument on the send path is now the one MISSING the newer check -- an inversion of the comment's own intent at line 62-64.",
  "notes": "Surfaced, not chased, and nothing outside the order was edited: the tzero copy, publish_to_portal.py and the two documents are untouched. Three routes an owner may choose, none taken here: (1) port the same grade_cix_series limb into the tzero copy, which makes the send gate strictest again and is the smallest change; (2) have publish_to_portal.py run BOTH copies; (3) factor the shared checks into one module both copies import, which is the real fix for a file that has now diverged twice and is the largest change. Route (1) or (3) also retires the standing confusion that the two copies' DOCSTRINGS each claim to be the production one. This needs a new order or an amendment to TO-GUARD-3: this seat's bounds name only the tplus1 copy."
}
```


### OPAL_BBGTML-Z-S13 -- the pinned Teams watch goes blind for a window when its 15-minute token lapses unre-selected; one live Andrew message dropped on 2026-10-08

Filed by 2.0.0_SA_COO~Z on the route of 0.0.0_AB_MSTR~Z (msg 32095) from 0.0.3_BG_BBGTerminal (msg 32093).

```json
{
  "id": "OPAL_BBGTML-Z-S13",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~Z",
  "surfaced_at": "2026-10-08T23:35:34Z",
  "one_line": "The pinned Teams watch goes BLIND for a whole window when its 15-minute issuer token lapses and is not re-selected: 1 of 3 windows measured blind on 2026-10-08, and Andrew's 21:57:19Z Tax SMA message was not emitted by the armed watcher (surfaced about 10 minutes late by a direct poll).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "REPORTED BY 0.0.3_BG_BBGTerminal msg 32093 (org/mcp/inbox/0.0.0_AB_MSTR/~Z/read/20261008T225301Z_0.0.3_BG_BBGTerminal_MEASURED__Teams-watch_blocker__1__went_B.md), NOT re-measured here: window A lapsed then re-selected, 0 events; window B lapsed with no re-selection line, blind; window C re-selected, emitted late, lapsed at the tail. Its evidence: the monitors' stderr banners in that seat's tasks/b95i1hu85.output (blind) and bj3z1t0zh.output (late emit).",
      "The same seat: Andrew's 21:57:19.836Z Tax SMA message was found by calling poll_addressed_teams_messages directly; the next watcher cycle emitted it about 10 minutes late.",
      "Routed to this seat by 0.0.0_AB_MSTR~Z msg 32095 as the placer of the Teams-watch row OPAL_BBGTML-Z-S10."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Blocker (1), documented by 4.0.0_SA_CRO~Z on 2026-09-24: the issuer token has a 15-minute TTL and is minted only on expiry. The armed watcher is the concierge's intake: every addressed Teams message is emitted as an event while it is armed.",
  "world_is": "When the token lapses and the re-selection does not happen, the watcher stays armed and emits nothing for the rest of its window, so a live addressed message is dropped until a later cycle or a direct poll finds it.",
  "notes": "Surfaced, not chased. A sibling of Z-S10 in the same engine (.claude/skills/teams-assist/teams-watch.py), not the same fault: S10 is the identity claim, this row is the token lifetime. The engine's owner per Z-S10 is 0.5.0_AE_OpalETL~Z, not registered at filing (get_agent_status 2026-10-08 ~23:3xZ). Disarm: an order to that seat for a refresh before expiry (or a re-select that is checked each cycle), cut by this seat when that seat is seated. Until then the compensating act is the terminal seat's own direct poll_addressed_teams_messages read, which is what found the dropped message."
}
```

### OPAL_BBGTML-Z-S14 -- the intake's FETCH token expired 2026-09-19, so the identity pin fix (repair 4) cannot reach its backlog gate: the read returns FETCH_FAILED 403, an UNKNOWN, not a zero

Filed by 2.0.0_SA_COO~ZB while preparing the Z6 repairs 2-5 issuance (CTO ruling @61e3067f5c, disposition 4).

```json
{
  "id": "OPAL_BBGTML-Z-S14",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZB",
  "surfaced_at": "2026-10-13T20:32:45Z",
  "one_line": "The D7 intake's fetch credential (secret opal/ticketing/svc-analyst-intake, a portal service JWT) expired 2026-09-19T20:03:28Z; the portal API answers the fetch HTTP 403, so the backlog read that gates repair 4 returns UNKNOWN, and the pin fix alone would move the scheduled task from exit 2 to exit 5, not to a working intake.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-13 ~20:30Z: python org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r4_backlog_read.py (dry-run production pass, send stub that raises) printed cursor created_at='2026-08-20T20:18:09.873Z', then 'FETCH_FAILED HTTPError: HTTP Error 403: Forbidden -- no row examined, cursor unchanged', BACKLOG: UNKNOWN, rc=3.",
      "MEASURED the same minute, claims only, token value never printed: the secret's JWT exp = 2026-09-19T20:03:28Z, iat 2026-08-20T20:03:28Z; secret metadata minted_by '0.7.0_AE_CloudOps (D7 TO-D final, CTO~Z ruling (b))', rotate_by 2026-09-10T20:03:28Z, expires_at 2026-09-19T20:03:28Z, iss opal-portal-auth, aud opal-portal-api.",
      "MEASURED: %USERPROFILE%/opal_ticket_intake/runner.log carries 844 'exit 5' lines; its last FETCH_FAILED line (24401) reads the same 403.",
      "READ, runner.py main(): svc_fetch_factory only reads the secret; gateway_send_factory's pin refusal (exit 2) fires BEFORE run_once ever calls the fetch, so since 2026-09-18 the identity refusal has masked the expired fetch token."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO ruling @61e3067f5c disposition 4: FIRST read the intake cursor and the count of tickets opened since 2026-09-03; land the oid pin only on a zero backlog or Andrew's word. The trace (OPAL_BBGTML_Z6_TRACE_20261013_Z.md Q3) left the fetch leg NOT MEASURED.",
  "world_is": "The backlog cannot be read at all: the fetch credential is 24 days expired and the API refuses it. The gate's input does not exist until the service token is re-minted, and a re-mint is a key act (prior service-token mints ran as never-widen pairs: TCKT_VNEXT NEVER_WIDEN_PAIR_SVC_COMMENTARY_MINT) that the Z6 ruling does not cover.",
  "notes": "Repair 4 is NOT cut in the Z6 issuance; it is parked on this row. Un-park condition: a CTO ruling on who re-mints opal/ticketing/svc-analyst-intake and under which project, then the re-run of r4_backlog_read.py reads a number. Asked of 1.0.0_SA_CTO~Z in one message. The row's ARMED standing is the client-facing hazard the ruling named: whoever re-mints the token without the pin fix gets exit 2 still; whoever re-mints it WITH the pin fix landed gets a first good pass that may post the whole backlog since cursor 2026-08-20T20:18Z into the client ticket channel. So the re-mint and the pin must be one act behind the backlog read."
}
```

### OPAL_BBGTML-Z-S15 -- the P0 gate's trailing line still says "transport sustained-down" on the new listener-up path, so the gate's own output contradicts itself

Filed by 0.7.0_AE_CloudOps~ZS while executing TO-Z6-R2 (cell Z6-R2). The line is inside the edited STEP 2 but outside the order's instruction set, so it was left byte-unchanged rather than amended at the cut.

```json
{
  "id": "OPAL_BBGTML-Z-S15",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZS",
  "surfaced_at": "2026-10-13T21:20Z",
  "one_line": "On the new $absent -eq 0 path the gate prints 'P0 gate: 8194 listening (3/3) ... listener up, not entitled' and then, two lines later, 'P0 gate: transport sustained-down, network OK -> sign-in warranted' -- the transport is NOT down on that path, so an unattended pull log now carries two contradictory classifications of the same state.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-13 ~21:10Z, AC1 of TO-Z6-R2 (r2_p0_listener_check.sh against the deployed bytes @f6cc68d6bf), full stdout in order: '[fallback] DAPI DOWN.' / '[fallback] P0 gate: 8194 listening (3/3) but dapi_check failed -> listener up, not entitled -> sign-in warranted.' / '[fallback] P0 gate: transport sustained-down, network OK -> sign-in warranted.' / '[fallback] fire-once ledger clear (0 in 6h).' / '[fallback] STUB: would now fill ...'",
      "READ integrations/bloomberg/auth/bbg_fallback.ps1 @f6cc68d6bf line 66: 'Say \"P0 gate: transport sustained-down, network OK -> sign-in warranted.\"' sits after the two network checks and is reached unconditionally by both the $absent -eq 0 and the $absent -eq 3 branches."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-Z6-R2 the_act item 2: on $absent -eq 0 print EXACTLY the 'listener up, not entitled' line 'and continue into the existing network checks (69.187.48.83:8194 and the 8.8.8.8:53 control), then STEP 3'. It names no change to the trailing line, and its bounds say nothing else in the file changes.",
  "world_is": "Both lines print on the same run. AC1 does not grade the trailing line (it greps only for the absence of 'not sustained-absent', the presence of 'listener up, not entitled', and the stub/fire-once marker), so the criterion passes with the contradiction in place.",
  "notes": "Remedy is one line and is the ISSUER's cut, not this seat's: guard it as 'if ($absent -eq 3) { Say ... }'. This seat wrote and discarded exactly that edit to stay inside the order's bounds mid-round. Cost of leaving it: a human reading tomorrow's 07:00 ET pull log sees the gate assert the transport is both up and sustained-down. No behavioural effect -- the branch taken is correct either way."
}
```

### OPAL_BBGTML-Z-S16 -- `wintrv.exe` absence is not a signed-out oracle: the DAPI measured UP and ENTITLED with zero wintrv processes, so the trace's "INFERRED signed out" and disposition 1's premise are both unconfirmed

Filed by 0.7.0_AE_CloudOps~ZS while executing TO-Z6-R2 AC2 (the real, un-forced run). The reading instrument is the one the ruling itself prescribes.

```json
{
  "id": "OPAL_BBGTML-Z-S16",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZS",
  "surfaced_at": "2026-10-13T21:20Z",
  "one_line": "At 21:12-21:14Z the Terminal's DAPI was UP and ENTITLED (a real SPX Index/PX_LAST returned) while Get-Process wintrv read 0 and the only Bloomberg processes were bbcomm and blpcrashmon, both started 19:07:29Z -- so 'no wintrv.exe therefore signed out' is an unsound inference, and the state the Z6 repair was cut against was not the state on the box.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-13 ~21:12Z, AC2 of TO-Z6-R2, un-forced run of the deployed bytes: 'powershell -File integrations/bloomberg/auth/bbg_fallback.ps1 -StubSubmit' printed '[fallback] checking DAPI availability...' then '[fallback] DAPI UP -- proceed with pull, no sign-in needed.' exit=0. Dapi-Up had just run dapi_check.py for real (no -ForceDown).",
      "MEASURED 2026-10-13T21:14:16Z, second independent run of the same oracle directly: 'C:\\Anaconda\\envs\\cma\\python.exe integrations/bloomberg/auth/dapi_check.py' printed 'DAPI: UP (session + SPX Index/PX_LAST returned -- entitled session live)' rc=0.",
      "MEASURED the same minute: @(Get-Process -Name wintrv).Count = 0; the process census matching 'wintrv|bbcomm|blp|bbg|dde' returned exactly bbcomm (pid 17756, started 2026-10-13T19:07:29.3429109Z) and blpcrashmon (pid 27320, started 19:07:29.3996499Z). 8194 listeners = 1, owned by bbcomm pid 17756.",
      "READ CTO_RULING_OPAL_BBGTML_Z6_REPAIR_DISPOSITIONS_20261013_Z.md: the leg table records 'after the 14:57 ET reboot there is no wintrv.exe, so the Terminal is INFERRED signed out', and disposition 1 says 'Confirm the sign-in with dapi_check.py, which makes a real data request, never bloomberg_health'. This row runs that prescribed confirmation and it disagrees with the inference."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-Z6-R2 context, 'Live state at issue (measured 20:36Z)': '8194 LISTEN with one listener (bbcomm.exe started by integrations/bloomberg/mcp/server.py); the Terminal shell wintrv.exe is not running (inferred signed out).' Disposition 1 treats a Terminal sign-in before 07:00 ET 2026-10-14 as Andrew's act, on the premise that the Terminal is signed out.",
  "world_is": "The DAPI is up and entitled with no wintrv.exe. Either the session was signed in all along (and wintrv is simply not the Terminal's live process name on this box), or it was signed in between 20:36Z and 21:12Z by an act this seat did not make and no record this seat read names. Not distinguished here; the 20:36Z reading was itself taken with the same unsound instrument, so there is no sound before-measurement to compare against.",
  "notes": "TWO consequences the issuer should weigh before 11:00Z. (1) Andrew's open call to sign the Terminal in may already be satisfied -- it should be re-read with dapi_check, not with a wintrv census. (2) EVIDENCE LIMIT on repair 2 itself: AC1 reaches the new classification only under -ForceDown, which short-circuits Dapi-Up before dapi_check is ever called. So the 'listener up, not entitled' branch has been exercised against a FORCED STEP-1 failure and never against a genuinely un-entitled session. ABSENT is not EXERCISED-AGAINST. The repair is still correct and still needed -- whenever a real dapi_check fails while 8194 listens, the old gate refused to sign in -- but nobody should report it as proven against the live un-entitled state."
}
```

### OPAL_BBGTML-Z-S17 -- the file cell Z6-R2 was ordered to edit sits under a standing Andrew no-modify order that names "the sign-in scripts", and the ruling that cut the edit neither cites nor lifts it

Filed by 0.7.0_AE_CloudOps~ZS after the edit landed. Surfaced, NOT adjudicated: per CLAUDE.md the receiving agent does not read a sovereign order wider or narrower, and this seat did not revert on its own reading.

```json
{
  "id": "OPAL_BBGTML-Z-S17",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZS",
  "surfaced_at": "2026-10-13T21:20Z",
  "one_line": "integrations/bloomberg/auth/bbg_fallback.ps1 was edited and deployed under TO-Z6-R2 while the record of Andrew's no-modify order says at HEAD that it 'still stands for the Positioning and ETFS-view files (integrations/bloomberg/pipeline/, the vehicle and the sign-in scripts)' -- and the CTO ruling that cut the cell contains no mention of the no-modify order at all.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ at HEAD, org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md lines 27-28, bytes printed: 'The order still stands for the Positioning and ETFS-view files (`integrations/bloomberg/pipeline/`, the vehicle and the sign-in\\nscripts), per call 5 of `ANDREW_DIRECT_20261006_1818Z_ALL_RECS_APPROVED_MSTRZ_OPEN_CALLS.md`.' The phrase wraps the line break, so a single-line grep for 'sign-in scripts' returns 0 against a file that contains it.",
      "READ integrations/bloomberg/auth/bbg_fallback.ps1 header line 2: 'bbg_fallback.ps1 -- UNSUPERVISED Bloomberg DAPI-down sign-in fallback (LD-0413)'. It is a sign-in script on its own description.",
      "CENSUS of CTO_RULING_OPAL_BBGTML_Z6_REPAIR_DISPOSITIONS_20261013_Z.md (4387 bytes, whole file) for 'no-modify|no modify': 0 hits. Its stated basis is 'Andrew's site Z memo: \"We want to make sure that's functional ... that people can use it.\"'",
      "ABSENT at HEAD: the basis the 201xZ record cites, 'ANDREW_DIRECT_20261006_1818Z_ALL_RECS_APPROVED_MSTRZ_OPEN_CALLS.md'. git ls-tree -r HEAD org/tier1_exec/ lists 43 ANDREW_DIRECT_20261006_* records and that filename is not among them; git log --diff-filter=D over the pattern returns no deletion. The nearest same-hour records are ANDREW_DIRECT_20261006_181xZ_*. So the standing clause's own citation does not resolve to a readable record.",
      "The surprise channel's own header (INVESTIGATION_v1.md line 4) states: 'integrations/bloomberg/ is under Andrew's no-modify order, so any remedy is his word.' Prior seats honoured it as covering this surface: BBG_SIGNIN_CLICK_COORD_DRIFT_20261006.md line 3 reads 'Status: PROPOSAL. NOT APPLIED. integrations/bloomberg/ is no-modify'."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO ruling @61e3067f5c disposition 2 cuts the edit as a CELL under OPAL_BBGTML: 'The file runs from the working tree, so the edit is the deploy: the cell carries a change-management entry and one real run.' TO-Z6-R2 names the file as the one production file to edit and states 'Saving the file IS the deploy.' Neither names the no-modify order.",
  "world_is": "The edit is landed and deployed at @f6cc68d6bf on box/sitez and is what the 07:00 ET 2026-10-14 Scheduled Task will run. Whether the Z6 memo ('make sure that's functional') lifts a standing order that specifically names the sign-in scripts is a sovereign reading this seat is barred from making in either direction, so it did not revert and did not widen.",
  "notes": "NOT A CLAIM THAT THE CELL WAS WRONGLY CUT. Two readings are open and this seat holds neither: (a) the Z6 memo authorises functional repair of the sign-in path, in which case the 201xZ record's standing clause is stale and should be struck; (b) the order stands, in which case cells Z6-R2 and Z6-R3 need Andrew's word and this one is already landed. DISARM IS ONE ACT EITHER WAY: the issuer or 1.0.0_SA_CTO~Z states which reading holds, in a record. If (b) and he says revert, the rollback is already specified by the order: git checkout f6cc68d6bf~1 -- integrations/bloomberg/auth/bbg_fallback.ps1, commit, and close the deploy ledger entry opal-bbgtml-z6-r2-p0-gate-20261013 as rolled back -- a 0-risk revert to bytes sha256 5aeb770858cead537dd8106754324a3428a580260cb259a2855f3c89395d9193. TIME-BOXED: whichever way it falls, it should fall before the 11:00Z fire. This row also blocks R3 (the next order on this lane), which edits bbg_signin.ps1 -- squarely a sign-in script by name."
}
```

### OPAL_BBGTML-Z-S18 -- a closed round's AC freezes teams-watch.py by AST equality, so the ordered Z6 R5 edit flips it PASS -> FAIL on commit

Filed by 0.7.0_AE_CloudOps~ZT while executing OPAL_BBGTML.TO-Z6-R5 step 2c (the launcher/consumer census).

```json
{
  "id": "OPAL_BBGTML-Z-S18",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZT",
  "surfaced_at": "2026-10-13T21:28:21Z",
  "one_line": "NFRA_OPALAI round-2 AC1 (e7.AC1.sh) freezes .claude/skills/teams-assist/teams-watch.py by AST EQUALITY against cut c8df03c408, but that file is LIVE PRODUCTION later projects are ordered to edit; the Z6 R5 receipt line flips that closed round's criterion PASS -> FAIL, and the flip is invisible until the edit is committed because the check reads HEAD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-13 ~21:18Z, working tree dirty with the R5 edit: bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e7.AC1.sh printed 'header consumers named 3 of 3; code AST equal to cut=yes; compiles=yes' / 'RESULT: PASS'.",
      "MEASURED the same minute, the same AST comparison run against the three refs side by side: cut(c8df03c408)=39398 bytes, HEAD=39750, worktree=40285; AST cut==HEAD True, AST cut==WORKTREE False. The check passes today ONLY because `git show HEAD:<file>` cannot see an uncommitted edit; it reads FAIL once the R5 commit lands.",
      "READ, e7.AC1.sh:1-7, its own BOUND clause: 'the module's code is UNCHANGED against the round-2 cut -- its AST with the module docstring removed is equal (comments are invisible to the AST)'. A comment-only edit would pass; the R5 receipt is a print statement, so it is an AST node.",
      "READ, CTO ruling @61e3067f5c disposition 5 and OPAL_BBGTML.TO-Z6-R5: the receipt line is the ORDERED act on this file, so the two contracts are in direct conflict by construction, not by accident.",
      "NEGATIVE CONTROL, same sweep: the sibling f15.AC1.sh also reads FAIL ('skill absent at HEAD'), but its subject is `git -C opal_ai show` of opal/agent/skills/bbg-teams-assist/SKILL.md in the SEPARATE opal_ai repo -- pre-existing and NOT caused by this edit."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "e7.AC1.sh grades NFRA_OPALAI OA-e-7 by asserting that teams-watch.py's AST equals the round-2 cut c8df03c408, as a standing acceptance criterion of a closed round.",
  "world_is": "An AST-equality freeze on a file whose own order-of-record tells other projects to change it is a criterion that must fail on the next authorized edit. It is not a defect in the R5 act and not a reason to withhold it: it is a grading instrument outliving the state it graded. Any later cell touching this engine inherits the same flip.",
  "notes": "Surfaced, not chased -- and NOT edited: TO-Z6-R5's bounds are exactly two files and its step 2c says to file a row for a consumer needing a change this order does not carry. This is a READER of the file, not a launcher, so the stdout contract is untouched: it never runs main() and never reads stdout. The launcher question itself came back clean -- the census found NO script, task or cron that execs the module (see the R5 deliverable). Disarm candidates for the owner to route to NFRA_OPALAI's issuer: re-cut e7.AC1's base to the post-R5 commit, or narrow the criterion from whole-module AST equality to the properties it actually means to protect (the header's 3 named consumers, py_compile, and the runner's empty stdout -- all three still hold at the worktree bytes)."
}
```

### OPAL_BBGTML-Z-S19 -- R6's twin, PORTAL_RETRIEVAL.md, still states `as_of_date` flat as the mdpf-platinum vintage field, and the tool it is twinned to says "keep in sync"

Filed by 0.7.0_AE_CloudOps~ZS executing TO-Z6-R6 step 3, which directs this row instead of an edit. The twin's RULE is not in conflict; its CHANNEL TABLE is now out of date.

```json
{
  "id": "OPAL_BBGTML-Z-S19",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZS",
  "surfaced_at": "2026-10-14T00:55Z",
  "one_line": "R6 replaced the flat `vintage_field: as_of_date` for platinum/mdpf/ with a three-step order in BUCKET_ALLOWLIST.yaml and in portal_lookup.py, but refs/PORTAL_RETRIEVAL.md:43 still prints `as_of_date` as THE vintage field for mdpf-platinum -- and the object it describes carries no as_of_date at all, so the twin now names a field that is absent from every aum-metrics.json measured.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ at HEAD, refs/PORTAL_RETRIEVAL.md line 43, bytes printed: '| mdpf-platinum | `platinum/mdpf/` | `as_of_date` | 461 objects; per-firm mirrors + `aggregate_aua/YYYY-MM-DD.json` daily snapshots since 2024-11-01 with reconciliation PASS/FAIL + provenance blocks -- richest MDPF surface |'. Line 42 is the separate `mdpf` row (`period`) and is NOT this finding.",
      "READ portal_lookup.py line 46 at HEAD: '# name -> {prefix, date_field, note}. Twin of refs/PORTAL_RETRIEVAL.md -- keep in sync.' The sync obligation is stated in the code this cell edited, so the two are now knowingly divergent.",
      "MEASURED 2026-10-14 ~00:4xZ, read-only S3 GET of four objects (the denominator is those four, not the 461-object prefix): platinum/mdpf/{49financial,global,cottonwood,inflection}/aum-metrics.json each returned as_of_date=None, exactly 1 source in _provenance.source_vintages, and 1 distinct date, 2026-10-12 in all four.",
      "NOT CONTRADICTED, and this is the half that matters: PORTAL_RETRIEVAL.md:13 rule 2 reads 'ANSWER FROM `data_as_of` (MDPF uses `period` / `as_of_date` -- same meaning: the data's as-of, never the run date)'. R6 follows that rule rather than breaking it -- the rule is silent on what to do when the named field is ABSENT, which is the whole gap R6 fills."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-Z6-R6 the_act item 3: 'Read refs/PORTAL_RETRIEVAL.md (portal_lookup.py:46 calls it the twin). If it states a vintage rule this edit contradicts, do NOT edit it: file a row naming the line.' The order's bounds also cap the cell at exactly two files, so the twin was out of the write surface either way.",
  "world_is": "The twin's RULE agrees with R6; the twin's TABLE ROW is stale. A BG-seat agent reading the table for mdpf-platinum is told to look for as_of_date, finds nothing, and is then on its own -- which is the exact path that produced the one-trading-day-too-fresh answers R6 was cut to stop. The tool now prints the right vintage regardless, so the stale line misleads a human reader of the doc rather than the tool's output.",
  "notes": "Remedy is one table cell, owned by whoever may write org/tier0_utility/0.0.3_BG_BBGTerminal/refs/ (this seat held a one-commit GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_UTILITY grant for R6's two named files only, and did not stretch it to a third file). Suggested text, matching the landed allowlist: 'as_of_date, then _provenance.source_vintages (oldest when several), then none -- LastModified is WRITE TIME only'. Low urgency: nothing serves off this line mechanically. NOT a blocker on R6, whose AC1 and AC2 both PASS."
}
```

### OPAL_BBGTML-Z-S20 -- disarm record: Z-S17 answered by Andrew's 'no hold' (R2 stays, R3 released); Z-S14 parked by Andrew's 'not a priority, TCKT is dell2's'

Filed by 2.0.0_SA_COO~ZB at the Z6 drain end.

```json
{
  "id": "OPAL_BBGTML-Z-S20",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZB",
  "surfaced_at": "2026-10-14T09:35:59Z",
  "one_line": "Disarm record for the two ARMED rows this seat owns: Z-S17 (the no-modify reading) is ANSWERED by Andrew-direct 2026-10-14 ~09:0xZ, 'There should be no hold', so R2 stays and R3 is released; Z-S14 (the expired intake fetch token) is PARKED by Andrew-direct 2026-10-13 ~20:5xZ, intake 'not a priority right now + TCKT work is on DELL2', so nothing re-mints the token or moves the pin from site Z.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_090xZ_NO_HOLD_ON_BLOOMBERG_SIGN_IN_REPAIRS.md (CLOUD @dd20a5edf4): VERBATIM 'What is the hold you are referring to? There should be no hold'; call sitez-20261013T215225Z-6c9f CLOSED --ruled-by andrew (open-calls.py close refused at 09:2xZ as already CLOSED). Acts: revert cron deleted; TO-Z6-R3 released @b066255b05.",
      "READ org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_205xZ_TICKET_INTAKE_NOT_PRIORITY_TCKT_IS_DELL2.md (CTO msg 33761); TO-Z6-R4 cancelled @ed9719f0b4; both never-widen halves marked WITHDRAWN. No re-mint, backlog read or pin edit ran: runner_config.json line 11 is unchanged at HEAD and the secret's AWSCURRENT is unchanged (no act of this seat or its lanes wrote it)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Z-S17 and Z-S14 each read hazard_standing ARMED with disarm_owner 2.0.0_SA_COO~ZB.",
  "world_is": "Z-S17's hazard (an edit to a held surface) no longer exists: Andrew says there is no hold, and what binds is only 'do not accidentally overwrite Positioning pipeline or ETFS view operations'. Z-S14's hazard (a first good intake pass posting a backlog into the client ticket channel) cannot fire from site Z: it needs a re-mint AND the pin, and both are withdrawn by Andrew's word. It re-arms only if someone re-opens the intake fix; that work is TCKT's on dell2.",
  "notes": "A new citing row rather than an in-place edit, because rows are append-only. Graduation of Z-S14..S19 is the CVO's. The OPAL_BBGTML Z6 drain-end message to 1.0.0_SA_CTO~Z carries all of Z-S14..S20."
}
```

```json
{
  "id": "OPAL_BBGTML-Z-S21",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZS",
  "surfaced_at": "2026-10-15T05:59:03Z",
  "one_line": "The sign-in fill's verify step prints an OCR read of the login NAME to stdout (a line 'username OCR (observation only): <value> similarity N%'), so any tee of a fill run, and every scheduled-pull log that goes through the fallback, carries the name; the order says never print or log a credential and the tool's own banner says values are never printed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZB",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "TO-Z6-R3 AC1 run 2026-10-15T05:44Z: two fills each printed '[fallback]   username OCR (observation only): <the name> similarity 100%' right after 'PHASE FILL. user_len=12 pw_len=9 (values never printed)'",
      "Grep of C:/Users/Opal Bloomberg/opal_bbg_logs for 'username OCR': 16 occurrences across 13 pull logs (bbg_tplus1_20260917 .. 20261013), so the line is routine, not new",
      "org/tier2_senior/0.7.0_AE_CloudOps~ZS/deliverables/z6_r3_exercise.log carries the line with the value REDACTED before commit (grep for the name: 0 hits); the pull logs live under the user profile and are not in the repo"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-Z6-R3 bounds: 'never print, log or commit a credential'; bbg_signin.ps1 prints 'values never printed' for the user and password lengths.",
  "world_is": "The password is never printed. The login NAME is, via an OCR observation line the verify step adds. Whether the name counts as a credential for that bound is the issuer's reading; it is a login identifier, not a secret, but it IS printed in a stream the order tells the seat to tee into a committed deliverable.",
  "notes": "No act owed here and nothing was changed. If the reading is that it is a credential, the fix is one line in the verify step (print the similarity only). This seat redacted its own copy and committed only the redacted log."
}
```
