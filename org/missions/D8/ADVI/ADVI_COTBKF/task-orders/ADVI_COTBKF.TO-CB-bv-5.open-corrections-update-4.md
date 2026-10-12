# TO ADVI_COTBKF.TO-CB-bv-5.open-corrections-update-4 -- round 74 CB-bv-5: the correction list brought current: the validation rule, the first return number, the family reading, the fetch

<to_id>ADVI_COTBKF.TO-CB-bv-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~131</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bv-5` (`decompositions/ADVI_COTBKF_DECOMP.round74.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bv-1, CB-bv-2, CB-bv-3, CB-bv-4

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, three revisions, a `tooling`
object); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` whole.

**Your item: change only what a record supports. This cell runs LAST: every record below is in the tree when you start; if one is
absent, that is the refusal clause.**

1. **The fund-basis entry (`dividend-adjusted-fund-series`):**
   - the ruling, quoted with its lines (section 2 item 2): "the date convention belongs to the VALIDATION, not to the price. The price
     a fund is valued at on a day is its unadjusted close for THAT day";
   - the validation rule and its three counts with the denominator, from
     `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.json`, and how many validated funds
     the adjusted close cannot be told from;
   - **the first return number**, in `extent` under the key `return_change`, from `.../0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`:
     the validated funds, the account-days compared, the changed account-days in the three bands, measured-to-blank and
     blank-to-measured, and the words "for the validated funds only; not the size of the whole defect". The ruling of section 2
     item 3 beside it, quoted: the three reaches "are not added, compared or quoted as a size". Mark the three reaches in `extent`
     as holdings counts, not return errors; do not delete them;
   - the family split's reading from `.../0.9.0_WK_ADVI_COTBKF~127/FAMILY_SPLIT.json` (by family, or not established), as an evidence
     row, with the sentence that no family rule enters the build's pricing;
   - the fetch from `.../0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.json`: asked, returned, empty; the readings, each NOT
     custodian-validated; the 94 unheld not fetched.
   - `floor_series` stays 19 and `ceiling_series` stays `NOT_MEASURED` unless the analysis moves them (it does not: section 1 says
     "19 fund series (21 by the validated-close instrument)"; quote that).
2. **`tooling.remint_mode`:** the CTO's line (section 2 item 4): the mode's rows are closed, and whether the real bucket honours the
   write condition is a line of the re-serve's pair: one conditional write against a scratch key in that bucket, by the applier,
   before the first real write. Record it as owed by the pair, not as done.
3. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
4. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 74); rewrite
   `OPEN_CORRECTIONS.md` to match. No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB74bv5-AC1" cell_refs="CB-bv-5"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};e=[x for x in c if 'dividend' in x['id']][0];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d return_change=%s floor=%s ceiling=%s corrections=%d keys_complete=%s dividend_evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),'return_change' in e['extent'],e['extent']['floor_series'],e['extent']['ceiling_series'],len(c),all(k<=set(x) for x in c),len(e['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=4 record_absent=0 return_change=True</expect></criterion>
`CB74bv5-AC1` -- the list is at its fourth revision, carries no stale string, and its fund-basis entry holds the first return
number. The issuer reads each changed entry against its record.

<expected_criteria>CB74bv5-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W131-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round74.md</decomp_doc> (round 74), cell `CB-bv-5`.
<owned_cells>CB-bv-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB74bv5-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~131/ADVI_COTBKF.TO-CB-bv-5.open-corrections-update-4.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB74bv5-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** every entry changed and what changed in it, with the record and the number printed from it; the return number as written and its caveat; the rulings quoted with their lines; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until ALL four other cells drain; the check counts the stale string; the return number is written with its caveat (validated funds only) and the three reaches are marked holdings counts, per the ruling; the bucket's handling of the write condition is recorded as owed by the pair, not done; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-74 analysis @42390144c0 (msg 5758), section 3 item 5; `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
