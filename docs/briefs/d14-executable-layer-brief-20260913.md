# D14 — THE EXECUTABLE LAYER: ONE REGISTRY, TWO BUILDERS, ONE FLAGGER — SO THE CANON ENFORCES ITSELF AT THE POINT A NAME IS MINTED — STEP-1 BRIEF

**Author:** `4.0.0_SA_CRO~D` · **UTC:** 2026-09-13 ~04:0xZ
**Mode:** NEW. The second of TWO Platform Logic briefs (Andrew ~03:2xZ card 2). It CONSUMES the naming brief
(`d14-naming-schema-brief-20260913.md` `@bf21181208`, IV.2 schema, IV.6 vocabulary) and does not restate it.
**Directive:** D14 "Platform Logic" (LAPTOP). Remediation shape RULED ~03:5xZ `@38f2268d48`: **D14 owns the rule, the
registry, the builders and the flagger; every FIX is minted where the resource lives (D8 keys / D12 infra), from a flag
carrying the string pair. D14 never owns a remediation project.**
**Commissioned by:** Andrew-direct ~03:0xZ, verbatim: *"I'd be curious to hear what (a) would look like, we could get a
brief on that too, need to know if dependent on (b) … what im thinking is if its possible to essentially gel around the
core naming taxonomy, core pipeline design based on tenant/product/etc, and deterministically flag that which is out of
pattern with remediation mechanism to do this as surgically as possible."* and ~03:2xZ card 3: the dependency is
**(b)-minimal** — identity spine + segment grammar, the full ontology OFF the critical path; **enforcement at AUTHORING
time first** (`safe-commit` / `safe-apply`), runtime later.
**Rulings this brief executes:** source-first key string; the resource-name schema (naming brief IV.2, L4 to ratify);
short forms `49f`/`inf`/`cot`, `bd` refused; remediation shape (a); R1–R3, R16, R21; GAP-2 (Lambda artifacts keep the
source-map tie); the standing veto on shadow pipelines and the moratorium on monitors (this builds GATES, not alarms).
**Consumer:** STEP 2, `1.0.0_SA_CTO` `/endpoint --forward`.

⛔ **This brief builds nothing on the applied plane and renames nothing.** It specifies a `lib/` module, a data file, a
gate limb, and a Terraform local — all repo-plane, all authoring-time.

---

# PART I — THE OUTCOME TERRITORY

### O1 — A producer never spells a key; it asks for one
A pipeline author writes `key(source="orion", scope="inflection", tier="bronze", table="positions", partition="2026-09-13")`
and gets `opal-data-assets/orion/inflection/bronze/positions/date=2026-09-13/` — the bucket included, from the tier rule
(R4–R7) and the registry — where today `STAGING_PREFIX = "gold/mdpf_revamp"` is one of 16 hand-spelled MDPF constants and
Inflection's producer was handed `opal-data-inf` by a human. **Your example ends here:** the same call with
`scope="49financial"` or `scope="cottonwood"` returns the same bucket, so the per-firm fork cannot be written.

### O2 — A Terraform author never spells a resource name; a local derives it
`local.name = opal_name(system="mdpf", scope="cottonwood", function="publisher", kind="role")` → `mdpf-cot-publisher-role`
(the builder takes the LONG key and emits the SHORT form — resource names carry short forms, bucket names and key
`{scope}` segments carry long forms, one spelling per slot — the per-slot split is PROPOSED and L4-ratified by the CTO
(96374), WHICH short forms was ruled ~03:5xZ; stated in the naming brief O3/IV.2; `bd` impossible) — and the cross-firm Deny's principal patterns are derived from the same
call, so the fence follows the spelling instead of enumerating it.

### O3 — Every pointer that names a firm reads ONE registry file, and cutting a firm over is one row
`data/firm_registry.json`, `lambda-edge/_shared/firm-config.mjs`, two copies of `firm_bucket_map()` in IRPT, `bucket_for()`
in `_authz/loaders.py`, `resolve_firm()` in `perfrp_firm_pin.py` (IV.2 — FIVE partial registries today) collapse to one
`infra/logic/registry/` file with a generated `.mjs`/`.py`/`.tf` view each; the deployed router's `p={…}` map is a build
output of it, not a constant.

### O4 — A commit or an apply that spells a name the builder would not have produced is REFUSED, and the refusal prints the canonical string
`safe-commit` (via `commit-gate.sh` / `ds-precommit-check.py`) and `safe-apply` grade every S3 key literal, every resource
name literal and every firm/product token in the diff: `CONFORMANT` passes; `ALIAS` passes with the canonical form printed
(a warning that does not block — the estate's ~330 alias names must keep compiling); `OUT-OF-PATTERN` refuses with the
canonical form printed. **The refusal text IS the remediation spec.** Today `ds-precommit-check.py` bans an ENUMERATED
list of foreign buckets/prefixes — the guard that CLAUDE.md §5 says "lapses silently when a name changes."

### O5 — A seat can run the flagger over the whole estate and get the ranked list of every out-of-pattern name and key, with its fix
The same grader, run in CENSUS mode over the repo (Terraform, `lib/config.py`s, Lambda sources) and the live corpus
(`comp-find --corpus aws`), prints the population the naming brief's IV.7 ranked by hand — with denominators, and with
the `(current, canonical)` pair per row. This list is what a D8/D12 remediation project is minted FROM (ruling (a)).

### O6 — A remediation project cannot go quiet half-done
While an OUT-OF-PATTERN string still exists in the repo for a surface a remediation project owns, the flagger refuses
commits that touch that surface without removing it — so "we tried to fix it and it never got done" becomes a refused
commit, not a forgotten ticket. (The live plane's undeclared 339 stay outside this until declared — IV.6.)

### O7 — Firm N+1 is one registry row plus the templates the builders already fill
Onboarding a firm = adding `{key, long, short, tenancy, bucket}` to the registry; the bucket module, the fence patterns,
the router map, the IRPT map, the freshness configs and the gate's vocabulary all derive. No seat writes a firm's name
into code. (The onboarding CHECKLIST — the canon brief's O6 — is what this makes one page long.)

---

# PART II — WHERE THE BOUNDARY SITS

**OWNS:** the registry file and its generated views (O3); `lib/opal_naming.py` — `key()`, `name()`, `grade()` (O1, O2, O4,
O5); the Terraform module that exposes `name()` as a local (O2); the flagger limb in `commit-gate.sh` / `ds-precommit-check.py`
and the `safe-apply` pre-plan check (O4, O6); the census mode and its report (O5); the registry's tests (positive controls
built from the real shapes — `\b`-blind regexes are the measured failure).
**RELIES ON:** the naming brief's schema and vocabulary (ratified at L4 as one document); `05_IDENTITY_SPINE.md` rows (the
spine owns identity; this brief gives it a runtime); `safe-commit.sh` / `safe-apply` as the existing necks; `comp-find
--corpus aws` as the live-plane instrument for census mode.
**SIBLINGS:** the two D8 migration briefs (first consumers of `key()`; their IV.6 mapping tables are `grade()` outputs done
by hand); `NFRA_IAMROLES202609` (the fence's derived patterns land on its plane); `NFRA_COMPRAIL` (the rail's hook model
is the precedent for a gate that prints a redirect); `ADVI_FIRMSEP` (`firm-config.mjs` is its module — it becomes a
generated view, not a hand-edited file); the shared-advisor-router (its `p={…}` map becomes a build output).
⚠ **A question ruling (a) makes load-bearing, carried from `0.0.0_AB_MSTR` 96338 (~04:00Z), NOT resolved here:** D12
"Platform Operations" is SITEZ-placed (`@efcfa8cc5b`), while the infra a D12-bound fix touches (this fabric's IAM roles,
CloudFront behaviours, the shared-advisor-router) is LAPTOP-worked. Whether a laptop seat can mint and work a D12 member
is UNRESOLVED — MSTR found placement PARSING in `.tools/directives-check.py:18,:61` and no refusing guard, and recorded it
as unresolved rather than absent. The first flag the census emits with a D12 destination inherits this; it is
`1.0.0_SA_CTO`'s at L3 when that member is cut, and Andrew's if placement was meant to route execution to SITEZ.
**NOT THIS BRIEF'S:** any rename or move (D8/D12 by ruling (a)); a runtime `PutObject` interceptor (later, by his word);
the full ontology (off the critical path by ruling); alarms/monitors (moratorium — the flagger is a GATE that refuses,
never a notifier); tags.

---

# PART III — THE QUALITATIVE BAR

- **O1 passes when** a new producer for firm N+1 compiles with ZERO bucket-name string literals, and a reviewer can
  prove it by grep — where today every producer carries a `lib/config.py` with a bucket in it.
- **O3 passes when** changing a firm's bucket in the registry changes the router's deployed map, the IRPT map and the
  fence patterns in one build, and a seat can show the five old registries are now generated files or deleted.
- **O4 passes when** a commit adding `opal-data-inf/silver/...` as a literal is refused with the line
  `opal-data-assets/orion/inflection/silver/...` printed — and a commit adding the canonical form passes.
- **O5 passes when** the census mode reproduces the naming brief's IV.7 counts (±the alias/OUT split) from the same
  corpus, denominators printed.
- **O7 passes when** onboarding a demo firm in a scratch branch is one registry row and every derived file diffs as
  expected — the negative arm being that a hand-typed firm name anywhere is refused by O4.

---

# PART IV — THE SUBSTRATE: FINDINGS, EACH WITH WHAT WAS MEASURED

### IV.1 — No key builder exists; the registry exists FIVE times
`comp-find 'def (build_|make_|canonical_)?(s3_)?key\(|FIRM_CONFIG|firm_registry|def resolve_firm|def firm_bucket|def bucket_for'
lib/ data/ infra/aws/lambda/ portal/src .tools/ --band DEF`: **79 hits / 12,486 files; DEF 19** — of which 9 are vendored
library `def key(self)` (scipy, sortedcontainers, strictyaml in Lambda layers) and 10 are the estate's:
`data/firm_registry.json` (read by IRPT's `directory_runner.py:122` and `holdings_snapshot.py:111`), `infra/aws/lambda-edge/
_shared/firm-config.mjs` (the router's FIRM_CONFIG, read by the same two scripts at `:123`/`:112`), `firm_bucket_map()`
defined TWICE (`directory_runner.py:170`, `holdings_snapshot.py:145`), `_authz/loaders.py:43 bucket_for(tenant)`,
`perfrp_firm_pin.py:57 resolve_firm(firm)`. `comp-which` has no curated rule for either question (build ladder step 2
run; the catalog does not cover it). **Finding:** the estate already wanted a registry badly enough to write it five
times; nobody wrote the builder once. O3 is a consolidation; O1/O2 are new code at the MINIMUM (step 7 of the ladder,
after steps 1–6 were checked).

### IV.2 — The minting points, and which gate already stands at each
| point where a name is created | today | gate that exists | what O4 adds |
|---|---|---|---|
| an S3 key in a producer | `lib/config.py` per pipeline, `STAGING_PREFIX` constants, f-strings | `commit-gate.sh` (py_compile + `ds-precommit-check.py` + ruff) — the precommit bans an ENUMERATED foreign-bucket list | a `grade()` limb over string literals matching `^(s3://)?opal-` or a tier token, in the staged diff |
| a resource name in Terraform | per-module `name = "..."` literals; `s3-49financial.tf` template | `safe-apply` (identity gates, plan) — no naming limb | a pre-plan pass over `name`/`function_name`/`role_name`/`bucket` attributes in the changed `.tf` |
| a pointer/map | `firm-config.mjs`, `FIRM_BUCKET_MAP`, `firm_registry.json`, `partner_roster.json`, freshness YAMLs | none | generated from the registry; a hand edit to a generated file is refused |
| a Lambda artifact key | `lambda-source-map.json` `artifact_s3_key` | source-map tie (GAP-2, ruled) | UNCHANGED — the source-map tie stays; only the KEY's grammar is graded |
| the console / CLI | 339 LIVE-no-DECLARED nodes | none | OUT OF REACH at authoring time — IV.6 |

### IV.3 — The grader is a function of `(string, type) → (verdict, canonical)`, three verdicts, no fourth
`grade()` tokenises on `-`/`_`/`/`, maps each token through the registry (system, scope incl. aliases, tier, kind, cadence),
and checks slot order per the schema. CONFORMANT = every slot canonical; ALIAS = every slot resolves but ≥1 via the alias
table (`bd`, `49f`-where-long-required, `Inflection-`); OUT-OF-PATTERN = a token resolves to nothing, or a firm sits in the
system slot, or a tier is missing where the bucket requires one. A string the tokeniser cannot split is a tokeniser
defect surfaced as a test failure, never a fourth verdict (Rule 24 (i); the naming brief's Part V). **Positive controls**
are built from the real shapes measured in `09_NAMING_CENSUS.md` — `cot-bd-session-daily-et` must grade OUT-OF-PATTERN
(vendor `bd`), `blackdiamond/49f/credentials` CONFORMANT, `CloudWatchLogs` OUT-OF-PATTERN (duplicate + camel),
`opal-data-inf/silver/x` OUT-OF-PATTERN with canonical `opal-data-assets/{vendor}/inflection/silver/x` — vendor UNRESOLVED
without the producer's declared source, which is itself the finding the flagger prints.

### IV.4 — Why authoring-time is where it sticks (the two prior attempts, measured against the four points)
Nessie/Iceberg (`globgrph-nessie` task, `pyiceberg-nessie-deps` layer) sits BELOW the key: it versions a table whose
location was already chosen. The ontology (`infra/system/ontology/worldmodel/10_census/`) sits BESIDE the estate: it lists
`GOLD_ROOT`/`SERVE_ROOT` values it does not check. Neither is at a minting point in IV.2, so neither could refuse
`opal-data-inf`. **Finding:** the property Andrew asked for — "deterministically flag that which is out of pattern" — is a
property of the GATE at the minting point, and both prior attempts were built one layer away from it.

### IV.5 — Refuse vs warn: the enforcement strength (PROPOSAL for L4)
OUT-OF-PATTERN on a NEW string → REFUSE. ALIAS on a NEW string → REFUSE (a new name must not mint a short form the
registry does not sanction — `bd` is the case). ALIAS on an EXISTING string touched by the diff → WARN with the canonical
printed (touching a file must not force a rename outside a remediation project — that is ruling (a)'s boundary).
OUT-OF-PATTERN on an EXISTING string in a surface a remediation project OWNS → REFUSE unless the diff removes it (O6).
Kill switch: the same shape as `org/mcp/comprail-gate1.enforce` — a file, audited, so a false refusal has a named escape
and a log line, never a bypass flag on the commit.

### IV.6 — What authoring-time cannot reach, stated so it is not read as covered
339 `LIVE-no-DECLARED` nodes (Lambda 15, role 16, rule 10, log group 68, policy 36, …) have no repo surface; the flagger
sees them only in CENSUS mode (O5), never at a gate. The SSM force-download path and console edits mint names with no
commit. **Finding:** these are the reason his "runtime later" clause exists; until then the census report is their only
instrument, and declaring them (a D12 sweep, naming brief IV.7 #5) is the precondition for the gate to reach them.

### IV.7 — The registry's shape (the (b)-minimal he approved), as data not prose
```
infra/logic/registry/
  systems.yaml    key, kind(product|vendor|platform), long, short?, owner_directive      # naming brief IV.5's 118 tokens, resolved
  scopes.yaml     key, kind(firm|product-scope|demo), long, short, tenancy(client|general|demo), bucket, aliases[]
  tiers.yaml      bronze|silver|gold|platinum|state|code -> home rule (R4-R7, R21, R16) per tenancy
  kinds.yaml      the closed kind + cadence enums (naming brief IV.2)
  generated/      firm-config.mjs · firm_registry.json · firm_bucket_map.py · names.tf (locals) · deny_patterns.tf
```
`05_IDENTITY_SPINE.md` is the human-readable view; the YAML is what code reads; the generated files are what the five
registries in IV.1 become. A PR that edits a `generated/` file by hand is refused (O4's simplest rule).

### IV.8 — Order of dependence between the pieces (named, not sequenced)
`grade()` needs the registry; `key()`/`name()` need the registry and the schema; the gate needs `grade()`; the census
mode needs `grade()` + the live corpus; O3's consolidation needs the generated views; O6 needs the gate AND a
remediation project to exist. Nothing needs the full ontology.

---

# PART V — WHAT MUST BE TRUE (named, not sequenced)

- **THE ONE D14-BEFORE-D8 DEPENDENCY (Andrew ~04:2xZ, "get this sorted out with CTO"):** the firm-bucket fence
  (`DenyForeignFirmPrincipals` on `s3-49financial.tf`) is re-derived from the registry to key on the SCOPE slot -- deny
  any principal whose scope token is not the bucket's firm -- replacing the enumerated system prefixes (`cot-*`, `inf-*`,
  `mdpf-*`, `opal-assets-mdpf-*`), BEFORE the D8 migration mints `opal-data-inflection` / `-cottonwood` from that
  template. Otherwise the schema-named MDPF runner (`mdpf-{scope}-runner-role`) is denied on all three firms by design.
  D8's KEYS need nothing from this brief (they are already canonical); the builders and the flagger are PARALLEL to D8,
  not a gate on it. Order: (1) L4 ratifies the naming schema; (2) spine v0.2 rows + the derived fence on the template;
  (3) D8 migrations; (4) builders/flagger alongside, D8 the first `key()` caller if timing allows.

- The schema (naming brief IV.2) is ratified at L4 before `grade()`'s slot rules are written — the grader encodes law,
  it does not make it.
- The registry YAMLs exist and are the ONLY source for the five generated files before any consumer is repointed (O3).
- `grade()` ships with positive controls from the measured shapes (IV.3) and a test that a `\b`-style regex would fail.
- The gate limb has its kill switch and audit log before it is enabled; enabled first in WARN-only for a measured window
  long enough to see the false-refusal rate on real commits, then REFUSE per IV.5 — the window is a number for L4/L5,
  not this brief.
- The Terraform-label census (naming brief IV.7 #10) runs before the `safe-apply` limb is specified.
- The two D8 migrations use `key()` for their destination strings (they are the first callers; a hand-spelled canonical
  key in a migration would be the pattern breaking in the project built to fix it).
- The moratorium holds: nothing here emits to SNS/SES; a refusal is a gate exit code and a printed line.

# PART VI — STATUS · ⛔ NOT OUTCOME-BEARING · measured 2026-09-13 ~03:5xZ
- No `lib/opal_naming.py`, no registry YAML, no naming limb in any gate exists (IV.1).
- Five partial firm registries exist (IV.1); the deployed router map is a constant (`07_ROUTING_REDERIVATION.md`).
- `ds-precommit-check.py` carries `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` as enumerated lists (CLAUDE.md §5).
- 339 LIVE-no-DECLARED nodes on the live plane (`09_NAMING_CENSUS.md`).

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM
- **`ds-precommit-check.py` and `commit-gate.sh` were not read in this session** — cited from CLAUDE.md §5/§6; the
  limb's insertion point is L5's read.
- **`safe-apply`'s internals were not read**; "pre-plan pass" is a placement claim, not a measured hook.
- **The five registries' CONTENTS were not diffed** against each other or the deployed map — only their existence.
- **No false-refusal rate is estimated**; the WARN window exists to measure it.
- **Runtime enforcement is not designed** (his "runtime later").
- **Whether a laptop seat can work a D12 (SITEZ-placed) member was not measured** — Part II carries MSTR's finding.
- **Effort is not estimated.**

## REFS TO CARRY
```
  BRIEF PATH        docs/briefs/d14-executable-layer-brief-20260913.md
  PROJECT           NONE-YET (a D14 member; L3 is 1.0.0_SA_CTO's)
  EXISTING PRD      NONE. Consumes: d14-naming-schema-brief-20260913.md @bf21181208 (IV.2 schema, IV.6 vocabulary, IV.7 ranking)
  THE REFERENCE SET infra/logic/09_NAMING_CENSUS.md · 05_IDENTITY_SPINE @45160b1525 · 02_DOCTRINE @a49a7dca18 · 07_ROUTING_REDERIVATION
  RULINGS CARRIED   ANDREW_DIRECT_20260913_030xZ (commission) · 032xZ (source-first; two briefs; (b)-minimal; authoring-time) ·
                    035xZ @38f2268d48 (remediation shape (a); short forms; bd refused)
  PRIOR ART         the five partial registries (IV.1) · comprail's hook + kill-switch model · ds-precommit's enumerated ban list
  SIBLING PROJECTS  d8-legacy-firm-buckets-migration · d8-mdpf-canon-migration (first key() callers) · NFRA_IAMROLES202609 · ADVI_FIRMSEP
  WAITING-ON        L4: the schema ratified as one document · refuse/warn matrix (IV.5) · the WARN window length ·
                    the Terraform-label census before the safe-apply limb
  MEASURED AT       2026-09-13 ~03:5xZ UTC
```
**Author:** 4.0.0_SA_CRO (Chief Research Officer) · **Home:** org/tier1_exec/4.0.0_SA_CRO/
