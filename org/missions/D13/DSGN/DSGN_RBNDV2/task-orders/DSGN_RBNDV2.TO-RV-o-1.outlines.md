# TO DSGN_RBNDV2.TO-RV-o-1 -- FWD-3/FWD-5: visible outlines and accent bars for the nested groups, rows and lead tile of Trending Topics

<to_id>DSGN_RBNDV2.TO-RV-o-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~27</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-o-1` (decomp v8 addendum 3 @2849839e8f) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~27, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-o-1` -- Andrew compared the original dark Trending Topics panel with the light one: "there is a lot of clear shaping around the panels in Trending Topics. In the lightmode version, there is none, it is all flat white. Let's start by doing one simple change and bringing in those edits so we can get some depth and nuance by having some visible outlines." The original draws a thin outline and a 3px green or red bar on the left edge of each group (Bullish Drivers, Bearish Pressures), an outline on every row and on the lead tile. The light version draws none: `NestedCard` is a borderless section, the rows and the tile are `border-transparent` (set by an earlier cell), and a pinned test (`rb-2-i1.sections.test.tsx`) requires `NestedCard` to carry no visual class, so the group outline must come from CSS through the `data-accent` attribute `NestedCard` already sets, not from the component.

**Make these changes (all of them, nothing else):**
1. In `portal/src/index.css`, add ONE new unlayered block of rules directly AFTER the second-layer silver rule (the 16-selector rule that sets `background-color: hsl(var(--bg-nest-2))`; find it by that declaration), under a comment that says what is true (a visible outline and a 3px accent bar for each nested group of a light panel, and why it is CSS on `data-accent`):
```
[data-panel-surface="light"] [data-accent] {
  border: 1px solid hsl(var(--hairline));
  border-radius: 3px;
}
[data-panel-surface="light"] [data-accent="success"] { border-left: 3px solid hsl(var(--success)); }
[data-panel-surface="light"] [data-accent="danger"] { border-left: 3px solid hsl(var(--danger)); }
[data-panel-surface="light"] [data-accent="primary"] { border-left: 3px solid hsl(var(--primary)); }
[data-panel-surface="light"] [data-accent="warning"] { border-left: 3px solid hsl(var(--warning)); }
```
(`--hairline` is the #C4CBDB edge colour; inside a light surface `--success` and `--danger` are the darker #14713B and #BB1B30.) Every selector begins with the scope attribute, none is one of the two exact selectors whose rule counts `rb-1-r.remap.test.ts` and `rb-1-r2.surfaces.test.ts` pin, and `rb-1-t.tokens.test.ts` requires every selector of a block that names the scope attribute to begin with it.
2. In `portal/src/components/market-performance/ExecutiveSummary.tsx`, five class strings carry `border border-transparent` (about lines 674, 989, 1059, 1078 and 1108; find them with `grep -n "border-transparent" src/components/market-performance/ExecutiveSummary.tsx`): the performer rows (about 674 and 1108), the hero story row (about 989) and the lead tile (about 1059 and 1078). On each, replace `border-transparent` with `border-[hsl(var(--hairline))]`; and on the three ROW strings (674, 989, 1108) replace `hover:border-transparent` with `hover:border-[var(--rb-ink-3)]`. Change nothing else on those lines or in the file.
3. Do NOT touch `NestedCard.tsx`, `PanelGrid.tsx`, any other block of `index.css`, any other file's borders, or the footer or header of the panel.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-9-o1.outlines.test.ts`, reading `src/index.css` with `@layer` and brace depth tracked (reuse the reader of `rb-4-w1.alpha-sweep.test.ts`) and `ExecutiveSummary.tsx` as text: the five rules exist outside every `@layer` with the exact declarations above, each selector beginning with the scope attribute; the five class strings named in item 2 hold `border-[hsl(var(--hairline))]` and none of them holds `border-transparent`; the three row strings hold `hover:border-[var(--rb-ink-3)]`; `NestedCard.tsx` is unchanged (it holds no `border` token); the test PRINTS `OUTLINES #C4CBDB 3px-ACCENT` and `VERDICT: OUTLINES-OK` only when every arm holds; the difference control runs the same arms on `git show e88ffb03:src/index.css` and it must FAIL there. Give each `test(...)` that runs `git show` an explicit third argument `30000` (ms timeout).

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes every round-8 cell) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB9O1-AC1" cell_refs="RV-o-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~27; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-9-o1.outlines.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: OUTLINES-OK</expect></criterion>
`RB9O1-AC1` -- the five rules exist unlayered with the exact declarations, the five class strings of `ExecutiveSummary.tsx` carry the hairline outline and no `border-transparent`, the rows carry the hover outline, `NestedCard.tsx` is unchanged, the difference control fails on the base text, and the test prints `VERDICT: OUTLINES-OK` only when every arm holds.

<criterion id="RB9O1-AC2" cell_refs="RV-o-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~27; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb9o1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB9O1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB9O1-AC3" cell_refs="RV-o-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~27; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB9O1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/`, `src/ui/components/modal/` and `src/components/market-performance/` passes: the summary line reads `0 fail`.

<expected_criteria>RB9O1-AC1, RB9O1-AC2, RB9O1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/index.css
portal/src/components/market-performance/ExecutiveSummary.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 3 @2849839e8f, cell `RV-o-1`.
<owned_cells>RV-o-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB9O1-AC1, RB9O1-AC2, RB9O1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~27/DSGN_RBNDV2.TO-RV-o-1.outlines.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB9O1-AC1,RB9O1-AC2,RB9O1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W27-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 3 -- no other order is open; every round-8 order is merged; the files were read at the feature tip e88ffb03.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~27, direct act (round-less, one cell, LOCAL, about 20 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 27 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md` section 5.
