# TO IRPT_FNTEND.TO-FE-s-89 -- reconcile fixture-map keys with round-14's stricter classifier, without weakening it

<to_id>IRPT_FNTEND.TO-FE-s-89</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~39</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-89` (round 15, v0.15) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~1 | **rows:** C-S147 | **base:** workspace = the round-15 issuance commit on CLOUD (your worktree branches from it), portal DEV `7dd3d067` (round 14's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-89` -- round 14's classifier fix (`FE-s-86`) correctly requires a concrete key to match a declared
template SEGMENT FOR SEGMENT, with no trailing operation. This is CORRECT and MUST NOT be weakened. But four
fixture files were never updated to match: they still carry bare PREFIX keys (`/performance/`, `/holdings/`,
`/analysis/`, `/narrative/`, `/status/`, `/export/`) left over from before the fix, so the classifier now
(correctly) reports them as NOT matching any declared template -- even though `scripts/ui-smoke.mjs`'s actual
fixture-SERVING logic (`:158`, `fixtureKeys.find(key => url.includes(key))`, a SEPARATE mechanism from the
classifier) still serves real requests against these prefix keys just fine.

**Measured denominators (CVO round-14 review, KEY-VALIDITY only -- these are NOT request-fulfilment numbers):**

| file | current | target |
|---|---|---|
| `fixtures/smoke/default.json` | 12/12 | 12/12 (already correct -- DO NOT TOUCH, it is your regression baseline) |
| `fixtures/smoke/reporting-answer-bearing.json` | 1/3 | 3/3 |
| `__tests__/fe-s-84/fixtures/reporting-qualified.json` | 1/3 | 3/3 |
| `fixtures/smoke/fe-s-13-wire.json` (generator-owned) | 3/9 | 9/9 |
| `fixtures/smoke/fe-s-14-print-v1.json` (generator-owned) | 0/2 | 2/2 |

**THE RISK, NAMED EXPLICITLY.** The fixture-SERVING match (`url.includes(key)`) is a SUBSTRING test: a bare
prefix key like `/performance/` matches ANY concrete request under that path, regardless of which account id the
test actually requests. If you replace `/performance/` with a single concrete key like
`/performance/A-0001`, a test that requests a DIFFERENT account (`/performance/A-0002`) will stop matching and
the fixture will silently fail to serve -- a real regression, not a fixed one. **Read every consumer of each
affected fixture file (grep the fixture filename across `__tests__/` and `scripts/`) before choosing a fix per
key**, and prove via the whole-suite criterion below that nothing that currently passes stops passing.

**Two remedy shapes, your choice per key, whichever is genuinely safe for that key's real consumers (CVO's own
framing: "migrate maps to concrete/template-aware keys, or explicitly distinguish prefix-map grammar" --
`REMEDIATION_v11.md` C-S147):**
(a) **Migrate to a genuinely concrete key** matching the FULL declared template (e.g., `analysis/{{jobId}}/sections`
    needs a key like `/analysis/JOB-0001/sections`, not just `/analysis/JOB-0001`) -- safe ONLY when you have
    confirmed every real consumer of that fixture requests that exact concrete value, or the serving code is
    also updated so a family of concrete keys under one prefix all resolve (see `default.json`'s own pattern,
    already migrated, as your model -- read it for the exact shape).
(b) **Explicitly declare a prefix-serve grammar** the classifier's reporting can name separately from concrete
    key validity, so KEY-VALIDITY reports the true count of genuinely declared-and-valid concrete keys while a
    SEPARATE line honestly reports "N prefix-serve key(s), not evaluated for template validity, still exercised
    for request fulfilment." **Do not do this by loosening `checkKeyValidity`/`routeKeyCandidates` themselves**
    (`scripts/ui-smoke.mjs:197-231`) -- those are round-14's fix and stay exactly as strict as they are; if you
    need a reporting-layer distinction, add it as new, additional output, never by re-widening the existing
    matcher.

**Generator-owned files.** `fe-s-13-wire.json` and `fe-s-14-print-v1.json` are written by
`__tests__/fe-s-13/gen-corpus.ts`'s `generateSmokeMap()`/`generatePrintMap()`. If you fix these at the source
(preferred, so a later regeneration cannot restore the defect -- CVO's own requirement), prove the regenerated
output equals your committed fix (same pattern FE-s-81/FE-s-85 already established: run the generator, diff
against your committed file, they must be byte-identical or the SAME concrete values). `default.json` is NOT
generator-owned in its current committed form (round-12's hand repair) -- do not regenerate over it.

**Your surface.** `src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json`,
`src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json`,
`src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json`,
`src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json`,
`src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts` (only the two map-generating functions, if you
choose remedy (a) for the generator-owned files), and your own `__tests__/fe-s-89/`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md`, `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text
   (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-14 analysis (`org/missions/D9/IRPT/IRPT_FNTEND/ledger/ROUND_ANALYSIS.round14.md`
   @8b1b0d6832); the CVO's round-14 slug (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v11.md`)
   and its full review (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND14_L8_L9_20260922.md`) -- your
   cell's remedy is quoted from these; read the SURROUNDING text too, not just your own paragraph.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 6010-6014 (outside every prior round's
   range): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`.
3. **A control is a claim.** Before trusting a passing assertion, run its wrong-state / negative arm and confirm
   it fails or reads UNMEASURABLE as required.
4. **Regression is the safety net.** This round FIXES instruments and fixtures that other cells' criteria already
   depend on -- the whole-suite criterion is not a formality, it is the proof you did not silently break a
   currently-passing test while fixing your own defect.
5. **Stop your dev server before the whole-suite criterion, verify the port closed** (`curl` returns `000`).
6. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it. A
   defect needing another cell's file is ONE surprise row, never a wider grant.
7. **Result file** (`<slug>.result.md` in your deliverables folder), disclosure paragraph first.
8. **Keep your context small:** write long outputs to files and read their tails.

### ACCEPTANCE

<criterion id="F89-AC1" cell_refs="FE-s-89" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F89-AC1` -- the whole portal typechecks.

<criterion id="F89-AC2" cell_refs="FE-s-89" drives="none"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/fe-s-89/verify-key-validity.mjs</invocation><expect>default\.json: 12 of 12.*reporting-answer-bearing\.json: 3 of 3.*reporting-qualified\.json: 3 of 3.*fe-s-13-wire\.json: 9 of 9.*fe-s-14-print-v1\.json: 2 of 2</expect></criterion>
`F89-AC2` -- write a small checker (plain node, no framework) that imports/re-evaluates the real checkKeyValidity function against each of the five fixture files' own keys and prints one line per file, `<file>: <n> of <total>` -- all five must read the target denominators above, default.json UNCHANGED at 12/12.

**COO CORRECTION (2.0.0_SA_COO~F, wind-down close-out):** the invocation above originally named a portal-root path (`__tests__/fe-s-89/...`) that never existed and fell outside this order's own BOUNDS Grant, which only ever named the nested `portal/src/pages/InvestorReporting/__tests__/fe-s-89/` path. The worker correctly refused rather than self-grading past the mismatch (row `IRPT_FNTEND-W39-S1`). Corrected to the path the Grant always specified; re-run independently by the COO, output matches `<expect>` exactly, rc=0.

<criterion id="F89-AC3" cell_refs="FE-s-89" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F89-AC3` -- REGRESSION: the whole IRPT_FNTEND suite is green -- no currently-passing test that consumes any of these five fixture files stops passing because of your key changes.

<criterion id="F89-AC4" cell_refs="FE-s-89" judgment="true" drives="none"/>
`F89-AC4` -- graded at L9 by the CVO: the chosen remedy per key (concrete migration vs explicit prefix-serve distinction) is genuinely safe for that key's real consumers, not merely passing by coincidence; the classifier's own strictness (round 14's fix) is unweakened; declared-key validity and exercised request fulfilment are reported as two separate figures, never conflated. RECORD; NO VERDICT.

<expected_criteria>F89-AC1, F89-AC2, F89-AC3, F89-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W39-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`checkKeyValidity`/`routeKeyCandidates` in `scripts/ui-smoke.mjs` are READ-ONLY to you** -- round 14 fixed
  them; this cell fixes the FIXTURE side, never loosens the classifier.
- **`fixtures/smoke/default.json` is READ-ONLY to you** -- it is already correct and is your regression baseline;
  touching it is an order violation, not a fix.
- **C-S176 declared N/A, with reason, at cut time:** this cell's criteria are data-object and pure-logic checks
  (fixture key content, a classifier re-evaluation, a suite regression run), not rendered visual assertions --
  the five-part visual control rule does not apply.
<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json
portal/src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-89/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.15, cell `FE-s-89`.
<owned_cells>FE-s-89</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F89-AC1`, `F89-AC2`, `F89-AC3`, `F89-AC4`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-89.fixture-key-grammar-reconciliation.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F89-AC1,F89-AC2,F89-AC3,F89-AC4 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-89.fixture-key-grammar-reconciliation.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `fixture-key-grammar-reconciliation.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.10 (both L4-R halves SIGNED, prd-signoff.py status ADMITTED).
the design: RUN by the issuer -- REMEDIATION_v11.md @f7546b6aec, the CVO's round-14 review, and ROUND_ANALYSIS.round14.md @8b1b0d6832, all read at HEAD.
the spec: RUN -- PRD FWD-12 ENDPOINT row and the CTO's round-14 analysis, both read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 15, wave 1, slot ~FE-s-89.
