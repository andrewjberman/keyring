# TO ADVI_COTBKF.TO-CB-bu-3.open-corrections-update-3 -- round 73 CB-bu-3: the correction list brought current: the two stale points; the fund-basis entry stating floor 19, ceiling unmeasured

<to_id>ADVI_COTBKF.TO-CB-bu-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~125</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bu-3` (`decompositions/ADVI_COTBKF_DECOMP.round73.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bu-1, CB-bu-2, CB-bu-4

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, two revisions, a `tooling` object);
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_73_20261011.md` whole. The list is STALE on two points, because revision 2 ran before two of round 72's records landed: it writes the
unadjusted-source read as `NOT_MEASURED (record absent at the time of this update)`, and it holds the re-mint mode at round 71's state.

**Your item: change only what a record supports. This cell runs LAST: every record below is in the tree when you start; if one is
absent, that is the refusal clause.**

1. **The fund-basis entry (`dividend-adjusted-fund-series`) states FLOOR AND CEILING** as the CTO rules them (section 1 and section 2
   item 1, quoted with their lines): the floor is 19 series, confirmed on the custodian's price; the ceiling is not measured; "Neither
   712 nor 3,187 measured account-days is the size." In `extent`: `floor_series` (19), `ceiling_series` (`NOT_MEASURED`), and the
   instruments kept, each labelled. Then this round's three-date read
   (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/THREE_DATE_READ.json`): the population, the convention it
   reads, the sizing counts, the reach stated as a floor with what is unsized, as a third labelled instrument. If its sizing reads more
   series adjusted than 19, do NOT move `floor_series`: the floor the CTO ruled is 19; put the new count beside it under
   `unreconciled`, for the CTO.
2. **The two stale points corrected:** the unadjusted-source read from
   `.../0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json` (45 of 93 on the row's own date; 88 of 93 one trading day earlier, a
   comparison not stated beforehand; coverage 76 with and 121 without); the re-mint mode in `tooling` from
   `.../0.9.0_WK_ADVI_COTBKF~121/REMINT_REPAIR.json` and this round's `.../0.9.0_WK_ADVI_COTBKF~124/REMINT_EDGES.json` (the repairs;
   whether a second writer is refused or only detected; the hard kill not described). No string `record absent` remains in the file.
3. **Two rulings recorded on the fund-basis entry, quoted with their lines:** the `other` class is NOT substituted by a rule change,
   and the nine are corrected as NAMED series, each on its own evidence (section 2 item 4); no basis rule rests on the day-before
   match yet (section 2 item 2).
4. **The 121 with no cached close:** the held count from `.../0.9.0_WK_ADVI_COTBKF~126/NO_CACHE_HELD_COUNT.json`, as an evidence row.
5. **The 2022-factor entry:** check the PRD for an addendum past v0.7 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the
   headings `## ADDENDUM v0`); quote it with its line if one landed; else unchanged.
6. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 73); rewrite
   `OPEN_CORRECTIONS.md` to match.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB73bu3-AC1" cell_refs="CB-bu-3"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};e=[x for x in c if 'dividend' in x['id']][0];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d floor=%s ceiling=%s corrections=%d keys_complete=%s tooling=%s dividend_evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),e['extent']['floor_series'],e['extent']['ceiling_series'],len(c),all(k<=set(x) for x in c),'tooling' in d,len(e['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=3 record_absent=0 floor=19 ceiling=NOT_MEASURED</expect></criterion>
`CB73bu3-AC1` -- the list is at its third revision, carries no stale `record absent` string, and its fund-basis entry states the
floor of 19 and an unmeasured ceiling. The issuer reads each changed entry against its record.

<expected_criteria>CB73bu3-AC1</expected_criteria>

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
  `ADVI_COTBKF-D2-W125-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round73.md</decomp_doc> (round 73), cell `CB-bu-3`.
<owned_cells>CB-bu-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB73bu3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~125/ADVI_COTBKF.TO-CB-bu-3.open-corrections-update-3.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB73bu3-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** every entry changed and what changed in it, with the record and the number printed from it; the floor and ceiling as written and the lines quoted; the two stale points as corrected; whether a PRD addendum past v0.7 exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until ALL three other cells drain, because revision 2 went stale by running early; the check counts the stale string and must read 0; the floor stays the CTO's 19 even if this round's sizing reads more, the new count going under unreconciled; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-73 analysis @35cf1a97dd (msg 5633), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v43 @bf44c1d294.
