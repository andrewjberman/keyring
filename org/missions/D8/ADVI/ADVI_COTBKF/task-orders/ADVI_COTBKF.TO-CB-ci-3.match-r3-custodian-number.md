# TO ADVI_COTBKF.TO-CB-ci-3.match-r3-custodian-number -- round 87 CB-ci-3: rule R3, a Commonwealth account number equal to Black Diamond's custodian account number, as a standalone module with its yield over the reachable unmatched active accounts

<to_id>ADVI_COTBKF.TO-CB-ci-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~174</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-3` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "we need to do better at matching." Today's crosswalk (`data/assets/scripts/silver/commonwealth_crosswalk.py`) has two rules: R1 compares a Commonwealth account number with Black Diamond's internal `account_id` (it matched 0), and R2 matches by holdings. The CRO measured that Black Diamond's holdings table carries a second number, the CUSTODIAN number (column `Account Number` in `fact_holdings`), and that 89 Commonwealth account numbers equal one of them (research note, section 4, "R1 against the custodian number": 87 new forward links, 2 already matched and agreeing with R2, so a control of 2 of 2). You build that rule as a module, measure it again yourself, and report how many of the unmatched ACTIVE accounts it reaches. You write NOTHING to S3 and you edit NO existing module: wiring a rule into the served crosswalk is a later act under a never-widen pair.

**Read first (under the repository root):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.copy.md` (the CRO's research; sections 3 and 4).
2. `data/assets/scripts/silver/commonwealth_crosswalk.py`: read its docstring, `normalize_account`, `current_locations`, `_fetch_inputs`, `load_inputs` and the R1/R2 code, to reuse the loaders by `import` (do not copy and do not edit the file). The Black Diamond side: `current_locations()` names the bucket, the accounts key and the holdings prefix; the holdings parquet parts carry the column `Account Number` beside `account_id`, which `HOLD_COLS` there does not project: you project it yourself.
3. The committed reverse match `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; columns `account_key,predecessor_key,match_basis,reason`; raw ids; 860 rows). Its `none` rows with a reason other than `NEW_CLIENT_AFTER_MIGRATION` are the reachable unmatched active accounts: 387 `none` less 168 new clients = 219.
4. The crosswalk as served: `s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.csv` (1,533 rows: each Commonwealth account, its status MATCHED or NOT_MATCHED, its `current_account`). Read it with the loader the crosswalk module's `opal_naming.address` form gives (never type the key by hand).

**Your items.**

1. **The module** `data/assets/scripts/silver/commonwealth_match_r3.py`. Rule R3: a Commonwealth account number, normalized exactly as `commonwealth_crosswalk.normalize_account` does (case, non-alphanumerics, leading zeros), equals the normalized custodian `Account Number` of Black Diamond holdings rows. The link is to the `account_id` of those rows. A custodian number that maps to MORE THAN ONE `account_id` is never linked (AMBIGUOUS, counted). A Commonwealth number that equals the custodian numbers of two different `account_id`s likewise. Output rows: `commonwealth_account, bd_account_id, rule "R3-custodian-number", status DETERMINISTIC | AMBIGUOUS`. Pure functions take frames and return frames (no S3 inside them); `main()` does the reads and takes `--out DIR` (a local directory outside the repository) and nothing else it must be told.
2. **The positive control.** Of the links R3 finds, count those whose Commonwealth account the served crosswalk already MATCHES, and of those, the number whose crosswalk `current_account` equals the R3 `bd_account_id` (agree) and the number that differ (disagree). A disagree is a finding, never hidden. Expected from the research: 2 of 2 agree.
3. **The yield.** Print: R3 links total (DETERMINISTIC), AMBIGUOUS, links to Commonwealth accounts the crosswalk had NOT matched ("new"), of the new links the number whose `bd_account_id` is an ACTIVE account (a `REVERSE_MATCH_V3.csv` `account_key`), and of those the number that are among the 219 reachable unmatched active accounts. The research expected 87 new, 0 active. Report your own figures; a difference from the research is reported with the reason if you can name it.
4. **The files.** `R3_LINKS.csv` into `C:/dev/_cotbkf_match_20261015/` (create it; outside the repository; it carries raw account numbers: columns `commonwealth_account,bd_account_id,rule,status,crosswalk_state`). In the repository only counts: write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~174/R3_RECORD.json` with exactly these top-level keys: `rule`, `commonwealth_accounts` (distinct, in the crosswalk), `custodian_numbers` (distinct non-blank in Black Diamond holdings), `links_deterministic`, `links_ambiguous`, `control` (`{"already_matched", "agree", "disagree"}`), `new_links`, `new_links_active`, `new_links_among_219`, `denominators` (`{"unmatched_active", "new_clients", "reachable"}`), `file` (`{"path", "rows", "sha256"}`), `sources_read` (each S3 prefix or key with the objects listed and read), `not_established`; and a short `.md` beside it. Neither carries an account number or a name.
5. **Tests** `data/assets/scripts/silver/tests/test_commonwealth_match_r3.py` on stub frames (made-up ids like `A1`, never real): one test each for: an equal number links; a custodian number held by two `account_id`s is AMBIGUOUS and not linked; normalization (case, leading zeros) makes `0012ab` and `12AB` equal.

### ACCEPTANCE

<criterion id="CB87ci3-AC1" cell_refs="CB-ci-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~174/R3_RECORD.json',encoding='utf-8'));c=d['control'];print('R3 links=%d ambiguous=%d new=%d new_active=%d among_219=%d control_agree=%d/%d disagree=%d reachable=%d'%(d['links_deterministic'],d['links_ambiguous'],d['new_links'],d['new_links_active'],d['new_links_among_219'],c['agree'],c['already_matched'],c['disagree'],d['denominators']['reachable']))"</invocation><expect>reachable=219</expect></criterion>
`CB87ci3-AC1` -- the R3 yield, its control and its denominator are printed from the record, and the reachable denominator reads 219.

<criterion id="CB87ci3-AC2" cell_refs="CB-ci-3"><invocation>python -c "import json,hashlib;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~174/R3_RECORD.json',encoding='utf-8'));f=d['file'];b=open(f['path'],'rb').read();n=sum(1 for _ in open(f['path'],encoding='utf-8'))-1;print('R3-FILE sha256_match=%s rows_match=%s outside_repo=%s'%(hashlib.sha256(b).hexdigest()==f['sha256'],n==f['rows'],not f['path'].startswith('org/')))"</invocation><expect>R3-FILE sha256_match=True rows_match=True outside_repo=True</expect></criterion>
`CB87ci3-AC2` -- the outside links file exists with the recorded checksum and row count.

<criterion id="CB87ci3-AC3" cell_refs="CB-ci-3"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_match_r3.py -q</invocation><expect>3 passed</expect></criterion>
`CB87ci3-AC3` -- the equality, ambiguity and normalization rules hold on stubs.

<expected_criteria>CB87ci3-AC1,CB87ci3-AC2,CB87ci3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_match_20261015/` (only the file `R3_LINKS.csv`). You change no other file; you do not edit `commonwealth_crosswalk.py`, `REVERSE_MATCH_V3.csv`, any existing script or test, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the Commonwealth silver crosswalk and transactions/positions as the crosswalk module reads them, and the Black Diamond accounts key and holdings prefix `current_locations()` names. State each listing's denominator. No write, delete or serve; no other bucket or prefix; NOT the restricted CRM prefix or the CRM zip under any name (open call d3cc is Andrew's). Do not run `aws sts get-caller-identity`.
- **No name of a person or an account is read into any output.** This cell needs numbers only. Account numbers appear only in the one outside file. Counts, dates, rule names and statuses only in the record, the report and any message.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`. On this box it may fail closed because the pinned account set is on another machine: then report the exact error and do NOT look for the set; the issuer runs a count-only substitute at the drain.
- **NEVER** `--apply`, an S3 write or delete, `--refresh`, or any edit of the served crosswalk. No vendor call. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W174-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_match_r3.py
data/assets/scripts/silver/tests/test_commonwealth_match_r3.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-3`.
<owned_cells>CB-ci-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci3-AC1, CB87ci3-AC2, CB87ci3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~174/ADVI_COTBKF.TO-CB-ci-3.match-r3-custodian-number.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci3-AC1,CB87ci3-AC2,CB87ci3-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the outside CSV in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the yield line: links, ambiguous, new, new among the active accounts, new among the 219, the control (agree/disagree of already matched). Then: how your figures differ from the research note's (87 new, 0 active, control 2 of 2) and why; every S3 read with its denominator; the three criterion lines; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables and a file in a scratch folder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- FWD-9 says a link is never guessed: R3 is equality of two numbers, with its own positive control against the served crosswalk (disagree is reported); an ambiguous number is never linked; BLIND: two systems may reuse a number for different accounts (the control against the 471 matched is the only detector), and the 87 links are to CLOSED accounts outside the active set, so this rule's value for the active 219 may be zero; the order reports that, it does not hide it.
lane: the <paths> block IS the grant (worker RULING 1). The module is new; no existing module is edited; nothing is written to S3.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` ruling amendment 3 item 1 (msg 6124); `4.0.0_SA_CRO~DELL2` research note section 4 (copy in `deliverables/2.0.0_SA_COO~C1/`).
