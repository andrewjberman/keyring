# TO ADVI_COTBKF.TO-CB-by-3.level-error -- round 77 CB-by-3: the level error sized where the census found a served reader, and only there: account-days and the share of value, as counts and proportions

<to_id>ADVI_COTBKF.TO-CB-by-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~145</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-by-3` (`decompositions/ADVI_COTBKF_DECOMP.round77.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-by-1

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT, made ONLY where cell 1 found a served reader. You change no code. Nothing is fetched, served or applied.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` section 2 and section 3 item 3 ("The level error sized where cell 1 finds a served reader, and only there:
account-days and the share of value affected, counts and proportions."); this round's census
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` and its `.md` (in the tree when you start;
if absent, that is the refusal clause): the readers classed, and for each serving reader whether its figure uses the store's close.

**Your item.**

1. **If the census found NO reader serving a figure from an affected close:** say so, with the census's own count and what it could
   not see; size nothing; the record's `sized` is an empty list and its headline says the level error is not served by any reader
   the census could reach. That is a complete result.
2. **Otherwise, for EACH such reader and for no other:** the population it serves for THIS project's firm (accounts as a COUNT,
   account-days, the date range), and within it the account-days on which one of the 15 failing funds is held at a value built from
   the affected close; and the SHARE OF VALUE affected: on those account-days, the failing funds' value as a share of the account's
   served value, as a distribution (median, the share of account-days above 5, 25 and 50 percent). And the level itself: per fund,
   the served close over the unadjusted close where one is held (this round's `FAILING_FUNDS.json`, if it has landed; else the
   round-76 median ratio), so the understatement is stated as a proportion and never as money.
3. **What kind of figure:** a value, a weight or a return. For a value or a weight the error is a level, on every day; for a return
   say which days it enters (the round-75 and round-76 records). Do not restate the return work.
4. **Reads only,** of the reader's own served artifact for this firm; one firm; no other firm's data opened. No account id, no
   account's value.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/LEVEL_ERROR.json` and a short `.md`. Top-level keys, exactly: `served_readers_from_cell_1`, `sized` (a list of `{"reader",
   "owner", "figure", "accounts", "account_days", "account_days_holding_a_failing_fund", "share_of_value", "level_by_fund"}`),
   `unsized` (a list, with why), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB77by3-AC1" cell_refs="CB-by-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/LEVEL_ERROR.json',encoding='utf-8'));c=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json',encoding='utf-8'));print('LEVEL-ERROR census_serving_from_an_affected_close=%d served_readers_from_cell_1=%d sized=%d unsized=%d sum=%d account_days_holding_a_failing_fund=%d'%(c['serving_from_an_affected_close'],d['served_readers_from_cell_1'],len(d['sized']),len(d['unsized']),len(d['sized'])+len(d['unsized']),sum(x['account_days_holding_a_failing_fund'] for x in d['sized'])))"</invocation><expect>LEVEL-ERROR census_serving_from_an_affected_close=</expect></criterion>
`CB77by3-AC1` -- the readers sized or left unsized are exactly the census's readers serving from an affected close (`sum` and
`served_readers_from_cell_1` equal the census's count); the issuer reads the account-days.

<criterion id="CB77by3-AC2" cell_refs="CB-by-3" judgment="true"/>
`CB77by3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: only readers the census found serving from an
affected close are sized, and an empty result is reported as one; the size is in account-days and proportions, never money; reads
only, of this firm's artifact; no account id or value appears.

<expected_criteria>CB77by3-AC1,CB77by3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READS ONLY**, of the served artifact of a reader the census named, for THIS project's firm. No write, no delete, no serve.
- **Another firm's data is never opened.** No account id, no account's value: counts and proportions only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W145-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round77.md</decomp_doc> (round 77), cell `CB-by-3`.
<owned_cells>CB-by-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB77by3-AC1, CB77by3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/ADVI_COTBKF.TO-CB-by-3.level-error.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB77by3-AC1,CB77by3-AC2` BEFORE the flip. Mechanical: CB77by3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the census's count of readers serving from an affected close and that the readers sized are exactly those; for each: the figure, the population as counts, the account-days holding a failing fund, the share of value as a distribution, the level by fund as a proportion; or the plain statement that no such reader was found and nothing was sized; every reader left unsized and why; the headline; the `LEVEL-ERROR` line; the account-id scan's DENOMINATOR line; a statement that only this firm's artifact was read and nothing was written; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a measurement over a served artifact, read only.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: reads only of this firm's served artifact under the existing role; no write, delete or serve.
comp-adversary: RUN -- held until the census drains; the readers sized must be exactly the census's, and the check prints both counts; an empty result is a complete result and is reported as one; the size is account-days and proportions, never money; BLIND: a reader the census could not see.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-77 analysis @1101e06fcd (msg 6154), section 3 item 3; `3.0.0_SA_CVO` round-76 grade file @d299fd357a.
