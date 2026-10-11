# TO IRPT_ANLREQ.TO-AR-y-41 -- the report_index members get the types the producer writes; the portal's wire folder is regenerated

<to_id>IRPT_ANLREQ.TO-AR-y-41</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the L6 gate's floor for an `infra/` path. The work itself is a contract document, tests, fixtures and generated portal type files: nothing is built, uploaded, applied or pushed.
**Decomp cells:** `AR-y-41`, `AR-y-42` (`decompositions/IRPT_ANLREQ_DECOMP_R4_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r4`, cut from portal DEV `6398c79eb4`
  (node_modules linked; never run `bun install`). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The workspace worktree shows
  ` M portal`: never commit it.

### CELL `AR-y-41` (inlined)

*In `OwnedAnalysisRequest.schema.json`, the members of `persist_inputs.report_index` that are empty schemas get the type the producer
actually writes. One refusal test for a wrong-typed value.*

- The contract: `docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json`, at
  `properties.persist_inputs.properties.report_index`: `oneOf [ {"type": "null"}, {object} ]`. The object alternative has
  `additionalProperties: false`, `required: [report_id, revision, retention_ref, sha256]`, and THREE members that are the empty schema
  `{}`: `report_id`, `revision`, `retention_ref` (`sha256` is already a 64-hex string). An empty schema admits anything and the portal's
  wire generator cannot render it.
- **Read the producer first; the types come from it, never from a fixture.** `infra/aws/lambda/investor-reporting/ops/owned_report.py`,
  `_custody_report_index` (about lines 175-225) and its caller (about lines 226-250): find exactly what value each of the three members
  holds when the method returns an index entry -- follow `report_id` (built as `"RPT-" + 32 hex`), the revision read from the index
  row's sort key or attribute, and `retention_ref` (read what object or string the index row stores under it, and where the repository
  writes it: `infra/aws/lambda/investor-reporting/reports/repository.py`). For each member state in your report: the type, the line
  that fixes it, and whether it could ever be another type on a path you read.
- **Then type the three members** as narrowly as the producer guarantees and no narrower: a `type`, plus a `pattern`, `minimum` or a
  nested object shape ONLY where the producer's code fixes it on every path. If `retention_ref` is an object, give it `type: object`
  with the members the producer always writes and say whether `additionalProperties` can be closed. Do not change the required list,
  `additionalProperties: false` on the index object, the `null` alternative, or anything outside `report_index`.
- **Fixtures.** `infra/aws/lambda/investor-reporting/_contracts/fixtures/OwnedAnalysisRequest.persist_inputs.*.json` (five files). The
  valid fixture's index reads `report_id: "rpt_1"`, `revision: 1`, `retention_ref: "ref_1"`. If your types refuse a VALID fixture, the
  fixture was never the producer's shape: correct the fixture to a value the producer could write and say so. Never loosen a type to
  keep a fixture.
- **One test**, in `infra/aws/lambda/investor-reporting/_contracts/test_persist_inputs_contract.py`, named exactly
  `test_persist_inputs_report_index_wrong_types_refused`: for each of the three members, the valid document with that member set to a
  value of a wrong type is refused by the schema. Follow the file's existing style (read it first).
- If the producer's value for a member genuinely can be two types, or you cannot determine it by reading, do NOT guess: type what you
  can, file a row saying what you read, and leave that member with the widest type the producer shows (`type` as a list is allowed).

### CELL `AR-y-42` (inlined)

*The portal's generated wire folder is regenerated from the typed contract so `iv-e-26.wire-regen.test.ts` passes.*

- The generator: portal `src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`. The test:
  `src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` (READ ONLY: never edit the test or the generator).
  Read both to learn where the generator reads the contract documents from and how the committed folder is produced.
- Today the test fails: `generate()` throws on the empty members above, and (reported by another project's worker, not re-measured
  here) two committed files, `ExportBundle.ts` and `ExportReceipt.ts`, differed from fresh output at an older portal commit.
- With cell `AR-y-41` done in the workspace worktree, regenerate the wire folder
  (`src/pages/InvestorReporting/contracts/wire/`) by the generator's own entry point, and commit EXACTLY what it writes. Never
  hand-edit a generated file. If the generator reads the contract from a place the portal branch does not get your workspace change
  from, say precisely where it reads from and make the regeneration read your typed contract by the generator's own documented means;
  if there is none, STOP this cell and file a row.
- If regenerated output changes a file OTHER than `OwnedAnalysisRequest.ts`, list each such file in your report with the reason the
  generator gives a different result (a contract that changed since the folder was last committed). Commit them: the test demands
  the folder equal fresh output. Do not touch any file outside the wire folder.
- Then `bun run typecheck` in the portal (about 40 seconds). If the regenerated types break a consumer, that is a FINDING: do not edit
  the consumer; file a row naming the file, the line and the type error, and report it.

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~11:1xZ): cell `AR-y-42` CLOSES AS A RESULT, by CTO ruling (`1.0.0_SA_CTO~DELL2`
msg 4797).** Gate limb that graded this amendment: read from this commit's own output.
- The regeneration was run and committed on portal branch `wk-IRPT_ANLREQ-51-portal-r4` @`890f1d0f3d` (on origin as a scratch branch;
  NOT merged, NOT for DEV). Its criterion `AR42-y-AC1` prints `Y42-WIRE-FAIL` and stays recorded FAIL in the proof instance: the test's
  drift arm reads 0 of 27, its third arm fails on a pin from a second generator (`gen-consumed.ts`), and fresh output drops hand-added
  exports and (worker's report) breaks 13 types in 8 consumers. Rows `IRPT_ANLREQ-D2-W51-S6` (BLOCKING) and `-S7`.
- The ruling: the wire folder's regeneration with its consumers is DSGN_IRPTV1's (`2.0.0_SA_COO~D2`), one cell; the branch is its
  input; rows W51-S6 and W51-S7 move to that seat with it. "A generated folder holds generator output and nothing else."
- Cell `AR-y-41` is done and merged @35c17fdd07 (`AR41-y-AC1`, `AR41-y-AC2` re-run by the issuer).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~11:2xZ): criterion `AR42-y-AC1` is RETIRED from this order, and the status returns
to `in_progress` for one bookkeeping act.** Gate limb that graded this amendment: read from this commit's own output.
`round-close-check --round 4` refuses an order that reads complete beside a FAIL row. The FAIL was honest and stays on the record in
AMENDMENT 1 above, in rows W51-S6 and W51-S7, and in the proof instance's history at commit `7a8dedb65e`. The cell `AR-y-42` is no longer
this order's to pass: the CTO ruled (msg 4797) that DSGN_IRPTV1 lands the regeneration. The issuer's first flip (@ce4c252845) was wrong
to read `complete` with that row in the instance.
**Do:** in the proof instance, keep rows `AR41-y-AC1` and `AR41-y-AC2` exactly as they are; REMOVE the acceptance row `AR42-y-AC1`; add,
wherever the instance's schema admits free text outside the acceptance rows (read an existing field such as a notes or exclusions
list; do not invent a field the checker refuses), one sentence: "AR42-y-AC1 printed Y42-WIRE-FAIL at 7a8dedb65e and was retired by the
issuer's AMENDMENT 2 on CTO ruling msg 4797; cell AR-y-42 closed as a RESULT, branch wk-IRPT_ANLREQ-51-portal-r4 @890f1d0f3d handed to
DSGN_IRPTV1." Re-run the two remaining checks and record what they print NOW. Commit, validate with the two ids, then flip to `complete`.
The criterion line for `AR42-y-AC1` below is struck: it is no longer an acceptance criterion of this order.

### ACCEPTANCE

<criterion id="AR41-y-AC1" cell_refs="AR-y-41"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r4/ar4_checks.py y41-types --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y41-TYPES-OK</expect></criterion>
`AR41-y-AC1`: all four members are typed, the required list is unchanged, the test file passes and holds the named test.

<criterion id="AR41-y-AC2" cell_refs="AR-y-41"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r4/ar4_checks.py y41-keep --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y41-KEEP-OK</expect></criterion>
`AR41-y-AC2`: the difference control -- the `_contracts` folder still fails exactly the two ids it fails at the base (the two
`analysis-request-original` ids), no more and no fewer. It passes at the base and must still pass.

(retired by AMENDMENT 2: the former criterion AR42-y-AC1 ran `ar4_checks.py y42-wire` and expected `Y42-WIRE-OK`; it printed `Y42-WIRE-FAIL`.)

<expected_criteria>AR41-y-AC1 AR41-y-AC2</expected_criteria>

The issuer runs the portal typecheck, lint and the whole InvestorReporting test folder at the drain, and sends the portal candidate to
the CTO before DEV (the wire folder is a product surface).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/InvestorReporting/contracts/wire/` only.
- READ only: everything else.
- No live act: nothing is built, uploaded, applied, pushed or called. No non-ASCII in what you add.

<paths>
docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json
infra/aws/lambda/investor-reporting/_contracts/test_persist_inputs_contract.py
infra/aws/lambda/investor-reporting/_contracts/fixtures/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R4_Y.md</decomp_doc>
<owned_cells>AR-y-41 AR-y-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR41-y-AC1 AR41-y-AC2 (AMENDMENT 2: AR42-y-AC1 is retired). The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-41.report-index-typed-and-wire-regenerated.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-41`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR41-y-AC1,AR41-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN (by reading) -- the contract document is read by the `_contracts` tests and by the portal's wire generator; a native search of `infra/aws/lambda/investor-reporting` (non-test) for `report_index` finds no runtime validator of this schema, and the release 5 pair records that irpt-status does not re-validate report schemas at runtime. comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission is used or changed.
comp-adversary: RUN -- by reading: 1 contract document, 1 producer method (ops/owned_report.py _custody_report_index), 5 fixtures and 1 test file read by the issuer; NOT seen: the repository code that writes retention_ref, and the portal generator source (the worker reads both). The lens: the cell could type a member to fit a fixture -- the face orders the type read from the producer, a fixture corrected rather than a type loosened, and a row where the producer shows two types.
lane: the contract document, the contract tests and fixtures, the portal's generated wire folder, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut from the CTO round-4 analysis @9da283e89f, section 4 item 2. The analysis says "the two typed members"; the issuer measured THREE
  empty members at this base and the cell types all three (check `y41-types` base: FAIL as expected, naming the three).
- `y41-keep` base: PASS as expected (2 failed, 202 passed). `y42-wire` base: FAIL as expected (0 pass, 1 fail at portal DEV 6398c79eb4).
- Seating: slot ~51 is reused; its round-3 orders are terminal.
