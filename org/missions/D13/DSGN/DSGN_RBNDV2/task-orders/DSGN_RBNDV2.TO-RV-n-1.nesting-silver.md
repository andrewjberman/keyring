# TO DSGN_RBNDV2.TO-RV-n-1 -- FWD-3/FWD-5: nested containers take a silver step per layer of nesting

<to_id>DSGN_RBNDV2.TO-RV-n-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~25</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-n-1` (decomp v8 addendum 1 @f9e30c80d9) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** RV-b-1 merged (all write src/index.css; cut and spawned one after the other) | **slot:** ~25, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-n-1` -- Andrew: "the contained internal panels, not the general container space within the panels, but items like the internal containers which list out the 3 top stories or three top performers etc in market overview ... need that silvery hue to give contrast. I would recommend a strategy with using the silver hue to bring in contrast/depth when there are multiple layers of nesting." The depth strategy, one silver step per layer and never a border: page ground #EAEAF7 -> panel #F8F8FD (`--bg-panel`, set by `RV-b-1`) -> a first nested container silver #EEF1F6 -> a container nested inside that one a deeper silver #E6EBF4; a nested container's hover is one step deeper (the existing `--semantic-background-hover` is already #E6EBF4). The containers that hold items (the Trending Topics rows, the Top and Bottom performer rows and their kind) paint their ground with the tokens `--bg-medium`, `--bg-card`, `--bg-dark` and `--bg-medium-alt` (classes such as `bg-[hsl(var(--bg-medium))]`); `RV-b-1` re-set those four AND `--semantic-background-contentPanel` to the panel tone in the inner-surface block `:root [data-panel-surface="light"] { ... }` of `portal/src/index.css`. The panel's general space (`--semantic-background-contentPanel`, table rows and the modal body) stays the panel tone.

**Make these changes (all of them, nothing else), all in `portal/src/index.css`:**
1. In the same `:root` token list that holds `--bg-panel` and `--bg-surface`, add `--bg-nest-1: 217.5 30.77% 94.9%;` (#EEF1F6, the first nested silver) and `--bg-nest-2: 218.57 38.89% 92.94%;` (#E6EBF4, the second nested silver), each with a comment saying which layer it is and the contrast intent; read as `hsl(var(--bg-nest-N))`.
2. In the inner-surface block `:root [data-panel-surface="light"] { ... }`, change `--bg-medium`, `--bg-card`, `--bg-dark` and `--bg-medium-alt` to `var(--bg-nest-1)`; leave `--semantic-background-contentPanel` at `var(--bg-panel)`, and leave `--bg-header` and `--semantic-background-hover` as they are. Update that block's comment: the four item-container grounds are the first silver step, the general space stays the panel tone.
3. Directly AFTER that block add one unlayered rule for the SECOND layer, with this exact selector list (a nested container inside another nested container), under a comment saying what is true:
```
[data-panel-surface="light"] :is(.bg-\[hsl\(var\(--bg-medium\)\)\], .bg-\[hsl\(var\(--bg-card\)\)\], .bg-\[hsl\(var\(--bg-dark\)\)\], .bg-\[hsl\(var\(--bg-medium-alt\)\)\]) :is(.bg-\[hsl\(var\(--bg-medium\)\)\], .bg-\[hsl\(var\(--bg-card\)\)\], .bg-\[hsl\(var\(--bg-dark\)\)\], .bg-\[hsl\(var\(--bg-medium-alt\)\)\]) {
  background-color: hsl(var(--bg-nest-2));
}
```
4. Do NOT add or change any border, any other block, any text colour, `--bg-surface` or `--bg-panel`.
5. Two existing tests pin the grounds and may be edited only as follows: `portal/src/__tests__/dsgn-rbndv2/rb-1-r2.surfaces.test.ts` arm RB1R2-AC1 (the five grounds): `--semantic-background-contentPanel` must equal `var(--bg-panel)`, the four item-container grounds must equal `var(--bg-nest-1)`, and `--bg-header` and `--semantic-background-hover` stay bare triples; `portal/src/__tests__/dsgn-rbndv2/rb-8-b1.panel-tone.test.ts`: its arm that says the five grounds equal `var(--bg-panel)` now says `--semantic-background-contentPanel` equals `var(--bg-panel)` and the other four equal `var(--bg-nest-1)`. Change nothing else in either test.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-8-n1.nesting.test.ts`, reading `src/index.css` as text with `@layer` and brace depth tracked: the two tokens are declared once with the exact triples; the four grounds equal `var(--bg-nest-1)`, `--semantic-background-contentPanel` equals `var(--bg-panel)`; the second-layer rule exists outside every `@layer` with the exact `:is(...) :is(...)` selector and `background-color: hsl(var(--bg-nest-2))`; no new `border` declaration appears in the changed blocks; the test PRINTS `NEST-STEPS #F8F8FD #EEF1F6 #E6EBF4` and `VERDICT: NESTING-OK` only when every arm holds; the difference control runs the same arms on `git show 3509eae8:src/index.css` and it must FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes RV-b-1) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB8N1-AC1" cell_refs="RV-n-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~25; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-8-n1.nesting.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: NESTING-OK</expect></criterion>
`RB8N1-AC1` -- the two nest tokens carry the exact triples, the four item-container grounds read the first silver and the general space the panel tone, the second-layer rule exists unlayered with the exact selector, the difference control fails on the base text, and the test prints `VERDICT: NESTING-OK` only when every arm holds.

<criterion id="RB8N1-AC2" cell_refs="RV-n-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~25; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb8n1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB8N1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB8N1-AC3" cell_refs="RV-n-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~25; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB8N1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/` and `src/ui/components/modal/` passes: the summary line reads `0 fail`.

<expected_criteria>RB8N1-AC1, RB8N1-AC2, RB8N1-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 1 @f9e30c80d9, cell `RV-n-1`.
<owned_cells>RV-n-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB8N1-AC1, RB8N1-AC2, RB8N1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~25/DSGN_RBNDV2.TO-RV-n-1.nesting-silver.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB8N1-AC1,RB8N1-AC2,RB8N1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W25-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 1 -- this cell and its sibling both write portal/src/index.css, so they are spawned one after the other, each after the previous merge (the gate allows the shared path; the serialization is the issuer's); the files were read at the feature tip 3509eae8.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~25, direct act (round-less, one cell, LOCAL, about 30 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 25 --portal-ref feature/dsgn-rbndv2-light` after the previous cell merges; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md`.
