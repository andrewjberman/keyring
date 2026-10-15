# ETFS_RIVALS task order -- `RIV-yb-1` -- THE RIVALFUNDS AI WRITER RUNS ON gpt-6-astra AND SENDS A REQUEST THAT MODEL ACCEPTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-yb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~44</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-yb-1` -- the rivalfunds AI writer runs on `gpt-6-astra`, and the request it sends is one that model accepts (Andrew at the `~RV` terminal 2026-10-15) -- APPENDED 2026-10-15, revision 1.32
- Placement: Andrew's word above; the 2026-10-15 13:00Z sweep graded 24 of 26 AI items grounded on `gpt-5.4`, with TXUE's two items served as Grounding FAIL after the one allowed correction (row ETFS_RIVALS-D1-S18).
- Measured (2026-10-15, the live API with the project key `rivalfunds/openai-api-key`, read-only calls): `gpt-6-astra` is listed among 133 models; a chat completion with `response_format` json_object and NO `temperature` returns 200; the same request with `temperature: 0.2` (what both clients send today)
  returns HTTP 400 "'temperature' does not support 0.2 with this model. Only the default (1) value is supported", so changing only the model string would fail EVERY AI call. `gpt-5.4` accepts both. A trial of the production chain (prompt `a1-chain/8`, nothing written) on `gpt-6-astra` for TXUE returned both
  items PASS with 0 corrections where `gpt-5.4` returned FAIL after 1. The live Lambda sets `RIVALFUNDS_AI_ENABLE` and `RIVALFUNDS_OPENAI_SECRET` and NO `RIVALFUNDS_AI_MODEL`, so the model in force is the code default `ai_accounts.DEFAULT_MODEL`.
- Interface: (1) `ai_accounts.DEFAULT_MODEL` defaults to `"gpt-6-astra"` (the env var `RIVALFUNDS_AI_MODEL` still overrides). (2) `ai_client.RestClient.chat` and `ai_accounts.OpenAIClient.chat` send `temperature` (0.2) ONLY when the model name starts with "gpt-5"; for every other model the key is omitted; nothing else in either
  request changes. (3) `PROMPT_VERSION` and every prompt constant are unchanged: the stored `model_version` column is how a row names the model, and the page footer prints it.
- Out of bounds: the prompts, `PROMPT_VERSION`, the grounding and wording checks, `run_chain`, `render.py`, Terraform and the Lambda environment (no env key is added), any vendor call, any Secrets Manager call.
- Checks: `round31/checks/yb1_model_gpt6_astra_check.py` (AC1 the default and the override, one test; AC2 the two clients, two tests; base FAIL 3). The grounded-count comparison on the live sweep is the CVO's J1 read after the deploy: on the first 13:00Z sweep after the deploy, `model_version` reads `gpt-6-astra` on 26 of 26 rows and the
  Grounding FAIL count is no greater than the 2 of 26 of 2026-10-15.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/yb1_model_gpt6_astra_check.py`. It FAILS at the base (3 failed) and is your target; do not edit it. It replaces `requests.post` and the `openai` SDK with recorders, so it needs no network and no key.
- `ai_accounts.py:48` is `DEFAULT_MODEL = os.environ.get("RIVALFUNDS_AI_MODEL", "gpt-5.4")`. `ai_client.RestClient.chat` (about line 31) posts `{"model", "messages", "response_format", "temperature": 0.2}`; `ai_accounts.OpenAIClient.chat` (about line 876) calls `chat.completions.create(..., temperature=0.2, max_completion_tokens=1500)`.
- The rule is by NAME, not by a list: send `temperature` (0.2) only when `str(model).startswith("gpt-5")`; otherwise omit the key. Do not touch `max_completion_tokens` in `OpenAIClient` and do not add one to `RestClient`.
- Several tests may assert the request body or the default model string; run the suite, and change a test assertion only where it names `gpt-5.4` as the DEFAULT or expects `temperature` for a non-gpt-5 model; list each one you change and why.
- AMENDMENT 1 (issuer, from your surprise row ETFS_RIVALS-D1-W44-S3): `rivalfunds/tests/test_r6ap1_ai_stage.py` is now in your `<paths>`. `test_rest_client_request_shape` (about lines 109-110) expects `"temperature": 0.2` for the model `"m"`, which is not a gpt-5 model: remove the `temperature` key from that expected dict and change nothing else in the file. Run the suite again; the failure count must return to the base's, with no new failure id.
- Regression net: `cd data/etfs/scripts && python -m pytest -q rivalfunds/tests`; report its final line.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~44/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W44-S<k>`, `"fabric": "dell1"`, `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/ai_client.py
data/etfs/scripts/rivalfunds/tests/test_riv_yb1_model.py
data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- `DEFAULT_MODEL` is `gpt-6-astra` when the env var is unset and the env var still overrides it.
- **AC2** -- both clients send `temperature` only for a `gpt-5` model and omit it for `gpt-6-astra`; the rest of each request is unchanged (the difference control is `gpt-5.4`).
- **J1** -- the CVO's read of the first 13:00Z sweep after the deploy, not yours.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-yb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/yb1_model_gpt6_astra_check.py -k ac1</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-yb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/yb1_model_gpt6_astra_check.py -k ac2</invocation><expect>2 passed</expect></criterion>
  <criterion id="J1" cell_refs="RIV-yb-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_yb1_model.py` only for a behaviour the check file does not pin. Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~44/ETFS_RIVALS.TO-RIV-yb-1.ai-writer-gpt-6-astra.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-yb-1.ai-writer-gpt-6-astra`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~RV):** Round 31, ONE issuance with RIV-ya-1. Andrew's word at this seat's terminal ("updated from 5.4 to 6", "gpt 6 astra") names the model; the id `gpt-6-astra` and the temperature refusal were measured by this seat against the live API (read-only) before the cut. A trial of the production chain on `gpt-6-astra` (nothing written) is recorded at the drain. Decomposition revision 1.32. Check file dry-run at the base before the cut: yb1 base: FAIL (3 failed) as expected. Chain B (`ai_accounts.py`, `ai_client.py`); no edge to chain A. The deploy is ONE act with ya-1's (a CloudOps seat, the five rivalfunds packages) under the round's never-widen pair; the CVO's J1 read follows the first sweep after it. Scope: Andrew's direct word at this terminal; the CTO is told in one line.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>31</round>
<workstream>2</workstream>
<slot>~44</slot>
<fabric>dell1</fabric>
