# TO IRPT_BCKEND.TO-IB-pr-500 -- the portal's `fe-s-15` and `fe-s-18` fixture generators reproduce their committed bytes, and `selected_sections` resolves (rows D2-W346-S2, S3, S4)

<to_id>IRPT_BCKEND.TO-IB-pr-500</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~350</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>171</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-171 ANALYSIS (msg 6764) section 1 rows D2-W346-S2, -S3 and -S4, and section 2 item 3 | **Decomp cell:** `IB-pr-500` (decomposition section 163) | **outcome_ref:** FWD-3

---

## WORKER FACE

**AMENDMENT 1 (issuer, 2026-10-13T04:4xZ; your rows W350-S1, S3 and S5 were right):** (a) S1: the committed `fe-s-18` outputs are MUTUALLY INCONSISTENT (the frozen map carries one firm id for the directory-resolve route, the other maps another), so no generator run can reproduce all of them: the `fe-s-18` generator is OUT of this order (item 2 below is DEFERRED; leave every `fe-s-18` file and its generator exactly as at your base; row S1 stays and is the issuer's). This order is the `fe-s-15` generator and the `selected_sections` alignment only. (b) S3: AC3's old-section scan was my defect (your base predates round 170's candidate, which carries the new section): AC3 is now the five tests only; AC1 is now the `fe-s-15` generator only. (c) S5: your base count (1213 pass, 27 skip, 4 fail at cf52fdbf) is the true base; my 1216/27/1 was the figure after round 170's candidate. Your portal commit `69f69895` and your workspace commit stand; finish the proof for the amended criteria.

**Cell `IB-pr-500` (inlined):** two portal fixture generators cannot reproduce the files they are supposed to write, so nobody can regenerate safely (the previous worker had to hand-edit six files instead): (1) `portal/src/pages/InvestorReporting/__tests__/fe-s-15/gen-fixtures.ts` writes `fixtures/fe-s-15/job.*.json` (five files) and two smoke maps; a regeneration DROPS the `unprojected_grant` block (`count 0, denominator 1, kinds {}`) and ADDS `status.internal_correlation_id` (`corr-8f21`) compared with the committed bytes. (2) `portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts` FAILS at `gen-fixtures.ts:424` (`clone(wire[HOLDINGS_KEY])`: `JSON Parse error, Unexpected identifier undefined`) because `HOLDINGS_KEY` (`:220`) is the BARE prefix `/api/scoped/investor-reporting/holdings/` while the committed wire map `fixtures/smoke/fe-s-13-wire.json` carries the HASHED key (`/api/scoped/investor-reporting/holdings/<hash>`); a partial run rewrote `fixtures/smoke/fe-s-18-frozen.json` far beyond its section. Repair the GENERATORS (not the committed outputs, which are the truth) so that each run reproduces the committed bytes. You work in the PORTAL repo (your worktree's `portal/` directory, `node_modules` linked, `bun` on PATH). This is a candidate for portal DEV.

**Do:**
1. Make `fe-s-15/gen-fixtures.ts` emit the `unprojected_grant` block and NOT emit `status.internal_correlation_id`, exactly as the committed `job.*.json` and the two `fe-s-15` smoke maps carry them (read the committed bytes; the generator's source of those members is wrong or missing).
2. DEFERRED by AMENDMENT 1 (do nothing here): make `fe-s-18/gen-fixtures.ts` find the holdings entry of the committed wire map (resolve the hashed key by prefix from the map's own keys, not by the bare constant) and reproduce every `fixtures/smoke/fe-s-18-*.json` it writes, section lines included (the committed ones now carry the extractor-form section).
3. Align `selected_sections` (row W346-S4): in `portal/src/pages/InvestorReporting/fixtures/wire/ExportBundle.valid.json` and `fixtures/wire/requests/submit-export.request.json`, set `selected_sections` to the section ids that exist in `fixtures/wire/AnalysisReport.valid.json` (its section_id list; today it names `S-RET-1` and `S-ALLOC-2`, which the AnalysisReport no longer carries). The producer's `ExportBundle.valid.json` still says `S-RET-1`: leave it, and file ONE observation row saying the producer fixture needs the same alignment (it is outside this grant).
4. A generator writes LF into a `core.autocrlf=true` tree: keep each committed file's EXISTING line endings (compare with `git diff --ignore-cr-at-eol`); do not mass-convert line endings.

**Do NOT** edit any product file under `portal/src/` outside `src/pages/InvestorReporting/fixtures/` and `src/pages/InvestorReporting/__tests__/`, any other generator, `package.json` or lockfiles; run no `bun install`; push nothing.

**Criteria (run each under `timeout 120` from your WORKSPACE root, the parent of `portal/`, record the output and exit code verbatim):**

<criterion id="IB171-5-AC1" cell_refs="IB-pr-500"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-5-AC1</invocation><expect>IB171-5-AC1 PASS</expect></criterion>
<criterion id="IB171-5-AC2" cell_refs="IB-pr-500"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-5-AC2</invocation><expect>IB171-5-AC2 PASS</expect></criterion>
<criterion id="IB171-5-AC3" cell_refs="IB-pr-500"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-5-AC3</invocation><expect>IB171-5-AC3 PASS</expect></criterion>

<expected_criteria>IB171-5-AC1, IB171-5-AC2, IB171-5-AC3</expected_criteria>

What the checks grade: AC1 the check RUNS the `fe-s-15` generator (`bun run <generator>` from `portal/`) and then `git diff --ignore-cr-at-eol --stat` over the `fe-s-15` outputs (the five job files and the two `fe-s-15` smoke maps) must be EMPTY (so you commit your portal changes BEFORE you run it, and the generators leave the tree clean); AC2 every `selected_sections` id in the portal ExportBundle wire fixture and the submit-export request fixture is a `section_id` of the portal AnalysisReport wire copy; AC3 the five token-citing portal tests still pass (21). Do not edit the checks. Run `bun test src/pages/InvestorReporting` ONCE at the end and report its counts against your base run (1216 pass, 27 skip, 1 fail at the last round's base; the one fail is pre-existing).

## BOUNDS

- **Grant:** the `paths` block and nothing else. Portal repo: only `src/pages/InvestorReporting/fixtures/` and `src/pages/InvestorReporting/__tests__/`. No product code, no dependency change, no push.
- **Refusal clause:** STOP, file a row, change nothing more, if a generator cannot be made to reproduce a committed file without changing a figure other than the ones named, or if a committed file is itself inconsistent (two committed files that no single generator can both reproduce).
- **Commit** in BOTH repos per your definition: the workspace commit (deliverables, order flip, rows) with `.tools/safe-commit.sh`, and the portal commit with plain `git -C portal commit` (same author and committer values, message file from the Write tool outside the worktree); ASCII only; never stage the workspace's `portal` gitlink.
- **Row ids** are `IRPT_BCKEND-D2-W350-S<k>` (the next free `k`). Report once, under 150 words.

<paths>
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/__tests__/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~350/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-500.portal-fixture-generators-reproduce-committed-bytes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 163 (round 171, workstream ~P), cell `IB-pr-500`.
<owned_cells>IB-pr-500</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB171-5-AC1, IB171-5-AC2, IB171-5-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~350/IRPT_BCKEND.TO-IB-pr-500.portal-fixture-generators-reproduce-committed-bytes.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- test fixtures and two generators of one portal page; no product file, no served artifact; the candidate lands on portal DEV through the CTO review lane (PROD rides the held promote `dell1-e7f2`). No live DSGN_IRPTV1 order names these files (non-complete orders' paths read: all superseded).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p171_cells.py dry-run at base on dell2 2026-10-13 ~04:0xZ: IB171-5 AC2 FAIL (`selected_sections` names `S-ALLOC-2`, not a section_id of the wire copy), AC3 FAIL (15 fixtures carry the old AnalysisReport section in the main portal checkout, which predates round 170's candidate). AC1 (running the generators) was dry-run in a throwaway portal worktree, not the shared checkout.
lane: the paths block IS the grant; worker slot ~350 of IRPT_BCKEND, a portal worktree pair. Class LOCAL.
</preflight>
