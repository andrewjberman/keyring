# AMGT_RESAPP task order -- `AMGT-rk-67` -- `comp-secrets get`: `--json --reveal` emits JSON carrying the value instead of silently falling through to the human text block, a new `--value-only` flag prints the bare value and nothing else, `--help` stops implying the bare-value idiom works, and the DEFAULT `--reveal` text block stays byte-identical so the one real parser keeps reading it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-67</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~67</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one repository CLI and adds one offline test file; it
  arms no cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act of any kind and MUST NOT: every test stubs
  the Secrets Manager client with a fake returning a sentinel; no role, policy or grant is read or changed, and
  Secrets Manager is never called.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~67`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~67;`. **NEVER RUN AN INSTALL.** **READ SECTION 4's SECURITY BOUNDS
BEFORE YOUR FIRST COMMAND.**

## 1. THE CELL, inlined in full -- `AMGT-rk-67` (R16 C3; row `AMGT_RESAPP-Z-W50-S4`'s two CLI findings; process)

**The ruling this cell implements, verbatim (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_COMP_SECRETS_REVEAL_CONTRACT_20260919T155xZ.md`
point 2, `:46-51`):** *"`--json --reveal` IS A DEFECT, NOT A CONTRACT. A flag combination that is accepted and
silently ignored is worse than one that errors. REC: `--json --reveal` emits JSON carrying the value. NOT DONE HERE:
`comp-secrets` is a shared surface and five seats plus a dozen worker subagents are running against it this hour;
changing a secrets CLI mid-round is an act that wants its own window, not a rider on a ruling. It is proposed,
carded, and left for a quiet window or Andrew's word -- proposing is legal, implementing is the part that waits."*

**The hold is LIFTED, verbatim (`ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.1, `:29-36`):** *"C3 -- the
hold is LIFTED. This seat's own ruling ... held the `--json --reveal` fix for 'a quiet window or Andrew's word.' The
COO's own read is right: Andrew's ~14:58Z allocation word names width, not this specific change, so it is not the
word the hold waits on. But the quiet window is now, measured, not asserted: round 15 is closed, round 16 has not yet
spawned a worker, and the COO's own census states current width at receipt was zero -- no live worker is reading
`comp-secrets` output this moment. An additive change (the default text block stays byte-identical; only
`--json --reveal`'s silent fall-through gains a real JSON emission) cannot break a caller that does not exist yet.
RULED: cut C3 in this wave, its own test file per the census (stubbed client, a sentinel value, no real secret
printed)."*

**The same ruling's point 1 (`:41-45`) is the contract you PRESERVE, not change:** the default `--reveal` output is a
DESCRIPTOR BLOCK whose last line is `value:` plus padding plus the value; callers needing the bare value extract that
line. Point 3 (`:52-54`): no gate is created. The ruling's "third finding" (`:56-69`) -- that a tool keeping a secret
out of its own log cannot keep it out of a document written ABOUT the tool -- is WHY section 4 exists.

**THE MEASURED STATE, at HEAD `1e2a54bf0f` (cite these lines; re-read the file at your own branch HEAD before
editing and STOP with a row if any citation moved):**
- `.tools/comp-secrets`, 364 lines, pure ASCII (non-ASCII byte delta 0), LF-only (crlf 0), measured by the issuer at
  the cut. Module docstring `:9-11` states the logging guarantee: *"the actual value prints ONLY with --reveal, to
  STDOUT ONLY. The auto-logger records `tool + args` (the secret NAME), NEVER stdout."*
- `cmd_get(args)` `:214-255`. It builds `meta` at `:229-235` (`name`, `firm`, `arn_tail`, `version`, `last_changed`,
  `rotation`, `binary`). **THE DEFECT, `:236-238`:** `if args.json and not args.reveal:` prints `meta` plus a `shape`
  field as JSON -- so `--json --reveal` does NOT enter this branch, falls through to the text block at `:239-251`, and
  returns 0 with no warning. The text block: `:239-241` print `name:`, `firm:` and `arn:` unconditionally; `:242-244`
  print a binary placeholder line and return 0 for a binary secret; `:245-251` print `value:       <value>` under
  `--reveal` (the comment at `:246-250` restates the logging guarantee); `:252-254` print `shape:` plus a redaction
  notice otherwise. Every text line goes through `_ascii()` (`:64-65`), which replaces non-ASCII with `?`.
- `main()` `:341-360`; the `get` subparser `:348-351`. **`:350`:** `pg.add_argument("--reveal", action="store_true",
  help="print the cleartext value (stdout only; not logged)")` -- the help text the ruling (`:35-37`) calls true about
  what is not logged and misleading about what is printed: it reads as if `--reveal` prints the bare value.
- `_client()` `:68-90` builds the real boto3 client and PROBES it with `list_secrets` -- the seam your tests replace
  (monkeypatch the module's `_client` to return a fake; never let the real one run). `_resolve()` `:150-164` calls
  `_all_secrets()` `:136-147`, which pages `list_secrets` -- your fake must answer `list_secrets(**kw)` with a
  `SecretList` holding one entry (`Name`, `ARN`, and optionally `LastChangedDate`/`RotationEnabled`) and no
  `NextToken`, and `get_secret_value(SecretId=...)` with `{"SecretString": "SENTINEL-NOT-A-SECRET", "VersionId": ...}`.
- The script has no `.py` suffix; load it in a test with `importlib.machinery.SourceFileLoader("comp_secrets",
  "<abs path>/.tools/comp-secrets")`. It inserts `org/modules/graph` on `sys.path` at `:48` itself and imports
  `sovereign_held` at `:49` -- loading it needs no network.
- **The ONE real parser of the default block:** `lib/research/social/collect.py:178-196`, `read_api_key()`, runs
  `[sys.executable, <repo>/.tools/comp-secrets, "get", secret_name, "--reveal"]` via `subprocess.run` (`:183-188`)
  and returns the first line starting `value:`, split on the first `:` and stripped (`:189-193`). **It calls the REAL
  tool against REAL AWS -- your test must NEVER call it unpatched** (section 4).
- Caller census at the cut (the census @a0d593560c item C3, measured by a read-only drafter): 145 occurrences of
  `comp-secrets get` in 70 files; ONE real parser (above); NO code caller passes `--json` with `get`. So the change is
  additive exactly as long as the default text block stays byte-identical.
- `.tools/tests/test_comp_secrets.py` does NOT exist at the cut. Existing siblings to copy the house shape from:
  `.tools/tests/test_comp_*.py` (for example `test_comp_schedule.py`, `test_comp_find_battery.py`).

**RULED, what you build:**

1. **`.tools/comp-secrets`, `cmd_get` `:214-255`:**
   - **`--json --reveal`:** emit `json.dumps({**meta, "value": value}, indent=2)` and return 0; for a BINARY secret emit
     `{**meta, "value": null}` and return 0 (`meta["binary"]` already says true -- truthful, not an error). The
     existing `--json` WITHOUT `--reveal` branch (`meta` + `shape`) is UNCHANGED. JSON uses `json.dumps`' default
     `ensure_ascii=True`, so a non-ASCII value is escaped losslessly, never `?`-substituted.
   - **`--value-only` (NEW flag on the `get` subparser):** prints the bare value followed by exactly one LF and NOTHING
     else (no `name:`/`firm:`/`arn:` lines), return 0. It REQUIRES `--reveal` -- without it, exit 2 with a usage line on
     STDERR and nothing on stdout (preserves the docstring's invariant that cleartext appears ONLY under `--reveal`).
     `--value-only` together with `--json` is refused the same way (exit 2, stderr, empty stdout). For a binary secret
     it exits 1 with a stderr line and empty stdout (there is no text value to print). It prints through the same
     `_ascii()` path as the text block -- no new encoding behaviour; the lossy `?` substitution for non-ASCII values is
     a known, SEPARATE issue this cell names and does not fix (row it if you hit it).
   - **The DEFAULT `--reveal` text block (`:239-251`, and the redacted path `:252-254`) stays BYTE-IDENTICAL** for
     every input that does not pass `--value-only` or `--json`.
2. **`.tools/comp-secrets`, `:350` `--help` text:** reword so it no longer implies a bare value -- it names that
   `--reveal` prints a descriptor block whose `value:` line carries the cleartext, and points at `--value-only` for the
   bare value. Add `--value-only`'s own `help=` saying it requires `--reveal` and prints the bare value only. Update
   the module docstring's `Usage:` line at `:21` to show the new flag. The logging comment at `:246-250` and the
   docstring guarantee at `:9-11` stay TRUE and unedited in substance.
3. **`.tools/tests/test_comp_secrets.py` (NEW)**, pytest, offline by construction, loading the script with
   `SourceFileLoader` and monkeypatching the loaded module's `_client` with a fake (never the real one), invoking
   `cmd_get(argparse.Namespace(ident=..., reveal=..., json=..., value_only=...))` and capturing stdout/stderr with
   `capsys`. Named arms (the `-k` names below must match):
   - `test_json_reveal_emits_value` -- `--json --reveal`: `json.loads(stdout)["value"] == "SENTINEL-NOT-A-SECRET"`, rc 0.
   - `test_json_without_reveal_unchanged` -- `--json` alone still emits `shape` and NO `value` key.
   - `test_value_only_bare` -- `--reveal --value-only`: stdout EXACTLY `"SENTINEL-NOT-A-SECRET\n"`, rc 0.
   - `test_value_only_requires_reveal` -- `--value-only` without `--reveal`: rc 2, stdout empty, the sentinel absent
     from stdout AND stderr. Exercise this one through `main()` with a patched `sys.argv` if argparse does the refusal.
   - `test_text_block_unchanged` -- default `--reveal`: stdout is 4 lines and BYTE-IDENTICAL to the output of HEAD's
     own `cmd_get` on the same fake. Obtain HEAD's copy with `git show HEAD:.tools/comp-secrets` into a temp file under
     `tmp_path`, load it with `SourceFileLoader` under a different module name, patch its `_client` identically, and
     compare the two captured stdouts.
   - `test_collect_parser_still_reads` -- call `lib.research.social.collect.read_api_key` with `collect.subprocess.run`
     MONKEYPATCHED to return `subprocess.CompletedProcess(args=[], returncode=0, stdout=<the default --reveal block
     rendered by the NEW cmd_get on the fake>, stderr="")` -- so no real process and no real AWS call ever runs -- and
     assert it returns the sentinel.
   - `test_new_modes_never_leak_to_stderr` -- for both `--json --reveal` and `--reveal --value-only`, the sentinel does
     not appear in captured stderr. (The auto-logger itself lives in the comp-tool hook, outside this file, and records
     argv -- the secret NAME and flags -- never stdout; this cell does not touch it. The arm proves the new modes add no
     second channel for the value.)
   - `test_binary_modes` -- a fake returning `{"SecretBinary": b"x"}`: `--json --reveal` gives `value` null with
     `binary` true, rc 0; `--reveal --value-only` gives rc 1, empty stdout.
   Every arm uses ONLY the literal sentinel `SENTINEL-NOT-A-SECRET`. No arm reads the environment for credentials,
   builds a real boto3 client or touches the network.

**What this cell does NOT change:** `cmd_list`, `cmd_consumers`, `cmd_rotation`, `_client`, `_resolve`, `_shape`,
`_ascii` or `main()` beyond the `get` subparser's flags and help; `lib/research/social/collect.py` (read only -- it
is the compatibility target, not a surface); the comp-tool auto-logger hook; the surprise-row schema (the ruling's
third finding is a separate schema proposal owned by `3.0.0_SA_CVO~Z`, not this cell); any existing caller.

**THE VALIDATION BAR:** a process cell with no security population and no served output; proven entirely on its
own offline battery with a stubbed client. No live AWS act, no deploy, no vendor call.

## 2. WHERE THIS CAME FROM

**ROUND 16**, decomposition s.24 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-16 rulings
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.1 (`:29-38`) and s.3
(`:78`), answering this seat's candidate census `ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c item C3;
the CTO's own ruling `CTO_RULING_COMP_SECRETS_REVEAL_CONTRACT_20260919T155xZ.md` points 1-3; the row
`AMGT_RESAPP-Z-W50-S4` (filed by `0.9.0_WK_AMGT_RESAPP~50`, disarm owner `1.0.0_SA_CTO~Z`) -- **which lives ONLY on
the held branch `wk-amgt-14-50` and which you must NOT look for** (section 4); everything you need from it is quoted
above from the ruling. PRD v0.13 @1699960261: no FWD or `C-` contract is touched (a fabric-tool cell).

## 3. SURFACES -- what you may read and write

<paths>
.tools/comp-secrets
.tools/tests/test_comp_secrets.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~67/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-67.comp-secrets-json-reveal-contract.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `lib/research/social/collect.py`, the
  CTO ruling, the round-16 rulings, the census and the sibling `.tools/tests/test_comp_*.py` files freely); this block
  governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~67 <0.9.0_WK_AMGT_RESAPP~67@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit (note `.tools/comp-secrets` has no `.py` suffix; AC3
  compiles it explicitly).

## 4. BOUNDS

**SECURITY BOUNDS -- ABSOLUTE, READ FIRST:**
- **NEVER RUN `comp-secrets get ... --reveal` (OR `--value-only`, OR `--json --reveal`) AGAINST A REAL SECRET.** THE
  ONLY VALUE ANY COMMAND IN THIS ORDER MAY EVER PRINT IS THE LITERAL SENTINEL `SENTINEL-NOT-A-SECRET`.
- **NEVER CALL AWS SECRETS MANAGER** -- NO REAL `_client()`, NO `boto3.client("secretsmanager")`, NO `aws
  secretsmanager` COMMAND, NOT EVEN `list`, `rotation` OR A BARE `get` WITHOUT `--reveal`. EVERY TEST STUBS THE CLIENT.
- **NEVER CALL `lib.research.social.collect.read_api_key` WITHOUT `collect.subprocess.run` MONKEYPATCHED** -- UNPATCHED
  IT SHELLS OUT TO THE REAL TOOL AGAINST REAL AWS.
- **NEVER PRINT, QUOTE, LOG OR WRITE ANY REAL SECRET VALUE ANYWHERE** -- NOT IN OUTPUT, A COMMIT MESSAGE, THE PROOF
  INSTANCE, THE SESSION LOG OR A SURPRISE ROW.
- **NEVER READ, SHOW, DIFF, LOG OR CHECK OUT BRANCH `wk-amgt-14-50` OR THE DIRECTORY `C:/tmp/wk-amgt-14-50`.** IT
  CONTAINS A LIVE LEAKED CREDENTIAL. DO NOT SEARCH THE REPOSITORY FOR API KEYS OR CREDENTIAL VALUES, AND DO NOT GO
  LOOKING FOR ROW `W50-S4` -- IT IS QUOTED IN SECTION 1 AS FAR AS YOU NEED IT.
- **IF ANY OUTPUT YOU ARE ABOUT TO RECORD WOULD CONTAIN A REAL VALUE, STOP.** FILE A BLOCKING ROW THAT DESCRIBES ITS
  SHAPE ONLY (e.g. "a 4-line block whose last line is `value: <...>`") -- NEVER ITS CHARACTERS -- WITH DISARM OWNER
  `2.0.0_SA_COO~Z`, AND DO NOTHING FURTHER. THIS IS ROW `W50-S4`'s LESSON: A TOOL THAT KEEPS A SECRET OUT OF ITS OWN
  LOG CANNOT KEEP IT OUT OF A DOCUMENT SOMEONE WRITES ABOUT THE TOOL.

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL.** PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO
alarm, monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH:
never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by changing the default
text block, never by editing `collect.py`, and never by relaxing any security bound above.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the file's line count (364),
non-ASCII delta (0) and CRLF count (0) at HEAD are re-measured by AC3 at your branch HEAD; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W67-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-67"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest .tools/tests/test_comp_secrets.py -v 2>&1 | tail -20</invocation><expect>a final line "N passed" with N at least 8 and 0 failed, the PASSED lines naming test_json_reveal_emits_value, test_json_without_reveal_unchanged, test_value_only_bare, test_value_only_requires_reveal, test_text_block_unchanged, test_collect_parser_still_reads, test_new_modes_never_leak_to_stderr and test_binary_modes; no output line anywhere carries any value other than the literal SENTINEL-NOT-A-SECRET (the file did not exist at the cut -- N is the count this cell creates, not a delta)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-67"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, re
src = io.open('.tools/comp-secrets', encoding='utf-8').read()
body = src.split('def cmd_get(args):', 1)[1].split('\ndef ', 1)[0]
code = '\n'.join(l for l in body.splitlines() if not l.strip().startswith('#'))
print('fallthrough_condition_present', 'if args.json and not args.reveal:' in code and 'args.reveal' in code and not re.search(r'args\.json and args\.reveal|args\.reveal and args\.json', code))
print('json_reveal_branch_present', bool(re.search(r'args\.json and args\.reveal|args\.reveal and args\.json', code)))
print('value_only_flag_declared', '--value-only' in src)
print('help_names_value_only', bool(re.search(r'--reveal.*help=.*value-only|value-only.*help=', src, re.S)))
print('help_line_old_text_present', 'help=\"print the cleartext value (stdout only; not logged)\"' in src)
print('cmd_get_opens_files', 'open(' in code)
"</invocation><expect>fallthrough_condition_present False (the bare "json and not reveal" test no longer decides the --json --reveal case on its own); json_reveal_branch_present True; value_only_flag_declared True; help_names_value_only True; help_line_old_text_present False (the misleading :350 help text is gone); cmd_get_opens_files False (the new modes write no file -- no second channel for the value)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-67"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m py_compile .tools/comp-secrets && echo "py_compile_rc 0" && python -c "
import io, subprocess
for f in ('.tools/comp-secrets', '.tools/tests/test_comp_secrets.py'):
    b = io.open(f, 'rb').read()
    print(f, 'lines', b.count(b'\n'), 'non_ascii_byte_delta', len(b) - len(b.decode('utf-8')), 'crlf', b.count(b'\r\n'))
h = subprocess.run(['git', 'show', 'HEAD~0:.tools/comp-secrets'], capture_output=True).stdout
base = subprocess.run(['git', 'merge-base', 'HEAD', 'SITEZ'], capture_output=True, text=True).stdout.strip()
b0 = subprocess.run(['git', 'show', base + ':.tools/comp-secrets'], capture_output=True).stdout
print('base', base[:10], 'base_non_ascii_byte_delta', len(b0) - len(b0.decode('utf-8')), 'base_crlf', b0.count(b'\r\n'), 'base_lines', b0.count(b'\n'))
"</invocation><expect>py_compile_rc 0; both files print crlf 0; each file's non_ascii_byte_delta EQUALS the base figure printed on the last line for .tools/comp-secrets (0 at the issuer's cut @1e2a54bf0f -- re-measured here from this worktree's merge-base with SITEZ, never assumed) and is 0 for the new test file; base_lines is the pre-edit line count (364 at the cut) and the new line count is larger -- this criterion grades "no non-ASCII and no CRLF introduced", reading the baseline, not a literal written in advance</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. **Before recording any output, confirm it contains no value other than the sentinel** (section 4).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~67/AMGT_RESAPP.TO-AMGT-rk-67.comp-secrets-json-reveal-contract.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once, naming AC1's test count and confirming, in one sentence, that no
command you ran reached Secrets Manager and no value other than the sentinel appears in anything you wrote.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>16</round>
<slot>~67</slot>
<fabric>site-z</fabric>
