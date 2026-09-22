# AMGT_RESAPP task order -- `AMGT-rk-105` -- `state_put_filing_attempt` treats an existing filing_attempt whose OUTCOME is unchanged (timestamps and live counters excluded) as SKIP-HELD instead of raising, so a multi-name battery run continues past an unchanged-unresolved name; the RESOLVED-supersede half is a RECORDED READER CHANGE for a later paired cell; CODE ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-105</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~105</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits three library modules and adds one test file; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; every test and script uses a STUB
  S3 client; the one live AWS act (AC0's read-only GET of two filing_attempt objects) runs under the seat's existing
  read credentials, and nothing is written to AWS by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~105`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
`.tools/` and the paths in section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~105;`. **NEVER RUN AN INSTALL.** Never read, show,
diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-105` (round 27, ahead of the B2 run)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24216, 2026-09-22T12:21:28Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T122128Z_1.0.0_SA_CTO_Z_Re_24215__all_5_calls_RULED_--_round_27_.md`,
lines 9-17):

> CALL 1: YES, a code-only cell, as recommended.
> - An existing filing_attempt for an unchanged UNRESOLVED outcome prints SKIP-HELD and does not raise.
> - "Unchanged" is judged on the outcome fields, never on the timestamp.
> - Criterion: a stub re-run of an unchanged unresolved name continues to the next name, with 0 puts for that key.
>
> CALL 2: FOLD it into the same cell, as recommended. There is NO delete.
> - The cell reads the portal's reader of filing_attempt FIRST.
> - If a RESOLVED record can supersede the old attempt with no reader change (a new key or a field the reader already honours), build that.
> - If it needs a reader change, that is a SERVED act: it takes a CTO/COO pair before deploy, and the cell stops at the code and names the pair.

**THE MEASURED STATE at SITEZ `d3ba12c64b` (RE-READ every line at your branch HEAD before editing):**

- **The one writer function:** `lib/research/harvest/filings.py:239-301` `state_put_filing_attempt(security_key, body,
  client=None)`. It makes a conditional `put_object(..., IfNoneMatch="*")` (`:266-273`). On `PreconditionFailed`
  (`:275-278`) it reads `head_object` metadata `document-sha256` and RAISES `store.HarvestStoreError` when it differs
  from the new body's sha (`:281-285`). It then reads back and raises on a mismatch (`:287-293`). The key is the fixed
  object `UNRESOLVED-SOURCE.json` under `amgt/harvest/state/filing_attempt/security_key=<slash-safe>/` (`:250-253`).
- **WRITER CENSUS, call sites of `state_put_filing_attempt`: N = 6.** `lib/research/filings/fetch.py:500` (inside
  `persist`, which the battery CLI calls at `lib/research/filings/battery.py:1350` under `--write-pool`),
  `lib/research/filings/batch.py:412` and `:672`, `lib/research/filings/analyze.py:1590`, and
  `lib/research/harvest/filings.py:370` (the M2 mover). Fixing the ONE function covers all six.
- **Why an unchanged re-run raises today:** the body carries `retrieved_at` (`fetch.py:269`, `_now_iso()`), and every
  battery attempt carries `seconds`. So a re-run of an unchanged outcome has a different sha and raises at `:281-285`.
  Measured at the cut: the live objects for CSL (`retrieved_at` 2026-09-21T17:22:05Z) and 6861 (2026-09-19T06:20:51Z)
  each carry 5 battery attempts. The free-text `reason` strings embed LIVE COUNTERS (6861 step 1 names the SEC ticker
  table's row count, and step 4 names pages visited), so a byte compare of `reason` would read "changed" on an unchanged
  outcome. CAT has no object (NoSuchKey).
- **READER CENSUS -- the supersede question (CALL 2), N = 5 readers of that key:**
  - `lib/research/management/roster.py:1145-1164` (`load_source_object`): reads SILVER FIRST and state ONLY when no
    silver row exists. A RESOLVED name already supersedes structurally, so this reader needs no change.
  - `lib/research/management/batch.py:116-135` (`census_filings`): silver first, then state. It needs no change.
  - `lib/research/filings/analyze.py:1370-1386` and the second reader near `:1440-1450`: silver first, then state.
    They need no change.
  - **`lib/research/api/scoped_amgt.py:1954-1981` `_read_filing_source_object`, used at `:2052-2055`: THE SERVED
    ADAPTER READER. It is NOT silver-aware.** It reads the fixed state key whenever the Thesis bundle's
    `drafting_status` is ABSENT, and it surfaces the object's `reason` as `drafting_reason`. The B2 run is
    fetch-and-store only, with no analysis, so a name that RESOLVES under B2 keeps `drafting_status` ABSENT. This reader
    would then keep serving the OLD unresolved reason.
  - The adapter cannot read parquet silver (its docstring, `:1963-1966`: no `lib.research.harvest.store`, no pyarrow in
    the deployed package), and the state key is write-once. **So NO write-side act can supersede the old attempt without
    a reader change. CALL 2's branch is: the reader change is a SERVED act, and it is NOT in this cell.**
- **Tests at the cut:** `lib/research/harvest/tests` **72 passed**; `lib/research/filings/tests` **100 passed**;
  `lib/research/management/tests` **95 passed, 13 subtests**. `lib/research/harvest/tests/test_filings.py:391`
  asserts `src.count("put_object") == 1` in the harvest filings module. Keep exactly ONE `put_object` call.

**RULED, what you build:**

1. `lib/research/harvest/filings.py`:
   - Add `_filing_attempt_outcome(document)`. It returns the OUTCOME projection of a filing_attempt object, the tuple
     of these fields only:
     - `status`, `security_key`, `accession`, `filing_identity`, `verified_site`;
     - `battery.order` and `battery.winner`;
     - for each `battery.attempts[i]`, the fields (`step`, `route`, `key`, `url`, `http_status`, `document_sha256`,
       `language`).
   - It EXCLUDES `retrieved_at`, `parser_version`, every `seconds`, every `tests`, and every free-text `reason` (the
     top-level one and each attempt's), because a `reason` embeds live counters. State that rule, and the measured
     reason for it, in the docstring.
   - In `state_put_filing_attempt`, when the sha differs (`:281`), `get_object` the existing body. If
     `_filing_attempt_outcome(existing) == _filing_attempt_outcome(new)`, return the receipt with `"skip_held": True`,
     `"existed": True` and `"put_performed": False`, and SKIP the read-back sha check. Otherwise raise exactly as
     today. Every receipt carries `"skip_held"` (False on every other path).
   - A malformed or non-JSON existing body is NOT skipped: raise as today.
2. `lib/research/filings/fetch.py` `persist`: carry `skip_held` into its returned dict (False on every path that
   does not write state).
3. `lib/research/filings/battery.py`, the `--write-pool` print in the per-name print block: when
   `receipt.get("skip_held")`, print `SKIP-HELD: s3://opal-data-harvest/<key> (unchanged UNRESOLVED outcome; held
   object kept)` INSTEAD of the `OK: uploaded` line. Every other line stays byte-identical.
4. New `lib/research/harvest/tests/test_filing_attempt_skip_held.py`, using a stub S3 client that enforces
   `IfNoneMatch`, stores `document-sha256` metadata, and counts `put_object`, `head_object` and `get_object` calls:
   - `test_unchanged_outcome_different_timestamp_is_skip_held`: 0 successful puts on the second call, and
     `skip_held` True.
   - `test_changed_outcome_still_raises`: a different attempt `http_status` raises `HarvestStoreError`.
   - `test_reason_counter_drift_is_unchanged`: only a digit inside a `reason` differs, and the result is SKIP-HELD.
   - `test_first_write_unchanged`: an absent key gives 1 put and `skip_held` False.
   - `test_malformed_existing_body_raises`.
   - `test_battery_three_names_continue_past_skip_held`: a stubbed `run_battery` over 3 names, the middle one
     UNRESOLVED with an existing held object of the same outcome and a different `retrieved_at`. `battery.main` with
     `--write-pool` over the stub client prints `SKIP-HELD` for the middle name, reaches the THIRD name, and records 0
     successful puts for the middle key.

**What this cell does NOT change:**
- `lib/research/api/scoped_amgt.py` (the served reader; a WALL);
- every other writer call site (they inherit the fix);
- `store.py`, the key grammar, the object name, the S3 objects;
- the portal.
There is no S3 write, no S3 delete and no deploy.

## 2. WHERE THIS CAME FROM

**ROUND 27**, decomposition s.35 (cut by `2.0.0_SA_COO~Z`), on the CTO's ruling msg 24216 (on msg 24215).
- The held B2 draft (rk-102) found that its multi-name `--write-pool` run would raise at CSL and never reach 6861.
- Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/filings.py
lib/research/filings/fetch.py
lib/research/filings/battery.py
lib/research/harvest/tests/test_filing_attempt_skip_held.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~105/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-105.filing-attempt-skip-held.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** That includes `lib/research/api/scoped_amgt.py`,
  `lib/research/harvest/store.py` and every existing test file. Reads need no grant.
- Scratch is `<your worktree>/.scratch/r105/` only, and is never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~105 <0.9.0_WK_AMGT_RESAPP~105@opal.agent>" -F <msgfile> -- <paths>`,
  with the message file written by the Write tool. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **CODE ONLY.** No S3 write, no S3 delete, no deploy, no vendor call. AC0's two GETs are the only live AWS act.
- **Imports in tests use QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1).
- **Run each test directory in its OWN pytest call.**
- **A script that carries a backslash is a FILE** (W84-S1).
- **Every comparison is pinned to `d3ba12c64b`.**
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row. It is
  never repaired or widened, and never satisfied by editing a WALL.
- **COUNT BARS ARE READ AT SPAWN (AC0) and each prints its denominator.**
- **SURPRISE ROWS:**
  - Ids are `AMGT_RESAPP-Z-W105-S<k>`, and each row carries `"project": "AMGT_RESAPP"` and `"fabric": "site-z"`.
  - Append by textual splice inside the one fenced JSON array.
  - `disarm_owner` is `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; each runs under timeout 600)

`.scratch/r105/ac0.py`:
```
import boto3, json, subprocess
print("pin_object", subprocess.run(["git", "cat-file", "-t", "d3ba12c64b"], capture_output=True, text=True).stdout.strip())
src = open("lib/research/harvest/filings.py", "rb").read().decode("utf-8")
print("put_object_count", src.count("put_object"))
calls = subprocess.run(["git", "grep", "-n", "state_put_filing_attempt(", "--", "lib"], capture_output=True, text=True).stdout.splitlines()
calls = [c for c in calls if "/tests/" not in c and "def state_put_filing_attempt" not in c]
print("writer_call_sites", len(calls))
s3 = boto3.client("s3", region_name="us-east-1")
for k in ("CSL_AU_Equity", "6861_JP_Equity"):
    o = json.loads(s3.get_object(Bucket="opal-data-harvest", Key="amgt/harvest/state/filing_attempt/security_key=%s/UNRESOLVED-SOURCE.json" % k)["Body"].read())
    print("held", k, o["status"], "attempts", len((o.get("battery") or {}).get("attempts") or []), "retrieved_at", o.get("retrieved_at"))
```

`.scratch/r105/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "d3ba12c64b", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
src = open("lib/research/harvest/filings.py", "rb").read().decode("utf-8")
print("put_object_count", src.count("put_object"), "delete_calls", src.count("delete_object"))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-105"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r105/ac0.py && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: "pin_object commit"; "put_object_count" P0 (measured 1 at the cut); "writer_call_sites" W0 (measured 6 at the cut); two "held" lines, each UNRESOLVED-SOURCE with its attempts count and retrieved_at; then the three suite lines H0 (72), F0 (100) and M0 (95, 13 subtests). Record every value: these are the baselines every later bar is written against. A drifted count is recorded, not a fail</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-105"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_filing_attempt_skip_held.py -v -p no:cacheprovider 2>&1 | tail -10</invocation><expect>"6 passed" and 0 failed, with the six named tests PASSED -- including test_battery_three_names_continue_past_skip_held proving the third name is reached with 0 successful puts for the middle key, and test_changed_outcome_still_raises proving a changed outcome is still refused</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-105"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"N passed" with N = H0 + 6 and 0 failed</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-105"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>filings "F0 passed" and management "M0 passed" (with its subtests), each unchanged from AC0 and with 0 failed</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-105"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r105/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/filings/battery.py, lib/research/filings/fetch.py, lib/research/harvest/filings.py and lib/research/harvest/tests/test_filing_attempt_skip_held.py; "put_object_count" equals P0 and "delete_calls 0"; each file "compiles True crlf 0" with non_ascii_chars equal to its value at the pin (0 for the new file)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~105/AMGT_RESAPP.TO-AMGT-rk-105.filing-attempt-skip-held.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4`; rc 0 is
   the verdict.
3. Flip the order's status (on the record face) to `complete` only if every criterion PASSES. Commit with
   `--only -- <paths>`.
4. Report ONCE, naming the suite counts before and after, AC1's six test lines, and AC4's file list.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r105/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **CALL 2's branch is the READER CHANGE, from a 5-reader census.** Four readers are already silver-first, so a
   RESOLVED name supersedes structurally there. The fifth, the SERVED adapter reader
   `scoped_amgt._read_filing_source_object` (`:1954-1981`, used at `:2052-2055`), is not silver-aware. It cannot read
   parquet in the Lambda, and the state key is write-once. So no write-side act can supersede it.
   - **A LATER PAIRED CELL**, with the pair `NEVER_WIDEN_ROUND28_<cell>_{COO,CTO}_HALF.md` (an adapter redeploy with the
     AC7 closure check), picks ONE design:
     - (i) The writer adds a sibling marker `RESOLVED.json` under the same partition when a battery run resolves a name
       that holds an UNRESOLVED marker, and the reader checks it first. This is additive and never a delete.
     - (ii) The reader gates the reason on the generated `_harvest_prefixes` silver presence through a JSON sidecar.
   - REC: (i), which is one GET and adds no new dependency.
   - Until that cell drains, a name that RESOLVES under B2 shows its OLD unresolved reason on the Thesis tab. Say so on
     Andrew's card.
2. **The outcome projection EXCLUDES free-text `reason`.** Measured: the live reasons embed counters that move between
   runs (6861 step 1 names the SEC ticker table's row count, and step 4 names pages visited). A byte compare would call
   every re-run "changed" and raise, which is the very failure this cell removes.
   - The held reason therefore stays served after a SKIP-HELD. It is the reason of the same outcome, with an older
     counter.
3. **A CHANGED unresolved outcome still RAISES, as today.** The key is write-once and there is no delete. A name whose
   attempts changed between runs still stops a multi-name run.
   - Open for the CTO: should a changed-unresolved outcome also continue, with the loop printing `CHANGED-HELD` and
     keeping the old object? That would need its own ruling, since it serves a stale reason by design.

<status>pending</status>
<round>27</round>
<slot>~105</slot>
<fabric>site-z</fabric>
