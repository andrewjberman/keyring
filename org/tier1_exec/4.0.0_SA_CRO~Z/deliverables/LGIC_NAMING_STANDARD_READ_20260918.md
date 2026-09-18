# THE LGIC NAMING STANDARD, AS IT IS

**For:** `4.0.0_SA_CRO~Z`, to write the plan against. **Author:** a read-only subagent of that seat.
**Measured:** 2026-09-18, worktree `C:\Users\Opal Bloomberg\Desktop\ajb_workspace`, branch `SITEZ`,
HEAD `c8989376008b7e84ccd34a92acee6cbfcb5d730c`. Last commit touching `infra/logic/02_DOCTRINE.md`,
`lib/opal_naming.py` or `infra/logic/registry/`: `7604292b33f9668258f8faf9f792b0eba5abd9d7`.
Registry vintage: `registry_hash()` = `c1cf1245378355731877cf5f738965769a3136b078445f8cf228028cf4e0ed5c`.
`org/standards/NAMING_SCHEMA.json` **v1.12**. `infra/logic/02_DOCTRINE.md` **v1.1**.

**This document states the standard. It contains no plan and no recommendation.**
Every rule carries `file:line`. Every claim is tagged MEASURED or INFERRED. Every count prints its
denominator. Every absence names the set searched.

**Transcription note:** the canon's text carries non-ASCII glyphs (em dash, arrow, section sign). This
file is ASCII, so in every quote below `--` stands for the em dash and `->` for the arrow. No other
byte of a quote is changed. Line numbers were verified by printing the bytes at each cited line, not by
searching for the quoted string.

---

## 1. THE GRAMMAR, EXACTLY

### 1.1 The key grammar -- what `key()` and `address()` take and return

The canon does not write the grammar by hand. `infra/logic/02_DOCTRINE.md:197-199` says the naming
axis is GENERATED into the canon from `org/standards/NAMING_SCHEMA.json`, and R1 grades against it
(`:149-151`). The generated block is `:201-354`. Its key section is N1:

- `:209` -- `- **grammar:** `{source}/{scope}/{tier}/{table}/{partition}``
- `:213` -- `- **full address:** `s3://{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}``
- `:211` (schema `key.container`) -- the bucket is the key's CONTAINER, `NEVER a segment of the key`
- `:216` -- `- **scope classes:** `FIRM` `PRODUCT` `MASTER` `GLOBAL``
- `:218` -- `- **scope form:** LONG`
- `:219` -- `- **entity id in the scope segment:** REFUSED (doctrine R2)`
- `:220` -- `- **tier, closed list:** `bronze` `silver` `gold` `platinum` `state` `code``
- `:221` -- `- **table case:** snake_case; a NEW platinum leaf is a kebab-case .json file (the served names)`
- `:226-229` -- `- **partition, one of:**` / `date=YYYY-MM-DD` / `a named leaf` /
  `{entity}={id} -- an entity partition; {entity} is the KEY COLUMN's name as the table carries it`
- `:223` -- the `code` tier: `{source}/{scope}/code/{built_tier}/{file}` -- "the table slot carries the
  tier the code builds (bronze, silver or gold)"

The scope rule, `:217`, verbatim (MEASURED, bytes printed):

> `- **scope rule:** a vendor MASTER keeps its own scope (doctrine R3: two masters of one firm are two
> scopes, never commingled -- schwab/08242234/, never schwab/49financial/). For every other key the
> scope is its AUDIENCE: a FIRM when the data is one firm's; global when every firm shares it. A
> PRODUCT key is a scope only beneath a VENDOR source (a feed for the product: pathfinder/etfs), never
> beneath itself as the source -- mdpf/global/..., never mdpf/mdpf/... (SC1, v1.5; the master case
> written at v1.6)`

R1 (`:149-151`) fixes the one further property: the key is **THE SAME STRING IN EVERY BUCKET**,
**source first**, superseding the older "in a per-firm bucket the plane starts at the tier" reading
(`:152-157`). In a firm bucket `{scope}` MUST EQUAL the bucket's firm key; in a product bucket
`{source}` is the product.

### 1.2 `key(source, scope, tier, table, partition)` -- `lib/opal_naming.py:1542-1555`

Five positional arguments, no bucket. MEASURED, the refusals in source order:

| step | source line | what it does | the refusal string |
|---|---|---|---|
| shape | `:1546-1547` -> `_segment` `:1524-1527` | each segment must be non-empty ASCII, no `/`, no outer space | ``<label> must be a non-empty ASCII string with no '/' and no outer space: <repr>`` |
| source | `:1548-1549` | `source` must be a `systems.json` key | ``source <repr> is not a systems.json key`` |
| scope | `:1550` -> `_long_scope` `:1530-1539` -> `lookup` `:226-232` | `scope` must resolve to a **`scopes.json`** row, and must be that row's LONG form | ``scope <repr> resolves to no scopes.json row`` / ``scope <repr> is not the LONG form: pass <long>`` |
| scope-rule | `:1551-1552` | `scope` may not equal `source` | ``a product is never a scope beneath itself (NAMING_SCHEMA.json key.scope_rule)`` |
| tier | `:1553-1554` | `tier` must be in `NAMING_SCHEMA.json key.tier` | ``tier <repr> is not one of NAMING_SCHEMA.json key.tier`` |
| return | `:1555` | `"%s/%s/%s/%s/%s"` | -- |

Registry rows consulted by `key()`: **`systems.json`** (the `{source}` vocabulary, 25 rows) and
**`scopes.json`** (the `{scope}` vocabulary, 9 rows). `tiers.json` is NOT read by `key()`.

### 1.3 `address(source, scope, tier, table, partition, object=None)` -- `:1558-1571`

`address()` is `key()` plus the bucket, and **the bucket is never an argument** (docstring `:1559`;
module header `:15`). The bucket comes from `_home_bucket` `:249-261`:

```
home = reg["tiers"]["homes"][scope_row["tenancy"]][tier]      # :251
  home["home"] == "shared"  -> home["bucket"]                  # :252-253
  home["home"] == "scope"   -> scope_row["bucket"]             # :254-255
  home["home"] == "source"  -> lookup(source, reg)["bucket"]   # :256-260
```

So `address()` consults **three** registry files: `systems.json` and `scopes.json` (through `key()`),
plus **`tiers.json`** for the tier home rule -- and, on a `source`-homed cell, `scopes.json` a second
time for the SOURCE's own bucket. A failure in `_home_bucket` is re-raised at `:1564-1565` as
``no home bucket for tier <tier> of scope <scope>: <exc>``.

`object` (`:1567-1570`) must be a non-empty ASCII string not starting with `/`.

### 1.4 The tier home rule -- `infra/logic/registry/tiers.json`, MEASURED, all 4 tenancies x 6 tiers

| tenancy | bronze | silver | gold | platinum | state | code |
|---|---|---|---|---|---|---|
| FIRM | shared:`opal-data-assets` | shared:`opal-data-assets` | scope | scope | scope | scope |
| PRODUCT | shared:`opal-data-assets` | shared:`opal-data-assets` | scope | shared:`opal-data-portal-v2` | scope | scope |
| COMPOSITE | shared:`opal-data-assets` | shared:`opal-data-assets` | **source** | shared:`opal-data-portal-v2` | **source** | **source** |
| DEMO-TENANT | shared:`opal-data-assets` | shared:`opal-data-assets` | scope | scope | scope | scope |

Denominator: 4 tenancies (the complete key set of `tiers.json` `homes`), 6 tiers (the complete
`NAMING_SCHEMA.json key.tier` list). **Bronze and silver are `shared:opal-data-assets` in 4 of 4
tenancies** -- there is no tenancy today under which `address()` puts bronze or silver anywhere else.
Each cell carries its own `rule:` string naming the doctrine rule it encodes (`tiers.json:11-41`).

### 1.5 `name(system, scope, function, kind, qualifier=None)` -- `:1589-1608`

The resource grammar, doctrine `:256`:

> `- **grammar:** `{system}-{scope}-{function}[-{qualifier}]-{last}``

with `:257` case kebab-case lowercase ASCII, `:258` **scope form: SHORT**, `:261`
`- **last slot:** `kind` by default; `cadence` for `EVENT_RULE`; `cadence` for `SCHEDULE``.
`:268` gives the closed 20-kind list; `:270-289` the node-type-to-kind table; `:291` the closed
4-cadence list plus `on-{event}`; `:293-309` the types NOT graded by kind.

MEASURED refusals of `name()`, in source order:

| step | line | the refusal string |
|---|---|---|
| system | `:1594-1595` | ``system <repr> is not a systems.json key (nor the reserved opal)`` |
| scope | `:1597-1598` -> `_long_scope(..., NAME_SCOPE_CLASSES)` | ``scope <repr> resolves to no scopes.json row`` / ``scope <repr> is a <class> scope; this slot takes FIRM/GLOBAL/MASTER`` |
| function/qualifier | `:1599-1602` | ``<tok> in the function or qualifier is a scope or refused token; pass the scope as scope`` |
| kind | `:1603-1604` | ``kind <repr> is neither a NAMING_SCHEMA.json kind nor a cadence`` |
| `opal` prefix | `:1606-1607` | ``opal before <repr> reads as a null prefix or an unresolved token (GRADING_RULE.md R2)`` |

`NAME_SCOPE_CLASSES` is `("FIRM", "GLOBAL", "MASTER")` at `:1586`. **A PRODUCT scope is refused in a
resource name's scope slot** -- the scope slot takes a firm, the global scope, or a master, and a
shared resource passes `scope=None` and carries no scope token (`:1597`; doctrine `:252`).

Registry rows `name()` consults: `systems.json` (the system vocabulary), `scopes.json` (the scope row's
SHORT form), and through `_vocab()` (`:972-1032`) also `exemptions.json` (the account id) and
`resources.json` (the resource-to-system rows, 91 of them).

### 1.6 The other grammars, doctrine `:311-315`

- `:312` -- `- **bucket:** data `opal-data-{scope}` (LONG); platform `opal-{account-id}-{purpose}`;
  standing shared `opal-data-assets` `opal-data-portal-v2`; a vendor name in a new bucket REFUSED`
- `:313` -- secret `{system}/{scope}/{purpose}`, scope form SHORT
- `:314` -- IAM policy `{system}-{scope}-{purpose}-policy`; duplicate name REFUSED
- `:315` -- log group `/aws/{service}/{resource-name}`, derived

**There is no builder function for a BUCKET NAME.** MEASURED: `lib/opal_naming.py` exposes `key()`,
`address()`, `name()`, `grade()`, `lookup()`, `fence_patterns()`, `registry_hash()`, `build_vectors()`
(module docstring `:6-18`, checked against the `def` census -- 0 of 0 functions named `bucket`). A
bucket name is GRADED by `grade(name, "S3_BUCKET")` (`_grade_bucket` `:1296-1325`) and is otherwise a
registry field (`scopes.json` `bucket`).

---

## 2. THE BUILDERS RUN, ON AMGT_RESAPP-SHAPED INPUTS

Instrument: `scratchpad/lgic_naming/run_builders.py` + `sim_rows.py` + `sim2.py`, importing
`lib/opal_naming.py` by path and calling the functions. READ-ONLY -- these compute strings.
Full transcripts in `builders_out.txt`, `sim_out.txt`, `sim2_out.txt` beside this file.

### 2.1 Every AMGT_RESAPP tier, scope `amgt` -- 5 of 5 REFUSED

```
REFUSED bronze  raw Bloomberg response    -> ValueError: scope 'amgt' resolves to no scopes.json row
REFUSED silver  typed model block         -> ValueError: scope 'amgt' resolves to no scopes.json row
REFUSED gold    drafted document          -> ValueError: scope 'amgt' resolves to no scopes.json row
REFUSED platinum served page payload      -> ValueError: scope 'amgt' resolves to no scopes.json row
REFUSED state   generation pointer        -> ValueError: scope 'amgt' resolves to no scopes.json row
```

Calls made (the exact arguments): `address("bloomberg","amgt","bronze","security_analysis_response","date=2026-09-18","raw.json")`,
`address("bloomberg","amgt","silver","model_block","date=2026-09-18","part-0000.parquet")`,
`address("amgt","amgt","gold","research_draft","date=2026-09-18","research_draft_20260918.parquet")`,
`address("amgt","amgt","platinum","research-app","date=2026-09-18","research-app.json")`,
`address("amgt","amgt","state","generation","generation_id=g-0001","pointer.json")`.

**THE REGISTRY ROW IT WANTS: a `scopes.json` SCOPE ROW keyed `amgt`.** The refusal is raised at
`_long_scope` `:1534` after `lookup()` `:232` finds no row. `amgt` IS a `systems.json` key
(`systems.json` row 5, class PRODUCT, long `asset-management`) -- that is the `{source}` vocabulary,
a different file and a different slot.

### 2.2 The same five, scope `harvest` -- 5 of 5 REFUSED, same refusal

```
REFUSED bronze/silver/gold/platinum/state -> ValueError: scope 'harvest' resolves to no scopes.json row
```

`harvest` is likewise a `systems.json` key (row 25, class PRODUCT, long `harvester-pool`) and **not** a
`scopes.json` row.

### 2.3 The same five, scope `global` -- 3 OK, 2 REFUSED

```
OK      bronze   -> s3://opal-data-assets/bloomberg/global/bronze/security_analysis_response/date=2026-09-18/raw.json
OK      silver   -> s3://opal-data-assets/bloomberg/global/silver/model_block/date=2026-09-18/part-0000.parquet
REFUSED gold     -> ValueError: no home bucket for tier gold of scope global: 'amgt'
OK      platinum -> s3://opal-data-portal-v2/amgt/global/platinum/research-app/date=2026-09-18/research-app.json
REFUSED state    -> ValueError: no home bucket for tier state of scope global: 'amgt'
```

**A finding, not a failure.** `global` carries tenancy COMPOSITE, whose gold/state/code are homed by
**source** (`tiers.json:29,31,32`). `_home_bucket` `:260` therefore calls `lookup(source)` -- and
`lookup("amgt")` raises `KeyError('amgt')`, which `:1564-1565` prints as the bare `'amgt'` at the end
of the message. **So the composite route ALSO wants a `scopes.json` row for the product, this time for
the `{source}` -- because on a COMPOSITE cell the source's row supplies the bucket.**

### 2.4 The same five, scope `49financial` -- 5 of 5 OK (the positive control)

```
OK bronze   -> s3://opal-data-assets/bloomberg/49financial/bronze/security_analysis_response/date=2026-09-18/raw.json
OK silver   -> s3://opal-data-assets/bloomberg/49financial/silver/model_block/date=2026-09-18/part-0000.parquet
OK gold     -> s3://opal-data-49financial/amgt/49financial/gold/research_draft/date=2026-09-18/research_draft_20260918.parquet
OK platinum -> s3://opal-data-49financial/amgt/49financial/platinum/research-app/date=2026-09-18/research-app.json
OK state    -> s3://opal-data-49financial/amgt/49financial/state/generation/generation_id=g-0001/pointer.json
```

This is the discriminator: the builders are not broken and the AMGT-shaped ARGUMENTS are not
malformed. The ONE thing that differs between 2.1 and 2.4 is whether the scope token has a
`scopes.json` row. If AMGT_RESAPP output is firm-attributable, this is already the canon's answer and
it needs no new row at all.

### 2.5 `name()` for AMGT_RESAPP-shaped resources -- 13 OK, 5 REFUSED of 18

```
OK   harvest  scope=None  function=harvest  kind=lambda        -> harvest-harvest-lambda
OK   amgt     scope=None  function=draft    kind=lambda        -> amgt-draft-lambda
OK   amgt     scope=global function=draft   kind=lambda        -> amgt-global-draft-lambda
OK   amgt     scope=49financial function=draft kind=lambda     -> amgt-49f-draft-lambda
OK   bloomberg scope=None function=fetch qualifier=bronze kind=lambda -> bloomberg-fetch-bronze-lambda
OK   amgt     scope=None  function=build  qualifier=gold kind=role    -> amgt-build-gold-role
OK   amgt     scope=None  function=generation kind=table       -> amgt-generation-table
OK   amgt     scope=None  function=research   kind=api         -> amgt-research-api
OK   amgt     scope=None  function=generation kind=queue       -> amgt-generation-queue
OK   amgt     scope=None  function=draft      kind=daily       -> amgt-draft-daily
OK   amgt     scope=None  function=draft      kind=on-silver-landed -> amgt-draft-on-silver-landed
OK   amgt     scope=None  function=read-gold  kind=policy      -> amgt-read-gold-policy
OK   amgt     scope=None  function=amgt       kind=lambda      -> amgt-amgt-lambda
REFUSED system=resapp                -> system 'resapp' is not a systems.json key (nor the reserved opal)
REFUSED scope='harvest'              -> scope 'harvest' resolves to no scopes.json row
REFUSED scope='amgt'                 -> scope 'amgt' resolves to no scopes.json row
REFUSED system=opal function=amgt    -> opal before 'amgt' reads as a null prefix or an unresolved token (GRADING_RULE.md R2)
```

**`name()` is already usable for AMGT_RESAPP today** -- `amgt` and `harvest` and `bloomberg` are all
systems.json keys, and a shared (scope-less) resource needs no scope row. The registry gap bites the
KEY grammar, not the RESOURCE grammar, except where a resource must carry a PRODUCT scope token --
which `NAME_SCOPE_CLASSES` (`:1586`) refuses anyway.

INFERRED (not measured against live AWS): the live names `amgt-resapp-api` and `harvester-box` are not
in this report's measured scope beyond the grade below.

### 2.6 `grade()` on the strings as spelled today

```
amgt-resapp-api                                 API_GW       -> CONFORMANT  canonical=amgt-resapp-api
harvester-box                                   EC2_INSTANCE -> RAISE: R1.f: 'harvester' is in no vocabulary; no registry row resolves it
opal-data-harvest                               S3_BUCKET    -> CONFORMANT  canonical=opal-data-harvest
opal-data-assets                                S3_BUCKET    -> CONFORMANT  canonical=opal-data-assets
opal-data-amgt                                  S3_BUCKET    -> CONFORMANT  canonical=opal-data-amgt
opal-data-asset-management                      S3_BUCKET    -> RAISE: B2: 'asset' after opal-data- is no scope key
amgt/global/gold/research_draft/date=2026-09-18 S3Key        -> CONFORMANT
bloomberg/amgt/bronze/response/date=2026-09-18  S3Key        -> CONFORMANT
```

A RAISE is not a verdict: `:349` says an unplaceable name "is a defect in the tokeniser, this file or
the registry and is fixed there -- it is never filed under one of the three verdicts, and there is no
fourth."

### 2.7 THE GRADER IS WIDER THAN THE BUILDER -- a measured, discriminating pair

The same four strings, through both instruments:

| string | `grade()` | `key()` | `address()` |
|---|---|---|---|
| `bloomberg/amgt/bronze/response/date=2026-09-18` | **CONFORMANT** | REFUSED: no scopes.json row | REFUSED |
| `bloomberg/harvest/bronze/response/date=2026-09-18` | **CONFORMANT** | REFUSED: no scopes.json row | REFUSED |
| `amgt/global/gold/research_draft/date=2026-09-18` | **CONFORMANT** | OK | REFUSED: no home bucket |
| `harvest/global/gold/social/date=2026-09-18` | **CONFORMANT** | OK | REFUSED: no home bucket |

Mechanism, MEASURED at the bytes: `_Vocab.__init__` `:977-978` builds
`self.products` = `systems.json` PRODUCT keys **UNION** `scopes.json` PRODUCT keys. `_grade_key`
`:1392` and `_grade_bucket` `:1304` accept any `v.products` member in the scope slot / bucket suffix.
`key()` `:1550` goes through `_long_scope` `:1532` -> `lookup()` `:226-232`, which reads
**`scopes.json` only**. So a `systems.json`-only PRODUCT key (`amgt`, `harvest`, `irpt`, `advi`,
`yang`) passes the GRADE and is refused by the BUILDER.

Consequence for the commit-time gate: `.tools/naming-gate.py` grades with `grade()` (its docstring
`:4`), so an AMGT key hand-typed as `bloomberg/amgt/bronze/...` **passes the gate today**, while
Rule 30's required `address()` call refuses it. The gate cannot catch this class.

---

## 3. THE SCOPE QUESTION

### 3.1 Is there a scope row for AMGT_RESAPP or `harvest`? NO.

MEASURED, denominator printed: `infra/logic/registry/scopes.json` carries **9** scope rows, the
complete `scopes` array:

| # | key | class | tenancy | bucket | bucket_provisioned | bucket aliases |
|---|---|---|---|---|---|---|
| 1 | `49financial` | FIRM | FIRM | `opal-data-49financial` | true | `opal-data-bd` (routed, provisioned) |
| 2 | `inflection` | FIRM | FIRM | `opal-data-inflection` | **false** | `opal-data-inf` (routed, provisioned) |
| 3 | `cottonwood` | FIRM | FIRM | `opal-data-cottonwood` | **false** | `opal-data-cot` (routed, provisioned) |
| 4 | `demo` | FIRM | DEMO-TENANT | `opal-data-demo` | true | -- |
| 5 | `global` | GLOBAL | COMPOSITE | `opal-data-portal-v2` | true | -- |
| 6 | `08242234` | MASTER | FIRM | `opal-data-49financial` | true | -- |
| 7 | `08335338` | MASTER | FIRM | `opal-data-49financial` | true | -- |
| 8 | `mdpf` | PRODUCT | PRODUCT | `opal-data-mdpf` | true | -- |
| 9 | `etfs` | PRODUCT | PRODUCT | `opal-data-etfs` | true | -- |

**9 of 9 rows listed. No `amgt` row. No `harvest` row. No `resapp` row.** (`scopes.json:12-294`.)

`amgt` and `harvest` DO exist in `infra/logic/registry/systems.json` -- the `{source}`/`{system}`
vocabulary, 25 rows:

- `systems.json:...` row `amgt`: `class PRODUCT`, `long asset-management`,
  `long_basis "org/missions/DIRECTIVES.yaml D5 title 'Asset Management'"`, `owner_directive D5`,
  `owner_claim "measured"`, `owner_basis "... D5 project AMGT_RESAPP; mission tree org/missions/D5/AMGT/"`.
- `systems.json:214-220` row `harvest`: `class PRODUCT`, `long harvester-pool`,
  `long_basis "infra/aws/terraform/harvest/ -- the consolidated harvester terraform module (one box,
  one lambda titled harvester, opal-data-harvest bucket shape)"`, `owner_directive D5`,
  `owner_claim "inferred"`, and an `owner_basis` citing R-6 of
  `SELF_DRIVE_LGIC_RULINGS_20260916.md:213-214`: *"opal-data-harvest LIVE, 132 objects, newest
  social/v1/_measurement/2026-09-15.json (2026-09-15T16:56Z)"*, plus
  `infra/aws/terraform/harvest/main.tf:11-14` and `scoped-amgt-api.tf:12-14`
  (*"main.tf of this module is explicit that harvest/ REPLACES amgt-resapp/tfstate"*,
  Andrew-direct 2026-09-11 ~17:3xZ).

`validate()` emits a WARNING on the `harvest` row (17 warnings, 0 refusals):
``D5 for 'harvest' is inferred, owed a confirmation``.

### 3.2 Is `opal-data-harvest` a registered bucket? NO.

MEASURED, whole-string census over the registry directory: **6 of 6 `.json` files swept; 2 lines carry
the literal `opal-data-harvest`, both in `systems.json` (`:217` `long_basis`, `:220` `owner_basis`),
both PROSE inside a basis string.** Zero occurrences in any `bucket` field, in `tiers.json`, or in
`NAMING_SCHEMA.json` `bucket.standing_shared` (which is exactly
`["opal-data-assets", "opal-data-portal-v2"]`).

Corroborating measurement on a different instrument -- an exhaustive sweep of the builder itself:

> **`address()` returns an `opal-data-harvest` address in 0 of 1350 combinations** (9 scopes x 25
> sources x 6 tiers). The 8 distinct buckets it CAN return, over that same denominator:
> `opal-data-assets` 446, `opal-data-49financial` 300, `opal-data-inflection` 100,
> `opal-data-cottonwood` 100, `opal-data-demo` 100, `opal-data-mdpf` 75, `opal-data-etfs` 75,
> `opal-data-portal-v2` 73. (The row and the column sums differ from 1350 because refused
> combinations are not counted.)

Note the asymmetry with 2.6: `grade("opal-data-harvest", "S3_BUCKET")` reads **CONFORMANT**, because
`_grade_bucket:1304` accepts `harvest` from `v.products` (the systems.json union). The bucket NAME is
gradeable; the bucket is not ADDRESSABLE.

### 3.3 Exactly which rows would have to be added

This section is MEASURED by simulation: the registry was copied into
`scratchpad/lgic_naming/registry_sim/`, rows were added there, `REGISTRY_DIR` was repointed and the
caches cleared, and `address()` was re-run. **The repo registry was never written.**

**(a) ONE `scopes.json` row, `harvest`, class PRODUCT, tenancy PRODUCT, bucket `opal-data-harvest`:**

```json
{"key":"harvest","class":"PRODUCT","long":"harvest","short":"harvest",
 "tenancy":"PRODUCT","bucket":"opal-data-harvest","bucket_provisioned":true,"note":"..."}
```

gives, MEASURED:

```
bronze   -> s3://opal-data-assets/bloomberg/harvest/bronze/security_analysis_response/date=2026-09-18/raw.json
silver   -> s3://opal-data-assets/bloomberg/harvest/silver/model_block/date=2026-09-18/part-0000.parquet
gold     -> s3://opal-data-harvest/amgt/harvest/gold/research_draft/date=2026-09-18/research_draft_20260918.parquet
platinum -> s3://opal-data-portal-v2/amgt/harvest/platinum/research-app/date=2026-09-18/research-app.json
state    -> s3://opal-data-harvest/amgt/harvest/state/generation/generation_id=g-0001/pointer.json
code     -> s3://opal-data-harvest/amgt/harvest/code/gold/build_draft.py
```

`validate()` on the simulated registry: **0 refusals, 17 warnings** (the same 17 `owner_directive`
warnings the live registry carries). The added row is schema-valid.

So ONE row moves **gold, state and code** into `opal-data-harvest`. It moves **bronze and silver into
`opal-data-assets`** and **platinum into `opal-data-portal-v2`**.

**(b) The `harvest` row spelled `amgt` instead -- REFUSED at four of six tiers:**

```json
{"key":"amgt","class":"PRODUCT","long":"amgt","short":"amgt",
 "tenancy":"PRODUCT","bucket":"opal-data-harvest", ...}
```

```
bronze   -> s3://opal-data-assets/bloomberg/amgt/bronze/...          OK
silver   -> s3://opal-data-assets/bloomberg/amgt/silver/...          OK
gold     -> REFUSED: a product is never a scope beneath itself (NAMING_SCHEMA.json key.scope_rule)
platinum -> REFUSED: a product is never a scope beneath itself
state    -> REFUSED: a product is never a scope beneath itself
code     -> REFUSED: a product is never a scope beneath itself
```

Because the derived tiers' `{source}` is also `amgt`. `key():1551-1552` enforces `:217`'s
`mdpf/global/..., never mdpf/mdpf/...`. **A product's derived key may never carry that product as both
its source and its scope** -- the scope must be a different token (`global`, a firm, or a second
product key such as `harvest`).

**(c) The COMPOSITE route -- the `harvest` row with tenancy COMPOSITE, keys written under `global`:**

```
bronze   -> s3://opal-data-assets/bloomberg/global/bronze/...
silver   -> s3://opal-data-assets/bloomberg/global/silver/...
gold     -> s3://opal-data-harvest/harvest/global/gold/research_draft/date=2026-09-18/draft.parquet
platinum -> s3://opal-data-portal-v2/harvest/global/platinum/research-app/date=2026-09-18/research-app.json
state    -> s3://opal-data-harvest/harvest/global/state/generation/generation_id=g-0001/pointer.json
code     -> s3://opal-data-harvest/harvest/global/code/gold/build_draft.py
```

Here `global`'s own tenancy (COMPOSITE) homes gold/state/code by **source**, so the `harvest` row
supplies the bucket through `lookup(source)` `:260`. This is the shape R7's composite branch describes.

**(d) For BRONZE and SILVER to land in `opal-data-harvest`, a `scopes.json` row is NOT enough.**
MEASURED: bronze and silver are `{"home":"shared","bucket":"opal-data-assets"}` in **4 of 4**
tenancies. A scope row selects a tenancy; it cannot change a tenancy's cells. The only registry edit
that produces an `opal-data-harvest` bronze/silver address is a **NEW `tiers.json` tenancy** (or an
edit to an existing one) whose bronze and silver cells are not the shared monolith. Simulated with a
`HARVEST` tenancy whose six cells are all `"home":"scope"`:

```
bronze   -> s3://opal-data-harvest/bloomberg/harvest/bronze/security_analysis_response/date=2026-09-18/raw.json
silver   -> s3://opal-data-harvest/bloomberg/harvest/silver/model_block/date=2026-09-18/part-0000.parquet
gold     -> s3://opal-data-harvest/amgt/harvest/gold/research_draft/date=2026-09-18/draft.parquet
platinum -> s3://opal-data-harvest/amgt/harvest/platinum/research-app/date=2026-09-18/research-app.json
state    -> s3://opal-data-harvest/amgt/harvest/state/generation/generation_id=g-0001/pointer.json
code     -> s3://opal-data-harvest/amgt/harvest/code/gold/build_draft.py
```

`validate()` accepts it (0 refusals). **That tenancy's bronze and silver cells DEPART from R4 and its
platinum cell departs from R6's general-platinum home** -- see s.5 and s.6. `tiers.json:6` states that
each cell's `rule:` cites the doctrine rule it encodes, and `tiers.json:7` states what the file does
NOT say: *"Where a firm's data lives TODAY during the legacy-bucket migration: that is each scope's
bucket aliases (scopes.json, routed and provisioned), not a tier rule."*

**Negative control on the simulation instrument.** A scope row with `"tenancy":"NOSUCHTENANCY"` was
fed to `validate()`, which returned **1 refusal**:
``('scopes.json[9]', 'tenancy', "'NOSUCHTENANCY' has no tier home rule in tiers.json")``.
So the 0-refusal results above are not a constant -- `validate()` can fail on this input class.

**(e) SUMMARY OF THE ROWS.** For `address()` to return an `opal-data-harvest` address:

| tier | rows required | departs? |
|---|---|---|
| gold | 1 `scopes.json` row (`harvest`, PRODUCT, bucket `opal-data-harvest`) | no -- R5 product bucket |
| state | the same row | no -- R21 |
| code | the same row | no -- R16 |
| platinum | the same row **plus** tenancy FIRM or DEMO-TENANT, or a new tenancy whose platinum cell is `scope` | yes if general -- R6 homes general platinum in `opal-data-portal-v2` |
| silver | the same row **plus** a `tiers.json` tenancy whose silver cell is not `shared` | yes -- R4, permitted for GENERAL data with a declared reason under R8 |
| bronze | the same row **plus** a `tiers.json` tenancy whose bronze cell is not `shared` | yes -- R4, and R4's own non-application says **bronze may not** |

The `systems.json` rows for `amgt` and `harvest` already exist and need nothing.

---

## 4. WHAT "TIER READABLE FROM THE PREFIX" REQUIRES

The canon does not state a per-tier prefix grammar. **It states ONE grammar for every tier and every
bucket**, with the tier as its third segment. MEASURED: `NAMING_SCHEMA.json key` carries one
`grammar` string and one `tier` list; there is no per-tier grammar key. So "tier readable from the
prefix" is exactly this:

1. **The tier is the THIRD segment of the key, always.** `:209`
   `{source}/{scope}/{tier}/{table}/{partition}`; `:213` the full address prepends only the bucket.
2. **The tier token is one of a closed list of six.** `:220`
   `bronze` `silver` `gold` `platinum` `state` `code`. `key():1553-1554` refuses anything else.
3. **The same string in every bucket, source first.** R1 `:149-151`:
   > `**R1 -- THE GRAMMAR.** A tier plane is a key in the KEY GRAMMAR rendered in s.3's generated
   > naming section (N1, "A3 NAMING -- THE NAMING SCHEMA, GENERATED") -- **THE SAME STRING IN EVERY
   > BUCKET**, source first.`
   and `:153-157`: **SUPERSEDED ... SOURCE-FIRST everywhere** (Andrew-direct 2026-09-13 ~03:2xZ,
   card 1, *"continuity from our largest monolith bucket."*). In a firm bucket `{scope}` MUST EQUAL
   the bucket's firm key; in a product bucket `{source}` is the product.
4. **`state` is a tier segment, not a tier plane.** R21 `:574-576`:
   > `**R21 -- WORKFLOW STATE IS A FIFTH CLASS, `state/`, NEVER INSIDE A TIER PLANE.** Per-request
   > intake, revisions, attempts, leases, outbox, quarantine, watermarks, parity scorecards,
   > session-trigger modes, OTP state: keyed by request/run, opaque ids, an expiry, under
   > `{source}/{scope}/state/{family}/...` in the bucket whose tenancy the state belongs to.`
5. **`code` carries the tier it BUILDS in the table slot.** `:223`:
   `{source}/{scope}/code/{built_tier}/{file}` -- "the table slot carries the tier the code builds
   (bronze, silver or gold)".
6. **Below the tier, the forms differ by tier.** `:221` a NEW platinum leaf is a kebab-case `.json`
   file; everywhere else the table is snake_case. `:222` a LEGACY served path below
   `{source}/{scope}/platinum/` keeps its bytes, and **membership is data**, read from
   `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json` (`:224`; MEASURED
   PRESENT on disk, 11,887 bytes). `:224` also states the failure mode: while that list is absent,
   `grade()` RAISES on a platinum key whose verdict turns on membership -- "never guessed CONFORMANT
   or OUT-OF-PATTERN".
7. **Nothing but tier data inside a tier plane.** R17 `:532-533`: backups, scratch and probes live
   under a `_backup/` root **outside the grammar**, dated, with an expiry.
8. **No entity identifier in the scope segment.** R2 `:177-179`; `:219` REFUSED. An entity id belongs
   in the key or the partition beneath the tier (`:184`).

**The format each tier's bytes must be in** (axis A5, doctrine `:423-470`) -- this is what makes the
tier segment mean something:

| tier | format law | line |
|---|---|---|
| bronze | RAW and untouched, byte-for-byte; zips stay zips; compact `YYYYMMDD`. **Parquet under `bronze/` is an architectural violation** | R9 `:425-427` |
| silver | typed, deduplicated PARQUET, event-triggered, COMPLETE; hive `date=` partitions; no column slimming, no entity filtering | R10 `:434-437` |
| gold | PARQUET. *"a full history to the extent we have it in nice clean dated/timestamped-in-title parquets and each day we just add a row."* JSON leaves the gold tier | R11 `:447-449` |
| platinum | JSON, and the publisher is the estate's ONLY JSON producer; every platinum publisher READS PARQUET and writes JSON | R12 `:462-464` |

---

## 5. THE CLIENT-ASSETS QUESTION, MEASURED AGAINST THE TEXT

Andrew has ruled. This section only prints the two passages and their lines. It adjudicates nothing.

### 5.1 Where the doctrine says "every source, every scope, every time"

`infra/logic/02_DOCTRINE.md:358-359`, verbatim at the bytes:

> `**R4 -- BRONZE AND SILVER HAVE ONE HOME: `opal-data-assets`.** Every source, every scope, every`
> `time. This is the ingest spine; it is what "consolidation" meant.`

Its authority line `:360-362` cites Andrew-direct 2026-07-13 ~23:55Z (*"bronze raw, silver parquet ...
into a dedicated opal-data-assets bucket"*), 2026-08-25 ~17:55Z (*"SILVER ... in opal-data-assets
(unchanged)"*), Rule 17b @`dd9b33de65`, and `3fd386598f` s.3.0.

### 5.2 Where the doctrine scopes that mandatory home to client-confidential data

**Three places, all MEASURED at the bytes.**

**(i) R4's own non-application, `:367-368`:**

> `- non-application: none for client data. For general data, silver may sit in the product bucket`
> `  under R8 with a declared reason; **bronze may not.**`

(the leading `-` is the canon's middle-dot bullet, transcribed).

**(ii) R8, `:414-416`:**

> `**R8 -- GENERAL DATA: TIER LAW HOLDS, ONE AXIS IS FREE.** For general data, every tier that exists`
> `obeys R9-R12; **bronze still lands in `opal-data-assets`** (R4); everything ABOVE bronze may live in`
> `the product bucket **with a declared reason** (R20).`

and its non-application `:421`: `- non-application: client-confidential data (R4-R7 bind, no free axis).`

**(iii) R14's grid, `:500-503`:**

> `| | **served as-ingested** | **derived** |`
> `|---|---|---|`
> `| **general** | bronze -> serve. No silver/gold/platinum REQUIRED. (Pathfinder, TrueShares --
> CORRECT, not debt) | bronze -> silver -> gold -> platinum in `opal-data-portal-v2`.
> **RECOMMENDED** (R8's free axis applies). |`
> `| **client-confidential** | bronze -> silver -> serve from the firm bucket | bronze + silver in
> `opal-data-assets`; gold + platinum in the firm bucket. **MANDATORY.** |`

R14's own heading `:497-498` calls it **THE rule**: *"every other rule says what conformance IS, this
one says whether it is required."*

### 5.3 The two passages read side by side

R4's imperative is unqualified in its own sentence -- **"Every source, every scope, every time"**
(`:358`). The qualification lives in R4's non-application line ten lines later (`:367-368`), in R8
(`:414-416`) and in R14's grid (`:500-503`), and it is ASYMMETRIC between the two tiers:

- **SILVER**, for GENERAL data: may leave `opal-data-assets` for the product bucket, **with a declared
  reason** under R20. A declared departure reads `DECLARED-EXCEPTION`, which the canon ranks
  immediately above `CONFORMS` (`:120`, `:125-128`): *"a declared departure is the pattern working,
  not failing."*
- **BRONZE**: **`bronze may not`** (`:368`), **`bronze still lands in opal-data-assets`** (`:415`),
  and R4's census/non-application gives no general-data carve-out for it. R9 `:432` reads
  `non-application: none`.

So on the text as written, moving SILVER into `opal-data-harvest` for general data is a declared-
exception path the canon names; moving BRONZE there is a departure the canon's R8 free axis does not
reach, and under R20 `:559-564` it is therefore either a declared departure Andrew acknowledges or a
`VIOLATES`. **INFERRED, and flagged as such:** whether AMGT_RESAPP's bronze is "general" is a
classification this report did not measure -- s.1's vocabulary line `:69` lists "market, ETF,
harvest, a de-identified composite" as general, and `:68` defines client-confidential as data
attributable to one firm at any grain.

R7 `:401-406` is the rule that decides which of the two a slice is:

> `**R7 -- ATTRIBUTABILITY DECIDES TENANCY, NOT PIPELINE SHAPE.** (a RANGE)`
> `- A slice ATTRIBUTABLE to one firm -- at ANY grain, account, relationship, or firm-level aggregate --`
> `  is that firm's data: **firm bucket, gold AND platinum, MANDATORY.**`
> `- A CROSS-FIRM COMPOSITE attributable to no single firm (a "global" row, a de-identified aggregate):`
> `  **product-bucket gold, `opal-data-portal-v2` platinum, PERMITTED** -- with the de-identification`
> `  basis written as a register entry (R20).`

`:412` -- `non-application: none -- this rule exists precisely for the case the single rule did not cover.`

### 5.4 Two further rules the CRO's plan will meet

- **R19 `:550-552`** -- `**R19 -- A MIGRATION IS ITS OWN PROJECT.** The canon classifies; it never
  moves. Each pipeline family reaches conformance in a separate project following MAP -> CLASSIFY ->
  RULE -> PORT -> REPOINT -> PROVE, with never-widen sign-off on every served key that moves.`
  `:556` -- `non-application: none.`
- **CLAUDE.md Rule 30 `:359-369`** -- `**EVERY NEW PIPELINE IS BUILT TO LGIC** ... Every S3 address is
  `lib/opal_naming.py address()` output and every resource name is `name()` output; **a builder
  REFUSAL is a missing registry row to add (`infra/logic/registry/`), never a hand-typed workaround**;
  a deliberate departure is an R20 register entry Andrew acknowledges.` Its NON-APPLICATION `:368-369`:
  `existing pipelines -- each reaches conformance through its own migration project (R19), never as a
  rider on unrelated work.`

---

## 6. THE EXCEPTION REGISTER -- schema, entries, and a declared reason in practice

### 6.1 The schema, `infra/logic/02_DOCTRINE.md:587-588`

> `Schema (absorbed at v1.0 from `D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md` s.6 -- provenance, not a
> pointer; Rule 24 four-postulate act):`
> ``pipeline . axis (A1-A5) . the exact departure . WHY . acknowledged by . when . PERMANENT |
> CONDITIONAL (condition)``

`:590-600` adds: exceptions are SOVEREIGN-ACKNOWLEDGED and recorded with detail; every entry states
PERMANENT or CONDITIONAL and a CONDITIONAL entry states the condition that would end it; and
**the entries have ONE carrier, `06_CONFORMANCE_LEDGER.md` s.6** (`:598`), "because two carriers of one
list drift."

### 6.2 The entries that exist -- 8 of 8, `infra/logic/06_CONFORMANCE_LEDGER.md:135-142`

| id | pipeline | axis | departure | kind | state |
|---|---|---|---|---|---|
| X1 | MDPF (Orion JWT) | A1 | reads `opal-data-inf/orion/jwt/current.json` | PERMANENT | GRANTED |
| X2 | MDPF `global/` | A2 | cross-firm composite gold in product bucket, platinum in portal-v2 | PERMANENT | GRANTED |
| X3 | ETFs | A2 | silver/gold/platinum in `opal-data-etfs` | CONDITIONAL | **OWED** |
| X4 | Pathfinder, TrueShares | A2/A5 | no gold, no platinum | PERMANENT | GRANTED |
| X5 | ETFs platinum | A5 | csv/html/pdf under `platinum/` | CONDITIONAL | **OWED** |
| X6 | `opal-data-demo` | A2 | a demo tenant, neither firm nor general | PERMANENT | GRANTED |
| X7 | MDPF 49financial `category-views.json` | A2 | firm-attributable platinum stays in portal-v2 | CONDITIONAL | GRANTED |
| X8 | Portal sign-in, 4 partner DynamoDB tables | A3 | the table NAME departs from the resource grammar | CONDITIONAL | GRANTED |

Denominator: 8 rows, the complete table at `:135-142`. Audit rule `:144-145`:
*"every CONDITIONAL entry is re-read when its condition's owner reports; an entry whose condition has
expired is a VIOLATION again, not a grandfathered exception."*

### 6.3 A declared reason in practice -- the R8 free-axis row is the one that is OWED

**The single register entry that is exactly the R8 free-axis case is X3, and it has NO reason
written.** `06_CONFORMANCE_LEDGER.md:137`, verbatim:

> `| X3 | ETFs | A2 | silver/gold/platinum in `opal-data-etfs` | R8 free axis -- reason owed | -- .
> decider: Andrew (R20: every exception is sovereign-acknowledged; not yet acknowledged) | CONDITIONAL
> . condition: the R8 free-axis reason is written into this row and Andrew acknowledges it (doctrine
> s.4: *"CONDITIONAL on the reason being written"*); until then s.3's three `opal-data-etfs` rows read
> WAITING . owner: Andrew | **OWED** |`

So the estate's ONE precedent for "general data above bronze in a product bucket with a declared
reason" is an entry whose reason is still owed, and whose three ledger plane rows read WAITING because
of it. MEASURED at `:137`.

**The closest GRANTED example of a written reason is X2**, `:136`, verbatim:

> `| X2 | MDPF `global/` | A2 | cross-firm composite gold in product bucket, platinum in portal-v2 |
> R7 composite branch -- basis written: aggregate counts/status/dates only, no account identifiers
> (`MDPF_TAXSMA_DATA_CONTRACT.json` `categories.wire_privacy`) | Andrew-direct 2026-09-15 ~14:4xZ,
> "RECS APPROVED" (card E2) . decider: Andrew -- decided, recorded @`9cf4a274db` | PERMANENT |
> **GRANTED** |`

**What a declared reason looks like, read off X2:** the WHY names the RULE BRANCH it travels
(R7 composite), states the SUBSTANTIVE basis in one clause ("aggregate counts/status/dates only, no
account identifiers"), and **cites an artifact that can be checked** (`MDPF_TAXSMA_DATA_CONTRACT.json`
`categories.wire_privacy`) -- not a description of intent. The acknowledgement carries Andrew's own
words, a timestamp, the card number and the commit the record landed at. X7 `:141` shows the
CONDITIONAL form: its condition names the event that ends it ("holds only until MDPF_CANON repoints
`platinum/mdpf/{firm}/` to the firm bucket; after that this key is a VIOLATION again") and names an
OWNER whose report triggers the re-read.

---

## 7. THE SUPPORTING REGISTERS, AS THEY STAND ON `harvest` AND `amgt`

- **`infra/logic/05_IDENTITY_SPINE.md:77`**, the PRODUCTS table, verbatim:
  > `| `harvest` / `find` | `imo` (bucket `opal-data-imo`, 304 per-company planes, dead 103d) .
  > `opal-data-harvest` (53 objects, no tier planes) | -- | UNRESOLVED: tick-list row 18; whether
  > `imo` is a product, a vendor, or retired is a word |`

  `:42` gives the PRODUCT key form: *"lowercase, the bucket suffix form"*, minted by **Andrew**
  (D10-1 per instance), examples `mdpf`, `etfs`. `:41` gives the FIRM key form, also Andrew's word.
  `:55` invariant 4: *"retiring an alias does not move data; adding a firm does not create a bucket.
  Each is its own act with its own owner."*

- **`infra/logic/04_SCOPE_TICKLIST.md:66`**, row 18, verbatim:
  > `| 18 | `opal-data-imo` | 304 per-company planes (R2 VIOLATION), 8,700 objects, **103d dead** |
  > no -- insurance-market prospecting data | PRODUCT (-> harvest/find) -- or RETIRE | -- |
  > x RETIRE (card 9) |`

  `:14-16` and `:70`: the table was TICKED 2026-09-13 ~01:3xZ, *"Nothing on this table is open."*
  **`opal-data-harvest` itself is not a row on this table** -- 19 rows, denominator printed at
  `:26-41`; the table's population was every `{source}/{scope}` pair in the monolith plus every bucket
  carrying a TIER PLANE, and `opal-data-harvest` carries none (`05_IDENTITY_SPINE.md:77`: "53 objects,
  no tier planes"). `:13`: *"Ticking a row classifies it for the ledger. It moves nothing."*

- **`infra/logic/09_NAMING_CENSUS.md`** is the resource-name census (2,531 live nodes, 33 node types,
  measured 2026-09-13 ~03:3xZ; header `:3-8`). Its headline `:20-27`: the separator (kebab, lowercase)
  and the order (`{system}-...-{kind}`) are settled; `:28-36`: **"the disorder is in the VOCABULARY,
  not the order"** -- 118 distinct first tokens with no registry saying which are systems. `:10-14`
  states what it cannot see: Terraform labels, and **the S3 KEY grammar per bucket** (cited from
  `01_CENSUS.md`, not re-measured here).

- **`infra/logic/07_ROUTING_REDERIVATION.md:15-22`** is the ADVI routing clause re-derived on the
  applied plane. Doctrine `:629-631` still carries it as UNRULED (`decider: 1.0.0_SA_CTO`), so R6
  rests on its storage half only. Not a naming surface; noted so the CRO does not read it as one.

---

## 8. THE ENFORCEMENT SURFACES, AND ONE MEASURED STALENESS IN RULE 30

- **`.tools/naming-gate.py`** -- the commit limb, called from `.tools/safe-commit.sh:682-708`. It
  grades the ADDED lines of the diff with `grade()` and applies DEC-6's matrix (docstring `:4-16`):
  NEW + OUT-OF-PATTERN -> REFUSE; NEW + ALIAS -> REFUSE; EXISTING + touched + ALIAS -> WARN;
  EXISTING elsewhere + OUT-OF-PATTERN -> WARN; CONFORMANT -> pass; a hand edit to a GENERATED file ->
  REFUSE. Its CONTEXT RULE (`:22-28`): a firm or product token is PERMITTED inside the arguments of a
  `key()`, `address()`, `name()` or `lookup()` call (read from the Python syntax tree), in the registry
  files, in a generated block, or inside an `opal_name` Terraform module call -- **anywhere else a
  string carrying one is a HAND-KEPT CARRIER**, refused when NEW.
- **`.tools/naming-apply-gate.py`** -- the `safe-apply` limb, two modes (`:3-12`): PRE-PLAN DIR mode
  never refuses; PLAN mode (`--plan-json`) refuses a REFUSE-worthy grade on a resource being ADDED.

**MEASURED STALENESS.** CLAUDE.md Rule 30 `:367` says *"the commit-time naming gate grades names
(WARN today, LGIC_ENFORCE)"*. The enforce switch **exists on disk and is tracked in git**:
`org/mcp/naming-gate.enforce`, 614 bytes, committed `d181e0ac5a` on 2026-09-17 by
`2.0.0_SA_COO~G`. `safe-commit.sh:691` reads exactly that path. Its own text:

> `LGIC_ENFORCE issuer act 2b (round-1 RULING ADD, G-F), flipped by 2.0.0_SA_COO~G on 2026-09-17.`
> `Preconditions, measured before the flip:`
> `- cell 2 (EN-n-1, the gate's domain) drained @1f9b7ea157, 9 of 9 mechanical criteria re-run PASS by the issuer.`
> `- plan-mode limb, --enforce, over the 68 planned roots of LIMB_ROOTS_CENSUS.r3.md (72 roots, 4 not planned):`
> `  61 PERMIT, 7 REFUSE; 1590 names graded; 16 names refused, 16 of 16 on a create/update action,`
> `  0 refusals of an existing resource. Positive control: a root's no-ops flipped to create -> REFUSE (rc 1).`
> `Remove this file to return the naming limbs to WARN.`

**So the naming limbs are ENFORCING, not WARN.** Rule 30's parenthetical is one day stale as of this
measurement.

---

## 9. WHAT THIS DOCUMENT DOES NOT CLAIM

- **It did not touch AWS.** Every object count, liveness fact and bucket-existence claim here is quoted
  from a registry or a canon document with its own vintage, not re-measured. `opal-data-harvest`
  "LIVE, 132 objects, newest 2026-09-15T16:56Z" is `systems.json:220` quoting
  `SELF_DRIVE_LGIC_RULINGS_20260916.md:213-214`; "53 objects, no tier planes" is
  `05_IDENTITY_SPINE.md:77`, an older reading. The two disagree on count and neither was re-taken.
- **It did not classify AMGT_RESAPP's data.** Whether its slices are client-confidential or general is
  the R7 `:401-406` test applied to facts this report did not measure. The parallel subagent is
  measuring the data shapes.
- **It graded no live resource except the eight strings in s.2.6**, which were typed by hand as
  plausible spellings, not read from AWS.
- **The simulations in s.3.3 wrote only to
  `scratchpad/lgic_naming/registry_sim/` and `registry_sim2/`.** `infra/logic/registry/` was not
  modified; `registry_hash()` at the top of this document is the live value.
- **It adjudicates nothing.** Andrew has ruled on where bronze and silver run and on what
  `opal-data-assets` is for; s.5 prints the canon's text beside that ruling and stops.
