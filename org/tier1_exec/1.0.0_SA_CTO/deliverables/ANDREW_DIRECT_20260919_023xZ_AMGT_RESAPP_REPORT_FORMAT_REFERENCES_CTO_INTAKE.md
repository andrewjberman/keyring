# Andrew-direct 2026-09-19 ~02:3xZ -- the asset-management team's REPORT FORMAT, and what it asks of AMGT_RESAPP

**Route:** laptop terminal -> laptop `0.0.0_AB_MSTR` -> agent bus (id `06e0fa4b`) -> `0.0.0_AB_MSTR~Z` -> this seat, exactly
as he asked it be routed. **Relay:** `0.0.0_AB_MSTR~Z`, 2026-09-19 02:47Z. **Ledger:** LD-0590.
**Recorded by:** `1.0.0_SA_CTO~Z`, before any act on it.

## His words, as relayed VERBATIM

> I need you to get a message to CTO~Z via MSTR~Z via agentbus. They are working on AMGT_RESAPP. Something that they need
> to be aware of is the format/style of what the asset management team looks for in these reports. I want to send them two
> references that the asset management team made with Claude, because we want to keep it in mind on two bases: 1.) We
> should have the content between our pages to be able to generate the information in these reports [...]

⚠ The relay carries his sentence to its truncation point in the message this seat received; the full text sits in the
laptop record `ANDREW_DIRECT_20260919_023xZ_AMGT_RESAPP_REPORT_FORMAT_REFERENCES.md` in the reference folder. **This seat
has NOT read that file** (it is on `origin/CLOUD`, not on SITEZ) and does not restate the second basis from memory. What
is carried below as BINDING is only what the relay states: **(1) content coverage** -- our pages must hold what is needed
to GENERATE the information these reports list; **(2) an EXPORT** -- a file that is "a better version of this" in 2 to 3
pages. **He said "two references" and named THREE files; nothing is inferred about which two he meant.**

## The files, verified HERE rather than relayed

`origin/CLOUD` @`1057a4f113`, `org/tier0_exec/0.0.0_AB_MSTR/deliverables/AMGT_RESAPP_REPORT_FORMAT_REFERENCES_20260919/`.
This seat extracted each blob from its own object store and hashed it; all three match the prefixes the laptop stated:

| file | sha256 (16) | pages | what it is |
|---|---|---|---|
| `REF_A_house_format_LLY_earnings_update_2Q26.pdf` | `96a1c61c245003db` | 5 | the team's house working format |
| `REF_B_opal_branded_LLY_2Q26_Earnings_Update_Opal.pdf` | `7fdb77fec640c76a` | 5 | the Opal-branded condensation |
| `REF_C_long_form_LLY_Q2-2026_Earnings_Update.pdf` | `48c1743ddfe23620` | 21 | the long form the short ones are cut from |

⚠ `git fetch origin` FAILED at this write (`Could not connect to github.com:443 after 21103 ms`); the blobs were already
in this device's object store from an earlier fetch, which is why the hashes could be taken at all. **The hash agreement
is this seat's own instrument, but the VINTAGE is inherited** -- if `origin/CLOUD` moved after that earlier fetch, this
device holds the earlier bytes. Re-verify at the next successful fetch.

## What this seat READ, and from which file

**`REF_B`, pages 1-5, read in full here** (text extracted with `pymupdf`). Its shape, measured from the document itself:
header line (name, ticker, event, quarter ended, reported date, price WITH its as-of date, market cap); a POSITION SUMMARY
that states the thesis and, in terms, **"No rating or price target is issued in this note -- the recommendation line is for
the portfolio manager"**; six KPI tiles (revenue, vs consensus with the estimate printed, non-GAAP EPS, EPS ex-item,
gross margin, FY guidance); positives and negatives as bullets each carrying its own figures; a guidance
**Prior / Updated / Direction** table; risks; valuation (peer multiples AND a DCF with the WACC stated); a
**When / Event / Why** catalyst table; an appendix with Q-over-Q and H1-over-H1 financials split by geography and product;
"Why we own it"; and a **Sources** block that, where two vendors disagree, **discloses the disagreement and explains both
constructions rather than picking one** (measured instance: a 39% beat against one consensus basis and a 5.2% miss against
another, with the reason each is defensible).
`REF_A` and `REF_C` are carried on the laptop MSTR's reading, NOT this seat's -- it has not opened them.

## THE L4 DELTA -- what our pages cannot generate today, first pass, against PRD v0.13

This is the CTO reading the references against the spec it owns. Each line names the clause, so the next bump can be cut
rather than debated.

1. ⛔ **QUARTERLY GRAIN IS ABSENT.** `REF_B` is a QUARTER note: Q2-2026 vs Q2-2025 and H1 vs H1 throughout. Our model
   block is ANNUAL (`C-MODEL-WINDOW-AND-ROWS`; the 8-quarter TTM inputs are the OPEN L4 question this seat already holds,
   Model brief M7). **Without quarterly actuals, none of the KPI tiles or the appendix table can be generated.** This is
   the largest single gap and it converts M7 from "robustness nicety" into a coverage requirement.
2. ⛔ **CONSENSUS AT THE EVENT, AND ITS VINTAGE.** `C-MODEL-FORECASTS` gives forward FY consensus (`BEST_*`). `REF_B`
   needs the QUARTER's consensus, and its Sources block turns on WHICH VINTAGE of consensus ("compiled before the
   quarter's business development was known"). A consensus figure without its compilation vintage cannot support that
   paragraph.
3. ⛔ **NO EVENT TRIGGER.** `C-INSTANTIATION-ENTRY` adds a SECURITY. An earnings update is an EVENT. Nothing in the spec
   starts a run because a company reported.
4. **Guidance prior/updated/direction: CLOSEST TO COVERED.** `C-FILINGS-ANALYZER` already extracts guidance changes; the
   PRIOR value and the DIRECTION arrow are the missing half.
5. ⛔ **DCF WITH A STATED WACC does not exist anywhere in the spec.** Valuation today is peer multiples
   (`C-PEER-SET-SA`, `C-PEERS-V-FLOORS`). A DCF is a new producer with its own assumptions surface, and its assumptions
   are exactly the kind of judgment `C-POSTURE` keeps machine-marked.
6. ⛔ **CATALYST CALENDAR (When/Event/Why) is absent** -- no clause produces dated forward events.
7. ⭐ **THE SOURCES BLOCK IS A RULE WE SHOULD ADOPT, NOT JUST A LAYOUT.** "Where sources disagree, DISCLOSE the
   disagreement and show both constructions" is the same discipline as `C-VERBATIM-GATE` and `C-MARK-NOT-DEGRADE`, applied
   to figures instead of prose. Today our provenance fields say WHERE a number came from; nothing says what to do when two
   defensible sources disagree, and the silent behaviour is to serve whichever the reader hit first.
8. **Position, weight and "Why we own it": PARTLY COVERED.** `C-POSTURE` carries membership and weight (`REF_A` prints
   FUND PFOE, WEIGHT 4.3%); the prose is judgment.
9. ⛔ **THE EXPORT ITSELF IS NOT IN THE SPEC.** Every FWD outcome serves a PAGE. His (2) asks for a 2-3 page FILE. That is
   a new endpoint, not a rendering detail, and it needs its own outcome.

## Disposition

**NOTHING HERE RE-OPENS ROUND 14.** The spec is frozen mid-round, 31 orders are executing, and none of the above changes
a cell a worker is building. It lands in the **PRD addendum that answers round 14's slug**, beside the CRO's seven
next-bump items, the CVO's two residuals, the Posture panel, the CEO-step answers and the filings bronze-retention defect.
**This seat carries it; no other seat is re-tasked by this record.**

## The one call this raises, and it is Andrew's

+-- CARD (report format) -- at Andrew ---------------------------------+
  **Does an Opal-generated report issue a RECOMMENDATION and a PRICE TARGET, or state the analysis and leave the
  recommendation to the portfolio manager?**
  `REF_A` (the team's house format) carries "Recommendation: Maintain position in PFOE" and a broker target-price table.
  `REF_B` (the Opal-branded one) says in terms that no rating or price target is issued and that the recommendation line
  belongs to the PM. His words name both as references and do not say which wins; the laptop MSTR named the tension and
  did not resolve it, correctly.
  ----------------------------------------------------------------------
  **REC -- follow `REF_B`: state the analysis, issue no rating or target.** Three reasons. (1) It agrees with what the
  spec already says about machine judgment -- `C-POSTURE` marks its verdict machine-made and "nothing in the trade
  pipeline reads it"; a generated BUY/HOLD is the one output that would invite being read as advice. (2) `REF_B` is the
  Opal-BRANDED artifact, i.e. the one shaped for how we present, and it is the one he pointed at for "a better version of
  this". (3) The house format's recommendation line is a HUMAN's act at a specific moment; a pipeline that prints one
  either restates a stale human decision or manufactures a new one. **A target-price TABLE sourced to named brokers is a
  different thing and is fine** -- that is reporting what others published, with attribution.
+---------------------------------------------------------------------+

-- `1.0.0_SA_CTO~Z`

---

## APPENDIX -- `4.0.0_SA_CRO~Z` READ `REF_A` AND `REF_C` (@`2d098d2ab7`): the delta STANDS, eight additions, and ONE CORRECTION TO MY CARD

This seat asked to be corrected before the addendum rather than after. The answer: **nothing in `REF_A` or `REF_C`
contradicts any of the nine items**, and item 1 (quarterly grain) is corroborated on both -- `REF_A`'s financial summary is
columned Mar-24 through Jun-26, `REF_C`'s snapshot is Q2-2026 vs Q2-2025 throughout.
**Provenance, and it is a genuinely independent path:** that seat read the PDFs out of the object store with `git show`
and recomputed sha256 on the extracted bytes, matching all three prefixes this seat took from its own extraction. **Two
seats, two paths, same hashes.** The inherited-vintage qualifier still stands for both of us: neither hashed bytes fetched
fresh from `origin/CLOUD`.

**EIGHT ADDITIONS to the L4 delta, carried as that seat's measurement:**
1. **FOUR forward years, not three.** `REF_A` carries 2025 | 2026E | 2027E | 2028E | 2029E; `C-MODEL-FORECASTS` specifies
   FY1-FY3 -- one short, and the fourth year is the one `REF_C`'s scenario table prices off.
2. **A balance-sheet block we do not pull at all**: cash, intangibles, fixed assets, total assets, current and LT
   liabilities, common equity, each as a percent of total assets. The model block's header scalars carry none of them.
3. ⭐ **`REF_C` s.8 ALREADY PRINTS Bear / Base / Bull** as `Key assumptions | FY2028E EPS | Multiple | Implied value`, with
   the bear and bull assumptions stated in words. **Andrew ruled Base at v0.12 and reserved Upside/Downside for "a
   methodology discussion" -- and the house's own answer to that discussion is in the document he sent us.** His open card
   should be re-put with `REF_C` s.8 in front of him rather than as an abstract question.
4. **Ownership and positioning as a SECTION** (`REF_C` s.7): institutional and insider ownership, shares short, percent of
   float, days to cover, the CHANGE in short interest, beta, and the ten largest holders with their 13F quarter.
5. **Per-product and per-region quarterly series** -- 14 figures by product by quarter with y/y growth, plus sales by
   region and therapy. **We have no product or segment time series anywhere**; segments are cited PROSE, which is exactly
   why the thesis driver chart refuses.
6. **y/y growth rows on every line** -- the Model sheet has none by construction.
7. **An earnings-call TRANSCRIPT is a cited source** (`REF_C` Sources). No transcript stage exists;
   `integrations/seekingalpha/rest_fetch.py` already documents a `/transcripts` endpoint on the session the Peers path now
   uses.
8. **Guidance as `Prior | Updated | Direction`** -- our analyzer extracts the item but neither the prior value nor the
   direction, which is the half that makes the line readable.

## ⚠ THE CORRECTION TO THIS SEAT'S OWN CARD, and it goes back to Andrew

My card asked whether an Opal report issues **"a RECOMMENDATION and a PRICE TARGET"**. `4.0.0_SA_CRO~Z`, having read
`REF_A` (which this seat has NOT opened), measures that its *"Rating actions and target price changes"* section **reports
what OTHER analysts did -- it is not a house target. NEITHER document issues a house price target.**
**So the card was over-stated by me, and it is narrower than I put it:** the only thing `REF_A` issues and `REF_B` declines
is **the POSITION LINE** (*"Recommendation: Maintain position in PFOE"*). The price-target half of my question was never a
live fork, and I have told him so rather than leaving the wider framing standing. **The REC is unchanged** -- follow
`REF_B` -- and that seat concurs, with the note that adopting `REF_B` costs us nothing of `REF_A`'s "Why we own" paragraph,
which is Opal's own voice.

**This is the exact failure this seat named in the PRD's own citation rule, committed one level up:** I characterised a
document I had not read, from a summary, and the characterisation was wider than the source. The delta items survive
because each names a clause rather than the document; the card did not, because it named the document.

-- `1.0.0_SA_CTO~Z`

