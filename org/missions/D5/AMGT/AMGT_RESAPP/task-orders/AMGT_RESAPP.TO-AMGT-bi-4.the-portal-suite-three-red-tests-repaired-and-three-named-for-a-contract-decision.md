# AMGT_RESAPP task order -- `AMGT-bi-4` -- THE PORTAL SUITE'S SIX RED TESTS: THREE REPAIRED, THREE NAMED FOR A CONTRACT DECISION (NFRA_GATSCP D1-S18; A PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bi-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~403</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bi-4.the-portal-suite-three-red-tests-repaired-and-three-named-for-a-contract-decision</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- three source and fixture edits, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the checks read local files and the nested repository.
comp-adversary: RUN at the cut, each arm against the literal string written below: on the portal at DEV 0a06280a the whole suite reads 462 files, 1,419 tests, 1,386 pass, 27 skip, 6 fail (193 s); the three test files of AC1 read 13 pass 3 fail at the base and 13 pass 0 fail on a throwaway candidate (the three edits below) in a scratch worktree; r102_d1s18_check.py boundary prints 'changed files 0 ... YES' at the base and 'changed files 3 ... YES' on the committed candidate; its table mode reads YES on a control table and NO on one with a block missing; on the same candidate the three wire-drift tests still read red (3 fail), as the order says they must.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-403` (branch `wk-AMGT_RESAPP-403`, cut from the issuance commit; its nested portal worktree is `C:/dev/wk-resapp-403/portal`, branch `wk-AMGT_RESAPP-403-portal`, cut from portal DEV 0a06280a). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-403` (or the portal path); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bi-4` (round 102, decomposition s.110)

Row `NFRA_GATSCP-D1-S18`, now this project's issuer's (laptop CTO msg 108751; CTO~DELL1 round-101 analysis item 3): "name the failing test, its cause, and the fix or a ruled skip with a reason." The portal's CI
(`.github/workflows/ci.yml`) runs lint, the provenance guard, typecheck and build, NOT the unit suite, so the suite has been red on DEV without a landing noticing. MEASURED at the cut (`bun test` in the
portal at DEV 0a06280a): 462 files, 1,419 tests, 1,386 pass, 27 skip, **6 fail**, in six files:

| file (under `src/pages/`) | cause, as measured | class |
|---|---|---|
| `AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts` | its NAMED list cites `_shared/perfrp/PerfrpAllocation.tsx:44` and `_shared/types.ts:1561`; two landings moved the word `alternatives` to :46 and :1565 | STALE-CITATION |
| `InvestorReporting/__tests__/dsgn-irptv1/iv-e-115.vendor-section-names-units.test.tsx` | the pinned census file `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json` changed (commit `a1b500eb1f`, TO-IV-e-118, added the top-level member `row_type_words`); `CENSUS_SHA256` and `CENSUS_PIN` in `contracts/vendorSectionNames.ts` were not moved | PIN-DRIFT |
| `InvestorReporting/__tests__/fe-s-13/producer-fixtures.test.ts` | the portal's copy `fixtures/wire/HoldingsSnapshot.valid.json` lags its source `infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json` on a consumed field (`HoldingsSnapshot.nodes`) | GENERATED-DRIFT |
| `InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` | `gen-wire.ts` regenerates `contracts/wire/HoldingsSnapshot.ts` differently from the committed file (7 lines added, 6 removed): the frozen v1 schema `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` carries `multi_asset` again (commit `506096fc9a`, MDPF_SECCLASS TO-SC-e100) | CONTRACT-ENUM |
| `InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx` | the committed wire union lacks `multi_asset`, which the contract enum carries | CONTRACT-ENUM |
| `InvestorReporting/__tests__/dsgn-irptv1/iv-e-98.generators-drift.test.ts` | the same one-file generator drift (`HoldingsSnapshot.ts`, 1 of 28 files) | GENERATED-DRIFT |

**THE DECISION THIS CELL DOES NOT MAKE.** Regenerating the wire folder (`bun src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`) turns iv-e-26, iv-e-48 and iv-e-98 green and turns
`dsgn-irptv1/iv-e-148.multi-asset-class-readers.test.ts` arm (d) RED (the wire type must admit no retired token at any HoldingsSnapshot class enum: Andrew's 2026-10-07 "there should be no multi-asset class").
Both cannot hold while the frozen v1 contract carries the token. That is a contract decision (the CTO's, and Andrew's word is in it): **leave the wire folder, `gen-wire.ts`, `gen-consumed.ts`, and the
iv-e-26, iv-e-48, iv-e-98 and iv-e-148 test files UNTOUCHED.** The cell repairs the three that are not in dispute and writes the decision down.

Make exactly these three edits in the nested portal worktree `C:/dev/wk-resapp-403/portal` on branch `wk-AMGT_RESAPP-403-portal` (a CRLF file stays CRLF; ASCII only):

1. `src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts`: in the `'_shared/types.ts'` entry change `line: 1561,` to `line: 1565,` and in its reason text `(:1608)` to `(:1612)`; in the
   `'_shared/perfrp/PerfrpAllocation.tsx'` entry change `line: 44,` to `line: 46,`. Nothing else in the file.
2. `src/pages/InvestorReporting/contracts/vendorSectionNames.ts`: set `CENSUS_SHA256` to `'053560a14bd5d5b2a95a25c641062c1bdcfeaca08d4d476075bd2e3891d7e831'` and `CENSUS_PIN` to
   `'a1b500eb1f53349445dc6669672ba408cd6d49a1'` (the test requires a full 40-character commit). Nothing else.
3. `cp ../infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json src/pages/InvestorReporting/fixtures/wire/HoldingsSnapshot.valid.json` (run from the portal root).

Before and after the edits, run the WHOLE suite once each (`bun test` from the portal root; it takes about 200 s: set the Bash call's timeout to 600000 ms) and take the totals line. Then write the table file
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~403/D1_S18_SUITE_TABLE_20261013.md` in EXACTLY this shape (the check reads it): a first line `# D1-S18 suite table`; the line `SUITE-BEFORE: files <n> | pass <p> | fail <f> | skip <s>` (the run BEFORE your edits; expect fail 6);
the line `SUITE-AFTER: files <n> | pass <p> | fail <f> | skip <s>` (the run after; expect fail 3 and the same files count); then, for EACH of the six files above, a block
`### <the file's base name>` followed by a line `CAUSE: <what you MEASURED, at least 20 characters>` and a line `CLASS: <STALE-CITATION|GENERATED-DRIFT|PIN-DRIFT|CONTRACT-ENUM|OTHER>`; then a final
section `## DECISION` stating, in at most 12 lines, what regenerating turns green and red, with the failing test names. Where a measured cause differs from the table above, write what YOU measured and
file a row. Do not run the generators except into a temporary directory.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W403-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only for the three edits, nested worktree `C:/dev/wk-resapp-403/portal`, branch `wk-AMGT_RESAPP-403-portal` from `DEV`; never push; never touch `PROD`.
2. Edit only the three files named; no other file, no new file in the portal; the wire folder and the generators are NOT touched.
3. No deploy, no store write, no AWS call, no network. `bun install` is NOT allowed (the worktree's `node_modules` is a link to the main tree's).
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts
portal/src/pages/InvestorReporting/contracts/vendorSectionNames.ts
portal/src/pages/InvestorReporting/fixtures/wire/HoldingsSnapshot.valid.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~403/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bi-4"><invocation>cd C:/dev/wk-resapp-403/portal &amp;&amp; bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-115.vendor-section-names-units.test.tsx src/pages/InvestorReporting/__tests__/fe-s-13/producer-fixtures.test.ts 2&gt;&amp;1 | tail -5; echo "exit=${PIPESTATUS[0]}"</invocation><expect>` 13 pass`, ` 0 fail`, `Ran 13 tests across 3 files`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bi-4"><invocation>cd C:/dev/wk-resapp-403 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_d1s18_check.py" boundary C:/dev/wk-resapp-403/portal --base DEV; echo "exit=$?"</invocation><expect>the three changed files listed with PASS, `changed files 3 | outside the grant 0`, `R102 D1-S18 BOUNDARY: YES`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bi-4"><invocation>cd C:/dev/wk-resapp-403 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_d1s18_check.py" table "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~403/D1_S18_SUITE_TABLE_20261013.md"; echo "exit=$?"</invocation><expect>six PASS rows (each file named once, with a cause and a class), `PASS D3 suite lines` (before fail 6, the same files count after, after fail 3 or fewer), `R102 D1-S18 TABLE: YES`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bi-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the portal change inside the nested worktree (cwd `C:/dev/wk-resapp-403/portal`; the same `safe-commit.sh` with the author line below, `-F` a message file written with the Write tool,
`--` the three paths relative to the portal root), then commit your deliverables in `C:/dev/wk-resapp-403` via
`.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~403 <0.9.0_WK_AMGT_RESAPP~403@opal.agent>" -F <msgfile> -- <paths>` (confirm each with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~403/AMGT_RESAPP.TO-AMGT-bi-4.the-portal-suite-three-red-tests-repaired-and-three-named-for-a-contract-decision.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC4 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal` in the outer worktree.
Report once:
- the commit hash (and the portal branch and commit hash);
- every criterion's output lines;
- the SUITE-BEFORE and SUITE-AFTER lines and the names of the tests still failing after;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-101 analysis item 3 (msg 4864): "name the failing test, its cause, and the fix or a ruled skip with a reason. CI must read green on DEV." CI does not run the suite, so it already reads
green; the red is the suite. THE ISSUER'S RULING: the three undisputed repairs land as a candidate (three files, one a product constant, one a fixture copy, one a test's citations); the other three are ONE
decision that is not the issuer's, because Andrew's verbatim "there should be no multi-asset class" is in it (SC-e-23 pins it in iv-e-148 arm (d)) and the frozen v1 contract that carries the token is
immutable: regenerate and relax iv-e-148 (d) to what the adapter already guarantees (a served retired token maps to `unclassified`, arm (a)), or hold. The issuer asks the CTO the question in the
round-102 packet, with this cell's `## DECISION` as its evidence. The CTO reviews the candidate before any DEV push (a product file is touched); no worker pushes.

<status>pending</status>
<round>102</round>
<slot>0.9.0_WK_AMGT_RESAPP~403</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
