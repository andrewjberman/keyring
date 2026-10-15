# TO DSGN_RBNDV2.TO-RV-w-1 -- FWD-3/FWD-5: the white-alpha classes map to ink inside every light surface, exactly, and an action-fill chip keeps its white text

<to_id>DSGN_RBNDV2.TO-RV-w-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~12</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-w-1` (decomp v4 @32026f852d) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 1) | **slot:** ~12, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-w-1` -- inside every light surface (`[data-panel-surface="light"]`, carried by each `Panel` and each `ModalFrame` root) the page bodies written for a dark ground use `text-white/N`, `border-white/N` and `bg-white/N` classes. The rule that makes them readable on white is in `portal/src/index.css` (the block headed "DSGN_RBNDV2 RB-t-1 -- THE ONE LEGIBILITY RULE FOR A LIGHT PANEL", about lines 546 to 555):

```
[data-panel-surface="light"] .text-white,
[data-panel-surface="light"] [class*="text-white/"]:not([class*=":text-white/"]) { color: var(--rb-ink); }
[data-panel-surface="light"] [class*="border-white/"]:not([class*=":border-white/"]) { border-color: var(--rb-rule); }
[data-panel-surface="light"] [class*="bg-white/"]:not([class*=":bg-white/"]) { background-color: transparent; }
```

It has two measured defects (live, in the opened modals). (1) The `:not([class*=":text-white/"])` exclusion skips any element whose class list ALSO holds a variant such as `hover:text-white` or `hover:bg-white/10`, so the inactive period chips of the Index Performance modal (`px-2 py-1 text-xs ... bg-white/5 text-white/60 hover:bg-white/...`) keep white at 60 percent on the silver surface (computed `oklab(0.999994 ... / 0.6)`). (2) An ACTIVE chip (`bg-[hsl(var(--primary))] text-white`) is turned navy by the `.text-white` selector and reads navy on violet (about 2.6:1).

**Replace that block** with exact-class selectors (an exact class token is matched with `.text-white\/60`, the slash escaped with a backslash; a variant class is a different token, so it cannot exclude anything), all unlayered, every selector beginning with `[data-panel-surface="light"] `:

- `color: var(--rb-ink)` for `.text-white`, and for `.text-white\/N` for each alpha N in 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95; and the same classes as hover states: `.hover\:text-white:hover` and `.hover\:text-white\/N:hover` (same 19 alphas) also `color: var(--rb-ink)`.
- `border-color: var(--rb-rule)` for `.border-white\/N` (19 alphas) and for `.hover\:border-white\/N:hover`.
- `background-color: transparent` for `.bg-white\/N` (19 alphas); and the hover form `.hover\:bg-white\/N:hover` gets `background-color: var(--rb-row-rule)` (a quiet hover tint, not transparent).
- THE EXCEPTION, written AFTER the rules above so it wins by order at equal or higher specificity: a `text-white` element that also carries a solid action fill stays white: `[data-panel-surface="light"] .bg-\[hsl\(var\(--primary\)\)\].text-white, [data-panel-surface="light"] .bg-\[hsl\(var\(--semantic-action-primary\)\)\].text-white { color: hsl(var(--bg-surface)); }` (`--bg-surface` is the HSL triple of white; read it as `hsl(var(--bg-surface))`, and `--rb-*` tokens are HEX read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`).
- Keep the comment above the rule, updated to say what is true now. Do not touch the `.dark-band` rules, the other `[data-panel-surface="light"]` blocks (the `--palette-*` remap, the inner-surface token remap), any chart colour, or anything outside the scope.

**The existing tests.** `src/__tests__/dsgn-rbndv2/rb-1-t.tokens.test.ts` (round 1) asserts the legibility rule's shape and may name the selectors you replace: update ONLY the arms that name the replaced selectors so they assert the new exact-class shape, and keep its scoping arms (every selector begins with the scope attribute, none sits inside an `@layer`, no unscoped `text-white` selector). `rb-1-r.remap.test.ts` and `rb-1-r2.surfaces.test.ts` must still print their VERDICT. Write the new test described below.

**Out of this cell:** every file except `portal/src/index.css` and the tests under `portal/src/__tests__/dsgn-rbndv2/`.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `cf2bdeaa` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB4W1-AC1" cell_refs="RV-w-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~12; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-4-w1.alpha-sweep.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ALPHA-SWEEP-OK</expect></criterion>
`RB4W1-AC1` -- reading `src/index.css` as text with brace depth and `@layer` nesting tracked: outside every `@layer`, inside the `[data-panel-surface="light"]` scope, a selector exists for `.text-white\/N`, `.border-white\/N` and `.bg-white\/N` for every N in the 19 alphas (5 to 95 in steps of 5) and for the `hover:` form of each (`.hover\:text-white\/N:hover`, `.hover\:border-white\/N:hover`, `.hover\:bg-white\/N:hover`), plus `.text-white` and `.hover\:text-white:hover`; the text and border and background rules set `var(--rb-ink)`, `var(--rb-rule)` and `transparent` (the hover background `var(--rb-row-rule)`); no selector in the file still contains `:not([class*=":text-white/"])`, `:not([class*=":border-white/"])` or `:not([class*=":bg-white/"])`; the action-fill exception rule exists after them and sets `hsl(var(--bg-surface))`; every selector begins with the scope attribute; no text contains `hsl(var(--rb-`; the test PRINTS `SELECTORS-BEFORE <n> SELECTORS-AFTER <m>`, the count of white-alpha selectors in the legibility block at `git show cf2bdeaa:src/index.css` (from the portal root) against the count now; (difference control: the same arms run on that base text must FAIL, proving the test can fail). The test prints `VERDICT: ALPHA-SWEEP-OK` only when every arm holds.

<criterion id="RB4W1-AC2" cell_refs="RV-w-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~12; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB4W1-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` (the tokens, canvas, remap, inner-surfaces and the new sweep tests) passes after your edit: the summary line reads `0 fail`.

<criterion id="RB4W1-AC3" cell_refs="RV-w-1" judgment="true"/>
`RB4W1-AC3` -- graded by the COO's live read at the drain (the computed colour of an inactive period chip in the opened Index Performance modal is navy, not `oklab(... / 0.6)`; an active chip's text on its violet fill is white; the white-alpha text counts before 3, 4, 0 and 0 read again after, in the Index Performance, U.S. Regime, Fear and Greed and Global RSI modals), then the CVO and Andrew (DEC-5), never self-graded. RECORD; no verdict.

<expected_criteria>RB4W1-AC1, RB4W1-AC2, RB4W1-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v4.md</decomp_doc> v4 @32026f852d, cell `RV-w-1`.
<owned_cells>RV-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB4W1-AC1, RB4W1-AC2, RB4W1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~12/DSGN_RBNDV2.TO-RV-w-1.alpha-white-sweep.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB4W1-AC1,RB4W1-AC2,RB4W1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB4W1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W12-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- `portal/src/index.css` measured at the feature tip cf2bdeaa (the legibility block, lines 546 to 555); no other order is open.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~12, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 12 --portal-ref feature/dsgn-rbndv2-light`.
