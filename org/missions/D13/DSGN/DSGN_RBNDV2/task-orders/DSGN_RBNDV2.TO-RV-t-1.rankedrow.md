# TO DSGN_RBNDV2.TO-RV-t-1 -- FWD-3/FWD-5: the Global RSI Ranked tab rows take the hairline outline

<to_id>DSGN_RBNDV2.TO-RV-t-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~31</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-t-1` (decomp v8 addendum 5 @97917488dc) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~31

---

## WORKER FACE

### THE CELL

`RV-t-1` -- Andrew, looking at the Global RSI modal on its Ranked tab, said: "make this one have the same outline" (the 1px `--hairline` outline the Spotlight cards took in `RV-r-1`). In `portal/src/components/market-performance/RSIModal.tsx` each ranked line is a `RankedRow` (find it with `grep -n "function RankedRow" src/components/market-performance/RSIModal.tsx`): its root `div` is `className="flex items-center gap-3 px-3 py-2 rounded bg-white/[0.03]"`, with no border.

**Make this change (and nothing else):**
1. In `RankedRow`, the root `div`'s class string becomes `className="flex items-center gap-3 px-3 py-2 rounded border border-[hsl(var(--hairline))] bg-white/[0.03]"` (the three tokens `border border-[hsl(var(--hairline))]` go right after `rounded`).
2. Do NOT touch `SpotlightCard`, `RankedSection`, the labels, `getRSIColor`, `getRSILabel`, the Full tab or any other class or file.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-11-t1.rankedrow.test.ts`, reading `src/components/market-performance/RSIModal.tsx` as text (`join(process.cwd(), ...)`; it must stand alone): the `RankedRow` function text (from `function RankedRow` to the next `function ` at column 0 after it) holds `border border-[hsl(var(--hairline))]` and `bg-white/[0.03]` and does not hold `border-transparent`; the `SpotlightCard` function text still holds `border-[hsl(var(--hairline))]`. The test PRINTS `RANKED-ROW #C4CBDB` and `VERDICT: RANKEDROW-OUTLINE-OK` only when every arm holds; the difference control runs the same arms on `git show 9db2045b:src/components/market-performance/RSIModal.tsx` and it must FAIL there. Give each `test(...)` that runs `git show` an explicit third argument `30000` (ms timeout); do not pass a `timeout` option to `execSync`.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes every round-8 cell) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB11T1-AC1" cell_refs="RV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~31; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-11-t1.rankedrow.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: RANKEDROW-OUTLINE-OK</expect></criterion>
`RB11T1-AC1` -- the new test prints `VERDICT: RANKEDROW-OUTLINE-OK` only when every arm holds, and its difference control fails on the base text.

<criterion id="RB11T1-AC2" cell_refs="RV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~31; mkdir -p .scratch; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > .scratch/rb11t1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB11T1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB11T1-AC3" cell_refs="RV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~31; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB11T1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/`, `src/ui/components/modal/` and `src/components/market-performance/` passes: the summary line reads `0 fail`.

<expected_criteria>RB11T1-AC1, RB11T1-AC2, RB11T1-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 5 @97917488dc, cell `RV-t-1`.
<owned_cells>RV-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB11T1-AC1, RB11T1-AC2, RB11T1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~31/DSGN_RBNDV2.TO-RV-t-1.rankedrow.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB11T1-AC1,RB11T1-AC2,RB11T1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W31-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Scratch files go under `<WS>/portal/.scratch/` only.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 5 -- one cell, one file (RSIModal.tsx); every earlier round-8 order is merged and no worker is live; the files were read at the feature tip 9db2045b.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~31, direct act (round-less, one cell, LOCAL, one class string); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 31 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md` section 10.
