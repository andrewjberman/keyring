# AMGT_CORPUS task order -- `CRPS-c-5` -- ROUND 1: the INDUCTION REQUEST for one backlog name the universe carries UNRESOLVED -- both populations measured and printed, one name picked by a stated rule, the exact add-security command and what it WILL add printed BEFORE anything else, an ambiguous identity refused; it EXECUTES NOTHING and calls no vendor, proven by a refusing transport and a positive-controlled poison

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes no store object and makes no AWS write; its crosswalk READ uses the layer's own loader.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **First act:** print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`,
  `.tools/`, `lib/research/corpus/backlog.py`, `lib/research/corpus/library.py`, `lib/research/corpus/extract.py`,
  `lib/research/corpus/tests/conftest.py` and `lib/research/identity/add_security.py` exist. If any is absent, STOP with
  a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~2;`.
- **NEVER INSTALL. NEVER CALL BLOOMBERG, ANY OTHER VENDOR, OR THE CLAUDE API. NEVER RUN `add_security`** (not `--dry-run`
  either: its dry run still makes the Bloomberg call). **NEVER WRITE `lib/research/identity/registrations.json`, the
  crosswalk pool, or any S3 object.**
- **THE RESEARCH LIBRARY IS READ-ONLY:** you may OPEN a file there with mode `"rb"` only. No write, move, rename or delete.

## 1. THE CELL, inlined in full -- `CRPS-c-5` (manifest row R5, outcome FWD-4 as amended in PRD v0.4)

**FWD-4, verbatim (PRD v0.4 @8fbb066b62):** *"A backlog name the universe does not yet carry can be INDUCTED BY ONE
COMMAND -- and this project produces that command's exact request, complete and executable, without calling any vendor.
DONE WHEN EXERCISED -- for one backlog name the universe carries UNRESOLVED, a single act produces the induction request:
it PRINTS what the induction WILL add before anything is added, REFUSES a name whose identity is ambiguous, and is driven
end to end with a REFUSING TRANSPORT and the poison POSITIVE-CONTROLLED, so the run COULD NOT have reached the network
rather than merely having not."*
**Its BOUNDARY, verbatim:** *"the induction ACT ITSELF is AMGT_RESAPP's, not this project's. `add_security` writes that
project's `registrations.json` and crosswalk pool and spends its vendor budget (one Bloomberg reference_data call per
name, even under --dry-run). THIS PROJECT'S HALF ENDS AT THE EXECUTABLE REQUEST."*
**Its POPULATION, verbatim:** *"'resolved but absent from the universe' may be EMPTY BY CONSTRUCTION -- the crosswalk is
BUILT from the universe. The population is therefore the backlog folders the universe carries UNRESOLVED (measured 60 of
93 ...). CRPS-c-5 measures the resolved-absent set and PRINTS BOTH DENOMINATORS; if it is non-empty, the original
population stands beside this one."*
**`C-NO-VENDOR-CALL`, untouched:** *"Nothing in this project calls an external vendor API or the Claude API."*

**THE INDUCTION PATH, measured at L5** (`lib/research/identity/add_security.py`, read-only):
- It takes `--bloomberg '<ROOT> <CC>'` and/or `--folder '<corpus folder>'`, `--as-of YYYY-MM-DD`, and exactly one of
  `--dry-run` / `--write-pool` (`build_parser`).
- With `--folder` and no `--bloomberg`, `_discover` reads the folder's ONE PAGER workbook for the ticker. **For the
  UNRESOLVED folders that read has already failed** (that is why they are unresolved), so `--folder` alone would return
  UNRESOLVED: *"the identifier is NOT guessed from the folder name."*
- `IDENTITY_FIELDS` is the Bloomberg field list the call requests. `_build_identity` is the identity dict it lands.
  `_persist_registration_and_pool` writes the registration row and the pool.
- **So an executable request for an UNRESOLVED folder must carry a `--bloomberg` candidate, and that candidate must be
  EVIDENCED, never guessed.** The evidence is the team's OWN report for that name: the research-pack header block carries
  `Ticker:` (the brief's scan, s.1: *"Header block: Ticker, Name, Sector, Location, Currency ..."*).

**RULED -- what you build:**
1. **`lib/research/corpus/induction_request.py`:**
   - **Both populations, printed first:** from `CRPS-c-4`'s `backlog.build()` (a fresh read), print
     `backlog_folders <N>`, `resolved_absent <a> of <N>` (folders the layer resolves to a `security_key` that the
     universe/crosswalk does NOT carry; measure it through the layer's own loaders, `crosswalk.load_crosswalk` and
     `crosswalk.record_for`) and `unresolved_in_universe <u> of <N>`. Then print `population <which>`: the original
     population if `a > 0`, else the UNRESOLVED one.
   - **Candidate evidence, per folder of the population:** open that folder's report files (`.docx` and `.pdf` only)
     with `"rb"`, extract with `lib/research/corpus/extract.py` `extract(...)` (read-only import), and find the header
     `Ticker:` value and the `Name:` value. Record `{file, locator, passage}`. Validate the candidate's SHAPE with the
     layer's own `crosswalk._parse_bloomberg`.
   - **AMBIGUITY REFUSAL:** a folder is REFUSED (`ambiguous: <reason>`) when its reports state two or more different
     tickers, or when `crosswalk.resolve(<candidate>)` returns a DIFFERENT existing `security_key` (an identity
     collision), or when the resolve reason begins `AMBIGUOUS:`. A folder whose reports state no ticker is `no_evidence`.
   - **Pick rule (stated, deterministic):** the first folder, in sorted order, of the population that has exactly one
     evidenced candidate and is not refused.
   - `python -m lib.research.corpus.induction_request --pick` prints, IN THIS ORDER:
     1. the population lines above, and one `candidate <folder> | <state> | <ticker or -> | <evidence file>` line per
        population folder;
     2. `WILL ADD` followed by, one line each: the folder, the candidate `--bloomberg` value with its evidence passage,
        the `IDENTITY_FIELDS` the call would request (read from the module constant), the registration row's fields
        and the pool the act would write (read from the module's code, named), and the security_key it would mint
        (`<ROOT>_<CC>_Equity`, the layer's grammar);
     3. `REQUEST python -m lib.research.identity.add_security --folder "<folder>" --bloomberg "<ROOT> <CC>" --as-of <UTC today> --write-pool`;
     4. `EXECUTING_SEAT AMGT_RESAPP (the induction act and its vendor word are that project's)`;
     5. `vendor_calls <n>` from a COUNTER incremented by the refusing transport (never a literal), `s3_writes <n>` from a
        counter, `registrations_json_changed <bool>` (its sha256 before versus after).
     It also writes the request as `induction_request.json` into your deliverables dir.
   - **THE REFUSING TRANSPORT AND THE POISON.** Inside the run (not only in tests), before anything else: replace
     `add_security._load_blp_client` with a function that RAISES and increments `vendor_calls`; poison `boto3.client`,
     `subprocess.run` and `socket.create_connection` to RAISE; and print a POSITIVE CONTROL: `poison_positive_control
     raised <k> of 4`, obtained by deliberately calling each of the four sites and catching the raise. **A no-network
     result is evidence only if the run COULD NOT have reached the network.**
2. **`lib/research/corpus/tests/test_induction_request.py`**, offline, under the package poison:
   - **AMBIGUOUS REFUSED:** a stub folder whose two reports state different tickers is refused and never picked;
   - **COLLISION REFUSED:** a candidate that resolves to a different existing key is refused;
   - **NO EVIDENCE, NO REQUEST:** a folder with no stated ticker is `no_evidence`, and no REQUEST line names it;
   - **WILL ADD PRECEDES REQUEST:** in the captured output, `WILL ADD` appears before `REQUEST`;
   - **THE TRANSPORT REFUSES:** calling the patched `_load_blp_client` raises and increments the counter.

**What this cell does NOT do:** it executes no induction, no dry run, no Bloomberg call, no registration or pool write, and
no S3 write, and it changes nothing under `lib/research/identity/`.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8 (chain B), spawned on `CRPS-c-2`'s valid drain, because the candidate evidence is
read with c-2's extractor. The request you produce is handed to `AMGT_RESAPP` by the issuer, never by you.

## 3. SURFACES

<paths>
lib/research/corpus/induction_request.py
lib/research/corpus/tests/test_induction_request.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-5.induction-request-no-vendor-call.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/identity/` (every file, including
`registrations.json`), `lib/research/harvest/`, and the library (`"rb"` only). Scratch in `.scratch/c5/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`,
with the message file written by the Write tool.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (issuer amendment on row `AMGT_CORPUS-Z-S4`): a wrong object you wrote is superseded by a
  NEW key (bump `method_version`), never deleted. An S3 delete is a human-confirmed act on this estate.
- **Pure ASCII source, LF, Python 3.9-compatible.** Zero vendor calls, zero S3 writes, zero identity-layer writes.
- **If NO folder of the population carries an evidenced, unrefused candidate,** that is a VALID measurement and a
  finding, not a failure. Print `picked NONE <reason>` in place of `WILL ADD` / `REQUEST`, and file a row. AC2 then
  records that output, and the issuer carries it to the CTO. **Never relax the evidence rule to produce a pick.**
- **Surprise rows:** `AMGT_CORPUS-Z-W2-S<k>`, next unused `k`, `disarm_owner` `2.0.0_SA_COO~X`. Append, never edit.
- **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement. Never repair or widen it.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_induction_request.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.induction_request --pick 2>&1 | tail -40</invocation><expect>(?s)resolved_absent \d+ of (\d+).*unresolved_in_universe \d+ of \1\b.*(WILL ADD.*REQUEST python -m lib\.research\.identity\.add_security --folder .* --bloomberg .* --write-pool|picked NONE ).*vendor_calls 0\b.*s3_writes 0\b.*registrations_json_changed False.*poison_positive_control raised 4 of 4</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-5" judgment="true"/>
  <criterion id="AC4" cell_refs="CRPS-c-5"><invocation>cd "$(git rev-parse --show-toplevel)" && git status --porcelain -- lib/research/identity/ && echo identity_tree_clean_check_done</invocation><expect>^identity_tree_clean_check_done\s*$</expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c5/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC3 (JUDGMENT, the CVO's):** `induction_request.json` and AC2's output. Is the request complete and executable as
  written, is the candidate's evidence a passage in the team's own report, and is every refusal justified? Record them,
  with NO verdict.
- **AC4:** the expectation matches ONLY when `git status` prints nothing for `lib/research/identity/` (the pattern is
  anchored to the start of the output).
- **`.scratch/c5/hyg.py`** (write it): diff the worktree against `git merge-base HEAD SITEZ` over `lib` and `org`; print
  `outside_allowed [...]`, `changed_files <n>`, per changed `.py` `compiles <bool> crlf <n> non_ascii <n>`, then
  `bad <n>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-c-5.induction-request-no-vendor-call.proof_of_spec.json`,
   each mechanical row carrying its `expect`, the judgment row `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~Z`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit with `--only`, including
   `induction_request.json`.
4. Report ONCE: both population lines, the picked folder and its REQUEST line (or `picked NONE` with the reason), and the
   counters.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the cut depended on one read the PRD did not make. `--folder` alone cannot induct an UNRESOLVED folder,
because its one-pager already failed, so the request carries an evidenced `--bloomberg` candidate from the team's own
report header. That also moved this cell's edge from c-4 to c-2 (decomposition s.4, amended before the cut). The handoff
of the request to `AMGT_RESAPP` is this seat's, at the drain.

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
