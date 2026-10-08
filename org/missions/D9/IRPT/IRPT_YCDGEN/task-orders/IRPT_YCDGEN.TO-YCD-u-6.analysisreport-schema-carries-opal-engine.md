# IRPT_YCDGEN task order -- `YCD-u-6` -- ROUND 6 (THREAD): THE ANALYSISREPORT SCHEMA CARRIES THE SERVED OPAL_ENGINE FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6L.md</decomp_doc>
<owned_cells>YCD-u-6</owned_cells>
</decomp_ref>
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

## 1. YOUR CELL (inlined from the round-6 addendum-L decomposition)

### `YCD-u-6` -- the AnalysisReport schema carries the served OPAL_ENGINE form (contract hop; FWD-1)
- `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json`: add the OPAL_ENGINE form as a NEW, ADDITIVE branch that matches
  the committed portal type `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` (your portal worktree is at
  d1b21c97). Do not change, narrow or remove any existing branch. Read how e-6 shaped the type before writing the schema.
- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py` (new): one argument, one RESULT line.
  - `schema`: validates every existing AnalysisReport fixture in the repo against the schema as it is at HEAD and as you changed it;
    every document valid before is still valid (`RESULT: schema PASS` only then). Name the fixtures it found and count them.
  - `regen`: runs the portal's wire generator (`portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`; read it for its
    out-dir argument) against the changed schema, writing to a temporary directory and NEVER into `contracts/wire/`. It then compares
    the generated `AnalysisReport.ts` with the committed one byte for byte: `RESULT: regen PASS` only when they are identical. Run bun
    from inside `portal/` with `--no-install`.
  - `census`: lists every reader of `AnalysisReport.schema.json` (the validator, the generator, tests), found by a search whose
    denominator is printed, and states for each that it reads the new branch without error: `RESULT: census PASS` only then.

## 2. THE CONTRACT YOU BUILD AGAINST

**R19 The AnalysisReport schema carries the served OPAL_ENGINE form.** The v1 schema gains the OPAL_ENGINE form as a new branch that
matches the committed `AnalysisReport.ts` at d1b21c97. Every document valid before stays valid. The generator, run to a temporary
directory against the new schema, produces an `AnalysisReport.ts` byte-identical to the committed one. Every reader of the schema is
named and read against the new branch. Why (measured, row IRPT_BCKEND-S388): today a regeneration REMOVES 56 lines from the committed
type, the OPAL_ENGINE form cell YCD-e-6 added by hand on 2026-10-05; the schema (last changed 2026-09-22) does not carry it.

## 3. WHAT YOU NEED TO KNOW

- The committed type is the truth to match: `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` at d1b21c97. Do NOT
  edit any file under `portal/` -- this order writes the schema and your check script only.
- The generator: `portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`. It can write to an out-dir; never let it write
  into `contracts/wire/`. If you cannot make it write elsewhere without editing it, file a row and stop that arm.
- If no byte-identical result is reachable with an additive branch, file a row naming the first differing line and why; do not
  change an existing branch to force it.
- Python checks: `python <script> <arm>` from the worktree root. ASCII only. No client figure and no secret in any committed file.

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including all of `portal/`. NEVER: a vendor call, any AWS call, a deploy, a
`bun install`, a package fetch, an edit under `portal/`. A check you cannot satisfy inside your `<paths>` is a surprise row appended to
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a
fenced json row; ids `IRPT_YCDGEN-W6-S<k>`, next unused k; `fabric` "laptop"; `surfaced_at` the real UTC time).

<paths>
docs/contracts/investor-reporting/v1/AnalysisReport.schema.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine.proof_of_spec.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every AnalysisReport document valid before the change is still valid against the changed schema
- **AC2** -- the generator run against the changed schema reproduces the committed AnalysisReport.ts byte for byte
- **AC3** -- every reader of the schema is named and reads the new branch

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py schema</invocation><expect>^RESULT: schema PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py regen</invocation><expect>^RESULT: regen PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-u-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py census</invocation><expect>^RESULT: census PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit in your outer worktree, then write the instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine.proof_of_spec.json`
with `to_id` `IRPT_YCDGEN.TO-YCD-u-6.analysisreport-schema-carries-opal-engine`, check it with `python .tools/proof-of-spec-check.py
<instance>`, and commit it. Report once: each criterion's verdict line with the output above it; the fixtures counted; the readers
named; files written; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** addendum L cell (IRPT_YCDGEN_DECOMP_R6L.md), cut on 1.0.0_SA_CTO~DELL2 ruling msg 1194
(v1 additive, three criteria) after row IRPT_BCKEND-S388 (2.0.0_SA_COO~P2 msgs 1187/1190). Chain `~6`, fresh slot. Worktree provisioned
with `.tools/wk-provision.sh provision IRPT_YCDGEN 6 --path C:/dev/wk-ycdgen-u6 --portal-ref d1b21c970c --node-modules link`. Risk SERVED:
a published contract document changes; nothing deployed moves.

<round>6</round>
<workstream>R6L_ANALYSISREPORT_CONTRACT</workstream>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
