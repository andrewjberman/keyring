# AMGT_RESAPP task order -- `AMGT-fa-6` -- THE STORE ADDRESS AND IO, AND THE RUN COMMAND (FWD-41; A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~427</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-6.the-store-address-and-the-run-command</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell writes and tests local Python only; `store.py` calls `s3:PutObject` and `s3:GetObject` in production use, but the checks use a fake client and no AWS call is made. The grant for the new prefix is read by the issuer before any write (s.5 of the decomposition).
comp-adversary: RUN at the cut -- `check_fa6_store_run.py` is a prepared acceptance check (16 arms: the builder address, the slash key, no typed address literal, write/read through a fake S3 client, the CLI in a subprocess with `--no-model`, the dry-run and the confirmed write); at the base it exits 1 on `ModuleNotFoundError: No module named 'lib.research.aifill'`, the build check failing as expected.
EGRESS CLASS, declared: NONE by the cell and its checks (a fake S3 client, no network). The cell's `--to-s3 --confirm-write` flag is an act the issuer takes later under a never-widen sign-off; no order runs it.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-427` (branch `wk-AMGT_RESAPP-427`, cut from the merged head that carries cells fa-1 to fa-5 (the issuer cuts this worktree after they merge)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-427`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-6` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41's census and thread need two things the builders and the serve do not give: the ONE address a name's document is stored at (the naming builder's, rule 30), and a command that runs the whole producer for one name. You write `store.py` (the address and the read/write of the document) and `run.py` (the command), and one test module. The package already carries `contract.py`, `orchestrate.py`, `model.py`, `inputs.py` and the five `block_<id>.py` builders (cells fa-1 to fa-5, merged): read `contract.py`, `orchestrate.py`, `model.py` and `inputs.py` first.


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

### `lib/research/aifill/store.py` -- exact interface
- Module constants: `TABLE = "ai_fill"`, `TIER = "gold"`, `SOURCE = "amgt"`, `OBJECT_NAME = "ai_fill.json"`. NO address, bucket path or key prefix is typed anywhere in the module (CLAUDE.md rule 30: every S3 address is builder output; a literal such as `amgt/harvest/gold` or a string containing `ai_fill/` is a defect; the docstring mentions none).
- `address_for(security_key) -> str`: `lib.research.harvest.store.address_of(SOURCE, TIER, TABLE, lib.research.harvest.store.entity_partition("security_key", security_key), object_name=OBJECT_NAME)` -- import that module as `from lib.research.harvest import store as hstore` at module scope. The result for `ASML_NA_Equity` is `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=ASML_NA_Equity/ai_fill.json`; a slash key such as `BP/_LN_Equity` is encoded by the builder (`security_key=BP-SLASH-_LN_Equity`), never split.
- `write_document(doc, client=None) -> dict`: validates with `contract.validate_document(doc)` called THROUGH the `contract` module (`from lib.research.aifill import contract`; the acceptance check patches `contract.validate_document`); any problem raises `contract.ContractError("; ".join(problems))` BEFORE any request. The body is `json.dumps(doc, sort_keys=True, ensure_ascii=True, indent=1).encode("ascii")`. `client` defaults to `boto3.client("s3", region_name="us-east-1")` built inside the function (import `boto3` inside it). One `client.put_object(Bucket=<bucket>, Key=<key>, Body=<bytes>, ContentType="application/json")`, the bucket and key split from `address_for(doc["security_key"])`. Returns `{"uri": <address>, "bucket": ..., "key": ..., "content_length": <int>, "sha256": <hex of the body>}`.
- `read_document(security_key, client=None) -> dict | None`: one `client.get_object(Bucket=..., Key=...)`; the parsed JSON on success; `None` when the object is missing (a `botocore` `ClientError` whose `Error.Code` is `NoSuchKey` or `404`, OR any exception whose class name is `NoSuchKey`); any other exception propagates unchanged.

### `lib/research/aifill/run.py` -- exact interface; runnable as `python -m lib.research.aifill.run`
- `main(argv=None, client=None) -> int` (and `if __name__ == "__main__": sys.exit(main())`). Arguments (argparse): `--key KEY` (required); `--inputs-file FILE` (a JSON file shaped like `inputs.served_inputs`' return, `{"overlay":..., "thesis":..., "errors":...}`; when absent, `inputs.served_inputs(key, function_name=args.function)` reads the live routes, where `--function NAME` defaults to the environment variable `AIFILL_SERVED_FUNCTION`; if neither is set print `BLOCKED: the served function name is not set (pass --function or set AIFILL_SERVED_FUNCTION, or use --inputs-file)` and return 2 before any other work; the module types no function name: CLAUDE.md rule 30); `--no-model`; `--out DIR`; `--to-s3`; `--confirm-write`.
- Order of work: (1) unless `--no-model`, if `ANTHROPIC_API_KEY` is not set or empty in the environment print `BLOCKED: ANTHROPIC_API_KEY is not set (use --no-model for a run with no model call)` and return 2, before reading any input; (2) read the inputs; if both served bodies are None print `WARN: both served bodies unreadable: <errors>` and go on; (3) the model callable: with `--no-model`, a function that raises `model.ModelError("model disabled by --no-model")`; otherwise `model.call_model`; (4) `doc = orchestrate.build_document(key, inputs, model_callable)`; (5) `problems = contract.validate_document(doc)` called through the `contract` module; any problem -> print `ERROR: document INVALID: <first problem>` and return 1 (nothing is written, anywhere); (6) print one line per block, in `BLOCK_IDS` order: `BLOCK <id> <source_class> <N chars | reason>` (the character count of `text` for a filled block, the `reason` for a NONE block), then the summary line `AIFILL RUN: key=<K> document=VALID blocks=5 (OPAL <n> WEB <n> NONE <n>)`; (7) with `--out DIR`: create the directory if needed and write the document to `<DIR>/<crosswalk.slash_safe_key(key)>.json` (`lib.research.identity.crosswalk.slash_safe_key`; ASCII JSON as in `write_document`) and print `WROTE: <path>`; (8) with `--to-s3`: print `DRY-RUN: would write <store.address_for(key)>` and write nothing, unless `--confirm-write` is also given, in which case `store.write_document(doc, client=client)` is called once and `WROTE: <uri> bytes=<content_length> sha256=<first 16 hex>` is printed. `client` is passed through to `store` (the acceptance check supplies a fake).
- The run command never prints, logs or stores the API key.

### `lib/research/aifill/tests/test_store_run.py`
Your own pytest module (no `__init__.py`): a fake S3 client, `store` (address, slash key, write refuses an invalid document before any put, round trip, missing is None, another error propagates) and `run.main` in-process with `--inputs-file` and `--no-model` (the files and the printed lines, the key stop with no key, the dry-run, the confirmed write, an invalid document never written). Python 3.9, ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W427-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/store.py`, `lib/research/aifill/run.py` and `lib/research/aifill/tests/test_store_run.py`. You may import every module already in the package; you edit none of them.
2. You never run `--to-s3 --confirm-write` against the real client, you never call the real model and you never call the live Lambda: the test and the checks use fakes, `--no-model` and `--inputs-file`.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/store.py
lib/research/aifill/run.py
lib/research/aifill/tests/test_store_run.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-6"><invocation>cd C:/dev/wk-resapp-427 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa6_store_run.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-6 ARMS: YES (N of N)` with N equal to the count printed and N at least 16, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-6"><invocation>cd C:/dev/wk-resapp-427 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_store_run.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~427 <0.9.0_WK_AMGT_RESAPP~427@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~427/AMGT_RESAPP.TO-AMGT-fa-6.the-store-address-and-the-run-command.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind fa-1 to fa-5. The `--to-s3 --confirm-write` act is a WORLD act (s.5 item 2 of the decomposition): the never-widen sign-off (CTO + COO) names the address, the blast radius and the per-key rollback, and the issuer reads the function role's S3 read on the new prefix with `comp-iam` first. This order only builds the command.

<status>staged</status>
<status>pending -- GO 2026-10-13T23:5xZ by the issuer (2.0.0_SA_COO~R2): fa-1 @ebe4c8d287, fa-2 @0a1877ea77, fa-3 @062a4ca24a, fa-4 @6c10ae95c6 and fa-5 @fe344586ce are merged, so contract, orchestrator, model, inputs and the five builders exist at the base this worktree is cut from.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~427</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
