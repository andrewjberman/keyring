# TO POSN_ASTTAX.TO-V6-1 -- THE POSITIONING PAGE RENDERS FIVE CLASSES: the order literal, the colour map, the Hedge->Equity fold dropped, one row per class in the summary, the allocation type widened to the five-class keys -- Models and ETFs modes. Committed on the round's ONE drain ref (AT5-s-6, F2; FWD-3/FWD-4/FWD-6)

<to_id>POSN_ASTTAX.TO-V6-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~22</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-POSITIONING-ONLY, s.3 the five classes in order) - **Decomp cell:** `AT5-s-6` - **Issuance:** round 5, wave 2, same slot as
`TO-V5-1` -- **you start this order only after your `TO-V5-1` is `complete` at HEAD and its branch is drained onto
`refs/drains/posn-5-portal`** (the COO tells you the drained hash when handing you this order). **GATES `AT5-s-7` (F3).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~22`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~22;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Workspace commits via safe-commit.sh under
your serial; portal commits inside `portal/` on YOUR branch. Never push, merge, rebase, `checkout --`, `clean`; never `git add portal`.

## THE PORTAL: START FROM THE DRAIN REF, NOT FROM THE PIN

Your `TO-V5-1` landed the tokens on `refs/drains/posn-5-portal` (`6c0deebd9121d5e955943d5a7507de51a102f480`, the drained hash; verify it with
`git -C portal rev-parse refs/drains/posn-5-portal` -- no fetch: your `portal/` is a LINKED WORKTREE of the same repository and reads
the ref directly). Your worktree's `portal/` is a LINKED WORKTREE of the portal repo, RE-CUT by the COO at hand-over on branch `wk-posn-5-22b-portal` FROM that ref (verify with `git -C portal rev-parse --abbrev-ref HEAD`; do NOT re-create it). Prove BOTH: the ref's tree
contains `ASSET_CLASS.structured` and `ASSET_CLASS.commodities` (`git -C portal show <ref>:src/lib/chartColors.ts`), and
`e85f6eb84f` is an ancestor of it. The gitlink does not move. Append your branch line to `ledger/PORTAL_REFS.md` at your first commit.

## THE CELL

The page is 14 files at the pin (`git ls-tree e85f6eb84f -- src/pages/Positioning`) plus the registry it imports. Measured sites:
- `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:215-219` `ASSET_CLASS_COLORS` = three keys ('Fixed Income', 'Equity', 'Cash')
  -> FIVE via F1's tokens (`ASSET_CLASS.fixedIncome/.equity/.structured/.commodities/.alternatives`), 'Cash' kept as a display
  alias of Fixed Income / Cash; `:1381-1383` the display fold: KEEP `'Cash' -> 'Fixed Income'` (ONE ratified class), DROP
  `'Hedge' -> 'Equity'` (the fold that hid the overlay; after R1 no served value is 'Hedge' at the top level); `:1392`
  `assetClassOrder = ['Fixed Income', 'Equity']` -> the five in the PRD's canonical order (read s.3 at `99cc431075`; never retype
  from here); `:594-595` the FI sort predicate reviewed for the five.
- `portal/src/pages/Positioning/panels/PositioningSummary.tsx:545-546` two hardcoded rows -> one row per ratified class, same order;
  `:627-651` the two-bucket fold (`fixedIncome: fixed_income + cash`, `equity: equity + hedge`) -> five buckets keyed to the served
  five-class allocation (`cash` folds into Fixed Income / Cash; `hedge` no longer exists once B1 is served -- read it as 0 if present
  and say so); `:704-712`, `:840-884` the `{fixedIncome, equity}` render type -> five keys; `:70-71`, `:91` colour lookups from F1.
- `portal/src/pages/Positioning/shared/etfAdapter.ts:105` `ZERO_ALLOCATION = {cash, fixed_income, equity, hedge}` -> the five-class
  keys the served payload carries after B1 (`cash, fixed_income, equity, structured, commodities, alternatives`; keep `hedge`
  OPTIONAL so a pre-B1 payload still parses -- the transition is a state, not a defect).
- `portal/src/api/portal-proxy.ts:969` `export interface PositioningAllocation` -- OUTSIDE the 14 files, IN your grant: widen to the
  five-class keys (`hedge?` optional for the transition).
- `portal/src/pages/Positioning/types.ts` if a five-key shape lives there.
- **ANDREW-DIRECT ~19:5xZ (msg 22910, record @`edbee96c07`), landed in THIS cell because `TO-V5-1` was complete before the word
  arrived:** *"Structured is going to be a pink base, as all volatility/options/overlay etc assets will be grouped into there,
  regardless if its a Fixed Income or an Equity Hedge or etc."* In `portal/src/lib/chartColors.ts` (now in your grant): MINT
  `pink700: '#be185d'` in PALETTE beside `pink600` (`:62` at `6c0deebd91`) and RE-BIND `'Volatility'` (`:311`, blue900 in the
  Equity block) to `PALETTE.pink700` -- a pink-family token distinct from the class base pink500 and from Hedge's pink600; move the
  line beside `'Hedge'` under the Structured-family comment. AND, per PRD v0.8 @`709d7b4221` C-COLOURS (Andrew ~20:2xZ *"b, Options
  Income"*; JEPI's new sub-asset), MINT `pink800: '#9d174d'` and ADD `'Options Income': PALETTE.pink800` beside them -- every
  Structured sub-asset (Hedge, Options Income, Volatility) on its own pink token distinct from pink500. `MIX_PIE` and `RISK_FACTOR_COLORS` (`:492`, a risk factor named
  Volatility) are NOT touched -- the Positioning page imports neither. Contrast is measured by `V6-AC9`; pink700 enters
  `lightBackgrounds` ONLY if white text on it measures below 4.5.
- **THE CLASS MAP HAS NO TEXT-COLOUR GUARD (row W22-S6, disarmed Z-S82):** `ASSET_CLASS.structured` (pink500) reads 3.527:1 under
  white text and `.commodities` (yellow500) 1.918:1, and nothing in chartColors.ts picks text for an ASSET_CLASS value. Every site
  you touch that draws a label over a class colour (the HoldingsTab map at `:215`, the PositioningSummary swatches and rows at
  `:70-71`, `:91`, `:545`) takes its text colour from ONE rule: mint `getAssetClassTextColor(bgHex)` beside `getSubAssetTextColor`
  (same shape, `:319-326`; pink500 and yellow500 in its light set) and call it at each site -- never a per-component literal.
  `V6-AC9` prints the census of ASSET_CLASS consumers under `src/pages/Positioning` and the per-site contrast table.
- **THE SERVED LABEL (B1, `TO-V1-1` amended Z-S78):** once B1 lands, `benchmarks.etf.structured|commodities|alternatives` carry
  `{ticker: null, label: "no benchmark"}`; if PositioningSummary's spread rows (`:213-225`) read a benchmark for a class they
  read that label and never a ticker. State what you observed.

**NOT yours:** `shared/satelliteAdapter.ts` (F3 owns it whole -- it reads `keyof PositioningAllocation` at `:133-159` and will
follow your type), `shared/bookSet.ts`, anything under `src/pages/Attribution/` (Andrew: *"we do not touch Attribution"*).

**The served data at your bar:** the local build (`bun run dev`) proxies `/api/*` to the served plane; after `TO-V1-1`'s deploy the
served `positioning_data.json` carries the five-class allocation keys; before it, only two classes carry weight and the other three
read 0. **Both states render five rows in canonical order** -- a zero row is a row. State which you observed.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W22-S<k>` (continue your sequence), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working. VXX dropping out of
Attribution's groups after R1 is Andrew's ACCEPTED consequence: do not file it.

## CRITERIA -- structured, one clause each

<criterion id="V6-AC1" cell_refs="AT5-s-6"><invocation>timeout 60 git -C portal show refs/drains/posn-5-portal:src/lib/chartColors.ts</invocation><expect>the file at the drain ref contains `structured: PALETTE.pink500` and `commodities: PALETTE.yellow500`, and `git -C portal merge-base --is-ancestor e85f6eb84f refs/drains/posn-5-portal` exits 0 (printed). Otherwise STOP with a row: your premise (F1 drained) is false.</expect></criterion> `V6-AC1` -- THE DEPENDENCY, READ BACK FROM THE REF.

<criterion id="V6-AC2" cell_refs="AT5-s-6"><invocation>timeout 60 git -C portal diff --stat refs/drains/posn-5-portal -- src/pages/Positioning src/api/portal-proxy.ts src/lib/chartColors.ts</invocation><expect>ONLY files inside src/pages/Positioning/ (never satelliteAdapter.ts, never bookSet.ts) plus src/api/portal-proxy.ts and src/lib/chartColors.ts changed (chartColors.ts hunks ONLY at PALETTE, TWO added tokens pink700 and pink800; the Volatility line; the new Options Income line; and the new getAssetClassTextColor function); zero files under src/pages/Attribution/; the hunk headers printed for HoldingsTab.tsx (:215, :1381, :1392), PositioningSummary.tsx (:545, :627), etfAdapter.ts (:105), portal-proxy.ts (:969).</expect></criterion> `V6-AC2` -- THE EDIT, ON EXACTLY THE SITES THE CELL NAMES.

<criterion id="V6-AC3" cell_refs="AT5-s-6"><invocation>timeout 120 node -e "<PRINT_ASSETCLASSORDER_LITERAL_EDITED>"</invocation><expect>both read the five ratified classes in the PRD s.3 canonical order (quoted from `99cc431075`), identical to each other, and the HoldingsTab colour map keys every one of the five to an F1 token (no literal hex).</expect></criterion> `V6-AC3` -- ONE ORDER, ONE COLOUR SOURCE, ON BOTH POSITIONING READERS.

<criterion id="V6-AC4" cell_refs="AT5-s-6"><invocation>timeout 600 bash -c "cd portal && bun run tsc -b"</invocation><expect>exit 0 with the checked-file count printed; POSITIVE CONTROL, REQUIRED: a one-line injected type error fails the same command (error TS printed), then reverted.</expect></criterion> `V6-AC4` -- THE BUILD, WITH AN INSTRUMENT THAT CAN FAIL.

<criterion id="V6-AC5" cell_refs="AT5-s-6"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/v6_models.png --port <PORT>"</invocation><expect>the Models mode screenshot READ (Read tool): LOC printed by the script is the Positioning route (no bounce to /login), five class rows visible in canonical order, one swatch per class, subtotals summing to the total to 0.1; then the same for the ETFs mode (.scratch/v6_etfs.png). State whether the served payload carried five-class weights (post-B1) or zeros for three classes (pre-B1) -- both are valid observations; a MISSING row is not.</expect></criterion> `V6-AC5` -- THE RENDER, READ, NOT CAPTURED.

<criterion id="V6-AC6" cell_refs="AT5-s-6"><invocation>timeout 120 node -e "<RENDERED_DOM_UI_SMOKE>"</invocation><expect>five distinct colours, each EQUAL to the F1 token's hex for that class (pink500 #ec4899 for Structured, yellow500 #eab308 for Commodities, ...), printed as a (class, expected, observed) table with zero mismatches.</expect></criterion> `V6-AC6` -- THE COLOUR ON SCREEN EQUALS THE REGISTRY, PER CLASS.

<criterion id="V6-AC7" cell_refs="AT5-s-6"><invocation>timeout 60 git -C portal log --format='%H %an %s' refs/drains/posn-5-portal..wk-posn-5-22b-portal</invocation><expect>your commit(s) only, authored 0.9.0_WK_POSN_ASTTAX~22; the superproject gitlink UNMOVED read two ways at the worktree root: `git ls-tree HEAD -- portal` prints 160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a portal and `git diff --cached -- portal` is EMPTY (row W22-S2: `git diff --submodule=log` reads the working tree and is non-empty by construction once your commit exists); PORTAL_REFS.md carries your branch line.</expect></criterion> `V6-AC7` -- COMMITTED ON YOUR BRANCH FROM THE REF; THE GITLINK UNMOVED.

<criterion id="V6-AC9" cell_refs="AT5-s-6"><invocation>timeout 120 node -e "<CONTRAST_CHECK_V6>"</invocation><expect>a (site, key, background, text, ratio) table covering (i) Volatility and Options Income on their new pink tokens through getSubAssetTextColor and (ii) EVERY site under src/pages/Positioning that renders text over an ASSET_CLASS value through getAssetClassTextColor -- the census printed as N sites across M files with the denominator (the ASSET_CLASS importers under src/pages/Positioning); every ratio >= 4.5; the text colour obtained by CALLING the file's own functions, never re-implemented; the negative controls printed (white on pink500 = 3.527, white on yellow500 = 1.918) and the instrument's self-test (white/black = 21.0).</expect></criterion> `V6-AC9` -- CONTRAST, THE CLASS MAP INCLUDED.

<criterion id="V6-AC8" cell_refs="AT5-s-6" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether dropping the Hedge->Equity fold while keeping Cash->Fixed Income is the reading of s.3 the PRD intends, and whether the pre-B1 zero rows would mislead a reader who opened the page between the deploy and the retag. Record the readings and offer NO verdict.</expect></criterion> `V6-AC8` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V6-AC1, V6-AC2, V6-AC3, V6-AC4, V6-AC5, V6-AC6, V6-AC7, V6-AC8, V6-AC9</expected_criteria>

<placeholders>CONTRAST_CHECK_V6, PORT, PRINT_ASSETCLASSORDER_LITERAL_EDITED, RENDERED_DOM_UI_SMOKE</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V6-1.the-positioning-page-renders-five-classes.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md
portal/src/pages/Positioning/tabs/HoldingsTab.tsx
portal/src/pages/Positioning/panels/PositioningSummary.tsx
portal/src/pages/Positioning/shared/etfAdapter.ts
portal/src/pages/Positioning/types.ts
portal/src/api/portal-proxy.ts
portal/src/lib/chartColors.ts
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-6`.
<owned_cells>AT5-s-6</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-5` (your TO-V5-1 tokens, on the drain ref); `AT5-s-1` (B1's served five-class keys -- read
at your bar, not required for the build). DOWNSTREAM: `AT5-s-7` (F3, your next order) binds the widened PositioningAllocation type.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source edits inside the frozen submodule; no deploy, no promote, no monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer read the line numbers at the pin e85f6eb84f; after
F1's commit they may shift by a few lines in chartColors.ts only -- the Positioning files are unchanged by F1; (2) the issuer has
not rendered the page on this device since the reboot and does not know whether the ui-smoke auth stub works against today's
served plane -- a bounce to /login is a row, not a retry loop; (3) the issuer has not read how PositioningSummary's benchmark
spread rows (:213-225) treat a class with a labelled-zero benchmark -- if a row reads "10% bet against nothing", say so in a row.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/POSN_ASTTAX.TO-V6-1.the-positioning-page-renders-five-classes.proof_of_spec.json
</proof_of_spec>
