# TO DSGN_RBNDV2.TO-RV-m-4 -- FWD-3: adopt the shared modal frame -- market modals

<to_id>DSGN_RBNDV2.TO-RV-m-4</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~8</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>2</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-m-4` (decomp v2 @95d724679e) | **outcome_ref:** FWD-3 | **depends_on:** RV-m-1 (chain 1, position 4) | **slot:** ~8, queue position 4 of 6

---

## WORKER FACE

### THE CELL

`RV-m-4` -- ADOPT THE FRAME in the market-performance modals (these are the modals Andrew opens from /market) (FWD-3, C-MODAL: the one permitted per-file edit).

**What adoption means.** For each file on the list below: if it draws its own modal dialog (its own `fixed inset-0` overlay, `role="dialog"` or `aria-modal`, scrim, header with title and close button, or a `catalyst/dialog` `Dialog`), replace that chrome with `ModalFrame` from `@/ui/components/modal/ModalFrame` (the frame is the first order of your queue and already exists in your worktree when this order runs; if `ModalFrame.tsx` is absent when you start, stop with a BLOCKING surprise row): the modal's title becomes `title`, its action buttons become `footer`, the rest becomes `children`; ALL state, effects, handlers, props and behaviour of the modal stay exactly as they are. If the file turns out NOT to draw a modal (a popover, dropdown, tooltip, drawer, inline panel), do not change it; list it in your test table as NOT-A-MODAL with a one-line reason. The adoption list is the deliverable: the test table names every file with ADOPTED or NOT-A-MODAL, and a modal not on a list is the defect, so also look in the files' own directories for any other `*Modal*`/`*Dialog*` file with its own overlay and name it in a surprise row (a wall: you may not edit it).

The list:
- `portal/src/components/market-performance/RSIModal.tsx`
- `portal/src/components/market-performance/MarketRegimeModal.tsx`
- `portal/src/components/market-performance/FearGreedModal.tsx`
- `portal/src/components/market-performance/IndexPerformanceModal.tsx`
- `portal/src/components/market-performance/KeywordSentimentModal.tsx`

These five files are large (500 to 1,200 lines); change only the overlay chrome. `ExecutiveSummary.tsx` in the same directory is NOT on your list.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's: you reproduce the fixture and invent nothing. TOKEN FORMATS (a defect in round 1 came from mixing them): the `--rb-*` tokens (`--rb-rule`, `--rb-row-rule`, `--rb-ink`, `--rb-ink-2`, `--rb-ink-3`, `--rb-quiet`, `--rb-accent`) are HEX values, so you read them as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`; `--bg-surface`, `--bg-page`, `--hairline` and the `--semantic-*` tokens are HSL triples, so you read them as `hsl(var(--X))`. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11), no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below its `## RECORD FACE` line.

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `adc70061` (the difference-control base). The fixture is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md`; read it first. Round 1 is merged on the branch: the `--rb-*` tokens, the ground `#EAEAF7`, the white panel primitives, and two scoped rules keyed on `data-panel-surface="light"` (text-white idioms resolve to navy ink; the old dark surface tokens resolve to white and silver). An element carrying `data-panel-surface="light"` therefore reads as a light surface for everything inside it. Do not start any server.

### ACCEPTANCE

<criterion id="RB2M4-AC1" cell_refs="RV-m-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/modal/__tests__/dsgn-rbndv2/rb-2-m4.adoption.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ADOPTION-OK</expect></criterion>
`RB2M4-AC1` -- reading each of the 5 listed files as text: a file the test table marks ADOPTED imports `ModalFrame` from `@/ui/components/modal/ModalFrame`, renders `<ModalFrame`, and contains none of `fixed inset-0`, `role="dialog"`, `aria-modal`, `aria-labelledby`, `from '@/ui/components/catalyst/dialog'`; a file marked NOT-A-MODAL carries a non-empty reason in the table and its text is byte-identical to the base (`git show adc70061:portal/<file>` from `<WS>`, compared); the table covers all 5 files with ADOPTED plus NOT-A-MODAL equal to 5 (print the denominator); (difference control: the same ADOPTED arms run on the base text of every ADOPTED file must FAIL, proving the test can fail). The test prints `VERDICT: ADOPTION-OK` only when every arm holds.

<criterion id="RB2M4-AC2" cell_refs="RV-m-4"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/modal/__tests__/dsgn-rbndv2/rb-2-m4.bound.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ADOPTION-BOUND-OK</expect></criterion>
`RB2M4-AC2` -- for each ADOPTED file, `git diff --numstat adc70061 -- <file>` (run by the test in the portal root with `execSync`) shows insertions plus deletions of at most 160 lines, and the file still contains every `useState`, `useEffect`, `onClick` and `onSubmit` token count it had at the base (the behaviour-preserved bound: a count may not fall). The test prints `VERDICT: ADOPTION-BOUND-OK` only when every arm holds.

<criterion id="RB2M4-AC3" cell_refs="RV-m-4" judgment="true"/>
`RB2M4-AC3` -- graded at the round-2 close by the COO on a market modal opened in the live walk (one of RSI, Fear and Greed, Market Regime), then the CVO and Andrew (DEC-5), never self-graded: the modal reads as the A-light panel with its content legible. RECORD; no verdict.


<expected_criteria>RB2M4-AC1, RB2M4-AC2, RB2M4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/RSIModal.tsx
portal/src/components/market-performance/MarketRegimeModal.tsx
portal/src/components/market-performance/FearGreedModal.tsx
portal/src/components/market-performance/IndexPerformanceModal.tsx
portal/src/components/market-performance/KeywordSentimentModal.tsx
portal/src/ui/components/modal/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v2.md</decomp_doc> v2 @95d724679e, cell `RV-m-4`.
<owned_cells>RV-m-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB2M4-AC1, RB2M4-AC2, RB2M4-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~8/DSGN_RBNDV2.TO-RV-m-4.market-modals.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB2M4-AC1,RB2M4-AC2,RB2M4-AC3` BEFORE the flip, run from inside your worktree. `RB2M4-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's round-2 close walk and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W8-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v2 -- every named existing file measured present at the feature branch adc70061; write sets are pairwise disjoint (decomp v2 section 3).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~8, queue position 4 of 6; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 8 --portal-ref feature/dsgn-rbndv2-light`.
