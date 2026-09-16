# POSN_AGGFIX -- PRD (step 4)

```json
{
 "project": "POSN_AGGFIX",
 "directive": "D4",
 "fabric": "site-z",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md@1e268c164e",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Pipeline position:** step 4 (L4). **Author:** `1.0.0_SA_CTO~Z`. **Fabric:** site-z.
**Brief:** `docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md` @ `1e268c164e` (L1, `4.0.0_SA_CRO~Z`), written
from `4.0.0_SA_CRO`'s plan `org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md`
(blob `0765b9af1f`).
**Endpoint pin:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_AGGFIX_ENDPOINT_FORWARD_20260915_Z.md` @ `8b0805e72a`,
confirmed by Andrew 2026-09-15 ~17:0xZ. The ENDPOINT section below is that file's fenced block, byte for byte.
**Model set:** `org/standards/POSN_AGGREGATE_MODEL_SET.json` (landed with this PRD).

---

## s.0 v0.2 -- ANSWER TO THE BRIEF-HALF REFUSAL (`4.0.0_SA_CRO~Z` @`7ffc16301a`, review @`3cb4034158`)

**Author** `1.0.0_SA_CTO~Z` (L4), 2026-09-15. **Changes the brief half only.** The ENDPOINT section is byte-unchanged, so
`3.0.0_SA_CVO~Z`'s ratified-text signature at half_hash `33458b1d30...` stands. That was proven by computing
`half_hashes` on these bytes before the file was written.

**THE DEFECT, ADOPTED IN FULL.** Re-read by this seat at SITEZ HEAD: `lambda_function.py:1796-1798` writes each model
book's `aum` as `aum_data.get(model_code, 0)`, the dict `load_aum_data` (`:1421`) fills from the legacy file. And
`:1811-1814` writes the aggregate's `total_aum` as `sum(aum_data.values())` from the same dict. So C-CURRENT-SOURCE moves
five book-level values, and v0.1's C-FIVE-BOOKS-UNCHANGED, S6 bound and S8 bound could not all hold.

**THE FIX, the reviewer's recommended option:**
1. C-FIVE-BOOKS-UNCHANGED (s.4) is scoped to every field of the five books except each book's `aum`.
2. Each book's `aum` becomes that model's OWN row in the current file's `by_model`. No blend share is added to a book's
   `aum`; blends enter only the aggregate's weights (C-MEMBERS).
3. C-NEVER-WIDEN (s.4) names the five book-level `aum` values in the blast radius, moving from the July file's figures
   to the current file's.
4. S2 (s.7) adds a census of the readers of `current_holdings.<code>.aum`, and of `json/positioning/positioning_data.json`
   outside the Positioning page directory. The reviewer's text-grain read found no Models-mode reader at portal
   origin/PROD `edf85ce503`, and did not measure destructured reads or consumers elsewhere.
5. C-NO-SILENT-EMPTY (s.4) states what survives. A failed weight read today writes `aum` 0 into every book (`:1798`).
   This project keeps that fallback for the books and changes only the aggregate's behaviour.
6. The S6 and S8 bounds (s.7), s.8 row 27 and s.10 step 1 are brought into line.

**THE TWO NON-BLOCKING NOTES, TAKEN:** S4 names `infra/aws/lambda-edge/shared-advisor-router/index.mjs` as its first
read. C-ONE-BOOK says the partner-firm-selection behaviour is read from the page by S13 and S14.

**CHECKED AND MATCHING BY THE REVIEWER, not re-opened:** the s.8 denominator and its line references; the S6 to S8
producer lines, `OUTPUT_KEY` `:2529` and the upload `:2618-2636`; S9; S10; the standards file's keys; S4's scope.

---

## ENDPOINT (step 2, /endpoint --forward)

```
ENDPOINT -- POSN_AGGFIX (confirmed by Andrew 2026-09-15)

  FWD-1  Opal staff can view one aggregate book of Opal's primary models on the
         Positioning page
         DONE WHEN  EXERCISED -- an Opal user has opened Positioning, chosen the
                    aggregate, and read both the composition picture and the
                    holdings table for it
         ACCEPT     An Opal staff member opens Positioning, picks the aggregate,
                    and both the composition chart and the holdings table show
                    the combined positions of Opal's primary models and blends of
                    them, as one book for all of Opal.

  FWD-2  Nobody outside Opal sees the aggregate on the page
         DONE WHEN  EXERCISED -- the page has been opened as an advisor and as a
                    client, each including a viewer whose browser remembers the
                    aggregate as its last choice, and no aggregate choice appeared
                    for either
         ACCEPT     An advisor or a client looking for the aggregate cannot find
                    it, and one whose browser remembered it lands on an ordinary
                    model instead.

  FWD-3  Each aggregate holding shows how the models share it, marked as all of Opal
         DONE WHEN  EXERCISED -- an Opal user has read the per-model split on
                    aggregate holdings, laid out as it was before the view was
                    removed, on the page as it looks today
         ACCEPT     For any aggregate holding, an Opal user can read how much of it
                    each model accounts for, in the layout the page used before,
                    plainly marked as all of Opal rather than any advisor's own
                    book, and as easy to read as the columns beside it.

  FWD-4  The aggregate uses Opal's current model mix
         DONE WHEN  EXERCISED -- the aggregate's model mix has been compared with
                    Opal's most recent assets-by-model figures, and they agree
         ACCEPT     The share each model carries in the aggregate matches Opal's
                    latest assets by model, not a mix left over from months ago.

  FWD-6  Every primary model's money counts in the aggregate, blends included
         DONE WHEN  EXERCISED -- the aggregate's inputs have been read: each blend of
                    primary models counts through the models it is split between,
                    nothing outside the primary models and their blends counts,
                    and the per-model figures have been reconciled to Opal's own
                    total
         ACCEPT     No primary model and no blend of primary models is left out of
                    the aggregate, nothing else is let in, and any gap between the
                    per-model figures and Opal's own total is explained, never
                    silently dropped.

  FWD-7  The aggregate figures are not sent to anyone outside Opal
         DONE WHEN  EXERCISED -- what an advisor's and a client's signed-in
                    sessions receive has been read and neither carries the
                    aggregate, while an Opal session still receives it
         ACCEPT     Looking at what an advisor's or a client's browser is given
                    shows nothing about Opal's model mix or Opal's total, while
                    Opal staff still get the aggregate and the page still works
                    for them.

  FWD-8  What clients and advisors already see on Positioning does not change
         DONE WHEN  EXERCISED -- each of the five model views has been compared
                    before and after the change, and they match
         ACCEPT     A client or advisor viewing any of the five models sees the same
                    holdings and weights after the change as before it.

  FWD-9  An Opal user who opens Positioning starts on the aggregate, unless they
         last chose another book
         DONE WHEN  EXERCISED -- Positioning has been opened as an Opal user with no
                    remembered choice and landed on the aggregate, and opened again
                    with a different book remembered and landed on that book
         ACCEPT     An Opal staff member who opens Positioning fresh sees the
                    aggregate first, and one who last looked at a particular model
                    comes back to that model.
```

---

## 1. The arc

The project starts with five reads that settle what the build stands on, because each one can change a cell: where
the gap between Opal's per-model assets and its own total comes from (S1); who else writes the aggregate block (S2);
what the page's internal-viewer check actually admits (S3); where, if anywhere, a viewer-tier refusal runs today
(S4); and whether the running producer matches its source (S5). Those unlock the producer change: the aggregate
takes its weights from Opal's current assets-by-model file, counts only the primary models and their blends, and
moves out of the file every signed-in viewer receives into its own Opal-only file, while the five model books stay
byte-identical (S6 to S8), landed through the producer's Terraform module under the never-widen halves (S10). That
unlocks delivery: a route that hands the Opal-only file to internal viewers and refuses advisors and clients (S11).
That unlocks the page: the aggregate selector, both panels, the per-model columns in the prior layout, and the
default-unless-remembered landing, all for Opal users only (S12 to S15). The arc ends when every outcome has been read
on the served page as an Opal user, an advisor and a client (S16).

## 2. Purpose -- what DONE means

An Opal staff member opens Positioning and, by default, reads one book for all of Opal: the combined positions of
the primary models and their blends, weighted by Opal's current assets by model, with each holding's split across
the models shown the way the page showed it before. Nobody outside Opal can see that book or receive its figures.
Nothing an advisor or a client already sees on Positioning changes.

## 3. Territory -- what this owns, and what it only relies on

**OWNS:**
- **T1.** The aggregate book in Models mode of the Positioning page: its selector entry, its two panels, its
  per-model columns, its viewer gate, its remembered-selection handling and its default landing.
- **T2.** The aggregate block the Positioning producer writes, and where that block's model weights come from.
- **T3.** The Opal-only file that carries the aggregate, and the route that serves it to Opal users alone.
- **T4.** The deploy of T2 and T3 through the producer's Terraform module.

**RELIES ON (does not own):**
- Opal's assets-by-model file `platinum/mdpf/global/aum-metrics.json`, its publisher, and the MDPF gold producer
  behind it. The gap in it belongs to that producer's owner; this project explains it and edits nothing there.
- The portal's internal-viewer predicate and the viewer-request auth function that injects the tier header.
- The portal colour law for the light canvas.
- The producer role's existing S3 grant on the portal bucket.

**SIBLINGS:**
- **POSN_ASTTAX** (D4, CLOSED @`e223c78ed5`). Same page, same producer, same served file. Its five-class taxonomy,
  benchmark rows and Satellites output ship beside the aggregate and must not move.
- **ETFS** macro (D4). The Satellites mode is its territory and is untouched.
- **The MDPF AUM family.** Relied on, never modified.

## 4. Acceptance properties -- these BIND the decomposition

- **C-ONE-BOOK.** There is one aggregate, for all of Opal. No aggregate per partner firm is built. Andrew b): "we just
  need it at global level". Both sources are already Opal-wide (brief F1 and F4; `4.0.0_SA_CRO~Z` msg 23178).
  Whether the aggregate shows while an internal viewer has a partner firm selected is read from the page by S13 and
  S14; it is the same global book either way.
- **C-MEMBERS.** The aggregate counts the primary models UST, ST, INT, LT and ULT, and blends whose every constituent
  is a primary model, each blend added to its constituents by share. Nothing else counts, and assets left out are
  reported with the aggregate. The members and the rule are data in `org/standards/POSN_AGGREGATE_MODEL_SET.json`.
  The two blends' constituents there are INFERRED from their names and are verified by S17. Andrew a) and f).
- **C-CURRENT-SOURCE.** The aggregate's model weights come from `platinum/mdpf/global/aum-metrics.json` `by_model`.
  The producer stops reading `json/portfolios/aum-metrics.json`, the dependency Andrew's 2026-09-09 ruling 5 treated as
  gone. Any reconciliation this project prints names the source file's own `period`. No date is promised on the page:
  FWD-5 is retired.
- **C-NO-SILENT-EMPTY.** A failed or partial weight read never produces an aggregate that reads as current. Today the
  producer serves an empty aggregate and still publishes when the weight read fails (brief F3, `:1474-1476` then
  `:1538-1541`). The five model books keep their current failure fallback, which writes `aum` 0 into each book
  (`:1798`); this project changes only the aggregate's behaviour on a failed or partial read.
- **C-GAP-EXPLAINED.** Any gap between the per-model figures and Opal's own total is explained before the aggregate is
  read as current. The explanation is this project's read of the producer that makes the file (S1). A defect found
  there is filed as a surprise row for its owner, and this project does not edit that producer.
- **C-OPAL-ONLY-DATA.** The aggregate's figures reach internal viewers only. The route refuses the advisor tier AND the
  client tier. A pattern that refuses clients alone is not enough. The route's refusal is exercised for an advisor
  and a client and its allowance for an internal viewer.
- **C-EXISTING-PREDICATE.** The screen gate uses the page's existing internal predicate, `isInternal() || isDev()`
  (`Positioning.tsx:267` @ portal `edf85ce503`), not a new one. What `isDev()` admits is read by S3 before the gate
  relies on it.
- **C-PRIOR-LAYOUT.** The restored selector entry and per-model columns follow the layout the page had before portal
  commit `d53049a0` removed them, re-authored only as far as today's colour tokens require. Andrew c): "how it was
  before is the right layout". The page is verified by rendering it as an Opal user, an advisor and a client.
- **C-DEFAULT-UNLESS-REMEMBERED.** An Opal user with no remembered choice lands on the aggregate. A remembered choice
  wins. A remembered or hand-edited aggregate choice is honoured only for an internal viewer, and anyone else falls
  back to the ordinary default. Andrew's D4 sentence.
- **C-FIVE-BOOKS-UNCHANGED.** In the shared served file, the five model books are byte-identical before and after every
  producer change in every field except each book's `aum`. Each book's `aum` moves to that model's own row in the
  current file's `by_model`, with no blend share added, because `lambda_function.py:1796-1798` writes it from the same
  table as the aggregate's weights. Everything else POSN_ASTTAX left in that file stays as it left it.
- **C-NEVER-WIDEN.** Any change to served output lands with the CTO and COO halves naming its blast radius. The writers
  of the aggregate block and of the shared file, and the readers of each book's `aum`, are counted first (S2), and the
  counts are printed. The blast radius names the five book-level `aum` values, which move from the July file's figures
  to the current file's. The producer deploys
  through its module with `safe-apply`, never a direct function-code update, with its change-management entry opened
  at the start and closed at completion.
- **C-PORTAL-PROMOTE.** Portal changes are committed behind the promote. The DEV to PROD promote, and any push, happen
  only on Andrew's word. The site-Z push hold stands.

## 5. Out of scope

- The aggregate on Attribution and Factor Tilts.
- The AGG bond-fund ticker, which shares the string. Any change near it discriminates per call site.
- A per-advisor aggregate.
- An aggregate per partner firm.
- A date on the page for the aggregate's model mix. FWD-5 is retired.
- The Satellites mode.
- The two dead portal fetch functions that still name the legacy AUM route (brief F8). They are surfaced, not removed.
- The legacy `json/portfolios/aum-metrics.json` object and its writer. This project stops reading it and decides
  nothing else about it.
- Any change to the MDPF gold producer or its publisher.
- The toggle-persistence pattern. It already exists and is reused.
- How this project relates to the D4 directive PRD `docs/architecture/D4_ETF_POSITIONING_VARIANT_PRD.md`, which was
  not read for this PRD.

## 6. Rulings that BIND

- **2026-08-24, Andrew-direct** (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_PULL_AGG_VIEW_THREE_PAGES_AND_TOGGLE_PERSISTENCE_PATTERN.md`).
  The concern, verbatim: *"my concern here is that the "Agg" view is somehow tied to Opal's aggregate models somehow as
  opposed to the Advisor's aggregate Opal Model exposure, which would be a problem."* This project restores the view
  for Opal users only, so that no advisor reads Opal's mix as their own.
- **2026-09-09, Andrew-direct ruling 5** (record
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md` `:29-31`),
  verbatim: *"We've excised the need for this already via not displaying an "AGG" view, which is what required
  aum-metrics. Neither /attribution nor /factor-tilts should have any reliance on /json/portfolios/."* Carried by
  C-CURRENT-SOURCE.
- **2026-09-15 ~16:2xZ, Andrew-direct:** POSN_AGGFIX is a D4 Positioning project for the `~Z` fabric. SITEZ record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md`.
- **2026-09-15 ~17:0xZ, Andrew-direct:** the endpoint answers a) to h), D4, and the full canonical flow. SITEZ record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_170xZ_POSN_AGGFIX_L2_ANSWERS_DONE_WHEN_D4_FULL_FLOW.md`.
  FWD-5 is RETIRED on e) "no this is irrelevant", and its id stays vacant.
- **D1 to D3, as settled.** The weights switch to the current file in the same change (D1). Blends count by share into
  their primary constituents (D2). The aggregate's figures move out of the shared file into an Opal-only one (D3).
  These are `1.0.0_SA_CTO~Z`'s reading of Andrew's d), f) and g), relayed back to him in plain words (msg 23179). If
  he reverses one, this PRD bumps.
- **Worker subagents hold NO cloud identity of their own. APPLIES to this project**, whose decomposition will seat
  workers: S1, S2, S4, S5, S9 and S17 read cloud or deployed surfaces, and S10's deploy runs from the box.
  > **Worker subagents hold NO cloud identity of their own.** A worker inherits the BOX's ambient AWS
  > credentials, which resolve to `Action:*` on `Resource:*`; there is no worker principal to scope, so a
  > cell that reads or writes a cloud surface from a worker is running as the box and not as itself.
  > ACCEPTED AS THE POSTURE FOR NOW by Andrew-direct 2026-09-05 ~13:3xZ at the `4.0.0_SA_CRO` terminal,
  > VERBATIM "recs approved" (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/`
  > `ANDREW_DIRECT_20260905_133xZ_RECS_APPROVED_BRIEF_TO_CUT_BRIEF_COMMISSIONED_WORKER_AMBIENT_CREDS_ACCEPTED.md`
  > @`8e89f1127f`), on `TO-OS-s-6`'s measurement by `0.7.0_AE_CloudOps~W`. **The word ACCEPTS the posture
  > and OPENS NO IAM ACT** -- do not read it as authorising a scoping project, and do not read it as
  > licence to widen what a worker touches.
- **Standing:** the site-Z push hold; the monitor and alert moratorium, so no freshness check or alarm is built on the
  aggregate; secrets through `comp-secrets`; NEVER-1 never-widen.

## 7. SURFACE MANIFEST (step 4 -> step 5)

Coverage by subtraction from printed denominators. **endpoint_outcomes = 8** (FWD-1, FWD-2, FWD-3, FWD-4, FWD-6, FWD-7,
FWD-8, FWD-9); **OWNS items = 4** (T1 to T4); **rows = 17**.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-6 | `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`; `s3://opal-data-assets/portal/gold/mdpf/global/aum-metrics/2026-09-14.json`; `s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json` | measured (gap 8,324,465.16 present in gold and platinum; legacy file tied within 0.01) | `4.0.0_SA_CRO~Z`, brief F4, head plus parse, 2026-09-15 16:41Z | worker, read-only | verify | -- | C-GAP-EXPLAINED | explain only; a defect is a surprise row for the producer's owner |
| S2 | FWD-7, FWD-8 | every writer of `current_holdings.AGG` and of `json/positioning/positioning_data.json`; every reader of `current_holdings.<code>.aum` and of that file outside `portal/src/pages/Positioning` | unmeasured (one writer found, brief F3; no Models-mode `aum` reader at text grain, `4.0.0_SA_CRO~Z` review @ `3cb4034158`; no census) | brief Part V item 5, Part VII item 7; the v0.1 brief-half review | worker, read-only | verify | -- | C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED | both censuses printed with their denominators before S8 |
| S3 | FWD-2, FWD-9 | `portal/src/pages/Positioning/Positioning.tsx:267` `isInternal() \|\| isDev()` @ portal `edf85ce503` | inferred (what `isDev()` admits is unread, brief Part VII item 9) | `4.0.0_SA_CRO~Z`, brief F6, `git show` at origin/PROD | worker, read-only | verify | -- | C-EXISTING-PREDICATE | -- |
| S4 | FWD-7 | viewer-tier enforcement for `/api/general/*`: first `infra/aws/lambda-edge/shared-advisor-router/index.mjs` (where `X-User-Tier` is defined), then `infra/aws/lambda-edge/auth-validator-edge/index.mjs:385` (injects it) and `infra/aws/lambda-edge/public-data-router/index.mjs` | unmeasured. The proxy docstring `portal/src/api/portal-proxy.ts:1419-1426` @ `edf85ce503` says the model route "blocks client tier". The two edge functions `comp-routes trace` names for that URL were searched and show no tier branch. Where a refusal runs, if one does, is unread | `1.0.0_SA_CTO~Z`, `comp-routes trace` on both URLs plus a native search of both functions, this PRD; `comp-find -i x-user-tier infra/aws`: 19 hits across 6,495 files | worker, read-only | verify | -- | C-OPAL-ONLY-DATA | decides S11's home; a live exposure found here is a surprise row, not this project's fix |
| S5 | FWD-4 | deployed `yang-generate-positioning` bytes against `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` at SITEZ HEAD | unmeasured (brief Part VII item 2) | -- | worker, read-only | verify | -- | C-NEVER-WIDEN | compare against the build input, never by file name |
| S6 | FWD-4, FWD-6 | `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:1421-1476` (`load_aum_data`; name map `:1437-1451`; legacy read `:1461`; empty on a failed read `:1474-1476`) | measured | `4.0.0_SA_CRO~Z`, brief F3, source read @ `ec29ae6fae`; `1.0.0_SA_CTO~Z`, native search confirms `:1421` | worker, `infra/aws/lambda/v2_portal/yang_pipeline/positioning/**` | port | S1, S5, S17 | C-CURRENT-SOURCE, C-MEMBERS, C-NO-SILENT-EMPTY | the five model books' holdings and weights inputs untouched; each book's `aum` moves to its own current row |
| S7 | FWD-6 | same file `:1525` `calculate_aggregated_holdings`; zero total returns an empty aggregate `:1538-1541` | measured | brief F3; native search confirms `:1525` | same | align | S6 | C-MEMBERS, C-NO-SILENT-EMPTY | the exercise re-derives per-holding values by hand for a sample |
| S8 | FWD-7, FWD-8 | same file `:1811` (the aggregate write), `:2529` `OUTPUT_KEY = 'json/positioning/positioning_data.json'`, upload `:2618-2636`; NEW -> an Opal-only key beside it, home chosen at L5 | measured (write sites); absent (the new key) | `1.0.0_SA_CTO~Z`, native search, this PRD; brief F1 for the served block | same | wire | S2, S7 | C-OPAL-ONLY-DATA, C-FIVE-BOOKS-UNCHANGED | the five books byte-identical in the shared file before and after, except each book's `aum` |
| S9 | FWD-4, FWD-7 | `infra/aws/terraform/yang-pipeline/iam.tf:34-46` `S3ReadWrite` on `arn:aws:s3:::opal-data-portal-v2/*` for `yang-pipeline-lambda-role` | measured: GetObject and PutObject already cover the current AUM file and any new key in that bucket | `1.0.0_SA_CTO~Z`, `comp-iam service yang-generate-positioning` plus a source read, this PRD | worker, read-only | verify | -- | C-NEVER-WIDEN | no IAM edit is expected; a key in another bucket reopens this row |
| S10 | FWD-4, FWD-6, FWD-7, FWD-8 | `infra/aws/terraform/yang-pipeline/lambdas.tf:162-172` `module "generate_positioning"` (artifact `yang-pipeline/yang-generate-positioning.zip`) | measured | `1.0.0_SA_CTO~Z`, source read, this PRD | worker, deploy through `safe-apply` | wire | S6, S7, S8, S9 | C-NEVER-WIDEN | both halves name the blast radius and the rollback per key |
| S11 | FWD-7 | NEW -> the route that serves the Opal-only key to internal viewers and refuses advisors and clients; home chosen at L5 after S4 | absent | -- | worker, edge or routing lane chosen at L5 | wire | S4, S8 | C-OPAL-ONLY-DATA | refusal exercised for an advisor and a client; allowance for an internal viewer |
| S12 | FWD-1, FWD-7 | `portal/src/api/portal-proxy.ts:1177` `getPositioningData` (unchanged); NEW -> a fetch for the Opal-only key | measured (existing); absent (new) | brief F6 @ `edf85ce503` | worker, `portal/src/api/**` | wire | S11 | C-OPAL-ONLY-DATA | the existing five-book contract unchanged |
| S13 | FWD-2, FWD-9 | `portal/src/pages/Positioning/Positioning.tsx:267` (predicate) and `:642` (the `HoldingsTab` mount, which does not receive it today) | measured | brief F6 | worker, `portal/src/pages/Positioning/**` | wire | S3, S12 | C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED | -- |
| S14 | FWD-1, FWD-3, FWD-9 | `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:39` (removal note), `:841` (first-render landing), `:1105` (Portfolio Composition), `:1197` (Holdings Breakdown) | measured | brief F6; the prior layout is read from `git -C portal show d53049a0` | same | port | S13 | C-PRIOR-LAYOUT, C-DEFAULT-UNLESS-REMEMBERED | current colour tokens; rendered as three viewer kinds |
| S15 | FWD-2, FWD-9 | `portal/src/pages/Positioning/shared/bookSet.ts:238` (the no-aggregate capability rationale) and `:39` | measured | brief F6 | same | align | S13 | C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED | never re-add an aggregate capability to the mode-only capability function |
| S16 | FWD-8 | the five model books on the served page as an advisor and a client, before and after | unmeasured | -- | worker | verify | S10, S14 | C-FIVE-BOOKS-UNCHANGED | the before read is taken ahead of S10 |
| S17 | FWD-6 | `org/standards/POSN_AGGREGATE_MODEL_SET.json` (members, blend constituents) | measured (5 primary and 2 blend rows in the current file, 0 outside); inferred (blend constituents) | `4.0.0_SA_CRO~Z`, brief F4; `1.0.0_SA_CTO~Z`, `comp-find 'Opal Blend 5050'`: 4 hits across 133 files, names only | worker, read-only | verify | -- | C-MEMBERS | a constituent that disagrees with a definition bumps the standard and this PRD |

**MECE check, both directions:**
```
  FORWARD   every OWNS item has >=1 row ............. 4 of 4   T1: S13 S14 S15 | T2: S6 S7 S8 | T3: S8 S11 S12 | T4: S10
  REVERSE   every WORK row maps to an OWNS item ..... 9 of 9   S6 T2, S7 T2, S8 T2+T3, S10 T4, S11 T3, S12 T3, S13 T1, S14 T1, S15 T1
  OUTCOMES  every FWD-n has >=1 row ................. 8 of 8   FWD-1 S12 S14 | FWD-2 S3 S13 S15 | FWD-3 S14 | FWD-4 S5 S6 S9 S10
                                                               FWD-6 S1 S6 S7 S10 S17 | FWD-7 S2 S4 S8 S9 S10 S11 S12
                                                               FWD-8 S2 S8 S10 S16 | FWD-9 S3 S13 S14 S15
  VERIFY    rows with verb verify ................... 8 of 17  S1 S2 S3 S4 S5 S9 S16 S17
```
Read the OUTCOMES line as assignment to a surface, never as issuance. A row owning an outcome is not a cell serving it.

## 8. BRIEF COVERAGE -- the headings of the brief @ `1e268c164e`

DENOMINATOR: 31 heading lines in the brief; 1 is the title; **30 non-title headings. COVERED: 30.** Each row carries the
heading's substance and where it is consumed.

| # | brief heading (line) | substance | consumed by |
|---|---|---|---|
| 1 | WHY THIS BRIEF EXISTS, AND WHAT IT DOES NOT CHANGE (`:14`) | Andrew's ~16:2xZ word; the plan re-cut into outcomes; not a gate; adds re-located producer lines, the gold-side gap, the legacy-reader census and ruling 5; leaves s.6 and D1-D4 to Andrew | s.6 (the ~16:2xZ word; s.6 settled as the full flow and D1-D4 settled at ~17:0xZ); s.7 cites the re-located lines |
| 2 | How the outcomes below map onto the landed endpoint (`:43`) | O1-O7 onto FWD-1..FWD-8; three findings: advisor tier outside Opal, the gap's owner outside the project, Phase 1 alone re-opening ruling 5 | ENDPOINT (FWD-2 and FWD-7 test advisors); C-GAP-EXPLAINED and S1; C-CURRENT-SOURCE (D1 settled together, so the Phase-1-alone branch is moot) |
| 3 | PART I -- THE OUTCOME TERRITORY (`:71`) | "Opal user" is the page's internal predicate; "non-Opal viewer" is every advisor and client | C-EXISTING-PREDICATE; C-OPAL-ONLY-DATA |
| 4 | O1 (`:77`) | an Opal user selects the aggregate in Models mode and reads both panels as for any model | FWD-1; S12, S14 |
| 5 | O2 (`:82`) | per-model contribution for every holding, legible on the light canvas | FWD-3; C-PRIOR-LAYOUT; S14 |
| 6 | O3 (`:87`) | no advisor or client finds the aggregate, including through a remembered or hand-edited selection | FWD-2; C-DEFAULT-UNLESS-REMEMBERED; S13, S15 |
| 7 | O4 (`:92`) | weights reflect recent model assets; the as-of date readable on the page | FWD-4 and C-CURRENT-SOURCE for the weights. The date clause is RETIRED with FWD-5 (Andrew e) |
| 8 | O5 (`:97`) | the reader can tell whether the blends are inside and how; nothing implies full coverage when a model is left out | FWD-6; C-MEMBERS (primary models and their blends only; assets left out reported); S17 |
| 9 | O6 (`:102`) | the aggregate total reconciles to Opal's own figure, or the reader can see why not | FWD-6; C-GAP-EXPLAINED; S1 |
| 10 | O7 (`:107`) | conditional on D3: no non-Opal viewer can retrieve the aggregate by any data route | FWD-7 (D3 settled: move it); C-OPAL-ONLY-DATA; S8, S11, S12 |
| 11 | PART II -- WHERE THE BOUNDARY SITS (`:114`) | the owns / relies-on / siblings / not-in-scope split | s.3 |
| 12 | II.1 This project OWNS (`:116`) | the Models-mode aggregate UI; the producer's aggregate block and its weight source; the Opal-only route if D3 is taken | s.3 T1, T2, T3 (D3 taken), plus T4 for the deploy |
| 13 | II.2 This project RELIES ON (`:124`) | the canonical AUM file, publisher and gold producer (gap owner unresolved); the internal predicate and JWT edge; the colour law | s.3 RELIES ON; S1 explains the gap without editing the producer; S3, S4 |
| 14 | II.3 Siblings, named (`:132`) | POSN_ASTTAX on the same page and producer; ETFS Satellites; the MDPF AUM family | s.3 SIBLINGS; C-FIVE-BOOKS-UNCHANGED; s.5 (Satellites) |
| 15 | II.4 NOT in scope (`:141`) | Attribution and Factor Tilts; the AGG ticker; per-advisor aggregate; toggle persistence reused; the dead legacy fetch functions surfaced; the legacy object's fate | s.5, every item, plus the per-partner-firm aggregate from Andrew b) |
| 16 | PART III -- THE QUALITATIVE BAR (`:154`) | answering the aggregate question; never mistaken for the reader's own positioning; never a stale mix as current; nothing else moves; legible in the house style | FWD-1 and FWD-3; FWD-2 and FWD-7; FWD-4 with C-CURRENT-SOURCE and C-NO-SILENT-EMPTY; FWD-8 with C-FIVE-BOOKS-UNCHANGED; FWD-3 with C-PRIOR-LAYOUT |
| 17 | PART IV -- THE SUBSTRATE (`:173`) | every finding carries its instrument, site Z, 16:36-16:55Z | s.7 MEASURED-BY column |
| 18 | F1 (`:177`) | served aggregate present: VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou`, 30 holdings, weights 1.0001, `model_breakdown` 30 of 30 over 5 codes, `total_aum` 1,637,144,180.01 | S8 (the block's current shape); S16 (the before read of the shared file) |
| 19 | F2 (`:192`) | weights are July's: legacy VersionId `2xsIhWJmoBR96Qy5NzsEpT8ZG5daawKe`, period 2026-07-22; five served `aum` fields equal the legacy rows; the blends sit outside | C-CURRENT-SOURCE; S6 |
| 20 | F3 (`:200`) | producer lines at SITEZ `ec29ae6fae`; the plan's line numbers are CLOUD-vintage; a failed weight read serves an empty aggregate and still publishes | S6, S7, S8 (lines re-confirmed); C-NO-SILENT-EMPTY |
| 21 | F4 (`:219`) | the canonical file: VersionId `OVcFBOpgjFywfYJGYjowX2VSVwLdiyez`, period 2026-09-14, seven rows with names as served, gap 8,324,465.16 identical in gold, the legacy file tied | C-CURRENT-SOURCE; C-GAP-EXPLAINED; S1; S17 and the standards file's `measured_against` |
| 22 | F5 (`:250`) | weights under each source, including the blends folded 50/50: UST 3.66%, ST 7.63%, INT 26.70%, LT 50.32%, ULT 11.69% | C-MEMBERS; the expected result S7's exercise compares against, labelled inferred on the blend constituents |
| 23 | F6 (`:262`) | portal anchors at origin/PROD `edf85ce503`; the local checkout is detached at an older commit; no aggregate entry on screen today | S3, S12, S13, S14, S15 (lines cited at PROD) |
| 24 | F7 (`:283`) | every signed-in viewer receives the same file with the aggregate inside; the JWT edge not re-measured | C-OPAL-ONLY-DATA; S4; S11 |
| 25 | F8 (`:290`) | 536 hits across 61,813 files; one live value reader of the legacy key, the producer at `:1461`; two dead portal wrappers with 0 callers | S6 (the read stops); s.5 (the wrappers and the legacy object) |
| 26 | F9 (`:312`) | the 2026-08-24 concern and decision verbatim; ruling 5 verbatim, its letter naming only Attribution and Factor Tilts, its premise that AGG is gone | s.6, both rulings verbatim; C-CURRENT-SOURCE |
| 27 | PART V -- WHAT MUST BE TRUE (`:326`) | nine items: s.6 answered; D1-D4 decided; the gap explained or disclosed; no dependency on `json/portfolios/`; never-widen with a writer census; five books byte-identical; the existing predicate; render as both viewer classes; Terraform deploy | 1 and 2: s.6. 3: C-GAP-EXPLAINED (explained, the bar Andrew confirmed). 4: C-CURRENT-SOURCE. 5: C-NEVER-WIDEN and S2. 6: C-FIVE-BOOKS-UNCHANGED, scoped at v0.2 to every field except each book's `aum`. 7: C-EXISTING-PREDICATE and S3. 8: C-PRIOR-LAYOUT, rendered as three viewer kinds. 9: C-NEVER-WIDEN, S5 and S10 |
| 28 | PART VI -- STATUS (`:356`) | status facts at the brief's clocks; marked not outcome-bearing | CONTEXT, no requirement. Superseded where they moved: the project is registered and the endpoint confirmed (s.6) |
| 29 | PART VII -- WHAT THIS BRIEF DOES NOT CLAIM (`:374`) | twelve disclosures | 1: the build is this project. 2: S5. 3: S4. 4: S1. 5: S17. 6: S7's exercise. 7: S2. 8: S1 (the owner is named with the explanation). 9: S3. 10: S14 reads `d53049a0`. 11: RESOLVED, the ~16:2xZ record is LOCAL on CLOUD @ `bd2fa195c0` and recorded on SITEZ. 12: s.5, not read here either |
| 30 | REFS TO CARRY (`:403`) | brief path, project, endpoint, directive and macro, source plan, siblings, prior art, rulings, clocks | the PRD header `brief_ref`; the preamble; s.3; s.6 |

## 9. Compiler evidence (`docs/architecture/PRD_AUTHORING_PROTOCOL.md` s.5)

**Surfaces touched:** a Lambda (the producer), portal components, and a new artifact claim. Not cross-firm: C-ONE-BOOK.

| tool + command | key output | disposition |
|---|---|---|
| `comp-iam service yang-generate-positioning` | role `yang-pipeline-lambda-role`; 7 operations; `s3:GetObject` GRANTED on the legacy AUM key at `:1459`; 6 UNRESOLVABLE-RESOURCE | Changed s.7 S9: the source read of `iam.tf:34-46` shows the bucket-wide grant, so the re-point and a new key need no IAM cell |
| `comp-routes trace getPositioningData` | "No match for: getPositioningData" | Confirmed the tool keys on URLs; the two URL traces below were run instead |
| `comp-routes trace /api/general/positioning/positioning_data.json` | behavior `/api/general/*`; viewer-request `auth-validator-edge`; origin-request `public-data-router`; key `json/positioning/positioning_data.json`; DESIRED plane | Changed s.7 S4 and S11 |
| `comp-routes trace /api/general/positioning/model.json` | the same edge chain; key `json/positioning/model.json` | Surfaced S4: no tier branch found in the two functions this chain names |
| `comp-platinum reverse platinum/mdpf/global/aum-metrics.json` | PRODUCER empty; served via `getAUMMetricsByFirm`; consumed by `ModelPortfolios` | Confirmed RELIES ON. The producer is named from the file's own `_provenance` (brief F4); the empty PRODUCER is a tool gap, not an absence |
| `comp-find -i 'Opal Blend 5050' org/standards data/mdpf/scripts/gold --files` | 4 hits across 133 files; keys in `dim_mdpf_aum_metrics.py:90-91` and `mdpf_revamp_model_crosswalk.py:215-216`; no constituent definition | Changed S17 and the standards file: constituents INFERRED |
| `comp-find -i 'x-user-tier' infra/aws --files` | 19 hits across 6,495 files; DEF `shared-advisor-router`; the injector `auth-validator-edge` | Changed S4 |

**Not run, and where each is carried:** `comp-cache collisions` and `comp-transform schema-check` on the Positioning
components go to the cells for S12 to S15. `check-lambda-layer-deps yang-generate-positioning` goes to the cell for
S10. The protocol's enforcement mode is WARN-only; these are named rather than skipped silently.

**Findings that updated this PRD:** the producer's IAM needs no cell (S9); the tier refusal for the existing model
route was not found where the traces point (S4); the blend constituents rest on names (S17).

## 10. Sequencing input for `2.0.0_SA_COO~Z` (not a dispatch)

1. **The verify rows first, in parallel:** S1, S2, S3, S4, S5, S9 and S17, plus S16's before read. S4 decides S11's
   home; S2's writer and `aum`-reader censuses precede any producer change; S17 precedes S6.
2. **The producer,** S6 then S7 then S8, in one worktree.
3. **The deploy,** S10, with both never-widen halves and the change-management entry.
4. **The route,** S11, after S4 and S8.
5. **The portal,** S12, S13, S14 and S15 in that order, committed behind the promote.
6. **The reads,** S16 and every FWD read on the served page as an Opal user, an advisor and a client, after Andrew's
   promote word.

Nothing here is a task order. L5 is the COO's.
