# LGIC_ENFORCE -- the executable layer: one registry, two builders and one flagger, so a name the rule would not have produced cannot be minted

```json
{
 "project": "LGIC_ENFORCE",
 "directive": "D14",
 "fabric": "laptop",
 "prd_version": "v1.0",
 "step": 4,
 "brief_ref": "docs/briefs/d14-executable-layer-brief-20260913.md@fc2a1ba75f",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "RATIFIED"
}
```

**Brief:** `docs/briefs/d14-executable-layer-brief-20260913.md` @`fc2a1ba75f`, author `4.0.0_SA_CRO~D`.
- Its later touch @`9ba5e5370d` is a one-line diff, and that line is the REFS `PROJECT` line.
- It has 8 top-level headings plus `## REFS TO CARRY`, which gives the 24 coverage entries below.

**Endpoint:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md`.
- Cut @`033b41c089`; its ruling stamps are @`e2210bf34c`.
- Andrew confirmed the DONE WHEN lines 2026-09-13 ~18:4xZ.

**Registration and order:**
- Registered @`f25395446e` under D14/LGIC, on the macro ratified @`464c1096d5`.
- **Counterpart:** `LGIC_NAMING`. Its PRD v1.2 is ADMITTED (brief half @`0114f04692`, ratified-text half @`0255660cae`). Its data file `org/standards/NAMING_SCHEMA.json` v1.2 is the schema this project executes.
- **Sequence** (`org/missions/SEQUENCE.yaml` v1, stage 1): this project waited on LGIC_NAMING's admitted PRD, and that gate is met. This project's own admitted PRD is the first half of the hold on `ADVI_FIRMBKTS` (held at DECOMP) and `MDPF_CANON` (held at REGISTERED). The second half is DEC-4's fence, applied on the template.

**Rulings this PRD executes, verbatim anchors:**
- The commission (Andrew ~03:0xZ / ~03:2xZ, relayed 96332): *"key/name builders off the identity spine, a flagger at safe-commit/safe-apply"*. The dependency is (b)-minimal, and enforcement comes at AUTHORING time first, runtime later.
- Remediation shape (a) (~03:5xZ, record @`38f2268d48`): D14 owns the rule, the registry, the builders and the flagger, and every fix is minted where the resource lives.
- The short forms `49f`, `inf` and `cot`, with `bd` refused in every slot (~03:5xZ card 2). The per-slot split is LGIC_NAMING S4.
- **THE FENCE** (~18:4xZ card 1): *YES, on three conditions that are ACCEPTANCE*. They are closed in writing at DEC-4.
- DONE WHEN confirmed as cut (~18:4xZ card 4).
- The monitor moratorium stands. Every refusal here is a gate's exit code and a printed line, and nothing in this project sends a message.

**The ENDPOINT section below is the endpoint's outcome block verbatim, except for two removals:**
- FWD-2's `DEPENDS` line. Both of its items are closed: the fence re-derivation was ruled YES on three conditions (DEC-4), and the form split is ratified at LGIC_NAMING S4.
- Three `(s.N)` pointers into the endpoint file's findings, which this PRD does not carry.

The precedent is `3.0.0_SA_CVO`'s revised correction 1 on LGIC_NAMING v1.2.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A pipeline never writes out where its data goes; it asks for the address
         and is given it
         DONE WHEN  EXERCISED -- a new pipeline for a new firm has been written this
                    way and a reviewer has checked it
         ACCEPT     a new pipeline for a firm never set up before is written without a
                    single storage location typed into it by hand, and a reviewer can
                    confirm that by searching its code -- where today every pipeline
                    carries a settings file with a storage location typed into it
         SOURCE     brief Part I O1; bar Part III O1

  FWD-2  Nobody creating infrastructure types its name; it is produced from one rule,
         and the rule keeping firms apart is produced from the same source
         DONE WHEN  EXERCISED -- a real piece of infrastructure has been named this way,
                    and the separation rule was produced from the same source and matched
         ACCEPT     someone setting up a new piece of infrastructure has its name produced
                    for them rather than typing it, and the rule keeping one firm's systems
                    away from another's comes from the same source -- so changing how a firm
                    is spelled changes both at once -- where today the name is typed by hand
                    and the separation rule is a separate hand-kept list of spellings
         SOURCE     brief Part I O2 -- NO Part III bar; cut from Part I alone

  FWD-3  Everything that needs to know where a firm's data lives reads it from one
         list, and moving a firm is one change to that list
         DONE WHEN  EXERCISED -- someone has changed one firm's entry and watched every
                    dependent place follow in a single build
         ACCEPT     someone changes where one firm's data lives in a single list, and in one
                    build every place that routes, guards or maps that firm's data follows;
                    the five separate lists kept by hand today are either produced from the
                    one list or gone
         SOURCE     brief Part I O3; bar Part III O3

  FWD-4  Any change that writes a storage address or a name the rule would not have
         produced is stopped, and the stop says what the correct form is
         DONE WHEN  EXERCISED -- a deliberately wrong change has been stopped with the
                    correct form printed, and a correct one let through
         ACCEPT     someone tries to save a change containing a hand-typed old-style storage
                    address and it is refused, with the correct address printed in the
                    refusal; the same change written correctly goes through; and an old
                    spelling that is still permitted goes through with the correct spelling
                    printed beside it, so existing work keeps running -- where today the only
                    such check is a hand-kept list that stops protecting the moment a name
                    changes
         SOURCE     brief Part I O4; bar Part III O4

  FWD-5  Anyone can run the check over the whole estate and get the complete ranked list
         of names and addresses that break the pattern, each with its fix
         DONE WHEN  EXERCISED -- the full run has been done and its totals compared with
                    the hand-made ranking
         ACCEPT     someone runs the check over everything -- the stored code and what is
                    actually running -- and gets a ranked list of every name and address that
                    breaks the pattern, each paired with its correct form, totals shown; the
                    totals agree with the ranking the naming work produced by hand; and a name
                    the check cannot read stops the run loudly rather than being filed as
                    breaking the pattern -- this is the list clean-up projects start from
         SOURCE     brief Part I O5; bar Part III O5; CARRIES the naming endpoint's FWD-5
                    machine-run bar

  FWD-6  A clean-up project cannot quietly stall half-done
         DONE WHEN  EXERCISED -- shown deliberately on a practice copy, with a clean-up
                    planted for the purpose
         ACCEPT     on a practice copy, a clean-up is set up that owns one area still
                    holding an old-style name, and a change touching that area without
                    removing the name is refused -- driven on purpose rather than waiting for
                    a real clean-up to stall; the first real clean-up project doing the same is
                    the confirmation, never the proof -- where today "we meant to fix it"
                    becomes a forgotten ticket
         SOURCE     brief Part I O6 -- NO Part III bar; cut from Part I alone

  FWD-7  Taking on a new firm is one entry in one list, and everything else is produced
         from it
         DONE WHEN  EXERCISED -- a demonstration firm has been added on a practice copy and
                    every produced file checked
         ACCEPT     on a practice copy, a demonstration firm is added as a single entry and
                    every file that ought to change does, exactly as expected; and anywhere
                    someone types that firm's name by hand instead, the change is refused --
                    where today every new firm means editing its name into many places by hand
         SOURCE     brief Part I O7; bar Part III O7
```

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| `org/standards/NAMING_SCHEMA.json` | **consumed** | the closed enumerations: the key grammar, container and leaf; bucket forms; resource grammar and last-slot rule; `kind.by_type` and `types_not_graded_by_kind`; cadences; secret, log-group and policy forms; `firm_forms`; `refused_tokens`; system classes; the grade signature and its three verdicts | produced by `LGIC_NAMING` (v1.2, admitted). `key()`, `name()`, `grade()` and the generator read it at run time and never copy it, so an enumeration has one owner |
| the grading rule, `(name, type) -> (verdict, canonical_form)` | **consumed and EXECUTED** | three verdicts, CONFORMANT / ALIAS / OUT-OF-PATTERN, and no fourth. An unplaceable name or an unresolved token RAISES | produced by `LGIC_NAMING` as a written, hand-applied rule (its cell N2). This project's `grade()` is its machine. A disagreement between them on any of N2's worked cases is a defect in one of the two, graded against N2 |
| the identity registry's ROWS | **produced** | `infra/logic/registry/*.json` (DEC-1): systems, scopes with their long and short forms and aliases, the tier home rule, exemptions, remediations. Their shape is the schema's; this project mints the rows | consumed by the builders, the generated views, the fence and the flagger. Seeded from `infra/logic/05_IDENTITY_SPINE.md`, which stays the human-readable view |
| the source-first key string | **consumed** (ruled) | `{source}/{scope}/{tier}/{table}/{partition}`, verbatim. The bucket is the key's CONTAINER and never a segment of it, and `{object}` is the LEAF under `{partition}` | ruled by Andrew ~03:2xZ. `key()` produces exactly it. The first callers are `ADVI_FIRMBKTS` and `MDPF_CANON` |
| `lib/opal_naming.py` | **produced** | `key(source, scope, tier, table, partition)` returns a full address, with the bucket taken from the tier home rule and the scope's tenancy, never from an argument. `name(system, scope, function, kind, qualifier=None)` takes the LONG scope and emits the SHORT form (S4); `scope=None` is a shared resource (S5). `grade(name, type)`. The standard library only | producers (pipelines), the Terraform module (through a shared vector file), the flagger, census mode |
| the generated views | **produced** | one file per carrier at the carrier's existing path, headed GENERATED with its registry hash. The first generation is byte-equivalent in what it exports | the edge router, the IRPT scripts, the IR authz loader, the perfrp pin and the precommit's cross-firm lists (DEC-5) |
| the fence patterns | **produced** | per firm bucket, the registry-derived allow set of DEC-4 | `infra/aws/terraform/shared-infra/s3-49financial.tf`, the template; and every bucket minted from it by `ADVI_FIRMBKTS` |
| the flagger's verdict line and kill switch | **produced** | `NAMING <verdict> <file>:<line> <string> -> <canonical>`. `org/mcp/naming-gate.enforce`: present means enforce, absent means warn only. Every verdict is logged | every committing seat, through `safe-commit`; every applying seat, through `safe-apply` |
| the census report | **produced** | ranked rows of (current, canonical, verdict, type, plane), with denominators | the remediation projects minted under ruling (a): D8 for keys, D12 for infrastructure |

`LGIC_NAMING`'s CONTRACTS (v1.2) states the first four rows from its own side, and the two tables agree row for row.
The one change of direction is intended: the registry rows are consumed there and produced here.

## THE DECISIONS -- CLOSED AT L4

- **DEC-1 The registry is JSON, in `infra/logic/registry/`.** The brief's IV.7 proposed YAML. JSON is read by the
  standard library in the commit gate, the Lambda runtime and the edge build, with no dependency. Bare python on this
  shell has no PyYAML, and that is how a gate fails at import.
  - The files are `systems.json`, `scopes.json`, `tiers.json`, `exemptions.json` and `remediations.json`:
    - `scopes.json` rows: key, class, long, short, tenancy, bucket, aliases.
    - `tiers.json`: tier to home rule per tenancy (R4-R7, R16, R21).
    - `exemptions.json`: per firm bucket, each exempt principal with its reason and sign-off reference.
    - `remediations.json`: per remediation project, its owned surfaces and ranking row.
  - **There is no kinds file.** Kinds and cadences are closed enumerations owned by `NAMING_SCHEMA.json`, and a copy
    here would be a second carrier.
- **DEC-2 The builders.** `lib/opal_naming.py`, standard library only.
  - `key()` has no bucket parameter, so the per-firm fork the brief's O1 describes cannot be written.
  - `name()` raises on a refused token and omits the scope slot when `scope=None`.
  - `grade()` implements the written rule exactly.
  - `generate` writes the views, and `census` is DEC-7.
- **DEC-3 Terraform has no plan-time program.** There is no `external` data source. The generator writes a locals file
  (firm short and long maps, bucket names, the fence's pattern lists) into `infra/aws/terraform/modules/opal_name/`,
  whose name output is HCL `format()` over those maps. It is proved against `lib/opal_naming.name()` on a vector file
  the Python builder generates, so the two builders cannot drift apart silently.
- **DEC-4 THE FENCE -- ANDREW'S THREE CONDITIONS, CLOSED IN WRITING.** Today `DenyForeignFirmPrincipals` in
  `s3-49financial.tf` (`:93`) denies an enumerated list: `role/cot-*`, `role/inf-*`, `role/mdpf-*` and
  `role/opal-assets-mdpf-*`.
  - **(i) The no-scope branch.** A firm bucket's Deny applies to every principal EXCEPT two:
    - a principal whose resource-name scope slot is THAT firm's short form;
    - a principal `exemptions.json` names for that bucket.

    So a principal carrying no scope token, which is legitimate for a shared resource under S5, is DENIED unless it is
    named. The reason: condition (ii), *"every existing writer holds a scoped identity or a named exemption first"*, has
    content only under a deny-by-default reading. Let unscoped principals through by default and (ii) is vacuous, and
    every future shared role reaches every firm's bucket.
  - **(ii) Existing writers first.** Before the Deny lands, cell E1 enumerates every principal that read or wrote each
    firm bucket in a stated window, from the CloudTrail data events card 3 made live on opal-data-bd, -inf, -cot and
    -49financial (validated @`231cd62ec5`), together with every principal the current policy and the role-side belts
    name.
    - Each one is re-identified with a scope token or named in `exemptions.json`.
    - One is known already: the template's own comment names `bd-gold-layer-runner`. It is a legacy principal
      carrying the refused token `bd`, and it must read silver outputs into gold.
    - The apply carries never-widen sign-off (CTO and COO, NEVER #1). The sign-off names every principal whose access
      changes, and the rollback: the prior policy document, kept verbatim in the change-management ledger entry.
  - **(iii) The service-principal exemptions are rows of `exemptions.json`, and the policy's list is generated, never
    typed.**
  - Route (a) of 2026-09-12, a carve-out for one principal, stays closed.
  - The four legacy patterns leave the template only when the derived set covers them.
  - **It is proved by REAL probes, never by `simulate-principal-policy`, which does not evaluate a resource policy.**
- **DEC-5 The carriers become generated views.** Measured at HEAD @`3f3b5337a1`, `comp-find` returned 5 definitions
  across 14,242 files:
  - `data/firm_registry.json`
  - `infra/aws/lambda-edge/_shared/firm-config.mjs:65` `FIRM_CONFIG`
  - `firm_bucket_map()` at `data/assets/scripts/gold/investor_reporting/directory_runner.py:170`
  - `firm_bucket_map()` at `holdings_snapshot.py:145`, in the same directory
  - `infra/aws/lambda/investor-reporting/_authz/loaders.py:43` `bucket_for`
  - `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py:57` `resolve_firm`
  - the precommit's `_CROSS_FIRM_FOREIGN_BUCKETS` (`.tools/ds-precommit-check.py:68`)
  - the precommit's `_CROSS_FIRM_FOREIGN_KEY_PREFIXES` (`:110`)

  Each becomes a generated file at its existing path, or its duplicate is deleted in favour of one generated module.
  - The first generation is BYTE-EQUIVALENT in what it exports. That is DELTA=0 on the served plane, which needs no
    never-widen hold.
  - Cell E1 first re-derives the whole carrier population by an unscoped read, because these are the brief's measured
    set. At least one carrier outside them is already named in the precommit's own comment: `comp-secrets`' firm
    pattern.
  - **Repointing the consumers that compute a firm's location in their own code is `ADVI_FIRMBKTS` FWD-3's** (the
    endpoint's s.2, ruling (a)). This project generates the lists and makes a hand edit refusable.
- **DEC-6 The flagger's matrix.** The brief's IV.5 is ratified, and its grain is stated. A string is NEW when it is on
  the diff's added lines and absent from the same file's pre-image; otherwise it is EXISTING.

  | the string is | verdict | the gate |
  |---|---|---|
  | NEW | OUT-OF-PATTERN | REFUSE, canonical printed |
  | NEW | ALIAS | REFUSE, canonical printed (a new name never mints an alias; `bd` is the case) |
  | EXISTING, touched | ALIAS | WARN, canonical printed |
  | EXISTING, in a surface `remediations.json` assigns to a live remediation | OUT-OF-PATTERN | REFUSE unless the diff removes it |
  | EXISTING, anywhere else | OUT-OF-PATTERN | WARN, canonical printed |
  | any | CONFORMANT | pass |
  | a hand edit to a generated file | -- | REFUSE: its bytes must equal the generator's output |
  | any | RAISE | printed as a rule or registry defect, never as a verdict, and refused like any refusal once enforcing |

  - **Inputs:**
    - S3 key and bucket literals
    - the resource-name attributes of changed `.tf` files, including those the Terraform-label census names
    - secret paths
  - **NOT graded:** prose, comments, and fixtures under `*/tests/*`, because a test must be able to hold a known-bad
    string as its positive control.
  - **The printed canonical fills every slot the grader can resolve, and names the slot it cannot.** For
    `opal-data-inf/silver/x`, that slot is `{source}`, unless the producer declares its source. It never guesses.
  - **WARN-ONLY FIRST,** for 7 days AND at least 200 graded strings, whichever is later. The false-refusal count is
    printed with its denominator, and the flip to REFUSE is announced to live seats before it is armed.
  - **The kill switch** is `org/mcp/naming-gate.enforce`, the same shape as `org/mcp/comprail-gate1.enforce`.
    Every verdict is logged.
  - **The commit limb** sits on the `safe-commit` path. The exact insertion point is L5's read, because the brief
    read neither `commit-gate.sh` nor `ds-precommit-check.py`.
  - **The `safe-apply` limb** (`.tools/safe-apply.sh`, not read at L4) is specified only after the Terraform-label
    census, and it runs before plan.
- **DEC-7 Census mode.** It covers the repo and the live plane: Terraform, `lib/config.py`-class files and Lambda
  sources, plus names by node type from `comp-find --corpus aws`.
  - It judges every nameable live name; the naming endpoint's machine bar is 1,912 at that census's vintage.
  - Its totals are compared with LGIC_NAMING's hand gradings (N2's worked cases, N6's two-grader sample) and with the
    naming census's IV.7 ranking.
  - A RAISE stops the run with the string printed.
  - **The run may happen before N2 and N6 exist, but its comparison half waits for them.**
- **DEC-8 A remediation is data.** `remediations.json` rows are written by the remediation project's CTO at its L3.
  FWD-6 is proved on a practice copy (a linked worktree on a scratch branch, never pushed) with a planted row.
- **DEC-9 The demonstration firm is fictitious and lives only on a practice copy.** It is never `demo` (kept by Andrew
  ~01:3xZ 2026-09-13) and never pushed. The expected diff set is computed from the registry's consumer list BEFORE the
  generator runs, and then compared with the actual diff.
- **DEC-10 FWD-2's real resource** is one that lands in a plan on the real Terraform tree with its name from the
  module, for a firm whose fence patterns come from the same registry row. The first candidates are the resources
  `ADVI_FIRMBKTS` mints for the new firm buckets.
- **DEC-11 Never, in this project:**
  - a live rename or move (S13; D8 and D12 under ruling (a))
  - a runtime interceptor (his "runtime later")
  - the full ontology
  - an alarm, monitor or notification of any kind
  - tags
  - Terraform labels, before the label census is read

  **The one applied-plane act is DEC-4's bucket policy,** which Andrew ruled (the brief itself builds nothing on the
  applied plane).
- **DEC-12 The D12 placement question** (the brief's Part II, `0.0.0_AB_MSTR` 96338) is carried, not resolved. The
  first census flag with a D12 destination inherits it, at that member's L3.

## PROJECT ARC AND DEFINED OUTCOME

**Defined outcome:**
- Every storage address and every resource name comes from one registry through one builder.
- The separation rule, the router's map, the IRPT map and the precommit's lists come from the same registry.
- A change that mints a name the builder would not have produced is refused, with the correct form printed.
- The estate's whole out-of-pattern population, each with its fix, is one command away.
- A clean-up cannot stall, and firm N+1 is one row.

**Arc:**
1. The censuses (E1).
2. The registry and the builders (E2, E3).
3. The Terraform module and the fence (E4, E5), which is the D14-before-D8 item; the sequence's hold on
   `ADVI_FIRMBKTS` lifts only when it is applied on the template.
4. The generated views at DELTA=0 (E6).
5. The flagger's WARN window, then REFUSE (E7, E8).
6. Census mode (E9).
7. The practice-copy exercises (E10, E11).
8. FWD-2 on a real resource (E12).

It closes when every FWD grades REALIZED.

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's, and it may split, merge or re-sequence these.

| cell | serves | brief sections consumed | contracts consumed (C) / produced (P) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| E1 the carrier census and the fence-writer census | FWD-3, FWD-2 (DEC-4 ii) | IV.1; IV.2; Part VII bullet 3 | C `NAMING_SCHEMA.json` | `comp-find` over the corpus; CloudTrail data events on opal-data-bd, -inf, -cot and -49financial | `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md`, `FENCE_WRITER_CENSUS.md` | an unscoped read of every firm long and short form and legacy bucket name, with the denominator; every principal seen on each firm bucket, with its evidence line and scope token or `none` | every carrier the unscoped read finds is listed or excluded with a reason; every principal seen on a firm bucket is listed with its token |
| E2 the registry rows and the generator | FWD-3, FWD-7 | IV.7; IV.8 | P the registry rows | `infra/logic/05_IDENTITY_SPINE.md` | `infra/logic/registry/*.json`; `lib/opal_naming.py` (`generate`) | the files parse; every scope row carries long, short, tenancy and bucket; `bd` appears only as an alias or a refused token | the generator reproduces each E1 carrier's exported content byte for byte |
| E3 the builders | FWD-1, FWD-2, FWD-4, FWD-5 | O1; O2; IV.3 | C `NAMING_SCHEMA.json`, the grading rule; P `lib/opal_naming.py` | -- | `lib/opal_naming.py`, `lib/tests/test_opal_naming.py` | IV.3's controls: `cot-bd-session-daily-et` OUT-OF-PATTERN; `blackdiamond/49f/credentials` CONFORMANT; `CloudWatchLogs` OUT-OF-PATTERN; `opal-data-inf/silver/x` OUT-OF-PATTERN with `{source}` named as unfilled. A test a `\b`-style regex would fail. N2's worked cases once they exist | every control yields its stated verdict; `key()` has no bucket parameter; `name("mdpf", "cottonwood", "publisher", "role")` returns `mdpf-cot-publisher-role` |
| E4 the Terraform module | FWD-2 | O2 | C the registry; P the module | -- | `infra/aws/terraform/modules/opal_name/` | the vector file from E3's builder; the module's outputs over the same vectors | every vector matches; the module has no `external` data source |
| E5 the fence | FWD-2; the sequence's manual gate on `ADVI_FIRMBKTS` | Part V bullet 1 | C `exemptions.json`, E1's writer census; P the fence patterns | `infra/aws/terraform/shared-infra/s3-49financial.tf` | -- | a change-management ledger entry opened at start; never-widen sign-off (CTO and COO); a plan showing only the policy change; four real probe arms | an allowed 49financial principal reads the bucket; a cot, inf or mdpf principal is denied; an unscoped principal not exempted is denied; an exempted one is allowed; the prior policy is kept for rollback |
| E6 the generated views | FWD-3 | O3; IV.1; IV.7 | C the registry; P the views | the six carrier paths and the two precommit lists (DEC-5) | -- | DELTA=0 per view (exports identical before and after); each consumer's existing tests | every view is byte-equivalent in its exports; a hand edit to one is refused by E7 |
| E7 the commit limb, the kill switch and the WARN window | FWD-4, FWD-6, FWD-7 | O4; IV.5; Part V bullets 4-5 | C `grade()`; P the verdict line and the kill switch | the `safe-commit` path (L5 reads the insertion point) | `org/mcp/naming-gate.enforce`; the verdict log | the WARN window's log with its denominator; the flip announcement | on a practice copy, a commit adding `opal-data-inf/silver/...` is refused with the canonical printed; the canonical form passes; an existing permitted alias passes with the canonical printed beside it |
| E8 the Terraform-label census and the `safe-apply` limb | FWD-4 | IV.2 row 2; Part V bullet 6 | C `grade()` | `.tools/safe-apply.sh` | `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md` | the label census, read before the limb is specified | a plan adding a resource whose name the module would not produce is refused before plan, with the canonical printed |
| E9 census mode | FWD-5 | O5; IV.6 | C `grade()`; C LGIC_NAMING N2 and N6 | `comp-find --corpus aws`; `infra/logic/09_NAMING_CENSUS.md` | `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md` | the repo and the live plane, denominators printed; totals set beside IV.7 and N6 | every nameable live name is judged; the totals agree with the hand ranking; a RAISE stops the run loudly |
| E10 FWD-6 on a practice copy | FWD-6 | O6 | C `remediations.json` | a linked worktree on a scratch branch | -- | a planted remediation row that owns one surface holding an old-style name | a change touching the surface without removing the name is refused; the change removing it passes |
| E11 FWD-7 and FWD-1 on a practice copy | FWD-7, FWD-1 | O1; O7; Part III O1, O7 | C the registry, `key()` | a linked worktree on a scratch branch | -- | one fictitious firm row (DEC-9); the expected diff set computed before the run | the actual diff equals the expected set; a hand-typed address for that firm is refused; a new pipeline for it holds no storage-location literal, by a second worker's search |
| E12 FWD-2 on a real resource | FWD-2 | O2 | C the module, the fence patterns | the real Terraform tree | -- | a plan with the resource named by the module; the fence patterns for its firm from the same row; on a practice copy, one short-form change | the resource's name and its firm's fence pattern both move on that one change |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| new | `infra/logic/registry/systems.json`, `scopes.json`, `tiers.json`, `exemptions.json`, `remediations.json` | E2, E5, E10 | the registry rows |
| new | `lib/opal_naming.py` | E2, E3, E9 | `key()`, `name()`, `grade()`, `generate`, `census` |
| new | `lib/tests/test_opal_naming.py` | E3 | the positive and negative controls |
| new | `infra/aws/terraform/modules/opal_name/` | E4 | the generated locals and the name output |
| new | `org/mcp/naming-gate.enforce` and its verdict log | E7 | the kill switch and the audit |
| new | `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/` | E1, E8, E9, E10, E11, E12 | the censuses, the report and the exercise records |
| edit | `infra/aws/terraform/shared-infra/s3-49financial.tf` (the bucket policy) | E5 | the derived fence |
| edit (generated) | `data/firm_registry.json`; `infra/aws/lambda-edge/_shared/firm-config.mjs`; `data/assets/scripts/gold/investor_reporting/directory_runner.py` and `holdings_snapshot.py`; `infra/aws/lambda/investor-reporting/_authz/loaders.py`; `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py`; `.tools/ds-precommit-check.py` (its two lists) | E6 | the carriers, as generated views |
| edit | the `safe-commit` path (`.tools/commit-gate.sh` or `.tools/ds-precommit-check.py`; L5 reads which) | E7 | the commit limb |
| edit | `.tools/safe-apply.sh` | E8 | the pre-plan limb |
| read | `org/standards/NAMING_SCHEMA.json`; `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` (N2, N6) | E3, E9 | the schema and the hand gradings |
| read | `infra/logic/05_IDENTITY_SPINE.md`, `infra/logic/09_NAMING_CENSUS.md` | E1, E2, E9 | the substrate |
| read | CloudTrail data events on the four firm buckets; the live plane via `comp-find --corpus aws` | E1, E9 | the writers and the live names |

## BRIEF COVERAGE

**Denominator.** The brief @`fc2a1ba75f` has 8 top-level headings (the title and Parts I-VII) and one
`## REFS TO CARRY`. Counting each of Part I's seven outcomes and Part IV's eight findings as its own entry, that is
**24 entries**. Every entry maps to a decision, a cell and an outcome, or carries `NOT CONSUMED` with its reason.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble (the commission, the rulings executed, "builds nothing on the applied plane and renames nothing") | DEC-11; the preamble above | all |
| 2 | PART I heading | structural | -- |
| 3 | O1 a producer asks for a key | DEC-2; E3, E11 | FWD-1 |
| 4 | O2 a Terraform local derives a name, and the fence comes from the same call | DEC-2, DEC-3, DEC-4; E3, E4, E5, E12 | FWD-2 |
| 5 | O3 one registry, generated views | DEC-1, DEC-5; E2, E6 | FWD-3 |
| 6 | O4 a refusal that prints the canonical string | DEC-6; E7, E8 | FWD-4 |
| 7 | O5 the ranked census | DEC-7; E9 | FWD-5 |
| 8 | O6 a remediation cannot go quiet | DEC-8; E10 | FWD-6 |
| 9 | O7 firm N+1 is one row | DEC-9; E2, E11 | FWD-7 |
| 10 | PART II the boundary (OWNS / RELIES ON / SIBLINGS / NOT THIS BRIEF'S) | CONTRACTS; DEC-5's repoint boundary; DEC-11; DEC-12; the SURFACE MANIFEST's excluded row | all |
| 11 | PART III the qualitative bar | the ENDPOINT's ACCEPT lines; the acceptance drafts of E3, E7, E9 and E11 | all |
| 12 | PART IV heading | structural | -- |
| 13 | IV.1 no key builder; the registry exists five times | DEC-5 (re-measured at HEAD); E1, E6 | FWD-3 |
| 14 | IV.2 the minting points and their gates | DEC-6; E7, E8. The Lambda artifact key row stays UNCHANGED: the source-map tie holds (GAP-2) and only the key's grammar is graded | FWD-4 |
| 15 | IV.3 the grader's signature, three verdicts, the positive controls | DEC-2, DEC-6; E3 | FWD-4, FWD-5 |
| 16 | IV.4 why authoring time is where it sticks | the placement of E7 and E8 at the minting points | FWD-4 |
| 17 | IV.5 refuse against warn | DEC-6, ratified with its grain stated | FWD-4, FWD-6 |
| 18 | IV.6 what authoring time cannot reach | DEC-7 (census mode reads the live plane); DEC-11 | FWD-5 |
| 19 | IV.7 the registry's shape | DEC-1 (JSON, no kinds file); E2 | FWD-3, FWD-7 |
| 20 | IV.8 the order of dependence | the ARC | all |
| 21 | PART V what must be true | bullet 1 is DEC-4 and E5; bullet 2 is met (LGIC_NAMING admitted); bullet 3 is DEC-5; bullets 4 and 5 are DEC-6; bullet 6 is E8; bullet 7 names `ADVI_FIRMBKTS` and `MDPF_CANON` as `key()`'s first callers (CONTRACTS); bullet 8 is DEC-11 | all |
| 22 | PART VI status | NOT CONSUMED: not outcome-bearing. Its figures are re-measured at HEAD in DEC-5 | -- |
| 23 | PART VII what the brief does not claim | the unread gates are read at L5 (E7, E8); the carriers' contents are graded by E1 and E6's DELTA=0; the false-refusal rate is DEC-6's WARN window; runtime is out (DEC-11); D12 is DEC-12. Effort: NOT CONSUMED, and no estimate is made here either | FWD-4 |
| 24 | REFS TO CARRY | NOT CONSUMED as work: a link list. Its WAITING-ON items are closed. The schema is ratified (LGIC_NAMING v1.2 admitted); the refuse/warn matrix and the WARN window are DEC-6; the label census precedes the `safe-apply` limb (E8) | -- |

## SURFACE MANIFEST

Surfaces this project writes, reads or executes. The one applied-plane change is the firm-bucket template's policy (E5).

| surface | kind | cell | owner |
|---|---|---|---|
| `infra/logic/registry/*.json` | new data files | E2 | LGIC_ENFORCE |
| `lib/opal_naming.py`, `lib/tests/test_opal_naming.py` | new code | E2, E3, E9 | LGIC_ENFORCE |
| `infra/aws/terraform/modules/opal_name/` | new Terraform module: locals and outputs only, no resources | E4 | LGIC_ENFORCE |
| `infra/aws/terraform/shared-infra/s3-49financial.tf`, the bucket policy only | an APPLIED change to a live bucket policy | E5 | applied by the infrastructure lane through `safe-apply`, under never-widen sign-off (CTO and COO) and a change-management ledger entry |
| the six carrier paths and `.tools/ds-precommit-check.py`'s two lists | generated replacements, DELTA=0 | E6 | written by LGIC_ENFORCE; any deploy rides its owner's deploy path (Rule 13), byte-equivalent |
| the `safe-commit` path and `.tools/safe-apply.sh` | gate limbs | E7, E8 | LGIC_ENFORCE |
| `org/mcp/naming-gate.enforce` and its verdict log | the kill switch and the audit | E7 | LGIC_ENFORCE |
| `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/` | the censuses, the report, the exercise records | E1, E8-E12 | LGIC_ENFORCE |
| practice copies: linked worktrees on scratch branches, never pushed | exercises | E10, E11, E12 | LGIC_ENFORCE |
| `org/standards/NAMING_SCHEMA.json`; LGIC_NAMING's N2 and N6; `infra/logic/05_IDENTITY_SPINE.md`, `09_NAMING_CENSUS.md`; CloudTrail data events on the four firm buckets; the live plane via `comp-find --corpus aws` | read only | E1-E3, E9 | -- |
| any live rename or move; a runtime interceptor; any alarm, monitor or notification; tags; the D12 placement question | excluded | -- | remediations where the resource lives (D8, D12) under ruling (a); Andrew for runtime |
