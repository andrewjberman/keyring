# TO DSGN_RBNDV2.TO-RV-s-1 -- FWD-3/FWD-5: the Trending Topic drilldown: signed figures on the delta tokens and an outline on each source-article row

<to_id>DSGN_RBNDV2.TO-RV-s-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~30</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-s-1` (decomp v8 addendum 4 @e4d9f4b324) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~30

---

## WORKER FACE

### THE CELL

`RV-s-1` -- Andrew sent a picture of the Trending Topic drilldown modal and said: "Do this one too" (the same two changes `RV-o-1` made: a visible outline on the item containers; the canonical return red and green on the signed figures). In `DrilldownModal` of `portal/src/components/market-performance/ExecutiveSummary.tsx`: the topic score (+0.539) and each source-article score (+0.70, -0.96) read `getSentimentColor` (a lighter `hsl(162, 79%, 46%)` / `hsl(355, 83%, 60%)`), the BULLISH pill and the 1, 2, 3 circles read `accentColor` (`PALETTE.green700` / `red600`), and each source-article row is `bg-white/[0.03]` with no outline. The numbers in the panels beside it read `--delta-positive` and `--delta-negative`.

**Make these changes, inside `DrilldownModal` only (find it with `grep -n "function DrilldownModal" src/components/market-performance/ExecutiveSummary.tsx`):**
1. Directly after the `accentColor` constant, add three constants (keep `accentColor` itself: the lead image gradient reads it):
   - `const inkColor = calculatedSentiment >= 0.05 ? 'hsl(var(--delta-positive))' : calculatedSentiment <= -0.05 ? 'hsl(var(--delta-negative))' : accentColor`
   - `const inkTint = calculatedSentiment >= 0.05 ? 'hsl(var(--delta-positive) / 0.125)' : calculatedSentiment <= -0.05 ? 'hsl(var(--delta-negative) / 0.125)' : `${accentColor}20``
   - `const inkBar = calculatedSentiment >= 0.05 ? 'hsl(var(--delta-positive) / 0.38)' : calculatedSentiment <= -0.05 ? 'hsl(var(--delta-negative) / 0.38)' : `${accentColor}60``
2. The sentiment pill (`style={{ backgroundColor: `${accentColor}20`, color: accentColor }}`, about line 863) becomes `style={{ backgroundColor: inkTint, color: inkColor }}`. The topic score span (`style={{ color: sentimentColor }}`, about line 867) becomes `style={{ color: inkColor }}`; if `sentimentColor` then has no other use inside `DrilldownModal`, delete that one constant (an unused local fails the typecheck). The numbered circle (`style={{ backgroundColor: `${accentColor}20`, color: accentColor }}`, about line 898) becomes `style={{ backgroundColor: inkTint, color: inkColor }}`. The bullet's left bar (`style={{ borderLeft: `3px solid ${accentColor}60` }}`, about line 905) becomes `style={{ borderLeft: `3px solid ${inkBar}` }}`.
3. The article row: inside `visibleArticles.map` add `const artInk = artSentiment >= 0.05 ? 'hsl(var(--delta-positive))' : artSentiment <= -0.05 ? 'hsl(var(--delta-negative))' : 'hsl(48, 96%, 53%)'` before the `return`, and the score span's `style={{ color: getSentimentColor(artSentiment) }}` becomes `style={{ color: artInk }}`. The row's class string (about line 943, `group flex items-center gap-3 px-3 py-2 rounded bg-white/[0.03] ...`) gains `border border-[hsl(var(--hairline))] hover:border-[var(--rb-ink-3)]` right after `rounded`.
4. Do NOT change `getSentimentColor` (the Trending Topics rank numbers and arrows share it and wait on Andrew's word), `accentColor`, the lead image or its gradient, the source badges on the image, `TrendCard`, `HeroTrendCard`, `PerformerCard`, or any file other than `ExecutiveSummary.tsx` and the new test.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-10-s1.drilldown.test.ts`, reading `src/components/market-performance/ExecutiveSummary.tsx` as text (`join(process.cwd(), ...)`; it must stand alone) and slicing the `DrilldownModal` function text (from `function DrilldownModal(` to the next `function ` at column 0): it holds `inkColor`, `inkTint`, `inkBar` and `artInk`; it holds `hsl(var(--delta-positive))` and `hsl(var(--delta-negative))`; it no longer holds `getSentimentColor(artSentiment)` and no longer holds `color: sentimentColor`; the article row class string holds `border-[hsl(var(--hairline))]`; it still holds `accentColor` (the gradient). Outside that slice the file still defines `getSentimentColor` with `hsl(162, 79%, 46%)` and still calls it. The test PRINTS `DRILLDOWN #C4CBDB DELTA-TOKENS` and `VERDICT: DRILLDOWN-OK` only when every arm holds; the difference control runs the same arms on `git show 4299f28a:src/components/market-performance/ExecutiveSummary.tsx` and it must FAIL there. Give each `test(...)` that runs `git show` an explicit third argument `30000` (ms timeout); do not pass a `timeout` option to `execSync`.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes every round-8 cell) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB10S1-AC1" cell_refs="RV-s-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-10-s1.drilldown.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: DRILLDOWN-OK</expect></criterion>
`RB10S1-AC1` -- the new test prints `VERDICT: DRILLDOWN-OK` only when every arm holds, and its difference control fails on the base text.

<criterion id="RB10S1-AC2" cell_refs="RV-s-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~30; mkdir -p .scratch; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > .scratch/rb10s1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB10S1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB10S1-AC3" cell_refs="RV-s-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB10S1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/`, `src/ui/components/modal/` and `src/components/market-performance/` passes: the summary line reads `0 fail`.

<expected_criteria>RB10S1-AC1, RB10S1-AC2, RB10S1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/ExecutiveSummary.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 4 @e4d9f4b324, cell `RV-s-1`.
<owned_cells>RV-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB10S1-AC1, RB10S1-AC2, RB10S1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~30/DSGN_RBNDV2.TO-RV-s-1.drilldown.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB10S1-AC1,RB10S1-AC2,RB10S1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W30-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Scratch files go under `<WS>/portal/.scratch/` only.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 4 -- the three cells of the addendum write disjoint files (PanelHeader.tsx; RSIModal.tsx; ExecutiveSummary.tsx); every earlier round-8 order is merged; the files were read at the feature tip 4299f28a.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~30, direct act (round-less, one cell, LOCAL, a few dozen product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 30 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md` sections 7 to 9.
