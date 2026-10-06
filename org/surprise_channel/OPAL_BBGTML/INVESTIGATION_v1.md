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
