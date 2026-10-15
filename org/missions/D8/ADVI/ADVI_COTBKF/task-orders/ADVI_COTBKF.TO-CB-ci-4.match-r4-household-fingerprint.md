# TO ADVI_COTBKF.TO-CB-ci-4.match-r4-household-fingerprint -- round 87 CB-ci-4: rule R4, a Commonwealth account's name to ONE Black Diamond household, then the holdings fingerprint inside that household within the date window; deterministic only on a fingerprint pass; client-line propagation through the same step

<to_id>ADVI_COTBKF.TO-CB-ci-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~175</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-4` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "we need to do better at matching ... The name is also a very obvious match mechanism". The CRO measured that a Commonwealth account's document name reaches ONE Black Diamond household precisely (positive control on the 471 already-matched accounts: 138 right, 0 wrong, 7 multi-household, 317 no hit), but that name plus registration class alone, inside the household, picks the right account 45 times and the WRONG one 15 times, with 78 ambiguous. So inside the household the link needs more. The CTO's rule (ruling amendment 3): a link is DETERMINISTIC only when a narrowed holdings fingerprint passes inside the household and the date window holds; otherwise it is a CANDIDATE for a person; a link is never guessed. You build that as a standalone module and report the yield over the 219 reachable unmatched active accounts. You write NOTHING to S3, you edit NO existing module, and you never read the CRM zip.

**Read first (under the repository root):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.copy.md` (sections 3, 4 and 5).
2. `data/assets/scripts/silver/commonwealth_crosswalk.py`: its docstring (rules R1, R2; "holdings as it left"; "first holdings"; the 0.8 bar and the 0.001 tolerance; the cash exclusion), `normalize_account`, `holdings_as_left`, `current_first_holdings`, `load_inputs`, `current_locations`. Reuse by `import`; do not copy; do not edit.
3. The Black Diamond accounts table (`current_locations()['accounts_key']`; columns the CRO used: `account_id`, `account_name`, `account_display_name`, `relationship_id`, `relationship_name`, `account_open_date`, `first_transaction_date`, `account_type`, `account_registration_type`; project what exists and state which columns were present) and holdings (`current_locations()['holdings_prefix']`).
4. The Commonwealth silver tables under `commonwealth/cottonwood/silver/` at `date=2026-06-23` (list the silver prefixes once; the addresses come from `lib/opal_naming.py` as the crosswalk module uses it, never typed by hand): `document_index` (the CRO's note: `listing_fields` carry `DisplayName` with the account, `ClientName`, `HouseholdName`, `AccountNumber`; 738 of the 1,533 accounts have a document) and `account_links` (`old_account`, `new_account`, `newest_account`, `client_line`).
5. The served crosswalk `crosswalk.csv` (1,533 rows: each Commonwealth account, MATCHED or NOT_MATCHED, `current_account`) and the committed reverse match `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; `account_key,predecessor_key,match_basis,reason`): its `none` rows whose reason is not `NEW_CLIENT_AFTER_MIGRATION` are the reachable unmatched active accounts, 219 of 387.

**Names are PII. The rule for this whole cell:** a name is read into memory, normalised, hashed with a RANDOM PER-RUN SALT (e.g. `hashlib.blake2b(token, key=salt)`; the salt exists only in memory and is never written) and compared as hashes. NO name, name token or hash of one is printed, logged, written to any file, committed, put in a report or a message. Any value-bearing scratch file is deleted before you finish. The only things that leave the process are account ids (outside file), counts and flags.

**Your items.**

1. **The module** `data/assets/scripts/silver/commonwealth_match_r4.py`; pure functions on frames; `main()` does the reads and takes `--out DIR` (outside the repository) and nothing else it must be told. Steps, in this order, each a function with a stated, tested rule:
   a. **Name to household.** For each Commonwealth account, its document names (the `DisplayName`, `ClientName` and `HouseholdName` that list it) normalised (lower case, alphanumeric tokens, a stated stop list for words like `trust`, `ira`, `llc`, `the`, `and`, `of`), tokens hashed; the Black Diamond household name (`relationship_name`, else the account names of its accounts) likewise. A household is a hit when the token overlap (shared tokens / tokens of the shorter set) is at least 0.6. The account reaches a household only when EXACTLY ONE household hits; zero or two or more is `NO_HOUSEHOLD` or `MULTI_HOUSEHOLD` (counted, never resolved).
   b. **Client-line propagation.** A Commonwealth account with no household by name, but whose `client_line` (from `account_links`) is shared with Commonwealth siblings MATCHED in the served crosswalk to Black Diamond accounts that all sit in ONE household, takes that household as `via client_line`. Siblings split across households give no household. Record how each link got its household: `via name` or `via client_line`.
   c. **Inside the household: the fingerprint.** Candidates are the household's Black Diamond accounts that no OTHER Commonwealth account is matched to in the served crosswalk. For each candidate apply the crosswalk module's R2 test (holdings as the Commonwealth account left, against the candidate's first holdings, security by security, quantity equal within 0.001, cash excluded) and keep its score. A candidate PASSES when its score is at least 0.8 (R2's bar; do not lower it).
   d. **The date window.** Derive it from data, not from a guess: for the already-matched pairs in the served crosswalk, measure the gap in days between the Commonwealth account's last transaction date and the Black Diamond account's first holdings date (or `first_transaction_date` where that is the column present); state the distribution (counts per band) and set the window as the narrowest symmetric band around the median that holds at least 95% of those pairs. A candidate is `window_ok` when its gap falls inside the band.
   e. **The tier.** DETERMINISTIC when the household is unique, EXACTLY ONE candidate passes the fingerprint, and that candidate is `window_ok`. CANDIDATE when the household is unique and at least one candidate has a score of at least 0.5, or is `window_ok` with the same registration type, but the DETERMINISTIC test fails (this is for a person to confirm; it is never linked). Otherwise `NONE`. Name plus registration type alone is NEVER DETERMINISTIC.
2. **The positive control, run first.** Run steps a to e over the 471 Commonwealth accounts the served crosswalk MATCHES, with their own crosswalk link hidden from step c's "other claims" test. Report: reached a unique household; of those, correct household; DETERMINISTIC links and, of them, the number equal to the crosswalk's `current_account` (right) and not equal (wrong); CANDIDATE counts; NONE. **If any DETERMINISTIC link in the control is wrong, you promote NO link to DETERMINISTIC in the real run (they all stay CANDIDATE) and say so; this is the guard.** The research expected the household stage at 138 right and 0 wrong.
3. **The real run.** Over the Commonwealth accounts the crosswalk does NOT match (1,062): the counts by `NO_HOUSEHOLD`, `MULTI_HOUSEHOLD`, `via name`, `via client_line`, and by tier. Then the yield: of the DETERMINISTIC and of the CANDIDATE links, how many point to a Black Diamond account that is ACTIVE (a `REVERSE_MATCH_V3.csv` `account_key`), and how many to one of the 219 reachable unmatched active accounts. The research estimated 59 unmatched reach a household and 16 reach one account of the same class, and client-line propagation reaches 89 households of which 39 touch an unmatched active account; report your own figures and the difference from the estimate.
4. **The files.** `R4_LINKS.csv` into `C:/dev/_cotbkf_match_20261015/` (outside the repository; raw account ids; columns exactly `commonwealth_account,bd_account_id,tier,household_via,fingerprint_score,window_ok,candidates_in_household`; no name column). In the repository write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~175/R4_RECORD.json` with exactly these top-level keys: `rule`, `columns_present` (the Black Diamond and Commonwealth columns actually used), `window` (`{"band_days", "basis_pairs", "share_inside", "distribution"}`), `control` (`{"matched", "reached_household", "household_correct", "deterministic", "det_right", "det_wrong", "candidate", "none", "guard_applied"}`), `real` (`{"unmatched", "no_household", "multi_household", "via_name", "via_client_line", "deterministic", "candidate", "none"}`), `yield` (`{"deterministic_active", "deterministic_among_219", "candidate_active", "candidate_among_219"}`), `denominators` (`{"unmatched_active", "new_clients", "reachable"}`), `file` (`{"path", "rows", "sha256"}`), `scratch_deleted` (true only when you deleted every value-bearing scratch file), `sources_read`, `not_established`; and a short `.md`. Neither carries an account number or any name.
5. **Tests** `data/assets/scripts/silver/tests/test_commonwealth_match_r4.py` on stub frames and made-up ids (`A1`, `H1`) and made-up tokens, one test each for: a name reaching two households is `MULTI_HOUSEHOLD` and gets no link; a unique household with exactly one fingerprint-passing candidate inside the window is DETERMINISTIC; two passing candidates is CANDIDATE; name plus registration type with a failing fingerprint is never DETERMINISTIC; client-line siblings split across two households give no household; a wrong DETERMINISTIC in the control demotes every link to CANDIDATE.

### ACCEPTANCE

<criterion id="CB87ci4-AC1" cell_refs="CB-ci-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~175/R4_RECORD.json',encoding='utf-8'));c=d['control'];r=d['real'];y=d['yield'];print('R4 control_det=%d right=%d wrong=%d guard=%s real_det=%d cand=%d via_name=%d via_line=%d det_219=%d cand_219=%d reachable=%d window_days=%s'%(c['deterministic'],c['det_right'],c['det_wrong'],c['guard_applied'],r['deterministic'],r['candidate'],r['via_name'],r['via_client_line'],y['deterministic_among_219'],y['candidate_among_219'],d['denominators']['reachable'],d['window']['band_days']))"</invocation><expect>reachable=219</expect></criterion>
`CB87ci4-AC1` -- the control, the guard, the real run, the yield over the 219 and the derived window are printed from the record.

<criterion id="CB87ci4-AC2" cell_refs="CB-ci-4"><invocation>python -c "import json,hashlib,csv;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~175/R4_RECORD.json',encoding='utf-8'));f=d['file'];b=open(f['path'],'rb').read();rows=list(csv.reader(open(f['path'],encoding='utf-8')));print('R4-FILE sha256_match=%s rows_match=%s columns=%s outside_repo=%s scratch_deleted=%s'%(hashlib.sha256(b).hexdigest()==f['sha256'],len(rows)-1==f['rows'],','.join(rows[0])=='commonwealth_account,bd_account_id,tier,household_via,fingerprint_score,window_ok,candidates_in_household',not f['path'].startswith('org/'),d['scratch_deleted']))"</invocation><expect>R4-FILE sha256_match=True rows_match=True columns=True outside_repo=True scratch_deleted=True</expect></criterion>
`CB87ci4-AC2` -- the outside links file has the recorded checksum, row count and exactly the named columns (none holds a name), and the value-bearing scratch is recorded deleted.

<criterion id="CB87ci4-AC3" cell_refs="CB-ci-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_match_r4.py -q</invocation><expect>6 passed</expect></criterion>
`CB87ci4-AC3` -- the six rules hold on stubs.

<expected_criteria>CB87ci4-AC1,CB87ci4-AC2,CB87ci4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_match_20261015/` (only the file `R4_LINKS.csv`). You change no other file; you do not edit `commonwealth_crosswalk.py`, `REVERSE_MATCH_V3.csv`, any existing script or test, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the Commonwealth silver tables named above and the Black Diamond accounts key and holdings prefix `current_locations()` names. State each listing's denominator. No write, delete or serve; no other bucket or prefix; NOT the restricted CRM prefix or the CRM zip under any name (open call d3cc is Andrew's); not the imaging `CLNT` PDFs. Do not run `aws sts get-caller-identity`.
- **PII.** The rule in THE CELL binds every item: no name, name token or name hash leaves memory; the salt is never stored; value-bearing scratch is deleted; account ids appear only in the one outside file. A criterion output, a log line or a message that would show a name is a stop.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`. On this box it may fail closed because the pinned account set is on another machine: then report the exact error and do NOT look for the set; the issuer runs a count-only substitute at the drain.
- **NEVER** `--apply`, an S3 write or delete, `--refresh`, or any edit of the served crosswalk. No vendor call. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W175-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_match_r4.py
data/assets/scripts/silver/tests/test_commonwealth_match_r4.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-4`.
<owned_cells>CB-ci-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci4-AC1, CB87ci4-AC2, CB87ci4-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~175/ADVI_COTBKF.TO-CB-ci-4.match-r4-household-fingerprint.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci4-AC1,CB87ci4-AC2,CB87ci4-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the outside CSV in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the control line (reached a household, right, wrong, whether the guard applied) and the yield line (deterministic and candidate over the 219). Then: the derived date window and its basis; the difference from the research estimates; the columns actually present on each side; every S3 read with its denominator; the three criterion lines; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Say that no name left memory and that scratch was deleted.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads of silver and Black Diamond tables and a file in a scratch folder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- FWD-9 says a link is never guessed: a name only picks a household; the fingerprint inside it (R2's bar) and the date window decide, and the control on the 471 matched demotes everything if one DETERMINISTIC is wrong; BLIND: a household that holds two real accounts of one client with the same holdings (two passers give CANDIDATE, never a link), and names that differ between systems (the control showed only 93 of 462 matched pairs agree on exact account name, so recall is low and a miss is silent: `NO_HOUSEHOLD` is counted, not explained).
lane: the <paths> block IS the grant (worker RULING 1). The module is new; no existing module is edited; nothing is written to S3. Names are PII (C-SENSITIVE is about the CRM zip's four fields; this order applies the same care to names).
</preflight>

Source: `1.0.0_SA_CTO~DELL1` ruling amendment 3 item 2 (msg 6124); `4.0.0_SA_CRO~DELL2` research note sections 4 and 5 (copy in `deliverables/2.0.0_SA_COO~C1/`).
