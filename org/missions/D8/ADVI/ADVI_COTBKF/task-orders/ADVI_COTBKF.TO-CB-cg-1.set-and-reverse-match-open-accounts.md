# TO ADVI_COTBKF.TO-CB-cg-1.set-and-reverse-match-open-accounts -- round 85 CB-cg-1: the active Cottonwood set and the reverse match rebuilt under "open at Black Diamond on the latest snapshot, cash included", raw keys, a reason for every `none` row from the committed list, checked against the round-82 files by aggregate invariants

<to_id>ADVI_COTBKF.TO-CB-cg-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~168</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>85</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cg-1` (`decompositions/ADVI_COTBKF_DECOMP.round85.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-cf-1 (merged @cdca442759)

---

## WORKER FACE

### THE CELL

**This is a READ of S3 tables and of committed files. You change no code, no test and no committed file. Nothing is built, served, corrected or fetched from a vendor. You write TWO new CSVs OUTSIDE the repository (they carry raw account numbers, which Andrew's word of 2026-10-09 allows in the private repository: "I don't care about the client data getting committed to Git"; the issuer commits them) and a record inside your own deliverables folder (no account number in it).**

**Read first:** the CTO's ruling, word for word (msg 7343): "'active' = an account OPEN at Black Diamond in the latest snapshot, cash-only included; not a 90-day window. Andrew's line is between current clients and 'client accounts that no longer are even active'. A current account holding only cash today is still a client, and its sold or matured securities are backfill he wants. ...
Rerun the set and the reverse match with: open at BD on the latest snapshot (any position, cash included). Print the new count against 769 and against the 90-day 875, re-hash, and keep the exemption current."
Then the round-82 order and record you are repeating under the new definition: `org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cd-1.active-set-and-reverse-match.md` (items 2 and 3 are the method; read them whole) and `deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json` (`sources` say what was read: the Commonwealth transactions, crosswalk and account_links at `date=2026-06-23/`, the Black Diamond silver holdings and the gold canonical holdings; `commonwealth_signs.py` is the signed-quantity rule).
The round-82 files: `deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET.csv` (42,319 rows; 769 accounts) and `REVERSE_MATCH.csv`; the round-84 result `deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASONS_RECORD.json` and the CLOSED LIST `deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASON_LIST.md` (committed before any classification; reuse its codes, tests and migration date M = 2026-06-23 unchanged; its candidate test used tokens and was partly `not_established`: with raw keys you can measure it, and you say so).
**Why raw keys:** the salt that tokenised the Commonwealth-side keys and 312 of the 769 Black Diamond keys is in no committed file and its worktree is gone (rows W164-S1, W164-S3, W167-S2), so the old keys cannot be re-derived. You key BOTH sides by the raw account number as the source tables carry it, so that dell1 can join and so that every key can be checked against a raw snapshot.

**Your item.**

1. **The definition, written down FIRST and counted three ways.** Primary (the CTO's): an account is ACTIVE iff it appears in the latest Black Diamond silver holdings snapshot (`s3://opal-data-cot/silver/holdings/`, dated 2026-10-12 per round 82; confirm the latest date by the listing) with at least one row of any kind, cash and cash-equivalent rows included. State precisely how you decide "open" from the columns (`account_id`, `units`, `cusip`, `ticker`, `cash_equivalent`); if a listed account has only zero-unit rows, count it separately and say how you ruled. Report: the primary count; the round-82 count (769: a non-cash position with units above zero);
   the 90-day count (875: any snapshot in 90 days); the differences primary minus 769 and primary minus 875, by the number of accounts in each; and for the accounts in the primary set but not in the 769: how many hold only cash-equivalent rows (round 84's worker found 14 crosswalk-current accounts of that kind).
2. **The active set file.** Method as round 82's item 2, under the primary definition and raw keys: per account, per security, the held windows (`held_from`, `held_to`, open if still held), never before 2012-01-01 and never before the account's earliest record, joined across the Commonwealth predecessor where the reverse match finds one. Columns exactly: `account_key,source_side,cusip,ticker,held_from,held_to,window_basis`. Cash-equivalent holdings are windows like any other (`window_basis` as before). Write `C:/dev/_cotbkf_active_set_20261013/ACTIVE_COTTONWOOD_SET_V2.csv` (UTF-8, LF, header line).
3. **The reverse match file.** As round 82's item 3, for every account in the primary set: `C:/dev/_cotbkf_active_set_20261013/REVERSE_MATCH_V3.csv`, columns exactly `account_key,predecessor_key,match_basis,reason`; `predecessor_key` is the raw Commonwealth account number or `none`; `match_basis` in `crosswalk_matched`, `account_links`, `near_match_waiting_on_a_person`, `none`; `reason` the crosswalk's reason code, or for a `none` row with no crosswalk reason, ONE code of the committed list (`NO_COMMONWEALTH_HOUSEHOLD`, `NEW_CLIENT_AFTER_MIGRATION`, `MISMATCH_NO_IDENTIFIER`, `OTHER`, with the list's sub-codes for OTHER), assigned by the list's tests in the list's order. Every `none` row carries a reason; a row you cannot class is a row, not a new code.
4. **Invariants against the round-82 files (aggregates, because the keys differ).** For the accounts that satisfy the OLD definition (the 769) the rebuild must reproduce: 769 accounts; 3,357 securities; 42,319 window rows; earliest window start 2013-04-08; 6,736 rows joined across a predecessor; the reverse match 457 crosswalk_matched, 12 near, 0 account_links, 300 none (273 reasonless plus 27 AMBIGUOUS). Print each invariant as `expected / got / MATCH|DIFF`. A DIFF is reported, never forced, and you say which side you trust and why (the old files were built with tokens and a key derivation that was never checked).
   For the reason codes of the 273: compare your counts with round 84's (152 / 89 / 32 / 0) and say what changed now that the candidate test is measurable.
5. **The four identifiers.** dell1's four (35907XEW3, 38150V6Q7, 912796Y37, 912797GE1): rows in the new set file for each, and for each the number of accounts that hold or held it among the primary set (counts only).
6. **Write the record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~168/ACTIVE_SET_V2_RECORD.json` and a short `.md` (no account number, name or value in either). Top-level keys, exactly: `definition` (`{"primary", "snapshot_date", "snapshot_accounts", "zero_unit_only_accounts", "count_primary", "count_769", "count_90d", "primary_minus_769", "primary_minus_90d", "cash_only_added"}`), `files` (a list of 2: `{"path", "rows", "sha256", "bytes"}`), `active_accounts`, `securities_active`, `window_rows`, `earliest_window_start`,
   `reverse_match` (`{"current_accounts", "crosswalk_matched", "account_links", "near_match_waiting_on_a_person", "none", "rows_in_file", "none_without_reason"}`), `none_by_code`, `invariants` (a list: `{"name", "expected", "got", "match"}`), `four_identifiers` (a list of 4: `{"cusip", "rows_in_set", "accounts"}`), `former_client_accounts`, `sources`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB85cg1-AC1" cell_refs="CB-cg-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~168/ACTIVE_SET_V2_RECORD.json',encoding='utf-8'));df=d['definition'];r=d['reverse_match'];print('ACTIVE-SET-V2 primary=%d vs769=%d vs90d=%d active=%d securities=%d window_rows=%d current=%d matched=%d near=%d none=%d none_without_reason=%d rows_in_file=%d invariants_match=%d/%d'%(df['count_primary'],df['count_769'],df['count_90d'],d['active_accounts'],d['securities_active'],d['window_rows'],r['current_accounts'],r['crosswalk_matched'],r['near_match_waiting_on_a_person'],r['none'],r['none_without_reason'],r['rows_in_file'],sum(1 for x in d['invariants'] if x['match']==True),len(d['invariants'])))"</invocation><expect>ACTIVE-SET-V2 primary=</expect></criterion>
`CB85cg1-AC1` -- the three counts are printed side by side, the reverse match's classes are counted against its rows, no `none` row lacks a reason, and the invariants are printed with their match flags.

<criterion id="CB85cg1-AC2" cell_refs="CB-cg-1"><invocation>python -c "import json,hashlib;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~168/ACTIVE_SET_V2_RECORD.json',encoding='utf-8'));f=d['files'];ok=all(hashlib.sha256(open(x['path'],'rb').read()).hexdigest()==x['sha256'] and len(open(x['path'],'rb').read())==x['bytes'] for x in f);n=[sum(1 for _ in open(x['path'],encoding='utf-8'))-1 for x in f];print('ACTIVE-SET-V2-FILES files=%d sha256_match=%s rows=%s outside_repo=%s'%(len(f),ok,n,all(not x['path'].startswith('org/') for x in f)))"</invocation><expect>ACTIVE-SET-V2-FILES files=2 sha256_match=True</expect></criterion>
`CB85cg1-AC2` -- the two files exist at the recorded paths with the recorded checksum and size, outside the repository.

<criterion id="CB85cg1-AC3" cell_refs="CB-cg-1" judgment="true"/>
`CB85cg1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: "active" is the CTO's, defined before it is counted and shown against 769 and 875; every window respects the 2012 floor and the account's earliest record; the reverse match drops no active account and every `none` row carries a code from the committed list, assigned by its tests in its order; the invariants against the round-82 files are printed with their results and a DIFF is explained, not forced;
the four identifiers are answered; no account number, name or value appears in the committed record, the report or any message.

<expected_criteria>CB85cg1-AC1,CB85cg1-AC2,CB85cg1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row), the folder `C:/dev/_cotbkf_active_set_20261013/` (the two new files only) and the file of this order.
- **You change no code, test, config, manifest or registry, and you do not edit any file in `deliverables/2.0.0_SA_COO~C2/`, `NONE_REASON_LIST.md` or the scan test.** The new files' commit, sha256 pin and exemption are the issuer's.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the tables the round-82 record lists (Commonwealth silver tables at `date=2026-06-23/`; the Black Diamond holdings keys): the two prefix listings the record describes and `get-object` of what they list (state each listing's denominator). No write, delete or serve; no other bucket; no restricted CRM prefix. If a read is refused, record the exact error and mark that part `not_established`.
- **Account numbers and values are never printed, committed or sent beyond the two outside files.** Counts, dates, codes and CUSIPs only in reports and records. Do not run `aws sts get-caller-identity`. Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/` in any way. Do not search for the old salt.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line (your committed files carry no account number, so it should read 0 hits beyond the pinned files).
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch;** no Black Diamond API call.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W168-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round85.md</decomp_doc> (round 85), cell `CB-cg-1`.
<owned_cells>CB-cg-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB85cg1-AC1, CB85cg1-AC2, CB85cg1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~168/ADVI_COTBKF.TO-CB-cg-1.set-and-reverse-match-open-accounts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB85cg1-AC1,CB85cg1-AC2,CB85cg1-AC3` BEFORE the flip. Mechanical: CB85cg1-AC1, CB85cg1-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the two external CSVs in `declared_exclusions` if the checker refuses them as file artifacts. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the two file paths with rows and sha256 (so the issuer can send the path at once). Then: the three counts side by side with the differences; the cash-only accounts added; the active accounts, securities and window rows; the reverse match classes and its denominator; the `none` rows by code and what changed against round 84; the invariants with their match flags; the four identifiers; every remote read made; the `ACTIVE-SET-V2` and `ACTIVE-SET-V2-FILES` lines; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- "active" is the CTO's, counted three ways; raw keys on both sides, so every key is checkable against a raw snapshot; the rebuild is checked against the round-82 files by aggregate invariants and a DIFF is reported; the none reasons come from the list committed before any classification; BLIND: an account open at Black Diamond that holds only zero-unit rows, and an account whose Commonwealth predecessor was never recorded.
lane: the <paths> block IS the grant (worker RULING 1); the two new CSVs sit outside the repository by design.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 7343 (ruling); round-84 record and list (`NONE_REASONS_RECORD.json`, `NONE_REASON_LIST.md` @9442dec344 / b8de2ba358); round-82 files and record; `3.0.0_SA_CVO` ADJUDICATION_v59 @e819f0fc64.
