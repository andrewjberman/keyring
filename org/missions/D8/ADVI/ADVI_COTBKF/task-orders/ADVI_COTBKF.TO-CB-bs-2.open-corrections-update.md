# TO ADVI_COTBKF.TO-CB-bs-2.open-corrections-update -- round 71 CB-bs-2: the correction list brought up to the records: the 2022 factor, 46 against 43, the dividend-adjusted series, the late-receipt rule struck

<to_id>ADVI_COTBKF.TO-CB-bs-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~117</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bs-2` (`decompositions/ADVI_COTBKF_DECOMP.round71.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bs-1

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` beside it (six entries, compiled in round 70 BEFORE that
round's other records landed); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_71_20261011.md` whole; `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` from the heading `## ADDENDUM v0.7` to the end (a later addendum on the
2022 factor may have landed: read whatever is there); and the records named below.

**Your item: bring the list up to the records, changing only what a record supports.**

1. **The 2022 factor and its extent.** From round 70's evidence record
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~112/SPINOFF_2022_EVIDENCE.json` and its `.md`: the reading
   (APPLY), the pairs on each side of the event, the reach (dates, priced holding account-days, measured account-days, the days
   where the price level enters the return), and what is not computed (the returns that would move). The entry's state follows the
   PRD: if an addendum applying the factor has landed, quote it with its line; if not, the entry says the reading is APPLY and the
   addendum is owed by `1.0.0_SA_CTO~DELL2`.
2. **46 day files by bytes against 43 by real change.** The CTO's round-71 analysis, section 2 item 5, records the reviewer's
   reconciliation: 47 rows differ in bytes over 46 dates; 44 carry a real change; 3 are floating-point residue on a value of zero.
   Find the reviewer's own record of it (`org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v41.md`, and the
   grade file it cites) and row ADVI_COTBKF-D2-W114-S1; quote the numbers from the record, not from the analysis. Move the
   withholding entry's flow counts from `unreconciled` to its extent, stating both numbers and what each counts; anything about the
   withholding days that is STILL two numbers stays under `unreconciled`.
3. **The dividend-adjusted series.** From this round's record
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/DIVIDEND_ADJUSTED_SERIES.json`: a NEW entry, with what was
   tested, what read adjusted, what was not tested, and the reach. If that record is absent, that is the refusal clause: this cell
   depends on it.
4. **The mis-scaled series entry** takes round 70's widened numbers
   (`.../0.9.0_WK_ADVI_COTBKF~113/CLOSE_VS_TRADE_SCAN_WIDE.json`): 8 series, with 334 too few, 44 thin ones off and 1,700 with no close
   beside it, and the 974,014 account-days resting on the 1,700. If the dividend-adjusted entry and this one count some of the same
   series, say so under `unreconciled`.
5. **The late-receipt rule is STRUCK.** The CTO withdrew it (round-71 analysis section 2 item 3; msg 5458). Remove it from
   `corrections` and record it under a new top-level `struck` list: `{"id", "struck_by", "why", "what_stands"}`, quoting the analysis:
   what stands is the ruling that a receipt arriving after an account's assets left is neither a return nor a contribution; how such
   a day is recognised is open, and no day is blanked on it. The out-of-sample numbers come from
   `.../0.9.0_WK_ADVI_COTBKF~114/RESIDUAL_RECEIPT_OUT_OF_SAMPLE.json`.
6. **Every other entry** is re-read against its records; change nothing a record does not support. Keep each entry's eight keys.
   Update `as_of`. Add a top-level `revisions` list with one item for this update: `{"round": 71, "by", "changed": [...]}`.
   Rewrite `OPEN_CORRECTIONS.md` to match.

**Rules.** A number you cannot find in a record is `NOT_MEASURED`. Print each number from its record before you write it. Where two
records still disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; refer to a
security by its ticker, not its CUSIP.

### ACCEPTANCE

<criterion id="CB71bs2-AC1" cell_refs="CB-bs-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json',encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};ids=[x['id'] for x in c];print('OPEN-CORRECTIONS-RECORD corrections=%d keys_complete=%s struck=%s late_receipt_in_list=%s dividend_adjusted_in_list=%s revisions=%d unreconciled=%d'%(len(c),all(k<=set(x) for x in c),','.join(x['id'] for x in d['struck']),any('receipt' in i for i in ids),any('dividend' in i for i in ids),len(d['revisions']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD corrections=</expect></criterion>
`CB71bs2-AC1` -- the list carries its entries with their eight keys, the struck rule under `struck`, the dividend-adjusted entry, and
one revision. The issuer reads `late_receipt_in_list` (False) and `dividend_adjusted_in_list` (True) and each changed entry against
its record.

<expected_criteria>CB71bs2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the deliverables folder, where the list sits at its top level, and your own NEW channel row)
  and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call
  (no Yahoo, no Bloomberg): the Yahoo cache on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price or
  per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W117-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round71.md</decomp_doc> (round 71), cell `CB-bs-2`.
<owned_cells>CB-bs-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB71bs2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~117/ADVI_COTBKF.TO-CB-bs-2.open-corrections-update.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB71bs2-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** every entry changed and what changed in it, with the record and the number printed from it; the struck entry and what stands; the new entry; what is still unreconciled; every number written as NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the reconciliation is quoted from the reviewer's own record, not from the analysis that reports it; a struck rule moves to a named list with what still stands, it does not vanish; the cell is held until the dividend-adjustment record exists; BLIND: a correction recorded only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-71 analysis @efaa09a585 (msg 5458), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v41 @76875db91b.
