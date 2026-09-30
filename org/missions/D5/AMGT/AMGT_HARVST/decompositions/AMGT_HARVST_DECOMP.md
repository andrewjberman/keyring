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

---

## 10. ROUND 2 (v1.1, the RECUT) -- from the L10 round-1 analysis @f869aa705c (`1.0.0_SA_CTO~Z`)

**Round 1 is CLOSED: 10 of 10 orders terminal, every proof-of-spec instance VALID, 56/1/2 of 59 criteria.**
**AND `FWD-1` IS NOT REALIZED.** Its bar is every article AND the listing page that found it. The issuer's own census of
`{source}/harvest/bronze/news_listing/`: **wsj 2, seeking-alpha 0, bloomberg 0, ft 0, barrons 0** -- one of five
publishers has a listing page at all. The CVO's framing, which the analysis kept and this recut adopts: *"the cell did
what it was told; the outcome needs publishers that answer."*

**WHAT THIS RECUT IS NOT.** A fourth vendor act is **NOT granted** by that analysis and needs its own word. So **no cell
here makes a vendor call**, and the question "why did four of five publishers yield nothing" is split deliberately:
- its CODE half is `HVST-r-5`, settled offline with stubs, so that what remains is genuinely the sessions;
- its SESSION half is a HOLD (section 11), owned by Andrew through `1.0.0_SA_CTO~Z`, not a cell.

### 10a. The five round-2 cells -- ALL INDEPENDENT (fanout 5 of 5, cap 8, no deferral)

| cell | row | outcome | act | state | round | touches |
|---|---|---|---|---|---|---|
| `HVST-r-1` | H8 | FWD-5, FWD-6 | **THE SPEC AMENDMENT, AND IT IS FIRST.** `SPEC_SECTION_timeline.md` fails one clause of its own judgment criterion: EVERY STATE DRAWN. Its section 6 enumerates Loading, a quiet security, the floor clamp, PARTIAL and DENIED, and a never-collected security -- but PARTIAL and DENIED are DATA states read from `chatter_daily`, and there is **NO state for the timeline call itself FAILING**, while section 5 names **no error envelope**. That is `Z-S227`/`C-S400` one project over, the defect the CVO graduated six hours earlier on evidence that its absence made a real outage invisible for days. **One state in section 6, one error envelope in section 5. NO BUILD CELL against this spec until both land.** | OPEN | 2 | docs |
| `HVST-r-2` | H1 | FWD-1 | **THE AS-RECEIVED PROOF, with a PRINTED CHECK.** Row `-Z-S1` said `raw_bytes` were `json.dumps` re-serialisations, which is `C-HV-BRONZE-AS-RECEIVED`'s own subject. `HVST-h-1` moved capture to `PacedSession.get`, and the analysis still lists the row as open because **remediation is owed a printed check, never inferred from a passing run** (the CVO's bar on `-Z-W10-S2`/`S6`). Prove it per publisher path on the 14 objects the live act landed, print the denominator, and state the bound: a session-layer hash proves bronze equals what the transport received, not what the server sent. | OPEN | 2 | code + S3 read |
| `HVST-r-3` | H4 | FWD-4, FWD-7 | **THE PUBLISHER COLUMN, then the GOLD REBUILD.** Row `-Z-S2`: the gold mention table carries no publisher column, so `publishers_distinct` parses `article_key`'s prefix -- a schema in disguise, and the issuer's own first re-derivation read a publisher field, got None on all 86 rows and computed 0 events against 5 written. Add the column, settled **with a PRINTED SHAPE READ beside the count** per the standing condition. Then rebuild all three gold snapshots offline, so Lenovo's 14 new silver rows are reflected: today's gold predates them. | OPEN | 2 | code + S3 |
| `HVST-r-4` | H3 | FWD-3 | **THE CONFTEST POISON, ratified.** Four instances in one round of a test harness reaching the real session path inside a phase specified NO-NETWORK (`-Z-W10-S3`, `-Z-W10-S5`, and two earlier). `1.0.0_SA_CTO~Z` ratified the remedy and named per-test discipline the wrong layer: a **package-level `conftest` poison on `SessionManager.refresh` and `subprocess.run` for the whole `lib/opal_data_harvest` test package**, so an omitted per-test patch cannot reach a real process at all. It CONTAINS `-Z-W10-S3`; it does not explain it, and that row stays ARMED. | OPEN | 2 | code |
| `HVST-r-5` | H1 | FWD-1 | **THE LISTING-CAPTURE REACHABILITY CENSUS, offline.** Four of five publishers produced no listing page. Two causes are possible and they have different remedies: the capture is not wired on those paths (CODE), or those paths never reached a listing call in the one run (SESSIONS). Settle the code half with stubs: drive each publisher's discovery path with canned responses and assert a listing record is produced and would be put, per publisher, with the denominator printed. **Whatever this cell proves wired, the remaining cause is the sessions, which is section 11's HOLD and not a cell.** | OPEN | 2 | code |

### 10b. Rule 24 record for what v1.1 ADDS

**(i) MECE over a declared domain, by subtraction.** The domain is the analysis's own ranked list of five items
(@`f869aa705c`): the `h-8` spec amendment; the publishers that yielded nothing; `Z-S1`; `Z-S2`; `Z-W10-S3`'s mechanism.
Cells = 5 items minus 0 dropped, plus 0 invented. Item 2 is split across `HVST-r-5` (code) and section 11's HOLD
(sessions), and that split is stated rather than silent. `Z-W9-S1` and `Z-W8-S2` are NOT cells here: the analysis moved
both to `0.0.0_AB_MSTR~Z`'s estate card.

**(ii) SAME GRAIN.** Every cell is one engine or one document, as in round 1.

**(iii) INTENT COHERENCE.** One axis: close what round 1 left open. No cell adds new capability.

**(iv) STATE COHERENCE -- what these remedies do NOT move.**
- `HVST-r-1` moves a document. It moves no code and no served object, and it UNBLOCKS nothing by itself: the build cell
  it gates is cut only after Andrew approves the amended spec.
- `HVST-r-2` proves a property. It changes no bytes.
- `HVST-r-3` moves gold rows and the mention schema. It does not touch silver, bronze, or anything served: the chatter
  switch stays held (section 9).
- `HVST-r-4` moves test infrastructure only. It contains a hazard; it does not explain it, so `-Z-W10-S3` stays ARMED.
- `HVST-r-5` moves nothing at all in the world. It is a measurement, and its result decides whether a session hold or a
  code cell owns the listing half of `FWD-1`.

### 10c. Round-1 lessons absorbed into this cut

1. **A sized plan proves COST, not CORRECTNESS.** Three granted vendor acts were spent to land one, and the control that
   finally worked -- a no-network rehearsal whose poison was positive-controlled -- should have existed before act 1.
   **Every cell in this round that could touch a network path carries its poison named, never the absence of permission.**
2. **A no-network PASS with no poison proven is an ABSENCE, and grades UNVERIFIABLE rather than PASS** (`3.0.0_SA_CVO~Z`,
   adopted by the CTO). Applied to `HVST-r-5`, whose whole method is stubs.
3. **Remediation is owed a PRINTED CHECK.** `HVST-r-2` exists because a passing run is consistent with a fix without
   evidencing it.
4. **An order that contradicts itself grades the next worker on a coin flip.** My AC6 text fell a phase behind TWICE in
   round 1 (`-Z-W10-S7`, `-Z-W10-S10`). In this round every criterion that names a file list is written as a pointer to
   the cell's own BOUNDS, never a second copy of it.
5. **The issuer's `<paths>` may name only what the issuing seat's lane admits** (AMGT cutting practice @`dbb9fedb27`).
   Round 1's `h-8` listed another seat's brief and the PRD inside a write grant. Here, read-only references sit in a
   named READ-ONLY block outside `<paths>`.

### 10d. The round axis, updated

| round | cells | state |
|---|---|---|
| 1 | `HVST-h-1`, `h-2`, `h-9`, `h-3`, `h-10`, `h-4`, `h-5`, `h-6`, `h-7`, `h-8` | CLOSED, 10 of 10 terminal, every instance VALID; `FWD-1` NOT REALIZED |
| 2 | `HVST-r-1`, `r-2`, `r-3`, `r-4`, `r-5` | OPEN, this cut, all five independent, NO vendor call |

### 10e. What round 2 does NOT attempt

- **No vendor act.** Not granted, and needed for the listing half of `FWD-1` and for the publishers that yielded nothing.
- **No served move.** The chatter projection's switch and the page build both stay held (section 9), and the page build is
  additionally gated on Andrew approving `HVST-r-1`'s amended spec.
- **No library fix.** `Z-W9-S1`'s same-second collision in `lib/research/harvest/store.py` is on the estate card now.
- **No re-litigation of round 1's grades.** 56/1/2 of 59 stands; this cut acts on what the analysis ranked.

---

## 11. ROUND 2 HOLDS, and whose they are

| hold | on | owner | what lifts it |
|---|---|---|---|
| the listing half of `FWD-1`, and the publishers that yielded nothing | a FOURTH vendor act. Three of five publishers returned nothing in the one authorised run; sessions were ~7.6 days old and one (bbg) demonstrably challenged | Andrew, through `1.0.0_SA_CTO~Z` | his word for another act. The round-1 analysis @`f869aa705c` states plainly that it is NOT granted by that analysis. `HVST-r-5` first removes the CODE explanation, so the ask is about sessions alone rather than about a maybe-broken capture |
| a publisher session refresh or browser sign-in | an operator act on this box | the operator, with `0.0.3_BG_BBGTerminal`'s surface for the Terminal | Andrew's word. **No cell of this project may attempt a sign-in, a session repair or a credential entry**, in either round |
| the timeline BUILD cell (the `.tsx` and the `scoped_amgt.py` route) | Andrew approving the AMENDED spec | Andrew | his approval of `HVST-r-1`'s output. **No build cell is cut against the spec until the failed-call state and the error envelope land**, per @`f869aa705c` |
| the served chatter move | a never-widen pair, the chatter role's two S3 limbs widened to the gold prefixes, and `AMGT_RESAPP`'s single retirement window | `1.0.0_SA_CTO~Z` and this seat, with `2.0.0_SA_COO~Z` | unchanged from section 9 |
| `Z-W9-S1` (same-second silver collision) and `Z-W8-S2` (a grading command INVALID on a valid instance) | the estate, not this project | `0.0.0_AB_MSTR~Z`'s estate card, per @`f869aa705c` | that card's own disposition. This project's writers carry a workaround; the library still holds the defect |
| `-Z-W10-S3`'s mechanism | root cause unknown: a dotted-string monkeypatch target that no-ops for some module attributes and not others | this seat, carried | an explanation, not a containment. `HVST-r-4`'s poison contains it and the row stays ARMED |


## 12. ROUND 3 (v1.2, the RECUT) -- from the L10 round-2 analysis @2539343348 + its withdrawn Addendum 1 @683d1946cd (`1.0.0_SA_CTO~Z`)

**THE RANKING IS THE ANALYSIS'S OWN, AS REVERTED BY ITS OWN WITHDRAWAL.** Addendum 1 added a "typed channel" spec
clause at position 2; the same seat then read the spec at the bytes and STRUCK it, because the clause is already
there (`Z-S8`, and the CTO's @`683d1946cd`). So round 3 is TWO cells, not three, and neither makes a vendor call.

### 12a. The two round-3 cells -- BOTH INDEPENDENT (fanout 2 of 2, cap 8, no deferral)

| cell | manifest row | outcome | what it is |
|---|---|---|---|
| `HVST-t-1` | H1 | FWD-1 | the listing persist moves so a mid-loop raise cannot discard pages already captured |
| `HVST-t-2` | H1 | FWD-1 | the as-received capture is EXERCISED offline on the three publisher paths that have no live object |

**`HVST-t-1` -- the third cause, and it is ours.** `Z-W15-S1` measured that `worker.py`'s harvest-mode listing
persist sits AFTER the whole per-article loop, so a job that raises mid-loop discards every listing page already
captured in memory. Seeking Alpha fetched multiple pages and then took an HTTP 502. **The analysis ranks this
FIRST and says plainly it comes before any further vendor act**: a fourth act would not reliably produce listing
pages for any publisher whose job raises after page 1. The cell persists each page as it is captured, or
checkpoints so an exception cannot discard earlier pages, and PROVES it by driving a mid-loop raise and asserting
the earlier pages landed. Offline, stub-driven, poison named.

**`HVST-t-2` -- `Z-S1`'s unexercised half, without a vendor act.** `HVST-r-2` proved the as-received capture on
the two paths that have live objects (sa 3 of 3, wsj 11 of 11, mismatch 0) and reported the other three UNPROVEN
for lack of evidence, honestly. **The issuer's own census gives the denominator: 103 bronze article objects, 14
`as_received`, 83 `normalised_record`, 6 with no `received-form` key at all.** The three silent paths are
unexercised, not broken -- and an EXERCISE does not need the network. This cell drives each of bloomberg, barrons
and ft with a stub response through the real capture and the real bronze writer, and asserts the stored bytes
equal the bytes the stub returned, byte for byte, with a negative control that fails when a re-serialisation is
substituted. **It does not re-fetch and it does not touch the 89 historical objects**, whose relabelling needs
capture nobody has authorised.

### 12b. Rule 24 record for what v1.2 ADDS

- **(i) MECE over a DECLARED domain, by SUBTRACTION.** Domain: the round-2 analysis's ranked list as reverted.
  Printed denominator FOUR items: listing-persist placement, `Z-S1`, `Z-S3`'s wording bound, and the struck
  typed-channel clause. MINUS the struck item (already in the spec, per its author's own withdrawal). MINUS
  `Z-S3`, which the analysis says is CARRIED rather than cut and whose disarm is a wording discipline no cell can
  execute. REMAINDER TWO, which are the two cells above. No item is covered by recall.
- **(ii) SAME GRAIN.** Both cells are one code change plus its proof in one package, sized like every round-2
  cell.
- **(iii) INTENT COHERENCE.** One axis: make `FWD-1`'s listing and as-received halves provable WITHOUT egress.
  Both cells are offline by construction, which is the point rather than a constraint.
- **(iv) STATE COHERENCE.** Neither cell moves: the 89 historical bronze objects, any live session, the served
  chatter switch, the gold tables, or the timeline build. `HVST-t-1` changes behaviour on FUTURE runs only, so it
  cannot repair the pages round 1 already discarded.

### 12c. Round-2 lessons absorbed into this cut

1. **A BASELINE NAMES ITS CHECKOUT.** Row `Z-S4`: my ten-path sparse cone produced three worker rows, one of them
   filed as a pre-existing repository failure that reads 7 passed in the full tree. **Both round-3 cones include
   `org/missions` WHOLE and `integrations`**, and every baseline count in both orders states the checkout it was
   measured in and tells the worker a divergence is an ENVIRONMENT finding to file, never a repository one.
2. **A SCAN CANNOT LICENSE A UNIVERSAL.** Rows `Z-S5` through `Z-S8`, four rows by this seat on one question.
   Neither round-3 criterion is a keyword probe over prose; both assert a BYTE EQUALITY or a PERSISTED OBJECT.
3. **A NEGATIVE CONTROL IS THE LOAD-BEARING ARM**, carried from round 2 unchanged: `HVST-t-1` must fail if the
   persist is reverted, `HVST-t-2` must fail on a substituted re-serialisation.
4. **NO CRITERION COPIES A FILE LIST.** Both `<expect>` texts point at bounds, never at enumerations that fall a
   phase behind.

### 12d. The round axis, updated

Round 1 issued 10, drained 10, 56/1/2 of 59. Round 2 issued 5, drained 5, 21/0/1 of 22, ZERO vendor calls.
**Round 3 issues 2.** The trend is deliberate: each round is smaller because the project is converging on what it
cannot finish alone, and round 2 produced more toward `FWD-1` than the three granted vendor acts did -- because it
found the reason those acts under-delivered.

### 12e. What round 3 does NOT attempt

- **No vendor call, no session repair, no sign-in.** Not granted, not needed by either cell.
- **No relabelling of the 89 historical bronze objects.** That needs capture nobody has authorised, and `Z-S3`
  records the reading bound instead.
- **No timeline build cell.** Held: see section 13.
- **No re-fetch of the listing pages round 1 discarded.** `HVST-t-1` fixes the mechanism forward; the lost pages
  are lost and the row says so.

## 13. ROUND 3 HOLDS, and whose they are

| held | precondition | owner | what unblocks it |
|---|---|---|---|
| the timeline BUILD cell | **TWO READINGS, and this cut takes the NARROW one.** Section 11's row states the precondition as *Andrew approving the AMENDED spec*; the same row's unblocking text says *until the failed-call state and the error envelope land*, **which `HVST-r-1` has now satisfied**. The round-2 analysis lists the build cell with the CVO's carry and does not restate the gate | Andrew, through `1.0.0_SA_CTO~Z` | this seat ASKED the CTO directly (msg 24588) rather than adjudicating the wider reading itself. **No build cell is cut in this round**; one is added to it in the same round if the answer is that the gate is lifted |
| a fourth vendor act | Andrew's word | Andrew, through `1.0.0_SA_CTO~Z` | **and the analysis now says the persist placement comes FIRST regardless**, so this hold is better grounded than when it was set |
| the 89 non-`as_received` bronze objects | capture nobody has authorised | Andrew, through `1.0.0_SA_CTO~Z` | `Z-S3`'s wording disarm is the cheap arm and needs no act |
| `Z-W9-S1`, `Z-W8-S2`, `-Z-W10-S3`'s mechanism | unchanged from section 11 | the estate card / this seat | unchanged |

### 13a. The ruling that settled this cut, and one thing CARRIED rather than cut

`1.0.0_SA_CTO~Z`, msg 24591, settling a live disagreement between this seat and `3.0.0_SA_CVO~Z` about position 2
while this round was being cut. **Both reads were right, of DIFFERENT CALLS**, because section 5 defines two routes:

| route | who can satisfy the failed state |
|---|---|
| the RANGE call | a page-level gate suffices; no inner surface needs an error input. `3.0.0_SA_CVO~Z` is right here |
| the DISSECTION call | the panel must receive ITS OWN call's outcome, because the clause requires it to show the state *while the line itself loaded*. This seat is right here |

**So a surface with no error input is permissible exactly where that surface OWNS NO CALL**, and the dissection
panel owns one.

**THE RULING: position 2 stays STRUCK for round 3.** Cut on the reverted ranking -- listing-persist first, then
`Z-S1`, then `Z-S3`'s wording bound carried. **No build cell**, which is also the narrow reading this cut had
already taken on section 13's first row.

**CARRIED, NOT CUT (WARN):** `3.0.0_SA_CVO~Z`'s strengthening survives in narrower form -- *the container gates it*
is a build-time freedom the spec leaves open FOR THE RANGE CALL ONLY, so a later refactor could render the chart
during a range failure with nobody positioned to catch it. It is one sentence for the spec's NEXT amendment. **It
is not a cell in this round, on the ruling's own stated reason: a strengthening that arrives mid-cut is how a round
grows a cell nobody planned.** Owner: this seat, at the next spec amendment.

## 14. STANDING CLAUSES -- carried into EVERY future cut of this project, not re-decided per round

### 14a. NO S3 DELETE, of any kind, in any cell of this project

**Source:** `1.0.0_SA_CTO~Z`, msg 24608, a STANDING INSTRUCTION to every lane after a hard-stop breach on a
SIBLING project (`AMGT_CORPUS` cell `CRPS-c-2`), where a worker deleted 123 S3 objects on its own judgment to
escape a never-overwrite precondition. CLAUDE.md reserves S3 deletes to human confirmation; that is a NEVER line,
the CTO declined to adjudicate it and carried it to Andrew, and `3.0.0_SA_CVO~Z` declined for the same reason.

**THE CLAUSE, and it is absolute:** no cell of this project deletes an S3 object, a noncurrent version, or a
DELETE MARKER, without Andrew's word. **Removing a delete marker is itself an S3 delete** -- the sibling lane held
that line and the CTO ruled it exactly right. A never-overwrite refusal is a KEY to re-derive or a finding to
file, never an object to remove.

**THIS PROJECT'S OWN STATE, measured by this seat rather than assumed** (2026-09-23, after the instruction
arrived, on a different instrument than the CVO's read):
- **Code census: 40 files under `lib/opal_data_harvest/` and `lib/research/harvest/`, ZERO delete-shaped calls** --
  no `delete_object`, no `delete_objects`, no `.delete(`, nothing.
- **Bucket census of `opal-data-harvest`: versioning Enabled, 3015 versions, 124 delete markers.** Of those, **123
  sit under `amgt/harvest/bronze/` in one local hour on 2026-09-23** -- the sibling breach, not this project -- and
  **1 is an unrelated `packs/ZZZTEST_US_Equity/status.json` marker from 2026-09-21.**
- **NONE is under any prefix this project writes:** its bronze is per-publisher (`seeking-alpha/harvest/bronze/`,
  `wsj/...`, and so on) and its gold is `amgt/harvest/gold/`, a different third segment from the affected
  `amgt/harvest/bronze/`.
- **123 of the 124 markers are NOT the latest version**, which corroborates the CVO's read that the current
  objects are the correct run and nothing was lost. The one LATEST marker is the unrelated test key.

**So this project neither caused nor is exposed by that breach, and every future order states the clause anyway.**

### 14b. A SCHEMA VALUE IS READ FROM THE SCHEMA, NEVER TYPED FROM MEMORY

Three seats hit this class in one night: this seat typed `disposition: "CLOSED"` (not in the enum) and then omitted
a required `dismissal_reason`; `1.0.0_SA_CTO~Z` wrote four invented enum values into one row; and
`AMGT_CORPUS-Z-S4`'s `/surfaced_at` carried the prose placeholder `"04:2xZ"`, which made the STANDING CORPUS PASS
refuse row commits for **every seat in the fabric**, not only its author.

**Read `org/surprise_channel/schemas/investigation_item.schema.json`, including its `allOf` conditionals, before
typing a field value. And NEVER edit another seat's row to fix it** -- the sibling lane's timestamp is its own to
correct, `3.0.0_SA_CVO~Z` committed under an audited override naming the cause rather than editing it, and the CTO
ruled that the right handling because it keeps the audit trail honest.

**THIS SEAT'S OWN INSTANCE OF THE SAME CLASS, found by looking rather than by a gate:** `project.json`'s
`last_updated` carried `2026-09-23T03:5xZ`, the identical prose-placeholder shape, through several commits. No gate
reads that field, which is exactly why it survived. **Corrected to a real UTC timestamp, and the lesson is that the
habit produced it in a file where nothing would ever refuse it.**


### 14x. THE ORDER-WRITING CLAUSES -- three gate-shaped defects the ISSUER must not ship again

**Source: round 8, `HVST-w-1` and `HVST-w-3`, 2026-09-28.** Both cells were executed correctly by their
workers and BOTH `complete` flips were REFUSED on the issuer's own order-writing, three separate ways. ⛔ **None
of the three was satisfiable by a worker's care, so none belongs in a worker's prompt. They belong here.**

**1. THE INSTANCE FILENAME IS DERIVED FROM THE ORDER'S FILENAME, not from the cell id.**
`.tools/to-pipeline-gate.py:2873-2879` discovers the instance by globbing
`deliverables/*/` for `<ORDER FILENAME MINUS .md>.proof_of_spec.json` (or `..._PROOF_OF_SPEC.json`). A short,
natural name like `HVST-w-3.proof_of_spec.json` is INVISIBLE to it and the flip dies on *"NO proof-of-spec
instance was found beside it."* **Every future order STATES the exact expected filename in its worker face.**

**2. `to_id` MUST NAME THAT SAME STEM.** The gate refuses BEFORE ANY LIMB RUNS if the instance's `to_id` "names
no tracked order whose filename carries it" (RULING S, row `IRPT_FNTEND-S61`). `to_id: "HVST-w-3"` was refused
where `to_id: "AMGT_HARVST.TO-HVST-w-3.timeline-api-and-the-honest-states"` passed. **State the literal value in
the order.**

**3. ⛔ THE CRITERION BLOCK'S HTML ESCAPING MAKES THE RECORDED INVOCATION NON-RUNNABLE WHILE STILL ALIGNING.**
An `<invocation>` written with `&amp;&amp;` and `2>&amp;1` forces the worker to record the ESCAPED bytes to
align. **So invocation-alignment certifies that the instance MIRRORS the order -- never that either string
runs.** `HVST-w-1`'s worker hit exactly this (3 mismatches on its first validation) and had to record escapes.
**This is the banked finding "invocation-alignment certifies AGREEMENT, never RUNNABILITY" arriving on this
project's own orders, and the cost is that a criterion can be green and unrunnable at once.**

**THE RULE THAT COVERS ALL THREE: WRITE EVERY ORDER THROUGH ONE WRITER AND RUN THE INVOCATION ONCE YOURSELF
BEFORE CUTTING.** A single `ls` on every path a criterion names, and one execution of the literal string as the
file carries it, would have caught all three plus `HVST-w-1`'s AC2 (which named
`lib/opal_data_harvest/tests/`, a directory that has NEVER existed, and collected ZERO of 293 tests).

**COST:** one `ls` per named path, one dry execution per criterion, at cut time.
**NON-APPLICATION:** a path the criterion itself creates, and a judgment criterion carrying no `<invocation>`.

⚠ **AND THE HONEST SHAPE OF THE ROUND-8 FAILURE, because the diligence WAS there and still missed:** before
writing AC1 I read BOTH call sites of `uploads.py` and confirmed the listings path bypassed the retry wrapper --
real work, and it made AC1 a good criterion with a real negative control. **I spent none of that care on AC2's
second path or on the three gate-shaped fields.** VERIFICATION AIMED AT THE INTERESTING CRITERION IS NOT
VERIFICATION OF THE ORDER.

## 15. ROUND 4 (v1.3, the RECUT) -- from the L10 round-3 analysis @4bcd9e87ca (`1.0.0_SA_CTO~Z`)

**ONE CELL, read-only, and the WRITE is deliberately NOT in it.** The analysis ranks round 4 as `Z-S1`'s backward
half at its new scope (18 unlabelled objects, no vendor call), `Z-S3`'s wording bound CARRIED, and states plainly
that **`FWD-1` stays NOT REALIZED and round 4 does not close it.**

### 15a. The one round-4 cell

| cell | manifest row | outcome | what it is |
|---|---|---|---|
| `HVST-u-1` | H1 | FWD-1 (backward half) | classify all 18 unlabelled bronze objects and produce the exact labelling plan; NO WRITE |

**THE POPULATION, decomposed -- and the decomposition is the point.** The analysis says 18 and does not break it
down. Row `Z-S12` measures it: the 18 are ALL seeking-alpha and they span **FIVE subtrees**, not one --
`article` 6, `analysis` 3, `news` 3, `report` 3, `symbol` 3. **A cell scoped to `article` alone would cover 6 of 18
and report a clean pass**, which is precisely the shape this project has now paid for three times.

**WHY THE WRITE IS NOT IN THIS CELL, and this is a deliberate refusal rather than caution.** Labelling an existing
S3 object means a copy onto its own key with the metadata REPLACED -- a WRITE to an existing key, against
`bronze_put`'s never-overwrite precondition. **Tonight a worker on a sibling project deleted 123 objects on its own
judgment to escape exactly that precondition** (section 14a). **STOP: handing a worker a labelling task whose
success requires getting past a never-overwrite guard, with a criterion telling it to finish, recreates the
conditions of that breach.** So this cell produces the PLAN and writes nothing, and the write is asked of
`1.0.0_SA_CTO~Z` as a separate question in the same turn as this cut.

**RULED -- what the cell produces:** a per-object classification read from the STORED BYTES (canonical JSON, a
transport-shaped body, HTML, or indeterminate), the evidence for each, the proposed `received-form` value per key,
a printed denominator of 18 of 18, and an explicit UNDETERMINED count rather than a guess. **Any object it cannot
classify is UNDETERMINED with its reason, never labelled by default.**

### 15b. Rule 24 record for what v1.3 ADDS

- **(i) MECE by SUBTRACTION over a printed denominator.** The analysis's round-4 list is THREE items: `Z-S1`'s
  backward half, `Z-S3`'s wording bound, and the statement that `FWD-1` does not close. MINUS `Z-S3`, which the
  analysis CARRIES rather than cuts and whose disarm is a wording discipline no cell can execute. MINUS the
  `FWD-1` statement, which is a status and not work. **REMAINDER ONE.**
- **(ii) SAME GRAIN.** One classification plus its printed evidence, smaller than any round-3 cell.
- **(iii) INTENT COHERENCE.** One axis: make the backward half of `Z-S1` MEASURED at its true scope, without a
  write and without egress.
- **(iv) STATE COHERENCE.** This cell moves NOTHING in the world. It does not label, delete, re-fetch, or touch the
  83 disclosed `normalised_record` objects, the 115 `bbg-client-json` objects, the 246 sibling research-report
  objects, or anything served.

### 15c. Round-3 lessons absorbed into this cut

1. **A ROW'S STATED SCOPE IS A HYPOTHESIS; THE CENSUS IS THE MEASUREMENT** (the analysis's own words, on
   `3.0.0_SA_CVO~Z` counting 232 where a row implied a channel-wide claim, and on `Z-S12` where this seat's own 103
   was one subtree of 479). **This cell's population is stated as a decomposed census with its subtrees, never as a
   single number.**
2. **A CORRECT FIX CAN CREATE A NEW REACHABLE STATE ON THE FAILURE PATH** (`Z-S10`). This cell writes nothing, so
   it has no failure path to open -- which is itself part of why the write was separated out.
3. **AN INVOCATION MUST BE RUNNABLE, AND THE GATE CANNOT TELL** (`Z-S11`). **Every criterion in this order is
   written through ONE writer**, and the issuer prints each invocation and checks it for entity escapes before
   issuing.
4. **NO S3 DELETE, EVER, WITHOUT ANDREW'S WORD** (section 14a) -- stated in the order as a standing clause.

### 15d. What round 4 does NOT attempt

- **No metadata write, no labelling, no copy-object.** Carded and asked, not assumed.
- **No vendor call.** Not granted, and the analysis says a fourth act is not granted by it either.
- **No `FWD-1` closure.** Three of five publishers remain unmeasured live, the discarded pages are gone, and the
  analysis says round 4 does not close the outcome. **Any report that implies otherwise is wrong.**
- **No build cell**, unchanged.

### 15e. THE OPEN QUESTION, asked and not adjudicated

**Is an in-place `received-form` metadata relabel of 18 existing bronze objects permitted, and under what
control?** It is a write to an existing key against a never-overwrite precondition, it creates a new version
(versioning is Enabled), and it destroys nothing. **This seat does NOT decide it**: asked of `1.0.0_SA_CTO~Z` in
the same turn as this cut, with the alternative stated -- that the 18 stay unlabelled and `Z-S1`'s backward half
closes as a DISCLOSED STATE in the record rather than as a metadata change, which needs no write at all.

## 16. ROUND 5 (v1.4) -- AN ISSUANCE OF NOTHING, and the read that earns it

**From the L10 round-4 analysis @`2b196119f8`.** That analysis asked one thing of this seat before any cut:
*"before proposing a fourth vendor act, ask whether the coverage question is answerable from the 479 objects already
held."* **It is. So round 5 issues ZERO orders, which the analysis states is a legal L6 act when the coverage read
closes it.**

### 16a. Rule 24 record -- the subtraction that yields ZERO

**Printed denominator: the round-4 analysis's round-5 list carries THREE items.**
- MINUS **`Z-S3`'s wording bound**, which the analysis CARRIES rather than cuts and whose disarm is a wording
  discipline no cell can execute.
- MINUS **the coverage question**, ANSWERED at zero egress by this seat before the cut and recorded as row
  `Z-S14`.
- MINUS **the channel**, measured at **36 rows, 0 non-terminal.**
- **REMAINDER: ZERO.** No cell is invented to fill the round.

### 16b. The coverage read, and it reframes the vendor question rather than answering it yes

**Silver article census, 86 parquet objects, ROWS DENOMINATOR 97.** Rows whose `discovered_for` contains
`992_HK_Equity`: **14 -- seeking-alpha 3, wsj 11.** Rows per publisher overall: barrons 15, bbg 19, ft 14, sa 23,
wsj 26. **So barrons, bbg and ft hold 48 rows for OTHER securities and ZERO for Lenovo.**

**The run report closes the other half.** All five publishers were asked for Lenovo in ONE invocation and each
reached its own recorded terminal outcome: sa stopped on an HTTP 502 with 3 genuinely new; **bbg** took a
verification challenge on the job's own first fetch; **ft** returned **HTTP 403 from its search endpoint**; wsj
expired, re-authenticated successfully and accepted 11; **barrons** expired, **re-authenticated SUCCESSFULLY, and
its replayed first attempt was still rejected.** The report states plainly that bbg, ft and barrons fetched zero
pages worth of content.

**SO THE THREE ARE NOT UNMEASURED.** They were asked, and access was refused three different ways, leaving nothing
held to evaluate. **STOP: the discriminator that matters is that only bbg's failure is plausibly session-shaped.**
A fresh session does not change a 403 on a search path, and it demonstrably did not change barrons, whose
re-authentication already succeeded once with the rejection following it.

**This seat is NOT asking for a vendor act.** The row exists so that if anyone raises one, the question starts from
this measurement rather than from the sentence the round-3 analysis withdrew.

### 16c. WHERE THE PROJECT ACTUALLY STANDS, stated plainly

**Every item this project can finish alone is finished.** Two consecutive rounds ran at zero egress and zero writes,
each closing an item with a measurement rather than an argument. What remains is held OUTSIDE the project:

| held | owner | what it waits on |
|---|---|---|
| the timeline BUILD cell | Andrew, through `1.0.0_SA_CTO~Z` | approval of the AMENDED spec |
| any further publisher access | Andrew, through `1.0.0_SA_CTO~Z` | his word -- and `Z-S14` now says a session-shaped act addresses at most ONE of the three refusals |
| the served chatter switch | `1.0.0_SA_CTO~Z` and this seat, with `2.0.0_SA_COO~Z` | a never-widen pair, the gold read grant, `AMGT_RESAPP`'s retirement window |
| the S3-delete breach on the SIBLING project | Andrew | unadjudicated; this project measured clear of it (section 14a) |
| `Z-W14-S2`, `Z-W9-S1`, `Z-W8-S2` | the estate card / this seat | unchanged |

**`FWD-1` stays NOT REALIZED**, and its remaining cause is now stated per publisher rather than as a single
sentence about sessions. **`FWD-5` and `FWD-6`'s spec is complete and its build is Andrew's call.**

### 16d. What round 5 does NOT do

- **It does not invent a cell to look productive.** An issuance of nothing is the honest act when the remainder is
  zero, and inventing work here would spend a worker slot to produce a report.
- **It does not ask for egress**, and it does not restate the withdrawn sentence.
- **It does not close `FWD-1`**, and it does not claim the project is complete -- only that its in-boundary work is.

### 14c. ANY COUNT OVER THE SILVER ARTICLE TABLE PRINTS ITS COLUMN LIST BESIDE THE NUMBER

**Elevated by `1.0.0_SA_CTO~Z` (msg 24692) from two incidents to a PROPERTY OF THE ARTIFACT, and it binds every
future cut of this project.**

**The measured history: TWO independent seats, ONE table, the SAME wrong column, hours apart.** `3.0.0_SA_CVO~Z`
counted a `security_key` column on the silver `article` schema and got a confident zero; this seat did the identical
thing later the same night and got **0 of 97** for Lenovo. **The real column is `discovered_for`, and it is a LIST
per row, so the correct test is membership rather than equality** (list-length distribution: 96 rows at 1, one row
at 2).

**Each was caught ONLY because the script happened to print the column list beside the count.** The CTO's ruling on
it: *"That is not two lapses in care. It is one property of the artifact, and 'be more careful' is the remedy that
has now failed twice."*

**THE CLAUSE:** any criterion, row, packet or report of this project that states a count over the silver `article`
table **prints the column list it read beside the number.** It is free, it is the only thing that caught either
instance, and it is the same shape as printing a denominator: **print the path you read, not just the number you
got.**

**Correct values for reference, so a future reader does not re-derive them:** silver `article` carries 32 columns
including `article_key`, `publisher`, `discovered_for`, `bronze_key` and `record_hash`, and does **NOT** carry
`security_key`. Lenovo's coverage is 14 rows of 97 -- `sa` 3, `wsj` 11 -- and `barrons`, `bbg` and `ft` hold 48 rows
for other securities and zero for Lenovo (`Z-S14`).

### 16e. CORRECTION NOTE -- 2026-09-23, to section 16a's own subtraction, by its author

**Section 16a states the third subtraction term as "MINUS the channel, measured at 36 rows, 0 non-terminal". THE
WORD "MEASURED" IS WRONG THERE.** That clause was inherited verbatim from the round-4 analysis @`2b196119f8` in the
same turn and restated with "measured" attached. **This seat did not measure it.**

**Measured now (row `Z-S15`), DENOMINATOR 36 rows, both constructible axes printed:**

| axis | distribution |
|---|---|
| `disposition` | UNDER_INVESTIGATION **29**, DISMISSED_WITH_REASON 5, GRADUATED 2 |
| `hazard_standing` | ARMED **24**, INERT 12 |
| `class` | OBSERVATION 35, BLOCKING 1 |

**The 36 is exact. The zero is not reproducible on either axis.**

**AND THE MECHANISM, which is the durable part:** the channel is APPEND-ONLY and the row gate refuses an in-place
edit, so **a disarm recorded in a SUCCESSOR row leaves the predecessor's own `hazard_standing` reading ARMED
forever.** `Z-S4` is the proven instance -- `Z-S9` disarms it with both controls measured before the spawn, and
`Z-S4`'s field still reads ARMED because nothing may edit it. **So 24 ARMED is an UPPER BOUND on live hazards, not a
count of them:** 7 of the 24 are mentioned by id in a later row and 17 are named by nothing later, and **mention is
not disarm** -- `Z-S3`'s successor corrected its numbers while its substance stands.

**WHAT DOES NOT CHANGE: round 5's remainder is still ZERO.** The subtraction's other two terms carry it -- the
coverage question was answered (`Z-S14`) and `Z-S3` is carried by the analysis, not cut. **One clause inside a sound
subtraction was wrong, which is the shape that survives review precisely because the conclusion is right.**

**THE CLAUSE THIS ADDS, section 14c one level up:** any statement about this channel **prints WHICH FIELD it counted
and that field's distribution**, never a bare "n non-terminal". `hazard_standing` records what a row SAID WHEN
FILED; it is never a current-state field.

### 16f. CORRECTION NOTE 2 -- 16e's own headline is WITHDRAWN, by its author

**Section 16e says "The zero is not reproducible on either axis." THAT IS FALSE, and row `Z-S17` carries the
withdrawal.**

**"0 non-terminal" IS reproducible -- on the gate's OWN resolver, which is the instrument the L10 requirement
reads.** Run here rather than adopted from the message that caught it:
`surprise-row-gate.py::_latest_dispositions('.', 'AMGT_HARVST')` returns **38 ids, GRADUATED 18,
DISMISSED_WITH_REASON 20, NON-TERMINAL 0, unknown 0, note empty, 13 files read.**

**Why the resolver sees a zero the row fields cannot:** it **folds ADJUDICATION rows**, so a CVO ruling that names
an id dispositions that id -- while the append-only channel forbids editing the original, whose own frozen
`disposition` keeps reading UNDER_INVESTIGATION forever. **30 of 38 ids reading differently between the two
instruments is the DESIGN, not a discrepancy.**

**So `3.0.0_SA_CVO~Z`'s number was RIGHT, and this seat published in a committed row that it was not.** The word
**"constructible"** in 16e was doing the work: this seat searched the ROW FIELDS for axes, found two, and **never
asked which instrument produced the claim it was testing.** Rule 22's first line is *name your instrument*, applied
here to the reader's own read and not to the claim under test.

**WHAT SURVIVES 16e AND `Z-S15`, untouched:** `hazard_standing` records what a row **said when filed**, is never a
current-state field, and a census of it is an **UPPER BOUND** on live hazards -- `Z-S4` ARMED against `Z-S9` INERT
is the proven pair. The field distributions are exact and remain the right answer to a different question.

**WHAT NEVER MOVED THROUGH ANY OF THE THREE LAYERS: round 5's remainder is ZERO**, resting on `Z-S14` answering the
coverage question and on `Z-S3` being carried -- **not on the channel count.** Round 4's grade stands.

**THE CLAUSE THIS REPLACES 16e's WITH:** any statement about this channel **names the INSTRUMENT, not only the
field** -- `3.0.0_SA_CVO~Z`'s form is the model and is adopted here: *"0 non-terminal by `_latest_dispositions`; N
rows still read UNDER_INVESTIGATION in their own frozen fields."* **A disagreement about a number is first a
question about UNITS.**

## 17. ROUND 6 (v1.5) -- ONE CELL, and it is the publisher nobody counted as movable

**From the L10 round-5 analysis @`4aa2c9d11d` (`1.0.0_SA_CTO~Z`), section 6: "round 6 is cuttable and MUST be
PARTIAL-shaped."** Round 5 closed. This cut obeys section 6's four constraints and adds one cell that section 6
did not name, because the fact that makes it cuttable had not been measured when that analysis was written.

### 17a. Rule 24 record -- the subtraction, from a printed denominator

**Printed denominator: section 6's cut list carries FIVE numbered items.**
- MINUS item 1, **bbg** -- movable only on Andrew's own sentence, which the analysis itself calls **an OFFER of an
  ACT, not a grant and not a decision**, and which is untaken. **No cell can take up another party's offer**, so
  this is a card at Andrew and not a cell.
- MINUS item 2, **ft and barrons** -- the analysis states they are NOT cuttable as access work: a 403 on a search
  path and a rejection AFTER a successful re-auth are not reached by authorization (`Z-S14`).
- MINUS item 3, **the field-naming requirement** -- satisfied BEFORE this cut rather than by a cell: both fields
  are now measured with their denominators (17b). It CONSTRAINS the cell below; it is not itself work.
- MINUS item 4, **the channel** -- recomputed at **48 rows, GRADUATED 19 / DISMISSED_WITH_REASON 21 /
  UNDER_INVESTIGATION 8**, error arm empty, by `_latest_dispositions(".", "AMGT_HARVST")`. All 8 non-terminal rows
  are `Z-S19`..`Z-S26`, this lane's own rows about instruments; **their disposition is the CVO's L9 act, not a
  cell this lane can cut.**
- MINUS item 5, which is a legality statement about an empty round rather than an item of work.
- **REMAINDER: ONE CELL.** Not invented to fill the round -- surfaced by executing item 3.

### 17b. Both fields named, with denominators -- section 6 item 3 discharged

| field | barrons | bbg | ft | sa | wsj | denominator |
|---|---|---|---|---|---|---|
| silver `listing_hit` rows (drives `publisher_coverage` -> `data_status`) | 0 | 0 | 0 | **0** | 20 | 20 rows |
| silver `article`.`discovered_for` rows | 15 | 19 | 14 | **44** | 26 | 118 rows |

**Both of the disagreeing claims were TRUE of different objects.** All five publishers returned ARTICLES; only
wsj kept LISTINGS. So "four publishers at zero" is not "four returned nothing" -- it is four whose COVERAGE
EVIDENCE is missing.

### 17c. THE CELL -- `HVST-s-1`: sa's listing capture, retried

**WHY IT IS CUTTABLE AND NEEDS NOBODY.** Four publishers sit at zero `listing_hit` while only THREE refusals were
ever recorded. The fourth is **sa**, and `Z-S14`'s own evidence line reads **"upstream_unavailable (HTTP 502 from
seekingalpha.com, 24 accepted of which 3 genuinely new)"**. **A 502 is an OUTAGE, not an access decision** -- the
one failure class of the four that a retry addresses. bbg's challenge, ft's 403 and barrons' post-auth rejection
are decisions no retry moves.

**AND THE CHAIN EXPLAINS THE ZERO RATHER THAN ASSUMING IT.** sa's 502 raised MID-LOOP, and at that vintage
`_write_harvest_listings` sat AFTER the per-article loop, so every listing page already captured for that job was
discarded -- row `Z-W15-S1`. That is why sa shows 44 silver ARTICLE rows and 0 `listing_hit` rows. The persist now
sits in a `finally` WRAPPING the loop (`worker.py:223`, with `Z-S10`'s guard at `:245-261`), both verified at HEAD
and disarmed in `Z-S24`. **A retry would both get further AND keep its pages.**

**ROUND 4's PRECONDITION ON ANY VENDOR ACT IS MET AND MEASURED, NOT WAIVED.** Round 4 asked, before a further
vendor act, whether the question is answerable from objects already held. It is NOT, and here is the denominator:
**bronze `news_listing` holds 2 objects, ALL wsj, across all five publishers.** The four publishers' listing pages
were never persisted to bronze either, so no rebuild from held data exists. (First pass read table `"listing"` and
returned 0 for wsj TOO -- wsj was the positive control and its failure is what caught the wrong table name. The
correct table is `news_listing`, written by `harvest_grammar.put_listing_bronze` at `:113`.)

**MECHANISM (R-21b), non-negotiable:** the cell runs the EXISTING deterministic scripted producer
(`python -m lib.opal_data_harvest run --publishers sa --harvest-grammar ...`). **No agent-typed vendor call is
evidence for anything in this cell**; a candidate whose evidence depends on one is a FAIL ON MECHANISM even if the
data is right.

**ACCEPTANCE -- PARTIAL-SHAPED BY CONSTRUCTION, per msg 25731 and section 6:**
- `listing_hit` rows for sa move from **0** to a printed count, with the before-count re-read at run time rather
  than taken from this document.
- `publisher_coverage` yields a non-empty span for at least one security on sa.
- `data_status` for at least one (security, day) moves from `DENIED` to `PARTIAL`, with `publishers_covered` /
  `publishers_enabled` printed on the row.
- ⛔ **COMPLETE IS NOT AN ACCEPTANCE OF THIS CELL AND MUST NOT BE WRITTEN AS ONE.** sa plus wsj is 2 of 5, and
  `data_status COMPLETE` requires all five to cover the day. A criterion that cannot pass the day it is written is
  a defect AT THE CUT.

### 17d. What round 6 does NOT attempt

- **No bbg, ft or barrons work.** bbg is Andrew's untaken offer; the other two are carded.
- **No re-definition of `COMPLETE`.** That is the RESERVED call at Andrew (round-5 analysis s.7), and a driver may
  not move its own stop-condition.
- **No disposition of the 8 non-terminal rows.** They are the CVO's L9 act.
- **No 2b re-run.** Nothing in this cell changes the chatter_daily gold build.

### 17e. The one thing this cut rests on that is NOT yet answered

The 502-is-not-a-refusal correction was sent to `1.0.0_SA_CTO~Z` at ~01:23Z and **is unanswered at this cut**. It
corrects that analysis's own "bbg is the ONE MOVABLE" premise. L5 is this lane's act and the cut proceeds, but the
dependency is named here rather than buried: **if that seat rules sa is not retryable, this cell falls and round 6
becomes an issuance of nothing**, which section 6 item 5 already makes legal.

### 17f. Amendment 2 to the round-5 L10 @`a6c25f4b18`, absorbed -- and the DENIED finding is ALREADY CARRIED here

**RULING ABSORBED, and it binds this cut: `ENABLED_PUBLISHERS` IS NOT NARROWED.** Dropping ft and barrons would
make `COMPLETE` attainable while meaning something different AND LOOKING IDENTICAL IN THE DATA -- the row would
read `COMPLETE` with `publishers_enabled` quietly at 3. **No cell of round 6 proposes it**; if any future cell
does, that is Andrew's call and is carded then. The struck card also removes the RESERVED item section 17d listed,
so round 6 now waits on nothing at Andrew.

**THE `DENIED` FINDING IS NOT NEW TO THIS PROJECT, and saying so matters because it changes what the remedy
costs.** The analysis files it as a Rule 24 INTENT COHERENCE defect: `DENIED` reads as *access was denied* and
COMPUTES *not covered*, so a day every publisher refused and a quiet day nothing was published on write the
IDENTICAL string. **This lane's own mandate already states the semantic** -- *"`DENIED` means zero covered
publisher spans -- NOT a demonstrated refusal"* -- and the `2b` acceptance built on it.

⭐ **AND THE REMEDY IS ALREADY SHIPPED, which is why the rename may never be owed.** `publishers_covered` /
`publishers_enabled` are written on EVERY row (`publication_gold.py:610-611`, this lane's `2b` addition), so a
consumer reads *0 of 5* or *2 of 5* directly and never has to interpret the word. The ambiguity the finding names
is real in the STRING and absent from the ROW. A future cell proposing to rename a served enum value should first
count the consumers that read the string rather than the pair -- and on today's evidence that set may be empty.

### 17g. `HVST-s-1` RAN AND THE CELL FAILED AT THE CUT, NOT AT THE WORLD -- the defect is the issuer's

**No vendor call was made.** `0.9.0_WK_AMGT_HARVST~19` executed the order exactly as written, recorded the
failure without retrying, and filed row `AMGT_HARVST-Z-W19-S1`. Every criterion produced its output with its
denominator; AC5 reads `outside_allowed []` with both delete methods raising on the positive control. **The
worker's conduct is not at issue. The ORDER is.**

**TWO DEFECTS, BOTH MINE, AND THE SECOND IS WORSE THAN THE FIRST.**

1. **The literal AC1 invocation crashes before any vendor call.** `__main__.py`'s `--security-json` handling
   wraps whatever the file parses to in a single-element list, so a multi-security ARRAY file breaks
   `Worker.run()` at `worker.py:330` with `TypeError: list indices must be integers or slices, not str`. I
   pointed the order at the six-name `securities.json` without exercising the flag against that file shape.

2. ⛔ **THE CELL COULD NOT HAVE PASSED EVEN IF sa HAD ANSWERED PERFECTLY.** `run --harvest-grammar` persists
   listing pages to a LOCAL sqlite/file outbox (`Worker._write_harvest_listings`, `worker.py:91-108`). **The S3
   bronze/silver listing writes happen only inside `HarvestUploader._run_listings`
   (`uploads.py:253-283`), reached only through the SEPARATE `upload-harvest` command.** My criteria measured S3
   surfaces (AC0/AC2 count `listing_hit` rows and bronze `news_listing` objects) against a command that does not
   write them. **AC2's delta was structurally pinned at +0 before the worker started.**

⛔ **THAT IS EXACTLY THE DEFECT CLASS THE ROUND-5 ANALYSIS RULED ON FOUR HOURS EARLIER** -- *"a criterion that
cannot pass the day it is written is a defect AT THE CUT, not a stretch goal"* -- and I wrote one into the very
round that ruling shaped, while quoting the ruling on the order's own face. **Knowing the rule and citing it in
the same document did not prevent committing it.**

⭐ **THE CHEAP CONTROL I SKIPPED, and it is the one this project keeps paying for:** the order names TWO planes
-- a command and an S3 surface -- and I never asked WHICH PLANE THE COMMAND WRITES. One read of
`uploads.py:253-283` before the cut, or one dry invocation of the flag against the actual file, would have
caught either defect. **COST: one read. NON-APPLICATION: a criterion whose invocation and whose measurement are
the same object.**

**WHAT THE ROUND ACTUALLY LEARNED, which is not nothing:** the capture and the S3 write are TWO commands, and
`upload-harvest` is the only path to the listing surfaces. `W10-S6`'s disarm note already said that command is
never offline-safe; what it did not say, and what this cell establishes, is that it is also **the only way any
listing row reaches S3 at all.** A corrected cell is `run --publishers sa --harvest-grammar` with a
SINGLE-security JSON, THEN `upload-harvest`, with AC2 measuring after the second.

### 17h. THE SECOND ATTEMPT (`~20`) REACHED THE CELL'S AUTHORIZATION CEILING -- the producer has NO BOUNDED-FETCH MODE, and that is an ANDREW CALL, not an amendment

**AMENDMENT 1 was correct and is not the blocker.** Slot `~20` ran the amended order to its end: AC0, AC1b,
AC2, AC3, AC4 and AC5 all PASS-by-output with their denominators, the proof-of-spec instance is VALID, and AC1
was correctly skipped as SUPERSEDED. **AC1a did not run, and the worker was right not to run it.** Row
`AMGT_HARVST-Z-W20-S1`, BLOCKING.

**WHAT THE WORKER FOUND:** the producer resolves its runtime root to the **worktree** root
(`publishers.py:22` `ROOT = Path(__file__).resolve().parents[2]`, config `runtime_root: .runtime/opal-data-harvest`).
A linked worktree has no `.runtime`, so `worker.py:152` `self.sessions.get(publisher)` finds no saved envelope and
falls through `auth.py:23-24` `saved or self.refresh(publisher)` into a **headed credentialed Chrome login** whose
bot wall is solved by a third-party vision model, in a `subprocess.run` with no timeout. That is a different and
larger act than this cell's ONE BOUNDED VENDOR ACT, so the cell stopped.

**THE ISSUER'S THREE READS, all made after the worker reported, each on a different instrument:**

1. **THE UPLOAD-ONLY PATH DOES NOT EXIST -- MEASURED, AND IT CORROBORATES `Z-W15-S1` ON A NEW INSTRUMENT.** The
   worker's own hypothesis was that the original 502 run's captured pages sit in the MAIN tree's outbox, invisible
   from the worktree. They do not. `.runtime/opal-data-harvest/progress.sqlite3` `harvest_listing_outbox` holds
   **2 rows TOTAL, both wsj, both `uploaded`; sa holds ZERO.** Beside it `harvest_raw_outbox` holds **sa 3
   `uploaded`, wsj 11** -- so sa's ARTICLES persisted and its LISTINGS did not, which is exactly what `Z-W15-S1`
   predicted from the code and is now measured on the OUTBOX rather than on the S3 surfaces. **Round 4's
   precondition ("no rebuild from held data exists for the other four") is re-confirmed on a second instrument.**
   The only path to an sa listing row is a FRESH capture.

2. **A SAVED ENVELOPE WOULD PREVENT THE LOGIN AT THE START -- `load()` HAS NO EXPIRY CHECK.**
   `SessionVault.load` (`storage.py:51-55`) tests `path.exists()` and decrypts; it does not read an expiry. So
   `get()` short-circuits on any existing `sa.dpapi`, and `.runtime/opal-data-harvest/secrets/sa.dpapi` exists
   (26,438 B, 2026-09-15). **Pointing `--runtime-root` at the main tree therefore does disarm the STARTUP login** --
   which is why option 1 in the row looked sufficient.

3. ⛔ **AND IT IS NOT SUFFICIENT, WHICH IS THE FINDING: THE ESCALATION IS ALSO MID-RUN, AND IT IS NOT SCOPED TO
   bbg/barrons.** `worker.py:274-293` has two recovery branches and they differ:
   - `VerificationRequired` -> `repair_verification`, but **guarded**: `if attempt or publisher not in {"bbg",
     "barrons"}: raise`. sa raises. Safe.
   - `AuthExpired` -> **`self.sessions.refresh(publisher)` on the first attempt, for ANY publisher including sa.**
     That is the same headed credentialed login, reached automatically from an ordinary fetch whose cookies the
     server has since expired.
   **So a ten-day-old session does not fail closed -- it fails INTO the login.** And no flag turns that off: a
   census for a bounded-fetch/no-refresh switch over `lib/opal_data_harvest/` returns **4 hits of 43 files, every
   one of them a `credentials_entered: False` telemetry field, and none a control.**

**THEREFORE THE CELL CANNOT BE EXECUTED WITHIN ITS OWN BOUND BY ANY AMENDMENT I CAN WRITE.** Whether the act stays
bounded depends on whether sa's saved cookies are still live server-side, **and that fact cannot be read without
making the call** -- the measurement and the hazard are the same act. `--runtime-root` buys the startup branch and
not the mid-run one, so offering it as "the fix" would be a bound that holds only on the lucky branch.

⭐ **THE SHAPE, and it is the one NEVER-1 states one level up:** I counted the WRITERS of the session state and
stopped at the entry point. **A recovery path is a second writer of the same state, and it runs on a branch the
happy path never shows you.** Reading `get()` alone certifies a login-free run that the `except` clause twelve
lines later can still perform. COST: one read of every `except` in the call path. NON-APPLICATION: a producer with
no recovery branch.

**ROUTED TO ANDREW AS ONE CARD, and the round holds there.** The question is not "may the pipeline call sa" --
that is settled and scripted. It is whether a **credentialed headed re-login to seekingalpha.com, with a
third-party vision model solving the bot wall**, is authorized as part of this retry. It is a different act from
the one round 6 was cut for, and `NEVER call an external vendor API without Andrew's explicit per-use word`
plus the moratorium on inferring wider scope both land on HIS word, not on mine. **No gate is being built and
nothing is being narrowed: the cell simply stops at the edge of what it was authorized to do.**

**STATE:** `HVST-s-1` stays OPEN at `pending`, round 6 does not close, and no L10 slug is cut -- an open order is
the honest carrier of a blocked act. The `~20` instance stands as filed.

## 18. ROUND 7 -- L5 DECOMPOSITION v1.6, over the round-6 analysis (`ledger/ROUND_ANALYSIS.round6.md`)

**The critical path is TWO CELLS DEEP and serial, and the analysis says so: cell 2's output is unreadable
until cell 1 lands.** Two further cells are independent of that path and run beside it.

### 18a. Rule 24 record -- the subtraction, from a PRINTED denominator

**Printed denominator: the analysis's enrichment list carries FIVE numbered items; two further cells were
ruled cuttable by the CTO at msg 25928 (@`9f0201abd2`) and are carried here because THIS SEAT TOLD THE CTO
they would land in the next issuance. 5 + 2 = SEVEN candidates.**

- Item 1, **Z-S28 disarm** -> **CELL `HVST-v-1`.** BLOCKING and it leads: everything else fires into a path
  that cannot reach silver.
- Item 2, **the bounded vendor act** -> **CELL `HVST-v-2`.** ⚠ **AND ITS SHAPE CHANGED BETWEEN THE ANALYSIS
  AND THIS CUT, which the cut must not paper over:** the analysis was written believing AC1a had never run.
  It ran at `02:17:52Z` under Andrew's SEPARATE per-use word, rc 0, `accepted: 5`, and **20 listing rows are
  already held in the local outbox**. So cell 2's first criterion needs NO vendor call at all -- it drains
  held pages. The fresh capture is its second criterion. Ledgered: `ledger/VENDOR_CALLS_2.0.0_SA_COO_Y.md`.
- Item 3, **the 8 ungraded judgment criteria** -> **NOT A CELL. A CONSTRAINT ON THE CUT.** L9 is the CVO's
  act and is never self-graded; what a decomposition controls is whether L9 has anything TO grade. Round 6
  gave it zero and had no plausibility oracle. **Round 7 carries a judgment criterion on the cell that can
  be wrong in a way no mechanical column shows** -- `v-2`, where a green delta over the wrong rows reads
  identical to a green delta over the right ones.
- Item 4, **the COO drain-end packet** -> **NOT A WORKER CELL. THE ISSUER'S OWN ARTIFACT**, produced at
  drain-end. Its absence is what bounded the slug's scope to the channel and the order; no worker can
  produce it, because it is a record OF the issuer's acts.
- Item 5, **the 3 carried channel rows** -> **NOT A CELL.** Disposition is the CVO's L9 act.
- **PLUS the timeline BUILD cell** (gate vacated as agent-made) -> **CELL `HVST-v-3`**, write surface
  disjoint from the sa path.
- **PLUS the ft/barrons DIAGNOSTIC** (authorization settled, what remains is diagnosis) -> **CELL
  `HVST-v-4`**, write surface disjoint.

⛔ **THE TWO CARRIED CELLS ARE NOT ON THE ANALYSIS'S LIST AND THAT IS STATED, NOT SMUGGLED.** The analysis is
the authoritative recut input and it names five items. `v-3` and `v-4` come from the CTO's own earlier
ruling, and this seat answered that ruling by saying both would land in the NEXT issuance -- this one.
Including them silently would be the COO widening a round; excluding them silently would be dropping a
commitment. **They are cut, they are named as additions, and they sit OFF the critical path.**

### 18b. THE CELLS, by WRITE SET

| cell | write set | risk | depends on |
|---|---|---|---|
| `HVST-v-1` | `lib/opal_data_harvest/` + its tests | LOCAL | -- |
| `HVST-v-2` | S3 bronze/silver `sa`; the local outbox; the vendor ledger | **WORLD** | `v-1` |
| `HVST-v-3` | the timeline build surface | LOCAL | -- |
| `HVST-v-4` | diagnostic evidence only, no producer change | **WORLD** (a live ft/barrons call) | -- |

**Fan-out: 3 chains, cap 8.** `v-1 -> v-2` serial; `v-3` and `v-4` independent. Derived from the dependency
graph above, not chosen.

### 18c. `HVST-v-1` -- make sa's listing pages reach silver

**The defect, already isolated (`Z-S28`):** sa's payload carries `themes` = `{}` on all 20 rows; arrow types
it `struct<>`; parquet refuses *"Cannot write struct type themes with no child field"*. **Emptiness, not
struct-ness** -- `links` (`struct<self: string>`) writes fine, and the isolating pair is in the row.

⛔ **THE FIX IS PUBLISHER-NEUTRAL OR IT IS NOT THE FIX.** Special-casing `themes`, or sa, leaves ft, barrons
and bbg to fail identically the first time one of them writes a listing row -- and **none of the three ever
has**, so the next failure is equally invisible. The cell coerces an EMPTY MAPPING to null wherever it
appears in a silver row, for every publisher.

**Its positive control is the whole point:** wsj's held payload must produce a BYTE-IDENTICAL row set and an
identical arrow schema before and after the change. A fix that quietly re-types a column wsj already writes
is a silver schema change wearing a bug fix's clothes.

### 18d. `HVST-v-2` -- drain what is held, then capture, then measure

**Criterion order is load-bearing and is the correction round 6 paid for:** drain the ALREADY-HELD pages
FIRST. They need no vendor call, they exercise `v-1` against real sa bytes, and if the fix is wrong the cell
learns it before spending a vendor act rather than after.

⛔ **THE VENDOR WORD IS SESSION-SCOPED AND EXPIRES SILENTLY.** Nothing refuses when it lapses; the seat
simply no longer holds what it believes it holds. **This cell runs while the word is live or it does not
run**, and a cell that cannot is a card to Andrew, never a queued order that quietly loses its
authorization.

⛔ **AND THE RUNTIME ROOT IS A GRANT THE ORDER MUST MAKE EXPLICITLY -- round 6 died on exactly this.** A
worker worktree has NO `.runtime`, so the producer finds no session vault and falls through to the headed
credentialed login. The order names `--runtime-root <main tree>/.runtime/opal-data-harvest` so the SAVED
envelope resolves. **If that envelope has expired, the cell STOPS with a BLOCKING row; it does not
re-authenticate.** Re-auth is a human act and is not this cell's to perform.

**Its JUDGMENT criterion (the CVO's, at L9):** are the listing rows that reached silver ABOUT the security
they are filed under? A mechanical delta counts rows; it cannot see rows counted against the wrong name,
and `v-2` is exactly where round 6 had no oracle.

### 18e. AMENDMENT AT THE CUT -- ROUND 7 IS TWO CELLS, NOT FOUR. `v-3` AND `v-4` MOVE TO ROUND 8

**This amends 18a/18b, written forty minutes earlier by this same seat, and the superseded text stands above
rather than being edited away.** The subtraction there is unchanged and still correct; what changes is which
of its cells this round CUTS.

**REASON 1 -- THE VENDOR WORD IS SESSION-SCOPED AND IT IS THE ONLY PERISHABLE THING IN THE ROUND.**
`v-1 -> v-2` is the critical path and `v-2` holds the only act that expires. `v-3` and `v-4` are independent
and lose nothing by waiting; the sa path loses its authorization if it waits. Cutting four orders delays the
two that are on a clock in order to start two that are not.

**REASON 2, AND IT IS THE ONE THAT WOULD HAVE BITTEN -- I HAVE NOT READ THE TIMELINE SPEC.** `v-3` is the
timeline BUILD cell. To cut it competently I need `SPEC_SECTION_timeline.md` at HEAD and the round-1 build
context, and I have read neither. ⛔ **TONIGHT THIS PROJECT PAID TWICE FOR CRITERIA WRITTEN AGAINST A SURFACE
THE ISSUER HAD NOT READ** -- `HVST-s-1` AC1 named a flag shape never exercised, and its AC2 measured an S3
surface the named command does not write (17g). **Cutting `v-3` now to honour a delivery promise would be
committing that same defect a third time, knowingly, in the same round that exists to clean up the second.**
A promise to cut a cell is not a promise to cut it badly.

**REASON 3 -- `v-4` IS A SECOND WORLD CELL AND IT WOULD SHARE THE LEDGER AND THE SESSION SURFACE WITH `v-2`.**
Two live vendor cells in one round, both writing vendor-ledger rows, both touching the device-local session
vault, is avoidable contention on the one surface whose failure mode is a silent credentialed login.

**WHAT IS OWED AND TO WHOM:** this seat told `1.0.0_SA_CTO~Z` (msg 25928 reply) that both cells would land in
the NEXT issuance. **They are not landing in it, and the CTO is told that in the issuance commit rather than
discovering it from a cell list.** Both are cut in round 8 off the round-7 analysis, `v-3` after this seat
reads the timeline spec.

**FAN-OUT, restated for what is actually cut: 1 chain, cap 8.** `v-1 -> v-2`, strictly serial. Cell 2's
output is unreadable until cell 1 lands, which is the analysis's own reasoning and not a choice made here.

### 18f. CELL ID COLLISION -- the round-7 cells were cut as `HVST-r-1..r-4` and those ids WERE ALREADY TAKEN

**`HVST-r-1` through `HVST-r-5` belong to an earlier round of this project** -- `r-1` is the timeline-spec
cell (`AMGT_HARVST.TO-HVST-r-1.timeline-spec-failed-call-state-and-error-envelope.md`), the very cell whose
BUILD the CTO vacated a gate over. Round 7's cells are renamed to the unused **`v`** series: `HVST-v-1`,
`HVST-v-2`, with the deferred pair as `HVST-v-3` and `HVST-v-4`. Sections 18a-18e above are read with that
substitution; the ids there were wrong when written.

⛔ **AND THE GATE PASSED THE COLLISION, WHICH IS THE PART TO KEEP.** `to-pipeline-gate` reported
*"1 owned cell(s) and 3 criterion reference(s) RESOLVE against ... (20 cell ids, index)"* for both orders --
**TRUE, and about the WRONG OBJECT.** `cell_refs="HVST-r-1"` resolved perfectly, against a cell cut in a
previous round. A reference check answers *does this id exist*, never *is this id YOURS*, and a reused id is
the one case where those two questions come apart. **A green resolve line is not an ownership check.**

⭐ **THE DISCRIMINATOR COSTS ONE COMMAND AND IT IS NOT A SEARCH FOR YOUR OWN ID -- IT IS A LISTING OF THE
DENOMINATOR:** `ls task-orders/ | cut -d. -f1 | sort -u` prints every id already spent (here: `h-1..h-10`,
`r-1..r-5`, `s-1`, `t-1`, `t-2`, `u-1`). Grepping for the id you intend to use is the wrong instrument --
finding it is exactly the outcome that should stop you, and a careless reader reads a hit as confirmation.
**Found only because a fresh worktree listed two files matching `TO-HVST-r-1*`.**

**COST:** one `ls` before naming a cell. **NON-APPLICATION:** the first round of a project, where no id is
spent yet.

## 19. ROUND 8 INPUT -- THE ARTICLE-ID DEDUPE IS ONE FLAG WE HAVE NEVER PASSED (Andrew-direct 2026-09-27)

**Andrew-direct:** *"we need a mechanism for article ID so we dont constantly pull same articles into database.
I believe the News pipeline has an existing solution for this."* **He is right that it exists. Nothing needs
building. It needs passing.**

### THE THREE LAYERS, and which were actually ON tonight

| layer | what it prevents | mechanism | state in tonight's runs |
|---|---|---|---|
| 1 | the BODY REQUEST for an article we hold | `--new-only` -> `config["new_only"]` | ⛔ **OFF -- never passed** |
| 2 | a duplicate bronze WRITE | `C-DEDUPE-BY-KEY` in `put_listing_bronze` | ON, structural, always |
| 3 | the VENDOR FETCH of a listing page we hold | `harvest_dedupe` | **ON already** |

⛔ **CORRECTION TO THIS SEAT'S OWN FIRST READING.** I reported that "none of it is on in our runs" and cited
`publishers.py:228` (`self.harvest_dedupe = False`) as evidence. **That line is only the pre-wiring default.**
`worker.py:176-178` derives the live value -- `harvest_on = self.config.get("harvest_grammar", False) and
self.harvest_client is not None`, then `client.harvest_dedupe = harvest_on` -- and `--harvest-grammar`
(`__main__.py:180`) was passed on EVERY invocation tonight. **So layer 3 was on the whole time, and reading a
constructor default as the runtime state was the error.** A default is not a state.

### LAYER 1 IS THE REAL GAP AND IT IS ARTICLE-ID SHAPED, which is exactly what he asked for

`worker.py:138-158`, when `new_only` is set:
- reads `SELECT article_id, path FROM articles WHERE publisher=? AND security_key=?`,
- builds `known_ids` **AND** `known_urls` (a URL match catches a re-issued id),
- hands both to the client, where `publishers.py:400` skips on `identity in self.known_ids` and `:461` on
  `identity in known_ids or item.get("url") in known_urls`,
- and reports `mode: new_only` with `previously_stored: <n>` on the run artifact.

**MEASURED, so it is not an empty mechanism:** the local `articles` table holds **121 rows** --
sa 46 / wsj 26 / bbg 19 / barrons 15 / ft 15, across 3-5 securities each. Every run tonight reported
`mode: qualification` and `previously_stored: 0`, so **46 already-stored sa articles were re-offered to the
body path instead of being skipped.**

### WHAT ROUND 8's CAPTURE CELL CARRIES

**`--new-only` on every `run` invocation**, with the criterion printing `previously_stored` and `mode` from the
run artifact -- a dedupe that cannot be seen in the evidence is a dedupe nobody can grade.

⚠ **AND THE BOUND ON LAYER 1, stated so it is not oversold: `known_ids` come from DEVICE-LOCAL sqlite, keyed
`(publisher, security_key)`.** It dedupes against THIS device's history, not against S3. A fresh machine, or a
worker worktree without the main tree's `.runtime`, starts blind -- which is the same locality that killed
round 6 (`Z-W19-S1`). Layer 3 is the one that survives a device change, because it reads bronze. **They are
complementary and the cell should pass both rather than treat either as the answer.**

**NON-APPLICATION:** a first-ever capture for a security has nothing stored, so layer 1 is inert there by
construction -- which is correct, not a defect.


## 20. ROUND 8 -- L5 DECOMPOSITION v1.7, over the round-7 analysis (`ledger/ROUND_ANALYSIS.round7.md` @cb2ba00a33)

**Issuer `2.0.0_SA_COO~Y`, 2026-09-28 ~00:3xZ.** Round 7 CLOSED, all nine FWD NOT REALIZED. The analysis's
section 5 is the enrichment list and its ORDER is adopted as given: **repair before capture.**

### 20.0 THE CELL-ID DENOMINATOR, read before any id is named (decomp 18f, and it bit twice in round 7)

`ls task-orders/ | cut -d. -f2 | sort -u` -> spent series letters **h, r, s, t, u, v** (21 orders). **Round 8 is
the `w` series**, `HVST-w-1` upward. The discriminator is the SPENT set, never a grep for the id I intend to
use -- a grep for `HVST-w-1` returns nothing whether or not `w` is free, and that is how `HVST-r-1` collided.

### 20.1 WHAT IS ISSUED AS AN ORDER, AND WHAT IS CARDED -- the vendor rule decides, not my preference

⛔ **The analysis binds this and I am not reading around it:** *"Every WORLD cell in round 8 needs a live
per-use word from Andrew before it fires; a cell without one is a card, not a queued order."* Round 6's egress
word was scoped to "this session" and **has lapsed**; the 2026-09-26 22:15Z word went to `0.7.0_AE_CloudOps~I`
for the Black Diamond producer and **does not travel**.

| # | cell | class | round-8 disposition |
|---|---|---|---|
| 1 | REPAIR -- `silver_append` collision, 3 red tests, `--harvest-grammar` help text | **LOCAL** | **ISSUED** as `HVST-w-1` |
| 2 | CAPTURE -- `--new-only` + `--harvest-grammar`, timeout-tolerant batch | WORLD | **CARDED** at Andrew, text drafted |
| 3 | `w-3` timeline BUILD | **LOCAL** | **ISSUED** as `HVST-w-3` (see 20.4 -- its scope is CUT DOWN by a measurement) |
| 4 | ft/barrons DIAGNOSTIC, carrying `Z-S31` | WORLD | **CARDED** at Andrew |
| 5 | bbg DIAGNOSTIC, carrying `Z-S32` | WORLD | **CARDED** at Andrew |
| 6 | the 16 carried backlog rows, re-measured | -- | **ISSUER ACT**, mine, not a cell |

**INTERPRETATION STATED SO THE CTO CAN CORRECT IT RATHER THAN DISCOVER IT:** I read "a card, not a queued
order" as *do not issue it to a worker*, so cells 2/4/5 are DECLARED here with their criteria drafted and are
NOT dispatched. On Andrew's per-use word each issues immediately without re-deriving anything. **The
alternative reading -- issue them with a non-firing precondition clause -- I rejected**, because a `pending`
order a worker can pick up is exactly a queued order, and the sentence forbids that.

### 20.2 FAN-OUT, derived and not chosen

`1 -> 2` is **serial** (the repair lands on the very path the capture writes). `3` is **independent and LOCAL**.
Cells **2, 4 and 5 are all WORLD and share two single surfaces** -- the vendor ledger and the device-local
session vault -- so **they serialise**, per this decomposition's own reason 3 (18e): two live vendor cells in one
round contend on the one surface whose failure mode is a silent credentialed login. **Issued fan-out this round
is therefore 2** (`w-1`, `w-3`), both independent of each other, well inside the cap of 8. Each build order
carries **at most three mechanical criteria**.

### 20.3 CELL `HVST-w-1` -- THE REPAIR (LOCAL). It lands before any capture because it owns the capture's write path

Three mechanical criteria, no more:

1. **`Z-W9-S1`'s listings half.** `silver_append` keys on a SECOND-PRECISION `run_stamp` with
   `IfNoneMatch="*"`, so **two writes inside one second collide**. ARMED on exactly the path a capture cell
   writes. The criterion exercises the collision (two appends in one second) and shows it no longer drops a
   write.
2. **The 3 red tests (`Z-W21-S2`).** The suite was ALREADY red at HEAD before round 7 touched anything -- 3
   failed / 160 passed -- and **one of the three is `WinError 183`, a filesystem-state failure, not a logic
   failure.** ⚠ The criterion states the count BEFORE and AFTER and names each test; a repair that fixes two
   and leaves the WinError is reported as such, not rounded to green.
3. **`Z-S27`, the `--harvest-grammar` help text** says "writes" for a flag that writes nothing to S3. Read
   alone it asserts the exact belief that produced round 6's failure. A text fix, and the criterion prints the
   new string.

**Cut rule applied:** the criterion asking for a passing test BY NAME uses `pytest -rA` or `-v`, **never `-q`**
(`Z-W21-S1`: `-q` never prints a passing test's nodeid, which made a round-7 criterion unsatisfiable by
construction).

### 20.4 CELL `HVST-w-3` -- THE TIMELINE BUILD (LOCAL), AND ITS SCOPE IS CUT DOWN BY A MEASUREMENT I TOOK FIRST

**The precondition is discharged: I read `SPEC_SECTION_timeline.md` at HEAD** (18,196 bytes,
`deliverables/0.9.0_WK_AMGT_HARVST~8/`), which is why the following two facts are in the cut instead of in a
round-9 post-mortem.

> ⛔ **FALSE, AND CORRECTED BY MEASUREMENT 2026-09-28 (`HVST-x-2` AC1, re-verified by the issuer):**
> `chatter_event` holds **12 rows across 7 securities, 4 of them Lenovo's own**, and `publishers_distinct`
> reaches **3**. The landed universe is **191** securities, not 89, with **55** carrying a day where
> `articles_total > 0`. **So FWD-6 was exercisable all along, and FWD-5 is now EXERCISED on Lenovo**
> (267 of 267 dense days, no gap, strongest-first with 0 sort violations).
>
> **THE ERROR SHAPE, kept because it is the reusable part:** `EVENT_MIN_PUBLISHERS = 2` WAS read at the
> bytes; *"only `sa` has landed listing rows"* was INHERITED from round 7's measurement of a different
> population at an older vintage -- and `chatter_event` itself was **never read**. Presenting that pair with
> the measured constant's authority is how an inherited number acquires standing it never earned.
> **A conclusion is only as measured as its weakest premise.** Row `AMGT_HARVST-Z-W27-S1`.

⛔ **FWD-6 IS UNSATISFIABLE BY CONSTRUCTION TODAY, AND A CRITERION FOR IT WOULD HAVE PASSED VACUOUSLY.**
Measured at the bytes: `publication_gold.EVENT_MIN_PUBLISHERS = 2`, `EVENT_MIN_ARTICLES = 2`, qualifying tiers
`('A','B')`. **Only `sa` has landed listing rows** (round 7: sa 0 -> 40; bbg in hard refusal since 09-15;
ft/wsj/barrons unexercised in gold). With ONE publisher landed, `publishers_distinct >= 2` is structurally
unreachable, so **`chatter_event` can hold ZERO rows for every security, Lenovo included.** The spec's own
acceptance asks the build to "show at least the event runs `chatter_event` holds for Lenovo" -- against an
empty set that criterion **PASSES while proving nothing**, and the spec even blesses the empty render as "the
correct, honest state." **A green column over an empty denominator is the failure mode this project has paid
for before.** So FWD-6 is NOT a criterion of `w-3`; it is named here as BLOCKED ON A SECOND PUBLISHER, with
its cause printed.

**What `w-3` IS graded on, all three checkable without rich data** -- the spec's substance is its HONEST-STATE
discipline, and that is testable on constructed inputs:
1. **The three API routes' SHAPE** (`timeline`, `timeline/day/{date}`, `timeline/event/{first_day}`) serving
   exactly the stored fields section 5 enumerates, with `breakout_ratio`/`z_score` computed AT SERVE TIME and
   never stored (`C-HV-ABSOLUTE-ONLY`).
2. **The error envelope and the failed-call state.** `{"error": true, "error_code", "message"}` is NEVER
   rendered as data, never merged into `series`/`events`/`articles`, and never degraded to an empty array --
   because an empty array is the honest "nothing in range" state and must not be reachable from a failure.
   **This is the one the spec says was a real graduated defect on this page's other panels (`Z-S227`/`C-S400`).**
3. **Quiet-COMPLETE vs PARTIAL vs DENIED never share an encoding** (section 2/6), on the line AND in the
   dissection.

⭐ **ONE OF THE SPEC'S OWN OPEN CALLS IS ALREADY ANSWERED BY THE CODE and the cell must not re-decide it:**
section 7 leaves open "whether the build cell mints a stable synthetic `event_id`". **`publication_gold._event_id`
already exists** -- `sha256("security_key|first_day|last_day")`. So the event route keys off that, not off a new
id and not off `first_day` alone. A build cell inventing a second id scheme would have been a silent
divergence from the producer.

### 20.5 THE THREE CARDED WORLD CELLS -- drafted, not dispatched

- **`w-2` CAPTURE.** `--new-only` AND `--harvest-grammar` on every `run`; the criterion PRINTS `mode` and
  `previously_stored` from the run artifact, because **a dedupe nobody can see in the evidence is a dedupe
  nobody can grade** (121 rows are held and every round-7 run read `previously_stored: 0`). The batch tolerates
  ONE timeout without cooling the publisher (`Z-W22-S2`: one slow body cost 7 of 8 jobs). **Carries round 8's
  JUDGMENT criterion** (below).
- **`w-4` ft/barrons DIAGNOSTIC**, carrying `Z-S31`: ft holds 15 rows under 14 DISTINCT `article_id`s while
  every other publisher is exactly 1:1, and `articles` has no unique constraint. **The question the round-7
  measurement could not answer because it did not group by `security_key`:** does any gold count double-count
  it? Diagnostic only, no producer change.
- **`w-5` bbg DIAGNOSTIC**, carrying `Z-S32`: why `search/query` refuses (9 consecutive 403s since
  2026-09-15T04:47Z) while `/user-info` reads 200 on 12 of 12. **FWD-1's five-publisher population is
  unreachable until this is explained, so no bbg CAPTURE is plannable before it.** ⭐ **New input the diagnostic
  starts from, found tonight in 12-day-unread base-addressed mail:** Andrew described this exact challenge on
  2026-09-14 -- *"the press and hold starts draining and you have to wait and un-press for a moment, and then
  press again after its gone down somewhat"* -- and **the producer already implements precisely that** (solver
  logs `drain -> release -> partial fall -> re-press`). It fails with `recoveries=0`, **meaning the drain never
  partially fell, so the technique's own precondition was never met.** That is where the diagnostic starts, not
  from scratch.

### 20.6 THE JUDGMENT CRITERION -- round 8 carries one again, and the analysis named where

**On `w-2`, the capture cell** (per the analysis: the cell where a green mechanical column can hide a wrong
result). **The question:** are the rows `--new-only` skipped truly already held -- the SAME article -- or did a
url/id mismatch skip a NEW one? A mechanical criterion counts skips; only judgment can say the skips were
right. Graded by `3.0.0_SA_CVO` at L9, never self-graded, and **presented with its output and no verdict.**

### 20.7 CUT RULES CARRIED, from the analysis (rules, not cells)

1. A criterion asking for a passing test by name uses `-rA` or `-v`, **never `-q`** (`Z-W21-S1`).
2. **A placeholder whose value contains whitespace is EXPANDED to a literal and `<placeholders>NONE</placeholders>`
   is declared** (`Z-W22-S6`; `1.0.0_SA_CTO~Z` ruling 20260927T220426Z -- `(\S+)` is a deliberate tamper guard,
   not a defect, so the order adapts and the tool does not).
3. `ls task-orders/ | cut -d. -f1 | sort -u` before naming a cell (20.0 above).
4. Worker scripts go in `deliverables/0.9.0_WK_AMGT_HARVST~<n>/scripts/`, **never `.scratch/`** -- `.scratch/`
   does not survive the drain and an issuer structurally cannot relocate a worker's files afterwards.
5. **The spawn face and the order FILE are ONE edit, not two.** Round 7 cost two rows (`Z-W22-S4`, `Z-W22-S5`)
   because I changed the face and not the file.

### 20.8 ITEM 6 -- THE ISSUER ACT, and one row of it is NOT this lane's to fix

The slug carried **16 of 28 rows without re-measuring them**, and the analysis adopts that as a stated limit
rather than absorbing it. **Re-measuring them is mine as `disarm_owner`, not a worker cell.** ⛔ **Exception,
named so it is not silently swept in: `Z-W11-S1` is `.tools/missions-tree-index.py`, a SHARED mechanism. It is
routed to the tool's owner and the route is RECORDED** -- and "recorded" means a route that exists, not a
sentence saying it was routed. Round 7 taught that one: I wrote "routed to the tool's owner" twice in committed
records while the row carried no `route` field at all.


## 21. ROUND 9 -- L5 DECOMPOSITION v1.8, over the CORRECTED round-8 analysis (`ledger/ROUND_ANALYSIS.round8.md` @1ae0fd36f6)

**Issuer `2.0.0_SA_COO~Y`, 2026-09-28 ~04:3xZ.** Cut on `1.0.0_SA_CTO~Z`'s go-ahead (042311Z) after
`0.0.0_AB_MSTR~Z`'s PARTIAL all-clear (041852Z): **commits resumed, pushes frozen to 05:00Z.** The purge never
ran -- `origin/CLOUD` unchanged at `9a5d538d35` with the pre-freeze tip still an ancestor.

⚠ **CUT AGAINST @1ae0fd36f6, NOT THE VERSION I READ AT 02:4xZ.** The analysis was corrected in place after I
disputed its finding 1, and cutting against the pre-correction bytes would have carried a diagnosis its own
author has struck. **The bytes were re-read at HEAD before this section was written.**

### 21.0 THE DENOMINATORS, read before any id is named

`ls task-orders/ | cut -d. -f2` -> spent series letters **h, r, s, t, u, v, w** (23 orders). **Round 9 is the
`x` series.** Worker slots: **MAX+1 over 25 -> `~26` and `~27`.** Never a grep for the id I intend, never a row
count -- both errors happened in round 7, on two different id spaces.

### 21.1 WHAT IS ISSUED, AND THE RULE THAT DECIDED IT

⛔ **The corrected rule from the round-8 analysis s.2, and it is binding on every recut from here:** *"the
round's judgment criterion sits on a cell that can issue without a pending Andrew word."* Round 8's L9 was
vacuous because the round-7 analysis put the only judgment criterion on a WORLD card. **Round 9's judgment
criterion therefore sits on `HVST-x-2`, a LOCAL cell.**

| # | cell | class | disposition |
|---|---|---|---|
| 1 | `HVST-x-1` -- second repair: the 2 red tests, the `publishers.py:672` guard, the flaky quarantine | **LOCAL** | **ISSUED** to `~26` |
| 2 | `HVST-x-2` -- timeline EXERCISE, **carrying the round's JUDGMENT criterion** | **LOCAL** | **ISSUED** to `~27` |
| 3 | `w-2`, `w-4`, `w-5` | WORLD | **CARDED at Andrew**, unchanged; each fires only on his live per-use word |
| 4 | the 16 carried rows | -- | **ISSUER act**, stated in the issuance commit (21.4) |

**Fan-out 2**, derived: `1` and `2` are independent and LOCAL. The three cards serialise on the vendor ledger
and the device-local session vault **when** they fire. Each order carries **at most three mechanical criteria**.

### 21.2 CELL `HVST-x-1` -- THE SECOND REPAIR. THREE ITEMS, AND ONE OF THEM IS NOT A TEST FIX

**The diagnosis is already done and committed** (`deliverables/2.0.0_SA_COO_Y/WHY_THE_RED_TESTS_ARE_STILL_RED_20260928.md`
@`9a5d538d35`), so this cell does not re-derive it. **It is TWO tests, not three** -- pytest counts SUBTEST
failures separately and `test_single_broken_dow_jones_article...` SUBFAILS twice.

1. **TEST B -- the test-double gap.** `publishers.py:672` does
   `session.get(base + "/client?legacy=false").json()` and `.json()` returns **None**, because that test's fake
   session has no handler for the auth-check URL while its siblings all provide one
   (`test_bronze_capture.py:285`/`:296`, `test_retrieval_provenance.py:239`). **`DowJones.check()` is behaving
   correctly; the DOUBLE is incomplete.**
2. ⛔ **THE `.json()` GUARD -- A PRODUCT CHANGE, NOT A TEST CHANGE, AND IT GETS ITS OWN CRITERION.**
   `:672` calls `.json()` unguarded, so a real non-JSON or empty body raises `AttributeError` **instead of the
   clean `AuthExpired` the method exists to raise** -- brittleness on a LIVE AUTH PATH. **Completing the double
   turns the test green and leaves this standing**, which is exactly why the analysis requires it shown
   DIRECTLY and not through the suite.
3. **TEST A -- QUARANTINE, not repair.** It alternated between `KeyError: 'bundle'` and
   `FileExistsError: [WinError 183]` across two identical runs. **A test that fails differently on identical
   input is not a regression baseline.** Quarantine with the reason named; **the diagnosis belongs to `w-4`'s
   scope** (same publisher, and `w-4` is carded), not here.

**The criterion bar from the analysis, adopted verbatim:** the suite's failed count is **ZERO or each remaining
failure is quarantined with a named reason.**

### 21.3 CELL `HVST-x-2` -- THE TIMELINE EXERCISE, and its FIRST act is a MEASUREMENT that may bound it

**This is the issuable cell the corrected rule requires, and it carries round 9's JUDGMENT criterion:** *are
the events shown the real coverage bursts?* A mechanical criterion counts spans; only judgment says the spans
mean something. Graded by `3.0.0_SA_CVO` at L9, **presented with its output and no verdict.**

> ⛔ **FALSE, AND CORRECTED BY MEASUREMENT 2026-09-28 (`HVST-x-2` AC1, re-verified by the issuer):**
> `chatter_event` holds **12 rows across 7 securities, 4 of them Lenovo's own**, and `publishers_distinct`
> reaches **3**. The landed universe is **191** securities, not 89, with **55** carrying a day where
> `articles_total > 0`. **So FWD-6 was exercisable all along, and FWD-5 is now EXERCISED on Lenovo**
> (267 of 267 dense days, no gap, strongest-first with 0 sort violations).
>
> **THE ERROR SHAPE, kept because it is the reusable part:** `EVENT_MIN_PUBLISHERS = 2` WAS read at the
> bytes; *"only `sa` has landed listing rows"* was INHERITED from round 7's measurement of a different
> population at an older vintage -- and `chatter_event` itself was **never read**. Presenting that pair with
> the measured constant's authority is how an inherited number acquires standing it never earned.
> **A conclusion is only as measured as its weakest premise.** Row `AMGT_HARVST-Z-W27-S1`.

⚠ **THE BOUND ROUND 8 ALREADY MEASURED, carried forward so this cell does not re-learn it:** `chatter_event`
can hold **ZERO rows for every security** while only `sa` has landed listing rows
(`EVENT_MIN_PUBLISHERS = 2`). **So FWD-6's arm of this exercise may be empty by construction, and an empty
result is NOT a pass** -- the cell's first act is to print `chatter_daily`/`chatter_event` row counts for the
validation security **and say which arm is exercisable before exercising either.**

⭐ **AND THE ONE MEASUREMENT ROUND 8 DECLINED TO GUESS AT IS THIS CELL'S TO TAKE:** round 7 measured "1 of 89
securities with a non-empty span" and **never named which security.** FWD-5 needs a day with
`articles_total > 0`. **The cell names that security from a read rather than assuming it is Lenovo** -- and if
it is not `992_HK_Equity`, the spec's acceptance security and the only exercisable one differ, which is itself
the finding.

### 21.4 ITEM 6 -- THE 16 CARRIED ROWS, and what I state rather than what I claim

The round-7 analysis adopted the slug's "16 of 28 not re-measured" as a stated limit; the round-8 analysis says
**this round's issuance commit states the 16 re-measured OR states why not.** Measured at HEAD before this cut:
**37 ARMED rows carry `2.0.0_SA_COO~Y` as `disarm_owner`**, which is a larger set than the slug's 16 and is not
the same population -- the slug's 16 is a subset of the channel's ARMED set at ITS vintage.

⛔ **REMEDIATION ROWS ARE NOT MINE TO WRITE.** CLAUDE.md section 2 and `surprise-row-gate.py:111` split it: the
`disarm_owner` ACTS and files evidence, **`3.0.0_SA_CVO` writes the clock.** The round-8 analysis briefly said
otherwise and **its author corrected it** at @1ae0fd36f6. So item 6 is discharged as EVIDENCE, twice ferried to
`3.0.0_SA_CVO~O` (0152Z, 0228Z), not as rows I mint.

### 21.5 CUT RULES CARRIED -- s.14x now covers the ones round 8 cost me

s.14x's three order-writing clauses bind this cut: **the instance FILENAME is the order's filename stem**,
**`to_id` names that same stem**, and **every criterion's invocation is RUN ONCE by the issuer before the cut**
because escaping can make a recorded invocation align while being unrunnable. Plus: `-rA` never `-q`
(`Z-W21-S1`); a whitespace-bearing placeholder is expanded and `NONE` declared (`Z-W22-S6`); scripts in the
worker's own `deliverables/<serial>/scripts/`, never `.scratch/`; and **the spawn face and the order FILE are
ONE edit** (`Z-W22-S4`/`S5`).


## 22. ROUND 10 -- L5 DECOMPOSITION v1.9, over the round-9 analysis (`ledger/ROUND_ANALYSIS.round9.md` @f330f1a2e2) + PRD v0.3

**Issuer `2.0.0_SA_COO~Y`, 2026-09-28 ~07:1xZ.** Three cells, all LOCAL, all issuable.

### 22.0 DENOMINATORS

Spent series letters **h, r, s, t, u, v, w, x** (25 orders) -> **round 10 is the `y` series.** Worker slots MAX+1
over 27 -> **`~28`, `~29`, `~30`.**

### 22.1 CELL 1's GATE WAS VERIFIED BY HASH, NOT BY THE STATUS LINE

The round-9 analysis gated cell 1 on the v0.3 ratified half being re-signed. ⛔ **`prd-signoff.py status` is NOT
the oracle for that and said so misleadingly:** it printed `ratified-text SIGNED ... current` while the stored
`half_hash` (`fa4257b6...`, `3.0.0_SA_CVO~Z`, v0.2) **differed from** the library's computed
`half_hashes()['ratified-text']` (`43375644...`). **Routed to `1.0.0_SA_CTO~Z`, which answered that the binding is
to the ENDPOINT hash BY DESIGN (v3.19 + the 2026-09-24 proportionate sign-off) and the REPORT was the defect --
fixed @`ea81ad7be3`, now printing "current by ENDPOINT hash; this half's text CHANGED since signed".** Both my
proposed causes were wrong; the observation was right.

**THE GATE IS NOW GENUINELY CLEAR, measured:** `prd/signoff/3.0.0_SA_CVO~O.json` exists, `prd_version v0.3`, pin
`5e05cb1d3c`, and its `half_hash` **43375644... MATCHES the computed current hash.** Cell 1 may be cut.

### 22.2 NEVER-1 DOES NOT FIRE, and the zero carries its cause

The analysis required: *"Before the rebuild, list every reader of `chatter_event` / `event_id`; if any is served,
the rebuild moves served output and carries its never-widen pair."* **The rebuild's diff is NOT delta-zero**
(12 -> 8 events, plus 2 spans narrowing so their `event_id` changes), so this mattered.

**MEASURED: no served surface reads `chatter_event`.** `comp-find 'chatter_event' portal infra/aws data` ->
**0 hits across 10,085 files scanned.** ⚠ **The zero's own bounds, stated rather than swallowed:** 1 file
unreadable, 1,869 binary and 32,708 ephemeral-floor files were NOT searched, so the zero does not cover those.
The only first-party readers are `publication_gold.py` (which **writes** it) and `timeline_api.py`, which is
**pure -- the caller supplies the loader** -- and the page that would serve it is **cell 3, not yet built.**
**So NEVER-1's never-widen pair does NOT fire this round.** ⛔ **It WILL fire the round after cell 3 ships**, and
that is written here so the next issuer does not re-derive it.

⚠ **AND `event_id` IS THE WRONG TERM TO CENSUS ON:** it returns 408 hits across `portal`/`infra`/`data` --
`close_event_id` in schwab silver, the OpenAI realtime SDK, globgrph -- **none of them this table.** The term
that answers the question is `chatter_event`. A census on the generic name would have manufactured a served
reader that does not exist.

### 22.3 THE THREE CELLS

| id | cell | class | slot |
|---|---|---|---|
| `HVST-y-1` | **re-derive the events** under the amended `C-HV-EVENT-SPINE` (publishers counted over tier-A only) | LOCAL | `~28` |
| `HVST-y-2` | **FWD-4** -- the strength grade re-derived from stored text and matched | LOCAL | `~29` |
| `HVST-y-3` | **the timeline PAGE** on the company view, over `w-3`'s API, **carrying the round's JUDGMENT criterion** | LOCAL | `~30` |

**`y-1`'s expected diff is NAMED, not discovered** (the CVO measured it at daily grain): **12 -> 8 events**, the
**4 spurious ones absent**, and **2 spans narrowing so their `event_id` MOVES** -- `BA` 09-07..08 -> 09-08, `HD`
08-17..20 -> 08-18. Plus `C-HV-GOLD-REBUILDABLE`: a rebuild from the same silver reproduces identical rows.
⭐ **Naming the `event_id` moves in the criterion matters because `_event_id` is `sha256(security_key|first_day|last_day)`**
-- a narrowed span is a NEW id, not an edited row, and a criterion that counted only "8 events" would pass while
silently orphaning two ids.

**`y-3` is the round's JUDGMENT cell** (round-8 rule: the judgment criterion sits on a cell issuable without a
pending Andrew word). It renders and **READS the screenshot** (`/frontend-dev`), **dev port 5174 ONLY**
(Andrew-direct 2026-09-24). ⚠ **It touches a PRODUCT file, so it is NOT the author-lands-on-DEV case** -- the CTO
reviews it. The cell builds; it does not push PROD.

**Fan-out 3**, derived: all three are LOCAL and independent to BUILD. `y-3` grades after `y-1` and `y-2` land,
which is a grading order, not a dispatch dependency.

### 22.4 ITEM 6 -- RESOLVED AFTER THREE CARRIES, AND THE FIGURE WAS WRONG

The analysis says the round-10 issuance states the 16 rows re-measured **or states in one line why not.** ⛔ **It
is not 16, and it is not one population.** Measured live from `surprise-channel/remediations/REMEDIATION_v1.md`
(40 rows, parsed as JSON rather than read off a summary line):

| | |
|---|---|
| total rows | **40** |
| `hazard_standing` ARMED | **28** -- this IS the "28" in "16 of 28" |
| whose own text says NOT RE-MEASURED (all 40) | **20** |
| **ARMED *and* not-re-measured** | **14** -- the apples-to-apples figure, **not 16** |

**AND THE 14 SPLIT IN TWO, BY THEIR OWN `remedy` TEXT:**
- **6 rows** -- *"Executed before round 7 and recorded by the disarm owner: ..."* (`Z-S10`, `Z-S4`, `Z-W10-S2`,
  `Z-W10-S6`, `Z-W13-S1`, `Z-W15-S1`). **These carry a recorded execution; what they lack is a CLOCK, which is
  `3.0.0_SA_CVO`'s to write, not a re-measurement.**
- **8 rows** -- *"Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm
  record found for this row in the channel"* (`Z-S11`, `Z-S23`, `Z-S3`, `Z-S5`, `Z-W10-S3`, `Z-W10-S8`,
  `Z-W14-S2`, `Z-W8-S2`). **These are the genuine backlog.**

**WHY IT WAS CARRIED THREE TIMES: "the 16" is an undifferentiated count, and six of its members needed nothing
from me.** Asking for "the 16 re-measured" as an issuance footnote asked for one act over two populations with
different owners. **The keepable form is the banked one: N items is not N CAUSES -- print the signature
distribution before accepting a backlog figure.** The **8** are named above and are the real work; re-measuring
claims spanning rounds 1-6 is **cell-sized, not an issuance line**, and it is carried as round 11's candidate
with its members enumerated so the next issuer inherits a list rather than a number.


## 23. ROUND 11 -- L5 DECOMPOSITION v2.0, over the round-10 analysis (`ledger/ROUND_ANALYSIS.round10.md` @3b9cd352b8, corrected in place)

**Issuer `2.0.0_SA_COO~Y`, 2026-09-28 ~11:3xZ.** Series **`z`** (spent: h, r, s, t, u, v, w, x, y over 28 orders).
Slots MAX+1 over 30 -> **`~31`, `~32`, `~33`**.

### 23.1 THE NEVER-WIDEN PAIR IS COMPLETE, and the CTO's read strengthened my half

**COO half @`7f9df49098`; CTO half @`9fddce21db`.** Its signing check confirmed the mechanism my forward-only
rollback rests on: **`_latest_gold_snapshot_rows` reads the ONE newest part by `(date, key)`, never a union, so a
later snapshot wins even on the same day.** That is the property that makes "restore by addition" sound rather
than hopeful. **Cell 1 may issue.**

### 23.2 ⛔ THE CTO'S FINDING WHILE SIGNING REFRAMES ROUND 10, AND THE DEFECT IS MINE

**There is NO SERVED ROUTE.** The panel calls `/api/scoped/amgt/security/<key>/timeline` and
`/timeline/day/<date>`; **`lib/research/api/scoped_amgt.py` has ZERO occurrences of `timeline`** (verified by this
seat: 0 hits over 1 file), and every `get_timeline*` reference in the estate is its own definition or a
test/proof script.

⛔ **SO `HVST-y-3` RENDERED AGAINST STUBS, AND MY AC1 COULD NOT TELL.** I required a render AND a read of the
screenshot -- which the worker did faithfully -- but **never required the data to arrive by the path a user
traverses.** **A RENDER CRITERION MUST NAME ITS DATA SOURCE, OR IT CERTIFIES THE COMPONENT AND NOT THE PATH.**
COST: one line in the criterion naming the route, and one read of the route's file at cut time.
NON-APPLICATION: a component whose contract is explicitly fixture-only.

⚠ **It also softens my own never-widen half**, and I would rather say so than let it read stronger than it is: I
wrote that readers "resolve to 8 events." True of the GOLD LOADERS; **there is no served reader at all, so the
rebuild moves nothing user-visible today.** The blast radius (one key) stands; the word "SERVED" was inherited
from the analysis and overstated. **Both halves are signed anyway, which is the conservative outcome.**

**Consequence: the CTO added NEW CELL 0** -- wire both routes in `scoped_amgt.py` with real newest-snapshot
loaders, authorised by it as CTO of both projects -- **and the portal push waits for it.**

### 23.3 THE CELLS

| id | cell | class | slot |
|---|---|---|---|
| `HVST-z-0` | **wire the two timeline routes** in `scoped_amgt.py` over real newest-snapshot loaders | LOCAL | `~31` |
| `HVST-z-1` | **rebuild `chatter_event` gold** under the amended rule, **never-widen pair SIGNED**, carrying the round's **JUDGMENT** criterion | **SERVED** | `~32` |
| `HVST-z-2` | **FWD-4's FIELD census** -- the DONE WHEN clause `y-2` did not exercise | LOCAL | `~33` |
| -- | FWD-5 on the served page | waits on **Andrew's word** for the DEV merge-then-push, then the deploy |
| -- | FWD-7, the chatter rank from the graded table | follows `z-2` |
| -- | `w-2`, `w-4`, `w-5` | **at Andrew**, unchanged |

⭐ **`z-2` EXISTS BECAUSE THE CTO READ FWD-4's DONE WHEN AND I DID NOT.** Its two clauses are (i) every
(article, company) pair CARRIES headline / opening / count / share / co-mentioned companies, and (ii) the grade is
re-derived and matches. **`y-2` exercised (ii) beautifully -- 263 of 263 -- and (i) was never measured.** I read
the grade MECHANISM (`assign_tier`) and not the OUTCOME's own definition. **Same shape as 23.2: verification aimed
at the interesting half.**

**Fan-out 3**, all issuable now; `z-1`'s judgment grades on the served plane AFTER `z-0` lands, which is a grading
order, not a dispatch dependency.

### 23.4 ITEM 6 -- CLOSED AFTER FOUR CARRIES, AND THE ANSWER IS THAT IT IS NOT A BACKLOG OF 8

The 8 genuinely-open rows were enumerated in `s.22.4` and are now **re-measured by reading what each asserts**.
⛔ **They are not 8 independent items. At least two are DEFECT CLASSES that recurred THIS SESSION because the rows
were filed and carried instead of disarmed:**

**CLASS A -- the dotted-string patch target that silently no-ops.**
`Z-W10-S3` (round 2: `monkeypatch.setattr("lib.opal_data_harvest.publishers...")` failed to intercept the real
class) and `Z-W14-S2` (its "NEW variant", an absolute `from lib...auth import SessionManager`) **are the same
defect `0.9.0_WK_AMGT_HARVST~28` filed AGAIN in round 10 as `Z-W26-S1`.** ⭐ **THREE FILINGS OF ONE CLASS ACROSS
EIGHT ROUNDS, each recorded as new.** **STILL LIVE, measured:** 8 dotted-string patch/setattr targets across 5
files -- and **it is broader than this project**, reaching `lib/research/posture/tests/` (4 sites),
`lib/research/api/tests/` and `lib/opal_data_harvest/test_verification.py:18`. The CTO already routed `Z-W26-S1`
as a repo-wide audit; **`Z-W10-S3` and `Z-W14-S2` are the same route and should ride it, not sit here.**

**CLASS B -- alignment certifies AGREEMENT, never RUNNABILITY.**
`Z-S11`, open since round 2, states it exactly: *"when BOTH carry the same unrunnable text it PASSES."*
⛔ **That is precisely what happened to me in round 10 with `y-3`'s AC3** -- order and instance both carried a
submodule pathspec that returns empty, and alignment passed 3/3. **A row filed eight rounds ago predicted this
session's defect and nobody acted on it, including me, and I had read the channel repeatedly.**

**THE FOUR SINGLETONS** stay singletons and keep their claims: `Z-S3` (a verdict sentence whose subject is PATHS
while its evidence population is 14 bronze objects), `Z-S5` (the amended spec closes one half of a judgment
criterion and not the C-S400 half), `Z-S23` (a census contaminated by its own output -- the seat wrote its result
into the channel the census reads), `Z-W8-S2` (the checker's coverage frame returning rc=1 on a correctly-built
instance), `Z-W10-S8` (the WSJ extractor pulling the whole `__NEXT_DATA__` blob into silver).

⛔ **THE KEEPABLE FORM, and it is why this was carried four times: A BACKLOG COUNT HIDES A DEFECT CLASS. "16
rows", then 14, then 8 -- every re-count asked "how many" and none asked "how many DISTINCT".** The estate
rediscovered Class A three times and Class B once because a row that is filed, carried and never grouped reads as
history rather than as a live hazard. **COST: group a backlog by its mechanism before quoting its size.**
**NON-APPLICATION: a backlog whose members are already known to be independent.**
### 23.5 AMENDMENT -- A FOURTH CELL: `HVST-z-3`, THE PATCH-TARGET AUDIT (ruled MINE)

**`1.0.0_SA_CTO~Z` ruling 20260928T114032Z, answering my route:** *"Folded: one class, one audit, one cell. This
is the owner I said I would name."* **I cut it. LOCAL. Slot `~34`.**

⭐ **IT AUTHORISES CROSS-PROJECT PATHS FOR THIS CELL ONLY** -- `lib/research/posture/tests/test_posture.py` (POSN)
and `lib/research/api/tests/test_scoped_amgt.py` (AMGT_RESAPP), as CTO of all three site-Z projects, plus this
project's three (`test_retrieval_provenance.py`, `test_verification.py`, `test_worker.py`). **5 files, the 8 sites
I measured.**

**Its three criteria are the CTO's, ADOPTED VERBATIM rather than paraphrased** -- a paraphrased criterion silently
redirects its only oracle:
1. **Per site a NEGATIVE CONTROL** proving the patch now takes effect -- the patched name, **read through the
   module object the CODE UNDER TEST uses**, is the mock. 8 sites printed as before/after pairs.
2. **Each touched suite passes**, pass count printed before and after -- **no test deleted or weakened.**
3. **The census re-run over `lib/` reads 0** dotted-string patch targets that miss, denominator printed.

⛔ **A STRUCTURAL FIX (`lib/__init__.py`, or a pytest import-mode change) IS IN SCOPE ONLY IF PROVEN HARMLESS
ACROSS THE FULL SUITE** -- otherwise fix per site, and the worker states which it chose and why. **That bound is
right: the structural fix is one line and would change how EVERY test in the estate imports.**

**Fan-out is now 4** (`z-0`, `z-1`, `z-2`, `z-3`), slots `~31`..`~34`, all issuable.

⚠ **A DISCIPLINE NOTE ON MY OWN FILENAMES, THIRD INSTANCE:** I stamped that route `1205Z` when the clock read
`11:40Z` -- same error as `0205Z`-for-00:45 and `0742Z`-for-07:15. **These names are coordinates peers CITE**: the
CTO's rulings quote mine back verbatim, so a wrong stamp corrupts another seat's record, not just mine. **The fix
is `date -u`, which costs nothing, and I had been estimating instead.** Every filename from here is read from the
clock.
### 23.6 CORRECTION -- I VERIFIED AGAINST A PARAPHRASE OF THE CONTRACT, NOT THE CONTRACT

I reported that FWD-4 clause (i) named five facts of which the schema carried two, and offered two readings.
⛔ **`1.0.0_SA_CTO~Z` (20260928T121201Z): NEITHER reading was right.** The fork came from its round-10 SHORTHAND
("headline / opening / count / share"). **The RATIFIED DONE WHEN reads:** *"whether the company is IN the
headline, IN the opening, how often it is named, how much of the article names it, which other covered companies
it names, and a strength grade"* -- **headline and opening are WHETHER facts, not text.** All six are carried:

| the ratified fact | column |
|---|---|
| in the headline | `mention_in_title` |
| in the opening | `mention_in_lead` |
| how often named | `mention_count` |
| how much of the article | `blocks_hit` / `blocks_total` |
| other covered companies | `co_mentioned_securities` |
| strength grade | `signal_tier` |

⭐ **AND `share`'s ABSENCE IS THE CONTRACT WORKING, NOT A GAP:** `C-HV-ABSOLUTE-ONLY` BARS a ratio from gold, so
share is computed at serve time -- **storing it would BREAK the contract.** I read an absence as a possible defect
when it was a deliberate prohibition.

⛔ **THE KEEPABLE FORM: I compared the schema against the ANALYSIS'S SUMMARY of FWD-4, never against FWD-4.**
CLAUDE.md rule 27 states the remedy in advance -- *"a citation ages separately from the text it quotes: verify a
quote by printing the bytes at the cited line, never by grepping for the quote."* **One read of FWD-4 in the PRD
would have dissolved the whole fork.** Worse: **I had cited `C-HV-ABSOLUTE-ONLY` MYSELF in `w-3`'s order**
("computed at serve time and never stored") and did not apply it to `share`. **COST: read the clause, not the
sentence that summarises it -- including when a trusted seat wrote the summary.**

**`z-2`'s cut is UNCHANGED and the CTO confirms it was right regardless:** its mapping-first criterion will now
find all six carried and the census over those seven columns closes clause (i). **A criterion that states its
mapping before counting is correct whether the mapping holds or not** -- which is exactly why it was the right
shape while the question was open.

## 24. ROUND 12 -- L5 DECOMPOSITION v2.1, over the round-11 analysis (`ledger/ROUND_ANALYSIS.round11.md` @91276ffa94)

**Issuer `2.0.0_SA_COO~H`** (re-seated from `~Y`, record @63854377ef), 2026-09-28 ~22:5xZ. Round 11 CLOSED; the
analysis's section 4 lists five items and asks for ONE issuance. Series **`a`** (spent: h, r, s, t, u, v, w, x, y, z
over 32 orders; `ls task-orders/ | cut -d. -f2` census). The three vendor cells keep their drafted ids `w-2`, `w-4`,
`w-5` (s.20.5), so the analysis's names resolve. Slots MAX+1 over 34: `~35` `~36` `~37` `~38`; the deploy is a SEAT.

### 24.1 THE FIVE ITEMS -> SEVEN ORDERS, and each split is a measurement, not a preference

| analysis item | order(s) | class | slot |
|---|---|---|---|
| 1 mount + ledgered deploy + timing | `HVST-a-1` declare the mount (tf list, precondition 16->18, route table 16->18) | WORLD by the L6 floor (tf path); runs no terraform | `~35` |
| | `HVST-a-2` PACKAGE AND DEPLOY, under a never-widen pair + NEVER-2 entry | WORLD | `0.7.0_AE_CloudOps~R` |
| 2 the lead names the plurality story | `HVST-a-3` the rule, proved in memory over landed data | LOCAL | `~36` |
| | `HVST-a-4` the served rebuild, under a fresh pair, carrying the round's JUDGMENT | SERVED | `~36` (continued) |
| 3 `w-5` bbg diagnostic | `HVST-w-5` ONE call pair through the estate's transport, NOT the producer's repair path | WORLD | `~37` |
| 5 `w-2` capture, capped | `HVST-w-2` sa only, 25 jobs max in invocations of 5, `--new-only`, carrying `s.20.6`'s JUDGMENT | WORLD | `~37` (continued) |
| 4 `w-4` ft/barrons diagnostic | `HVST-w-4` answered WITHOUT a vendor call | LOCAL | `~38` |

1. **Item 1 is two orders because the deploy cannot work as listed (row `Z-S35`, filed at this cut).** The deployed
   `opal-amgt-scoped-api` package carries pyarrow 0 and `lib/opal_naming` 0, and its only layer
   (`opal-amgt-print-deps:1`, numpy 2.2.6, 121.7 MB unzipped) carries pyarrow 0 -- so a mount plus a code-only
   redeploy would answer an import failure on both timeline routes. The packaging choice (wheel source, 250 MiB
   budget) is an infra call on halves the CTO signs, so it rides the deploy seat's order, not a worker's.
2. **Item 2 is two orders because NEVER-1 reads the expected outcome from the producer's OWN rule at signing**, and
   the rule does not exist until `a-3` merges (the `y-1` -> `z-1` pattern of rounds 10-11).
3. **Item 4 carries no vendor call.** The rows gold reads are keyed by `article_key` (`publication_gold.py:714-718`,
   `:584`, `:621`); the sqlite `articles` table has a composite primary key (`worker.py:32-33`), so `Z-S31`'s premise
   is false and the one duplicate is one ft story naming two securities. One Opal S3 read settles the rest; the
   barrons half is a local test flake. Andrew's word is a permission and is not spent where no vendor byte is needed.
4. **Item 3 routes around the producer.** A bbg 403 inside `run` opens a headed Chrome press-and-hold and can call the
   metered Kimi vision API (`verification.py:84,114-132,123-125`); `AuthExpired` fires the credentialed login
   (`worker.py:285-293`). None is covered by the word. The estate's `bloomberg_rest_fetch.check/.search` return the
   raw responses on the parked session without any of them. The decomp's s.20.5 starting hypothesis (the drain never
   fell) is withdrawn: 8 of 8 traced holds, AND the one success, show the same non-draining trace.

### 24.2 FAN-OUT, derived

Edges: `a-1 -> a-2` (the deploy applies the declared mount); `a-3 -> a-4` (the rebuild runs the merged rule);
`w-5 -> w-2` (one runner, shared ledger and session vault, the analysis's order). `w-4` has no edge.
**M = 4 chains; N = 4 worker slots + 1 seat; cap 8 not pressed.** Write sets are disjoint: `a-1` owns the tf and the
api route table/tests; `a-2` owns the build script and the ledger; `a-3` owns `publication_gold.py` and its event
tests; the rest write only their deliverables, the channel, and (`w-5`/`w-2`) one ledger file.

### 24.3 PAIRS OWED, and by whom

- `a-2`: COO half `deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A2.md`, written after `a-1` merges and a
  `--build-only` closure diff exists; it cards the RESAPP routes the same artifact serves. CTO half by
  `1.0.0_SA_CTO~Z`. The seat is spawned by this seat after both are committed.
- `a-4`: COO half `deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A4.md`, written after `a-3` merges,
  stating whether `a-2` has made the table user-visible by then. CTO half by `1.0.0_SA_CTO~Z`.

### 24.4 CHECKS DRY-RUN AT THE BASE (report 2 C4)

`a-1.AC1` base: FAIL as expected (7 failures; its first draft read 18 at a base of 16 off quoted comment text and was
fixed before the cut). `a-2.AC1` base: FAIL as expected (6; the first draft passed the ceiling arm vacuously on a 404
and was fixed). `a-2.AC2` base: FAIL as expected on its 2 build arms; rollback-target and 3 RESAPP controls PASS.
`a-1.AC2` and `a-3.AC2` are suite controls, PASS at the base (255; 12). The `a-3`/`a-4`/`w-*` scripts are
worker-written as in every prior round of this project, each criterion stating its base expectation.

## 25. ROUND 13 -- L5 DECOMPOSITION v2.2, over the round-12 analysis (`ledger/ROUND_ANALYSIS.round12.md` @094cc1f110)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~03:3xZ. Round 12 CLOSED (7 of 7; the timeline serves on the deployed API).
Series **`b`** (spent: h, r, s, t, u, v, w, x, y, z, a over 39 orders). Slot MAX+1 over 38: **`~39`**.

### 25.1 THE LIST -> TWO ORDERS, ONE CHAIN

| analysis item | order | class | slot |
|---|---|---|---|
| 1 one story per event + calendar tokens out of the link vocabulary (the `C-HV-EVENT-SPINE` round-12 addendum), STOP limb: none of the six one-company events lost or split | `HVST-b-1` the rule, proved in memory | LOCAL | `~39` |
| | `HVST-b-2` the served rebuild under a never-widen pair, carrying the round's JUDGMENT | SERVED | `~39` (continued) |
| 2 `Z-S37` (`safe-merge --continue` whitelists the index snapshot) | **not a cell** | -- | -- |

1. **Item 1 is two orders for the round-12 reason:** NEVER-1 reads the expected outcome from the producer's own rule at
   signing, and the rule exists only after `b-1` merges.
2. **Item 2 is not a cell:** the analysis makes it "a cell only if this project owns a write surface for it", and
   `.tools/safe-merge.sh` is not this project's (its authoring lane is `2.0.0_SA_COO` base; the fix is proposed on row
   `Z-S37`). This seat's disarm stands as a procedure: the pre-`--continue` foreign-path diff, run on every drain since.
3. **The STOP limb's population is the L9's, not mine:** `ADJUDICATION_v20.md` @`19dfdd2579` graded 6 of 8 served events as
   one company event (992_HK x3, COST 09-14, HD 08-18, NVDA 06-01). Both orders check SPAN and TIER-A MEMBERSHIP, never the
   id, because the addendum moves every id ("`event_id` carries the story").
4. **User-visible:** since round 12 the deployed timeline serves the newest `chatter_event` part, so `b-2` is the first
   rebuild of this table a user sees.

### 25.2 FAN-OUT

`b-1 -> b-2` is one chain (the rebuild runs the merged rule). **M = 1, N = 1, cap 8 not pressed.** Write set: `b-1` owns
`publication_gold.py` and its event tests; `b-2` writes only its deliverables and the channel.

### 25.3 NOT CELLS

The Seeking Alpha 402 (`Z-W37-S4`) is the account holder's to read; the portal push of `92a2576254` is under Andrew's
hold (~20:3xZ). Neither waits on this round.

## 26. ROUND 14 -- L5 DECOMPOSITION v2.3, over the round-13 analysis (`ledger/ROUND_ANALYSIS.round13.md` @f1de5ca7ce)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~07:0xZ. Round 13 CLOSED (2 of 2; the CVO graded 7 of 7 served events one story,
read IN-SAMPLE). Series **`c`** (spent: h, r, s, t, u, v, w, x, y, z, a, b over 41 orders). Slot MAX+1 over 39: **`~40`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the held-out read of the one-story rule + the burst-shape census (no new vendor leg) | `HVST-c-1` | LOCAL | `~40` |

**Measured at the cut (CLOUD `f1de5ca7ce`), so the order states its base rather than predicting it:** 130 of 263
mention rows over 50 of 55 securities are held-out (44 tier A/B); the rule forms **0 events** on them; the newest mention
is 2026-09-15 (no capture postdates the rule); 1 (security, day) carries more than 3 tier-A/B articles (BA 09-08, in-
sample); the largest served event is 3 articles over 1 day. **So the held-out event set is empty and a precision grade is
impossible here;** the order adds a RECALL arm (held-out near-miss stories laid out for L9) inside the ruling's intent.
**Fan-out: 1 of 1 chain, N = 1.** NOT cells: the event route (`Z-W39-S1`, ruled not cut), the portal push (Andrew's hold),
the Seeking Alpha 402 (the account holder), a further bbg diagnostic (its own word), `Z-S37` (the tool's authoring lane).

## 27. ROUND 15 -- L5 DECOMPOSITION v2.4, over the round-14 analysis (`ledger/ROUND_ANALYSIS.round14.md` @f00c9a0c43)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~08:4xZ. Round 14 CLOSED (1 of 1; 0 held-out events, round 13 stays IN-SAMPLE).
Series **`d`** (spent: h, r, s, t, u, v, w, x, y, z, a, b, c over 42 orders). Slot MAX+1 over 40: **`~41`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1a common-name aliases: universe census of non-suffix tails, `.com` at minimum, `Z-W40-S1` read first, proved in memory | `HVST-d-1` | LOCAL | `~41` |
| 1b rebuild mention + daily + event under a never-widen pair; false-hit sample and new-event judgment at L9 | `HVST-d-2` | SERVED | `~41` (continued) |

**Split for the NEVER-1 reason of rounds 12-13:** the pair reads its expected diff from `d-1`'s merged rule. **Measured at
the cut (CLOUD `b907d17f1c`):** the served mention (263 rows, 55 securities) and daily (50,997 rows) parts were built on
09-24 by `2.0.0_SA_COO~Y` from `universe_securities.build()` over pool `universe/v1/2026-09-16.json` (191 securities, sa
join off) -- not from the `~4` 6-security file -- so both cells pin that input; 1 of 191 alias sets carries a dot tail
(AMZN); silver grew 118 -> 120 articles since, so `d-1` attributes every moved row ALIAS or DRIFT. **Issuer widening, carded
to the CTO:** `chatter_daily` joins the radius because `build_daily` reads the newest mention part and `/timeline` serves it.
**Fan-out: 1 of 1 chain (d-1 -> d-2, one worker), N = 1.** NOT cells: the event route (`Z-W39-S1`), the portal push
(Andrew's hold), the Seeking Alpha 402 (the account holder), `Z-S37` (the tool's authoring lane).

## 28. ROUND 16 -- L5 DECOMPOSITION v2.5, over the round-15 analysis (`ledger/ROUND_ANALYSIS.round15.md` @ce26d1244b)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~10:3xZ. Round 15 CLOSED (2 of 2; the CVO read 12 of 12 new matches as the company
and the AMZN 09-07 event as one own-company story, a sample of one). Series **`e`** (spent: h, r, s, t, u, v, w, x, y, z,
a, b, c, d over 44 orders). Slot MAX+1 over 41: **`~42`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1a one text span, one count: the matcher change, proved in memory | `HVST-e-1` | LOCAL | `~42` |
| 1b rebuild mention + daily under a never-widen pair, events measured; one-count-per-mention judgment at L9 | `HVST-e-2` | SERVED | `~42` (continued) |

**Measured at the cut (CLOUD `c13ec03ca8`), a prototype span count over 120 silver articles:** `mention_count` moves on 14
of 275 rows across 6 securities (AMZN 8, UPS 2, GOOGL, GOOG, DAL, FDX 1 each); **8 rows move tier C -> D** (tier C is
`mention_count >= 2`); title, lead and blocks_hit move on 0 rows, so A/B and events are expected not to move. **The
ruling's premise ("does not touch tier") is corrected here for C/D and carded to the CTO;** the ruling is unchanged.
**Fan-out: 1 of 1 chain (e-1 -> e-2, one worker), N = 1.** NOT cells: held-out reads (no new data), the event route
(`Z-W39-S1`), the portal push (Andrew's hold), `Z-W40-S1` (not in this analysis's list).

## 29. ROUND 17 -- L5 DECOMPOSITION v2.6, over the round-16 analysis (`ledger/ROUND_ANALYSIS.round16.md` @f424435829)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~12:1xZ. Round 16 CLOSED (2 of 2; the double count is gone, 8 = 8 = 8 on the
crash report; `Z-W41-S2` graduates). Series **`f`** (spent: h, r, s, t, u, v, w, x, y, z, a, b, c, d, e over 46 orders).
Slots MAX+1 over 42: **`~43`, `~44`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 ticker and brand census: added mentions per form, a printed sample for the text read at L9 | `HVST-f-1` | LOCAL | `~43` |
| 2 a security's first burst survives name detection (`Z-W40-S1`); fixture mechanism test + served events unmoved | `HVST-f-2` | LOCAL | `~44` |

**Measured at the cut (CLOUD `9ebf76b6da`):** 191 securities, 120 silver articles, 8 served events; the served event part
equals `event_rows` over the served mention part (`e-2` AC2). `f-2` points at `match_forms` (the aliases that hit, carried
on every mention row) as a non-inferred name source; the worker chooses the mechanism. A moved served event stops `f-2` at
BLOCKING (a pair and its own cell follow). **Fan-out: 2 of 2 chains, independent, N = 2, cap 8.** NOT cells: the event
route (`Z-W39-S1`), the portal push (Andrew's hold), new held-out reads (the Seeking Alpha 402).

## 30. ROUND 18 -- L5 DECOMPOSITION v2.7, over the round-17 analysis (`ledger/ROUND_ANALYSIS.round17.md` @c296f4ba12)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~14:1xZ. Round 17 CLOSED (2 of 2; `Z-W40-S1` graduated; the census read hit by hit,
tickers 172/240, short names 61/291). Series **`g`** (spent: h, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f over 48 orders).
Slot MAX+1 over 44: **`~45`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the alias rule: case-sensitive tickers 2+ chars with a refusal list; the whole-brand list; the parent-brand refusal in code | `HVST-g-1` | LOCAL | `~45` |
| 2 the served rebuild on the new rule (mention, daily, event) under a never-widen pair | `HVST-g-2` | SERVED | `~45` (continued) |

**Measured at the cut (CLOUD `f1c482d24f`):** served parts 5 / 6 / 7 (mention 275, daily 51,952, event 8). `KO_US_Equity`
carries the alias `Coca-Cola`, so the ruled listed-brand check refuses `KOF`. **Walmart Inc. is in neither the 191 nor
the pool's 250 names**, so that check cannot refuse the planted `WALMEX*` -> `Walmart` entry the same ruling requires.
**Issuer's ruling:** the refusal is TWO limbs in code: (a) any other pool name's alias or company name; (b) an explicit
parent-brand refusal list in `whole_brand_aliases.json`, starting with `Walmart` and citing the census. Carded to the CTO.
`g-2` AC1 is a post-act read, with the act and its dry pre-check as standing clauses (round 16 `Z-W42-S1`/`S2`).
**Fan-out: 1 of 1 chain (g-1 -> g-2, one worker), N = 1, cap 8.** NOT cells: a brand-to-parent source, the event route
(`Z-W39-S1`), the portal push (Andrew's hold), new held-out reads (the Seeking Alpha 402).

## 31. ROUND 19 -- L5 DECOMPOSITION v2.8, over the round-18 analysis (`ledger/ROUND_ANALYSIS.round18.md` @d11fd4d089)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~20:3xZ. Round 18 CLOSED: 2 of 2; the alias rule is served; the CVO read the rule
179 of 179 correct; ASML's DENIED->PARTIAL was ruled correct. Series **`i`** (spent: h, r, s, t, u, v, w, x, y, z, a, b, c,
d, e, f, g over 50 orders; census from `ls task-orders/`). Slot MAX+1 over 45 is **`~46`**; the deploy is a SEAT.

| analysis item | order | class | slot |
|---|---|---|---|
| 2 the whole-brand list agrees with its refusal limb (`UBS` off; test: no entry refused by limb (a)) | `HVST-i-1` | LOCAL | `~46` |
| 1 a PARTIAL day names its publisher -- the rule and both routes, proved in memory | `HVST-i-2` | LOCAL | `~46` (continued) |
| 1 -- the served `chatter_daily` rebuild carrying the codes, under a never-widen pair | `HVST-i-3` | SERVED | `~46` (continued) |
| 1 -- the scoped-API redeploy so both routes serve the codes, under a pair + NEVER-2 entry | `HVST-i-4` | WORLD | `0.7.0_AE_CloudOps~A` |

**Item 1 is three orders, by the round-12 pattern (s.24.1), and each split is a measurement:**
1. **`i-2` before `i-3`:** NEVER-1 reads the expected outcome from the producer's own rule at signing, and that rule
   does not exist until `i-2` merges.
2. **`i-4` is a seat order:** `timeline_api.py` is packaged into `opal-amgt-scoped-api`. The deployed function at the cut
   (`lg6NJ2JL...`, RESAPP ww-1, 19:18:58Z) serves neither `publishers_covered` nor any codes. That was measured:
   `round19/checks/i-4.AC1.base.txt` records 272 of 272 ASML_NA days lacking both fields. The analysis's "the served
   `/timeline` and `timeline_day` carry both" is reached only by a deploy.

The analysis orders `UBS` first ("cell 1 depends on cell 2"), so the securities file `i-3` builds from carries the
list fix.

**Widened inside the decomposition (issuer's ruling):**
- `i-1`'s in-memory proof covers daily and event as well as mention, because row `Z-W45-S2` measured that `aliases`
  reach `data_status`.
- `i-3`'s dry step re-reads the scoped API's CodeSha256 beside the ETags (row `Z-S41`).

**Fan-out: 1 of 1 chain (`i-1 -> i-2 -> i-3 -> i-4`); N = 1 worker slot + 1 seat; cap 8 not pressed.** Edges:
- `i-1 -> i-2`: one worker, and `i-2`'s build uses `i-1`'s securities file.
- `i-2 -> i-3`: the rebuild runs the merged rule.
- `i-3 -> i-4`: AC1 of `i-4` compares the served codes to the LANDED column, which exists only after `i-3`.

Write sets are disjoint:
- `i-1` owns `whole_brand_aliases.json` and the tests.
- `i-2` owns `publication_gold.py`, `timeline_api.py` and the tests.
- `i-3` writes only its deliverables and the channel.
- `i-4` owns the tf dir and the change-management ledger.

**Pairs owed:**
- `i-3`: COO half `deliverables/2.0.0_SA_COO_H/round19/NEVER_WIDEN_HALF_COO_I3.md`, written after `i-2` merges; CTO half
  by `1.0.0_SA_CTO~Z`.
- `i-4`: COO half `.../round19/NEVER_WIDEN_HALF_COO_I4.md`, written after `i-3` lands, from a `--build-only` closure
  diff carded by project; CTO half by `1.0.0_SA_CTO~Z`.

**Checks dry-run at the base (report 2 C4):**
- `i-4.AC1`: FAIL as expected (6).
- `i-4.AC2`: FAIL as expected on its 2 build arms; the rollback target and 3 RESAPP controls PASS.
- `i-1`, `i-2` and `i-3` scripts are worker-written, as in every prior round of this project, and each criterion states
  its base expectation.

**NOT cells** (analysis s.4):
- the tier rule for passing mentions;
- a brand-to-parent source;
- the event route (`Z-W39-S1`);
- the portal push (Andrew's hold);
- new held-out reads (the Seeking Alpha 402).

## 32. ROUND 20 -- L5 DECOMPOSITION v2.9, over the round-19 analysis (`ledger/ROUND_ANALYSIS.round19.md` @a251f02116)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~22:4xZ. Round 19 CLOSED: 4 of 4. Publisher codes are served end to end, the
"covered" wording is ruled in DSGN, and `Z-W45-S1`/`S2` graduated. Series **`j`**; slots MAX+1 over 46 are **`~47`**
and **`~48`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the event route serves the stored event by its stored id (`Z-W39-S1`) -- THE CODE | `HVST-j-1` | LOCAL | `~47` |
| 1 -- wiring + mount + redeploy so the route answers users | NOT CUT: HELD for the CTO (row `Z-S42`) | -- | -- |
| 2 the story-span census (`Z-W41-S1`), measurement only | `HVST-j-2` | LOCAL | `~48` |

**Why item 1's served half is held, not cut (row `Z-S42`, measured at the cut):**
- The event route answers no user: the deployed function returns `404 no /api/scoped/amgt route`.
- The gateway's 108 routes carry only `/timeline` and `/timeline/day`.
- The adapter states the route "IS NOT WIRED", and a test asserts it.
- The page builds only the two mounted URLs.

So the analysis's AC ("all 8 served events answer 200 by their stored ids" after a redeploy) cannot be met by a
redeploy. It needs an adapter wiring plus a terraform mount: a NEW served surface that no page calls. That is the
CTO's call, carded with a REC (mount only when DSGN_AMGTV1's page needs an event window by id).

The code defect is real (8 of 8 stored ids differ from the recomputed id) and the fix is right under either answer, so
`j-1` is cut now, unwired.

**Fan-out: 2 of 2 chains (`j-1`; `j-2`), independent; N = 2 worker slots; cap 8 not pressed.** Write sets are
disjoint: `j-1` owns `timeline_api.py` and its tests; `j-2` writes only its deliverables and the channel.

**Checks at the base:**
- `j-1` AC1: the named tests FAIL by construction. AC2 (b) FAILS (the old route is `first_day`-keyed and its id is
  recomputed; issuer read 8 of 8 differ).
- `j-2` AC1 (a) must reproduce the served event part (8 events, ETag `c146a325...`).
- The scripts are worker-written, as in every prior round.

**NOT cells** (analysis s.4 plus this cut):
- the page wording (DSGN_AMGTV1);
- `Z-S37` (the tool's owner, PARKED on MSTR~Z);
- a field rename;
- the event route's wiring, mount and deploy (HELD, `Z-S42`).

## 33. ROUND 21 -- L5 DECOMPOSITION v3.0, over the round-20 analysis (`ledger/ROUND_ANALYSIS.round20.md` @4b8bd40242)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-29 ~23:1xZ. Round 20 CLOSED: 2 of 2; `Z-W39-S1` and `Z-S37` graduated. The span rule
is ADOPTED with a roundup guard, the link window is unchanged, and the lead question waits on a census. Series **`k`**;
slots MAX+1 over 48 are **`~49`** and **`~50`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the span rule plus the roundup guard, in code, dry-rebuilt (HD ends 08-18; 992 HK and AMZN equal `j-2`'s) | `HVST-k-1` | LOCAL | `~49` |
| 2 the updated-time census over the 120 silver articles (plus the bronze they point to), HD's barrons lead by name | `HVST-k-2` | LOCAL | `~50` |

**Fan-out: 2 of 2 chains, independent; N = 2 worker slots; cap 8 not pressed.** Write sets are disjoint: `k-1` owns
`publication_gold.py` and its tests; `k-2` writes only its deliverables and the channel.

**Widened inside the decomposition (issuer's ruling):**
- `k-1` AC2 (b) requires the 5 events `j-2` KEPT to stay row-equal, so the rule change is bounded on the untouched
  events as well as the three it moves.
- `k-2` reads bronze through silver's own keys where silver lacks a time field. It is still Opal S3 only, with no fetch.

**Round 22** is the SERVED `chatter_event` rebuild under a never-widen pair, cut after the CTO rules the lead question on
`k-2`.

**Checks at the base:**
- `k-1` AC1: the named tests FAIL.
- `k-1` AC2 (c) and (d): FAIL (the served rule is per-day).
- `k-2` is a census with no FAIL arm.
- The scripts are worker-written.

**NOT cells:**
- the link window (ruling 4);
- the event route mount (HELD);
- the roundup flag's producer.

## 34. ROUND 22 -- L5 DECOMPOSITION v3.1, over the round-21 analysis (`ledger/ROUND_ANALYSIS.round21.md` @63c272600a, corrected @3100474cde)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~00:0xZ. Round 21 CLOSED: 2 of 2. The span rule plus the guard at 4 is merged.
The retitled-preview lead is ACCEPTED and DISCLOSED. Series **`l`**; slots **`~51`** and **`~52`**.

**Before the cut the issuer measured analysis ruling 2's premise FALSE:**
- `is_roundup` IS `co_mention_count >= 5` by construction (`DEFAULT_ROUNDUP_AT`; 304 of 304 rows).
- So "the guard reads `co_mention >= 4` only" is outcome-identical to `k-1` (dry run: KEPT 5 / CHANGED 3 / GONE 0; AMZN
  09-06..09-07, not 09-08).
- Carded (msg 26795). The CTO corrected s.2a @`3100474cde`: cell 1 is a one-line simplification with AC "8 of 8
  identical", and cell 2 is cut NOW.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the guard reads `co_mention_count >= 4` only -- a simplification, 8 of 8 events identical to `k-1` | `HVST-l-1` | LOCAL | `~51` (`worker-light`) |
| 2 the served `chatter_event` rebuild on the span rule, under a never-widen pair naming HD's lead change and AMZN's span | `HVST-l-2` | SERVED | `~52` |

**Fan-out: 2 of 2 chains, independent; N = 2 worker slots; cap 8 not pressed.** `l-1` cannot move an outcome, so `l-2`
does not wait on it. `l-2` builds from the rule at `88dbe4af64`. Write sets are disjoint: `l-1` owns
`publication_gold.py` and its tests; `l-2` writes only its deliverables and the channel.

**Pair owed:** `l-2`'s COO half `deliverables/2.0.0_SA_COO_H/round22/NEVER_WIDEN_HALF_COO_L2.md` (signed this tick) and
its CTO half.

**NOT cells:**
- the `is_roundup` producer;
- the link window;
- the event route mount (HELD).

## 35. ROUND 23 -- L5 DECOMPOSITION v3.2, over the round-22 analysis (`ledger/ROUND_ANALYSIS.round22.md` @9d7bd0e4f9)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~01:1xZ. Round 22 CLOSED: 2 of 2, AC4 MET 3 of 3, and `Z-W41-S1` graduated. The
event work is done for the served half. **Finding (analysis ruling 3):** seven of nine FWDs have gone ungraded since
round 10. Round 23 re-reads them from the served store. Series **`m`**; slots **`~53`**, **`~54`** and **`~55`**.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 FWD-1/2/3: re-readable byte-exact, every sent field kept, how each article was found | `HVST-m-1` | LOCAL (read-only over the served store) | `~53` |
| 2 FWD-4/7: the strength carriers per pair (grade re-derived from stored text), and the page's rank against a rank recomputed from the graded daily table | `HVST-m-2` | LOCAL (read-only) | `~54` |
| 3 FWD-8/9: undelivered desktop articles, and article history since 2026-01-01 per covered security | `HVST-m-3` | LOCAL (read-only) | `~55` |

**Fan-out: 3 of 3 chains, independent; N = 3 worker slots; cap 8 not pressed.** Each cell writes only its own
deliverables folder and the channel. Each carries at most 3 criteria, each quotes its FWDs' DONE WHEN lines verbatim,
and each prints what this machine cannot see as NOT MEASURABLE HERE rather than estimating it.

**The adversaries, named in each preflight:**
- A pass rate over a filtered population.
- A grade "re-derived" by the producer itself.
- FWD-9's history read off the daily table's ROW range, which covers every day by construction, instead of off the
  ARTICLES.

**NOT cells:**
- events;
- the link window;
- the event route mount;
- the Seeking Alpha capture (until the account reads 200).

## 36. ROUND 24 -- L5 DECOMPOSITION v3.3, over the round-23 analysis (`ledger/ROUND_ANALYSIS.round23.md` @d1ec6f4118)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~02:0xZ. Round 23 CLOSED. The seven FWDs are graded: **FWD-4 and FWD-8 REALIZED**;
FWD-1/2/3/7/9 NOT REALIZED with named gaps; 2 of 9 REALIZED. Series **`n`**; slots **`~56`..`~60`** plus the seat
`0.7.0_AE_CloudOps~A`.

| analysis item | order | class | slot |
|---|---|---|---|
| 1 the collector keeps received bytes, links the listing object, rank+page for all, a run record (FWD-1/3) | `HVST-n-1` | LOCAL | `~56` |
| 2 sa's 5 missing fields + 6 missing rows in silver; query-by-company over the mention join (FWD-2) | `HVST-n-2` | LOCAL (a served silver rebuild, if AC2 shows rows move, is a follow-on paired order) | `~57` |
| 3 why the served rank holds 2 rows; the `gold` rank's expected diff (FWD-7) | `HVST-n-3` | LOCAL read | `~58` |
| 4 the `CHATTER_AXIS_SOURCE=gold` flip (FWD-7) | `HVST-n-4` | WORLD, under a pair and a NEVER-2 entry | `0.7.0_AE_CloudOps~A` (after `n-3`) |
| 5 the backfill plan for all 191 covered names, before any run (FWD-9) | `HVST-n-5` | LOCAL | `~59` |
| 6 `/timeline/day`: profile, then fix in code (FWD-5 latency; routed from DSGN r7 ruling 2) | `HVST-n-6` | LOCAL (the redeploy is a follow-on paired WORLD seat order) | `~60` |

**Fan-out: 5 of 5 chains start now (`n-1`, `n-2`, `n-3`, `n-5`, `n-6`); `n-4` follows `n-3`; N = 5 worker slots + 1 seat;
cap 8 not pressed.**

**Write sets are disjoint:**
- `n-1` owns named collector files (not `silver_from_bronze.py`) and `store.py`.
- `n-2` owns `silver_from_bronze.py` and its test.
- `n-6` owns `timeline_api.py`, `publication_gold.py`, the timeline loaders in `scoped_amgt.py` and their tests.
- `n-3` and `n-5` write only their deliverables.

**The two follow-ons, `n-2`'s served silver rebuild and `n-6`'s redeploy,** are the `i-2` -> `i-4` pattern. Each is cut
after its code merges, with its expected diff read from the merged code at signing.

**`n-4`'s checks are issuer-written after `n-3` drains,** because their content IS `n-3`'s measurement. They are
dry-run at the base before the dispatch. This is the one recorded departure from "every check a file at the cut".

**NOT cells:**
- re-fetching the 104 rebuilt originals;
- the backfill run (until `n-5`'s plan is read);
- events.

## 37. ROUND 25 -- L5 DECOMPOSITION v3.4, over the round-24 analysis (`ledger/ROUND_ANALYSIS.round24.md` @6c5b4339a1)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~03:4xZ.
- Round 24 is CLOSED, built but not served. 2 of 9 FWDs are REALIZED.
- Rulings: `ledger/CTO_RULING_ROUND24_N4_HOLD_GRAMMAR_FLAG_SILVER_TIE_20260930.md` @5998e71f23, with ruling 2 amended
  @e49bbdb3d2 on this seat's card (msg 26880).
- Series **`o`**; slots **`~61`..`~65`**.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 `chatter_daily` coverage from run records (FWD-7) | `HVST-o-1` | LOCAL (a served rebuild on this rule is a later paired order) | `~61` | now |
| 2 the scheduled run passes `--harvest-grammar` (FWD-1/3) | `HVST-o-2` | LOCAL, NO pair (amended ruling 2: the task is Disabled, 0 triggers; re-arming it is Andrew's) | `~62` | now |
| 3 `silver_latest` tie-break on `run_stamp`, in EVERY newest-wins silver reader (FWD-2) | `HVST-o-3` | LOCAL | `~63` | now |
| 4 the paired served sa silver rebuild (FWD-2) | `HVST-o-4` | WORLD, under a pair | `~64` | after `o-3` drains and both halves are committed; issuer-written checks |
| 5 Lenovo's backfill on barrons/bbg/ft/wsj; the repeat fetches 0 (FWD-9, then 3) | `HVST-o-5` | WORLD, under a pair; R-21 scripted egress | `~65` | after both halves are committed; issuer-written checks with the BEFORE snapshot |

**Fan-out: 4 of 4 chains start now (`o-1`, `o-2`, `o-3`, `o-5`). `o-4` follows `o-3`. N = 5 worker slots; cap 8.**
- `o-1`, `o-2` and `o-3` are spawned now.
- `o-5`'s worker is spawned when its pair is committed.

**Write sets:**
- `o-1` owns `worker.py`'s run-record code, and in `publication_gold.py` the coverage functions (`publisher_coverage`,
  `daily_rows` coverage, `build_daily`).
- `o-3` owns `store.py`, and in `publication_gold.py` the silver readers (`_iter_latest_articles`,
  `_latest_articles_for_keys`).
- `publication_gold.py` is therefore named by both, split at the function boundary each face states. A drain conflict
  there is resolved by the issuer at the merge.
- `o-2` owns `run-local.ps1` and `README.md`.
- `o-4` and `o-5` write only their deliverables and the served objects their halves name.

**NOT cells:**
- `n-6`'s redeploy: it rides AMGT_RESAPP r51's one build (ruling 1, routed to `2.0.0_SA_COO~Z`).
- Re-arming the Scheduled Task (Andrew's).
- The portal DEV promotion (Andrew's, through the integrator).
- The other 190 names' backfill (next round, on the Lenovo run's actual pages).
- The `CHATTER_AXIS_SOURCE` flip, which is re-cut when gold resolves a gradable pair.

## 38. ROUND 26 -- L5 DECOMPOSITION v3.5, over the round-25 analysis (`ledger/ROUND_ANALYSIS.round25.md` @300ea99310)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~06:1xZ. Round 25 is CLOSED: the first SERVED writes since round 22, both pairs held on
the output, 2 of 9 FWDs REALIZED. Series **`p`**; slots **`~66`..`~69`**.

**Rulings applied:**
- **Ruling 1:** every WORLD half names the command that reaches the put, the config defaults the argv leaves unset, and a
  stub put-count dry run.
- **Ruling 2:** every check base is pinned at cut.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 the mention rebuild (FWD-2; inputs to FWD-4/7; the ANDREW-DIRECT count) | `HVST-p-1` | WORLD, under a pair | `~66` | after its pair and issuer checks |
| 2 FWD-3's two rows: the never-stored fetch, the wsj key split | `HVST-p-2` | LOCAL | `~67` | now |
| 3 a span-bearing Lenovo bbg/wsj run, its upload, the `chatter_daily` coverage rebuild (FWD-7) | `HVST-p-3` | WORLD, under a pair plus R-21 scripted egress | `~68` | after `p-1` drains, then its pair and checks |
| 4 why ft and barrons refuse (FWD-1/9) | `HVST-p-4` | LOCAL, no request sent | `~69` | now |

**Fan-out: 4 of 4 chains.**
- `p-2` and `p-4` are spawned now.
- `p-1` is spawned when its pair is committed.
- `p-3` follows `p-1`: its daily build reads the newest mention snapshot. N = 4 slots; cap 8.

**Write sets:**
- `p-2` owns `worker.py`, `publishers.py` and `storage.py` for its fix.
- `p-3`'s act runs on the code pinned at its signing.
- `p-1`, `p-3` and `p-4` write only their deliverables and the served objects their halves name.

**NOT cells:**
- the other 190 names (ruling 4: ft and barrons are read first);
- the gold flip (waits on `p-3`'s evidence);
- the schedule (Andrew's).

**Section 38 addendum (issuer, 2026-09-30 ~07:5xZ) -- `p-3` split per `ledger/CTO_RULING_ROUND26_P3_SPLIT_AND_FWD7_DENOMINATOR_20260930.md`.**
- `HVST-p-3` is part (a) only, the `chatter_daily` rebuild: complete @`49611d45cb`.
- **Part (b)** (the span-bearing Lenovo bbg/wsj run, its upload, and the rebuild that reads the persisted run record) is
  **carried to round 27 as its first cell.**
  - `to-pipeline-gate` refuses a second issuance within round 26 (ONE ISSUER PER ROUND). `p-3` is terminal.
  - Round 27 opens FWD-7's denominator work, and (b) is that work's positive arm.
- Its COO half and checks are already signed at `round26/NEVER_WIDEN_HALF_COO_P5.md` and `round26/checks/p-5.*`. The round-27
  order cites them, re-measured at its cut.

## 39. ROUND 27 -- L5 DECOMPOSITION v3.6, over the round-26 analysis (`ledger/ROUND_ANALYSIS.round26.md` @ff4405d3d5)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~08:3xZ. Round 26 is CLOSED, 2 of 9 FWDs REALIZED. PRD v0.4 adds
`C-HV-RANK-DECLARED-SET` and `C-HV-COVERED-VS-FOUND`.
- The packet's "serves `[bbg, wsj]`" was the union. The series reads `[bbg, wsj]` on 8 of 273 days (CVO v35, ruling 1).
- Series **`q`**; slots **`~70`..`~75`** plus the seat `0.7.0_AE_CloudOps~A`.

| analysis item | order | class | slot | dispatch / merge |
|---|---|---|---|---|
| 1 `p-3(b)`: span-bearing Lenovo run, upload, and the rebuild reading the persisted run record | `HVST-q-1` | WORLD, under a pair plus R-21 | `~70` | FIRST, once the CTO half is signed at the cut |
| 2 `Z-S44`: bbg as-received parses into silver | `HVST-q-2` | LOCAL | `~71` | now; merges after `q-1` drains |
| 3 FWD-7 eligibility census, declared set (bbg, wsj), COVERED only | `HVST-q-3` | LOCAL read | `~72` | after `q-1` drains |
| 4 `C-HV-RANK-DECLARED-SET` in code (`chatter_axis`, `generation_writer.py`) | `HVST-q-4` | LOCAL | `~73` | now; merges after `q-1` drains |
| 5 `C-HV-COVERED-VS-FOUND` in code (`publishers_found_codes`) | `HVST-q-5` | LOCAL | `~74` | now; merges after `q-1` drains |
| 6 barrons B2 guard edit + ft F1 403 body, tests only | `HVST-q-6` | LOCAL, no request | `~75` | now; merges after `q-1` drains |
| 7 the gold flip on the declared-set rule | `HVST-q-7` | WORLD, under a pair plus NEVER-2 | `0.7.0_AE_CloudOps~A` | after `q-3` and `q-4` merge; issuer checks from `q-3`'s N |

**Fan-out: 7 of 7 cut in ONE issuance.**
- `q-1` goes first (ruling 6).
- `q-2`, `q-4`, `q-5` and `q-6` run now, with their merges held until `q-1` drains.
- `q-3` follows `q-1`, and `q-7` follows `q-3` and `q-4`.
- N = 6 slots + 1 seat; cap 8.

**Write sets:**

| order | owns |
|---|---|
| `q-2` | `silver_from_bronze.py` |
| `q-4` | `chatter_axis.py`, `generation_writer.py` |
| `q-5` | `publication_gold.py` (`daily_rows` fields and schema only) and `timeline_api.py` |
| `q-6` | `worker.py`, `transport.py` |
| `q-1`, `q-3`, `q-7` | their deliverables and the served objects their halves name |

**NOT cells:**
- the 190-name backfill;
- the bbg silver rebuild (round 28);
- the schedule (Andrew's).

## 40. ROUND 28 -- L5 DECOMPOSITION v3.7, over the round-27 analysis (`ledger/ROUND_ANALYSIS.round27.md` @8c0b34526b)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~09:5xZ.
- Round 27 is CLOSED, 2 of 9 FWDs REALIZED. PRD v0.5: the declared set is derived from config.
- Series **`aa`** (every single letter is used); slots **`~76`..`~80`**.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 reach from cached listings + the rejected-key hold | `HVST-aa-1` | LOCAL | `~76` | now |
| 2 fresh-day span-bearing Lenovo run + the daily rebuild serving `publishers_found_codes` | `HVST-aa-2` | WORLD, under a pair plus R-21 | `~77` | after `aa-1` merges, on a fresh UTC day (>= 2026-10-01); the pair is signed against the merged code |
| 3 the served bbg silver rebuild on `q-2`'s parse | `HVST-aa-3` | WORLD, under a pair | `~78` | after the CTO rules the 11 hash-keyed rows' fate (carded ~09:43Z); does not overlap `aa-2` |
| 4 the declared set derived from `ENABLED_PUBLISHERS` minus universe-wide refusals | `HVST-aa-4` | LOCAL | `~79` | now |
| 5 the pre-run listing-page print over the 190 names (`C-HV-EGRESS`) | `HVST-aa-5` | LOCAL, no request | `~80` | now |

**Fan-out: 5 of 5 cut.**
- `aa-1`, `aa-4` and `aa-5` start now.
- `aa-2` follows `aa-1` and a fresh day.
- `aa-3` follows its ruling.
- N = 5 slots; cap 8.

**Write sets:**

| order | owns |
|---|---|
| `aa-1` | `worker.py`, `publishers.py` |
| `aa-4` | `chatter_axis.py` |
| `aa-2`, `aa-3`, `aa-5` | their deliverables and the served objects their halves name |

**NOT cells:**
- the gold flip (it needs at least 10 eligible names);
- the backfill run (round 29);
- the barrons and ft runs (Andrew's).

## 41. ROUND 29 -- L5 DECOMPOSITION v3.8, over the round-28 analysis (`ledger/ROUND_ANALYSIS.round28.md` @c907537920)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~12:5xZ.
- Round 28 is CLOSED, 2 of 9 FWDs REALIZED. The run-record path is a SOURCE of coverage; FWD-7 is bound only by reach.
- Series **`ab`**; slots **`~81`..`~83`**.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 live wsj reach from `timestamp` (`Z-W76-S1`), `p-2`'s test re-pointed (`Z-W76-S2`), `NM5NLQ6K50XZ01` seeded into the hold | `HVST-ab-1` | LOCAL | `~81` | now |
| 2 the mention rebuild over silver with the 11 bbg rows | `HVST-ab-2` | WORLD, under a pair | `~82` | after its halves are signed; does not overlap `ab-3` |
| 3 backfill batch 1, 10 names x {bbg, wsj}, measured-first | `HVST-ab-3` | WORLD, under a pair plus R-21 | `~83` | after `ab-1` merges; halves signed against the merged code; does not overlap `ab-2` |

**Fan-out: 3 of 3 cut.**
- Chain 1: `ab-1` then `ab-3`.
- Chain 2: `ab-2`.
- The WORLD acts run one at a time. N = 3 slots; cap 8.

**Write sets:**

| order | owns |
|---|---|
| `ab-1` | `publishers.py`, `worker.py`, `test_p2_fetched_and_stored_keys.py`, its new test, and one seed row in the runtime `rejected_hold` |
| `ab-2`, `ab-3` | their deliverables and the served objects their halves name |

**Issuer ruling on `Z-W76-S1`:** `_hit_date` reads `timestamp` and `printPublicationDate`, so a wsj backfill bound-stops at
the floor. The paging change is intended, because it spends fewer pages.

**NOT cells:**
- batches 2+ (they wait on batch 1's measurement);
- the gold flip (the declared set is empty);
- the barrons and ft runs (Andrew's);
- the daily rebuild that reads the new mention snapshot and batch 1 (a later paired rebuild).
