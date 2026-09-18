# TO DSGN_REBRND.TO-RB-s-4 -- ordered scales -- one hue, ramped light to dark -- EXCEPT WHERE THE COLOUR IS CANON

> **AMENDMENT 1, 2026-09-11, issuer `2.0.0_SA_COO~D`.** This order shipped with a FALSE PREMISE and the
> worker's `RB4-AC4` FAIL is what surfaced it. **The duration ladder is FIRM CANON and is NOT this cell's
> to change.** Andrew-direct, VERBATIM: *"UST orange is canonical and ULT red is canonical"* and, on the
> follow-up, *"all five are canonical, revert and add FactorTilts as the sixth. These are the only colors
> that truly must stay locked in."* Read the AMENDED CELL below; where this amendment and the original
> text disagree, **the amendment wins and the original is the defect.**

> **AMENDMENT 2, 2026-09-14, issuer `2.0.0_SA_COO~D` -- THIS ORDER IS REOPENED (status set back to pending); it is
> NOT re-cut.** Your Amendment-1 work is merged and stands (portal `547d12fd`, workspace `296214fbd4`). Row
> `DSGN_REBRND-W1-S15` asked the issuer to rule which clause governs `ReturnVolatilityScatter`'s `ULT_COLOR` /
> `LT_COLOR`: **THE CANON LOCK GOVERNS.** They paint the ULT and LT halves of the shared benchmark diamond, and before
> this cell they were byte-equal to canon; Andrew locked those rungs everywhere (*"That must remain consistent"*), so
> Amendment 1's KEEP list naming them was the issuer's error and is corrected below.
> **YOUR ACT, AND ONLY THIS:** set `src/components/ReturnVolatilityScatter.tsx:121-122` back to their pre-cell bytes
> at portal `dc1d8020` -- `const ULT_COLOR = '#ef4444'  // Red` and `const LT_COLOR = '#3b82f6'  // Blue` -- touch
> nothing else, then re-run EVERY mechanical criterion below, re-validate and re-commit the proof instance, and flip
> `complete` only when all of them PASS by output.
> **The checker is upgraded by the issuer** (`rb4-canon-check.py`, READ-ONLY to you): ARM A now reads the `primary:`
> line beneath a colourless rung label (row `W1-S17`), and a new ARM E reads rung-named constants (the W1-S15 blind
> spot). Exercised before this amendment on three extracted trees: today's tree -> `CANON-BROKEN` naming exactly
> `ReturnVolatilityScatter.tsx:121` and `:122`; the pre-revert navy tree `0e87cb9f` -> `CANON-BROKEN` now also naming
> the five `MODEL_PORTFOLIO_COLORS` primaries (`:19/28/37/46/55`) that were invisible; today's tree with the two lines
> on canon -> `CANON-INTACT`. Rows `W1-S13` (the retired AC4) and `W1-S17` are disarmed by this amendment; `W1-S14`
> (four writers, one source) and `W1-S16` (legacy names) ride to L10 and ask nothing of you.

<to_id>DSGN_REBRND.TO-RB-s-4</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-4` | **outcome_ref:** FWD-3 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 4

---

## WORKER FACE

### THE CELL

`RB-s-4` -- ordered scales.

⛔ **THE DURATION LADDER IS CANON. REVERT IT, DO NOT RAMP IT.** The original text below called the
ladder's five hues "the defect this cell exists to remove". **That sentence was wrong.** `UST orange /
ST amber / INT green / LT blue / ULT red` are the firm's own convention -- the colours MEAN the models --
and Andrew has locked all five. They are, in his words, *"the only colors that truly must stay locked in."*

**The canonical five, which no act of this order may move:**

| rung | constant | hex |
|---|---|---|
| UST | `PALETTE.orange500` | `#F97316` |
| ST | `PALETTE.amber500` | `#F59E0B` |
| INT | `PALETTE.green500` | `#10B981` |
| LT | `PALETTE.blue500` | `#3B82F6` |
| ULT | `PALETTE.red500` | `#EF4444` |

**YOUR FIRST ACT IS A REVERT.** Commit `0e87cb9f99` moved four writers off canon. Put them back, at the
values above, and leave the fifth alone because it was already right:

| # | writer | state at `0e87cb9f99` | required |
|---|---|---|---|
| 1 | `src/pages/Attribution/constants/holdings-shared.tsx` `PORTFOLIOS` | navy ramp | **REVERT to canon** |
| 2 | `src/pages/Positioning/tabs/HoldingsTab.tsx` `BOOK_COLOR_CYCLE` | navy ramp | **REVERT to canon** |
| 3 | `src/lib/chartColors.ts` `MODEL_COLORS` | navy ramp | **REVERT to canon** (`AGG` keeps `opalIndigo`) |
| 4 | `src/lib/modelPortfolioColors.ts` `MODEL_PORTFOLIO_COLORS` | navy ramp | **REVERT to canon**, aliases included |
| 5 | `src/pages/FactorTilts/constants.ts` | **already canon** | **leave as-is -- this is the sixth writer** |

⚠ **AND FIX THE COMMENTS WHILE YOU ARE THERE.** `modelPortfolioColors.ts` still reads `// Ultra-Long Term
(ULT) - Red` beside a navy hex. Those comments are the TELL that the colour was NAMED deliberately; a
comment that contradicts the value beside it is how the next reader learns the wrong thing.

**What this cell KEEPS.** The original premise survives exactly where firm convention does not reach, and
your ramp work there STANDS -- do not revert it: `--ramp-1..5` in `index.css`, the six `--sentiment-*`
tokens repointed onto it, the `/market` Fear & Greed arc, the EmotionalIntensityMeter gradient and its
score-to-colour function, and the TopicCloud stops. (**AMENDMENT 2:** the two benchmark colours in
`ReturnVolatilityScatter` are REMOVED from this list -- they are the ULT and LT rungs and ARE canon.) None of the rest is canon; the gauge arc was a red-orange-yellow-green
consumer-crypto rainbow encoding a strictly ordered quantity, and that IS a reading error.

⛔ **THE SIXTH WRITER IS `aum.ts`, IT IS IN SCOPE, AND IT IS THE WORST OF THE SIX.**
`src/api/endpoints/aum.ts:1072-1088` -- `getModelColor()` -- keys the same five models by their
**EARLIER NAMES**. Andrew-direct, VERBATIM: *"Those are earlier names, Aggressive is ULT, Conservative is
LT, the rest are obvious"* and *"Conservative is LT which is Blue. That must remain consistent."* All five
are off canon and three are the WRONG HUE ENTIRELY, so today the same model renders one colour on
`/aum` and a different one on `/attribution`:

| legacy key | rung | renders | canon | |
|---|---|---|---|---|
| `'Aggressive'` | ULT | `#f5365c` | `#EF4444` | red, wrong value |
| `'Conservative'` | LT | `#2dce89` | `#3B82F6` | **green where canon is BLUE** |
| `'Intermediate'` | INT | `#5e72e4` | `#10B981` | **purple-blue where canon is GREEN** |
| `'Short-Term'` | ST | `#fb6340` | `#F59E0B` | orange, wrong value |
| `'Ultra Short-Term'` | UST | `#11cdef` | `#F97316` | **teal where canon is ORANGE** |

⚠ **AND THERE IS A SECOND, INDEPENDENT BUG IN THAT FUNCTION -- FIX IT IN THE SAME EDIT.** The lookup is
`modelName.includes(key)` over `Object.entries`, which walks in INSERTION order, and `'Short-Term'` is
inserted BEFORE `'Ultra Short-Term'`. `'Ultra Short-Term'.includes('Short-Term')` is **true**, so every
UST model matches the ST branch first and the teal line is DEAD CODE that has never rendered. Repointing
the five hexes alone would leave UST silently taking ST's colour. **Match on the longest key first, or
match exactly.**

⚠ **DO NOT WIDEN THIS INTO A RENAME.** Andrew: *"I thought we had already scanned through and changed any
old names to the new ones but im not surprised there are little holdouts."* The legacy NAMES are a
separate question with its own blast radius (`getModelColor` is called with names from the API, so
renaming the keys without knowing what the API sends breaks the lookup). **This order fixes the COLOURS
and the shadowing bug. The name holdouts are an OBSERVATION row for L10.**

**Andrew's constraint binds and it cuts BOTH ways.** Chart series that are NOT ordered **keep their colour**. Do not desaturate a categorical palette in the name of this cell. What changes is only what encodes an ORDER.

**The test that matters: legend-covered, the order is still readable.** If a reader must consult a legend to know which end is "more", the ramp has failed.

### ACCEPTANCE

<criterion id="RB4-AC1" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB4-AC2" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-4_positioning_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC2` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB4-AC3" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-4_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC3` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB4-AC4" cell_refs="RB-s-4"><invocation>cd <WS> && timeout 120 python -c "import pathlib,re; files=[p for p in pathlib.Path('portal/src').rglob('*.tsx') if re.search(r'\\bUST\\b',p.read_text(encoding='utf-8',errors='replace')) and re.search(r'\\bULT\\b',p.read_text(encoding='utf-8',errors='replace'))]; hues=set(); [hues.update(re.findall(r'(?:text|bg|border|fill|stroke)-(red|orange|amber|yellow|lime|green|emerald|teal|cyan|blue|indigo|violet|purple|fuchsia|pink|rose)-\\d{2,3}', p.read_text(encoding='utf-8',errors='replace'))) for p in files]; print('LADDER-FILES:',len(files),'DISTINCT-HUES:',len(hues),sorted(hues)); print('VERDICT:','ONE-HUE' if len(hues)<=1 else 'MULTI-HUE')"</invocation><expect>VERDICT: ONE-HUE</expect></criterion>
`RB4-AC4` -- **RETIRED BY AMENDMENT 1. DO NOT RUN IT AND DO NOT TRY TO SATISFY IT.** It counted Tailwind
class tokens (`text-red-500` and kin) across every `.tsx` naming `UST` and `ULT`. The ladder is encoded as
**hex constants**, so all 113 occurrences it counted were OTHER colours -- categorical column groups,
sign/diverging, status -- and **zero were the ladder**. Its domain and its subject did not intersect, so
it could not have differed had the claim been false, and the only way to drive it green was to desaturate
the categorical palettes this same order FORBIDS touching. The worker recorded `FAIL` rather than
reinterpreting the verdict or editing a palette to turn a criterion green; that was correct on both counts.
Replaced by `RB4-AC4R` and `RB4-AC6` below.

<criterion id="RB4-AC4R" cell_refs="RB-s-4"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-canon-check.py</invocation><expect>VERDICT: CANON-INTACT</expect></criterion>
`RB4-AC4R` -- **the canonical duration ladder is intact at every site.** Two arms, because the ladder is
written in two grammars and an instrument reading only one certifies the other clean while it is broken:
ARM A reads rung-LABELLED sites (`id: 'UST'`, `name: 'Ultra-Short Term'`); ARM B reads the POSITIONAL
writers (`BOOK_COLOR_CYCLE`, `MODEL_COLORS`) that carry no rung token at all -- and `BOOK_COLOR_CYCLE` is
the writer that actually renders the `/positioning` chips. Every off-canon line prints with its file, line,
rung, actual and expected value. **Exercised by the issuer on three trees before issue:** canon tree ->
`CANON-INTACT`; the navy tree -> `CANON-BROKEN` naming all 13 off-canon lines plus both positional writers;
a tree with no `portal/` -> `CANON-BROKEN`, so an empty sweep cannot score as a clean pass.
**AMENDMENT 2 -- FIVE GRAMMARS NOW, NOT FOUR.** The worker proved two blind spots by experiment (rows W1-S15, W1-S17):
a rung label whose colour sits on a later `primary:` line, and a constant named for its rung (`const ULT_COLOR =`).
Both are read now -- ARM A's lookahead and ARM E -- and the output prints how many sites each found, so a zero is
visible rather than silent. Exercises are in the Amendment 2 note at the top of this order.

<criterion id="RB4-AC6" cell_refs="RB-s-4"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-ramp-check.py</invocation><expect>VERDICT: ONE-HUE-RAMPED</expect></criterion>
`RB4-AC6` -- **the NON-canonical ordered scales are on one hue.** `--ramp-1..5` declarations all agree on a
single hue number, and all six `--sentiment-*` tokens resolve to a ramp step rather than to the old
rainbow. This is the half of the original premise that survives, and your existing work already satisfies
it -- **exercised by the issuer: the current tree -> `ONE-HUE-RAMPED`, the pre-cell tree ->
`RAINBOW-REMAINS` naming all six off-ramp tokens.** Do not revert it to get `RB4-AC4R` green; the two are
independent and both must pass.

<criterion id="RB4-AC5" cell_refs="RB-s-4" judgment="true"/>
`RB4-AC5` -- graded at L9 from the PNGs: each ordered quantity uses ONE hue ramped light to dark; with the legend covered the order is readable; the gauge arc is a ramp, not a rainbow; and chart series that are NOT ordered still carry their colour. RECORD; NO VERDICT.

<expected_criteria>RB4-AC1, RB4-AC2, RB4-AC3, RB4-AC4R, RB4-AC5, RB4-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Do not touch a categorical palette.** Only encodings of ORDER change.
- ⛔ **THE CANON LOCK (AMENDMENT 1).** `UST #F97316 / ST #F59E0B / INT #10B981 / LT #3B82F6 / ULT #EF4444`
  are locked by Andrew and are the ONLY locked colours in this round -- *"These are the only colors that
  truly must stay locked in."* Everything else in this cell remains yours to move. **The lock covers
  ORDER as well as value:** *"They must always be listed in the same order with same colors, it is
  duration order, UST ST INT LT ULT. Always this way, left to right"* -- *"or top to bottom if in a
  vertical context."* Declaration sequence is the reading axis on either orientation, so one rule covers
  both, and `RB4-AC4R` ARM D grades it on every ordered ARRAY. A keyed lookup `Record` is EXEMPT because
  its declaration order does not render; the checker PRINTS that exemption rather than passing silently.
- `deck_generation/DESIGN_BIBLE.md` is PRECEDENT and is READ-ONLY here.

<paths>
portal/src/
portal/src/index.css
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-canon-check.py
org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-ramp-check.py
</paths>

> The two checkers are READ-ONLY to you and are ISSUER artifacts -- they are named here because
> `<paths>` must cover every file the worker READS as well as every file it writes. Do not edit them to
> make a criterion pass; a checker you had to edit is a finding, and findings are rows.

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-4`.
<owned_cells>RB-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids (AMENDMENT 1a -- the id list now matches `<expected_criteria>`; the retired `RB4-AC4` is NOT an
acceptance row): `RB4-AC1`, `RB4-AC2`, `RB4-AC3`, `RB4-AC4R`, `RB4-AC5`, `RB4-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`) -- REWRITE the prior instance, which carried the retired
`RB4-AC4` FAIL -- validated with
`python .tools/proof-of-spec-check.py <instance> RB4-AC1,RB4-AC2,RB4-AC3,RB4-AC4R,RB4-AC5,RB4-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `ordered-scales.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- 3 gates registered for this project (FWD-9's grade half, Andrew's; the brief's Appendix A prose defect; comp-adversary's false-GONE path parser). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: an AWS-surface token sweep returned 0 hits over the PRD's SURFACE MANIFEST and 0 over the whole PRD. No cell writes an AWS surface.
comp-adversary: RUN at L5 on the PRD -- 3 of 3 cited commits verified; 19 paths, 16 stable, 3 GONE all resolved (one is the register's own dangling D13 doc, one is `portal/DESIGN.md` correctly absent on CLOUD, one is a FALSE GONE from the tool's path parser). Blindness stated: its complement is filesystem adjacency, not the dependency chain.
lane: the `<paths>` block IS the grant (RULING 1). `design/` resolves UNDEFINED in `.owned-paths.yaml` for every agent -- a refusal there is a BLOCKING row, never an override.
</preflight>

Seating: slot ~1, queue position 4; fresh worktree pair branched from `feature/d13-visual-elevation`.
