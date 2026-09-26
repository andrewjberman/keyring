# AMGT_CORPUS task order -- `CRPS-h-2` -- ROUND 6: every key's Base-case ratio by name, both sides of both bounds, and the team's own workbook cells laid beside the served Base case -- evidence, selecting nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-h-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 1 drift candidate, on data/black_diamond; 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only (opal-data-harvest); nothing written outside the worker's deliverables.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 6. Serves **FWD-12**'s Base-case guard: the band's ACCEPT side, and
the judgment half (AC4 below) that compares a served Base case with the team's own workbook. You produce EVIDENCE; you grade
nothing and choose nothing.

## 1. THE CELL -- `CRPS-h-2`

**Where this came from.** The served Model block for each security is
`s3://opal-data-harvest/derived/model_block/<security_key dir>/<stamp>/model_block.json`; the NEWEST stamp directory (by name)
is served. Its `cases.base` is either `{"status": ..., "value", ...}` served, or `{"status": "ABSENT", "cause", "reason",
"inputs": {"consensus_eps": {...}, "trailing_median_pe": {...}}, "px_last": {...}}` refused. The guard refuses a Base case whose
`base / px_last` falls outside [0.33, 3.0] (`integrations/bloomberg/research/model_block_pull.py`, `CASE_BAND_LOW`/`HIGH`),
and every refusal but one sits 5x-23x outside: the 3.0 ceiling rests on ONE case (NFLX, 3.043). Nothing yet shows what sits
just INSIDE either bound. Separately, the team's own workbooks sit in bronze: every
`s3://opal-data-harvest/amgt/harvest/bronze/research-report-extract/security_key=<k>/<id>/extract.json` whose `type` is
`xlsx` carries `sheet_data` labels and `bronze_key`, the raw workbook object. 79 are workbooks; 61 carry a Base/Bull/Bear or
target label.

**RULED -- what you build:** ONE read-only scripted producer,
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py`, run as
`python <that path> --out-json <path> [--out-md <path>]`, deterministic (sorted keys and rows, no timestamps in the JSON, the
same bytes on two runs), writing ONLY the paths it is given. It writes `CASE_EVIDENCE_ROUND6.json` of this shape:

```
{"ratio_census": {"rows": [ {"security_key": <the block's directory name, exactly>, "status": <cases.base.status>,
                             "cause": <cause or null>, "base": <number or null>, "px_last": <number or null>,
                             "quote_ccy": ..., "reporting_ccy": ..., "ratio": <number or null>,
                             "ratio_basis": "quote-unit" | "unconverted" | null, "bin": <one bin label>} ... ],
                  "bins": {<bin label>: <count>},
                  "near_floor": [<up to 5 rows each side of 0.33, by distance>],
                  "near_ceiling": [<up to 5 rows each side of 3.0, by distance>]},
 "workbook": {"rows": [ {"security_key": <block directory name>, "workbook_key": <bronze_key>, "sheet": ..., "cell": "B12",
                         "label": <the cell text>, "right": [<up to 6 numbers to the right in that row>],
                         "below": [<up to 3 numbers below in that column>], "served_base": ..., "px_last": ...,
                         "ratio": ..., "status": ..., "cause": ...} ... ]}}
```

- One census row for EVERY security key directory holding a block, served or refused or neither. A refused row carries the
  ratio recomputed from its own `inputs` and `px_last` (eps x median PE / px_last); `ratio_basis` is `quote-unit` when both
  sides are in one unit (a GBp/GBP pair scaled x100 exactly as the guard does), `unconverted` when the currencies differ, `null`
  when no ratio is computable. Bins (every row in exactly one): `<0.33`, `0.33-0.5`, `0.5-1.0`, `1.0-1.5`, `1.5-2.0`,
  `2.0-2.5`, `2.5-3.0`, `3.0-3.5`, `>=3.5`, `unconverted`, `not-computable`.
- A workbook row for EVERY cell in a bronze workbook whose text matches, case-insensitively, `\b(base|bull|bear|upside|downside)\b`
  or `target price|price target`, opened from `bronze_key` with openpyxl (`data_only=True`, read-only). Read the numbers
  beside it as they are; NEVER pick one as "the" Base case, never convert, never infer a unit. A workbook that cannot open is a
  row with `sheet`/`cell` set to the reason, never skipped silently.
- `CASE_EVIDENCE_ROUND6.md`: the bins as a table; `near_floor` and `near_ceiling` by name; then, for the CVO's sample, one
  table per venue (London `LN`, US `US`, Asian listings) of served Base case beside the workbook cells, every refused key
  with a workbook included.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/CASE_EVIDENCE_ROUND6.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/CASE_EVIDENCE_ROUND6.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-2.case-ratio-census-and-workbook-side-by-side.md
</paths>

READ-ONLY: every module in the repo. Scratch `.scratch/h2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write, NO vendor or gateway call (every read is `opal-data-harvest`), NO edit
  to any producer. A Base/Upside/Downside figure is never computed, chosen or proposed here.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h2_AC1.sh</invocation><expect>h2 OK census_rows (\d+) bins_sum \1 keys_with_block \1 workbook_names [1-9]\d* rows_without_coord 0\b</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h2_AC2.sh</invocation><expect>h2 determinism identical sha [0-9a-f]{12}</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h2_AC3.sh</invocation><expect>h2 floor LN [1-9]\d* US [1-9]\d* ASIA [1-9]\d* refused_in_census (\d+) of \1\b</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-h-2" judgment="true"/>
</proof_of_spec>

- AC1 the evidence covers every key holding a block, bins summing to it, every workbook cell located; AC2 the producer is
  deterministic; AC3 the sample floor (R-1): every venue present and every refused key in the census.
- **AC4 (JUDGMENT, the CVO's, at L9 -- nothing for you to produce beyond the evidence):** beside the team's own workbook for
  that name, does each served Base case read as a plausible Base case, and does the distribution just inside 0.33 and 3.0
  support those bounds? The sample is a FLOOR and names every venue present (R-1): at least one London, one US large-cap, one
  Asian listing, and every refused key that has a workbook.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-h-2.case-ratio-census-and-workbook-side-by-side.proof_of_spec.json`
   (AC4 as a declared exclusion; the checker admits no judgment row).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the bins line, `near_ceiling` by name, and AC3's line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-5 analysis s.3 and s.5 items 2-3 @`37217d8053` ("cells 2 and 3 share the band's evidence"); CVO row
Z-S40 (the comparator did not exist in the corpus; any workbook read is a scripted producer, never an agent turn). No vendor
call, so the egress lift and its ledger condition do not arise. Checks dry-run at the base: AC1/AC2/AC3 FAIL (no evidence, no
producer).

<risk>LOCAL</risk>
<status>pending</status>
<round>6</round>
<slot>~2</slot>
<fabric>site-z</fabric>
