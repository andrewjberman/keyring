# THE CANONICAL-FORM REFACTOR + LEGACY DECOMMISSIONING SPEC -- mdpf + advi

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0715-0740Z** · **archetype:** IMPLEMENT (design) + TRACE
**Commission (Andrew-direct at this terminal):** validate the canonical five-layer form (bronze raw
-> event-driven silver parquet -> GOLD PARQUET at `opal-data-assets/portal/gold/{mdpf,advi}/{global|firm}`
-> platinum publisher rendering JSON for the portal), and cross-reference against the measured
legacy channels so implementation knows every repoint. **Verifier: 3.0.0_SA_CVO** (their 49F
A/B/C/D+W specs are the archetype substrate; ~A derives INF/COT). Consumers: CTO (matrix/arch),
COO (decomposition).
**Grounding registry:** RECON-1 @41692cd3d2 (mdpf, CERTIFIED @cc62267d89) · RECON-4
@be316d868c+addenda (identity, CERTIFIED @4918e8b48f/@da62a742c5/@fca75880f7) · the GIPS run
@e323c1cfac · task-1 @a876ee6ae9 + engine @5bb3b2626d · CVO 49F specs (A@9c294bbf15..D@1e11389af8,
W) · ~A's ADVREVIEW + INF shape spec · MDPF_DEBTCLEAN_PRD (Andrew verbatim on the gold root :830) ·
pattern spec v1.0 @d272021791 (LAW: 9 atoms, thin-adapter, event-driven L2). Every legacy claim
below carries its RECON citation -- nothing re-derived from belief.

---

## 1. THE TARGET FORM, VALIDATED -- five layers, one contract each

| L | Layer | Contract | Validation verdict |
|---|---|---|---|
| L1 | **Ingestion -> BRONZE, raw** | `opal-data-assets/{vendor}/{firm}/bronze/` -- byte-faithful vendor delivery (Rule 17a; parquet is NEVER bronze) | **VALID + already live for the conformant trees** (schwab/08335338, blackdiamond/cottonwood, smartx/platform measured landing daily) |
| L2 | **Event-driven bronze->silver** | S3 ObjectCreated on bronze landing -> converter -> `{vendor}/{firm}/silver/{table}/date=D/data.parquet` (dedup+dtype only, Rule 17) | **VALID = RATIFIED LAW** (@d272021791 L2 event-driven). Schedule-floor law composes: an event ACCELERATES, a clock FLOORS (the dead-sentinel lesson, RECON-1 delta row 4 -- a chain whose ONLY trigger is another pipeline's success is the measured 9-day freeze class). Every L2 leg declares pack-01's A1-A5 per the Group-W discipline |
| L3 | **GOLD = PARQUET** at `portal/gold/{product}/{scope}/` | analytics tables derived from silver, **parquet not JSON** -- see §1a | **ADOPT -- assessed feasible and actively simplifying** (§1a); ONE naming act to close formally (§1b) |
| L4 | **PLATINUM PUBLISHER** -- the ONLY JSON producer | reads gold parquet, renders served JSON into `opal-data-portal-v2/platinum/{product}/{scope}/` (17b's serving tier), hyphen spelling, schedule floor, one publisher per product | **VALID + the live mdpf publisher already has this shape** (13:50Z daily, hyphenated per-firm keys -- RECON-1; input format is the repoint) |
| L5 | **Portal reads platinum only** | FE/proxy -> platinum keys | **VALID = measured today for mdpf** (RECON-1: the proxy reads portal-v2; no direct-gold portal read found) |

### 1a. The gold-parquet question ("I am curious if..."): YES -- and it retires two standing hazards

**Mechanics:** gold tables land as `portal/gold/{product}/{scope}/{table}/date=D/data.parquet`
(the same partition grammar as silver -- one grammar, three tiers), plus `_manifests/` (the
consolidator's existing manifest discipline transposes) and `_code/` (pattern atom 2). Agents query
gold directly with DuckDB/pandas/pyarrow over S3 -- schema'd, columnar, partition-pruned: the
agentic-friendly property is real and immediate (the Kimi/comp-estate entry layer reads tables, not
JSON blobs). The consolidator's put-with-readback + version-guard semantics PORT to the parquet
writes (named port task -- the downgrade-refusal guard at mdpf_aggregate_aua:1315 is the pattern).

**It retires two standing hazards, structurally:**
1. **The spelling-law trap dissolves at the gold tier.** Today's guarded set exists because gold
   spells JSON families with `_` while platinum serves `-` (the account-distribution bell class,
   MEMORY-guarded). With gold as parquet TABLES, there are no gold JSON filename families to
   confuse with served ones -- the hyphen/underscore law collapses to ONE boundary (inside the
   publisher), which is where it always belonged.
2. **The two-writer JSON surface ends.** Today consolidator + accrual + aum-metrics emitters all
   write gold JSONs (three writers, one prefix -- RECON-1). Under the target form they become gold
   TABLE builders and the publisher is the only JSON producer -- the one-producer-per-served-key
   law (the 07-23 ruling) becomes enforceable by construction.

**Flags for CVO's verify (stated, not hidden):** (i) Group D was specced shape-frozen "up to the
emitters" -- its emitters must be confirmed as PUBLISHER LEGS consuming C-canonicals-as-parquet
(a format assumption inside D, one cell to check); (ii) comp-freshness / comp-estate entries keyed
on today's gold JSON keys re-key to parquet partitions (config repoint, enumerable); (iii) any
gold-JSON consumer outside the publisher that my census missed -- the comp-find sweep (411 hits,
code band) found writers + publisher + records only, but CVO's independent re-derivation is the
control.

### 1b. The ONE naming act to close (F-1 of ~A's review, reconciled -- surfaced, not adjudicated)

Rule 17b's grammar is `{vendor}/{firm}/{medallion}` with 17b's own census marking top-level
`portal/` as non-conforming residue; ~A's F-1 flagged Group A's product-root default on exactly
that. **Andrew has now stated the product-root form three times** (the third framing @043954Z, the
DEBTCLEAN PRD's verbatim ":830 -- all /mdpf assets under portal/gold/mdpf", and today's commission
naming `portal/gold/{mdpf and advi}/{global or firm}`). This spec therefore builds on the
product-root form as the operative direction, and asks for **one ratification line from Andrew**
("`opal-data-assets/portal/gold/{product}/{scope}` is the canonical GOLD home; 17b's vendor-tree
grammar governs bronze+silver; platinum stays in opal-data-portal-v2") -- a Rule-24 naming act
that retires F-1 formally instead of leaving the two records in tension. **Vendor trees keep
bronze+silver (17b intact); the product tree holds gold+serving-prep: ingestion is vendor-shaped,
analytics are product-shaped -- that split is the coherent reading of both records.**

### 1c. THE NAMING DECISION, REFINED (Andrew ~0750Z: "ok with product gold and silver in
### opal-data-portal-v2, however... we should be consistent with mdpf") -- TWO COHERENT END-STATES

His consistency constraint is the load-bearing one: whichever bucket holds product gold holds it
for BOTH products. The two coherent forms, measured:

**OPTION A -- product tiers in opal-data-assets (the spec's current form).**
`opal-data-assets/portal/gold/{mdpf,advi}/{scope}/` (+ product intermediates beneath the product
root); `opal-data-portal-v2` = SERVING ONLY (platinum + the legacy json families it already has).
Bucket law: **assets-bucket holds ALL assets (vendor medallions + product analytics); portal-v2
converges toward serving-only.** COSTS: zero mdpf migration (it is already there: 80 objects,
_code, _manifests, the accrual grammar, the 08-07-simulated IAM wildcard grant, the DEBTCLEAN
consolidation table + pocketed mdpf_revamp relocation all TARGET this root); 17b amended by one
line (the portal/ subtree ratified as the product-gold home). ADVI simply JOINS mdpf.

**OPTION B -- product tiers in opal-data-portal-v2.**
`opal-data-portal-v2/gold/{mdpf,advi}/{scope}/` + platinum beside it. Bucket law: **assets-bucket =
vendor-shaped tiers (bronze/silver), portal-v2 = product-shaped tiers (gold + platinum)** -- the
bucket boundary becomes the vendor->product transformation boundary, which is conceptually clean.
COSTS, measured: (i) the mdpf CONSISTENCY MOVE he names -- 80 objects is trivial but ~7
writer/grant/record surfaces re-point AGAIN (consolidator A4_PREFIX, accrual grammar, aum-metrics,
publisher read, the fresh IAM wildcard grant re-granted on portal-v2, DEBTCLEAN consolidation
table + the pocketed brief re-targeted, CVO's A4 contract row) -- re-doing this month's landings;
(ii) 17b's ratified "ALL assets housed in opal-data-assets" takes a larger amendment than Option
A's; (iii) **the security-shape cost, the one that does not wash out: every gold BUILDER becomes a
WRITER on the client-serving bucket.** Today portal-v2's write surface is publishers (plus legacy
residue) and its IAM carries deliberate serving-protection denies (the runner explicit-deny on
json/portfolios/* is live, measured in the 08-06 failure log). Option A keeps the serving bucket's
writer set minimal; Option B enlarges it by the whole builder population. (iv) portal-v2 today is
MEASURED as 27 mixed top-level prefixes (assets/, raw/, lambda-packages/, json/, platinum/...) --
Option B cements the mixed state; Option A lets portal-v2 converge to serving-only as legacy
retires.

**RECOMMENDATION: OPTION A.** Consistency is satisfied by advi JOINING mdpf where mdpf already
lives; zero re-migration; the serving bucket's write surface stays minimal; 17b needs the smaller
amendment; portal-v2 gets a convergence path instead of a cemented mix. "Product silver": vendor
silver stays in vendor trees under EITHER option (17b intact, live, conformant); product-scoped
INTERMEDIATES (the ex-feeds class) live under the product gold root in whichever bucket wins.
**RULED ~0754Z, ANDREW-DIRECT VERBATIM: "Option A, proceed."** THE NAMING ACT IS CLOSED:
`opal-data-assets/portal/gold/{product}/{scope}` is the canonical gold home; vendor trees keep
bronze+silver; `opal-data-portal-v2` is the serving tier and converges toward serving-only; advi
JOINS mdpf. ~A's F-1 is formally retired (Group A's product-root default now stands RULED, not
defaulted). **The Rule-17b one-line amendment is a LAW-SURFACE edit and routes to CTO** (law
surfaces land only via main CTO); the ruling recorded here is its authority. Sec1b's
draft ratification line is superseded by this ruling.

## 2. THE LEGACY INVENTORY + DISPOSITIONS (every row cites its measurement)

**Disposition enum:** REPOINT (consumer moves to canonical read) · FOLD (artifact moves into the
product tree) · REBUILD (function survives, mechanism replaced) · RETIRE (function ends; delete
after drain) · PARKED-INHERITED (existing Andrew park, untouched here). **Gates carried:**
opal-data-mdpf deletion = T5.B+CTO "migrate before kill" (kill-list); any served-key move =
never-widen CTO+COO; `json/mdpf/*` = PARKED (Andrew; the hyphen bell + guarded set).

### 2a. MDPF legacy channels

| # | Channel (measured state) | Disposition | Precondition |
|---|---|---|---|
| M1 | **opal-data-mdpf/mdpf/feeds/** -- 6 feeds; 3 written by cron lambdas (live nightly), 3 by the dark EC2 chain (frozen 08-06) [RECON-1] | **REBUILD-THEN-RETIRE: per-feed.** Feeds are gold-tier intermediates; each either (a) DISSOLVES into direct silver reads by the gold builders (model_aua_positions' content already lands as smartx silver -- fact_allocation_account_map + model tables, MEASURED), or (b) lands as a gold parquet table in the product tree. Per-feed disposition table = a named COO decomposition input, drafted from RECON-1's feed schemas | the smartx-silver equivalence check per feed (cheap, at-rest) |
| M2 | **wsb/wsd cron lambdas** -- hardcoded bucket writes [RECON-1: wsb:65,248] | **REPOINT** writes to the canonical home chosen per M1; env-indirected this time (the hardcode is the measured anti-pattern) | M1 per-feed call |
| M3 | **EC2 main chain** (sentinel-dead trigger; 7+ stages; 2 IAM-severed) [RECON-1] | **REBUILD as the canonical event chain:** L2 conversions event-driven off bronze; gold builders event-driven off silver WITH the W3 ruled clock as floor; the two IAM-dead stages RETIRE now (already severed -- deleting dead stage code is not a serving move) | Group-W wiring spec instantiated for mdpf |
| M4 | **Accrual bridge** (daily 13:40Z; reads partner_roster FROM code store) [RECON-1] | **REBUILD:** becomes a gold parquet builder; partner_roster moves OUT of the code store into a gold reference table (pattern atom 6: config never lives in code) | none -- self-contained |
| M5 | **Floor consolidator** (reads assets-native silver/gold + mdpf_revamp staging; writes gold JSONs + _manifests) [RECON-1] | **REBUILD:** same reads, parquet writes; version-guard ported; _manifests discipline kept verbatim | gold-parquet layout ratified (§1b) |
| M6 | **gold/mdpf_revamp staging** (outside the product root) [RECON-1 Part B atom-4 violation] | **FOLD** into `portal/gold/mdpf/_aggregate_aua/` -- ALIGNS with the POCKETED retirement brief @76d4ba532 (already decided, pocketed) | unpocket the brief; consolidator repoint same window |
| M7 | **Platinum publisher** (live 13:50Z, hyphenated per-firm platinum keys) [RECON-1] | **REPOINT input** gold-JSON -> gold-parquet; otherwise UNCHANGED -- it already IS the L4 of the target form | M5 lands first (no shadow: publisher flips input in the same port window, one cutover, rollback = re-point back) |
| M8 | **smartx readers** (compute_account_distribution + per-firm + timeseries; read mdpf/feeds hardcoded) [RECON-1] | **REPOINT** reads to smartx canonical silver (the same content, measured landing daily) | per-feed equivalence (M1); the per-firm bells are CLIENT-FACING -- never-widen co-sign on the repoint window |
| M9 | **opal-data-mdpf/code/** store + DS deploy map (safe_deploy_core:103) + pipeline_cli special layout + EC2 sync --delete [RECON-1] | **REPOINT** deploy target to the product `_code/` home (atom 2); pipeline_cli's special-case layout RETIRES with it | M3's rebuild defines the runtime set first |
| M10 | **telemetry/ + bmkaud-evidence/ + cache/** [RECON-1 census] | **RETIRE:** archive telemetry to the product tree's `_runlogs/` convention (08335338 already models it); evidence/cache reviewed-then-deleted | T5.B window |
| M11 | **json/mdpf/* serving incl. account-distribution bells** (per-firm LIVE 08-10; flat frozen 07-23) [RECON-1/4] | **PARKED-INHERITED** -- Andrew's park stands; the target-form successor is the platinum publisher rendering these families, and the park lifts only on his word with never-widen co-sign. This spec stages the successor; it does NOT touch the park | Andrew word; ETFS CANON (the recorded park reason) |
| M12 | **opal-data-mdpf bucket itself** | **RETIRE-WHOLE after M1-M10 drain** -- the kill-list's own gate (T5.B + CTO, "migrate before kill") is the deletion act's home; this spec supplies the migrate half | every M-row above CLOSED + negative probes (the standard drain discipline) |

### 2b. ADVI legacy channels

| # | Channel (measured state) | Disposition | Precondition |
|---|---|---|---|
| A1 | **08335338 root FLAT residue** (canonical/, dimensions/, dim_*, fact_* beside the medallion) [RECON-4 window listing] | **FOLD-OR-RETIRE per prefix:** the medallion (bronze/silver/gold) is canonical; the flat twins get a per-prefix census (live-writer? consumer?) then fold or delete. ~A's instruction-4 EXTRACT/DISCARD partition of runners_49f is the sibling act | one listing + writer census per prefix |
| A2 | **runners_49f corpus** (a00/a01 + c00-c04 + fit harness) [CVO handoff] | **REBUILD = the A/B/C/D specs themselves** -- the archetype REPLACES the corpus; legacy runners RETIRE on the port protocol (build-correct, port, drain, delete) after the new runner's acceptance batteries pass | the specs' own gates; COO decomposition |
| A3 | **INF chain** (opal-data-inf medallion + gold dims + publishers + sentinel) [~A's INF spec + RECON-3 substrate] | **REBUILD per ~A's INF A/B/C/D+W** (their spec IS the plan); the pipeline-complete sentinel chain gains the schedule-floor law (the dead-sentinel class measured twice tonight); INFLECTION_REP_IDS allowlist RETIRES (~A: a Group-A precondition, the fork's measured breaker) | ~A's specs through CTO review |
| A4 | **INF publishers** (inf-portal-publisher + advisor-publisher; live delivery) [~A GROUP D] | **REPOINT input to gold parquet when INF's gold ports; the chain itself stays untouched in v1** (~A's own port protocol) | INF Group D census (D_00 first act) |
| A5 | **COT/BD ingest** (blackdiamond/cottonwood 3-tier, daily, CONFORMANT) [RECON-4 addendum] | **KEEP -- it already matches the target form** (bronze raw + silver parquet + gold dim, event-marked daily). It is the estate's existence proof of L1-L3; only its gold layer re-homes to the product tree under the §1b naming act | the naming act |
| A6 | **json/* advi serving under opal-data-portal-v2** (platinum/firm + advisors families) [~A GROUP D census] | **REPOINT to publisher-rendered platinum on the port protocol, family by family, shape-frozen** (D's byte-schema discipline); never-widen on every served family | ~A's D_00 census per family |
| A7 | **bd-49f-runner** (lag=1, env-config) [RECON-1 U-row] | **RETIRE into the archetype** (its function = a Group-A/B leg); disposition confirmed at ~A's quality partition | A2 |

## 3. THE REPOINT MAP -- consumer edges, current -> target (implementation grade)

| Consumer | Reads today (measured) | Reads under target form | Wave |
|---|---|---|---|
| Platinum publisher (mdpf) | portal/gold/mdpf/*.json | portal/gold/mdpf/{scope}/{table}/ parquet | P2 |
| smartx acct-distribution producers | opal-data-mdpf/mdpf/feeds/model_aua_positions | smartx/platform/silver model tables (equivalence-checked) | P2 (never-widen: client-facing bells) |
| smartx timeseries | feeds/model_aua_positions + non_model_aua | smartx silver + the non_model gold table (M1 call) | P2 |
| mdpf gold builders (consolidator/accrual/aum-metrics) | silver + mdpf_revamp staging + partner_roster-in-code | assets silver + portal/gold/mdpf/_aggregate_aua + gold reference table | P1 |
| DS deploys (safe_deploy_core mdpf row) | opal-data-mdpf/code/ | portal/gold/mdpf/_code/ | P3 |
| EC2 runners (both legs) | code sync --delete from opal-data-mdpf | _code/ home, rebuilt triggers (floor+events) | P1-P3 |
| comp-freshness / comp-estate entries | gold JSON keys | parquet partition keys (config re-key, enumerable) | P2 |
| INF publishers | opal-data-inf gold JSONs | INF gold parquet (when INF ports) | per ~A |
| Portal FE/proxy | platinum (already) | platinum (unchanged) | none |

## 4. SEQUENCING -- build-correct-and-port-over; NO shadow channels, NO standing comparators

**P0 (now):** the §1b naming line at Andrew · CVO verify of this spec · Group-W instantiation for
mdpf (the scheduling atoms per leg). **P1:** gold builders REBUILT parquet-writing into the
ratified layout (validation = tests + ad-hoc QA runs, run-and-read, nothing standing) -- behind
the MDPF remediation waves' completion (the W-waves continue UNTOUCHED; this form is their
successor, not their competitor). **P2:** the port window -- publisher input flip + smartx repoints
+ config re-keys, one cutover per consumer family, same-window rollback, never-widen co-signs on
client-facing families. **P3:** deploy-plane repoint (DS map, _code home) + M10 archive.
**P4:** drains + negative probes + the T5.B deletion act (opal-data-mdpf) and A1 residue deletes.
**Advi runs on ~A's spec sequence through the same P-gates, one firm at a time (INF then COT per
Andrew's archetype-then-replicate order).**

## 5. WHAT THIS SPEC DOES NOT DO

No dispatch, no gates minted, no serving key touched, no park lifted, no remediation wave altered,
no deletion executed (T5.B owns the kill act; this spec is its migrate-before-kill half). The
INF/COT builds belong to ~A's specs; the archetype builds to the A/B/C/D sequence; decomposition
to COO at the archetype trigger.

## 6. CVO VERIFICATION HOOKS (where to attack first)

(1) §1a's "no gold-JSON consumer outside the publisher" -- re-derive the consumer census
independently (my sweep: comp-find 411 hits, code band = writers + publisher + records). (2) M1's
per-feed silver-equivalence claims -- the smartx model tables' content-parity vs the feeds is
asserted-from-schemas, one diff each at rest. (3) M8's repoint safety -- the bells are
client-facing; the equivalence check IS the never-widen evidence. (4) The Group-D emitter-format
cell (§1a flag i). (5) Every RECON citation resolves at its commit -- the certified runs carry the
cells. (6) The sequencing's no-shadow compliance -- each port is flip+rollback, nothing parallel;
attack any row that smells like a standing second channel.

## 7. CVO VERIFY FOLDED (VERIFIED-WITH-AMENDMENTS @4e02646c97 -- zero dispositions refused; four amendments adopted verbatim)

**A1 (MEASURED, folds into M7): "the publisher" is a FAMILY OF TWO.** The live same-bucket
publisher AND `mdpf_egress_publisher.tf` -- the cross-bucket successor reading `portal/gold/mdpf/*`,
wo2 repoint in-flight (.open_deploys). CVO's re-derived census (417 hits / 25,251 files, 34
non-doc files fully classified) confirms NO consumer outside the family. **M7 amends: both members
named; the parquet format flip SEQUENCES WITH the wo2 transition as ONE ordered act** -- never two
overlapping input changes on the publisher family.

**A2 (MEASURED, replaces the M1 method): the one-at-rest-diff-each equivalence method is REFUSED AS
STATED.** CVO ran it on the headline feed: coverage ties, totals tie 0.237 percent, row-wise 0.12
percent -- and the SAME-STATE pair is STRUCTURALLY UNAVAILABLE at rest (weekend map partition
EMPTY; channels pull 03:31Z Tue-Sat vs 13:55Z daily -- different clocks, never the same state).
**M1's equivalence checks amend to: SAME-STATE PAIRED PULLS in one window, or an EX-ANTE tolerance
frame ruled before the diff runs.** A diff whose divergence is indistinguishable from one
trading-day of drift proves nothing either way.

**A3 (folds into M8): the bell repoint's never-widen evidence inherits A2 with stakes.** A
client-facing co-sign cannot rest on a diff that a weekend of market movement would also produce --
M8's precondition is now the SAME-STATE paired-pull equivalence, explicitly.

**A4 (folds into the P1->P2 seam): PER-FAMILY ATOMICITY.** Builder flip + publisher-input flip land
in ONE window per served family, OR the interim old-writer continuation is NAMED with its END
CONDITION in the wave row. CVO's words, adopted as the rule: *"an unstated overlap is how a shadow
is born without anyone deciding to build one."*

**Group-D format cell: CONFIRMED by CVO** (their clarification folds into Group B -- theirs).

**The routed unknown, answered as a PROPOSED contract line (CTO concur requested -- data-semantics
is the arch lane):** L2's no-data-day semantics: **non-trading days produce NO partition**
(lib/trading_calendar resolves FIRST -- the T-1 law; Group W's Sunday row already states it);
**a TRADING day with no bronze delivery produces NO partition + a LOUD catch-up-floor detection**
-- never an empty partition, never a silent carry-forward; **carry-forward is a SERVING-tier
decision only** (the publisher's measured re-serve-last-good), never a silver/gold fabrication.
One line, three states, each with its owner. **CONCURRED BY CTO 080121Z as proposed -- and now
DOUBLY LOAD-BEARING: Andrew's ~0757Z silver-completeness trigger requirement makes this line the
trigger predicate's CALENDAR CONTRACT** (a non-trading day correctly never fires the gold runner;
a trading day whose silver never lands is the catch-up floor's loud case). The 17b law amendment is
LANDED @a9c159f134 (gold-is-parquet in the law line; migration authority = the ratified spec set +
cutover acts, never the law line itself). Both remaining CTO items from this spec are CLOSED.

## 8. WAVE-LABEL RENAME + THE FIVE-PHASE MAPPING (Andrew build order @4dbf4a0d7c, ~0810Z)

**COLLISION FIXED BEFORE IT MISROUTES (the night's own namespace rule, applied to my own labels):**
Andrew's ruled build order is **P1 SCRIPTS -> P2 TIMING -> P3 REPOINTS -> P4 PUBLISHERS -> P5
DECOMMISSION (gated on the portal verified in-taking + displaying)** -- and this spec's waves were
also P-numbered, with P3/P4 meaning DIFFERENT things in each. Sovereign vocabulary wins:
**this spec's waves rename P0-P4 -> R0-R4 (refactor waves)**, and the mapping to his phases is:

| Refactor wave (this spec) | Slots into Andrew's build phase |
|---|---|
| R0 naming + Group-W + verify | done (pre-P1 substrate) |
| R1 gold builders rebuilt parquet | **P1 SCRIPTS** (+ ~A's Group-W pages = **P2 TIMING**'s frame) |
| R2 the nine port windows | **P3 REPOINTS** (M-row map = P3's substrate) + **P4 PUBLISHERS** (M7's one-ordered-act) |
| R3 deploy-plane repoint | **P3 REPOINTS** (tail) |
| R4 drains + T5.B kill | **P5 DECOMMISSION** -- the 19-channel disposition map is P5's WORKLIST and NOTHING in it moves before the P5 gate (portal verified in-taking + displaying; cert-of-built is the verifier) |

In-flight X-acts continue as P3 pilot work (his record). COO reshapes the decomposition around the
phase-gates; every R-row keeps its owner/trigger/precondition unchanged -- only the labels moved.
