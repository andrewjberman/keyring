# MDPF_SECCLASS -- one canonical per-security classification table for every holdings surface

```json
{
 "project": "MDPF_SECCLASS",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/canonical-security-table-brief-20260929.md@87ad6973f3",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
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
         ACCEPT     each declared exception names its owner and its reason; a reader of Positioning's
                    ETF view or the Schwab firm data can tell a class that came from the shared list
                    from one that came from the declared exception; the old quiet rules such as "treat
                    hedges as alternatives" or "VXX is equity" are gone, not declared
         SOURCE     brief O6 (l.68-73); section 2 below (the CTO's decision)

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
