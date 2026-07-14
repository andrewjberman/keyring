# CTO session part 3 — OPAL_ASSETS refinement → OPAL_RUNNERS, the Schwab + SmartX ETL, and the end-to-end monolith

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**Serial:** 1.0.0_SA_CTO · **Date:** 2026-07-14 · **Window:** since part-2 log `94a1f4a89` (PRD v1.3.4) → C5 dispatch (`9c7f234c0`)
**Continues:** `session_CTO_opal_assets_ownership...` (part 1) + `session_CTO_part2_monolith_rulings...` (part 2)

## What this window did, in one paragraph
Refined OPAL_ASSETS from a design into a LIVE, accruing monolith (`opal-data-assets` exists,
`opal-assets-v0.4.0`), drove the C-series through their gates, stood up OPAL_RUNNERS as the successor
project with the 49F refactor case study as its centerpiece, and — on Andrew's HAR captures — designed
and dispatched the SmartX holdings-activity ETL (C5). The through-line Andrew set: **the monolith must
be truly end-to-end contained and robust — day-to-day AND backfill, in pattern.**

## Rulings + gates issued this window (all committed, see hashes)
- **PRD v1.3.4–v1.5.0** (`f8ea5725d`…`0cf9e2b80`): 01_raw carve-out (257 pre-floor incl. 121 RLD tax files
  MIGRATE, ruled by Andrew), SSE reversal (deny dropped, 0.7.0's HCL stands), Glacier restore (BULK,
  background-fill per Andrew's priority inversion), TRN_NNA ruled GOLD-tier (5 raw silver types), the C2
  orion FLAT-generation map + the 3 legacy prefixes' 257-treatment, ruling 17 no-noncurrent-expiry, and
  **§4b THE POPULATION CAMPAIGN** (bronze+silver completely locked up, per-channel).
- **THE MONOLITH IS LIVE** (`cb153456c`): C1 closed on COO's independent live-AWS verify (SSE AES256,
  versioning, 10 probe objects, opal-assets-v0.4.0); C2/C3(c)/C4 applied; the fence (router cannot write
  its sources, box cannot read the monolith) exercised twice.
- **OPAL_RUNNERS PRD v0.1→v0.3** (`5999d7fc2`, `cb153456c`, `a44ba24a4`, `797a3213a`): registered;
  W1 census corrected (176 gold scripts not 248, 29/176 unmapped); **W4 falsifier FIRED** — the 49F
  role/fee model is BD-sourced, Andrew ruled "0833 + ONE scoped BD advisor dim daily."
- **SmartX** (`ad8036d3c`, `560174501`, `797a3213a`, `9c7f234c0`): three yaliu HARs investigated →
  findings deliverable → **C5 ETL TO dispatched to 0.5.0**.
- **C2 corruption** (by message, not yet committed): the "stall" was a type-collapse key collision; my
  (a)+(b)-as-fix framing WITHDRAWN; real fix (preserve {type} + assert distinct-landings) ratified; the
  distinct-landing-not-write-count lesson elevated to a doctrine-level audit of every conservation guard.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| `aws s3 ls --recursive` (operational) | 0824/0833 bronze verifies (324, 6,932); SmartX-v2 exports census (1,386/95MB); 01_raw enumeration | PASS | live-primitive grounding, denominators printed, never producer self-report |
| Python HAR parse (scratchpad) | 3 yaliu HARs (494/728/881 entries) → endpoint census + response-shape probe | PASS | the SmartX endpoint surface + the 16-mo ledger fetch-mechanism confirmed on bytes |
| `git log`/`Grep`/`Read` | PRD/deliverable edits, header locators | PASS | native tools; HARs held in scratchpad (live tokens, never committed) |
**What worked:** grounding every SmartX claim on HAR bytes (not D4 recollection) caught that HAR#1's
surface ≠ HAR#2/3's (activity ledger only appeared in #2). **What failed:** index-lock contention on 3
commits (other agents mid-commit) — waited it out, never touched the lock; one `-m` backtick-gate block
(corrected to `-F` heredoc). **Gap:** the C2 write-count guard passed a collision — every conservation
guard in the consolidation now needs a distinct-landing audit (folded into the connector-sweep rubric).

## MCP traffic (window)
~30 messages handled. Significant: C1/C2/C3(c)/C4/RestoreObject apply gates ruled; C5 GO to 0.5.0;
DS provenance-trace GO + 49F-fork close; C2 stall-escalation ruled (real fix + doctrine); the four
sovereign-lift reads ruled (advisor-NNA verify, D2 scoping, 49F runner, held-lib); basis-label fix folded.

## CURRENT STATE (zero-context handoff surface)
**The monolith `opal-data-assets` is LIVE** (`opal-assets-v0.4.0`, us-east-1, SSE-S3/AES256, versioned,
no noncurrent-expiry). Grammar: `{source}/{scope}/{layer}/{feed}/{date}/`. Serving layer UNTOUCHED
(gold runners/platinum stay put — that is the end-state boundary).

**Schwab ETL (0.6.2 lane):** 0833 migrated (6,932, 13c-clean). 0824 wide pull running (~4,055/5,966).
C3(c) = BOTH-masters daily REST schedule APPLIED (0833 cron(45 9,21), 0824 cron(15 10,22), staggered
30min, shared events-ssm role, session-lock refuse-on-contention BUILT). 01_raw 257 pre-floor migrate
via C3 (217 Glacier → BULK restore, background). Live per-master exercise waits on SDD-session-free.

**SmartX ETL (0.5.0 lane — C5, `9c7f234c0`, GO'd, DESIGN-GATE PENDING to me):** grain =
(account|model)×symbol×day in `opal-data-assets/smartx/`; 8-feed bronze/silver map grounded on the yaliu
HARs; account activity = full 16-mo ledger in ONE unparameterized GET; auth bundle → Secrets Manager
(Andrew-direct §3a); distinct-landing guard required; backfill is a bounded resumable process (not 900s
Lambda). **0.5.0 authoring the design note now; NO bronze bytes until I rule the key mapping.** ETF
parity day-2 (22:00Z) outranks C5.

**Other channels:** ETF C4 retargeted (first bronze on tonight's 22:00Z run). Orion/Eclipse/cot C2
polling mirror LIVE but **first-run backfill is CORRUPT (type-collapse)** — corrected fix (preserve
{type} + distinct-landing guard) at my gate; the 2,269 corrupt orphans are a deletion decision routed
to Andrew (source intact, re-derivable, zero loss). Eclipse/cot mirrored correctly.

**OPAL_RUNNERS:** registered, PRD v0.3. 49F premise LOCKED as "0833 + one scoped BD advisor-role/fee dim
daily." W1 census done (176 gold scripts, disposition in progress). Build gates on the (now-lifted) 49F
block; the casebook method (layer-by-layer 49F decomposition) is the sec-4 centerpiece.

**Sovereign state:** 49F/Schwab/bd DOMAIN BLOCK LIFTED (Andrew ~03:3xZ, verification DEMANDED). INF hold
STANDS (Door 5/6, frozen-3, never-summed, 17a — all untouched). SmartX egress lifted (standing).

## NEXT STEPS (the handoff Andrew asked for — refining OPAL_ASSETS into OPAL_RUNNERS, end-to-end contained + robust, in pattern)

### A. FINISH LOCKING THE MONOLITH DAY-TO-DAY (OPAL_ASSETS close-out) [1.0.0_SA_CTO owns; lanes as noted]
1. **C2 corrupted mirror — close the loop:** gate 0.7.0's corrected fix (preserve {type} + distinct-landing
   assertion, exercised against a synthetic collision); get Andrew's deletion call on the 2,269 orphans;
   re-mirror to convergence; verify type-distinctness on landed bytes. **[0.7.0_AE_CloudOps → CTO gate]**
2. **C3(c) Schwab daily — verify first real fires:** both masters' 09:45+/10:15+ UTC schedules land bronze;
   the session-lock refuses-loud on the first natural overlap; 13c + partition list per master. **[0.6.2]**
3. **C6 silver population (§4b P-2):** DS runs backfill conversions over EVERY landed bronze tree until
   parquet exists for every partition held, then the daily event-wiring carries it. The distinct-landing
   audit applies to the parser conservation too. **[0.4.0_DS]**
4. **C11 emitter → one-bucket-only + the DDB cohort rows** (0833 + Cottonwood-AUA), gated on C3+C6. **[0.4.0_DS]**
5. **The ligament assessment (§4b P-3):** every EventBridge-trigger→Lambda-writer connector at BOTH layers
   (bronze scheduled + silver event) gets the four verdicts (fire/run/land/verify), read-only, trading-
   calendar-resolved, printed denominators. This IS "extremely covered on writes/pulls." **[COO commissions; CTO gates forks]**
6. **C12 legacy inventory + retirements** (opal-data-schwab staging, opal-data-smartx-v2, the 3 legacy orion
   prefixes' 257-treatment, 01_raw sequence) — inventory only, deletions are Andrew-confirm. **[0.4.0_DS doc]**

### B. THE SMARTX ETL — carry it to fully-contained (in pattern) [0.5.0 builds; CTO gates]
1. **The design gate** (imminent): rule the 8-feed key-mapping grammar + the distinct-landing set-identity
   contract BEFORE any at-scale pull. This is the permanent-in-bronze decision.
2. **Backfill in pattern:** the 3 append-only feeds (activity/performance/changerequests) = one pull each to
   the vendor-stated floor; the snapshot feeds accrue-forward. The 1,386 GUI-era exports mirror channel-
   labeled as a separate step. **The one open probe** (holdings screen with an as-of date change) closes
   whether per-holding daily QUANTITY becomes a direct pull vs a gold reconstruction — worth one more capture.
3. **Auth bundle in Secrets Manager** (Andrew-direct): the credential/JWT/refresh/cookie-slot lifecycle,
   opal-data-bd JWT co-park retired, grants pinned + 22a-verified, expired→re-mint-loud.
4. **The credential-grant decision is Andrew's:** yaliu (higher-grant, Yang's personal) vs a dedicated
   service login. Build stays credential-configurable until he rules.
5. **SmartX GOLD (later TO, NOT C5):** the model-summary rollup + the AdvI model-specific client views +
   the DDB cohort row. C5 delivers bronze+silver only.

### C. THE BRIDGE INTO OPAL_RUNNERS (the analytics runners) [CTO designs; build gates on Andrew's word]
1. **The 49F casebook** — layer-by-layer decomposition of the damaged legacy 49F gold runner into THE
   CANONICAL FORM CASEBOOK (the doc the lighter Inflection/Cottonwood runners build against). Now a LIVE
   refactor target (block lifted), not read-only archaeology. Premise locked: **0833 + one scoped BD
   advisor-role/fee dim daily** — I bind the exact dim + wiring at the sec-4.3 lock; that daily BD read
   becomes a new ligament in the sweep.
2. **The group A/B/C/D contracts** (contracts-only canonicalization, script forks stay) — validated against
   all four implementations (bd/cot/inf/canonical-schwab); the 29 unmapped scripts get named dispositions.
3. **Incremental-by-design** (≤$100/mo per box, rust/polars for heavy tables) — the antithesis of the
   c6i.16xlarge full-recompute the 49F casebook exists to kill. The GLDINC shadow-cache is the engine seed.
4. **Runner topology** (partner-level EC2, reads-only monolith silver, D-group writes platinum) + the
   channel-box ingest pattern (auth bundles in Secrets Manager — the same §3a pattern generalizes to the
   Schwab/BD channel boxes). W2/W3/W5 assessments feed this.

### D. STANDING / PARKED (mine, not tonight's work)
- The `send_message` forgery gate (2 accidental forgeries, self-reported — one-line fix using the existing
  identity guard); the gate-candidate batch for Andrew's nod (reset-HEAD~1-in-shared-worktree, the >100MB
  commit-gate check 0.5.0 is building, doctrine notes). HALTGT latch repair. MEMORY.md line-cap compaction.

**The design principle threading all of it (Andrew, this session):** every layer has one job; the monolith
stores COMPLETE (never Opal-filtered — the emitter/runner is the one parse-down point); backfill and daily
share ONE pattern per channel (append-only = one pull + dedup; snapshot = accrue-forward); and every
conservation guard asserts on the REAL landed property (distinct keys / set-identity), never a proxy.

## POST-LOG ADDENDUM (work after this log's commit 85896c6ca)
**The C5 SmartX design gate: PASSED.** 0.5.0's design note (`a2f02123a`,
`deliverables/SMARTX_C5_INGEST_DESIGN_NOTE_20260714.md`) authored toward the gate; all 6 decisions ruled
(by message, no PRD change needed — the rulings bind the TO/design):
- **Q1 [PERMANENT] — reportedModelId is the model path key** for ALL FOUR model feeds incl. performance
  (modelId = fetch-param + recorded field ONLY, never a path segment). Closes the two-UUID-space collision
  (`models/{id}/performance` fetched by modelId vs siblings by reportedModelId) — the exact "one entity,
  two path roots" C2 class. **This is the permanent-in-bronze key decision; locked.**
- **Q2 — 2-segment per-entity scope is IN-GRAMMAR** for SmartX (`model/{rmid}`, `account/{acctId}`,
  `platform`) — still `{source}/{scope}/{layer}/{feed}/{date}`, scope is compound because SmartX's scope
  IS the entity id (897 models / 452 accounts), unlike C4's single-token ETF scope. Documented as deliberate.
- **Q3 — fold the holdings `?asOf` probe read-and-record** in backfill pass 1, NON-load-bearing
  (accrue-forward is the default; a prior-date snapshot only ADDS a dated pull, never blocks).
- **Q4** credential = Andrew's (build configurable, flag exercised grant). **Q5** gui-era exports OUT
  (separate step). **Q6** bronze pull != gold re-derive, on the record — operator-driven resumable
  S3-checkpointed backfill legitimate; daily on the extended `smartx-rest-pull` Lambda.
- **THE GUARD, ratified as the reference template:** 0.5.0's set-identity check (landed-keys ==
  enumerated-targets, **RAISE on shortfall OR SURPLUS**, verdict on ListObjectsV2 bytes, mutant-exercised
  on both a collision AND a surplus key) is BETTER than I specified — surplus detection catches a
  stray/duplicate write a shortfall-only check misses. **Now the reference pattern for the C2 fix + the
  connector-sweep conservation audit.**

**0.5.0 build order (RAVC-closed, building now, idle-hours):** (1) the distinct-landing GUARD FIRST —
self-contained, mutant-exercised, no bronze byte until it RAISES on its collision + surplus mutants;
(2) auth-bundle retrieval module (reuse `smartx-jwt-refresher`); (3) name exact `smartx/*` +
`opal-data-assets/smartx/*` ARNs → MCP 0.7.0 for grants AGAINST the ruled key mapping; (4) backfill
append-only feeds first, then snapshot accrual, then silver. Parity day-2 (22:00Z) preempts without asking.
**This updates NEXT STEPS §B.1 (the design gate) to DONE — B.2–B.5 remain.** Next contact from 0.5.0:
the `?asOf` probe result or an architecture fork.
