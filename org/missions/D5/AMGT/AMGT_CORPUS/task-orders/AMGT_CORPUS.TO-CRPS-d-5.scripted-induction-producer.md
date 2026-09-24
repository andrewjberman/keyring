# AMGT_CORPUS task order -- `CRPS-d-5` -- ROUND 2: the SCRIPTED induction producer -- one `add_security` call per evidenced backlog name, once, ambiguous and unevidenced names printed and never called, built and dry-exercised here against an injected fake client, FIRED ONLY by the issuer at the drain

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3; the fire's writes are add_security's own and run at the drain under the issuer's credential.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 2. Work ONLY in your worktree (its absolute path is in your prompt).
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/induction_request.py` and
  `lib/research/identity/add_security.py` exist. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~2;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY** beyond the listing
  `induction_request` already does. **NEVER run the real `add_security` in any mode -- its `--dry-run` STILL CALLS
  Bloomberg** (its docstring: "the record is shown from the in-memory response"). Every exercise here goes through an
  INJECTED fake client.

## 1. THE CELL, inlined in full -- `CRPS-d-5` (manifest row R13, NEW; serves FWD-19's induction)

**FWD-19 (the induction half), verbatim:** *"... the 60 today-unresolved folders are inducted by a SCRIPTED producer and
re-ingested ..."*. **`C-NO-VENDOR-CALL` (v0.5), verbatim:** *"This project calls no external vendor API and no Claude API,
WITH ONE EXCEPTION: the identity induction of a backlog name may make ONE Bloomberg `reference_data` call per name, ONCE,
through `add_security`, from a SCRIPTED DETERMINISTIC PRODUCER. Every other vendor surface stays barred, the Claude API
stays barred, and the Model-block figure pull is NOT covered by this exception."* **Its three limits:** an agent turn is
not a producer; the word authorizes the CALLS, not a PICK (America Movil AXMB/AMXB stays REFUSED with its reason); the
Model pull is a separate word. **Andrew's mechanism constraint (R-21), verbatim:** *"the pull should be
deterministic/scripted in nature like the existing pull, i do not like the idea of relying on an agent for something a
script can do way better."*

**THE EXISTING PRODUCER YOU WRAP (read-only, `lib/research/identity/add_security.py`):** ONE `reference_data` call lands
a security's identity; `main(argv)` takes `--folder "<folder>"` (or `--bloomberg`), `--as-of YYYY-MM-DD`, and exactly one
of `--dry-run` / `--write-pool`; it is idempotent on `registrations.json` (an already-registered folder makes NO call and
prints `already-registered ...`); `--write-pool` REFUSES an `--as-of` that is not today (UTC); it REFUSES a security_key
collision (rc 4) and prints `bloomberg_calls N` on every path; the client seam is `_load_blp_client()`.

**RULED -- what you build, new module `lib/research/corpus/induction_run.py`:**
- `rows_for_run(root)`: the induction request rebuilt FRESH (`induction_request.measure_population` +
  `build_request` over the backlog the universe carries UNRESOLVED) -- never a stored `induction_request.json`.
- `run(rows, as_of, call, stdout)` where `call(argv) -> rc` defaults to `add_security.main`: for every row in state
  `EVIDENCED`, ONE call `["--folder", <folder>, "--bloomberg", "<root> <cc>", "--as-of", as_of, "--write-pool"]` (AMENDMENT 2: the report-evidenced ticker root and exchange code from the request row, which agree with the folder token by amendment 1; NEVER `--folder` alone), its rc and printed lines captured;
  every row NOT evidenced (`AMBIGUOUS`, `NO_EVIDENCE`, any other state) is printed with its reason and NEVER called.
  Per-row read-back `{folder, state, called, rc, outcome: registered|already-registered|refused|unresolved|error,
  security_key|reason, bloomberg_calls}` (the outcome parsed from `add_security`'s own printed lines); totals FIRST and
  LAST: `population P evidenced E ambiguous A other O called C registered R already_registered K refused F errors X
  bloomberg_calls B sum P` where E + A + O = P and C = E. The read-back is written as JSON to your deliverables dir
  (`induction_run_<as_of>_<mode>.json`).
- **`--dry-run`:** the whole loop with an INJECTED fake `call` that records argv, makes no call and returns a scripted rc
  per folder (registered for the first evidenced row, already-registered for the second, refused for one, so every
  outcome branch is exercised); `bloomberg_calls 0` by construction. Under the test poison, `add_security._load_blp_client`,
  boto3 client construction, `subprocess.run` and sockets all RAISE, and the test proves each poison bites.
- **`--fire`:** REFUSED unless BOTH `OPAL_INDUCTION_FIRE=1` is set in the environment AND `--as-of` names today (UTC), and
  refused inside pytest (`PYTEST_CURRENT_TEST` set). The refusal prints `REFUSED: --fire requires OPAL_INDUCTION_FIRE=1
  and today's --as-of; this is the issuer's drain act under R-16 V2 / R-21 / C-NO-VENDOR-CALL v0.5` and exits 3 with
  `bloomberg_calls 0`. When permitted, `--fire` runs `run()` with the REAL `add_security.main` -- you never exercise this
  branch; the issuer does, once, on this terminal, per `integrations/bloomberg/READ_HERE.md`.
- **Determinism:** rows are processed in the request's sorted order; the same rows and the same rcs produce a
  byte-identical read-back apart from the timestamp line.

- **ISSUER AMENDMENT 1 (2026-09-24 ~07:3xZ) -- THE FOLDER-VS-REPORT DISAGREEMENT REFUSAL, a general rule, never a name:** the
  dry-run read-back showed `America Movil AXMB MM` EVIDENCED and CALLED with security_key `AMXB_MM_Equity`: the classifier
  sees only the REPORTS' ticker (AMXB) and never compares it to the FOLDER's own token (AXMB). `3.0.0_SA_CVO~Z`'s standing
  ruling (carried by the CTO's R-16 and the PRD's A.4 limit 2): a two-character transposition between the folder and the
  report, with no third source, is a REFUSAL with a reason, never a pick. So, BEFORE any call: parse the folder name's own
  trailing Bloomberg token pair (`<TICKER> <CC>`: the last two whitespace tokens when the last is a 2-3 letter exchange code
  and the one before it is an all-caps ticker; a folder with no such pair contributes no token and is not refused by this
  rule). An EVIDENCED row whose report ticker ROOT differs from the folder's ticker token is state `DISAGREEMENT`, NEVER
  called, printed with `folder_token X report_token Y no third source` as its reason, and carried in the read-back like any
  refused row. The totals line becomes `population P evidenced E ambiguous A disagreement D other O called C registered R
  already_registered K refused F errors X bloomberg_calls B sum P` where E + A + D + O = P and C = E. A folder whose tokens
  AGREE is unchanged. This is the mechanism form of the ruling: it refuses every future transposition, not one name.

- **ISSUER AMENDMENT 2 (2026-09-24 ~08:1xZ) -- THE CALL CARRIES `--bloomberg`, MEASURED AT THE FIRE:** the issuer's fire at 08:02Z
  (20 calls as issued) made ZERO Bloomberg calls: `add_security._discover` with `--folder` alone reads the folder's ONE PAGER
  workbook for the identifier (`build_universe.discover_bloomberg_ticker`) and returned UNRESOLVED for all 20 -- 12 folders carry
  no ONE PAGER workbook, 8 carry the template placeholder `AAPL US` -- and persisted 20 UNRESOLVED registration rows (reverted
  by the issuer as the uncommitted output of a mis-shaped call; the diff is kept in the issuer's deliverables). The request row
  ALREADY holds the report-evidenced identifier (`root`, `cc` from `classify_folder`, agreeing with the folder token under
  amendment 1), so the call passes BOTH `--folder <folder>` (add_security's idempotency key and registration folder) AND
  `--bloomberg "<root> <cc>"` (the identifier: `_discover` takes the READY branch and the ONE reference_data call is made).
  The read-back gains `bloomberg_arg` per called row. `--dry-run`'s fake `call` must ASSERT that every argv carries both
  `--folder` and a parseable `--bloomberg`, and a test proves a `--folder`-only argv is refused by the producer itself
  (never reaching `call`). AC2's totals line and expect are unchanged (bloomberg_calls 0 in a dry run by construction).

**What this cell does NOT do:** no edit under `lib/research/identity/` (another lane's surface; imported, never
changed); no Bloomberg call; no S3 write; no ingest re-run (the issuer runs the existing `ingest` after the fire).

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0, chain B, the only cell on this slot. `CRPS-d-4` (the census) runs after this cell's fire.

## 3. SURFACES

<paths>
lib/research/corpus/induction_run.py
lib/research/corpus/tests/test_induction_run.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-5.scripted-induction-producer.md
</paths>

**READ-ONLY:** `lib/research/corpus/induction_request.py`, `lib/research/corpus/backlog.py`, `lib/research/corpus/library.py`,
`lib/research/identity/add_security.py`, `lib/research/identity/crosswalk.py`. Scratch in `.scratch/d5/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII source, LF, Python 3.9-compatible.**
- **Tests:** offline under the poison plus the `_load_blp_client` poison, each poison positive-controlled; the fake `call`
  covers every outcome branch; the `--fire` refusal is asserted with and without the env var and with a non-today as-of.
- **Surprise rows:** `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.
- The `--dry-run` LISTS the library through `induction_request`'s own readers (opens `rb` only where that module already
  does, to gather evidence); it writes nothing anywhere but your deliverables dir.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 600`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_induction_run.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.induction_run --dry-run --as-of 2026-09-24 2>&1 | tail -3</invocation><expect>population ([1-9]\d*) evidenced \d+ ambiguous [1-9]\d* disagreement [1-9]\d* other \d+ called \d+ registered \d+ already_registered \d+ refused \d+ errors \d+ bloomberg_calls 0 sum \1\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.induction_run --fire --as-of 2026-09-24 2>&1 | tail -3</invocation><expect>(?s)REFUSED: --fire requires OPAL_INDUCTION_FIRE=1.*bloomberg_calls 0\b</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe against the REAL backlog (the population and the ambiguous count are read
  from the library and the crosswalk; the calls are faked) -- `ambiguous` must be >= 1 (Copa and Uber collide with existing keys today) and `disagreement` must be >= 1
  (America Movil AXMB vs AMXB); AC3 the difference control on the gate the fire sits behind (reason: the one thing this cell must
  never do is call Bloomberg from a worker turn, and the refusal is the proof it cannot).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-d-5.scripted-induction-producer.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every criterion passes. Commit via safe-commit with the pathspec of exactly the
   files you changed plus the instance and the dry-run read-back JSON.
4. Report ONCE: the AC2 totals line, the list of AMBIGUOUS folders with their reasons, and the AC3 refusal line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER REOPEN 2026-09-24 ~07:3xZ (2.0.0_SA_COO~X):** the worker's first close (8afe2f1187) was VALID on the face as issued; the face was
incomplete -- it carried the CVO's AXMB/AMXB refusal as a NAME in the bounds and no MECHANISM in the rules, and the fresh
request classifies that folder EVIDENCED. Amendment 1 adds the folder-vs-report disagreement refusal and one token to the totals
line; AC2's expect gains `disagreement [1-9]\d*`; the order is re-opened to `pending` and the same worker is continued on it.

**ISSUER REOPEN 2 2026-09-24 ~08:1xZ (2.0.0_SA_COO~X):** the fire as issued reached the vendor ZERO times (add_security's folder
path, not the report evidence). Amendment 2 fixes the call shape; the order re-opens to `pending` for the same worker. The
issuer's fire read-back is at deliverables/2.0.0_SA_COO~X/induction_run_2026-09-24_fire_attempt1.json.

**ISSUER NOTES:** the FIRE is the issuer's drain act (decomposition s.5 duty 1, s.9 hold): after this cell drains VALID,
ONE exchange with `2.0.0_SA_COO~Z` on the pinned candidate (`add_security` is its surface), READ_HERE s.2 sign-in state
checked, then `OPAL_INDUCTION_FIRE=1 python -m lib.research.corpus.induction_run --fire --as-of <today>` once, the
read-back recorded in this lane's deliverables, then the existing `ingest` re-run. A worker face carries the vendor ban;
Andrew's word authorizes a scripted producer; the seat holding both the word and the terminal runs it.

<status>pending</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
