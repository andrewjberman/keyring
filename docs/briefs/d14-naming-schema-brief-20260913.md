# D14 — EXPLICIT TERMINOLOGY FOR EVERY PATH AND EVERY RESOURCE NAME: THE LEAST-DISRUPTIVE SCHEMA, MEASURED, WITH THE CURRENT STATE RANKED BY TENSION — STEP-1 BRIEF

**Author:** `4.0.0_SA_CRO~D` · **UTC:** 2026-09-13 ~03:4xZ
**Mode:** NEW. The first of TWO Platform Logic briefs (Andrew ~03:2xZ, card 2: *"all recs approved"* — naming first,
the executable layer second).
**Directive:** D14 "Platform Logic" (LAPTOP). This brief is D14's own: it defines the vocabulary the executable layer
(brief two) is parameterised by. Remediation of any name it flags is NOT this project's — it is minted where the
resource lives (D8 for pipeline keys, D12 for infra), per the discussion recorded `@462b7b809a` (not yet ruled).
**Commissioned by:** Andrew-direct ~03:0xZ, verbatim: *"I want to make sure that we have very explicit terminology for
all paths, that goes for bucket nested folders/files, resource names, everything, i want you to look at everything in
the cloud and try to assess the patterns for each resource type and come up with the least disruptive / closest to
current state naming mechanism. then the brief will contain that and a spec on the current state with highest tension
surfaces with the designated naming schema."* and the bottom line: *"a pattern that sticks so that we never have to
reinvent the wheel again when bringing in new resources … stop all the various forks that break patterns by firm."*
**Rulings this brief executes:** the SOURCE-FIRST key string `{source}/{scope}/{tier}/{table}/{partition}` (~03:2xZ card 1);
(b)-minimal = identity spine + segment grammar (card 3); R1–R3 (`02_DOCTRINE.md`).
**Substrate:** `infra/logic/09_NAMING_CENSUS.md` — 2,531 live nodes, 33 types, every number below is from it.
**Consumer:** STEP 2, `1.0.0_SA_CTO` `/endpoint --forward`.

⛔ **This brief renames nothing.** A schema is a rule new names obey and old names are graded against; a live rename is a
remediation project with its own never-widen sign-off.

---

# PART I — THE OUTCOME TERRITORY

### O1 — Anyone minting a new resource of any type knows its name before they open the console, and two people would mint the same name
A seat creating a Lambda, role, rule, schedule, queue, topic, table, secret, alarm, bucket or key for firm N+1 or product
N+1 derives the name from `(system, scope, function, kind)` and the spine, and a second seat derives the same string —
where today 118 different first tokens have been used as "the system" and one firm is spelled three ways in every type.

### O2 — A reader tells a SYSTEM from a SCOPE from a KIND by position, in any name, in any type
`cot-bd-session-daily-et` reads as *scope=cottonwood, source=blackdiamond, function=session, cadence=daily* only if you
already know it; under the schema the same information is positional and the reader needs no history. `bd` stops
meaning both Black Diamond and 49 Financial.

### O3 — Every name that spells a firm or product spells it ONE way PER SLOT, and the alias table is the only place the other spellings survive
**PROPOSED — ratified at L4 by `1.0.0_SA_CTO` (96374), revertible on Andrew's word.** ⛔ Attribution corrected 06:0xZ: card 2
(~03:5xZ, `@38f2268d48`) ruled WHICH short forms exist (`49f`/`inf`/`cot`, one each, alongside the long forms; `bd` refused)
— it did NOT rule WHERE each is used; the per-slot split is the CTO's 96353 finding 3, decidable at L4 because it narrows
nothing he ruled (both forms stay sanctioned; buckets long by D10-2; key scope long by the source-first string). The
sanctioned SHORT form (`49f` / `inf` / `cot`, one each) is the firm token in EVERY RESOURCE NAME; the LONG form (`49financial` /
`inflection` / `cottonwood`) is the firm token in BUCKET NAMES and in the `{scope}` SEGMENT OF KEYS. One spelling per slot,
never a choice. `bd` and `mockadv` live in the spine's alias table as history and are never minted — where today the
cross-firm fence denies `role/mdpf-*` by a name pattern, and a pattern over three spellings of one firm is three patterns.

### O4 — A key reads the same string in the monolith, a firm bucket and a product bucket
`{source}/{scope}/{tier}/{table}/{partition}` everywhere (ruled). A consumer that learned `opal-data-assets` has learned
`opal-data-49financial` and `opal-data-mdpf`. The 08-18 template's tier-first comment and MDPF_CANON §3 are superseded
in text, not by a move.

### O5 — A seat can grade any existing name or key as CONFORMANT / ALIAS / OUT-OF-PATTERN by one rule and print the conformant form beside it
The grade is computable (a tokeniser + the spine), not judged — and the printed conformant form is the remediation spec
the executable-layer brief's flagger will emit. This outcome is the naming brief's half of "deterministically flag."

### O6 — The current estate is ranked: someone can point at the ten naming surfaces where the tension is highest and say what each costs today
Part IV.7 is that list. It exists so remediation projects are minted from the top of it, not from whichever name a seat
happens to touch.

---

# PART II — WHERE THE BOUNDARY SITS

**OWNS:** the schema per resource type (IV.2–IV.5); the segment vocabulary (`system`, `scope`, `function`, `kind`, `cadence`)
and its four-postulate record (IV.6); the alias table's shape (the spine owns its rows); the grading rule (O5) as a
SPECIFICATION (the flagger that runs it is brief two); the tension ranking (IV.7).
**RELIES ON:** `05_IDENTITY_SPINE.md` (the canonical keys — this brief adds the SYSTEM axis to it: products, vendors,
platform subsystems); `02_DOCTRINE.md` R1–R3 (key grammar, scope-segment law, plane-tagged vocabulary); the ~03:2xZ
source-first ruling; `01_CENSUS.md` / `06_CONFORMANCE_LEDGER.md` for key-plane conformance.
**SIBLINGS:** brief two (the executable layer — builders, flagger, registry runtime: consumes this); the two D8 migration
briefs (first consumers of the key string; their IV.5/IV.6 tables are instances of IV.2); `NFRA_IAMROLES202609` /
`NFRA_OPSEC202609` (IAM naming touches their plane — the fence is keyed on names); `07_ROUTING_REDERIVATION.md` (API
route grammar is NOT this brief's; routes are a served contract).
**NOT THIS BRIEF'S:** any rename; Terraform LABEL grammar (repo plane — measured next, brief two's authoring surface);
tags; AWS-issued identifiers (KMS ids, distribution ids, service principals).

---

# PART III — THE QUALITATIVE BAR

- **O1 passes when** two seats asked to name "the Lambda that publishes Cottonwood's MDPF slice" write the same string
  without conferring — where today they would write `cot-mdpf-publisher`, `mdpf-cot-publisher` and `opal-assets-mdpf-cottonwood-publisher`.
- **O2 passes when** a reader who has never seen the estate says which token is the firm in any conforming name.
- **O3 passes when** an IAM condition that needs "every principal of firm X" is ONE pattern.
- **O5 passes when** the grading rule, run over the 1,912 nameable live names, prints a verdict for every one and a
  conformant form for every non-conformant one — no `UNDETERMINED`.
- **O6 passes when** a remediation project cites a row of IV.7 as its reason.

---

# PART IV — THE SUBSTRATE: FINDINGS, EACH WITH WHAT WAS MEASURED

### IV.1 — The estate already has a dominant grammar, and it is not the disorder
`09_NAMING_CENSUS.md` §1–2: kebab-case ≥ 98% in every compute/infra type; system-first 86–100% in 13 of 19 nameable
types; kind suffixes already in use with a stable vocabulary (`-role` 194/240, `-sg` 23/27, `-profile` 17/19, `-dlq`,
`-alerts`, `-api`, `-daily/-weekly/-hourly`, `-trigger`). **Finding:** the least-disruptive schema is the dominant
pattern with its vocabulary pinned — not a new grammar. Almost no live name changes ORDER; what changes is which words
are allowed in each slot.

### IV.2 — THE SCHEMA (PROPOSAL for L4; one rule per plane, the same vocabulary in all of them)

**Keys (ruled):**
```
{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}
  bucket     opal-data-{tenant|product}   |  opal-data-assets  |  opal-data-portal-v2  |  opal-{account}-{purpose}
  source     spine SYSTEM key: a vendor/feed (blackdiamond, schwab, orion, eclipse, smartx, ycharts, fred)
             or a product/system (advi, irpt, mdpf, etfs) for derived tiers
  scope      spine SCOPE key: a firm (49financial, inflection, cottonwood, demo) or a product scope (global)
             -- never an entity id (R2)
  tier       bronze | silver | gold | platinum | state | code            (R21 state; R16 code)
  table      snake_case; platinum leaves kebab-case .json (the served names)
  partition  date=YYYY-MM-DD | a named leaf
```
**Resource names (compute, IAM, messaging, storage, EC2, SSM, alarms):**
```
{system}-{scope}-{function}[-{qualifier}]-{kind}          kebab, lowercase, ASCII
  system     the spine SYSTEM key -- a product (advi, irpt, mdpf, etfs, find, news, trade, yang, smartx),
             a platform subsystem (gateway, stitch, globgrph, agentbus, opsec, firmsep, estate), or a
             vendor when the resource IS the vendor integration (blackdiamond, schwab, ycharts, fred)
  scope      the spine SCOPE key when the resource is tenant- or product-scoped; OMITTED when shared
             (a shared resource has NO scope token, not a fake one)
             ⛔ SHORT form here (49f | inf | cot | demo | global) -- the LONG form belongs to bucket names
             and key {scope} segments only (the per-slot split: PROPOSED, L4-ratified by the CTO 96374;
             WHICH short forms: ruled ~03:5xZ. One spelling per slot)
  function   what it does: session, silver-chain, gold, publisher, exporter, runner, fetch, download, ...
  qualifier  optional narrowing: a table, a leg (backstop, floor, accelerator), an environment (dev|prod)
  kind       the resource-type suffix, closed list: role | policy | profile | sg | api | table | queue | dlq |
             topic | alerts | secret | alarm | layer | runner (EC2) | build | document (SSM) |
             lambda (a function; the measured suffixes -trigger/-publisher/-scanner/-api are FUNCTION tokens
             that today double as kinds -- the closed list makes `lambda` the kind and keeps them as functions)
             + cadence for rules/schedules: daily | weekly | monthly | hourly | on-<event>
```
**Secrets (keep the live grammar — 86/96 already conform):** `{system}/{scope}/{purpose}` slash-path.
**Log groups:** derived — `/aws/{service}/{resource-name}`; conform automatically once the resource does.
**Buckets:** `opal-data-{scope}` for tenant/product data buckets — LONG form (`opal-data-49financial`); `opal-{account-id}-{purpose}`
for platform buckets; no new bucket carries a vendor name (`opal-data-bd` is the counter-example).
**IAM policies:** SAME rule as resources with `-policy` kind; purpose-first names (`cross-firm-deny-…`, `s3-read-…`)
become `{system}-{scope}-{purpose}-policy` — the purpose moves to the function slot; ⛔ **a policy name is never
duplicated** (`CloudWatchLogs` exists SIX times today, distinguishable only by ARN).

### IV.3 — Two spellings of every firm, in two positions, in every type — the single largest tension
Census §1.3, §4: 49 Financial = `bd` (~120 names), `49f` (~45), `49financial` (4); Inflection = `inf` (~140) / `inflection`
(4); Cottonwood = `cot` (~30) / `cottonwood` (2). The firm token is position 0 in ~210 names (firm-as-system) and
position 1 in ~75 (firm-as-scope). **Finding:** this is the resource-name form of the identity split the spine measured
on keys, and it is what makes the cross-firm fence a NAME-PATTERN list (`role/cot-*`, `role/inf-*`) that lapses when
a spelling changes (CLAUDE.md §5 NEVER, "an enumerated ban list lapses silently"). **Schema consequence:** the firm is a
SCOPE (position 1), never a system; each firm has ONE canonical key and ONE sanctioned short form (the spine decides
which; today `49financial`/`inflection`/`cottonwood` are the bucket names and the only long forms in use).

### IV.4 — `bd` is a vendor in one name and a firm in the next
Census §1.4: `cot-bd-session-daily-et` (vendor), `bd-49f-session-trigger` (vendor + firm), `bd-allocations` / `opal-data-bd`
(firm). **Finding:** the token is ambiguous by POSITION and by REFERENT at once. The schema resolves it by refusing `bd`
in both slots: the vendor is `blackdiamond` (the secrets already spell it so: `blackdiamond/49f/credentials`), the firm is
`49financial`. This is the one place the schema changes a TOKEN rather than pins a slot, and it is the token with the
widest blast radius (~120 names + a bucket + an IAM fence pattern).

### IV.5 — 118 first tokens, three of which are not systems at all
Census §3: project CODES in the system slot (`gldinc` 7, `quartz` 5, `cmtque` 4, `opsec`, `firmsep`), workstream codes
(`wsb`/`wsd` 12), cadences and generic nouns (`daily`, `historical`, `exec`, `infrastructure`, `market`), and `opal` as a
null prefix before a real system (`opal-assets-mdpf-portal-publisher`, `opal-bd-49f-session-fetch`). **Finding:** a
project code in a resource name outlives the project and reads as a system forever; `opal-` as a null prefix means
`opal-*` (445) is not one system but eighteen. **Schema consequence:** the SYSTEM axis joins the identity spine with a
closed registry (IV.6); a project code is never a system; `opal` is reserved for account-level platform resources
(`opal-gateway`, `opal-cloudtrail-logs-…`) and is otherwise dropped.

### IV.6 — The vocabulary as a schema: the four-postulate record (Rule 24)
- **MECE over a declared domain — by subtraction:** the domain is the 1,912 nameable live names (census §2 totals);
  every name tokenises to `(system, scope?, function, qualifier*, kind)` or is graded OUT-OF-PATTERN; the residue that
  fits no slot after the pass (camel IAM/alarms ~110, purpose-first policies ~90, library-first layers 7, `default` ×2)
  is enumerated, not omitted.
- **Same grain:** every value is ONE token; a compound like `silver-chain` is a FUNCTION token, not two.
- **Intent coherence:** one axis per slot — `system` says WHO produces, `scope` says FOR WHOM, `function` says WHAT,
  `kind` says WHICH AWS TYPE. A firm never sits in `system`; a cadence never sits in `function`.
- **State coherence:** the schema moves NO live name; grading a name ALIAS or OUT-OF-PATTERN does not change its drift
  class, its Terraform declaration or its IAM bindings — those move only in a remediation project.
- **Word-boundary census:** the first-token distribution (census §3, 118 tokens, denominator 1,912) is the token census
  the postulate demands; the `kind` list is the measured suffix census (§2).

### IV.7 — THE CURRENT STATE, RANKED BY TENSION (the "spec" Andrew asked for)
| # | surface | measured | why it is tension | what a remediation project would be (NOT minted here) |
|---|---|---|---|---|
| 1 | **Firm spelled `bd`/`49f`/`inf`/`cot` in ~330 resource names, firm-as-system in ~210** | census §1.3, §4 | the fence is a name-pattern list; the runner-name collision (D8 brief IV.11) is one instance; every new firm copies whichever spelling its author saw | alias table first (O3); names migrate WITH the project that next touches each resource — never a mass rename |
| 2 | **`bd` = vendor AND firm** | §1.4; `opal-data-bd` + ~120 names | ambiguous referent inside the tenant boundary | retires with `opal-data-bd` (D8 migration) for the bucket; the ~120 names per #1 |
| 3 | **Key grammar split: source-first (assets) vs tier-first (bd/inf/cot/49financial/portal-v2/mdpf)** | `01_CENSUS.md`, ledger; ruled source-first | the two D8 migrations ARE this row | the two D8 briefs |
| 4 | **96 camel IAM policies incl. 6× `CloudWatchLogs` duplicates; 6 camel roles; 6 camel alarms** | census §2 | a duplicated policy name is only addressable by ARN; camel breaks every kebab tokeniser | rename-on-touch under NFRA_IAMROLES; duplicates first |
| 5 | **339 `LIVE-no-DECLARED` nodes** (Lambda 15, role 16, rule 10, log 68, policy 36 …) | census §2, DB drift | a name minted outside Terraform is outside the authoring-time flagger; these are where the pattern will keep breaking | declare-or-retire sweep (D12); the flagger cannot bite here until they are declared |
| 6 | **Project/workstream codes as systems** (`gldinc`, `quartz`, `cmtque`, `wsb`, `wsd`) | §3 | outlive their project; read as systems forever | rename-on-touch; never mint a new one |
| 7 | **`opal-` as a null prefix** (445 names, 18 types) | §3 | `opal-*` is eighteen systems | new names drop it unless account-level; existing stay |
| 8 | **Purpose-first IAM policy names** (`cross-*` 39, `s3-*` 29, `cloudwatch-*` 23) | §2 | a second grammar inside one type | fold into `{system}-{scope}-{purpose}-policy` on touch |
| 9 | **Secrets: 10 of 96 off the slash-path grammar** | §2 | small; the grammar is otherwise the estate's best | rename-on-touch |
| 10 | **Terraform LABELS and tags — UNMEASURED** | census §5 | the flagger's authoring surface is the one plane this census could not see | the next census (brief two's substrate) |

---

# PART V — WHAT MUST BE TRUE (named, not sequenced)

- The identity spine gains a SYSTEM axis (products, vendors, platform subsystems) with one canonical key each and one
  sanctioned short form, before any builder is written (brief two depends on it).
- The `kind` list and the `cadence` list are CLOSED enums in the spine, not prose in this brief.
- The schema is ratified at L4 as ONE document with the key string (already ruled) and the resource string (IV.2) —
  the two must share the vocabulary or the estate has two spines.
- Grading (O5) is specified as a function of `(name, type)` → `(verdict, canonical_form)` with the three verdicts
  CONFORMANT / ALIAS / OUT-OF-PATTERN and NO fourth value; a name the tokeniser cannot place is a defect in the
  tokeniser, not a fourth verdict.
- No live rename is authorized by the schema; each remediation cites an IV.7 row and carries its own sign-off.
- The Terraform-label census (IV.7 #10) runs before brief two's flagger is specified.

# PART VI — STATUS · ⛔ NOT OUTCOME-BEARING · measured 2026-09-13 ~03:3xZ
- Live plane: 2,531 nodes / 33 types (DB vintage 02:09:00Z); 1,912 nameable; 339 LIVE-no-DECLARED.
- The key string is ruled source-first (~03:2xZ); no resource-name rule exists on any law surface today.
- `05_IDENTITY_SPINE.md` is a SEED (firms/products/vendors/masters); no system axis, no alias table as data.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM
- **Terraform labels, module names and tags were not measured** (repo plane).
- **S3 key grammar was not re-measured** — cited from `01_CENSUS.md`/the ledger.
- **API route grammar is out of scope** (a served contract, `07_ROUTING_REDERIVATION.md`).
- **The "system" classification of the 118 first tokens (IV.5) is this seat's READ of the names**, not a registry — the
  registry is the spine's to mint.
- **No name was graded by a running tokeniser**; the percentages are from a regex pass with the slot vocabulary
  hypothesised in the script (`name_census2.py`) — O5's grader does not exist yet.
- **Which short form each firm keeps** (`49f` vs none) is the spine's call, not made here.
- **Effort is not estimated.**

## REFS TO CARRY
```
  BRIEF PATH        docs/briefs/d14-naming-schema-brief-20260913.md
  PROJECT           LGIC_NAMING  (D14 / LGIC) (REGISTERED @f25395446e, Andrew ~21:3xZ "yes 2 all", record @464c1096d5; dep_stage REGISTERED, L4 next)
  EXISTING PRD      NONE. Law inherited: infra/logic/02_DOCTRINE.md R1-R3, R16, R21; the ~03:2xZ source-first ruling
  SUBSTRATE         infra/logic/09_NAMING_CENSUS.md (2,531 nodes / 33 types; per-type table; first-token vocabulary)
  THE REFERENCE SET 05_IDENTITY_SPINE @45160b1525 (gains a SYSTEM axis) · 01_CENSUS · 06_CONFORMANCE_LEDGER · 08_TENSION_MAP
  RULINGS CARRIED   ANDREW_DIRECT_20260913_030xZ (the commission) · ANDREW_DIRECT_20260913_032xZ (source-first; two briefs; (b)-minimal)
  SIBLING BRIEFS    brief two (executable layer) -- consumes IV.2/IV.6 · d8-legacy-firm-buckets-migration · d8-mdpf-canon-migration
  WAITING-ON        L4 ratification of IV.2 as one document with the key string · the spine's short-form call ·
                    the Terraform-label census (IV.7 #10) · Andrew's ruling on the remediation shape (D14 owns rule+flagger; fixes where the resource lives)
  MEASURED AT       2026-09-13 ~03:3xZ UTC (live DB vintage 02:09:00Z)
```
**Author:** 4.0.0_SA_CRO (Chief Research Officer) · **Home:** org/tier1_exec/4.0.0_SA_CRO/
