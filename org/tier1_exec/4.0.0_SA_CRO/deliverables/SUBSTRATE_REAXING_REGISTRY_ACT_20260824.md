# REGISTRY ACT (DRAFTED, NOT APPLIED) - SUBSTRATE RE-AXED
## v3.22 -> v3.23 · minting `Substrate_Class`, `Substrate_Path`, `CLASS_GRAIN` · re-axing `Substrate`

**Author:** `4.0.0_SA_CRO` (base registrar) · **Date:** 2026-08-24
**Tier:** 1 - THE LIVE SYSTEM. Our instance. See `docs_abcdeg/plan/TRACK_MAP.md`.
**Status:** ⛔ **DRAFTED. NOT APPLIED. NOT COMMITTED TO THE YAML.** Needs a word to land.

---

## 1. AUTHORITY

**Andrew-direct 2026-08-24 at the CRO terminal, VERBATIM:**

> *"there are substrate concepts included in here that were designed before we really understood how
> we wanted to structure. I would say that there are two foundational substrate types, a 'cloud'
> resource space, which we'll call aws, ms, google, github, etc. And a 'local' resource space, which
> is any kind of on-prem or local data surface. These 'Substrates' can be broken down. E.g., github
> there may be multiple repos, in our case there is ajb_workspace and portal. We need a way to track
> this. the concepts of 'semctl' 'pipeline' 'codebase' are kind of deprecated when you look at it
> through this lens. substrate should be cloud environments or comparable local environments. the
> 'portal' substrate is really a sub-substrate of github. 'codebase' here is really 'ajb_workspace'
> which is another sub-substrate of 'github' which is not adequately covered."*

**Three follow-up rulings, same session, VERBATIM:** *"path, sentinel, and make hybrid a third value"*.

---

## 2. THE DEFECT BEING REPAIRED - Rule 24(ii), same grain

The live `Substrate` axis carries three grains at once:

| value | live nodes | grain |
|---|---|---|
| `aws`, `ms` | 8,081 | provider |
| `portal`, `codebase` | 11,338 / 0 | repository (a partition INSIDE a provider) |
| `pipeline` | 1,337 | function (already ruled off-axis: "folds into codebase") |
| `semctl` | 23 | not a resource at all - CLASS-GRAIN objects |

And `github`, the provider `portal` and `ajb_workspace` actually live on, **does not appear on the
axis at all** - so the two repos read as peers of `aws` rather than children of a provider. That
absence is his *"not adequately covered"*.

---

## 3. THE PROPOSED AXIS SET

```
Substrate_Class   {CLOUD, LOCAL, HYBRID}                CLOSED, 3 values, UNIVERSAL
Substrate         {aws, ms, google, github, ...}        OPEN, DECLARED PER DEPLOYMENT
Substrate_Path    ordered, variable-depth partition     OPEN, DECLARED
                  path within a Substrate
CLASS_GRAIN       sentinel on Substrate                 the axis does not apply at class grain
```

**THE DISCRIMINATOR FOR `Substrate_Class` IS CONTROL LOCUS, AND DECLARING IT IS LOAD-BEARING.**
`CLOUD` = provider-operated · `LOCAL` = self-operated · `HYBRID` = split. Under control-locus,
colocation is `LOCAL` (the customer controls everything; the building's owner is irrelevant to
substrate semantics) and AWS Outposts / Azure Stack are `HYBRID` (provider control plane, customer
premises). **Under the alternative reading - hardware location - the axis is NOT MECE and `HYBRID`
degrades into a residue bucket within a month.**

**`Substrate_Path` is a PATH, not a fixed sub-level, because natural depth differs by provider:**
`github -> ajb_workspace` (2) · `aws -> account -> region -> service` (4) · `ms -> tenant -> site ->
library` (4). A fixed single sub-substrate field would flatten those and re-commit the same grain
error one level down.

---

## 4. RULE 24 FOUR-POSTULATE RECORD

| Postulate | Verdict | Basis |
|---|---|---|
| **(i) MECE** | **PASS on control-locus** | Three values over one discriminator, no fourth cell. `HYBRID` survives the residue-bucket test: its contents are statable POSITIVELY (*customer-premises hardware running a provider's control plane*), not as "everything that did not fit". **FAILS if the discriminator is read as hardware location** - hence the declaration above is normative, not explanatory. |
| **(ii) SAME GRAIN** | **PASS** | One grain per axis: class / provider / partition. This postulate is the entire reason for the act. |
| **(iii) INTENT COHERENCE** | **PASS** | Each axis answers one question: what kind of environment · which environment · which partition inside it. |
| **(iv) STATE COHERENCE** | **PASS** | Adding a provider = declare a `Substrate` value plus its paths. All values move under one remedy. |

---

## 5. TOKEN CENSUS - RUN, CONTROLLED, TWO COLLISIONS ADJUDICATED

Pinned surface set: `SYSTEM_DEFINITIONS.yaml` 109,442 B · `NFRA_ONTOLOGY_RULE_BANK.yaml` 109,632 B ·
`NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` 50,326 B.
Controls: `Substrate` 27, `Motif` 2 (present) · generated negative `Zzqx9NotReal` 0.
Sibling-substring over the proposed set + the existing axis, both boundary regimes: **NONE**.

| token | exact | any-case | verdict |
|---|---|---|---|
| `Substrate_Class` | 0 | 0 | CLEAN |
| `Substrate_Path` | 0 | 0 | CLEAN |
| `CLASS_GRAIN` | 0 | 0 | CLEAN |
| `HYBRID` | 0 | 0 | CLEAN |
| `LOCAL` | 9 | 16 | **OCCUPIED - retired axis** |
| `CLOUD` | 17 | 20 | **OCCUPIED - LIVE HOMONYM** |

**`LOCAL`** collides with the RETIRED `Territory` axis `{LOCAL, GIT, AWS-CLOUD, MS-CLOUD}`, retired
2026-08-12 because *"its four values were TWO AXES FLATTENED ONTO ONE"* - the identical defect class
this act repairs, one axis over, using one of the same words. **Mitigating and measured:**
`Deploy_State`'s live values are `deployed | undeployed`, **not** `LOCAL`/`GIT`. The deploy sense
migrated under different value names, so `LOCAL` is live on no axis today. Collision is with history.

**`CLOUD`** is a **LIVE HOMONYM**: it is this repository's git branch name and it appears in
`Deploy_State`'s own binding prose - *"deployed = the CLOUD branch"*. Two live senses of one word
would sit in the same canon file.

**THEREFORE BOTH VALUES SHIP WITH THEIR SENSE FENCES AT MINT TIME, NOT AS A LATER REPAIR.**

---

## 6. THE ACT - exact YAML to apply

### 6a. `Substrate` entry - replace `definition`, add `substrate_class`, `path_law`, `sentinel`

```yaml
  Substrate:
    definition: >-
      The ENVIRONMENT partition of the Estate over which C0-C3 is materialized separately -- a cloud
      resource space or a comparable local one. RE-AXED 3.23 (Andrew-direct): the prior enum
      {aws, portal, codebase, ms} carried THREE GRAINS ON ONE AXIS -- providers (aws, ms), a
      repository (portal), and a repository under a wrong name (codebase = ajb_workspace) -- while
      `github`, the provider both repositories actually live on, was ABSENT from the axis entirely.
      Values are DECLARED PER DEPLOYMENT, never ratified closed: this estate declares
      {aws, ms, github}. A partition INSIDE a substrate is `Substrate_Path`, never a Substrate value.
      Retired values: `portal` -> github/portal · `codebase` -> github/ajb_workspace · `pipeline` ->
      github/ajb_workspace (function, never a substrate) · `semctl` -> CLASS_GRAIN (not a resource).
    substrate_class: >-
      Every Substrate declares a Substrate_Class. This estate: aws=CLOUD, ms=CLOUD, github=CLOUD.
    path_law: >-
      A Substrate_Path is an ORDERED, VARIABLE-DEPTH partition path scoped to its Substrate; depth is
      per-provider and declared, never fixed. github -> ajb_workspace is depth 2; aws -> account ->
      region -> service is depth 4. A path is scoped to its parent, so a repository name cannot
      collide across providers. A FIXED single sub-substrate field would flatten differing depths and
      re-commit the grain error one level down -- that is why this is a path.
    sentinel: >-
      CLASS_GRAIN -- the axis DOES NOT APPLY at class grain. Motif families and system kinds are the
      VOCABULARY, not occurrences of it, and a class is not materialized on a platform. Ratified by
      the B section 5.6 count law: "the same layer may have a small class population and a much
      larger instance population; both can be correct." This estate: 19 C2Motif families + 4
      C3System kinds = 23. NOT an exclusion -- a COUNTABLE sentinel, so the population stays visible
      to a coverage count. An excluded population is invisible to its own denominator.
```

### 6b. NEW term `Substrate_Class`

```yaml
  Substrate_Class:
    definition: >-
      THE FOUNDATIONAL KIND OF A SUBSTRATE, discriminated by CONTROL LOCUS -- who operates the
      control plane. CLOUD = provider-operated. LOCAL = self-operated (on-prem or any comparable
      local data surface). HYBRID = split (customer-premises hardware running a provider's control
      plane; AWS Outposts, Azure Stack). Minted 2026-08-24, Andrew-direct, VERBATIM "two foundational
      substrate types, a 'cloud' resource space ... and a 'local' resource space" + "make hybrid a
      third value". CLOSED at three values and UNIVERSAL -- unlike Substrate, whose values are
      declared per deployment.
    authority: org/tier1_exec/4.0.0_SA_CRO/deliverables/SUBSTRATE_REAXING_REGISTRY_ACT_20260824.md
    sits_at: the class axis above Substrate
    status: reserved_ratified
    discriminator_is_normative: >-
      CONTROL LOCUS, NOT HARDWARE LOCATION, AND THE DISTINCTION IS LOAD-BEARING. Under control-locus
      the axis is MECE over three values with no fourth cell, and COLOCATION IS `LOCAL` -- the
      customer controls everything and the building's owner is irrelevant to substrate semantics.
      Under a hardware-location reading the axis is NOT MECE (a 2x2 appears, one cell empty) and
      HYBRID degrades into a residue bucket. HYBRID passes the residue-bucket test ONLY because its
      contents are statable POSITIVELY -- provider control plane on customer premises -- rather than
      as "everything that did not fit".
    sense_fence: >-
      SENSE FENCE (3.23, at mint time rather than as a later repair, because the census found the
      collision BEFORE the mint): the value `CLOUD` on this axis is a PROVIDER-OPERATED ENVIRONMENT.
      It is NOT the git branch `CLOUD` that Deploy_State binds against ("deployed = the CLOUD
      branch") -- BOTH SENSES ARE LIVE AND BOTH ARE CORRECT, and they occur in this same file. The
      value `LOCAL` is a SELF-OPERATED ENVIRONMENT. It is NOT the retired Territory axis's `LOCAL`,
      which was a DEPLOY STATE and is now expressed as `undeployed`. Re-use is legitimate PRECISELY
      BECAUSE that retirement moved the deploy sense onto different value names -- but a reader who
      remembers Territory will misread it, and that reader is who this fence is for.
```

### 6c. NEW term `Substrate_Path`

```yaml
  Substrate_Path:
    definition: >-
      An ORDERED, VARIABLE-DEPTH partition path within a Substrate, scoped to its parent. This
      estate: github -> ajb_workspace, github -> portal. Minted 2026-08-24 Andrew-direct ("these
      Substrates can be broken down ... we need a way to track this"; "path"). Depth is PER-PROVIDER
      and DECLARED -- a fixed sub-substrate field would flatten github's depth-2 against aws's
      depth-4 and re-commit the grain error one level down.
    authority: org/tier1_exec/4.0.0_SA_CRO/deliverables/SUBSTRATE_REAXING_REGISTRY_ACT_20260824.md
    sits_at: the partition axis below Substrate
    status: reserved_ratified
```

### 6d. Changelog entry

```yaml
  - "3.23 2026-08-24: SUBSTRATE RE-AXED (Andrew-direct, CRO terminal; VERBATIM in the act record) --
    the axis carried THREE GRAINS (providers aws/ms, a repository portal, a repository misnamed
    codebase) while `github`, the provider both repos live on, was ABSENT. +Substrate_Class
    {CLOUD, LOCAL, HYBRID} discriminated by CONTROL LOCUS (normative; the hardware-location reading
    is NOT MECE). +Substrate_Path, an ordered VARIABLE-DEPTH path (fixed sub-levels would flatten
    github's depth-2 against aws's depth-4). +CLASS_GRAIN sentinel -- countable, never an exclusion.
    Substrate values become DECLARED PER DEPLOYMENT, which is the section-3.9 portability repair:
    the axis is universal, its values are this estate's instance. Token census RUN with controls;
    TWO COLLISIONS ADJUDICATED AND FENCED AT MINT TIME -- `CLOUD` is a LIVE HOMONYM with this repo's
    git branch (cited in Deploy_State's own bindings) and `LOCAL` collides with the retired Territory
    axis, whose retirement reason (two axes flattened) is the same defect class repaired here.
    NO MIGRATION IN THIS ACT: 20,779 live nodes keep their `layer` values. Registered by
    4.0.0_SA_CRO."
```

---

## 7. WHAT THIS ACT DOES **NOT** DO

- **No migration.** All 20,779 live nodes keep their current `layer` values. The value map below is
  the NEXT act and needs its own authorization.
- **No `layer` -> `substrate` column rename.** That is the CTO arch-call already recorded on the
  `Substrate` entry (2026-08-12, still open).
- **No `Territory` change.** It stays deprecated with its binding residue intact.
- **No graph re-derive.**

## 8. THE MIGRATION MAP (a SEPARATE act, recorded here so it is not lost)

| today `layer` | live | `Substrate_Class` | `Substrate` | `Substrate_Path` |
|---|---|---|---|---|
| `portal` | 11,338 | CLOUD | `github` | `portal` |
| `ms` | 6,006 | CLOUD | `ms` | *(tenant/site - to declare)* |
| `aws` | 2,075 | CLOUD | `aws` | *(account - to declare)* |
| `pipeline` | 1,337 | CLOUD | `github` | `ajb_workspace` |
| `codebase` | 0 | CLOUD | `github` | `ajb_workspace` |
| `semctl` | 23 | **CLASS_GRAIN sentinel** | - | - |

**20,756 of 20,779 map cleanly; the residual 23 are correctly excluded as a DECLARED, COUNTABLE
category.** This migration resolves the 1,360-node frozen residue (`pipeline` + `semctl`) that the
`Substrate` entry has carried as "OPEN FINDING, not chased" since 2026-08-19 - measured unchanged
across five days, so it is residue from an incomplete retirement rather than a growing leak, and a
one-time migration closes it.
