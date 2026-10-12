# TO ADVI_COTBKF.TO-CB-bz-3.open-corrections-update-8 -- round 78 CB-bz-3: the correction list brought current: the ruling in force on row D2-S131, the causes to completion, the store's field

<to_id>ADVI_COTBKF.TO-CB-bz-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~150</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bz-3` (`decompositions/ADVI_COTBKF_DECOMP.round78.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bz-1, CB-bz-2

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, seven revisions, a `tooling`
object); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_78_20261012.md` whole; row ADVI_COTBKF-D2-S131 in the channel.

**Your item: change only what a record supports. This cell runs LAST: both records below are in the tree when you start; if one is
absent, that is the refusal clause.**

1. **The ruling in force, at the top of the merged entry (`adjusted-close-used-as-price`),** under a key `in_force`, quoted with its
   lines from section 2: row D2-S131 accepted, BLOCKING and INERT; "neither act is cut, by any lane, until the fund basis is fixed
   and proven. No rebuild of a holdings partition dated before 2026-06-08 for this firm; no consumer is attached to the minted
   table. This is a ruling on what is cut, read by the issuer; nothing is built to enforce it." Its `state` stays `OPEN`. Add the
   same two prohibitions to the list's top-level `not_established`-adjacent notes ONLY as a pointer to the entry; do not restate.
2. **What round 77 established, as the analysis words it** (section 1, quoted): "No served figure carries the error today", with the
   limits kept beside it, and the by-year shape (the reviewer's medians, 0.46 in 2020 rising to 1.00 in 2026), as an evidence row.
3. **This round's two records, into the merged entry's `extent`:**
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~148/PRICE_PAID_CAUSES.json` under `causes_to_completion` (the
   test and its constants; the held-out fit against chance; the reading; what is still off, by cause under both orders, and
   `none_found`; the fit once the charge is set aside, or the plain shares if the reading is not `holds`); and
   `.../0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json` under `store_field` (whether the store holds an unadjusted close; the
   field; coverage of the dates the back-fill reads by the store and by the cache, with the denominators; the fifteenth fund and
   what it lacks). Replace the round-76 unreconciled item about the 124 none-found rows and the post hoc reading with what the test
   now shows, in its words; where it does not settle it, the item stays and says so.
4. **`closes_when`:** the addendum as section 3 names it, quoted and marked NOT YET WRITTEN: it "names the price basis per fund
   class, makes the minted table carry its basis in a field a reader can reject on, and states the proof".
5. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
6. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 78); rewrite
   `OPEN_CORRECTIONS.md` to match, the ruling in force stated in the merged row. No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB78bz3-AC1" cell_refs="CB-bz-3"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};m=[x for x in c if x['id']=='adjusted-close-used-as-price'][0];e=m['extent'];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d in_force=%s causes=%s store_field=%s state=%s corrections=%d keys_complete=%s evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),'in_force' in m,'causes_to_completion' in e,'store_field' in e,m['state'],len(c),all(k<=set(x) for x in c),len(m['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=8 record_absent=0 in_force=True causes=True store_field=True state=OPEN corrections=6</expect></criterion>
`CB78bz3-AC1` -- the list is at its eighth revision with six entries; the merged entry carries the ruling in force and this round's
two records. The issuer reads each change against its record.

<expected_criteria>CB78bz3-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W150-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round78.md</decomp_doc> (round 78), cell `CB-bz-3`.
<owned_cells>CB-bz-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB78bz3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~150/ADVI_COTBKF.TO-CB-bz-3.open-corrections-update-8.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB78bz3-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the ruling in force as written, with its lines; every entry changed and what changed in it, with the record and the number printed from it; what the test now shows about the 124 rows; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until both other cells drain; the ruling in force is quoted with its lines and not paraphrased, since it tells a seat what is not to be cut; the post hoc item is replaced only by what the test shows; no new value in the state field; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-78 analysis @e5d2fc8e59 (msg 6229), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v46 @d389aa8f85.
