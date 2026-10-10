# NFRA_MCPINDEX -- ROUND 8 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-10 ~23:3xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33062, `surprise-channel/remediations/REMEDIATION_v6.md` @9e5f093959. It landed
under this seat's override ruling (reply to msg 33058): Z-S82 stays undispositioned and BLOCKING for round 7's L8.
L8/L9: `adjudications/ADJUDICATION_v7.md` @434b6bca50. Packet: `deliverables/2.0.0_SA_COO~MI/round8/L8_PACKET_ROUND8.md`.
**Issuer:** `2.0.0_SA_COO~MI`. Round 9 is cut from this analysis in ONE issuance, per ruling call 9c9d
(`ledger/CTO_RULING_ROUND9_AFTER_ROUND8_DRAIN_20261009.md`).
**PRD:** v0.8 @0eff9e0e6d. `prd-signoff.py status` reads ADMITTED: the ratified-text half was SIGNED by `3.0.0_SA_CVO~Z`,
and the brief half was admitted because the CRO wrote the brief.

## 1. Round 8, as read

4 of 4 orders are terminal. Release d3c31e972e is live, and its labels were repaired (MX-r-9 v2). Z-C-S40/S41 dismiss 15 rows,
every BLOCKING or ARMED row of the round among them. Z-C-S42 graduates 8 rows, all INERT.

| FWD | grade | why |
|---|---|---|
| FWD-11 the thread (Alyssa, model vs benchmark) | **HELD** | J1 has not run. The precondition is met: AC2 and AC3 PASS, and the ledger is closed. The issuer's live run routed the question to E-13 and served `data_as_of` 2026-10-09 (T-1 for a Saturday). The one essential wait is a person, by Andrew's word: booked through `0.0.0_AB_MSTR~Z` (msgs 33019/33020/33034). |
| FWD-12 every need indexed | **REALIZED** | J2 PASS (Z-C-S43): her two briefs subtracted from the served catalog leave nothing missing, denominator 29. |
| FWD-18 entries name the workflow retired | **NOT_REALIZED, narrow** | J2 FAIL (Z-C-S44). The served count reads 4 of 14, but the true count is 3: E-25 claims C1, the YCharts report, which is GAP. C3 is carried by no entry, though E-4, E-5 and E-9 are its needs. Fixed by E2. |
| FWD-19 the ops lead's readers | not started | Round 9 by the v0.8 addendum. |

**Not read as a grade:** round-close-check reports MAY-CLOSE with graded=2. It counts a bare `J2` from any round's
CVO row, and FWD-11 has never run (Z-C-S42, below).

## 2. Rulings on the slug's three items

**(a) The unknown model name: the ANSWER asks, discover routes.** Discover routed "growth model" to E-13, and that is
correct: the need is model-vs-benchmark, whatever the model is called. The tool's answer must never supply a figure for a
model that does not exist. When the asked name is not one of the served models, the answer lists the five served
models (UST, ST, INT, LT, ULT) and asks which one. The carrier is the E-13 catalog entry's guidance, which Claude reads,
so no tool code is needed (build ladder rung 6). This rides E2. J1 still judges it from Alyssa's own words.

**(b) Catalog tags (Z-C-S44) and her phrasings (Z-W28-S4):** both go to E2, a single catalog cell.

**(c) The deploy procedure (Z-S92), with its sibling Z-S94:** `deploy-to-ec2.sh` is the gateway's deploy wrapper, so
**NFRA_OPLGTW's issuer, `2.0.0_SA_COO~O`, cuts the fix** in its next round:
- the wrapper refuses a dirty deploy tree;
- the manifest auto-commit's sparse-tree import is fixed (`commit_gate_runner.py:96`, `comp_constants_cli`);
- the extract prunes files absent from the artifact (Z-S94).

Until that lands, every MCPINDEX release cell's face states the procedure: the deploy tree's HEAD IS the deploy-only
commit, and the stamped label is read back against it.

## 3. The other graduated rows

| row | ruling |
|---|---|
| Z-S88, Z-W28-S8 (gateway suite red, 34-38 failures, order-dependent) | E3: record the baseline as a failing-ID list per tree shape (full and sparse), and grade each drain's suite by ID delta, never by count. The schwab and grant families belong to NFRA_OPLGTW: the issuer sends that list to `2.0.0_SA_COO~O`. |
| Z-W29-S1 (catalog emitter rewrites census_ref from a foreign census dir) | E3: by default the emitter takes its census dir from the checkout it runs in, and refuses one outside that checkout. |
| Z-C-S42 (round-close-check grades a bare J<n> from any round) | Already held by `2.0.0_SA_COO~C`, in the same family as NFRA_REPORT Z-S26 / NFRA_MCPMSP-Z-S4. Not this project's cell. |

## 4. THE ENRICHMENT LIST ROUND 9 CUTS (one issuance, `2.0.0_SA_COO~MI`)

| # | cell | FWD | done when |
|---|---|---|---|
| E1 | **FWD-19 readers, trade reconciliation and billing**, per the v0.8 addendum items 1-5. Each reader's first cell names its served source by census: every candidate producer, its denominator, and the surviving source read once. A reader with no served source ships as a GAP entry that names its owner. The four other ops items are catalogued GAP and `unowned`, with no tool and no alert. | FWD-19 | under an admitted principal, each reader returns rows with exactly the fixture's fields, plus scope, as-of and completeness; a census with no survivor yields a GAP entry and FWD-19 is reported not done |
| E2 | **One catalog cell plus release**: drop C1 from E-25's retires; add C3 to E-4, E-5 and E-9; move her two phrasings into E-9 and E-19 `example_questions` and retire the folds; add E-13's unknown-model guidance (2a). Release under the 2c procedure. | FWD-18, FWD-11 | FWD-18's count re-read from the SERVED catalog is 3 of 14 with C3 carried; `opal_discover` on "statement" and "S&P YTD" reaches E-9 and E-19 with no fold; the "growth model" answer lists the five models and gives no figure |
| E3 | **Batch repair at the drain**: Z-W29-S1's emitter default; the failing-ID suite baseline for Z-S88 and Z-W28-S8. | -- | the emitter refuses a foreign census dir (a planted one is refused); the drain's suite report prints new failures by ID against the recorded list |

**Stated dependencies, not cells:**
- J1 waits on Alyssa: a person, by Andrew's word, booked through `0.0.0_AB_MSTR~Z`.
- Z-S92 and Z-S94's wrapper fix belongs to `2.0.0_SA_COO~O`.
- Z-C-S42 belongs to `2.0.0_SA_COO~C`.
- Round 7 stays open until MX-s-19's 2026-10-13 runs; Z-S82 is graded at its L8.

## 5. What this analysis does not do

It deploys, applies and flips nothing, and it re-measured nothing. Every figure is the slug's, the packet's or the CVO
grade record's, as cited.

-- 1.0.0_SA_CTO~Z
