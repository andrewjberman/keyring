# TO DSGN_RBNDV2.TO-RV-g-1 -- FWD-3/FWD-5: the positive and negative colours are darker inside every light surface

<to_id>DSGN_RBNDV2.TO-RV-g-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~24</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-g-1` (decomp v8 addendum 1 @f9e30c80d9) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** RV-b-1 merged (all write src/index.css; cut and spawned one after the other) | **slot:** ~24, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-g-1` -- Andrew: "the red/green canonical colors for positive/negative should be darker if there is a shared color for all those figures, so it stands out better on the light background" and, after the COO's measurement, "rec approved keep going". Measured: the shared pair is `--success` and `--danger` (`portal/src/index.css`: `--success: var(--status-success)` the Argon green #2dce89, `--danger: var(--status-danger)` #f5365c), read as `hsl(var(--success))` and `hsl(var(--danger))` in 38 and 29 source files; the signed figures on `/market` compute to `rgb(45, 205, 136)` (contrast 1.94 to 1 on the panel tone #F8F8FD) and `rgb(251, 112, 132)` (2.56 to 1), far under the 4.5 to 1 text needs.

**Make this one change in `portal/src/index.css` (nothing else):** directly AFTER the inner-surface block `:root [data-panel-surface="light"] { ... }` (the one that re-sets `--bg-medium`, `--bg-card` and the other nested grounds; find it by that selector), add a NEW unlayered block, under a comment that says what is true (the darker positive and negative pair for a light surface, with the two hex values and their contrast on #F8F8FD, and that its selector is `[data-panel-surface="light"]:not(.dark-band *)`, deliberately not `:root [data-panel-surface="light"]` or the bare scope, because `rb-1-r2.surfaces.test.ts` and `rb-1-r.remap.test.ts` pin the number of rules with those two exact selectors; a custom property set directly on the panel root beats the inherited root-level value whatever the selector specificity):
```
[data-panel-surface="light"]:not(.dark-band *) {
  --success: 145 70% 26%;   /* #14713B, 5.74 to 1 on #F8F8FD */
  --danger: 352 75% 42%;    /* #BB1B30, 5.99 to 1 on #F8F8FD */
}
```
A custom property set on the panel root is inherited by everything inside the panel, modal or popup (each carries `data-panel-surface="light"`), so every `hsl(var(--success))` and `hsl(var(--danger))` figure darkens at once with no component edit. Do NOT change the root-level definitions of `--success`, `--danger`, `--status-success` or `--status-danger`, the `--sentiment-*` ramp, any `.dark-band` rule, or any other block. (A dark band is not a light surface and keeps its own colours.)

**ISSUER RULING (2026-10-15 ~20:1xZ, on the worker's BLOCKING row `DSGN_RBNDV2-W24-S1`; amends the selector above):** the selector is `[data-panel-surface="light"]:not(.dark-band *)` everywhere this order names the new block (a light surface that is not inside a dark band; it begins with the scope attribute, so `rb-1-t.tokens.test.ts` arm (b)/(c) holds, and it is not one of the two exact selectors whose rule counts `rb-1-r.remap.test.ts` and `rb-1-r2.surfaces.test.ts` pin). Use it in the CSS block, in its comment (say it begins with the scope attribute because `rb-1-t.tokens.test.ts` requires that, and is neither of the two pinned exact selectors) and in your new test. No existing test is edited.

**Test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-8-g1.signal-pair.test.ts`, reading `src/index.css` as text with `@layer` and brace depth tracked (reuse the reader of `rb-4-w1.alpha-sweep.test.ts`): exactly one rule with the selector `[data-panel-surface="light"]:not(.dark-band *)` declares `--success: 145 70% 26%` and `--danger: 352 75% 42%`, it sits outside every `@layer`, and it declares nothing else; the root-level `--success` and `--danger` definitions are unchanged (`--success: var(--status-success)`, `--danger: var(--status-danger)`); the test PRINTS `SIGNAL-PAIR #14713B #BB1B30` and `VERDICT: SIGNAL-PAIR-OK` only when every arm holds; the difference control runs the same arms on `git show 3509eae8:src/index.css` and it must FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at the feature tip when you were provisioned (it includes RV-b-1) (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB8G1-AC1" cell_refs="RV-g-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~24; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-8-g1.signal-pair.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SIGNAL-PAIR-OK</expect></criterion>
`RB8G1-AC1` -- the scoped block carries the exact two triples outside every `@layer` and nothing else, the root definitions are unchanged, the difference control fails on the base text, and the test prints `VERDICT: SIGNAL-PAIR-OK` only when every arm holds.

<criterion id="RB8G1-AC2" cell_refs="RV-g-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~24; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb8g1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB8G1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB8G1-AC3" cell_refs="RV-g-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~24; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB8G1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/` and `src/ui/components/modal/` passes: the summary line reads `0 fail`.

<expected_criteria>RB8G1-AC1, RB8G1-AC2, RB8G1-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 addendum 1 @f9e30c80d9, cell `RV-g-1`.
<owned_cells>RV-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB8G1-AC1, RB8G1-AC2, RB8G1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~24/DSGN_RBNDV2.TO-RV-g-1.signal-pair.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB8G1-AC1,RB8G1-AC2,RB8G1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W24-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 addendum 1 -- this cell and its sibling both write portal/src/index.css, so they are spawned one after the other, each after the previous merge (the gate allows the shared path; the serialization is the issuer's); the files were read at the feature tip 3509eae8.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~24, direct act (round-less, one cell, LOCAL, about 30 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 24 --portal-ref feature/dsgn-rbndv2-light` after the previous cell merges; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md`.
