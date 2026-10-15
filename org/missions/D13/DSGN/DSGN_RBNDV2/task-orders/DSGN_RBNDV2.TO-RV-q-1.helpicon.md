# TO DSGN_RBNDV2.TO-RV-q-1 -- FWD-3/FWD-5: the help icon directly after the panel title text (answers call 002b)

<to_id>DSGN_RBNDV2.TO-RV-q-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~28</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-q-1` (decomp v8 addendum 4 @e4d9f4b324) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~28

---

## WORKER FACE

### THE CELL

`RV-q-1` -- Andrew: "the tooltip helper icon is placed directly after the panel title text. that pattern should be implemented across the entire platform." The Global RSI modal title already does it (`RSIModal.tsx`, the `title` slot: a `span` with `inline-flex items-center gap-2` holding the title text and then the help icon). `PanelHeader.tsx` is the platform's shared panel header, and it puts the help icon (only when `helpText` is given) in the RIGHT-hand group beside the actions, so every panel that passes `helpText` shows the icon far from its title.

**Make these changes (all of them, nothing else):**
1. In `portal/src/ui/components/panels/PanelHeader.tsx` move the help affordance INTO the title element. The `<h3>` keeps every class it has and gains `inline-flex items-center gap-2`. Its children become the title text, then, only when `helpText` is given, `<span className="inline-flex normal-case tracking-normal font-normal">` wrapping the existing `<HelperTip content={helpText} side="auto">` and its `HelpCircle` (size 14, the same classes it has now). The span resets the eyebrow's uppercase, tracking and weight so a tooltip drawn inline does not inherit them. The 2px accent underline then runs under title and icon, as in Andrew's picture.
2. The right-hand group: remove the help affordance from it and render it only when `actions` is given: `(helpText || actions) &&` becomes `actions &&`; keep `flex items-center gap-3 flex-shrink-0` and `{actions}`.
3. Update the file's header comment (the lines that say the help affordance sits on the right, and `RIGHT: Help icon (when helpText is given) -> Actions/Toggles`) and the `helpText` prop doc (`shown as a quiet help icon on the right`) to say the help icon sits directly after the title text. Change no prop, no other class.
4. Do NOT touch any other file. A pinned test, `src/ui/components/panels/__tests__/dsgn-rbndv2/rb-1-p.panel.test.tsx` arm (d), matches `<h3[^>]*>TITLE</h3>` for a header with NO `helpText` and requires `border-b-2`, `border-[var(--rb-accent)]` and `pb-1` on the `<h3>`: with no `helpText` the `<h3>` must hold the title text alone.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-10-q1.helpicon.test.ts`, reading `src/ui/components/panels/PanelHeader.tsx` as text (`join(process.cwd(), 'src/ui/components/panels/PanelHeader.tsx')`; it must stand alone, no workspace paths). The text between the first `<h3` and the first `</h3>` after it holds `helpText`, `HelperTip`, `HelpCircle`, `inline-flex items-center gap-2`, `border-b-2`, `border-[var(--rb-accent)]` and `pb-1`; the span holds `normal-case tracking-normal`; the text after that `</h3>` holds neither `HelpCircle` nor `HelperTip`; it holds `actions && (` and does not hold `helpText || actions`. The test PRINTS `HELP-ICON-AFTER-TITLE` and `VERDICT: HELPICON-AFTER-TITLE-OK` only when every arm holds; the difference control runs the same arms on `git show 4299f28a:src/ui/components/panels/PanelHeader.tsx` and it must FAIL there. Give each `test(...)` that runs `git show` an explicit third argument `30000` (ms timeout); do not pass a `timeout` option to `execSync`.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes every round-8 cell) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB10Q1-AC1" cell_refs="RV-q-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~28; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-10-q1.helpicon.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HELPICON-AFTER-TITLE-OK</expect></criterion>
`RB10Q1-AC1` -- the new test prints `VERDICT: HELPICON-AFTER-TITLE-OK` only when every arm holds, and its difference control fails on the base text.

<criterion id="RB10Q1-AC2" cell_refs="RV-q-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~28; mkdir -p .scratch; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > .scratch/rb10q1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB10Q1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB10Q1-AC3" cell_refs="RV-q-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~28; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB10Q1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/`, `src/ui/components/modal/` and `src/components/market-performance/` passes: the summary line reads `0 fail`.

<expected_criteria>RB10Q1-AC1, RB10Q1-AC2, RB10Q1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/ui/components/panels/PanelHeader.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 4 @e4d9f4b324, cell `RV-q-1`.
<owned_cells>RV-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB10Q1-AC1, RB10Q1-AC2, RB10Q1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~28/DSGN_RBNDV2.TO-RV-q-1.helpicon.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB10Q1-AC1,RB10Q1-AC2,RB10Q1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W28-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Scratch files go under `<WS>/portal/.scratch/` only.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 4 -- the three cells of the addendum write disjoint files (PanelHeader.tsx; RSIModal.tsx; ExecutiveSummary.tsx); every earlier round-8 order is merged; the files were read at the feature tip 4299f28a.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~28, direct act (round-less, one cell, LOCAL, a few dozen product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 28 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md` sections 7 to 9.
