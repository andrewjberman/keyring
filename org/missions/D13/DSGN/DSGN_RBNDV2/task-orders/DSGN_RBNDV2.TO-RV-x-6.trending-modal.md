# TO DSGN_RBNDV2.TO-RV-x-6 -- FWD-2, FWD-5: the Trending Topics detail modal is light on the shared frame and the tile arrows keep white on their fill

<to_id>DSGN_RBNDV2.TO-RV-x-6</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~18</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-x-6` (decomp v5 @f4c4268583) | **outcome_ref:** FWD-2, FWD-5 | **depends_on:** -- (chain 6) | **slot:** ~18, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-x-6` -- Andrew: "The modal popup for the 'Trending Topics' panel needs to be done in light mode as well" and "The trend arrow in the image should be white".

**The popup.** In `portal/src/components/market-performance/ExecutiveSummary.tsx`, `DrilldownModal` (about lines 731-975) is the one modal still on its own dark overlay: its root is `fixed inset-0 z-[100] ... bg-black/60 backdrop-blur-sm`, it carries its own close button (about line 782) and its own footer ("Sentiment: LLM analysis (-1.0 bearish to +1.0 bullish)" and a Close button, about lines 958-970). Move it onto the shared frame: read `portal/src/ui/components/modal/README.md` and `portal/src/ui/components/modal/ModalFrame.tsx`, and mirror how `portal/src/components/market-performance/IndexPerformanceModal.tsx` adopts `ModalFrame` (props for the title, close, body and `footer`). Keep every piece of content (the hero tile, the sentiment chip and score, the topic title, the context bullets, the source articles list with its more link, the footer note and Close action) and its behaviour (open, close on Escape or backdrop through the frame, the article links). Remove the own overlay, the own close button and the `backdrop-blur`. Inside the frame the stylesheet rule turns the old `text-white*` classes to ink; leave those classes as they are.

**The marker for white-on-colour.** A coloured gradient tile must keep white content. Add the attribute `data-ink="on-fill"` to (a) the tile element that holds the trend arrow in the panel's `TrendIcon` tile (about lines 1053-1090, the element that carries the gradient fill and the `w-12 h-12 text-white` icon) and (b) the hero element of the popup (the gradient block that holds the `w-24 h-24 text-white` arrow svg and the source chips). Another cell adds the stylesheet rule that keeps `text-white` white inside an element marked `data-ink="on-fill"`; this cell only adds the attribute. In the hero, the source chips `bg-black/50 text-white/...` stay as they are.

**Test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-5-x6.trending-modal.test.ts`, reading `ExecutiveSummary.tsx` as text: it imports `ModalFrame`; it holds no `fixed inset-0`, no `backdrop-blur` and no `bg-black/60`; `data-ink="on-fill"` occurs at least twice; the footer note `Sentiment:` is still present; the test PRINTS `DRILLDOWN-OWN-OVERLAY-BEFORE <n> DRILLDOWN-OWN-OVERLAY-AFTER <m>` (the count of `fixed inset-0` in `git show 7f8731df:src/components/market-performance/ExecutiveSummary.tsx` against now) and `VERDICT: TRENDING-MODAL-OK` only when every arm holds; the difference control runs the same arms on the base text and they must FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave for this round: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `7f8731df` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB5X6-AC1" cell_refs="RV-x-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~18; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-5-x6.trending-modal.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TRENDING-MODAL-OK</expect></criterion>
`RB5X6-AC1` -- `ExecutiveSummary.tsx` imports `ModalFrame`, holds no `fixed inset-0`, no `backdrop-blur` and no `bg-black/60`, carries `data-ink="on-fill"` at least twice and keeps the `Sentiment:` footer note; the before and after counts print; the difference control fails on the base text; the test prints `VERDICT: TRENDING-MODAL-OK` only when every arm holds.

<criterion id="RB5X6-AC2" cell_refs="RV-x-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~18; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB5X6-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB5X6-AC3" cell_refs="RV-x-6" judgment="true"/>
`RB5X6-AC3` -- graded by the COO's live read at the drain, then the CVO and Andrew (DEC-5), never self-graded: pressing a Trending Topics row opens a dialog on the light frame (white surface, silver edge, square close) with its title, bullets, source articles and footer legible in dark ink; the tile arrow reads white on its gradient once the stylesheet rule of the other cell is merged. RECORD; no verdict.

<expected_criteria>RB5X6-AC1, RB5X6-AC2, RB5X6-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v5.md</decomp_doc> v5 @f4c4268583, cell `RV-x-6`.
<owned_cells>RV-x-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB5X6-AC1, RB5X6-AC2, RB5X6-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~18/DSGN_RBNDV2.TO-RV-x-6.trending-modal.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB5X6-AC1,RB5X6-AC2,RB5X6-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB5X6-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W18-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip 7f8731df.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~18, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 18 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md`.
