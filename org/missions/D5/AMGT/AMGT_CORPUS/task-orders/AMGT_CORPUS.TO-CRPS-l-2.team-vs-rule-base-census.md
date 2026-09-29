# AMGT_CORPUS task order -- `CRPS-l-2` -- ROUND 10: a read-only census of the team's Base case against the rule's Base over every name that carries both, with its distribution and denominator

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-l-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 10. Serves the served-Base-case guard of **FWD-12**: the direct test
of the rule's EPS / P-E pairing.

## 1. THE CELL -- `CRPS-l-2`

**Where this came from.** Two Base cases are now served per name, from different sources:
- **The team's**, in the served dossier: `lib.research.corpus.dossier.read_dossier(security_key)["document"]["fields"]["cases"]["base"]`
  -> `{"value": {<metric>: {<year>: <string as written>}}, "unit"/"unit_as_written": ..., "citation": {...}}` with metrics
  such as `EPS`, `Multiple`, `Price`, `Return` and years such as `2026E`..`2030E`; or `{"value": null, "absent": <reason>}`.
- **The rule's**, in the newest stored model block
  `s3://opal-data-harvest/derived/model_block/<security_key>/<newest stamp>/model_block.json` -> `cases.base` with `status`
  (`SERVED` / `ABSENT`), `value` (only when SERVED), `ratio_to_px_last`, `px_last.value`, `inputs.consensus_eps`,
  `inputs.trailing_median_pe`, `band`, `band_basis`, `cause`, `reason`. It is computed by
  `lib/research/api/case_rule.py` (`compute_cases`; read it for how the Base figure is formed and which fiscal year the
  consensus EPS is). When the band refuses a Base (e.g. ADBE_US_Equity: ABSENT, `ratio_to_px_last 3.319...` on
  `px_last 238.93`), the rule's figure still exists as `ratio_to_px_last x px_last.value`.
- The CVO's L9 reading: ML / ORA / SAP agree within 10%; ADBE's rule Base is about 3.4x the team's.

**RULED -- what you build (the CTO's round-9 analysis, ruling 2):** `lib/research/corpus/base_census.py` (new), run as
`python -m lib.research.corpus.base_census`, READ-ONLY (S3 reads only; it writes nothing and grades nothing):
1. Over `lib.research.corpus.dossier._resolved_security_keys()`, pair each name's team Base with its rule Base:
   - **rule Base**: `value` when SERVED; `ratio_to_px_last x px_last.value` when the rule computed a figure the band refused
     (`ratio_to_px_last` and `px_last.value` present); otherwise no rule figure (state the cause).
   - **team Base**: the team's Base `Price` for the fiscal year the rule's consensus EPS is for (read the year from
     `inputs.consensus_eps` / `case_rule.py`; if the rule states no year, the team's FIRST year), parsed as a number from the
     team's string. State the year paired on, per name.
2. Per name one line: `base <key> team <v> rule <v> ratio <team/rule> year <y> rule_status <status> team_unit <symbol or none> listing <ccy or none>`;
   per name that cannot pair: `base <key> unpaired <reason>`. Units are printed, never converted.
3. Final line EXACTLY:
   `base_census names <N> both <b> team_only <t> rule_only <r> neither <n> within_10pct <w> beyond_2x <x> median_ratio <m>`
   with `both + team_only + rule_only + neither = N`, and `within_10pct` / `beyond_2x` counted over `both`.
4. `lib/research/corpus/tests/test_base_census.py` (new), offline stubs: a SERVED pair; a band-refused rule figure
   reconstructed from ratio x px; a team-only and a rule-only name; the partition sums to N.

## 3. SURFACES

<paths>
lib/research/corpus/base_census.py
lib/research/corpus/tests/test_base_census.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-2.team-vs-rule-base-census.md
</paths>

READ-ONLY: every other file (`dossier.py`, `case_rule.py`, `model_block_pull.py` included), every S3 object. Scratch `.scratch/l2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write, no `--write`, no `derive`, no vendor call.
- The census judges nothing: no threshold refuses, flags or changes anything; it prints.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l2_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l2_AC2.sh</invocation><expect>(?ms)^base ADBE_US_Equity team \S+ rule \S+ ratio \S+.*^base_census names [1-9]\d* both [1-9]\d* team_only \d+ rule_only \d+ neither \d+ within_10pct \d+ beyond_2x \d+ median_ratio \S+</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on the real served dossiers and blocks: ADBE paired (its rule figure is
  band-refused, so this also proves the ratio x px reconstruction), and the partition printed.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-l-2.team-vs-rule-base-census.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the summary line; every name `beyond_2x` with its line; the year basis you paired on.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-9 analysis s.2 ruling 2 + s.4 item 2 @`abfad1355c`. Checks dry-run at the base: AC1 FAIL (no tests
ran); AC2 FAIL (No module named lib.research.corpus.base_census). Re-run by this seat after chain A's rewrite as the real run.

<risk>LOCAL</risk>
<status>complete</status>
<round>10</round>
<slot>~2</slot>
<fabric>site-z</fabric>
