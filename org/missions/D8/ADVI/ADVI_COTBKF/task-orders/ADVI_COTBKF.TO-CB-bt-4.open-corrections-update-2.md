# TO ADVI_COTBKF.TO-CB-bt-4.open-corrections-update-2 -- round 72 CB-bt-4: the correction list updated: the dividend-adjusted series with the three counts; the fund-basis ruling; the re-mint mode's state

<to_id>ADVI_COTBKF.TO-CB-bt-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~122</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bt-4` (`decompositions/ADVI_COTBKF_DECOMP.round72.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bt-1

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, one revision); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_72_20261011.md` whole
(section 2 item 1 is a RULING: the basis for a fund series is the unadjusted value the fund traded at on the day, and a
dividend-adjusted close is a defect of the store, not a method); and this round's records.

**Your item: change only what a record supports.**

1. **The dividend-adjusted entry takes the three counts** of `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/REINVESTMENT_PRICE_CHECK.json`:
   confirmed adjusted, confirmed not, nothing to test on, with the fund-series total; the re-derived reach beside round 71's (both
   numbers, labelled by instrument); the disagreements with round 71 by count; and the ruling quoted with the analysis's line. Its
   `what` no longer says "graded: pending": say what was graded and by which record (the reviewer's grade is cited in
   `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v42.md`). If the round-72 record is absent, that is
   the refusal clause: this cell depends on it.
2. **Where a corrected series would come from**, as an evidence row on the same entry, from
   `.../0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json` IF it has landed: the source that reproduces the custodian's price on the
   nine (or `NONE`), and the coverage beyond the nine. If that record is not in the tree when you run, write
   `NOT_MEASURED (record absent at the time of this update)` and say so in your report: do not wait for it.
3. **The re-mint mode**, as a top-level `tooling` object (it is not a correction to the served table): its state from
   `.../0.9.0_WK_ADVI_COTBKF~121/REMINT_REPAIR.json` if it has landed (repairs, points described and not), else from round 71's
   `.../0.9.0_WK_ADVI_COTBKF~118/REMINT_FAILURE_PATHS.json` (18 points, 10 not described) with the note that the repair is in flight.
4. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); if one applying the factor has landed, quote it with its line; if not, the entry is unchanged.
5. **Every other entry** is re-read against its records and left alone unless a record moved. Update `as_of`; append one item to
   `revisions` (`{"round": 72, "by", "changed": [...]}`); rewrite `OPEN_CORRECTIONS.md` to match.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED`. Where two records
disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a security by its ticker.

### ACCEPTANCE

<criterion id="CB72bt4-AC1" cell_refs="CB-bt-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json',encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};e=[x for x in c if 'dividend' in x['id']][0];print('OPEN-CORRECTIONS-RECORD revisions=%d tooling=%s dividend_entry_pending=%s corrections=%d keys_complete=%s struck=%d dividend_evidence_rows=%d unreconciled=%d'%(len(d['revisions']),'tooling' in d,'pending' in e['what'],len(c),all(k<=set(x) for x in c),len(d['struck']),len(e['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=2 tooling=True dividend_entry_pending=False</expect></criterion>
`CB72bt4-AC1` -- the list carries its entries with their eight keys, two revisions, the tooling object, and a dividend-adjusted entry
that no longer says pending. The issuer reads each changed entry against its record.

<expected_criteria>CB72bt4-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W122-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round72.md</decomp_doc> (round 72), cell `CB-bt-4`.
<owned_cells>CB-bt-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB72bt4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~122/ADVI_COTBKF.TO-CB-bt-4.open-corrections-update-2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB72bt4-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** every entry changed and what changed in it, with the record and the number printed from it; which of this round's records had landed when you ran and which had not; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until the reinvestment-price record exists; a record of this round that has not landed is written NOT_MEASURED with that reason, never guessed; the re-mint mode is recorded as tooling, not as a correction to what is served; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-72 analysis @19911afdeb (msg 5561), section 4 item 4; `3.0.0_SA_CVO` REMEDIATION_v42 @fd300b1f97.
