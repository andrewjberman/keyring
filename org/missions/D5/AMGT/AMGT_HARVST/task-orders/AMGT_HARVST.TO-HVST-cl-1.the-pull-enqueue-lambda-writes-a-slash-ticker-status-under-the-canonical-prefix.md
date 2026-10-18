# AMGT_HARVST task order -- `HVST-cl-1` -- ROUND 97, workstream PULLENQ-CODE: THE `pull_enqueue` LAMBDA WRITES A SLASH TICKER'S STATUS OBJECT UNDER THE CANONICAL PREFIX (CODE AND OFFLINE TESTS; NO DEPLOY) (row `D1-W173-S1`; CTO round-96 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cl-1.the-pull-enqueue-lambda-writes-a-slash-ticker-status-under-the-canonical-prefix</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~174</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests only: fake boto3 clients, NO network, NO S3, NO SQS, NO Lambda call, NO `aws` call of any kind, NO Terraform, NO upload of the artifact, NO deploy. NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a change that moves the SQS message's `security_key` off the raw form (the consumer applies the rule itself and expects the raw key), a status key for a key WITHOUT a slash that differs by one byte from today's, a second normalizer written differently from `crosswalk.slash_safe_key` (the copy must be equal over every key shape, tested), an import of `lib/` or `crosswalk` into the Lambda (the deployed zip ships ONE file, `lambda_function.py`, and an import would fail at run time in AWS), a malformed ticker that falls through and writes a raw key, a test that passes whatever the code does (it has a mutant), a status write that happens before the fence or before the key is validated, a change to the fence, the response shapes or the SQS call beyond what the cell names, and a deploy.
</preflight>

## 0. THE CELL

The `opal-research-pull-enqueue` Lambda (`infra/aws/lambda/research/pull_enqueue/lambda_function.py`) turns a pull request into (1) a status object `packs/<security_key>/status.json` and (2) one SQS message `{ticker, security_key, requested_at}`. Its `security_key(ticker)` only replaces spaces by `_`, so a slash ticker such as `BP/ LN Equity` gives `BP/_LN_Equity` and the status key `packs/BP/_LN_Equity/status.json`: the RAW spelling. Everything else in the harvest stores a slash key under the canonical spelling (`crosswalk.slash_safe_key`: `/` becomes `-SLASH-`, `BP-SLASH-_LN_Equity`), and the box-side consumer (`integrations/bloomberg/research/pull_consumer.py::_write_status`) writes and reads `packs/<crosswalk.slash_safe_key(security_key)>/status.json`. So a pull request for a slash ticker strands its REQUESTED status under a prefix the consumer and the readers never look at (the writer census `HVST-ck-4`, row `D1-W173-S1`; no raw status object is stored today). **The CTO's ruling: the Lambda writes the canonical spelling through the shared rule; a key without a slash is byte-equal to today; status objects already written raw stay readable through the union read; nothing is moved.** This cell is the code and its offline tests. The deploy is a separate order of another seat (Terraform), not yours.

## 1. THE BUILD (LOCAL code; about 30 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `infra/aws/lambda/research/pull_enqueue/lambda_function.py` (all of it), `test_bx1_tier_fence.py` and `test_by1_refusal_logged.py` in the same folder (how the module is loaded with fake `boto3` clients; copy that), `lib/research/identity/crosswalk.py` (`SLASH_SAFE_TOKEN`, `_check_key_shape`, `slash_safe_key`, `SlashSafeKeyError`), `infra/aws/terraform/harvest/build-and-upload.sh` (the zip holds `lambda_function.py` ALONE) and `infra/aws/ec2/opal-gateway/app/harvest_keys.py` (the gateway's copy of the same rule and how it is guarded: copy that PATTERN).
b. **The change, in `lambda_function.py` only:** add a self-contained function `_slash_safe_key(key)` that is a COPY of `crosswalk.slash_safe_key` including its shape checks (the same refusals for a non-str, empty, non-ASCII, outer-whitespace or token-containing value), written with the standard library only (the zip ships one file; NO import of `lib`, `crosswalk` or any other repo module), raising `ValueError` on a refusal. Build the status key as `"packs/%s/status.json" % _slash_safe_key(sec_key)`. **The raw `sec_key` stays in `status_obj["security_key"]` and in the SQS message body exactly as today** (the consumer applies the rule itself). **If the rule refuses the key, the handler returns `_response(400, {"error": "missing or invalid 'ticker' in request body"})` (the same text as the existing invalid-ticker response) BEFORE any S3 or SQS call**; the fence order is unchanged (the fence first, then the ticker, then the key). Nothing else in the file changes (no refactor, no rename, no change to `security_key`, `_response`, the fence or the log line).
c. New test `infra/aws/lambda/research/pull_enqueue/test_cl1_status_key_canonical.py` (offline, fake `boto3` clients, the loading style of `test_bx1_tier_fence.py`; change nothing in any existing test). Arms: (1) a slash ticker (`BP/ LN Equity` and `NG/ LN Equity`) through a valid `internal` direct-invoke event: the one `put_object` Key is `packs/BP-SLASH-_LN_Equity/status.json` (and the NG form), the status body's `security_key` is the RAW `BP/_LN_Equity`, and the one SQS message body's `security_key` is the RAW `BP/_LN_Equity`; (2) a key without a slash (`UNH US Equity`, `NVDA US Equity`): the `put_object` Key and the whole `put_object` and `send_message` argument sets equal what the UNCHANGED code produces (compute the old key inline as `"packs/%s/status.json" % ticker.strip().replace(" ", "_")` and assert equal); (3) **the equality arm:** `_slash_safe_key` equals `crosswalk.slash_safe_key` (imported in the TEST, not in the Lambda) over EVERY key of `infra/aws/ec2/opal-gateway/tests/fixtures/cj2_continuation_keys.txt` and over `BP/_LN_Equity`, `NG/_LN_Equity`, plus the refusals: both raise on a non-str, an empty string, a non-ASCII value, a value with outer whitespace and a value already containing `-SLASH-` (the arm asserts each pair raises or returns the same); (4) a ticker the rule refuses (one containing `-SLASH-`) returns the 400 and makes ZERO S3 and ZERO SQS calls; (5) the fence still refuses a non-internal caller with the 403 and zero calls (one assertion; the existing arms cover the rest); (6) **A MUTANT:** with `_slash_safe_key` monkeypatched to the identity, arm (1) FAILS (assert that it does); (7) a source check: the module source contains no import of `lib` or `crosswalk` (parse `lambda_function.py` with `ast` and assert it imports only standard-library modules and `boto3`).
d. Do not edit `build-and-upload.sh`, any Terraform file, any existing test, `pull_consumer.py`, `crosswalk.py` or any other file. Do not build, upload or deploy the zip. A surprise is a row; keep working.

<paths>
infra/aws/lambda/research/pull_enqueue/lambda_function.py
infra/aws/lambda/research/pull_enqueue/test_cl1_status_key_canonical.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~174/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cl-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_cl1_status_key_canonical.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cl-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py infra/aws/lambda/research/pull_enqueue/test_by1_refusal_logged.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^22 passed in</expect></criterion>
</proof_of_spec>

- AC1 is the built behaviour with its difference-control (arm 6 is its mutant, part of the criterion). AC2 is the unchanged-behaviour check: the two existing test files (22 tests at the base, issuer dry run 2026-10-18 ~14:5xZ) must still pass; do not change either of them. **If AC2 reads less, DO NOT edit the expectation, a test or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`22 passed in 0.30s`). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W174-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body, AND run the gate against your row WITHOUT the override first (the override must cover the Z-S106 pair only).
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~174/AMGT_HARVST.TO-HVST-cl-1.the-pull-enqueue-lambda-writes-a-slash-ticker-status-under-the-canonical-prefix.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cl-1.the-pull-enqueue-lambda-writes-a-slash-ticker-status-under-the-canonical-prefix` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cl-1.the-pull-enqueue-lambda-writes-a-slash-ticker-status-under-the-canonical-prefix.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-96 analysis (`ledger/ROUND_ANALYSIS.round96.md` @db6c34a7cc, msg 8092) item 1 ("`pull_enqueue` writes the canonical spelling through the shared resolver (`slash_safe_key`); a Terraform cell on the macro's CloudOps lane, under its own pair, built with the live-diff discipline; grade: a slash ticker's status lands under the canonical prefix, and a non-slash ticker is byte-equal; status objects already written raw stay readable through the union read; nothing is moved").
- **A COPY of the rule, by the package's shape** (one file in the zip, `ARTIFACT-ZIP entries=1`): the same pattern, and the same standing question, as the gateway's copy (row `D1-W171-S3`, call `48ae`, the cross-adjudication XA-20261018T094750Z-cbaa). The equality arm (3) over the fixture's 105 keys is its guard. If the cross-adjudication later rules that the module ships in the artifact, this copy goes with that ruling.
- **Class `WORLD` is the L6 gate's floor for an `infra/` path, not a deploy.** The deploy is `HVST-cl-2` (the seat on the macro's CloudOps lane, Terraform only, under its own never-widen pair, DEFINED and held until this merges).
- Chain A of round 97, slot ~174, worktree `C:/dev/wk-harvst-174`, branch `wk-AMGT_HARVST-174`. **Sparse set at provision (checked against `<paths>` and every file the face names):** `.claude/agents`, `lib/research`, `infra/aws/lambda/research/pull_enqueue`, `infra/aws/terraform/harvest`, `infra/aws/ec2/opal-gateway/app`, `infra/aws/ec2/opal-gateway/tests/fixtures`, `integrations/bloomberg/research` and `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2` (the existing tier-fence test loads `check_e2e.py` from there).
- **COMPLETE (issuer, 2026-10-18 ~15:2xZ):** worker `~174`, branch merged `349e7ee0da` (code, test and rows `5df3755664`, proof instance `34e78a930d` VALID re-pinned). The worker's first report was AC2 `1 failed, 21 passed` and a blocking row (`D1-W174-S1`): MY provisioning error (I gave the RESAPP deliverables folder a path under `AMGT_HARVST/` instead of `AMGT_RESAPP/`, so `check_e2e.py` was absent; my file check at provisioning counted output lines and hid the error). I added the right folder, re-ran, and the worker re-pinned. READ BY ME: AC1 `16 passed`, AC2 `22 passed` (both re-run in the worker's tree after the sparse fix); the whole `lambda_function.py` diff (26 lines: a stdlib copy `_slash_safe_key` equal in shape checks to `crosswalk.slash_safe_key`, the status key built through it, the raw `sec_key` kept in the status body and the SQS message, a refused key a 400 before any write; nothing else touched); `lambda_function.py` md5 at the merge `45c83ddf74640e90368e8bebf712b52c`, the new test md5 `9a1e487a72a40dfa372b1768fb21e533`. Row `D1-W174-S2` ACCEPTED: a slash-free ticker the shared rule refuses (non-ASCII, or containing `-SLASH-`) now gets a 400 with zero writes where the old code wrote a REQUESTED status and returned 202; the box consumer's `crosswalk.slash_safe_key` call (`pull_consumer._write_status`) refuses the same key, so that old status was already stranded; the deploy pair for `cl-2` names this behaviour. NOT ESTABLISHED: any deployed behaviour (nothing was built, uploaded or deployed); the equality of the copy over keys outside the fixture's 105 and the two slash keys; that API Gateway's authorizer never sends such a ticker. Nothing outside the two product files and the deliverables changed.
- **SENT:** with the round-97 issuance.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>97</round>
<workstream>PULLENQ-CODE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
