# CTO fold -- the 2026-10-02 Security Analysis UI/UX walk into DSGN_AMGTV1, AMGT_HARVST and AMGT_RESAPP

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~18:4xZ.
**Andrew-direct ~17:33Z**, record `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261002_173xZ_SECURITY_ANALYSIS_UIUX_WALK_BRIEFS_TO_CTO_Z.md`
@a48c546a1c, VERBATIM in part: "I want briefs written for frontend work that will go to COO~D, backend news scanner tie in
feature work should go to COO~H. CTO~Z should receive everything first to filter and properly fold in to their /canonical-flow."
**Inputs** (`4.0.0_SA_CRO~Z` msg 28626, @3d25203d5a):
- the frontend brief `docs/briefs/dsgn-amgtv1-security-analysis-uiux-brief-20261002.md` (O1-O8);
- the HARVST brief `docs/briefs/amgt-harvst-news-sentiment-and-windows-brief-20261002.md` (O1-O5);
- the register `docs/briefs/amgt-security-analysis-ui-findings-20261002.json` (36 SAUX rows).

## Rulings (the briefs' open questions; the CTO decides each)

| # | call | ruling | why |
|---|---|---|---|
| 1 | FWD-12 x FWD-23: light or dark (brief 1, section 0.1) | **LIGHT.** FWD-12's identity header leaves the band. The Lead Panel and the header become white hairline panels with navy ink, the /philosophy GraphicCard face, in the /book L0 order. FWD-20's band clause becomes `bandContainersTopLevel <= 1` and `lightOnDark == 0`. | Andrew offered both. Light is the C3 direction, it agrees with this seat's FWD-11 ruling (14:4xZ: the finished card family is /philosophy and the C3 target), and FWD-23's source is his own "need to keep going with" the /philosophy fixture cards. |
| 2 | FWD-21 restatement | **RESTATED.** One bubble per security stays (his 10-01 "no other views"). The calendar-month cursor gives way to rolling windows (FWD-26). The layout is a collage, largest at the centre, by a deterministic spiral placement with NO new dependency. The fill is the served tone through ONE shared sentiment-colour module, with a legend. | N7, N8, N10, verbatim. The spiral is the Topic Cloud placement rule already in the estate. A new layout dependency is not needed for a few dozen circles (build ladder rung 7, minimum code). |
| 3 | FWD-22: trim the 94 bars? | **YES, at rest.** It shows the 10 largest gainers and the 10 largest losers, and the full list opens in the same panel. Bars stay. The face states its window. | N7 names "the various chatter/price views" for too much scrolling (INFERRED for price, and named so). The full list stays one action away, so nothing is lost. |
| 4 | The sentiment ramp versus DESIGN C7 (brief 1, part V, INFERRED) | **ADMITTED, scoped.** The Topic Cloud ramp is diverging (-1..+1, neutral centre). C7's single-hue rule is for ORDERED scales. Sentiment is a diverging measure, so the diverging ramp applies to sentiment fills only, with a legend. | It is the estate's existing colorway (`getSentimentColor`, TopicCloud.tsx:44-90). A single-hue ramp would hide the sign, which is the point of the encoding. |
| 5 | The producer/serving split for the news-scanner work (brief 2, part II) | **HARVST writes gold; AMGT_RESAPP serves it.** HARVST FWD-16 (FinBERT tone per article version) and FWD-17 (per-name window tone, voters, counts). RESAPP FWD-36 (`?days=` windows plus tone on the chatter payload). | This seat's standing ruling (msg 28540): one project's loop never writes into another's surface. `scoped_amgt.py` / `monthly_chatter.py` are RESAPP's. |
| 6 | The FinBERT scorer | **REUSE `opal-news-ai-sentiment`** (finbert_batch_processor, `infra/aws/terraform/news-pipeline/finbert-batch.tf`). No new model and no external vendor: it is Opal infrastructure. The invoke grant for the HARVST gold-build role is a cell for the IAM lane. | Build ladder rung 2. Andrew-direct 2026-09-16: "finbert not being sure is not a vote", so neutral or low-confidence labels are not voters (FWD-17). |
| 7 | The 365-day window: history before 2026-01-01, or a stated start? | **A STATED START.** The served window start says "since <date>" where the store is shorter. No back-collection is pulled for it. | No new scraping or vendor cost. The face is honest (DSGN FWD-26). |
| 8 | Earnings dates (SAUX-10): no owner | **PRODUCER: AMGT_CORPUS**, as Bloomberg fields in the Model-block pull. **SERVING: AMGT_RESAPP FWD-37** markers. Until the pull exists, the route serves the marker kind with its reason, and DSGN FWD-5 renders the designed empty state. | It is not harvest data (brief 2). Bloomberg is the one source that covers every name, US and non-US. The pull waits on Andrew's vendor word already carded (CORPUS FWD-22 / FWD-20, `/open-calls` ~17:3xZ calls 2-3). This ruling spends no new vendor leg and adds the fields to that same pull. |
| 9 | Register rows assigned to `2.0.0_SA_COO~Z` | **Placed:** SAUX-10 to RESAPP FWD-37; SAUX-12, 22, 25 and 29 to RESAPP FWD-38; SAUX-28 and the serving half of SAUX-19 to RESAPP FWD-36. | Each is a served-data defect on RESAPP's routes. |
| 10 | SAUX-35's walker side (the `--thread` bar wait) | **Not a project cell.** The page half (Escape closes the account menu) is DSGN FWD-27. The walker change goes to the ui-walk skill's owner as a tool item. | The instrument is not the product. |

## What landed (this commit)

- `DSGN_AMGTV1_PRD.md` **v0.9**:
  - FWD-5, 12, 20 (band clause), 21 and 22 are amended, and FWD-25, 26 and 27 are new;
  - the ENRICHMENT BACKLOG gains the 36-row SAUX register, mapped to each row's FWD (coverage gate 36/36).
- `AMGT_HARVST_PRD.md` **v0.14**: FWD-16 and FWD-17.
- `AMGT_RESAPP_PRD.md` **v0.33**: FWD-36, 37 and 38.
- **All three are ENDPOINT changes.** The ratified-text halves read STALE, owed by `3.0.0_SA_CVO~Z` (`prd-signoff.py status`). Per
  the proportionate sign-off rule, the L4 notifier withholds the COO delivery until the CVO re-signs.

## Routing (L5/L6 is the COOs'; this seat cuts nothing)

| seat | project | cut from |
|---|---|---|
| `2.0.0_SA_COO~D` | DSGN_AMGTV1 | FWD-5, 12, 21, 22, 25, 26 and 27, plus the 29 COO~D register rows. The page reads served fields the day they are served. |
| `2.0.0_SA_COO~H` | AMGT_HARVST | FWD-16 and 17, plus the FWD-6 density enrichment (HARVST brief O5). |
| `2.0.0_SA_COO~Z` | AMGT_RESAPP | FWD-36, 37 and 38. |
| `2.0.0_SA_COO~X` | AMGT_CORPUS | The earnings-date fields join the Model-block field set, carried with the pending vendor word. No pull before that word. |
