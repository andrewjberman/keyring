# LGIC_NAMING -- the naming schema: one grammar for every storage address, bucket and resource name, graded by one rule

```json
{
 "project": "LGIC_NAMING",
 "directive": "D14",
 "fabric": "laptop",
 "prd_version": "v1.7",
 "step": 4,
 "brief_ref": "docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe758",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "RATIFIED"
}
```

Brief: `docs/briefs/d14-naming-schema-brief-20260913.md` @`1b42dbe758` (author `4.0.0_SA_CRO~D`; 8 top-level headings, 22
coverage entries below). Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md`,
cut @`b6eddd11a0`, amendment record and ruling stamps @`e2210bf34c`; DONE WHEN confirmed by Andrew 2026-09-13 ~18:4xZ.
Registered @`f25395446e` under D14/LGIC on the macro ratified @`464c1096d5`. The closed enumerations this PRD decides
are data: `org/standards/NAMING_SCHEMA.json` (v1.1 at PRD v1.1), landed with the first issue. Counterpart: `LGIC_ENFORCE` (the
executable layer: registry, builders, flagger), which consumes this schema; its PRD does not exist yet.

**Rulings this PRD executes, verbatim anchors:** the SOURCE-FIRST key string (Andrew ~03:2xZ, *"all recs approved"*,
relayed 96332); WHICH firm short forms exist -- *"one sanctioned short form per firm -- 49f, inf, cot -- ALONGSIDE the
long forms ... bd is REFUSED in every slot"* (~03:5xZ card 2, record @`38f2268d48`); remediation shape (a), D14 owns the
rule and the flag and every fix goes where the resource lives (~03:5xZ); FWD-6 graded at APPLIED (~18:4xZ card 5). **The
per-slot split -- WHERE each form is used -- is ratified HERE, at L4, by `1.0.0_SA_CTO`, and is revertible on Andrew's
word:** it narrows nothing he ruled (both forms stay sanctioned; buckets were ruled long in D10-2; the key `{scope}` is
long in the ruled source-first string).

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Anyone creating something new in the estate knows its name before they
         start, and two people working separately choose the same name
         DONE WHEN  EXERCISED -- two people have actually named the same new thing
                    without conferring, and matched
         ACCEPT     two people who have not spoken are each asked to name the same new
                    piece of infrastructure -- say, the one that publishes Cottonwood's
                    model-portfolio figures -- and each writes down the identical name,
                    where today they would write three different ones
         SOURCE     brief Part I O1; bar Part III O1
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c

  FWD-2  Anyone reading a name can tell which part is the system, which is the firm
         or product, and which says what kind of thing it is -- from position alone
         DONE WHEN  EXERCISED -- someone new to the estate has read names and pointed
                    at the firm in each, unaided
         ACCEPT     someone who has never seen this estate is shown a name and says which
                    part of it is the firm without looking anything up -- and the same
                    letters never mean two different things, the way one abbreviation
                    today means both a data vendor and a client firm
         SOURCE     brief Part I O2; bar Part III O2
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c

  FWD-3  Every name that refers to a firm or product spells it one of its approved
         ways, and every other spelling survives only in one lookup list
         DONE WHEN  EXERCISED -- someone has written the rule that catches every system
                    belonging to one firm, and it was a single rule
         ACCEPT     someone writing the security rule that must catch every system
                    belonging to one firm writes it once, as a single rule, and it catches
                    all of them -- where today it takes one rule per spelling, and a new
                    spelling slips past it without anyone noticing
         SOURCE     brief Part I O3; bar Part III O3
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c

  FWD-4  An address for a stored file reads the same way in every storage location
         DONE WHEN  EXERCISED -- someone who knows one location's layout has read an
                    address in another and understood it correctly
         ACCEPT     someone who has learned how addresses are laid out in the main shared
                    storage reads an address in a firm's own storage, or a product's, and
                    understands it the same way with nothing new to learn; and every older
                    written description of a different layout says plainly that it has been
                    replaced
         SOURCE     brief Part I O4
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c

  FWD-5  There is a rule that decides, for any existing name, whether it follows the
         pattern, uses an old spelling, or breaks the pattern -- exact enough that two
         people applying it get the same answer
         DONE WHEN  EXERCISED -- two people have applied the written rule by hand to the
                    same set of real names and compared
         ACCEPT     two people apply the written rule by hand to the same set of real names
                    from the estate and reach the same answer for every one, including the
                    correct name for each one that breaks the pattern; and a name the rule
                    cannot place is treated as a flaw in the rule to be fixed, never quietly
                    filed under one of the three answers -- so that whatever machine is
                    later built to apply it has something exact to copy
         SOURCE     brief Part I O5
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c

  FWD-6  The worst naming problems in the estate are ranked, and anyone can point at
         the top ten and say what each one costs today
         DONE WHEN  APPLIED -- the ranked list exists and every entry states its cost
         ACCEPT     someone deciding what to fix first reads a ranked list of the ten worst
                    naming problems, each with a plain statement of what it costs today --
                    what breaks, what someone has to do by hand, or what it blocks -- and
                    starts from the top instead of from whatever name they tripped over
         SOURCE     brief Part I O6
         PIN        ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md@e2210bf34c
```

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| `org/standards/NAMING_SCHEMA.json` | **produced** | the closed enumerations: key grammar and tiers, bucket forms, resource grammar and last-slot rule, kind list by resource type, cadence list, secret / log-group / policy forms, firm long and short forms, refused tokens, system classes and exclusions, the grade signature and its three verdicts | consumed by `LGIC_ENFORCE` (its `key()`, `name()` and `grade()` builders and the registry-derived deny patterns), and read by every seat minting a name |
| the grading rule, `(name, type) -> (verdict, canonical_form)` | **produced** (as a written, hand-applicable specification; cell N2) | three verdicts CONFORMANT / ALIAS / OUT-OF-PATTERN and no fourth; an unplaceable name or an unresolved token RAISES | consumed by `LGIC_ENFORCE`, whose flagger executes it |
| the identity registry's ROWS (firms, products, vendors, platform subsystems, their keys and aliases) | **consumed** | rows only; this project fixes their shape and mints none | produced by `LGIC_ENFORCE` (ruling (a)); seed `infra/logic/05_IDENTITY_SPINE.md` until it exists |
| the source-first key string | **consumed** (ruled) | `{source}/{scope}/{tier}/{table}/{partition}`, verbatim; the bucket is the key's CONTAINER and never a segment of it, and `{object}` is the LEAF under `{partition}` (data file `key.container`, `key.leaf`) | ruled by Andrew ~03:2xZ; first applied by `ADVI_FIRMBKTS` and `MDPF_CANON` |

`LGIC_ENFORCE`'s PRD must state these same four rows from its side; until it is written there is no counterpart text to
compare, and this section is the one both will be read against.

## THE SCHEMA -- EVERY DECISION CLOSED AT L4

Each line below is closed; every enumeration it names is data in `org/standards/NAMING_SCHEMA.json` and is not restated
as a second copy here.

- **S1 Keys (ruled).** The key is `{source}/{scope}/{tier}/{table}/{partition}` -- the ruled string, verbatim, the same in every bucket. The
  bucket is the key's CONTAINER and is never written into the key; the object is the LEAF under `{partition}`. A full
  address is therefore `s3://{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}`.
  `{source}` is a registry VENDOR key, or a PRODUCT/SYSTEM key for derived tiers. `{scope}` is a FIRM, PRODUCT, MASTER
  or `global`, in the LONG form, never an entity id (doctrine R2; a vendor MASTER is valid, R3). `{tier}` is one of
  bronze, silver, gold, platinum, state (R21), code (R16); a code home's form is the data file's `key.code` (row S7,
  ruled). Tables are snake_case; a NEW platinum leaf is a kebab `.json`, and a LEGACY served path keeps its bytes
  (`key.legacy_served_path`; rows S6 and S8, ruled), and a path is legacy only if `key.legacy_served_paths` lists it (row S10, ruled at v1.4: membership is data, so the grade stays a function of `(name, type)` over this file; until the list lands, a key whose verdict turns on it RAISES). The partition forms, the entity partition among them (row S6;
  doctrine R2), are `key.partition`. The three rows were ruled at v1.3 by the CTO adjudication `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_S6_S7_S8_ENTITY_PARTITION_CODE_TIER_LEGACY_SERVED_PATHS.md`.
- **S2 Buckets.** Tenant and product data buckets are `opal-data-{scope}` in the LONG form; platform buckets are
  `opal-{account-id}-{purpose}`; `opal-data-assets` and `opal-data-portal-v2` stand. No new bucket carries a vendor name.
- **S3 Resource names.** `{system}-{scope}-{function}[-{qualifier}]-{last}`, kebab, lowercase, ASCII. `{last}` is the
  resource's KIND from the closed list, except EventBridge rules and Scheduler schedules, whose last slot is a CADENCE.
- **S4 The per-slot form rule (ratified here).** A firm or product in a resource name's `{scope}` slot, IAM principals
  included, is spelled in its SHORT form (`49f`, `inf`, `cot`, `demo`, `global`); in a bucket name and in a key's
  `{scope}` segment, in its LONG form (`49financial`, `inflection`, `cottonwood`, `demo`, `global`). One spelling per
  slot, never a choice. Secret paths are resource names and take the SHORT form (`blackdiamond/49f/credentials`).
- **S5 Shared resources carry no scope.** A resource serving more than one tenant omits the `{scope}` slot entirely --
  never a placeholder. (This is the input the `LGIC_ENFORCE` fence conditions must decide about: an unscoped principal is
  legitimate under this schema.)
- **S6 The system slot.** A system is a PRODUCT, a PLATFORM_SUBSYSTEM, or a VENDOR (only when the resource is that
  vendor's integration). A firm is never a system; nor is a project code, a workstream code, a cadence or a generic
  noun. `opal` is reserved for account-level platform resources and is never a null prefix. Which systems exist is the
  registry's rows, not this document.
- **S7 Kinds.** The closed list is the `kind` block of the data file, with the resource type each belongs to. **Every type
  key in the data file is a node_type value of the live-plane instrument (`comp-find --corpus aws`), spelled as it
  returns it** -- 33 types at the graph vintage 2026-09-13 12:15:54 UTC -- so the grader's `type` has one owner. Of the
  33, 18 are graded by kind and 15 are not; the 15 are enumerated by subtraction in `types_not_graded_by_kind`, each
  with its rule (cadence-last, derived, the bucket, key or secret grammar, or its bucket's name) or its exclusion
  (AWS-issued ids, DNS names, route contracts, event-source expressions, and IAM users, which are named by their
  holder or issuer). Four types the brief's list missed were added by that subtraction: ECS task definitions ->
  `task`, state machines -> `sfn`, load balancers -> `lb`, ECS clusters -> `cluster`. `secret` was removed, because
  secrets keep the slash-path grammar where a suffix would repeat the type. `-trigger`, `-publisher` and `-scanner`
  are function tokens, not kinds.
- **S8 Cadences.** daily, weekly, monthly, hourly, or `on-{event}` with a kebab event token.
- **S9 Secrets, log groups, policies.** Secrets `{system}/{scope}/{purpose}`; log groups are derived as
  `/aws/{service}/{resource-name}` and conform when their resource does; IAM policies are
  `{system}-{scope}-{purpose}-policy`, the purpose in the function slot, and a duplicate policy name is refused.
- **S10 Refused tokens.** `bd` is refused in every slot: the vendor is `blackdiamond`, the firm is `49financial`.
  `mockadv` is an alias row, never minted.
- **S11 The grade.** `grade(name, type) -> (verdict, canonical_form)`. CONFORMANT: the grammar holds and every slot
  carries a canonical spelling. ALIAS: the grammar holds but a slot carries an alias the registry resolves. OUT-OF-PATTERN:
  the grammar fails. A canonical form is printed for every ALIAS and OUT-OF-PATTERN. A name the rule cannot place, or a
  token no registry row resolves, RAISES as a defect in the rule or the registry; there is no fourth verdict.
- **S12 Scope of the schema.** Keys, buckets, resource names, secrets, log groups, policies. NOT covered: Terraform labels
  and module names (measured before `LGIC_ENFORCE` specifies its flagger), tags, AWS-issued identifiers, API routes.
- **S13 No rename.** The schema grades and moves no live name. A remediation is minted where the resource lives (D8 for
  keys, D12 for infrastructure), cites a row of the tension ranking, and carries its own sign-off.

- **S14 The round-1 rulings (L10, v1.5).** These come from `1.0.0_SA_CTO`'s ROUND-1 ANALYSIS
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md`) and rule the slots round 1
  measured as unruled. Each is data in `org/standards/NAMING_SCHEMA.json` v1.5 and is not restated here:
  - the function is the verb, or the process as the item names it (FN1);
  - the qualifier is a tier or a named table, and an alarm's condition is always written (FN2, FN3);
  - a secret's purpose is its credential kind, after the interface it opens (FN4);
  - `{entity}` is the key column (P1);
  - a vendor MASTER keeps its own scope under doctrine R3 (S1), and every other key's scope is its audience: a firm, or `global` when every firm shares it (SC1);
  - a one-vendor build is that vendor's integration at every tier (SY1);
  - a placeholder is a typed gap filled from its source (PH1);
  - AWS-fixed names are outside the grade's domain (AW1).
  The five ruled key segments are unchanged, and the grade stays `(name, type)`.
  v1.6 answers `4.0.0_SA_CRO`'s refusal of v1.5's brief half (review
  `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_5_20260914.md` @`f6172f7dfa`). Each ruling had left another line on
  the old rule:
  - SC1 gains the master case above;
  - AW1 is carried into N2 and coverage row 17;
  - PH1's dependency on `LGIC_ENFORCE` is carried into the arc and N6.
  v1.7 carries `1.0.0_SA_CTO`'s ROUND-2 ANALYSIS
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md`), as data in
  `NAMING_SCHEMA.json` v1.7:
  - a noun-phrase function drops every token already written in the system or scope slot (`orion-inf-ingest`, never
    `orion-inf-orion-ingest`) (FN1b);
  - only the resource's OWN kind is barred from its function, and another type's kind that names the subject it serves
    stays (FN1c);
  - both of those bind the grade as well as the namer. FN1's word-choice clauses bind the namer, who has the item's
    description, and a grade keeps a function's words as written;
  - `demo` reads as a firm in every naming slot, as the identity registry's row defines it, and the registry governs
    where it and the seed differ (DM);
  - FWD-2's reader may be told what each position holds, because reading "from position" presupposes it (POS);
  - SY1's worked example is a name outside every naming-exercise item set (EX1).

## PROJECT ARC AND DEFINED OUTCOME

**Defined outcome:** a seat that has never seen the estate derives any new name from the schema and the registry and
matches a second seat; reads any conforming name by position; writes one pattern per firm; reads any storage address the
same way in every bucket; grades any existing name to one of three verdicts with its canonical form; and starts fixing
from the top of a costed ranking.

**Arc:** the schema is decided and lands as data with this PRD (S1-S13). The project then proves it by hand, before any
machine exists, because the machine is `LGIC_ENFORCE`'s: the written grading rule and its worked cases (N2), three
exercises done by seats that did not write the schema (N3, N4, N6), the replacement notices on the older layout texts
(N5), and a cost line on every row of the ranking (N7). It closes when every FWD grades REALIZED. FWD-5 depends on
another project here: its correct name, for a live name that carries no system token, needs `LGIC_ENFORCE`'s
resource-to-system rows (S14 PH1). So FWD-5 grades REALIZED on completeness only once those rows exist. This PRD states
that dependency rather than let an exact-but-incomplete grade read as done.

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's and may split, merge or re-sequence these.

| cell | serves | brief sections consumed | contracts consumed (C) / produced (P) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| N1 the schema as data | FWD-1, FWD-2, FWD-3, FWD-5 | IV.2, IV.3, IV.4, IV.5, IV.6; Part V bullets 2-4 | P `NAMING_SCHEMA.json` | -- | `org/standards/NAMING_SCHEMA.json` (landed WITH this PRD at L4) | the data file parses; every enumeration S1-S13 names is present in it | **delivered at L4; no L7 cell unless an L10 addendum changes it** |
| N2 the written grading rule with worked cases | FWD-5 | O5; IV.6 (the residue enumerated, not omitted); Part V bullet 4; Part VII bullet 5 | C `NAMING_SCHEMA.json`; P the grading rule | `infra/logic/09_NAMING_CENSUS.md` | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` | at least one worked case per verdict and per resource type in the data file's `kind.by_type`, drawn from real live names (`comp-find --corpus aws`), each with its canonical form; the census residue classes (camel IAM, purpose-first policies, library-first layers, workstream-coded schedules) each graded; the AWS-fixed names (S14 AW1: the `default` security group, AWS-managed policies read by ARN, and AWS-created log groups; 15 measured by name and prefix in row W1-S4) each dispositioned as EXCLUDED, never graded | every worked case yields exactly one of the three verdicts or a stated RAISE |
| N3 the blind naming and reading exercises | FWD-1, FWD-2 | O1, O2; Part III O1, O2 | C `NAMING_SCHEMA.json`, the identity registry (`infra/logic/registry/`; the seed `infra/logic/05_IDENTITY_SPINE.md` served until it existed, and where they differ the registry governs -- S14 DM) | -- | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` (exercise records) | two workers, briefed only with the schema and the registry, each name the same set of new resources (including the Cottonwood model-portfolio publisher) without conferring, and no briefing spells an item's answer (S14 EX1); a third, briefed with the same two and told what each position of the grammar holds (S14 POS), reads a set of conforming names and marks the firm in each | identical strings from both namers on every item; the reader marks the firm correctly in every conforming name, and no token reads as two referents |
| N4 one pattern per firm | FWD-3 | O3; IV.3; Part III O3 | C `NAMING_SCHEMA.json` | the live principal names (`comp-find --corpus aws`, `IAM_ROLE`) | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` | for each firm, one pattern written from S3-S5, applied to the canonical forms of every principal the census attributes to that firm, with the denominator printed | one pattern per firm catches every attributed principal's canonical form and no other firm's |
| N5 the replacement notices on older layouts | FWD-4 | O4; Part II RELIES ON (the source-first ruling); IV.7 row 3 | C the ruled key string | -- | edits to the texts below, each by its owner | the two older layout texts: the 2026-08-18 template comment `infra/aws/terraform/shared-infra/s3-49financial.tf:8-13`, and `MDPF_CANON_PRD.md` s.3; a reading exercise across a firm bucket and a product bucket | each older text states it is replaced by S1, citing this PRD; a reader who learned `opal-data-assets` reads an address in another bucket correctly |
| N6 the hand-grading agreement exercise | FWD-5 | O5; Part III O5 | C the grading rule (N2) | `infra/logic/09_NAMING_CENSUS.md` | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` | two workers who did not write N2 each grade the same sample of real live names, the sample drawn across every resource type, with the denominator printed | the two gradings agree on every name, verdict and canonical form; any disagreement or RAISE returns to N2 as a rule defect; a canonical form carrying a placeholder (S14 PH1) is exact but not the complete correct name, and is counted apart, so N6 can pass on agreement while FWD-5's completeness waits on `LGIC_ENFORCE`'s rows |
| N7 the costed ranking | FWD-6 | O6; IV.7 (all ten rows) | -- | the brief's IV.7 | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/TENSION_RANKING.md` | each of the ten rows with a plain cost line: what breaks, what someone does by hand, or what it blocks | ten rows, each with a cost line a reader can dispute |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| new | `org/standards/NAMING_SCHEMA.json` | N1 | the closed enumerations (landed with this PRD) |
| new | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` | N2 | the written grading rule and worked cases |
| new | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/TENSION_RANKING.md` | N7 | the costed ranking |
| new | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` (exercise records) | N3, N4, N6 | exercise inputs, answers and comparisons |
| edit | `infra/aws/terraform/shared-infra/s3-49financial.tf` (comment lines 8-13 only) | N5 | the replacement notice; a comment edit, no resource change |
| edit | `docs/architecture/MDPF_CANON_PRD.md` s.3 | N5 | the replacement notice, landed by its owner at `MDPF_CANON`'s L4 |
| read | `infra/logic/09_NAMING_CENSUS.md`, `infra/logic/05_IDENTITY_SPINE.md`, `infra/logic/02_DOCTRINE.md` | N2-N7 | the substrate |
| read | the live plane via `comp-find --corpus aws` | N2, N4, N6 | real names for worked cases and samples |

## BRIEF COVERAGE

Denominator: the brief at `1b42dbe758` has 8 top-level headings (the title and Parts I-VII) and one `## REFS TO CARRY`;
with Part I's six outcomes and Part IV's seven findings each an entry, that is **22 entries**. Every entry maps to a cell
and outcome or carries `NOT CONSUMED` with its reason.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble (commission, rulings executed, "this brief renames nothing") | S13; the preamble above | all |
| 2 | PART I heading | structural | -- |
| 3 | O1 anyone minting a new resource knows its name | N1, N3 | FWD-1 |
| 4 | O2 system / scope / kind by position | N1, N3 | FWD-2 |
| 5 | O3 one spelling per slot, aliases in one table | S4, S10; N1, N4 | FWD-3 |
| 6 | O4 a key reads the same in every bucket | S1, S2; N5 | FWD-4 |
| 7 | O5 grade any name by one rule | S11; N2, N6 | FWD-5 |
| 8 | O6 the ranked current estate | N7 | FWD-6 |
| 9 | PART II boundary (OWNS / RELIES ON / SIBLINGS / NOT THIS BRIEF'S) | CONTRACTS; S12, S13; SURFACE MANIFEST excluded rows | all |
| 10 | PART III qualitative bar | the ACCEPT lines of the ENDPOINT section | all |
| 11 | PART IV heading | structural | -- |
| 12 | IV.1 the dominant grammar exists | S3 (order kept, vocabulary pinned) | FWD-1, FWD-2 |
| 13 | IV.2 the schema | S1-S9; N1 | FWD-1..FWD-5 |
| 14 | IV.3 two spellings of every firm | S4; N4 | FWD-3 |
| 15 | IV.4 `bd` is a vendor and a firm | S10; N3 (the reader exercise), N4 | FWD-2, FWD-3 |
| 16 | IV.5 118 first tokens; project codes and `opal` in the system slot | S6 | FWD-1, FWD-2 |
| 17 | IV.6 the four-postulate record | S7, S11 (the residue enumerated; no fourth verdict); N2. S14 AW1 is a STATED NARROWING of the brief's declared 1,912-name domain: the AWS-fixed names leave the grade's domain as EXCLUDED, never as a fourth verdict. 15 were measured by name and prefix in row W1-S4's population (vintage 2026-09-14 12:13:53 UTC); the rest of the AWS-managed policies are counted by ARN. The brief's 1,912 was measured at the brief's own vintage, so the two are not subtracted as one set | FWD-5 |
| 18 | IV.7 the tension ranking | N7; N5 (row 3) | FWD-6, FWD-4 |
| 19 | PART V what must be true | S6 (system axis to the registry), N1 (closed kind and cadence lists), this PRD (one document with the key string), S11 (three verdicts), S13 (no rename), S12 (Terraform labels out, measured before the flagger) | all |
| 20 | PART VI status | NOT CONSUMED: not outcome-bearing; its measured figures are cited through N2's substrate | -- |
| 21 | PART VII what the brief does not claim | S12 (labels, tags, routes out of scope); N2 (no running tokeniser: the rule is written and hand-applied); the short-form question is RULED (~03:5xZ) and closed by S4 | FWD-5 |
| 22 | REFS TO CARRY | NOT CONSUMED as work: a link list; its WAITING-ON items are closed -- L4 ratification by this PRD, the short-form call by the ~03:5xZ ruling, the remediation shape by ruling (a); the Terraform-label census is `LGIC_ENFORCE`'s | -- |

## SURFACE MANIFEST

Surfaces this project writes, reads or executes. Nothing here is deployed; no AWS resource is created, renamed or changed.

| surface | kind | cell | owner |
|---|---|---|---|
| `org/standards/NAMING_SCHEMA.json` | new data file | N1 | LGIC_NAMING (landed at L4 by 1.0.0_SA_CTO) |
| `org/missions/D14/LGIC/LGIC_NAMING/deliverables/` | new documents and exercise records | N2, N3, N4, N6, N7 | LGIC_NAMING |
| `infra/aws/terraform/shared-infra/s3-49financial.tf` lines 8-13 | comment edit only | N5 | the infrastructure lane holding that file; no resource block changes |
| `docs/architecture/MDPF_CANON_PRD.md` s.3 | text edit | N5 | MDPF_CANON, at its own L4 |
| `infra/logic/09_NAMING_CENSUS.md`, `05_IDENTITY_SPINE.md`, `02_DOCTRINE.md` | read | N2-N7 | 4.0.0_SA_CRO (lane PLATFORM_LOGIC_DOCS) |
| the live AWS plane through `comp-find --corpus aws` | read only | N2, N4, N6 | -- |
| any live rename, any registry row, any builder or flagger, any IAM change | excluded | -- | remediations where the resource lives; LGIC_ENFORCE for the registry, builders and flagger |
