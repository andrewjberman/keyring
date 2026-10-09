# IRPT_YCDGEN task order -- `YCD-u-6` -- ROUND 6 (THREAD): THE ANALYSISREPORT SCHEMA CARRIES THE SERVED OPAL_ENGINE FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6L.md</decomp_doc>
<owned_cells>YCD-u-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~6</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a contract document change; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the defect was measured by row IRPT_BCKEND-S388 and ruled by the CTO (msg 1194)
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT) -- the Analysis report made in house, Opal-branded, with no YCharts call. Work ONLY in the worktree
your spawn line names; every path below is relative to that root. No vendor call, no AWS call, no deploy.

**RULES THAT BIND THIS ORDER (verbatim, from the dell2 CTO and Andrew):**
- "Never `bun install`. Provision a worktree only with `wk-provision.sh --node-modules link` (it links C:\dev\ajb_workspace\portal\node_modules, the kit tree) or `none`. The rest of 106215 stands: bun only inside a portal tree holding node_modules, always --no-install, no registry-reaching probe."
- "research browsing only when necessary; no packages, no installs, no file fetched onto the box."

## 1. YOUR CELL (inlined from the round-6 addendum-L decomposition, RECUT 2026-10-08 on 1.0.0_SA_CTO~DELL2 ruling msg 1250)

### `YCD-u-6` -- the portal generator builds AnalysisReport.ts from the served v2 schema (contract hop; FWD-1)
The served AnalysisReport contract is `infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json` (built by
YCD-s-6 @a9bb757ee3). The v1 schema `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` is FROZEN by a sha256 pin
(`test_v1_untouched`). The portal generator still builds AnalysisReport.ts from v1. This cell moves that ONE source to v2.
- DISCARD the earlier v1 edit on this branch (commit 0b6115b205): restore `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json`
  to its bytes at `git merge-base HEAD CLOUD`. Never edit v1 or v2 schema content.
- `portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`: make the AnalysisReport document schema (and only it) read from
  the v2 path above, and make its generated header cite that path. Every other contract keeps its v1 source unchanged. The portal is a
  git submodule at d1b21c97 on branch `wk-IRPT_YCDGEN-6-portal`; commit your portal edit there first, then commit the submodule pointer
  in the outer worktree. Do NOT write into `contracts/wire/`.
- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py`: rework the three arms (one argument, one RESULT line):
  - `schema`: the v1 file's sha256 equals its merge-base copy, AND every AnalysisReport v2 fixture under
    `infra/aws/lambda/investor-reporting/_contracts/fixtures/` validates exactly as its file name says (valid/invalid); count them.
    `RESULT: schema PASS` only then.
  - `regen`: runs the changed generator (bun from inside `portal/`, `--no-install`) to a temporary directory, then compares the generated
    `AnalysisReport.ts` with the committed `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` with the leading header
    comment block EXCLUDED from both; prints the first differing line if any. `RESULT: regen PASS` only when the bodies are identical.
  - `census`: lists every reader of either AnalysisReport schema file (validator, generator, tests; search denominator printed) and runs
    the python tests among them (including `_contracts/tests/test_analysisreport_v2.py`) here AND at `C:/dev/ajb_workspace` (CLOUD);
    `RESULT: census PASS` only when each reader is named and no test is red here that is green on CLOUD (print both result sets).

## 2. THE CONTRACT YOU BUILD AGAINST

**R19 (recut) The wire type is generated from the served contract.** The portal generator reads AnalysisReport from the v2 schema; v1
stays byte-frozen; the generated AnalysisReport.ts body equals the committed one (header excluded). Why (measured, rows W6-S1..S3):
the committed type carries the OPAL_ENGINE form that v2 defines, while the generator still reads v1, so a regeneration today REMOVES it.

## 3. WHAT YOU NEED TO KNOW

- The committed type is the truth to match: `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` at d1b21c97.
- If the v2-generated body cannot equal the committed body without editing a schema, file a row naming the first differing line and
  why; do not edit a schema or the committed type to force it.
- Python checks: `python <script> <arm>` from the worktree root. ASCII only. No client figure and no secret in any committed file.

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`. NEVER: a vendor call, any AWS call, a deploy, a `bun install`, a package fetch,
an edit under `portal/` other than gen-wire.ts. A check you cannot satisfy inside your `<paths>` is a surprise row appended to
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a
fenced json row; ids `IRPT_YCDGEN-W6-S<k>`, next unused k; `fabric` "dell2"; `surfaced_at` the real UTC time).

<paths>
docs/contracts/investor-reporting/v1/AnalysisReport.schema.json
portal
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine.proof_of_spec.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- v1 is byte-frozen and every v2 fixture validates as its name says
- **AC2** -- the generator, reading v2, reproduces the committed AnalysisReport.ts body (header excluded)
- **AC3** -- every reader of either AnalysisReport schema is named and no reader test is newly red against CLOUD

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py schema</invocation><expect>^RESULT: schema PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py regen</invocation><expect>^RESULT: regen PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py census</invocation><expect>^RESULT: census PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit in your outer worktree, then overwrite the instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine.proof_of_spec.json`
with `to_id` `IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine`, check it with `python .tools/proof-of-spec-check.py
<instance>`, and commit it. Report once: each criterion's verdict line with the output above it; files written; rows filed. Leave the
`<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** addendum L cell (IRPT_YCDGEN_DECOMP_R6L.md), cut on 1.0.0_SA_CTO~DELL2 ruling msg 1194
(v1 additive, three criteria) after row IRPT_BCKEND-S388 (2.0.0_SA_COO~P2 msgs 1187/1190). Chain `~6`, fresh slot. Worktree provisioned
with `.tools/wk-provision.sh provision IRPT_YCDGEN 6 --path C:/dev/wk-ycdgen-u6 --portal-ref d1b21c970c --node-modules link`. Risk SERVED:
a published contract document changes; nothing deployed moves.

<round>6</round>
<workstream>R6L_ANALYSISREPORT_CONTRACT</workstream>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
**AMENDMENT 2026-10-08 (2.0.0_SA_COO~G2, issuer):** recut on 1.0.0_SA_CTO~DELL2 ruling msg 1250 (answering my msg 1245): the
v1-additive cell (ruling 1194) is superseded; the first proof instance (df5280bce5: AC1 PASS, AC2 FAIL, AC3 FAIL) measured that v1 is
sha-pinned and the served contract is v2. Cell, contract, paths and all three criteria rewritten; worker class, risk and chain unchanged.
Rows W6-S1..S3 resolve against this recut. Gate limb: none graded this modification (a MODIFIED order; LIMB 6 fires only on a newly
added one, and this order declares `<placeholders>NONE</placeholders>`, so GATE viii has nothing to grade).

**AMENDMENT 2 2026-10-08 (2.0.0_SA_COO~G2, issuer):** AC3 narrowed to "no reader test newly red against CLOUD": the three red
tests of instance c73a029dc3 (two `assert 19 == 20` route counts, one absent brand asset) touch neither schema and are red on CLOUD
too (row D2-W6-S2). AC2 is NOT amended (CTO ruling msg 1250); it is met by the next cell on this chain, YCD-v-6 (decomposition R6L
revision 1.1), after which this order's AC2 is re-run. Gate limb: none graded this modification (modified order; no placeholders).

<status>complete</status>
