# TO ADVI_COTBKF.TO-CB-ci-5.match-name-review-list -- round 87 CB-ci-5: the exact-name 1:1 REVIEW LIST, candidate links for a person to confirm, with corroboration flags and no PII value, never an automatic link

<to_id>ADVI_COTBKF.TO-CB-ci-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~176</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-5` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "The name is also a very obvious match mechanism if nobody tried that already to push stuff over the line." Nobody had. The CRO measured, between the 1,062 Commonwealth accounts the crosswalk could not match and the 387 unmatched active Black Diamond accounts: 43 exact-name hits, 30 of them unique 1:1, 29 of those corroborated by a second field (date window 29, same registration class 18, a holdings candidate 5). The CTO's ruling (amendment 3): this is the answer to "push stuff over the line" AS A REVIEW LIST for a person to confirm. It is NEVER an automatic link (FWD-9: a link is never guessed), it carries no PII value, and it shows link ids and corroboration flags only. You build that list and report it. You write NOTHING to S3, you edit NO existing module, and you never read the CRM zip.

**Read first (under the repository root):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.copy.md` (sections 3, 4, 5).
2. `data/assets/scripts/silver/commonwealth_crosswalk.py`: docstring, `normalize_account`, `current_locations`, `load_inputs`. Reuse by `import`; do not copy; do not edit.
3. Black Diamond accounts table (`current_locations()['accounts_key']`; columns the CRO used: `account_id`, `account_name`, `account_display_name`, `relationship_id`, `relationship_name`, `account_open_date`, `first_transaction_date`, `account_type`, `account_registration_type`; project what exists, state which were present) and the Commonwealth silver tables under `commonwealth/cottonwood/silver/` at `date=2026-06-23` (addresses from `lib/opal_naming.py` as the crosswalk module builds them, never typed by hand): `document_index` (the account's document names) and `transactions` (last activity date).
4. The served crosswalk `crosswalk.csv` (each Commonwealth account, MATCHED or NOT_MATCHED) and the committed reverse match `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; `account_key,predecessor_key,match_basis,reason`): its `none` rows whose reason is not `NEW_CLIENT_AFTER_MIGRATION` are the 219 reachable unmatched active accounts (387 `none` less 168 new clients).

**Names are PII. The rule for this whole cell:** a name is read into memory, normalised, hashed with a RANDOM PER-RUN SALT (e.g. `hashlib.blake2b(token, key=salt)`; the salt exists only in memory and is never written) and compared as hashes. NO name, name token or hash of one is printed, logged, written to any file, committed, put in a report or a message. Any value-bearing scratch file is deleted before you finish. The only things that leave the process are account ids (the one outside file), `link_id`s, counts and flags.

**Your items.**

1. **The module** `data/assets/scripts/silver/commonwealth_match_names.py`; pure functions on frames; `main()` does the reads and takes `--out DIR` (outside the repository) and nothing else it must be told.
2. **Exact name.** A Commonwealth account's document names, and a Black Diamond account's `account_name` and `account_display_name`, are normalised the same way (lower case, alphanumeric tokens, token-SORTED so that word order does not matter, a stated stop list for words like `trust`, `ira`, `llc`, `the`, `and`, `of`) and hashed. Two names are an EXACT match when the sorted token sets are equal. Candidates: unmatched Commonwealth accounts (1,062) against unmatched ACTIVE Black Diamond accounts (the 387 `none` rows, new clients included: say how many new-client rows hit and exclude them from the 219 count). A pair is 1:1 when the Commonwealth account hits exactly one active account AND that account is hit by exactly one Commonwealth account. Only 1:1 pairs go on the list.
3. **Corroboration flags** (booleans, never values): `date_window_ok` (the Commonwealth account's last transaction date and the Black Diamond account's first holdings or open date fall within 120 days of each other; state the date column you used), `same_registration_class` (the Black Diamond `account_registration_type` equals the Commonwealth side's class where the Commonwealth side carries one; where it carries none, the flag is `null`, not false), `holdings_candidate` (the Commonwealth account's holdings as it left share at least one non-cash security with the Black Diamond account's first holdings; reuse `holdings_as_left` and `current_first_holdings` from the crosswalk module), `already_claimed` (the Black Diamond account is MATCHED to some other Commonwealth account in the served crosswalk, which would make the pair a conflict).
4. **The list.** One row per 1:1 pair: `link_id` (the first 12 hex of `sha256("commonwealth_account|bd_account_id")` of the two raw ids, so a person can quote a row without an account number), the four flags, `corroborations` (the count of true flags among the first three), `in_219` (the Black Diamond account is one of the 219 reachable), `tier` fixed at `REVIEW`. NO name, name token, hash of a name, account number or value in the list. Write it in two places: `REVIEW_LIST.csv` in the repository at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/` (columns exactly `link_id,date_window_ok,same_registration_class,holdings_candidate,already_claimed,corroborations,in_219,tier`), and `REVIEW_KEY.csv` in `C:/dev/_cotbkf_match_20261015/` (outside the repository: columns `link_id,commonwealth_account,bd_account_id`), so that a person with access can resolve a link id to its accounts.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/NAME_REVIEW_RECORD.json` with exactly these top-level keys: `columns_present`, `hits` (`{"exact_name_pairs", "one_to_one", "one_to_many_commonwealth", "many_to_one_bd", "new_client_hits"}`), `list` (`{"rows", "in_219", "with_zero_corroborations", "with_one", "with_two", "with_three", "already_claimed"}`), `date_basis` (the columns used and the 120-day window), `denominators` (`{"unmatched_commonwealth", "unmatched_active", "new_clients", "reachable"}`), `files` (a list of 2: `{"name", "path", "rows", "sha256"}`), `scratch_deleted` (true only when you deleted every value-bearing scratch file), `sources_read`, `not_established`; and a short `.md`. Neither carries an account number or any name.
6. **Tests** `data/assets/scripts/silver/tests/test_commonwealth_match_names.py` on stub frames, made-up ids (`A1`, `B1`) and made-up tokens, one test each for: token order does not matter (`ann lee` equals `lee ann`); a Commonwealth account hitting two active accounts is not on the list; two Commonwealth accounts hitting one active account are not on the list; a missing registration class gives `null`, not false; the list file has exactly the eight columns and no id column other than `link_id`.

### ACCEPTANCE

<criterion id="CB87ci5-AC1" cell_refs="CB-ci-5"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/NAME_REVIEW_RECORD.json',encoding='utf-8'));h=d['hits'];l=d['list'];print('NAME-REVIEW exact=%d one_to_one=%d rows=%d in_219=%d two_plus=%d zero=%d reachable=%d'%(h['exact_name_pairs'],h['one_to_one'],l['rows'],l['in_219'],l['with_two']+l['with_three'],l['with_zero_corroborations'],d['denominators']['reachable']))"</invocation><expect>reachable=219</expect></criterion>
`CB87ci5-AC1` -- the hits, the list, the corroboration spread and the 219 denominator are printed from the record.

<criterion id="CB87ci5-AC2" cell_refs="CB-ci-5"><invocation>python -c "import json,hashlib,csv;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/NAME_REVIEW_RECORD.json',encoding='utf-8'));ok=[];[ok.append(hashlib.sha256(open(f['path'],'rb').read()).hexdigest()==f['sha256'] and sum(1 for _ in open(f['path'],encoding='utf-8'))-1==f['rows']) for f in d['files']];rows=list(csv.reader(open([f['path'] for f in d['files'] if f['name']=='REVIEW_LIST.csv'][0],encoding='utf-8')));print('REVIEW-FILES files=%d match=%s list_columns=%s key_outside_repo=%s scratch_deleted=%s'%(len(d['files']),all(ok),','.join(rows[0])=='link_id,date_window_ok,same_registration_class,holdings_candidate,already_claimed,corroborations,in_219,tier',all(not f['path'].startswith('org/') for f in d['files'] if f['name']=='REVIEW_KEY.csv'),d['scratch_deleted']))"</invocation><expect>REVIEW-FILES files=2 match=True list_columns=True key_outside_repo=True scratch_deleted=True</expect></criterion>
`CB87ci5-AC2` -- both files exist with the recorded checksums and row counts, the committed list has exactly the eight named columns (no name, no account number), the key file sits outside the repository, and the scratch is recorded deleted.

<criterion id="CB87ci5-AC3" cell_refs="CB-ci-5"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_match_names.py -q</invocation><expect>5 passed</expect></criterion>
`CB87ci5-AC3` -- the five rules hold on stubs.

<expected_criteria>CB87ci5-AC1,CB87ci5-AC2,CB87ci5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_match_20261015/` (only the file `REVIEW_KEY.csv`). You change no other file; you do not edit `commonwealth_crosswalk.py`, `REVERSE_MATCH_V3.csv`, any existing script or test, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the Commonwealth silver tables named above and the Black Diamond accounts key and holdings prefix `current_locations()` names. State each listing's denominator. No write, delete or serve; no other bucket or prefix; NOT the restricted CRM prefix or the CRM zip under any name (open call d3cc is Andrew's); not the imaging `CLNT` PDFs. Do not run `aws sts get-caller-identity`.
- **PII.** The rule in THE CELL binds every item. Account ids appear only in `REVIEW_KEY.csv`. A criterion output, a log line or a message that would show a name is a stop.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`. On this box it may fail closed because the pinned account set is on another machine: then report the exact error and do NOT look for the set; the issuer runs a count-only substitute at the drain.
- **NEVER** `--apply`, an S3 write or delete, `--refresh`, or any edit of the served crosswalk. The list is never fed to the crosswalk by this cell. No vendor call. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W176-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_match_names.py
data/assets/scripts/silver/tests/test_commonwealth_match_names.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-5`.
<owned_cells>CB-ci-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci5-AC1, CB87ci5-AC2, CB87ci5-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/ADVI_COTBKF.TO-CB-ci-5.match-name-review-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci5-AC1,CB87ci5-AC2,CB87ci5-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the outside CSV in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the list line: exact-name pairs, 1:1 pairs, rows on the list, how many are among the 219, the corroboration spread (zero, one, two or more). Then: the difference from the research (43 hits, 30 unique 1:1, 29 corroborated); the date columns used; the columns present; every S3 read with its denominator; the three criterion lines; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Say that no name left memory and that scratch was deleted.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads of silver and Black Diamond tables and files in a scratch folder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- FWD-9 says a link is never guessed: every row is tier REVIEW, a candidate for a person, and nothing consumes the list; the 1:1 test is two-sided; BLIND: exact-name recall is low (only 93 of 462 already-matched pairs agree on exact name, the two systems format names differently), so absence from the list says nothing; and two real clients who share a name (a 1:1 hit that is wrong; the control on matched pairs is the only evidence, which this cell does not run: the CRO's 15 wrong class picks warn that class alone is weak).
lane: the <paths> block IS the grant (worker RULING 1). The module is new; no existing module is edited; nothing is written to S3. Names are PII; the committed list carries link ids and booleans only.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` ruling amendment 3 item 3 (msg 6124); `4.0.0_SA_CRO~DELL2` research note sections 4 and 5 (copy in `deliverables/2.0.0_SA_COO~C1/`).
