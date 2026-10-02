# ETFS_RIVALS task order -- `RIV-ap-1` -- ROUND 6 (ENRICHMENT): THE AI ACCOUNTS AS A PRODUCTION STAGE (analysis cell 1, RFW-D08)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ap-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: RUN at L5 -- `comp-iam service etfs-rivalfunds-daily-lambda`: role etfs-rivalfunds-daily-role; the AST op list reads 0 operations because it sees only the wrapper lambda_function.py (blind to the package's boto3 calls); the live publish-page policy read 2026-10-02 13:4xZ holds 5 statements and no secretsmanager action on any rivalfunds role
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ap-1` -- the AI accounts as a production stage (analysis cell 1; RFW-D08)
- New `rivalfunds/ai_stage.py`: `run_for_day(sink_spec, day)` runs `ai_accounts.run_day(day, sink_spec,
  client=ai_client.default_client(), provenance={"run_path": "scheduled", ...})` when `RIVALFUNDS_AI_ENABLE == "1"` and the
  page day holds no `research_hypotheses` object. It is a no-op on a second call for the day (CALL 5).
- New `rivalfunds/ai_client.py`: `RestClient(api_key).chat(messages, model)` POSTs with `requests` (already in the layer) to
  https://api.openai.com/v1/chat/completions with `Authorization: Bearer`, model, messages, `response_format` json_object and
  temperature 0.2, and returns choices[0].message.content. `default_client()` builds a RestClient from the secret named by
  `RIVALFUNDS_OPENAI_SECRET`, read at call time. Web search is unavailable in the Lambda (VEW-2: a fallback only).
- The dedicated secret is named by `name()` (add an LGIC registry row if the builder refuses).
- `gen_policies.py`: `secretsmanager:GetSecretValue` on that ONE ARN, to the daily role alone. Its generated `lambdas` map
  gives the daily Lambda an `environment` {RIVALFUNDS_AI_ENABLE: "1", RIVALFUNDS_OPENAI_SECRET: <name>}; `main.tf` passes it
  through.
- The secret's value is set by the issuer at the deploy. Tests stub the transport.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- `ai_accounts.run_day(page_day, sink_spec, client, run_id, model, provenance, funds)` writes ONE append-only object per run; `default_client()` today builds the `openai` SDK client, which the Lambda layer (`pandas-pyarrow-requests`, main.tf:93) does not carry; `requests` it does.
- The publish stage builds the A1 tables in `publish_page.produce_a1`; the hookup calling `ai_stage.run_for_day` after it, and `ai_accounts.default_client` delegating to `ai_client.default_client`, are the ISSUER's merge hookups -- do not edit publish_page.py or ai_accounts.py.
- Only the daily Lambda may carry the gate: the 07:00 ET marker-driven publish runs in the publish-page Lambda and must never call the vendor; the 09:00 ET sweep runs in the daily Lambda.
- `gen_policies.py --out infra/aws/terraform/etfs-rivalfunds` regenerates `generated.auto.tfvars.json` and `policies/*.json`; main.tf reads the `lambdas` map. Names come from `lib/opal_naming.py name()`; a builder refusal is a registry row under `infra/logic/registry/`, never a typed name.
- VEW-2 (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`) covers OpenAI for this chain; web search is a fallback only and stays unavailable in the Lambda.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6ap1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/ai_stage.py
data/etfs/scripts/rivalfunds/ai_client.py
data/etfs/scripts/rivalfunds/tests/test_r6ap1_*.py
infra/aws/terraform/etfs-rivalfunds/gen_policies.py
infra/aws/terraform/etfs-rivalfunds/policies/
infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json
infra/aws/terraform/etfs-rivalfunds/main.tf
infra/logic/registry/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- ai_stage.run_for_day writes exactly one research_hypotheses object with the gate set, and a second call writes nothing; control: gate unset writes nothing (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC1.py`)
- **AC2** -- ai_client.RestClient posts the documented chat-completions request; default_client builds it from the named secret, read at call time (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC2.py`)
- **AC3** -- only the daily role reads secrets (GetSecretValue on ONE ARN), and only the daily Lambda carries the gate and the secret name (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the first scheduled account reads as well as a seat run's; positive control: the 2026-10-02 accounts, run 20261002T110438Z-ai-rg4

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ap-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ap-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ap-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ap-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ap-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-ap-1.ai-accounts-production-stage.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ap-1.ai-accounts-production-stage`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~1`, slot `~1`, position 2 of 3 (st-1 -> ap-1 -> r-6). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
ap-1.AC1 FAIL (ImportError ai_client/ai_stage) as expected; ap-1.AC2 FAIL (ImportError) as expected; ap-1.AC3 FAIL (no secretsmanager grant, no environment) as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~1</slot>
<fabric>site-z</fabric>
