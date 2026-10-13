# TO ADVI_COTBKF.TO-CB-ce-1.four-cusips-missing-from-the-set -- round 83 CB-ce-1: four CUSIPs a matched active client traded are absent from ACTIVE_COTTONWOOD_SET.csv: the cause per CUSIP, the rows with windows to add, and the same test over every security a matched active account traded

<to_id>ADVI_COTBKF.TO-CB-ce-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~164</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ce-1` (`decompositions/ADVI_COTBKF_DECOMP.round83.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of S3 tables and of two committed files. You change no code. Nothing is built, served, corrected or fetched from a vendor. You write rows to ONE file in your own deliverables folder; you do NOT edit the active set file or any test.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_83_20261013.md` section 2 item 1 ("Test EVERY security a matched active account traded against the set, not only dell1's four ... Name the cause per security and add the held rows with windows under a new sha256, keeping the exemption current. Counts and causes go to dell1 through this seat."), then the CTO's earlier instruction, word for word: "For each [of 35907XEW3, 38150V6Q7, 912796Y37, 912797GE1], give the cause: no-predecessor window, blank-CUSIP row, non-9-character id, former-client-only, or other. If an active account held it, add its rows with windows to the set. Counts and causes back to me; no account data."
The context: two bonds and two matured T-bills that a MATCHED Cottonwood client traded (last trades 2023-08, 2024-02, 2025-09, 2026-05); MDPF_DEMQUE refuses them because the set does not carry them. Andrew's rule: "any active account has backfill for its various securities ... held for the period that they were held."
The set and its record: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET.csv` (header `account_key,source_side,cusip,ticker,held_from,held_to,window_basis`; 42,319 rows; 769 active accounts), `REVERSE_MATCH.csv`, and the worker record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json` whose `sources` lists exactly what was read and how (the Commonwealth transactions, crosswalk and account_links tables under `s3://opal-data-assets/commonwealth/cottonwood/silver/*/date=2026-06-23/`; the Black Diamond holdings under `s3://opal-data-cot/`;
the signed-quantity rule in `data/assets/scripts/silver/commonwealth_signs.py`). Reuse that method: the same definition of "active", the same account keys, the same window rule, the same 2012 floor. The key for a Commonwealth account is the token the set already uses; where you must derive it, derive it the way the record says and CHECK your derivation by reproducing the set's row count for a sample of 20 accounts before relying on it.

**Your item.**

1. **Is each of the four in the set at all?** Count rows with that exact `cusip` in the committed set file. Then, in the Commonwealth transactions (Trade_Date, Cusip, Symbol columns): for each of the four, the number of accounts that traded it, the first and last Trade_Date, and whether the CUSIP appears in the `Cusip` column, only in the `Symbol` column, or in neither (blank `Cusip`).
2. **Who held it.** For each, how many of those accounts are in the active set (769, via the crosswalk and account_links exactly as the record built them), how many are NOT active (former clients), and how many are active but reached by no Commonwealth predecessor. Counts only.
3. **The cause per CUSIP,** one of: `no_predecessor_window` (the active account has no Commonwealth predecessor, so its history was never read), `blank_cusip_row` (the set carries the holding but under a blank `cusip`), `non_9_char_identifier` (carried under an identifier that is not 9 characters), `former_client_only` (no active account traded it), `window_rule_dropped_it` (an active account with a predecessor traded it and the window rule did not emit a row: say why, e.g. net quantity never positive, a type the signed rule drops, a maturity or redemption row), or `other` (say what). State the evidence for each (a count and the rule's file and line).
4. **The rows to add.** For each of the four where an active account held it, the rows `account_key,source_side,cusip,ticker,held_from,held_to,window_basis` exactly as the set writes them, with windows by the same rule, never before 2012-01-01 nor the account's earliest record. A bond that matured has a `held_to` (its last held day); report how you set it. Write them to
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/ACTIVE_SET_ADDITIONS.csv` (the `cusip` column is the only place a CUSIP appears; UTF-8, LF, header line). If an active account held none of them, the file holds only the header and you say so.
5. **The generalization: is the set complete for securities traded by matched active accounts?** Over ALL Commonwealth transactions of the active accounts (matched and linked), count the distinct CUSIPs traded, the distinct CUSIPs in the set for those accounts, and the difference; classify every missing CUSIP by the item 3 causes and print the counts per cause. Say how many of the missing are fixed-income (CUSIP begins with `9127`, or the security type the transaction table carries for bonds and bills; state the rule you used). Do NOT write rows for this generalization; report the counts and write the missing CUSIPs
   with their cause to `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/MISSING_BY_CAUSE.csv` (columns `cusip,cause,accounts_active,first_trade,last_trade`).
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/FOUR_CUSIPS.json` and a short `.md` (no account key, number or value in either). Top-level keys, exactly: `in_set` (a list of 4: `{"cusip", "rows_in_set"}`), `traded` (a list of 4: `{"cusip", "accounts_traded", "first", "last", "in_cusip_column", "in_symbol_only", "blank_cusip"}`), `held_by` (a list of 4: `{"cusip", "active", "not_active", "active_no_predecessor"}`), `cause` (a list of 4: `{"cusip", "cause", "evidence"}`),
   `additions` (`{"rows", "file", "sha256", "bytes"}`), `generalization` (`{"distinct_traded_by_active", "distinct_in_set", "missing", "by_cause": {...}, "missing_fixed_income"}`), `derivation_check` (`{"sample_accounts", "rows_reproduced", "rows_in_set"}`), `sources`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB83ce1-AC1" cell_refs="CB-ce-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/FOUR_CUSIPS.json',encoding='utf-8'));g=d['generalization'];print('FOUR-CUSIPS cusips=%d with_cause=%d additions_rows=%d traded_by_active=%d in_set=%d missing=%d missing_fixed_income=%s derivation=%s/%s'%(len(d['cause']),sum(1 for x in d['cause'] if x['cause']),d['additions']['rows'],g['distinct_traded_by_active'],g['distinct_in_set'],g['missing'],g['missing_fixed_income'],d['derivation_check']['rows_reproduced'],d['derivation_check']['rows_in_set']))"</invocation><expect>FOUR-CUSIPS cusips=4 with_cause=4</expect></criterion>
`CB83ce1-AC1` -- each of the four has a cause; the additions file has a recorded row count; the generalization is counted and the derivation was checked against the set. The issuer reads whether the set is complete.

<criterion id="CB83ce1-AC2" cell_refs="CB-ce-1"><invocation>python -c "import json,hashlib;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/FOUR_CUSIPS.json',encoding='utf-8'));a=d['additions'];b=open(a['file'],'rb').read();print('ADDITIONS-FILE rows=%d sha256_match=%s bytes_match=%s header_ok=%s'%(sum(1 for _ in open(a['file'],encoding='utf-8'))-1,hashlib.sha256(b).hexdigest()==a['sha256'],len(b)==a['bytes'],open(a['file'],encoding='utf-8').readline().strip()=='account_key,source_side,cusip,ticker,held_from,held_to,window_basis'))"</invocation><expect>ADDITIONS-FILE rows=</expect></criterion>
`CB83ce1-AC2` -- the additions file exists with the recorded checksum and size and the set's header.

<criterion id="CB83ce1-AC3" cell_refs="CB-ce-1" judgment="true"/>
`CB83ce1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each cause is a measured class with its evidence, not an inference; "active" and the keys are the set's own; the derivation was checked before use; no window starts before 2012-01-01 or an account's earliest record; the generalization counts securities of ALL matched active accounts, not only the four; no account number, name or value appears in the record, the report or any message.

<expected_criteria>CB83ce1-AC1,CB83ce1-AC2,CB83ce1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry, and you do not edit `ACTIVE_COTTONWOOD_SET.csv`, `REVERSE_MATCH.csv` or the scan test.**
- **AWS: READ-ONLY, through the `.tools/aws` shim:** `get-object` of the Commonwealth silver tables the record lists (`date=2026-06-23/`) and of the Black Diamond holdings keys the record lists; no listing beyond the one prefix listing the record describes (state its denominator); no write, delete or serve; no other bucket; no restricted CRM prefix. If a read is refused, record the exact error and mark that part `not_established`.
- **Account numbers and values are never printed, committed or sent.** Counts, dates, CUSIPs and reason codes only. A CUSIP appears only in a CSV column named exactly `cusip` or in the order's own text. Do not run `aws sts get-caller-identity` (its output carries the AWS account id). Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/` in any way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line. The additions file carries account keys: report whether the scan flags it (it will unless the keys are tokens); do NOT edit the test; the issuer rules the exemption.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull); no Black Diamond API call.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W164-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round83.md</decomp_doc> (round 83), cell `CB-ce-1`.
<owned_cells>CB-ce-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB83ce1-AC1, CB83ce1-AC2, CB83ce1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~164/ADVI_COTBKF.TO-CB-ce-1.four-cusips-missing-from-the-set.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB83ce1-AC1,CB83ce1-AC2,CB83ce1-AC3` BEFORE the flip. Mechanical: CB83ce1-AC1, CB83ce1-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the additions and missing-by-cause CSVs as `declared_exclusions` only if the checker refuses them as file artifacts. You flip your own order `<status>` to `complete` in the commit that carries the proof instance.
</proof_of_spec>

**REPORT:** FIRST the four causes in one line each (CUSIP, cause, the count behind it). Then: per CUSIP the traded, held-by and in-set counts; the additions file's rows, sha256 and bytes; the generalization (traded, in the set, missing, by cause, fixed-income missing); the derivation check; every remote read made; the `FOUR-CUSIPS` and `ADDITIONS-FILE` lines; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the derivation is checked against the set before it is used; each cause is a measured class; the generalization covers every matched active account, not the four; BLIND: a security traded under a symbol that was later renamed, and a bond whose redemption is typed as a sale.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-83 analysis @01ed464473 (msg 7298), section 2 item 1, which takes this cell "as drafted" from msgs 7280 and 7287 (relaying `1.0.0_SA_CTO~DELL1` via `0.0.0_AB_MSTR~DELL2` msg 7285); pivot direction O4.
