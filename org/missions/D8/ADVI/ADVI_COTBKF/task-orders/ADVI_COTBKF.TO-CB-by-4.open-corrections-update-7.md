# TO ADVI_COTBKF.TO-CB-by-4.open-corrections-update-7 -- round 77 CB-by-4: the correction list brought current: two entries merged into one defect, an adjusted close used as a price

<to_id>ADVI_COTBKF.TO-CB-by-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~146</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-by-4` (`decompositions/ADVI_COTBKF_DECOMP.round77.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-by-1, CB-by-2, CB-by-3

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (seven entries, one struck, six revisions, a `tooling`
object); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` whole.

**Your item: change only what a record supports. This cell runs LAST: every record below is in the tree when you start; if one is
absent, that is the refusal clause.**

1. **Two entries become ONE** (section 3 item 4, quoted with its lines): "the trade-day entry and the holdings-on-an-adjusted-close
   entry are ONE defect, an adjusted close used as a price, and are merged, with the instrument that reaches it named." The merged
   entry has id `adjusted-close-used-as-price`, the eight keys every entry has, `state` `OPEN`, and a key `merged_from` listing the
   two ids it replaces (`dividend-adjusted-fund-series`, `trade-day-valuation`). NOTHING is dropped in the merge: both entries'
   `extent` objects are carried under labelled keys (`holdings` and `trade_days`), both evidence lists are concatenated in order,
   both unreconciled lists are concatenated with exact duplicates removed. Its `what` states the defect once, in the CTO's words
   (section 1 and section 2, quoted with their lines: the close the build did not replace is more than 20 percent off the price
   paid on 3,205 of 3,614 trades, on purchases and sales alike; "It is the close."; "A close at three quarters of the traded price
   is a LEVEL error."), and names the instrument that reaches it: the price paid on a trade (14,250 of 91,040 units; 61 of the 197
   funds left on the store; 238 of 270 series not classed by trades). `floor_series` and `ceiling_series` stay as they are.
2. **Into the merged entry, from this round's records** under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/`:
   `0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` (the store and key; the readers by class; the serving readers; how many serve from
   an affected close, with their owners and the row ids filed; what the census could not see) under a key `who_reads_the_closes`;
   `0.9.0_WK_ADVI_COTBKF~144/FAILING_FUNDS.json` (the 15: how many have an unadjusted close held, where; how many of those reproduce
   the price paid) under `failing_funds`; `0.9.0_WK_ADVI_COTBKF~145/LEVEL_ERROR.json` (the level error where it is served: readers
   sized, account-days, the share of value; or that none is served by a reader the census reached) under `level_error_where_served`.
   **AMENDMENT 1 (issuer, on CTO msg 6196):** and that cell's second record, `0.9.0_WK_ADVI_COTBKF~145/NO_SNAPSHOT_BRANCH.json` (the
   first snapshot date; the partitions before it, which branch built them and whether they still exist; whether the page can be
   asked for such a date; the failing funds held before; whether a served figure from an affected close was found, with its date
   range and the row id; the three readers not established and what would establish each) under a key `no_snapshot_branch`. This
   record too is in the tree when you start.
   **AMENDMENT 2 (issuer, on CTO msg 6213, 2026-10-12T00:44Z):** and the issuer's own record of the three reads the CTO ruled,
   `2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_77_THREE_READERS_READ.json` (the three readers the census left not established: two now
   established as serving nothing from the price store; the third does not name the store by code, and whether a portal page opens
   it for this firm is carried as needing a window) under a key `three_readers_read`. It replaces the "not established" standing of
   those three in what you write, with its own limits kept.
3. **`closes_when`** quotes section 4: the fund-basis addendum "is written after cell 1, because what must be corrected first
   depends on what is served", marked NOT YET WRITTEN.
4. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
5. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 77), saying which
   two ids were merged into which; rewrite `OPEN_CORRECTIONS.md` to match (six rows). No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB77by4-AC1" cell_refs="CB-by-4"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};ids=[x['id'] for x in c];m=[x for x in c if x['id']=='adjusted-close-used-as-price'];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d merged=%s old_ids_left=%d corrections=%d keys_complete=%s merged_from=%s carried=%s readers_key=%s evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),bool(m),sum(1 for i in ids if i in ('dividend-adjusted-fund-series','trade-day-valuation')),len(c),all(k<=set(x) for x in c),','.join(sorted(m[0].get('merged_from',[]))) if m else '',bool(m and 'holdings' in m[0]['extent'] and 'trade_days' in m[0]['extent']),bool(m and 'who_reads_the_closes' in m[0]['extent']),len(m[0]['evidence']) if m else 0,sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=7 record_absent=0 merged=True old_ids_left=0 corrections=6</expect></criterion>
`CB77by4-AC1` -- the list is at its seventh revision with six entries; the two old entries are gone and one merged entry stands in
their place, carrying both extents. The issuer reads the evidence and unreconciled counts against revision 6 (nothing dropped).

<expected_criteria>CB77by4-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W146-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round77.md</decomp_doc> (round 77), cell `CB-by-4`.
<owned_cells>CB-by-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB77by4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~146/ADVI_COTBKF.TO-CB-by-4.open-corrections-update-7.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB77by4-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the merged entry as written, with its first sentence and the two ids it replaces; that nothing was dropped: the evidence and unreconciled counts before and after; what was added from this round's three records; the rulings quoted with their lines; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until ALL three other cells drain; a merge can lose rows, so both extents are carried under labelled keys and the evidence and unreconciled counts are printed before and after; the old ids must be gone and the new entry must name them; no new value in the state field; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-77 analysis @1101e06fcd (msg 6154), section 3 item 4; `3.0.0_SA_CVO` round-76 grade file @d299fd357a.
