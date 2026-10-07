# AMGT_RESAPP task order -- `AMGT-bb-7` -- THE POOL RECORD CARRIES ITS LEGAL NAME AND NAME SEARCH READS IT (ROW Z-W275-S1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~293</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_E_NOTES.md) -- 100 of 243 pool records carry a name search can read; 'apple' and 'microsoft' answer nothing; this project's own stored objects name 243 of 243. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-293` (branch `wk-AMGT_RESAPP-293`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-293`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-7` (round 78, decomposition s.86)

Typing a company name into the search lists nothing for 143 of the 243 companies we hold, because their stored record
carries no name: "apple" and "microsoft" both answer "no company we cover matches". The names exist. This project's own
stored universe objects (`s3://opal-data-harvest/universe/v1/<date>.json`) carry the company name of every holding, and
68 records carry the name their own registration stored. Make the builder of the stored name list put a legal name on
every record, state where it came from, and make the search read it.

You do NOT write the stored name list. The issuer mints it after your cell drains. Your proof is a build in memory.

**File 1: `lib/research/identity/crosswalk.py`.**

1. Add `universe_names(universe, universe_source, client=None)`. It returns a dict of company key to
   `{"value": <name>, "source": <where it was read>}`, or `None`.
   - `universe` is `None`: return `None` (the question is not asked).
   - `universe_source` starts with `s3://`: list every object under `universe/v1/` in `POOL_BUCKET` whose key matches
     `universe/v1/<YYYY-MM-DD>.json`, read each one, oldest first, and take every entry of `names` whose `source` is
     `"holding"`, whose `security_key` is set and whose `name` is a non-empty string. A newer object's name replaces an
     older one's. `value` is the name with outer whitespace removed and nothing else changed; `source` is
     `s3://opal-data-harvest/<that object's key>`. The object already in hand as `universe` need not be fetched again.
   - any other `universe_source` (a pinned local file, as the tests use): take the same entries from the one document
     `universe` and read nothing from the store; `source` is `universe_source`.
   - a failure to list or read the store RAISES. It is never answered with an empty dict.
   - keep the result in a module-level dict keyed by `universe_source`, so several builds in one run read once.
2. `build_crosswalk(...)` gains one keyword argument, `legal_names=None`.
   - `legal_names is None`: nothing changes. No record gains a field and no count is added; the document is the one
     built today, byte for byte.
   - `legal_names` is a dict (it may be empty): after the records are final (after the union with `served`, after the
     ENRICH rows, after the retirements), every record gains ONE field, `legal_name`, an object with exactly three keys:
     - the record's own `identity.name` is a non-empty string:
       `{"value": <that name, outer whitespace removed>, "status": "MEASURED", "evidence": "the record's own identity.name (the Bloomberg NAME of its registration pull)"}`;
     - otherwise `legal_names` holds the record's `security_key`:
       `{"value": <its value>, "status": "MEASURED", "evidence": "<its source> :: names[] entry with source 'holding', its name"}`;
     - otherwise: `{"value": null, "status": "ABSENT", "evidence": "no stored source carries a legal name for this record; its research folder name, where it has one, is source_row.folder"}`.
   - a record carried from `served` that already holds `legal_name` keeps it as it is; one that does not gains it by the
     same rule.
   - `denominators["with_legal_name"]` is the count of records whose `legal_name.value` is not null.
   - No other field of any record changes: not `provenance`, not `identity`, not `source_row`.
3. `main()`: read the names once, `legal_names = universe_names(universe, universe_source)`, and pass
   `legal_names=legal_names` to both `build_crosswalk` calls (the `--disclosure` one and the one `--dry-run` and
   `--write-pool` share).
4. Add one paragraph to the `build_crosswalk` docstring stating the argument, the order of the three sources and that
   `None` leaves the document as it was.

**File 2: `lib/research/identity/crosswalk.schema.json`.** Add two OPTIONAL properties and make nothing required:
- on a record, `legal_name`: an object, `additionalProperties: false`, required `value`, `status`, `evidence`;
  `value` is a string or null, `status` is one of `MEASURED`, `ABSENT`, `evidence` is a string of 1 or more characters;
- on `denominators`, `with_legal_name`: an integer, minimum 0.
Give each a `description` naming this cell (AMGT-bb-7). An object built before this cell must still pass.

**File 3: `lib/research/identity/add_security.py`.** In `_build_document`, pass
`legal_names=crosswalk.universe_names(universe, universe_source)` to `build_crosswalk`. Change nothing else there.

**File 4: `lib/research/api/name_search.py`.** `_stored_names(record)` gains a third name after the two it reads today:
the record's `legal_name.value`, when `legal_name` is an object and the value is a non-empty string, added only when it
is not already in the list (compare case-insensitively). Nothing else in the matching changes. The candidate's `name`
stays the first stored name, so a company with a folder name still shows under it, and a company with only a legal
name now shows that. Update the module docstring's "Name:" paragraph to say so.

**Tests.**
- New file `lib/research/identity/tests/test_crosswalk_legal_name.py`, on fixtures only (no store, no network), at least:
  a record with `identity.name` takes it; a record with none takes the map's name and names the map's source in
  `evidence`; a record with neither reads `value` null and `status` ABSENT; `identity.name` wins over the map;
  `legal_names=None` builds a document equal to the one built without the argument; a built document with legal names
  passes `_validate_document_against_schema`; `universe_names` on a pinned local document takes only entries whose
  `source` is "holding" and reads nothing from the store; `universe_names(None, None)` is `None`.
- In `lib/research/api/tests/test_name_search.py` add `test_a_legal_name_lists_its_company`: a record whose only name is
  `legal_name.value` "Apple Inc" lists under "apple" and "Apple" with the name "Apple Inc"; a record with a folder name
  and a legal name lists under either and shows the folder name; a record whose `legal_name.value` is null lists by its
  ticker's first word only. Keep the eight tests there passing.
- Every test file already under `lib/research/identity/tests/` must keep passing unchanged. If one fails because of your
  change, your change is wrong: the default document must not move.

**Rules.**
1. You run NO `--write-pool`, on `crosswalk` or on `add_security`, and you make no store write, put, copy or delete of
   any kind. `--dry-run` and `--disclosure` are allowed. No deploy. No Bloomberg, vendor, SEC or model call.
2. The names come from this project's own stored objects only. You do NOT read, import or copy anything under
   `lib/research/harvest/`, `lib/opal_data_harvest/` or `org/missions/D5/AMGT/AMGT_HARVST/`, and you type no company
   name into code.
3. A name is stored as it was read. Nothing is cleaned, cut, re-cased or guessed; a folder name is never written into
   `legal_name`.
4. The search still never guesses: an exact stored form answers `exact` as today, and a typed company name is never
   answered as `exact`.
5. Any sentence the search serves stays in plain words. Do not use: identity, unresolved, security key, crosswalk,
   dossier, landed, model block, estate, stage, input ledger, bronze.
6. You do NOT edit `lib/research/identity/build_universe.py`, `lib/research/identity/registrations.json`,
   `lib/research/api/scoped_amgt.py` or anything under `infra/`.
7. ASCII only in every file you write.

Report: how many of the records of an in-memory build carry a legal name and from which source (the check prints it),
the keys that carry none, and what "apple", "microsoft" and "airbnb" answer on that build.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W293-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. You run no command with --write-pool and make no store write: the mint is the issuer's act under its own signed pair.
4. Every existing field of every existing pool record is unchanged; the legal name is an ADDED field.
5. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
6. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
7. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/crosswalk.schema.json
lib/research/identity/add_security.py
lib/research/api/name_search.py
lib/research/identity/tests/test_crosswalk_legal_name.py
lib/research/api/tests/test_name_search.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~293/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb7.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>an in-memory build carries legal_name (value, status, evidence) on every record, each value equal to the check's own reading of the stores with its source stated, 200 or more named (211 of 243 on 2026-10-07) and the rest ABSENT, the count stated and the schema check passed, the new test file passing; C1-C4 PASS; R78 BB7 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb7.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>on that in-memory build "apple" lists AAPL_US_Equity as "Apple Inc", "microsoft" lists MSFT_US_Equity as "Microsoft Corp" and "airbnb" lists ABNB_US_Equity, none as exact; every stored name typed whole lists its own record; test_a_legal_name_lists_its_company exists and its file passes; C1-C3 PASS; R78 BB7 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb7.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>(BOUND) the in-memory build holds exactly the served object's keys and every field of every record other than legal_name equals the served record's; no top-level field moves outside the listed ones; a build not handed names carries none; every stored key still answers exact; the two packages' tests pass; C1-C5 PASS; R78 BB7 AC3 SERVED: YES; and exit=0. The fields AC3 lets move, and why (the check's MOVING list): research_universe.read_at (the build's clock); research_universe.folders, denominators.research_folders_live and coverage_vintage.snapshot_stale_against_live (counts of the live research directory at the moment of the build, not of the builder); denominators.with_legal_name (the one added count)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~293 <0.9.0_WK_AMGT_RESAPP~293@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~293/AMGT_RESAPP.TO-AMGT-bb-7.the-pool-carries-each-legal-name.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO rulings file @f97be3fd6f (bb-7: the pool carries the name, not a copied file), row Z-W275-S1. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_E_NOTES.md` (cell E1), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~293</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
