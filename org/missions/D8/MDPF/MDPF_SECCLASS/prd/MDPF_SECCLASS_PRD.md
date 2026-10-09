# MDPF_SECCLASS -- one canonical per-security classification table for every holdings surface

```json
{
 "project": "MDPF_SECCLASS",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.16",
 "step": 4,
 "brief_ref": "docs/briefs/canonical-security-table-brief-20260929.md@87ad6973f3",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17"],
 "status": "RATIFIED"
}
```

Author: `1.0.0_SA_CTO`. D8 / MDPF / laptop. Register row `org/missions/D8/MDPF/MDPF_SECCLASS/project.json` @dc175119ab.

Brief: `docs/briefs/canonical-security-table-brief-20260929.md` @`87ad6973f3` (the L1 brief of `4.0.0_SA_CRO` @be6ef31a65 plus
its O7/O8 addendum), 251 lines. Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CANONICAL_SECURITY_TABLE_ENDPOINT_FORWARD_20260929.md`
@`8639932f66`. Andrew confirmed its DONE WHEN lines, 2026-09-29 ~19:5xZ:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_195xZ_CANONICAL_SECURITY_TABLE_DONE_WHEN_CONFIRMED.md` @`3054ca47ec`.
The section below carries the endpoint's outcomes verbatim.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An advisor opens a Black Diamond client's holdings and sees each security's class and
         sub-class exactly as Opal's one shared list holds it, on the live Black Diamond outputs
         DONE WHEN  EXERCISED -- one live run of the Black Diamond chain for the latest day, traced
                    from the shared list to the page the advisor reads
         ACCEPT     for a real Black Diamond client, gold funds such as GLD and PHYS read as
                    commodities and VXX reads as a hedge, the same as Positioning shows them; the
                    trace shows every class on that page came from the one shared list, and the old
                    Black Diamond copy of the list was never consulted at any step
         SOURCE     brief O1 (l.33-41), "The candidate thread"

  FWD-2  Anyone who asks "what class is this security in Opal's holdings?" gets one answer,
         whichever screen or report they look at
         DONE WHEN  EXERCISED -- a set of securities checked across every holdings screen and report
         ACCEPT     a chosen handful of securities (at least one fund, one gold fund, VXX, and one that
                    is on no list) shows the same class and sub-class on Investor Reporting, Positioning,
                    each firm's reports, the 49F data, the partner feed, the market overview and the
                    attribution view; a security with no entry is shown as unclassified by name, never
                    quietly put into some class
         SOURCE     brief O2 (l.43-48)

  FWD-3  A person corrects or adds a security in one place, and every screen shows the change
         after its next ordinary run
         DONE WHEN  EXERCISED -- one real correction or addition made on demand, and read on every
                    screen after its next run
         ACCEPT     one security is added or corrected in the one place; nobody edits a second file or
                    list; after each screen's next run the new class shows everywhere FWD-2 names, and
                    nowhere still shows the old one
         SOURCE     brief O3 (l.50-54)

  FWD-4  Anyone can prove there is no second definition of a security's class left anywhere in
         Opal's code
         DONE WHEN  EXERCISED -- the repeatable check run on demand and read at each round's close
         ACCEPT     a check anyone can rerun lists every place in the code that assigns a class to a
                    security outside the one shared list, and says how many places it looked at; at the
                    end it lists none, and when an old copy is deliberately put back as a test, the
                    check finds it
         SOURCE     brief O4 (l.56-60); Part IV.4 (the existing one-definition pattern)

  FWD-5  The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it
         DONE WHEN  EXERCISED -- the copy deleted on Andrew's confirmation, after the check reads
                    that nothing uses it. That confirmation is Andrew's act for a destructive,
                    unrecoverable step, and it is asked for the moment the check reads zero.
         ACCEPT     before the deletion, the FWD-4 check and the list of who is allowed to read the old
                    copy both show no remaining user; every figure that moved when its last users were
                    switched was listed before and read after; the old values are kept on record, so a
                    disputed figure can still be traced
         SOURCE     brief O5 (l.62-66); Part V (l.179-181)

  FWD-6  Where a screen must classify from a different authority, that is written down, and a reader
         can tell which rule a security follows
         DONE WHEN  EXERCISED -- a reader looks up securities on the screens that follow another
                    authority and can say, for each, which rule applied and who owns it
         ACCEPT     an exception exists only where Andrew has agreed to that one by name; each names its
                    owner and its reason; a reader of a screen that keeps one can tell a class that came
                    from the shared list from one that came from the exception; the old quiet rules such
                    as "treat hedges as alternatives" or "VXX is equity" are gone, not declared
         SOURCE     brief O6 (l.68-73); section 2 below (the CTO's decision); Andrew-direct
                    2026-10-05 21:05Z ("consolidating sector onto this table"); midstream brief O3
                    (l.80-85)

  FWD-7  A security that newly appears in any firm's daily holdings gets its entry in the shared
         list on a regular schedule, before anyone has to notice it
         DONE WHEN  EXERCISED -- the scheduled classification fired on demand against a day that holds
                    a security with no entry. The ordinary scheduled run that follows is the check that
                    it keeps working, and a one-off catch-up run is test evidence only.
         ACCEPT     on a day holding a security that no list covers, the scheduled step adds its class
                    and sub-class without a person starting it by hand; no screen shows that security as
                    "Other" or unclassified for longer than the schedule's own gap; where the step asks
                    an outside model for the classification, that use has Andrew's word, never a default
         SOURCE     brief addendum O7 (CRO 102981, brief addendum pending); Andrew, walk 2 of 2026-09-29
                    ("structure a continuous pipeline as new securities become apparent")

  FWD-8  The shared list says whether each security is a fund or an individual stock, and a holdings
         table uses that to place individual stocks after the funds
         DONE WHEN  EXERCISED -- one real client's holdings, with both funds and individual stocks, read
                    on the page
         ACCEPT     each entry in the shared list says fund or individual stock; for a client holding both,
                    the holdings table shows the funds by their classes first and the individual stocks
                    after them, and nothing but the shared list decides which is which
         SOURCE     brief addendum O8 (CRO 102981, brief addendum pending); Andrew, walk 2 of 2026-09-29
                    ("individual securities should be marked as such ... a field in that DynamoDB table")

  FWD-9  Every stock collected for Rival Funds has its entry in the shared list, with its history
         filled in as far back as one year
         DONE WHEN  EXERCISED -- the whole Rival Funds stock list read against the shared list and the
                    history it fills
         ACCEPT     for every stock Rival Funds collects, the shared list gives its class, sub-class and
                    whether it is a fund or an individual stock, and its history is filled in back one
                    year (or to its first trading day, if it is younger); none is missing, and no new pull
                    reaches further back than one year (history already stored further back is kept)
         SOURCE     Andrew-direct 2026-10-05 ~03:3xZ at site Z, item 3 ("Every single stock that is
                    collected for the purpose of Rival Funds should be ingested with full backfill on the
                    ETFClassifier canonical opal table"); the cap, "we can just put a cap on all lookback
                    of 3 years for rivalfunds inclusions"; the depth, Andrew-direct 2026-10-06 ~18:1xZ,
                    "B, 1 year for rivalfunds"

  FWD-10 A stock that newly enters through the trading of the Opal ETFs or the rival ETFs gets its
         entry and its history by a dedicated routine, before anyone has to notice it
         DONE WHEN  EXERCISED -- the routine fired on demand on a day a stock first appears in an Opal
                    ETF's or a rival ETF's holdings. The ordinary scheduled run that follows is the check
                    that it keeps working
         ACCEPT     when a stock first appears in the holdings of an Opal ETF or a rival ETF, the routine
                    adds its entry and fills its history back three years without a person starting it;
                    where it asks an outside source or model, that use has Andrew's word, never a default
         SOURCE     Andrew-direct 2026-10-05 ~03:3xZ at site Z, item 4 ("As new stocks enter from trading
                    activity of the Opal ETFs and the Rival ETFs, those stocks should be backfilled and
                    included in the ETFClassifier table through some kind of routine, dedicated mechanism")

  FWD-11 A security that no source Opal already holds can place still gets its entry in the shared
         list, classified by Opal's AI classifier, and every entry made that way can be listed
         DONE WHEN  EXERCISED -- the classifier has run on a security nothing else could place, its
                    entry has been read, and the list of AI-made entries has been read and holds it
         ACCEPT     a security nothing else can place gets an entry with an asset class, a sub class and
                    a clean, properly capitalized name, and no person has to review it first. Anyone can
                    pull up one list of every entry the AI made
         SOURCE     Andrew-direct 2026-10-05 ~20:2xZ ("new rows are added for unrecognized securities and
                    theyre cleaned up and proper capitalized in that table") and ~20:5xZ ("Yes add the AI
                    Classifier. Those can land without human review, but we want an index somewhere of
                    all those that land by AI")

  FWD-12 The shared list carries the sector and industry group of each security an Opal ETF holds, and the Positioning
         page's ETF view shows sector, industry group, class and sub-class from the shared list
         DONE WHEN  EXERCISED -- the ETF view opened for one Opal ETF and its holdings' sectors read
                    against the shared list
         ACCEPT     every holding in an ETF's view shows the sector and the industry group the shared
                    list gives it, and the page takes no sector, industry group or class from anywhere
                    else. The list holds no measurements about a security, only what kind of thing it is
         SOURCE     Andrew-direct 2026-10-05 21:05Z ("I am ok with consolidating sector onto this table.
                    The question at that point isw whether the characteristics would need to be handled
                    here as well, which I'd prefer they were not"); Andrew-direct 2026-10-05 ~20:4xZ
                    ("consistently using ONLY the canonical ETFClassifier table"); Andrew-direct
                    2026-10-05 21:49Z (industry group moves onto the list with sector: "Yes agreed")

  FWD-13 An advisor opens any client's Holdings tab on Investor Reporting and every security's
         class and sub-class is the shared list's
         DONE WHEN  EXERCISED -- one Cottonwood client's Holdings tab opened and its securities read
                    against the shared list
         ACCEPT     every security on the page shows the class and sub-class the shared list gives it.
                    None is labelled from the old list, from a match on its name, from a word in its
                    name, or from the shape of its ticker. A security the shared list does not hold is
                    shown as unclassified, by name
         SOURCE     midstream brief O1 (l.67-71) and its candidate thread (l.60-65)

  FWD-14 An advisor reads a properly written security name wherever holdings are listed
         DONE WHEN  EXERCISED -- Andrew has opened a Cottonwood client's Holdings tab and read the names
         ACCEPT     the name beside each holding is the shared list's clean, properly capitalized name,
                    not the custody feed's capital-letter string. Andrew opens a Cottonwood client's
                    Holdings tab and cannot find a security name he would want cleaned up
         SOURCE     midstream brief O2 (l.73-78) and PART III item 1 (l.149)

  FWD-15 A person filling the shared list can pull, for each firm, the held securities that have no
         entry, and sees the count reach zero
         DONE WHEN  EXERCISED -- the list pulled for each of the three firms and read at zero
         ACCEPT     on demand, for each firm, a person gets the list of held securities with no entry
                    and its total. It reads zero for all three firms
         SOURCE     midstream brief O4 (l.87-91)

  FWD-16 Anyone looking at a mix by asset class on any screen can say how the shared list's six
         classes became that screen's groups
         DONE WHEN  EXERCISED -- a reader has looked up the mapping for each screen that groups
                    differently from the shared list
         ACCEPT     each screen that shows fewer groups than the shared list's six classes has one
                    stated mapping that the person looking at it can read. Every security that changes
                    group when a screen switches to the shared list was named before the switch
         SOURCE     midstream brief O6 (l.100-104) and PART III item 3 (l.152)

  FWD-17 Every security the old Black Diamond list holds has its entry in the shared list, placed
         again under the shared list's six classes
         DONE WHEN  EXERCISED -- the count of old-list securities with no entry in the shared list
                    read at zero
         ACCEPT     every security in the old list, held today or not, has an entry in the shared
                    list. Each was placed again under the shared list's own six classes and its own
                    wording, not carried across as the old list had it
         SOURCE     Andrew-direct 2026-10-05 21:49Z ("B all of it"; "i meant the asset classes"); his
                    word of ~21:4xZ the same day ("run it on a 6 field basis with the new
                    nomenclature/fields as part of the adaptation/reclassifier process")

```

## ENDPOINT PROVENANCE (outside the ratified section)

- **Pins.**
  - FWD-1..FWD-6 come from the brief @be6ef31a65.
  - FWD-7 and FWD-8 come from its addendum, which the endpoint cited as "pending". It is committed @`87ad6973f3`, the pin
    this PRD's `brief_ref` names: O7 at l.75-84, O8 at l.86-97.
- **The CTO decision the brief left open** (endpoint section 2): Bloomberg GICS (Positioning's ETF view) and the Schwab
  security master are DECLARED DEPARTURES under FWD-6. They are not writers of the canonical table, though either may be
  read as an INPUT to FWD-7's classification.
- **FWD-8's shape.** The brief's Part II reserves table SHAPE to POSN_ASTTAX's successor, while its O8 says "the FIELD is
  this project's". The endpoint took O8's reading, and this PRD closes it: the field `instrument_kind` is this project's
  (C-FIELD).

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-TABLE: the canonical table | consumed; POSN_ASTTAX (closed, C-ONE-SOURCE, C-FIVE-CLASSES) | DynamoDB `etf-classifications`, hash key `ticker`. The seed source is `infra/aws/lambda/v2_portal/_shared/etf_classification.py`, the seed path `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py`, and the one client `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`. Every surface reads a class through that client, or through a served artifact built by it. No second client copy is made; the existing second copy (`yang-generate-holdings-attribution/etf_classifications_dynamodb.py`) is a copy under FWD-4. |
| C-FIELD: fund or single security | extended; this project | One new attribute, `instrument_kind`, with values and definitions closed as data in `org/standards/MDPF_SECCLASS_CONTRACT.json` (v0.1.0 at ratification; v0.2.0 per the v0.2 addendum below). A row without it is shown as unknown, never defaulted. The table's existing columns and the five classes do not change. v0.2 adds `identifier_namespace` in {TICKER, CUSIP} (an absent value reads TICKER), so a CUSIP-keyed row has the key `CUSIP:<9 chars>`. |
| C-WRITER: who writes a row | extended; this project | Recorded per row in `classified_by` (the same contract file). v0.2 (addendum below): four values, `seed`, `scheduled`, `constituents` and `legacy`; the constituents seeder is a named writer that writes only where no row exists, and `legacy` labels a row written before the contract, provenance not recorded. `seed` is the seed path, and it always wins. `scheduled` is FWD-7's classification: it writes only a ticker with no row, by a write conditional on absence, so it never overwrites a correction. A correction is made in the seed source. Any other writer is a copy that FWD-4's census reports. |
| C-SERVER: server side | Andrew-direct 2026-09-29 ~19:5xZ | Classification, `instrument_kind` and the fund-before-single ordering key are produced by backend jobs and SERVED. A portal surface renders what it is served and derives none of the three. The portal's ticker constants (`etf-categories.ts`, `HoldingsBreakdownTable.tsx`) are copies under FWD-4. |
| C-VENDOR: outside models | Andrew's per-use word | FWD-7 classifies first from sources already held: the ticker's existing row in a retiring per-firm table, read once as an input and never as a writer; Bloomberg GICS fields; the Schwab security master. An outside-model call is made only under an Andrew word recorded for that use, never as a pipeline default. The estate's existing outside-model classifiers (`data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`, `data/cot/scripts/gold/B_01b.classify_new_securities.py`, `data/black_diamond/scripts/classification/classify_bd_securities.py`, `data/inf/scripts/classification/classify_assets.py`) write per-firm tables. They are copies under FWD-4/5 and are not the FWD-7 path. |
| C-DEPARTURE: declared exceptions | consumed; ETFS_CANON / ETFS_POSITIONING; the Schwab composition pipeline | Positioning's ETF view keeps Bloomberg GICS (`data/etfs/scripts/gold/etf_positioning_gold.py`). The Schwab firm composition keeps Schwab as security master (`data/canonical/schwab/gold/build_gold_firm_composition.py:7`). Each is listed in the departure register (S19) with owner and reason. A fold such as `hedge -> alternatives` or `VXX = equity` is not a departure. |
| C-SERVED: every retirement is a served move | law (CLAUDE.md NEVER never-widen) | Each surface's move from a copy to the canonical table lists, per ticker, the classes that change before the move and reads them after it on the served artifact. It has CTO+COO halves naming blast radius and a rollback per key. Writers of each served property are counted and printed. |
| C-FIRM: firm trees | law (CLAUDE.md NEVER cross-firm) | The canonical table is reference data shared across firms, so it is not firm data. Every pipeline keeps its own firm tree and reaches the table through its own cells. No cell writes one firm's pipeline tree from another's. |
| C-NAMES: rule 30 | consumed; LGIC | No new S3 address is created. If FWD-7 needs a new function, its names are builder output from `lib/opal_naming.py` `name()`, run 2026-09-29 ~20:0xZ: `name('mdpf', None, 'secclass', 'lambda')` -> `mdpf-secclass-lambda`; `name('mdpf', None, 'secclass', 'role')` -> `mdpf-secclass-role`; `name('mdpf', None, 'secclass', 'daily')` -> `mdpf-secclass-daily` (the schedule). Scope None marks a shared resource. The existing tables `etf-classifications` and `bd-securities` predate the canon and are not renamed here (R19). |
| C-DELETE: the fork's end | Andrew's act | `bd-securities` is deleted only on Andrew's confirmation, asked the moment FWD-4's census and the live IAM grant read (`infra/aws/terraform/bd-pipeline/iam.tf` and any the live census adds) show no reader. Its rows are exported to a retained record first. |

## 1. The arc

Start: one canonical table (`etf-classifications`) that two Positioning surfaces read. A Black Diamond fork
(`bd-securities`) has drifted from it: GLD and PHYS are alternatives/Gold there, VXX alternatives/Volatility. About fifteen
ticker-to-class copies sit across the BD, COT, INF, 49F, partner, market-overview, Positioning-lambda and portal code.

End: every holdings surface answers a ticker's class, sub-class and fund-or-single kind from that one table; the fork is
deleted; a census reads zero copies; new tickers get a row on a schedule; and the two legitimate other authorities are
declared.

## 2. THREAD -- FWD-1, the Black Diamond chain end to end (round 1)

1. Canonical table `etf-classifications` -> the BD classifier library (`data/black_diamond/scripts/gold/lib/etf_classifier.py`) reads it through the one client instead of scanning `bd-securities`; the `hedge -> alternatives` fold (`:99,108`) goes
2. BD classifier library -> BD silver assets dimension (`data/black_diamond/scripts/silver/build_bd_assets_dim.py:154`) takes class and sub-class from the canonical row
3. BD assets dimension -> BD gold composition artifacts (`data/black_diamond/scripts/gold/D_03.composition_artifacts.py:116`) carry the canonical class per holding
4. BD composition artifacts -> the served BD client surfaces (the advisor-facing composition artifacts and the client portal summary the BD gold chain serves) read on the page for one real client on the latest trading day
5. Trace -> every class on that page resolved to its canonical row, and the run's reads show no `bd-securities` access (CloudTrail/SDK trace or code-path read, printed with its denominator)

Round 1 builds only this thread. The thread's never-widen halves list GLD, PHYS, VXX and every other BD-held ticker whose
class moves, and read them back after.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

1. FWD-4 census instrument, before the first copy outside the thread retires: a rerunnable scan with a printed denominator, planted-copy negative control.
2. FWD-7 scheduled classification writing `classified_by = scheduled` rows for tickers with no row (the ~M workstream).
3. FWD-8 `instrument_kind` on every row, plus the served ordering key (the ~M workstream).
4. COT copies: `data/cot/scripts/gold/lib/etf_classifier.py`, the COT new-security scripts.
5. INF: `data/inf/scripts/classification/classify_assets.py` and its readers.
6. 49F: `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:58,220`.
7. Lambda copies: partners `etf_classification.py:230,235` and `etf_classifier.py:9`; `yang-generate-etf-returns/etf_classification.py:115`; `yang-generate-holdings-attribution/etf_classifications_dynamodb.py`; `market-overview-tiered-generator/lambda_function.py:67`; `yang-generate-positioning/lambda_function.py:324`.
8. `lib/research/identity/positioning_chain.py:163`.
9. Portal copies: `portal/src/pages/Positioning/constants/etf-categories.ts:11-66`, `portal/src/components/holdings/HoldingsBreakdownTable.tsx:69,129`.
10. FWD-6 departure register and its reader-visible marking.
11. FWD-3 one-edit exercise across every FWD-2 surface.
12. FWD-2 cross-surface read.
13. FWD-5: retire `seed_bd_securities.py`, `seed_canonical_securities.py` and the per-firm classifiers; IAM read; Andrew's delete confirmation; delete.

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Deploy mechanics |
|---|---|---|---|
| etf-classifications seed path | Lambda-side seed script, run on the seed path | the only human write path (FWD-3) | seed run; live rows compared to seed output |
| BD gold/silver chain | scheduled Python per firm (BD) | FWD-1 thread | DS lane `safe-deploy.sh`; firm tree kept |
| COT, INF, 49F / assets chains | scheduled Python per firm | FWD-2/4 enrichment | same, each in its own tree |
| yang-pipeline Lambdas (positioning, portfolios, holdings attribution), partners, market overview | Lambda artifacts with vendored modules | FWD-2/4 enrichment | Terraform only; deployed bytes diffed against the build input (`infra/aws/lambda/ci/` source maps) |
| portal bundle | React bundle | renders served values only (C-SERVER) | DEV by the lease seat; PROD on Andrew's word |
| FWD-7 scheduled classification | a scheduled backend job | new-ticker rows | names per C-NAMES if new; a schedule is the trigger, never upstream success alone |

## 5. WORKSTREAMS AND OWNERS

- **FWD-7 and FWD-8 backend cells: `2.0.0_SA_COO~M`, server side.** Andrew-direct 2026-09-29 ~19:5xZ, verbatim: "Some
  of the backend jobs should probably be assigned to COO~M as it pertains to item 7 and likely item 8, as we'd prefer
  to do a lot of that work server side."
  - ~M's write surfaces are the seed path, the scheduled classification and the served ordering key.
  - The thread workstream's write surfaces are the BD chain. The two are disjoint.
- **Seating fit, measured at L4 and not resolved here.** The seating lint (`.tools/to-decomp-ref-lint.py`) tests a NEW
  order's `<issued_to>`, which in this workflow is a project-named worker serial (e.g. `0.9.0_WK_MDPF_SECCLASS~n`). A
  fresh project worker holds nothing elsewhere and passes by construction. CLAUDE.md rule 27 states the seating rule
  does not reach Tier 1, and the COO lanes sit under `org/tier1_exec/`.
  - A probe of two draft orders at `org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/` read "0 under task_orders/".
  - The lint's path test names `task_orders/`, while the tree's folder is `task-orders/`. So the lint did NOT EVALUATE
    tree orders here: an instrument limit, recorded for the owning seat, and no pass or refusal is claimed.
- **The thread and the other enrichment workstreams** are issued by the COO lane seated at L6. Cells (a)+(b) of the
  placement (IRPT_BCKEND ~M round 25, IB-mr-251) and the portal half (DSGN_IRPTV1 ~D) are relied on, not re-done.

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. The field and the writer rule are data (C-FIELD, C-WRITER, `org/standards/MDPF_SECCLASS_CONTRACT.json` v0.1.0).
2. The departures are the two named in C-DEPARTURE. Any third is an L10 addendum, never a cell's choice.
3. The FWD-4 census is a repo instrument with a printed denominator and a planted-copy negative control. Its domain
   is ticker-to-class assignment in code outside the C-TABLE package, and the brief's token census (98 files) is its
   starting denominator, not a copy count.
4. FWD-5's delete is Andrew's act (C-DELETE); every other act is the cells'.
5. Outside-model use in FWD-7 is per-use Andrew word (C-VENDOR); a cell that needs it names the use and waits for the
   word on that act alone, while the rest of the round proceeds.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim` names the evidence class of the address. `measured` means the file was read to exist at L4 (2026-09-29
~20:0xZ); line numbers are `held` from ~D's census @099316efdd unless stated.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S01 | FWD-1,FWD-2,FWD-3 | `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` | measured | file read at L4 (client, table_name default `etf-classifications`) | Lambda shared | consume | -- | FWD-1 | the one client; no fork |
| S02 | FWD-3,FWD-7 | `infra/aws/lambda/v2_portal/_shared/etf_classification.py` + `yang_pipeline/seed-etf-classifications.py` | measured | files exist at L4 | seed path | align | S01 | FWD-3 | seed always wins (C-WRITER) |
| S03 | FWD-1 | `data/black_diamond/scripts/gold/lib/etf_classifier.py` | measured (file); held (`:99,108`) | file exists at L4 | DS BD | align | S01 | FWD-1 | fold removed; no bd-securities scan |
| S04 | FWD-1 | `data/black_diamond/scripts/silver/build_bd_assets_dim.py` | measured (file); held (`:154`) | file exists at L4 | DS BD | align | S03 | FWD-1 | firm tree kept |
| S05 | FWD-1 | `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` | measured (file); held (`:116`) | file exists at L4 | DS BD | align | S04 | FWD-1 | served move under halves |
| S06 | FWD-4,FWD-5,FWD-7 | `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`, `E_18.detect_new_securities.py` | measured | read at L4: writes `bd-securities`, classifies via OpenAI `gpt-5.4-mini` | DS BD | retire | S08 | FWD-5 | its detection may be reused as FWD-7 input; its writer retires |
| S07 | FWD-4 | `data/cot/scripts/gold/lib/etf_classifier.py`, `data/cot/scripts/gold/B_01b.classify_new_securities.py`, `E_18.detect_new_securities.py` | measured | files exist at L4 | DS COT | align | S01,S14 | FWD-2 | COT tree only |
| S08 | FWD-7 | NEW scheduled classification (names `mdpf-secclass-lambda` / `-role` / `mdpf-secclass-daily` if a function is new) | unmeasured | builder output C-NAMES | ~M backend | wire | S01,S02 | FWD-7 | writes only absent rows; vendor per C-VENDOR |
| S09 | FWD-8 | `etf-classifications` attribute `instrument_kind` + the served ordering key | unmeasured | contract C-FIELD | ~M backend | wire | S02 | FWD-8 | no class value moves |
| S10 | FWD-4 | `data/inf/scripts/classification/classify_assets.py` | measured | read at L4: writes `classified_by = gpt-4o-mini` rows | DS INF | retire | S14 | FWD-4 | INF tree only |
| S11 | FWD-4 | `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py` | measured (file); held (`:58,220`) | file exists at L4 | DS 49F | align | S01,S14 | FWD-2 | 49F tree only |
| S12 | FWD-4 | `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classification.py`, `etf_classifier.py` | measured (files); held (`:230,235`; `:9`) | files exist at L4 | Lambda partners | align | S01,S14 | FWD-2 | Terraform deploy |
| S13 | FWD-4 | `yang-generate-etf-returns/etf_classification.py`, `yang-generate-holdings-attribution/etf_classifications_dynamodb.py`, `yang-generate-positioning/lambda_function.py`, `market-overview-tiered-generator/lambda_function.py` (all under `infra/aws/lambda/v2_portal/`) | measured (files); held (lines) | git ls-files at L4 | Lambda yang / market overview | align | S01,S14 | FWD-2 | Terraform deploy; byte diff vs build input |
| S14 | FWD-4 | NEW census instrument (rerunnable; printed denominator; planted-copy control) | unmeasured | ruling 6.3 | verification | verify | -- | FWD-4 | reads code only |
| S15 | FWD-4 | `lib/research/identity/positioning_chain.py` | measured (file); held (`:163`) | file exists at L4 | lib | align | S01 | FWD-4 | -- |
| S16 | FWD-4 | `portal/src/pages/Positioning/constants/etf-categories.ts`, `portal/src/components/holdings/HoldingsBreakdownTable.tsx` | measured (files); held (lines) | files exist at L4 | portal | align | S09 | FWD-2 | renders served values (C-SERVER) |
| S17 | FWD-5 | `data/black_diamond/scripts/classification/seed_bd_securities.py`, `seed_canonical_securities.py`, `classify_bd_securities.py` | measured | files exist at L4 | DS BD | retire | S14 | FWD-5 | rows exported to a retained record first |
| S18 | FWD-5 | `infra/aws/terraform/bd-pipeline/iam.tf` + DynamoDB `bd-securities` | measured (file); table unmeasured at L4 | git ls-files at L4 | CloudOps | retire | S17 | FWD-5 | delete on Andrew's word only (C-DELETE) |
| S19 | FWD-6 | NEW departure register (Bloomberg GICS in `data/etfs/scripts/gold/etf_positioning_gold.py`; Schwab in `data/canonical/schwab/gold/build_gold_firm_composition.py`) | unmeasured | C-DEPARTURE | this project | wire | -- | FWD-6 | owner + reason per entry |
| S20 | FWD-1..FWD-8 | NEW journey test across S01-S19 | unmeasured | the eight ACCEPT lines | verification | verify | S05,S08,S09,S14 | all | reads served artifacts |

MECE check: outcomes 8/8 have at least one row. Every copy the brief's Part IV.3 names has a row: S03-S07, S10-S13 and
S15-S17. Relied-on work (cells (a)+(b), the portal display order) has no row by design.

## 8. BRIEF COVERAGE -- content carried, not just cited

The brief at @87ad6973f3 has 1 level-1 title, 8 level-2 headings (Parts I-VII and REFS) and 8 level-3 outcome headings:
17 of 17 are mapped.

| Brief heading | Carried content | Consuming sections / surfaces |
|---|---|---|
| Title and preamble | Andrew's words: the Positioning table feeds ALL holdings, a row per security with class and sub-asset, no duplicated tables or rules; placement (c); (a)(b)(d) placed elsewhere | header; C-TABLE; section 5 |
| PART I -- outcome territory | the table's identity (hash key `ticker`, five columns); seed source, seed path, client; the territory is every OTHER assignment plus the fork | C-TABLE; S01, S02 |
| O1 -- the thread | BD surfaces answer from the canonical table; GLD/PHYS Commodities/Metals, VXX Structured/Hedge; no `bd-securities` read; why BD (densest copies, one firm, one served surface) | FWD-1; section 2 hops 1-5; S03-S05 |
| O2 -- one answer anywhere | IR Holdings, Positioning Models/Satellites, BD/COT/INF composition, 49F dim, partner feed, market overview, attribution; unclassified by name | FWD-2; S07, S10-S13, S16 |
| O3 -- one edit | seed source only; no second file, table or hand `put-item`; PHYS first proof | FWD-3; C-WRITER; S02 |
| O4 -- no second definition | census outside the canonical package reads zero; `ids.py` one-definition pattern; repeatable, denominator printed, run at each round's close | FWD-4; ruling 6.3; S14 |
| O5 -- the fork gone, provably | no reader by census plus live IAM; last readers moved under halves with before/after; delete on Andrew's confirmation; seed-and-drift record kept | FWD-5; C-DELETE; S17, S18 |
| O6 -- declared departures | Bloomberg GICS (ETFs mode) and the Schwab security master as candidates; folds are copies, not departures | FWD-6; C-DEPARTURE; S19 |
| O7 -- scheduled new-ticker rows | a day-over-day draw gains its row on a schedule; one-off backfill is QA, scheduled run is acceptance; vendor model only on Andrew's per-use word | FWD-7; C-WRITER; C-VENDOR; S08 |
| O8 -- fund vs single security | the row carries ETF/fund vs single security; one sub-asset gradient for funds, single securities after; order is the portal's, FIELD is this project's | FWD-8; C-FIELD; C-SERVER; S09 |
| PART II -- boundary | owns copies, the fork and its IAM, the census, the departure register; relies on POSN_ASTTAX (table shape), IRPT_BCKEND (a)+(b), DSGN_IRPTV1 (display order), each firm's tree; siblings named | C-TABLE; C-FIRM; section 5; provenance (FWD-8 shape) |
| PART III -- qualitative bar | one answer, one edit, zero by census with its denominator, a moved figure read not predicted, nothing silently folds | C-SERVED; C-FIELD absent rule; ruling 6.3 |
| PART IV -- substrate | (1) table and one-source rule ratified; (2) fork and its drift, three values of VXX across three writers; (3) copies by file:line plus the 98-file token census; (4) the `ids.py` pattern; (5) three serving shapes; (6) retirement is a served move; (7) names predate the canon, R19 | section 4 engines; C-SERVED; C-NAMES; S03-S18 |
| PART V -- must be true | (a)+(b) landed first; seed source reproducible (live rows equal seed output, or the difference listed; POSN_ASTTAX seeder guard); census before the first retirement; per pipeline, rule 20 graph read plus halves plus ticker list plus before/after; IAM read before touching the table; Andrew confirms the delete; ordering answered in the portal half | backlog order (census item 1); C-SERVED; C-DELETE; S02; section 5 |
| PART VI -- status (not outcome-bearing) | ~D trace 17:4xZ values; placement 18:2xZ; token census 18:4xZ (98 files); IR today through `bd-securities` (moved by cell (a)) | section 1 arc; S-row claims |
| PART VII -- does not claim | no live table or deployed-byte read; dormant copies retire the same way; departures were the CTO's call (closed); no pipeline order (L5's); no new name proposed (C-NAMES gives builder output if needed) | provenance; ruling 6.2; C-NAMES; section 3 |
| REFS TO CARRY | brief path, siblings, prior art (the table, seed path, client, `ids.py`, the POSN_ASTTAX seeder guard), Andrew's words @099316efdd, placement @c3c3f414dc | header; C-TABLE; related in the register row |

## ADDENDUM v0.2 (1.0.0_SA_CTO, 2026-09-30 ~07:4xZ) -- contract wording, not an endpoint change

Records rulings already made and carried by the round-1 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md` @151c890591 (C-WRITER: four `classified_by` values, the 238 unlabelled rows to `legacy`)
and by ruling 103139 (E9: a CUSIP key as `CUSIP:<9 chars>` with `identifier_namespace`). C-FIELD and C-WRITER above are amended in place. No FWD line, DONE WHEN or ACCEPT changes: this is a change to the CONTRACTS
section under the sign-off's proportionate rule (Andrew-direct 2026-09-24: only an ENDPOINT change re-signs). The CVO may read it; nothing waits on it.

## ADDENDUM v0.3 (1.0.0_SA_CTO, 2026-10-05 ~03:4xZ) -- an ENDPOINT change: FWD-9 and FWD-10 added on Andrew's word

**Word:** Andrew-direct 2026-10-05 ~03:3xZ at site Z `2.0.0_SA_COO~RV`.
- Record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_CLICKABLE_TICKERS_ETFCLASSIFIER_BACKFILL.md`
  on origin CLOUD @41158af7f9, items 3 and 4. The three-year cap is record `cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_LOOKBACK_CAP_3Y.md`
  @357e681ddf (site-Z local, relayed verbatim by `0.0.0_AB_MSTR` msg 105116).
- Site Z (`1.0.0_SA_CTO~Z` msgs 29427 and 29446) asked this seat to place it.
- The "ETFClassifier canonical opal table" is this project's canonical table, DynamoDB `etf-classifications` (C-TABLE). That is why
  the work lands here and not in ETFS_RIVALS.

**What changed and why (endpoint re-entry):**
- FWD-7 was RIGHT and INCOMPLETE. Its domain is any firm's daily holdings; Andrew's item 4 adds the Opal ETFs' and the rival ETFs'
  trading. FWD-7 stands unchanged; FWD-10 is added at the next unused number.
- FWD-9 is new: a universe this project never named, Rival Funds' collected stocks.
- No outcome is retired.

**Contract notes (bind the next round's cells):**
- **C-BACKFILL.** "History" means the series a holding's modal reads for that security. Its homes and names are builder output
  (`lib/opal_naming.py address()` / `name()`, rule 30). The classification itself stays the `etf-classifications` row (C-TABLE,
  C-FIELD). The lookback is capped at three years, measured from the run day.
- **The security list is an INPUT from ETFS_RIVALS (site Z).** It is read from the artifact that project serves; it is never routed
  as work across fabrics. If no such served list exists, the next round's first cell names the gap as a row and comes back here.
  **Measured answer** (site Z `2.0.0_SA_COO~RV` msg 29471, relayed by `0.0.0_AB_MSTR` msg 105136): there is no dedicated list
  today.
  - **Interim input:** `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<report_date>/holdings-<revision>.parquet`,
    refreshed Monday to Friday at about 07:10 ET, with a 09:00 ET sweep.
  - **Planned:** gold table `security_universe` (3-year window, same cadence). Its served path comes from site Z, and the round
    switches to it when that path is served.
- **Vendor:** a history or classification source not already worded by Andrew needs his per-use word (CLAUDE.md). The routine never
  defaults to one.
- **Moratorium:** FWD-10's routine is a scheduled producer, not an alert or monitor (CLAUDE.md NEVER moratorium).

**Placement:** the next MDPF_SECCLASS round, cut by `2.0.0_SA_COO~M` from this seat's next round analysis. The current round's
spec and decomposition stay frozen, with the multi_asset leg V on Monday 10:15Z.

**Sign-off:** an ENDPOINT change, so `3.0.0_SA_CVO` re-signs the ratified-text half. The brief half: this is Andrew's own word,
recorded at site Z, so no CRO brief precedes it.

## ADDENDUM v0.4 (1.0.0_SA_CTO, 2026-10-05 ~21:0xZ) -- an ENDPOINT change: FWD-11 added on Andrew's word

**Word:** Andrew-direct at the `1.0.0_SA_CTO` terminal, three records in `org/tier1_exec/1.0.0_SA_CTO/deliverables/`:
- `ANDREW_DIRECT_20261005_202xZ_YCDGEN_INHOUSE_ENDPOINT_THREE_CALLS_ANSWERED_CLASSIFICATION_THROUGH_CANONICAL_TABLE.md`
  ("all security classification for ALL Opal applications passes through that table");
- `ANDREW_DIRECT_20261005_204xZ_YCDGEN_TYPO_AND_SWAP_AI_PIPELINE_CLASSIFY_IN_ETFCLASSIFIER_SHAPE.md`;
- `ANDREW_DIRECT_20261005_205xZ_AI_CLASSIFIER_YES_NO_HUMAN_REVIEW_INDEX_OF_AI_ROWS_YAHOO_PRICE_TABLE_OK_IF_NECESSARY.md`.

**What the table does today** (`2.0.0_SA_COO~M`,
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ETF_CLASSIFICATIONS_VOCABULARY_AND_UNKNOWN_ROW_PATH_20261005.md`
@73a3c60af8): a new security gets a row only from a direct match; one with no match is listed UNRESOLVED; no model is called.
13 rows are `classified_by model`, landed once from a reviewed set.

**What changed and why (endpoint re-entry):**
- FWD-7 and FWD-10 were RIGHT and INCOMPLETE: both end at UNRESOLVED when no held source matches. They stand unchanged. FWD-11
  is added at the next unused number. No outcome is retired.

**Contract notes (bind the next round's cells):**
- **C-WRITER.** The `model` value already exists in `org/standards/MDPF_SECCLASS_CONTRACT.json` (`classified_by.values`), with its
  writer `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` and its two confidence fields. FWD-11 puts that
  writer in service after the direct-match plan, for the tickers the plan leaves UNRESOLVED. It writes by the same conditional
  put, so it never replaces a row. The contract's precedence stands: a seed row always wins, and a correction is made in the seed
  source.
- **C-VENDOR.** Andrew's ~20:5xZ word is the recorded word for this use: the AI classifier in this path, with no human review
  before a row lands. It names no model. The cell uses the model the existing writer already calls and sends what that writer
  sends today (the security's name and ticker only). A different model, or a wider payload, needs his word.
- **Value bound.** A model verdict lands only if its `asset_class` and `sub_asset_class` are members of the table's own
  vocabulary; a verdict outside it leaves the ticker UNRESOLVED. The model never mints a class.
- **Clean naming.** The row's `name` is written in proper case from the source name, with vendor suffixes and all-caps removed.
  The rule is one function with a test table, not a model output.
- **C-AIINDEX (new).** The index of AI-landed rows is the rows themselves: `classified_by = model` with
  `classification_confidence`, `low_confidence` and the write time. One readable listing of them is rewritten by each classifier
  run. Builder output printed at this addendum: `address('mdpf','global','gold','ai_classified_securities','date=2026-10-05',
  object='index.json')` -> `s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=2026-10-05/index.json`. This amends
  C-NAMES' "no new S3 address" by this one. A row a later seed run corrects leaves the listing, because it is no longer
  `classified_by model`.
- **Consumers named, not built here:** IRPT_YCDGEN PRD v0.4 (C-CLASSIFY, C-RESOLVE) reads the table and asks for a row through
  this path. It adds no writer.
- **Moratorium:** the classifier is a scheduled producer. The listing is an artifact, not a notification.

**Placement:** the next MDPF_SECCLASS round, cut by `2.0.0_SA_COO~M` from this seat's next round analysis. The current round's
spec and decomposition stay frozen.

**Sign-off:** an ENDPOINT change, so `3.0.0_SA_CVO` re-signs the ratified-text half. The brief half: Andrew's own word, recorded
at this seat, so no CRO brief precedes it.

## ADDENDUM v0.5 (1.0.0_SA_CTO, clock read 21:06Z 2026-10-05) -- an ENDPOINT change: FWD-6 amended in place, FWD-12 added

**Word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_2105Z_SECTOR_CONSOLIDATED_ONTO_THE_TABLE_CHARACTERISTICS_NOT.md`,
and his word at the `4.0.0_SA_CRO` terminal
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_204xZ_HOLDINGS_SURFACES_ONLY_CANONICAL_ETFCLASSIFIER_TABLE.md`).
The check behind it: `docs/briefs/holdings-surfaces-canonical-classifier-check-20261005.md` @35859eb97d, placed by
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20261005_2056Z_HOLDINGS_SURFACES_CANONICAL_ONLY_INTO_MDPF_SECCLASS.md`.

**What changed and why (endpoint re-entry):**
- FWD-6 was WRONG in one member: it named Positioning's ETF view as a declared exception. Andrew's "ONLY" removes it. FWD-6 is
  amended in place, id unchanged; the Schwab firm data stays a declared exception, since no word of his names it.
- FWD-12 is added at the next unused number. No outcome is retired.

**Read by this seat (measured):** `data/etfs/scripts/gold/etf_positioning_gold.py:986-1009` and `:1208-1219`. The ETF producer
takes each holding's `GICS_SECTOR_NAME` from the daily Bloomberg characteristics file and serves it as `sub_asset_class`, accepted
only if it is one of the 11 adopted names (`:121-150`); `asset_class` comes from the cash flag. The table has no sector field:
its equity `sub_asset_class` mixes ten GICS names with size and region labels (`2.0.0_SA_COO~M`'s scan @73a3c60af8).

**Contract notes (bind the next round's cells):**
- **C-SECTOR (new).** One new attribute on `etf-classifications`, its name and closed values declared as data in
  `org/standards/MDPF_SECCLASS_CONTRACT.json` with the four-postulate record and a token census (rule 24). It is NOT the legacy
  `sector` attribute (179 seed rows of another grain), which keeps its bytes. Its values are the 11 names the ETF producer
  already adopts, so the page's vocabulary does not change. `sub_asset_class` is not rewritten by this change.
- **The writer.** The Bloomberg characteristics file is an INPUT: a scheduled writer copies `GICS_SECTOR_NAME` onto the security's
  row. A correction is made in the seed source and wins, as for every field (C-WRITER).
- **C-NOCHAR (new; Andrew's preference).** No measurement enters the table: no ratio, market value, yield, duration, beta or
  price. The characteristics file keeps its home and its readers. The table says what kind of thing a security is.
- **C-DEPARTURE** loses its Positioning member when FWD-12's move lands; until then it stands as written.
- **The move is a served-output move** (C-SERVED): per ETF, the sector of every holding is listed before and read after, and
  delta 0 is the expected read. A holding the table lacks is added first (FWD-9, FWD-10, FWD-11), never shown blank.
- **Not decided:** the ETF view's finer level, `industry_group`, stays on its current path until Andrew says.

**Placement:** the next MDPF_SECCLASS round. The current round's spec and decomposition stay frozen.

**Sign-off:** an ENDPOINT change, so `3.0.0_SA_CVO` re-signs the ratified-text half. The brief half: Andrew's own word.

## ADDENDUM v0.6 (1.0.0_SA_CTO, clock read 21:12Z 2026-10-05) -- form only, on `3.0.0_SA_CVO`'s refusal of the v0.5 half

Review `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_PRD_V05_RATIFIED_TEXT_REVIEW_20261005.md` @4d959d5ee5. Two SOURCE
lines in the ENDPOINT block are corrected: FWD-6's carries no dated history clause (ADDENDUM v0.5 records the amendment), and
FWD-12's names no seat serial. No outcome's meaning changes.

**Andrew-direct, 21:12Z at this terminal:** "I am having CRO run an analysis and brief of this. It seems like this should be able
to be folded into the MDPF_SECCLASS project." Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_2112Z_CRO_BRIEF_ON_SECTOR_FOLD_INTO_MDPF_SECCLASS.md`. FWD-12 and
ADDENDUM v0.5 are that fold as this seat wrote it from his direct words, before the brief. When the brief lands, this seat
reconciles FWD-12 and the contract notes to it here, by amendment or a next-id outcome. No second project is opened.

## ADDENDUM v0.7 (1.0.0_SA_CTO, clock read 21:27Z 2026-10-05) -- an ENDPOINT change on the midstream brief: FWD-6 amended, FWD-13 to FWD-16 added

**Brief (L1, midstream):** `docs/briefs/mdpf-secclass-one-classification-table-midstream-brief-20261005.md` @6636ceef4c, 252 lines,
on Andrew's word at the research seat's terminal
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_211xZ_ONE_CLASSIFICATION_TABLE_CONSOLIDATE_BD_SECURITIES.md`).
Evidence: `docs/briefs/one-classification-table-consolidation-analysis-20261005.md`. Its measurements are the brief's; this seat
re-measured none. NOT READ at this re-entry: the analysis file itself, the task-order register, the decompositions.

**The brief's finding: the direction is unchanged.** It asks for one outcome the endpoint lacked, one exception closed, and
surfaces the manifest did not name.

| Brief | Endpoint | What happened |
|---|---|---|
| O1 the Holdings tab reads only the shared list | FWD-13, new | RIGHT and INCOMPLETE: FWD-2 says "one answer" but no outcome owned this page. It is the thread of this phase |
| O2 clean names wherever holdings are listed | FWD-14, new | missing: FWD-11 promised a clean name only for rows the AI makes |
| O3 no second authority without Andrew's say | FWD-6, amended in place | an exception now needs his agreement by name |
| O4 the missing list, pulled on demand, reaching zero | FWD-15, new | the staying-at-zero half is FWD-7, unchanged |
| O5 sector from the shared list on the ETF view | FWD-12, unchanged | the field question is C-SECTOR (ADDENDUM v0.5): a new field, not `sector`, not `sub_asset_class` |
| O6 six classes to each screen's groups | FWD-16, new | -- |
| O7 no ticker list in the portal | FWD-4, unchanged | "anywhere in Opal's code" already includes the portal; the surfaces are named below |
| O8 nothing reads or writes the old list, then it is deleted | FWD-5, unchanged | the newly found readers and writers are named below |

**Rulings this re-entry closes (the brief's two "the CTO may need"):**
1. **FWD-11's word covers the securities labelled by ticker shape today** (the brief counts 668). FWD-11's text is "a security
   that no source Opal already holds can place"; a guess from a ticker's shape is not a source. They go to the AI classifier
   after the direct-match plan, like any other.
2. **Whether FWD-6 reaches the Schwab firm composition is Andrew's.** Until he says, that exception stands and FWD-6 does not
   grade REALIZED.

**Contract notes (bind the next round's cells):**
- **The Holdings fallback ends.** Ruling 103169's declared exception (the old list plus three guess layers behind the shared
  list) is withdrawn by FWD-6 as amended. It is REMOVED only after the shared list holds the securities it labels today; removal
  is a served move per firm (C-SERVED), every moving security named first.
- **The `CUSIP:` lookup (RULINGS batch 266, option (b), now RULED IN).** The brief measures 187 held securities that have a
  `CUSIP:<id>` row the Holdings producer never tries. The producer reads `CUSIP:<security_id>` after a symbol miss. It is a
  second key form of the same list, not a second authority. Its own half, with the 187 listed.
- **The old list stops growing first.** Three writers add rows to it daily (brief PART V). Each is stopped, as a named cell in
  its own tree, before FWD-5's check can read zero.
- **A key form for a security with no ticker and no CUSIP** (the brief counts 58 held). It is declared in
  `org/standards/MDPF_SECCLASS_CONTRACT.json` with the four-postulate record before any such row is written.
- **Names (FWD-14).** The clean-name rule of ADDENDUM v0.4 applies to every row, not only model rows. The Holdings page prints
  the list's name; the custody description stays available as its own field. The published `HoldingsSnapshot` contract changes
  with its consumer first (the page refuses a field it does not know).
- **Which security is this.** Working out which security a custody name refers to keeps a home after the old list is gone; it
  reads the shared list and writes nothing to it.
- **Boundary.** The list is this project's. The Holdings producer and `HoldingsSnapshot` are IRPT_BCKEND's Holdings workstream;
  the ETF producer is ETFS_POSITIONING's; each firm's chain is its own tree. A cell that touches one of them is cut in that
  owner's tree and ships through that owner's release.
- **Surfaces the manifest did not name (brief 0.2), added as S21 to S26:**

| id | outcome_ref | surface | claim | owner |
|---|---|---|---|---|
| S21 | FWD-13, FWD-14 | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `bd_securities_fallback.py` | held (brief); `:938-972` and `:999-1011` measured by this seat today | IRPT_BCKEND Holdings workstream |
| S22 | FWD-5 | `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py`, a reader of the old list | held (brief) | the news pipeline |
| S23 | FWD-4 | `portal/src/pages/Attribution/constants/etf-categories.ts`, `holdings-shared.tsx` | held (brief) | portal |
| S24 | FWD-4 | `portal/src/lib/tickerRegistry.ts` | held (brief) | portal |
| S25 | FWD-5 | `data/black_diamond/scripts/classification/resolve_tickers.py` | held (brief) | the Black Diamond chain |
| S26 | FWD-16 | the geography list in `yang-generate-positioning/lambda_function.py:95` | held (brief) | the yang pipeline; no home in the list is decided |

**Placement:** the next MDPF_SECCLASS round, cut from this seat's round analysis. The current round stays frozen.

**Sign-off:** an ENDPOINT change, so the ratified-text half re-opens. The brief half: the brief's author is the research seat.
The four new DONE WHEN lines are put to Andrew for confirmation.

## ADDENDUM v0.8 (1.0.0_SA_CTO, clock read 21:31Z 2026-10-05) -- contract notes only: two of ADDENDUM v0.7's rulings answered by Andrew

**Word:** Andrew-direct at the research seat's terminal, "Recs approved", record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_213xZ_THREE_RECS_APPROVED_AND_CIK_QUESTION.md`
@a998e96856 (relayed by msg 105404). The ENDPOINT section is not edited.

- **The AI classifier covers the 668 securities labelled today by a guess** (his card 1, with the index of AI-made rows as the
  condition already set). This confirms ADDENDUM v0.7 ruling 1; it is now his word, not this seat's reading.
- **The Schwab firm composition stays an exception, agreed by name** (his card 3: "keep it as the one named exception for now;
  revisit once the canonical table covers every held security"). This answers ADDENDUM v0.7 ruling 2. Under FWD-6 as amended it
  is the one exception that exists; C-DEPARTURE names it and nothing else once FWD-12's move lands.
- **Not a ruling:** in the same record he asks whether a CIK field belongs on the table beside sector. It is a question, answered
  to him by the research seat; nothing is added to the table's shape on it.

## ADDENDUM v0.9 (1.0.0_SA_CTO, clock read 21:33Z 2026-10-05) -- contract notes only: no CIK field for now; the old list migrates through reclassification

**Words:** two Andrew-direct records at the research seat's terminal, @e21062c19b (relayed by msg 105407):
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_213xZ_NO_CIK_FIELD_FOR_NOW.md` and
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_214xZ_LEGACY_MIGRATION_RECLASSIFIED_ONE_TABLE_FOR_CONSISTENCY.md`. The ENDPOINT section is
not edited.

- **No CIK field.** "No we can hold off of CIK for now ... ticker is probably stable enough for that if need be." The table's
  shape gains sector (C-SECTOR) and nothing else. "For now" is his qualifier: a hold, not an exclusion.
- **The old list's rows reach the shared list through reclassification, never as they are.** His words: "we would have to run it
  on a 6 field basis with the new nomenclature/fields as part of the adaptation/reclassifier process." This agrees with what
  already binds here: the shared list is never overwritten from the old one (C-WRITER; his rule of 2026-09-29), an old row is
  read as an INPUT only, and a value lands only if it is a member of the shared list's own vocabulary (ADDENDUM v0.4).
- **A consumer named by product: Advisor Intelligence.** He says the old list exists because it serves that application. Which of
  its screens read the old list was not traced by the brief. That trace is a cell of the next round, before any reader there
  is switched (C-SERVED).
- **Two points he has not settled, put to him by the research seat, and NOT decided here:**
  1. "a 6 field basis": the shared list's six asset classes, or six fields per row.
  2. How much of the old list migrates: the securities held today (the brief counts 2,053 of 10,873 rows labelling something
     held), or all of it.
  FWD-15 as written counts HELD securities with no entry. If his answer to point 2 is "all of it", FWD-15's bar changes and this
  seat amends it then; no cell that fills rows is cut on the wider reading before he says.

## ADDENDUM v0.10 (1.0.0_SA_CTO, clock read 21:49Z 2026-10-05) -- an ENDPOINT change on Andrew's five answers: FWD-12 amended, FWD-17 added

**Word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_2149Z_FIVE_CALLS_ALL_OF_BD_SECURITIES_SIX_ASSET_CLASSES_INDUSTRY_GROUP_ONTO_TABLE.md`.

**What changed and why (endpoint re-entry):**
- **FWD-17 is new** (his call 1, "all of it"). FWD-15 was RIGHT and INCOMPLETE: it counts HELD securities with no entry. It stands
  unchanged, and the whole old list gets its own outcome at the next unused number. This replaces ADDENDUM v0.9's statement that
  FWD-15's bar would be amended.
- **FWD-12 is amended in place** (his call 5): the industry group moves onto the list with sector. ADDENDUM v0.5's "not decided"
  line on `industry_group` is closed.
- **FWD-13 to FWD-16:** their DONE WHEN lines are confirmed by him (call 3).
- No outcome is retired.

**Contract notes (bind the next round's cells):**
- **Six means the six asset classes** (his call 2). The reclassifier places every old row under the shared list's six
  `asset_class` values; the old list's four classes and its two quiet folds are not carried. FWD-16's mapping is where a screen
  that shows fewer groups states how the six became its own.
- **The whole old list, in this order:** securities held today first (FWD-13 and FWD-15 depend on them), then the rest. The
  research seat's brief counts 10,873 old rows, 2,378 of them already in both lists. Each remaining row goes through the
  direct-match plan, then the AI classifier (FWD-11), with the value bound and the index of AI-made rows as already set. A row
  nothing can place is listed UNRESOLVED by name; FWD-17 does not grade REALIZED while that list is not empty.
- **Key forms.** The old list keys some rows `NAME::<slug>`. The key form for a security with no ticker and no CUSIP (ADDENDUM
  v0.7) is declared before any such row is written; it now gates part of FWD-17, not only the 58 held.
- **C-SECTOR gains a second attribute for the industry group.** Same rule: its own new attribute, its closed values declared as
  data in the contract file with the four-postulate record and a token census. Its source is the Bloomberg industry-group name
  the ETF producer already reads (`etf_positioning_gold.py`, `GICS_INDUSTRY_GROUP_FIELD`). That producer's own header says the
  field's values were not yet measured in the served artifact; the values are measured before they are declared.
- **C-NOCHAR stands:** sector and industry group are labels. No measurement enters the list. No CIK field (ADDENDUM v0.9).

**Placement:** the next MDPF_SECCLASS round. **Sign-off:** an ENDPOINT change, so the ratified-text half re-opens.

## ADDENDUM v0.11 (1.0.0_SA_CTO, clock read 00:03Z 2026-10-06) -- contract note only: Andrew's word for the AI classifier at the full old-list volume

**Word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md`: "RUn on the full old table". The ENDPOINT section is not edited.

- **C-VENDOR.** His word covers the outside-model use for FWD-17 at its full volume: up to 8,495 old-list rows (the research
  seat's count), the model the existing writer calls, name and ticker only, after the direct-match plan. This closes
  `3.0.0_SA_CVO`'s note 1 on v0.10. No cap, and no second release by him, sits between the held securities and the rest.
- The order of ADDENDUM v0.10 stands as sequencing, not as a gate: held securities first.

## v0.12 ADDENDUM (1.0.0_SA_CTO, 2026-10-06) -- FWD-9's depth is one year

Andrew-direct 2026-10-06 ~18:1xZ at this seat, answering the securities-database call on rival funds' depth: "B, 1 year for
rivalfunds" (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_181xZ_COO_C_BOTH_SECHIST_REGISTER_HOLD_RIVALS_1Y.md`).
FWD-9 is amended in place (id unchanged): the depth is one year. TO-SC-e18 (complete) filled three years; that history is KEPT, not
deleted, because a delete is Andrew's act and he ordered none. From this version a new Rival Funds stock is filled one year back.
The ENDPOINT changed, so the ratified-text half re-opens for `3.0.0_SA_CVO`. The depth policy per ingestion point is owned from here
by MDPF_SECHIST; this outcome keeps the row and the fill.

## ADDENDUM v0.13 (1.0.0_SA_CTO~DELL1, 2026-10-07) -- the round-8 analysis: FWD-12 amended in place; contract notes

**Analysis:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` (same commit), on
`3.0.0_SA_CVO`'s slug (msg 179, ADJUDICATION_v7 @cb765997e2). Author's authority: laptop `1.0.0_SA_CTO` ruling 106047 (1) and the
NFRA_CTLPLN v0.12 addendum (a Dell CTO writes L4 and L10 for its box's projects).

- **FWD-12 amended in place (id unchanged), row S44.** Its title read "each security", while its DONE WHEN and ACCEPT grade the ETF
  view's holdings. The title now says what is graded: each security an Opal ETF holds. **No longer promised by this outcome:** a
  sector or industry group on rows no Opal ETF holds (rival-fund stocks, client securities, unheld old rows). The source stays the
  Bloomberg characteristics leg the ETF producer already reads. A held security the leg does not return is a C-PULL cell at site Z
  under the daily vehicle's existing vendor use; nothing is inferred from a name.
- **FWD-14 source (row S45), no wording change.** A held row with no name takes the custody feed's security name through `clean_name`,
  once row W28-S5 is repaired. An AI-made row keeps FWD-11's clean name.
- **FWD-15 path (row W26-S8).** FWD-11's producer runs over FWD-15's per-firm missing list, held first, after the direct-match plan,
  under FWD-11's recorded C-VENDOR word (same model, name and ticker only).
- **FWD-17 (row W25-S2).** The population is the whole old list, held or not. "Held" means a non-zero market value in the latest
  served holdings partition of any of the three firms on the census as-of. The "58" is retired.
- **C-BOUND (row W26-S6).** The contract's closed `sub_asset_class` list is the bound for a DIRECT or AI verdict, cash included, not
  only the values the table holds today.
- **C-SECTOR values (rows W24-S2, W24-S1).** `gics_sector` carries the 11 GICS sectors (Real Estate added). The industry-group list
  carries full GICS names, and a decode table in the same contract maps the vendor's 30-character spellings to them. An unmapped
  spelling leaves the field empty, and the row is listed.
- **Manifest paths (row S47).** S13's files are `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/etf_classification.py`,
  `.../yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py`,
  `.../yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` and
  `infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py`. S26 is
  `.../yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:95`.

**Sign-off:** an ENDPOINT wording change on FWD-12, so the ratified-text half re-opens for `3.0.0_SA_CVO` (dell1).

## ADDENDUM v0.14 (1.0.0_SA_CTO~DELL1, 2026-10-07) -- contract note only: Cash is a sub-class of cash alone

**Analysis:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_9_20261007.md` (same commit), on
`3.0.0_SA_CVO`'s slug msg 247. The ENDPOINT section is not edited.

- **C-BOUND, row W36-S2.** Under the six classes, the sub-class `Cash` belongs to `cash` only; `fixed_income` carries no `Cash`
  sub-class. A screen that shows cash inside fixed income states that fold as its FWD-16 mapping; the list itself never folds.
  The canonical `CASH` row (`fixed_income` / `UltraShortDuration`, `classified_by: legacy`, read 2026-10-07 12:5xZ) is corrected
  to `cash` through the seed source by its own pair.

## ADDENDUM v0.15 (1.0.0_SA_CTO~DELL1, 2026-10-07) -- contract note only: the "Cash" token places a security in cash

**Word:** Andrew-direct ~14:1xZ at the `2.0.0_SA_COO~M2` terminal (dell2), on the "Classification not found" tickers of the 10-05
Cottonwood build (BDCASHIN, FCASH, CQP and five more), VERBATIM: "most of those items literally have "Cash" as a token within, which
would be the "Cash" asset class. The others could likely be websearched." Record
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/ANDREW_DIRECT_20261007_141xZ_NEXT_CALLS_GO_1_2_UNCLASSIFIED_TICKERS_CASH_TOKEN.md` @fa8d7d1cf7.
The ENDPOINT section is not edited.

- **C-CASH-TOKEN (new source rule for the TABLE, not for a screen).** A security whose ticker or name carries `CASH` as a whole token
  is placed in `asset_class = cash` (sub-class `Cash`, ADDENDUM v0.14) when the table is filled, by the direct plan, with
  `classified_by` naming the rule. FWD-13 is unchanged and still binds the screens: a page never labels a security from a word in its
  name. The rule lands in the shared list, and every screen reads the list. A whole token means a word boundary, not a substring.
  `CASH` in `CASHMERE` does not count, and the rule's test pins both.
- **The others: research, not downloads.** A security the token rule does not place is researched by web search (research only, no
  download, per Andrew's download tiers), and the finding lands through the existing seed or AI path with its source recorded.
  Nothing is guessed.

## ADDENDUM v0.16 (1.0.0_SA_CTO~DELL1, 2026-10-07) -- contract note only: C-CASH-TOKEN's name leg is an allowlist

Asked by `2.0.0_SA_COO~M1` (msg 345, row W47-S1): v0.15's whole-word name rule places "Cash Flow Dividend Fund", an equity fund, in
cash. Andrew's word was about unplaced tickers that carry "Cash" as a token, and a wrong class is worse than a blank.

- **Ticker leg, unchanged:** a ticker piece matching `^(BD|F)?CASH(IN|OUT)?$` (BDCASHIN, FCASH, CUSTODIAL_CASH, FID:CASH) is cash/Cash.
- **Name leg, narrowed:** a security is placed in cash only when its WHOLE normalized name (case-folded, punctuation and spacing
  collapsed) is one of: `cash`, `cash & cash equivalents`, `cash and cash equivalents`, `cash equivalents`, `cash balance`,
  `cash sweep`, `cash in`, `cash out`. The allowlist lives in the contract file as data. A word inside a longer name does not count.
- **Precedence:** neither leg overrides an existing seed or canonical row. The rule fills only rows nothing else placed.
- The test pins "Cash Flow Dividend Fund", "Cash Cow" and CASHMERE OUT.
