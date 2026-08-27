# ANDREW-DIRECT 2026-08-25 ~17:55Z -- GOLD CONSOLIDATION: one bucket per product-or-firm, code beside it

**Channel:** CTO terminal, direct to `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`.
**Status:** ⛔ **DIRECTION RECORDED. NOTHING MOVES. NOT A MIGRATION AUTHORIZATION.**

## VERBATIM (the operative clauses)

> "I think the issue we're discovering is that we have "gold" folders kind of randomly all over the
> place. The pattern that makes the most sense to me based on our architecture is that we pull in
> effectively all assets to one bucket through the same pattern (that is opal-data-assets in the
> various bronze channels) with event-trigger silver parquet conversion. I think what needs to happen
> then is that the various gold layers go to a bucket specific to that product or firm, depending on
> the shape, this bucket is where the code for said gold process/aggregation/analytics should be as
> well. Then there is a platinum publisher that picks those files up and brings them in json format
> to the portal, opal-data-portal-v2. I think the way this should go is we streamline all of this in
> opal-data-mdpf. no "mdpf_revamp" no opal-data-assets/portal/gold, none of that. It should be the
> exact same pattern for opal-data-etfs, holding gold queryable parquets for all ETFS_CANON
> ETFS_INGESTION ETFS_POSITIONING all of that at the gold layer, in the case of advisor intelligence,
> it should be the gold advi items per firm sit in opal-data-49financial opal-data-inflection
> opal-data-cottonwood (we'll spell it out so it doesnt get confused with the opal-data-bd
> opal-data-inf opal-data-cot old layers)."

> "I want to scope this out so this kind of scenario never bites us again and we have to go searching
> trying to remember where the fuck some fragment of a process is."

Also directed: *"rigidly map these out and every single dependency"*, per-scope dataflow assessment
(Global / 49 Financial / Inflection / Cottonwood), *"a lot of atom-decomp, a lot of comp-dataflow
comp-find"*, contracts confirmed by proof-of-spec, and **all triggers / EventBridge rules / schedules
repointed as needed, all code in canonical locations and referenced from those locations.**

## THE TARGET PATTERN, AS HE STATED IT

```
INGEST     all assets -> opal-data-assets/{vendor}/{firm}/bronze/      (one pattern, unchanged)
SILVER     event-triggered parquet conversion, in opal-data-assets     (unchanged)
GOLD       -> a bucket specific to the PRODUCT or FIRM, and THE CODE LIVES THERE TOO
             product-shaped : opal-data-mdpf . opal-data-etfs
             firm-shaped    : opal-data-49financial . opal-data-inflection . opal-data-cottonwood
PLATINUM   a publisher picks gold up and writes JSON -> opal-data-portal-v2                (unchanged)
```
Spelled-out firm names are deliberate, to avoid collision with the legacy `opal-data-bd` /
`opal-data-inf` / `opal-data-cot` layers.

## ⛔ THIS AMENDS RULE 17b AND THAT IS HIS CALL, NOT A DERIVED ONE

CLAUDE.md Rule 17b currently ratifies **four tiers across TWO buckets** -- bronze/silver/gold ALL in
`opal-data-assets`, platinum in `opal-data-portal-v2` -- and the 2026-08-11 amendment names the
product-gold home as `opal-data-assets/portal/gold/{product}/{scope}/`. **His instruction moves gold
OUT of `opal-data-assets` entirely and explicitly names `portal/gold` as a thing to remove.**

**So this is a LAW AMENDMENT, not an implementation detail.** It cannot be executed under the current
rule and must not be half-executed against it. The amendment is his to make explicitly; this record
captures the direction, not the authorization.

## THE MEASURED SPRAWL -- what is actually out there, 2026-08-25 ~17:5xZ

### `gold/mdpf_revamp/` -- his first question: where is it and what is in it
`s3://opal-data-assets/gold/mdpf_revamp/` -- **478 objects**, eight prefixes:
`49financial/` (3) . `cottonwood/` (5) . `global/` (5) . `inflection/` (3) .
**`_aggregate_aua/` (457 daily files)** . `_audit/` . `meta/` . `portfolios/`

### MDPF GOLD EXISTS IN FOUR PLACES
| location | contents |
|---|---|
| `opal-data-assets/gold/mdpf/` | `_manifests_qa/` |
| `opal-data-assets/gold/mdpf_revamp/` | **478 objects -- the live one** |
| `opal-data-assets/portal/gold/mdpf/` | `49financial/ cottonwood/ global/ inflection/ _code/ _manifests/` |
| `opal-data-mdpf/mdpf/` + `opal-data-mdpf/code/` | `bronze/ feeds/`; 2,304 objects total |

⛔ **AND `_code/` APPEARS IN TWO OF THEM** -- `portal/gold/mdpf/_code/` AND `opal-data-mdpf/code/`.
That is his "where the fuck is some fragment of a process" complaint, measured.

### ETF AND 49F ARE EACH SPLIT ACROSS TWO
- ETF gold: `opal-data-assets/portal/gold/etfs/` **and** `opal-data-etfs/gold/` (1,112 objects; that
  bucket already carries `gold/ silver/ platinum/ bbg/ config/ daily/ snapshots/`)
- 49F gold: `opal-data-assets/portal/gold/mdpf/49financial/` **and** `opal-data-49financial/gold/`
  (4,475 objects, plus `_code/` carrying `a00_dim_account.py`, `a01_dim_relationship.py`, runners…)

### THE TARGET BUCKETS ARE PARTLY ALREADY PROVISIONED -- and this is the good news
```
opal-data-mdpf          EXISTS   2,304 objects   (code/ mdpf/ telemetry/ bmkaud-evidence/)
opal-data-etfs          EXISTS   1,112 objects   (gold/ silver/ platinum/ + feeds)
opal-data-49financial   EXISTS   4,475 objects   (gold/ _code/)
opal-data-inflection    DOES NOT EXIST
opal-data-cottonwood    DOES NOT EXIST
```
**Three of five target buckets exist and two already hold gold in roughly the target shape.** This is
a consolidation toward a pattern partially in place, not a greenfield build. `opal-data-etfs` is the
closest thing to a reference implementation the estate has.

### TRIGGER SURFACE
**137 EventBridge rules materialised client-side** (never `--query length()` on a paginated list);
**35 are scope-relevant.** Notable now, before any repoint:
- **6 DISABLED** rules in scope -- `bd-49f-fees-runner-daily`, `bd-49f-runner-daily`,
  `bd-gold-layer-monthly-trigger`, `consolidation-gold-runner-scheduled-start`,
  `inf-gold-full-on-bronze-complete`, `inf-gold-incremental-daily`. **A disabled rule is a
  disposition question, not a repoint target -- each needs a live/dead ruling before migration.**
- **6 EVENT-ONLY** (no schedule) incl. **`mdpf-feeder-accelerator`**, which is the known
  scheduled-pipeline defect and the direct cause of the 07-18 six-day freeze.
- 5 `opal-assets-silver-*-sweep-daily` rules -- the silver layer he is NOT changing.

## SCOPE OF WORK -- honest, not sized

Every one of these is a real workstream, and the list is the deliverable at this stage:
1. **Per-scope dataflow map** (Global / 49F / Inflection / Cottonwood) -- bronze -> silver -> gold ->
   platinum -> portal route, every producer, every consumer, every trigger. `comp-dataflow` /
   `comp-estate` / `comp-find`, denominators printed.
2. **Dependency census** -- for each gold object: who writes it, who reads it, which portal surface
   it lands on. **The consumer side is the dangerous half: a mis-mapped reader breaks a served page.**
3. **Contract confirmation** -- proof-of-spec against the real artifacts, not the docs.
4. **Trigger/schedule repoint plan** -- 35 rules, plus the 6 disabled ones' disposition.
5. **Code relocation to canonical homes** -- including the two-`_code/` MDPF split and the
   `mirror_schemas.py` five-home class DS~M measured today.
6. **The law amendment** (Rule 17b) -- his word, then the rule.
7. **Cutover** -- served keys move under NEVER#3 (never-widen sign-off), one scope at a time.

## ⛔ CONSTRAINTS THAT BIND ANY EXECUTION OF THIS

- **NEVER#3: moving served output requires never-widen sign-off (CTO+COO).** Several of these ARE
  served. `json/mdpf/*` teardown is already PARKED and `account-distribution.json` is a live served
  bell.
- **NEVER: no shadow/parallel channel, no standing comparator.** *"Do it correctly the first time and
  port over."* This migration is exactly where someone will propose a dual-write or a parity
  comparator. **Both are vetoed.**
- **Rule 27**: register -> PRD -> COO atom-decomp of the operative surfaces -> TOs off decomp cells.
  **This is a macro, not a project** -- likely several registered projects under one directive.
- **Rule 24**: "product-shaped vs firm-shaped" is an AXIS and needs the four-postulate test before it
  is used to place buckets. It is not obviously MECE -- MDPF is a product served per-firm.
- **A live outage is in flight** (MDPF_COTREMEDIATION, global still frozen). **This work does not
  start on top of it.**

## ⛔ GAP CLOSED ~18:0xZ -- THE FULL BUCKET CENSUS, AND THE PROBLEM IS WIDER THAN GOLD

The limits section below said eight buckets were listed but unsearched. **They are now searched.**
Medallion-tier prefixes across all 16 `opal-data-*` buckets:

| bucket | bronze | silver | gold | platinum | code |
|---|---|---|---|---|---|
| `opal-data-bd` | Y | Y | **Y** | **Y** | Y |
| `opal-data-cot` | Y | Y | **Y** | **Y** | Y |
| `opal-data-inf` | Y | Y | **Y** | **Y** | Y |
| `opal-data-etfs` | - | Y | **Y** | **Y** | - |
| `opal-data-49financial` | - | - | **Y** | - | Y (`_code`) |
| `opal-data-assets` | (per-vendor) | (per-vendor) | **Y** | - | Y |
| `opal-data-mdpf` | (under `mdpf/`) | - | - | - | Y |
| `opal-data-demo` | - | - | - | **Y** | - |
| `opal-data-portal-v2` | - | - | - | **Y** | - |
| `opal-data-imo` | - | - | - | - | Y |
| astn · news-av · news-v2 · pm · portfolio · trade-submissions | - | - | - | - | - |

**THREE HEADLINE COUNTS:**
1. **GOLD LIVES IN SIX BUCKETS** -- `bd`, `cot`, `inf`, `etfs`, `49financial`, `assets` (the last
   carrying THREE separate gold trees of its own: `gold/mdpf/`, `gold/mdpf_revamp/`,
   `portal/gold/`). Not the three or four the first pass showed.
2. ⛔ **PLATINUM LIVES IN FIVE BUCKETS -- `bd`, `cot`, `inf`, `etfs`, `demo` -- PLUS
   `opal-data-portal-v2`. RULE 17b SAYS PLATINUM IS THE SERVING TIER AND LIVES IN
   `opal-data-portal-v2`.** This is a larger and more surprising divergence than the gold sprawl,
   and **it is NOT in the directive's stated scope** -- his instruction addresses gold and leaves
   "a platinum publisher writes JSON to opal-data-portal-v2" unchanged. **Surfaced, not folded in.**
   Whether those five are live serving tiers, legacy residue, or intermediate staging is UNKNOWN and
   is its own question.
3. **CODE LIVES IN SIX BUCKETS** -- `49financial/_code`, `assets/code`, `bd/code`, `cot/code`,
   `inf/code`, `imo/code`, plus `mdpf/code`. **That is his complaint measured exactly: "some
   fragment of a process" can be in any of seven places.**

**THE REFERENCE IMPLEMENTATION IS `opal-data-etfs`, AND THE TARGET MDPF BUCKET IS THE EMPTIEST ONE.**
`etfs` already carries `silver/ gold/ platinum/` in something close to the target shape.
`opal-data-mdpf` carries `code/` and `mdpf/` and **no medallion tiers at all** -- so the largest,
most-contested product has the least-built target bucket. That inverts the natural build order:
**the hardest migration has the least scaffolding, and the easiest one is already nearly done.**

**AND THE THREE LEGACY BUCKETS ARE NOT MERELY OLD NAMES.** `bd`, `cot`, `inf` each carry a COMPLETE
five-tier stack. Andrew's instruction names them only as a naming-collision hazard ("so it doesn't
get confused with… old layers"). **Their DISPOSITION is unstated and it is the biggest unknown in
this directive** -- a full stack is not decommissionable by assumption, and MDPF_GLOBAL's T5 (legacy
decommission, gated on T1-T3) is plausibly the same question already scoped elsewhere.

## HONEST LIMITS OF THIS MAP

- The prefix scan covers the **top two levels** of `opal-data-assets` plus the named target buckets.
  **There may be gold-shaped trees deeper, or in buckets I did not enumerate** (`opal-data-bd`,
  `opal-data-inf`, `opal-data-cot`, `opal-data-demo`, `opal-data-astn`, `opal-data-pm`,
  `opal-data-portfolio`, `opal-data-imo` were listed but NOT searched for gold prefixes).
  **This is a first-pass map, not a completed census, and the census is workstream 1.**
- Object counts are `s3 ls --recursive | wc -l` at one instant. Timestamps from `s3 ls` render LOCAL;
  none is quoted here as UTC.
- **No claim is made about which of the four MDPF gold trees is authoritative.** `mdpf_revamp` is the
  one the live chain writes (measured today); the others' status is undetermined and determining it
  is part of workstream 1, not an inference from object counts.
