# DSGN_IRPTV1 -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD

```json
{
 "project": "DSGN_IRPTV1",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md@1cccbe6bc6",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO a398ff25a800 @2c60ba747f", "brief": "SIGNED 4.0.0_SA_CRO 5a7bc670e9fe @cbd50ce98f"},
 "author": "2.0.0_SA_COO~D",
 "round": 1,
 "rectangle": "the THREAD's hops (PRD v0.5 THE THREAD, eight hops; spine v3.16 L5)",
 "cells": 4,
 "chains": 3,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D` (L5 is the COO's; no seat certifies this before L6). **Input:** PRD v0.5 @`1cccbe6bc6`,
ADMITTED -- both halves SIGNED at these bytes (`prd-signoff.py status`, 2026-09-24 ~06:0xZ): ratified-text
`3.0.0_SA_CVO` @`2c60ba747f` (bytes unchanged since v0.4), brief `4.0.0_SA_CRO` @`cbd50ce98f`. Receiving-check: ACCEPT by
`prd-manifest` at v0.4; v0.5 changed the brief half only (ENRICHMENT BACKLOG ids re-lettered, the portal-base clause on
the sequencing line). First landed @`c3d8dc63f7` against v0.4; pins bumped to v0.5 before any issuance, so the round
has not begun and nothing is re-versioned.
**Frozen at the cut.** It does not version during the round; a cell that looks wrong mid-round is a **surprise row,
never an edit** (`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/`).

**Rulings reaching every cell:** CTO batch 27 @`0a101a6668` (IRPT-DSGN-COO-D-CALLS-20260924): CALL 1 (a) this
project's workers render the advisor surface, M supplies projection / schema / republish, P supplies contracts / api /
`render/**` + package; (b) each cell's touch on a P- or M-written file is ONE mount line or ONE adapter function, named
literally in `<paths>`, read by the CTO before the issuance; (c) `2.0.0_SA_COO~M`'s portal UI work stops at the labels
pin `e5dd8487`; CALL 2 the portal base and branch (§4); CALL 3 the `spread` member (§2, §8). PRD CONTRACTS rules: the FE
derives nothing; every figure is a wire fact; "not supplied", never zero; the producer's vocabulary only in a
disclosure surface; `unprojected_grant` is a partial-data fact whose visible indicator stays on the body;
`portal/DESIGN.md` governs. Spine L6 diet: a build cell carries at most THREE mechanical criteria; repo-wide hygiene
runs at the drain.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

The round-1 rectangle is the PRD's THREAD, one cell per adapter to build or repair. The hops, VERBATIM from PRD v0.4
THE THREAD (the section's own list is the denominator, not this seat's recollection):

```
  1. Real login -> the portal session (the portal's auth, a real Opal user)
  2. Firm control reads Global (All) -> resolve-scope against the deployed directory function
  3. Browse / search -> Anna Thiessen's Cottonwood brokerage account found and chosen
  4. POST selections -> a selection id for that account
  5. Identity card -> name, firm, accounts by name + masked tail, holdings total, business date (C1)
  6. Performance headline -> YTD net return, the server-stated spread or "not supplied", beginning / ending value (C6's headline half)
  7. Holdings L0 hero -> the Models / SMAs / Client card from the published Cottonwood revision, names from `display` (C3)
  8. Security list -> the sortable table of securities with ticker, name, sleeve, weight and value (C4's table half)
```

```
  THREAD hops (PRD v0.4, the list above) ....................................... 8
  minus hops the PRD names "exist and are consumed unchanged (P's shared surfaces)"
    -- hops 1, 2, 3, 4 ......................................................... -4
  ------------------------------------------------------------------------------
  RENDER ADAPTERS TO BUILD IN ROUND 1 ("round 1 builds the four render adapters
    at hops 5-8", PRD v0.4) ..................................................... 4
```

**The unscoped control (Rule 24's domain falsifier).** Read from the other end -- the 14 CELL CANDIDATES -- the
candidates that serve FWD-1 are C1, C3, C4 (table half) and C6 (headline half): four, the same four surfaces the hop
list names in parentheses. C2 (firm control) is not a build in the thread: hop 2 reads Global (All) through the
existing `<select>` (`portal/src/pages/InvestorReporting/index.tsx:152-156` at DEV `7975c3bb`), and the PRD's backlog
places C2 at item 2. The two readings agree on the set.

**The two splits are the PRD's own** (v0.4 hops 6 and 8 say "headline half" and "table half"): C6's control row and
C4's treemap are ENRICHMENT BACKLOG items 4 and 3, not round 1.

**Status vocabulary** -- four values, and NOT-EVALUATED is one of them so non-evaluation cannot be encoded as a
verdict: `MEASURED` (evidence in hand at the cut, instrument named) · `DECLARED` (the PRD or a ruling asserts it; not
independently measured here) · `NOT-EVALUATED` (not looked at; neither pass nor fail) · `N/A`.

---

## 2. THE RECTANGLE -- 4 render adapters x 6 fields

Measured at portal DEV `7975c3bb` (= the workspace gitlink at `c4b9056831`) unless stated. Paths are portal-relative
under `src/pages/InvestorReporting/` unless prefixed.

| # | hop | render adapter (what is built) | current state | wire facts consumed | collision set (closer contract v1.4) | cell |
|---|---|---|---|---|---|---|
| 5 | selection -> identity card | `header/IdentityCard.tsx` (NEW) mounted at the ONE line where `ScopeSummary` mounts (`index.tsx:186`); `ScopeSummary` is rendered UNCHANGED inside the card's "About this scope" disclosure (CTO 100332: `header/ScopeSummary.tsx` is NOT touched by any cell); **the card renders the `unprojected_grant` partial-data indicator ON ITS OWN BODY from `scope.availability.unprojectedGrant` when count > 0, in advisor words** (PRD v0.4 CONTRACTS; row `IRPT_BCKEND-W1-S28` ARMED; a C1 that hides it re-opens S28 and fails FWD-2's brief-half reading); branch on shape first: a refusal carrying `public_reason_code` UNPROJECTED_GRANT renders its reason and no count | `MEASURED` -- `header/ScopeSummary.tsx:96-151` prints Selection / Permitted accounts / Scope as of / Directory as of / Scope match / Cohort / Not fully projected on `Panel variant="nested"`; account chips at `header/ClientSearch.tsx:184-205` are raw ids; `PartialDisclosureFact` (`ScopeSummary.tsx:67-76`) is the indicator's current carrier | `DirectoryEntry.displayName`, `maskedDiscriminator`, `kind`, termination (`contracts/index.ts:371-380`); `ResolvedScope.permittedAccountIds`, `verifiedRequestFirm.displayName`, `sourceTimestamps.businessAsOf`, `availability.unprojectedGrant {count, denominator, kinds}`; `HoldingsSnapshot.custodyTotalAmount` / `custodyTotalCurrency` (`:824`) | **P** writes `index.tsx` and `header/*` (portal `f0e7e362`, `8e616985`, `09d5d5ea`); ONE mount line, CTO-read | `IV-t-1` |
| 6 | selection -> performance headline | `tabs/reporting/PerformanceHeadline.tsx` (NEW) on a `Panel`, mounted in `tabs/reporting/ReportingTab.tsx` at ONE line in place of `Summary`'s screen use; state / reason / business date / revision to a footer line + popover | `MEASURED` -- `render/performance/Summary.tsx` renders beginning / ending / period return inside `.ir-page` (the print stylesheet), prints `no-summary-return-for-answered-window` as a value, has no spread tile; `tabs/reporting/AnswerStatus.tsx` band above it prints state + reason verbatim | `PerformanceReport.actualDates`, `summaryReturns[window == actualDates]` (selection rule `periodReturnForAnsweredWindow`, imported never edited), `beginningValue`, `endingValue` (MetricValue), `valuationCurrency`; **`spread`: NOT on the FE contract at `7975c3bb`** (0 hits in `contracts/index.ts`) -- renders "not supplied", the criterion prints which branch fired (CALL 3; backlog item 11) | **P** writes `tabs/reporting/*` (`c70855f3`, `a0fa8137`, `9290626f`) and owns `render/**` (NEVER written by this project); ONE mount line, CTO-read | `IV-t-2` |
| 7 | selection -> Holdings L0 hero | `mdpfResultFromSnapshot` in `tabs/holdings/DrillTree.tsx:140` (ONE adapter function) extended to fill `children` / `members` from the nodes beneath each L0 category, so `CategoryViewTree`'s hover detail and "View breakdown" dialog carry the sleeve tiles; names from `display` first | `MEASURED` -- L0 cards named by taxonomy path (M's closer edit); `members: [], children: {}` for every category (`:151`); `<CategoryViewTree result={mdpfResult} ground="light" />` at `:255` only when `roots.length === 1`. **M's labels pin `e5dd8487` (rows read `display` first, Client plug wording, qualifier badges) is NOT an ancestor of DEV `7975c3bb`** (`git -C portal merge-base --is-ancestor`, rc=1); it sits on `codex/irpt-m-ui-labels` and `irpt-dev-candidate-2-20260924` (§4) | `HoldingsSnapshot.nodes` (kind, displayName, `display?` `:791`, amount, `pctOfTotal` `:801`, hierarchyPath / modelName from P's additive carry `92e2ad96`), `custodyTotalAmount` | **M** wrote `tabs/holdings/*` and STOPS at `e5dd8487` (CALL 1(c)); ONE adapter function, CTO-read | `IV-t-3` |
| 8 | leaf nodes -> security list | `tabs/holdings/SecurityList.tsx` (NEW): sortable / filterable table over `kind: 'security'` leaves -- ticker (`securityId` tail), name (`display.label`, else the ticker), sleeve (parent path), weight (`pctOfTotal`), value (`amount`); asset class / sector ABSENT, not blank; basis / denominator / provenance to the footer; mounted in `tabs/holdings/HoldingsTab.tsx` at ONE line below `DrillTree` | `MEASURED` -- no flat security table exists; `tabs/holdings/SliceTable.tsx` renders only the current node's children with nine columns | `HoldingsNode.securityId` (`:792`), `display?` (`:791`, accepted since portal `bf3b971b`; the FILL is the SERVED republish the L6 cut waits on), `pctOfTotal`, `amount`, the parent chain; `unique_position_count` | **M** (as row 7); ONE mount line, CTO-read | `IV-t-4` |

**The one `DECLARED` that is load-bearing, stated:** `display.label` on the published Cottonwood revision is DECLARED
by the sequencing word ("SERVED -- model names on Anna's page" is the L6 precondition), not measured by this seat at
this cut. `IV-t-4`'s criterion prints leaves-carrying-`display` beside leaves, so an unfilled republish is detected,
not hidden; and before the issuance commit this seat reads the served `holdings-snapshot` for Anna's selection once and
records that count in the `fanout:` data.

---

## 3. THE CELLS -- 4 (round 1)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1 (`PREFIX-<axis>-<digits>`): prefix `IV`, axis `t` =
thread (round 1); later rounds use axis `e` = enrichment.

| cell | what it is | PRD candidate | serves | writes (portal-relative) | reads (never writes) |
|---|---|---|---|---|---|
| `IV-t-1` | IDENTITY CARD: name, firm, relationship / account kind, accounts as chips (display name + masked tail, toggleable to narrow), holdings unique custody total, business date; entitlement bookkeeping into an "About this scope" disclosure that renders the existing `ScopeSummary` unchanged (its `PartialDisclosureFact` moves down with it); the partial-data indicator ALSO rendered on the card's own body in advisor words from `scope.availability.unprojectedGrant`; `Panel`, navy ink | C1 (thread part) | FWD-1 hop 5; FWD-2 partial; FWD-11 partial | `src/pages/InvestorReporting/header/IdentityCard.tsx` (new); `index.tsx:186` (ONE mount line, P-written, CTO-accepted 100332) | `header/ScopeSummary.tsx` (rendered unchanged inside the disclosure, never edited), `contracts/index.ts`, `header/search.ts`, `src/ui/components/panels/*`, `portal/DESIGN.md` |
| `IV-t-2` | PERFORMANCE HEADLINE for the answered default window: period return, spread (`spread` when present, else "not supplied"), ending value, beginning value -- never a reason code as a value; `Panel`; state / reason / date / revision in the footer + popover | C6 (headline half) | FWD-1 hop 6; FWD-5 partial; FWD-11 partial | `src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx` (new); `tabs/reporting/ReportingTab.tsx:217` (ONE mount line, P-written, CTO-accepted 100332; `:170` `REQUEST_FAILED_ENVELOPE` is P's hop-11 line and is NEVER touched -- the drain merge takes P's side) | `render/performance/Summary.tsx`, `render/manifest.ts`, `state/availability.ts`, `contracts/index.ts` |
| `IV-t-3` | HOLDINGS L0 HERO: `CategoryViewTree` fed Models / SMAs / Client WITH children / members from the snapshot, names from `display` first, so the hero reads as it does on Model Portfolios | C3 | FWD-1 hop 7; FWD-6 (L0); FWD-10 partial | `src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx` (ONE adapter function `mdpfResultFromSnapshot`, M-written to `e5dd8487`, CTO-accepted 100332: `members: [], children: {}` at `:151` becomes the sleeve fill from the served `display` and the ruled tree -- strategy > constituent models + SMA + Client plug) | `src/components/CategoryViewTree.tsx` (extended or wrapped, never forked), `tabs/holdings/slices.ts`, `contracts/index.ts` |
| `IV-t-4` | SECURITY LIST: sortable / filterable table over the leaf security nodes; ticker, name, sleeve, weight, value; asset class / sector absent until ruled; basis / denominator / provenance in the footer | C4 (table half) | FWD-1 hop 8; FWD-6 (L2); FWD-11 partial | `src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx` (new); `tabs/holdings/HoldingsTab.tsx:197` (ONE following line after `<DrillTree snapshot={snapshot} />`, M-written, CTO-accepted 100332) | `tabs/holdings/slices.ts`, `src/pages/Positioning/tabs/HoldingsTab.tsx` (the pattern), `contracts/index.ts` |

**Coverage of the thread: 4 of 4 render adapters, 8 of 8 hops** (1-4 consumed unchanged, per the PRD). **Coverage of
the PRD's candidate set in round 1: 4 of 14** (C1, C3, C4-table, C6-headline). The remaining ten candidates and the
two split halves are the PRD's ENRICHMENT BACKLOG items 1-11 in the PRD's order; round 1 covers every cell of THIS
ROUND's rectangle, which is the thread (spine L6). **C13 / C14 in round 1:** applied ONCE inside each cell to that
cell's own surface -- each new component is a `Panel` with navy ink and moves its tokens to a disclosure -- and graded
once at the drain; no round-1 cell restyles a surface it does not build; the Performance tab as a whole stays on
`render/print.css` until the backlog's panel-system item.

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP** (D13 placed LAPTOP, Andrew-direct 2026-09-11). **No cell is owned by a seat**; each
is served by a worker `0.9.0_WK_DSGN_IRPTV1~<n>` at L7 in a worktree PAIR provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 <n> --path <abs> --portal-ref <portal_ref>`: the workspace worktree off
`HEAD` (`CLOUD`) and the portal worktree INSIDE it at `<abs>/portal` (the script's `portal_dir="$worktree/portal"`;
portal is a gitlink -- CALL 2), `node_modules` linked, never installed.

**Branch placement (CALL 2, accepted):** `portal_ref` = the portal `DEV` HEAD at the cut, written into the `fanout:`
data; the drain merges each worker's portal branch into the project candidate branch `dsgn-irptv1-r1` (off
`portal_ref`); the DEV landing is `0.0.0_AB_MSTR`'s on Andrew's word after the CTO's review.

**THE BASE AT THE CUT MUST CARRY M's LABELS PIN, AND DEV AT THIS CUT DOES NOT.** CALL 1(c) stops M at `e5dd8487`, and
`IV-t-3` / `IV-t-4` build on those rows. Measured at L5: `e5dd8487` is on `codex/irpt-m-ui-labels` and
`irpt-dev-candidate-2-20260924`, NOT an ancestor of DEV `7975c3bb`. So "DEV HEAD at the cut" is correct only once P's
candidate 2 has landed on DEV -- the same landing that serves the `display` republish's portal side. The L6 cut
verifies `git -C portal merge-base --is-ancestor e5dd8487 <portal_ref>` (rc=0) and records it beside `portal_ref` in
the `fanout:` line; rc=1 means the cut is early (finding F3, now the PRD's own sequencing line at v0.5: if the candidate lags the served
republish, the base STAYS DEV and the cut waits).

---

## 5. DEPENDENCY EDGES AND CHAINS

Edges are keyed to observed completion AND to write collision: two worktrees editing one file is a guaranteed conflict
at the drain, so the collision set, not the logical arrow, decides the queue.

```
  IV-t-1   (header/*, index.tsx mount)          -- no inbound edge
  IV-t-2   (tabs/reporting/*)                   -- no inbound edge
  IV-t-3 --> IV-t-4   (both tabs/holdings/*; IV-t-4's HoldingsTab.tsx mount sits beside IV-t-3's DrillTree adapter)
```

**CHAINS (connected components of the undirected edge set): M = 3**, exactly the PRD's own line "Chains: header (5),
performance (6), holdings (7, 8)".

| chain | cells | write surfaces | disjoint from the others? |
|---|---|---|---|
| A -- header | `IV-t-1` | `header/*`, `index.tsx:186` | yes |
| B -- performance | `IV-t-2` | `tabs/reporting/*` | yes |
| C -- holdings | `IV-t-3` -> `IV-t-4` | `tabs/holdings/*` | yes |

**Fan-out this decomposition supports:** `N = 3 of M = 3 chains, cap 8`; the L6 issuance states and defends the final
line. Each chain's touch on a P- or M-written shell file is ONE literal line or ONE function, named in `<paths>` and
read by the CTO before the issuance (CALL 1(b)).

---

## 6. BATTERY DISPOSITION

Spine L5, round 1 of a threaded project: every lens defaults to `DECLARED-NOT-APPLICABLE` with the reason "thread
round; the lens runs on the enrichment round that touches its surface", except `comp-iam`, which is `RUN` whenever
the thread touches IAM.

- **`comp-iam` -- DECLARED-NOT-APPLICABLE, measured not assumed.** Word-boundary AWS-surface token sweep over the
  whole PRD at HEAD (v0.4 @`c4b9056831`, 26,070 bytes): `lambda terraform .tf iam s3 cloudfront ecs sns ses dynamodb
  glue` = **0 of 11 tokens, 0 hits** (the same sweep at v0.2, 20,815 bytes, also 0). No cell writes an AWS surface; the
  thread touches IAM only through P's deployed functions, consumed unchanged. Bound: a later DEV / PROD promotion of
  the candidate branch is an act with an IAM surface and is NOT covered here.
- **`comp-schedule` -- DECLARED-NOT-APPLICABLE (thread round).** The round's gates are recorded in §8 as sequencing
  inputs; the lens runs on the enrichment round.
- **`comp-adversary` -- DECLARED-NOT-APPLICABLE (thread round).** Runs on the enrichment round against the PRD and the
  task orders (which carry `<decomp_ref>`, resolving the T11 neighbourhood blindness DSGN_REBRND's L5 recorded).

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** §1: 8 hops (the PRD's own list) minus 4 consumed-unchanged = 4 adapters,
falsified from the candidate set with the same result. Each adapter is claimed by exactly one cell; the four write
sets are disjoint files plus one ruled line each in a shell file. Exhaustive against the hop list; mutually exclusive
for ownership of a surface's target state and for touch.

**(ii) SAME GRAIN.** Every cell is one render adapter over one wire object, gradeable by (a) the rendered facts
against the wire facts on the served response for Anna's selection, (b) the hop's seam probe against the REAL
neighbour (the deployed function), (c) at most one further criterion. The PRD's own halves keep the grain.

**(iii) INTENT COHERENCE.** One axis: the ADVISOR-FACING RENDER of the thread's four reads. Not data (M / P / Y), not
contracts (P), not `render/**`, not the design law (DSGN_REBRND), not any backlog item.

**(iv) STATE COHERENCE -- what each remedy does NOT move.**
- `IV-t-1` moves what the header SHOWS. It does NOT move who may see what (the selection stays server-accepted,
  `POST selections` -> `sel_<64hex>`; chips narrow the PRESENTATION and re-select through the same request), and it
  does NOT move the partial-data indicator off the body (it is rendered on the card AND retained in the disclosure).
- `IV-t-2` moves the headline's presentation. It computes NO spread, gain or average; `spread` renders only when the
  wire carries it; `periodReturnForAnsweredWindow`'s selection rule is unchanged.
- `IV-t-3` moves what `CategoryViewTree` is FED. It does NOT move the L0 taxonomy (the contract's, M's projection)
  and re-attributes no amount.
- `IV-t-4` moves the existence of a flat security list. It adds no asset class, sector, quantity or price (absent
  columns, not blank) and does NOT replace `SliceTable`'s per-node drill.

---

## 8. SEQUENCING INPUTS, FINDINGS CARRIED, AND THE DRAIN TRACE

**Sequencing (CTO batch 27 + PRD v0.4 PATHS):** L5 lands on ADMITTED at v0.4 (this commit). **L6 is cut when the COT
`display` republish is SERVED** (model names on Anna's page) **and the portal base carries `e5dd8487`** (§4). The D1
resident run is NOT a precondition. The round-1 DRAIN TRACE additionally needs the Performance path for hop 6: (i) X10
ACTIVE (ACCEPTED, batch 27; M's registry row, P's rebuild) and (ii) one installed one-use plan on Andrew's per-use
word -- NOT waited on: absent by the drain, hop 6 is graded from the LIVE refusal ("not supplied" with the producer's
public reason on screen), FWD-1 stays NOT_REALIZED, and the live return is round 2's first enrichment item (PRD v0.4,
the CTO's choice stated). A hop fed by a fixture still fails FWD-1.

**F2, RESOLVED at v0.5 @`1cccbe6bc6`** (kept for the record): at v0.4 the PRD's ENRICHMENT BACKLOG items 3-10 cited candidate ids shifted
against its CELL CANDIDATES section at the same pin (`git show c4b9056831:...PRD.md`, backlog lines 190-197 vs
candidates 203-235: item 3 "C3, C4 remainder" where the L1 bars are C5; item 4 "C5, C6 remainder" where chart / heatmap
are C7 / C8; item 5 vocabulary "C13" (C14); item 6 drawer "C7" (C9); item 7 stepper "C8, C9" (C10); item 8 prospect
"C10" (C11); item 9 export "C11" (C12); item 10 panel "C12, C14" (C13). Items 1, 2, 11 are right; the FWD ids and the
words were correct throughout. v0.5 re-lettered items 3-10 to the section's own ids (C5; C4 remainder / C6 remainder, C7, C8 /
C14 / C9 / C10 / C11 / C12 / C13); this decomposition's section 3 cites match them.

**F3, carried into the PRD at v0.5:** the sequencing line now requires `e5dd8487` an ancestor of portal `DEV` before the L6
cut and records `portal_ref` + the is-ancestor rc in the fanout data; section 4 states the same rule.

**The live trace is the COO's drain act, not a cell** (PRD v0.4 THE THREAD). At the round-1 drain `2.0.0_SA_COO~D`
runs the eight hops on the assembled candidate against the real backend with a signed-in session, the HAR read in
place, CloudWatch lines cited, the artifact kept under
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/`. Whose sign-in: this seat holds the playwright tool
but no credential; Andrew's or the CTO's signed-in session is the gate, named here, not waited on for the cut.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. `display.label` on the served revision is DECLARED until this seat reads the served snapshot at the L6 cut.
2. P's and M's files are measured at portal `7975c3bb`; the base moves with candidate 2; the four touch points are RULED (CTO 100332: index.tsx:186,
   ReportingTab.tsx:217, DrillTree.tsx:140-160 `mdpfResultFromSnapshot`, HoldingsTab.tsx:197) and are re-read at the cut against
   `portal_ref` before being written literally into each order's `<paths>`; `header/ScopeSummary.tsx` is out of every `<paths>`.
3. No cell has been exercised; every target state is a specification.
4. M = 3 is the PRD's own chain statement and this cut's write-collision reading; a CTO ruling that routes a mount line
   differently re-derives the edge set at the cut, recorded in the issuance commit.
5. No effort or duration estimate appears here, deliberately.
