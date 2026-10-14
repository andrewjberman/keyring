# AMGT_RESAPP task order -- `AMGT-fa-7` -- THE SERVE: `read_ai_fill` AND THE `/thesis` BUNDLE'S `ai_fill` (FWD-41; A BUILD, NOT DEPLOYED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~422</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-7.the-serve-reads-the-fill-into-the-thesis-bundle</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell edits served code and its tests; no grant, key or policy is touched. NOTE for the deploy leg (not this order): the function role must read `amgt/harvest/gold/ai_fill/`; the issuer reads that with `comp-iam` before the store write.
comp-adversary: RUN at the cut -- `check_fa7_serve.py` is a prepared acceptance check (18 arms: the local-root and pool reads, the INVALID cases, the address equal to the builder's, the Lambda-safe imports); at the base before fa-9 14 of its 18 arms FAIL (`no attribute 'read_ai_fill'`) and the four control arms PASS (4 of 18); `check_api_suite_no_new_failures.py` at the base reads `YES (base 4 failing, now 4 failing, new 0, passed 969)`, a control passing as expected.
EGRESS CLASS, declared: NONE. No network call; the S3 client is faked and the local-root override is a temp directory.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-422` (branch `wk-AMGT_RESAPP-422`, cut from the merged head that carries cell fa-9 (the issuer cuts this worktree after fa-9 merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-422`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-7` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41's blocks reach the page through the existing `/thesis` route: the Exec Management and Thesis tabs, and (through the bundle the page already holds) the identity header's description line. You add the read of the fill document to `lib/research/api/scoped_amgt.py` and one wiring line to `read_thesis_bundle`. The overlay route gains NOTHING (no new read in any overlay path: the cold overlay is at 3.77 s against a 3.0 s target in this same round, and another seat owns that). The function is NOT deployed by this order; a later pair carries the apply.


### The contract every cell of this workstream writes against (ratified in the decomposition, inlined)

`fill/v1` document, one per security key, and its five blocks:
```
{ "schema": "aifill/v1", "security_key": "<K>", "as_of": "YYYY-MM-DD", "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "producer": {"version": "opal-aifill/1.0.0", "model": "claude-opus-5"},
  "blocks": { "mgmt_bio": B, "mgmt_recent": B, "mgmt_team_view": B, "thesis_pillars": B, "identity_description": B } }   # exactly these five
B = { "block_id": "<id>", "source_class": "OPAL_SOURCE" | "WEB_SEARCH" | "NONE", "machine_written": true,
      "text": "<plain ASCII text, 1..1200 chars>" | null, "reason": "<plain sentence>" | null,
      "citations": [ {"source_kind": "opal"|"web", "url": str|null, "title": str|null, "quote": str|null, "ref": str|null} ],
      "opal_inputs": [str], "model_call": {"model","web_search_requests","input_tokens","output_tokens"} | null }
```
Block rules: `NONE` has `text` null, `reason` a non-empty plain sentence with no underscore, and no citations. Any other class has `text` non-empty (at most 1200 characters, ASCII, no `**`),
`reason` null and at least one citation. A `web` citation has an http(s) `url`. An `opal` citation has a plain-words `ref` an analyst reads (no `_`, `[`, `]`, `{`, `}`, and not starting `thesis.` or
`overlay.`); it may also carry an http(s) `url`. `WEB_SEARCH` has at least one web citation, no opal citation, and `model_call.web_search_requests >= 1`. `OPAL_SOURCE` has at least one opal
citation and no web citation. `machine_written` is always `true`. `opal_inputs` holds the code-path names of the served fields used (never displayed).

The builder seam: a block builder is `lib.research.aifill.block_<id>.build_block(ctx) -> dict` and does no I/O of its own. `ctx` is a `BlockContext(security_key, inputs, model, now)` with
`ctx.inputs = {"overlay": dict|None, "thesis": dict|None, "errors": {...}}` (the two served route bodies of `/api/scoped/amgt/security/<key>/overlay` and `/thesis`), `ctx.now` a tz-aware UTC
datetime, and `ctx.model(prompt, *, system=None, web_search_max_uses=0, max_tokens=1500)` returning an object with `.text`, `.citations` (a list of `{"url","title","cited_text"}`), `.searches`,
`.input_tokens`, `.output_tokens`, `.web_search_requests`, `.model`, `.stop_reason`; it RAISES `ModelError` on any failure and never returns partial text.

### What you write in `lib/research/api/scoped_amgt.py` (one new region, placed beside the drafting reader, and one wiring line)
Mirror `_read_drafting_document` and `read_drafted_sections` (read them first, around `ENV_DRAFTING_ROOT`): the same local-directory override, the same shape of status, the same refusal to serve anything half-validated.
- Constants: `ENV_AIFILL_ROOT = "AMGT_AIFILL_ROOT"`, `AIFILL_OBJECT_NAME = "ai_fill.json"`, `AIFILL_SERVED = "SERVED"`, `AIFILL_ABSENT = "ABSENT"`, `AIFILL_INVALID = "INVALID"`, `AIFILL_SCHEMA = "aifill/v1"`, `AIFILL_BLOCK_IDS = ("mgmt_bio", "mgmt_recent", "mgmt_team_view", "thesis_pillars", "identity_description")`.
- The ADDRESS: the Lambda reads new-grammar prefixes ONLY from the generated module `lib/research/api/_harvest_prefixes.py` (`_hp`; the adapter never imports `lib.opal_naming` or `lib.research.harvest.store`: see the comments at the top of the file and at `FILING_ATTEMPT_STATE_PREFIX`). Cell fa-9 (merged before your worktree was cut) added the generated constant `_hp.AI_FILL_GOLD_PREFIX`; confirm it is there (`python -c "from lib.research.api import _harvest_prefixes as h; print(h.AI_FILL_GOLD_PREFIX)"`) and do NOT edit the generator or the generated module. In `scoped_amgt.py` the S3 key is `_hp.AI_FILL_GOLD_PREFIX + crosswalk.security_key_partition(security_key) + "/" + AIFILL_OBJECT_NAME` and the bucket is `crosswalk.POOL_BUCKET` (the bucket the drafting reader uses). No `gold/ai_fill` string literal in `scoped_amgt.py`.
- `_read_ai_fill_document(security_key) -> (document|None, source, reason|None, read_completed)`: `source` is `"local"`, `"pool"` or `"none"`. When `os.environ.get(ENV_AIFILL_ROOT)` is set, read `<root>/<crosswalk.slash_safe_key(security_key)>.json` (a missing file: `(None, "none", "no AI fill document at <path> (AMGT_AIFILL_ROOT is set, so the pool was not asked)", True)`; a file that does not parse: `(None, "none", "AI fill document at <path> did not parse: <ErrClass>: <err>", False)`). Otherwise ONE `_s3_client().get_object(Bucket=..., Key=...)` (never a LIST); an exception naming `NoSuchKey` (class name or message): `(None, "none", "no AI fill document at s3://<bucket>/<key>: <ErrClass>: <err>", True)`; any other exception: the same message form with `read_completed` False; a body that does not parse: `(None, "none", "AI fill document s3://... did not parse: ...", False)`.
- `_validate_ai_fill_document(document, security_key) -> (ok, reason)`, SELF-CONTAINED (the Lambda package does not carry `lib.research.aifill`; do not import it): the document is a dict; `schema == AIFILL_SCHEMA`; `security_key` equals the requested key; `as_of` and `generated_at` are strings; `blocks` is a dict whose keys are exactly `AIFILL_BLOCK_IDS`; each block is a dict with `block_id` equal to its key, `source_class` in `("OPAL_SOURCE","WEB_SEARCH","NONE")`, `machine_written is True`; a `NONE` block has `text` None and a non-empty string `reason` and no citations; any other block has a non-empty string `text`, `reason` None, and a non-empty list of citation dicts each with `source_kind` in `("opal","web")`, a `web` citation holding a `url` string that starts `http://` or `https://`, an `opal` citation holding a non-empty `ref` string; a `WEB_SEARCH` block has at least one web citation. `reason` is the FIRST problem found, as a plain sentence naming the block id.
- `read_ai_fill(security_key) -> dict` (public, importable): returns `{"status", "reason", "source", "read_completed", "as_of", "generated_at", "producer", "blocks"}`. `security_key` None -> `status` ABSENT, `reason` `"identity UNRESOLVED -- no measured security key to read an AI fill document by"`, `source` `"none"`, `read_completed` True, `blocks` `{}`. No document -> ABSENT with the reader's reason, source and read_completed, `blocks` `{}`, `as_of`/`generated_at`/`producer` None. A document that fails validation -> INVALID, the validator's reason, `read_completed` True, `source` the reader's, `blocks` `{}` (nothing is served half-validated). A valid document -> SERVED, `reason` None, `blocks` the document's blocks UNCHANGED, `as_of`, `generated_at`, `producer` from the document.
- The wiring: in `read_thesis_bundle`, after `bundle.update(read_drafted_sections(resolved_key))`, add `bundle["ai_fill"] = read_ai_fill(resolved_key)`. That is the only edit outside the new region. Do NOT call `read_ai_fill` from any overlay function. Leave the covered-no-block answer path as it is.

### `lib/research/api/tests/conftest.py` (AMENDMENT 1: one line)
The package's autouse fixture `empty_pool_roots` points `AMGT_POOL_ROOT` and `AMGT_DRAFTING_ROOT` at empty directories so no test reaches the live bucket. Add the same for the new reader, as one more line in that fixture: `monkeypatch.setenv(scoped_amgt.ENV_AIFILL_ROOT, str(tmp_path_factory.mktemp("empty_aifill")))`. Nothing else in the file moves. (Measured by the first worker: without it the existing thesis tests made 29 live GETs of the fill key across 44 passing tests.) Your own tests that exercise the S3 seam delete the variable with `monkeypatch.delenv` and patch `_s3_client`, as the conftest docstring says.

### `lib/research/api/tests/test_ai_fill_serve.py`
Your own pytest module (this directory has `__init__.py` and a `conftest.py`; follow its neighbours): the local-root reads (served, absent, unparseable), each INVALID case, the UNRESOLVED key, the pool read with a fake `_s3_client` (the exact bucket and key, a slash key, NoSuchKey, another error), one GET and no LIST, `read_thesis_bundle` carrying `ai_fill` (monkeypatch its heavy readers the way a neighbouring test does, or assert on the source line if no neighbour shows how), and the prefix constant. Python 3.9, ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W422-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/api/scoped_amgt.py`, `lib/research/api/tests/test_ai_fill_serve.py` and `lib/research/api/tests/conftest.py` (AMENDMENT 1: the ONE line below). The generator, the generated prefixes module and `test_harvest_prefixes.py` are cell fa-9's (already merged): you edit none of them. In `scoped_amgt.py` your edits are the constants and functions of the new region and the one wiring line; another seat edits other regions of the same file in parallel: do not touch, reformat, reorder or rename anything else.
2. You never deploy, never `terraform apply`, never `aws lambda update-function-code`, never write S3 (the S3 client in your tests is a fake), and you change no overlay function.
3. `scoped_amgt.py` gains no import of `lib.opal_naming`, `lib.research.harvest.store` or `lib.research.aifill` (the Lambda package is the module's own surface plus `_harvest_prefixes`).
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_ai_fill_serve.py
lib/research/api/tests/conftest.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-7"><invocation>cd C:/dev/wk-resapp-422 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa7_serve.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-7 ARMS: YES (N of N)` with N equal to the count printed and N at least 18, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-7"><invocation>cd C:/dev/wk-resapp-422 &amp;&amp; PYTHONPATH="$(pwd)" timeout 500 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_api_suite_no_new_failures.py" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL API SUITE: YES (base 4 failing, now 4 failing, new 0, passed P)` with P at least 969 plus the test functions you added; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~422 <0.9.0_WK_AMGT_RESAPP~422@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~422/AMGT_RESAPP.TO-AMGT-fa-7.the-serve-reads-the-fill-into-the-thesis-bundle.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any; AC2's line; and the `git diff --stat` of your branch against its base.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2026-10-13 ~23:3xZ, the issuer, after worker ~422's report; no gate limb graded it: the order is open and `<placeholders>NONE` stands):** the first worker's row W422-S1 (ARMED, disarm owner the issuer) measured that `conftest.py` set no `AMGT_AIFILL_ROOT`, so existing thesis tests reached the live fill key (29 GETs). The cut omitted the hermetic default the two neighbouring roots have. `conftest.py` joins `<paths>` for that one line. Rows S2 (the validator enforces the contract's block rules beyond the face's list: accepted, it is the same contract) and S3 (the naming gate WARNs on the display literal `s3://{0}/{1}`: a WARN, not a refusal) are observations.

**ISSUER NOTES:** STAGED behind `AMGT-fa-9`'s merge (the generated constant `_hp.AI_FILL_GOLD_PREFIX`): the first cut of this order carried the generator edit in its own `<paths>`, which the L6 gate graded as an infrastructure path with a WORLD floor against LOCAL, so the edit became fa-9 and this order stays LOCAL. The serve is written against the contract, not against `lib.research.aifill`, so the Lambda package never needs the aifill package (a deploy-leg fact: `scoped_amgt.py` and the regenerated `_harvest_prefixes.py` are the packaged members that change). Shared surface with `~R1`: `scoped_amgt.py` (different regions; the drain merges through `safe-merge.sh` and re-runs the whole api suite) and the function itself (ONE applier at a time: `~R1`'s round 104 applies first, msg 5213; this order is merged but NOT applied). Two criteria: AC1 the behaviour, AC2 the neighbour suite.

<status>staged</status>
<status>pending -- GO 2026-10-13T22:5xZ by the issuer (2.0.0_SA_COO~R2): fa-9 merged @957b04a764, so `_hp.AI_FILL_GOLD_PREFIX` exists at the base this worktree is cut from.</status>
<status>complete -- 2026-10-13T23:4xZ by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-422 @73bd667357 merged @cd31b97501, proof instance VALID (rc=0). The first run's row W422-S1 (conftest.py set no AMGT_AIFILL_ROOT, so existing thesis tests reached the live fill key) was ruled by AMENDMENT 1 (one conftest line) and the slot re-seated. AC1 PASS (`AIFILL FA-7 ARMS: YES (18 of 18)`, re-run by the issuer), AC2 PASS (`AIFILL API SUITE: YES (base 4 failing, now 4 failing, new 0, passed 1008)`, re-run by the issuer). NOT DEPLOYED: the function has one applier at a time and ~R1's round 104 applies first.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~422</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
