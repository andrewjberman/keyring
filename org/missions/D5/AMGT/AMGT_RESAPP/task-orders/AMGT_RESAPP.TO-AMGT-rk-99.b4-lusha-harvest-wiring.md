# AMGT_RESAPP task order -- `AMGT-rk-99` -- B4 WIRING: a PUBLIC Lusha harvest entry point that takes the roster, reaches the Lusha client through a public seam, and writes `contact_match` silver only on an explicit switch, with the C-LUSHA-EXCEPTION guard on the path; CODE ONLY, 0 Lusha calls, the key never read

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-99</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~99</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits two library modules and adds one test file; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, grant or secret is read or changed; no AWS call and no Lusha call
  of any kind is made by this order (every test injects a stub Lusha client and a stub S3 client).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~99`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your
first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`, `.tools/`
and the paths in section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row. Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~99;`. **NEVER RUN AN INSTALL.** **NEVER read, export, print
or request the Lusha key** -- not through `comp-secrets`, the environment or a file; no criterion needs it. Never read,
show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-99` (round 25, ahead of the B4 run)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24189, 2026-09-22T10:47:03Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T104703Z_1.0.0_SA_CTO_Z_Re_24188__all_3_calls_RULED_as_recommend.md`,
line 13):

> CALL 2 (B4 wiring): RULED IN, round 25. A public entry point that takes the roster, so matches bind to officers. It
> reaches the Lusha client through a public seam (promote or wrap _lusha_client). The C-LUSHA-EXCEPTION guard sits on
> that path, with a test that a contact field never reaches the writer. Code only: 0 Lusha calls, the key is never read,
> and a test forces the client to raise.

**Why this cell exists:** the rk-87 Lusha silver writer has NO production caller. A B4 run today would have to chain
private functions by hand and would pass no roster, so no Lusha result would bind to an officer.

**THE MEASURED STATE, at `4183e30531` (SITEZ; `lib/` byte-identical to `7fa3268fd0`). RE-READ every line at your branch
HEAD before editing:**

- **`lib/research/harvest/lusha.py`** (155 lines; rk-87). It imports `store`, `enrich` and `roster` (`:28-30`).
  - `contact_match_rows(results, company_domain, fetched_at, officers=None, results_total=None)` (`:90`) is PURE: it
    builds each row ONLY from the `KEPT_FIELDS` allow-list (`:41-44`) and binds `matched_officer` via
    `enrich.name_matches` (`_matched_officer`, `:70`).
  - `already_fetched(company_domain, since, client=None)` (`:139`) is the dedupe check.
  - `write_contact_match(rows, run_stamp, client=None)` (`:152`) calls `store.silver_append`.
  - Its docstring (`:24`) says "NOT WIRED. No existing file imports this module".
  - Production callers of `contact_match_rows` / `write_contact_match` / `already_fetched` outside the module and its
    tests: **0**.
- **`lib/research/management/enrich.py`** (1294 lines):
  - `_lusha_client(api_key=None, client=None)` (`:264`) returns `client` unchanged when one is injected (`:265-266`).
    Only otherwise does it load the estate `LushaClient` by path (`:267`) and read `LUSHA_API_KEY` from the
    environment (`:271`).
  - `prospecting_page(client, company_domain)` (`:300`) is the ONE billable page. It tries `client._execute(...)`
    first and falls back to `client.contacts_prospecting(...)` on any exception (`:322`, then `:334`). If BOTH raise, the
    exception propagates.
  - `scrub(value)` (`:91`) drops every contact key recursively and counts what it removed; `is_contact_key(key)`
    (`:85`) is the test.
  - `domain_for(security_key, table=None)` is at `:140`.
  - `build_document` (`:627`) is today's only caller of `_lusha_client` (`:659`).
  - THREE existing tests patch `enrich._lusha_client` by name to prove it is NOT called:
    `management/tests/test_jp_president_and_readable_reasons.py:552`, `:666` and
    `test_reproject_public_profile.py:361`. So the private name MUST stay a module attribute that `build_document`
    looks up at call time.
- **The guard tests already on `lusha.py`** (`harvest/tests/test_lusha.py`):
  - `:184` -- no `.bronze_put` call anywhere in the module (AST);
  - `:195` -- the module imports no `boto3`, `urllib`, `requests`, `lusha_client` or `LushaClient` NAME. It walks
    `Import` / `ImportFrom` nodes only, so an attribute call `enrich.lusha_client(...)` is legal.
  - Both must stay green, unedited.
- **The roster:** `roster.load_source_object(security_key, source_path=None, client=None)` (`roster.py:1116`) and
  `roster.build_roster(source_object, as_of, source_label="")` (`roster.py:1167`) yield the `officers` list, exactly
  as `build_document` does (`enrich.py:630`, `:644`).
- **Tests at the cut** (one pytest call per directory): `lib/research/harvest/tests` **64 passed** (`test_lusha.py`
  **9**); `lib/research/management/tests` **95 passed**, 13 subtests passed.
- **Encoding at the cut:** `enrich.py` and `lusha.py` are each 0 CRLF and 0 non-ASCII characters.

**ISSUER RULINGS (L5), what you build:**

1. **The public seam: WRAP, do not rename.** In `enrich.py`, add `def lusha_client(api_key=None, client=None):` whose
   body is `return _lusha_client(api_key=api_key, client=client)`, looking `_lusha_client` up at call time, with a
   docstring naming it the public seam. `_lusha_client` and `build_document` are UNCHANGED, so the three existing
   patches keep binding. Nothing else in `enrich.py` moves.
2. **The entry point**, in `lusha.py`:
   `harvest_company(company_domain, officers, run_stamp, fetched_at=None, write=False, since=None, lusha_client=None,
   s3=None)`. In order:
   - (a) **REFUSE before any call** if `officers` is empty or `None`: raise `ValueError`. The roster is REQUIRED, so
     matches bind to officers, and no credit is spent on a name with no roster. Also refuse if `company_domain` is
     empty.
   - (b) **Dedupe:** if `since` is not `None` and `already_fetched(company_domain, since, client=s3)`, return
     `{"status": "SKIPPED-HELD", "credits": 0, "rows": [], "written": False, "receipt": None}`. No client is built and
     no call is made.
   - (c) `client = enrich.lusha_client(client=lusha_client)`, then `page = enrich.prospecting_page(client,
     company_domain)`. A raise propagates UNCAUGHT, and nothing below runs.
   - (d) `results, removed = enrich.scrub(page["results"])`, then `rows, skipped = contact_match_rows(results,
     company_domain, fetched_at or <utc now>, officers=officers, results_total=page["total"])`.
   - (e) **THE C-LUSHA-EXCEPTION GUARD, on this path:** a private `_assert_no_contact_field(rows)` raises
     `store.LushaExceptionError` if any row's key set is not a subset of `KEPT_FIELDS`, or if any key satisfies
     `enrich.is_contact_key`. It runs on EVERY call, BEFORE any write, and whether or not `write` is set.
   - (f) If `write`, `receipt = write_contact_match(rows, run_stamp, client=s3)`; otherwise `receipt = None`. **Default
     OFF.**
   - Return `{"status": "CALLED", "credits": page["credits"], "results_returned": len(results), "contact_keys_removed":
     removed, "skipped": skipped, "matched": <rows with a non-null matched_officer>, "rows": rows, "written":
     bool(write), "receipt": receipt}`.
3. **A CLI**, `python -m lib.research.harvest.lusha --security-key K --run-stamp S [--since ISO] [--write]`, with
   `--write` defaulting OFF:
   - it builds `officers` via `roster.load_source_object` + `roster.build_roster` (as `build_document` does);
   - it takes the domain from `enrich.domain_for`;
   - it calls `harvest_company` and prints the returned counts (NEVER a row's values).
   It is NOT run in this cell.
4. Update `lusha.py`'s module docstring: the "NOT WIRED" paragraph becomes one naming `harvest_company` as the wired
   entry point, and noting that the RUN is a later cell under its own pair and Andrew's word.
5. **Tests**, in ONE new file `lib/research/harvest/tests/test_lusha_harvest.py` (pytest, QUALIFIED imports, W85-S1).
   Every test injects a STUB Lusha client (a class with `_execute` and `contacts_prospecting`, counting calls) and
   monkeypatches `lusha.write_contact_match` / `store.silver_append` with a recorder. **No real client is built and no
   key is read:** each test also deletes `LUSHA_API_KEY` from the environment via `monkeypatch.delenv(...,
   raising=False)` and patches `enrich._estate_module` to raise if called. Names must match AC1:
   - `test_matches_bind_to_roster_officers` -- the stub returns two results, one matching a roster officer by name.
     The matching row carries `matched_officer` equal to that officer and the other carries `None`; `write=False`
     makes 0 recorder calls.
   - `test_contact_field_never_reaches_the_writer` -- the stub's results carry `emails`, `phones`, `mobile` and a
     nested contact key. With `write=True`, the recorder receives rows whose keys are all within `KEPT_FIELDS`, and
     `enrich.is_contact_key` is False for every key.
   - `test_guard_refuses_a_contact_bearing_row_before_any_write` -- with `contact_match_rows` monkeypatched to return a
     row carrying `emails`, `harvest_company(..., write=True)` raises `store.LushaExceptionError` and the recorder has 0
     calls.
   - `test_client_that_raises_propagates_and_nothing_is_written` -- a stub whose `_execute` AND `contacts_prospecting`
     both raise: `harvest_company` raises, and the recorder has 0 calls.
   - `test_key_is_never_read_with_an_injected_client` -- with `LUSHA_API_KEY` unset and `_estate_module` patched to
     raise, `enrich.lusha_client(client=stub) is stub` and `harvest_company` completes on the stub.
   - `test_empty_roster_refused_before_any_call` -- `officers=[]` and `officers=None` each raise `ValueError`, and the
     stub records 0 calls.
   - `test_held_domain_skips_the_call` -- `already_fetched` monkeypatched True with `since` set: returns
     `SKIPPED-HELD`, and the stub records 0 calls.
   - `test_public_seam_wraps_the_private_name` -- patching `enrich._lusha_client` changes what `enrich.lusha_client`
     returns, proving the existing patches still bind.

**What this cell does NOT change:** `store.py` (a WALL); `roster.py`; `enrich.py`'s every existing function body
(`_lusha_client`, `prospecting_page`, `scrub`, `build_document` and the rest); `KEPT_FIELDS`, `contact_match_rows`,
`already_fetched`, `write_contact_match`; the estate `data/find/imo/scripts/_util/lusha_client.py`; every existing test;
any S3 object. No Lusha call, no key read, no AWS call.

## 2. WHERE THIS CAME FROM

**ROUND 25**, decomposition s.33 (cut by `2.0.0_SA_COO~Z`), on the CTO's msg 24189 (answering the COO's msg 24188) plus
the round-24 analysis (msg 24182). The B4 RUN cell rides behind this one on Andrew's per-use word (the key is
unrotated; "rotate later"), with its own pair. Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/lusha.py
lib/research/management/enrich.py
lib/research/harvest/tests/test_lusha_harvest.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~99/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-99.b4-lusha-harvest-wiring.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. Every existing test file is a wall: if one must
  change to stay green, STOP and REFUSE with a row. Scratch is `<your worktree>/.scratch/r99/` only, never committed.
  The only shared file is `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~99 <0.9.0_WK_AMGT_RESAPP~99@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**CODE ONLY.** No Lusha call, no key read (`comp-secrets`, the environment or any file), no AWS call, no deploy. Never
run the new CLI.
- **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1).
- **Run each test directory in its OWN pytest call** (W85-S1).
- **A script that carries a backslash is a FILE** you write from this order's text verbatim (W84-S1). Every script
  below is a file.
- **The discriminating comparison is pinned to commit `4183e30531`** (Z-S193), never HEAD or a merge-base.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** AC0 re-measures every baseline before you edit; every
  later bar is "AC0's value plus N" or "equal to AC0's value".
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W99-S<k>`, with `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.
  Append by textual splice inside the one fenced JSON array; never edit an existing row. A worker names the issuer
  (`2.0.0_SA_COO~Z`) as `disarm_owner`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 600)

**Script files.** Write each block below to the named file under `<your worktree>/.scratch/r99/`, byte-for-byte, then
run it from the worktree root as the criterion states.

`.scratch/r99/ac0.py`:
```
import subprocess
def run(args):
    return subprocess.run(args, capture_output=True, text=True).stdout
print("pin_object", run(["git", "cat-file", "-t", "4183e30531"]).strip())
enr = open("lib/research/management/enrich.py", "rb").read().decode("utf-8").splitlines()
print("enrich_264", enr[263].strip())
print("enrich_659", enr[658].strip())
names = ["contact_match_rows(", "write_contact_match(", "already_fetched(", "harvest_company("]
hits = []
for n in names:
    for line in run(["git", "grep", "-n", n, "--", "lib", "integrations", "data", ".tools"]).splitlines():
        path = line.split(":", 1)[0]
        if path != "lib/research/harvest/lusha.py" and "/tests/" not in path:
            hits.append(line.split(":", 2)[0] + ":" + line.split(":", 2)[1])
print("production_lusha_writer_calls", len(hits), sorted(hits))
patches = [l for l in run(["git", "grep", "-n", "_lusha_client", "--", "lib/research/management/tests"]).splitlines()]
print("existing_private_patches", len(patches))
for f in ("lib/research/management/enrich.py", "lib/research/harvest/lusha.py"):
    b = open(f, "rb").read()
    print(f, "crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

`.scratch/r99/ac4.py`:
```
import subprocess
def run(args):
    return subprocess.run(args, capture_output=True, text=True).stdout
changed = sorted(run(["git", "diff", "--name-only", "4183e30531", "HEAD", "--", "lib", "integrations", "infra", ".tools", "data"]).split())
print("changed_code_files", changed)
diff = run(["git", "diff", "4183e30531", "HEAD", "--", "lib/research/management/enrich.py"]).splitlines()
removed = [l for l in diff if l.startswith("-") and not l.startswith("---")]
added_defs = [l for l in diff if l.startswith("+def ")]
print("enrich_removed_lines", len(removed), "enrich_added_defs", added_defs)
patches = [l for l in run(["git", "grep", "-n", "_lusha_client", "--", "lib/research/management/tests"]).splitlines()]
print("existing_private_patches", len(patches))
```

`.scratch/r99/ac5.py`:
```
for f in ("lib/research/management/enrich.py", "lib/research/harvest/lusha.py", "lib/research/harvest/tests/test_lusha_harvest.py"):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r99/ac0.py && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit, the baseline every later bar reads against. It prints "pin_object commit"; "enrich_264" carries "def _lusha_client(api_key=None, client=None):"; "enrich_659" carries "prospecting_page(_lusha_client(client=lusha_client), company_domain)"; "production_lusha_writer_calls N0" (measured 0 at the cut); "existing_private_patches P0" (measured 3); and each module's crlf and non_ascii_chars (measured 0 and 0). Then the harvest suite's "H0 passed" (measured 64) and the management suite's "M0 passed" (measured 95, 13 subtests). A drifted line NUMBER is recorded, not a fail, if the LINE is the same; a differing N0, P0, H0 or M0 is recorded and becomes the baseline</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_lusha_harvest.py -v -p no:cacheprovider 2>&1 | tail -12</invocation><expect>a final line "8 passed" and 0 failed, with the PASSED lines naming test_matches_bind_to_roster_officers, test_contact_field_never_reaches_the_writer, test_guard_refuses_a_contact_bearing_row_before_any_write, test_client_that_raises_propagates_and_nothing_is_written, test_key_is_never_read_with_an_injected_client, test_empty_roster_refused_before_any_call, test_held_domain_skips_the_call and test_public_seam_wraps_the_private_name</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"(H0 + 8) passed" and 0 failed, where H0 is AC0's harvest count (measured 64, so 72): test_lusha.py's two guard tests (no bronze_put call, no client/network import) stay green unedited, with the entry point in the module</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"M0 passed" and 0 failed, where M0 is AC0's management count (measured 95, with 13 subtests passed): the three existing patches of enrich._lusha_client still bind, and build_document is unchanged</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r99/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/harvest/lusha.py, lib/research/harvest/tests/test_lusha_harvest.py and lib/research/management/enrich.py; "enrich_removed_lines 0" (the wrap only ADDS to enrich.py; no existing line changes) with "enrich_added_defs" exactly ['+def lusha_client(api_key=None, client=None):']; "existing_private_patches" equal to AC0's P0 (measured 3)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-99"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r99/ac5.py</invocation><expect>all three files print "compiles True", crlf 0, and non_ascii_chars EQUAL to AC0's measured value for each existing file (measured 0 for both) and 0 for the new test file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~99/AMGT_RESAPP.TO-AMGT-rk-99.b4-lusha-harvest-wiring.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict). Flip the order's status
(on the record face) to `complete` only if every criterion PASSES, and commit with `--only -- <paths>`. Report once,
naming AC0's baselines, the suite counts before and after, and AC4's lines.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES of the two modules to `.scratch/r99/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **WRAP, not promote.** Three existing management tests patch `enrich._lusha_client` BY NAME. A rename would silently
   un-bind them, and they would keep passing while guarding nothing. The wrap keeps one body and two names, with the
   private one authoritative.
2. **The entry point lives in `lusha.py`, not `enrich.py`.** `lusha.py` already imports `enrich`, so the reverse
   import would be circular. `enrich.build_document` is NOT rewired to call it: the served management document path
   stays byte-identical, and changing it is the RUN cell's pair, not a code-only wiring cell's.
3. **The guard is a SECOND control on top of the allow-list.** `contact_match_rows` already builds rows from
   `KEPT_FIELDS` only. The new guard catches a future edit to `KEPT_FIELDS` or to row construction that lets a contact
   key through, at write time, which is what C-LUSHA-EXCEPTION protects.
4. **An empty roster refuses before the call**, matching `build_document`'s `if officers and company_domain`. No
   credit is spent on a name with no roster to bind to.
5. **For the B4 run cell:** 6861 (Keyence) is the only validation name with a verified site, and its roster is a
   filing roster. The run cell names the CLI invocation, a credit cap and `--since`.
6. **Pin:** `4183e30531`. Re-pin to the issuance commit if s.33 moves anything under `lib/`.

<status>pending</status>
<round>25</round>
<slot>~99</slot>
<fabric>site-z</fabric>
