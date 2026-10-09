# ETFS_RIVALS task order -- `RIV-wj-1` -- WORKSTREAM 3: THE GENERATED STACK GRANTS THE DAILY LAMBDA ONE READ OF THE BRIGHT DATA KEY SECRET

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~33</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: RUN -- this cell adds ONE IAM statement (GetSecretValue on one exact ARN) to the daily Lambda's GENERATED policy file only; nothing is applied here (the RIV-wi-1 deploy pair applies it)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL 2 as expected; limbs (2) and (4) PASS)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wj-1` -- the generated stack grants the daily Lambda ONE read of the existing Bright Data key secret and names it in that Lambda's environment (CTO ruling ADDENDUM 7; RIV-wi-1's grant) -- APPENDED 2026-10-09, revision 1.27
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 7 @aa290d707e
  (1.0.0_SA_CTO~DELL1 msg 2555): option (a) -- GetSecretValue on exactly
  `arn:aws:secretsmanager:us-east-1:313476888478:secret:find-insure/bright-data/api-key-7ojPkd`, no wildcard, no other
  action, no copy of the secret; `BD_SERP_ZONE` stays plain environment; the generated policy diff shows ONE new
  statement. Row D1-S11 tells FIND_INSURE's owner of the second consumer.
- Measured (14:2xZ, key names only): the SERP key is `find-insure/bright-data/api-key` (a raw string);
  `find-dualbiz/bright-data/serp` names it as `api_key_secret` and gives `zone` = `serp_opal`. RIV-wi-1 (merged
  @e17ab4e69d) reads the key from `BRIGHT_DATA_API_KEY`, else from the secret named by `RIVALFUNDS_SERP_SECRET`, and the
  zone from `BD_SERP_ZONE`. The stack's one existing secrets grant is the OpenAI secret (`gen_policies._ai_secret`,
  statement `GetOpenAISecret`, the daily Lambda's environment `RIVALFUNDS_AI_ENABLE`, `RIVALFUNDS_OPENAI_SECRET`).
- Interface (`infra/aws/terraform/etfs-rivalfunds/gen_policies.py` and its committed outputs):
  1. A constant for the ONE ARN with a comment citing ADDENDUM 7 (a foreign secret has no builder home; R19: this existing
     pipeline is not migrated by this cell).
  2. For the sweep stage (the daily Lambda) only: one more statement, `Sid` `GetSerpSecret`, `Effect` `Allow`, `Action`
     `["secretsmanager:GetSecretValue"]`, `Resource` `[<the ARN>]`; and the environment gains `RIVALFUNDS_SERP_SECRET` =
     the ARN and `BD_SERP_ZONE` = `serp_opal`, keeping its two keys.
  3. The committed `generated.auto.tfvars.json` and `policies/*.json` are regenerated with `--out
     infra/aws/terraform/etfs-rivalfunds` and equal a fresh regeneration (line endings aside).
- Out of bounds: every `.tf` file, every other Lambda, any `terraform plan` or `apply`, any AWS call; the rivalfunds code.
- Check: `ws3_item8_prep/wj1_serp_grant_check.py` (AC1; base FAIL 2: limbs (1) and (3); limbs (2) and (4) PASS at the
  base and must keep passing).

### The workstream's guards (verbatim)

GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the 2026-10-09 11:00Z
vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (a cell that
finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build. It FAILS at the base (2 failures) and is your target; do not edit it.
  `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wj1_serp_grant_check.py` regenerates
  the stack into a temp dir and compares it with the committed copies at e17ab4e69d.
- `infra/aws/terraform/etfs-rivalfunds/gen_policies.py`: `AI_STAGE_KEY` = "sweep" (~line 62), `_ai_secret()` (~76),
  the per-stage loop (~224-268) where `GetOpenAISecret` and the daily environment are added for the sweep stage. Run it as
  `python infra/aws/terraform/etfs-rivalfunds/gen_policies.py --out infra/aws/terraform/etfs-rivalfunds`. The
  committed outputs are `generated.auto.tfvars.json` and `policies/<lambda>.json`. Standard library only; ASCII only.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including every `.tf` file, `lib/`, the rivalfunds code, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~33/`).
NEVER: any AWS call (no Secrets Manager read, no IAM, no S3), any `terraform` command, any deploy. A row you file goes in
the investigation file below with id `ETFS_RIVALS-D1-W33-S<k>`, `"fabric": "dell1"`.

<paths>
infra/aws/terraform/etfs-rivalfunds/gen_policies.py
infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json
infra/aws/terraform/etfs-rivalfunds/policies/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- one new statement on exactly the ARN, the daily environment gains the two keys, nothing else moves, the
  committed copies equal the regeneration.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wj-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wj1_serp_grant_check.py</invocation><expect>WJ1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~33/ETFS_RIVALS.TO-RIV-wj-1.serp-secret-grant.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wj-1.serp-secret-grant`. Report once: AC1's verdict line with the output above it; files
written; the new statement and environment verbatim (the ARN is not a secret value); rows filed (id + one line); anything
the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** RIV-wi-1's grant, placed by 1.0.0_SA_CTO~DELL1 ruling ADDENDUM 7 @aa290d707e
(msg 2555), option (a). Decomposition revision 1.27. Cell id and slot listed before naming (0 hits for RIV-wj-1, slot
~33, workstream 3h). Check dry-run at the base (e17ab4e69d + amendment commits): WJ1 RESULT: FAIL 2 failures ((1), (3));
(2) and (4) PASS -- (4) normalizes line endings because a Windows checkout writes CRLF (193 CRLF in the daily policy as
checked out; equal after normalization). Applied only by the RIV-wi-1 deploy pair.

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>28</round>
<workstream>3h</workstream>
<slot>~33</slot>
<fabric>dell1</fabric>
