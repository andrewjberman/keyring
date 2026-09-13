# D8 — THE FIRST MIGRATION: THREE LEGACY FIRM BUCKETS → THE SPELLED-OUT FIRM BUCKETS, WITH THE IDENTITY SPINE AS PREREQUISITE — STEP-1 BRIEF

**Author:** `4.0.0_SA_CRO~D` · **UTC:** 2026-09-13 ~02:2xZ
**Mode:** NEW (greenfield). No project exists; no Part 0.
**Directive:** **D8 "Data Pipelines"** (LAPTOP; `DIRECTIVES.yaml` :329). ⛔ Andrew-direct 2026-09-13 ~02:3xZ, verbatim:
*"No this wouldnt go in D14 if anything this would go in D8 or D12."* then *"Probably D8 really if thats still
Pipeline-coded."* — D8's registered title IS "Data Pipelines" (read at HEAD this turn), so the condition he named
holds and D8 is the home. D14 "Platform Logic" supplies the LAW this project executes (`infra/logic/02_DOCTRINE.md`);
it does not own the project. The commission record (`…014xZ…`) said "first D14 migration project" and is corrected
in-file; L3 registration is `1.0.0_SA_CTO`'s.
**Commissioned by:** Andrew-direct ~01:4xZ 2026-09-13, verbatim: *"I'd like to run #1 and #5 as the prerequisite of #1 as
a project. I'd like you to write a brief on the subject, and one of the major things id request you add in addition to
the general mechanics of the migration is that we establish canonical path strings for how this data is folded. I think
it probably makes the most sense to model the path format of opal-data-assets so there's continuity from our largest
monolith bucket. Part of doing this is not just the bucket creation, its the eventbridge rule/schedule repointing, the
portal and any associated pointers repointing, and more. I really need you to look through what needs to happen here end
to end, a full clean swap, including decommissioning of legacy resources."* (record `ANDREW_DIRECT_20260913_014xZ_…`)
**Standing rulings this brief executes, not re-argues:** D10-2 (a) — the spelled-out buckets become THE firm buckets;
`opal-data-bd` / `-inf` / `-cot` RETIRE after migration (~01:3xZ); R4–R7, R16, R17, R21 (`02_DOCTRINE.md`);
the identity spine as O4 (`05_IDENTITY_SPINE.md`); `platinum/advi/{firm}/` MIGRATES (call 4); `mockadv` and `demo`
per §IV.9.
**Consumer:** STEP 2, `1.0.0_SA_CTO` `/endpoint --forward`.

⛔ **This brief authorizes no move.** Every act it enumerates is L5–L7 work under never-widen sign-off on every served
key (NEVER#3), one firm at a time. It is a MAP of the swap, not the swap.

---

# PART I — THE OUTCOME TERRITORY

Each is one thing a named kind of person can DO that they cannot do today. Qualitative; no number invented here.

### O1 — Anyone reads a key and knows what it is, whichever bucket it sits in

A seat reads `opal-data-49financial/advi/49financial/gold/fact_account_gains/date=2026-09-11/data.parquet` and, without
opening anything, knows the producing system, the firm, the tier, the table and the partition — and knows that the SAME
string minus the bucket would be that firm's key in `opal-data-assets`. Today the same fact is spelled `gold/canonical/
account_gains/{*}.parquet` in one bucket, `gold/account_gains/{*}.parquet` in another, and nothing says which firm or
which producer (finding IV.4). **This is the canonical-path-string outcome Andrew named; the strings are in IV.5.**

### O2 — A migration engineer computes any legacy key's new home by ONE rule, never by judgment

Given any of the 228 attributed keys in the three legacy buckets (IV.3), the engineer applies one mapping table (IV.6)
and gets exactly one of: a firm-bucket key under the canonical string, an `opal-data-assets` key (bronze/silver go home),
a `state/` key (R21), a `code/` key (R16), or RETIRE — with no key left "undetermined." A key the table cannot place is a
defect in the table, not a case for the engineer.

### O3 — Every route, rule, policy and pointer that names a firm resolves it through the registry

The scoped router's firm map, the origin-response guard, IRPT's `FIRM_BUCKET_MAP`, the three EventBridge served-guards,
the `FIRMSEP` bypass detector, the bucket-policy principals, `data/firm_registry.json`, `partner_roster.json`, the freshness
configs and the Terraform `firm_id`s all READ the firm's bucket from one registry instead of spelling it. Cutting a firm
over is then a registry edit plus a never-widen move — not eight edits in eight files. (O4 of the canon brief, made
executable here; the deployed router already has the shape of that registry in its `p={…}` map, IV.7.)

### O4 — A firm's users see the same dashboard the morning after their cutover, and nobody can tell from the browser

For each of the three firms in turn, every served key answers from the new bucket byte-identical to what it answered
from the old one — the L4-R sign-off's blast-radius half names every served key and its rollback — and the old bucket
is still there, unmodified, for the rollback window. The scoped router's tenant assertion holds at TENANT grain in the
new topology (LD-0442's remediation, `07_ROUTING_REDERIVATION.md` §4), so a second firm's twins in one bucket no longer
defeat it.

### O5 — A pipeline owner sees every trigger that fires their pipeline land on the new bucket, and none on the old

The 11 EventBridge rules whose PATTERNS name a legacy bucket (IV.8) fire on the new one; the ~45 schedules that target
the pipelines' Lambdas fire unchanged while those Lambdas' bucket configuration points at the new bucket; the S3→Lambda
notification configurations (a singleton per bucket — bd 3, inf 2) exist on the new buckets before the old are quiet.
The owner reads this from `trigger-map.json` and the live rules, not from a runbook.

### O6 — An operator retires a legacy bucket and can prove nothing read or wrote it for the whole quiet window

Before `opal-data-bd` is deleted, the operator shows: zero writers (every producer repointed, verified by the served-key
write trail — PREFIX-SCOPED to `platinum/firm/` today, Part V), zero readers over a declared window (CloudTrail `GetObject`
census — ⛔ NOT the `FIRMSEP` detector: `FIRMSEP-s3-direct-access-bypass` has been FAILING at EventBridge → SNS on every
invocation since 2026-05-11, its certification having counted invocations and never read failures (`3.0.0_SA_CVO`
`@3e9200d8f1`, relayed CTO 96374); its SNS emission is evidence of nothing, and this sentence said the opposite at v1), every rule and notification retired or repointed, the bucket policy
removed, every hold and ledger that names it re-pointed or closed SUPERSEDED, the Terraform resources removed from state,
and the per-version delete on a versioned bucket taken as its own Andrew-class act (IRPT_BCKEND-W4-S20: "deleted" on a
versioned bucket means hidden). **Decommissioning is a proof, not a button.**

### O7 — The one key the estate is forbidden to write has an explicit successor or an explicit retirement

`s3://opal-data-inf/gold/meta/pipeline-complete.json` is THE ONE PROHIBITION (Door 6, `OPAL_ASSETS_CONSOLIDATION_PRD.md` §0),
and the `mdpf-feeder-accelerator` rule watches it (IV.8). Retiring `opal-data-inf` retires that key. Someone can point at
the ruling that says what replaced it — or that nothing did and the accelerator rule was retired with it.

### O8 — A declared exception that lives in a bucket being retired is either re-homed by a ruling or the bucket survives for it

MDPF_CANON row B2 (`opal-data-inf/orion/jwt/current.json`, a STANDING DECLARED EXCEPTION, Andrew via CTO~X 76365) is a
consumer of a bucket this project retires and is ruled not to move (IV.10). Someone reads, in one place, either its new
home under `state/` with the ruling that moved it, or the sentence that keeps `opal-data-inf` alive for one key.

---

# PART II — WHERE THE BOUNDARY SITS

**This project OWNS:** the canonical path strings and the legacy→canonical mapping (O1, O2); ~~the identity-spine RUNTIME
and~~ the repoint of every firm-naming consumer to ~~it~~ the D14 registry (O3) — ⛔ **the RUNTIME claim is SUPERSEDED by
Andrew's ~03:5xZ ruling (a): D14 owns the registry and its generated views (`d14-executable-layer-brief-20260913.md` O3);
this project owns only the REPOINT. Consequence (CTO 96353): FWD-3 cannot be met until the D14 registry exists — the
SECOND D14-before-D8 item, scoped to this one outcome; the other seven stay independent.** the three per-firm cutovers of gold + platinum + state + code
(O4, O5); the bronze/silver moves OUT of the legacy buckets INTO `opal-data-assets` (R4) for these three firms; the
decommission proofs and acts for the three legacy buckets (O6, O7, O8); the Terraform for the two firm buckets that do not
exist (`opal-data-inflection`, `opal-data-cottonwood`) on the `s3-49financial.tf` template.

**This project RELIES ON, and does not own:** the canon (`02_DOCTRINE.md`); the ledger (`06_CONFORMANCE_LEDGER.md`); the
served graph's key attributions (`comp-find --corpus aws`, the 228 rows); LD-0442's remedy text for the tenant assertion
(`1.0.0_SA_CTO`'s granularity call); the `/endpoint`, PRD and L4-R gates.

| sibling | relationship |
|---|---|
| **MDPF_CANON / tension-map #2** | ADJACENT, in parallel. Its `platinum/mdpf/{firm}/` slices land in the firm buckets THIS project builds (R7); its dedicated runner's NAME collides with the firm bucket's Deny (IV.11) — the naming is this project's spine work, the runner is MDPF's. |
| **IRPT_BCKEND** | CONSUMER. Writes per-firm platinum to `<FIRM_BUCKET_MAP>/investor-reporting/`; its row 11 (which bucket for 49F) is answered by this project's cutover; its `platinum/` prefix fix (contradiction 1b) lands on the canonical string in IV.5. |
| **tension-map #3 (client data in the shared bucket)** | FOLDED IN for the advi half: `platinum/advi/49financial/*` moves with 49F's cutover and carries the router change. |
| **tension-map #4 (SmartX grammar)** | NOT this project; it is bronze in `opal-data-assets`. |
| **NFRA_OPSEC202609 / NFRA_IAMROLES202609** | ADJACENT. The cross-firm Deny on each new bucket and the role-side belts (bd:534 / cot:192 / inf `cross-firm-deny.tf`) are theirs to keep coherent; this project supplies the FIRM keys and asks for the belts to name the new buckets (IV.9). |
| **OPAL_ADVIPOINTERS.GOLDHOME-REPOINT-49F** (2026-08-18/19) | PRIOR ART — minted `opal-data-49financial` as *"the clean-slate TEMPLATE for the firm-bucket grammar"* with born-with controls. Its grammar comment is the tier-first form IV.5 measures against. |
| **OPAL_ASSETS / OPAL_CONSOLIDATION** | PRIOR ART — the ingest-router and the S3-notification singleton hazard (§2b) are inherited as facts. |
| **The hygiene sweep (tension-map #7)** | AFTER this project; the `_legacy` pairs and dead twins inside these buckets are RETIRE rows it inherits, not moves. |

**Not this project's:** vendor egress; any apply (L7 under `safe-apply`, CTO-gated); amending the cross-firm Deny for
MDPF's runner (MDPF's act, on this project's naming); the pause (lifted); `opal-data-demo` (ruled KEPT, untouched).

---

# PART III — THE QUALITATIVE BAR

- **O1/O2 pass when** a seat that has never seen the legacy layout places all 228 attributed keys with the table and a
  second seat, independently, places them the same way — where today two seats reading `gold/artifacts/x.json` disagree
  on whether it is gold or platinum.
- **O3 passes when** cutting a firm over touches ONE registry row and the router, the guards and IRPT follow — where
  today the same firm is spelled eight ways in eight files.
- **O4 passes when** a firm's advisor opens the same page the morning after and reads the same numbers, and the L4-R
  sign-off's blast-radius half named every served key that moved — where today no per-firm cutover has ever been done.
- **O5 passes when** a pipeline owner reads the live rule set and finds no pattern naming a retired bucket.
- **O6 passes when** the decommission ledger for a bucket shows the quiet-window read census at zero on a named
  instrument, not on an assertion — where today "retired" means "nobody remembers a reader."
- **O7/O8 pass when** the prohibition key and the B2 exception each have one sentence of disposition citing a ruling.

---

# PART IV — THE SUBSTRATE: FINDINGS, EACH WITH WHAT WAS MEASURED

All measured 2026-09-13 ~01:4xZ–02:1xZ unless stated. Instruments named per finding.

### IV.1 — The repo names these buckets in 781 files; the repoint surface is the DEF band
`comp-find 'opal-data-(bd|inf|cot)\b' infra/ data/ portal/src lib/ .tools/ --all`: **2,641 hits across 14,169 files
scanned; 781 files**; bands HEAD 443 · DEF 342 · SURFACED 955 · CONFIG 283 · TEST 84 · DOC 534. **DEF (where a bucket
name is DEFINED — a constant, a config key) is the surface a repoint edits:** `lib/config.py` in each of
`data/black_diamond/scripts/{gold,silver}`, `data/cot/scripts/gold`, `data/inf/manual_api`, `data/canonical/schwab/*`
(27 builders), `data/assets/scripts/gold/runners_49f/{d_publisher_port,dryfit_driver,fit_harness}.py`,
`.tools/silver-dtype-migrate.py`, the bronze converters, the `_lib/watermark.py` pair. **CONFIG (58 files)** is the
declared plane: the Terraform CHANGELOGs for `bd-pipeline`, `cot-pipeline`, `inf-pipeline`, `mdpf-pipeline`,
`opal-assets`, `portal-auth`, `shared-infra`; `infra/aws/ec2/EC2_MANIFEST.json`; `infra/aws/lambda/ci/{lambda-source-map,
trigger-map}.json`; `infra/aws/lambda/investor-reporting/PATH_MANIFEST.json`; two SSM force-download documents;
`data/firm_registry.json`; `data/mdpf/config/partner_roster.json`; `data/{black_diamond,cot,inf}/scripts/gold/gold_freshness_config.yaml`;
`data/served_freshness_config.yaml`. **Finding:** the repoint is ~340 definition sites plus ~58 declared surfaces; the
DOC band (534) is history and must NOT be edited.

### IV.2 — The live plane names them in 249 nodes across six types
`comp-find --corpus aws 'opal-data-(bd|inf|cot)\b'` (vintage 2026-09-13 00:53:52Z): **249 hits across 2,511 nodes** —
CLOUDFRONT_DISTRIBUTION 1 · EVENT_RULE 11 · IAM_POLICY 3 · S3_BUCKET 3 · S3_BUCKET_POLICY 3 · **S3Key 228**. The three
bucket policies read `drift=LIVE-no-DECLARED` — **they are not in Terraform**; read live (IV.9).

### IV.3 — The 228 attributed keys are the population O2 must place, and they reveal five key classes
The served graph attributes each key to `writer-firm` / `reader-firm` / `firm-lambda`. Grouped by what they ARE (not by
their current prefix): **(a) served JSON** — `platinum/{firm,advisors,clients,accounts}/…` AND the legacy `gold/artifacts/*.json`,
`gold/entities/*/…json`, `gold/platinum/*`, `gold/views/*.json` (JSON the router serves is PLATINUM by function, R12);
**(b) analytical parquet** — `gold/canonical/*`, `gold/timeseries/*`, `gold/dimensions/*`, `gold/holdings/*`, `gold/lots/*`,
`gold/positions_cube/*`, `gold/views/*.parquet`, `gold/cache/*`, `gold/account_gains/*`; **(c) operational state** —
`gold/_state/*`, `gold/_parity/*`, `gold/meta/*_watermark.json`, `gold/manifests/*`, `gold/canonical/watermarks.json`,
`config/*`, `otp/state.json`, `blackdiamond/{49f,cot}/session-trigger-mode.json`, `silver/meta/gap_manifest.json` — the
R21 `state/` class Andrew ruled ~01:3xZ; **(d) ingest tiers in the wrong bucket** — `bronze/orion-api/*`,
`bronze/orion-api-v2/*`, `silver/*`, `schwab/silver/*` (R4 → `opal-data-assets`); **(e) retire candidates** —
`gold/validation/*`, `gold/holdings_lots_v2_dryrun/*`, `gold/timeseries/holdings_lots_shadow/*` (a SHADOW — R18),
`gold/canonical/canonical_performance_2026-04-20.parquet` (a dated singleton). Plus **(f) code** — `code/gold/*` (R16).
**Finding:** the legacy `gold/` prefix holds three tiers' worth of things; "move gold" is not a move, it is a sort.

### IV.4 — Two firm-bucket grammars exist and they disagree on the first segment
**The monolith (R1, live):** `opal-data-assets/{source}/{scope}/{tier}/{table}/{partition}/…` — source-first.
**The 08-18 template (`s3-49financial.tf` header, Andrew-direct 2026-08-18 ~17:30Z):** `opal-data-{firm}/gold/{product}/{table}/date={D}/data.parquet`,
`gold/{product}/dimensions/{dim}/date={D}/`, `_code/` at bucket root — tier-first, product second. **What is actually
in `opal-data-49financial` today:** `gold/` only (25,577 objects; 16,067 parquet / 8,859 json). **Andrew's word today:**
model the firm bucket on the monolith *"so there's continuity."* **Finding:** the two grammars are his at different
dates; today's is later and names its reason. IV.5 proposes the monolith form and names the template's clause as the
one it supersedes, for L2/L4 to ratify.

### IV.5 — THE CANONICAL PATH STRINGS (PROPOSAL, for L4 to ratify; the reason for each is stated)
**The rule: the bucket is a TENANCY boundary, never a grammar boundary. One string, everywhere.**

```
opal-data-assets/{source}/{scope}/{tier}/{table}/{partition}/{object}          (R1, unchanged)
opal-data-{firm} /{source}/{scope}/{tier}/{table}/{partition}/{object}          (the SAME string)

  {source}   the PRODUCING SYSTEM's spine key:  a vendor (blackdiamond, schwab, orion, eclipse, smartx)
             for pass-through data; a product/system (advi, irpt, mdpf, etfs) for DERIVED tiers
  {scope}    in a FIRM bucket, MUST EQUAL the bucket's own firm key  <- the invariant a gate checks
  {tier}     in a firm bucket: gold | platinum | state | code only (bronze/silver never -- R4)
  {table}    snake_case table or artifact family; {partition} hive `date=YYYY-MM-DD` or a named leaf
```

Worked strings, by class from IV.3:
```
(b) opal-data-49financial/advi/49financial/gold/fact_account_gains/date=2026-09-11/data.parquet
(a) opal-data-49financial/advi/49financial/platinum/firm/header_metrics.json
(a) opal-data-49financial/advi/49financial/platinum/advisors/{id}/book.json
(a) opal-data-49financial/mdpf/49financial/platinum/aggregate-aua-timeseries.json      <- R7 firm slice of a product
(a) opal-data-49financial/irpt/49financial/platinum/investor-reporting/...              <- IRPT row 1b closes here
(c) opal-data-49financial/advi/49financial/state/watermarks/load_flows.json
(c) opal-data-49financial/advi/49financial/state/parity/positions_cube/{run}/scorecard.json
(c) opal-data-49financial/blackdiamond/49financial/state/session/trigger-mode.json
(f) opal-data-49financial/code/advi/gold/...                                            <- R16, one code home
(d) opal-data-assets/orion/inflection/bronze/{feed}/{YYYYMMDD}/...                       <- goes HOME, not to the firm bucket
```
**Why source-first and why `{scope}` is repeated inside its own bucket:** (1) continuity — his word; a key is the same
string in the monolith and the firm bucket, so a consumer that learns one layout has learned both; (2) the repeated
`{scope}` makes every key SELF-DESCRIBING and gives the tenant assertion something to assert at TENANT grain
(bucket + `{scope}` segment must agree — LD-0442's remedy text exactly); (3) a product pipeline writing a firm slice
(R7) has a place to say WHICH product produced it without inventing a prefix. **What it supersedes:** the 08-18
template's `gold/{product}/…` (tier-first) and `_code/` at root. **What it keeps from the template:** born-with
controls, `date={D}/data.parquet` partitions, the cross-firm Deny. **Router consequence:** the scoped rewrite targets
change from `/gold/artifacts/…` to `/advi/{firm}/platinum/…` — one table in the router, one in the response guard.

### IV.6 — THE MAPPING TABLE (legacy key → canonical), the O2 rule
| legacy (in `opal-data-{bd,inf,cot}`) | class | canonical destination | rule |
|---|---|---|---|
| `platinum/**` | a | `advi/{firm}/platinum/**` (same tail) | R6 |
| `gold/artifacts/**.json`, `gold/entities/**.json`, `gold/platinum/**`, `gold/views/*.json` | a | `advi/{firm}/platinum/{artifacts,entities,firm,views}/**` | R12 — served JSON is platinum whatever it was called |
| `gold/canonical/{t}/{*}.parquet`, `gold/timeseries/{t}/…`, `gold/dimensions/*.parquet`, `gold/holdings/*`, `gold/lots/*`, `gold/positions_cube/*`, `gold/views/*.parquet`, `gold/cache/*`, `gold/account_gains/*` | b | `advi/{firm}/gold/{t}/date={D}/data.parquet` | R5, R11 (JSON twins → parquet) |
| `gold/_state/**`, `gold/_parity/**`, `gold/meta/*_watermark.json`, `gold/manifests/**`, `gold/canonical/watermarks.json`, `silver/meta/gap_manifest.json` | c | `advi/{firm}/state/{watermarks,parity,manifests}/**` | R21 |
| `config/*` | c | `advi/{firm}/state/config/*` (reference data the runners read) | R21 |
| `otp/state.json` (inf) | c | `orion/inflection/state/otp/state.json` — **and the `inf-otp-state-change` rule follows it** | R21 |
| `blackdiamond/{49f,cot}/session-trigger-mode.json` | c | `blackdiamond/{firm}/state/session/trigger-mode.json` | R21 |
| `bronze/**`, `silver/**`, `schwab/silver/**` | d | `opal-data-assets/{vendor}/{firm}/{bronze,silver}/**` — for inf: bronze **re-landed raw** from source (4,802 parquet under bronze cannot be moved, R9) | R4, R9 |
| `code/gold/**` | f | `code/{source}/gold/**` | R16 |
| `gold/validation/**`, `gold/holdings_lots_v2_dryrun/**`, `gold/timeseries/holdings_lots_shadow/**`, dated singletons | e | RETIRE after `comp-blast` clears each for a live reader | R17, R18 |
| `gold/meta/pipeline-complete.json` (inf) | — | **its own row: O7** | Door 6 |
| `orion/jwt/current.json` (inf) | — | **its own row: O8** | B2 |
| `gold/eclipse/{*}/_meta/gold_complete.json`, `silver/eclipse/{*}/_meta/silver_complete.json` | c | `eclipse/inflection/state/complete/**` — **and the completion-sentinel rules follow** | R21 |

**Finding:** every one of the 228 attributed keys lands in exactly one row above (checked by class, not by recall — the
class list is the subtraction of IV.3 from the 228). Two rows are not moves but decisions (O7, O8).

### IV.7 — The portal's pointers: one router map, one shared module, one declared origin, one guard, one IRPT map
Measured from the DEPLOYED `shared-advisor-router` v25 (`07_ROUTING_REDERIVATION.md` §3): `p={49financial:{bucket:"opal-data-bd"},
inflection:{bucket:"opal-data-inf"}, mockadv:{bucket:"opal-data-bd"}, demo:{bucket:"opal-data-demo"}, cottonwood:{bucket:"opal-data-cot"}}`;
the source is the shared `FIRM_CONFIG` module (`f215cfdddf`, ADVI_FIRMSEP.03). The CloudFront distribution declares
origin `S3-opal-data-bd` for the four scoped S3 behaviours (the router rewrites the domain per request, but the declared
origin must exist and carry the OAI). The origin-response guard `shared-advisor-router-response:5` **re-derives the
bucket independently** (LD-0442 ledger: it 502'd on the first exercised fetch when it did not know the new bucket).
IRPT_BCKEND's `FIRM_BUCKET_MAP` reuses the same map. `portal/src/api/endpoint-mapping.ts` documents SCOPED = per-partner
bucket. **Finding:** the router map IS the identity spine's first consumer and already has its shape; O3 turns it from
a constant into a read.

### IV.8 — EventBridge: 11 rules name a bucket in their PATTERN; ~45 schedules do not, their Lambdas do
From the live plane (IV.2) and `trigger-map.json`:
- **Pattern rules (the pattern itself changes):** `FIRMSEP-s3-direct-access-bypass` (watches `GetObject` on ALL THREE →
  SNS; **goes blind on the new buckets unless its list is widened BEFORE cutover and narrowed after**);
  `opal-{49f,cot,inf}-served-guard-on-write` (each on `platinum/firm/header_metrics.json` in its bucket);
  `cot-bronze-complete`, `cot-silver-complete`, `inf-assets-trigger-bronze-complete`, `inf-gold-full-on-bronze-complete`
  (DISABLED), `inf-silver-chain-bronze-complete` (completion sentinels — these move to `opal-data-assets` with the bronze,
  R4, so the rules repoint to the MONOLITH, not the firm bucket); `inf-otp-state-change` (follows `state/`); and
  **`mdpf-feeder-accelerator` on `opal-data-inf/gold/meta/pipeline-complete.json` — the prohibition key (O7).**
- **Schedules (unchanged; their targets' config changes):** ~45 `cron(...)`/`rate(...)` triggers targeting the bd-*,
  cot-*, inf-* Lambdas (session/runner/fees/keepalive/allocation/asset-dim/realized/transaction/unrealized/gold/prices/
  accounts/assets/positions/reps/txn/billing/tax/performance/jwt/export/etf-ownership/value-parity/nna-partition), plus
  `opal-assets-ingest-mirror-{cot,inf}-daily` (the mirror INTO assets — this project makes it unnecessary) and
  `exec-summary-trigger` on `bd-pipeline.gold-chain`. **Denominator:** trigger-map entries naming a bd/inf/cot unit, read
  in full above. Also: **`inf-canonical-prices-daily` is DISABLED and HELD** (OPAL_ASSETS §3 ruling); the migration must
  not re-enable it by moving it.
- **S3→Lambda notification configurations (a SINGLETON per bucket):** `opal-data-bd` 3, `opal-data-inf` 2, `opal-data-cot`
  0 (measured, `get_bucket_notification_configuration`). Each must be re-created on the destination bucket and the
  consolidation PRD's clobber hazard (§2b) applies to the assets bucket's 11-rule configuration.

### IV.9 — IAM and bucket policies: three undeclared policies to retire, one new-bucket policy that cannot serve yet
Measured live (`get_bucket_policy`): `opal-data-bd` / `-inf` / `-cot` each carry **`AllowScopedAdvisorOAI`** (OAI
`E139998VWH0PD`, `s3:GetObject` on `/*`) and an **OAC grant to the CloudFront service principal on `gold/*`** conditioned
on distribution `EVTSA9VEHNZVH` — and all three are `LIVE-no-DECLARED`. **`opal-data-49financial` carries ONLY
`DenyForeignFirmPrincipals`** (`cot-*`, `inf-*`, `mdpf-*`, `opal-assets-mdpf-*` roles) — **no OAI grant, no OAC grant**:
CloudFront cannot serve it today. Versioning Enabled on all four; lifecycle rules bd 4 / inf 3 / cot 2 / 49financial
none. The role-side belts (`bd:534`, `cot:192`, inf `cross-firm-deny.tf`) name the OLD buckets. **Finding:** each new
bucket needs the two serving grants on its `platinum/**` (and `gold/**` if the OAC path stays) BEFORE its router-map
row flips, and the belts must be widened to the new names — NFRA_IAMROLES's plane, this project's ask.

### IV.10 — Two rulings sit INSIDE `opal-data-inf` and a "full clean swap" would sweep them (from `1.0.0_SA_CTO` 96310)
`MDPF_CANON_PRD.md` §4: **B1** `opal-data-bd/schwab/silver/rps/` read → REPOINT, ruled (lands via assets); **B2**
`opal-data-inf/orion/jwt/current.json` read → **STAYS, a STANDING DECLARED EXCEPTION** (Andrew via CTO~X 76365).
**Finding:** B2 is a consumer of a bucket this project retires and is ruled not to move; on every mechanical axis it
looks like every other reader. It is O8, and it means **`opal-data-inf` cannot be fully decommissioned without either
re-homing that key under `state/` by a new ruling or keeping the bucket alive for one object.** Also from the same
message: `mockadv → opal-data-bd` — retiring `bd` moves TWO map entries; whether `mockadv` follows 49financial into
`opal-data-49financial` is a question, not an assumption (IV.9 of the spine records it as an alias; no ruling homes it).

### IV.11 — The fence matches on the writer's NAME, and Andrew has already ruled the writer's shape (from `1.0.0_SA_CTO` 96311, `3.0.0_SA_CVO` 96309)
Andrew-direct 2026-09-12 ~13:4xZ: **"C"** — no narrow exception to the cross-firm fence; per-firm runs; and *"There
should be a dedicated mdpf runner for this also not reusing a firm specific runner."* The new firm buckets' Deny is keyed
on `aws:PrincipalArn` patterns `role/mdpf-*` and `role/opal-assets-mdpf-*`. **Finding:** a dedicated MDPF runner named
`mdpf-<anything>` is denied BY NAME from the firm buckets it must write R7 slices into. The runner is MDPF's; **its NAME
is a spine decision this project owns** — role names are aliases too. The CVO's point stands and is carried: the fact
that blocks the swap sits on the DESTINATION bucket, which a census over the source names cannot return.
**And the collision has a WORKING PRECEDENT (`3.0.0_SA_CVO` 96315 via CTO 96319, `comp-iam refresh-census` generated
2026-09-13T02:02:58Z, denominator 250 roles — refreshed first; the committed census was 09-09 against a 24h TTL):**
inside `opal-data-49financial`, past the fence, unconditioned: `bd-exporter-ec2-role` (`AdviChainGoldRW`, Get+Put on
`gold/advi/*`) and `opal-advi-stitch-landing-role` (Put on `gold/advi/reference/`); and **`irpt-directory-refresh-role`
ALREADY writes `investor-reporting/directory/_refresh/*` in all three CURRENT firm buckets** — none of the three
matches an ArnLike pattern. **CORRECTED 2026-09-13 ~04:2xZ (Andrew: "get this sorted out with CTO"):** "name the runner outside the four
patterns" is WITHDRAWN -- under the D14 naming schema (`d14-naming-schema-brief-20260913.md` IV.2, system-first) the
runner is `mdpf-{scope}-runner-role`, which `role/mdpf-*` denies by design; a name outside the patterns would be
NON-CONFORMANT. The fence's pattern list (`cot-*`, `inf-*`, `mdpf-*`, `opal-assets-mdpf-*`) is the OLD firm-as-system
grammar baked into IAM. **The resolution is D14's, and it is the ONE hard D14-before-D8 item:** the Deny keys on the
SCOPE slot (any principal whose scope token is not the bucket's firm), derived from the registry (executable-layer brief
O2), replacing the enumerated prefixes -- landed on `s3-49financial.tf` BEFORE this project mints the two new buckets
from it. This is NOT the exception route Andrew refused ("C", 09-12): it replaces the list, it does not carve a
principal out of it -- a distinction for `1.0.0_SA_CTO` at L4, back to Andrew as one card if the CTO reads it as the
refused route. ⛔ **W2-S49's "grants
PutObject on no firm bucket" (09-12 09:41Z, 26 statements) is a DEAD VINTAGE** — 33 statements this turn incl.
`IrptDirectoryFirmDestWrite`; C-S87 is the live row. NOT MEASURED: whether any of those grants would reach the two
buckets this project CREATES (nothing can hold a grant on a bucket that does not exist).

### IV.12 — The records that name these buckets are a population, not a footnote
`comp-find` over `org/critical_paths/` + `org/tier0/ledger/`: **275 hits across 1,366 files**; HEAD 85 (36 deploy-completion
ledgers and holds naming a bucket in their filename) · DOC 189. Among them: `HOLD_INF_CANONICAL_NNA_REBUILD_20260713.md`,
`DOOR5_REVERT_RUNBOOK_20260713.md`, `MDPF_EXECUTION_PLAN_20260722.md`, the `DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial`
hold (already stale once), LD-0442 and its carried hazard row. **Finding:** decommissioning re-points or closes
SUPERSEDED every hold that names the bucket; the deploy ledgers stay as history. A hold left pointing at a deleted bucket
is the `DO_NOT_DECOMMISSION` failure again.

### IV.13 — What the identity spine already resolved, and what this project adds
`05_IDENTITY_SPINE.md` `@45160b1525`: 49 Financial has **eight** spellings across four planes; inflection and cottonwood
three each; the deployed router map is the seed's first consumer. **This project adds the RUNTIME** (a YAML the gates
and the router build read, or a TF data source — L4's choice) and retires aliases one consumer at a time, `bd`/`inf`/`cot`
last, when their buckets are gone.

---

# PART V — WHAT MUST BE TRUE (named, NOT sequenced — sequencing is step 5)

- The identity-spine runtime exists before the first router-map row flips (O3 before O4).
- The canonical path strings are ratified at L4 before any key is written to a new bucket (IV.5 is a PROPOSAL).
- The two missing buckets exist on the `s3-49financial.tf` template with born-with controls, AND carry the two serving
  grants (IV.9), before their firm's cutover.
  ⛔ **TWO PRECONDITIONS AT MINT, NOT ONE (`3.0.0_SA_CVO` 96373 s.8 `@614423c438`, relayed CTO 96374):** the template
  provisions FIVE resources and NO read instrument — `opal-data-49financial`, its first output, has no server access
  logging, no metrics configuration, and is absent from the organisation trail's read selector — so `opal-data-inflection`
  and `opal-data-cottonwood` would be born with O6 unprovable. And the template CANNOT fix it alone: the trail's read
  selector is CLI-applied (`cloudwatch-alarms.tf:208-211`) and absent from Terraform, so no plan ever shows drift on it.
  Both the bucket-side instrument (template) and the trail selector (CLI, a shared audit surface) must cover a new bucket
  BEFORE it is minted, or the quiet-window clock for that bucket cannot start.
- The scoped router's tenant assertion is re-derived at TENANT grain (bucket + `{scope}`) in the same change that moves
  `platinum/advi/{firm}/` (LD-0442's remedy; `1.0.0_SA_CTO`'s granularity call).
- The origin-response guard learns the new buckets by INDEPENDENT re-derivation, not by importing the router's decision.
- `FIRMSEP-s3-direct-access-bypass`'s bucket list is widened BEFORE any cutover and narrowed AFTER the last decommission.
- inf's bronze is RE-LANDED from source into `opal-data-assets`, never converted (R9); the completion-sentinel rules
  repoint to the monolith, not the firm bucket.
- O7 (the prohibition key) and O8 (the B2 exception) each have a ruling before `opal-data-inf` is touched.
- The dedicated MDPF runner's role name does not match `mdpf-*` / `opal-assets-mdpf-*`, or the Deny is amended
  explicitly — never worked around (IV.11).
- `mockadv`'s home is decided (IV.10). `demo` is untouched (ruled KEPT).
- Every served key that moves has a never-widen sign-off naming its rollback (NEVER#3); the old bucket stays unmodified
  through the rollback window.
- Decommission of a bucket is preceded by a zero-reader census over a declared window on a named instrument (O6).
  ⛔ **AND THE INSTRUMENT MUST COVER THE PREFIXES AND THE DIRECTION THE OUTCOME CLAIMS BEFORE THE WINDOW OPENS** — added
  2026-09-13 ~03:1xZ from `3.0.0_SA_CVO` 96326 + `1.0.0_SA_CTO` 96328 (`cloudtrail get-event-selectors`, both trails,
  selectors printed in full): READS are recorded for `opal-data-bd` and `-inf` (whole bucket, ReadOnly data selector) and
  for `opal-data-cot` NOWHERE; WRITES on all three are recorded ONLY under `platinum/firm/` (the served-key write trail,
  StartsWith); S3 server access logging is off on all three (CVO's limb). So "nothing read cot for N days" and "reads on
  cot were never recorded" are the same zero, and a write to `gold/`, `bronze/`, `silver/`, `code/` or `state/` during the
  window is invisible. ⚠ The trap: "is the bucket in CloudTrail" answers YES for all three (the write trail names them) —
  the discriminator is `readOnly`, not presence. CloudTrail data events are not retroactive: **the quiet-window clock
  cannot start before the selectors cover the buckets and prefixes**, which puts a start-date consequence on the window
  Andrew is asked to size (CTO 96323). Not measured: a third read instrument on cot (VPC flow, app logs, CloudWatch
  request metrics). Amending a trail selector is a shared audit surface — named as a precondition, not proposed as an act.
- The per-version delete on a versioned bucket is its own Andrew-class act (IRPT_BCKEND-S41 precedent).
- Each firm is its own cutover under R19; **49F first** is a dependency claim (its bucket exists; its gold is there;
  the advi half folds in), not an order.

---

# PART VI — STATUS · ⛔ NOT OUTCOME-BEARING · measured 2026-09-13, clocks per line

- The pause is LIFTED (~01:3xZ); IRPT_BCKEND/FNTEND resume on their own reads.
- `opal-data-49financial` exists: gold only, 25,577 objects, Deny-only policy, versioning on, no lifecycle (02:0xZ).
  `opal-data-inflection`, `opal-data-cottonwood` do not exist (census, 16:3xZ 09-12).
- The deployed router is v25 (`40697fe79d`); its map names the three legacy buckets (00:3xZ).
- D10 → D14 fold landed `@f8e647f026` (MSTR 02:13Z); Rule 17b's citation repointed to the D10 PRD `@522a45f5c5` (CTO)
  and flagged for a second repoint when the D14 PRD exists.
- MDPF_CANON's producer census (22 producers / six buckets) exists at `MDPF_CANON_PRD.md` §4; its vintage is 2026-08-25
  and the CTO does not vouch for its currency.
- All CRO commits LOCAL; origin/CLOUD `6ced337f86` at the last ls-remote (01:2xZ).

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

- **No producer was traced by execution.** The 228 attributions are the served graph's; `writer-firm` says which firm's
  runner writes, not which script. Each firm's MAP step traces its scripts (the DEF band is the starting list).
- **The ~45 schedules were read from `trigger-map.json` (declared), not from the live scheduler.** EventBridge SCHEDULER
  schedules are invisible to `describe-rule`; one is in the map (`etfs-reports-monthly-run`, not this project's).
- **The 11 pattern rules' TARGET Lambdas were read from the map; their live state was not re-read.**
- **The S3 notification configurations' targets were counted, not read.**
- **The 08-18 template's clauses beyond the header comment were not read** (the file was read to line 80).
- **CloudTrail coverage of the three buckets was not measured by this seat** — the CVO/CTO measurement is carried in
  Part V with its instrument named; this list held its absence when the brief was cut.
- **No lifecycle rule was read** (counts only): a rule that expires or transitions objects in a legacy bucket is a
  hazard to the rollback window and must be read at MAP.
- **`FIRMSEP-s3-direct-access-bypass` was cited as a working detector at v1 without reading its invocation failures** —
  it is dark (Part I O6, corrected); the CVO's measurement is the instrument.
- **`opal-data-inf`'s and `-cot`'s policies were read; the role-side belts were not** (`bd:534`, `cot:192`, inf
  `cross-firm-deny.tf` cited from the template's comment). The identity-plane grants in IV.11 are the CVO's
  measurement (instrument named there), not this seat's.
- **The COO's 08-21 rejection of republish-to-bd (msg 64839) was not read** (`07` §4 precondition one).
- **No count of objects per legacy key class** — the 228 are prefixes/patterns; the ledger's bucket totals are the
  volumes (bd 125,653; inf 96,774; cot 7,047).
- **Effort is not estimated.** A number here would be treated as ratified downstream.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md
  PROJECT           NONE-YET  (a MEMBER project of D8 "Data Pipelines", by his ~02:3xZ word; L3 is 1.0.0_SA_CTO's)
  LAW IT EXECUTES   D14 "Platform Logic" -- infra/logic/02_DOCTRINE.md (the canon); D14 owns the rules, not this project
  EXISTING PRD      NONE for this project.  Inherited as law: infra/logic/02_DOCTRINE.md (R1, R4-R7, R9, R11, R12,
                    R16, R17, R18, R19, R21) · MDPF_CANON_PRD.md s.4 (B1 repoint, B2 STAYS) · s3-49financial.tf
                    header (the 08-18 template) · LD-0442 + its carried row · OPAL_ASSETS_CONSOLIDATION_PRD.md s.2b
  THE REFERENCE SET infra/logic/ -- 01_CENSUS @d35653da5e · 02_DOCTRINE @a49a7dca18 · 05_IDENTITY_SPINE @45160b1525 ·
                    06_CONFORMANCE_LEDGER @4faf061126 (+v2.1) · 07_ROUTING_REDERIVATION @c728c2a52e ·
                    08_TENSION_MAP @c6be748be7 (items 1, 3, 5)
  RULINGS CARRIED   ANDREW_DIRECT_20260913_013xZ (nine calls: D10-2, platinum/advi, R21, R16 non-app, mockadv/demo) ·
                    ANDREW_DIRECT_20260913_014xZ (this commission) · ANDREW_DIRECT_20260912_134xZ (route C; dedicated
                    mdpf runner) · ANDREW_DIRECT_20260818 (the firm-bucket template) · e29a895ce3 · 3fd386598f
  MEASURED INPUTS   repo census (781 files; bands) · live census (249 nodes / 2,511) · the 228 attributed keys ·
                    trigger-map.json (~55 bd/inf/cot triggers) · four live bucket policies · deployed router v25
  SIBLING PROJECTS  MDPF_CANON (tension #2) · IRPT_BCKEND · NFRA_OPSEC202609 · NFRA_IAMROLES202609 ·
                    OPAL_ADVIPOINTERS.GOLDHOME-REPOINT-49F (prior art) · the hygiene sweep (after)
  WAITING-ON        L4 ratification of IV.5 (the path strings) · rulings for O7 and O8 · mockadv's home ·
                    the MDPF runner's name (MDPF's act on this project's spine) · 1.0.0_SA_CTO's tenant-grain call
  MEASURED AT       2026-09-13 ~01:4xZ-02:1xZ UTC; Part VI clocks per line
```

**Author:** 4.0.0_SA_CRO (Chief Research Officer) · **Home:** org/tier1_exec/4.0.0_SA_CRO/
