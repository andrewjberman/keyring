# TO NFRA_TRNSPT.TO-TR-l14 -- the commentary Lambda: handler wiring H2 -> H6, its NAMES.json, its Terraform (DESIRED, plan only)

<to_id>NFRA_TRNSPT.TO-TR-l14</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-l-14` (`decompositions/NFRA_TRNSPT_DECOMP_R14.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-l-14`: the one deployable unit of FWD-10's journey. IRPT_BCKEND (`~P2`) cuts the READY stream (H1) only once
`outlook-global-commentary-draft-lambda` exists; this cell builds it as code and Terraform, NOT applied.

**The pieces you wire (all merged, READ them):** `data/transcripts/scripts/commentary/entry.py` (`handler(event, context, reader)` -> per
record `abstract_request` + `ticket_context`, never raises), `drafter.py` (`draft(request, gold_rows, *, model, wipe_gate_passed, now=...)`,
`KimiAdapter(http_post=, api_key_reader=, url=)`), `ticket_client.py` (`write_draft_ticket(draft, ticket_context, *, post, token_reader)`,
`stub_post`). Contracts: `org/standards/NFRA_TRNSPT_READY_EVENT_CONTRACT.json` (agreed by ~P2) and
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` v0.1. Pattern to copy for the
Terraform: `infra/aws/terraform/transcripts/mail_pull.tf` (names read from a `NAMES.json` of builder output, its own role and policy, the shared
`infra/aws/lambda/transcripts-pull/build.sh` bundle, python3.11 with the pandas-pyarrow layer from `pull.tf`, no alarm/SNS).

**Build:**
1. `data/transcripts/scripts/commentary/NAMES.json`: rows `lambda`, `role`, `policy`, `queue`, each `{system: "outlook", scope: "global",
   function: "commentary-draft", kind, qualifier: null, name}` where `name` is EXACTLY `lib.opal_naming.name(system, scope, function, kind)`
   (generate it with the builder; never type a name -- the commit gate REFUSES hand-typed names). Add `"_provenance"`.
2. `data/transcripts/scripts/commentary/lambda_handler.py`: `lambda_handler(event, context, ports=None)`. `ports` (injected in tests; built
   from env + boto3 in `_live_ports()` only when `ports is None`): `composition_reader(request_id)`, `gold_rows()` (non-held-out gold rows;
   empty list today), `model` (a `KimiAdapter` when env `KIMI_STANDING_WORD_REF` is non-empty, else `None`), `post`, `token_reader`,
   `wipe_gate_passed` (env `WIPE_GATE_RECORD` non-empty). Flow per record: `entry.handler` -> if `model is None`: record
   `{"stage": "no_vendor_word"}` and STOP (no model call, no ticket) -> `drafter.draft(...)` -> `ticket_client.write_draft_ticket(...)`.
   Returns `{"results": [...], "failed": [...]}`; NEVER raises; logs request ids only, never prompt or draft text. `_live_ports()` reads names
   only from env (bucket/key prefixes, secret ids, the ticket API base); no hard-coded resource name.
3. `infra/aws/terraform/transcripts/commentary.tf` (NEW; DESIRED; header says "NOT APPLIED -- plan only until CALL 1 and the irpt-key leg"):
   `aws_lambda_function` (name from NAMES.json, handler `data.transcripts.scripts.commentary.lambda_handler.lambda_handler`, the shared zip),
   `aws_sqs_queue` DLQ (queue name from NAMES.json), `aws_iam_role` + `aws_iam_role_policy` (logs to its own group; s3:GetObject on
   `outlook/transcripts/gold/*` in the transcripts bucket; secretsmanager:GetSecretValue on `astn/kimi/api-key`; sqs:SendMessage to its DLQ;
   kms via an `aws_kms_grant` on the transcripts key like mail_pull.tf), env vars `KIMI_STANDING_WORD_REF = ""` and `WIPE_GATE_RECORD` = the
   CTO's round-12 analysis path. The IRPT composition read and the `irpt` key decrypt are LEFT OUT with a comment naming them as the laptop leg
   (a key another box uses). No event source mapping (H1 is ~P2's). Run `terraform fmt` on the file.
4. `data/transcripts/scripts/tests/test_commentary_lambda.py` with all ports faked (synthetic data; import the entry fixtures by path): at least
   `test_full_path_lands_ticket` (model fake, `stub_post`: result `action: done`) and `test_no_vendor_word_never_calls_model` (model `None`: a
   counting fake proves 0 calls, no `post` call, stage `no_vendor_word`); a test that a port exception lands in `failed` and nothing raises.

### ACCEPTANCE

<criterion id="TR14-l14-AC1" cell_refs="TR-l-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R14_CHECKS/r14_checks.py l14</invocation><expect>R14-L14-OK</expect></criterion>
`TR14-l14-AC1` -- the full faked path lands a ticket; with no vendor word the model is never called.

<criterion id="TR14-l14-AC2" cell_refs="TR-l-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R14_CHECKS/r14_checks.py l14n</invocation><expect>R14-L14N-OK</expect></criterion>
`TR14-l14-AC2` -- every NAMES.json row equals the builder's output.

<expected_criteria>TR14-l14-AC1, TR14-l14-AC2</expected_criteria>

Dry-run at the base (box/dell2 1440a9d3d1): both FAIL (absent) -- as expected. Keep every `test_commentary_*.py` green. The plan run is the
issuer's.

## BOUNDS

- **Grant.** The four paths below, this order's file, your deliverables folder. Everything else READ only.
- **WORLD by path floor (infrastructure Terraform); NOTHING is applied.** No `terraform apply` or `plan`, no AWS, HTTP, model or gateway call, no secret read. `terraform fmt` only.
- **Refusal clause.** If the builder refuses a name, do not type one: file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across
  every document under `surprise-channel/`) naming the missing registry row, and stop on AC2.

<paths>
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/NAMES.json
infra/aws/terraform/transcripts/commentary.tf
data/transcripts/scripts/tests/test_commentary_lambda.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R14.md</decomp_doc> (round 14), cell `TR-l-14`.
<owned_cells>TR-l-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR14-l14-AC1, TR14-l14-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-l14.commentary-lambda.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR14-l14-AC1,TR14-l14-AC2` BEFORE the flip. Commit code first, then pin each
artifact to a commit that contains it.
</proof_of_spec>

**REPORT:** the NAMES.json rows, the handler's stages, the Terraform resource list, the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- DESIRED Terraform, no apply; the trigger is ~P2's stream.
comp-iam: RUN at plan time by the issuer (the role's policy is new IAM; Step F lets dell2 apply roles/policies, reported after the fact).
comp-adversary: RUN -- 6 sources read (entry, drafter, ticket_client, both contracts, mail_pull.tf); BLIND to the IRPT composition bucket and the irpt key (left out as the laptop leg) and to the live ticket API (H5 not live). Traps: a hand-typed name, a model call without Andrew's word, an apply from a worker, transcript text in logs; the face forbids each.
lane: one handler, one names file, one Terraform file, one test, the investigation file.
</preflight>

Source: `/next-calls NFRA_TRNSPT --drive` (2026-10-09, keep-driving on); decomposition round 14 cell TR-l-14 and issuer rulings 1-2.
