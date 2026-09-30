# DSGN_AMGTV1 -- ROUND 4 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~19:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26681, READ-acked, subject *"L10 slug DSGN_AMGTV1 round 4 @01d9495d43"*,
citing `surprise-channel/adjudications/ADJUDICATION_v6.md`. Issuer packet: `deliverables/2.0.0_SA_COO~D/round4/DRAIN_END_READ.md`
@`e4620fa1f9` (msg 26672).

**Round 4 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

6 of 6 orders are terminal and drained. The CVO's L9 verdicts, from its own shots and its own signed-out run:
- **w-1 (the instrument):** the walk now FAILS on the sign-in page. `Z-S3` graduates on the CVO's signed-out control (rc=3,
  WALK VOID, shot `001` is the sign-in page).
- **w-2: MET.** Tickers read as a PM types them ("BP/ LN", "WALMEX\* MM", "9433 JP").
- **w-3: MET.** The Model face carries no status labels (0 where round 3 had 18 or more).
- **w-4: MET.** Exec Management has one dark band, and the detail says in words where the list was looked for. One
  residual: the served machine reason is still appended verbatim.
- **w-5: PARTIAL.** The comparable's gaps are said once, and the figure cites read as words, but only 8 of the 18 cites
  read as words. The other 10 carry 7 passage ids, 2 "fit score PFOE ... status ABSENT" and 1 "membership: held in PFDE".
- **w-6: PARTIAL.**
  - Met: one legend; dates that do not overlap.
  - Defects: the last tick is clipped at the right edge, and two oranges sit at CIE76 dE 18.1 (VLO US / WALMEX\* MM).
  - Not graded: the pick-and-follow, because no walk ever clicked a legend button.

## 2. RULINGS ON THE CVO'S OBSERVATIONS AND THE CARRIED ROWS

1. **Model tile names: CONFIRMED, no cell.** The worker read the letter codes, but the names agree with the producers' own
   definitions, which quote Andrew verbatim:
   - `lib/research/scores/peers_v.py:1-8`: PEERS V is "a peer-relative valuation z-score over six yield-form measures",
     so "Peer valuation score" is accurate.
   - `lib/research/scores/divergence.py:1-8`: DIVERGENCE D is "(model NTM FCF - consensus NTM FCF) / analyst dispersion".
     "Forecast divergence score" is accurate. Cell 4 sharpens it to "Divergence from consensus forecast" so that a PM
     reads what it diverges from.
2. **The Model face's two Base cases: RULED -- each line names whose case it is.** "The research team's Base case is not
   served on this page yet" and "Base case: 159.61 EUR (adjusted consensus EPS x trailing-median P/E)" are both true, but
   they read as a contradiction. The team's line says "The research team's Base case", and the rule's line says "Opal's
   rule-based Base case". This is FWD-6's "says whose view it is", applied to the Model face. Cell 4.
3. **`Z-S1` (ARMED, carried four rounds): RE-RULED here so that it can be stamped DISARMED.** My round-2 ruling stands:
   - FWD-1's thread stays on Valero.
   - Valero's dossier carries no team case, so hop 6 is met by the page's honest line (the team's case is not in their
     pack yet), and no covered-name swap is needed.
   - FWD-6 is walked on INTU, which does carry the team's case.
   - No ENDPOINT change follows. `3.0.0_SA_CVO~Z` stamps `Z-S1` DISARMED at its next compile, on this ruling.
4. **`Z-W4-S1` (ARMED):** half (b) is AMGT_RESAPP `ww-4`'s. That order is `complete`, and its L8 grade is owed in
   AMGT_RESAPP. It stays carried here and is not graded from this project.
5. **Producer asks (C-PRESENTATION-ONLY, never page-side).** Both are routed to AMGT_RESAPP's round-49 enrichment list,
   which this seat writes at its round-48 analysis:
   - **(a)** A served company `name` on the rank-history series, which FWD-3's line labels need. The list rows already
     carry it through `ww-2`, deployed with `ww-1` at 19:18Z.
   - **(b)** Officers from a second source when a filing has no officer section. FWD-7's ACCEPT, "shows the company's
     officers ... even when the company's filing has no officer section", needs this.

## 3. FWD GRADES

- **`FWD-4`, `FWD-9`: REALIZED**, standing.
- **`FWD-3`: NOT REALIZED.**
  - The legend is one and the dates do not overlap.
  - The pick is unproven on pixels.
  - The labels are tickers until the producer ask (a) serves a name.
- **`FWD-7`: NOT REALIZED.** The detail says where it looked, but no officer is shown for a filing without an officer
  section. That waits on the producer ask (b).
- **`FWD-10`: NOT REALIZED.** 10 of 18 Posture cites still carry codes.
- **`FWD-11`: NOT REALIZED.**
  - Codes remain: the Posture cites, the Exec machine reason, and the generations line "24 ABSENT, 6 SERVED" with its id.
  - The side-by-side read is not yet walked.
- **`FWD-1`, `FWD-2`:** the served name and classification are deployed as of `ww-1`'s apply at 19:18Z, with its V1 leg
  open. Round 5's walk grades both, after V1 closes.
- **`FWD-6`:** the INTU arm waits on AMGT_RESAPP `vv-4`'s successor.
- **`FWD-5`, `FWD-8`:** not yet cut. FWD-5 depends on HARVST's served timeline, which moved with `g-2` at 19:26Z.
- **2 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 5 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **Posture cites read as words** | FWD-10, FWD-11 | 7 passage ids become the document and section in words (from the served citation fields). "fit score PFOE: no score (status ABSENT ...)" and "membership: held in PFDE" each become one sentence with no preset code. The census gains a passage-id and preset-code class. |
| 2 | **The history view's pick, edge and colours** | FWD-3 | A walker step clicks one `data-series-ticker` button and screenshots the picked line. The rightmost date tick is not clipped. The palette's minimum pairwise CIE76 dE is at least 25 over all 45 pairs (VLO US / WALMEX\* MM is 18.1 today). |
| 3 | **The lead chart's generations line and the second band** | FWD-11 | "24 ABSENT, 6 SERVED" and the generation id become one plain sentence. The load view has one dark band (the source footer is not a second band). The census sees the generations line. |
| 4 | **The Model face says whose Base case each is** | FWD-6, FWD-11 | Ruling 2's two labels. The divergence tile reads "Divergence from consensus forecast". |
| 5 | **Exec "Read detail" without the machine reason** | FWD-7, FWD-11 | The served reason moves to a data attribute; the visible text keeps "Where we looked: ...". |
| 6 | **One date form and readable captions on the dark header** | FWD-11 | One date format across the page. The 1-4 low-contrast captions on the dark header meet the estate's contrast. |

**The round's one real run:** the signed-in walk on VLO, INTU and SAP GY, **after `ww-1`'s V1 leg closes**. It includes:
- the four lead-panel lists (FWD-2 graded on served names and classifications);
- the history view with ten names, one of them picked (FWD-3);
- a signed-out control first (cell 1 of round 4).

**Fan-out:** 6, cap 8.

**NOT cells:**
- "$1,234" inside INTU's drafted prose (C-PRESENTATION-ONLY).
- The two producer asks, which go to AMGT_RESAPP.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- The merged worker checkouts `wk-dsgn-amgtv1-13` to `-17`: removing them is a recursive deletion [CLAUDE.md Agent
  Autonomy]. It is on this seat's list to him.

## Compiler Tools

- The CVO's v6: its own shots, its signed-out walk, and its palette dE computation. The COO's DRAIN_END_READ section 4.
- FWD-3, FWD-7, FWD-10 and FWD-11 DONE WHEN / ACCEPT read at the PRD's ENDPOINT section (`prd/DSGN_AMGTV1_PRD.md:52-124`).
- `comp-find 'peers_v|divergence_d'` over `lib`: 35 hits in 362 files. The producer docstrings were read at
  `peers_v.py:1-8` and `divergence.py:1-8`.
