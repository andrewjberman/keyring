# TO ADVI_COTBKF.TO-CB-da-1.account-match-review-sheet -- round 104 CB-da-1: build one Excel workbook a person can read, that presents the 107 proposed Commonwealth-to-Black-Diamond account pairs to confirm (and the 11 already settled) in plain words, grouped by household; written to the desktop only; read-only, counts only in the repo

<to_id>ADVI_COTBKF.TO-CB-da-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~194</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-da-1` (`decompositions/ADVI_COTBKF_DECOMP.round104.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew-direct, 2026-10-16 ~16:30Z, verbatim: "The match packet is not very easy to read, its a bunch of account strings, no human being is going to read that. there has to be an easier mechanism to present that information." The committed near-match packet is a CSV of 12-character link ids and bands; the real account numbers sit in a separate key file. Someone has to decide, for each of 107 proposed pairs, whether a Commonwealth account (a former account) and a Black Diamond account (a current account) belong to the same client. You build the sheet that lets a person do that by reading names, dates, holdings and values, not strings. **You read; you write no link, change no rule, send nothing, upload nothing, and contact no one. The workbook goes to the desktop and nowhere else.**

**Inputs (READ-ONLY; all off git except the packet):**
1. The key `C:/dev/_cotbkf_match_20261015/NEAR_MATCH_REVIEW_KEY.csv` (118 rows: `link_id, commonwealth_account, bd_account_id, crm_confidence, crm_hhid, crm_household, crm_pair_siblings, crm_bd_household_check`).
2. The committed packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/NEAR_MATCH_REVIEW_PACKET.csv` (columns `link_id, routes, r4_tier, r4_household_via, r4_window_ok, r4_fingerprint_band, name_corroborations, in_219, bd_account_state, competing_pairs`) and its page `NEAR_MATCH_REVIEW_PACKET.md` (what each column means). A pair is TO CONFIRM when `r4_tier` is not `DETERMINISTIC` (107 rows); the other 11 are already settled by the holdings fingerprint.
3. The local cache `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache/`: `accounts.parquet` (`account_id, relationship_id, account_open_date`) and `holdings.parquet` (`date, account_id, asset_name, ticker, units, cusip`) are the Black Diamond side; `positions.parquet` (`AccountNumber, Cusip, Symbol, Quantity, AsOfDate`) and `transactions.parquet` (`Account_Number, Cusip, Symbol, Quantity, Trade_Date, Transaction_Type`) are the Commonwealth side. Your worktree has no `.scratch`: pass absolute paths.
4. The served Commonwealth tables, one `get_object` each at the pinned VersionId, for the old account's value and dates: `account_day_value` at `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a` (`s3://opal-data-assets/commonwealth/cottonwood/silver/account_day_value/date=2026-06-23/part-00000.parquet`; columns `account, date, cusip, quantity, close, value`).
5. Human-readable account names and registrations: find where each side's account name, client line or registration lives by following the code that built the packet: `data/assets/scripts/silver/cotbkf_review_packet.py` and the R4 route it reads (`r4_household_via` is "the account name, or the client line"), its tests, and the round-90 records under `deliverables/0.9.0_WK_ADVI_COTBKF~180/` and its neighbours. Read-only S3 reads of the Black Diamond and Commonwealth silver tables that route reads are allowed. Report in the record what each side actually has (`identifies` below).

**The workbook (the CTO's spec, msg 6874): ONE Excel file, `C:/Users/Test/Desktop/Cottonwood_Account_Match_Review_20261016.xlsx`, written with `openpyxl`.**
- **Sheet 1, `Read me`** (it must be the first sheet), in plain words, at least 600 characters: what a match is here (a Commonwealth account and a Black Diamond account that belong to the same client, so the old history can follow the client); how to answer (in the `To confirm` sheet, set `Your answer` to Yes, No or Unsure for each row; leave a row blank to skip; for a group marked "choose at most one", answer Yes on at most one row); how many rows there are to confirm (107) and how many were already settled (11); what `Match strength` means and exactly how it is set (rule below); what the sheet cannot tell (it cannot say which candidate is right, only that it passed the tests; a Yes is the confirmer's word); what is not in it (no tax number, date of birth, licence or passport number; account numbers appear nowhere in the visible columns); and that the file is confidential client data to be kept off email and shared drives.
- **Sheet 2, `To confirm`**: ONE ROW PER PROPOSED PAIR (107 rows), GROUPED BY HOUSEHOLD (sort so a household's rows sit together; a thin header row or a "Household" column repeating the household's name is fine, but keep one row per pair and no merged cells inside the data). Columns, with these exact headings, in this order: `Household`, `Old account name`, `Old account active`, `Old account value`, `Old account top holdings`, `Proposed account name`, `Proposed account opened`, `Proposed account value`, `Shared holdings`, `Match strength`, `Competing candidates`, `Your answer`, and the LAST column, hidden, headed `link_id`. `Old account` is the Commonwealth side and `Proposed account` the Black Diamond side. `Old account name` / `Proposed account name`: the account's name or registration as found (item 5); if a side has none on file, show `(no name on file)` and the last four digits of the account number in brackets, never the full number. `Old account active`: first and last trade or position month. `Old account value` / `Proposed account value`: the last valued day's total value for the old account (served `account_day_value`, the last date it has a value) and the latest total for the proposed one, whole dollars, with the date beside it in the same cell text (for example `$412,300 on 2017-11-30`); a blank where there is none. `Old account top holdings` / `Shared holdings`: up to five security NAMES (not tickers alone, never cusips) in plain words, by value or by units, separated by `; `; shared holdings are the securities both accounts hold or held. `Match strength`: exactly one of `strong`, `likely`, `weak`. `Competing candidates`: when `competing_pairs` is above 0, a plain sentence naming the OTHER proposed account(s) for the same old account (by name and value, not by number) and ending "choose at most one"; competing pairs must sit on ADJACENT rows (same old account first), so a person sees them side by side. `Your answer`: empty in every row, with a list data validation of exactly `Yes,No,Unsure` on every data row. `link_id`: the pair's 12-character id, the only place it appears; the column is hidden.
- **Sheet 3, `Already matched`**: the 11 deterministic pairs, one row each, for information (no answer column): `Household`, `Old account name`, `Proposed account name`, `Old account value`, `Shared holdings`, and a one-line note "Settled by the holdings fingerprint; nothing to confirm".
- **Match strength rule (state it verbatim on the `Read me` sheet).** `strong`: `routes` includes R4, `r4_fingerprint_band` is `>=0.8`, `r4_window_ok` is true, and `competing_pairs` is 0. `weak`: `r4_fingerprint_band` is `<0.5`, or `r4_window_ok` is false, or the pair was found only by the name route with `name_corroborations` of 0 or 1. `likely`: every other pair. (`crm_confidence` and `crm_household` may be shown in a ninth, optional visible column headed `Cottonwood CRM says` ONLY if non-empty, in plain words such as "same CRM household as the other proposed pair"; it must not change the strength.)
- **Formatting for a human:** frozen header row, wrapped text, column widths that fit, the household's rows shaded alternately, `strong`/`likely`/`weak` as plain words (colour optional), the file opens on `Read me`. No macros, no images, no external links.

**Your items.**
1. Read the packet, the key and `cotbkf_review_packet.py`; find each side's name/registration source; list in your report, per side, what identifies an account (name, client line, registration class, open date, holdings) and how many of the 118 pairs lack a name on each side.
2. Build the workbook as specified and save it to the desktop path above. Do not save it anywhere else (no copy in the worktree, the repo, the scratch folders of the repo, or the Downloads folder), and do not email, upload, Taildrop or commit it. Open it back with `openpyxl` and read three of its rows aloud in your report in WORDS ONLY with the names replaced by `[name]` (to show it is readable), no values and no numbers.
3. Run the issuer's checks (AC2 and AC3 below) and fix the workbook until they pass.
4. The record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~194/REVIEW_SHEET_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `workbook` (`{"path_class":"desktop","sheets":[...],"data_rows_to_confirm","rows_already_matched","households"}`), `strengths` (`{"strong","likely","weak"}`), `competing_groups` (the number of groups of competing rows and the rows in them), `identifies` (per side: `{"name_source","pairs_with_name","pairs_without_name","open_date_source","holdings_source","value_source"}`), `blanks` (per visible column of `To confirm`: the number of rows with no entry), `rule_text_on_read_me` (true/false), `what_this_shows` (two sentences in counts), `not_established`; and a short `.md` beside it. COUNTS AND SOURCE NAMES ONLY: no account number, name, household name, security name or dollar value in the record, the `.md` or your report.

### ACCEPTANCE

<criterion id="CB104da1-AC1" cell_refs="CB-da-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~194/REVIEW_SHEET_RECORD.json',encoding='utf-8'));m=d['measured'];w=d.get('workbook') or {};s=d.get('strengths') or {};print('REVIEW-SHEET-RECORD measured=%s' % m + ((' rows=%d settled=%d households=%d strong=%d likely=%d weak=%d' % (w['data_rows_to_confirm'],w['rows_already_matched'],w['households'],s['strong'],s['likely'],s['weak'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^REVIEW-SHEET-RECORD measured=(True rows=107 settled=11 households=\d+ strong=\d+ likely=\d+ weak=\d+|False reason=.+)$</expect></criterion>
`CB104da1-AC1` -- the record states the 107 rows to confirm, the 11 settled, the households and how the strengths split, or states plainly why nothing could be built.

<criterion id="CB104da1-AC2" cell_refs="CB-da-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cz1_review_sheet_check.py</invocation><expect>^REVIEW-SHEET sheets_ok=True rows=107 ids_match=True link_id_hidden_last=True answer_blank=True answer_validation=True visible_account_strings=0 visible_link_ids=0 blank_old_name=\d+ blank_new_name=\d+ blank_value=\d+ strengths=.+$</expect></criterion>
`CB104da1-AC2` -- the issuer's script opens the desktop workbook and checks it: `Read me` first with real text, a `To confirm` sheet of 107 rows whose hidden last column holds exactly the packet's 107 to-confirm link ids once each, an empty `Your answer` column with a Yes/No/Unsure list validation, and NO full account string or link id in any visible cell. (It prints the blank counts and the strength counts; read it, do not edit it.)

<criterion id="CB104da1-AC3" cell_refs="CB-da-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cz1_review_sheet_check.py --offgit org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~194/REVIEW_SHEET_RECORD.json org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~194/REVIEW_SHEET_RECORD.md</invocation><expect>^SHEET-OFFGIT outside_repo=True tracked_review_xlsx=0 record_account_strings=0$</expect></criterion>
`CB104da1-AC3` -- the workbook is outside the repository, no review workbook is tracked by git, and the committed record and its `.md` carry no account string of the key.

<expected_criteria>CB104da1-AC1,CB104da1-AC2,CB104da1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). The ONE write outside the repository is the workbook at the desktop path named above. You change no code, test or other committed file. Scratch, if any, stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r104/` (gitignored); a small build script of yours may be committed in your deliverables folder as evidence provided it contains no account string, name or value. Your instance rows for artifacts that already exist in a commit are pinned to that commit's FULL hash.
- **AWS: READ-ONLY** (`get_object` of the served `account_day_value` at its pinned VersionId and the read-only reads of Black Diamond and Commonwealth silver tables the packet's route already uses); no write, no vendor call, no Bloomberg, no Yahoo. You contact no one: not Cottonwood, not Commonwealth, not Black Diamond or Orion, and you send nothing by email, Teams, Taildrop or the broker.
- **PRIVACY.** The workbook holds client names and values and is confidential: it stays on the desktop. It carries NO tax identifier, date of birth, driver's licence or passport number (the four restricted CRM fields), and no account number in a visible column. If a source you read carries one of the four restricted fields, do not copy it and say so (by field name, never value) in `not_established`.
- **NEVER** apply a link, change a rule or the key, edit any module, serve, push, override a gate or `--force`; never write a name, account string or dollar value into a record, a row, a commit message or a message.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W194-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only; the row carries no name, string or value. If a side has NO human-readable name anywhere you can read, build the sheet with the fallback in the column spec, say so in `identifies`, and file one row.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-da-1.account-match-review-sheet.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip; the one write outside the repository is the desktop workbook.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round104.md</decomp_doc> (round 104), cell `CB-da-1`.
<owned_cells>CB-da-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB104da1-AC1, CB104da1-AC2, CB104da1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~194/ADVI_COTBKF.TO-CB-da-1.account-match-review-sheet.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB104da1-AC1,CB104da1-AC2,CB104da1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the `REVIEW-SHEET-RECORD` line. Then: where each side's name, dates, holdings and value come from and how many pairs lack a name on each side; the sheets and the counts of rows, households, strengths and competing groups; the blank counts per column; three rows read aloud in words with `[name]` in place of names; whether the file is only on the desktop; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account number, name, security name or dollar value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local workbook and a counts record; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE one get_object of a served object at a pinned version and read-only reads of silver tables the packet's route already reads, under the existing role; no new permission; no vendor access.
comp-adversary: RUN -- the workbook is checked by an issuer script against the committed packet's 107 to-confirm ids and the off-git key's account strings (positive and negative controls run on synthetic workbooks: a complete one, one leaking an account string, one short of three rows, one without validation and hiding); BLIND: the script cannot judge whether a name or holding is the RIGHT one for its row (only that the row is present, labelled and free of account strings), so the issuer spot-reads three rows against the key before it goes to Andrew, and cannot tell whether a person finds the sheet easy to read, which is Andrew's judgment on opening it; names and values come from sources the worker finds, so a wrong join would put a wrong name on a row and the check would pass.
lane: the <paths> block IS the grant (worker RULING 1) and names the order file for the status flip; the one write outside the repository is the desktop workbook, named in the face.
</preflight>

**ISSUER NOTES:** Source: Andrew-direct 16:30Z (record @ffae57dacc) and CTO msg 6874 (the spec; "do not wait for who confirms"). Mechanical checks dry-run at the base (the workbook and record are absent): AC1, AC2 and AC3 FAIL as expected. The checker was run on four synthetic workbooks built from the real link ids (complete: all true; leaking one account string: visible_account_strings=1; three rows short: ids_match=False; no validation and not hidden: both False) and its off-git mode against the key file (211 account strings found) as a negative control.
