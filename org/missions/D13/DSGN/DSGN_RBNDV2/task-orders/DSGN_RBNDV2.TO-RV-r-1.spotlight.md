# TO DSGN_RBNDV2.TO-RV-r-1 -- FWD-3/FWD-5: the Global RSI Spotlight cards get the outline; HOTTEST and COLDEST read the canonical green and red

<to_id>DSGN_RBNDV2.TO-RV-r-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~29</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-r-1` (decomp v8 addendum 4 @e4d9f4b324) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~29

---

## WORKER FACE

### THE CELL

`RV-r-1` -- Andrew, after `RV-o-1` was read live, showed the Global RSI modal on its Spotlight tab and said: "I like what you did there, lets also do it here". What `RV-o-1` did: a visible outline on the item containers, and the canonical return red and green on a label. In `RSIModal.tsx` each Hottest and Coldest card (`SpotlightCard`) is `border border-transparent` (an earlier sweep turned the original `border-white/10` transparent), and the HOTTEST and COLDEST labels are the lighter `text-[#22c55e]/70` and `text-[#ef4444]/70`.

**Make these changes (all of them, nothing else):**
1. In `portal/src/components/market-performance/RSIModal.tsx`, in `SpotlightCard` (find it with `grep -n "function SpotlightCard" src/components/market-performance/RSIModal.tsx`), replace `border-transparent` with `border-[hsl(var(--hairline))]` on the card's root `div` (about line 477). Change nothing else on that line.
2. In the same function, the `labelColor` line (about line 475): `'text-[#22c55e]/70'` becomes `'text-[hsl(var(--delta-positive))]'` and `'text-[#ef4444]/70'` becomes `'text-[hsl(var(--delta-negative))]'`; the `'text-white/40'` branch stays. In `RankedSection` the two labels (about lines 516 and 522, the `div`s that read `Hottest` and `Coldest`) get the same two replacements in their class strings, the other classes unchanged.
3. Do NOT touch `getRSIColor`, `getRSILabel`, the score and status spans (their colour is the five-band RSI scale, not the signed return pair), `RankedRow`, the tab buttons, the selectors, or any other border. Change no other file.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-10-r1.spotlight.test.ts`, reading `src/components/market-performance/RSIModal.tsx` as text (`join(process.cwd(), ...)`; it must stand alone): the `SpotlightCard` function text (from `function SpotlightCard` to `function RankedRow`) holds `border-[hsl(var(--hairline))]` and not `border-transparent`; the file holds no `text-[#22c55e]/70` and no `text-[#ef4444]/70`; `text-[hsl(var(--delta-positive))]` and `text-[hsl(var(--delta-negative))]` each occur at least twice; the `RankedRow` text and the `getRSIColor` function text are unchanged from `git show 4299f28a` (compare the two function bodies). The test PRINTS `SPOTLIGHT #C4CBDB CANONICAL-LABELS` and `VERDICT: SPOTLIGHT-OUTLINES-OK` only when every arm holds; the difference control runs the same arms on `git show 4299f28a:src/components/market-performance/RSIModal.tsx` and it must FAIL there. Give each `test(...)` that runs `git show` an explicit third argument `30000` (ms timeout); do not pass a `timeout` option to `execSync`.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes every round-8 cell) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB10R1-AC1" cell_refs="RV-r-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~29; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-10-r1.spotlight.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SPOTLIGHT-OUTLINES-OK</expect></criterion>
`RB10R1-AC1` -- the new test prints `VERDICT: SPOTLIGHT-OUTLINES-OK` only when every arm holds, and its difference control fails on the base text.

<criterion id="RB10R1-AC2" cell_refs="RV-r-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~29; mkdir -p .scratch; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > .scratch/rb10r1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB10R1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB10R1-AC3" cell_refs="RV-r-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~29; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB10R1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/`, `src/ui/components/modal/` and `src/components/market-performance/` passes: the summary line reads `0 fail`.

<expected_criteria>RB10R1-AC1, RB10R1-AC2, RB10R1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/RSIModal.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 4 @e4d9f4b324, cell `RV-r-1`.
<owned_cells>RV-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB10R1-AC1, RB10R1-AC2, RB10R1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~29/DSGN_RBNDV2.TO-RV-r-1.spotlight.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB10R1-AC1,RB10R1-AC2,RB10R1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W29-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Scratch files go under `<WS>/portal/.scratch/` only.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 4 -- the three cells of the addendum write disjoint files (PanelHeader.tsx; RSIModal.tsx; ExecutiveSummary.tsx); every earlier round-8 order is merged; the files were read at the feature tip 4299f28a.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~29, direct act (round-less, one cell, LOCAL, a few dozen product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 29 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md` sections 7 to 9.
