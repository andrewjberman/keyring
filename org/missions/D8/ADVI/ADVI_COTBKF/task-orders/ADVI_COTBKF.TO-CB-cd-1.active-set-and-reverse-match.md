# TO ADVI_COTBKF.TO-CB-cd-1.active-set-and-reverse-match -- round 82 CB-cd-1: the active Cottonwood set with each account's per-security held windows, and the reverse match (every current Black Diamond Cottonwood account with its Commonwealth predecessor or "none")

<to_id>ADVI_COTBKF.TO-CB-cd-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~161</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>82</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cd-1` (`decompositions/ADVI_COTBKF_DECOMP.round82.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of the firm's own served and silver tables and of the Commonwealth silver tables. You change no code. Nothing is built, served, corrected or fetched from a vendor. The set is written to ONE file OUTSIDE the repository (account keys must not enter the tree); only counts, a checksum and a path are committed.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_82_20261013.md` whole, section 2 ruling 4 and section 3 item 1, word for word:
"the active Cottonwood set: every currently active account, with its per-security held windows, under the 2012 floor and each account's earliest record; the reverse match: every current Black Diamond Cottonwood account with its Commonwealth predecessor or 'none'. It is read-only. Its path goes to dell1's MDPF_DEMQUE through `0.0.0_AB_MSTR~DELL2`, so former clients are EXCLUDED from every draw."
And "One file plus its path. Counts printed, no account value." Then Andrew's words and the outcome, `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O4 (lines 220-249, quoted there),
and the backfill law (`git show origin/box/dell1:org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`, record @82c7c92449: nothing before 2012-01-01; an account's history starts at its earliest record). The crosswalk record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md` (FWD-8: 1,533 Commonwealth accounts, 471 MATCHED, 1,062 NOT_MATCHED, 21 near matches waiting on a person) and the readers it names
(`data/assets/scripts/analysis/commonwealth_fwd8_read.py`, `commonwealth_account_history.py`).

**Where the data is (read-only; confirm each by the estate's tools before relying on it, and say what you confirmed):**

| side | source |
|---|---|
| Commonwealth | `s3://opal-data-assets/commonwealth/cottonwood/silver/` (tables: transactions, positions, crosswalk, account_links, document_index and the others the manifest lists; use `date=2026-06-23/`): `crosswalk/.../crosswalk.csv` (Commonwealth account to Black Diamond account, with MATCHED/NOT_MATCHED and a reason), `account_links/.../account_links.csv` (old account to its successor) |
| Black Diamond | the firm's own bucket `s3://opal-data-cot/`: the dated snapshots under `silver/holdings/` (the latest snapshot date is the "current" mark; the snapshots begin 2026-06-08) and `gold/canonical/holdings/{date}.parquet` (134 keys; the 47 dated 2026-04-22 to 2026-06-07 were built by the no-snapshot branch); `B_00.canonical_holdings.py:127-139` shows how the snapshot dates are listed |

**Your item.**

1. **Define "currently active", write the definition down FIRST, and report the count under the primary definition and two alternatives.** Primary: the account holds a position in the latest Black Diamond holdings snapshot (state its date and the number of accounts it lists). Alternatives (counts only): holds a position in any snapshot dated in the last 90 days;
   has any transaction dated in the last 90 days. Say how many accounts differ between the primary and each alternative.
2. **The active set file.** One account per row; for each, its per-security held windows: `security` (CUSIP and ticker), `held_from`, `held_to` (open if still held). A window starts at the account's earliest record, never before 2012-01-01 (the backfill law); where an account has history on both sides (Commonwealth before, Black Diamond after), the windows join across the predecessor link (state how, in the
   record). Columns exactly: `account_key`, `source_side`, `cusip`, `ticker`, `held_from`, `held_to`, `window_basis` (one of `commonwealth_transactions`, `black_diamond_holdings`, `joined`, `not_established`). **`account_key` is the crosswalk's own pseudonymous token (the `acct#...` form the Commonwealth silver tables already use) wherever one exists; where only a Black Diamond account number exists, a salted
   SHA-256 token with the salt printed nowhere and kept only in the file `.scratch/` of your worktree; NEVER print an account number or an account value.** Write it as `C:/dev/_cotbkf_active_set_20261013/ACTIVE_COTTONWOOD_SET.csv` (create the folder; it is OUTSIDE the repository on purpose), UTF-8, LF, with a header line. Do not open or print anything else under `C:/dev/_cotbkf_private_evidence_20261009/`.
3. **The reverse match.** Write `C:/dev/_cotbkf_active_set_20261013/REVERSE_MATCH.csv`: every CURRENT Black Diamond Cottonwood account (the primary definition's accounts) with its Commonwealth predecessor key or the word `none`, columns exactly: `account_key`, `predecessor_key`, `match_basis` (`crosswalk_matched`, `account_links`, `near_match_waiting_on_a_person`, `none`), `reason` (the crosswalk's reason code or `none`). Count: matched, linked, near matches waiting on a person, none. The crosswalk matches one direction only (FWD-8); this is the other direction, read from the same tables, and any
   current account the crosswalk cannot reach is `none` with the reason, never silently dropped. Print the denominator: current accounts in the snapshot = rows in the file.
4. **Former clients.** Count (not list) the Commonwealth accounts that are NOT in the active set (accounts with history but no position in the primary definition), and the number of securities that appear only in their windows. This is the quota the demand queue stops spending; give the counts of securities in the active set and securities only former clients held.
5. **Write the committed record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json` and a short `.md` (no account key, number or value in either). Top-level keys, exactly: `definition` (`{"primary", "snapshot_date", "snapshot_accounts", "alt_90d_snapshots", "alt_90d_transactions", "differs_from_alt_1", "differs_from_alt_2"}`), `files` (a list of 2: `{"path", "rows", "sha256", "bytes"}`),
   `active_accounts`, `securities_active`, `window_rows`, `earliest_window_start`, `windows_clipped_by_floor` (a count), `windows_joined_across_predecessor` (a count), `reverse_match` (`{"current_accounts", "crosswalk_matched", "account_links", "near_match_waiting_on_a_person", "none", "rows_in_file"}`), `former_client_accounts`, `securities_only_former_clients`, `sources` (a list of what you read, with the date or version), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB82cd1-AC1" cell_refs="CB-cd-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json',encoding='utf-8'));r=d['reverse_match'];print('ACTIVE-SET active_accounts=%d securities_active=%d window_rows=%d earliest=%s current_accounts=%d matched=%d linked=%d near=%d none=%d rows_in_file=%d former=%d'%(d['active_accounts'],d['securities_active'],d['window_rows'],d['earliest_window_start'],r['current_accounts'],r['crosswalk_matched'],r['account_links'],r['near_match_waiting_on_a_person'],r['none'],r['rows_in_file'],d['former_client_accounts']))"</invocation><expect>ACTIVE-SET active_accounts=</expect></criterion>
`CB82cd1-AC1` -- the set and the reverse match are counted; the reverse match's four classes are printed with the rows in its file. The issuer reads that the classes sum to the current accounts.

<criterion id="CB82cd1-AC2" cell_refs="CB-cd-1"><invocation>python -c "import json,hashlib;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json',encoding='utf-8'));f=d['files'];ok=all(hashlib.sha256(open(x['path'],'rb').read()).hexdigest()==x['sha256'] and len(open(x['path'],'rb').read())==x['bytes'] for x in f);n=[sum(1 for _ in open(x['path'],encoding='utf-8'))-1 for x in f];print('ACTIVE-SET-FILES files=%d sha256_match=%s rows=%s outside_repo=%s'%(len(f),ok,n,all(not x['path'].startswith('org/') for x in f)))"</invocation><expect>ACTIVE-SET-FILES files=2 sha256_match=True</expect></criterion>
`CB82cd1-AC2` -- the two files exist at the recorded paths with the recorded checksum and size, outside the repository. The issuer reads the row counts against the record.

<criterion id="CB82cd1-AC3" cell_refs="CB-cd-1" judgment="true"/>
`CB82cd1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: "currently active" is defined before it is counted and the alternatives are shown; no window starts before 2012-01-01 or before the account's earliest record; the reverse match drops no current account and says why an account is `none`; the former-client counts are counts, not a list;
no account number, name or value appears in the repository, in a message or in the record; `not_established` stands wherever a source could not be read.

<expected_criteria>CB82cd1-AC1,CB82cd1-AC2,CB82cd1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row), the new folder `C:/dev/_cotbkf_active_set_20261013/` (the two data files only) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READ-ONLY, through the `.tools/aws` shim:** `get-object` of the Commonwealth silver tables above (`date=2026-06-23/`), of the Black Diamond holdings snapshots under `s3://opal-data-cot/silver/holdings/` and of `gold/canonical/holdings/` keys you need, and ONE `list-objects-v2` of `silver/holdings/` for the dates (the listing is auto-paginated and counted; state its denominator). No write, delete or serve; no other bucket; no restricted CRM prefix. If a read is refused, record the exact error and mark that part `not_established`.
- **Another firm's data is never opened.** No account number, name or value is printed, committed or sent: counts, dates, CUSIPs, tickers and reason codes only. A CUSIP appears only in the CSV column named exactly `cusip`.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull); no Black Diamond API call: the snapshots on S3 are what is read.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Nothing else under that folder is opened or printed.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W161-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round82.md</decomp_doc> (round 82), cell `CB-cd-1`.
<owned_cells>CB-cd-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB82cd1-AC1, CB82cd1-AC2, CB82cd1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ADVI_COTBKF.TO-CB-cd-1.active-set-and-reverse-match.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB82cd1-AC1,CB82cd1-AC2,CB82cd1-AC3` BEFORE the flip. Mechanical: CB82cd1-AC1, CB82cd1-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. You flip your own order `<status>` to `complete` in the commit that carries the proof instance, as the earlier rounds' workers did.
</proof_of_spec>

**REPORT:** FIRST, the two file paths, their rows and sha256 (so the issuer can send the path at once). Then: the definition and the three counts; the active accounts, securities and window rows; windows clipped by the floor and joined across a predecessor; the reverse match's classes and denominator; the former-client counts; every remote read made; the `ACTIVE-SET` and `ACTIVE-SET-FILES` lines; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and snapshot tables; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- "active" is defined before it is counted and the alternatives are shown; a window never starts before the floor or the account's earliest record; the reverse match drops no current account; no account number reaches the repository; BLIND: an account active on the Black Diamond side that holds only cash, and a successor link the crosswalk never recorded.
lane: the <paths> block IS the grant (worker RULING 1); the two data files sit outside the repository by design.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-82 analysis @ea59dfcdec (msg 7196), section 2 ruling 4, section 3 item 1; pivot direction O4; `3.0.0_SA_CVO` REMEDIATION_v50 @43b340c673.
