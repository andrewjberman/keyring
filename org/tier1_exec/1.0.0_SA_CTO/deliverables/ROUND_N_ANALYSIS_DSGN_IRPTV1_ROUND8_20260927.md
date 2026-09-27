# ROUND-N ANALYSIS -- DSGN_IRPTV1, round 8 (answering the CVO slug ADJUDICATION_v6 + REMEDIATION_v4)

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~22:1xZ. **Answers:** 3.0.0_SA_CVO msg 102159, slug
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/adjudications/ADJUDICATION_v6.md` @`6e820aa89b` (with
REMEDIATION_v4). **Contract:** PRD `DSGN_IRPTV1_PRD.md` v0.18 @`5d44d0fa62` (ADMITTED; the UI CLEANUP FINDINGS
section UIC-01..23 rides this round). **Recut by:** 2.0.0_SA_COO~D, in ONE issuance (round 9).

## 1. What the round measured

- **Judgment criteria**, graded on the window-18 walk (local portal DEV `3b98939b`, 1440 px, plus the CRO's same-build
  walks):
  - PASS: IVE57-AC2, IVE58-AC2, IVE61-AC2;
  - FAIL: IVE56-AC2 (UIR-30), IVE59-AC2 (UIR-37), IVE60-AC2 (UIR-32/34/49), IVE62-AC2 (the READY job reads 'Status
    unavailable'), IVE63-AC2 (UIR-45).
- **Per row:** 14 PASS, 7 FAIL, 1 NOT_EVALUATED (the R10 label: every walked answer ended on the page date, so the
  control case holds).
- **ARMED rows:** 12 of 12 dispositioned.
  - Closed: W29-S8, W29-S9, S19 (tip), W36-S2, W38-S1.
  - OPEN: W34-S1 and W35-S2 (~D), and W35-S1 (this seat).

**Reading:** round 8 moved 9 of the round-7 failures to PASS (UIR-04/13/11/15/25/46/31/33/36/47/41 and the
amendments). The 7 that remain are narrow and named, and none is a new outcome. The round-9 list below joins them with
the v0.18 cleanup findings (UIC-01..23), so this is an enrichment round, not a PRD addendum.

## 2. Rulings owed by this seat

### C-S60 -- IV-e-55 passed on its second 3-run sample

**RULED: the CVO's reading stands.** "No retries" means the FIRST pinned sample is the grade.
- S7, W21-S2, W23-S1 and W29-S10 stay OPEN.
- They close together when W34-S1 (fe-s-45/residuals.test.ts flaking under the pinned runner) is FIXED and ONE pinned
  3-run sample on the drained round-9 tree meets the bar: an identical failing set, a subset of the Q rows.
- The fe-s-45 fix is round-9 item E9. It names the order dependence it removes. A re-run that happens to pass is not a
  fix.

### W35-S1 -- the firm display-name source (Rule 30)

**RULED: neither an R20 departure nor a naming-gate exemption. The canon already holds the fact.**
- `infra/logic/registry/scopes.json` carries each scope's `tenant.display_name` ("49 Financial", "Inflection Wealth
  Management", "Cottonwood Capital Advisors", ...). Its `_about` states that every generated view reads the forms from
  that row.
- The sanctioned source is therefore a DEC-5 **generated view**: a generated TS module rendered from `scopes.json`, which
  the portal imports. `header/firmDisplay.ts`'s title-case transform is retired, and no firm literal is typed in portal
  source.
- If a round-7/8 acceptance line needs a shorter page label than `display_name` (the UIR-04 pass read 'Cottonwood'),
  the cell adds a registry FIELD for it: a Rule-30 registry row addition, validated by `python lib/opal_naming.py
  validate`. It never adds a literal.
- This is round-9 item E10. Its grant covers the generator's view target, the generated module, and
  `header/firmDisplay.ts` plus its callers. The registry field, if needed, is this seat's Rule-30 act, committed before
  the cut.

### UIR-37 -- which palette yields (TO-IV-e-59 froze both)

**RULED: the Opal MODEL colours are fixed; the ASSET-CLASS palette yields.**
- FWD-12 binds each Opal model to "its one colour, the same colour it wears on Model Portfolios". That colour is
  estate-wide identity, so it cannot move for one page.
- FWD-13's asset-class colours are this page's to choose, within the portal's colour law.
- Round-9 item E4 may change `chartColors.ts`'s asset-class entries whose hue sits within a named distance of any Opal
  model colour. The cell states the distance rule, lists every other page that consumes the changed entries (the change
  reaches them too, and consistently), and adds a test that fails when any asset-class colour falls within that
  distance of a model colour.
- `modelPortfolioColors.ts` stays read-only.

### S25 -- the READY job still reads 'Status unavailable' (IV-e-66 threaded the tenant)

**RULED: a diagnosis first, then the owner.** The cell traces window 15's REQ-67e12718 from the history row's status
read to the served answer (HAR plus irpt-status log) and names the file:line.
- If the page drops the answer, ~D fixes it.
- If irpt-status serves the wrong shape or scope (~Y's drift census @`974ec72ce9` names irpt-status as the one
  served-path drift), it routes to IRPT_BCKEND ~P's irpt-status rebuild.
- Either way, the list says words, never `ANALYSIS_REQUIRES_ATTENTION` (FWD-11).

## 3. The ENRICHMENT LIST -- round 9 (ONE issuance; every item keeps its row's acceptance line verbatim)

| # | Work | Rows | FWD |
|---|---|---|---|
| E1 | **One firm mention**: the firm chip above each tab repeats the identity line; one goes | UIR-30 | FWD-2, FWD-15 |
| E2 | **Breadcrumb and bases**: a strategy drill names the account with the same tail and mask as the header (one mask form everywhere); the ALL CATEGORIES card draws no one-slice pie | UIR-32, UIR-34, UIR-49 | FWD-14, FWD-6 |
| E3 | **Dates and source line**: one client date format on Performance (header, axis, daily table) and the directory stamp; the source line names the source in client words, never a function name | UIR-45, UIC-14, UIC-17 | FWD-2, FWD-5, FWD-15 |
| E4 | **Model vs asset-class colour** (ruled above) | UIR-37 (+ UIC-11 distinct account colours at 4+ accounts) | FWD-12, FWD-13, FWD-21 |
| E5 | **The Analysis history** (S25 diagnosis ruled above); words, not codes; by client name | IV-e-62 / S25, UIC-23 | FWD-7, FWD-11 |
| E6 | **Performance reads as a finished answer** | UIC-01, 02, 04, 05, 07, 08, 09 (UIC-06 is ~P's backend half) | FWD-5, FWD-11, FWD-15, FWD-16, FWD-19, FWD-20 |
| E7 | **Holdings charts at any account count** | UIC-10, 12, 13 | FWD-2, FWD-14, FWD-19, FWD-21, FWD-23 |
| E8 | **Analysis setup behaves like a form** (variant selection, default title, validation timing, 1440 px, loading), plus **Export on Analysis** from an answer-bearing signal | UIC-18..22, W35-S2 | FWD-7, FWD-8, FWD-9, FWD-18 |
| E9 | **The fe-s-45 order dependence**, fixed and named; then ONE pinned 3-run sample on the drained tree | W34-S1 -> S7, W21-S2, W23-S1, W29-S10 | -- |
| E10 | **Firm display names from the registry's generated view** (ruled above) | W35-S1 | FWD-2, FWD-15 |
| E11 | **The export hop**: TO-IV-e-67 (poll when the receipt is null, S26) is in flight as a direct act. With IRPT_BCKEND's adapter decrypt grant (packet f7aa7b3c, both halves), the next K8 grades READY with a %PDF | S26 | FWD-9 |
| E12 | **Round-9 walk coverage**: the R10 exception label on an answer that ends before the page date (read-only), and the UIC surfaces across 49F, INF and COT | R10, UIC-* | per row |

**Sequencing guidance (the COO decides the chains):**
- E9 goes first on its own chain, so the round's mechanical grades are trustworthy.
- E10 needs the registry view target before its render change.
- E5 waits on its diagnosis.
- E3, E6 and E7 touch Performance and Holdings in parallel; E8 is Analysis.

## 4. Carried (not DSGN cells)

- UIC-06 (an unanswerable window says why): IRPT_BCKEND ~P.
- UIC-15 (name beside ticker) and UIC-16 (full account type): ~M, Monday (R4). 49F's full account types wait on
  Schwab's registration-code list, carded to Andrew.
- UIR-26 (identical account labels) and UIR-48 (model amounts): ~M.
- S19's history purge: Andrew ruled "definitely delete" (record @`fce766f6ed`). 0.0.0_AB_MSTR executes tonight,
  ~03:00-05:00Z, under a freeze.

## 5. Push state

Everything cited is LOCAL on CLOUD (the CVO's ls-remote read: origin/CLOUD `8a6932422c`).
