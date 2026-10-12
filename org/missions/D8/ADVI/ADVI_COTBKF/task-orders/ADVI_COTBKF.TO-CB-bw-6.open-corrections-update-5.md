# TO ADVI_COTBKF.TO-CB-bw-6.open-corrections-update-5 -- round 75 CB-bw-6: the correction list brought current: the trade-day mechanism as its own entry, marked a lead

<to_id>ADVI_COTBKF.TO-CB-bw-6</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~137</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-6` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bw-1, CB-bw-2, CB-bw-3, CB-bw-4, CB-bw-5

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, four revisions, a `tooling`
object); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` whole.

**Your item: change only what a record supports. This cell runs LAST: every record below is in the tree when you start; if one is
absent, that is the refusal clause.**

1. **A NEW entry, its own, marked a LEAD:** id `trade-day-valuation`, with the eight keys every entry has, `state` `OPEN`, and an
   extra key `lead` set to true. Its `what` begins "LEAD, not a finding:" and states the mechanism in the CTO's words, quoted with
   their lines (section 2 item 2): on the day shares are bought, the build values the new shares at a close that is too low against
   the cash that paid for them, and the difference lands in that day's return; "a different mechanism from a holding carried at an
   adjusted close, and a larger one". Its `extent` and `evidence` come from
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json` (the trade days; confirmed, refuted,
   undecided; the reading under its own rule; the share of the total change on trade days; which close makes the shares worth the
   cash) and `.../0.9.0_WK_ADVI_COTBKF~133/NO_TRADE_ROW_CAUSES.json` (the 74: counts per cause, `none_found`). If cell 1's reading is
   `refuted` or `not_established`, the entry says so in its first sentence and stays a lead. `owner` 1.0.0_SA_CTO~DELL2;
   `closes_when`: the fund-basis rule as a PRD addendum that says how a purchase is valued on its day (section 4, quoted).
2. **The fund-basis entry (`dividend-adjusted-fund-series`):** the return number's reviewer count beside the worker's (1,577 at a
   floor of 1e-12; 1,575 at 1e-9; the same bands), with the nine accounts from `.../0.9.0_WK_ADVI_COTBKF~136/NINE_ACCOUNTS.json`
   (counts and concentration only); the refuting control from `.../0.9.0_WK_ADVI_COTBKF~134/REFUTING_CONTROL.json` (how many of the 33
   adjusted series the rule refuted, and whether the arm is shown able to refute); the ruling of section 2 item 3 quoted (it "changes
   what is being sized"); the open question on the 882 basis points and the direction of the changes resolved, or left open, by what
   cells 1 and 2 show, in their words. Row D2-S125 closed (section 2 item 5).
3. **VBTLX** from `.../0.9.0_WK_ADVI_COTBKF~135/VBTLX_BY_DATE.json`: the cause, or `not_named`; what rests on its off dates; and that
   it is excluded from every count until the cause has a name (section 2 item 6, quoted). Place it where the record's cause puts it:
   under `mis-scaled-price-series` if the build's close is the wrong side, as an evidence row and an `unreconciled` item; otherwise
   as an `unreconciled` item on the fund-basis entry.
4. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
5. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 75); rewrite
   `OPEN_CORRECTIONS.md` to match, the new entry in its own row marked LEAD. No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id, no
account label's values beyond the counts the record holds; a security by its ticker.

### ACCEPTANCE

<criterion id="CB75bw6-AC1" cell_refs="CB-bw-6"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};t=[x for x in c if x['id']=='trade-day-valuation'];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d trade_day_entry=%s lead=%s corrections=%d keys_complete=%s trade_day_evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),bool(t),bool(t and t[0].get('lead') is True and t[0]['what'].startswith('LEAD')),len(c),all(k<=set(x) for x in c),len(t[0]['evidence']) if t else 0,sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=5 record_absent=0 trade_day_entry=True lead=True corrections=7</expect></criterion>
`CB75bw6-AC1` -- the list is at its fifth revision, carries no stale string, and holds the trade-day mechanism as a seventh entry of
its own, marked a lead. The issuer reads each changed entry against its record.

<expected_criteria>CB75bw6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the deliverables folder, where the list sits at its top level, and your own NEW channel row)
  and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call.
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
  `ADVI_COTBKF-D2-W137-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-6`.
<owned_cells>CB-bw-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw6-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~137/ADVI_COTBKF.TO-CB-bw-6.open-corrections-update-5.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw6-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the new entry as written, with its first sentence; every other entry changed and what changed in it, with the record and the number printed from it; the rulings quoted with their lines; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until ALL five other cells drain; the new entry is marked a lead by a key the check reads and by its first words, and stays a lead whatever cell 1 reads; no new value is added to the `state` field; the check counts the stale string; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 6; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
