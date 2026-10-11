# TO ADVI_COTBKF.TO-CB-bx-5.open-corrections-update-6 -- round 76 CB-bx-5: the correction list brought current: the trade-day entry from a lead to confirmed on 12, size open

<to_id>ADVI_COTBKF.TO-CB-bx-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~142</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bx-5` (`decompositions/ADVI_COTBKF_DECOMP.round76.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bx-1, CB-bx-2, CB-bx-3, CB-bx-4

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (seven entries, one struck, five revisions, a `tooling`
object); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` whole.

**Your item: change only what a record supports. This cell runs LAST: every record below is in the tree when you start; if one is
absent, that is the refusal clause.**

1. **The trade-day entry (`trade-day-valuation`) moves from a lead to CONFIRMED ON 12, size open** (section 3 item 5): its key `lead`
   becomes false; its `what` begins "CONFIRMED ON 12, size open:" and states, in the CTO's words quoted with their lines (section
   1): "The served table marks those purchases at about three quarters of the cash paid, on the day they were made. That is no
   longer a lead. It rests on a fact the build's formula does not use." and the limits the same section lists. `state` stays `OPEN`.
   Into its `extent` and `evidence`, from this round's four records under
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/`: `0.9.0_WK_ADVI_COTBKF~138/PURCHASE_ROWS_OFF.json` (the 26 percent: counts per
   cause under both orders; `none_found`; the fit after the benign causes, for purchases and for sales);
   `0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json` (the denominators; the four bands; purchases and sales; the control on the substituted
   funds; the fund series not reached); `0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json` (the rule; the five classes over 270; the
   named funds as a COUNT and a pointer, not a copied list; the changes of class; the conflicts);
   `0.9.0_WK_ADVI_COTBKF~141/TRADE_DAY_RETURN.json` (the trade term only: measured trade account-days over 10 basis points in three
   bands, split by price fit; the accounts and funds as counts; what the blank days would hold, apart). `size_in_returns` says what
   is now measured and what is not: the trade term on measured days; NOT the carried holding; NOT the blank days.
2. **The fund-basis entry (`dividend-adjusted-fund-series`):** the instrument changes (section 2, quoted with its lines): the
   reinvestment price reaches 34 of 270 fund series; the price paid on a trade reaches every fund ever bought or sold. Add the
   price-paid instrument as a fourth labelled instrument with its counts, and the shape of the rule the CTO states in section 4,
   quoted and marked NOT YET WRITTEN ("It is not written before the 26 percent has causes").
3. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
4. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 76); rewrite
   `OPEN_CORRECTIONS.md` to match. No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB76bx5-AC1" cell_refs="CB-bx-5"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};t=[x for x in c if x['id']=='trade-day-valuation'][0];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d trade_day_confirmed_on_12=%s lead=%s state=%s corrections=%d keys_complete=%s trade_day_evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),t['what'].startswith('CONFIRMED ON 12, size open'),t.get('lead'),t['state'],len(c),all(k<=set(x) for x in c),len(t['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=6 record_absent=0 trade_day_confirmed_on_12=True lead=False state=OPEN</expect></criterion>
`CB76bx5-AC1` -- the list is at its sixth revision, carries no stale string, and its trade-day entry reads CONFIRMED ON 12 with the
size open and is no longer flagged a lead. The issuer reads each changed entry against its record.

<expected_criteria>CB76bx5-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W142-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round76.md</decomp_doc> (round 76), cell `CB-bx-5`.
<owned_cells>CB-bx-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB76bx5-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~142/ADVI_COTBKF.TO-CB-bx-5.open-corrections-update-6.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB76bx5-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the trade-day entry as written, with its first sentence; every other entry changed and what changed in it, with the record and the number printed from it; the rulings quoted with their lines; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until ALL four other cells drain; the entry's standing is carried by its first words and by the lead key the check reads, with no new value in the state field; the size is written as what is measured (the trade term on measured days) and what is not; the rule's shape is quoted and marked not yet written; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-76 analysis @8ae9f87cf2 (msg 5996), section 3 item 5; `3.0.0_SA_CVO` round-75 grade file @0e95fc9cca.
