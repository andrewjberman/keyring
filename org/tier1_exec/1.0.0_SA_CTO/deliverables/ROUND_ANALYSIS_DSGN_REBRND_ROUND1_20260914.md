# ROUND-1 ANALYSIS -- DSGN_REBRND

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~19:3xZ · **Step:** L10.

**Input:**
- `3.0.0_SA_CVO`'s slug, msg 96703.
- The CVO's record `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md` @`77a5acbf40`, on
  `feature/d13-visual-elevation`. The carriers `C-S1`..`C-S14` and the 37 remediation rows are on the same branch
  @`14ca97a535`.
- `2.0.0_SA_COO~D`'s drain-end read, msg 96662.

**Order:** the CVO's slug came first, then this analysis. Round 2 is already set by Andrew's ~18:4xZ word: it runs
INTERACTIVELY, with `2.0.0_SA_COO~D` making each page's edits itself, no worker and no task order, and his
confirm/revise the gate between pages (PRD preamble, fifth ruling). So this analysis feeds the page slices directly,
not a single issuance.

---

## 0. WHAT ROUND 1 DELIVERED -- SAID FIRST

- **Orders:** 15 of 15 terminal on their governing proof instances.
- **Rows:** 67 new, all dispositioned: 26 DISMISSED, 8 DECOMP_INVALIDATING (the page inversion), 33 GRADUATED, plus the
  CVO's own C-S11..C-S14. Carrier-less rows: 0 of 67.
- **L9:** 22 judgment criteria graded against PRD v0.5 (the text that issued the round): 10 PASS (8 with a named
  qualification), 9 FAIL, 3 NOT_EVALUATED.
- **The biggest single fact:** the light-mode inversion was never in round 1's grant. 4,887 light-on-dark idioms in
  171 page files sit outside every cell (`W1-S9`, `S2` and siblings, C-S4). That is why several FAILs read as they
  do, and why round 2 exists in the shape Andrew set.

## 1. THE OUTCOMES -- GRADED AGAINST v0.5, THE TEXT THAT ISSUED THE ROUND

| outcome | grade | the evidence (CVO record s.3) | where it goes |
|---|---|---|---|
| FWD-1 one firm across the boundary | NOT EVALUATED | RB14-AC5: the walk was not performed, and the site half was absent. RB14-AC4 FAIL: several IV.3 differences are not bands. RB3-AC7 FAIL: 33 of 40 contrast pairs. RB1-AC6 FAIL: the dark mode is complete in the JSON but not selectable | RULING W (s.2); the inversion page slices (R17); a dark-mode toggle in the foundation |
| FWD-2 figures in the firm's typeface | REALIZED on the typeface, NOT EVALUATED on alignment | RB2-AC6: 6 of 6 sampled figures are Lato tabular; the alignment clause has no before-capture | a populated figure-column render on the first page slice |
| FWD-3 order read off colour | NOT REALIZED | RB4-AC5 FAIL: the Global RSI bars colour an ordered 0-100 scale through four hue families (RSIBars.tsx:140-155) | `S3` on the /market slice (the first page) |
| FWD-4 one action at a glance | NOT REALIZED | RB5-AC5R FAIL: 0/1/0 persistent actions on the three routes, PM's inside a band; the accent "Neutral" label (C-S11) | RULING A (s.2), and the Neutral label neutralised (C-S11) |
| FWD-5 focus visible | REALIZED, with a named qualification | RB6-AC5/AC6 PASS: 462 of 462 Tab stops ringed; survives a 24px default | the ring token (W1-S22) in the foundation |
| FWD-6 one contract, reject by clause | NOT REALIZED | RB7-AC4 PASS (the build from the contract alone); RB7-AC5 FAIL (0 of 5 author agreements); C-S12 (DESIGN.md carries no class labels) | the contract's class labels and terminator (C-S7, C-S12); the author agreement, `2.0.0_SA_COO~D`'s |
| FWD-7 status and data colour disjoint | NOT REALIZED on /market | W2-S7 (8 role-and-ground pairs below the floors), W1-S37 (/market gain/loss colours in neither family) | the /market slice; FWD-13's per-pair checker |
| FWD-8 one rendering system | NOT EVALUATED | RB11-AC6: no render of two migrated charts on record; W2-S1: the word cloud | RULING V (s.2) |
| FWD-9 Andrew's side-by-side | his | RB15-AC5 PASS grades the pack's form only | his word |
| FWD-10 the screen filled by the work | NOT YET | RB9-AC4/AC6 PASS; RB9-AC5 FAIL: no designed terminator in DESIGN.md (W1-S29) | the contract's terminator clause |
| FWD-11 four designed states | NOT REALIZED | RB10-AC5 FAIL: seven routes draw data, EMPTY or LOADING where ERROR is owed (W3-S4); RB13-AC4 FAIL: 65 of 96 renders show their named state | per page slice (W3-S3..S6); NO-PERMISSION wired (W3-S1) |

## 2. THE RULINGS OWED TO THIS SEAT

- **RULING G -- the governing PRD is CLOUD's** (C-S13, ARMED, this seat's). `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`
  on CLOUD, at the version its two halves sign, governs round 2. The copy on `feature/d13-visual-elevation` reads v0.2
  and is a stale fork.
  - At each signed version `2.0.0_SA_COO~D` replaces the branch copy with CLOUD's bytes (`git checkout CLOUD -- <that
    path>`, committed on the branch), so a reader in either tree reads the same text.
  - The CVO grades against CLOUD's. Nothing merges to CLOUD. C-S13 is disarmed by this ruling plus that act.
- **RULING A -- FWD-4's "one" is AT MOST one** (W1-S20). A view with no primary action (/positioning, /market) spends
  the accent on no action, and that meets FWD-4. What FWD-4 forbids is a SECOND action accent, not a view without one.
  /portfolio-management's Upload Portfolio stays that page's one action, and its place in a band is the page slice's
  to fix. Written into FWD-4, R5 and the CONTRACTS clause at v0.9, so L9 grades the text and not this note.
- **RULING V -- the word cloud is FWD-8's one named exception** (W2-S1). FWD-8's own CONSTRAINT says a chart that
  cannot be migrated without changing what it shows is a surprise row, never a quiet exception. A word cloud (TopicCloud,
  `@visx/wordcloud`) has no axis, tick or legend to share, and the incumbent library has no word cloud. It stays on
  `@visx`, named in the contract with that reason, and FWD-8's census reads one charting library plus this one named
  exception. Written into FWD-8 and R9 at v0.9.
- **RULING W -- FWD-1's site half is the existing measurement** (W1-S34). `design/brand/opalinvest.com.json` (3 pages,
  2026-09-11) is the site half, at its vintage and disclosed as such. A new capture of opalinvest.com is egress, and it
  is made only on Andrew's per-use word. The WALK in FWD-1's DONE WHEN is a human act: one person who has never seen the
  portal. Who that person is, and when, is Andrew's, as FWD-9 is.
- **C-S11 -- the Fear & Greed "Neutral" label in the accent is outside FWD-4's closed set.** It is neutralised on the
  /market slice. The set is extended only by Andrew's word, and none has been given for it.

## 3. FOR ANDREW, WITH THIS SEAT'S RECS (C-S9) -- THEY ARE HIS, NOT RULED HERE

1. **The locked canon hexes against the 3:1 non-text bar** (W2-S8). Three locked canon hexes measure below WCAG 2.1 SC
   1.4.11's 3:1 on the white panel that Option A makes the default ground.
   - **REC:** keep each hue, and move only the lightness of the three to the nearest value that meets 3:1 on white.
     CONTRACTS already says the contract may be stricter than the bar, never looser, so the lock yields on lightness
     and holds on hue.
2. **The dark-mode accent's roles** (W1-S11). No single accent value meets 4.5:1 both as white-on-accent and as
   accent-on-band in the selected dark mode; the luminance bounds do not overlap.
   - **REC:** two dark-mode accent values, each classed DERIVED with its rule: one for fills that carry white text, and
     one for ink and rings on the band.

The other items open at him stand where they stood: FWD-9; the sidebar (keep or revert to DEV's); the three tooltip
types; true Lato Bold (W1-S8).

## 4. WHAT ROUND 2's PAGE SLICES CARRY -- BY CARRIER GROUP

Round 2 is interactive (the fifth ruling), so these are what `2.0.0_SA_COO~D` works through with Andrew. They are not
orders. The FOUNDATION lands once, behind the page-level surface scope; the rest land page by page, /market first.

| group | rows | lands in |
|---|---|---|
| C-S4 the page inversion (DECOMP_INVALIDATING) | W1-S9, W1-S10, S2, W2-S5, W2-S6, W2-S7, W1-S27, W1-S33 | each page slice (R17), on the inversion rule and the role and state tokens (R15, R16) |
| C-S5 designed states and keyboard | W3-S1, W3-S3, W3-S4, W3-S5, W3-S6 | NO-PERMISSION wiring in the foundation; the rest per page |
| C-S6 colour writers and FWD-4 | W1-S4, W1-S8 (Andrew's), W1-S14, W1-S16, W1-S20 (RULING A), W2-S11, S3, W1-S37 | the one-writer fixes in the foundation; S3 and W1-S37 on /market |
| C-S7 the contract and its tokens | W1-S3, W2-S9, W1-S22, W1-S25, W1-S29 | the foundation: DESIGN.md and the token file |
| C-S8 FWD-8 and the rewrites | W2-S1 (RULING V), W2-S2, W2-S15, W1-S24, W1-S34 (RULING W), W1-S36 | the foundation; the shadows per page |
| C-S9 Andrew's two | W1-S11, W2-S8 | s.3 |
| C-S10 checker and cut discipline | W1-S6, W1-S12, W1-S17, W1-S18, W1-S21, W1-S23, W1-S35 | any checker `2.0.0_SA_COO~D` runs during round 2 |
| the CVO's own | C-S11 (neutralise), C-S12 (class labels, with C-S7), C-S13 (RULING G), C-S14 (the grade pattern) | as stated |

**C-S14 / LGIC_NAMING-C-S10, the grade pattern:** widened to `^[A-Za-z0-9]+-(AC|J)[0-9]+R?$`. The pattern comes from a
census of 3,069 task orders and proof instances, where the only amended suffix in use is R. The commit is its own; its
hash is in the send.

## 5. NOT RULED HERE

- Andrew's items (s.3, and the ones listed after it).
- The order of pages after /market. It follows his comments.
- Any merge of the feature branch. The confinement stands.
