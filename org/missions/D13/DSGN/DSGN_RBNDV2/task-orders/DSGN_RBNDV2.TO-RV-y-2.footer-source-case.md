# TO DSGN_RBNDV2.TO-RV-y-2 -- FWD-3, FWD-5: every footer source name reads in proper capitalization

<to_id>DSGN_RBNDV2.TO-RV-y-2</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~20</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>6</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-y-2` (decomp v6 @e4848abcad) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 2) | **slot:** ~20, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-y-2` -- Andrew: "Footers of all panels and modals need proper capitalization". Round 5 removed the forced uppercase from `PanelFooter.tsx`, so a footer now reads its source string as written, and two strings are written in the wrong case: `portal/src/components/market-performance/SentimentGauge.tsx` line 128 `footnote: 'Source: Global news.'` and `portal/src/components/market-performance/ExecutiveSummary.tsx` lines 245 and 264 `'Source: Financial news.'` (a source name is a proper name: "Global News", "Financial News"). **Fix the class, not the two strings:** sweep every footer source string in the portal.

**Sweep.** From the portal root run `git grep -n -E "Source: |Sources: " -- 'src/*.tsx' 'src/*.ts' ':!*__tests__*'` and read every line that is a footer string (a `footnote:`, `content="Source: ..."`, `source = '...'`, a `Source:` string in a modal footer, or a template literal building one such as `Source: ${...}.`); ignore code comments, file header comments and API docs. For each footer string apply this rule: in the source name after `Source: `, every word starts with a capital letter, except the small words `and`, `or`, `of`, `the`, `via`, `for`, `by`, `on`, `more` which stay lower case, and acronyms and brand names stay as written (Bloomberg, CNN, CNBC, SS&C Black Diamond Wealth Solutions). Fix every string that breaks the rule. Also read how a template literal builds its names (for example `formatSourcesForFootnote` in `portal/src/lib/sourceRanking.ts` is read-only for you; if it can output a lower-case source name, write a surprise row naming the line, do not edit it).

**Write the list.** Create `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~20/FOOTER_SOURCE_LIST.md`: one table row per footer string found, columns `file | line | before | after`, `after` equal to `before` when it already obeyed the rule, and a summary line `FOOTER-STRINGS <n> CHANGED <k>`.

**Test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-6-y2.footer-source-case.test.ts`: it walks every non-test `.ts` and `.tsx` file under `src`, extracts each string literal that begins `Source: ` or `Sources: ` (single quote, double quote or backtick, not inside a `//` or `*` comment line), applies the capitalization rule above to the part after `Source: ` up to the final period (a `${...}` placeholder is skipped), and requires zero violations; it PRINTS `FOOTER-STRINGS <n> VIOLATIONS-BEFORE <b> VIOLATIONS-AFTER <a>` (the before computed from `git show d0cb67d0:<file>` for the files that changed) and `VERDICT: FOOTER-SOURCE-CASE-OK` only when VIOLATIONS-AFTER is 0; the difference control runs the same checker on the base text of `SentimentGauge.tsx` and it must report at least one violation.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave in round 5: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `d0cb67d0` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB6Y2-AC1" cell_refs="RV-y-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~20; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-6-y2.footer-source-case.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FOOTER-SOURCE-CASE-OK</expect></criterion>
`RB6Y2-AC1` -- the sweep finds every footer source string, no string breaks the capitalization rule after the edit, the before and after violation counts print, the difference control reports a violation on the base text of `SentimentGauge.tsx`, and the test prints `VERDICT: FOOTER-SOURCE-CASE-OK` only when VIOLATIONS-AFTER is 0.

<criterion id="RB6Y2-AC2" cell_refs="RV-y-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~20; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB6Y2-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB6Y2-AC3" cell_refs="RV-y-2" judgment="true"/>
`RB6Y2-AC3` -- graded by the COO's live read at the drain, then the CVO and Andrew (DEC-5), never self-graded: the Daily Cloud footer on Market Overview reads 'Source: Global News.' and the Trending Topics footer ends with proper-case source names. RECORD; no verdict.

<expected_criteria>RB6Y2-AC1, RB6Y2-AC2, RB6Y2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/SentimentGauge.tsx
portal/src/components/market-performance/ExecutiveSummary.tsx
portal/src/components/CategoryViewTree.tsx
portal/src/components/ReturnVolatilityScatter.tsx
portal/src/pages/
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v6.md</decomp_doc> v6 @e4848abcad, cell `RV-y-2`.
<owned_cells>RV-y-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB6Y2-AC1, RB6Y2-AC2, RB6Y2-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~20/DSGN_RBNDV2.TO-RV-y-2.footer-source-case.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB6Y2-AC1,RB6Y2-AC2,RB6Y2-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB6Y2-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W20-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v6 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip d0cb67d0.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~20, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 20 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md; CTO analysis ledger/ROUND_ANALYSIS.round5.md`.
