# DSGN_AMGTV1 task order -- `AV-t-2` -- THE SECURITY HEADER READS AS FOUR CARDS, EACH OPENING A WINDOW WITH ITS FIGURES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~2</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut -- AC1 reads 1 of 3 arms at the base and 3 of 3 on a scratch reference implementation; AC2 reads 0 of 5 at the base and 5 of 5 on it; AC3 reads 2 of 2 at the base (a bound). Blind spot, stated: static markup with the estate chrome stubbed, so a window opening, contrast and layout are the walk's (AC4).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-t-2` (round 1, the thread's hop 4)

On Security Analysis, a PM opens a name (the thread's name is Valero, `VLO_US_Equity`) and the identity header shows seven
small stat tiles in a row -- too much text (Andrew: "never more than four cards", progressive disclosure, cards that open a
window like the Philosophy page's cards). Replace the seven tiles with **FOUR CARDS**, each leading with one figure and opening
a window with the rest:

| card key | title | figures, in order (figure key -- label -- the `header_figures` mnemonic it reads) |
|---|---|---|
| `price` | Price | `price` Price `PX_LAST`; `market_cap` Market cap `CUR_MKT_CAP`; `avg_volume` Average volume `VOLUME_AVG_30D` |
| `financials` | Financials | `enterprise_value` Enterprise value `CURR_ENTP_VAL`; `net_debt` Net debt `NET_DEBT` |
| `market_features` | Market features | `beta` Beta `EQY_BETA`; `volatility` Volatility `VOLATILITY_30D` |
| `trading_technicals` | Trading technicals | `trend` Trend (no mnemonic is served; always not carried this round); `avg_volume` Average volume `VOLUME_AVG_30D`; `short_interest` Short interest `SI_PERCENT_EQUITY_FLOAT` |

1. **New file `portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx`** exports:
   - `HeaderCards` -- the four cards, in the order above, each a `<button>` carrying `data-header-card="<card key>"` and
     `data-header-card-state="SERVED"` when at least one of its figures is carried, `"NOT_CARRIED"` when none is. Each card's
     lead is its FIRST CARRIED figure (label + formatted value), in an element carrying `data-header-card-lead`; a card with no
     carried figure leads with a plain-words line (e.g. "Volatility and beta are not in the data yet"). Clicking a card opens
     its window: the estate's `HeroDialog` from `@/ui/components/graphic/HeroGraphic` (props `open, onClose, eyebrow, title,
     subtitle?, icon?, meta?, children, footer?, size?`), its body `HeaderCardDetail`, its footer `DialogStamp` (same file;
     props `stamp, source`) carrying the figures' vintage and source in words (e.g. "2026-09-29 | Source: Bloomberg").
     The pattern to copy is the Philosophy page's card strip + HeroDialog
     (`portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx:183-214`, `:220-292`), minus its hover
     shadow (DESIGN.md C11).
   - `HeaderCardDetail` -- props `{ cardKey: string; bundle: SecurityOverlayBundle }`, the window body: one element per figure
     of that card carrying `data-card-figure="<figure key>"` and `data-card-figure-state="SERVED"` (label + value) or
     `"NOT_CARRIED"` (label + a plain-words sentence, e.g. "Volatility is not in the data yet").
2. A figure is CARRIED when `bundle.header_figures` holds an entry with that mnemonic and a non-null value. Format values with
   the existing `formatStatValue` exported by `portal/src/pages/SecurityAnalysis/components/StatTile.tsx` (read it; do not edit
   it); a money figure uses that figure's own `currency` field when present.
3. **In `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx`**, replace the seven-tile row (the
   `STAT_TILE_DEFS.map(...)` block, "The seven Stat tiles (FWD-22)") with `<HeaderCards bundle={bundle} />`. Nothing else in
   that file moves: identity line, session badge, Back / Refresh, `HeaderBrief` (description, posture line, feed, timeline),
   the Trending / Breakout points and the axis footnote stay exactly as they are.
4. **In `portal/src/pages/SecurityAnalysis/constants.ts`**, put the four card definitions (the table above) as data the two
   components read. `STAT_TILE_DEFS` may be removed or left unused; nothing else imports it.

**The rule this cell must not break (C-PRESENTATION-ONLY):** the page derives nothing -- no figure is computed, converted or
guessed; a figure the payload does not carry reads as not carried, in plain words. **No vendor mnemonic (e.g. `CURR_ENTP_VAL`)
ever appears in visible text** -- it may sit in a data attribute or in code, never on the face.

**Design law (portal `DESIGN.md`, binding):** the header is the page's one dark band (C3); cards on the band use band ink
(`--palette-white` / `--palette-mediumGray` tokens as the file uses today), no translucent white (C5.8), no shadow (C11), one
primary action per view (C8: Refresh stays the primary). The window body is white with navy ink, as HeroDialog draws it.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the three files in `<paths>` under `portal/` change. `StatTile.tsx`, `HeaderBrief.tsx`, every `src/ui/**` and
   `src/components/**` file, every other page and every harness: unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/constants.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~2/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/StatTile.tsx`,
`portal/src/ui/components/graphic/HeroGraphic.tsx`, `portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`,
`portal/src/pages/SecurityAnalysis/types.ts` (`SecurityOverlayBundle`), `portal/DESIGN.md`, and the issuer's checks and
fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/` (never edit them; the Valero overlay
fixture there is the served payload the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/t-2.AC1.cjs"; echo "exit=$?"</invocation><expect>HEADER FOUR CARDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/t-2.AC2.cjs"; echo "exit=$?"</invocation><expect>CARD WINDOWS: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/bound.cjs" HEADER tabs.harness.cjs:20 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>HEADER BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-t-2" judgment="true"/>
</proof_of_spec>

AC1 is the face on Valero's served overlay (four cards in order, each with a lead, no stat tile left) plus an arm with every
figure removed (four designed not-carried cards) and no mnemonic in visible text. AC2 is each card's window body on the same
payload (Valero carries no volatility and no trend: those two read NOT_CARRIED). AC3 is the bound: the two page harnesses that
load this header and read green at the base stay green. A fourth criterion, with its reason: AC4 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded -- the header reads as four cards on the
band and the Financials window reads as the Philosophy modal pattern with its date and source stamp (C-ESTATE-FIXTURES,
DESIGN.md C3, C5, C11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~2/DSGN_AMGTV1.TO-AV-t-2.the-header-reads-as-four-cards.proof_of_spec.json`.
Report once: what changed and where, the AC1-AC3 output lines, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (PRD v0.2 :159-176), hop 4, CTO msg 26416. Base 8fa7abde: AC1 FAIL (1 of 3), AC2 FAIL
(0 of 5), AC3 PASS (2 of 2). Scratch GREEN arm: AC1 3 of 3, AC2 5 of 5. Card composition from brief IV.1 M7 and O4; the
short-interest mnemonic choice (percent of float vs days-to-cover) and currency per figure are FWD-4's round.

<status>complete</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
