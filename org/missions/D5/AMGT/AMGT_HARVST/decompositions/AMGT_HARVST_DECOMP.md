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

## 42. ROUND 29 RE-CUT -- L5 DECOMPOSITION v3.9, over PRD v0.9 (`C-HV-TRUST-TOKEN`) and Andrew-direct 2026-09-30 ~12:5xZ

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~14:0xZ.
- **The source:** CTO msg 27155. The record is
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_125xZ_OPEN_CALLS_RECS_APPROVED_TRUST_TOKENS_BACKOFF.md`.
  PRD v0.9 @`e1b5fd6d8c`, signed @`b9f1a8bc81`.
- **The act list moved:** Andrew's word moved barrons B1, ft and the schedule re-arm out of his acts and into collection work.
  The CTO directed them into round 29.

**A re-cut into the round's ONE issuance.** It MODIFIES orders and adds no file. `to-pipeline-gate` refused three added order
files: ONE ISSUER PER ROUND is keyed to the round, and a re-cut adds no file.

| item | carried by | class | dispatch |
|---|---|---|---|
| `C-HV-TRUST-TOKEN` in the collector: Secrets credentials, stored token first, a 429 is not expiry, bounded backoff with jitter, every attempt in the run record | `HVST-ab-1` AMENDMENT 2 (phase B) | LOCAL | after `ab-1` AMENDMENT 1 reports; the same worktree, where `publishers.py` and `worker.py` are already `ab-1`'s |
| barrons (B1) and ft Lenovo jobs, token-first, ft's kept 403 body read first | `HVST-ab-3` AMENDMENT 1: the batch-1 collection run also carries Lenovo x {barrons, ft}, under the same pair | WORLD, pair plus R-21 | after `ab-1` (both amendments) merges |
| re-arm the collection schedule, daily, for the names batch 1 reached | `HVST-ab-3` AMENDMENT 1, phase B, under a re-signed pair | WORLD, pair | after batch 1's after-reads pass |

**The chains now:**
- Chain 1: `ab-1` (A1, A2), then `ab-3` (phase A: batch 1 plus barrons/ft Lenovo), then `ab-3` phase B (the schedule).
- Chain 2: `ab-2`.

The WORLD acts run one at a time, `ab-2` then `ab-3`. N = 3 slots; cap 8.

**NOT cells:**
- the ft credential re-harvest (superseded: the credentials are in AWS Secrets);
- the NEVER-2 edit (Andrew asked to see the text; the CTO's).

## 43. ROUND 30 -- L5 DECOMPOSITION v3.10, over the round-29 analysis (`ledger/ROUND_ANALYSIS.round29.md` @d0bc0a79f0)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~17:3xZ.
- Round 29 is CLOSED, 2 of 9 FWDs REALIZED. PRD v0.10 adds the `bot_check` class; `prd-signoff` reads ADMITTED (the
  ENDPOINT hash is unchanged).
- Series **`ac`**; slots **`~84`..`~86`**. The round-29 addendum's refused files never landed, so these slots are unused.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 the `bot_check` attempt class (v0.10); the repair-failed path keeps its body | `HVST-ac-1` | LOCAL | `~84` | now |
| 2 the sa probe on RESOLVED securities, the account read first | `HVST-ac-2` | WORLD, pair + R-21 | `~85` | after its halves; does not overlap `ac-3` |
| 3 the paired daily rebuild carrying `ab-2`'s pairs | `HVST-ac-3` | WORLD, pair | `~86` | after its halves; does not overlap `ac-2` |

**Fan-out: 3 of 3 cut, in 3 independent chains.** The WORLD acts run one at a time: `ac-3` first (its inputs are fixed now),
then `ac-2`. N = 3 slots; cap 8.

**Write sets:**

| order | owns |
|---|---|
| `ac-1` | `transport.py`, `worker.py`, `verification.py`, a new `bot_check.py`, and its test |
| `ac-2`, `ac-3` | their deliverables and the served objects their halves name |

**Premise corrected at the cut:** the analysis's "four batch-1 kept bodies" are TWO (wsj, ft). bbg's and barrons' refusals were
raised by `verification.py` ~:21 without the response, so `ac-1` change 3 keeps that body from now on.

**NOT cells:**
- the batch-1 retry for wsj, ft, bbg and barrons (Andrew's headed session refresh; analysis section 5);
- any challenge handler (his 09-15 sequencing);
- batches 2+;
- a licensed-route probe.

## 44. ROUND 31 -- L5 DECOMPOSITION v3.11, over the round-30 analysis (`ledger/ROUND_ANALYSIS.round30.md` @6adebef352)

**Issuer `2.0.0_SA_COO~H`**, 2026-09-30 ~20:2xZ.
- Round 30 is CLOSED, 2 of 9 FWDs REALIZED; FWD-3 moved (covered-vs-found is live on the served route).
- **Bound by** the CTO cloud ruling section 0 and `4.0.0_SA_CRO~Z`'s bot-ops playbook @`7bcc258369`: NO traffic to bbg, wsj
  or barrons from the site Z box before the 05:00 ET first light.
- Series **`ad`**; slots **`~87`..`~89`**.

| analysis item | order | class | slot | dispatch |
|---|---|---|---|---|
| 1 the token store: wsj and barrons bundles into Secrets; ft's bundle expiry; the sa check's `{user_id}` (`Z-W85-S2`) | `HVST-ad-1` | LOCAL A0, then WORLD (Secrets writes), pair | `~87` | A0 now; the pair on the merged code |
| 2 sa batch 1: 10 resolved `sa_symbol` names, measured-first, stop at the first challenge, never a sign-in | `HVST-ad-2` | LOCAL A0 (`--no-sign-in`), then WORLD, pair + R-21 | `~88` | A0 now; the pair on the merged code; the act finishes before 08:00Z 10-01 |
| 3 the residential-IP assignability read | `HVST-ad-3` | LOCAL read | `~89` | now |

**Fan-out: 3 of 3 cut, in 3 independent chains.** The WORLD phases run one at a time. N = 3 slots; cap 8.

**Write sets:**

| order | owns |
|---|---|
| `ad-1` | `credentials.py`, `sa_rest_fetch.py` (the collector's sa consumer), its test |
| `ad-2` | `__main__.py`, `sessions.py`, `worker.py`, its test |
| `ad-3` | its deliverables only |

The first two are disjoint, so the A0 phases run in parallel.

**Premises re-measured at the cut** (ruling 4):
- the bundles to store are 2 (`wsj.dpapi`, `barrons.dpapi`);
- the resolved universe has 89 rows, all with `sa_symbol`, and the first 10 are named in `ad-2`;
- there is NO `--no-sign-in` switch in `__main__.py` today.

**NOT cells:**
- bbg, wsj and barrons (the playbook's first light at 05:00 ET is `2.0.0_SA_COO~H`'s own act on Andrew's word, per cloud
  ruling section 0 item 3b);
- the warm-up in the harvester (waits on first light);
- sa batches 2+;
- the cloud host (phase 2).

## 45. ROUND 32 -- L5 DECOMPOSITION v3.12, over the round-31 analysis (`ledger/ROUND_ANALYSIS.round31.md` @309b2da963) + PRD v0.13 (the Friday addendum, ADMITTED)

**Issuer `2.0.0_SA_COO~H`**, 2026-10-01 ~05:3xZ. Seated by the CTO placement @`e18d3a4e6a` (fan-out cap 3).
- Round 31 is CLOSED. Andrew: the project "is not over until we beat captchas and have robust auth solution"; "we do not
  accept any defeat". BLOCKED is never a final state (`C-HV-NO-DEFEAT`).
- **Rulings carried** (analysis section 4 and its rulings): the 105-page sa ceiling is VOID; `error` joins the STOP set
  (`Z-W88-S3`); R7, sa keeps its route, and no new residential arm is opened.
- Series **`ae`**; slots **`~90`..`~92`**.

| analysis item | cell | order | class | slot | dispatch |
|---|---|---|---|---|---|
| 1 FWD-12 wrong-object repair (precondition) | `HVST-ae-1` | `ae-1` | LOCAL A, then WORLD B (quarantine + gold rebuild), pair | `~90` | A now; B on the pair over the merged code |
| 2 FWD-13 one browser identity | `HVST-ae-2` | `ae-2` | LOCAL | `~91` | now |
| 3 first-light grade + confound arm | `HVST-ae-3` | none: the issuer's direct act after the 09:00Z fire (analysis item 3) | WORLD (publisher traffic after 05:00 ET) | issuer | ~09:1xZ |
| 4 FWD-15 the site Z backfill driver, sa first | `HVST-ae-4` | `ae-4` | LOCAL A (code), then WORLD B (the sa run), pair | `~92` | A now (code has no data edge); B after `ae-1` B drains |
| 5 FWD-11 the challenge path for bbg, wsj, barrons + renewal | `HVST-ae-5` | `ae-5` | LOCAL A, then WORLD B, pair | `~91` (after `ae-2`) | A after `ae-2` drains and `HVST-ae-3` is graded |

**Fan-out: 3 workers over 2 dependency chains, cap 3** (placement). Chain A: `ae-1` -> `ae-4` B. Chain B: `ae-2`, `ae-3`
-> `ae-5`. `ae-4` A (code only) has no data edge, so it takes the third slot now; its WORLD run waits on `ae-1` B.

**Write sets (disjoint):**

| order | owns |
|---|---|
| `ae-1` | `publishers.py` (the sa leg + the sa page cap), `sa_quarantine.py` (new), `test_ae1_sa_listing_body.py` (new), the silver-read exclusion in `lib/research/harvest/publication_gold.py` |
| `ae-2` | `tab_transport.py` (new), `auth.py`, `contracts.json`, the three CRO REST clients' UA lines, `test_ae2_one_identity.py` (new) |
| `ae-4` | `backfill_driver.py` (new), `test_ae4_backfill_driver.py` (new) |
| `ae-5` | `verification.py`, `test_ae5_challenge_path.py` (new) |

**Hookups at the merge (no cell owns them):** the `publishers.py` session build selects `TabSession` for a publisher whose
contract reads `"transport": "tab"` (ae-2's export; `publishers.py` is ae-1's file).

**Premises measured at the cut:**
- sa silver: 85 rows over 66 parts; **38 WRONG-OBJECT** (listing-discovered, raw `/api/v3/articles/{news_id}` capture,
  title unequal to the stored listing hit: 32 with a differing title, all dated 2023; 6 with no stored hit, dated 2021).
  A DATE is not the signature: 4 genuine 2025 Lenovo items are listed in live mode. Oracle `round32/checks/ae1_common.py`.
- gold `article_security_mention` newest part `date=2026-09-30/part-20260930T134616Z`: 379 rows, 139 sa.
- **KEY SPACE (row `Z-S51`):** the collector universe (89 keys, `BA` / `security-<hash>`) and gold (`BA_US_Equity`, 71
  keys) share 0 keys; 32 of 89 names carry a ticker. FWD-14's census is graded here on the collector's own silver,
  keyed by `discovered_for`; the gold join is the CTO's to rule.
- depth baseline: 20 distinct sa articles since 2026-01-01 over universe keys; 3 of 89 names with any; 0 at 50+.
- the in-tab transport idiom exists (`verification.py:164`, `page.evaluate(fetch(url, {credentials:'include'}))`).

**Checks dry-run at the base (all FAIL as expected; they are build checks):** `ae-1.AC2` (38 of 85 outside a
quarantine), `ae-1.AC3` (no manifest), `ae-2.AC2` (`tab_transport` absent), `ae-4.AC2` (driver absent), `ae-4.AC3` (no
run summary; 20 = baseline), `ae-5.AC2` / `ae-5.AC3` (no record).

**NOT cells this round:** a residential arm for bbg/wsj/barrons/ft (Andrew's act, analysis section 5); FWD-14's own
census (graded when the driver's runs mature); the cloud host (phase 2).

## 46. ROUND 33 -- L5 DECOMPOSITION v3.13, over the round-32 analysis (`ledger/ROUND_ANALYSIS.round32.md` @749ec2c72e)

**Issuer `2.0.0_SA_COO~H`**, 2026-10-01 ~11:4xZ. FWD-14 (6 of 89 at 50+) and FWD-11 NOT MET; no defeat. Series **`af`**;
slots **`~90`..`~92`**; fan-out cap 3 (placement). The sa backfill (issuer, detached) keeps running throughout.

| analysis item | cell | order | class | slot | dispatch |
|---|---|---|---|---|---|
| 0 remove `verification_locator.py` | `HVST-af-0` | none: issuer direct act, DONE @ca957fb24a | LOCAL | issuer | done |
| 1 ft in-tab backfill | `HVST-af-1` | none: issuer direct act (unlock re-probe 12:02Z after the 429; then the detached driver) | WORLD | issuer | ~12:0xZ |
| 2 input-source instrument + a CHALLENGED pass (wsj/barrons re-mint already done in ae-5) | `HVST-af-2` | `af-2` | LOCAL A, WORLD B | `~91` | now |
| 3 Z-S51 census fix + the FWD-14 depth table over gold | `HVST-af-3` | `af-3` | LOCAL (S3 reads) | `~90` | now |
| 4 bbg date-ordered discovery (the census was measured in ae-5: wsj + bbg monthly sitemaps reach 2026-01) -> wire `discovery` into the collector's bbg/wsj listing + a live bbg job | `HVST-af-4` | `af-4` | LOCAL A, WORLD B | `~92` | now |

**Fan-out: 3 workers over 3 independent chains, cap 3.** Write sets: `af-2` `input_source.py` (new) + its test +
`verification.py`; `af-3` `depth_census.py` (new) + its test; `af-4` `publishers.py` (the bbg and wsj listing legs) +
`discovery.py` + its test. Disjoint.

**Checks dry-run at the base (all FAIL as expected):** `af-2.AC2` (no record), `af-3.AC2` (module absent), `af-4.AC2`
(no record). AC1 of each order is the worker's plant test.

**NOT cells:** the served gold rebuild (a SERVED act; COO half @534a521e45, CTO half asked) -- the issuer's act under
the pair; a residential arm (Andrew's act).

## 47. ROUND 34 -- L5 DECOMPOSITION v3.14, over the round-33 analysis (`ledger/ROUND_ANALYSIS.round33.md` @b25abce8d4)

**Issuer `2.0.0_SA_COO~H`**, 2026-10-01 ~13:3xZ. FWD-14 (6 of 89 at 50+) and FWD-11 (bbg only) NOT MET; no defeat.
Series **`ag`**. The sa and ft backfills (issuer, detached) keep running.

| analysis item | cell | order | class | slot | dispatch |
|---|---|---|---|---|---|
| 1 wsj/barrons re-mint + a challenged pass under the monitor | `HVST-ag-1` | `ag-1` | WORLD | `~91` | now |
| 2 ft and sa challenged passes under the monitor | `HVST-ag-2` | `ag-2` | LOCAL A (an ft solver if needed), WORLD B | `~90` | now |
| 3 bbg/wsj sitemap discovery feeding the driver | `HVST-ag-3` | none: issuer direct act -- the collector's tab legs already list through the sitemaps (af-4) and the driver calls the collector; the act is the bbg and wsj driver runs in their own runtime roots (row Z-W91-S14: one job per runtime), recorded as `~92/ag3_runs.json` | WORLD | issuer | now |

**Fan-out: 2 workers over 2 independent chains, cap 3** (cell 3 needs no worker). Write sets: `ag-1` the deliverables +
`verification.py` (a slider fix only if needed); `ag-2` the deliverables + `verification.py` (an ft solver) + its test.
`ag-1` and `ag-2` both MAY touch `verification.py` -> `ag-1` may not edit it (it records, it does not build); `ag-2` owns it.

**Checks dry-run at the base (all FAIL as expected):** `ag-1.AC2` (no record), `ag-2.AC2` (no record), `ag-3.AC2` (no
record).

**Bounds shared by both orders:** one seat per publisher (ag-1: wsj, barrons; ag-2: ft, sa; the issuer's ag-3 runs
take bbg and wsj -- so ag-1's wsj work runs FIRST, before the issuer's wsj driver run starts); the main runtime is
held by the ft backfill and `~92`'s runtime by the sa backfill -> every live job runs in its own runtime root.

## 48. ROUND 35 -- L5 DECOMPOSITION v3.15, over the round-34 analysis (`ledger/ROUND_ANALYSIS.round34.md` @6cbef26707)

**Issuer `2.0.0_SA_COO~H`**, 2026-10-01 ~15:4xZ. FWD-11 limb 1 MET for bbg/wsj/barrons; limb 2 open on all five;
FWD-14 unmet. Series **`ah`**. The sa, bbg and wsj drivers keep running; the ft driver is stopped (`STOP_FT`, 15:4xZ)
so `ah-3` holds ft alone.

| analysis item | cell | order | class | slot |
|---|---|---|---|---|
| 1 a real challenge DOM captured per publisher at load -> the planted fixture the real solver passes (limb 2b) | `HVST-ah-1` | `ah-1` | LOCAL A (capture hook), then the issuer drains A so the live drivers capture; B (fixture + solve test) | `~91` |
| 2 per-minute monitor windows; any minute with human input VOID; the limb-2a grade per publisher | `HVST-ah-2` | `ah-2` | LOCAL | `~90` |
| 3 ft: 324 of 357 rejected fetches in job 1 were `publisher_did_not_unlock_body` -- unlock the ft bodies | `HVST-ah-3` | `ah-3` | WORLD | `~92` |

**Fan-out: 3 of 3 chains, cap 3.** Write sets are disjoint: `ah-1` `verification.py`, `transport.py`,
`challenge_capture.py`, `fixtures/challenges/`; `ah-2` `load_window_grade.py`; `ah-3` `publishers.py`,
`tab_transport.py`, `contracts.json`. Each cell has its own test file.

**Checks dry-run at the base (all FAIL as expected):** `round35/checks/ah-1.AC2.py` (no captured fixture),
`ah-2.AC2.py` (no grader), `ah-3.AC2.py` (no ft record).

## 49. ROUND 36 -- L5 DECOMPOSITION v3.16, over the round-35 analysis (`ledger/ROUND_ANALYSIS.round35.md` @89539ccbc2)

**Issuer `2.0.0_SA_COO~H`**, 2026-10-01 ~19:5xZ. Series **`ai`**. Rulings 1-4 shape the cells; ruling 2 (the overnight
unattended run, 03:00-11:00Z) and ruling 6 (gold #3 at 20:00Z, #4 before Fri 13:00Z) are issuer acts; ruling 5 (the
Andrew verbatim record) landed @72b72eb0cf / @db9e2f7d43.

| analysis item | cell | order | class | slot |
|---|---|---|---|---|
| 1 limb 2a per minute, +/-1 guard band, 1,440 clean minutes, every clean-minute challenge passes | `HVST-ai-1` | `ai-1` | LOCAL | `~90` |
| 2 ft session longevity; the ft driver returns only after a 2-hour run with no logout | `HVST-ai-2` | `ai-2` | WORLD | `~92` |
| 3 capture-at-load armed on all five; same-vendor fixture equivalence for wsj/barrons; 2b reads OPEN (NO SAMPLE), never MET-BY-ABSENCE | `HVST-ai-3` | `ai-3` | LOCAL | `~91` |

**Fan-out: 3 of 3 chains, cap 3.** The write sets are disjoint:
- `ai-1`: `load_window_grade.py`.
- `ai-2`: `publishers.py`, `tab_transport.py`, `worker.py`, `contracts.json`.
- `ai-3`: `challenge_capture.py`, `verification.py`, `transport.py`.

Each cell has its own test file.

**Checks dry-run at the base (all FAIL as expected):** `round36/checks/ai-1.AC2.py` (the grader carries no
per-minute fields), `ai-2.AC2.py` (no record), `ai-3.AC2.py` (no all-five status).

### 49.1 ROUND 36 AMENDMENT 1 -- the bbg silver repair cell (CTO ruling msg 28084), 2026-10-01 ~23:3xZ

Row Z-S57 (@548ecf1e1c): 772 of 779 stored bbg articles are pending in the upload outbox on `JSONDecodeError`, with 0
uploaded. The in-tab bbg bodies are HTML and `silver_from_bronze` parses bbg as JSON. The CTO ruled YES to ONE
mid-round repair cell, bounded:
- a bbg HTML branch, with no change to the other publishers' JSON paths;
- plants on a real stored bbg body plus a JSON control;
- the drain printed before and after.

Gold #4 (the last under the signed pair) runs only after the drain, with a census of 0 gone and 0 changed outside the
new bbg rows. If the cell is not drained by 10:00Z, #4 runs without it, before 13:00Z.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-ai-4` bbg HTML silver branch | `ai-4` | SERVED (code LOCAL; the drain is the live driver's upload) | `~91` |

Base check `round36/checks/ai-4.AC2.py` before the cut: FAIL (772 stranded, 0 uploaded).

### 49.2 ROUND 36 AMENDMENT 2 -- the bbg drain batching cell (CTO ruling msg 28222), 2026-10-02 ~05:2xZ

Row Z-S58 (@18ee3ffbd5): after the ai-4 fix the bbg outbox drains at about 1 row per 90 s, and the rate falls as it
runs. Each pending row is its own `(source, run_stamp)` group, and each `silver_append` re-reads every bbg silver part
(576 parts, 69 MB). 288 rows left would take 7 h or more, past the 10:00Z bound for gold #4. The CTO ruled YES to ONE
mid-round repair cell, bounded:
- `uploads.py` `_run_articles` makes ONE `silver_append` per source per pass (`silver_append` already writes one part
  per fetch-date partition);
- it falls back to per-row appends on `SilverRowError`, so a W91-S19-class row cannot strand its batch;
- paths are `uploads.py` and its test only; risk SERVED;
- CONDITION: plant 1 proves the batched pass writes the SAME row set (keys plus values) as the per-row path on the same
  fixture. The part layout may differ, the rows may not. A row difference is a served-output change and needs
  never-widen sign-off.

The one real run at close is the live drain reaching 0 pending with gold-readable silver. Gold #4 stays on ruling
28084: it runs before 13:00Z, and without the rest of the drain if the drain has not finished by 10:00Z.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-ai-5` batched silver append per source | `ai-5` | SERVED (code LOCAL; the drain is the issuer's upload-harvest pass) | `~90` |

Base check `round36/checks/ai-5.AC2.py` before the cut: FAIL (see the issuance commit).

### 49.3 ROUND 36 AMENDMENT 3 -- the limb-2a grader per challenge (CTO ruling, self-drive tick 2 @bb3c328367), 2026-10-02 ~06:2xZ

The CTO ruled that FWD-11 limb 2a is graded PER CHALLENGE, answering ADJUDICATION_v45 section 2:
- a challenge is CLEAN when no hardware input occurs from 2 min before its presentation to 2 min after its
  resolution;
- a challenge with input in that band is VOID, and it voids only itself, never its hour or the run;
- 2a is MET when every non-void challenge passed and each publisher that presents challenges has at least one
  non-void challenge;
- a publisher that presents none stays MET-BY-ABSENCE.

The 24-clean-hour / 1,440-clean-minute count was the grader's own construction and is dropped. Limb 2b and session
renewal are unchanged. This seat amends the grader; `3.0.0_SA_CVO~Z` grades on it. No PRD half re-opens.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-ai-6` per-challenge +/-2 min grader | `ai-6` | LOCAL, DIRECT-ACT (one cell, under 300 product lines) | `~90` |

Base check `round36/checks/ai-6.AC2.py` before the cut: FAIL as expected (the grader emits the per-minute shape).

## 50. ROUND 37 -- the round-36 analysis enrichment list (`ledger/ROUND_ANALYSIS.round36.md` @e38e50aa55), 2026-10-02 ~07:0xZ

Round 36 is CLOSED and gold #4 is served. FWD-11 is NOT REALIZED. Three limbs hold it: ft limb (1); barrons limb 2a
(NOT_EVALUATED, because no barrons request falls in a monitor window); and limb 2b on wsj, barrons, ft and sa (no
challenge sampled). Ruling 4 says no cell provokes a challenge.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-aj-1` | `aj-1` | grader: anchor each band on the challenge's presentation (bbg emits `challenge_presented`; until it does, the HTTP 403 that precedes each pass); `requests` counted inside the monitor windows only; NOT_EVALUATED at 0 windowed requests (ruling 1) | LOCAL | worker `~90` |
| `HVST-aj-2` | issuer act (no TO: L7 orders go to Tier-2 seats only, LD-0521) | the load monitor back up now, and up for the life of FWD-11 (ruling 2) | LOCAL, issuer act | `2.0.0_SA_COO~H` |
| `HVST-aj-3` | issuer act (no TO, as round 34's ag-3 driver runs) | one barrons collection inside a monitor window (ruling 3) | WORLD, issuer act | `2.0.0_SA_COO~H` |
| `HVST-aj-4` | `aj-4` | the ft keep-alive run: 2 h from a sign-in Andrew solves by hand while present; one keep-alive event per page load (ruling 5) | WORLD, STAGED on Andrew | worker `~92` |

Dependencies:
- aj-3's grade reads aj-1's windowed `requests`, so aj-3 is GRADED after aj-1 merges; the run itself goes now.
- aj-4 waits on Andrew's presence for the hand-solved hCaptcha. No solver vendor is used (CTO 28235).

**Issuer amendments carried here (rulings 6 and 7, no cell):**
- **W91-S19 error text:** row Z-S63 carries it. Recurrence is measured as 1 of 830 bbg bodies, so no repair cell.
- **Worktree recipe (Z-W90-S11):** a sparse worktree for a HARVST cell is cut with this cone:
  `lib .tools org/missions infra/logic/registry org/standards org/tier1_exec/4.0.0_SA_CRO/scripts integrations/seekingalpha org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST org/modules/graph org/surprise_channel org/projects`.
  These are the paths the collector suite and the commit gates read, as measured by ~90 in ai-5.

**Load-monitor window record:** window1 2026-10-01 to ~10:48Z; window2 14:49Z to 2026-10-02 04:03Z, preserved as
`load_monitor.window2.json` before the restart; window3 opened 2026-10-02 06:52:23Z (pid 22892). All three are listed
in `.runtime/harvest-backfill/runtimes.json`. Round 36's windows are pinned for aj-1's AC2 in
`deliverables/2.0.0_SA_COO_H/round37/runtimes.round36_windows.json`.

**Checks dry-run at the base before the cut:**
- `round37/checks/aj-1.AC2.py` FAIL as expected (no `requests_counted`; barrons reads MET-BY-ABSENCE on 52 unwindowed
  requests).
- `aj-3.AC2.py` FAIL as expected (requests not windowed). The first draft PASSED at the base on the unwindowed count;
  the `requests_counted` marker was added so the check cannot pass before aj-1.
- `aj-4.AC2.py` FAIL as expected (no record).
- `aj-2.AC2.py` is the cell's own 10-minute proof, run after the cut.

**Issuer acts aj-2 and aj-3** carry no task order: to-pipeline-gate refuses a TO addressed to a Tier-1 seat. Each act's proof is its check under `round37/checks/`, run by the issuer, with the output committed beside it (`round37/aj-2.AC2.output.txt`, `round37/aj-3.AC2.output.txt`). aj-2 is done (06:52:23Z, pid 22892); aj-3 runs inside window3.

### 50.1 ROUND 37 AMENDMENT 1 -- cell 5: bbg failure capture + one bounded retry, and limb 2a PER RUN (CTO 28278; round-36 addendum ruling 8 @1c693565e7), 2026-10-02 ~07:4xZ

Row Z-S64 (@a92996d1f0): a clean, unassisted bbg press-and-hold failed at 06:59:52Z inside window3 (0 hardware events),
in run `20261002T065754Z-bbg-4f3bfa12bd`. The job ended `bot_check` with no solve event, and no capture exists. The
run stays UNCLASSIFIED (ruling 8c).

The CTO ruled YES to cell 5, folded with addendum ruling 8:
- every bbg bot_check reaches the in-tab solve, with its challenge events recorded;
- a failed solve writes a capture bundle before giving up, regardless of the hourly cap: DOM snapshot, screenshot,
  and the HTTP status and response headers of the challenge exchange;
- one bounded retry follows, 60-120 s later, recorded as a second challenge event;
- the grader grades limb 2a PER RUN: MET when a run inside a monitor window has every presented challenge non-void
  and passed. A failed run elsewhere does not void a passing one; it is printed as the window pass rate beside the
  verdict.

bbg restarts after the merge, under the monitor.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-aj-5` bbg failure capture + bounded retry + per-run grader | `aj-5` | SERVED (code LOCAL; it reaches the live bbg path at the next driver job) | `~90` |

Base check `round37/checks/aj-5.AC2.py` before the cut: FAIL as expected (the grader has no `grain` and no per-run
entries).

### 50.2 ROUND 37 AMENDMENT 2 -- cell 6: the ft sign-in via the NopeCHA browser extension (CTO 28484; VEW-1), 2026-10-02 ~13:3xZ

Andrew permanently whitelisted NopeCHA for egress (~13:08Z, record @179990b502; `org/ref/VENDOR_EGRESS_WHITELIST.yaml`
VEW-1). aj-4's unattended sign-in then failed (row Z-W92-S18, records @5d61b62795): `nopecha.Token.solve` returned
error 19, "This API endpoint has been discontinued" (1 call, 0 Kimi). No session existed, so the 2 h run never started.

The CTO ruled YES to cell 6 (WORLD, workstream ftsolver):
- the NopeCHA browser extension is loaded into the ft Chrome profile with the key from Secrets;
- the Recognition API is the fallback;
- Kimi and vision stay out.

Criteria: the extension loads; a planted hCaptcha is solved with 0 Token API calls; ONE real unattended ft sign-in,
recorded with its challenge events (ruling 8b).

Placement: the extension route is built in HARVST's own `lib/opal_data_harvest/`, and the ~92 sign-in harness calls
it. The CRO's `org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py` (the Token API caller, authored by
4.0.0_SA_CRO~Z) is NOT in the write surface. If the collector's own renewal must route through it, that is a row and
an ask to its owner.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-aj-6` ft sign-in via the NopeCHA extension | `aj-6` | WORLD | `~92` |

Base check `round37/checks/aj-6.AC2.py` before the cut: FAIL as expected (no record).

**50.2 AMENDED 2026-10-02 ~13:3xZ (Andrew-direct "bETTER IDEA, LETS USE A NEW SOLVER", record @9bc0e127be):** cell aj-6 is
re-pointed from the NopeCHA browser extension to the Ocilar hCaptcha API (`POST https://api.ocilar.com/api/v1/solve/hcaptcha`).
The key is in Secrets `ocilar/credentials` (us-east-1). The write set is `lib/opal_data_harvest/ocilar_hcaptcha.py` plus
its plants and the ~92 deliverables. The criteria shape is unchanged: plants, then ONE real unattended ft sign-in with
its challenge events, `solved_by` ocilar, and 0 NopeCHA Token / Kimi / vision calls.

### 50.3 ROUND 37 AMENDMENT 3 -- cell 7: title + published_precision into the gold mention rows (CTO track-C ruling msg 28509; RESAPP r62 addendum @40e1d622aa), 2026-10-02 ~14:1xZ

Track C was ruled A after 4.0.0_SA_CRO~Z's research (@adb64006ed). Step 1 is HARVST's: `title` (VERBATIM, rule 17b)
and `published_precision` join `GOLD_MENTION_SCHEMA` and the gold mention rows. Then gold is rebuilt under a NEW
never-widen pair, because the round-32 pair's 4 rebuilds are spent. The CTO half is owed. Step 2 (RESAPP round 63,
2.0.0_SA_COO~Z: the day route reads the headline from gold) lands after it.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-aj-7` title + published_precision in gold mention rows | `aj-7` | SERVED (code LOCAL; served gold moves only at rebuild #5, under its own pair) | `~90` |

**Issuer act after the merge: rebuild #5.**
1. A round-37 signing dry run whose rule permits a served row to differ ONLY by gaining `title` and
   `published_precision` (every pre-existing field equal), gone 0, and daily OTHER 0.
2. The COO never-widen half names the blast radius: every served mention row gains two fields; nothing else moves; the
   rollback is the BEFORE snapshot as a newer part. The CTO half is owed.
3. The act, under the pair.

Base check `round37/checks/aj-7.AC2.py` before the cut: FAIL as expected (the schema lacks both fields).

### 50.4 ROUND 37 AMENDMENT 4 -- cell 8: barrons silver dict titles (CTO 28525; row Z-W90-S17), 2026-10-02 ~14:3xZ

aj-7's AC2 surfaced it, and the BASE builder fails identically. Barrons silver holds 164 rows, and 149 of them carry
`title` as `{'text': ...}`, all from today's 07:06Z+ aj-3 run. `publication_gold._match_counts` raises TypeError on
them, so no gold rebuild can run. The cause is in `silver_from_bronze._extract_barrons`: it takes `headline` raw,
while `_extract_wsj` unwraps a dict headline through `typed_text`.

The CTO ruled YES (SERVED, workstream barronstitle), with three conditions:
1. The re-derivation touches exactly the 149 dict-title rows (manifest 149 of 149), and the other 15 barrons rows
   and every other publisher are untouched.
2. Plants show a dict title unwraps, a string title passes unchanged, and the base builder no longer raises.
3. Rebuild #5 carries the never-widen pair.

| cell | order | class | slot |
|---|---|---|---|
| `HVST-aj-8` barrons dict title -> string | `aj-8` | SERVED (code LOCAL; silver is re-derived by the issuer) | `~90` |

Issuer act after the merge:
1. Snapshot the 15 others' record_hash and the 149 targets into `round37/aj8_rederive_manifest.json`.
2. Re-pend exactly those 149 outbox rows in `.runtime/opal-data-harvest`.
3. Run `upload-harvest` (the bronze put is skipped; silver is re-appended).
4. Run AC2.

Base check `round37/checks/aj-8.AC2.py`: FAIL as expected (no manifest).

## 51. ROUND 38 -- the round-37 analysis enrichment list (`ledger/ROUND_ANALYSIS.round37.md` @29fbb123e0), PRD v0.15, 2026-10-02 ~19:5xZ

Round 37 is CLOSED (CVO slug 28694; ADJUDICATION_v49 @76f4381bce). FWD-11 is NOT REALIZED:
- ft limb (1) is a QUALIFIED WAIT on HVST-RECHECK-OCILAR-1 (2026-11-01);
- CRO~Z researches alternatives, and no ft cell is cut until that research lands;
- (2b) is organic only.

This round cuts the enrichment list's items 1 to 3 in ONE issuance. Item 4 (ft) is not cut, per ruling 3.

| cell | order | what | class | slot |
|---|---|---|---|---|
| `HVST-ak-1` | `ak-1` | FWD-16: `finbert_sentiment.py` (the scorer client over `opal-news-ai-sentiment`, the append-only `article_sentiment` score store keyed by `record_hash`, a `score`/`census` CLI); the 3 tone fields on every gold mention row | SERVED (code LOCAL; 3 live Lambda calls in AC2, no write) | `~90` |
| `HVST-ak-2` | `ak-2` | FWD-17: `window_tone.py`; `chatter_window` per name per 30/90/365-day window ending at T-1; articles_total, scored, voters (non-neutral, no threshold), tone over voters (null at 0 voters); a stated served start | SERVED (code LOCAL) | `~92` |
| `HVST-ak-3` | `ak-3` | FWD-6 density: a read-only census of spikes against dry-built and served events; the spike definition is fixed at the cut at 2x and 3x | LOCAL | `~91` |

**Fan-out: 3 of 3 chains, cap 8.**
- Chain A (ak-1) and chain B (ak-2) share ONE interface, fixed here: `finbert_sentiment.latest_scores(client=None)`
  returns `{record_hash: {"label", "score", "scorer"}}`, with the score signed (+conf / -conf / 0.0 for neutral).
  ak-2 imports it lazily and injects it in tests, so the two chains run in parallel.
- The write surfaces are disjoint: ak-1 owns `publication_gold.py`; ak-2 owns a new module only; ak-3 owns its
  deliverables only.

**The IAM invoke-grant cell (analysis item 1) is NOT cut.** The identity that runs HARVST gold builds on site-Z (IAM
user `Andrew_Berman`) DryRun-invoked `opal-news-ai-sentiment` at 19:4xZ and got StatusCode 204. The grant act would
move nothing: a ZERO with its cause named. A scheduled gold producer's role, when one exists, will need the grant.
That is carried, not cut.

**Rule 30:** both new gold tables, `article_sentiment` and `chatter_window`, are addressed through `store.address_of`,
which wraps `opal_naming.address()`. The scope `harvest` and the systems `amgt` and `harvest` are registered. The
table is a free snake_case segment, so no registry row is owed (`opal_naming.py:1570-1574`).

**Substrate card (rule 28): `opal-news-ai-sentiment`.**
- PROCESS: FinBERT, one text per synchronous call. The news pipeline drives it 14x a day through
  `finbert-batch-processor`; HARVST calls it on demand.
- ARTIFACT: no persistence of its own. HARVST persists to gold `article_sentiment` at
  `amgt/harvest/gold/article_sentiment/`.
- TRUST:
  - coverage: every silver article with a title or text;
  - key: `record_hash`;
  - failure mode: a non-200 or exception is an ERROR row, never a neutral;
  - its contract is INFERRED from the caller (the container source is not in the repo), so ak-1's AC2 measures it.
  - owner: the news pipeline (`infra/aws/terraform/news-pipeline/lambdas.tf:246-268`).

**Observation for ak-1** (row filed at the cut): `record_hash` hashes every silver column except
bronze_key/fetched_at/record_hash, `run_stamp` included (`store.py:330-334`; `silver_from_bronze.py:289`). A re-fetch
of unchanged text is therefore a new version, and FWD-16's letter re-scores it. FinBERT is deterministic, so the tone
read is unchanged and only the call is spent.

**Issuer acts after the merges (no TO):**
1. **The corpus scoring:** `finbert_sentiment score` live, on a measured sample first for throughput, then the corpus.
2. **A gold rebuild** under a NEW never-widen pair (COO half by this seat after a signing dry run; CTO half owed):
   - every served mention row gains the 3 tone fields and nothing else moves;
   - the first `chatter_window` snapshot;
   - the served `chatter_event` rebuild, if ak-3's census shows the dry-built events cover spikes materially better.
3. **The real run at close:** the `census` subcommand (scored / unscorable / total) and the window rows for the
   validation security (Lenovo) read from served gold.

**Checks dry-run at the base before the cut** (all FAIL as expected):
- `round38/checks/ak-1.AC2.py`: the module is absent;
- `ak-1.AC3.py`: the schema lacks the 3 fields;
- `ak-2.AC2.py`: the module is absent;
- `ak-3.AC2.py`: there is no census.

Positive control on their live read paths:
- served `chatter_event` has 8 rows;
- served mention has 23,691 rows, 715 of them for the 5 check securities;
- `published_utc` is a datetime;
- T-1 = 2026-10-01.

## 52. ROUND 39 -- the round-38 analysis enrichment list (`ledger/ROUND_ANALYSIS.round38.md` @3da5563fd8), PRD v0.17, 2026-10-02 ~23:5xZ

Round 38 is CLOSED (CVO slug 28797; ADJUDICATION_v50 @8f911c0199).
ARMED went from 10 to 2; Z-S11 was fixed in the checker @9edfeae04d.

| cell | order | what | class | slot |
|---|---|---|---|---|
| `HVST-al-1` | `al-1` | Z-W91-S10 (placed by Z-S79): a Dow Jones 200 listing with 0 parseable hits sets `listing_empty_200` (status-gated, reset per call); the job records the event and status; NOT a driver STOP status; planted pages only | LOCAL | `~91` |
| `HVST-al-2` | `al-2` | FWD-16 v0.17: tone keyed to `content_key` = sha256 of the exact `article_text` scored (Z-S67); `sentiment_content_key` on the gold mention row; window join by it; 0 Lambda calls | SERVED (code LOCAL; served at a later rebuild under its own pair) | `~90` |

**Fan-out: 2 of 2 chains, cap 8.** The write surfaces are disjoint: al-1 owns `publishers.py`; al-2 owns
`finbert_sentiment.py`, `publication_gold.py` and `window_tone.py`.

**Remediation folded, no cell:** Z-S68 (the 3 stale timeline-day tests) was repaired by `2.0.0_SA_COO~Z` @949b24cadb, as
the RESAPP am-1 regression repair. The research suite reads 334 passed and 0 failed at the cut. Row Z-S81 resolves Z-S68.

**Hygiene at the drain, not a TO criterion:** `round39/checks/suites_green.py` (both suites, 0 failed). At the cut it
reads 334 passed (research) and 597 passed with 3 skipped (collector).

**Checks dry-run at the base before the cut (all FAIL as expected):**
- `round39/checks/al-1.AC2.py`: no `LISTING_EMPTY_200`, no flag;
- `al-2.AC2.py`: `content_key` is absent;
- `al-2.AC3.py`: `build_mention` has no `sentiment_by_key`.

## 53. ROUND 40 -- the round-39 analysis enrichment list (`ledger/ROUND_ANALYSIS.round39.md` @481c0a83e8), 2026-10-03 ~01:3xZ

Round 39 is CLOSED (CVO slug 28854). ARMED reads 0 over 294 items. The enrichment list has ONE LOCAL cell.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-am-1` | DIRECT ACT (LOCAL, under the size floor; `/dispatch` Step 2) | Z-C-S69: at most ONE null-label marker row per key-less (no-text) article. `finbert_sentiment.marked_article_keys` reads the marked `article_key`s from the written parts; `score_missing(..., marked_keys=)` skips them and dedupes within a run; `score` passes them, and its dry-run count excludes them | LOCAL | `2.0.0_SA_COO~H` |

Proof: `deliverables/2.0.0_SA_COO_H/round40/am-1.proof.txt`.
- `test_am1_marker_once.py`, 3 of 3 passed:
  - two runs over a planted key-less pair give 1 marker each and 0 calls;
  - a re-silvered key-less article is marked once in one run;
  - a scorable article is still scored once.
- Mutant (the skip removed): 3 failed.
- Research suite: 347 passed.
- 0 Lambda calls; no S3 write; no publisher text.

## 54. ROUND 41 -- Andrew-direct ~20:3xZ card 2 ("yes to all recommendations"), 2026-10-03 ~20:4xZ

**Authority:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261003_20xxZ_YES_TO_ALL_SEVEN_OPEN_CALL_RECS.md`
@9fe6e6f111, card 2: "HARVST: run FinBERT scoring over the stored articles, and the event rebuild" -- yes. Relayed by
`1.0.0_SA_CTO~Z` msg 29001: "cut and run them through the canonical loop; a served gold move takes its never-widen
pair". **Not covered:** FT collection and STOP_FT (unchanged; no collector runs).

Issuer `2.0.0_SA_COO~H`. Series **`an`**. Three issuer DIRECT ACTS, one chain (an-1 -> an-2 -> an-3), fan-out 1 of 1, cap 8.

| cell | what | class | gate |
|---|---|---|---|
| `HVST-an-1` | FinBERT scoring of the stored silver articles: `python -m lib.research.harvest.finbert_sentiment score --as-of 2026-10-03`, in `--limit` batches so a failed run loses one batch. Dry run at the cut: 13,235 silver articles, 0 already scored, 13,224 to score, 11 no-text markers. Calls the Opal Lambda `opal-news-ai-sentiment` only. Writes new parts of gold `article_sentiment`, a table no served route reads. | WORLD (Opal Lambda + S3 write, nothing served) | the dry run, then the batch receipts |
| `HVST-an-2` | Served gold rebuild of `article_security_mention` + `chatter_daily` over the scores (FWD-16): every mention row gains the 4 `sentiment_*` fields. | SERVED | never-widen pair (COO half + CTO half), rule checked before and after the write |
| `HVST-an-3` | Served `chatter_event` rebuild over the newest mention snapshot (the event rebuild). Served at the cut: 8 rows. | SERVED | never-widen pair (COO half + CTO half) |

Evidence folder: `deliverables/2.0.0_SA_COO_H/round41/`.

## 55. ROUND 42 -- the round-41 analysis enrichment list (`ledger/ROUND_ANALYSIS.round41.md` @98f36bf49a), 2026-10-03 ~23:5xZ

Round 41 is CLOSED (CVO slug 29069, ADJUDICATION_v53 @716910082a): FWD-16 and FWD-6 REALIZED. The enrichment list has ONE item
(ruling 2): FWD-17 `chatter_window`. Authority chain: Andrew's card 2 (@9fe6e6f111) as ruled by the CTO (ruling 2: the window tone
is the step that turns the article scores into the tone the pages read). Collection stays with Andrew.

Issuer `2.0.0_SA_COO~H`. Series **`ao`**. One chain, fan-out 1 of 1, cap 8. Issuer DIRECT ACT (the builder exists, HVST-ak-2).

| cell | what | class | gate |
|---|---|---|---|
| `HVST-ao-1` | FWD-17: the first served `chatter_window` part through its builder (`python -m lib.research.harvest.window_tone build`): per security, 30/90/365-day windows ending T-1; voters = non-neutral scored articles; tone = mean signed score over voters, null at 0 voters. Plant: `test_ak2_window_tone.py::test_i_all_neutral_name_is_voters_zero_tone_none_in_every_window` (an all-neutral name reads voters 0, tone null, never 0.0), plus the count of real rows with scored > 0 and voters 0 in the build. | SERVED (a new gold table; no route reads it yet) | never-widen pair; the dry run recomputes every row independently from the mention snapshot and the scores (MISMATCH 0) |

RESAPP's chatter route then reads `chatter_window` as RESAPP's own cell (FWD-36's tone limb), not this project's.
Evidence folder: `deliverables/2.0.0_SA_COO_H/round42/`.

## 56. ROUND 43 -- the round-42 analysis enrichment list (`ledger/ROUND_ANALYSIS.round42.md` @bad41f3f91), 2026-10-04 ~00:5xZ

Round 42 is CLOSED (CVO slug 29096, ADJUDICATION_v54 @5428dcb51f). FWD-17 is met on 206 of 212 covered names; the 6 with 0
mentions (8766_JP, BKRKY_US, EXPD_US, ICT_PM, KCDMY_US, ST_SP) carry no window row, and absent is not zero (Z-C-S74, ruling 1).

Issuer `2.0.0_SA_COO~H`. Series **`ap`**. One chain, fan-out 1 of 1, cap 8. Issuer DIRECT ACT (code under the size floor, then
the served write).

| cell | what | class | gate |
|---|---|---|---|
| `HVST-ap-1` | `window_tone.build_window_rows(..., security_keys=)`: every universe name gets its 3 rows; a name with 0 mentions reads articles_total 0, scored 0, voters 0, tone null, scorer null. `build_window` and the dry-run CLI pass the universe keys. Plant: a universe name with 0 mentions reads three explicit zero rows (`test_ak2_window_tone.py`). Then the served write: a new `chatter_window` part of 212 x 3 = 636 rows, the 618 served rows unchanged. | SERVED (no route reads the table yet) | never-widen pair; dry run: 618 served rows byte-equal, 18 added rows all explicit zeros on the 6 names, independent recompute MISMATCH 0 |

Evidence folder: `deliverables/2.0.0_SA_COO_H/round43/`.

## 57. ROUND 44 -- the round-43 analysis enrichment list (`ledger/ROUND_ANALYSIS.round43.md` @9cacf32e54), 2026-10-04 ~03:2xZ

Round 43 is CLOSED (CVO slug 29129, ADJUDICATION_v55 @30f9a5e5f5): FWD-17 REALIZED. Board: REALIZED 5 of 17; open without new
collection 4 (FWD-2, 5, 7, 12); open needing new collection 8 (held on Andrew's word: "We will discuss internally on how to
proceed with further data collection after review").

Issuer `2.0.0_SA_COO~H`. Series **`aq`**. Four READ cells, independent: fan-out 4 of 4 chains, cap 8. Each reads first and
writes its evidence to `deliverables/2.0.0_SA_COO_H/round44/` only; a repair cell is cut only where a read fails (a served write
under a pair). No collection, no vendor call, no S3 write, no publisher request.

| cell | FWD | read | class |
|---|---|---|---|
| `HVST-aq-1` | FWD-2 | Field census over the stored originals (bronze) per publisher: every field the publisher sent (language, paywall flags, the publisher's ticker tags, sentiment, themes, summary where sent) is typed in the queryable table (silver/gold), and a query by company and date returns it. Missing fields are named per publisher with their count. | LOCAL read |
| `HVST-aq-2` | FWD-5 | A served read of a company's timeline (`opal-amgt-scoped-api`): pick a day; its articles are listed strongest first (the order key named and checked on every listed article). Graded at L9 as judgment. | SERVED read |
| `HVST-aq-3` | FWD-7 | The basis of the served chatter rank (graded daily table or raw count), read from the route code at HEAD and the served response; plus one planted pair (a passing mention in many articles vs a subject of a few) through the rank's own function. | SERVED read + LOCAL plant |
| `HVST-aq-4` | FWD-12 | The grade from the round-32 evidence for (a)-(d), and (d)'s re-check over every stored sa row from storage only. Any limb that needs a publisher request is named. | LOCAL read |

## 58. ROUND 45 -- the round-44 analysis enrichment list (`ledger/ROUND_ANALYSIS.round44.md` @ed9efe80ea), 2026-10-04 ~20:5xZ

Round 44 is CLOSED (CVO slug 29208, ADJUDICATION_v56 @876c7d30e1); FWD-5 is REALIZED. Board: REALIZED 6 of 17; open without new
collection 2 (FWD-2, FWD-12); open needing new collection 9, held on Andrew's word ("We will discuss internally on how to proceed
with further data collection after review"). FWD-7 is in the collection partition (ruling 2).

Issuer `2.0.0_SA_COO~H`. Series **`ar`**. Three cells, independent: fan-out 3 of 3 chains, cap 8; ONE worker (`~93`, ar-1) and
two issuer acts (ar-2, ar-3; L7 orders go to Tier-2 seats only, LD-0521). No collection, no vendor call, no backfill.

| cell | order | FWD | what | class | executes |
|---|---|---|---|---|---|
| `HVST-ar-1` | `ar-1` | FWD-2 | Type every lost field (barrons first; the bbg, ft and wsj page-level descriptors; ft's JSON-LD publisher block) in `silver_from_bronze.py` and the publisher field maps; diagnose the 3 sampled wsj originals with no silver row; an in-memory field census over the stored originals reads 0 lost; a dry-run re-derivation manifest over every stored original of the four publishers (pre-existing columns changed 0). THEN the issuer's served re-derivation under a never-widen pair, graded by the same census over served silver. | SERVED (pair at the drain) | worker `~93`, then issuer |
| `HVST-ar-2` | issuer act | FWD-12 (c) | `config.json` `max_listing_pages.sa` 25 -> 200; `worker.listing_page_cap()` carries the backfill branch's expression; plants `test_ar2_sa_listing_cap.py` (5 pass; 2 fail with the config reverted). (a), (b), (d) re-read with the aq-4 instrument. | LOCAL (direct act) | `2.0.0_SA_COO~H` |
| `HVST-ar-3` | issuer act | FWD-9 (row Z-S82, CTO msg 29207) | The served clip at STORE_START, measured on the served code path before any change: `checks/ar-3.AC1.py` runs `scoped_amgt._serve_timeline_body` for every name over live gold. | LOCAL read (ruled down from SERVED, below) | `2.0.0_SA_COO~H` |

**Issuer ruling on ar-3 (inside this decomposition; no gate limb graded it, recorded here):** the analysis cut the clip as a
SERVED change under a pair. Measured first, the two WIRED routes already clip at the floor by construction:
- the range route clamps `from` at `BACKFILL_FLOOR` (2026-01-01) and drops every event whose `last_day` precedes it;
- `chatter_daily` starts at the floor, so the day route answers TIMELINE_DAY_NOT_FOUND on every pre-2026 day;
- the event route is NOT wired (`lib/research/api/scoped_amgt.py:5308`).

Over 212 names: 0 leaks; 496 events served; the 11 pre-2026 events (7 names: ASML_NA, ASML_US, COST, FDX, HD, NVDA, TSLA) are
never served (0 cross the floor); 1,355 day-route probes on pre-2026 days serve no data. Clipped and never served: 11
`chatter_event` rows and 19,967 `article_security_mention` rows on 202 names; gold is untouched. A served change would be a 0-diff
deploy, so no code and no deploy is cut (a verified DELTA=0 needs no hold). The one future-reachable leak is an event that crosses
the floor (0 today); it is named, not built. Row Z-S84 corrects Z-S82's "events and the timeline can show pre-2026 days".

Worktree recipe for ar-1: the sparse cone of section 50. Evidence folder: `deliverables/2.0.0_SA_COO_H/round45/`.

**Checks dry-run at the base before the cut:**
- `round45/checks/ar-1.AC2.py` base: FAIL as expected (the in-memory census script is absent).
- `round45/checks/ar-1.AC3.py` base: FAIL as expected (script absent). Its grader `ar1_grade.py` over the base's served-silver
  census (`round44/aq-1.field_census.json`) reads FAIL: lost per publisher barrons 39, bbg 10, ft 9, sa 0, wsj 20.
- `round45/checks/ar-3.AC1.py` base: PASS as expected (a bound check; 0 leaks).

## 59. ROUND 46 -- the round-45 analysis enrichment list (`ledger/ROUND_ANALYSIS.round45.md` @4f01f5ab8d), 2026-10-05 ~01:0xZ

Round 45 is CLOSED (CVO slug 29353, ADJUDICATION_v57 @f38cf87fbf); FWD-2 and FWD-12 are REALIZED. Board: REALIZED 8 of 17; open
without new collection 0; open needing new collection 9 (FWD-1, 3, 7, 9, 10, 11, 13, 14, 15).

Issuer `2.0.0_SA_COO~H`. Series **`as`**. Fan-out 3 of 3 chains, cap 8.
- One worker, `~94`, on as-1.
- Three issuer acts. L7 orders go to Tier-2 seats only (LD-0521).
- as-1b is chained after as-1; it is the run, and it waits on the run universe.

| cell | order | FWD | what | class | executes |
|---|---|---|---|---|---|
| `HVST-as-1` | `as-1` | FWD-7 (+ the 9 collection outcomes) | **The run's universe.** The collector's universe becomes the RANK's 191 names (pool `universe/v1/2026-09-16.json`). Every security carries `security_key` = the pool key, which is the declared-set join key that `worker.py:467` stamps as `gold_security_key`. The search identities (company, ticker, aliases, sa_symbol) are resolved with NO vendor call, and per-publisher coverage is printed. The driver's dry run plans 191 x 5 jobs. | LOCAL | worker `~94` |
| `HVST-as-1b` | issuer act, after as-1 merges | FWD-1, 3, 7, 9, 10, 11, 13, 14, 15 | **THE collection run** (CTO ruling @a142505a06; Andrew @441338fdf7: ONE universe-scope run per publisher). Gates before the first request: 191/191 resolved, and the sa bound printed (191 x 220 = 42,020 requests at most, about 9.7 days at 4,320/day; the 2026-01-01 floor stops most names far earlier). It runs under its own never-widen pair: bronze and silver append through the uploader, plus run records. No recurring cadence and no new mechanism. | WORLD (publisher egress on Andrew's word) | `2.0.0_SA_COO~H` |
| `HVST-as-2` | issuer act | FWD-17 (RESAPP FWD-36, routed @2db6fd3e3d ruling 2) | `chatter_window` built over the rank universe UNION RESAPP's covered set (`covered_universe.covered_security_keys()`, 95). A 0-mention name gets FWD-17's explicit zero row. It goes through the existing `window_tone build --securities-json` under a never-widen pair, with no code change. If the served table's 212 names are not all in the union, they stay in the list (GONE 0). | SERVED | `2.0.0_SA_COO~H` |
| `HVST-as-3` | issuer act | (instrument, row Z-S85) | The named field census (`round45/ar-1.field_census.reader_rule.py`) chooses the served row through one function that uses `store.supersedes`. Plant: on barrons key 00b99ce0, the tie reads the `-r2` part (74 columns); the run_stamp rule as a mutant reads the pre-round part. | LOCAL (direct act) | `2.0.0_SA_COO~H` |

Worktree recipe for as-1: the sparse cone of section 50. Evidence folder: `deliverables/2.0.0_SA_COO_H/round46/`.

**Checks dry-run at the base before the cut:**
- `round46/checks/as-1.AC2.py` base: FAIL as expected. The collector universe has 89 securities, 0 carrying `security_key`, and
  0 of the 191 rank names are resolved.
- `round46/checks/as-1.AC3.py` base: FAIL as expected. The driver dry run plans UNIVERSE 89, 445 PLAN lines, NETWORK CALLS 0.

## 60. ROUND 47 -- the round-46 analysis enrichment list (`ledger/ROUND_ANALYSIS.round46.md` @585391af7f), 2026-10-05 ~06:1xZ

Round 46 is CLOSED. Board: REALIZED 8 of 17; open without new collection 0; open needing new collection 9. The collection run
(as-1b, pair COO @30ed1c8b83 + CTO @138b152f2a) continues across the boundary. ft is held (Andrew-direct @b023b75324).

Issuer `2.0.0_SA_COO~H`. Series **`at`**.
- **Fan-out:** 1 of 2 chains, cap 8. One worker, `~95`, on at-1; two issuer acts. at-2 chains after at-1.
- **Ruling 2 (standing, no cell):** a transport-class stop on any leg is resumed by the issuer from the leg's own checkpoint, as
  the same run.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-at-1` | `at-1` | **Batched listing upload** (row Z-S86, ruling 1). `HarvestUploader._run_listings` makes ONE `silver_append` per SOURCE per pass, at the batch's greatest run_stamp, isolating untableable rows locally first, exactly as the article path does since HVST-ai-5. Plants: identical silver ROWS on a planted set (only the object count differs) and prefix reads = 1 per source per pass. Timing control: 100 listing pages, old against new. | LOCAL | worker `~95` |
| `HVST-at-2` | issuer act, after at-1 merges | **The landing:** place `R46_STOP_SA_BARRONS`, `R46_STOP_BBG` and `R46_STOP_WSJ`; wait until every driver ends after its current job (no harvest code lands while a leg runs, because each job spawns from the working tree); merge; then resume each leg from its OWN checkpoint, as the same run (CTO condition 1). ft stays held. | WORLD (the run's own legs) | `2.0.0_SA_COO~H` |
| `HVST-at-3` | issuer act, at the round-47 drain | **The per-leg report** (condition 4): concluded and stopped jobs by status out of 191, plus `publisher_universe_verdicts` per publisher (`round46/as-1b.report.py`). | LOCAL read | `2.0.0_SA_COO~H` |

**Checks dry-run at the base before the cut:**
- `round47/checks/at-1.AC2.py` base: FAIL as expected (the timing control is absent).

### 60.1 AMENDMENT 1 (issuer, 2026-10-05 ~06:5xZ): cell `HVST-at-4`, the silver_append column-union fix (row Z-W95-S2)

Worker ~95's row Z-W95-S2 (ARMED; disarm owner the issuer): `pa.Table.from_pylist` takes its columns from the FIRST row.
Measured in pyarrow 24.0.0: `[{'a':1},{'a':2,'b':3}]` -> `['a']`, and row 2's `b` is gone. `store.silver_append` builds each date
group that way, so every multi-row append (the article path since HVST-ai-5, the live collection run's uploads, and round 45's
re-derivation bins) can silently drop a later row's extra columns. Bronze keeps every original, so the loss is recoverable by
re-derivation.
- Round 45's VERIFY could not see it: it compared record_hash, which is computed from the row before the write, and only the
  columns PRESENT in the served row.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-at-4` | issuer act | `store.silver_append` gives every row of a date group the union of the group's keys (first-seen order) before the table is built. Plants 4/4; the mutant drops `dek`. Held on branch `coo-h-r47-store-union` @46f165ea6e. It lands WITH at-1 through at-2 (every leg stopped). | SERVED (all silver writers) -> CTO decision | `2.0.0_SA_COO~H` |

- **The damage census** (`round47/at-4.dropped_columns_census.py`, read-only) rebuilds every served article row written since
  2026-10-04T23:00Z from its original and counts the dropped keys. Its result decides the re-derivation scope for round 48.
- **Gate limb:** none graded this amendment. It is recorded here.

### 60.2 AMENDMENT 2 (issuer, 2026-10-05 ~16:5xZ): cell `HVST-at-5`, widen the run universe by the approved research names

Andrew-direct 2026-10-05 ~16:3xZ, verbatim, answering "Do you want me to add the 59?": "Yes I do". The run universe
(`rank_universe_20260916.json`, 191 names) predates the research-name resolutions in `lib/research/identity/registrations.json`
(56 approved resolutions, @b7819604e0 + @505fc14404, 2026-09-24; plus folders added after the 2026-09-16 snapshot).
- Measured at the build: 16 of the 56 were ALREADY in the run under their fund-holding keys (for example Netflix, Visa,
  Mastercard, TSM). The widening therefore ADDS 43 names: 40 of the 56, plus Quanta PWR US, AIA 1299 HK and Hitachi 6501 JP.
  Universe 191 -> 234. The 191 original identity records are byte-identical (same collector keys).
- AIA and Hitachi carry no SA symbol (rule R3), so their sa jobs have nothing to search; the other publishers search by name.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-at-5` | issuer act | `round47/at-5.widen_universe.py` writes `round47/rank_universe_20261005.json` + `rank_universe_identity_20261005.json` (no vendor or S3 call); `config.json` points `universe_source` / `symbol_resolution_source` at them. Lands after PARITY CLOSED; then each leg is stopped at a job boundary by its stop file and relaunched from its OWN checkpoint (dry-run plans: sa 221, barrons 194, bbg 185, wsj 135 pairs). ft stays held (Andrew-direct @b023b75324). | LOCAL code + config; the added collection is the run Andrew widened | `2.0.0_SA_COO~H` |

- **Not moved:** the declared-set denominator. `publisher_universe_verdicts` reads the pool universe (`universe/v1/2026-09-16.json`,
  191 resolved keys), not this file; rebuilding that pool universe is the identity owner's act, not this cell's.
- **Gate limb:** none graded this amendment. It is recorded here.

## 61. ROUND 48 -- the round-47 analysis enrichment list (`ledger/ROUND_ANALYSIS.round47.md` @acc5c6e750), 2026-10-06 ~03:0xZ

Round 47 is CLOSED. Board: REALIZED 8 of 17; 9 a qualified wait on Andrew's presence. Every collection leg is STOPPED (row Z-S89,
CTO @69ce080222). A leg resumes only once Andrew hand-solves its challenge, and sa only once its account answers 200. The FWD-7 bar
is 95% of the run universe (223 of 234), per ruling 1.

Issuer `2.0.0_SA_COO~H`. Series **`au`**.
- **Fan-out:** 2 of 2 chains, cap 8. The two cells write disjoint files: `backfill_driver.py` for au-1 and `worker.py` for au-2.
- **Not cut:** enrichment item 3 (the RESAPP gold rebuild) is event-gated on `2.0.0_SA_COO~Z`'s ask; it is cut by amendment when
  the ask arrives, as a served write under a pair. Item 4 (the resume) is an issuer act, not a cell.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-au-1` | `au-1` | **Upload timeout caught** (row Z-S87, ruling 3). `Collector.upload` catches `subprocess.TimeoutExpired`; `drive()` records `upload_timeout` as a transport-class stop (in `STOP_STATUSES` and `TRANSIENT_STOPS`), so it auto-resumes within budget, and otherwise writes the stop to the checkpoint and prints its SUMMARY. A planted timeout proves it. | LOCAL | worker `~96` |
| `HVST-au-2` | `au-2` | **Soft-block status** (row Z-S88, ruling 4). In `worker.py`, a job that would read `listing_empty_200` reads `soft_block` when the publisher already held at least one article for the name (`result["previously_stored"] > 0`); otherwise it stays `listing_empty_200`. `soft_block` is not a driver stop status and is outside `SUCCESSFUL_RUN_STATUSES`, so it never counts toward the 95% bar. | LOCAL | worker `~97` |

**Checks dry-run at the base before the cut:**
- `au-1` AC1 (`pytest lib/opal_data_harvest/test_au1_upload_timeout.py`) base: FAIL as expected (the test is absent).
- `au-2` AC1 (`pytest lib/opal_data_harvest/test_au2_soft_block.py`) base: FAIL as expected (the test is absent).

## 62. ROUND 49 -- the round-48 analysis enrichment list (`ledger/ROUND_ANALYSIS.round48.md` @6d005e5261), 2026-10-06 ~07:0xZ

Round 48 is CLOSED (board 8/17; 9 a qualified wait on Andrew). Ruling 1 asks for a census of the stored ft and wsj records for an
address constructed with no request, and a plain "no link was stored" where there is none. No ft.com or wsj.com host is contacted,
and Andrew's FT hold stands.

**Census at the cut (issuer, read-only, silver_latest, no publisher contact):** the records already STORE their own canonical
address, so nothing needs to be constructed.
- **ft:** 185 articles. 171 carry `html_meta["og:url"]` (`https://www.ft.com/content/<uuid>`) and no top-level `url`; the other 14
  are normalised records that carry the top-level `url` and no `html_meta`.
- **wsj:** 463 articles. 448 carry `html_meta["og:url"]` and `articleData.sourceUrl`; the other 15 carry the top-level `url`.
- The two sets are DISJOINT in both publishers, so no article carries both, and the byte-equality proof is run on the shared FORM
  instead (scheme, host, path shape) plus, for wsj, `og:url` == `articleData.sourceUrl` on every article carrying both.
- The union covers every stored article: 185/185 and 463/463.

Issuer `2.0.0_SA_COO~H`. Series **`av`**.
- **Fan-out:** 1 of 1 chain, cap 8 (av-2 depends on av-1).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-av-1` | `av-1` | **ft/wsj stored canonical address.** `publication_gold.article_url` for ft and wsj reads the top-level `url`, else `html_meta["og:url"]` (first value if a list), else for wsj `articleData.sourceUrl`. The address is accepted only on the publisher's own host (`https://www.ft.com/content/...`, `https://www.wsj.com/...`), else None; never constructed or guessed, and no host is fetched. A census script prints article-level link coverage per publisher, with the og:url/sourceUrl agreement on wsj. | LOCAL | worker `~98` |
| `HVST-av-2` | issuer act, after av-1 merges | **Served gold rebuild #7** under a NEW never-widen pair, on the rebuild-#6 rule with ft/wsj `url` the only moved field class. | SERVED -> CTO half | `2.0.0_SA_COO~H` |

**Checks dry-run at the base before the cut:**
- `av-1` AC1 (`pytest lib/research/harvest/test_av1_stored_canonical_url.py`) base: FAIL as expected (the test is absent).

## 63. ROUND 50 -- the round-49 analysis ADDENDUM 1 (`ledger/ROUND_ANALYSIS.round49.md` @3bf4e2ea1e), 2026-10-06 ~19:3xZ

Round 50 is triggered by the 18:39Z resume of bbg, barrons and wsj (Andrew-direct ~18:3xZ, record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_183xZ_HARVST_SA_PAID_FT_LATER_RESUME_BBG_BARRONS_WSJ_REMOVE_WORKTREES.md`).
FT stays deferred. Andrew-direct ~19:2xZ moves SA to the tab pattern (Google sign-in in its own profile, REST in-tab, no proxy).

**Measured at the cut (issuer):** since 18:39Z, 5 of 15 resumed jobs (bbg 2, wsj 2, barrons 1) ended `error` / `TimeoutError`
with ZERO request attempts, each right after `stored_token_used`. That is the tab build, whose `TabSession.__init__` runs
`self.page.goto(origin)` (`lib/opal_data_harvest/tab_transport.py:92`) under Playwright's default: wait for `load`, 30 s. The
historical rate was 16 of 880 jobs across the three roots. Machine load at the time: 37.6 of 63.5 GB free, CPU 14%.

Issuer `2.0.0_SA_COO~H`. Series **`aw`**.
- **Fan-out:** 2 of 2 chains, cap 8. The in-tab probe read 200 (account 200 / 4,774 B; listing 200 / 5 items) after Andrew's
  Google sign-in, so `aw-2` is cut in this issuance. Write sets are disjoint (`aw-1`: `tab_transport.py` + its test; `aw-2`:
  `publishers.py`, `contracts.json` + its test).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-aw-1` | `aw-1` | **The origin load wait.** `TabSession.__init__` opens the origin with `wait_until="domcontentloaded"` and an explicit timeout (module constant `ORIGIN_TIMEOUT_MS = 60000`). A timeout there raises a NAMED error `OriginLoadTimeout` (a `RuntimeError` subclass defined in `tab_transport.py`) whose message names the publisher and origin, so a run record's `error_type` reads `OriginLoadTimeout`, never a bare `TimeoutError`. The context is still closed on failure. Plants on a LOCAL http server (no publisher host): a page whose `load` never fires opens the tab; a page whose document never arrives raises `OriginLoadTimeout`; a mutant that restores the `load` wait makes the first plant fail. | LOCAL | worker `~99` |
| `HVST-aw-2` | `aw-2` | **SA on the tab pattern.** `contracts.json` sa `transport: tab` (egress native in-tab, no proxy); `TAB_ORIGINS["sa"]`; an sa sign-in route on bbg's Google pattern; one real in-tab fetch per endpoint class answering 200 through the transport. | LOCAL | worker `~100` |

**The close run (issuer, after `aw-1` merges):** the next jobs of the three live legs build their tab from the merged code (each
job spawns a fresh collector from the shared tree); the 5 `TimeoutError` pairs are re-run with `--names` and each must reach its
first request. That is the round's one real run for `aw-1`.

**Checks dry-run at the base before the cut:**
- `aw-1` AC1 (`pytest lib/opal_data_harvest/test_aw1_origin_load_wait.py`) base: FAIL as expected (the test is absent).
- `aw-1` AC2 / `aw-2` AC3 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (667 passed, 1 skipped).
- `aw-2` AC1 (`pytest lib/opal_data_harvest/test_aw2_sa_tab.py`) base: FAIL as expected (the test is absent).
- `aw-2` AC2 (`cat .../aw-2.live_probe.out`) base: FAIL as expected (no such file).

## 64. ROUND 51 -- the round-49 analysis ADDENDUM 2 (`ledger/ROUND_ANALYSIS.round49.md` @a246fcd07f), 2026-10-07 ~00:1xZ

Round 50 is CLOSED (`deliverables/2.0.0_SA_COO_H/round50/ROUND50_CLOSE_RUN.md` @e8c062b598). Rows AMGT_HARVST-Z-S90 and Z-S91: the
wsj job for T US Equity fetched 502 articles in 3 h 03 min and accepted 0 (431 `company_not_mentioned`), then met a 401 under
`--no-sign-in`; the wsj leg is STOPPED on `sign_in_refused` and waits for Andrew's sign-in in the wsj profile.

**Read at the cut (issuer):** the wsj query is already the company name (`slug_query(security["company"])`,
`lib/opal_data_harvest/publishers.py:700,762`); the symbol is never queried. The defect is `discovery._matches`
(`lib/opal_data_harvest/discovery.py:65-67`), which tests each query word as a SUBSTRING of the slug: `sse` matches `dissects`,
`assets`, `businesses`; AT&T's words `at`, `t` match almost any slug. ADDENDUM 2 item (1) names the query; the cell fixes the
matcher, which serves the same outcome for every name. Items (2) and (3) are cut as written, with the replay run OFFLINE over the
18 stored wsj sitemap files because wsj is signed out.

Issuer `2.0.0_SA_COO~H`. Series **`ax`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-ax-1` | `ax-1` | **Slug phrase match + the unselective bound.** `discovery._matches` admits a sitemap item only when a run of consecutive WHOLE slug tokens, joined, equals the query's words joined (or that + `s`). A wsj job that has fetched K articles and accepted none ends `candidate_set_unselective` (K is `contracts.json` wsj `unselective_after`, derived by script from the finished-job records with the denominator printed); the driver records the pair done with that status and the leg continues. Offline replay over the stored wsj sitemaps: T US Equity and SSE LN fall to K or fewer candidates; the three finished names with the most accepted articles keep every accepted URL. | LOCAL | worker `~101` |

**The close run (issuer, after `ax-1` merges and Andrew's wsj sign-in):** the wsj leg resumes from `r46_wsj_checkpoint.json`
(`--clear-stop wsj`) and the T US Equity pair re-runs under the new rule.

**Checks dry-run at the base before the cut:**
- `ax-1` AC1 (`pytest lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py`) base: FAIL as expected (the test is absent).
- `ax-1` AC2 (`cat .../ax-1.replay.out`) base: FAIL as expected (no such file).
- `ax-1` AC3 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (674 passed, 1 skipped on merged CLOUD at the round-50 close).

## 65. ROUND 52 -- the round-49 analysis ADDENDUM 3 item 1 (`ledger/ROUND_ANALYSIS.round49.md` @c6a7f4eff8), 2026-10-07 ~02:3xZ

Round 51's order is terminal (`ax-1` merged @a02b56aaa5). Its live close run is owed (wsj waits on Andrew's sign-in). Row
AMGT_HARVST-Z-S92: the round-51 matcher loses 33 of 3,282 accepted bbg URLs (Amazon.com 17 of 17); wsj keeps 566 of 566. The CTO
ruled (b): the rule changes before bbg resumes. bbg is stopped on its own `bot_check` (01:55Z) and the issuer's stop file.

**Measured at the cut (issuer, offline; `deliverables/2.0.0_SA_COO_H/round51/ax-1.matcher_rules_eval.out` plus the cut-time run):**
`com` added to the one form list, and a slug matching when the joined-adjacent rule matches OR every query word is a whole slug
token in any order, keeps 3,276 of 3,282 bbg and 566 of 566 wsj; AT&T 11 candidates, SSE 0, Bank of America 9, Amazon 94 in the
26,907 stored wsj URLs. The 6 residual bbg URLs: 4 substring accidents (`sap` in `whatsapp`, `ubs` in `hubs`, `nokia` in
`nokian`, `monster` in `monsterverse`) and 2 Eli Lilly slugs carrying `lilly` alone. ADDENDUM 3's bar of 3,282 of 3,282 is not
reachable by a whole-token rule; the order's bar is bbg lost <= 6, each in one of those two classes.

Issuer `2.0.0_SA_COO~H`. Series **`ay`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-ay-1` | `ay-1` | **Form words not required; name words as whole tokens in any order.** `_LEGAL_SUFFIX` (the one declared form list) gains `com`, so `Amazon.com Inc` queries `Amazon`. `discovery._matches` keeps round 51's joined-adjacent rule and also admits a slug in which every query word is a whole token (or the word + `s`), in any order; a word never matches inside a longer token. Offline replay over every accepted bbg and wsj URL and the stored wsj sitemaps: wsj 566 of 566; bbg lost <= 6, each a substring accident or an Eli Lilly alias case; AT&T, SSE and Bank of America at or below 100 candidates. | LOCAL | worker `~102` |

## 66. ROUND 53 (not yet issued) -- the round-49 analysis ADDENDUM 3 item 2: an alias set per name

Separate and non-gating by the ruling. One cell, `HVST-az-1`: each security's query is an alias SET (the legal name without its
form words, plus the research-folder name), never a first-word rule; Meta Platforms is the build case (2 candidates where 118 wsj
slugs carry `meta`), Bank of America and AT&T are the controls. Unread at this cut: where the research-folder name per security
lives. Cut in its own issuance once that input is read.

**Checks dry-run at the base before the round-52 cut:**
- `ay-1` AC1 (`pytest lib/opal_data_harvest/test_ay1_name_tokens.py`) base: FAIL as expected (the test is absent).
- `ay-1` AC2 (`cat .../ay-1.replay.out`) base: FAIL as expected (no such file).
- `ay-1` AC3 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (695 passed, 1 skipped on merged CLOUD at the round-51 drain).

## 67. ROUND 53 -- the round-49 analysis ADDENDUM 4 (`ledger/ROUND_ANALYSIS.round49.md` @22b49f7b04), 2026-10-07 ~03:5xZ

Round 52's order is terminal (`ay-1` merged @ba9ad361fd). wsj and bbg resumed 03:21Z and 03:29Z (both profiles read signed in, no
challenge); the OMAB pair re-ran on the round-52 rule (`no_new_articles`, as before). Row AMGT_HARVST-Z-S94: the driver records
every job done whatever its status (`lib/opal_data_harvest/backfill_driver.py:314`) and a resume skips done pairs (`:120`), so 37
pairs that ended on a stop status were never retried (wsj 8, bbg 8, barrons 12, sa 9;
`deliverables/2.0.0_SA_COO_H/round52/stop_status_pairs.json`). One barrons article answering HTTP 400 ended two whole jobs.

Issuer `2.0.0_SA_COO~H`. Series **`ba`**. The alias cell of section 66 (`HVST-az-1`) moves to round 54.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-ba-1` | `ba-1` | **A stopped pair is retried, not done; one dead article does not end a job.** `done` is recorded only on a declared set of concluded statuses; any other status goes to a retry record with its attempt count, and to `gave_up` with its reason after 3 attempts. An existing checkpoint's stop-status `done` rows move to `retry` on load, so the 37 legacy pairs are planned at each leg's next invocation. The summary prints collected / retry / gave_up / never_started, summing to the pair count. An article request answering 400, 404 or 410 is skipped and recorded and the job continues; 401/403 still stop it. | LOCAL | worker `~103` |

**The close run (issuer, after `ba-1` merges):** each leg's next invocation migrates its checkpoint and plans its stopped pairs;
the issuer reads the `PAIRS` lines and checks the 37 against `stop_status_pairs.json`.

**Checks dry-run at the base before the cut:**
- `ba-1` AC1 (`pytest lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py`) base: FAIL as expected (the test is absent).
- `ba-1` AC2 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (706 passed, 1 skipped on merged CLOUD at the round-52 drain).

## 68. ROUND 54 -- the alias set per name, as ruled by the round-49 analysis ADDENDUM 6 (`ledger/ROUND_ANALYSIS.round49.md` @c1f0c8a429), 2026-10-07 ~09:2xZ

Round 53's order is terminal (`ba-1` merged @296601ed65). Section 66's input was read at the relaunch: the crosswalk carries a
research-folder name on 96 of 237 records and on none of Meta, Bank of America, AT&T or Amazon (row AMGT_HARVST-Z-S95). ADDENDUM 5
left the cell uncut; ADDENDUM 6 names the alias source as the hand-written list `lib/research/harvest/whole_brand_aliases.json`,
extended per security, each entry citing its census and its plane. Section 66's "plus the research-folder name" is superseded by
that ruling; the rest of section 66 stands.

Issuer `2.0.0_SA_COO~H`. Series **`az`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-az-1` | `az-1` | **A name's slug query is an alias set; a brand word enters only from the hand-written list.** The collector appends each `plane: slug` brand to the security's `aliases`; discovery admits a slug that matches any one alias, with one sitemap request per month; the 7 existing entries are marked `plane: text` and stay out of the slug plane; first slug entries Meta and Lilly. Proof on the offline replay: Meta up, the 2 Lilly slugs recovered (bbg kept >= 3,278 of 3,282), wsj 566 of 566, Bank of America and AT&T unchanged, exactly 2 of 234 names changed. | LOCAL | worker ~104 |

**Not in this round (ADDENDUM 6):** one suffix list in place of two (next enrichment list); the cut or decorated legal names (row
AMGT_HARVST-Z-S96: up to 20 of 234; the cell follows from the count); any further brand entry.

**The close run (issuer, after `az-1` merges):** the META and LLY pairs re-run on wsj and bbg with `--names`.

**Checks dry-run at the base before the cut:**
- `az-1` AC1 (`pytest lib/opal_data_harvest/test_az1_alias_set.py`) base: FAIL as expected (the test is absent).
- `az-1` AC2 (`cat .../0.9.0_WK_AMGT_HARVST~104/az-1.replay.out`) base: FAIL as expected (no such file).
- `az-1` AC3 (`pytest lib/research/harvest/tests/test_alias_rule_round18.py lib/research/harvest/tests/test_universe_securities.py`) base: PASS as expected (40 passed).

## 69. ROUND 55 -- the gold-plane census for the two slug brands (`1.0.0_SA_CTO~Z` msg 30842), 2026-10-07 ~11:3xZ

Round 54's order is terminal (`az-1` merged @05638ecfd9; close run @0849993cba). The CVO graded the collector's text check at 29
of 30 for each brand (@cc31b43fbc) and the CTO admitted both there (msg 30836; recorded @bb02e46a3b). Msg 30842: the gold text
matcher is a third plane with its own census -- there a brand attributes a mention inside ANY stored article -- and no gold
rebuild happens before that grade.

Issuer `2.0.0_SA_COO~H`. Series **`bb`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bb-1` | `bb-1` | **What the gold text matcher would ADD with `Meta` and `Lilly` as brands: a dry-run census, no rebuild.** Over every latest silver article, with the served matcher's own pattern builder: added spans, NEW pairs, title and lead flips per brand, split by publisher; a control (an existing alias adds 0) and the served-matcher agreement control; a seeded sample of 30 added rows per brand for the CVO's grade (bar 29 of 30). No product file changes. | LOCAL | worker ~105 |

**Not in this round:** flipping either entry's `plane`, a gold rebuild, any further brand; row AMGT_HARVST-Z-S96's cell (cut or
decorated legal names) and the one-suffix-list item wait for the analysis that names them.

**Checks dry-run at the base before the cut:**
- `bb-1` AC1 (`cat .../0.9.0_WK_AMGT_HARVST~105/bb1_census.out`) base: FAIL as expected (no such file).
- `bb-1` AC2 (`pytest .../0.9.0_WK_AMGT_HARVST~105/test_bb1_added_spans.py`) base: FAIL as expected (the test is absent).
- `bb-1` AC3: judgment, graded by `3.0.0_SA_CVO~Z`.

## 70. ROUND 56 -- gold's securities list takes legal names from the collector's identity record (`1.0.0_SA_CTO~Z` msg 30864), 2026-10-07 ~12:0xZ

Round 55's order is terminal on its mechanical criteria (`bb-1` merged @1b87f2b0e1, closed @0dd1c04910; its judgment criterion
is at `3.0.0_SA_CVO~Z`, both samples graded as cut). Row AMGT_HARVST-Z-S98: for 138 of 242 securities gold's alias set is the
security key alone. Msg 30864: that outranks both brands and is the next issuance's first cell; ONE gold rebuild follows it,
under its own never-widen pair, and none before.

Issuer `2.0.0_SA_COO~H`. Series **`bc`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bc-1` | `bc-1` | **Gold's list takes each security's legal name from the collector's identity record when the pool carries none; the census prints what each name gains.** The pool's own name wins; nothing is derived from a key or ticker; a slash tail on an identity name is removed and counted; cut names are listed, not altered. Census over every latest silver article with the served matcher: key-only alias sets before and after, pairs gained per name, the name-quality class, the round-55 brand lines re-run against the new list, agreement control. No gold build. | LOCAL | worker ~106 |

**Not in this round:** the gold rebuild (its own never-widen pair, after this cell); flipping either brand's `plane`; repairing
the cut legal names of row AMGT_HARVST-Z-S96; one suffix list in place of two.

**Checks dry-run at the base before the cut:**
- `bc-1` AC1 (`pytest lib/research/harvest/tests/test_bc1_legal_names.py`) base: FAIL as expected (the test is absent).
- `bc-1` AC2 (`cat .../0.9.0_WK_AMGT_HARVST~106/bc1_census.out`) base: FAIL as expected (no such file).
- `bc-1` AC3 (`pytest lib/research/harvest/tests -q`) base: PASS as expected (297 passed).

## 71. ROUND 57 -- the gold brands and the Lilly anchor (`1.0.0_SA_CTO~Z` msgs 30873, 30876), 2026-10-07 ~12:4xZ

Round 56's order is terminal (`bc-1` merged @0b35eeba2a): key-only alias sets 137 to 3 of 242; article pairs 14,895 to 22,979
over 18,634 silver articles. The CVO graded the round-55 samples (@8289c4e3ed): Meta 30 of 30, Lilly 29 of 30 with a first
name as the miss. Msg 30873: Meta is admitted on gold; a bare `Lilly` counts on gold only in an article that also carries
`Eli Lilly` or the upper-case ticker. Msg 30876: the anchor stands at its measured cost (it drops both of Lilly's 2 new pairs,
one wrong and one a passing link line; read @2aba59986e).

Issuer `2.0.0_SA_COO~H`. Series **`bd`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell; same chain as `bc-1`, so worker ~106's queue).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bd-1` | `bd-1` | **`Meta` is a gold brand; a bare `Lilly` counts on gold only beside the security's own name or ticker.** Each entry gains a `gold` object (admitted, anchor, census) and keeps `plane: slug`; the list puts an unanchored gold brand in `aliases` and an anchored one in a new `anchored_aliases`; `_security_mentions` counts an anchored alias only when the unanchored count is at least 1. Plants with the TV review as the negative control and the mutant that shows it bites. Census over every silver article: Lilly gains 0 pairs, both known pairs listed as dropped, Meta gains pairs, no other security changes. No gold build. | LOCAL | worker ~106 |

**Not in this round:** the gold rebuild (ONE act after this cell, under its own never-widen pair, CTO~Z msg 30864 item 3);
row AMGT_HARVST-Z-S96's cut names; one suffix list in place of two.

**Checks dry-run at the base before the cut:**
- `bd-1` AC1 (`pytest lib/research/harvest/tests/test_bd1_gold_brands_and_anchor.py`) base: FAIL as expected (the test is absent).
- `bd-1` AC2 (`cat .../0.9.0_WK_AMGT_HARVST~106/bd1_census.out`) base: FAIL as expected (no such file).
- `bd-1` AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (380 passed).

## 72. ROUND 58 -- the list repair the rebuild #8 dry run asked for (`1.0.0_SA_CTO~Z` msg 31008), 2026-10-07 ~14:0xZ

Round 57's order is terminal (`bd-1` merged @088d226de5). Row AMGT_HARVST-Z-S99: the served gold was built from the 212-name
file `round33/securities.universe.r33.json`, not from `build()`. Msg 30924: one rebuild is still wanted, after a signing dry
run. The dry run (`deliverables/2.0.0_SA_COO_H/round57/GOLD_REBUILD8_SIGNING_READ.md` @b787ec1026, PUTS 0) STOPS the rebuild as
the list stands: 140 served pairs lost over 5 securities (a decorated pool name wins over the legal name), Air Liquide +3,543
pairs on the exact-case ticker form `AI`, 43 new ticker forms unread. Msg 31008 rules the repair.

Issuer `2.0.0_SA_COO~H`. Series **`be`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-be-1` | `be-1` | **The identity legal name is always an alias and never replaced; a pool name with a ticker or exchange tail is not an alias; `AI` is refused as a ticker form.** One stated decorated-name rule with its mutant; a list comparison against the served file and the round-57 list (served aliases missing before and after, the six named securities, pool names refused and kept, new ticker forms). No silver read, no gold build. | LOCAL | worker ~107 |

**The close run (issuer, after `be-1` merges):** the signing dry run re-run on the repaired list, extended as msg 31008 rules:
pairs gained per NEW ticker form; 0 pairs lost; every gained pair assigned to one cause (a new security, a new alias, silver
growth) summing to the total; then a sample of 30 pairs from the largest non-silver-growth gainers for `3.0.0_SA_CVO~Z` (bar
29 of 30); then the rebuild's never-widen pair.

**This round reverses a ruling of this seat:** `bc-1`'s "the pool's own name wins over the identity record" (section 70).

**Checks dry-run at the base before the cut:**
- `be-1` AC1 (`pytest lib/research/harvest/tests/test_be1_legal_name_always.py`) base: FAIL as expected (the test is absent).
- `be-1` AC2 (`cat .../0.9.0_WK_AMGT_HARVST~107/be1_list_compare.out`) base: FAIL as expected (no such file).
- `be-1` AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (397 passed).

## 73. ROUND 59 -- the Seeking Alpha job record (`1.0.0_SA_CTO~Z` rulings C2 @f97be3fd6f, msgs 31046, 31054), 2026-10-07 ~15:0xZ

Row AMGT_HARVST-Z-S100: the collector read Alibaba, Boeing and Costco on 2026-10-06/07 while AMGT_RESAPP's freshness page
showed them last read 2026-09-11; the page reads a store these runs do not write. Ruling C2 routes the collector half here on
ONE contract, `lib/research/freshness/seeking_alpha_job_record.schema.json` @25ebedb3a3 (`2.0.0_SA_COO~Z` msg 31059): one
writer (the collector), one reader (`AMGT-bb-16`). This round runs beside round 58's close run (the gold rebuild #8 signing dry
run 2); the two write disjoint files.

Issuer `2.0.0_SA_COO~H`. Series **`bf`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell; no edge to the `be` chain: `lib/opal_data_harvest` against `lib/research/harvest`).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bf-1` | `bf-1` | **One record per finished Seeking Alpha job, to the schema file, at the builder's address; a one-time emitter for jobs already finished; a switch that is off.** `job_record.py` (build, address, write-once), the call in `worker.run_job` behind `seeking_alpha_job_record.enabled`, `emit_job_records.py` with `--dry-run` and `--write`, the registry row, plants, and the real dry run over the two Seeking Alpha runtime roots. The worker sends no put. | WORLD (the gate's floor: `<paths>` names `infra/logic/registry/`) | worker ~108 |

**The issuer's acts after the merge (each recorded; `1.0.0_SA_CTO~Z`'s exercised read and a change-management entry, as a WORLD cell requires):** read the dry
run; `--write` the one-time emit; flip the switch in its own commit; confirm one live job writes its record.

**Checks dry-run at the base before the cut:**
- `bf-1` AC1 (`pytest lib/opal_data_harvest/test_bf1_job_record.py`) base: FAIL as expected (the test is absent).
- `bf-1` AC2 (`cat .../0.9.0_WK_AMGT_HARVST~108/bf1_emit_dryrun.out`) base: FAIL as expected (no such file).
- `bf-1` AC3 (`pytest test_ba1_stopped_pair_is_retried.py test_az1_alias_set.py lib/research/freshness/tests -q`) base: PASS as expected (32 passed).

## 74. ROUND 60 -- seven ticker forms refused on their graded census (`1.0.0_SA_CTO~Z` msgs 31173, 31209), 2026-10-07 ~17:2xZ

Rounds 58 and 59 are terminal (`be-1` merged @01e8088aee; `bf-1` merged @23d65887ca, its records written and its ledger
closed @8240461f26). Signing dry run 2 (@6b49d49e10) met the bar: 0 pairs lost, 14,337 gained, each with one cause. The CVO
graded the gain sample 29 of 30 and the ticker-form sample (@399fcf7d0a): BATS 0 of 10, JD 2, ICT 0, ML 0, BE 1, SAN 0, CAT 10
of 10, the other forms 30 of 30 with MSCI's rows being index and fund names. Msg 31209: the stricter line holds, so `MSCI`'s
bare form is refused with the six.

Issuer `2.0.0_SA_COO~H`. Series **`bg`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell, DIRECT ACT).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bg-1` | `bg-1` | **Seven exact-case ticker forms join `ticker_refusals`, each on its graded census: BATS, JD, ICT, ML, BE, SAN, MSCI.** Data in `whole_brand_aliases.json`; plants that each form is removed, that removing the entry brings it back, that name aliases do not move, and that CAT, CSL, TTE and SLB keep theirs. No network, no build. | LOCAL | worker ~109 |

**The close run (issuer):** signing dry run 2 re-run on the list with the seven refused; then the rebuild's never-widen pair.
Before that re-run, msg 31209's three terms: CAT's name read from the registry (`CATERPILLAR INC`,
`lib/research/identity/registrations.json`); 10 CSL pairs sampled and graded (row AMGT_HARVST-Z-S101); the 9 forms no sampled
row reached stated with their pair counts.

**Checks dry-run at the base before the cut:**
- `bg-1` AC1 (`pytest lib/research/harvest/tests/test_bg1_ticker_refusals.py`) base: FAIL as expected (the test is absent).
- `bg-1` AC2 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (count in the issuance commit).

## 75. ROUND 61 -- six enrichment items after served gold rebuild #8 (`1.0.0_SA_CTO~Z` msg 31486, analysis @3b19f962e0), 2026-10-08 ~00:3xZ

Round 60 is terminal: `bg-1` merged, rebuild #8 DONE 2026-10-07 22:48Z (record @1c819a517e, ledger closed). The round-60
analysis rules R1 to R7 and lists six items. No rebuild is cut in this round (R7): R1 to R5 land on the builder and the next
rebuild is its own pair after their grades.

Issuer `2.0.0_SA_COO~H`. Series **`bh`**.
- **Fan-out:** 3 of 4 chains, cap 8 (the `bh-4 -> bh-5 -> bh-3` chain shares `universe_securities.py` and `bh-3` needs CSL's
  name from `bh-4`; `bh-1` is a chain of one; `bh-2` and `bh-6` are two chains of one queued on one light worker, because the
  box is running two collection legs).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bh-1` | `bh-1` | **The pairs that rest on the bare-name fallback alone: a census by security with its denominator, and a sample of 30.** Read-only script over the served list file and silver; a packet with every span in context; no grade by the worker. JUDGMENT: the CVO grades the 30, bar 27. | LOCAL | worker ~111 |
| `HVST-bh-2` | `bh-2` | **Every pair resting on one of the nine ticker forms no sample reached (20 at the dry run), whole, in context.** Read-only. JUDGMENT: the CVO reads all; a form with 2 or more wrong pairs is refused. | LOCAL | worker-light ~112 |
| `HVST-bh-3` | `bh-3` | **A bare ticker form shared with a company outside coverage counts only beside a second anchor; `CSL` is the case.** `ticker_anchors` data, two per-security fields, the matcher, plants with the Carlisle line as negative control, a census: 39 of 39 good pairs kept, 3 of 3 Carlisle pairs dropped, 0 other securities changed. | LOCAL | worker ~110 (third) |
| `HVST-bh-4` | `bh-4` | **A key-only security takes its name from `lib/research/identity/registrations.json`: CAT, CSL, Keyence.** The join after pool and identity map, plants, a census. No vendor call. | LOCAL | worker ~110 (first) |
| `HVST-bh-5` | `bh-5` | **A legal name cut inside a corporate suffix loses the fragment; one suffix list; every changed name printed** (row Z-S96). Plants, a census. | LOCAL | worker ~110 (second) |
| `HVST-bh-6` | `bh-6` | **What `ICT_US_Equity` is and where its key came from**, from five sources each with its record count. Read-only record. | LOCAL | worker-light ~112 (second) |

**The close run (issuer):** read each census and packet; hand the two packets to `3.0.0_SA_CVO~Z`; run the suite on the merged
tree. No gold is built.

**Checks dry-run at the base before the cut:**
- `bh-1` AC1, `bh-2` AC1, `bh-6` AC1 (`cat` of an output file) base: FAIL as expected (no such file).
- `bh-3`, `bh-4`, `bh-5` AC1 (`pytest` of the cell's new test file) base: FAIL as expected (the test is absent).
- `bh-3`, `bh-4`, `bh-5` AC2 (`cat` of the cell's census output) base: FAIL as expected (no such file).
- `bh-3`, `bh-4`, `bh-5` AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (419 passed).

## 76. ROUND 62 -- the two items ADDENDUM 1 added to the round-60 analysis' list (`1.0.0_SA_CTO~Z` msg 31493, @c75d056652), 2026-10-08 ~00:5xZ

The CVO's L10 slug (msg 31492, `ADJUDICATION_v65.md` @98e21862f2) arrived after the analysis; ADDENDUM 1 adds two items. The
analysis names them round 61's items 7 and 8; they are cut as ROUND 62, its own issuance, because the L6 gate admits one
issuance per round and round 61's was committed (@fcf5542a36) minutes before the addendum. No worker was spawned between the two.

Issuer `2.0.0_SA_COO~H`. Series **`bh`**, continued.
- **Fan-out:** 2 of 2 chains, cap 8 (`bh-7` queues on worker ~110 behind round 61's three orders, which write the same
  `universe_securities.py`; `bh-8` is a chain of one in `lib/opal_data_harvest`).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bh-7` | `bh-7` | **A brand belongs to the issuer: two listings of one issuer may both carry it** (R8, row Z-W107-S2). One issuer = an equal registry LEI, or a shared ticker root with one company name equal to the other's name or suffix form. Plants with two different companies as negative control; a census: `ASML` back on `ASML_US_Equity`, 0 pairs lost, 0 securities changed outside a group. | LOCAL | worker ~110 (fourth) |
| `HVST-bh-8` | `bh-8` | **A Seeking Alpha job record's `finished_at` is the job's own end** (row Z-W108-S2). The run record carries it per job; both writers read it through one helper; an old run record keeps its address. Code and plants only: no S3, no emit, no switch change. The merge is the issuer's act with a ledger entry. | SERVED | worker ~113 |

**Checks dry-run at the base before the cut:**
- `bh-7` AC1 (`pytest` of the new test file) base: FAIL as expected (the test is absent); AC2 (`cat bh7_census.out`) base: FAIL
  as expected (no such file); AC3 (the harvest suite) base: PASS as expected (419 passed).
- `bh-8` AC1 (`pytest test_bh8_job_finished_at.py`) base: FAIL as expected (the test is absent); AC2 (`pytest test_bf1_job_record.py
  test_ba1_stopped_pair_is_retried.py test_az1_alias_set.py lib/research/freshness/tests -q`) base: PASS as expected (count in
  the commit).

## 77. ROUND 63 -- two rulings on the first reads of the rebuilt gold (`1.0.0_SA_CTO~Z` msgs 31542, 31551, 31554), 2026-10-08 ~02:4xZ

The CVO graded round 61's two packets (@31fbcebb42, and the other 12 fallback pairs @9e8ca92e4e): the fallback sample 27 of
30, all 27 Nokia and the 3 other-case hits wrong; the nine forms 16 of 17, the miss Hawaiian Electric on `HEI`. Rulings: the
bare-name fallback matches the stored case only (13 wrong pairs and 2 true BP pairs go, the 2 named); HEI joins the
second-anchor rule; no rebuild until both are graded. Round 61's `bh-3` is merged with its symbol anchor (@1866108355) and
round 62's `bh-7` is executing on slot ~110.

Issuer `2.0.0_SA_COO~H`. Series **`bh`**, continued.
- **Fan-out:** 1 of 1 chain, cap 8 (both cells write files slot ~110's chain holds: `publication_gold.py` and
  `whole_brand_aliases.json`; they queue behind `bh-7`).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bh-9` | `bh-9` | **The bare-name fallback matches the company name in its stored case only.** One matcher change for a security with no aliases; plants with the verb "sap" and "200-bp" as negative controls and the mutant; a census: every removed pair printed, Nokia removed 0, the two true BP pairs removed and named, securities with aliases changed 0. | LOCAL | worker ~110 (after `bh-7`) |
| `HVST-bh-10` | `bh-10` | **`HEI` under the second-anchor rule.** One data entry on the terms ruled for CSL; plants with the Hawaiian Electric line as negative control; a census: HEICO pairs kept of 2, Hawaiian Electric dropped of 1. Cut to MEASURE whether a bare ticker list can be kept; a miss returns as a finding. | LOCAL | worker ~110 (after `bh-9`) |

**The close run (issuer):** read both censuses; the removed fallback pairs and any HEI result go to `3.0.0_SA_CVO~Z` and
`1.0.0_SA_CTO~Z`; the suite on the merged tree. No gold is built. The next rebuild is its own never-widen pair, whose rule
allows a lost pair only by name (the two BP pairs, and the 3 Carlisle pairs).

**Checks dry-run at the base before the cut:**
- `bh-9` AC1, `bh-10` AC1 (`pytest` of the cell's new test file) base: FAIL as expected (the test is absent).
- `bh-9` AC2, `bh-10` AC2 (`cat` of the cell's census output) base: FAIL as expected (no such file).
- `bh-9` AC3, `bh-10` AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (460 passed).

## 78. ROUND 64 -- rebuild #9 under its pair, and the issuer grouping for TTE and ICT (`1.0.0_SA_CTO~Z` msg 31575, ADDENDUM 2 @e93cccc7be), 2026-10-08 ~04:5xZ

Rounds 61 to 63 are terminal, 10 of 10 orders (@6c959d416b). ADDENDUM 2 records rulings R9 to R13 and lists three items for
round 64: rebuild #9 under its own pair; row Z-W110-S5; then the first walk of the Security Analysis feed on rebuilt gold.

Issuer `2.0.0_SA_COO~H`. Series **`bi`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one order; the other two items are not orders of this issuance, for the reasons below).

| item | how it runs | class |
|---|---|---|
| **Rebuild #9** | The ISSUER'S ACT under its never-widen pair, as rebuild #8 was: dry run `deliverables/2.0.0_SA_COO_H/round64/gold_rebuild9.signing.py` (in flight, PUTS 0), rule `gold_rebuild9_rule.py`, the 21 removals named by key in `REBUILD9_NAMED_REMOVALS.json` (4 true pairs lost). No worker order. | SERVED |
| `HVST-bi-1` (`bi-1`) | **The issuer grouping reaches the two TotalEnergies listings and says why the two ICT listings stay apart.** Limb 2 ignores whitespace in the name comparison; a `reason` on each root left apart; plants with the ICT pair as negative control; a census: TTE grouped, ICT not, built dicts changed 0. Merged AFTER the act. worker-light ~114. | LOCAL |
| **The first walk of the Security Analysis feed on rebuilt gold** | Needs the rebuilt gold and its stamp: an unmet dependency today. Cut as the next round the tick the act ends. | -- |

**Checks dry-run at the base before the cut:**
- `bi-1` AC1 (`pytest test_bi1_grouping_whitespace.py`) base: FAIL as expected (the test is absent).
- `bi-1` AC2 (`cat bi1_census.out`) base: FAIL as expected (no such file).
- `bi-1` AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`) base: PASS as expected (491 passed).

## 79. ROUND 65 -- the first walk of the Security Analysis feed on rebuilt gold (ADDENDUM 2 item 3), 2026-10-08 ~06:5xZ

Round 64 is terminal: rebuild #9 DONE 06:25Z under its pair (record @60818dd705, ledger closed: mention 48,025 to 48,358,
21 pairs removed by name, 4 of them true, lost 0, unexplained 0); `bi-1` merged after it (@0090d94c29) and `build()` at the
merged HEAD still equals the served list file. The walk's dependency, the rebuilt gold and its stamp, is now met.

Issuer `2.0.0_SA_COO~H`. Series **`bj`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bj-1` | `bj-1` | **Twelve securities through the page's own feed reader (`scoped_amgt.read_feed`) on the rebuilt gold.** A read-only script; per security its status, item count and newest 15 items with the matched forms; the 21 named removals checked absent from the walked feeds; no grade by the worker. JUDGMENT: the CVO reads the packet. | LOCAL | worker-light ~115 |

**Checks dry-run at the base before the cut:**
- `bj-1` AC1 (`cat bj1_feed_walk.out`) base: FAIL as expected (no such file).

## 80. ROUND 66 -- when each source thinned, the capitalised headline, and a second feed walk (`1.0.0_SA_CTO~Z` msg 31613, ADDENDUM 3 @f7ad546af4), 2026-10-08 ~07:5xZ

Rounds 64 and 65 are terminal (rebuild #9 DONE; `bi-1`, `bj-1` merged). The CVO graded the first feed walk (@96206b0d29) and
filed two rows: Z-S103 (silver holds 714 articles published in the 30-day window, 5 of them FT, and none naming Caterpillar,
CSL or AIG) and Z-S102 ("25 BP Rate Increase" on BP's feed). ADDENDUM 3 rules R14 (a collection gap, read first, from what is
held only) and R15 (a capitalised headline does not pair on the exact-case form alone), then a second feed walk.

Issuer `2.0.0_SA_COO~H`. Series **`bk`**.
- **Fan-out:** 2 of 3 chains, cap 8 (`bk-1` and `bk-2` run now on disjoint write sets; `bk-3` is issued and HELD until a newer
  gold part is served, which needs the rebuild that carries `bk-2`'s rule under its own pair).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bk-1` | `bk-1` | **Articles collected per source per day over 90 days, from silver, bronze and the collector's run records only; the day each source thinned.** Read-only; three tables and one mechanical THINNED line per source; no publisher called. JUDGMENT: the CVO reads whether it is a collection gap. | LOCAL | worker ~116 |
| `HVST-bk-2` | `bk-2` | **In a headline capitalised throughout, the exact-case form alone does not pair; it needs a second anchor.** One matcher rule for every security; plants with the "25 BP Rate Increase" title as negative control and the mutant; a census printing the pairs it removes per security, every removed pair for a reviewer, pairs added 0. No rebuild. | LOCAL | worker ~117 |
| `HVST-bk-3` | `bk-3` | **The second walk of the page's feed, the same twelve securities, beside the first walk.** Held until a newer part is served. JUDGMENT: the CVO reads the packet. | LOCAL | worker-light ~118 (held) |

**The close run (issuer):** read both censuses; `bk-2`'s removed pairs go to `3.0.0_SA_CVO~Z`; the count it moves and `bk-1`'s
THINNED days go to `1.0.0_SA_CTO~Z`. The rebuild that carries `bk-2` is its own never-widen pair, naming every removed pair.

**Checks dry-run at the base before the cut:**
- `bk-1` AC1, `bk-3` AC1 (`cat` of an output file) base: FAIL as expected (no such file).
- `bk-2` AC1 (`pytest test_bk2_capitalised_headline.py`) base: FAIL as expected (the test is absent); AC2 (`cat bk2_census.out`)
  base: FAIL as expected (no such file); AC3 (`pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q`)
  base: PASS as expected (498 passed).

## 81. ROUND 67 -- two READ cells before the second walk: the never-collected set, and what AIG's empty jobs asked for (`1.0.0_SA_CTO~Z` msg 31631, R18), 2026-10-08 ~08:3xZ

Round 66's `bk-1` is terminal (@0ae995ac2b): no source thinned; the collection is a one-security backfill with no daily
sweep. The CVO graded it a collection gap (@e84dcdce42) with two causes: Caterpillar and CSL have NO job at all; AIG has six
jobs that returned nothing. R18 adds two read cells, before the second walk. The ruling names them as additions to round
66's issuance; they are cut as ROUND 67, its own issuance, because the L6 gate admits one issuance per round and round 66's
was committed @e739de56ec. `bk-2` is executing and `bk-3` stays held.

Issuer `2.0.0_SA_COO~H`. Series **`bl`**.
- **Fan-out:** 1 of 2 chains, cap 8 (two read cells on one worker, in order: the second reuses the first's reading of the two
  run-record stores, and the box already holds one live worker worktree).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bl-1` | `bl-1` | **The covered list (242) less the securities that ever had a collection job, on the union of the S3 run records and this device's, the two counts reconciled first.** Per source too; every never-collected security with its served pair count. No job run. | LOCAL | worker ~119 (first) |
| `HVST-bl-2` | `bl-2` | **What AIG's six empty jobs asked for, beside Nokia's productive jobs:** the request each sent, read from its record; the identity each was given; what the records show and what they cannot tell apart. No job run. | LOCAL | worker ~119 (second) |

**Checks dry-run at the base before the cut:**
- `bl-1` AC1 (`cat bl1_never_collected.out`) base: FAIL as expected (no such file).
- `bl-2` AC1 (`cat bl2_aig_requests.out`) base: FAIL as expected (no such file).

## 82. ROUND 68 -- the three universes reconciled and the truncated stored names repaired, nothing fetched (`1.0.0_SA_CTO~Z` msg 31637, R19 and R20), 2026-10-08 ~09:0xZ

`4.0.0_SA_CRO~Z`'s research (@2394cfc3d8) found the PRD puts any schedule outside the project and Andrew holds the mechanism
and cadence, so R19 withdraws "a scheduled sweep is owed": no sweep cell, no switch. R20 replaces the two read cells of msg
31631. `bl-2` is WITHDRAWN unspawned; `bl-1` was executing and finishes as the read behind (a). `bk-2` is terminal (merged
@6ef6703bf6: 3 pairs removed); `bk-3` stays held.

Issuer `2.0.0_SA_COO~H`. Series **`bm`**.
- **Fan-out:** 1 of 1 chain, cap 8 (both cells write the same two new files; `bm-2` edits what `bm-1` makes).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bm-1` | `bm-1` | **The three universes reconciled (gold list 242, crosswalk 237, collector 234) and one identity record and universe entry added for each listed security the collector lacks (CAT, CSL, Keyence named so far), as NEW dated files beside the script.** The round-47 files and the config pointer are not touched; plants; nothing fetched. | LOCAL | worker ~120 (first) |
| `HVST-bm-2` | `bm-2` | **AIG's truncated stored name repaired in the new identity file, and every other name cut the same way printed.** A stored full name where one exists, else the suffix fragment dropped, else left and listed; plants; nothing fetched. | LOCAL | worker ~120 (second) |

**Not in this round, stated:** moving `lib/opal_data_harvest/config.json` to the new files, and any run for an added or
repaired name. The first is the issuer's act on `1.0.0_SA_CTO~Z`'s word once no leg reads the old files; the second waits on
Andrew's per-use word.

**Checks dry-run at the base before the cut:**
- `bm-1` AC1, `bm-2` AC1 (`pytest` of the cell's new test file) base: FAIL as expected (the test is absent).
- `bm-1` AC2, `bm-2` AC2 (`cat` of the cell's output) base: FAIL as expected (no such file).

## 83. ROUND 69 -- the stored names made whole or stated, before any word is asked for (`1.0.0_SA_CTO~Z` msg 31649, R22), 2026-10-08 ~09:3xZ

Rounds 67 and 68 are terminal: `bl-1` (8 of 242 covered securities never had a collection job), `bm-1` (8 identity records
added in new dated files), `bm-2` (2 truncated names repaired, 3 left cut), merged @1fd0140d91 and @1b2e841422. R22: the
collector's pointer does NOT move now; it rides Andrew's word with the runs. Two repairs first, in one cell.

Issuer `2.0.0_SA_COO~H`. Series **`bn`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bn-1` | `bn-1` | **AIG's stored name becomes its full legal name, from a stored source or three agreeing article spans, with the collector's derived query shown against held titles; `ICT_US` and the two OMAB lines repaired or each said why not; one script yields the final files** (row Z-W120-S3). No pointer move, no collector code change, no job. | LOCAL | worker ~121 |

**Checks dry-run at the base before the cut:**
- `bn-1` AC1 (`pytest test_bn1_names_made_whole.py`) base: FAIL as expected (the test is absent).
- `bn-1` AC2 (`cat bn1_names_made_whole.out`) base: FAIL as expected (no such file).
- `bn-1` AC3 (`pytest test_bm1_identity_records.py test_bm2_truncated_names.py test_bf1_job_record.py test_az1_alias_set.py -q`) base: PASS as expected (count in the issuance commit).

## 84. ROUND 70 -- a stored per-security query override, set for AIG only (`1.0.0_SA_CTO~Z` msg 31664, R23), 2026-10-08 ~10:3xZ

Round 69's `bn-1` is terminal (@357b53c71b): AIG's stored name is its SEC legal name and both OMAB lines are whole, in the
new unpointed identity file; `ICT_US` is unrepaired with its reason, accepted. The query the collector derives for AIG is
still "AMERICAN INTERNATIONAL", because `publishers._LEGAL_SUFFIX` strips "group". R23: fix it as a stored per-security
override, never by changing the suffix rule.

Issuer `2.0.0_SA_COO~H`. Series **`bo`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bo-1` | `bo-1` | **An optional `query_override` on an identity record that replaces the derived queries when present; set for `AIG_US_Equity` only through the one builder.** `_LEGAL_SUFFIX`, `slug_query` and the matcher unchanged; plants with the absent field as negative control and the mutant; the derived query of all 242 names before and after (1 changed, 241 identical), 0 of 234 changed on the round-47 file, and the two American Airlines titles excluded. | SERVED | worker ~122 |

**The merge is HELD** on the live Seeking Alpha leg ending AND a never-widen pair: a merge into `lib/opal_data_harvest` is a
deploy to whatever the driver runs next. The order stays open until then.

**Checks dry-run at the base before the cut:**
- `bo-1` AC1 (`pytest test_bo1_query_override.py`) base: FAIL as expected (the test is absent).
- `bo-1` AC2 (`cat bo1_query_table.out`) base: FAIL as expected (no such file).
- `bo-1` AC3 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (count in the issuance commit).

## 85. ROUND 71 -- a malformed override and the stored label, before the pointer ever moves (CTO half @d6ea0eff2f, condition C2; msg 31679), 2026-10-08 ~11:1xZ

Round 70's `bo-1` is BUILT on branch `wk-AMGT_HARVST-122-r70` @419dc9b1fc and its never-widen pair is complete (COO half
@ca5cb29676, CTO half @d6ea0eff2f); the merge waits on the live Seeking Alpha leg ending. The CTO half's C2 names two things
owed before the collector is ever pointed at the new identity file.

Issuer `2.0.0_SA_COO~H`. Series **`bp`**.
- **Fan-out:** 1 of 1 chain, cap 8 (one cell, stacked on `bo-1`'s branch because it edits the same functions).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bp-1` | `bp-1` | **Which jobs a malformed query override stops, shown by test on the code as found, then contained to exactly one job with a named status and no fallback; and one helper so an overridden security's stored listing label reads the query that was searched** (row Z-W122-S1). `slug_queries` stays the one writer of the queries; the 242-name table re-read. | SERVED | worker ~123 |

**The merge is HELD** like `bo-1`'s, and this cell's commits are not covered by `bo-1`'s pair.

**Checks dry-run at the base (branch `wk-AMGT_HARVST-122-r70`) before the cut:**
- `bp-1` AC1 (`pytest test_bp1_malformed_override.py`) base: FAIL as expected (the test is absent).
- `bp-1` AC2 (`cat bp1_query_table_rerun.out`) base: FAIL as expected (no such file).
- `bp-1` AC3 (`pytest lib/opal_data_harvest -q`) base: PASS as expected (778 passed, 3 skipped on that head).

## 86. ROUND 73 -- the collector's acceptance check, and the lower-case alias read (row AMGT_HARVST-Z-S104; `1.0.0_SA_CTO~Z` R25, R26, R27), 2026-10-08 ~16:1xZ

Found on the eight names run on Andrew's word: the Wall Street Journal finished 8 of 8 with 0 stored. The collector searches
with the legal suffix stripped and accepts only on the full stored name; for 149 of 242 names every alias ends in a
legal-form word. (Round 72 was the issuer's direct act, the rebuild-#10 dry run, with no order.)

Issuer `2.0.0_SA_COO~H`. Series **`bq`**.
- **Fan-out:** 2 of 2 chains, cap 8 (disjoint write sets: `lib/research/harvest/` and `lib/opal_data_harvest/`; no edge).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bq-1` | `bq-1` | **R26(a): whether gold pairs a lower-case common word with a security whose alias is that word, shown by a planted test with two controls; nothing repaired.** | LOCAL | worker-light ~124 |
| `HVST-bq-2` | `bq-2` | **R25 as amended by R27: a fetched article is accepted on the strings `slug_queries` returned, whole-word and case-insensitive; proof table over 242 that the new rule is a superset of the old; the one-word forms listed.** | SERVED | worker ~125, stacked on 537ac56e9b |

**NOT cut:** R26(b), a stored-case rule for gold's aliases. It waits on the issuer's census over built gold of which pairs
such a rule would remove, by security (R27). **Merge order when the time comes (R26):** gold first, then acceptance; each
merge its own pair; `bq-2`'s merge is HELD while any collection leg runs. **Nothing is re-collected** on this round.

**Checks dry-run at the base before the cut:**
- `bq-1` AC1 base: FAIL as expected (the test is absent). AC2 base: FAIL as expected (no such file).
- `bq-2` AC1 base: FAIL as expected (the test is absent). AC2 base: FAIL as expected (no such file). AC3 base: PASS as
  expected (787 passed, 3 skipped on 537ac56e9b).

## 87. ROUND 74 -- gold's capital-initial alias rule (R30), and FWD-18's continuous cycle: the runner and its start with the box (PRD v0.22, both halves SIGNED), 2026-10-08 ~21:4xZ

R30 (`1.0.0_SA_CTO~Z` msg 32004) on the issuer's round-73 census @7e1509b798: an exact-stored-case rule removes 1,466 good
and bad pairs alike; the rule instead is a capital first letter on the matched text. FWD-18 (PRD v0.22 @e30fb3e610;
`prd-signoff.py status` read ADMITTED 21:1xZ; `1.0.0_SA_CTO~Z` msg 31923 "cut it after that sign") is one process on this
box that cycles bbg, wsj, barrons and sa without end, one record per cycle; the FT is never run. Round 73's `bq-2` is
still open (worker ~125 reseated 21:2xZ after the issuer's session ended); this round does not touch its files.

Issuer `2.0.0_SA_COO~H`. Series **`br`**.
- **Fan-out:** 3 of 3 chains, cap 8 (no edges: `br-3` needs only the runner's command line, fixed in both orders; write
  sets disjoint at file grain: `lib/research/harvest/`; `cycle_runner.py`, its test, `backfill_driver.py`;
  `install-cycle-schedule.ps1`, `README.md`).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-br-1` | `br-1` | **R30: an alias matches in gold only where the matched text begins with a capital letter, or equals the stored alias exactly (the issuer's clause, for "eBay"); census on the round-73 population with both denominators; REMOVED SAMPLE 30 for the CVO; KEPT READ on V, CDNS, BKNG, ORA.** | SERVED | worker ~126 |
| `HVST-br-2` | `br-2` | **FWD-18 hop 1: `cycle_runner`, a cycle per publisher over the backfill driver with the floor at the last COMPLETED cycle, one record per cycle, a refused sign-in recorded by name and the pass going on; negative arm: a held article counted held with no body request.** | SERVED | worker ~127 |
| `HVST-br-3` | `br-3` | **FWD-18 hop 2: `install-cycle-schedule.ps1`, the runner registered at log-on with no time limit; `-Plan` registers nothing; the cell registers nothing.** | LOCAL | worker-light ~128 |

**NOT cut:** FWD-18 hop 3, the page an analyst reads ("can tell from the page's own words when a publisher did not run"):
it needs cycle records that exist; it is the next enrichment. **Activation at close (the issuer):** the r47 sa backfill
leg ends or is stopped before the runner runs `sa`; the task is registered against a PINNED checkout of the merged runner;
ACCEPTANCE per publisher is the first cycle completing with no one at the box after start. **Merges:** `br-1` carries its
own never-widen pair and serves in a rebuild after #11 (R28, R30); `br-2` is not merged while a collection leg runs from
the shared tree.

**Checks dry-run at the base before the cut:**
- `br-1` AC1 base: FAIL as expected (no tests ran: the test is absent). AC2, AC3 base: FAIL as expected (no such file).
- `br-2` AC1 base: FAIL as expected (absent). AC2 base: FAIL as expected ("No module named lib.opal_data_harvest.cycle_runner").
  AC3 base: PASS (765 passed, 1 skipped).
- `br-3` AC1, AC2 base: FAIL as expected (no such script). AC3 base: PASS (`TASK ABSENT`).

## 88. ROUND 75 -- rebuild #11's dry run (the AIG and OMAB list move), the installer's publishers, and the runner activated on bbg, wsj and barrons (`1.0.0_SA_CTO~DELL1` msgs 1410 and 1430, `ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38), 2026-10-09 ~02:1xZ

Rounds 73 and 74 are terminal, 5 of 5. Round 66's `bk-3` (the second feed walk) completed @5f2ab28b0d after rebuild #10 served.
The project moved to dell1 (@a4bcfa869f); site Z confirmed one issuer (`0.0.0_AB_MSTR~DELL1` msg 1303). The round-74 analysis
places the drain packet's four items and lists four for round 75.

Issuer `2.0.0_SA_COO~W1`. Series **`bs`**.
- **Fan-out:** 2 of 3 chains now, cap 8. `bs-1` and `bs-2` have disjoint write sets
  (`deliverables/0.9.0_WK_AMGT_HARVST~129/`; `lib/opal_data_harvest/install-cycle-schedule.ps1`) and no edge. `bs-3`
  depends on `bs-2`'s merge and is issued HELD.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bs-1` | `bs-1` | **Rebuild #11's signing dry run (R28):** `build()` at HEAD differs from the frozen r72 list in exactly AIG_US_Equity, OMAB_MM_Equity and OMAB_US_Equity. The rebuild #10 rule is run against the served rebuild #10 parts with PUTS 0, plus per list-moved security the pairs served, built, gone and added, and the first ten gone and added titles each, for `3.0.0_SA_CVO~Z`. | LOCAL | worker ~129 |
| `HVST-bs-2` | `bs-2` | **The installer takes `-Publishers`.** Today `install-cycle-schedule.ps1:11` passes no `--publishers`, so the runner would run its default four, sa included; placement 2 needs bbg, wsj and barrons alone. An unknown name (the FT) is refused, and with no `-Publishers` the arguments are unchanged. | SERVED | worker-light ~130 |
| `HVST-bs-3` | `bs-3` | **The runner registered at log-on on the site Z box, bbg, wsj and barrons, against a PINNED checkout of the merged `bs-2`; acceptance per publisher is the first completed cycle record with no one at the box.** Ordered to site Z's producer seat, `0.7.0_AE_CloudOps~Z`, through `0.0.0_AB_MSTR~DELL1`. HELD until `bs-2` is merged under its pair and the issuer sends the pin. | WORLD | `0.7.0_AE_CloudOps~Z` (held) |
| `HVST-bs-4` | `bs-4` | **The r47 Seeking Alpha backfill resumed from its own checkpoint (133 done) as a DECLARED detached job on the site Z box, with completion reported to `0.0.0_AB_MSTR~DELL1`.** WORKSTREAM `R47` (its own issuance; write surface `deliverables/0.7.0_AE_CloudOps~Z/r47/`), cut after round 75's issuance @c7909af157 on `1.0.0_SA_CTO~DELL1` msgs 1430 and 1441 and site Z `1.0.0_SA_CTO~Z` msg 32271 (MSTR msg 1436), before anything of round 75 was spawned. Its completion lets the runner add sa and meets the `bo-1`/`bp-1` pair's C-a. | WORLD | `0.7.0_AE_CloudOps~Z` |
| `HVST-bs-5` | `bs-5` | **Rebuild #12's signing dry run: R30 served.** The baseline is rebuild #11's parts and the r75 list; every removed pair must be in br-1's R30 class (br-1's own classifier), counted beside the census's 280; any change outside the class is listed and is a STOP. WORKSTREAM `R12`, on `1.0.0_SA_CTO~DELL1` msg 1939 (ADDENDUM @745633e993). | LOCAL | worker ~131 |

**Not orders (the issuer's acts, each under its own never-widen pair, in placement 3's order):** rebuild #11's served write
on `bs-1`'s output after `3.0.0_SA_CVO~Z` grades the titles; then `br-1`'s merge (branch 126 @c868d27d87); then `bq-2`'s
merge (branch 125 @09642610bd). Each lands in a producer path or served gold, so `1.0.0_SA_CTO~Z`'s half is signed before
each act (msg 1267). The `bo-1`/`bp-1` merge (branch 123 @537ac56e9b, both halves signed) waits only on its C-a: the r47
leg is to resume from checkpoint 133 (msg 1430), so C-a holds again when that leg completes.

**NOT cut:** the runner's `sa` cycle, which joins on site Z's report that r47 COMPLETED (msg 1430); FWD-18 hop 3, cut once
cycle records exist (placement 4).

**Checks dry-run at the base before the cut (box/dell1 HEAD, 2026-10-09 ~02:1xZ):**
- `bs-1` AC1, AC2, AC3 base: FAIL as expected (no such file).
- `bs-2` AC1 base: FAIL as expected (the ACTION line carries no `--publishers`). AC2 base: FAIL as expected (no refusal
  printed). AC3 base: PASS as expected (ACTION ends `STOP"`, followed by WORKDIR).
- `bs-5` AC1, AC2, AC3 base: FAIL as expected (no such file).
- `bs-4` AC1, AC2 base: FAIL as expected (no such file; they are written on the site Z box).
- `bs-3` AC1, AC2: not run at the base. They read a scheduled task on the site Z box, which this box cannot read; the base
  state is `TASK ABSENT` per `br-3`'s close (@ef68288dee).

**AMENDMENT 1 to section 86 (issuer `2.0.0_SA_COO~W1`, on `1.0.0_SA_CTO~DELL1`'s round-74 placement 1):** "`bq-2`'s merge
is HELD while any collection leg runs" now reads "`bq-2`'s merge is HELD while a collection leg runs FROM THE TREE BEING
MERGED INTO". The runner runs from a PINNED checkout, which moves only by an explicit re-pin, never by box-sync. The merge
is still a site-Z deploy under a never-widen pair carrying `1.0.0_SA_CTO~Z`'s half. No gate limb graded this amendment: the
decomposition is not a task order, and `to-pipeline-gate.py` grades task orders.

## 89. ROUND 76 -- R31: a common-word alias needs a second anchor (`1.0.0_SA_CTO~DELL1` msg 2333, `ledger/ROUND_ANALYSIS.round74.md` ADDENDUM 3), 2026-10-09 ~11:2xZ

Rebuild #12 served R30 (graded ACCEPT 50 of 50, @7104334f35; ledger closed @b89f2f09c4). The CVO's finding: 14 of 20 kept
count-down rows are still off-topic (8 travel visas, 6 fruit or colour "Orange"). R31 rules the next matcher rule. Round 75
still holds bs-3 and bs-4 at site Z and the bo-1/bp-1 and bq-2 merges (which wait on r47); this round does not touch them.

Issuer `2.0.0_SA_COO~W1`. Series **`bt`**.
- **Fan-out:** 1 of 1 chain, cap 8.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bt-1` | `bt-1` | **R31 in gold's matcher, behind `_COMMON_WORD_SECOND_ANCHOR_RULE`.** The common-word alias set is MEASURED against a vendored public-domain word list (hash recorded). A second anchor is the ticker, the full name, or another non-common alias of the same security. Tests with a mutant, plus a MENTION-grain census on served rebuild #12: mentions before and after, pairs removed and counted down, the CVO's 14 rows, and a 20 removed / 20 kept sample. | SERVED | worker ~132 |

**Then (not orders):** bt-1's merge under its own pair; rebuild #13 serving R31 under its own pair (dry run, then act),
on the same ladder as br-1 and #12.

**Checks dry-run at the base before the cut:**
- `bt-1` AC1 base: FAIL as expected (no tests ran: the test is absent). AC2 base: FAIL as expected (no such file).
  AC3 base: PASS as expected (518 passed).

## 90. ROUND 77 -- FWD-18 hop 3's precondition: the activated runner's cycle records, read at site Z (`1.0.0_SA_CTO~DELL1` msg 2464, `ledger/ROUND_ANALYSIS.round76.md` @509739cb9d), 2026-10-09 ~13:2xZ

Round 76 closed: bt-1 AC4 MET, R31 retired, records only (@43019e178e). The analysis's item 1 cuts the page that says when a
publisher did not run only if the activated runner's cycle records exist. At the cut, `origin/box/sitez` holds 0
`*.cycle.json` under `deliverables/0.7.0_AE_CloudOps~ZW/`. The records are not in the repo, so the cell is the read at
site Z. Carried, not cut: the `sa` cycle after r47 (bs-4), and bo-1/bp-1 and bq-2's merges.

Issuer `2.0.0_SA_COO~W1`. Series **`bu`**.
- **Fan-out:** 1 of 1 chain, cap 8.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bu-1` | `bu-1` | **The runner's cycle records, read at site Z.** Per publisher (bbg, wsj, barrons): files, completed, completed after activation, the newest record's fields; the task state and the runner process. Read-only; restart nothing. | LOCAL | `0.7.0_AE_CloudOps~ZW` |

**Then (not orders):** with records in hand, round 78 cuts the page that says when a publisher did not run (FWD-18 hop 3).

**Checks dry-run at the base before the cut:**
- `bu-1` AC1, AC2, AC3 base: FAIL as expected (no such file).

**AMENDMENT 1 to section 90 (2026-10-09 ~15:0xZ, issuer), WORKSTREAM `B`** (`1.0.0_SA_CTO~DELL1` msg 2605). bu-1 landed @48864ff38b
(0 completed cycles; bbg stopped "error", failed 3; wsj and barrons stopped "sign_in_refused"; r47 JOB-EXIT rc=0). One read cell
is added; the wsj and barrons hand sign-in goes to site Z as a crossbox CALL, not a cell.
- **Fan-out:** 1 of 1 chain, cap 8.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bu-2` | `bu-2` | **Why bbg's first cycle stopped on "error".** The checkpoint's failed keys and their errors verbatim, the run summary's error fields, the runner log around 12:55Z, and the current cycle's progress. Read-only; restart nothing. | LOCAL | `0.7.0_AE_CloudOps~ZW` |

**Checks dry-run at the base before the cut:** `bu-2` AC1, AC2, AC3 base: FAIL as expected (no such file).

## 91. ROUND 78 -- a pair error does not stop the cycle (`1.0.0_SA_CTO~DELL1` msg 2724, on HVST-bu-2 @6e5290eafb), 2026-10-09 ~16:0xZ

bu-2 read why bbg's first cycle stopped. 88 pairs were no_new_articles, then 3 pair jobs returned `error`, and the driver's
transient-stop rule stopped the publisher with 151 pairs never started. The error text is dropped by `record_job_outcome`,
and the runner writes no log. r47 (sa) stopped the same way at 134 of 242 (bs-4's closure read, STOPPED-INCOMPLETE). The CTO
ruled (a) keep the detail, (b) in cycle mode a pair error counts as failed and the cycle runs on, with 5 consecutive errors
still stopping the publisher, and (c) a log. The merge goes under the site-Z producer pair. Carried: bs-3 (needs Andrew's
WSJ/Barron's sign-in at site Z, site-Z call 9f24), bs-4 (r47 incomplete), bu-1/bu-2 flips.

Issuer `2.0.0_SA_COO~W1`. Series **`bv`**.
- **Fan-out:** 1 of 1 chain, cap 8.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bv-1` | `bv-1` | **A pair error keeps its detail, counts as failed, and the cycle runs to the end of the list.** `MAX_CONSECUTIVE_PAIR_ERRORS = 5` still stops the publisher, with the last detail as the reason. A cycle that reached every pair is completed with `failed` and `failures` stated. The runner appends its output to `<state-dir>/cycle_runner.log`. Fixture tests and a mutant. | SERVED | worker ~133 |

**Then (not orders):** bv-1's merge under the site-Z producer pair (COO + `1.0.0_SA_CTO~Z`); the re-pin of site Z's runner to
the merged commit (a WORLD act under its own pair); the live read of bbg's next cycle (242 of 242, details kept).

**Checks dry-run at the base before the cut:**
- `bv-1` AC1 base: FAIL as expected (no test file). AC2 base: PASS (53 passed). Full `lib/opal_data_harvest` suite at the base:
  5 failed, 770 passed, 3 skipped (pre-existing; named in the order).

## 92. ROUND 79 -- the bbg live cycle under round 78's code (`1.0.0_SA_CTO~DELL1` msg 2937, `ledger/ROUND_ANALYSIS.round78.md`), 2026-10-09 ~18:0xZ

Rounds 77 and 78 MAY-CLOSE. bv-1 is merged at b5a7a3a4b6 (on CLOUD). No live completed cycle has been read, so FWD-18's acceptance
is unmet. The analysis's enrichment list: (1) read bbg's next cycle to its end under the new code; (2) wsj and barrons wait on
Andrew's hand sign-in (site-Z call 9f24), and no cell is cut for them; (3) the hop-3 page, cut once (1)'s completed record
exists; (4) the issuer dispositions the 18 stale remediation rows in round 79's packet (an issuer act, not a cell).

Issuer `2.0.0_SA_COO~W1`. Series **`bw`**.
- **Fan-out:** 1 of 1 chain (bw-1 -> bw-2), cap 8.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bw-1` | `bw-1` | **Re-pin site Z's runner to b5a7a3a4b6**, keeping the old pin's state dir and runtime root (cycle history and re-queue carry over). The installer is run with `-Plan` first, then once; the reaper dry run lists the runner EXEMPT; the old pin is the rollback. Under its own never-widen pair. | WORLD | `0.7.0_AE_CloudOps~ZW` |
| `HVST-bw-2` | `bw-2` | **bbg's first post-re-pin cycle, read to its end.** The BBG CYCLE line, `requeued`, every failure with its detail verbatim, the runner log, the record copied. AC3 (judgment, CVO): 242 of 242 attempted, failures with detail, a stop only on the cap. | LOCAL | `0.7.0_AE_CloudOps~ZW` |

**Then (not orders):** the hop-3 page on bw-2's record; the wsj and barrons reads on Andrew's sign-in.

**Checks dry-run at the base before the cut:**
- `bw-1` AC1 and AC2 are site-Z reads and cannot run from dell1 (by bu-1, AC1 would FAIL: WORKDIR is the old pin). AC3 base: FAIL
  as expected (no such file).
- `bw-2` AC1 and AC2 base: FAIL as expected (no such file).

## 93. ROUND 80 -- the enqueue tier fence, failure reasons, and the staged bs-3 successor (`1.0.0_SA_CTO~DELL1` msg 4352, `ledger/ROUND_ANALYSIS.round79.md` section 2), 2026-10-12 ~13:4xZ

Round 79 slugged MAY-CLOSE (`3.0.0_SA_CVO` msg 4351, ADJUDICATION_v71 @b284aa2d50). bw-2 AC3 graded FAIL on clause 3 (all 8 failure
details the bare word `error`, row D1-S7). The analysis's enrichment list: (1) the research-pull-enqueue tier fence, FIRST, fail
closed, four arms; (2) D1-S7: every failure row carries its reason; (3) bs-5's instance rows amended to the two-class rule, which
releases round 75's slug; (4) bs-3's successor, STAGED on Andrew's WSJ/Barron's sign-in.

Issuer `2.0.0_SA_COO~W1`. Series **`bx`**.
- **Fan-out:** 2 of 2 chains (bx-1 -> bx-2; bx-3), cap 8.
- **Item 1 is cut as TWO cells** (build, then deploy) because a worker is LOCAL-only and a deploy is a WORLD act under its own
  pair, as the CTO's ruling says ("under its own pair"). It is one outcome; the split is the class boundary, not extra scope.
- **Item 3 is an issuer amendment, not a cell** (done @812da3235c; round 75 reads MAY-CLOSE).

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-bx-1` | `bx-1` | **The enqueue handler refuses a non-internal caller.** `lambda_handler` reads the authorizer `tier`, 403 unless exactly `internal`, no context is 403 (fail closed), the fence before any S3 or SQS call; unit tests (four arms and a mutant); `check_e2e.py` amended to send an internal context and given `--enqueue-only`. | WORLD by the gate's path floor (an `infra/aws/lambda/` path); the cell executes no world act | worker `0.9.0_WK_AMGT_HARVST~134` |
| `HVST-bx-2` | `bx-2` | **The fenced handler deployed, and the deployed function proved.** Build, upload, a targeted plan that changes only the code hash, one `safe-apply`, and three side-effect-free invocations (no ticker): non-internal 403, no context 403, internal with no ticker 400. Under its own never-widen pair. The authorizer's `tier` field is read before the apply (C-d). | WORLD | `0.7.0_AE_CloudOps~HV1` |
| `HVST-bx-3` | `bx-3` | **Every failed pair names its reason.** The exception class and the vendor's message, cut to 300 characters, secrets redacted, no full body; a success row unchanged; planted failure of each kind in the fixture. | LOCAL | worker `0.9.0_WK_AMGT_HARVST~135` |
| `HVST-bx-4` | (none) | **bs-3's successor, STAGED.** bbg, wsj and barrons each ending a completed cycle unattended, graded by the CVO. It names Andrew's Barron's and WSJ sign-in at site Z as its one wait (a vendor login is his act). Cut the turn the sign-in is on record. | LOCAL (read) | `0.7.0_AE_CloudOps~ZW` |

**Then (not orders):** bx-3's merge under a never-widen pair (COO + the CTO's producer half); a re-pin of site Z's runner to the
merged commit (a WORLD act under its own pair) and a bbg cycle read in which failures name their reasons; the full live e2e of the
research seam, if the CTO wants it, through the Bloomberg queue.

**Checks dry-run at the base before the cut:**
- `bx-1` AC1 and AC2 base: FAIL as expected (no test file; "no tests ran").
- `bx-3` AC1 base: FAIL as expected (no test file). AC2 base: PASS as expected (63 passed in 12.8 s).
- `bx-2` AC1, AC2 and AC3 base: FAIL as expected (the `.out` files do not exist).
- Full `lib/opal_data_harvest` suite at the base: 5 failed, as named in bv-1's order (pre-existing).

## 94. ROUND 81 -- the refusal log line, and the runner re-pin (`1.0.0_SA_CTO~DELL1` msg 4394, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1), 2026-10-12 ~14:3xZ

Round 80 slugged MAY-CLOSE: bx-1 merged @824bdb355b, bx-2 deployed @adfc9044a0 (arms 403/403/400), bx-3 merged @1c69fa35a3. The
CTO's addendum: the fence stays exact (no per-function userType exception; the laptop counts Dev users whose tier is not internal,
0 closes D1-S9); round 81 = (1) a refusal log line carrying the tier string (closes D1-S8 and makes his post-act read observable),
(2) the site Z runner re-pin as a crossbox ORDER through MSTR (the symptom of row D1-W135-S2 persists until it).

Issuer `2.0.0_SA_COO~W1`. Series **`by`**.
- **Fan-out:** 2 of 2 chains (by-1 -> by-2; by-3), cap 8.
- **Item 1 is a build cell and a deploy cell, as in round 80** (a worker is LOCAL-only; a deploy is a WORLD act under its own pair).
- `HVST-bx-4` (bs-3's successor) stays STAGED on Andrew's WSJ/Barron's sign-in; it is not cut.

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-by-1` | `by-1` | **A refusal is logged with the tier it saw.** The fence's refusal branch writes `DENIED: tier=<tier or NONE>` (printable ASCII, cut to 32, nothing else: no ticker, body, account or user), the log call cannot change the 403; success path byte-for-byte; unit tests and a mutant. | WORLD by the gate's path floor; no world act | worker `0.9.0_WK_AMGT_HARVST~136` |
| `HVST-by-2` | `by-2` | **The refusal-logging handler deployed and proved.** The round-80 act again: build, upload, a targeted plan of one change, one `safe-apply`, three side-effect-free arms (no ticker), and a log read showing `DENIED: tier=partner` and `DENIED: tier=NONE` and no `internal`. Under its own pair. | WORLD | `0.7.0_AE_CloudOps~HV1` |
| `HVST-by-3` | `by-3` | **The site Z runner re-pinned to 1c69fa35a3** (bx-3 merged), state dir and runtime root carried, the cycle ended by its stop file first (not killed), both pin worktrees LOCKED against the govern GC (row Z-S111), a kill-maint dry run lists it EXEMPT. Under its own pair; delivered as a crossbox ORDER. | WORLD | `0.7.0_AE_CloudOps~ZW` |

**Then (not orders):** a bbg cycle read in which failures name their reasons (FWD-18's acceptance, graded by the CVO); adding sa to
the runner (its own cell and pair); the first real internal enqueue read in the function's log; the CTO's Dev-user count.

**Checks dry-run at the base before the cut:**
- `by-1` AC1 base: FAIL as expected (no test file). AC2 base: PASS as expected (`test_bx1_tier_fence.py`: 15 passed).
- `by-2` AC1, AC2 and AC3 base: FAIL as expected (the `.out` files do not exist).
- `by-3` AC1 and AC2 are site Z reads and cannot run from dell1: AC1 would read `wk-harvest-runner-pin-b5a7a3a4b6` and FAIL as expected;
  AC2 reads the old state dir and would PASS today (it must still hold after, which is its point). AC3 base: FAIL as expected (no such file).

## 95. ROUND 81, ADDENDUM -- the fence admits a Dev login (`1.0.0_SA_CTO~DELL1` msg 4413, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 2; row D1-S9), 2026-10-12 ~14:4xZ

The CTO, as the cluster lead, reversed his own ADDENDUM 1 on the laptop CTO's count (msg 108578: 3 of 6 Dev logins carry a tier other
than internal, all opal-capital admins): the fence admits `tier == internal` OR `userType == Dev`, no context still 403. He ruled it
rides by-2's deploy if by-1 is not merged, "otherwise its own pair". by-1 is merged @31590746f1 and by-2's deploy had begun, so it is
its own build (by-4) and its own deploy (by-5). Series `by` continues. This is a SECOND WORKSTREAM of round 81 (`<workstream>DEVADMIT</workstream>`, as round 75's R47 was): the L6 gate admits one issuance per round per workstream and round 81's first issuance is section 94.

- **Fan-out:** 1 of 1 chain (by-4 -> by-5), cap 8. (by-1 -> by-2 and by-3 are section 94.)

| cell | order | what | class | executes |
|---|---|---|---|---|
| `HVST-by-4` | `by-4` | **The fence admits a Dev login.** `_caller_user_type` beside `_caller_tier` (same two places, the authorizer context only, never the body); admit when `tier == "internal"` or `userType == "Dev"`, exact, case-sensitive; no context 403; log line unchanged (tier only); unit tests and a mutant. | WORLD by the gate's path floor; no world act | worker `0.9.0_WK_AMGT_HARVST~137` |
| `HVST-by-5` | `by-5` | **The Dev-admitting fence deployed and proved.** The same act as by-2 after it: build, upload, a targeted plan of one change, one `safe-apply`, four side-effect-free arms (no ticker): Dev with an advisor tier 400, advisor non-Dev 403, no context 403, internal 400. Under its own pair. | WORLD | `0.7.0_AE_CloudOps~HV1` |

**Checks dry-run at the base before the cut:**
- `by-4` AC1 base: FAIL as expected (no test file). AC2 base: PASS as expected (`test_bx1_tier_fence.py` and `test_by1_refusal_logged.py`).
- `by-5` AC1, AC2 and AC3 base: FAIL as expected (the `.out` files do not exist).

## 96. ROUND 81, WORKSTREAM DEVREVERT -- the Dev-admit ruling withdrawn (`1.0.0_SA_CTO~DELL1` msg 4463, `ROUND_ANALYSIS.round79.md` ADDENDUM 3 @b5915fba35), 2026-10-12 ~15:3xZ

The laptop CTO (msg 108607): the token's `tier` derives from `firmId` (opal-capital means internal), so the Dev rows already log in as
internal. The Dev-admit ruling of section 95 is WITHDRAWN and the fence stays tier-only; D1-S9 closes NOT EXPOSED (on NFRA_CTLPLN PRD
v0.27). The STOP arrived after by-4 had merged (f94560218c) and by-5 had deployed (33189f2667, 14:40:46Z).

- `HVST-by-4` and `HVST-by-5` go to `cancelled` by that ruling; by-4's code is reverted in the repo by by-6's step 0 (the COO lane cannot write
  `infra/aws`; and not by `git revert` of the merge: that would also remove the channel rows and the proof instance, which are append-only).
- **`HVST-by-6`** (seat `0.7.0_AE_CloudOps~HV1`, WORLD): the live function is restored to HVST-by-2's artifact **by S3 object version**,
  so its code hash EQUALS the by-2 deploy's (`cWiraC3E...`, the CTO's added proof, msg 4465), with the deployed source read back and four
  side-effect-free arms (Dev with an advisor tier 403, advisor 403, no context 403, internal 400). Covered by by-2's signed artifact and
  by ADDENDUM 3; no widening act.
- **Fan-out:** 1 of 1 chain (by-6), cap 8.
- **Checks dry-run at the base:** `by-6` AC1, AC2 and AC3 base: FAIL as expected (the `.out` files do not exist).

## 97. ROUND 82 -- STAGED: the site Z runner re-pin, carried from round 81 (`1.0.0_SA_CTO~DELL1` msg 4476), 2026-10-12 ~16:2xZ

`HVST-by-3` (re-pin site Z's cycle runner to `1c69fa35a3`, the bx-3 merge) could not be delivered: site Z's manager session has not
consumed its inbound queue since 13:45Z, so `~ZW` never saw the crossbox ORDER. The CTO cancelled by-3 and staged this successor for
round 82 (msg 4476), which carries his by-3 half unchanged while the pin stays `1c69fa35a3` and the act is the same.

| cell | what | class | executes | un-park condition |
|---|---|---|---|---|
| `HVST-bz-1` (STAGED, no order cut) | **The site Z runner re-pinned to `1c69fa35a3`**, exactly by-3's act and steps: the running cycle ended by its stop file (not killed), the state dir and runtime root carried, both pin worktrees LOCKED against the govern GC, a kill-maint dry run lists it EXEMPT; the first ended cycle record under the new pin closes row D1-W135-S2. Under the carried pair. | WORLD | `0.7.0_AE_CloudOps~ZW` | site Z's manager consuming (the restart expected after the laptop returns, around 19-20Z); then `1c69fa35a3` an ancestor of origin/CLOUD, read at the act |

**Disposition of row D1-W135-S2 (ARMED, disarm owner this seat):** CARRIED to `HVST-bz-1`, owner `~ZW`.
**Fan-out when cut:** 1 of 1 chain, cap 8. It is cut the turn the un-park condition reads true, by a crossbox ORDER through MSTR, as by-3 was.

## 98. ROUND 82 -- the driven post-deploy read; the re-pin and bs-3's successor stay staged (`1.0.0_SA_CTO~DELL1` msg 4486, `ledger/ROUND_ANALYSIS.round81.md` section 2), 2026-10-12 ~16:4xZ

Round 81 slugged MAY-CLOSE (CVO msg 4485, ADJUDICATION_v73 @40d147647f) and the CTO graded rounds 80 and 81: the fence HOLDS (live hash
equals by-2's, handler byte-equal to HEAD, arms 403/403/400); the refusal log line HOLDS (D1-S8 closed); DEVADMIT was cancelled and rolled
back (D1-S9 NOT EXPOSED); bx-3 is merged and NOT SERVED at site Z (the runner still runs b5a7a3a4b6; W135-S2 stays ARMED). OWED, not passed:
his bx-2 post-act read. His process note for the issuer: a deploy that rests on a cross-box ruling still being applied at the other box
waits for that box's apply receipt (discipline, not a gate); by-5 deployed 50 minutes before the withdrawal.

Issuer `2.0.0_SA_COO~W1`. Series **`bz`**. Round 82's ONE issuance:

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-1` | (none) | the site Z runner re-pinned to `1c69fa35a3` (section 97) | WORLD | `0.7.0_AE_CloudOps~ZW` | STAGED, un-parked when site Z's manager consumes |
| `HVST-bz-2` | `bz-2` | **The post-deploy read, DRIVEN.** One internal-context enqueue of ONE covered ticker, `SAP GY Equity` (its pack prefix exists; no status object exists, so the act CREATES it and overwrites nothing; amended after the seat's C-b stop, row D1-S12), once; its 202, the status object, the queue's message count and the absence of a `DENIED` line since T0 are read. The consumer is NOT started (no Bloomberg draw). | WORLD | `0.7.0_AE_CloudOps~HV1` | CUT |
| `HVST-bx-4` | (none) | bs-3's successor: bbg, wsj and barrons each ending a completed cycle unattended, graded by the CVO | LOCAL (read) | `0.7.0_AE_CloudOps~ZW` | STAGED on Andrew's WSJ/Barron's sign-in |

Round 75's held slug releases on the issuer's bs-5 amendment (@812da3235c): carried, not re-ruled. The CVO sends it.

- **Fan-out:** 1 of 1 chain (bz-2), cap 8.
- **Not orders:** a restart of site Z's manager session (Andrew only if no manager can); the WSJ/Barron's sign-in (Andrew).

**Checks dry-run at the base before the cut:**
- `bz-2` AC1, AC2 and AC3 base: FAIL as expected (the `.out` files do not exist).

## 99. ROUND 83 -- the runner re-pin, un-parked (`1.0.0_SA_CTO~DELL1` msgs 4476 and 4505, `ledger/ROUND_ANALYSIS.round81.md` and `.round82.md`), 2026-10-12 ~20:5xZ

The CTO ruled round 83 is not cut until `HVST-bz-1` or `HVST-bx-4` un-parks (msg 4505). `bz-1`'s un-park condition was "site Z's manager
consuming". MSTR~DELL1 msg 4547 (from site Z's manager, bus 1634215e, measured there): crossbox ORDER 5f49 reached `~ZW`'s inbox at
2026-10-12T20:28:19Z, so the condition reads true. The cause of the earlier silence is corrected: site Z was dark 14:09Z-20:27Z on a WEEKLY
LIMIT that resets 2026-10-14 06:00Z; only the manager and its CTO have run since 20:27Z. `~ZW` reads LIVE and IDLE, telemetry stopped at 14:09Z.
Whether the other site Z seats resume is Andrew's call. The EXPIRED-state item was carried (YAGNI, msg 4505): it is not a cell.

Issuer `2.0.0_SA_COO~W1`. Series **`bz`** continues (the staged id `HVST-bz-1` of section 97).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-1` | `bz-1` | **The site Z runner re-pinned to `1c69fa35a3`**: by-3's act, the running cycle ended by its stop file (not killed), state dir and runtime root carried, both pin worktrees LOCKED, a kill-maint dry run lists it EXEMPT. The first cycle record under the new pin closes row D1-W135-S2. The CTO's by-3 half and the COO half carry unchanged. | WORLD | `0.7.0_AE_CloudOps~ZW` | CUT (a crossbox ORDER through MSTR) |
| `HVST-bx-4` | (none) | bs-3's successor | LOCAL (read) | `0.7.0_AE_CloudOps~ZW` | STAGED on Andrew's WSJ/Barron's sign-in |

- **Fan-out:** 1 of 1 chain, cap 8.
- **Not orders:** whether the dark site Z seats resume (Andrew); the weekly limit resets 2026-10-14 06:00Z.

**Checks dry-run at the base before the cut:**
- `bz-1` AC1 and AC2 are site Z reads and cannot run from dell1 (AC1 would read `wk-harvest-runner-pin-b5a7a3a4b6` and FAIL as expected;
  AC2 reads the old state dir and would PASS today, which is the point: it must still hold after). AC3 base: FAIL as expected (no such file).

## 100. STAGED, NOT ISSUED -- the runner can never block on a console selection (row `AMGT_HARVST-Z-S115`; CTO half ADDENDUM 1 item 4, `1.0.0_SA_CTO~DELL1` msg 4645), 2026-10-13 ~06:4xZ

**Why it exists.** Round 83's `HVST-bz-1` found the site Z runner stopped for 9 h 24 m by the console's QuickEdit selection state (title
`Select C:\Program Files\Python314\python.exe`; the runner blocks on its next console write, so it never reached its stop-file check). One Escape
released it and it ended itself with zero pairs lost. Nothing stops the next click: the runner is still launched as a console `python.exe`. This is
a STATE-coherence defect of the launch, and it is staged for the next round (the issuance comes from the CTO's round-83 analysis, not from here).

**The fix is the launch, not a monitor** (moratorium): the task starts a windowless interpreter, so there is no console to select.
`install-cycle-schedule.ps1` already takes a `-Python` parameter (line 17), so the installer needs at most a default, not a rewrite.

| cell | what | class | executes | state |
|---|---|---|---|---|
| `HVST-bz-3a` | **The installer registers the runner windowless by default:** `-Python` resolves to the `pythonw.exe` beside `python.exe` when none is given, and `-Plan` prints it. A test builds the runner's `say()` and its cycle record under `sys.stdout = None` and `sys.stderr = None` (what `pythonw` gives) and shows no exception. | LOCAL | `0.9.0_WK_AMGT_HARVST~<n>` (a worker, one cell, about 40 lines) | STAGED |
| `HVST-bz-3b` | **Site Z re-registered once windowless:** the stop-file stop (it now ends in seconds at a pair boundary), `-Plan` read first, register once, start once, the census reads one runner whose image is `pythonw.exe`. Both pins stay locked. | WORLD | `0.7.0_AE_CloudOps~ZW` | STAGED behind 3a, needs a signed pair |

- **Alternative named and not chosen:** `HKCU\Console\...QuickEdit=0` for `python.exe`. It changes every python console of that Windows user on
  that box, so its blast radius is wider than this task. Left to the CTO's analysis.
- **Open to the CTO:** whether the runner's log lines can all reach a file without a console (the order's own evidence reads the log file, so yes
  by reading; 3a's test is what proves it).
- **Not issued here:** round 83 is one order, and a second cell in it is a second issuance in the round.

## 101. ROUND 84 -- the runner with no console, and the first ended cycle read (`1.0.0_SA_CTO~DELL1` msg 4670, `ledger/ROUND_ANALYSIS.round83.md` section 3), 2026-10-13 ~07:2xZ

Input: the CVO's slug msg 4669 (`ADJUDICATION_v75` @d3501cc7f3, MAY-CLOSE) and the CTO's round-83 analysis @bcb24fcac3. Row `AMGT_HARVST-Z-S115` is ARMED
(disarm owner this seat, the disarm act is this round's first cell). The interim for the running cycle was sent same turn (MSTR relay to `~ZW`).
Issuer `2.0.0_SA_COO~W1`. Section 100's `bz-3a` is cut as **`HVST-bz-3`** and `bz-3b` is **`HVST-bz-4`** (ids without a letter, for the gates).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-3` | `bz-3` | **The runner can run with no console window.** `Tee` tolerates a `None` real stream; the installer gains `-Windowless` (the `pythonw.exe` beside `python.exe`); a test runs the cycle runner under the REAL `pythonw.exe` and carries a mutant (the unguarded `Tee` ends the cycle as `AttributeError`). | LOCAL | worker `0.9.0_WK_AMGT_HARVST~138` | CUT |
| `HVST-bz-5` | `bz-5` | **The first ENDED bbg cycle under the new pin is read**: every failure names its reason (`FAILED` = `NAMED` >= 1), read-only, no plant. Start condition: such a record exists (about 17:00Z). Closes D1-W135-S2's CARRIED_BY. | LOCAL (read) | seat `0.7.0_AE_CloudOps~ZW` | CUT (crossbox ORDER) |
| `HVST-bz-4` | (cut after bz-3's merge) | **Site Z re-registered windowless** at a cycle boundary by the stop file, `-Plan` read first, one runner whose image is `pythonw.exe`, no `conhost.exe` child, the log writing for three consecutive jobs; both pins locked; before the old interpreter is retired the first real cycle under `pythonw` is read. | WORLD | seat `0.7.0_AE_CloudOps~ZW` | STAGED: cut under workstream `WINDOWLESS-SITEZ` once its pin `M` (bz-3's merge) is a real commit and the pair is signed |
| plant | (none) | **A planted failing pair** for D1-W135-S2, only if bz-5 reads `FAILED=0`. Writes the state dir on a live producer, so its own pair. | WORLD | `0.7.0_AE_CloudOps~ZW` | STAGED, conditional |
| `HVST-bx-4` | (none) | bs-3's successor | LOCAL (read) | `0.7.0_AE_CloudOps~ZW` | STAGED on Andrew's WSJ/Barron's sign-in |

- **Fan-out:** 1 worker of 2 chains (bz-3 and bz-5 share no file and no edge), cap 8. bz-5 is a seat order, not a spawn.
- **Why bz-4 is not cut in this issuance:** its pin is the merge commit of bz-3, which does not exist yet, and a placeholder pin on a WORLD order is a
  hole the seat can step into. The same shape as `by-3` -> `bz-1` and the DEVADMIT workstream.
- **Why `pythonw`:** QuickEdit-off stops a mouse selection but not the console's Mark command; no console has neither. Recorded on bz-3's issuer notes.
- **Order of the two site Z acts:** bz-5's record must exist before `bz-4` re-registers, or the stop at the boundary writes the record bz-5 reads as a
  `stopped_by_operator` one; bz-5 reports `STOPPED=` in its line so that is visible, not hidden.
- **Not orders:** Andrew's WSJ/Barron's sign-in; the reader-side EXPIRED rule (rides the first pull-status reader, carried).

**Checks dry-run at the base before the cut:** bz-3 AC1 base: FAIL as expected (`no tests ran`: the file does not exist); bz-3 AC2 base: PASS as expected
(`61 passed`); bz-5 AC1 base: FAIL as expected (the round-79 record prints `FAILED=8 NAMED=0`), with a PASS control (`FAILED=8 NAMED=8`) and a no-record
arm (`NO-ENDED-CYCLE-SINCE`, rc 1).

## 102. ROUND 84, workstream WSJBARRONS -- `HVST-bx-4` UN-PARKED on the existing credential (`1.0.0_SA_CTO~DELL1` msg 4795, Andrew-direct 2026-10-13 ~12:2xZ item 4), 2026-10-13 ~12:5xZ

Andrew: "we have credentials and HARVEST scripts that do this". The act asked of him (open call 8c66, WSJ/Barron's sign-in) is withdrawn. The CTO: find the
existing credential and the script, read where each lives without printing the secret, cut bx-4's successor on them, no new vendor scope.

**Where they live (names and metadata only, no value read):** the credential is the Secrets Manager secret `dowjones/credentials` (us-east-1), one secret
for `wsj` and `barrons` (`lib/opal_data_harvest/credentials.py` `CREDENTIAL_SECRETS`; it exists, one version, changed 2026-09-14); the sign-in is
`org/tier1_exec/4.0.0_SA_CRO/scripts/dowjones_harvest_session.py`, called by `lib/opal_data_harvest/auth.py` `SessionManager._refresh`, which saves the
session to the box's own DPAPI vault (`SessionVault`). The runner is `--no-sign-in`, so a publisher without a valid saved session ends `sign_in_refused`.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-6` | `bz-6` | **`wsj` and `barrons` each hold a valid saved session**: state read first; ONE mint per publisher only where it reads `VALID=False`, through `SessionManager.refresh`; the first refusal stops both; no `--park`, no secret printed. | WORLD | seat `0.7.0_AE_CloudOps~ZW` | CUT (workstream WSJBARRONS); needs a signed pair before it is sent |
| `HVST-bz-7` | `bz-7` | **bx-4's acceptance, read only:** `wsj` and `barrons` each end a COMPLETED cycle (`completed true`, `stopped` none) unattended since 08:09:08Z. Organic, about a day (a pass is bbg, wsj, barrons in turn). | LOCAL (read) | seat `0.7.0_AE_CloudOps~ZW` | CUT |
| `HVST-bx-4` | (none) | **SUPERSEDED by bz-6 and bz-7**: its one wait (Andrew's sign-in) is withdrawn. | -- | -- | CLOSED as superseded |

- **Instruments (this seat's, tested):** `deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py` (+ `test_bz6_session_state.py`, 6 passed: it prints no cookie,
  username or token, and a refusal names the exception class only) and `bz7_publisher_cycles.py` (base and control arms dry-run).
- **Fan-out:** 0 workers (two seat orders), 2 chains, cap 8: bz-7 needs bz-6's instance.
- **Not orders:** a re-mint after a recorded `sign_in_refused` (its own order under its own pair, cut on the record); Seeking Alpha, FT and Bloomberg.

## 103. ROUND 84, workstream BRIEFOFF -- the 3 AM WSJ/FT morning brief is turned off (`1.0.0_SA_CTO~DELL1` msg 5131, Andrew-direct ~20:0xZ call 7), 2026-10-13 ~20:3xZ

Andrew: "No let's turn that off we don't need that." The CTO: disable `astn-wsjft-3am-run` under a pair; nothing deleted; rollback = re-enable.

**Measured at the cut (2026-10-13 ~20:2xZ):** the schedule is live, `State ENABLED`, `cron(0 3 * * ? *)` America/New_York, target Lambda `astn-wsjft-orchestrator`, input `{"mode":"run"}`, last modified 2026-06-25.
Denominator: 1 scheduler schedule and 0 EventBridge rules carry the `astn` prefix. Terraform: 1 writer, `aws_scheduler_schedule.astn_run` at `infra/aws/terraform/astn-pipeline/orchestrator.tf` line 175,
`state = "ENABLED"`. The next fire is 03:00 ET (07:00Z), so the act must land before then to spare tonight's run. The project record `org/projects/ASTN_WSJFT.json` is CLOSED (2026-08-25).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-8` | `bz-8` | **The schedule `astn-wsjft-3am-run` reads `DISABLED`** with its expression, target and input unchanged, and the Terraform source says the same (no drift): one attribute edited, a targeted plan that reads exactly 0 to add / 1 to change / 0 to destroy, a targeted `safe-apply`. Nothing is deleted; the Lambda, IAM, bucket, SNS and EC2 instance are not touched. | WORLD | seat `0.7.0_AE_CloudOps~HV1` | CUT (workstream BRIEFOFF); needs a signed pair before it is sent |

- **Fan-out:** 0 workers (one seat order), 1 chain of 1, cap 8. It shares no file with bz-7 (the only open round-84 order) and no edge with the runner.
- **Why a workstream and not the next round:** the schedule fires nightly; a cell cut after the round-84 L10 would let more runs go. Disjoint boundary (an AWS scheduler and one Terraform line, no harvest code, no site Z), disjoint write surface, a different `~lane` (`HV1`), one issuer.
- **Not orders:** deleting the schedule, the Lambda or the bucket; the dormant FT-reattempt code (stays as recorded); any change to the digest content or its recipients.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the live schedule reads `ENABLED`); AC2 base PASS as expected (the expression reads `cron(0 3 * * ? *)`, which is also its after-state: an unchanged-field control); AC3 base FAIL as expected (the source reads `"ENABLED"`).

## 104. ROUND 85 -- the session refresh, then the project PARKS (`1.0.0_SA_CTO~DELL1` msg 5209, `ledger/ROUND_ANALYSIS.round84.md` section 2; Andrew-direct ~21:1xZ), 2026-10-13 ~21:4xZ

Round 84 ended bx-4's acceptance NOT MET (row `AMGT_HARVST-Z-S119`): wsj returned 401 after 35 pairs and 69 minutes under `--no-sign-in`, barrons on its first key, though both saved sessions read `VALID=True` (a local predicate).
The CTO's ruling (A): the runner refreshes once per publisher per cycle through the existing `SessionManager`; no new credential path, no secret printed; the refusal class is recorded before the refresh, and if it is not
expiry the refresh cannot fix it and that is the finding; closed on one full cycle per publisher with the session alive at its end, or the named non-expiry cause. After round 85 the project PARKS and `~W1` stands down.

**Where the seam is (read, names and line ranges only):** each pair is one `collector run --no-sign-in ... --max-jobs 1` subprocess spawned by `backfill_driver.Collector.run_job` (about line 262); a persisted 401 raises `transport.AuthExpired`
(raise sites about lines 591 and 607), `worker.run_job` turns it under `--no-sign-in` into `SignInRefused` and the job status `sign_in_refused` (about lines 753-756 and 773-776); `drive()` (about line 360) treats `sign_in_refused` as a
STOP status. `auth.SessionManager.refresh(publisher)` is the existing sign-in. So the budget "once per publisher per cycle" belongs to `drive()`, which is called once per cycle and owns the checkpoint, not to the per-pair subprocess.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-9` | `bz-9` | **A refused pair carries its evidence, and the driver refreshes once.** `AuthExpired` carries `status`, `host`, `login_redirect`; the job record carries a `refusal` object (field names only, no body, no cookie); `drive()` prints a `REFUSAL` line and records it in the checkpoint for ANY stop status with its class from one explicit table over `STOP_STATUSES`; under a new flag `--refresh-once` (default OFF) a `sign_in_refused` job whose class is `expired` gets ONE `SessionManager.refresh(publisher)` per publisher per cycle (budget kept in the checkpoint, so a restart does not re-spend) and the SAME pair replays once; a second refusal in the cycle, a refresh that raises, or any other class makes no further sign-in. `cycle_runner` passes the flag; the installer gains `-RefreshOnce`. | LOCAL | worker `0.9.0_WK_AMGT_HARVST~139` | CUT |
| `HVST-bz-10` | (cut after bz-9's merge) | **Site Z re-registered with `-Windowless -RefreshOnce`** at a cycle boundary by the stop file, `-Plan` read first, one runner, both pins locked, the old pin kept as the signed rollback. | WORLD | seat `0.7.0_AE_CloudOps~ZW` | STAGED: cut under workstream `REFRESH-SITEZ` once its pin (bz-9's merge) is a real commit and the pair is signed |
| `HVST-bz-11` | (cut with bz-10) | **The close read, read only:** each of `wsj` and `barrons` ends one full cycle (`completed true`, `stopped` none) with the session alive at its end, OR the checkpoint's `REFUSAL` record names a non-expiry cause for the publisher. Organic, about a cycle length. | LOCAL (read) | seat `0.7.0_AE_CloudOps~ZW` | STAGED with bz-10 |
| read | (none) | **The 2026-10-14 07:00Z non-fire of `astn-wsjft-3am-run`** (Lambda `Invocations` for that window, expect none). | LOCAL (read) | `2.0.0_SA_COO~W1` | CARRIED, not an order |

- **Fan-out:** 1 worker, 1 chain of 1, cap 8. bz-10 and bz-11 are seat orders, not spawns.
- **Why the refresh is gated on the class:** a refresh costs a headful sign-in on a shared Dow Jones account that can lock. It is spent only when the response says the session expired; a bot check, an entitlement stop or an unclassified refusal is recorded and left alone.
- **The class table (MECE over the declared domain `STOP_STATUSES`):** `sign_in_refused` -> `expired`; `bot_check` -> `blocked`; `account_or_harvester_unavailable` -> `entitlement`; every other member (`unclassified`, `throttled`, `upstream_unavailable`, `cooldown`, `error`, `upload_timeout`) -> `other`.
- **Why bz-10 is not cut in this issuance:** its pin is bz-9's merge commit, which does not exist yet (the same shape as bz-3 -> bz-4).
- **Not orders:** a re-mint (round 84's finding was that a plain re-mint postpones wsj and leaves barrons untouched); FT; the servable-prefix list work (a standing deliverable).
- **Checks dry-run at the base before the cut:** bz-9 AC1 base FAIL as expected (`no tests ran`: the file does not exist); bz-9 AC2 base PASS as expected (`76 passed`).

## 105. ROUND 85 -- a repair inside bz-9's own scope: the refresh is limited to wsj and barrons (row `AMGT_HARVST-D1-S16`, this seat), 2026-10-13 ~22:5xZ

Found reading `credentials.py` and `auth.py` beside the merged bz-9 (`44aadb7f1d`) before sending the bz-10 pair: `REFUSAL_CLASSES` maps `sign_in_refused` to `expired` for every publisher and `refresh_wanted()` tests only the class and the checkpoint budget, so under `--refresh-once` a `bbg` job refused as expired would spend
its one refresh through the non-Dow-Jones branch of `SessionManager._refresh`, whose credential is `google/andrew-goldengate/credentials`: an automated headful Google sign-in that ruling (A) never named. The flag is OFF and unregistered, so nothing has fired. The issuer rules inside its own decomposition; this narrows bz-9, it adds no capability.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-12` | `bz-12` | **`refresh_wanted()` admits only `wsj` and `barrons`** (one module constant); a refusal of any other publisher is recorded as before and never refreshed; the bz-9 tests that used another publisher for the refresh arms move to `wsj` or `barrons`; a loop over EVERY publisher of `credentials.PUBLISHERS` proves only those two refresh, and a mutant with the constant widened fails it. | LOCAL (direct act, about 40 product lines) | worker `0.9.0_WK_AMGT_HARVST~140` | CUT |
| `HVST-bz-10` | (re-pinned) | **Site Z re-registered with `-Windowless -RefreshOnce`**: its pin is now bz-12's merge, not `44aadb7f1d`. | WORLD | seat `0.7.0_AE_CloudOps~ZW` | STAGED on bz-12's merge pin (its draft is not issued) |
| `HVST-bz-11` | (with bz-10) | **The close read**, unchanged. | LOCAL (read) | seat `0.7.0_AE_CloudOps~ZW` | STAGED with bz-10 |

- **Fan-out:** 1 worker, 1 chain of 1, cap 8 (bz-12 only).
- **Why a new order and not an edit of bz-9:** bz-9 is complete and merged; its record stays as written.
- **Checks dry-run at the base before the cut:** bz-12 AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected.

## 106. ROUND 85, workstream REFRESH-SITEZ -- `HVST-bz-10` and `HVST-bz-11` CUT on the merge pin `3d88eccbc3` (bz-9 `44aadb7f1d` + bz-12), 2026-10-13 ~23:4xZ

bz-12 (`3d88eccbc3`, on `origin/CLOUD` as of the cut) limited the refresh to `wsj` and `barrons`, so the staged site Z cells are cut on that pin. Cut as a second workstream of the project (its own `<workstream>` element), disjoint from the finished build workstreams: it writes only site Z deployment artifacts and reads cycle records.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-bz-10` | `bz-10` | **Site Z re-registered with `-Windowless -RefreshOnce`** from pin `3d88eccbc3` at a cycle boundary by the stop file, `-Plan` read first, one runner, every harvest pin locked, the old pin `995adcaeaa` the signed rollback, the account stop rule, `bz10_t0.txt` written just before the start. | WORLD | seat `0.7.0_AE_CloudOps~ZW` | CUT; needs a signed pair before it is sent |
| `HVST-bz-11` | `bz-11` | **The close, read only** by `bz11_close_read.py` (10 tests): per publisher `ALIVE`, `NON_EXPIRY:<class>`, `REFRESH_FAILED`, `NOT_CURED` or `WAITING`; `CLOSE=MET` when both are ALIVE or NON_EXPIRY. Organic, about a cycle length (the sequence is bbg, then wsj, then barrons). | LOCAL (read) | seat `0.7.0_AE_CloudOps~ZW` | CUT; starts on `bz10_t0.txt` |

- **Fan-out:** 0 workers (two seat orders), 2 chains, cap 8: bz-11 reads what bz-10 starts.
- **Not orders:** a re-mint; a sign-in by any hand; FT; `bbg`, `sa` and `ft` are never refreshed (row D1-S16).
- **Checks dry-run at the base before the cut:** bz-11 AC1 base FAIL as expected (`CLOSE=WAITING reason=no-t0-file`); AC2 base PASS as expected (`10 passed`). bz-10's AC1 and AC2 are site Z reads (base: `WorkingDirectory` is `...pin-995adcaeaa` and the task arguments carry no `--refresh-once`); AC3's file does not exist.
- **After this round the project PARKS** (Andrew-direct ~21:1xZ, CTO msg 5209); collection keeps running at site Z.

## 107. ROUND 86 -- the park lifts; the wsj and barrons refresh becomes the in-profile renew (`1.0.0_SA_CTO~DELL1` msg 6075, `ledger/ROUND_ANALYSIS.round85.ADDENDUM_1_UNPARK.md` and `ADDENDUM_2_R86_CODE_CELL.md`; Andrew-direct 2026-10-15 ~16:0xZ), 2026-10-15 ~16:4xZ

Andrew placed the wsj and barrons ops on dell1 (`org/tier1_exec/2.0.0_SA_COO~W1/ANDREW_DIRECT_20261015_160xZ_WSJ_BARRONS_OPS_RUN_ON_DELL1.md` @94086281f2). The first dell1 read (`ledger/ROUND86_FIRST_DELL1_READ_20261015.md` @06d5850df2) found that `SessionManager.refresh` writes a bundle the tab job never reads, and that `verification.renew` writes the profile it does read (row `AMGT_HARVST-D1-S17` answers Z-S121). The CTO ruled one code cell.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ca-1` | `ca-1` | **`SessionManager.refresh` of a publisher whose contract is `transport: tab` with `seed_from_bundle: false` is the in-profile renew** (keyed on the contract fields, not the names); the worker's `AuthExpired` branch records `profile_renewal` (`renewed`, `stale`, `operator_input_detected`, `post_renewal_status`); bundle-seeded publishers unchanged. | LOCAL (direct act, about 60 product lines) | worker `0.9.0_WK_AMGT_HARVST~141` | CUT, pending |
| `HVST-ca-1` AC3 | (the issuer's run) | **One real job, refused expired, renewed in-profile with no person at the keyboard, ending `complete_candidates` with more than 0 accepted**, `operator_input_detected` recorded: `deliverables/2.0.0_SA_COO_W1/round86/ca1_real_job.py` from a linked worktree of the merged head. | LOCAL (real run) | `2.0.0_SA_COO~W1` at the drain | HELD for `0.0.0_AB_MSTR~DELL1`'s confirmation that site Z stopped wsj and barrons |

- **Fan-out:** 1 worker, 1 chain of 1, cap 8.
- **Why AC3 is not a worker criterion:** the worker runs every invocation under `timeout 120`; a headful sign-in job takes about 2.5 minutes. The CTO's ruling places the real job in the cell; it is graded here, by the issuer, on the merged head (dispatch Step 5, the one real run), and the CTO is told.
- **Not in this round** (addendum 1): anything else from the enrichment list; the first full dell1 cycle (held for the site Z stop); FT, Bloomberg, Seeking Alpha, which stay at site Z.
- **Checks dry-run at the base before the cut:** ca-1 AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`113 passed, 4 subtests passed`). AC3 base: NOT run (a real vendor job; held).

## 108. ROUND 87 -- all harvest publishers move to dell1 (`1.0.0_SA_CTO~DELL1` msg 6094 and 6099, addenda 3 and 4; Andrew-direct 2026-10-15 ~16:3xZ), 2026-10-15 ~19:1xZ

Round 86 is drained (`d0c48b3946`, AC3 PASS at `de87f708fb`). Andrew moved ALL harvest operations to dell1 (Seeking Alpha and Bloomberg now, FT later by his own hand). Site Z's runner is stopped (Ready) at 18:54Z; the formal stop-and-Disabled read-back is site Z's, due about 19:20Z, relayed by `0.0.0_AB_MSTR~DELL1`. The CTO's order: dell1 starts each publisher on its own clock after its local proof; production collection is a SCHEDULED runner on dell1, never a hand-run; the runner goes in at a pin that carries NFRA_OPLGTW E1+E2 (`39ae28559b`, in this branch) and prints E2's S3 GET count and bytes in its cycle record.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-1` | `cb-1` | **The harvest library stops naming site Z as where it runs**: README line 3, `requirements.txt` line 1, the `backfill_driver.py`, `tab_transport.py` and `test_ae4` docstrings, and the unread `contracts.json` `execution` label; a six-file test with a positive control. | LOCAL (direct act, about 15 lines) | worker `0.9.0_WK_AMGT_HARVST~143` | CUT, pending |
| `HVST-cb-2` | (cut after the read-back and the signed pair) | **The dell1 scheduled runner**, registered by `install-cycle-schedule.ps1 -Windowless -RefreshOnce -Publishers wsj,barrons` from a pin that carries `39ae28559b` and the ca-1 merge; `-Plan` read first; one runner; the first productive cycle per publisher reported with the run record, the accepted count and the GET bytes (the E2 proof). Moves served output: a never-widen pair (COO and CTO halves) first. | WORLD | seat `0.7.0_AE_CloudOps~SC1` (idle, live on dell1) | STAGED: waits on site Z's formal read-back and the pair |
| `HVST-cb-3` | (after the issuer's first read) | **Seeking Alpha local proof**: one job `complete_candidates` with more than 0 accepted, no upload. Its profile has no in-profile sign-in (`verification.ACCOUNT_CHECKS` lacks `sa`); the first read decides whether a script gets the session or Andrew signs in once in a Chromium. | LOCAL (a vendor read) | issuer's read, then a cell | STAGED |
| `HVST-cb-4` | (after the issuer's first read) | **Bloomberg local proof** (the bloomberg.com web session, credential `google/andrew-goldengate/credentials`; NOT the Terminal, `integrations/bloomberg/READ_HERE.md` does not apply to it): one job `complete_candidates`, no upload. Round 85's refresh ruling excluded the Google path; addendum 3 names this proof. | LOCAL (a vendor read) | issuer's read, then a cell | STAGED |

- **Fan-out:** 1 worker (cb-1), 1 chain of 1, cap 8; cb-2 is a seat order; cb-3 and cb-4 start as the issuer's own read (the round-86 shape: scripts first, no code change before the read).
- **Order of starting:** wsj and barrons are in the runner from cb-2; sa and bbg join by a re-registration (`-Publishers wsj,barrons,sa,bbg`) once their proofs are in. A preference, not a dependency (addendum 4).
- **Ledger of what is NOT in this round:** FT (Andrew provides the session); the PRD's 16 lines naming site Z (the CTO's edit, the CVO's re-sign); site Z's own runner and records.
- **Checks dry-run at the base before the cut:** cb-1 AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`93 passed`). cb-2 and cb-3/4 are not cut.

## 109. ROUND 87, workstream RUNNER -- the runner's browser window is minimised before the runner is registered (`1.0.0_SA_CTO~DELL1` msg 6165, CTO half `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md`), 2026-10-15 ~19:5xZ

The tab transport opens a visible headful Chrome per job (`tab_transport.py:99`), so a continuous runner would keep a window on the desktop that hosts every agent terminal. The CTO half rules: a minimise cell first, measured on one real job, then register; if that fails, do not register headful. Measured by this seat before the cut: the flag `--start-minimized` leaves a plain Chrome window NOT minimised (`IsIconic` False at 4 s); minimising over the browser's debug protocol (`Browser.setWindowBounds`, `windowState: minimized`) does, the window stays minimised through a navigation, `document.visibilityState` stays `visible`, a screenshot works.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-5` | `cb-5` | **A `TabSession` minimises its own window at start** (`minimize=True`; the three protocol calls inside a swallow-everything `try`, before the origin `goto`); launch arguments, profile and every other method unchanged; a fake-Playwright test with a mutant. | LOCAL (direct act, about 20 lines) | worker `0.9.0_WK_AMGT_HARVST~144` | CUT, pending |
| `HVST-cb-5` AC3 | (the issuer's run) | **One real `wsj` job with every Chrome window sampled for minimisation**: `deliverables/2.0.0_SA_COO_W1/round87/cb5_window_probe.py`; PASS needs `complete_candidates`, accepted > 0, zero samples not minimised after a 3 s launch allowance. | LOCAL (real run) | `2.0.0_SA_COO~W1` at the drain | HELD for the cb-5 merge |
| `HVST-cb-2` | (staged) | **The dell1 runner**, after cb-5's AC3 passes and site Z's formal Disabled read-back (CTO C-g) is on file. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | STAGED |

- **Fan-out:** 1 worker (cb-5), 1 chain of 1, cap 8.
- **Checks dry-run at the base before the cut:** cb-5 AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`47 passed`). The probe's positive control: a plain Chrome window reads not minimised; zero Chrome windows before and after.
- **Deviation from the CTO half (reported to him):** the half names `--start-minimized`; it was measured and does not minimise, so the cell uses the protocol call.

## 110. ROUND 87, workstream RUNNER-REGISTER -- `HVST-cb-5` merged and measured; `HVST-cb-2` CUT, STAGED; `HVST-cb-6` defined, 2026-10-15 ~20:0xZ

`HVST-cb-5` merged `e6649b1250` (AC1 5 passed, AC2 47 passed); its issuer-run AC3 PASSED (`2657939237`): a real `wsj` job ended `complete_candidates` with 5 accepted, 383 of 384 window samples minimised, the 384th inside the 3 s launch allowance, none after it. The CTO half's condition (c) is met for the cell.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-2` | `cb-2` | **The dell1 runner registered for `wsj` and `barrons`** from a locked pin carrying `39ae28559b`, `d0c48b3946`, `08c80a8f75` and `e6649b1250`; `OPAL_HARVEST_PROFILE_ROOT` set so a re-pin keeps the profiles; the stop file's parent created first (row Z-S120); `-Plan` read first; five reads (log fresh, task XML, no console, collector spawn, every runner window minimised) at +3 and +15 minutes; signed rollback; account stop rule. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on site Z's formal Disabled read-back (CTO C-g) filed as `ledger/SITE_Z_RETIRE_READBACK_20261015.md` |
| `HVST-cb-6` | (cut at the registration) | **The close read, read only:** the first productive cycle per publisher: its `.cycle.json`, the accepted count, `s3_get_count` and `s3_get_bytes` (CTO C-h, the E2 proof); reported to the CTO and, through MSTR, to site Z. Organic, about a cycle length. | LOCAL (read) | seat `0.7.0_AE_CloudOps~SC1` | DEFINED |

- **Fan-out:** 0 workers (a seat order), 1 chain.
- **Checks at the cut:** cb-2's criteria are reads of dell1's scheduler and of a file the seat writes; at the base no task exists, so AC1 and AC2 FAIL as expected, and AC3's file does not exist. Not dry-run as commands (they would read a task that does not exist).

## 111. ROUND 87, workstream PROFILE-STORE -- the first dell1 pass found a second defect of the same family; `HVST-cb-8` CUT, `HVST-cb-9` defined, 2026-10-15 ~20:4xZ

`HVST-cb-2` registered the dell1 runner (T0 20:23:04Z, pin `47c623dcf8`) and its first pass failed: `wsj` and `barrons` each REFUSAL expired, REFRESH done (3 s), REFUSAL expired again; the stop rule fired and `0.7.0_AE_CloudOps~SC1` ended the runner by its stop file at 20:27:16Z (SC1 msg 6206; rows `D1-S19`, `D1-S20`). Read from `.runtime/harvest-cycle/state/cycle_runner.log` lines 245-252 and 502-509 and run record `20261015T202310Z-wsj-23b255623f`: `status` sign_in_refused, `detail` "SignInRefused: sign-in refused: --no-sign-in", `token_source` None, `request_attempts` empty. The job never opened its tab: `TokenFirstSessions.get()` demands a stored session, the runner's runtime root has none, and `--no-sign-in` forbids the sign-in that would create one. The refresher's 3 s `done` was the in-profile renew finding the profile already signed in. Not the account.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-2` | `cb-2` (amendment 1) | **Seed the runner's saved-session directory, restart, repeat the reads** (operational unblock; the pair is unchanged). | WORLD | seat `0.7.0_AE_CloudOps~SC1` | pending, amended |
| `HVST-cb-8` | `cb-8` | **`TokenFirstSessions.get()` returns a profile-store envelope, with no refresh, for a publisher whose session lives in its browser profile** (the SAME predicate `SessionManager.refresh` uses, factored into `auth.profile_is_store`); every other publisher unchanged; a loop test with a mutant. | LOCAL (direct act, about 25 lines) | worker `0.9.0_WK_AMGT_HARVST~145` | CUT, pending |
| `HVST-cb-8` AC3 | (the issuer's run) | **One real `wsj` job, `--no-sign-in`, from a worktree with NO saved session and a signed-in profile**: `complete_candidates`, accepted > 0, `token_source` `browser_profile`. | LOCAL (real run) | `2.0.0_SA_COO~W1` at the drain | HELD for the cb-8 merge |
| `HVST-cb-9` | (after cb-8 merges) | **Re-pin the runner** to a head carrying cb-8, by the stop-file boundary, with a pair half (a re-pin is a new act; round 85 signed one per re-pin). | WORLD | seat `0.7.0_AE_CloudOps~SC1` | DEFINED |

- **Fan-out:** 1 worker (cb-8), 1 chain of 1, cap 8.
- **Checks dry-run at the base before the cut:** cb-8 AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`144 passed, 4 subtests passed`).

## 112. ROUND 87, workstream RUNNER-REREGISTER -- `HVST-cb-2` COMPLETE, `HVST-cb-8` merged; `HVST-cb-9` (with `HVST-cb-7`) CUT, STAGED; `HVST-cb-6` still organic, 2026-10-15 ~21:0xZ

`HVST-cb-2` complete (second pass live since 20:32:04Z, R1-R4 TRUE at +15). `HVST-cb-8` merged `a879d12881`; its real-job criterion MOVES: the issuer's separate job (section 111) cannot run, because the production runner holds the publisher browser profiles and a second Chrome on one would collide. The first pass after the cb-9 re-pin, with the seed to be deleted, is its real run (cb-9 step 5, AC2).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-7` + `HVST-cb-9` | `cb-9` | **One re-registration** from a locked pin Q carrying `a879d12881` with `wsj,barrons,sa,bbg`, at a stop-file boundary, the seeded copies deleted only after a job reads `token_source=browser_profile`; reads at +3 and +15 minutes; signed rollback; stop rules incl. CTO C-j. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on the first complete `wsj` and `barrons` cycle records (C-b2) |
| `HVST-cb-6` | (read) | **The first productive cycle per publisher**: `.cycle.json`, accepted count, `s3_get_count`, `s3_get_bytes` (CTO C-h); reported to the CTO and, through MSTR, to site Z (which unlocks its pin worktrees). | LOCAL (read) | `2.0.0_SA_COO~W1` and SC1 | ORGANIC |

- **Fan-out:** 0 workers (a seat order), 1 chain.
- **Pair:** COO addendum 2 `deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB9_REPIN_AND_JOIN.md` (sha256 `3df7917cb98b4bd8872f56b3f0ba2d1f1d66e323da8101d74f2ef3af4c6edfbb`); CTO addendum 2 `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_2_REPIN.md` @21dc90d6b5.
- **Checks at the cut:** cb-9 AC1 base reads `--publishers wsj barrons` (FAIL as expected); AC2 and AC3 files do not exist (FAIL as expected). Reads of dell1's scheduler; not command-dry-runnable beyond that.

## 113. ROUND 87, workstreams EGRESS-COUNT and EGRESS-FIX -- the first complete dell1 cycle exposed that every collector job re-reads the whole silver `article` prefix; the runner is STOPPED; `HVST-cb-10` and `HVST-cb-11` CUT (`1.0.0_SA_CTO~DELL1` msgs 6335, 6339, 6344), 2026-10-16 ~00:1xZ

The first complete dell1 cycle (`wsj`, `20261015T203204Z`: 242 asked, 3 new, 1 failed, completed) carried `s3_get_count` and `s3_get_bytes` of 0 and 0: the runner process's own counters, while every pair runs as a subprocess. Measured by this seat in one process (`deliverables/2.0.0_SA_COO_W1/round87/cb10_job_get_probe.py`): one `no_new_articles` `bbg` job = 747 GETs, 212,043,826 bytes. The source is `harvest_grammar.watermark` -> `store.silver_latest`, uncached in a job (`ledger/ROUND87_EGRESS_FINDING_JOB_FULL_SILVER_READ_20261016.md`). Per watermark call (`cb10_watermark_probe.py`): wsj 125.4 MiB, barrons 9.9, sa 80.4, bbg 202.2; times 242 pairs, wsj is about 29.6 GiB per cycle. The CTO's bar (msg 6339 item 3): above 5 GiB a cycle, stop the runner. The stop file was written 23:59Z; the runner ended 00:01:34Z (barrons cycle `20261015T234451Z` `stopped_by_operator`; task `Ready`, no process). The CTO (msg 6344) allows a `barrons`-only restart (about 2.3 GiB per cycle); `wsj`, `sa`, `bbg` wait for cb-11.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-10` | `cb-10` | **Every `run` and `upload-harvest` process writes its own GET delta** to `<runtime>/s3_get_ledger.jsonl`; a `run` also puts `s3_get_count` and `s3_get_bytes` in its run record; the cycle record sums the ledger over its own window (`s3_jobs_lines`, `s3_get_count_jobs`, `s3_get_bytes_jobs`); no existing key changes. | LOCAL (direct act, about 70 lines) | worker `0.9.0_WK_AMGT_HARVST~146` | CUT, pending |
| `HVST-cb-11` | `cb-11` | **Design B: a backfill job's bound comes from a LOCAL watermark** (`state` table row `wm|<publisher>|<security>`, advanced only by a STORED article, never backward) and reads no silver from S3; `plan --with-watermark` keeps its S3 read. | LOCAL (direct act, about 50 lines) | worker `0.9.0_WK_AMGT_HARVST~147` | CUT, pending |
| `HVST-cb-11` AC3 | (the issuer's run) | **One real job read:** `cb10_job_get_probe.py` for `bbg` on the BA pair after BOTH merges: `get_count` near 0 against 747 / 212,043,826 bytes. | LOCAL (real run) | `2.0.0_SA_COO~W1` at the drain | HELD for the merges |
| `HVST-cb-9` | (staged) | **The re-registration**, now behind cb-10 and cb-11 (CTO order); its pin carries both; `sa` and `bbg` join only after cb-11 landed; the list, the 5 GiB bar and the stop rules re-read before it is sent. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | STAGED |

- **Fan-out:** 2 workers on 2 chains (disjoint write sets: cb-10 `s3_ledger.py`, `__main__.py`, `cycle_runner.py`; cb-11 `worker.py`, `harvest_grammar.py`), cap 8.
- **Not in these cells:** the uploader's `silver_append` reads (the CTO: separate; cb-10 makes them measurable); NFRA_OPLGTW E1 (filed to site Z through MSTR).
- **Checks dry-run at the base before the cut:** cb-10 AC1 and cb-11 AC1 base FAIL as expected (`no tests ran`: the files do not exist); AC2 (both) base PASS as expected (`125 passed, 4 subtests passed`).

## 114. ROUND 87, workstream EGRESS-WRITE -- the uploader is the second copy of the whole-table read; `HVST-cb-12` CUT (`1.0.0_SA_CTO~DELL1` msg 6388), 2026-10-16 ~02:0xZ

The first complete cycle on pin Q (`wsj`, `20261016T003123Z`) cost 5 GETs / 96,855 bytes (old code about 29.6 GiB). `barrons` uploads measured 5 uploads / 922 GETs / 12.9 MiB. The LIST-only sizes (`cb10_silver_sizes_probe.py`): `sa` `listing_hit` 284.2 MiB, `sa` `article` 80.4, `bbg` `article` 202.2, `wsj` `article` 125.4: an upload reads its whole target table, so `sa` and `bbg` would blow the 5 GiB bar. The CTO: cut the uploader on the write side, same design as B; `sa` and `bbg` join only after cb-12 shows their projected per-cycle total under 5 GiB.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-12` | `cb-12` | **`silver_append(..., known=...)`** (opt-in: no table read, de-duplicated against a mapping; default path unchanged; returns `written_hashes`), a local `silver_known` table in the progress database, and `HarvestUploader`'s two call sites passing `known_db`; recorded only AFTER a put succeeds. | LOCAL (direct act, about 90 lines) | worker `0.9.0_WK_AMGT_HARVST~148` | CUT, pending |
| `HVST-cb-12` AC3 | (the issuer's read) | **`upload-harvest` ledger lines near 0 GETs** on the runner after a re-pin; then `sa`/`bbg` projections. | WORLD-adjacent read | `2.0.0_SA_COO~W1` and SC1 | HELD for the merge and a re-pin pair half |

- **Fan-out:** 1 worker, 1 chain, cap 8.
- **Behaviour change named in the order:** rows this runtime never appended are unknown to it, so an identical row already in S3 can be appended again; a duplicate is not a wrong value (consumers read the newest row per key).
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`110 passed`).

## 115. ROUND 87, workstream EGRESS-SEED -- reading the merged cb-12 found a date-key miss and no seed; `HVST-cb-14` CUT (CTO addendum 3 and C-d3, msgs 6395 and 6396), 2026-10-16 ~02:5xZ

The CTO signed the re-pin for cb-12 and added C-d3: before the first upload to a table under the new pin, `silver_known` holds that table's existing keys, seeded once; the first uploads' record states the seed source and 0 duplicate keys written. cb-12 does not seed (it starts empty), and reading its lookup against the real keys found a second defect: the `listing_hit` key holds a `datetime.date` (`silver_from_bronze.py:655`), `encode_key` stores it as a string, and `silver_append` looks up with the `date` object, so a re-uploaded `listing_hit` row is never recognised as unchanged. Both are cb-12's, and mine (the cb-12 order named the datetime limit as acceptable).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-14` | `cb-14` | **`silver_known.load` returns a `KnownMap` whose `get` normalises the key through `encode_key`** (a `date` key now matches); **a one-off command** `seed_silver_known seed` (reads each uploader table once, writes `silver_known` and a snapshot file) and `check --since` (lists new parts, counts rows already in the snapshot as DUPLICATES); the cb-12 test that pinned the old limit is updated. | LOCAL (direct act, about 120 lines) | worker `0.9.0_WK_AMGT_HARVST~149` | CUT, pending |
| `HVST-cb-13` | (staged) | **The re-pin to a head carrying cb-12 and cb-14**, wsj and barrons, with the seed run by the executor while the runner is stopped, and the check after the first uploads (C-d3). Its order text is re-read for the seed and the check before it is sent. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | STAGED behind cb-14 |

- **Fan-out:** 1 worker, 1 chain, cap 8.
- **Checks dry-run at the base before the cut:** cb-14 AC1 base FAIL as expected (the new test file does not exist); AC2 base PASS as expected (`110 passed`); the cb-12 file reads `9 passed` at the base.

## 116. NAMED NEXT INCREMENT (not a round-87 cell) -- the `opal-harvest-security-metrics` read surface (cluster-lead ruling XA-20261016T024917Z-cdcc, CLOUD `08cba0ba64`; CTO msgs 6434 and 6437), recorded 2026-10-16

The cluster lead ruled that the seven `served/*` rows of OG-ap-23 are site Z's to build and the DynamoDB table `opal-harvest-security-metrics` goes to this project "as that producer's own read surface", because dell1 now owns its key shape and cadence. The CTO ruled (A): no build today; the runner egress work (cb-13, then `sa` and `bbg`) keeps priority; this increment is carried to the next round analysis.

| item | state |
|---|---|
| **The surface** | NOT cut. The typed readers already in `lib/research/api/scoped_amgt.py` (`read_generation_pointer`, `read_generation_rows`; the table is a generation-pointer store, pointer row `_CURRENT` per axis and date) come first. |
| **Question 1 (to answer at the next analysis)** | WHO CALLS IT: site Z's gateway cannot call dell1 code, so likely an S3 or Lambda reader. |
| **Question 2** | Does the caller need a never-widen IAM read grant (GetItem and Query on the table) for the gateway role? |
| **Owner / condition** | `2.0.0_SA_COO~W1`; un-parks at the CTO's next round analysis that names the caller. |

- **Update to section 116 (03:02Z, CTO msg 6442, from site Z's CTO msg 34683):** the read surface is an AGENT read surface built on dell1 as this project's own, so Question 1 is ANSWERED (the callers are agents on dell1, not the site Z gateway) and Question 2 is MOOT (no gateway IAM grant is in scope). Its shape: a typed reader module beside `scoped_amgt.py`'s readers, invokable from a dell1 seat shell. Still a named increment after the runner cells (CTO option A stands); still NOT a round-87 cell.

## 117. ROUND 87, workstream RUNNER-JOIN -- `HVST-cb-15` (`sa` and `bbg` join the dell1 runner, seeded once) CUT, STAGED behind cb-13's evidence (03:59Z)

The CTO signed addendum 4 (msg 6460), effective on C-a4 (cb-13's evidence: the first uploads read about 0 GETs, `check` ends `DUPLICATES=0`, the 5 GiB bar holds). At the cut: the cb-13 pass (T0 2026-10-16T03:27:57Z) has made 116 `run` lines at 0 GETs and 0 bytes, no upload yet. The old pin's last barrons cycle record (`20261016T013317Z`, 27 pairs, stopped by operator) read `s3_get_count_jobs` 6,636 / `s3_get_bytes_jobs` 126,566,449 (about 4.7 MiB per pair, uploads included): the measured before-figure for the uploader.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cb-15` | `cb-15` | **Stop at a stop-file boundary, seed `sa` and `bbg` once (about 567 MiB), re-register `wsj,barrons,sa,bbg` from the same pin, read, check duplicates**; `sa` leaves the list if its session reads logged out; branches F, G, E. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on C-a4 |

- **Fan-out:** 0 workers (a seat order), 1 chain.
- **Checks at the cut:** AC1 base reads `--publishers wsj barrons` (FAIL as expected); AC2 and AC3 files do not exist (FAIL as expected); reads of dell1's scheduler and of files the seat writes.

## 118. ROUND 88 -- the CTO's round-87 analysis (`ledger/ROUND_ANALYSIS.round87.md` @4a08fffabe, ERRATUM 1 @74515c1f4a; msgs 6766, 6776, 6780): seven cells cut in ONE issuance, 2026-10-16 ~15:5xZ

The CTO's enrichment list (six items) as corrected: item 3 (W132-S4) is STRUCK (it measured R31, retired by his ADDENDUM 7, msg 2438; closed as moot); item 2 (resolve) is re-cut as "a ticker-shaped query that matches no ticker slot never returns `exact` on a name" because Procter & Gamble is not in the 243-security universe (live reads); item 2 (attribution) cannot test "KIMBERA MM's list holds it" because `KIMBERA MM` is not held either, so the report is recorded MISFILED and excluded from KMB's list. Item 5 is ruled YES by the CTO (msg 6776): re-register `wsj,barrons,sa`. The live state at the cut: the runner is Running on `sa` (22 of 242 jobs in 6 hours), `bbg` is off the list by Branch G, 21 `sa` upload lines at 0 GETs.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cc-1` | `cc-1` | **A served model figure carries its claim**: `basis` and `figure_claim` in the gateway's `FIG_FIELDS`; `IS_DIL_EPS_CONT_OPS` is claimed as NOT the reported diluted EPS (UNH, BA named). | WORLD (infra path floor) | worker-light `~150` | CUT |
| `HVST-cc-2` | `cc-2` | **A research report attaches to the security it is about**: measure the misfile census first (read-only), then a pure identity check in `typed.py` and the gateway filter; KMB's list excludes the Kimberly-Clark de Mexico report and names the exclusion. | WORLD (infra path floor) | worker `~151` | CUT |
| `HVST-cc-3` | `cc-3` | **A ticker-shaped query that matches no ticker slot never returns `exact` on a name** (PG gives `candidates`, PCG resolves by its ticker). | WORLD (infra path floor) | worker-light `~152` | CUT |
| `HVST-cc-4` | `cc-4` | **The `bbg` page closure is traced on one local leg** (three arms: as the runner, minimise disabled, a control job) and the closer is named. | WORLD | seat `0.7.0_AE_CloudOps~SC1` (the AMGT CloudOps lane, rule 34) | CUT |
| `HVST-cc-5` | `cc-5` | **`wsj` and `barrons` run their first dell1 cycles**: stop at a job boundary, re-register `wsj,barrons,sa`, report each publisher's first cycle (run record, accepted, GET bytes) and the `sa` restart check (CTO condition). | WORLD | seat `0.7.0_AE_CloudOps~HV1` (spawned before rule 34 landed; it stopped the runner mid-act, so the hold stays with it and it closes idle after) | CUT |
| `HVST-cc-6` | `cc-6` | **The 32 stale OPEN remediation rows are each moved** (met / re-owned / dismissed): 34 OPEN minus the two round-87 items, read from `comp-surprise --json`. | LOCAL | worker `~153` | CUT |
| `HVST-cc-7` | `cc-7` | **The gateway serves the three S29 fixes and each is read on the served tool** (resolve PG, the UNH EPS claim, KMB research). | WORLD | `0.7.0_AE_CloudOps~SC1` (the AMGT lane, rule 34) | CUT, STAGED: waits on cc-1, cc-2, cc-3 merged and a signed never-widen pair |

- **Fan-out:** `N of M chains, N=4 workers (cc-1, cc-2, cc-3, cc-6) of M=7 chains, cap 8`; cc-4 and cc-5 are cc-5 at HV1 (the runner hold) and cc-4 and cc-7 at SC1 (the AMGT lane) in parallel; cc-7 is staged. The three code cells have disjoint write sets (`harvest_figures.py` / `typed.py` + `harvest_research.py` / `harvest_identity.py`); cc-2 and cc-3 touch different files in `opal-gateway/app/`.
- **Checks at the cut (dry-run at the base):** cc-1 AC1 FAIL as expected (no test file), AC2 PASS (`16 passed` on `test_og_gt1/gt3/gt4`); cc-2 AC1/AC2 FAIL as expected, AC3 regression recorded by the worker before and after; cc-3 as cc-1; cc-6 AC1 FAIL as expected (`TRIAGE FAIL no triage file`), AC2 FAIL; cc-4 and cc-5 files do not exist (FAIL); cc-5 AC1 reads `--publishers sa wsj barrons --refresh-once` (FAIL as expected against `wsj barrons sa`); cc-7's file does not exist.
- **Not cut (named):** a silver REBUILD for KMB's misfiled report; adding Procter & Gamble or `KIMBERA MM` to the universe; a per-leg budget with rotation (the pass stays serial; the CTO's analysis did not list it); a fix for the `bbg` closure; `ft`; the named `opal-harvest-security-metrics` increment (section 116).

## 119. ROUND 89 -- the CTO's round-88 analysis (`ledger/ROUND_ANALYSIS.round88.md` @07264722d8; msg 7491): two cells cut in ONE issuance, one item named blocked, 2026-10-17 ~12:2xZ

The CTO's enrichment list (three items). Round 88 closed MAY-CLOSE (CVO `ADJUDICATION_v82.md`; 20 rows dismissed, `comp-surprise` ARMED 0). `D1-S29` (a) and (c) are FIXED and served; **(b) is NOT fixed**: KMB's `fund_of_record` and `last_stated_position` (dossier and continuation) still cite the excluded Mexico report `fbd50086c4065785`, so `D1-S29` stays OPEN.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cd-1` | `cd-1` | **A dossier or continuation field that cites a misfiled report is not served, and is named** (`misfiled_fields_excluded`): `_research` in `harvest_research.py` drops a field whose entry names a listed report of the same security, for both parts; a control security keeps every field. | WORLD (infra path floor) | worker `~154` | CUT |
| `HVST-cd-2` | `cd-2` | **The gateway serves it and KMB is read on the served tool with a control name**: release cut on the live base carrying the two `HVST-cd-1` files, deployed under its own never-widen pair, KMB and a control read before and after. | WORLD | `0.7.0_AE_CloudOps~SC1` (the AMGT lane, rule 34) | CUT, STAGED: waits on `cd-1` merged and the CTO half of the pair (COO half signed, sha256 `8b5102de...a9d8`) |
| item 2 (the cc-6 dispositions as appended lines on 31 rows) | none | **NOT CUT, blocked on a ruling.** The 28 owner moves and 3 dismissals are on REMEDIATION rows (10 files under `surprise-channel/remediations/`, lane `TREE_CVO`: neither this seat nor a worker is admitted); the owner-move limb of `.tools/surprise-row-gate.py` admits one appended evidence entry that cites a ruling as `R-<n>` with `@<hash>` (`RULING_CITATION_RE`), and the CTO's ruling is a section of an analysis, not an `R-` id; a dismissal is a clock move (`CLOSED_UNREMEDIATED`) the analysis says is not one. The issuer asked the CTO to name the writer and the citation form. | LOCAL | none | BLOCKED, asked |
| item 3 (the dell1 harvest cycles keep running) | none | No cell: `HVST-cc-5`'s hourly `sa` reads continue at SC1; a cell is cut only if a cycle fails. | -- | SC1 | CARRIED |

- **Fan-out:** `N of M chains, N=1 worker (cd-1) of M=1 chain, cap 8`; `cd-2` consumes `cd-1`'s merge, so the two orders are ONE chain (worker `~154`, then seat SC1); nothing runs in parallel on it.
- **Checks at the cut (dry-run at the base):** `cd-1` AC1 FAIL as expected (`ERROR: file or directory not found: tests/test_cd1_dossier_misfiled.py`, no tests ran); AC2 PASS as expected (`33 passed in 2.41s` over `test_cc1/cc2/cc3` and `test_og_gt1/gt3/gt4`). `cd-2`'s output file does not exist (all three FAIL).
- **Not cut (named):** the silver or gold REBUILD that re-derives the KMB dossier without the misfiled reports (the true remedy; `cd-1` hides the served field); a `not_held` sign on `harvest_resolve_security("PG")` (`D1-S39`, beyond the CTO's three items); the tolerant hold loop for `bbg`, the per-leg budget, the installer STOP parent, the `request_kind` label and the other candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md` (the CTO listed none of them); `ft`.

### 119a. ROUND 89 AMENDMENT 1 (issuer, 2026-10-17 ~12:1xZ; CTO msg 7494, `ledger/NEVER_WIDEN_CD2_GATEWAY_DOSSIER_CTO_HALF.md` @cfe7f25c42)

- **Item 2 is HANDED to `3.0.0_SA_CVO`, not blocked** (supersedes the BLOCKED row above): the writer is the CVO in its next sweep from `deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json`; the rows are REMEDIATION rows in its own lane, so they are its own entries, citing `ledger/ROUND_ANALYSIS.round88.md` section 2 @07264722d8, with no `R-` id. No cell, no order.
- **`HVST-cd-2` gains the CTO half's C-8 and C-9** as steps 1b (the host owner is told first, through `0.0.0_AB_MSTR~DELL1`, and the issuer sends GO) and 5 (the release ref is pushed by the integrator on the issuer's ask and site Z lands it). The CTO half is SIGNED and binds the COO half unchanged (sha256 `8b5102de...a9d8`). `cd-2` stays STAGED until `cd-1` is merged.

## 120. ROUND 90 -- the CTO's round-89 analysis (`ledger/ROUND_ANALYSIS.round89.md` @fa28a5790e; msg 7642): one cell cut, four cells defined and NOT cut, 2026-10-17 ~15:4xZ

The CTO's enrichment list (four items). Round 89 closed MAY-CLOSE (CVO `ADJUDICATION_v83.md`, `REMEDIATION_v20.md`); `D1-S29` is REMEDIATED on the CVO's served read, all three limbs. Live state at the cut: gateway `1753c741d9` serves; the dell1 runner runs `wsj,barrons,sa` (interim 22: `DUPLICATES=0`, 0 GETs); site Z lands `rel-amgt-harvst-cd2` on its lineage and re-cuts ap-36 on it.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ce-1` | `ce-1` | **Why UNH's `fund_of_record` and `last_stated_position` read absent beside a report that states PFOE, and how ONE security's dossier is rebuilt**: a read-only measurement (bounded S3 reads, a pure function run on fetched documents) that names the cause (`rule_miss`, `stale_object`, `report_not_in_items`, `no_stated_position` or `other`) and the rebuild entry point, its inputs, whether it runs for one security and whether it needs the misfiled-reports list. Changes no product file. | LOCAL (direct act) | worker `~155` | CUT |
| `HVST-ce-2` | -- | **The UNH derivation is fixed (or the one-line rule is written), and the `parts_absent.dossier` wording names only the requested fields it excluded** (the CTO's nit). Defined by `ce-1`'s `CAUSE`: `rule_miss` -> a code fix in `lib/research/corpus/continuation.py` with an offline test and a mutant arm, plus the wording change in `harvest_research.py`; `stale_object` -> no code cell, the object is rebuilt by `ce-3`'s method and the wording change ships alone; `report_not_in_items` -> the input filter is the fix; `no_stated_position` -> the one-line rule is written into the decomposition and the wording change ships alone. | WORLD (infra path floor when it touches the gateway) | worker | DEFINED, NOT CUT: waits on `ce-1` |
| `HVST-ce-3` | -- | **The KMB dossier is rebuilt from the reports that remain after the exclusions and graded on the live read** (the CVO's enrichment). Defined by `ce-1`'s `REBUILD_ENTRY`, `REBUILD_ONE_SECURITY` and `REBUILD_NEEDS_EXCLUSION_INPUT`: a data-writing run on the harvest bucket (gold objects for KMB), so a seat order with a ledger, never a worker. | WORLD | seat `0.7.0_AE_CloudOps~SC1` (rule 34) | DEFINED, NOT CUT: waits on `ce-1` |
| `HVST-ce-4` | -- | **The gateway serves the `ce-2` code under its own never-widen pair** (COO half, CTO half; the host owner told first, the release ref pushed after), with a live read of UNH showing PFOE and a control name unchanged. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | DEFINED, NOT CUT: waits on `ce-2` (only when `ce-2` changes a gateway file) |
| item 4 (the dell1 harvest cycles keep running) | none | No cell: SC1's hourly `sa` reads stand (CTO round-88 item 3, round-89 item 4); a cell is cut only if a cycle fails. | -- | SC1 | CARRIED |

- **Why four cells are defined and not cut:** their text depends on a fact that does not exist yet (the cause; the rebuild entry point and whether it takes the exclusion list). A cell the issuer cannot inline is a cell it cannot issue (`/dispatch` Step 0, item 3); a cut on a guess would send a worker or a seat a defective face. The seat cuts each the tick `ce-1` closes; this is a recut inside the round, which the gate notes and does not grade at `EXECUTING`.
- **Fan-out:** `N of M chains, N=1 worker (ce-1) of M=1 chain, cap 8`; `ce-2`, `ce-3` and `ce-4` consume `ce-1`'s answer, so they are one chain behind it (`ce-2` and `ce-3` can then run in parallel).
- **Checks at the cut (dry-run at the base):** `ce-1` AC1, AC2 and AC3 FAIL as expected (`cat` of a file that does not exist).
- **Not cut (named):** `harvest_resolve_security("PG")` still has no `not_held` sign (`D1-S39`); the standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md` (the tolerant hold loop for `bbg`, the per-leg budget, the installer STOP parent, the `request_kind` label, the barrons reject class, the prebuilt-dist switch, the `opal-harvest-security-metrics` read surface); `ft`.

### 120a. ROUND 90 RECUT -- `HVST-ce-1` merged (`0dfc96bdd1`); the measured answer cuts three cells and stages two, 2026-10-17 ~16:0xZ

`HVST-ce-1` closed. `CAUSE=rule_miss` (layout level): `UNH_US_Equity`'s one report `48d81f053e5076e8` is in the derivation's inputs, the stored continuation equals what today's code yields (5 of 5 fields), and `_recommendation_candidates` tests an anchored label regex against a whole pdf PAGE whose text starts `1 \n \nUnitedHealth Group Incorporated ...` with `Recommendation: Maintain positions in PFOE and DIVZ` at offset 75, so it never reads it. The rebuild entries are `lib/research/corpus/continuation.py::write_one(security_key)` then `lib/research/corpus/dossier.py::write_one(security_key)` (the dossier CLI takes `--security-key`; the continuation CLI does not); gold writes NEVER overwrite (a changed input set or method version writes a NEW name beside the old; the gateway serves the newest); neither writer takes an exclusion input. Measured: 47 GET/HEAD requests, 1,626,460 bytes, 24 objects. Worker rows `D1-W155-S1` (ARMED, disarm owner `1.0.0_SA_CTO`: the pdf rule's premise), `-S2` (ARMED, disarm owner this seat: the rebuild writers have no exclusion input), `-S3` (INERT).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ce-2` | `ce-2` | **A pdf page that carries a `Recommendation: <content>` LINE is read for `fund_of_record` and `last_stated_position`** (colon required, same line; docx unchanged), `METHOD_VERSION` continuation `/3` to `/4`, a read-only census of the rule's effect on every security (old rule against new on the same fetched inputs). | LOCAL | worker `~156` | CUT |
| `HVST-ce-3` | `ce-3` | **Under a field filter `parts_absent.dossier` names only the requested fields it excluded** (the CTO's nit). | WORLD (infra path floor) | worker-light `~157` | CUT |
| `HVST-ce-6` | `ce-6` | **The corpus library reads no report on the misfiled list**: `typed.MISFILED_REPORTS` (the gateway's two entries) and `reports_for` drops them, a drift test against the gateway's list. | LOCAL | worker `~158` | CUT |
| `HVST-ce-4` | -- | **The gold objects are rebuilt for the securities the `ce-2` census lists and for KMB, and graded on the live gateway read** (UNH showing fund PFOE, KMB citing neither Mexico report, a control name unchanged): `continuation.write_one` then `dossier.write_one` per security, a data write on the harvest bucket. A seat order under its own never-widen pair (COO and CTO halves; the blast radius is every served dossier the census lists, rollback per key: the old objects stay, the newest wins, so a rollback is a write that outranks the new, named in the halves). | WORLD | seat `0.7.0_AE_CloudOps~SC1` (rule 34) | DEFINED, NOT CUT: waits on `ce-2` and `ce-6` merged, the census read, and the pair |
| `HVST-ce-5` | -- | **The gateway serves the `ce-3` wording** under its own never-widen pair (host owner told first, release ref pushed after); batched with any other gateway change that is due rather than restarting the host for a wording alone. | WORLD | seat `0.7.0_AE_CloudOps~SC1` | DEFINED, NOT CUT: waits on `ce-3` merged |
| item 4 (the dell1 harvest cycles keep running) | none | No cell: SC1's hourly `sa` reads stand. | -- | SC1 | CARRIED |

- **Fan-out:** `N of M chains, N=3 workers (ce-2, ce-3, ce-6) of M=3 chains, cap 8`: disjoint write sets (`continuation.py` and its tests; `harvest_research.py` and its test; `typed.py` and its test). `ce-4` consumes `ce-2` and `ce-6`; `ce-5` consumes `ce-3`.
- **Checks at the cut (dry-run at the base):** `ce-2` AC1 FAIL as expected (no test file), AC2 PASS (`53 passed in 1.07s`), AC3 FAIL as expected (no census file); `ce-3` AC1 FAIL as expected, AC2 PASS (`38 passed in 2.27s`); `ce-6` AC1 FAIL as expected, AC2 PASS (`35 passed in 0.94s`).
- **Not cut (named):** a rebuild of every securities' gold objects beyond the census's CHANGED list; `harvest_resolve_security("PG")` `not_held` (`D1-S39`); the standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`; `ft`.

### 120b. ROUND 90 -- `HVST-ce-2`, `-3`, `-6` merged; `HVST-ce-4` CUT, STAGED behind the CTO half (2026-10-17 ~17:1xZ)

`HVST-ce-6` merged `87b542aed4`, `HVST-ce-3` merged `b77e08e198`, `HVST-ce-2` merged `344ea6a5fc` (after AMENDMENT 1: the pdf line rule is a fallback and its value carries `line_only`; the census reads 30 securities absent-to-value and 0 value-to-value, 94 of 94). The measured answer cuts `ce-4`.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ce-4` | `ce-4` | **The gold continuation and dossier objects of 31 securities (the census's 30 plus `KMB_US_Equity`) are rebuilt and read on the served tool**: `continuation.build` then `write_one`, then `dossier.build` then `write_one`, serially, canary UNH and KMB first; UNH shows fund PFOE, KMB cites neither Mexico report, the control `CPA_US_Equity` is unchanged. Add-only (gold never overwrites). | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on the CTO half (COO half signed, sha256 `5b486cda...6149`; list `ce4_securities.txt` sha256 `7881772d...c67b`) |
| `HVST-ce-5` | -- | The gateway serves the `ce-3` wording under its own pair, batched with any other gateway change. | WORLD | seat SC1 | DEFINED, NOT CUT: unchanged |

- **Fan-out:** `N of M chains, N=0 workers (ce-4 is a seat order) of M=1 chain, cap 8`; `ce-4` is one chain behind the merged `ce-2` and `ce-6`.
- **Check at the cut (dry-run at the base):** `ce-4` AC1 to AC3 FAIL as expected (`cat` of a file that does not exist).
- **Armed rows still open:** `D1-W155-S1`, `D1-W155-S2`, `D1-W158-S2`; the issuer dispositions them when the served reads of `ce-4` are clean.

### 120c. ROUND 90 -- the gateway base moved again; `HVST-ce-4` is running (2026-10-17 ~18:3xZ)

- **Gateway base:** site Z reports (CTO msg 35550, relayed by `0.0.0_AB_MSTR~DELL1` msg 7704) ledger `nfra-oplgtw-gateway-release-batch6` CLOSED 2026-10-17T18:11:52Z; the live gateway is `efcc8ae19f7eebb04e2f45f45c0def28af037c24` on base `1753c741d9` (`TO-OG-ap-36`, re-cut on our commit). Our `app/harvest_research.py` is KEPT (the host's md5 equals its blob). A scratch ref `origin/rel-nfra-og-live-efcc8ae19f` holds it. **Consequence for `HVST-ce-5`** (the `ce-3` wording): its release is cut on `efcc8ae19f` (or the live commit read from the manifest and the instance at the cut), with `DEPLOY_BASE_REF` set, after a host-owner notice through MSTR; the signed-pair rule of `cd-2` (the pair binds the live deployed commit, no hash) carries over, and the `<merge>^1` equality is re-printed against the new live file.
- **Live hazard named by site Z (row `Z-S375`, fix pending):** the gateway tool `etfs_compare_peers` can OOM the 1.8 GB host. No AMGT order calls it, and no served read of `HVST-ce-4` may call it.
- **`HVST-ce-4`:** 39 manifest entries of 62 written by 18:33Z (UNH and KMB canary read served 17:30Z, branch X for KMB, no stop or branch-B line); the run ends about 19:20Z inside the 19:30Z window.
- **Armed rows:** `D1-W155-S1`, `D1-W155-S2`, `D1-W158-S2` remain open until the served reads of `ce-4` close; the issuer dispositions them then.

## 121. ROUND 91 -- the CTO's round-90 analysis (`ledger/ROUND_ANALYSIS.round90.md` @307764abfe; msg 7721): two cells cut in ONE issuance, four defined and NOT cut, 2026-10-17 ~20:2xZ

Round 90 closed MAY-CLOSE (CVO `ADJUDICATION_v84.md`, `REMEDIATION_v21.md`; 11 rows dismissed including the ARMED `D1-W155-S1`, `-S2`, `D1-W158-S2`); `D1-S43` REMEDIATED on the CVO's own served read. **A served correctness defect introduced by the round's own rule graduated, row `C-S61`:** `MNST_US_Equity`'s line `RECOMMENDATION: CANDIDATE FOR PFOE` is served as `fund_of_record` `PFOE`, so a candidate reads as a holding; the derivation takes the first fund token whatever the verb. **The issuer's error:** reading the round-90 census (`ce2_census.out`) the issuer took `CANDIDATE FOR <fund>` lines for stated positions and did not separate a candidate from a holding; at least `8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `HEI`, `MNST`, `MSCI`, `SNPS` carry that shape. The wrong claim has been served since 17:30Z; the fix adds NEWER objects (gold never overwrites, nothing is deleted).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cf-1` | `cf-1` | **A no-write census over all 94 names of the verb phrase before the fund token**, each distinct phrase with its count and which rule path supplied it, and the list of every name whose SERVED `fund_of_record` came from a line that is not a holding (for the 31 rebuilt names read from the stored gold objects). It classifies nothing. | LOCAL (direct act) | worker `~159` | CUT |
| `HVST-ce-5` | `ce-5` | **The gateway serves the `ce-3` wording** under its own never-widen pair, host owner told first, the ref pushed after; the issuer's reservation is in the pair (the live trigger is gone after `ce-4`). | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on the CTO half (COO half signed, sha256 `be0a5ad6...c59f`) |
| `HVST-cf-2` | -- | **`fund_of_record` and `last_stated_position` take a fund only from a holding verb** (maintain, hold, add and so on, as the census names them and the CTO and the issuer classify); a candidate or watch line is served as such, in its own field or with an absent reason, never as the fund of record; continuation method `/5`; offline tests with a mutant; a fixture for each class the census finds. | LOCAL | worker | DEFINED, NOT CUT: waits on `cf-1` and the classification |
| `HVST-cf-4` | -- | **The forward rebuild of the affected names** (the census's list) writes NEWER gold objects under its own never-widen pair; proof: `MNST_US_Equity` served with no `PFOE` `fund_of_record`, `UNH_US_Equity` unchanged, and a control. A seat order, canary first, a manifest line per write, run FOREGROUND or under a supervisor that checks the manifest after each write and stops on a gap (item 3 below). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cf-2` merged and the pair |
| `HVST-cf-3`, `HVST-cf-5` | -- | **The corpus-wide `fund_form` object without the two Mexico reports** (`fund_form.gather_items` drops `typed.MISFILED_REPORTS`; then a rebuild of the per-fund objects under its own pair). **SEQUENCING HAZARD, named:** `substrate._fund_form_member` picks the stored fund form whose `inputs` equal `fund_form.current_inputs(fund)` NOW; the moment `gather_items` changes, every dossier build finds no stored fund form until the new objects are written. So `cf-3` is NOT merged into the tree any dossier rebuild runs from until `cf-5` has written the new fund forms, and `cf-4` runs from a worktree pinned BEFORE `cf-3`. | LOCAL / WORLD | worker, then SC1 | DEFINED, NOT CUT: after `cf-4` |
| item 3 (`D1-S44`) | none | **The driver's silent death:** SC1 read dell1 for an event, a memory limit or a reaper and found none (`ce4_before.out`); the cause is not readable. The CTO's rule goes into the faces of `cf-4` and `cf-5`: a long write run goes foreground, or under a supervisor that checks the manifest after each write and stops on a gap; a detached process is unbuffered with its stdout and exit status logged to a file. No new tool. | -- | -- | RULE (in the orders) |
| item 6 (the dell1 harvest cycles keep running) | none | SC1's hourly `sa` reads stand. | -- | SC1 | CARRIED |

- **Fan-out:** `N of M chains, N=1 worker (cf-1) of M=3 chains, cap 8`: the C-S61 chain (`cf-1` then `cf-2` then `cf-4`), the gateway chain (`ce-5`, a seat order), and the fund-form chain (`cf-3` then `cf-5`, held behind `cf-4`).
- **Checks at the cut (dry-run at the base):** `cf-1` AC1 and AC2 FAIL as expected (`cat` of a file that does not exist); `ce-5` AC1 to AC3 FAIL as expected (no `ce5_served.out`).
- **Not cut (named):** `D1-S39` (`not_held`); the `line_only` text recovered from the extraction's `section_leads`; the standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`; `ft`.

### 121a. ROUND 91 -- `HVST-ce-5` DEFERRED by the CTO (msg 7727); the hold on the fund_form code is accepted (2026-10-17 ~20:1xZ)

- **`HVST-ce-5` is SUPERSEDED** (status `superseded`): the CTO did not sign the half and amended his round-90 item 5. After `HVST-ce-4` no live read triggers the new sentence, so a gateway restart for it alone "is not worth the window"; the two files of `HVST-ce-3` ride the next gateway release due for a live reason, under that release's own order and pair with the same controls. The carrier is `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md`. No GO was sent; SC1 started nothing.
- **Accepted by the CTO:** the hold on the `fund_form` code behind `cf-4` ("right") and the naming of the C-S61 misread ("the cf-1 census is the remedy").
- **Fan-out line of section 121 stands** (`N of M chains, N=1 worker (cf-1)`); `ce-5` leaves the round's cell set.

### 121b. ROUND 91 -- `HVST-cf-1` merged (`934ecb88c5`); the census cuts `HVST-cf-2` (2026-10-17 ~20:4xZ)

`HVST-cf-1` read all 94 names: 22 distinct verb phrases; 69 names have a fund token. The non-holding phrases are `candidate for` (10 names: the 9 round-90 rebuilds `8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `HEI`, `MNST`, `MSCI`, `SNPS` and `CLX_US_Equity`, served that way before round 90), `initiate ~<N>% position in` (`CNR`), `interesting exposure for` (`ST_SP`) and the bracketed template `[BUY IN IDVZ TO X%]` (`ML_FP`). A second served defect predates round 90: four names serve a `COMPANY DESCRIPTION:` paragraph as `last_stated_position`.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cf-2` | `cf-2` | **`fund_of_record` only from a line that states a holding**; a candidate, initiation, interest or template line is served in `last_stated_position` with a `stance` and never as the fund of record; continuation method `/5`; a table test over the 22 census phrases; a read-only census of the effect (expected 13 names change). The issuer's classification of the phrases is in the order; the CTO ratifies it in the rebuild's pair. | LOCAL | worker `~160` | CUT |
| `HVST-cf-4` | -- | The forward rebuild of the names `cf-2`'s census lists, newer objects only, canary `MNST_US_Equity` first, `UNH_US_Equity` unchanged and a control; a seat order under its own never-widen pair; foreground or manifest-checking supervisor (item 3). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cf-2` merged and the pair |
| `HVST-cf-3`, `-5` | -- | The `fund_form` chain: unchanged (held behind `cf-4`; section 121). | -- | -- | DEFINED, NOT CUT |

- **Fan-out:** `N of M chains, N=1 worker (cf-2) of M=1 chain, cap 8` (the C-S61 chain; `cf-4` consumes `cf-2`).
- **Check at the cut (dry-run at the base):** `cf-2` AC1 FAIL as expected (no test file), AC2 PASS (`66 passed` over seven files), AC3 FAIL as expected (no census file).
- **Armed row:** `D1-W159-S1` (the `ML_FP` template) stays open until `cf-2` and the rebuild.
- **Asked of the CTO (not blocking the code cell):** ratify the classification; say whether the `COMPANY DESCRIPTION` defect (4 names) joins this fix.

### 121c. ROUND 91 -- the CTO ratified the classification and the four JP names join `cf-2` and `cf-4` (msg 7735, 2026-10-17 ~20:4xZ)

- **Ratified as set:** `potential add in` ("currently ~2.5%"), `increase position in` and `maintain or consider increasing` are holdings; `initiate ~2% position in`, `candidate for`, `interesting exposure for` and the `[BUY IN ... TO X%]` template are not; the default for an unknown phrase stays NOT a holding.
- **`8306_JP_Equity`, `8316_JP_Equity`, `8766_JP_Equity`, `9433_JP_Equity` JOIN `cf-2`** (AMENDMENT 1 of the order: a closed list of section headings; a description paragraph is never `last_stated_position`) **and `cf-4`'s rebuild list and its served proof.**

### 121d. ROUND 91 -- `HVST-cf-2` merged (`80d0701876`); `HVST-cf-4` CUT, STAGED behind the CTO half (2026-10-17 ~21:5xZ)

`HVST-cf-2` (after AMENDMENT 1 for the four JP names and AMENDMENT 2: a stance is claimed only where a fund token is) merged; its census (94 of 94, baseline pinned at the round-90 commit) lists exactly 17 changed names and `HOLDING_CHANGED=0`.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cf-4` | `cf-4` | **The gold continuation and dossier of 17 securities are rebuilt** (the 13 non-holding names `8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `CLX`, `CNR`, `HEI`, `ML_FP`, `MNST`, `MSCI`, `SNPS`, `ST_SP`, and the four JP names `8306_JP`, `8316_JP`, `8766_JP`, `9433_JP`), add-only, from a worktree pinned at `80d0701876` (no `fund_form` change), canary `MNST` then `8306_JP`, `UNH` and `CPA` read before and after, each name a foreground command with the manifest checked (CTO item 3). | WORLD | seat `0.7.0_AE_CloudOps~SC1` | CUT, STAGED: waits on the CTO half (COO half signed, sha256 `275d5739...95b0`; list `cf4_securities.txt` sha256 `221a63c3...ee48`) |
| `HVST-cf-3`, `-5` | -- | The `fund_form` chain, held behind `cf-4`. | -- | -- | DEFINED, NOT CUT |

- **Fan-out:** `N of M chains, N=0 workers (cf-4 is a seat order) of M=1 chain, cap 8`.
- **Check at the cut (dry-run at the base):** `cf-4` AC1 to AC3 FAIL as expected (no `cf4_served.out`).
- **Armed row:** `D1-W159-S1` (the `ML_FP` template) stays open until the rebuild is read served.

## 122. ROUND 92 -- the CTO's round-91 analysis (`ledger/ROUND_ANALYSIS.round91.md` @9bdb466396; msg 7773): one cell cut in ONE issuance, four defined and NOT cut, 2026-10-17 ~23:3xZ

Round 91 closed MAY-CLOSE (CVO `ADJUDICATION_v85.md`, `REMEDIATION_v22.md`; 6 rows dismissed including the ARMED `D1-W159-S1`). **C-S61 is REMEDIATED at gold** (12 of 17 rebuilt names read served: mine MNST, ML_FP, CLX, UNH; the CVO's ADBE and SNPS; SC1's eight). **`D1-S46` graduated:** the silver `research_reports[].fund` still reads the named token for a candidate or template line. The CTO's ruling (msgs 7771, 7773): silver KEEPS `fund` and GAINS `fund_relation`; every consumer that means "held" reads `fund_relation = holding` only; a no-write census over the 94 names first, then the silver rebuild under its own never-widen pair; the `fund_form` chain (`cf-3`, `cf-5`) after it, holding reports only, no Mexico reports; `ce-5` stays deferred; the dell1 cycles continue under the S44 rule.

**Read by the issuer for this cut (code at the working tree, `4b44abc97c` for `continuation.py`):**
- **Writer:** `typed.py::record()` builds the silver row from `_find_fund(text)`: the first fund token within 250 characters of the first `REC*MENDATION` header, else the first bare fund token anywhere (`fund_evidence` is the text up to that token). It is written by `store.silver_append`, which appends ONE NEW PART per `fetched_at` date partition and never overwrites; a row is skipped only when its (record key, `record_hash`) is unchanged, so a new key rewrites every row into a new part; the reader takes the newest `fetched_at`, a tie to the later `run_stamp`.
- **The classification to reuse:** `continuation.py::_line_stance` (`template` / `candidate` / `holding` / `unclassified`; `candidate` folds the words candidate, initiate, interesting). The CTO's six names split `candidate` three ways (`candidate`, `initiate`, `interest`) and have no value for an unknown phrase, which `_line_stance` calls `unclassified` and which is NOT a holding. **The cell adds `unclassified` as a seventh value (MECE: a phrase the table has not seen needs a home; the CTO is told).** `none` = the row names no fund, or the fund came from the bare-token fallback (no recommendation line states a relation).
- **The held-consumer:** `fund_form.py:262` (`gather_items`) reads `row.get("fund")`; that is `cf-3`.
- **THE GATEWAY WHITELIST (a finding the ruling does not name):** `harvest_research.py::REPORT_FIELDS` (line 60) is a fixed tuple; the served `research_reports[]` entry is `{f: row.get(f) for f in REPORT_FIELDS}` plus `part`. **`fund_relation` is not served to any gateway consumer until `REPORT_FIELDS` gains it, and that is a gateway release** (site Z the host owner, a restart, the `ce-3` wording can ride it). The CTO's proof (ADBE, SNPS, MNST, ML_FP, CLX read candidate or template) is a gateway read; the alternative is a direct read of the silver parquet. Asked of the CTO in the cut message.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cg-1` | `cg-1` | **`fund_relation` is a key of the silver row** (a new pure module `fund_relation.py`, called by `typed.py::record()`), seven values; offline tests with mutants and a drift test against `_line_stance` over the 22 round-91 census phrases; **a read-only census of the stored silver** (the newest row per report as the gateway serves it) printing the count per relation and the CTO's named proof line; **a dry run of the rewrite** (a recording client, nothing put) printing the rows, the date partitions and the part keys it would write. It does not touch `fund_form`, `continuation.py` or the gateway. | LOCAL (reads S3, writes nothing) | worker `~161` | CUT |
| `HVST-cg-2` | -- | **The silver rewrite:** every row re-appended with `fund_relation` (derived from its stored `fund` and `fund_evidence`, no bronze or extraction read), new parts only, canary then the rest, a manifest line per part, foreground (S44); proof: ADBE, SNPS, MNST, ML_FP, CLX read candidate or template and UNH reads holding in the silver, and every row the dry run named is in the newest part. A seat order under its own never-widen pair. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cg-1` merged and the pair |
| `HVST-cg-3` | -- | **The gateway serves `fund_relation`** (`REPORT_FIELDS` gains it; the `ce-3` wording may ride the same release), host owner told first. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on the CTO's word on the release and the pair |
| `HVST-cf-3`, `HVST-cf-5` | -- | The `fund_form` chain: `gather_items` counts `fund_relation = holding` reports only and drops `typed.MISFILED_REPORTS`; then the per-fund objects are rebuilt, under their own pair; the code lands only together with newly written fund forms (the dossier-build hazard of section 121). | LOCAL, then WORLD | worker, then SC1 | DEFINED, NOT CUT: wait on `cg-2` |
| item 4 (the dell1 cycles) | none | SC1's hourly `sa` reads stand; long write runs are foreground with a manifest check after each write (S44). | -- | SC1 | CARRIED |

- **Fan-out:** `N of M chains, N=1 worker (cg-1) of M=1 chain, cap 8` (`cg-1` then `cg-2` / `cg-3`, then `cf-3`, then `cf-5` are one dependency chain; the gateway cell is a seat order).
- **Checks at the cut (dry-run at the base):** `cg-1` AC1 FAIL as expected (no test file), AC2 PASS as expected (`58 passed`), AC3 and AC4 FAIL as expected (`cat` of a file that does not exist).
- **Not cut (named):** `ce-5` (deferred, rides `cg-3` if the CTO says so); `D1-S39` (`not_held`); the `line_only` text recovered from `section_leads`; the standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

### 122a. ROUND 92 -- the CTO cut `cg-3` (msg 7775): the gateway release rides the silver rewrite; `HVST-cg-4` (the code half) CUT in parallel (2026-10-17 ~23:3xZ)

The CTO accepted the recommendation: a gateway consumer still reading `fund` as held is the live reason `ce-5` was waiting for. **Order (his):** (1) `cg-1` census and dry run; (2) the silver rewrite (`cg-2`) under its pair; (3) `cg-3`, the gateway release, AFTER the silver lands so the field is never served empty; (4) the proof read through the gateway on ADBE, SNPS, MNST, ML_FP and CLX with UNH as control; `cf-3` and `cf-5` follow (2). One release, its own pair, site Z told first, the stale-base guard on the live commit (`ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md`); the two `ce-3` files ride it.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cg-4` | `cg-4` | **`REPORT_FIELDS` gains `fund_relation`** (one tuple, `harvest_research.py:60`) with an offline test (served, absent-key row served `None`, pinned tuple, all seven values, a mutant). The CODE half of the gateway release; deploys nothing. | WORLD (the path floor of `infra/`; workstream `GATEWAY-FUNDREL`) | worker `~162` (light) | CUT, in parallel with `cg-1` (disjoint write sets) |
| `HVST-cg-3` | -- | **The gateway release** on the live deployed commit: the files of `cg-4` and of `ce-3` (`b77e08e198`), nothing else; host owner told first; the controls of the carried file; restart; the MCP tool count and `/health` equal before and after. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cg-2` (the field must not be served empty), `cg-4` merged and its own pair |
| `HVST-cg-2` | -- | The silver rewrite (section 122). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cg-1` merged and the dry run read |
| `HVST-cf-3`, `HVST-cf-5` | -- | The `fund_form` chain (section 122). | LOCAL, then WORLD | worker, then SC1 | DEFINED, NOT CUT: wait on `cg-2` |

- **Fan-out (this recut):** `N of M chains, N=2 workers (cg-1, cg-4) of M=2 chains, cap 8` (the silver chain `cg-1` then `cg-2` then `cf-3` then `cf-5`; the gateway-code chain `cg-4`, which `cg-3` consumes after `cg-2`).
- **Checks at the cut (dry-run at the base):** `cg-4` AC1 FAIL as expected (no test file), AC2 PASS as expected (`43 passed`).

### 122b. ROUND 92 -- `HVST-cg-4` merged (`290f2e9e6d`); `HVST-cg-3` CUT, STAGED behind the silver rewrite and its pair (2026-10-17 ~23:5xZ)

`HVST-cg-4` (worker `~162`) merged: `REPORT_FIELDS` gains `fund_relation`; AC1 `5 passed`, AC2 `43 passed`, proof VALID (all re-run here on the merged tree). Its ARMED note `D1-W162-S1` (a closed batch-4 ledger names a rollback to `d3ae88be46`) is dismissed by row `D1-S48`: the manifest shows the live commit moved three times since, and the release is cut on the live commit with the `b77e08e198^1` equality guard.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cg-3` | `cg-3` | **The gateway release** of `harvest_research.py` (the `ce-3` hunk and the `REPORT_FIELDS` hunk) and the two tests, on the live commit; the host owner told first; START CONDITION (b): a newest silver part is read and carries `fund_relation`; proof `FUND_RELATION_SERVED` on ADBE, SNPS, MNST, ML_FP, CLX with UNH as control. Workstream `FUNDREL-RELEASE`. | WORLD | seat SC1 | CUT, STAGED: waits on `HVST-cg-2` complete and the pair (COO half to write after the dry run is read, CTO half to sign) |
| `HVST-cg-2` | -- | The silver rewrite (section 122). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cg-1` merged |
| `HVST-cf-3`, `HVST-cf-5` | -- | The `fund_form` chain (section 122). | LOCAL, then WORLD | worker, then SC1 | DEFINED, NOT CUT: wait on `cg-2` |

- **Fan-out (this recut):** `N of M chains, N=0 workers (cg-3 is a seat order) of M=1 chain, cap 8`.
- **Check at the cut (dry-run at the base):** `cg-3` AC1 to AC4 FAIL as expected (no `cg3_served.out`).

### 122c. ROUND 92 -- `HVST-cg-1` merged (`ad116e0037`); the CTO ruled two classification gaps (msg 7782); `HVST-cg-5` CUT before the silver rewrite (2026-10-18 ~00:0xZ)

`HVST-cg-1` merged: census over 353 stored reports (`holding=117 candidate=14 initiate=2 interest=2 template=1 unclassified=2 none=215`), the CTO's proof line equal, re-run by the issuer identical; the dry run plans 3 new parts (353 rows, nothing put). Two holdings read wrong: `ORA_FP` (`Consider size reduction in IDVZ`, `unclassified`) and `CPA` (header misspelled `RECOMMEDATION`, `none`). **Ruled (CTO, msg 7782):** (a) `reduction` is a holding word; (b) `RECOMMEDATION` is accepted as one closed-list alias, no fuzzy matching; re-run the census before the rewrite; expected `holding=121 unclassified=0 none=213`. **The issuer adds `adding`** (CPA's line reads `Consider adding ... in IDVZ taking it to 150-200bps`; `add` is whole-word, so without it the two CPA rows would read `unclassified`); named to the CTO.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cg-5` | `cg-5` | **`fund_relation` reads `reduction` and `adding` as holding words and accepts the alias `RECOMMEDATION`** (before the fund token, closed list), offline arms with a mutant, and a re-run of the census (`MOVED_ROWS=4`: the 2 ORA and the 2 CPA rows). Workstream `FUNDREL-CLASSIFY`. | LOCAL | worker `~163` (light) | CUT |
| `HVST-cg-2` | -- | The silver rewrite (section 122). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cg-5` merged (the classifier is fixed into the rows) |
| `HVST-cg-3` | `cg-3` | The gateway release (section 122b). | WORLD | seat SC1 | CUT, STAGED (waits on `cg-2` and the pair) |
| `HVST-cf-3`, `HVST-cf-5` | -- | The `fund_form` chain. | LOCAL, then WORLD | worker, then SC1 | DEFINED, NOT CUT: wait on `cg-2` |

- **Fan-out (this recut):** `N of M chains, N=1 worker (cg-5) of M=1 chain, cap 8` (the silver chain `cg-5` then `cg-2` then `cf-3` then `cf-5`; `cg-3` is a seat order).
- **Check at the cut (dry-run at the base):** `cg-5` AC1 FAIL as expected (`17 passed` does not match `22 or more`), AC2 PASS as expected (`58 passed`), AC3 and AC4 FAIL as expected (no census file).

### 122d. ROUND 92 -- `HVST-cg-5` merged (`a9aecdd593`); `HVST-cg-2` CUT, STAGED behind the CTO half, site Z and GO (2026-10-18 ~00:2xZ)

`HVST-cg-5` merged: the re-census reads `holding=121 candidate=14 initiate=2 interest=2 template=1 unclassified=0 none=213` (the CTO's expected counts; re-run by the issuer, identical to the worker's); `MOVED_ROWS=4`; the CTO's guard on `adding` (msg 7784) is clear: two rows match, both `CPA`, a held position. The dry run at `a9aecdd593` (issuer): 353 rows, 3 new parts (121, 148, 84), nothing put.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cg-2` | `cg-2` | **Every stored silver `research-report` row (the newest per report, 353) is re-appended with `fund_relation`** as 3 NEW parts, one date partition per foreground command, smallest (`2026-09-25`, 84 rows) first, each part read back before the next; nothing served changes until `cg-3`. A seat order under its own never-widen pair (COO half written, sha256 `11cf6bd0...9158`; the CTO half is next). Workstream `SILVER-REWRITE`. | WORLD | seat SC1 | CUT, STAGED: waits on the CTO half, site Z's answer and the issuer's GO |
| `HVST-cg-3` | `cg-3` | The gateway release (section 122b). | WORLD | seat SC1 | CUT, STAGED (waits on `cg-2` complete and its own pair) |
| `HVST-cf-3`, `HVST-cf-5` | -- | The `fund_form` chain. | LOCAL, then WORLD | worker, then SC1 | DEFINED, NOT CUT: wait on `cg-2` |

- **Fan-out (this recut):** `N of M chains, N=0 workers (cg-2 is a seat order) of M=1 chain, cap 8`.
- **Check at the cut (dry-run at the base):** `cg-2` AC1 to AC3 FAIL as expected (no `cg2_served.out`).
- **Gold effect named in the pair:** none; the gateway reads silver rows through a fixed tuple that does not carry the key yet (`cg-4` merged, not released), so UNH and CPA read equal before and after.

### 122e. ROUND 92 -- `HVST-cg-2` WRITTEN (01:00Z, 3 parts, 353 rows), the CTO signed `cg-3` (`48d6e4e72b`); `HVST-cf-3` CUT (2026-10-18 ~01:2xZ)

`HVST-cg-2` wrote its three parts (84 + 121 + 148 = 353 rows) 01:00:35Z to 01:01:14Z; SC1 read each back (PASS) and the issuer re-read the bucket by the gateway's newest-part rule: 353 of 353 from the new parts, all with `fund_relation`, counts equal the census, 0 mismatches against the superseded rows. **C-7 ruled (issuer, accepted by the CTO msg 7813):** the `part` pointer and `source_keys` naming the new parts are the expected consequence of add-only parts; my COO half said they would stay equal and was wrong (AMENDMENT 2 of `cg-2`). The ledger close of `cg-2` is SC1's, pending. The CTO signed the `cg-3` half (`48d6e4e72b`, binds `29d9e1b9...87c4`): the order is SC1 commits `cg-2`'s close, then site Z is told, then the cut and deploy, then the proof, then the ref to the shared lineage.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cf-3` | `cf-3` | **`fund_form.gather_items` counts only reports whose silver row states `fund_relation == holding` and never the misfiled reports; a row without the key raises; `METHOD_VERSION` `2`;** offline tests with a mutant; a read-only census with a pinned baseline (`a9aecdd593`), expected `funds=2 reports_after=115 dropped_nonholding=22` (IDVZ 82, PFOE 33; DIVZ has no holding report). Workstream `FUNDFORM-CODE`. | LOCAL | worker `~164` | CUT |
| `HVST-cf-5` | -- | The fund-form rebuild: `fund_form.write()` once, IDVZ and PFOE, two NEW `v2` objects, then one dossier-build probe on a holding name and the control, under its own pair; no dossier build is run by anyone between the `cf-3` merge and this write. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cf-3` merged |
| `HVST-cg-3` | `cg-3` | The gateway release (sections 122b and 122c). | WORLD | seat SC1 | CUT, STAGED: pair SIGNED both halves; waits on `cg-2`'s ledger close COMMITTED, site Z and GO |

- **Fan-out (this recut):** `N of M chains, N=1 worker (cf-3) of M=2 chains, cap 8` (the fund-form chain `cf-3` then `cf-5`; the gateway chain, a seat order; the two chains share no write set).
- **Check at the cut (dry-run at the base):** `cf-3` AC1 FAIL as expected (no test file), AC2 PASS as expected (`80 passed`), AC3 FAIL as expected (no census file).

### 122f. ROUND 92 -- `HVST-cg-3` DEPLOYED and complete; `HVST-cf-5` CUT, STAGED behind its pair (2026-10-18 ~02:3xZ)

`HVST-cg-3` landed 02:06:03Z (release `4257a2aa42`, ledger closed `ee508eb3cb`, ref pushed): `harvest_get_research` now serves `fund_relation` in each `research_reports[]` entry; I read MNST, ML_FP, CLX and UNH through it myself (`candidate`, `template`, `candidate` x2, `holding`); SC1 read ADBE and SNPS; gold values unchanged. One effect the COO half did not name: the tool caps `research_reports[]` by response size, so the added key shows one fewer entry for a security with many reports (CPA 10 to 9 of 37; row `D1-S50`).

**A CORRECTION to sections 121, 122e and the `cf-3` notes:** the hazard of changing `fund_form.gather_items` is NOT that a dossier build finds no stored fund form; `substrate._pick_stored` (lines 121-159) falls back to the lexicographically last stored object with `current` False and returns an absence only when the partition is empty. A dossier built between the `cf-3` merge and `cf-5` would SILENTLY cite the stale version-1 form. The precaution (no dossier or continuation build between the two) stands for that reason.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cf-5` | `cf-5` | **Two `research-fund-form` objects (method version 2) are written: PFOE (33 reports, the canary) then IDVZ (82), each its own foreground command with a read-back;** then `read_latest` and the substrate view resolve them as current, an in-memory dossier preview differs from the stored dossier only in `fund_form_ref`, and the served reads of UNH and CPA are equal. DIVZ gets no form. A seat order under its own never-widen pair (COO half written, sha256 `a7c7f05e...8b6f`; the CTO half is next). Workstream `FUNDFORM-REBUILD`. | WORLD | seat SC1 | CUT, STAGED: waits on the CTO half, site Z's answer and the issuer's GO |

- **Fan-out (this recut):** `N of M chains, N=0 workers (cf-5 is a seat order) of M=1 chain, cap 8`.
- **Check at the cut (dry-run at the base):** `cf-5` AC1 to AC4 FAIL as expected (no `cf5_served.out`).
- **Round 92 cells:** `cg-1`, `cg-2`, `cg-3`, `cg-4`, `cg-5`, `cf-3` complete; `cf-5` staged. When `cf-5` closes the round's enrichment list (items 1 and 2) is done; item 3 (`ce-5`) was folded into `cg-3`; item 4 (the cycles) is SC1's.

### 122g. ROUND 92 -- `HVST-cf-5` complete (ledger closed `334218577d`); round-92 packet sent; the CTO ruled `D1-S52` (msg 7864, `ledger/CTO_RULING_D1_S52_CONTINUATION_PICK_20261018.md` @162d5a6934) (2026-10-18 ~03:3xZ)

All 7 round-92 orders are `complete` (`cg-1`, `cg-2`, `cg-3`, `cg-4`, `cg-5`, `cf-3`, `cf-5`); `round-close-check` round 92 = `orders=7 verdict=MAY-CLOSE`; the L8 packet is `ledger/ROUND92_L8_PACKET_20261018.md` (`bf48426b91`).

**STANDING INSTRUCTION OF THIS DECOMPOSITION'S ISSUER (the CTO's ruling; it IS the disarm of the ARMED row `D1-S52`):** no dossier or continuation rebuild is ORDERED for any security whose newest stored continuation is below the current continuation method (`/5`; 77 of the 94 securities today; the `HVST-cf-4` names are the 17 at `/5`) until round-93 cell 1 lands, and none is ordered that reads DIVZ's stale fund form (C-6). Cause, read by the CTO: when no stored continuation is at the current method, `continuation._select_stored` (line 1103) returns the FIRST key in sort order, so the pick follows the object-name hash (UNH: `28404359`, method `/3`, fund absent, not the `/4` PFOE object the gateway serves). **Round-93 cell 1 (with DIVZ), the CTO's:** the fallback picks the highest `method_version`, then the last written; graded by a difference test (UNH picks `/4`) and a census of the substrate's pick against the object the gateway serves. The CVO's remediation row carries `disarms: AMGT_HARVST-D1-S52`.

| cell | state |
|---|---|
| round 93 cell 1 (the continuation pick and DIVZ) | the CTO's round-92 analysis item; cut when the analysis arrives |
| round 93 other items | `D1-S49` (one shared classifier), `D1-S50` (the response-size cap), `D1-S51` (idle seat and unread mail), the standing candidates |

## 123. ROUND 93 -- the CTO's round-92 analysis (`ledger/ROUND_ANALYSIS.round92.md` @943c856f6e; msg 7867): two worker cells cut in ONE issuance, five defined and NOT cut, 2026-10-18 ~03:5xZ

Round 92 closed MAY-CLOSE (CVO `ADJUDICATION_v86.md`, `REMEDIATION_v23.md` @44e57223b3; 9 rows dismissed; the controlled reading of `HVST-cf-5` `AC3` upheld, the literal FAIL kept on the record). `D1-S52` was DISARMED by the CTO's standing no-rebuild instruction (section 122g). The round-93 enrichment list (CTO): (1) the picker fix with DIVZ's version-2 form at 0 reports; (2) one shared classifier (`D1-S49`) with a no-write census before any gold write; (3) the response states its truncation (`D1-S50`) on a gateway release; (4) a `/5` rebuild of the exposed names only after (1) and (2) read 0 differing; (5) the harvest cycles under the S44 rule. **`D1-S51` is MSTR's row, not a cell.** The CTO's S51 rules for orders to SC1 (msgs 7871, 7874): every stop and every expected question goes in the order before the run; no ask that needs an answer inside a write window; check SC1's READ ack within 10 minutes of handing it an order and type a nudge if none.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ch-1` | `ch-1` | **`continuation._select_stored` with no candidate at the current method version picks the highest `method_version`, then the last written; never the first key;** a difference-controlled offline test (the UNH-shaped four pick `/4`, the old rule `/3`); a read-only census over every security with a continuation partition: `old`, `new` and the gateway's pick, with the denominator. Workstream `PICKER-FIX`. | LOCAL | worker `~165` | CUT |
| `HVST-ch-4` | `ch-4` | **`fund_form.write` writes a form for every fund of the closed set `FUNDS`; a fund no holding report names gets `reports 0` and an `absent` reason** (IDVZ and PFOE documents unchanged, method version stays `2`); offline tests with a mutant; a read-only census (expected `forms=3 idvz=equal pfoe=equal divz=absent divz_reports=0`). Workstream `DIVZ-FORM`. | LOCAL | worker `~166` | CUT |
| `HVST-ch-2` | -- | **One shared word-list module** read by gold `continuation._line_stance` and silver `fund_relation.classify`, no copy; the drift test over all 353 stored report lines; before any gold write a no-write census lists every gold value the shared list would move (a non-zero count goes under its own pair, never as a rider; `METHOD_VERSION` is NOT bumped here, because a bump makes every name "no `/5` continuation"). | LOCAL | worker | DEFINED, NOT CUT: edits `continuation.py` as `ch-1` does; waits on `ch-1` merged (one chain) |
| `HVST-ch-5` | -- | The DIVZ form written: ONE `research-fund-form` object (`fund=divz`), under its own never-widen pair, every stop and expected question in the order before the run (CTO msg 7871). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `ch-4` merged and its pair |
| `HVST-ch-3` | -- | The response states its truncation (`research_reports_truncated: k of n`), cap unchanged. **A PREMISE OF THE CTO'S ITEM IS CONTRADICTED BY THE CODE AND IS ASKED BACK:** `harvest_research.py` lines 409-417 already set `truncated: true` and `omitted_items.research_reports: <k>` whenever a list is cut, so the cut is not silent; the new field would add shown-of-total. | WORLD (the `infra/` floor) | worker | DEFINED, NOT CUT: held on the CTO's answer (one ask) |
| `HVST-ch-6` | -- | The gateway release for `ch-3` (the `ce-5` wording already rode `cg-3`; nothing remains to ride). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `ch-3` |
| `HVST-ch-7` | -- | A `/5` rebuild of the names with no `/5` continuation, under its own pair; the standing instruction lifts then, not before. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `ch-1` and `ch-2` merged and their censuses reading 0 differing |
| item 5 (the cycles) | none | SC1's hourly `sa` reads stand; long write runs are foreground with a manifest check after each write (S44). | -- | SC1 | CARRIED |

- **Fan-out:** `N of M chains, N=2 workers (ch-1, ch-4) of M=3 chains, cap 8`: A (`ch-1` then `ch-2` then `ch-7`), B (`ch-3` then `ch-6`, held on the CTO's answer), C (`ch-4` then `ch-5`). The two worker cells share no write set (`continuation.py` and its tests against `fund_form.py` and its tests).
- **Checks at the cut (dry-run at the base):** `ch-1` AC1 FAIL as expected (no test file), AC2 PASS as expected (`82 passed`), AC3 and AC4 FAIL as expected (no census file); `ch-4` AC1 FAIL as expected, AC2 PASS as expected (`66 passed`), AC3 FAIL as expected.
- **Not cut (named):** `ch-2`, `ch-3`, `ch-5`, `ch-6`, `ch-7` as above; the second key-order fallback `substrate._pick_stored` line 158 (outside the CTO's ruling; `ch-1` files a row); the standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

### 123a. ROUND 93 -- item 3 WITHDRAWN by the CTO (addendum 1 of `ledger/ROUND_ANALYSIS.round92.md` @e2dd469994; msg 7877); `HVST-ch-3` and `HVST-ch-6` are not cut (2026-10-18 ~03:4xZ)

The CTO read `harvest_research.py` lines 409-417 and confirmed that `truncated: true` and `omitted_items` already state a truncation; his "silent" framing was wrong; **item 3 is withdrawn, `D1-S50` closes as already stated, `HVST-ch-3` (the new field) and `HVST-ch-6` (its gateway release) leave the round's cell set.** The shown-of-total sentence rides ONLY a gateway release that is due for another reason. (`ce-5`'s wording already rode `HVST-cg-3`; nothing remains to ride.)

- **Fan-out line of section 123 amended:** `N of M chains, N=2 workers (ch-1, ch-4) of M=2 chains, cap 8` (chain A: `ch-1` then `ch-2` then `ch-7`; chain C: `ch-4` then `ch-5`); chain B is withdrawn.
- **Cells left:** `ch-1` (worker `~165`) and `ch-4` (worker `~166`) CUT; `ch-2`, `ch-5`, `ch-7` DEFINED, NOT CUT as in section 123.
- **Row `D1-S50`:** closes as already stated (the CVO dispositions it).

### 123b. ROUND 93 -- `HVST-ch-4` merged (`2e0dc6af2e`); `HVST-ch-5` CUT, STAGED behind its pair; `HVST-ch-1`'s census budget was the issuer's miscount (2026-10-18 ~04:1xZ)

`HVST-ch-4` (worker `~166`) merged: AC1 `7 passed`, AC2 `66 passed`, AC3 `CENSUS-FORMS forms=3 idvz=equal pfoe=equal divz=absent divz_reports=0` (re-run by the issuer, identical); IDVZ and PFOE are byte-equal to the stored version-2 objects, DIVZ `a181f84957dbb8b7.json` is the one new object (0 reports, an absent reason). `HVST-ch-1` (worker `~165`): code and tests done (AC1 `14 passed`, AC2 `82 passed`); its census aborted at request 1501 of my 1500-request budget after 67 of 95 partitions (about 22 requests per security): **my miscount**; AMENDMENT 1 raised it to 3500 requests and 600 MiB and the worker reruns and regrades (it also fixed a defect of its own, the `PICK` line prefix).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ch-5` | `ch-5` | **The ONE DIVZ `research-fund-form` object (method version 2, 0 reports, an absent reason) is written;** read back; `read_latest("DIVZ")` and the substrate pick resolve it current; `fund_form --compare` runs over three funds; the UNH gateway read is equal. A seat order under its own never-widen pair (COO half written, sha256 `183efbbf...7e7a`; the CTO half is next); the CTO's S51 rules are applied (section 3 of the order holds every stop and expected question). Workstream `DIVZ-WRITE`. | WORLD | seat SC1 | CUT, STAGED: waits on the CTO half, site Z's answer and the issuer's GO |

- **Fan-out (this recut):** `N of M chains, N=0 workers (ch-5 is a seat order) of M=1 chain, cap 8`.
- **Check at the cut (dry-run at the base):** `ch-5` AC1 to AC4 FAIL as expected (no `ch5_served.out`).

### 123c. ROUND 93 -- `HVST-ch-1` merged (`bec8a53981`); `HVST-ch-5` PENDING at SC1 with its pair signed (CTO half @add9119d81); `HVST-ch-2` CUT (2026-10-18 ~04:2xZ)

`HVST-ch-1` (worker `~165`) merged: AC1 `14 passed`, AC2 `82 passed`, AC3/AC4 `CENSUS-PICKER securities=95 with_current=17 no_current=78 new_equals_gateway=78 new_differs_from_gateway=0 old_equals_gateway=26 old_differs_from_gateway=52` and `PICK UNH_US_Equity candidates=4 old=28404359/3 new=4d837586/4 gateway=4d837586/4` (re-run by the issuer, identical). **The hazard of `D1-S52` was not UNH-only: the old rule differed from the served object for 52 of the 78 names with no `/5` continuation.** `no_input_match=0`. The standing instruction (section 122g) lifts when `ch-1` AND `ch-2` are merged with their censuses reading 0 differing; `ch-1`'s reads 0.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ch-2` | `ch-2` | **One shared word-list module `line_words.py`** read by gold `continuation._line_stance` and silver `fund_relation.classify` (the three patterns are the SAME objects, no copy); an offline test with a mutant; **two read-only censuses:** the drift over every stored report line (expected `drift=0`) and the gold census (every gold value the shared list would move, the baseline pinned at `bec8a53981`; a non-zero count goes under its own pair). `METHOD_VERSION` is NOT bumped. Workstream `SHARED-CLASSIFIER`. | LOCAL | worker `~167` | CUT |
| `HVST-ch-5` | `ch-5` | The DIVZ form written (section 123b). | WORLD | seat SC1 | PENDING at SC1 for preparation (handed 04:08:41Z); the CTO half is signed; waits on site Z's answer and the issuer's GO |
| `HVST-ch-7` | -- | The `/5` rebuild, under its own pair. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `ch-2` merged and both censuses reading 0 differing |

- **Fan-out (this recut):** `N of M chains, N=1 worker (ch-2) of M=2 chains, cap 8` (chain A: `ch-2` then `ch-7`; chain C: `ch-5`, a seat order).
- **Check at the cut (dry-run at the base):** `ch-2` AC1 FAIL as expected (no test file), AC2 PASS as expected (`137 passed`), AC3 and AC4 FAIL as expected (no census file).

### 123d. ROUND 93 -- `HVST-ch-2` merged (`766b8e25e0`); `HVST-ch-5` written; the CTO ruled the scope of item 4 (msg 7903); `HVST-ch-8` CUT (2026-10-18 ~04:3xZ)

`HVST-ch-2` (worker `~167`) merged: AC1 `5 passed`, AC2 `137 passed`, AC3 `CENSUS-SHARED-DRIFT rows=140 drift=0`, AC4 `CENSUS-GOLD-MOVE securities=95 moved=0 fields_moved=0 moved_at_current=0` (re-run by the issuer, identical). **The CTO's measure for item 4 is met:** `ch-1` (the new picker equals the gateway for 78 of 78 names) and `ch-2` (0 of 95 gold values move). `HVST-ch-5`: the DIVZ `research-fund-form` object `a181f84957dbb8b7.json` (method 2, 0 reports) was written 04:29:21Z and read back (the issuer's own bucket read agrees: 12 objects, `read_latest` returns a version-2 form for all three funds); SC1 is on the after-checks.

**Ruled (CTO, msg 7903): the `/5` rebuild writes the 78 CONTINUATIONS ONLY; dossiers stay as served** (a dossier rebuild moves `model_rows` and `as_of`: a separate decision under its own pair, not ordered). The standing instruction (section 122g) **lifts for those 78 continuations** once `ch-1` and `ch-2` are merged (met); it does NOT lift for dossiers. The pair of `HVST-ch-7` must print, per name, every field where the in-memory `/5` continuation differs from the served one: each difference is explained by the method change or is a STOP; the gateway serves continuations, so the pair names that served move and covers both branches.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ch-8` | `ch-8` | **A read-only census of what a `/5` continuation rebuild of the 78 names would change:** each continuation built in memory (`continuation.build`, never `write_one`) and compared FIELD BY FIELD with the one the gateway serves (the gateway's pick rule copied from line 349); a positive control (MNST, at `/5`: 0 changed) and a negative control (a planted change: exactly 1); per-name per-field `DIFF` lines. Workstream `REBUILD-CENSUS`. | LOCAL | worker `~168` | CUT |
| `HVST-ch-7` | -- | The `/5` rebuild: 78 continuation objects, add-only, under its own never-widen pair written FROM `ch-8`'s census. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `ch-8` merged and read, and the pair |

- **Fan-out (this recut):** `N of M chains, N=1 worker (ch-8) of M=2 chains, cap 8` (chain A: `ch-8` then `ch-7`; chain C: `ch-5`, a seat order already written).
- **Check at the cut (dry-run at the base):** `ch-8` AC1 to AC3 FAIL as expected (no census file).

### 123e. ROUND 93 -- `HVST-ch-8` complete; the `ch-7` pair signed; `HVST-ch-7` CUT (2026-10-18 ~04:5xZ)

`HVST-ch-8` merged `091ebacda9`, re-run by the issuer: `CENSUS-CONT-REBUILD partitions=95 at_current=17 names=78 unchanged=78 changed=0 fields_changed=0 inputs_equal=78 name_exists=0`; controls 0 and 1. The pair of `HVST-ch-7`: COO half sha256 `19d80c8bf6bafa94157d1152cc2bcf9f8a11a58fe0c21dc877c49f0dbf8f213c` (`dc5611d194`), CTO half SIGNED `5d4e716fd1` (msg 7909), with one correction applied in the order: the worktree is AT `091ebacda9` exactly (HEAD differs by 22 files under `lib/research`).

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ch-7` | `ch-7` | The `/5` rebuild: 78 `research-continuation` objects, add-only, canary UNH then CPA read through the gateway before the other 76, under the signed pair. Workstream `CONT-M5`. | WORLD | seat SC1 | CUT, STAGED: waits on site Z's answer (C-10) and my GO |

- **Fan-out (this recut):** `N of M chains, N=0 workers, 1 seat order (ch-7) of M=1 chain, cap 8`.
- **Check at the cut, dry-run at the base:** `ch-7` AC1 to AC4 FAIL as expected (no `ch7_served.out`).

### 124. ROUND 94 -- the CTO's round-93 analysis (`ledger/ROUND_ANALYSIS.round93.md` @5ef0dd0efd, msg 7921; round 93 MAY-CLOSE per the CVO's msg 7919) read; ONE issuance (2026-10-18 ~05:5xZ)

The enrichment list (the round's rectangle): item 1 `W165-S3` (the substrate's second fallback), item 2 the dossier rebuild decision (a no-write census first), item 3 the `cg-3` release lineage, item 4 `S51` exercised once, item 5 the dell1 harvest cycles keep running.

**One correction I make to the list:** item 1 says "every stored table the substrate reads (continuation, fund form, dossier)"; `substrate.py` calls `_pick_stored` for continuation, sector_template, fund_form and typecast (lines 216, 250, 270, 282), not the dossier. The census order reads those four; the CTO is told.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-ci-1` | `ci-1` | A read-only census of every stored partition of the four tables the substrate reads: whether any object's `inputs` match today's; for each partition with none, the key-order pick against the rule pick (the highest `method_version`, then the last written); positive and negative controls. Workstream `PICK2-CENSUS`. | LOCAL | worker `~169` | CUT |
| `HVST-ci-2` | `ci-2` | `substrate._pick_stored`'s fallback (line 158) calls `continuation._select_stored` over all the partition's objects, still `current` False; a difference-controlled offline test with a mutant; the census re-run after the change (`module_equals_rule` for every fallback partition). Workstream `PICK2-FIX`. Depends on `ci-1` (same worker queue `~169`). | LOCAL | worker `~169` | CUT, queued behind `ci-1` |
| `HVST-ci-3` | `ci-3` | A no-write census of what a dossier rebuild of the 95 names would move: each dossier built in memory (`dossier.build`, never `write_one`) against the dossier the gateway serves (its `_pick_dossier` rule), field by field, with the cause decided from the `inputs` that differ (`other` is a row); controls. Workstream `DOSSIER-CENSUS`. | LOCAL | worker `~170` | CUT |
| `HVST-ci-4` | -- | The `cg-3` release lineage: `4257a2aa42` is on origin as `rel-amgt-harvst-cg3` (ls-remote read 05:3xZ), contained in neither `origin/CLOUD` nor `origin/box/sitez`; the integrator `0.0.0_AB_MSTR~DELL1` decides the merge into the shared lineage and tells site Z; its ack is recorded. A coordination act with the integrator, no task order (no seat but the integrator may write the shared lineage; an order may not be issued to a Tier-0 seat). | -- | issuer, by message to MSTR | DIRECT (message sent with the issuance) |
| item 4 | -- | `S51` exercised once: the next order I hand to an idle SC1 records the READ-ack time. **Already exercised by `HVST-ch-7`:** handed 04:55:15Z, found idle by a peek at 05:01Z, nudge typed 05:01:47Z, READ ack 05:01:57Z (6 min 42 s after the handing, inside 10 minutes; delivery state read). Recorded as an instance row on `D1-S53`. | -- | issuer | DONE, row filed |
| item 5 | -- | The harvest cycles keep running under the S44 rule: a standing instruction, no cell. | -- | -- | STANDING |

- **Fan-out (this issuance):** `N of M chains, N=2 workers (ci-1 then ci-2 in one queue ~169; ci-3 at ~170) of M=3 chains (A: ci-1 then ci-2; B: ci-3; C: ci-4, a message to the integrator), cap 8`.
- **Checks at the cut, dry-run at the base:** `ci-1` AC1 to AC3 FAIL as expected (no census file); `ci-2` AC1 FAIL as expected (no test file), AC2 PASS as expected (`96 passed in 1.09s` over nine files), AC3 FAIL as expected; `ci-3` AC1 to AC3 FAIL as expected.
- **Not cut (named):** the dossier rebuild itself (the CTO: "not ordered this round"; with the census in hand it goes under its own pair naming the served moves).

### 125. ROUND 95 -- the CTO's round-94 analysis (`ledger/ROUND_ANALYSIS.round94.md` @428b762698, msg 7946; round 94 MAY-CLOSE per the CVO's msg 7945); ONE issuance (2026-10-18 ~07:3xZ)

The enrichment list (the round's rectangle): item 1 `W170-S3` (one key form for slash keys; census first), item 2 the non-slash dossier rebuild under its own pair, item 3 the slash-key dossiers after item 1, item 4 carried (the `cg-3` lineage, base ref `aa2efa2cf3`; `S51`'s one idle-seat READ-ack instance), item 5 the harvest cycles continue.

**The CTO's RULING (section 3):** the rebuild runs for every name WITHOUT a slash in its key (75 of the 77 names whose build moves a served field), under its own never-widen pair; the two slash-key names wait for item 1.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cj-1` | `cj-1` | A read-only census of every slash key in the corpus: which tables hold it under which spelling (raw `security_key=BP/_LN_Equity/` or encoded `BP-SLASH-_LN_Equity`), the denominator printed, with a positive control (a non-slash key: one spelling) and a classifier control. Workstream `SLASH-CENSUS`. | LOCAL | worker `~171` | CUT |
| `HVST-cj-2` | -- | One key form for slash keys: every writer and reader of the harvest tables resolves a slash key through the ONE function `write_one` partitions with (`crosswalk.security_key_partition`); the gateway's harvest tools normalize the requested key through it; `BP/_LN` and `NG/_LN` return the full record whichever form is requested; any stored object under the wrong form is a row, never a rename or a delete. | WORLD (the gateway code is under `infra/`; the gate floors it) | worker, then a release | DEFINED, NOT CUT: waits on `cj-1`'s census (the direction of the fix depends on which tables hold which spelling: the stored reports may sit under the RAW form while the writers partition by the ENCODED one; the CTO's spec says one function, the census says where the stored objects are) |
| `HVST-cj-3` | -- | The gateway release of `cj-2` (DEPLOY_BASE_REF=`aa2efa2cf3`), under its own pair. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-2` merged |
| `HVST-cj-4` | `cj-4` | The non-slash dossier rebuild: 75 `research_dossier` objects, add-only, canary UNH then CPA read through the gateway before the other 73, batches of at most 10, S44, no continuation written, site Z told first, under the pair (COO half `deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ4_DOSSIERS_NONSLASH.md`). Workstream `DOSSIER-WRITE`. | WORLD | seat SC1 | CUT, STAGED: waits on the CTO half, site Z's answer (C-10) and my GO |
| `HVST-cj-5` | -- | The slash-key dossiers (`BP/_LN_Equity`, `NG/_LN_Equity`), under the same pair shape. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-2` merged and `cj-1`'s census reading every slash key whole |
| item 4 | -- | The `cg-3` lineage waits on site Z (CTO msg 7943; item closes when `cg-3` is contained in `CLOUD`); `S51` is exercised again at `cj-4`'s handing (row `D1-S54` holds the first instance). | -- | -- | CARRIED |
| item 5 | -- | The harvest cycles keep running under the S44 rule: standing. | -- | -- | STANDING |

- **Fan-out (this issuance):** `N of M chains, N=1 worker (cj-1) plus 1 seat order (cj-4) of M=2 cuttable chains (A: cj-1 then cj-2, cj-3, cj-5; B: cj-4), cap 8`. The second chain has no worker; its executor is the CloudOps seat under a pair.
- **Checks at the cut, dry-run at the base:** `cj-1` AC1 to AC3 FAIL as expected (no census file); `cj-4` AC1 to AC4 FAIL as expected (no `cj4_served.out`).
- **The `KMB_US_Equity` note:** the 18 names whose build moves no field include `KMB_US_Equity`, whose `inputs` differ from the stored dossier's by the continuation key only; `write_one` would write it. The ruling names the 77 moved names; KMB is outside `cj-4` and is named in the pair.

### 126. ROUND 95 -- `HVST-cj-1` complete; `HVST-cj-2` CUT; the slash-key hold; the ARMED row (2026-10-18 ~07:5xZ)

`HVST-cj-1` merged `bc1f5233ec`, re-run by the issuer (identical): the corpus holds exactly two slash keys, stored ONLY under the encoded partition in every keyed table (214 objects), the silver column holds the raw spelling, and the gateway's raw-key prefixes match 0 objects of either key. The direction of the fix follows: the gateway normalizes (the partition form for prefixes, the raw key for the silver column); no writer and no stored object changes.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cj-2` | `cj-2` | The gateway's harvest tools resolve a slash key to its one stored form at the entry of every harvest tool: a difference-controlled offline test with a mutant, the unchanged existing tests (48), and a read-only replay of the changed tool code against the real stored objects for both keys in both spellings (expected `whole=4`). Code and tests only, no release. Workstream `SLASH-FIX`. | WORLD (the gate floors `infra/`; no deploy) | worker `~171` | CUT (queued behind `cj-1` in the same worker queue) |
| `HVST-cj-3` | -- | The gateway release of `cj-2` (`DEPLOY_BASE_REF=aa2efa2cf3`), under its own pair. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-2` merged |
| `HVST-cj-5` | -- | The two slash-key dossiers under the same pair shape as `cj-4`. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-2` merged (the CTO: "after item 1 is merged and its census reads every slash key whole") |

- **Standing hold (mine, recorded here):** NO `write_one` (dossier or continuation) runs for `BP/_LN_Equity` or `NG/_LN_Equity` until `cj-2` is merged and its replay reads `whole=4`. It is mechanical in `cj-4` (the 75-name list excludes both; the driver refuses a name outside the list) and `cj-5` is not cut.
- **The ARMED row `AMGT_HARVST-D1-W171-S1` (disarm owner `2.0.0_SA_COO~W1`) is NOT disarmed today.** It names the served incompleteness for the two keys, which is the live condition and not an act hazard: it stays ARMED until `cj-3` is released, when I disarm it with my own served read of `BP/_LN_Equity` and `NG/_LN_Equity` in both spellings through the live gateway, each returning the dossier, continuation, ai_fill and reports (a dismissal row of mine that `adjudicates` it, as `D1-S47` did for `D1-W159-S1`). **A consequence the round 95 packet states:** the L10 close needs every ARMED row dispositioned, so round 95 cannot close before `cj-3`.
- **Fan-out (this recut):** `N of M chains, N=1 worker (cj-2, the same queue as cj-1) of M=2 cuttable chains (A: cj-2 then cj-3, cj-5; B: cj-4, in its window), cap 8`.
- **Checks at the cut, dry-run at the base:** `cj-2` AC1 FAIL as expected (no test file), AC2 PASS as expected (`48 passed in 2.91s` over nine files), AC3 FAIL as expected (no replay file).

### 127. ROUND 95 -- `HVST-cj-2` complete (merged `c692c5dfbb`); `HVST-cj-6` CUT; three ARMED rows named; the site Z lineage landed (2026-10-18 ~08:1xZ)

`HVST-cj-2`: the three tools of `harvest_research.py` read a slash key from its one stored form; replay `whole=4`, identical on my re-run. The worker's rows found (a) the app holds a COPY of the module's rule (`D1-W171-S3`, ARMED: arm 7 of the test is the only drift guard), (b) the peers, posture, scores, filings, drafting and management prefixes hold BOTH spellings and stay on the caller's spelling (`D1-W171-S4`, ARMED: the CTO decides the spelling), (c) `harvest_figures.py` and `harvest_identity.py` build raw `security_key=` partitions from the caller's key (`D1-W171-S5`, ARMED).

**A correction of my own `cj-1` note:** its sentence said the corpus holds the two slash keys only under the encoded form in every keyed table; the census domain (two roots, `security_key=` partitions) was narrower than the sentence; the peers, posture, scores and filings tables outside it hold both spellings. The note is corrected.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cj-6` | `cj-6` | The same normalizer applied to every other gateway harvest module that builds a `security_key=` partition from a caller's key (`harvest_figures.py`, `harvest_identity.py`, any other the audit finds): one definition in the app, a difference-controlled test with a mutant, the ten existing test files (56), and a read-only replay. Workstream `SLASH-OTHER`. | WORLD (the `infra/` floor; no deploy) | worker `~171` | CUT (same worker queue) |
| `HVST-cj-3` | -- | ONE gateway release carrying `cj-2` and `cj-6` (`DEPLOY_BASE_REF=aa2efa2cf3`), under its own pair. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-6` merged |
| `HVST-cj-5` | -- | The two slash-key dossiers. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-3` released and read |

- **For the CTO (the packet, not an inbox ask):** `D1-W171-S3` (whether the module moves where the artifact ships it) and `D1-W171-S4` (which spelling a reader takes for the path-keyed tables); neither blocks `cj-3`.
- **Site Z's lineage landed** (MSTR msg 7965): `cg-3`, `aa2efa2cf3`, `d077cef043` and `efcc8ae19f` are ancestors of `origin/box/sitez` (merge `105647b69d`); none is on `origin/CLOUD` yet; item 3 of round 94 closes when CLOUD holds `cg-3`.
- **Fan-out (this recut):** `N of M chains, N=1 worker (cj-6, the same queue as cj-2) of M=2 cuttable chains (A: cj-6 then cj-3, cj-5; B: cj-4, in its window), cap 8`.
- **Checks at the cut, dry-run at the base:** `cj-6` AC1 FAIL as expected (no test file), AC2 PASS as expected (`56 passed in 3.04s` over ten files), AC3 FAIL as expected (no replay file).
- **ARMED rows open (disarm owner me):** `D1-W171-S1`, `-S3`, `-S4`, `-S5`: the round 95 L10 close needs them dispositioned.

### 128. ROUND 95 -- `HVST-cj-6` complete (merged `34fb405b29`); round-94 item 3 CLOSED; the release cut question (2026-10-18 ~08:4xZ)

`HVST-cj-6` merged: one normalizer in `app/harvest_keys.py`, imported by `harvest_research.py`, `harvest_figures.py` and `harvest_identity.py`; the fundamentals kinds, the bestdata query and coverage read the partition form; replay re-run by me, identical (12 of 14 cells equal; the two coverage cells differ by the path-component prefixes this cell keeps, CTO decision). New rows: `D1-W171-S6` (ARMED, the coverage cells), `-S7` (INERT: the encoded spelling already reached the objects; only the raw one was refused: corrects the worker's S5 and my sentence in the `cj-6` order), `-S8` (INERT: `test_og_gt8.py` fails before and after; it reads `deploy-to-ec2.sh`), `-S9` (INERT: `publication-links/v1/BP//`).

**Round-94 item 3 is CLOSED** (CTO msg 7975, MSTR msg 7974; my own read: `4257a2aa42` is an ancestor of `origin/CLOUD` at `2ae0766ad1`).

**The release (`HVST-cj-3`):** the CTO's rule (msg 7975): cut from the CLOUD tip with `DEPLOY_BASE_REF=aa2efa2cf3`, under the pair of this cell, which lists every file in the live-to-cut diff. **I measured that diff: 35 files under `infra/aws/ec2/opal-gateway/` (`git diff --name-status aa2efa2cf3 origin/CLOUD`), of which 7 are ours** (`app/harvest_research.py`, `harvest_figures.py`, `harvest_identity.py`, `harvest_keys.py` NEW, `tests/test_cj2_slash_key_one_form.py`, `tests/test_cj6_slash_key_other_tools.py`, `tests/fixtures/cj2_continuation_keys.txt`); the other 28 include `server.py`, `destructive_ops.py`, `family_depth.py`, `probe_listener.py`, `admin_people_access.py`, `refs/partner_roster.json` and `refs/silver_families.json`. The three modified files are md5-equal at `aa2efa2cf3` and at the pre-change base `845b69a8cc` (`596c299597067fe5a8afb8e3493a0ed9`, `610eb6862918d2c6695c10d2de58734f`, `9c8d1fd69ffe0594968b4acd2751fba9`), so they apply clean on the live commit. **I asked the CTO (one ask, REC yes) whether the release is cut on `aa2efa2cf3` plus those 7 files only (as `cg-3` was), instead of the CLOUD tip.** `cj-3` is not written until he answers.

| cell | order | what | class | executes | state |
|---|---|---|---|---|---|
| `HVST-cj-3` | -- | ONE gateway release carrying `cj-2` and `cj-6`, `DEPLOY_BASE_REF=aa2efa2cf3`, under its own pair, with the served reads of `BP/_LN_Equity` and `NG/_LN_Equity` in both spellings (the disarm test of the ARMED rows `D1-W171-S1` and `-S5`). | WORLD | seat SC1 | DEFINED, NOT CUT: waits on the CTO's answer on the cut and on SC1 being free (`HVST-cj-4` runs to about 11:35Z) |
| `HVST-cj-5` | -- | The two slash-key dossiers under the same pair shape as `cj-4`. | WORLD | seat SC1 | DEFINED, NOT CUT: waits on `cj-3` released and read |

- **Fan-out:** none this recut (no cuttable cell without an unmet dependency; `cj-4` runs).
- **ARMED rows open (disarm owner me):** `D1-W171-S1`, `-S3`, `-S4`, `-S5`, `-S6`.
