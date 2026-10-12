# TO ADVI_COTBKF.TO-CB-ca-1.sechist-as-it-stands -- round 79 CB-ca-1: the securities history MDPF_SECHIST owns, as it stands: owner and fabric, whether it exists, its fields, whether it carries a basis, which of the 15 funds and held days it covers

<to_id>ADVI_COTBKF.TO-CB-ca-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~151</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ca-1` (`decompositions/ADVI_COTBKF_DECOMP.round79.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of the tree, of code and, only where the rule below allows, of one landed object. You change no code. Nothing is
built, fetched from a vendor, or written to any bucket.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the two sections headed `## ADDENDUM v0.8` (near line 292: it is also the round-79 analysis and holds the ENRICHMENT LIST) and `## ADDENDUM v0.9` (near line 343, the SIGNED text: it REPLACES item 2 of C-BASIS; v0.8's two tokens AS_TRADED and ADJUSTED are WITHDRAWN and are not used anywhere): CONTRACT C-BASIS items 3 and 4 ("The source is the one v0.4 ADDENDUM 2 already names: the securities
history that MDPF_SECHIST owns (C-SERIES), where 'prices land once per security'. It is NOT the price store, and it is NOT the cache
folder ... No second lander is built for this project." / "Until that history holds an as-traded close for a held fund day, that
day is UNPRICED") and ENRICHMENT LIST item 1, word for word: "MDPF_SECHIST as it stands: its owner and fabric, whether the
securities history exists, its fields, whether it carries a basis, which of the 15 funds and which held days it covers. Counts and
dates, the denominator printed. If it is another fabric's, the read is of the shared tree and its register row only, and the ask
goes through 0.0.0_AB_MSTR~DELL2." Then this PRD's `v0.4 ADDENDUM 2` (find its heading; read what it says of the history and of
C-SERIES), and the round-78 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json` (the price store has one price column and no basis; the upstream landing
`data/mdpf/scripts/demque/land_cot.py` declares one price column, `close` = `as_traded_close`).

**The 15 funds:** VEIRX, PCBIX, ABNFX, SGIIX, GFFFX, FOCPX, FCNTX, PRILX, BALCX, AGTHX, DISVX, DFLVX, NFFFX, MEIIX, VGHAX. Their held trading days in the build: 20,718 in all (per fund in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json`, key `by_fund`).

**Your item.**

1. **The project, from the tree:** where MDPF_SECHIST lives (`org/missions/D*/MDPF/MDPF_SECHIST/`), its register row, its OWNER
   (which seat and which FABRIC or box holds it), its stage, its PRD's statement of what the securities history is (its contract
   C-SERIES or whatever it is called there, quoted with file and line), and its task orders terminal and open as counts.
2. **THE FABRIC RULE, applied before any data is read.** If the project is held by THIS fabric (dell2), continue to step 3. **If it
   is another fabric's:** read the shared tree and its register row ONLY; make NO read of its buckets or landings; set
   `read_scope` to `tree_only`; and say in your report, first, that the ask must go through `0.0.0_AB_MSTR~DELL2` and what exactly
   should be asked (the fields, the basis, the coverage of the 15 funds). You do not message anyone.
3. **Whether the securities history EXISTS, and where (this fabric only):** the landing or table as the code and infra name it
   (file and line; you type no address of your own); whether it is built, scheduled and populated: from the code, the infra and the
   served graph first; one read of ONE object or one partition listing only if those do not answer, with the denominator printed.
4. **Its fields, and whether it carries a BASIS:** every column (from the writer's code and, where read, from the object's own
   schema). The signed text (ADDENDUM v0.9) says `as_traded_close` is "a COLUMN of the securities history's own writers" (69
   occurrences in 25 files under `data/mdpf/scripts/`, the CTO's census) and a VALUE of this project's per-point column `basis`
   (`data/assets/scripts/silver/commonwealth_daily_valuation.py:211`; the other value is `store`). So: does the history hold a
   column named `as_traded_close`; is the split scaling already applied in it, or is it the vendor's close alone (which the signed
   text says is split-adjusted and not dividend-adjusted); is there any other price column beside it; and is anything said per
   row about where the point came from? Quote the field names and the writer's lines. "Carries a basis" is true only if a field
   or the column's own definition in the writer states it.
5. **Coverage:** which of the 15 funds it holds (by which key: a ticker, a CUSIP, an id), and for each, how many of its held
   trading days carry a price there (count, first, last), with the denominator; and whether the price it holds equals the
   unadjusted close in the local vendor cache (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/`) on common dates (the share equal within 0.1 percent), so
   the reader knows whether "as-traded" there IS the traded close. If the history does not exist or holds none of the 15, say so
   in one sentence: under C-BASIS item 4 every such day is UNPRICED, and the count of such days is the finding.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~151/SECHIST_AS_IT_STANDS.json`, a `.csv` (columns: cusip, ticker, in_history, key_used, days_in_history, first, last,
   held_trading_days, held_trading_days_covered, share_equal_unadjusted; CUSIPs only in the column named exactly `cusip`) and a
   short `.md`. Top-level keys, exactly: `project` (`{"path", "owner", "fabric", "stage", "orders_terminal", "orders_open"}`),
   `read_scope` (`tree_only` or `tree_code_and_data`), `ask_through_mstr` (a string, or null), `history_exists` (true, false or
   `not_established`), `where` (`{"as_named_in_code", "scheduled", "populated"}`), `fields` (a list), `carries_a_basis` (true, false
   or `not_established`), `funds` (15), `funds_in_history`, `held_trading_days` (20718 unless your recount differs: say so),
   `held_trading_days_covered`, `unpriced_under_c_basis`, `by_fund` (a list of 15), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB79ca1-AC1" cell_refs="CB-ca-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~151/SECHIST_AS_IT_STANDS.json',encoding='utf-8'));p=d['project'];print('SECHIST-AS-IT-STANDS funds=%d listed=%d owner=%s fabric=%s read_scope=%s history_exists=%s fields=%d carries_a_basis=%s funds_in_history=%d held_trading_days=%d covered=%d unpriced_under_c_basis=%d sum=%d ask_through_mstr=%s'%(d['funds'],len(d['by_fund']),str(p['owner'])[:30],str(p['fabric'])[:20],d['read_scope'],d['history_exists'],len(d['fields']),d['carries_a_basis'],d['funds_in_history'],d['held_trading_days'],d['held_trading_days_covered'],d['unpriced_under_c_basis'],d['held_trading_days_covered']+d['unpriced_under_c_basis'],bool(d['ask_through_mstr'])))"</invocation><expect>SECHIST-AS-IT-STANDS funds=15 listed=15</expect></criterion>
`CB79ca1-AC1` -- the project's owner and fabric are read; the read scope is stated; the history's existence, fields and basis are
stated; every held trading day of the 15 funds is covered or unpriced (`sum` equals `held_trading_days`).

<criterion id="CB79ca1-AC2" cell_refs="CB-ca-1" judgment="true"/>
`CB79ca1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the fabric rule was applied before any data was
read, and another fabric's data was not read; the history's existence is read from what is built and populated, not from a
contract's wording; "carries a basis" is true only where a field states it; coverage is counted against the held trading days
with the denominator; `not_established` is used where the tree does not say.

<expected_criteria>CB79ca1-AC1,CB79ca1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: only if the project is THIS fabric's, and then read-only:** the served graph first; at most one object's schema and rows
  for the 15 funds, or one partition listing with its denominator. No write, no delete, no serve. If the project is another
  fabric's: NO read of its data at all.
- **Another firm's data is never opened.** No account id: this cell reads prices, dates, tickers and a project's records.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed. A
  read of the history is a read of an Opal artifact, not of a vendor.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W151-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round79.md</decomp_doc> (round 79), cell `CB-ca-1`.
<owned_cells>CB-ca-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB79ca1-AC1, CB79ca1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~151/ADVI_COTBKF.TO-CB-ca-1.sechist-as-it-stands.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB79ca1-AC1,CB79ca1-AC2` BEFORE the flip. Mechanical: CB79ca1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** FIRST: the project's owner and fabric, the read scope that followed, and, if it is another fabric's, exactly what must be asked through 0.0.0_AB_MSTR~DELL2. Then: its stage and orders; its own statement of what the history is, with file and line; whether the history exists, where, scheduled and populated; its fields and whether one states a basis; per fund, whether it is there, by which key, its days, and the held trading days covered; the days unpriced under C-BASIS; whether its price equals the unadjusted close; every remote read made, or that none was; the `SECHIST-AS-IT-STANDS` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of the tree, of code and of at most one landed object; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on this firm under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the fabric rule is applied before any data is read, and another fabric's data is not read at all; existence is read from what is built and populated, never from a contract's wording; a basis counts only where a field states it; coverage is counted against the held trading days with the denominator; BLIND: a history landed under a name the tree does not link to this project.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` PRD ADDENDUM v0.8 @fab39b5beb, which is also the round-79 analysis (msg 6275), its ENRICHMENT LIST item 1, with ADDENDUM v0.9 @95da777fbf (msg 6282), the SIGNED text; `3.0.0_SA_CVO` REMEDIATION_v47 @77527824fd.
