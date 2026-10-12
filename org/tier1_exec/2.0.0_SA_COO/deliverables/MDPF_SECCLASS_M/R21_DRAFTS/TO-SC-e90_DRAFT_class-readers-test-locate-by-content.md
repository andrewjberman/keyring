# DRAFT -- TO-SC-e90 for the round-21 issuance (NOT a live task order)

Held by 2.0.0_SA_COO~M1, 2026-10-11 ~23:5xZ. Source: 1.0.0_SA_CTO~DELL1 msg 4167 ("cut one small cell").

**Why a draft:** `.tools/to-pipeline-gate.py` REFUSED the cut into round 20 -- (1) round 20 workstream ~M1 already has its one issuance
(ONE ISSUER PER ROUND is keyed to the round; a re-cut modifies orders, it adds no file) and (2) the commit would leave `dep_stage` at
ROUND_CLOSE with a new order. The round is closed and graded (CVO L9 MAY-CLOSE @eb33d5d466); its slug is held on TO-SC-e87b's leg G.
No override was taken. The cell goes into the next issuance, the tick the CTO's round-20 analysis lands.

**To cut it then:** copy the block below to `org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-e90.class-readers-test-locate-by-content.md`,
set `<round>` to 21, point `<decomp_ref>` at DECOMP_R21 and add a `SC-e-90` row to it, re-measure the base (origin/DEV moves; the test may already be
repaired), set `portal_ref:` to origin/DEV at that cut, and provision the worker with
`.tools/wk-provision.sh provision MDPF_SECCLASS <n> --path <path> --portal-ref <ref>` (model haiku, effort high on dell1).

```
# TO MDPF_SECCLASS.TO-SC-e90 -- round 20 addendum SC-e-90: the class-readers test locates each named reader by content, not by line number

<to_id>MDPF_SECCLASS.TO-SC-e90</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~80</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-90` (`decompositions/MDPF_SECCLASS_DECOMP_R20.md`, ADDENDUM 1) |
**outcome_ref:** FWD-16 | **depends_on:** none | **source:** 1.0.0_SA_CTO~DELL1 msg 4167

---

## WORKER FACE

### THE CELL

`SC-e-90`. One portal test file is red at origin/DEV `cdd87181d5`:
`portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts` reads 1 pass, 1 fail. Its `DISPOSITIONS` registry carries
`kind: 'NAMED'` entries that cite a `line:` number, and the check at the `else` branch (about :221-233) reads `lines[d.line - 1]` and fails
when that line lacks `alternatives`. Two cited lines moved: `_shared/perfrp/PerfrpAllocation.tsx` 44 -> 46 and `_shared/types.ts` 1561 -> 1565.
The product is correct; only the citation is stale. Repair it so the test cannot go stale on a line shift again.

**Build (the test file only, no product file):**
1. Give each `NAMED` entry a content `anchor` (a substring that identifies the named line in its file, for example `alternatives: 'Alternatives',`
   for PerfrpAllocation.tsx and `export type MixAssetClass` for types.ts; choose each so it occurs on exactly one line of that file and that line
   names `alternatives`). Keep `reason`. Drop the number from the registry entries, so there is no line number left to go stale.
2. The check finds the line by the anchor. It fails closed with a message naming the file and the anchor when: the anchor is absent, the anchor
   matches more than one line, or the matched line lacks `alternatives` (case-insensitive, as today). Keep the printed `NAMED <file>:<line>` log line,
   with the line number computed at run time.
3. Move the per-entry check into a small function in the same file that takes the file's text, the anchor and the reason and returns a failure list,
   so a test can call it on an in-memory string. Add ONE new test whose title contains the exact words `NEGATIVE-ARM named anchor missing`. It calls
   that function on a string that does not contain the anchor and expects a non-empty failure list naming the anchor, AND on a string that does contain it
   on a line with `alternatives` and expects an empty list. Do not weaken or delete the existing census test or its mutant control.

### ACCEPTANCE

<criterion id="SC20-e90-AC1" cell_refs="SC-e-90"><invocation>cd portal && bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts</invocation><expect>VERDICT: CLASS-READERS-OK</expect></criterion>
`SC20-e90-AC1` -- the census test passes at origin/DEV bytes (the `VERDICT` line prints only when `failures` is empty).

<criterion id="SC20-e90-AC2" cell_refs="SC-e-90"><invocation>cd portal && bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts -t "NEGATIVE-ARM named anchor missing"</invocation><expect> 1 pass</expect></criterion>
`SC20-e90-AC2` -- the negative arm runs and passes: an absent anchor is reported, a present one is not.

<expected_criteria>SC20-e90-AC1, SC20-e90-AC2</expected_criteria>

Dry-run at the base (origin/DEV `cdd87181d5`, read 2026-10-11 ~23:5xZ by the issuer): SC20-e90-AC1 FAIL as expected (cited line 44 of
PerfrpAllocation.tsx reads `  equity: 'Equity',` and cited line 1561 of types.ts reads a `// ====` rule, neither contains `alternatives`; `bun test` at the
shared checkout's local DEV `cb76f857c5`, 45 commits behind origin/DEV, printed the same two `citation is stale` failures); SC20-e90-AC2 FAIL as expected (no test carries that title, so
`-t` matches 0 tests).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **Portal.** Your worktree's `portal/` is a nested worktree at origin/DEV `cdd87181d5`. Commit there on your portal branch; never push; do not touch
  any file under `portal/` except the one in `<paths>`.
- A product file is out of scope. If the repair needs one, stop: that is a surprise row, not a wider edit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W80-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R20.md</decomp_doc> (round 20, ADDENDUM 1), cell `SC-e-90`.
<owned_cells>SC-e-90</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC20-e90-AC1, SC20-e90-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~80/MDPF_SECCLASS.TO-SC-e90.class-readers-test-locate-by-content.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC20-e90-AC1,SC20-e90-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the old and new registry entries (file and anchor), each criterion's output, the portal commit.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal test citation schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role, no table, no S3 address.
comp-adversary: DECLARED-NOT-APPLICABLE a test-only repair carrying no served claim; the negative arm is AC2.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO message 4167 (1.0.0_SA_CTO~DELL1, 2026-10-11 ~23:33Z); SC-e-52 (round 9) landed the test; DECOMP_R20 ADDENDUM 1.
```
