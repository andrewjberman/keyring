# AMGT_CORPUS task order -- `CRPS-g-1` -- ROUND 5: the machine Base case REFUSES rather than serves when it cannot be right -- forward EPS <= 0, no price to check it against, or base/px_last outside [0.33, 3.0] -- and is expressed in the price's own currency unit; NO vendor call in this cell

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 and calls no vendor; the re-derive is the issuer's drain act under its pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 5. Serves **FWD-12** (the Model tab's cases). **First read
`integrations/bloomberg/READ_HERE.md`.** NEVER call Bloomberg, NEVER open a blpapi session, NEVER run `pull` or `derive` for
real: `cases-report` (which you build) reads already-landed raw from S3 and writes nothing, and it is the only live run you make.

## 1. THE CELL -- `CRPS-g-1`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py`'s `_compute_cases` serves a Base case as FY1
`BEST_EPS` x the median of every closed fiscal year's `PE_RATIO`, and carries `PX_LAST` "as context only". Measured on the served
route over the 32 names whose Base is served: 7 are implausible against their OWN `px_last` in the same block --
`BA_US_Equity` -18.03 vs 196.80 (forward EPS -0.828); four London names at 0.014-0.046x (`ULVR_LN`, `HSBA_LN`, `RKT_LN`,
`BP/_LN`: the price quotes in GBp, the earnings in GBP, a factor of 100); `NFLX_US` 3.04x and `NOW_US` 4.45x; plus `ROG_SW`
served with NO `px_last` at all. The other 24 sit at 0.54-2.00x.

**RULED -- what you build (in `_compute_cases` and its callers only):**
- Tested in THIS order, the first that applies decides, each yielding `{"status": "ABSENT", "reason": <derived>, "cause": <one of
  the four>}` for `base` (Upside/Downside keep their ruled ABSENT unchanged):
  1. `cause "forward_eps_not_positive"`: FY1 `BEST_EPS` <= 0; the reason names the value.
  2. `cause "no_price"`: no `PX_LAST` figure; the reason says the case cannot be checked against a price.
  3. units: when the block's own `currencies` record shows a minor-unit quote (a quote currency that is the hundredth of the
     reporting currency, e.g. `GBp` vs `GBP`, read from the block's currency fields, never from a venue list), the Base value is
     expressed in the QUOTE unit (x100) before the band; the served case carries `quote_currency`, `reporting_currency` and
     `unit_factor`. If the two currencies differ in any other way, `cause "currency_mismatch"` refuses with both named: the
     block converts NOTHING (its own `currencies.converted` is False, by ruling), and 26 of this project's 89 blocks quote and
     report in different currencies (e.g. `ULVR_LN` GBp vs EUR, `JD_US` USD vs CNY), so a Base case built from reporting-currency
     EPS cannot be read against a quote-currency price.
  4. `cause "outside_band"`: `base / px_last` outside `[0.33, 3.0]` (module constants `CASE_BAND_LOW`, `CASE_BAND_HIGH`); the
     reason prints the ratio and the band.
  Otherwise `base` is SERVED as today, now also carrying `ratio_to_px_last` and `band`.
- The served block names its P/E window rule in `inputs.trailing_median_pe.window_rule` (e.g. "every closed fiscal year carrying
  a PE_RATIO figure"), beside the `window` and `n` it already prints.
- A read-only mode `model_block_pull.py cases-report --securities <s1> [<s2> <s3>]` (Bloomberg identifiers, at most 3): for each,
  read the NEWEST landed raw stamp from S3, rebuild the figures and cases in memory exactly as `derive` would, write NOTHING, and
  print `cases <sec_key> base <SERVED|ABSENT> ratio <r|none> cause <cause|none> reason <text>`, then
  `cases_report served <n> refused <m>`.
- `tests/test_model_cases_guard.py` (fixtures, no network): each of the four causes, the GBp x100 path landing in band, a
  plausible US name served with its ratio, and the precedence order.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_cases_guard.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-1.model-cases-guard.md
</paths>

READ-ONLY: everything else under `integrations/bloomberg/`, `lib/research/`. Scratch `.scratch/g1/`. Deliverables:
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/`. The puller runs as a script with the repo on `PYTHONPATH`.

**ISSUER AMENDMENT 1 (2026-09-25 ~18:1xZ, `2.0.0_SA_COO~X`, on `1.0.0_SA_CTO~Z`'s confirmation of the band):** every refusal's
reason names the RATIO AND BOTH OPERANDS it was decided on -- for `outside_band`, the base (in the quote unit), `px_last` and the
ratio, e.g. `base 218.24 USD / px_last 71.72 USD = 3.043, outside [0.33, 3.0]` -- so a near-miss is legible, never silent. The
precedence stays as ruled: the currency check decides BEFORE the band (cause first, symptom second).

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call, NO S3 write, NO change to the field lists, the history chunking, the
  cap, the landing addresses or any figure other than the cases. Upside/Downside stay the ruled ABSENT string.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-g-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-g-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g1_AC2.sh</invocation><expect>(?s)cases BA_US_Equity base ABSENT ratio \S+ cause forward_eps_not_positive.*cases ULVR_LN_Equity base ABSENT ratio \S+ cause currency_mismatch.*cases RKT_LN_Equity base SERVED ratio \d+\.\d+.*cases_report served 1 refused 2</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-g-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g1_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-g-1" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the producer's own read-only report on landed raw refuses Boeing for its EPS, refuses
  Unilever for a GBp-vs-EUR mismatch, and serves Reckitt (GBp vs GBP) once scaled x100; AC3 the bound: the Bloomberg research suite still passes.
- **AC4 (JUDGMENT, the CVO's, at L9 on the issuer's REAL re-derive -- nothing for you to produce):** the band table over every
  key with a Base case, served or refused. Are the refusals right for their cause, and do the served values read as plausible
  Base cases beside the team's own workbook for that name? The sample is a FLOOR and names every venue present (R-1): at least
  one London, one US large-cap, one Asian listing, and every refused key.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-g-1.model-cases-guard.proof_of_spec.json`
   (the shape of your f-1 instance; AC4 as a declared exclusion, the checker admits no judgment row).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if AC1-AC3 pass; commit the files you changed plus the instance.
4. Report ONCE: AC2's lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-4 analysis s.8 item 1 as amended by A1 @`047b6211e1`, item 6 (window declared), R-5. The band is the
issuer's choice (decomposition s.1a). The drain runs `cases-report` over the 89 for the derive-pair addendum's expected outcome,
then re-derives. Checks dry-run at the base: AC1 FAIL (no such test file), AC2 FAIL (no `cases-report` mode), AC3 bound.

<risk>SERVED</risk>
<status>pending</status>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
