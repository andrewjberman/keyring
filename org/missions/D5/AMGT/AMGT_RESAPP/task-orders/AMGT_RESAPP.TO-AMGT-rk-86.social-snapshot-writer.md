# AMGT_RESAPP task order -- `AMGT-rk-86` -- cell H6: the social collector gains a harvest-grammar writer through H0-store (the vendor snapshot as received to bronze `bright-data/social_snapshot`, one silver `social_post` row per post keyed `(platform, post_id)`, the bucket as the fetch-key authority for `request_sha256`); FORMAT ONLY -- COLLECTION STAYS OFF, no schedule, no live job, no S3 write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-86</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~86</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- collection is RESERVED and OFF (Andrew 09-15 hold); this order arms no
  cron, alarm, monitor or cadence and wires the collector to no schedule, Lambda, EventBridge rule or scheduled task.
  Measured at the cut: 0 references to the social collector under infra/, .github/, org/mcp/*.ps1 and the harvester's
  install-schedule.ps1; the one infra mention is a comment (scoped-amgt-api.tf:160). AC4 re-measures.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed, and the social prefixes stay
  ungranted on purpose (scoped-amgt-api.tf:160); every test runs against stub S3 and stub vendor clients with the AWS
  credential variables pointed at a nonexistent profile (AC3), so the order makes no AWS or vendor call.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~86`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~86;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential. Never read any worktree of
round 20's `AMGT-rk-79`. **Never run `python -m lib.research.social.collect` for real: it triggers a billed vendor
job.** Only its functions, under stubs.

## 1. THE CELL, inlined in full -- `AMGT-rk-86` (chain H, wave 2, cell H6; plan s.5.6)

**The contracts (PRD v0.17 @`1f7459456a`, `prd/AMGT_RESAPP_PRD.md`):** C-BRONZE-AS-RECEIVED `:866-871` (the response
bytes exactly as received, one object per fetch, never overwritten; form (c) for a request:
*"`{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`"*); C-SILVER-PARQUET `:873-875`
(every row carries `bronze_key`, `fetched_at`, `record_hash`); C-DEDUPE-BY-KEY `:885-890` (*"Before any vendor call,
the writer checks the bucket for the fetch key ... The bucket is the authority for what has been fetched, never a file
on one desktop."*); C-FORMAT-SEQUENCE `:895-907` (the move and its readers are a later cell's).

**The plan (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` @`1a9f1c4469`,
s.5.6 `:325-345`), verbatim in the parts this cell serves:** *"The vendor's snapshot is not in the bucket:
`lib/research/social/collect.py:452-470` writes it to a local job directory. Collection is RESERVED and OFF by Andrew's
09-15 hold."* Proposed: *"bronze `s3://opal-data-harvest/bright-data/harvest/bronze/social_snapshot/date=2026-09-15/<request_sha256>.json`;
silver `.../bright-data/harvest/silver/social_post/date=.../part-*.parquet` (row per post). The measurement summary is
gold"*. *"Fetch key = `request_sha256` (`collect.py:541`, already computed): the same request inside the same window is
not re-submitted (it is billed). Silver record key `(platform, post_id)`"*. *"Recommendation: adopt the format now,
while collection is off, so the first live collection lands in the right place. The format does not switch collection
on."*

**Measured at the cut (HEAD `dbfcfc0817`):**
- `lib/research/social/collect.py`, 1104 lines, ASCII, LF. The snapshot bytes arrive at `:757`
  (`status_code, raw = client.snapshot(snapshot_id)`) and are parsed at `:758-764`; they are never stored. The only
  S3 write is `write_pool_object` `:479-511` (`social/v1/_measurement/<as_of>.json`, reached only with `--write-pool`).
  The request hash is `request_sha256(inputs)` `:541-549`. `to_item` `:374-449` reads the post id from
  `record.get("post_id") or record.get("id")`, else a 24-hex content hash.
- Builder output at the cut, live registry (duplicate `harvest` row deleted @`10bace8916`, validate 0 refusals):
  `bright-data/bronze/social_snapshot` + `date=2026-09-15` + `<sha>.json` ->
  `s3://opal-data-harvest/bright-data/harvest/bronze/social_snapshot/date=2026-09-15/<sha>.json`;
  `bright-data/silver/social_post` -> `s3://opal-data-harvest/bright-data/harvest/silver/social_post/date=2026-09-15/part-x.parquet`.
- Test baseline: `lib/research/social/tests` **33 passed**, 0 failed.
- **Fetch-key writer census (by subtraction, native Grep of `.put_object(`/`write_pool(` over the six AMGT code roots,
  non-test, @`dbfcfc0817`):** 32 lines, minus 2 comment lines = **30 call sites**; minus the 29 that write no social
  key = **1 writer of this channel today**, `collect.py:492` (`social/v1/_measurement/`). No writer of
  `bright-data/harvest/*/social_*` exists. **After this cell the new writer exists and is wired into NO schedule and NO
  production path.**
- The collector is **not packaged** in either AMGT Lambda (the chatter-axis closure, `build_zip.closure()`, is 15
  members, none under `lib/research/social/`; the scoped-api's 58 packaged paths carry only the data file
  `social_accounts.json`, never `collect.py`).

**WHAT YOU BUILD (ISSUER RULINGS, `2.0.0_SA_COO~Z`, L5):**
1. **A `write_harvest: bool = False` parameter on `run()` and a `--write-harvest` CLI flag, default OFF.** With it
   False, `run()` behaves byte-for-byte as today (AC5 compares). `--write-pool` and `write_pool_object` are unchanged
   -- the measurement object's move to gold is a later cell's.
2. **The bucket is the fetch-key authority in harvest mode:** BEFORE `client.trigger(...)`, call
   `store.fetch_key_exists("bright-data", "social_snapshot", store.date_partition(as_of), object_prefix=sha)`. A
   non-empty result means the same request is already stored: NO trigger, NO spend -- the run reads the stored
   snapshot from bronze instead (a resume from the bucket, not from the local ledger file). With harvest mode off, the
   local-ledger resume is unchanged.
3. **Bronze = the snapshot response as received:** right after `:757`, in harvest mode only,
   `store.bronze_put("bright-data", "social_snapshot", store.date_partition(as_of), store.form_c_object(sha, "json"), raw,
   content_type="application/json")` -- `raw` exactly as the client returned it, never `json.dumps` of the parse.
4. **Silver = one row per delivered vendor record:** `store.silver_append("bright-data", "social_post", rows,
   record_key_fields=("platform", "post_id"), run_stamp=store.stamp(<fetched_at>))`, each row = every vendor field of
   the record (flattened one level, typed) plus `platform` (`"reddit"`), `post_id` (the same rule `to_item` uses),
   `bronze_key` (the bronze receipt's key) and `fetched_at`. Only the store writes; this module gains ZERO
   `put_object` calls.
5. **No new vendor surface:** `DATASET_ID`, `TRIGGER_TYPE`, `DISCOVER_BY`, `TRIGGER_ROUTE`, `SNAPSHOT_ROUTE` and
   `BrightDataClient` are unchanged (AC5).
- Tests: NEW `lib/research/social/tests/test_collect_harvest.py`, offline (a stub `BrightDataClient` and a stub S3
  client passed as the store's `client=`), with these arms (names must match AC1):
  `test_harvest_off_by_default_writes_nothing`, `test_snapshot_bronze_is_bytes_as_received`,
  `test_known_request_skips_the_trigger`, `test_silver_row_per_post_keyed_platform_post_id`,
  `test_unchanged_post_is_skipped_on_second_run`, `test_address_is_builder_output`,
  `test_pinned_base_has_no_harvest_path` (DISCRIMINATING: `git show` the pin's `collect.py` into a temp file, import it
  under another name, and show `run` has no `write_harvest` parameter -- pinned
  `dbfcfc0817bdd8694796165e3e4489d03973fb0a`, never HEAD or a merge-base, row Z-S193).

## 2. WHERE THIS CAME FROM

**ROUND 21**, decomposition s.29 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s acceptance of the round-21 shape
(msg 24090) and PRD v0.17 ADMITTED @`1f7459456a` (msg 24098), from the chain-H proposal
`.scratch/r21_drafts/HARVEST_CHAIN_DECOMP_PROPOSAL.md` s.3 row H6 (*"collection stays OFF"*; no M or B cell for social).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/social/collect.py
lib/research/social/tests/test_collect_harvest.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~86/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-86.social-snapshot-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** -- above all `lib/research/social/{schema.json,
  measurement.schema.json,validator.py,measure.py}`, `lib/research/harvest/**` (rk-81's), `lib/opal_naming.py` and
  `infra/**`. Reads need no grant. Scratch is `<your worktree>/.scratch/r86/` only.
- **Collision check, done at the cut:** round 21's other cells write `lib/research/harvest/**` (rk-81),
  `infra/aws/terraform/harvest/*.tf` (rk-82), `integrations/seekingalpha/**` + `lib/opal_data_harvest/**` (rk-85) and
  the Bloomberg/filings files (rk-83/rk-84). No overlap. The only shared file is `INVESTIGATION_v1.md` (append-only;
  do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~86 <0.9.0_WK_AMGT_RESAPP~86@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**COLLECTION STAYS OFF (Andrew's 09-15 hold): NO live job, NO vendor call, NO S3 write, NO AWS call at all, NO
schedule, NO trigger, NO Lambda, NO deploy.** Every test uses stubs; AC3 runs them with no resolvable credentials. No
pair is needed: the cell has no live act. PORTAL not your surface; NO alarm, monitor, SNS/SES-send, notification or
freshness checker. No secrets are needed -- `read_api_key` is never called by a test (the stub client replaces
`BrightDataClient`). No non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by a live job, never by
wiring the collector to a schedule, never by editing a WALL, and never by writing S3 outside the store.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure the social suite (33 passed at the cut)
before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W86-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; a worker names the issuer
(`2.0.0_SA_COO~Z`) as `disarm_owner`, never itself.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys, importlib; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("refusals", len(r[0]) if isinstance(r, tuple) else r); [print(t, q, n.address("bright-data", "harvest", t, q, p, o).split("/")[2]) for t, q, p, o in (("bronze", "social_snapshot", "date=2026-09-15", "0" * 64 + ".json"), ("silver", "social_post", "date=2026-09-15", "part-x.parquet"))]; st = importlib.import_module("lib.research.harvest.store"); need = ("bronze_put", "fetch_key_exists", "silver_append", "silver_latest", "date_partition", "form_c_object", "stamp", "record_hash"); print("store_names_present", sum(hasattr(st, x) for x in need), "of", len(need))'</invocation><expect>"refusals 0", then 2 lines each ending "opal-data-harvest" (measured so at the cut @dbfcfc0817), then "store_names_present 8 of 8" (AMGT-rk-81 merged). At the cut the store module was ABSENT (ModuleNotFoundError: No module named 'lib.research.harvest') because rk-81 had not drained -- a ModuleNotFoundError, a line printing opal-data-assets, or fewer than 8 of 8 is a STOP: file a BLOCKING row and edit nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/social/tests/test_collect_harvest.py -v -p no:cacheprovider 2>&1 | tail -15</invocation><expect>0 failed, and PASSED lines naming test_harvest_off_by_default_writes_nothing, test_snapshot_bronze_is_bytes_as_received, test_known_request_skips_the_trigger, test_silver_row_per_post_keyed_platform_post_id, test_unchanged_post_is_skipped_on_second_run, test_address_is_builder_output and test_pinned_base_has_no_harvest_path -- 7 of 7 named arms (more arms are allowed; print the total)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/social/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"N passed" with 0 failed, N = the spawn baseline (33 at the cut) plus this cell's new arms</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u AWS_ACCESS_KEY_ID -u AWS_SECRET_ACCESS_KEY -u AWS_SESSION_TOKEN AWS_PROFILE=nonexistent-rk86 AWS_CONFIG_FILE=/dev/null AWS_SHARED_CREDENTIALS_FILE=/dev/null python -m pytest lib/research/social/tests/test_collect_harvest.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>the same pass count as AC1 with 0 failed -- with no credentials resolvable any real AWS call would raise, so a green run proves only the stubs were touched; zero S3 writes and zero vendor calls by this cell (the Z-S192 census of the act's own write set)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess, io; pin = "dbfcfc0817bdd8694796165e3e4489d03973fb0a"; mine = subprocess.run(["git", "log", "--format=%H", pin + "..HEAD", "--author=0.9.0_WK_AMGT_RESAPP~86 <"], capture_output=True, text=True).stdout.split(); touched = sorted({p for c in mine for p in subprocess.run(["git", "show", "--name-only", "--format=", c], capture_output=True, text=True).stdout.split()}); print("files_touched_by_this_cell", touched); print("infra_or_schedule_touched", [p for p in touched if p.startswith(("infra/", ".github/")) or p.endswith(".ps1")]); tracked = subprocess.run(["git", "ls-files", "infra", ".github", "org/mcp", "lib/opal_data_harvest/install-schedule.ps1"], capture_output=True, text=True).stdout.split(); hits = [f for f in tracked if f.endswith((".tf", ".yml", ".yaml", ".ps1", ".json", ".py", ".sh")) and ("social.collect" in io.open(f, encoding="utf-8", errors="replace").read() or "social/collect" in io.open(f, encoding="utf-8", errors="replace").read())]; print("tracked_files_scanned", len(tracked)); print("schedule_refs_to_collector", hits)'</invocation><expect>"files_touched_by_this_cell" lists only paths in section 3; "infra_or_schedule_touched []"; "tracked_files_scanned" with its denominator and "schedule_refs_to_collector []" (0 at the cut) -- collection stays off, the collector is wired to nothing</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import ast, subprocess; pin = "dbfcfc0817bdd8694796165e3e4489d03973fb0a"; now = open("lib/research/social/collect.py", encoding="utf-8").read(); old = subprocess.run(["git", "show", pin + ":lib/research/social/collect.py"], capture_output=True, text=True).stdout; node = lambda s, name: next((ast.dump(n) for n in ast.walk(ast.parse(s)) if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Assign)) and (getattr(n, "name", None) == name or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) == name for t in n.targets)))), None); names = ("write_pool_object", "BrightDataClient", "request_sha256", "to_item", "DATASET_ID", "TRIGGER_TYPE", "DISCOVER_BY", "TRIGGER_ROUTE", "SNAPSHOT_ROUTE"); print("unchanged", sum(node(now, x) == node(old, x) and node(old, x) is not None for x in names), "of", len(names)); print("put_object_calls", sum(1 for n in ast.walk(ast.parse(now)) if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "put_object")); run = next(n for n in ast.walk(ast.parse(now)) if isinstance(n, ast.FunctionDef) and n.name == "run"); kw = {a.arg: d for a, d in zip(run.args.args[-len(run.args.defaults):], run.args.defaults)}; print("write_harvest_default", ast.literal_eval(kw["write_harvest"]) if "write_harvest" in kw else "ABSENT")'</invocation><expect>"unchanged 9 of 9" (the measurement writer, the vendor client, the request hash, the item rule and every vendor-surface constant are byte-identical to the pin), "put_object_calls 1" (the legacy measurement write only -- 1 at the cut; the harvest path writes only through the store), "write_harvest_default False"</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-86"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; [print(f.split("/")[-1], "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in ("lib/research/social/collect.py", "lib/research/social/tests/test_collect_harvest.py")]'</invocation><expect>2 lines, each "compiles True crlf 0 non_ascii_bytes 0" (collect.py is ASCII/LF at the cut)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~86/AMGT_RESAPP.TO-AMGT-rk-86.social-snapshot-writer.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip the status
tag in the record face to `complete` ONLY if every criterion passes; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r86/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the cell spawns ONLY after `AMGT-rk-81` (H0-store) has drained -- AC0 STOPs otherwise. It is the
only chain-H cell with no M or B follow-on: the first live collection waits on Andrew lifting the 09-15 hold, and will
land in the right place because of this cell.

<status>pending</status>
<round>21</round>
<slot>~86</slot>
<fabric>site-z</fabric>
