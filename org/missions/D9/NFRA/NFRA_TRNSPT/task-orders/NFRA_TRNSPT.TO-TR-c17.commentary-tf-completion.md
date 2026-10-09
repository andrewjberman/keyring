# TO NFRA_TRNSPT.TO-TR-c17 -- complete commentary.tf so the Lambda can run live (row D2-S8)

<to_id>NFRA_TRNSPT.TO-TR-c17</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-c-17` (`decompositions/NFRA_TRNSPT_DECOMP_R17.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-c-17` (CTO msgs 2259 and 2293; row NFRA_TRNSPT-D2-S8). `C:\dev\ajb_workspace\data\transcripts\scripts\commentary\lambda_handler.py`
`_live_ports()` (:45-87) reads five env names that `C:\dev\ajb_workspace\infra\aws\terraform\transcripts\commentary.tf` does not declare
(its env, :113-118, holds only `KIMI_STANDING_WORD_REF` and `WIPE_GATE_RECORD`): `COMPOSITION_BUCKET`, `COMPOSITION_KEY_PREFIX`,
`TICKET_API_BASE`, `KIMI_API_URL`, `TICKET_TOKEN_SECRET_ID`. Its policy (:51-82) reads only the model key secret `astn/kimi/api-key-*`. And
`token_reader` returns the whole SecretString, but the ticket secret's value is JSON with the bearer in `.token` (contract v0.2,
`C:\dev\ajb_workspace\org\missions\D7\TCKT\TCKT_VNEXT\deliverables\2.0.0_SA_COO~V2\FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` :25-26, :110).
Work in your worktree; every path above is relative to the repo root there.

**Build:**
1. `commentary.tf` env -- declare all five, plus `KIMI_STANDING_WORD_REF = "4d77a9c3ea"` (the open-egress law edit; CTO msg 2252):
   - `TICKET_TOKEN_SECRET_ID = "opal/ticketing/svc-commentary"` (contract :110).
   - `KIMI_API_URL = "https://api.moonshot.ai/v1/chat/completions"` -- the estate constant
     (`infra/aws/lambda/investor-reporting/ycharts/generate/kimi_port.py:18`); cite it in a comment.
   - `TICKET_API_BASE` -- MEASURE the base the ticket write path `POST {api_base}/api/scoped/tickets` is served at (contract :25; the Ticket
     Center's API in `infra/aws/lambda/ticket_center/` and its Terraform, or ~V2's run record
     `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/`). Cite the source line in a comment.
   - `COMPOSITION_BUCKET` + `COMPOSITION_KEY_PREFIX` -- MEASURE where IRPT retains the analysis composition
     (`infra/aws/lambda/investor-reporting/reports/request_composition.py` and its caller's S3 write), so that `prefix + request_id + ".json"`
     is the object `composition_reader` reads (lambda_handler.py :56-61). The values must be `lib/opal_naming.py address()` output, read the way
     `commentary.tf` reads `NAMES.json` (record them in `data/transcripts/scripts/commentary/NAMES.json` under a `composition` key with the
     builder call that produced them), never typed. If the composition is not retained as one object per request id, or `address()` refuses,
     leave both values empty, say so, and file the row (see BOUNDS).
2. `commentary.tf` policy -- add `secretsmanager:GetSecretValue` on `arn:aws:secretsmanager:*:*:secret:opal/ticketing/svc-commentary-*`;
   `s3:GetObject` on the composition prefix; `kms:Decrypt` on the `irpt` key ARN, resolved by a data source or a reference the estate already has
   (never a typed ARN). Update the header comment: the file is no longer held by "CALL 1"; it is held only by its never-widen pair.
3. `lambda_handler.py` -- `token_reader` returns `json.loads(secret)["token"]`; the Kimi `api_key_reader` keeps the estate's shape (the plain
   key string, as `kimi_port.py` reads it). Nothing else changes.
4. `data/transcripts/scripts/tests/test_commentary_live_ports.py` (new), LOCAL, no AWS:
   `test_tf_env_declares_every_live_port_name` (parse lambda_handler.py for every `env.get("<NAME>"` and assert each NAME is declared in
   commentary.tf's `environment.variables` block); `test_token_reader_reads_the_token_field` (patch the boto3 secrets client with a fake returning
   `'{"token": "abc"}'`; `token_reader()` returns `"abc"`); `test_policy_reads_ticket_secret_and_composition` (the policy text names the
   svc-commentary secret pattern and an `s3:GetObject` on the composition prefix). Keep every `test_commentary_*.py` green.
5. If `terraform` resolves (`.tools/terraform.exe` or PATH), run `terraform fmt -check` and `terraform validate` in
   `infra/aws/terraform/transcripts` after `terraform init -backend=false`; report each result. Never plan or apply.

### ACCEPTANCE

<criterion id="TR17-c17-AC1" cell_refs="TR-c-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R17_CHECKS/r17_checks.py c17</invocation><expect>R17-C17-OK</expect></criterion>
`TR17-c17-AC1` -- the three named tests pass and the live-ports test file is green.

<expected_criteria>TR17-c17-AC1</expected_criteria>

Dry-run at the base (box/dell2 ce7106eecf): `R17-C17-FAIL absent: data/transcripts/scripts/tests/test_commentary_live_ports.py` -- FAIL as
expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call, no plan, no apply, no HTTP; fakes only. The apply is the issuer's, under a pair.
- **Refusal clause.** If the composition is not retained per request id, or `address()` refuses its address, or the ticket API base has no
  source you can cite, leave that value empty, keep the rest, and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every
  document under `surprise-channel/`). Never type a bucket, prefix, ARN or URL you did not measure.

<paths>
infra/aws/terraform/transcripts/commentary.tf
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/NAMES.json
data/transcripts/scripts/tests/test_commentary_live_ports.py
data/transcripts/scripts/tests/test_commentary_lambda.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R17.md</decomp_doc> (round 17), cell `TR-c-17`.
<owned_cells>TR-c-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR17-c17-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-c17.commentary-tf-completion.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR17-c17-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** each env value with its source line, the composition address and the builder call, the policy statements added, the token change,
the test names, the check line, terraform fmt/validate results (or "terraform not resolved"), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the trigger is H1's event source mapping (IRPT_BCKEND), outside this cell.
comp-iam: RUN -- 1 policy read (commentary.tf :51-95, 4 statements + 1 grant); the cell adds 3 statements on the IAM side; the irpt key-policy side is the laptop's and is simulated at apply (CTO msg 2259).
comp-adversary: RUN -- 4 sources read (lambda_handler.py :45-87, commentary.tf, contract v0.2 :25-26 and :110, kimi_port.py :18); BLIND to the composition's S3 home and the ticket API base, which the worker measures. Traps: a typed bucket or ARN, a Bearer of the whole JSON, a widened secret pattern; the face fixes each.
lane: one .tf, the handler, NAMES.json, two tests, the investigation file.
</preflight>

Source: CTO msgs 2259, 2293 (analysis ADDENDUM 4); row NFRA_TRNSPT-D2-S8; decomposition round 17 cell TR-c-17 and issuer rulings 1-4.
