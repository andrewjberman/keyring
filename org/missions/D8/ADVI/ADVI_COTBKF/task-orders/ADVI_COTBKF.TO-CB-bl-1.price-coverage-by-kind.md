# TO ADVI_COTBKF.TO-CB-bl-1.price-coverage-by-kind -- round 64 CB-bl-1: price coverage measured by kind, and by where a price could already be held

<to_id>ADVI_COTBKF.TO-CB-bl-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~90</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bl-1` (`decompositions/ADVI_COTBKF_DECOMP.round64.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, shares, security identifiers (CUSIP, symbol), asset kinds, dates, file-and-line citations and reason codes only** in your record, report, commit messages and rows. Never an account id, never an account's position size, value, flow or return tied to an account. Aggregate before you print.

**This is a MEASUREMENT. Read `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_64_20261011.md` sections 1, 3 and 4 item 1, and rows ADVI_COTBKF-D2-S100 and D2-S101 in the channel, first.**

**Why.** Cottonwood's minted returns table is truthful and about 94% blank: an account-day holding ANY unpriced position is not
measured, and 15,993,996 of 21,102,041 position rows carry no value. Before any price source is added, the CTO wants to know, by
kind, whether the missing prices are already held somewhere this build does not read.

**Your item, for ONE date, 2026-05-06** (the latest full date: 10,090 position rows, 826 distinct securities, 459 unpriced; the
table tapers after 2026-06-01).

1. **By kind.** From `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet` (columns `date`, `cusip`, `value`, `price_source` only)
   and the silver transactions cache `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` (columns `Cusip`, `Asset_Type`, `Symbol` only): for
   each `Asset_Type`, the securities held, the securities unpriced, the position rows and the unpriced position rows. The four totals
   must read 826, 459, 10,090 and 6,122; if they do not, that is the refusal clause.
2. **(a) Does the custodian's own data carry a price or a market value this build does not read?** Find, from the code
   (`data/assets/scripts/silver/commonwealth_*.py`, the PRD's manifest rows S02 to S04 and S10 at
   `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` lines 160 to 175), what Cottonwood position or transaction data the
   custodian delivered and where its local or silver copy is. Read its SCHEMA and, for each unpriced kind, count how many of the
   unpriced securities have a non-null price or market value there on or near that date. Say which column, with file and line for
   where the build reads or ignores it.
3. **(b) Does a store Opal already keeps hold a price?** The stores this build reads are listed in
   `data/assets/scripts/silver/commonwealth_price_census.py` and `commonwealth_daily_valuation.py`. For each unpriced kind, count
   how many of the unpriced securities each of THOSE stores prices on that date (the local price caches under `C:/dev/ajb_workspace/.scratch/advi_cotbkf`). **You do
   NOT read any other firm's bucket or prefix**, and you add no source.
4. **The ruling already on record.** Quote, with its line numbers, what the PRD says the price source for each kind is (lines 210
   to 225), and say for each unpriced kind whether that ruled source has been pulled.
5. **Write the record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~90/PRICE_COVERAGE_BY_KIND.json` and a short `.md` beside it. Top-level keys, exactly: `date`, `securities`, `unpriced`,
   `position_rows`, `unpriced_position_rows`, `kinds` (a list of `{"kind", "securities", "unpriced", "position_rows",
   "unpriced_position_rows", "custodian_carries_price_for", "kept_store_prices", "ruled_source", "ruled_source_pulled"}`),
   `evidence` (a list of `{"claim", "file", "line"}`), `not_established` (a list of strings).

**S3.** A read-only `get` of ONE named object in a bucket this project already reads is allowed if a local copy does not exist; say
which object and why. No listing of another firm's prefix, no write.

### ACCEPTANCE

<criterion id="CB64bl1-AC1" cell_refs="CB-bl-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~90/PRICE_COVERAGE_BY_KIND.json',encoding='utf-8'));k=d['kinds'];print('PRICE-COVERAGE-RECORD date=%s securities=%d unpriced=%d position_rows=%d unpriced_position_rows=%d kinds=%d kind_unpriced_sum=%d evidence_rows=%d'%(d['date'],d['securities'],d['unpriced'],d['position_rows'],d['unpriced_position_rows'],len(k),sum(x['unpriced'] for x in k),len(d['evidence'])))"</invocation><expect>PRICE-COVERAGE-RECORD date=2026-05-06 securities=826 unpriced=459 position_rows=10090 unpriced_position_rows=6122</expect></criterion>
`CB64bl1-AC1` -- the record exists, its four totals are the measured ones, and the per-kind unpriced counts are printed with their sum.

<criterion id="CB64bl1-AC2" cell_refs="CB-bl-1" judgment="true"/>
`CB64bl1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each count carries its denominator; answers (a) and
(b) rest on a schema and a count, not on a name; no other firm's data was read; what is not established is said.

<expected_criteria>CB64bl1-AC1,CB64bl1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ local data under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` (the base checkout; never write
  there) and write scratch under your own worktree `.scratch/` only (never committed).
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. A commonwealth script you run carries
  `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round64.md</decomp_doc> (round 64), cell `CB-bl-1`.
<owned_cells>CB-bl-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB64bl1-AC1, CB64bl1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~90/ADVI_COTBKF.TO-CB-bl-1.price-coverage-by-kind.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB64bl1-AC1,CB64bl1-AC2` BEFORE the flip. Mechanical: CB64bl1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the `PRICE-COVERAGE-RECORD` line; the per-kind table; answers (a) and (b) per kind with their counts and the column or store named; the PRD lines on the ruled source; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE at most one read-only get of a named object in a bucket this project already reads; no write; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- the four totals are pinned to the measured ones so a wrong join stops the cell; answers rest on a schema and a count; another firm's data is barred by name; BLIND: a price held in a store this build does not list.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-64 analysis @5cc2574c67 (msg 4579), section 4 item 1; `3.0.0_SA_CVO` REMEDIATION_v36 @877c95fb20.
