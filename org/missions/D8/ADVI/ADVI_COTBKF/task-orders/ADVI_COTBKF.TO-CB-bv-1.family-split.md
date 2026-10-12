# TO ADVI_COTBKF.TO-CB-bv-1.family-split -- round 74 CB-bv-1: the date convention by fund family, rule first; stated per family or as not established

<to_id>ADVI_COTBKF.TO-CB-bv-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~127</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bv-1` (`decompositions/ADVI_COTBKF_DECOMP.round74.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` section 2 item 2 and section 3 item 1; row ADVI_COTBKF-D2-S125 in the channel (the reviewer's: of the 15
decided funds whose reinvestment row matches the cached close of the trading day BEFORE, 12 are one family; of the 17 that match the
same day, 1 is; "The family is read from the first two words of the custodian's own security description"; "A count on 32 funds, with
exceptions each way: a lead, not a result"); the round-73 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/THREE_DATE_READ.json`, its `.csv` and `.md` (101 funds, 944 cells; its rule:
equal within 0.5 percent, a fund decided on 5 or more cells with a share of 0.60 and a margin of 0.20).

**The ruling that bounds this cell.** "The date convention belongs to the VALIDATION, not to the price." The family split is tested so
a reinvestment row is set beside the right day's close when a series is being shown unadjusted. No family rule enters the build's
pricing, and you propose none.

**Your item.**

1. **Reproduce the row first:** the 32 decided funds of round 73 (17 same, 15 before), each with its family as the first two words of
   the custodian's security description in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/`: 12 of 15 and 1 of 17 in the one family. If you do not get those, say
   what you get and why.
2. **THE RULE FIRST.** Before any count beyond step 1, write to a file in your scratch (with a clock timestamp) and copy into the
   record: (a) how a fund's family is read (the description field, how many words, how variants of one family's name are folded);
   (b) what makes a family's convention `same`, `before` or `not established` (a minimum of decided funds in the family; the share of
   them that must agree); (c) what makes the split as a whole `by family` (how many families must each have a convention, and how
   many funds may sit against their family) or `not established`; (d) how the undecided funds are used: the per-fund rule of round
   73 left 69 undecided for too few cells, so state a POOLED test per family (the family's cells taken together: equal on the same
   day against equal on the day before, on cells where only one of the two matches) and its threshold. Then keep it.
3. **Per family, over the whole population (101):** funds, decided funds by winner, undecided; the pooled cells (same only, before
   only, both, neither); the family's convention under your rule. Every fund that sits against its family, by ticker.
4. **Out of sample inside the family:** for the one large day-before family, does the convention the 12 decided funds show hold on
   that family's UNDECIDED funds, by the pooled cells of those funds alone? Counts.
5. **Other splits that could explain the same thing,** stated before they are run in the same rule file and then counted: share
   class (the last letter pattern of the ticker), kind (open or closed end), substituted or left on the store, the period of the
   rows. For each: does it separate same from before as well as family does? One line each.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~127/FAMILY_SPLIT.json`, a `.csv` of the 101 funds (columns: cusip, ticker, family, cells, equal_same, equal_before, winner,
   against_family; CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `reproduced_row`
   (`{"before_in_family", "before_total", "same_in_family", "same_total"}`), `rule` (`{"text", "written_at"}`), `funds`, `families` (a
   list of `{"family", "funds", "decided_same", "decided_before", "undecided", "pooled", "convention"}`), `reading` (`by_family` or
   `not_established`), `against_family` (a list), `held_out_in_family`, `other_splits`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB74bv1-AC1" cell_refs="CB-bv-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~127/FAMILY_SPLIT.json',encoding='utf-8'));r=d['reproduced_row'];f=d['families'];print('FAMILY-SPLIT rule_written=%s row=%d/%d+%d/%d funds=%d families=%d family_funds=%d with_a_convention=%d reading=%s against_family=%d'%(bool(d['rule']['written_at']),r['before_in_family'],r['before_total'],r['same_in_family'],r['same_total'],d['funds'],len(f),sum(x['funds'] for x in f),sum(1 for x in f if x['convention'] in ('same','before')),d['reading'],len(d['against_family'])))"</invocation><expect>FAMILY-SPLIT rule_written=True</expect></criterion>
`CB74bv1-AC1` -- the rule was written first; the reviewer's row is reproduced; every fund of the population sits in one family
(`family_funds` equals `funds`); the issuer reads the reading and the count against family.

<criterion id="CB74bv1-AC2" cell_refs="CB-bv-1" judgment="true"/>
`CB74bv1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule precedes the counts and was kept; `not
established` is used where the funds are too few; the family's convention is tested on funds that did not suggest it; the other
splits were named before they were run; no pricing rule is proposed.

<expected_criteria>CB74bv1-AC1,CB74bv1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- A fund family's name, a ticker and a fund's price are not client data. An account id or an account's amounts are, and are never printed.
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
  `ADVI_COTBKF-D2-W127-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round74.md</decomp_doc> (round 74), cell `CB-bv-1`.
<owned_cells>CB-bv-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB74bv1-AC1, CB74bv1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~127/ADVI_COTBKF.TO-CB-bv-1.family-split.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB74bv1-AC1,CB74bv1-AC2` BEFORE the flip. Mechanical: CB74bv1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the reviewer's row as reproduced; the rule as written before the counts, with its timestamp; each family with its funds, decided and pooled counts and its convention; every fund against its family, by ticker; the held-out test inside the large family; each other split in one line; the reading; the `FAMILY-SPLIT` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the reviewer's row is the positive control; the rule precedes the counts; the family's convention is tested on its undecided funds, which did not suggest it; the rival splits are named before they are run; `not established` is a legal reading; no pricing rule is proposed, per the ruling; BLIND: a family read from a description field, with no sponsor master to check it against.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-74 analysis @42390144c0 (msg 5758), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
