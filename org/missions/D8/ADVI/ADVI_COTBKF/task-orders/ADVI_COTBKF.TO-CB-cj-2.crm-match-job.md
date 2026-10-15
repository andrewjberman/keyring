# TO ADVI_COTBKF.TO-CB-cj-2.crm-match-job -- round 88 CB-cj-2: the ONE job -- assume the grant's role, read the restricted CRM zip in memory, join its identifiers to both sides, write only account-link rows and counts; matched and unmatched over the 219

<to_id>ADVI_COTBKF.TO-CB-cj-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~177</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>88</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cj-2` (`decompositions/ADVI_COTBKF_DECOMP.round88.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** CB-cj-1 (applied and read back)

---

## WORKER FACE

### THE CELL

**UN-PARKED (see AMENDMENT 1 in this file's record face): the grant is live and read back. You act now. The role ARN, the deadline and the key are in `GRANT_RECORD.json` named in Read-first item 2.**

**Why.** Andrew, 2026-10-15: "I agree with (a), let's see what we can do with that for now." Option (a): ONE job, with a short-lived role, reads the restricted CRM zip (`CRM_CottonwoodCapitalAdvisors.zip`, landed by Andrew in the firm bucket under the restricted prefix) and uses its identifiers to link Commonwealth accounts to current Black Diamond accounts. Nothing from the zip may leave the job except account-link rows. A person reads the result and decides what to do with it. The job's limits, each a bound below: IN MEMORY (never to disk); LINK IDS ONLY; NO PERSONAL DATA OUT; LOGGED by its own run record; and the grant is removed at the job's end by another order.

**Read first (under the repository root):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md` (sections "What the job MAY emit", "What the act may NOT do", "Both branches named") and `.../NEVER_WIDEN_R88_CRM_MATCH_GRANT_CTO_HALF.md` (conditions C1 to C3).
2. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json`: `role_arn`, `deadline_utc` (the day's 23:59Z), the key. The role is yours to assume, once, and only for this job.
3. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.copy.md` (section 3: the identity columns on both sides; section 4: the join rates; what the CRO could and could not measure).
4. `data/assets/scripts/silver/commonwealth_crosswalk.py` (docstring, `normalize_account`, `current_locations`, `load_inputs`): reuse by `import`, never copy, never edit. The Commonwealth side: the served crosswalk `crosswalk.csv` and the silver tables; the Black Diamond side: the accounts key and the silver `fact_holdings` table (`opal_naming.address('blackdiamond','cottonwood','silver','fact_holdings')`; columns `AccountID` and `Account Number`, the custodian number); see `commonwealth_match_r3.py` (round 87) for how they were read.
5. The committed reverse match `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; `account_key,predecessor_key,match_basis,reason`): its `none` rows whose reason is not `NEW_CLIENT_AFTER_MIGRATION` are the 219 reachable unmatched active accounts (387 `none` less 168 new clients). The key to read the zip with: `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip` (built by `opal_naming`, never typed by hand elsewhere).

**The rules of the job (every one binds, and a breach is a STOP, not a finding to carry on from):**
- **In memory.** The zip is read with `get_object` into memory (`BytesIO`) and opened with `zipfile`; no member, no byte of the zip and no CRM-derived text is written to disk, to the worktree, to `.scratch/`, to a temp file, to a cache, to a log or to a console. Credentials from `sts.assume_role` live in variables of the process only (no `~/.aws` write, no environment file). If `ContentLength` exceeds 1.5 GB, stop with `TOO_LARGE_FOR_MEMORY` (recorded; no read).
- **No value out.** What is allowed to leave the process is exactly: (a) the link rows `commonwealth_account, bd_account_id, rule, tier` (ids and a rule name and a tier, the shape the crosswalk already carries); (b) COUNTS; (c) the zip's member NAMES and each CSV member's HEADER names (schema, not values; needed to say which columns the job used). NO name, tax id, date of birth, address, licence or passport number, email, phone, policy number, and NO value of any other CRM column, ever; not in a log, a message, an exception text, a criterion output, a commit or a record. Exceptions print the exception class and a short code only; install `sys.excepthook` to do that and never print a frame's locals or a row.
- **Link ids only, graded by FWD-9.** A link is `DETERMINISTIC` only when the CRM carries a STABLE KEY on one record that ties a Commonwealth account number (as it appears in the Commonwealth tables) to a current Black Diamond identifier (`account_id` or the custodian `Account Number`): an old/new account-number pair, or a tax-id pair if and only if Black Diamond's tables carry the same identifier (state which, by column name). Any link that rests on a shared person or household identifier, a name, or anything not a direct pair is `CANDIDATE`. A link that would give one Commonwealth account two Black Diamond accounts, or two Commonwealth accounts one Black Diamond account, is never written as DETERMINISTIC (both are CANDIDATE, counted as ambiguous). `rule` is one name from a short list you define and state (for example `CRM-account-pair`, `CRM-household`).
- **Logged.** The run record is the log: start, end, role ARN, session name, the one key, `ContentLength`, the member names and header names, which columns the job used (names), row counts by tier, the 219 yield. The CloudTrail S3 data event for the GET is NOT yours to read (the withdrawal order reads it); the record says plainly that it did not read it.
- **One run.** One `assume_role` call (session name exactly `cotbkf-crm-match-177`), one `head_object`, at most ONE `get_object` of the key. A failed run is recorded and stops; there is no retry loop.

**Your items.**

1. **The module** `data/assets/scripts/silver/cotbkf_crm_match_job.py`, pure functions plus a `main()` taking `--out DIR` (outside the repository; default `C:/dev/_cotbkf_match_20261015`) and `--role-arn ARN` and `--record PATH`. Pure functions take frames or lists and return rows; no S3 inside them. Constants: the allow-list `ALLOW_COLUMNS = ["commonwealth_account", "bd_account_id", "rule", "tier"]`, the key, the session name. A writer that is given any row with a different column set raises.
2. **Tests** `data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py` on stubs and made-up ids/tokens (`A1`, `B1`, an in-memory stub zip built with `zipfile` and `BytesIO` with fake headers and rows): one test each for: (a) the writer refuses a row set whose columns differ from `ALLOW_COLUMNS`; (b) a record pair on one CRM row gives DETERMINISTIC and a shared household identifier alone gives CANDIDATE; (c) a Commonwealth account that would take two Black Diamond accounts is never DETERMINISTIC; (d) with `builtins.open` patched to raise on any write mode except the links path, the whole match on the stub zip completes (nothing else is written); (e) `NOT_LANDED` (a stub client whose `head_object` raises a 404) writes no links file and a record with `landed` false and zero rows. Commit the module and tests FIRST (before the real run).
3. **The run (once).** Read the grant record; check the clock against `deadline_utc` (if less than 90 minutes remain, STOP: the withdrawal needs the time); assume the role; `head_object`: 404 -> record `landed: false` (NOT_LANDED), write no links file, finish the record; 403 -> record the exact error class and message text of the refusal (an AWS error text names no CRM content) and stop; else read, open, record member and header names, choose the join columns BY NAME (state them), match, write `CRM_LINKS.csv` in the outside folder with exactly the four columns.
4. **The yield over the 219.** For each of the 219 reachable active accounts (the V3 `none` rows without `NEW_CLIENT_AFTER_MIGRATION`): linked DETERMINISTIC, linked CANDIDATE only, unlinked. Report `matched` (DETERMINISTIC or CANDIDATE) and `unmatched` and each tier separately. Also how many Commonwealth accounts (of 1,533) the links touch.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~177/JOB_RECORD.json` with exactly these top-level keys: `role_arn`, `session_name`, `key`, `started`, `ended`, `landed` (true or false), `content_length`, `members` (names only), `header_columns` (member name to a list of COLUMN NAMES only), `columns_used` (names), `output_columns`, `rules` (the rule names used), `counts` (`{"deterministic", "candidate", "ambiguous"}`), `rows_total`, `over_219` (`{"reachable", "deterministic", "candidate_only", "unlinked", "matched", "unmatched"}`), `commonwealth_accounts_touched`, `scratch_disk_write` (false only if the process wrote nothing but the links file and this record), `cloudtrail_data_event_read` (false), `file` (`{"path", "rows", "sha256"}`), `not_established`; and a short `.md` with the same figures. No CRM value, name, account number or dollar appears in either. When the record is written, REPORT AT ONCE: the withdrawal runs as the job's NEXT act.

### ACCEPTANCE

<criterion id="CB88cj2-AC1" cell_refs="CB-cj-2"><invocation>timeout 60 python org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/round88/checks/crm_checks.py job --file org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~177/JOB_RECORD.json --links C:/dev/_cotbkf_match_20261015/CRM_LINKS.csv</invocation><expect>^CRM-JOB: OK landed=(True|False) rows=\d+ bad=-$</expect></criterion>
`CB88cj2-AC1` -- the record names the one key, the output columns equal the allow-list exactly, the links file's header line equals it and its row count equals the record's, the tiers sum to the rows, the 219 splits into matched and unmatched, and the job wrote nothing else to disk. (With `landed` false the links file is absent and the check reads the record only.)

<criterion id="CB88cj2-AC2" cell_refs="CB-cj-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q</invocation><expect>5 passed</expect></criterion>
`CB88cj2-AC2` -- the allow-list, the tiering, the no-ambiguous-deterministic rule, the nothing-else-written rule and the NOT_LANDED path hold on stubs.

<criterion id="CB88cj2-AC3" cell_refs="CB-cj-2" judgment="true"/>
`CB88cj2-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9 and never self-graded: no CRM column value, name, personal identifier or sample row appears in any committed file, record, log line, message or exception text of this cell; the links carry only the four columns; DETERMINISTIC rests on a direct stable-key pair and nothing weaker; the record states what the job did not read.

<expected_criteria>CB88cj2-AC1,CB88cj2-AC2,CB88cj2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the one outside folder `C:/dev/_cotbkf_match_20261015/` (only the file `CRM_LINKS.csv`). The ONE S3 key you may touch in the firm bucket is the zip (through the role). Reads of the Commonwealth and Black Diamond silver tables through your own shell identity as in round 87 (read-only). You edit no existing file.
- **The zip, and only the zip, through the role.** No other key, no listing of the prefix (the role cannot list and you do not try), no other bucket through the role, no write of any kind to S3. Do not run `aws sts get-caller-identity`. Do NOT assume the role for any purpose but this one run, and do not share its credentials with anything.
- **NEVER** write CRM content to disk or to a log; never print a row, a header's values, a sample; never contact Cottonwood or send anything outside; never wire the links into the served crosswalk; no `--apply`, no S3 write, no vendor call, no push, no gate override, no `--force`; do not weaken, delete, xfail or skip any test. A breach of the job's rules above is a STOP: write what happened WITHOUT any CRM content, file a row, finish the record, report, and the withdrawal runs.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; on this box it may fail closed (the pinned set is on another machine): report the exact error and do NOT look for the set.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W177-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. A row carries NO CRM content.

<paths>
data/assets/scripts/silver/cotbkf_crm_match_job.py
data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round88.md</decomp_doc> (round 88), cell `CB-cj-2`.
<owned_cells>CB-cj-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB88cj2-AC1, CB88cj2-AC2, CB88cj2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~177/ADVI_COTBKF.TO-CB-cj-2.crm-match-job.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB88cj2-AC1,CB88cj2-AC2,CB88cj2-AC3` BEFORE the flip. Mechanical: CB88cj2-AC1, CB88cj2-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. Declare the outside CSV in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when both mechanical criteria PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST, as soon as the record is written, one line to `2.0.0_SA_COO~C1`: landed or NOT_LANDED, rows by tier, matched and unmatched over the 219, the record path (the withdrawal starts on this). Then: AC1 and AC2 lines; which columns the job used (names) and why; what it did not read; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Nothing in the report quotes a CRM value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-shot job; nothing is scheduled or served.
comp-iam: RUN by the grant order (`CB-cj-1`): the role can GetObject the one key and nothing else; this order adds no permission.
comp-adversary: RUN -- the allow-list is a criterion the checker grades on the links file's header; the job cannot print a value because the rules forbid it and the test (d) proves nothing else is written; BLIND: the checker cannot see what the process held in memory or what a careless exception text might carry (the excepthook rule and the CVO's judgment criterion are the only controls), the shared shell user means another seat could in principle assume the role (the withdrawal order lists every AssumeRole event: C1), and `DETERMINISTIC` rests on the worker's reading of column NAMES alone (the CVO grades it).
lane: the <paths> block IS the grant (worker RULING 1). Risk WORLD: a restricted-data read under a time-limited grant; the CTO's exercised read and the change-management entry are the grant order's.
</preflight>

**ISSUER NOTES:** STAGED at the cut, UN-PARKED by AMENDMENT 1 below. Un-park conditions (all): `CB-cj-1` is complete (its AC1 PASS); the issuer's UN-PARK AMENDMENT below names the role ARN, the deadline and the read-back; at least 90 minutes remain before `deadline_utc`. Authority: Andrew-direct 2026-10-15 ~19:0xZ, "I agree with (a), let's see what we can do with that for now."; CTO ruling amendment 5.

**AMENDMENT 1 (2.0.0_SA_COO~C1, 2026-10-15 19:5xZ) -- UN-PARKED, GO:** (1) `CB-cj-1` is complete: the grant is LIVE since 19:49:31Z, role `arn:aws:iam::313476888478:role/cloudops-cot-crm-match-role` (read back live by this seat: `get-role` returns it, max session 3600), `CRM-GRANT: OK` on the record `deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json` (apply commit e128e60b43, record 94ac0d28fe), deadline `2026-10-15T23:59:00Z`, trust = the dell1 agent user. (2) Plenty of time remains (more than 90 minutes before the deadline); the withdrawal order `CB-cj-3` is un-parked by this seat the moment your record is written, so write it promptly after the run. (3) Nothing in the order changes. Status pending.
