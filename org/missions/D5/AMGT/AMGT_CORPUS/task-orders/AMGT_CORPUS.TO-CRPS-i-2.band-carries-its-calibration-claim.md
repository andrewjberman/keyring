# AMGT_CORPUS task order -- `CRPS-i-2` -- ROUND 7: the Base case's band carries its CLAIM -- the 3.0 ceiling is measured, the 0.33 floor is uncalibrated -- and no bound or served number moves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-i-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule surface; the re-derive is the issuer's drain act under a pair addendum.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell's probe is the read-only cases-report.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 7. Serves **FWD-12**'s Base-case guard: a VALUE MUST CARRY ITS CLAIM.

## 1. THE CELL -- `CRPS-i-2`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` holds `CASE_BAND_LOW = 0.33` and
`CASE_BAND_HIGH = 3.0` (`:1076-1077`); `_compute_cases` serves a Base case carrying `ratio_to_px_last` and
`"band": [CASE_BAND_LOW, CASE_BAND_HIGH]` (`:1244-1245`, `:1259-1260`), or refuses it with cause `outside_band`. The two bounds
do not carry the same evidence. Measured over 97 block keys (AMGT_CORPUS round 6, evidence
`deliverables/0.9.0_WK_AMGT_CORPUS~2/CASE_EVIDENCE_ROUND6.json` at commit `6d18367755`): two names sit inside the ceiling
between 2.5 and 3.0 and one just outside at 3.043, so the ceiling discriminates; the 0.33-0.5 bin is EMPTY, the nearest accept
is 0.537, and the only name below 0.33 is refused for a different cause, so the floor has never decided anything. Today a
reader sees both bounds as one bare pair.

**RULED -- what you build:**
- Every SERVED Base case, and every Base case refused with cause `outside_band`, gains ONE additive field beside `band`:
  `"band_basis": {"low": {"value": CASE_BAND_LOW, "calibration": "uncalibrated", "basis": <one sentence>}, "high":
  {"value": CASE_BAND_HIGH, "calibration": "measured", "basis": <one sentence>}}`. The two `basis` sentences state the
  measurement above and cite `AMGT_CORPUS round 6 h-2 @6d18367755`; they live as module constants beside the bounds, with the
  two `calibration` words, so the claim sits next to the number it qualifies.
- `band` stays exactly as it is (readers use it). No bound value, no ratio, no disposition, no reason string changes.
- `cases-report` appends ` band_basis low <value> <calibration> high <value> <calibration>` to each line whose Base case carries
  the field.
- `integrations/bloomberg/research/tests/test_band_basis.py` (new): the field on a served case and on an `outside_band`
  refusal; its absence on the three other refusal causes; `band` byte-identical to before; the cases-report suffix.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_band_basis.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-2.band-carries-its-calibration-claim.md
</paths>

READ-ONLY: every other module. Scratch `.scratch/i2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call, NO `pull`, NO `derive`, NO S3 write: `cases-report` is the only
  stage you run against the store.
- The existing Bloomberg research tests keep passing unmodified; if one pins the old served shape byte-for-byte, REFUSE with its
  name rather than editing it.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i2_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i2_AC2.sh</invocation><expect>(?m)^cases SAN_FP_Equity base SERVED ratio \S+ .*band_basis low 0\.33 uncalibrated high 3\.0 measured</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i2_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the read-only cases-report prints the claim on a served name; AC3 the bound:
  the Bloomberg research suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-i-2.band-carries-its-calibration-claim.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-6 analysis s.6 items 2 and 4 @`1e53f322f3`; ADJUDICATION_v9 s.2(B). The drain re-derives every block
key from landed raw under a derive-pair addendum (COO + CTO halves), which serves the claim AND re-mints Z-W2-S10's three
pre-g-1 blocks with band and currency fields. Checks dry-run at the base: AC1 FAIL (no such file), AC2 FAIL (no band_basis
suffix), AC3 bound.

<risk>SERVED</risk>
<status>pending</status>
<round>7</round>
<slot>~3</slot>
<fabric>site-z</fabric>
