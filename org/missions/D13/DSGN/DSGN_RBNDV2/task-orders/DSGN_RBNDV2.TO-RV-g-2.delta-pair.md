# TO DSGN_RBNDV2.TO-RV-g-2 -- FWD-3/FWD-5: the return-delta tokens are darker inside every light surface

<to_id>DSGN_RBNDV2.TO-RV-g-2</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~26</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-g-2` (decomp v8 addendum 2 @3645e0e884) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** RV-n-1 merged (both write src/index.css next to each other; cut and spawned one after the other) | **slot:** ~26, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-g-2` -- the continuation of `RV-g-1`. Andrew: "the red/green canonical colors for positive/negative should be darker ... so it stands out better on the light background" and "rec approved keep going". `RV-g-1` re-set `--success` and `--danger` inside the light scope, and a live read after its merge showed the signed figures on `/market` UNCHANGED (`+2.31%` still `rgb(45, 205, 136)`, `-10.73%` still `rgb(251, 112, 132)`): the signed figures do not read `--success` and `--danger`. They read the return-delta tokens `--delta-positive`, `--delta-negative` and their `-hover` steps (`portal/src/index.css`: root `--delta-positive: 154 64% 49%` #2dce89 and `--delta-negative: 348 90% 59%` #f5365c at about lines 150-153, and a lightened set for the named-layer scope at about lines 400-403: `--delta-negative: 351 94% 71%` #FB7185, `--delta-positive-hover: 156 72% 67%`, `--delta-negative-hover: 0 93% 82%`), consumed by `portal/src/lib/performanceUtils.ts` (lines 74 and 75) and `ExecutiveSummary.tsx` (lines 696 and 697) as `text-[hsl(var(--delta-positive))] group-hover:text-[hsl(var(--delta-positive-hover))]`. That is the shared pair; the COO's earlier statement that it was `--success` and `--danger` was wrong and is corrected here.

**Make this one change in `portal/src/index.css` (nothing else):** in the block `RV-g-1` added, the one whose selector is `[data-panel-surface="light"]:not(.dark-band *)` (find it by that selector; it currently declares `--success` and `--danger`), add four declarations and update its comment (say the block now also re-sets the return-delta tokens that the signed figures read, name the reading `performanceUtils.ts`, and give each hex with its contrast on #F8F8FD):
```
  --delta-positive: 145 70% 26%;         /* #14713B, 5.74 to 1 on #F8F8FD */
  --delta-negative: 352 75% 42%;         /* #BB1B30, 5.99 to 1 on #F8F8FD */
  --delta-positive-hover: 145 72% 21%;   /* #0F5C2F, 7.65 to 1: a hover goes one step deeper */
  --delta-negative-hover: 352 78% 35%;   /* #9F1426, 7.62 to 1: a hover goes one step deeper */
```
Keep `--success` and `--danger` there as they are (titles and status chips read them). A custom property set directly on the panel root beats the lightened value that the named-layer scope sets on a page element above it, so no selector change is needed. Do NOT change any root-level definition, the named-layer block, `.dark-band`, the selector of the block, or any other block or file.

**Test.** Edit `portal/src/__tests__/dsgn-rbndv2/rb-8-g1.signal-pair.test.ts` (your predecessor's own test of that block; you may change only what this cell requires): the block now declares exactly the six names `--success`, `--danger`, `--delta-positive`, `--delta-negative`, `--delta-positive-hover`, `--delta-negative-hover` with the exact triples above; the root-level `--delta-positive` (`154 64% 49%`) and `--delta-negative` (`348 90% 59%`) definitions are unchanged; the test PRINTS `SIGNAL-PAIR #14713B #BB1B30 DELTA-PAIR` and `VERDICT: SIGNAL-PAIR-OK` only when every arm holds; the difference control (the same arms on `git show 3509eae8:src/index.css`) must still FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes RV-b-1, RV-g-1 and RV-n-1) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB8G2-AC1" cell_refs="RV-g-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~26; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-8-g1.signal-pair.test.ts 2>&1 | tail -25</invocation><expect>SIGNAL-PAIR #14713B #BB1B30 DELTA-PAIR</expect></criterion>
`RB8G2-AC1` -- the block carries the six exact triples outside every `@layer`, the root-level delta definitions are unchanged, the difference control fails on the base text, and the test prints the line `SIGNAL-PAIR #14713B #BB1B30 DELTA-PAIR` (the test at the base tip does not print it) and `VERDICT: SIGNAL-PAIR-OK` only when every arm holds.

<criterion id="RB8G2-AC2" cell_refs="RV-g-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~26; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb8g2-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB8G2-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB8G2-AC3" cell_refs="RV-g-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~26; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB8G2-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/` and `src/ui/components/modal/` passes: the summary line reads `0 fail`.

<expected_criteria>RB8G2-AC1, RB8G2-AC2, RB8G2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/index.css
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 2 @3645e0e884, cell `RV-g-2`.
<owned_cells>RV-g-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB8G2-AC1, RB8G2-AC2, RB8G2-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~26/DSGN_RBNDV2.TO-RV-g-2.delta-pair.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB8G2-AC1,RB8G2-AC2,RB8G2-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W26-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 2 -- this cell and RV-n-1 write portal/src/index.css next to each other, so they are spawned one after the other, each after the previous merge; the files were read at the feature tip 3509eae8.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~26, direct act (round-less, one cell, LOCAL, about 10 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 26 --portal-ref feature/dsgn-rbndv2-light` after RV-n-1 merges; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md`.
