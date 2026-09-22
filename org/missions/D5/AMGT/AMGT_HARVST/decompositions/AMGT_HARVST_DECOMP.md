# AMGT_HARVST -- L5 decomposition (COO) -- v1.0 (round 1)

**Seat:** `2.0.0_SA_COO~Y`, seated by Andrew 2026-09-22 to drive this project to completion (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_150xZ_AMGT_HARVST_ANDREW_SPAWNS_COO_Y_ISSUE_PRD_ON_SIGNOFF.md`).
**Directive:** D5. **Fabric:** site-z, branch `SITEZ`.
**Consumes:** PRD v0.2 s.4 SURFACE MANIFEST H1-H10 at `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`
@9102ccfe81. At this cut, `python .tools/prd-signoff.py status AMGT_HARVST` reads `ADMITTED`, with both halves
SIGNED and current: the ratified text by `3.0.0_SA_CVO~Z` @0a7533928d, and the brief half by `4.0.0_SA_CRO~Z`
@98c5a5e548.
**Handoff read first:** `org/missions/D5/AMGT/AMGT_HARVST/ledger/HANDOFF_L4_TO_L5_COO_Y_20260922.md` @9a012735fc,
plus the two v0.2 corrections in `1.0.0_SA_CTO~Z`'s msg 24295 (gold absolute-only; the first job is the 2026 backfill).

**The rectangle is RECEIVED, not derived here.** L4 wrote the manifest. L5 mirrors it and re-grounds what it can at
its own vintage. It then adds the dependency edges, the placement axis and the battery.
**This file does not re-open the manifest's MECE.** It makes ONE ordering decision of its own, which section 4 states
and defends: the H10 run executes after H1-H3, not after H1-H6.

---

## 1. The rectangle -- ten cells over ten manifest rows, `HVST-h-<n>` mirroring `H<n>`

**THE INVARIANT THIS FILE COMMITS TO:** every cell mirrors exactly one manifest row, and every row has exactly one
cell. Measured at this cut: 10 cells over 10 rows, a bijection.

**CELL-ID CONFORMANCE, MEASURED** (`org/standards/DECOMP_CELL_ID_CONVENTION.md`, SHAPE 1): the ids were loaded
into the enforcer object itself (`.tools/proof-of-spec-check.py` `CELL_ID_RE`) and matched there.
- 10 of 10 ids match.
- The malformed controls:
  - a lowercase prefix: refused;
  - underscores: refused;
  - a two-letter axis: admitted, because the regex's `[a-z]{1,4}` admits it. No cell here uses one.

No cell id from another project's decomposition is written in this file. The L6 coverage limb indexes every
cell-shaped token here as a cell of THIS decomposition, so siblings are cited by path only, and the `AMGT_RESAPP`
cell that built the bronze writer is named "the round-21 bronze writer cell".

**CELL STATUS VOCABULARY.** This is ADOPTED, not authored: the closed set `AMGT_RESAPP`'s decomposition records (by
path, `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md` s.2a):
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. No cell carries `NOT-EVALUATED` at this cut; that is
measured (10 of 10 evaluated), not a missing value.

| cell | row | outcome | act (the engine, and what binds it) | state | chain position | touches |
|---|---|---|---|---|---|---|
| `HVST-h-1` | H1 | FWD-1 | BRONZE CAPTURE, CODE ONLY. Every publisher path keeps the bytes it received: `raw_bytes` on FT (HTML), WSJ (HTML) and Barron's (JSON), beside the existing SA and Bloomberg JSON. Every listing or search response that found an article is also kept. The bronze writer puts one object per fetch through `harvest_grammar.put_article_bronze` (the ONE writer) with `received-form` in S3 metadata. The listing lands under `{source}/harvest/bronze/news_listing/date=<d>/`. Fixture tests only: no vendor call and no S3 write. | OPEN | A1 | code |
| `HVST-h-2` | H2 | FWD-2 | SILVER FROM BRONZE, CODE ONLY. `harvest_grammar.article_silver_row` is rebuilt to read the BRONZE object (JSON, or the HTML with its embedded JSON extracted here), never the 18-field normalised record. It keeps every vendor field, typed, and adds the three clocks (`published_utc`, `published_offset_min`, `published_date_utc`, `published_precision`; `fetched_at`; `first_discovered_at`). Every row carries `bronze_key`, `retrieval_mode`, `run_stamp` and `record_hash`. A `listing_hit` table sits beside it. The `date=` partition is the FETCH date. Replay test: bronze fixture, then silver rows, twice, gives identical rows. | OPEN | A2 | code |
| `HVST-h-9` | H9 | FWD-8 | DESKTOP OUTBOX UPLOAD. The articles and links held only in this desktop's runtime (`.runtime/opal-data-harvest`) reach the new grammar through the ONE writer, deduped by `article_hash`. Where the desktop kept no received bytes (FT, WSJ and Barron's today), the stored object's `received-form` is `normalised_record`, never `as_received`. The upload is reachable from the CLI. Writes S3 `opal-data-harvest` only. **Not vendor egress** (`C-HV-EGRESS`). | OPEN | A3 | this box -> S3 |
| `HVST-h-3` | H3 | FWD-3, FWD-9 | RETRIEVAL RUNGS, PROVENANCE AND WATERMARK, CODE ONLY. Every discovered article records `retrieval_rung` (`symbol_listing`, `name_search` or `ticker_search`), `search_query`, `search_rank` and `search_page`. Discovery pages back to the later of the FLOOR (2026-01-01) and the WATERMARK (the newest held `published_utc` for that security and publisher). The dedupe check runs before any vendor call, for articles by `article_hash` and for listings by the listing fetch key. A PLAN mode prints each publisher's listing page count with ZERO network. The mention FLOOR (`publishers.py` word-bounded gate) is unchanged. | OPEN | A4 | code |
| `HVST-h-10` | H10 | FWD-1, FWD-2, FWD-3, FWD-9 | THE LENOVO RUN, VENDOR EGRESS UNDER THE TRIAL WORD. ONE harvester run for `992_HK_Equity`, all five publishers, `retrieval_mode=backfill`, from the floor 2026-01-01. The plan's page counts are printed and recorded BEFORE any vendor call. Bloomberg's per-symbol `news()` is tried ONCE, and is adopted or recorded UNRESOLVED with its reason. After the run: every bronze object is re-read and matched byte for byte; silver is rebuilt from bronze; and a SECOND run the same UTC day makes ZERO vendor calls, proven with a transport that refuses any request. This is `AMGT_RESAPP`'s stage 9, executed here once (`C-HV-BOUNDARY`). | OPEN | A5 | vendors -> this box -> S3 |
| `HVST-h-4` | H4 | FWD-4 | GOLD `article_security_mention`. A new gold producer over silver computes one row per (article, security) with every field `C-HV-MENTION-GRADE` names. The tier partition runs A, then B, then C, then D, first match wins. The share is computed at assignment and never stored. The weights and thresholds are working defaults, stated in the deliverable. A re-derivation from stored silver matches. Written to `amgt/harvest/gold/article_security_mention/` in `opal-data-harvest`, under builder-output addresses. | OPEN | A6 | code + S3 |
| `HVST-h-5` | H5 | FWD-5, FWD-7, FWD-9 | GOLD `chatter_daily`, ABSOLUTE ONLY. One row per (security, UTC day), DENSE from 2026-01-01 with a zero row for an empty day. Every field `C-HV-DAILY-DENSE` names, including `data_status`. `published_utc` is the only clock that places an article on a day. No ratio, share, z-score or normalised figure is stored (`C-HV-ABSOLUTE-ONLY`). A rebuild from the same silver is identical (`C-HV-GOLD-REBUILDABLE`). Run on Lenovo's silver from `HVST-h-10`. | OPEN | A7 | code + S3 |
| `HVST-h-6` | H6 | FWD-6 | GOLD `chatter_event`. Clustered runs of UTC days per security, using the working rule: tier A+B articles >= 2 from >= 2 publishers, merged across gaps of <= 1 day. Each event carries its lead headline and its articles. Run on Lenovo. | OPEN | A8 | code + S3 |
| `HVST-h-7` | H7 | FWD-7 | THE CHATTER PROJECTION, CODE ONLY. `lib/research/metrics/chatter_axis.py` reads `chatter_daily` (and `article_security_mention` for coverage) through its ONE read adapter. The ranks come from graded `mention_score`, and relative figures are computed in the producer at serve time. Tests prove that a company named once in passing in many articles no longer outranks one that was the subject of a few. **No deploy, no Terraform, no DynamoDB write in this cell**: the served move is a never-widen act and waits on section 9. | OPEN | A9 | code |
| `HVST-h-8` | H8 | FWD-5, FWD-6 | THE TIMELINE DESIGN SPEC. The day-by-day mention line on the security page, day dissection (articles strongest first) and event spans. It names the API shape `scoped_amgt.py` would serve, with every relative figure computed at serve time. **No `.tsx` and no API edit** (`C-HV-DESIGN-SPEC-FIRST`). The build is a later cell, cut on the spec's approval. | OPEN (spec) | B1 | docs |

---

### 1a. Re-groundings performed at L5, at SITEZ @8337781c46

These re-ground what a decomposition can re-ground without spending a vendor call or doing a cell's work. Every
figure is from this seat's own read.

**Bronze bytes (`HVST-h-1`): the handoff's claim HOLDS.**
```
comp-read lib/opal_data_harvest/publishers.py --enumerate 'raw_bytes'
  5 hits / 374 lines | CODE=5 | call sites at :221 (inside seeking_alpha :197-221) and :249 (inside bloomberg :223-253)
  financial_times :255-281 and DowJones.article :343-374 pass NO raw_bytes
```
The listing or search responses are parsed and discarded on every path: SA `news()`, Bloomberg `search()` (pages
1-3), the FT search page, and the Dow Jones `discover()` search page. **No listing response is kept anywhere today.**

**Discovery depth (`HVST-h-3`): the machinery cannot backfill today.**
- `lib/opal_data_harvest/config.json` sets `articles_per_security: 5` and `candidate_limit: 20`. `Worker.run_job`
  stops at `target` accepted articles.
- FT and Dow Jones read ONE search page. Bloomberg reads at most 3.
- Nothing pages by date.

So the floor and watermark paging in `C-HV-RETRIEVAL-PROVENANCE` is NEW behaviour, not a parameter change.

**Silver shape (`HVST-h-2`):** `harvest_grammar.article_silver_row` (`:100-107`) copies the normalised record.
`C-HV-SILVER-FROM-BRONZE` supersedes it, as the PRD states.

**The uploader (`HVST-h-9`):**
- `python -m lib.opal_data_harvest upload` reaches the legacy `Uploader` only (`__main__.py` `upload` branch).
- `HarvestUploader` (`uploads.py:103-162`) is reachable from no command.
- `config.json` carries no `harvest_grammar` key, so harvest mode is OFF and `harvest_raw_outbox` receives nothing.

**Lenovo (`HVST-h-10`):**
- `config.json` `pilot_securities` holds five US names and not Lenovo.
- The run selects Lenovo from the universe (`universe_source`) or fails loudly. The cell measures which.
- The trial word caps Seeking Alpha at the ADR line.

**The chatter-axis role (`HVST-h-7`, and the later served act):** `comp-iam role amgt-resapp-chatter-axis-lambda-role`
(DESIRED plane, Terraform) shows 4 statements:
- `s3:GetObject` on `harvest/${p}*`;
- `s3:ListBucket` conditioned on `s3:prefix` over `local.chatter_axis_pool_prefixes`;
- DynamoDB `PutItem` and `BatchWriteItem`;
- logs.

**Reading gold needs both S3 limbs widened to the gold prefixes.** That is a Terraform act, which is why `HVST-h-7`
is code only.

---

## 2. Rule 24 four-postulate record, for what this file ADDS

What this file adds is: the cell set, the chain ordering, and two values it rules.

**(i) MECE over a declared domain, by subtraction.**
- The domain is the manifest's printed rows H1-H10: 10 rows.
- Cells = 10 rows minus 0 excluded = 10.
- No row is split and none is merged.

The one value set this file authors is the `received-form` enum on bronze metadata: `as_received | normalised_record`.
- Its domain is the population of bronze writes. Every write is either the bytes a publisher sent, or a record whose
  bytes were not kept (only the desktop's legacy bodies).
- A third member would be a write of neither. None exists, because the ONE writer accepts only those two inputs.
- **Token census:** `received-form` appears in the PRD (the contract names the metadata key); `normalised_record` is new.

**(ii) Same grain.** Every cell is one ENGINE (one row of the manifest), so every cell sits at one grain.

**(iii) Intent coherence.** The chain axis orders by DATA dependency (what a cell reads that another writes), and
nothing else. `HVST-h-8` sits on its own chain because it reads only contracts.

**(iv) State coherence.** What one remedy does NOT move:
- `HVST-h-10` moves bronze and silver for Lenovo. It moves no gold and nothing served.
- `HVST-h-7` moves code and no served row.
- `HVST-h-9` moves the three US pilots' legacy articles into the new grammar. It does not re-fetch them, so their
  `received-form` stays `normalised_record` forever, and FWD-1's byte-for-byte bar is graded on articles fetched
  AFTER `HVST-h-1`, never on these.

---

## 2b. BATTERY DISPOSITION PER LENS

### `comp-schedule --drift` -- RUN, WITHIN BUDGET (22.2 s)
```
REACHED-DENOMINATORS: C1=23; C2=7; C3=12; C4=21; C5=334
GATES ARMED: 2 [--drift]  G-3 (owner CTO, evidence data/inf/scripts/silver/convert_transactions_to_silver.py:94)  G-7 (owner POD4, gold_dispatch.sh)
```
Neither armed gate names a harvest, chatter or AMGT surface.

The open-deploy census:
- `org/critical_paths/.open_deploys/` in the shared tree holds 7 entries plus `.unindexed_red_state.json`, and none
  names harvest or chatter.
- **BLINDNESS, STATED:** 28 other live worktrees were NOT read (the CLAUDE.md NEVER-2 worktree clause). This cell set
  opens no deploy, so no act here depends on that read.
- **`HVST-h-9` WRITES S3.** Its worker reads the union across every live worktree before the first put.

### `comp-iam` -- RUN (`roles`, and `role amgt-resapp-chatter-axis-lambda-role`)
- 3 roles match harvest or chatter: `amgt-resapp-chatter-axis-lambda-role`, `amgt-resapp-chatter-axis-scheduler-role`
  and `harvest_enqueue`.
- The chatter role grants are in s.1a.
- **BLINDNESS:** this is the DESIRED plane (Terraform) only. `comp-iam roles` prints no vintage.
- **This box's own credential, the one `HVST-h-9`, `HVST-h-4`, `HVST-h-5` and `HVST-h-6` write S3 with, is NOT read by
  this lens.** Each of those workers measures it with a real PUT to its own new prefix and records the outcome. A
  refusal there is a surprise row, never a workaround.

### `comp-adversary` -- RUN on this file; declaration at section 7.

### `comp-blast` -- DECLARED-NOT-APPLICABLE
No cell in this round moves a served object. The served acts (the DynamoDB projection and the page) are held out in
section 9.

---

## 2c. BOUNDS THE BATTERY ADDED TO CELLS -- carried into the L6 cut
- `HVST-h-7`: no `terraform`, no `safe-apply`, no Lambda deploy, no DynamoDB write. It changes code and tests only.
- `HVST-h-9`, `HVST-h-4`, `HVST-h-5`, `HVST-h-6`: S3 writes ONLY under `opal-data-harvest`, ONLY at builder-output
  addresses, never overwriting. A refused PUT is a row, never a hand-typed key.
- `HVST-h-10`: vendor calls ONLY inside the trial word's cap (one harvester run for Lenovo), and ONLY after the plan's
  page counts are printed. The second same-day run makes zero vendor calls by construction.

---

## 3. Placement axis

Every cell executes on **site Z** (this desktop, branch `SITEZ`):
- the harvester needs this box's signed-in publisher sessions (DPAPI, current user);
- the gold producer and the chatter code live in this fabric's tree.

No cell executes on the laptop fabric.

---

## 4. Dependency edges, keyed to OBSERVED completion (a drained, VALID proof-of-spec instance), never a status word

```
  chain A:  HVST-h-1 -> HVST-h-2 -> HVST-h-9 -> HVST-h-3 -> HVST-h-10 -> HVST-h-4 -> HVST-h-5 -> HVST-h-6 -> HVST-h-7
  chain B:  HVST-h-8
```
- **h-2 after h-1:** silver reads the bronze form h-1 defines.
- **h-9 after h-2:** the upload writes bronze AND silver through both writers.
  - It is placed before h-3 because h-1, h-2, h-3 and h-9 all edit `lib/opal_data_harvest`.
  - Serialising them removes a guaranteed merge conflict between two worktrees on the same files.
  - The pilots' data it lands is the gold cells' second sample (FWD-8, and the handoff s.5).
- **h-3 after h-9:** same package; the watermark reads what is already held.
- **h-10 after h-3:** the run needs capture, silver and paging. **THE ONE ORDERING DECISION:**
  - The manifest lists H10 as depending on H1-H6. This file runs the EGRESS after H1-H3 and closes H10's gold half
    (FWD-9's dense daily rows) inside `HVST-h-5`.
  - Reason 1: gold is rebuildable from silver (`C-HV-GOLD-REBUILDABLE`), so no second vendor pass is ever needed.
  - Reason 2: `AMGT_RESAPP`'s stage 9 waits on exactly H1+H2 (`C-HV-BOUNDARY`).
  - Reason 3: the gold cells are then built on Lenovo's real silver, not only on fixtures.
  - What it does NOT change: the one trial run is spent exactly once, and FWD-9 is graded REALIZED only when `HVST-h-5`
    shows the dense series.
- **h-4 -> h-5 -> h-6:** one producer module, each table read by the next.
- **h-7 after h-5:** the projection reads `chatter_daily`. It is placed after h-6 only to keep one worker on the
  chain; it has no h-6 dependency.
- **h-8:** reads contracts only. There is no edge.

**M = 2** dependency-independent chains.

---

## 5. The round -- one issuance, fan-out as data

- **Round 1 covers all 10 cells in ONE issuance.** Chain B's cell spawns at once. Chain A spawns one cell at a time,
  each as its predecessor drains VALID. Each cell gets its own slot `~<n>`, following the sibling project's practice of
  a fresh worker per chained cell, so no worker carries nine cells of context.
- Fan-out line for the issuance commit: `fanout: cap 8, 10 orders, 2 chains; wave 1 = h-1 and h-8 at once; chain A
  continues h-2, h-9, h-3, h-10, h-4, h-5, h-6, h-7, each on its predecessor's valid drain.`
- The surprise channel opens at the issuance:
  `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md`.
- **Coordination owed by this seat, not by a worker:** when `HVST-h-10` drains VALID, this seat tells `2.0.0_SA_COO~Z`
  (`AMGT_RESAPP`), by file and message, that stage 9 has landed. The pointer is the instance path and the silver
  prefixes.

---

## 6. `<preflight>` -- what this decomposition actually ran
```
prd-signoff.py status AMGT_HARVST      ADMITTED, v0.2 @9102ccfe81, 2 of 2 halves SIGNED current
sequence-check.py --project AMGT_HARVST  not in SEQUENCE.yaml (not sequenced); 2 live COO lanes on this box
to-check.py --all --assignee 2.0.0_SA_COO~Y  0 active of 3116 scanned
comp-schedule --drift                  2 armed, 0 on these surfaces (C1=23 C2=7 C3=12 C4=21 C5=334)
comp-iam roles / role                  3 matching roles; chatter role 4 statements (DESIRED plane)
comp-read publishers.py --enumerate raw_bytes   5 hits / 374 lines
comp-read harvest_grammar.py --enumerate        4 hits / 146 lines
proof-of-spec-check.py CELL_ID_RE      10 of 10 ids match; 2 of 3 malformed controls refused
```

---

## 7. comp-adversary declaration

`comp-adversary compose` on this file (UNCOMMITTED), read-vintage HEAD @8337781c46 at 2026-09-22T15:12:28Z, rc 0:
- Cited commits: 6 attempted, 6 VERIFIED, 0 UNVERIFIABLE.
- Cited paths: 7 attempted, 5 stable, 2 flagged:
  - The G-3 evidence path was an elision of this file's own (`data/inf/.../`). It is corrected above to the path
    `comp-schedule` printed.
  - `surprise-channel/investigations/INVESTIGATION_v1.md` is ABSENT BY DESIGN. It opens at the issuance (s.5).
- The neighborhood is filesystem adjacency: 752 uncited siblings, capped at 25 shown. T11 is not resolved, because a
  decomposition carries no `<decomp_ref>`.
- **The blindness the tool declares, and which this file accepts:** the siblings are `org/standards/` and the
  project tree, not the cells' dependency chain. The chain's real neighbours are the harvester package, the
  `lib/research/harvest/store.py` writer, and the chatter-axis module and its Terraform. These were read directly in
  s.1a.
- Declared-excluded by the tool at v1: toolgraph independence; comp-axes; comp-blast and comp-trace expansion;
  comp-pulse and comp-cochange.

---

## 8. What this decomposition REFUSES to assume
- **That the publisher sessions are live.** `HVST-h-10` measures each publisher's auth before any listing call. A
  logged-out publisher is UNRESOLVED with its reason for this run, and the one trial run is NOT re-spent on it without
  Andrew's word.
- **That Lenovo resolves to a company name the mention gate matches.** "Lenovo" in a HK listing, and the ADR line on
  SA, are measured in `HVST-h-10`, never assumed from the pilots.
- **That this box can write the new gold prefixes.** Each writing cell measures it with a real PUT.
- **That a PLAN mode's page count equals what a run will fetch.** The plan prints the planned MAXIMUM per publisher.
  `HVST-h-10` records planned against actual.
- **Any threshold.** The tier weights, the 0.3 share, the roundup at 5 and the event rule are the PRD's working
  defaults, stated in each deliverable, never tuned in a cell.

---

## 9. Holds, and whose they are

| hold | on | owner | what lifts it |
|---|---|---|---|
| FWD-9 for every security after Lenovo | the backfill list and a per-use word per run | Andrew | his list (promised @78106b9cea) and the word; then one `HVST-h-10`-shaped cell per security, cut at L10. The CVO's carry item asks the CTO to qualify this on the outcome (msg 24295) |
| the served chatter move (FWD-7 EXERCISED on the page) | a never-widen pair (CTO + COO halves), the chatter role's two S3 limbs widened to the gold prefixes, and `AMGT_RESAPP`'s `C-FORMAT-SEQUENCE` single window retiring `publications/v1/` and `publication-links/v1/` | `1.0.0_SA_CTO~Z` + this seat, with `2.0.0_SA_COO~Z` for the window | `HVST-h-5` and `HVST-h-7` VALID; then a round-2 cell or a direct act off the signed pair |
| the timeline `.tsx` and the `scoped_amgt.py` route (FWD-5, FWD-6 EXERCISED) | approval of `HVST-h-8`'s spec (`C-HV-DESIGN-SPEC-FIRST`) | Andrew | his approval of the spec; then a build cell at L10 |
| non-English press, social, SERP, any cadence, any deletion | out of scope (PRD s.2) | Andrew | a PRD change, never a cell |

-- `2.0.0_SA_COO~Y`
