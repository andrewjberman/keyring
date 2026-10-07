# AMGT_HARVST task order -- `HVST-bg-1` -- ROUND 60 (`1.0.0_SA_CTO~Z` msgs 31173, 31209; CVO grade @399fcf7d0a): SEVEN EXACT-CASE TICKER FORMS ARE REFUSED ON THEIR GRADED CENSUS -- DATA AND PLANTS, NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~109</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL data and plants. NO network at all: no S3, no publisher or vendor host, no gold or silver build, no collector run. NOTHING is fetched from the internet: no package, script or program (Andrew-direct 2026-10-07); if a module you need is not installed, stop and say so in your report. Collection legs are LIVE on the shared tree: touch nothing outside your worktree and do not read `.runtime`.
comp-adversary: RUN at L5 -- the adversary is a refusal entry with no census, a refused form that also removes a company NAME alias, an eighth form refused that the grade did not refuse (CAT, CSL, TTE, SLB), or a plant with no control that the form was there before.
</preflight>

## 0. THE CELL

`lib/research/harvest/whole_brand_aliases.json` `ticker_refusals` lists exact-case ticker forms that are NOT given to a
security (today `RTX`, `ST`, `AI`). `lib/research/harvest/universe_securities.py` `ticker_verdict` reads it: a security whose
ticker root is on the list gets no exact-case form; its name aliases are untouched.

A graded census (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND58_GOLD_REBUILD8_GAIN_AND_FORM_GRADE_20261007.md`
@399fcf7d0a; samples in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/GOLD_REBUILD8_FORM_SAMPLE.md`)
read the pairs that rest on each NEW ticker form. Ruled: seven forms are refused. Per form, the security, the grade and what
the form matched instead:

| form | security | grade | what it matched | pairs resting on it |
|---|---|---|---|---|
| `BATS` | BATS_LN_Equity (British American Tobacco) | 0 of 10 | the exchange prefix on an ETF ticker, "( BATS: ITA )" | 65 |
| `JD` | JD_US_Equity (JD.com) | 2 of 10 | JD Sports, JD Vance, a law degree | 24 |
| `ICT` | ICT_PM_Equity (International Container Terminals) | 0 of 10 | information and communications technology | 18 |
| `ML` | ML_FP_Equity (Michelin) | 0 of 10 | machine learning; MoneyLion | 12 |
| `BE` | BE_US_Equity (Bloom Energy) | 1 of 10 | BE Semiconductor, BE Aerospace, the BE-4 engine | 15 |
| `SAN` | SAN_FP_Equity (Sanofi) | 0 of 10 | Banco Santander (Sanofi's US ticker is SNY) | 22 |
| `MSCI` | MSCI_US_Equity (MSCI Inc) | 10 of 11 rows are index or fund names ("MSCI World Index", "iShares MSCI China ETF"), ruled not news about MSCI Inc | 125 |

NOT refused, and not to be touched: `CAT` (10 of 10, Caterpillar), `CSL` (measured separately), `TTE`, `SLB`, and every other
form. A refused form removes only the exact-case ticker form; `MSCI Inc`, `JD.com`, `Sanofi` and the other NAME aliases stay.

## 1. THE BUILD (LOCAL, small)

1. **The data.** Add seven `ticker_refusals` entries to `whole_brand_aliases.json`, each `{"ticker": "<FORM>", "census":
   "..."}`. Each census string cites the grade file and hash above, gives the grade and the pairs from the table, and says in
   a few words what the form matched. Keep the file ASCII; change nothing else in it.
2. **Plants** in `lib/research/harvest/tests/test_bg1_ticker_refusals.py` (no network), through the real
   `securities_from_universe` on a small fixture pool document and the REAL list file:
   - (i) for each of the seven: an entry with that ticker (`BATS LN`, `JD US`, `ICT PM`, `ML FP`, `BE US`, `SAN FP`,
     `MSCI US`) and a company name gets NO exact-case ticker form, and its name aliases are exactly what they are with the
     seven entries removed from the rule;
   - (ii) the control: with the seven entries removed from a copy of the rule, each of the seven DOES get its form (so the
     plant shows the refusal is what removes it);
   - (iii) `CAT US`, `CSL AU`, `TTE FP` and `SLB US` still get their forms;
   - (iv) the refusal list read from the real file is exactly `{RTX, ST, AI, BATS, JD, ICT, ML, BE, SAN, MSCI}`, and every
     entry carries a non-empty `census`;
   - (v) the summary's `ticker_forms_refused_by_reason["refusal_list"]` counts the seven on the fixture.
3. An existing assertion that pins the refusal set (`test_alias_rule_round18.py`) changes to the ten; list it in your report.
   Change no other existing assertion unless this cell is the reason, and list each.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/tests/test_bg1_ticker_refusals.py
lib/research/harvest/tests/test_alias_rule_round18.py
lib/research/harvest/tests/test_be1_legal_name_always.py
lib/research/harvest/tests/test_universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~109/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You READ, and never write: `lib/research/harvest/universe_securities.py`, the grade file and the sample named in section 0.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bg-1"><invocation>python -m pytest lib/research/harvest/tests/test_bg1_ticker_refusals.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bg-1"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W109-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~109/AMGT_HARVST.TO-HVST-bg-1.seven-ticker-forms-refused.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bg-1.seven-ticker-forms-refused`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31173 (the second sample and its bars: 9 of 10 keeps a named form, else `ticker_refusals`)
  and msg 31209 (the stricter line holds: the bare form `MSCI` is refused with the six; MSCI Inc keeps every pair it holds
  through its other aliases; none of the 33,665 served pairs is lost). CVO grade @399fcf7d0a. Decomposition section 74.
- DIRECT ACT: one cell, well under 300 product lines, `LOCAL`. Its close is the issuer's one real run: the signing dry run
  re-run on the list with the seven refused (`round58/gold_rebuild8.signing2.py`), then the rebuild's never-widen pair.
- `CSL` is NOT in this cell: msg 31209 term 2 has it measured first (10 CSL pairs, graded; row AMGT_HARVST-Z-S101). If it is
  refused it is one more entry, added by amendment before the dry run is re-run.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base PASS as expected
  (414 passed on merged CLOUD at the round-58 drain).

**COMPLETE 2026-10-07 ~17:3xZ (issuer):**
- **Built:** worker ~109 @ca2316368e + @df0ecbd592; merged @a280f06450 (4 paths, index check 0 of 4 differ).
- **AC1 PASS:** 5 of 5 (plant (ii) is the control: with the seven entries removed each form comes back). **AC2 PASS:** 419 of
  419; the same count on merged CLOUD.
- **Existing assertion changed:** `test_alias_rule_round18.py` pins the refusal set to the ten (was three).
- **Rows:** none.
- **CSL is NOT refused:** `3.0.0_SA_CVO~Z` graded all 42 pairs 39 of 42 against a bar of 38
  (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND58_GOLD_REBUILD8_CSL_FORM_GRADE_20261007.md` @f6e370e6cc); the
  three that fail are Carlisle Companies, the same three the mechanical word flag found.
- **Close run:** signing dry run 3 on the list with the seven refused (`deliverables/2.0.0_SA_COO_H/round60/`), launched after
  this close; then the rebuild's never-widen pair.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>60</round>
<slot>~109</slot>
<fabric>site-z</fabric>
