# AMGT_RESAPP task order -- `AMGT-rl-2` -- THE PAGE SHELL AND THE IDENTITY HEADER: one band in each mode, the sticky wrapper gone, seven labelled tiles with their provenance one hover away

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~131</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Harness renders through react-dom/server; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~131`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and `test -d org && test -d .tools && echo TREE-OK`;
then `test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (it must exist -- if it does not, that is a BLOCKING
row and you stop). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~131;`. **NEVER RUN AN INSTALL.**
Never push, merge, rebase, `checkout --` or `clean`. **No vite dev server on this cell** -- your proofs render through
`react-dom/server` harnesses; the issuer runs the browser instrument at the drain.

**The portal is a NESTED repository at `<worktree>/portal`.** Portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~131 <0.9.0_WK_AMGT_RESAPP~131@opal.agent>" -F <msgfile> -- <portal paths>`),
then the outer commit from the worktree root carries `portal` (the gitlink) and your deliverables. Messages PURE ASCII via
the Write tool. Scripts and logs under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~131/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-2` (round 37, decomposition s.45)

Two outcomes, both RENDER outcomes, both graded by a person on the PNG and by the instrument on the JSON:

- **`FWD-21` (its band half):** *"A PM opens BA_US_Equity and reads the Thesis ON ONE SCREEN under ONE dark band ...
  bandContainersTopLevel == 1, the identity header is that band, the tab panels are white hairline panels."* TODAY:
  four stacked bands on the Thesis state (the Lead Panel's `Panel variant="mixed"`, the tab body's own `mixed` panels), a
  `sticky top-0 z-40` wrapper measured INERT (0 px covered) and recommended removed.
- **`FWD-22`:** *"price, market cap, net debt, enterprise value, beta and short interest render as Stat tiles with units
  and tabular numerals, and each tile's tooltip carries the mnemonic and full-precision value verbatim."* TODAY: 14 rows
  of `161867780096.00003 ABSOLUTE CUR_MKT_CAP` in the overlay's list.

**F1 is RESOLVED by Andrew ~04:5xZ (brief Part VII): in Universe mode the Lead Panel is the page's ONE band; in Security
mode the IDENTITY HEADER is the ONE band and the discovery band is not rendered.** Every other container on the page is a
white hairline panel (`Panel variant="nested"`, or `"heatmap"` for a table). The five tabs stay in their ratified order
(Thesis, Exec Management, Peers, Model, Posture); no tab moves; no route or DTO moves (`C-PRESENTATION-ONLY`).

## 2. WHAT YOU BUILD (portal, relative to `portal/`)

**(1) `src/pages/SecurityAnalysis/SecurityAnalysis.tsx` -- the shell decides the mode.** In UNIVERSE mode (no selected
security) render `<LeadPanel ...>` exactly as today (it is another cell's file and stays the band). In SECURITY mode
(`state.selectedSecurityKey` set) render the new `IdentityHeader` (below) instead of `LeadPanel`, then the tab bar, then
the active tab. Remove the `sticky top-0 z-40` wrapper entirely. The tab content wrapper carries no dark class. The
Print/Export action stays in `PageHeaderCleanBadge`'s `actions` slot (another cell rebuilds it; do not touch it).

**(2) `src/pages/SecurityAnalysis/components/SecurityOverlay.tsx` -- becomes the IDENTITY HEADER, the one band in Security
mode.** Export `IdentityHeader` (keep the `SecurityOverlay` export name as an alias so the harnesses' imports resolve). It
is the ONE `Panel variant="mixed"` (band) in Security mode and it reads the SAME `/overlay` bundle the overlay reads today
(`identity`, `header_figures`, `description`, `feed`, `posture`, `bloomberg_session_state`, `axis_reads`): LEFT the display
ticker (`identity.display_ticker`, never the path segment; an UNRESOLVED identity says so in place of the name -- AMGT-rj-1
is KEPT), the name, sector, country, and the crosswalk vintage as a footnote (11px); RIGHT "Back to universe" as a
SECONDARY button (navy on white, 3px radius) calling the page's clear-selection, and "Refresh" as the ONE primary action
(the only `#5F3BE3` fill in Security mode -- C8). BELOW: a row of **seven `StatTile`s** -- price, market cap, enterprise
value, net debt, beta, short interest, average volume -- each showing a FORMATTED value with its unit (`$1.62T`, `1.05`,
`2.1%`, `4.3M`), numerals tabular (C2), and a `DataTooltip` (from `@/components/DataTooltip`, read-only import) carrying
the FULL `ProvenanceLine` (value at full precision, unit, mnemonic, definition, vintage, source) VERBATIM. A figure the
payload does not carry renders the tile in its ABSENT state ("not carried on this payload") -- **never computed, never
guessed** (`C-PRESENTATION-ONLY`; value-must-carry-its-claim). Then the description sentence with a navy outline
"machine" chip (label size, 2px radius) where the payload marks it machine, the posture line as today, the feed as a
three-item list with "Expand" (the Dashboard's Bullish/Bearish shape), and the two axis captions folded into ONE footnote
"On today's rankings: ...". The Bloomberg session badge stays visible (DESIGN_SPEC S2) as an icon beside band ink, never
defaulting to CONNECTED.

**(3) `src/pages/SecurityAnalysis/components/StatTile.tsx` -- NEW, local to the page.** `portal/src/ui/components/Stat.tsx`
is `bg-zinc-900 text-white` (a dark idiom) and is NOT edited; this tile is white-panel: label 13px/700 navy, value 14px/400
tabular navy, unit at footnote size, `data-stat-tile="<mnemonic>"`, `data-stat-state="SERVED|ABSENT"`, 4px radius, no shadow.

**(4) The shared atoms the header and the tabs use -- INVERTED under C5:** `IdentityLine.tsx` (4 idioms),
`ProvenanceLine.tsx` (3), `GenerationCaption.tsx` (1), `CheckFaceBadge.tsx` (8): navy ink on white, status as an icon beside
navy text, opacity 1.0, nothing below 11px, weights 400/700, radii 2/3/4/pill. Their PROPS and exports do not change (the
tab cells render them unchanged). `HeaderBrief.tsx` (12) is folded into the identity header or inverted in place -- your
call, stated in your report. `constants.ts`, `figureIdentity.ts`, `refusalPresentation.ts`, `readCompleteness.ts`,
`index.ts`: inverted where they carry a class string; otherwise untouched.

**(5) `__rendercheck__/renderCheck.tsx`** -- its `readColourLaw()` asserts the OLD law (light text only inside a dark
container). Invert the assertion to the contract: a band-valued container appears at most ONCE at top level per render, and
light-on-dark idioms appear ONLY inside it. **(6) `__harness__/tabs.harness.cjs`** -- keep it running; amend only the band
assertions it makes about the header (it is yours); its `exec_officers_rendered` arm belongs to another cell's component
and is reported as-is.

**(7) `__harness__/shell.harness.cjs` -- NEW.** Same loader as `tabs.harness.cjs` (actual components, installed typescript,
`react-dom/server`, hooks stubbed with `tabsFixture.BA_US_Equity.json`'s `overlay`). It renders the shell in BOTH modes and
CHECKS, printing `CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n` at the end:
`universe_band_count` == 1 (one `dark-band`/mixed Panel in the markup, the Lead Panel's) · `security_band_count` == 1 (the
identity header's, and NO LeadPanel band in the markup) · `sticky_wrapper_absent` == true (`sticky top-0` absent from both
renders) · `stat_tiles` == 7 (seven `[data-stat-tile]`, each with a non-empty formatted value or `data-stat-state="ABSENT"`)
· `tooltip_carries_provenance` == true (each SERVED tile's tooltip markup contains the mnemonic AND the raw value from the
fixture, e.g. `CUR_MKT_CAP` and `161867780096.00003`) · `primary_actions_security` == 1 (exactly one `#5F3BE3`/indigo fill
class in the Security render, on Refresh) · `back_to_universe_present` == true · `identity_unresolved_rendered` == true
(a second render with an UNRESOLVED identity fixture shows the UNRESOLVED sentence in place of the name) · `feed_expand`
== true (three items and an Expand affordance) · `axis_footnote` == 1 ("On today's rankings:" once).

## 3. BOUNDS

1. **Files you may write are exactly the `<paths>` below.** `tabs/*.tsx`, `LeadPanel.tsx`, `RankedList.tsx`, `RankedChart.tsx`,
   `StarredList.tsx`, `PrintExportAction.tsx`, `cscTable.ts`, `modelSheet.ts`, `postureCites.ts`, `ThesisDriverChart.tsx` are
   OTHER cells' files this round -- do not touch them; if the shell needs a change there, file a row and stop on that item.
   `src/ui/**`, `src/components/**`, `src/api/**` are read-only.
2. **The contract is `portal/DESIGN.md` C1-C12.** No size below 11px; weights 400/700 only; radii 2/3/4 or pill; no
   `box-shadow` but the focus ring; navy ink; `#6B7280` secondary text on a panel only; status colour never as text on a
   light ground (C6/C9); every empty state one of `PanelEmpty`/`PanelLoading`/`PanelError`/`PanelNoPermission` from
   `@/ui/components/states` (C12) -- the header with no bundle renders `PanelLoading` while loading and `PanelError` with the
   cause when the read failed, never a blank band.
3. **What is KEPT:** the identity block's semantics (AMGT-rj-1), the three-state reads, the generation caption's FACTS, the
   session badge's three states, the machine marking. The spec changes how these are shown, never whether.
4. **No route, DTO, query key or served figure moves.** A figure the tiles need that `/overlay` does not carry is a
   SERVED-RUNTIME ASK: record it in your report and render ABSENT.
5. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do not
   rescue:** a criterion you cannot satisfy as written is refused with its measurement.

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/figureIdentity.ts
portal/src/pages/SecurityAnalysis/refusalPresentation.ts
portal/src/pages/SecurityAnalysis/readCompleteness.ts
portal/src/pages/SecurityAnalysis/index.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
portal/src/components/DataTooltip.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~131/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

`types.ts` is read-only for you except an ADDITIVE export the tile needs; every other cell reads it too, so no existing
type changes shape.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/shell.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 10 of 10 with each CHECK line printed -- universe_band_count 1, security_band_count 1, sticky_wrapper_absent true, stat_tiles 7, tooltip_carries_provenance true, primary_actions_security 1, back_to_universe_present true, identity_unresolved_rendered true, feed_expand true, axis_footnote 1. A missing check line, or any CHECK reading other than its expected value, FAILS</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/SecurityAnalysis.tsx src/pages/SecurityAnalysis/components/SecurityOverlay.tsx src/pages/SecurityAnalysis/components/HeaderBrief.tsx src/pages/SecurityAnalysis/components/IdentityLine.tsx src/pages/SecurityAnalysis/components/ProvenanceLine.tsx src/pages/SecurityAnalysis/components/GenerationCaption.tsx src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx src/pages/SecurityAnalysis/components/StatTile.tsx src/pages/SecurityAnalysis/constants.ts src/pages/SecurityAnalysis/figureIdentity.ts src/pages/SecurityAnalysis/refusalPresentation.ts src/pages/SecurityAnalysis/readCompleteness.ts src/pages/SecurityAnalysis/index.ts</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES: FILES 13 TOTAL 0 -- every one of the 13 lines reads idiom=0 size=0 weight=0 radius=0 shadow=0. The walk counted 50 idioms across these files before this cell (SecurityOverlay 22, HeaderBrief 12, CheckFaceBadge 8, IdentityLine 4, ProvenanceLine 3, GenerationCaption 1); a non-zero line names the file and is a FAIL, not a rounding</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs; echo "exit=$?"</invocation><expect>THE SHARED HARNESS STILL RENDERS THE HEADER AND FIVE TABS: every CHECK line printed; every check reads its expected value EXCEPT exec_officers_rendered, which is reported AS-IS (it read false at DEV HEAD c1ac41ec before this round and belongs to the Exec Management cell's component, not to this file). A new WRONG-WAY check other than exec_officers_rendered FAILS this criterion</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~131/AMGT_RESAPP.TO-AMGT-rl-2.shell-and-identity-header.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** what
you did with `HeaderBrief.tsx`, every figure the seven tiles could not find on the `/overlay` payload (the SERVED-RUNTIME
ASK list, possibly empty), the two commit hashes, and any row you filed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. Interface with rl-8 (Lead Panel): from this cell on, `LeadPanel` is
rendered in UNIVERSE mode only; rl-8 strips its Security-mode branch (the overlay) as dead code. Neither cell edits the
other's file; the drain's `tsc` is the meet. `types.ts` is shared read-only with one additive export admitted here so the
tile's props type has a home; every other cell treats it as read-only.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~08:4xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-37-131).
shell.harness.cjs CHECKS-OK 10 of 10; ui-class-census FILES 13 TOTAL 0; tabs.harness.cjs 19 of 20 with exec_officers_rendered
the criterion's own named exemption (rl-4's component, fixed on wk-AMGT_RESAPP-133). No rows. Drained @973dc1cf5d; portal DEV
ce3c907a (merge of e7f3ca49), gitlink 0b49bb2e -> ce3c907a. Drain-time ui-contract-check (contract-check-after-rl-2/): still FAIL
as expected mid-wave -- bandContainersTopLevel moved thesis 4 -> 3 and exec/peers/model/posture 3 -> 2 (the tabs' own dark panels
are later cells); weights/sizes/radii/shadows/purpleFills unchanged (rl-8 + rl-9 surfaces). The PASS is owed by rl-9's re-assert.

<status>complete</status>
<round>37</round>
<slot>~131</slot>
<fabric>site-z</fabric>
