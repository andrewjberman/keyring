# NFRA_MCPINDEX -- DECOMPOSITION (L5) -- round 1 -- v2

```json
{
 "project": "NFRA_MCPINDEX",
 "directive": "D9",
 "macro": "NFRA",
 "fabric": "laptop",
 "round": 1,
 "decomp_version": "v2",
 "supersedes": "v1 @020ab35a75 (frozen, never issued; recut on 1.0.0_SA_CTO 98944, offers A and B ruled before L6)",
 "step": 5,
 "prd_ref": "org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md@b7dc80e2cc",
 "prd_version": "v0.5",
 "prd_signed_at": "prd-signoff.py status NFRA_MCPINDEX at cut head 57751941a0: ADMITTED; ratified-text SIGNED 3.0.0_SA_CVO current; brief SIGNED 2.0.0_SA_COO~B current",
 "brief_ref": "docs/briefs/opal-mcp-tool-index-brief-20260917.md@826ac6925a (last commit on the file = the pin; no drift)",
 "research_ref": "docs/briefs/opal-mcp-tool-index-scoping-20260917.md@2a7fc3339f (RESEARCH ONLY, PRD VII.6 -- its D6 placement and business-first names are OVERRULED by Andrew 2026-09-17)",
 "author": "2.0.0_SA_COO~M",
 "cells": 38,
 "edges": 93,
 "chains_maximal_paths": 448,
 "components": 1,
 "critical_path_cells": 11,
 "cell_id_shape": "MX-<axis>-<n> (DECOMP_CELL_ID_CONVENTION shape 1)",
 "worker_serial": "0.9.0_WK_NFRA_MCPINDEX~<slot>",
 "measured_at_head": "7755816cf6 (re-checked at the cut head: 5 Gateway files moved in between, all MDPF_TAXSMA TX-g-1's; every fact cited below re-read at 57751941a0 and unchanged)",
 "cut_head": "57751941a0",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~M`, seated by `1.0.0_SA_CTO` on Andrew-direct 2026-09-21 ~00:5xZ (arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_005xZ_SELF_DRIVE_RESCOPED_MDPF_TAXSMA_NFRA_MCPINDEX.md`
@07b8a03ec3; msgs 98879, 98882). The letter `~M` was already named by this project's own `blocking` field from Andrew's
2026-09-18 ~23:3xZ seat order. One project, this seat. L5 is the COO's; no seat certifies this before L6.

**Input, graded before use.** `python .tools/prd-signoff.py status NFRA_MCPINDEX` at the cut head: v0.5 @b7dc80e2cc
**ADMITTED**, both halves SIGNED and current. `sequence-check.py --project NFRA_MCPINDEX`: PLACED, stage 0 ("Andrew's seat
priority -- MDPF_CANON, then IRPT_BCKEND, then MDPF_TAXSMA, then NFRA_MCPINDEX"), flags none. The whole PRD (370 lines) was
read; the brief was read at its pin; the research record was read AS RESEARCH (VII.6).

**Andrew's words that bind this cut.** His five card answers of 2026-09-17 (verbatim in the brief and the project row):
LGIC naming; versioned in S3; D9; Opal staff only, beta one at a time; portal reads precomputed, silver queried live.
~02:4xZ 2026-09-21 via 0.0.0_AB_MSTR (98917), verbatim: *"we try to stay light for the remainder of the session as far as
new spawns"* -- this binds the L6 fan-out's first wave (s.5), never the cut.

**v2 against v1, on 1.0.0_SA_CTO's rulings 98944 (both before L6; v1 was never issued).** Offer A: *"A HOME IS
DEFINED BY WHAT READS IT AT RUNTIME"* -- the repository `CAT` stays the ONE home and the source; S3 carries IMMUTABLE
VERSIONS, write-once, and is NEVER read on the serving path; if any runtime reader is ever pointed at the S3 copy the
ruling is VIOLATED. So `MX-c-3` no longer touches the load path, and its judgment criterion becomes a mechanical one.
Whether S3 versions are written this round was left to this seat: **they are**, because FWD-10's ACCEPT names "the
catalog is versioned in S3 at a builder-named address". Offer B: *"C2 CONSTRAINS THE TOOL'S PROPERTIES, NOT THE FILE THEY
ARE TYPED INTO"* -- the composed design is ADOPTED, with the bar that every tool is resolvable through BOTH registries
by name, PROVEN by an exercised lookup over the printed denominator, and that a composed path which can ship a tool
resolving through neither FAILS C2. `MX-c-4` and `MX-v-2` carry that bar as criteria. The cell set, edges and chain
read are unchanged from v1.

**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`).

**What binds every cell, from the PRD and the law.** Every new S3 address is `lib/opal_naming.py address()` output and
every new resource name is `name()` output (Rule 30); a builder refusal is a registry row, never a typed path. No tool
ships without a catalog entry and a safety classification (C2). Every answer states scope, as-of date, completeness and
source, and never sums across masters or firms (C4). No new vendor egress; YCharts only on Andrew's per-use word. Opal
staff only; admission is Andrew's. The PRD path `app/refs/DATA_CATALOG.yaml` is **Gateway-relative**: its repository
path is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (s.1 falsifier 1), and every path in this document is
repository-absolute.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  SURFACE MANIFEST rows (PRD SURFACE MANIFEST, S1 .. S11) ........................... 11
  minus rows excluded, read-only or delivered at L4 ..................................  -0
  ---------------------------------------------------------------------------------
  SURFACES THIS ROUND'S CELLS SERVE ................................................. 11   (each has >= 1 cell, s.3 coverage)
  CONTRACTS C1 .. C8 ................................................................  8   (each has >= 1 cell)
  ENDPOINT OUTCOMES FWD-1 .. FWD-10 (PRD header endpoint_outcomes) .................. 10   (each has >= 1 building cell and 1 proving cell)
  ACCEPTANCE LINES A1 .. A12 ......................................................... 12   (each has a proving cell)
  PRD OPEN ITEMS: PART V preconditions 9 + PART VII non-claims 6 ..................... 15   (s.2, each assigned)
```

The PRD's evidence boundary says the brief measured the repository only and **every capacity claim is DESIRED until a
cell exercises it**. VII.5 binds L5 to **print the bytes at a cited line, never grep for the quote**. Six falsifiers were
run against the PRD's own claims before any cell was cut. Five of them changed what a cell must do.

**Falsifier 1 -- the catalog's path (GRAIN).** `test -f app/refs/DATA_CATALOG.yaml` at the repository root: **ABSENT**.
`git ls-files '*DATA_CATALOG*'`: **1 tracked path**, `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (129,860
bytes; last commit 96dcb4a66a 2026-08-20 `0.5.0_AE_OpalETL~Z`). The PRD's path is relative to the Gateway root. A worker
handed the PRD's string as a repository path reads nothing. Every cell below names the repository path.

**Falsifier 2 -- C1's premise that the live catalog has no identified writer (STATE, printed at the bytes).** C1 and
its v0.2 repair rest on `emit_catalog_v02.py:5`. At 7755816cf6 and again at 57751941a0:

```
  emit_catalog_v02.py:5     THE LIVE refs/DATA_CATALOG.yaml IS NEVER TOUCHED BY THIS SCRIPT.        <- DOCSTRING
  emit_catalog_v02.py:38-41 # THE ONE CATALOG HOME (CTO~Z ruling 2448/2449, 2026-08-20): the runtime file query_v0 loads,
                            # catalog_gate enforces, the EC2 deploy tree ships, and this emitter WRITES. No staged copy,
                            # no second output (V03-2; the v0.2 staged file was deleted in the same commit).
  emit_catalog_v02.py:42-43 OUT_DIR = ...("infra","aws","ec2","opal-gateway","app","refs"); OUT = .../"DATA_CATALOG.yaml"
  emit_catalog_v02.py:735   with io.open(OUT, "w", encoding="ascii") as f:                            <- THE WRITE
  DATA_CATALOG.yaml:7-9     HOME RULE: ... THIS EMITTER writes it. No staged copy, no BG-side copy (deleted @88a00a3f81)
  graphql_plumbing/DESIGN.md:66-67  ... emit_catalog_v02.py is the ONLY writer (single output path; the battery asserts it)
```

**The code writes the live file. Only the docstring says otherwise, and it is superseded text** -- the V03-2 change
rewrote the comment beside `OUT` and left the module docstring standing. Four carriers agree (code, code comment,
catalog header, DESIGN.md) against one (the docstring). The PRD read the one. **What this does NOT establish:** that the
emitter RUNS on any cadence. The catalog's last commit is a 2026-08-20 port act, so the writer is identified in CODE
(DESIRED) and has not been EXERCISED since. `MX-c-1` keeps C1's census bar and its exercise, and it **starts from this
measured hypothesis** instead of hunting for a writer. It also corrects the docstring so the next reader is not misled
the same way. s.11 finding 1.

**Falsifier 3 -- S4's transaction table (GRAIN).** The PRD says "exposing `fact_trn` is this project's own cell".
`data/assets/scripts/silver/schwab_projections.py:40-82` declares **4 projections**: `dim_position` (:43), **`dim_transaction`
(:55, TRN section 1)**, `dim_asset` (:71), `dim_balance` (:82). No `fact_trn` exists under that name. The Schwab engine's
`integrations/schwab/datasets.json` exposes **3 of the 4** (`dim_position`, `dim_balance`, `dim_asset`, parsed,
denominator 3), and `data_entitlement.py:64` pins the same three. So the unexposed transaction table is **`dim_transaction`**.
The research record (P2) agrees ("`dim_transaction` and `fact_*` not exposed"). `MX-t-2` names it. s.11 finding 3.

**Falsifier 4 -- S9's gate (STATE).** PRD S9, V.6, A7 and brief-coverage row 10 carry entity resolution as PARKED on D3's
residual enum. `infra/aws/ec2/opal-gateway/app/entity_resolution/SCAFFOLD.md:1-11`, printed: *"ENUM GATE DISCHARGED
2026-08-19 ~2310Z ... **GATE DISCHARGED @2ff219b592** ... the D3.1 residual enum is adopted and CONSUMED ... **REMAINING
GATE: the identity-plane DATA BINDING** (a06 crosswalk / bridge / household nesting -- client-data surfaces, a
laptop-deploy act). `resolve()` raises loudly until then."* Both D3 orders read complete
(`D3_MODELOVERLAY.TO-D3.1` and `.TO-D3.1b`, `<status>` printed). **The PRD's gate is discharged. The remaining gate is a
data binding, and it is a laptop act inside S9.** `MX-e-1` is therefore OPEN, not HELD. s.11 finding 4.

**Falsifier 5 -- the catalog's versioned S3 home under the builder (Rule 30).** `address(source, scope, tier, table,
partition)` at the cut head. The positive control resolves (`mdpf`,`49financial`,`platinum`,... ->
`s3://opal-data-49financial/...`). For the catalog:

```
  REFUSED  ("gateway","opal",     *, "data_catalog", ...)  scope 'opal' resolves to no scopes.json row
  REFUSED  ("gateway","all-firms",*, "data_catalog", ...)  scope 'all-firms' resolves to no scopes.json row
  REFUSED  ("gateway","global","state"|"gold", ...)        no home bucket for tier state|gold of scope global
  OK       ("gateway","global","platinum","data_catalog","version=v0.4") -> s3://opal-data-portal-v2/gateway/global/platinum/data_catalog/version=v0.4
  OK       ("gateway","global","silver",  "data_catalog","version=v0.4") -> s3://opal-data-assets/gateway/global/silver/data_catalog/version=v0.4
```

`scopes.json` holds **9 rows** (4 FIRM, 1 GLOBAL, 2 MASTER, 2 PRODUCT). A builder-named home **exists today**, so no
registry row is owed. Which tier is correct is `MX-c-3`'s choice, stated with its reason. The `gateway` system key is
present in `systems.json` (25 keys). s.11 finding 8.

**Falsifier 6 -- the PRD's other citations (VII.5), printed at the cited lines at the cut head.**

| citation | printed | verdict |
|---|---|---|
| `DATA_CATALOG.yaml:3` "BUILT BY emit_catalog_v02.py" | as quoted | HOLDS |
| `emit_catalog_v02.py:5` disclaimer | as quoted | HOLDS AS TEXT; SUPERSEDED BY THE CODE (falsifier 2) |
| `D6_OPAL_ANALYST_GRAPHQL_PRD.md:57` | "The GraphQL layer cannot precede W5 without re-minting a second catalog" | HOLDS |
| `D6_OPAL_ANALYST_GRAPHQL_PRD.md:102-103` | "the index is the only thing that keeps the resolver catalog single-sourced" | HOLDS |
| `graphql_plumbing/DESIGN.md:67` "the ONLY writer" | as quoted, at :66-67 | HOLDS (and agrees with the code, not the docstring) |
| `graphql_plumbing/DESIGN.md:41-49` five parked business tools | `find_account`, `get_account_details`, `get_account_performance`, `find_accounts_missing_fee_splits`, `get_account_data_issues` at :44-45 | HOLDS; **the names violate C3** (no system token) -- s.11 finding 7 |
| `lib/opal_naming.py:1589-1602` (brief IV.4) "scope passed as scope" | `def _long_scope(reg, scope, classes=None)` -- validates scope as its own slot, LONG form required | HOLDS AT THE FUNCTION; pin it by name, not line |
| `NAMING_SCHEMA.json` "v1.10 does not grade MCP tool names" | version **v1.12**; `not_covered` 6 entries, 0 name tools; 0 `mcp`/tool-name tokens in the whole schema | SUBSTANCE HOLDS; **version pin stale** -- s.11 finding 6 |
| brief IV.9 `read_teams_attachment` unclassified | in `data_entitlement.NATIVE_TOOLS` (:90); absent from `destructive_ops.SAFE_TOOLS` and `DESTRUCTIVE_OPS`; `classify()` returns `_UNKNOWN_TAG` (fail-closed) | HOLDS |
| Ground truth "49 registered, 44 enabled" | 35 native + 9 integration + 5 Schwab = 49; pinned `test_entitlement_admin.py:332 assert len(registered_tool_names) == 44` | HOLDS |
| Ground truth "three `dim_*` exposed" | 3 of 4 projections exposed | HOLDS (and names the 4th, falsifier 3) |
| brief IV.2 "36 served-data rows" | YAML parse: 15 channels, 36 rows | HOLDS (different instrument from the brief's census) |

**Status vocabulary.** Evidence columns take four values. NOT-EVALUATED is one of them, so non-evaluation is never a verdict.

| value | meaning |
|---|---|
| `MEASURED` | evidence in hand at the cut, instrument named |
| `DECLARED` | the PRD, brief or research record asserts it; not re-measured here |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply |

Cell status takes `OPEN`, `HELD` (a named gate stands, s.6) or `DONE`. At v1: **33 OPEN, 5 HELD** (`MX-r-2` on G-A;
`MX-v-3`, `MX-v-5` on G-B; `MX-v-4` on G-B and G-Q; `MX-i-3` on G-S). `MX-r-1` is OPEN with a refusal-shaped first
criterion (s.3, release).

---

## 2. THE PRD'S OPEN ITEMS, EACH ASSIGNED

PART V (9 preconditions) and PART VII (6 non-claims) are the PRD's own list of what is not yet true. Assigned 15 of 15.
None becomes an expected value about the world before its cell reads it.

| item | the open question (short form) | cells that answer it |
|---|---|---|
| V.1 | catalog extended to silver, ONE writer, versioned S3 home from the builder | `MX-c-1` (writer), `MX-c-2` (schema), `MX-c-3` (home) |
| V.2 | per-property analysis before that property's tools | `MX-a-1` .. `MX-a-7`; each `MX-t-k` depends on `MX-a-k` |
| V.3 | one fenced read role per property; the grant model extended beyond two masters and three datasets | `MX-i-1`, `MX-i-2`, `MX-i-3` (roles); `MX-g-1` (grant model) |
| V.4 | every tool in `destructive_ops` and `data_entitlement`; the pinned count moves with each tool | `MX-c-4` (the mechanism); every tool cell moves its own count |
| V.5 | NFRA_OPLGTW's Schwab tools enabled before FWD-3 is exercised | **not this project's act.** Gate G-Q (s.6); holds `MX-v-4` only |
| V.6 | a way to match one person across systems before FWD-7 | `MX-e-1` -- the D3 enum gate is DISCHARGED (s.1 falsifier 4); the data binding is the cell |
| V.7 | a long-history substrate before FWD-8's first half | `MX-h-1` (measure and choose), `MX-h-2` (build and answer once) |
| V.8 | each new integration through the enablement checklist | every tool cell cites `NFRA_INTEGRATIONS_STANDARD.md` s.5 and s.8.1; the enable is gate G-A on `MX-r-2` |
| V.9 | a roster Andrew controls, one at a time | `MX-g-2`; the admission itself is gate G-B |
| VII.1 | AWS state, sizes, counts and timings unmeasured | `MX-p-1` (Gateway and IAM, live); each `MX-a-k` (its property's silver, live); `MX-h-1` (sizes for long history) |
| VII.2 | the common questions are not enumerated | `MX-a-1` .. `MX-a-7` write them; `MX-v-1` authors the independent question set from them; PART III's beta bar feeds round 2 |
| VII.3 | the naming rule is a reading, the canon does not grade tools | `MX-n-1` enforces it by criterion; the schema bump stays the CTO's to raise at LGIC_NAMING |
| VII.4 | Bloomberg is the SITEZ read, not claimed here | `MX-h-3` names it and builds nothing for it |
| VII.5 | citations not re-verified line by line | done for the PRD's citations here (s.1 falsifier 6); every cell re-prints any line it relies on |
| VII.6 | the scoping record is research, and two of its recommendations were overruled | read as research only; `MX-t-*` and `MX-d-1` name tools under C3, never the record's business-first names |

---

## 3. THE CELLS -- 38

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `MX`. Axes: `p` baseline, `c` catalog, `n` naming,
`g` grant model and roster, `d` discover, `q` typed query, `a` per-property analysis, `t` per-property tools, `i` read
roles, `e` entity resolution, `h` on-demand, `v` validation, `r` release.

Path abbreviations, relative to the repository root: `GW` = `infra/aws/ec2/opal-gateway`; `APP` = `GW/app`; `INT` =
`APP/integrations`; `TST` = `GW/tests`; `CAT` = `APP/refs/DATA_CATALOG.yaml`; `EMIT` = `workflows/atom_decomposition`;
`TFGW` = `infra/aws/terraform/opal-gateway`; `STD` = `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`. Every cell also
writes `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~<slot>/` and may append to the
investigation file. A cell that changes the world (an S3 write, an apply or a deploy) also writes
`org/critical_paths/change_management/` and its `org/critical_paths/.open_deploys/<slug>.json` sentinel.

**Each acceptance line is ONE criterion.** `J` marks a judgment criterion: no verdict at L7, graded by `3.0.0_SA_CVO` at
L9. A criterion asserting a control states what must DIFFER when the control is engaged, and proves it in the same
harness with the control disengaged (spine L6); those are marked `(difference)`. A **census** criterion owes no flipped
twin; its discipline is the printed denominator (spine L6 non-application).

**The one architectural fact every tool cell rests on.** FWD-10's ACCEPT and PROOF require that adding a property is
**"one catalog entry plus a tool ... nothing else"**. Today it is not. Adding one integration touches `INT/registry.py`
(`_load_builtin_factories`, a hand list at :28-48), `APP/destructive_ops.py`, `APP/data_entitlement.py` (`NATIVE_TOOLS`,
`INTEGRATION_TOOLS`, `TOOL_CLASSES`, and the Schwab-only `MASTERS`/`DATASETS` at :63-64) and the pinned count
`TST/test_entitlement_admin.py:332`. So `MX-c-4` and `MX-g-1` make classification, registration and grant scope **compose
from each integration's own declaration**. C2's letter still holds: every tool is still resolvable through both
registries by name, and each tool cell still moves its **own** pinned count. After those two cells, every property's
tools write **only their own integration directory and their own test file**. That is what gives this decomposition
parallel width, and it is what FWD-10 is graded on. s.10 choice 1.

### Baseline

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-p-1` | the live pre-change baseline of the Gateway and its IAM, read only | VII.1; inputs to `MX-i-3`, `MX-r-1` | deliverables only | OPEN |

**`MX-p-1` acceptance**
- the deployed Gateway commit on instance `i-07dccb1615503ac99` is read through SSM and printed, with the reading's UTC time (98928 reported 1764e54a16 at ~03:0xZ 2026-09-21; the cell re-reads, never inherits)
- the deployed `ENABLED_INTEGRATIONS` value on the host is read and printed, its empty case printed as empty rather than omitted
- the deployed `app/refs/DATA_CATALOG.yaml` SHA-256 on the host is compared with the blob at the cell's HEAD, MATCH or MISMATCH printed
- the registered MCP tool list the deployed Gateway serves is read in-process on the host, denominator printed, and compared by name with the 49-name union of `NATIVE_TOOLS`, `INTEGRATION_TOOLS` and `SCHWAB_TOOLS` at the cell's HEAD
- `opal-gateway-role` trust and every inline and attached policy are read back live with `aws iam`, and each statement is compared with `comp-iam role opal-gateway-role`'s 14 DESIRED statements, per-statement MATCH or DRIFT printed
- the Schwab reader role declared in `TFGW/schwab_reader_iam.tf` is read back live, and its S3 resource fence is printed by prefix
- the current release's rollback target is identified by commit and artifact key under `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/`, and a Head on that key is printed (existence, size, LastModified)
- `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` s.7.2 step 1's restorability precondition is printed at the bytes and evaluated against that rollback target, PASS or FAIL with the reason
- `python -m pytest infra/aws/ec2/opal-gateway/tests -q` at the cell's HEAD records collected, passed and failed counts, and every failing or erroring test id
- every AWS call in the cell's command log is a read verb (Describe, Get, List, Head, SSM read-only send-command)

### S1 -- the catalog

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-c-1` | the live catalog writer confirmed by census and exercised once; the stale docstring corrected | C1, V.1, FWD-10 | `EMIT/emit_catalog_v02.py` (the module docstring, lines 1-10, ONLY) | OPEN |
| `MX-c-2` | the catalog schema extended to silver datasets, one source file per entry, through the one writer | C1, V.1, FWD-1, FWD-10 | `EMIT/emit_catalog_v02.py` (the entry reader and field emission), `EMIT/validate_catalog_v02.py`, `EMIT/battery_catalog_v02.py`, `EMIT/catalog_entries/` (new, one file per dataset entry), `CAT` (emitter output only), `EMIT/tests/test_catalog_silver_entries.py` (new) | OPEN |
| `MX-c-3` | immutable catalog versions archived in S3 at a builder-named address; the repository file stays the ONE runtime home (CTO 98944) | C1, FWD-10 | `EMIT/publish_catalog_version.py` (new), `EMIT/tests/test_catalog_home.py` (new) | OPEN |
| `MX-c-4` | classification and registration compose from each integration's declaration; a tool with no catalog entry or no classification is REFUSED at registration | C2, V.4, A11, FWD-10 | `APP/destructive_ops.py`, `APP/data_entitlement.py` (tool-class composition only), `INT/base.py`, `INT/registry.py`, `TST/test_entitlement_admin.py` (the :332 pin only), `TST/test_tool_classification_composition.py` (new) | OPEN |

**`MX-c-1` acceptance**
- every file in the repository that opens `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` or a path ending `refs/DATA_CATALOG.yaml` for writing is enumerated, denominator printed, by a census that reads code (open-for-write, `write_text`, `shutil`, redirection), never by a docstring or header
- each candidate writer's own bytes are printed at its write call and at any line that disclaims the live file
- the census names exactly one writer whose write call targets the live path, or it reports zero or more than one and REFUSES
- (difference) the named writer is run once at the cell's HEAD with one reversible change to an emitter input, the served file changes by exactly that row, and the same run with the input unchanged leaves the served file's SHA-256 unchanged (the run and its revert both in the cell's command log)
- the module docstring's disclaimer at `EMIT/emit_catalog_v02.py:5` is replaced by a statement agreeing with `:38-43`, and no other line of the file changes (`git diff --stat` shows the docstring hunk only)
- `CAT`'s header line 3 still names the writer, re-printed after the change
- `J` the cell's writer finding is sufficient for a reader who has only the catalog's header, the emitter and this cell's record to know who writes the live catalog

**`MX-c-2` acceptance**
- the entry schema carries exactly the C1 fields -- business meaning, example questions, grain, freshness field, firm-scope rule, never-sum rules, producer, tools -- each with a type the validator enforces
- a dataset entry is ONE source file under `EMIT/catalog_entries/`, and the emitter reads that directory
- (difference) with one planted entry file added, the emitter's output gains exactly that entry and the validator passes; with the same file missing one C1 field, the validator REFUSES and names the field
- the 36 existing rows across 15 channels re-emit with every existing field unchanged, compared field by field and denominator printed (version and build-head fields excepted and named)
- `validate_catalog_v02.py` and `battery_catalog_v02.py` pass at the cell's HEAD, run output printed
- the emitted file stays ASCII-clean (`len(b) - len(b.decode('utf-8')) == 0` printed)
- no second catalog file is created (a census of `*DATA_CATALOG*` and `*catalog*.yaml` under `infra/aws/ec2/opal-gateway` and `workflows/atom_decomposition`, before and after, denominators printed, identical except the new `catalog_entries/` source files)
- the Rule 24 four-postulate record for the entry schema's value sets (firm-scope rule, never-sum rules, freshness field kinds) is written in the cell's deliverable with a word-boundary token census

**`MX-c-3` acceptance**
- the archive's S3 key is `address()` output at the cell's HEAD, the call and its return printed, and the module computes the key only through that call
- the chosen tier (platinum or silver at scope `global`, the two the builder resolves) is stated with one reason, and the two refused tiers are recorded as refused
- the publisher's only input is the repository file `CAT`, and a published object's SHA-256 equals `CAT`'s at the publishing commit
- a version, once written, is never overwritten: a second publish of the same version with different bytes is refused, and a publish of new bytes mints a new version
- the publish opens its change-management entry and commits the OPEN sentinel before the S3 write, and closes both before the read that grades it
- one published version is read back from S3 with its object version id, SHA-256 and LastModified, and the SHA-256 equals `CAT`'s at the publishing commit
- exactly ONE runtime reader of the catalog exists and its path resolves to the repository `CAT`: every catalog load under `infra/aws/ec2/opal-gateway/app` is censused by code read (open, `yaml` load, `CATALOG_PATH`), denominator printed, and each resolves to `CAT`
- zero readers of the archive exist on the serving path: the archive's bucket-and-prefix string is censused over `infra/aws/ec2/opal-gateway`, denominator printed, and occurs only in this cell's publisher and its test
- (difference) the cell's test fails when a planted runtime loader pointed at the S3 archive is added under `infra/aws/ec2/opal-gateway/app`, and passes with the plant removed (CTO 98944: a runtime reader of the S3 copy VIOLATES the ruling)
- no statement is added to `opal-gateway-role` for the archive, compared by name against `MX-p-1`'s 14 statements
- no file under `infra/aws/ec2/opal-gateway/app` changes (`git diff --stat` over that directory, printed empty)

**`MX-c-4` acceptance**
- `IntegrationSpec` (`INT/base.py`) carries a per-tool classification and a per-tool catalog-entry reference, and `validate_integration_spec` refuses a spec with either missing
- `destructive_ops.classify(tool)` returns the declared class for an integration tool, read through the registered spec, and still returns `_UNKNOWN_TAG` (fail-closed) for any tool with no declaration
- (difference) a planted integration whose one tool has no classification is refused at `register_enabled` and adds zero tools, while the same integration with the classification declared registers that tool, in one test module (FWD-10 PROOF, the refusal half)
- (difference) a planted tool with a classification but no catalog-entry reference is refused at registration, while the same tool with the reference registers
- `INT/registry.py` discovers integrations from their own directories, and the four existing ids (`ycharts`, `opal_portal`, `globgrph`, `schwab`) register exactly as before, names printed before and after
- every one of the 49 existing tool names resolves through `destructive_ops.classify` and `data_entitlement` to the class it had before the change, compared by name, denominator 49, zero differences
- `read_teams_attachment` is classified, and it is no longer denied by the fail-closed branch; the classification it receives is stated with its reason (`J` below)
- `J` `read_teams_attachment`'s classification is correct for a tool that reads the content of a Teams attachment by URL, and it neither widens what any tier can reach nor reads as a write
- the pinned count at `TST/test_entitlement_admin.py:332` becomes a derived count that asserts, by name, every registered tool against its integration's own pinned list, and it still fails when a tool is registered without being pinned (difference: one planted unpinned tool fails it; removing the plant passes)
- the Gateway suite's collected, passed and failed counts are printed before and after the edit, and no test that passed before fails after
- C2's bar, EXERCISED (CTO 98944): for every registered tool, denominator printed, a lookup by name through `destructive_ops.classify` returns its declared class and a lookup by name through `data_entitlement` returns its tool class, and the tool's catalog-entry reference resolves to an entry in `CAT` -- zero tools fail any of the three
- (difference) a planted tool reachable by the composed registration path but resolving through neither registry is REFUSED at registration, while the same tool with both declarations registers (a composed path that could ship it FAILS C2)

### C3 -- naming

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-n-1` | the C3 tool-name rule as a registration-time validator | C3, A12, VII.3 | `APP/tool_names.py` (new), `INT/base.py` (the name check wired into `validate_integration_spec` only), `TST/test_tool_names.py` (new) | OPEN |

**`MX-n-1` acceptance**
- the rule is `{system}_{function}[_{qualifier}]`: `system` a key of `infra/logic/registry/systems.json` read at runtime, or the reserved `opal` (`NAMING_SCHEMA.json` `system.reserved`); `function` a base-form verb from a stated list; the validator imports no hand-typed system list
- a scope argument is validated through `opal_naming`'s `_long_scope` (LONG form, a `scopes.json` row), and a scope value folded into a tool name is refused
- (difference) a planted tool named without a system token (the parked `find_account` shape, `DESIGN.md:44`) is refused at registration, while the same tool renamed to a conforming name registers
- (difference) a planted tool whose name carries a scope token (a master number or a firm name) is refused, while the same tool with the scope as an argument registers
- the rule binds this project's integrations; the 49 existing names are censused against it with the conforming count and the non-conforming list printed, and the non-conforming legacy names are listed as grandfathered by name, never exempted by pattern
- `J` the verb list and the grandfathered list are the narrowest that let every existing tool keep working

### Grant model and roster

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-g-1` | the grant model extended beyond Schwab: each integration declares its scope (masters or firms, datasets, prefixes, columns), composed by `data_entitlement` | C7, V.3, FWD-3..FWD-5, FWD-9 | `APP/data_entitlement.py` (the grant-scope model only), `TST/test_grant_model_composition.py` (new) | OPEN |
| `MX-g-2` | the beta roster over every data tool: per-person tool lists, admission and removal at runtime | C8, S11, V.9, FWD-9 | `GW/ops/schwab_entitlement_admin.py` (generalised to every data integration), `APP/access_state.py` (only if the roster's runtime state needs a new field), `TST/test_beta_roster.py` (new) | OPEN |

**`MX-g-1` acceptance**
- `MASTERS` and `DATASETS` (`data_entitlement.py:63-64`) are no longer the whole model: each integration's declared scope is composed, and the Schwab integration declares exactly the two masters and three datasets it has today
- every existing Schwab entitlement test passes unchanged, counts printed before and after
- (difference) a principal granted master `08242234` who asks for master `08335338` in any phrasing is refused with `ENTITLEMENT_DENIED`, while the same request for `08242234` passes, in one test client (the existing pair, re-run under the composed model)
- (difference) a principal granted firm A of a planted firm-scoped integration is refused firm B's rows in every enumerated phrasing (scope argument, filter value, group-by value), while firm A's request passes
- a scope value absent from `scopes.json` is refused before any read
- the model extends NFRA_OPLGTW's rather than forking it: one grant table, one `ENTITLEMENT_DENIED` code, one audit path, shown by the call path in the test
- `J` no composition rule lets one integration's declaration widen another integration's scope

**`MX-g-2` acceptance**
- (difference) a principal who is not admitted lists ZERO tools of this project's integrations, while the same principal once admitted lists exactly the granted set, compared by name
- an admitted principal lists exactly their granted set and nothing else, compared by name, denominator printed
- (difference) removal takes effect on the next call with no redeploy and no process restart: the same principal, same process, lists the tools before removal and none after, timestamps printed
- admission and removal are one operator command each, one person per command, and a command naming two people is refused
- a principal outside Opal staff is refused admission
- every admission and removal writes one audit record carrying the operator, the principal reference, the change and its UTC time

### S2 -- discover

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-d-1` | the discover family under the `opal` system, reading the ONE catalog | S2, FWD-1, A1 | `INT/opal_discover/` (new), `TST/test_opal_discover.py` (new) | OPEN |

**`MX-d-1` acceptance**
- the family reads the catalog through the existing load path, which resolves to the repository `CAT` (the ONE home, CTO 98944), never the S3 archive, and reuses `APP/graphql_plumbing/catalog_gate.py` for the firm gate rather than re-implementing it
- for a catalogued dataset, the answer names the property, the dataset, its freshness field and latest value, its firm scope, its caveats and the next tool to call
- (difference) for an uncatalogued subject, the answer says it is not catalogued and names no dataset and no tool, while a catalogued subject in the same test returns a named tool
- every tool name passes `MX-n-1`'s validator and every tool carries its classification and catalog reference (`MX-c-4`)
- the family's own pinned tool list moves with each tool, in this cell's test
- the family is loaded for every admitted session and for no non-admitted session (tested against `MX-g-2`'s roster once present; before that, against a stub stated as a stub)

### S6 / C6 -- the typed query

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-q-1` | the typed query generalised to any catalogued silver dataset, reusing the Schwab engine by import | C6, S6, FWD-6, A6 | `INT/opal_query/` (new), `TST/test_opal_query.py` (new) | OPEN |

**`MX-q-1` acceptance**
- the query is a structured object (filters, group-bys, aggregates); a raw SQL string in any field is refused
- the engine is the Schwab engine reached by import (`INT/schwab/engine.py`, `query.py`); no file under `INT/schwab/` changes (`git diff --stat` over that directory is empty)
- a dataset is queryable only through its catalog entry: grain, additivity and never-sum rules are read from the entry, not typed in the module
- (difference) a query that sums an additive field across two masters or two firms is refused on the call path, while the same query scoped to one master passes -- and a mutant that bypasses the check makes the refusing arm FAIL (R-OG-13/R-OG-15 bar: the check is on the path the tool actually calls)
- (difference) a group-by that breaks the entry's declared grain is refused, while a grain-respecting group-by passes, with its mutant control
- hard caps on scanned bytes, rows and wall time are read from configuration, and each cap, when hit, yields a response marked cut short with the cap named -- never a silent truncation marked complete
- every response carries the C4 envelope: scope, as-of date, complete-or-cut-short, source dataset
- "no data for that date" is returned as no data, never as zero (a planted empty partition proves it)
- every tool name passes `MX-n-1` and every tool is classified and catalog-referenced (`MX-c-4`); this cell's pinned list moves with each tool

### S8 -- the per-property analysis (read only; each carries its property's first live measurement)

| cell | property | serves | writes | status |
|---|---|---|---|---|
| `MX-a-1` | Portal: `platinum/mdpf`, `platinum/etfs`, `platinum/advi`, `json/*` in `opal-data-portal-v2`; advisor intelligence in the Inflection and Cottonwood firm buckets | S8, FWD-2, C5, A2 | deliverables only | OPEN |
| `MX-a-2` | Schwab: masters 08242234 and 08335338, the four projections | S8, FWD-3 | deliverables only | OPEN |
| `MX-a-3` | Black Diamond | S8, FWD-4 | deliverables only | OPEN |
| `MX-a-4` | Orion (Inflection) | S8, FWD-4 | deliverables only | OPEN |
| `MX-a-5` | Eclipse (Inflection) | S8, FWD-4 | deliverables only | OPEN |
| `MX-a-6` | SmartX | S8, FWD-4 | deliverables only | OPEN |
| `MX-a-7` | ETFs: TrueShares and Pathfinder, per fund | S8, FWD-5 | deliverables only | OPEN |

**`MX-a-k` acceptance (each of the seven, over its own property)**
- the property's silver (or, for `MX-a-1`, served) prefixes are listed live at the cell's run time, with object count, total bytes and newest partition date per table, and the read verb in the command log
- each table's grain, freshness field and latest value are read from the objects or their producer's code at the cell's HEAD, the source printed per field
- each table's firm or master scope rule is stated with the key-prefix segment that carries it, and a table whose scope cannot be read from its key is named
- every never-sum rule is stated with its reason (cross-master, cross-firm, cross-date, non-additive field)
- the property's common questions are written down as a numbered list, each with the table and the fields that answer it; the list's source is stated (producer code, portal page, prior art, or reasoning) and nothing on it is presented as measured user demand
- each common question is assigned to a proposed purpose-built tool or to the typed query, with the reason
- the proposed tool names pass `MX-n-1`'s rule as stated in C3 (the validator may not exist yet; the rule's text is the input)
- the proposed read fence is stated as exact prefixes, and any table outside it is named as excluded with the reason
- a property with no silver or served data at the cell's run time says so, and proposes no tool
- `J` the question list is what a staff member would plausibly ask of this property, and no common question is left to the typed query without a stated reason

**Property-specific additions**
- `MX-a-1`: the four surface families are the denominator (C5, A2), and each surface's portal page is named with the precomputed key it reads
- `MX-a-1`: the advisor-intelligence tables' firm buckets and prefixes are listed separately from `opal-data-portal-v2`, as C5's separate grant requires
- `MX-a-2`: `dim_transaction` (`schwab_projections.py:55`) is listed with its columns, and whether the Schwab reader role's fence admits its prefix is read from `TFGW/schwab_reader_iam.tf` (DESIRED) and from `MX-p-1`'s live read once present (APPLIED)
- `MX-a-2`: the 16 full Schwab tables the research record names (P2) are censused, and each is marked in or out of this round's tool set with the reason
- `MX-a-7`: every question class is answered per fund (TrueShares, Pathfinder), and a fund with no data for a date is named with that date

### S3, S4, S5 -- per-property tools

Each tool cell writes its own new integration directory and its own test file, and nothing else. The catalog is
generated, so a tool cell also adds its own entry file(s) under `EMIT/catalog_entries/` and re-emits `CAT` through the
one writer. `CAT` is never hand-merged; a conflict on it resolves by re-emission at the drain (s.8 bound 10).

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-t-1` | Portal tools over the four surface families, reading the SAME precomputed keys the portal reads | S3, C5, FWD-2, A2 | `INT/portal_index/` (new), `TST/test_portal_index.py` (new), `EMIT/catalog_entries/portal_*` (new entries), `CAT` (emitter output) | OPEN |
| `MX-t-2` | Schwab purpose-built tools for positions, balances and transactions, with `dim_transaction` exposed | S4, FWD-3, A3 | `INT/schwab_index/` (new), `TST/test_schwab_index.py` (new), `EMIT/catalog_entries/schwab_*`, `CAT` | OPEN |
| `MX-t-3` | Black Diamond tools | S4, FWD-4, A4 | `INT/blackdiamond_index/` (new), `TST/test_blackdiamond_index.py` (new), `EMIT/catalog_entries/blackdiamond_*`, `CAT` | OPEN |
| `MX-t-4` | Orion tools -- **the FWD-10 exercise: the next property after the first three, added as a catalog entry plus a tool, timed** | S4, FWD-4, FWD-10, A10 | `INT/orion_index/` (new), `TST/test_orion_index.py` (new), `EMIT/catalog_entries/orion_*`, `CAT` | OPEN |
| `MX-t-5` | Eclipse tools | S4, FWD-4, A4 | `INT/eclipse_index/` (new), `TST/test_eclipse_index.py` (new), `EMIT/catalog_entries/eclipse_*`, `CAT` | OPEN |
| `MX-t-6` | SmartX tools | S4, FWD-4, A4 | `INT/smartx_index/` (new), `TST/test_smartx_index.py` (new), `EMIT/catalog_entries/smartx_*`, `CAT` | OPEN |
| `MX-t-7` | ETF tools per fund: holdings, net assets, daily NAV | S5, FWD-5, A5 | `INT/etfs_index/` (new), `TST/test_etfs_index.py` (new), `EMIT/catalog_entries/etfs_*`, `CAT` | OPEN |

**`MX-t-k` acceptance (each of the seven)**
- every tool the cell registers is one its analysis (`MX-a-k`) proposed, and every question the analysis assigned to a purpose-built tool has one, compared by name
- every tool name passes `MX-n-1`'s validator at registration
- every tool carries its classification and its catalog-entry reference, and registers through `MX-c-4`'s composed path
- this cell's own pinned tool list moves with each tool it adds, and the derived global count (`MX-c-4`) passes
- every tool's scope is declared through `MX-g-1`'s model, and a request outside it is refused with `ENTITLEMENT_DENIED`
- every answer carries the C4 envelope, and "no data for that date" is never rendered as zero (a planted empty partition proves it)
- (difference) a phrasing that sums across masters or firms is refused, while the single-scope phrasing passes (for `MX-t-1`, `MX-t-7`: across firms or funds)
- the integration is built dormant: with `ENABLED_INTEGRATIONS` empty it adds zero tools, and with its id set it adds exactly its pinned list (STD s.6, G7)
- `validate_integration_spec` returns `[]` for the spec (STD s.8.1, the machine subset of G1-G5), printed
- the integration's tests pass against fixtures built from the analysis's measured shapes, and no fixture carries a client name, a full account number or a balance
- no file outside the cell's `writes` changes (`git diff --stat` against the cell's base, printed)

**Cell-specific additions**
- `MX-t-1`: (difference) for each of the four surface families, the tool's figure and as-of date for one fixture equal the served object's figure and as-of date read by the portal's own code path, while a fixture with the served object's date shifted by one day reports the mismatch -- parity is compared, never assumed
- `MX-t-1`: advisor-intelligence tools read only through the grant `MX-i-2` scoped, and none reads a firm bucket through a silver role
- `MX-t-2`: `dim_transaction` is queryable through its catalog entry and the typed query (`MX-q-1`), and no file under `INT/schwab/` changes
- `MX-t-2`: one master and one date per answer, never summed across masters (C4; NFRA_OPLGTW's ruling)
- `MX-t-2`: tool names do not collide with the five existing `schwab_*` tools, compared by name
- `MX-t-4`: the cell's elapsed wall time, from its first commit to its last, is printed
- `MX-t-4`: the cell's hand-written diff is exactly the catalog entry file(s) plus the integration directory plus its test; every other changed file is generator output reproducible by re-running a named generator, each named (`CAT` by the emitter; the role by `MX-i-1`'s generator)
- `MX-t-4`: the cell writes no description twice: the tool's MCP description is generated from the catalog entry, and a diff of the two shows one source
- `MX-t-7`: every tool answers per fund, and a fund with no data for a date says so

### S7 / C7 -- read roles and grants

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-i-1` | a generator: catalog entry -> one fenced reader role per silver property, plus the Gateway's AssumeRole statement | C7, V.3, FWD-10 | `infra/logic/generators/gateway_reader_roles.py` (new), `TFGW/generated_reader_roles.tf` (generator output only), `TST/test_reader_role_generator.py` (new) | OPEN |
| `MX-i-2` | the advisor-intelligence firm-bucket grant, NAMED AND SCOPED in its own cell before any advisor-intelligence tool | C5, C7 | `TFGW/generated_reader_roles.tf` (generator output, the firm-bucket class only), `infra/logic/generators/gateway_reader_roles.py` (the firm-bucket class only), `TST/test_reader_role_generator.py` (the firm-bucket cases only) | OPEN |
| `MX-i-3` | ONE `safe-apply` in the `opal-gateway` root of every generated role | C7, FWD-3..FWD-5 | `TFGW/` (apply only; no source edit) | HELD (G-S) |

**`MX-i-1` acceptance**
- every generated role name is `name()` output and every fenced prefix is `address()` output, the calls printed; the generator types no name and no prefix
- one role per silver property whose catalog entry exists, and no role for a property without one
- each role's S3 policy is exactly `GetObject` and `ListBucket` on its property's exact prefixes, and nothing wider (no bucket-wide resource, no wildcard beyond the partition segment)
- (difference) the generated plan for one property's role, evaluated with `aws iam simulate-custom-policy` offline against a key under another property's prefix, returns implicitDeny, while a key under its own prefix returns allowed
- the Gateway's AssumeRole statement is generated per role with its external id, following `TFGW/schwab_reader_iam.tf`'s shape, and the Schwab role is not regenerated or changed
- where `MX-a-2` found the Schwab fence does not admit `dim_transaction`'s prefix, the generator emits that one prefix addition and nothing else for Schwab, stated as a change to NFRA_OPLGTW's role
- `terraform validate` and a `plan` in the root, run through the estate's plan path, show only the generated resources, count printed
- no firm bucket appears in any silver role (the cross-firm guard's buckets, `.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_BUCKETS`, printed and compared)

**`MX-i-2` acceptance**
- the grant's role name is `name()` output and its prefixes are `address()` output at firm scope, calls printed
- the grant covers exactly the advisor-intelligence prefixes `MX-a-1` listed in the Inflection and Cottonwood firm buckets, and nothing else in those buckets
- the grant is a separate role from every silver role, and no silver role gains a firm-bucket resource (C7)
- (difference) the policy, simulated offline against an advisor-intelligence key, returns allowed, and against any other key in the same firm bucket returns implicitDeny
- the cross-firm Deny belts that bind the firm buckets are printed, and the grant is shown not to require a Deny exemption
- `J` the grant is the narrowest that serves C5's parity read, and it cannot be used to read another firm's advisor intelligence by any phrasing a tool accepts

**`MX-i-3` acceptance**
- the change-management entry is opened and the OPEN sentinel committed before the apply, and both are closed before the grading reads
- the apply runs through `safe-apply` in `TFGW`, never bare `terraform apply` and never `-target`
- the plan before the apply shows only the generated roles, their policies and the AssumeRole statements, and zero changes to every other resource, the count printed
- every applied role is read back live with `aws iam get-role` and `get-role-policy`, and each equals its generated policy
- (difference) the Gateway, assuming one applied role, reads one object under that property's prefix and is refused one object under another property's prefix, both calls live and printed
- `opal-gateway-role`'s pre-existing 14 statements are read back after the apply and are unchanged, compared with `MX-p-1`'s read

### S9 -- entity resolution

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-e-1` | the identity-plane data binding for the existing resolver, and one resolver tool | S9, V.6, FWD-7, A7 | `APP/entity_resolution/` (the binding and `resolve()` only; `disposition_contract.py` and `resolver_skeleton.py`'s confidence model are consumed, not changed), `INT/opal_entity/` (new), `TST/test_opal_entity.py` (new), `EMIT/catalog_entries/entity_*`, `CAT` | OPEN |

**`MX-e-1` acceptance**
- the SCAFFOLD's remaining gate is re-read at the cell's HEAD and printed (`SCAFFOLD.md:1-11`), and the enum gate's discharge @2ff219b592 is confirmed by `git cat-file -e`
- the identity-plane surfaces the binding reads (the a06 crosswalk, bridge and household nesting the SCAFFOLD names) are located at the cell's run time, each with its path, row count and date, or named absent
- the matching rule is stated in the cell's record, and `resolve()` implements exactly that rule
- the disposition contract (`data/_contracts/smartx_bd_join_disposition.yaml` v1.0) is consumed by path and vintage, and its classes are the resolver's classes (D6-4)
- precision and recall are printed on a named sample drawn by a stated rule, with the sample's size and the labelled truth's source
- every unmatched record is reported with its class, never dropped, and the report's count plus the matched count equals the input count
- (difference) two distinct people who share a name or an address are returned as two, never merged, while one person appearing in two systems is returned as one, in one test
- the 16-row `KEY_OUTSIDE_ACCOUNT_GRAMMAR` class returns CANNOT-ANSWER, never a guess
- no client name, full account number or balance enters the repository; the sample is recorded by masked reference only
- the tool is named, classified, catalog-referenced and scoped under `MX-n-1`, `MX-c-4` and `MX-g-1`

### S10 -- on-demand paths

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-h-1` | measure and choose the long-history substrate | S10, V.7, FWD-8 | deliverables only | OPEN |
| `MX-h-2` | build the chosen substrate and answer one long-history question through the index | S10, FWD-8, A8 | `INT/opal_history/` (new), `TST/test_opal_history.py` (new), `EMIT/catalog_entries/history_*`, `CAT`; plus the substrate's own home the choice names (`infra/aws/terraform/<root>/` via `name()`/`address()`, stated at `MX-h-1`) | OPEN |
| `MX-h-3` | the vendor reads in the SAME index: catalog entries for the six existing YCharts tools; Bloomberg named as the SITEZ read | S10, FWD-8, VII.4 | `EMIT/catalog_entries/ycharts_*` (new), `CAT`, `TST/test_ycharts_in_index.py` (new) | OPEN |

**`MX-h-1` acceptance**
- the Gateway's in-process envelope is measured on the host (memory limit and wall-time cap of the capped child process), with the source of each number
- for the largest silver table in each property the analyses covered, total bytes over its full history are listed live
- at least three candidate substrates are compared -- Athena with a Glue table over silver, a precomputed gold answer table, a Lambda scan -- each with its standing cost, per-query cost, new infrastructure and any schedule it would create
- the choice is stated with the one span it must hold, and that span is shown to exceed the in-process envelope
- no candidate adds a monitor, an alarm, a duplicate output path or a standing comparator (the moratoria, CLAUDE.md), each checked by name
- `J` the choice is the cheapest that answers FWD-8's bounded long-history question, and its standing cost is stated where a reader will see it

**`MX-h-2` acceptance**
- every new resource name is `name()` output and every new S3 address is `address()` output, calls printed
- the change-management entry and OPEN sentinel precede any apply, and both close before the grading reads
- one long-history question is answered through a tool in the index, over a span the in-process engine cannot hold, with the answer stating its substrate, its span, its cost and its elapsed time
- the answer is bounded: a cap on scanned bytes and on rows applies, and a query that would exceed either returns cut short with the cap named
- (difference) the same question over a span the in-process engine CAN hold is routed to the in-process engine, while the long span routes to the substrate, in one test
- the tool is named, classified, catalog-referenced and scoped under `MX-n-1`, `MX-c-4` and `MX-g-1`

**`MX-h-3` acceptance**
- each of the six YCharts tools (`ycharts_freshness`, `ycharts_snapshot_metrics`, `ycharts_time_series`, `ycharts_fund_series`, `ycharts_risk_return_scatter`, `ycharts_search`) has a catalog entry, and `MX-d-1`'s discover names them for a market-data question
- no YCharts call is made by the cell: the tests stub the client, and the command log contains no request to a YCharts host
- the index names Bloomberg's on-demand read as the SITEZ standing read and exposes no Bloomberg tool on this fabric
- no new vendor host is added to any integration's `hosts`, compared before and after

### Validation (independent of every author it grades)

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-v-1` | the cold question set and the common-question set, with expected routes, authored from the analyses alone | FWD-1, FWD-6, A1, A6 | `org/missions/D9/NFRA/NFRA_MCPINDEX/validation/QUESTION_SETS.md` (new) | OPEN |
| `MX-v-2` | the producer journey: every tool of this project exercised in-process against the built Gateway | C2..C7, A6, A11, A12 | `TST/acceptance/test_mcpindex_journey.py` (new), `TST/acceptance/mcpindex_fixtures/` (new) | OPEN |
| `MX-v-3` | the live routing exercise: the cold set and the common set asked in a live session by a non-author | FWD-1, FWD-6, A1, A6 | deliverables only | HELD (G-B) |
| `MX-v-4` | the live answer exercises: FWD-2..FWD-5, FWD-7, FWD-8, each with a second instrument | FWD-2..FWD-5, FWD-7, FWD-8; A2..A5, A7, A8 | deliverables only | HELD (G-B, G-Q) |
| `MX-v-5` | the live roster exercise: one admission and one removal, two sessions | FWD-9, A9 | deliverables only | HELD (G-B) |

**`MX-v-1` acceptance**
- the author authored no tool, no analysis and no catalog entry of this project
- the cold set is written from the seven analysis records only, with each question's expected property, dataset and tool written before the index is consulted, and the file committed before `MX-v-3` runs (commit order printed)
- the common set is every question the analyses assigned to a purpose-built tool, each with its expected tool
- every question in both sets is in plain English a staff member would use, with no tool name, dataset name or catalog term in it
- the cold set includes at least one question per property and at least one about an uncatalogued subject, whose expected route is "not catalogued, no tool"
- `J` the cold set would expose a mis-indexed property: no question is phrased to match a tool's description

**`MX-v-2` acceptance**
- the author authored none of `MX-c-4`, `MX-n-1`, `MX-g-1`, `MX-g-2`, `MX-d-1`, `MX-q-1`, `MX-t-*`, `MX-e-1`, `MX-h-2`, `MX-h-3`
- every tool this project registers is enumerated from the running registry, denominator printed, and each is called at least once
- the count of registered tools without a catalog entry or without a classification is zero, denominator printed (A11)
- every registered tool is looked up BY NAME through both `destructive_ops` and `data_entitlement`, each lookup exercised in the harness and its result printed, and every tool's catalog-entry reference resolves in `CAT` (C2's bar, CTO 98944)
- every registered tool name passes the C3 rule, and a planted non-conforming name is refused in the same run (A12)
- (difference) for every tool, a call outside the caller's grant is refused and a call inside it passes, in one harness (C7)
- every answer carries the C4 envelope, and a planted empty date renders as no data, never zero, for every data tool
- (difference) the typed query's sum-across-masters refusal fires on the path the tools call, and a mutant that bypasses it makes the arm FAIL (C6)
- (difference) with `ENABLED_INTEGRATIONS` empty, the harness registers zero tools of this project; with every id set, it registers exactly the union of the pinned lists
- the Gateway suite at the cell's HEAD records collected, passed and failed counts, with no failure that `MX-p-1`'s baseline did not already carry

**`MX-v-3` acceptance**
- the session is a live Claude session against the deployed Gateway by a person admitted under `MX-g-2`, who built no part of the index
- the cold set from `MX-v-1` is asked verbatim, and the count routed correctly over the count asked is printed, with every wrong route listed (A1)
- the common set is asked without naming any tool, and the count reaching its purpose-built tool over the count asked is printed (FWD-6 routing half)
- the uncatalogued question is answered "not catalogued" and names nothing
- the session transcript is stored in the cell's deliverable with no client name, full account number or balance in it
- `J` the routing result meets FWD-1's bar ("on the first try") for the questions a staff member would actually ask

**`MX-v-4` acceptance**
- FWD-2: per surface family (4), one live side-by-side read naming the portal page, the tool call and both values; figure and as-of date identical; zero disagreements; denominators printed
- FWD-3: per question class (positions, balances, transactions), one live transcript, one master and one date per answer, with the row count reproduced from the same silver objects by a second instrument (a direct DuckDB read of the object under the reader role)
- FWD-4: per property (4), the analysis record, the tool list it produced and one live answer per tool class with its denominators
- FWD-5: per fund (2) and per question class (holdings, net assets, NAV), one live answer compared with the served artifact
- FWD-7: one real client answered across two systems, with the match rule, the sample's precision and recall, and the unmatched list, recorded by masked reference
- FWD-8: one long-history answer and one market-data answer, each naming its substrate and its cost; the market-data answer is made through the YCharts path only under Andrew's per-use word for that call (G-Y)
- every live answer states its date, scope and completeness, and a disagreement between a tool and its second instrument is a finding, never averaged away
- `J` each second instrument is independent of the tool it checks (a different read path, not the tool re-run)

**`MX-v-5` acceptance**
- two live sessions, one admitted and one not admitted, each with the tool list it sees printed by name
- the not-admitted session lists no data tool of this project
- one refusal transcript in the admitted session: a phrasing asking for another master's or firm's data, refused
- one removal, with its roster change and UTC timestamp, and the removed person's next call showing no data tools, with no redeploy between (deploy log for the window printed)

### Release

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `MX-r-1` | release the built code to the Gateway DORMANT: no new integration enabled; the live tool surface unchanged for every principal | release; FWD-* substrate | `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/<slug>.json`; the deploy through `infra/aws/ec2/safe-ec2-deploy.sh` | OPEN (refusal-shaped first criterion) |
| `MX-r-2` | enable this project's integrations: `ENABLED_INTEGRATIONS` and IAM, arch-gated | release; FWD-1..FWD-10 | the host `.env` through the deploy path; `org/critical_paths/` | HELD (G-A) |

**`MX-r-1` acceptance**
- **first, before any deploy act:** the current release's rollback target is restorable under `SCHWAB_PILOT_RUNBOOK.md` s.7.2 step 1's own precondition, read at the bytes and evaluated against the artifact `MX-p-1` identified; if it is not, the cell REFUSES and deploys nothing (1.0.0_SA_CTO 98899: OG-r-1 AC10 found the prior rollback target NOT restorable, and 98928 reports the live release has no valid rollback)
- no NFRA_OPLGTW or MDPF_TAXSMA Gateway release is in flight, read from every live worktree's `org/critical_paths/.open_deploys/` (`git worktree list --porcelain`, then `ls-tree` per tree, per-tree denominator printed; `ls -a`, never `ls -1`)
- the change-management entry is opened and the OPEN sentinel committed before the deploy, and both are closed before the grading reads
- the deploy runs through `infra/aws/ec2/safe-ec2-deploy.sh` only
- the deployed package's member list carries every new integration directory, each file's SHA-256 equal to the source at the cell's HEAD, compared with LF-normalised bytes and the normalisation stated (OG-r-1 AC4's CRLF class)
- (difference) the registered tool list for a non-admitted principal and for an admitted principal equals `MX-p-1`'s list by name after the deploy, and the host's `ENABLED_INTEGRATIONS` is unchanged -- DELTA=0 on the served tool surface
- the deployed catalog's SHA-256 equals the repository `CAT` at the cell's HEAD, and equals a version `MX-c-3` archived (so the served catalog is always one that exists as an immutable version)
- the Gateway service is active after the deploy, read through SSM, and the rollback to the prior artifact is stated as a command, not exercised

**`MX-r-2` acceptance**
- the CTO's G1-G8 arch-gate (STD s.8.1) is signed for each integration this cell enables, cited by commit, before the enable
- each enabled integration's id is added to `ENABLED_INTEGRATIONS` through the deploy path, never a runtime flip on the host
- (difference) after the enable, a non-admitted principal lists zero tools of this project, while an admitted principal lists exactly their granted set
- a below-`min_tier` caller is denied with `min_tier_denied` and zero egress, on the deployed Gateway (STD G5)
- the audit lake carries one deny and one ok record for each enabled integration, tier-stamped (STD G6)
- the change-management entry and sentinel open before and close after, as in `MX-r-1`

### Coverage, run not asserted

**Outcomes, 10 of 10** (the PRD header's `endpoint_outcomes`). Each lists the cells that build it and, last, where it is proved live:

| FWD | built by | proved in |
|---|---|---|
| FWD-1 | `MX-c-1`, `MX-c-2`, `MX-c-3`, `MX-d-1`, `MX-a-*` | `MX-v-1`, `MX-v-3` |
| FWD-2 | `MX-a-1`, `MX-i-2`, `MX-t-1` | `MX-v-2` (offline parity), `MX-v-4` |
| FWD-3 | `MX-a-2`, `MX-q-1`, `MX-g-1`, `MX-t-2`, `MX-i-1`, `MX-i-3` | `MX-v-4` (held on G-Q) |
| FWD-4 | `MX-a-3`..`MX-a-6`, `MX-t-3`..`MX-t-6`, `MX-i-1`, `MX-i-3` | `MX-v-4` |
| FWD-5 | `MX-a-7`, `MX-t-7`, `MX-i-1`, `MX-i-3` | `MX-v-4` |
| FWD-6 | `MX-q-1`, `MX-d-1`, `MX-a-*` | `MX-v-2` (typed half), `MX-v-3` (routing half) |
| FWD-7 | `MX-e-1`, `MX-t-2`, `MX-t-3` | `MX-v-4` |
| FWD-8 | `MX-h-1`, `MX-h-2`, `MX-h-3` | `MX-v-4` (market half under G-Y) |
| FWD-9 | `MX-g-1`, `MX-g-2` | `MX-v-5` |
| FWD-10 | `MX-c-1`..`MX-c-4`, `MX-i-1`, `MX-t-4` | `MX-t-4` (timed diff), `MX-c-4` (planted refusal) |

**Surfaces, 11 of 11:** S1 `MX-c-1` `MX-c-2` `MX-c-3` ; S2 `MX-d-1` ; S3 `MX-t-1` ; S4 `MX-t-2`..`MX-t-6` ; S5 `MX-t-7` ;
S6 `MX-q-1` ; S7 `MX-i-1` `MX-i-2` `MX-i-3` `MX-g-1` ; S8 `MX-a-1`..`MX-a-7` ; S9 `MX-e-1` ; S10 `MX-h-1` `MX-h-2` `MX-h-3` ;
S11 `MX-g-2`. Cells serving no single surface: `MX-p-1` (baseline), `MX-c-4` and `MX-n-1` (contracts C2, C3), `MX-v-*`
(validation), `MX-r-*` (release).

**Contracts, 8 of 8:** C1 `MX-c-1` `MX-c-2` `MX-c-3` ; C2 `MX-c-4` (every tool cell obeys it) ; C3 `MX-n-1` ; C4 every tool
cell, proved in `MX-v-2` ; C5 `MX-a-1` `MX-i-2` `MX-t-1` ; C6 `MX-q-1` ; C7 `MX-g-1` `MX-i-1` `MX-i-2` `MX-i-3` ; C8 `MX-g-2`.

**Acceptance lines, 12 of 12:** A1 `MX-v-3` ; A2 `MX-v-4` ; A3 `MX-v-4` ; A4 `MX-v-4` ; A5 `MX-v-4` ; A6 `MX-v-2` `MX-v-3` ;
A7 `MX-v-4` ; A8 `MX-v-4` ; A9 `MX-v-5` ; A10 `MX-t-4` `MX-c-4` ; A11 `MX-v-2` (built by `MX-c-4`) ; A12 `MX-v-2` (built by
`MX-n-1`).

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D9 is placed LAPTOP (Andrew-direct 2026-09-10 ~18:5xZ, "D9 as a whole is Laptop now"),
and the project row's `fabric_ruling` carries it. AWS acts reach account 313476888478 (us-east-1) from this laptop; on-host
Gateway reads run through SSM. **No cell is owned by a seat**; every cell is served by a worker at L7
(`0.9.0_WK_NFRA_MCPINDEX~<n>`). **No cell routes across fabrics:** Bloomberg on-demand is the SITEZ read and is
named, never reached (VII.4).

**Person-operated and sovereign acts are not cells.** Admission of a beta person (G-B), the CTO's arch-gate (G-A),
Andrew's per-use word for a live YCharts call (G-Y) and the enabling of NFRA_OPLGTW's Schwab tools (G-Q) are gates
(s.6). `MX-v-3`, `MX-v-4` and `MX-v-5` carry out the live exercises once those gates stand. **Unmeasured at the cut:**
whether a sanctioned non-human test principal exists in the Gateway's identity model that a worker could hold for a
live session. Until one is shown to exist, the live session is the admitted person's act and the worker prepares,
records and grades it. s.11 finding 10.

---

## 5. DEPENDENCY EDGES, CHAINS, AND THE FAN-OUT THIS SUPPORTS

Edges are keyed to **observed completion**: `A -> B` means B's acceptance cannot be evaluated until A's artifact is at
HEAD (or, for an apply or deploy, live and read back).

```
  catalog, registration, naming, grant model
    MX-c-1 -> MX-c-2     MX-c-2 -> MX-c-3     MX-c-2 -> MX-c-4     MX-c-2 -> MX-d-1     MX-c-2 -> MX-q-1
    MX-c-2 -> MX-i-1     MX-c-2 -> MX-h-2     MX-c-2 -> MX-h-3     MX-c-4 -> MX-n-1     MX-c-4 -> MX-g-1
    MX-g-1 -> MX-g-2     MX-g-1 -> MX-q-1     MX-n-1 -> MX-d-1     MX-n-1 -> MX-q-1     MX-n-1 -> MX-h-3
  roles
    MX-i-1 -> MX-i-2     MX-i-1 -> MX-i-3     MX-i-1 -> MX-t-4     MX-a-1 -> MX-i-2     MX-i-2 -> MX-t-1
    MX-i-2 -> MX-i-3     MX-p-1 -> MX-i-3     MX-t-2 .. MX-t-7 -> MX-i-3   (6 edges)
  analyses -> tools; every tool on naming, grant model; silver tools on the typed query
    MX-a-k -> MX-t-k  (k = 1..7)     MX-n-1 -> MX-t-k  (k = 1..7)     MX-g-1 -> MX-t-k  (k = 1..7)
    MX-q-1 -> MX-t-k  (k = 2..7)
  FWD-10: the fourth property follows the first three
    MX-t-1 -> MX-t-4     MX-t-2 -> MX-t-4     MX-t-3 -> MX-t-4
  entity resolution; on-demand
    MX-t-2 -> MX-e-1     MX-t-3 -> MX-e-1     MX-h-1 -> MX-h-2     MX-q-1 -> MX-h-2     MX-d-1 -> MX-h-3
  validation
    MX-a-k -> MX-v-1  (k = 1..7)
    MX-t-1 .. MX-t-7, MX-d-1, MX-q-1, MX-e-1, MX-h-2, MX-h-3, MX-g-2 -> MX-v-2   (13 edges)
  release and live exercise
    MX-v-2 -> MX-r-1     MX-i-3 -> MX-r-1     MX-c-3 -> MX-r-1     MX-p-1 -> MX-r-1
    MX-r-1 -> MX-r-2     MX-g-2 -> MX-r-2     MX-r-2 -> MX-v-3     MX-r-2 -> MX-v-4     MX-r-2 -> MX-v-5
    MX-v-1 -> MX-v-3
```

**The chain read, computed from the 93 edges by a script (not chosen), at the cut:**

```
  cells 38, edges 93, acyclic: yes (Kahn order covers 38 of 38)
  heads (no incoming edge) = 10 :  MX-p-1 MX-c-1 MX-a-1 MX-a-2 MX-a-3 MX-a-4 MX-a-5 MX-a-6 MX-a-7 MX-h-1
  leaves (no outgoing edge) = 3 :  MX-v-3 MX-v-4 MX-v-5
  edge-connected components = 1
  M, maximal head-to-leaf paths = 448
  longest dependency path = 11 cells :
    MX-c-1 -> MX-c-2 -> MX-c-4 -> MX-g-1 -> MX-q-1 -> MX-t-2 -> MX-e-1 -> MX-v-2 -> MX-r-1 -> MX-r-2 -> MX-v-3
  width by earliest level:  L0 10 | L1 2 | L2 3 | L3 3 | L4 4 | L5 7 | L6 2 | L7 2 | L8 1 | L9 1 | L10 3
```

**THE BINDING FACTS.** (a) The project is **wide at the head and narrow in the middle.** Ten heads can start at once:
the baseline, the catalog writer, the seven analyses and the substrate choice, **all of them read-only**. Then a
four-cell spine (`MX-c-1 -> MX-c-2 -> MX-c-4 -> MX-g-1`) must finish before any tool cell can be evaluated, because every
tool registers through the composed path those cells build. (b) After the spine, **seven tool cells widen again** (L5 =
7), each in its own directory. That width is the payoff of s.3's architectural fact, and it is what FWD-10 grades.
(c) Everything converges on one integration harness (`MX-v-2`) and one release (`MX-r-1`). (d) Every wait outside a
worker sits at the tail: G-S on `MX-i-3`, G-A on `MX-r-2`, G-B on the three live exercises, G-Q on FWD-3's.

### The distinct-worker constraint

| cell | must not share a worker with | why |
|---|---|---|
| `MX-v-1` | every author of `MX-a-*`, `MX-t-*`, `MX-d-1`, `MX-c-2` | the cold set is written before and apart from the index it tests (FWD-1: "asked cold by someone who did not build the index") |
| `MX-v-2` | every author of `MX-c-4`, `MX-n-1`, `MX-g-1`, `MX-g-2`, `MX-d-1`, `MX-q-1`, `MX-t-*`, `MX-e-1`, `MX-h-2`, `MX-h-3` | the run that grades the integrated build is not its author's |

The constraint binds on context, never on the slot number: a cold start is a fresh context.

### A slotting that satisfies every constraint above (L6's to choose and defend)

| slot | queue, in dependency order | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` catalog spine | `MX-c-1` -> `MX-c-2` -> `MX-c-4` -> `MX-g-1` -> `MX-g-2` | none; this is the critical path's head |
| `~2` naming, discover, query | `MX-n-1` -> `MX-d-1` -> `MX-q-1` -> `MX-h-3` | `MX-n-1` after `MX-c-4`; `MX-q-1` after `MX-g-1` |
| `~3` analyses, portal side | `MX-a-1` -> `MX-a-2` -> `MX-a-7` -> `MX-i-1` -> `MX-i-2` | `MX-i-1` after `MX-c-2` |
| `~4` analyses, platform side | `MX-a-3` -> `MX-a-4` -> `MX-a-5` -> `MX-a-6` -> `MX-h-1` | none |
| `~5` baseline, independent validation, release | `MX-p-1` -> `MX-v-1` -> `MX-v-2` -> `MX-r-1` -> `MX-r-2` -> `MX-v-3` -> `MX-v-4` -> `MX-v-5` | `MX-v-1` after all `MX-a-*`; `MX-v-2` after every cell it grades; `MX-r-1` after `MX-i-3` and `MX-c-3`. This slot authors nothing `MX-v-1` or `MX-v-2` grades |
| `~6` tools A | `MX-t-1` -> `MX-t-2` -> `MX-e-1` | after `MX-n-1`, `MX-g-1`, `MX-q-1`, `MX-i-2` |
| `~7` tools B | `MX-t-3` -> `MX-t-5` -> `MX-t-6` -> `MX-t-7` | same |
| `~8` catalog home, FWD-10, history, roles | `MX-c-3` -> `MX-t-4` -> `MX-h-2` -> `MX-i-3` | `MX-c-3` after `MX-c-2`; `MX-t-4` after `MX-t-1..3`; `MX-i-3` after every `MX-t-2..7` and G-S |

**The fan-out this supports: up to 8 workers over M = 448 maximal paths, cap 8.** **The first wave is lighter, on
Andrew's ~02:4xZ direct to stay light:** the ten heads are read-only and cheap, and the COO states the wave it spawns
at L6 as data (`fanout: N of M chains, cap K, reason: ...`) against the box's measured memory at that moment. The
cut does not fix N. Each hand-off is a fresh worktree from HEAD at hand-off time. Disk at the cut: 20 GB free on C:.

---

## 6. GATES AND NOTICES -- the promises this project creates

None is an approval gate this seat invented. Each is standing law, the PRD's own runtime input, or a shared-resource
sequencing fact, and its carrier is named.

| id | what must exist | carrier of the rule | owner | cells it holds |
|---|---|---|---|---|
| **G-S** | no NFRA_OPLGTW or MDPF_TAXSMA apply in flight in the `opal-gateway` Terraform root, and that root's owner-less plan drift dispositioned, so the plan shows only this project's generated roles | one Terraform state, one writer at a time; the Schwab reader role (`TFGW/schwab_reader_iam.tf`) and MDPF_TAXSMA `TX-i-3` share this root | the COO lanes holding NFRA_OPLGTW and MDPF_TAXSMA (`2.0.0_SA_COO~T` for TX-i-3; NFRA_OPLGTW's lane is closing on Andrew's word, 98917) and `1.0.0_SA_CTO` for the owner-less drift rows | `MX-i-3` |
| **G-A** | the CTO's G1-G8 arch-gate signed per integration before its enable-deploy | `NFRA_INTEGRATIONS_STANDARD.md` s.5 step 5 and s.8.1 (standing law) | `1.0.0_SA_CTO`; `3.0.0_SA_CVO` live-certs G5-G7 after | `MX-r-2` |
| **G-B** | the first beta person admitted by Andrew under `MX-g-2`'s command | C8; PRD authority ("Opal Staff only, but we'll be beta testing it one at a time") | Andrew | `MX-v-3`, `MX-v-4`, `MX-v-5` |
| **G-Q** | NFRA_OPLGTW's five Schwab tools enabled in deployment | PRD V.5 and the project row's `blocking`: "that project's act, never a gate on this one's halves". 98928: NFRA_OPLGTW refused the enable (G-C absent; R-OG-22 open; no valid rollback) and it now needs **Andrew's word**, carded by `1.0.0_SA_CTO` | Andrew, on `1.0.0_SA_CTO`'s card | `MX-v-4` (FWD-3's arm only; the other arms need G-B alone) |
| **G-Y** | Andrew's per-use word for the one live YCharts call in FWD-8's market-data answer | Agent Autonomy: "NEVER call an external vendor API without Andrew's explicit per-use word" | Andrew | `MX-v-4` (the FWD-8 market arm only) |
| **N-1** | a notice, **not a gate**: before `MX-c-4` or `MX-g-1` spawns, this seat sends the COO lanes holding NFRA_OPLGTW and MDPF_TAXSMA the shared Gateway files those two cells write (`APP/data_entitlement.py`, `APP/destructive_ops.py`, `INT/base.py`, `INT/registry.py`, `TST/test_entitlement_admin.py`) | NFRA_OPLGTW authored `data_entitlement.py` and the Schwab integration; MDPF_TAXSMA `TX-g-1` touched `APP/server.py` and `APP/config.py` between this cut's measurement and its head | `2.0.0_SA_COO~M` | none (it precedes a spawn) |
| **N-2** | a notice, **not a gate**: before `MX-r-1` spawns, the same lanes are told a Gateway release is coming, and their in-flight state is read (MX-r-1's second criterion measures it) | one Gateway host, one release in flight | `2.0.0_SA_COO~M` | none |

**What is deliberately NOT a gate.** The LGIC_NAMING schema bump that would GRADE tool names (C3) is `1.0.0_SA_CTO`'s to
raise there; nothing here waits on it, and `MX-n-1` enforces the rule by criterion meanwhile. The D3 residual enum is
**not** a gate: it was discharged @2ff219b592 (s.1 falsifier 4).

---

## 7. THE BATTERY -- run at L5, each lens with its blindness stated

| lens | disposition | result | what it does NOT cover |
|---|---|---|---|
| `comp-adversary` | RUN | `compose` on the PRD (read-vintage HEAD @2aa1e26cbf, 02:42:45Z; artifact-vintage b7dc80e2cc): **7 of 7** cited commits VERIFIED; cited paths **7 attempted / 7 stable / 0 flagged**; 1,754 uncited siblings, 12 digested by its declared S1-S4 salience rule (S1 POSTDATES 12 of 101), 1,742 not digested (budget, declared); 0 of 12 digests deferred; 5 complement sources run, 4 declared-excluded (toolgraph, comp-axes, comp-blast neighborhood, comp-pulse) | `T11: decomposition neighborhood NOT RESOLVED` (the PRD carries no `<decomp_ref>`), so the siblings are filesystem adjacency, not this decomposition's chain. **It checks that a cited path is STABLE, never that it is the right path or that the text at it is still true: it passed the PRD's Gateway-relative catalog path and could not see s.1 falsifiers 2-4.** DISCLOSED DEFECT: a reader thread raised `UnicodeDecodeError: 'charmap' codec can't decode byte 0x90` (cp1252) during the run; rc=0 and all 12 selected digests returned, so no counted digest was lost, but the lost bytes' owner is not identified. A re-run against each task order at L7 resolves T11 |
| `comp-schedule` | RUN, APPLICABLE | self-test **PASS 6/6**. View at `--budget 1800`: within budget (94 s), **5 of 5 carriers**, C1 SENTINEL 138 -> 7 gates, C2 DEPLOY-LEDGER 7 -> 7, C3 MORATORIA 12 -> 12, C4 SCOPE-GUARD 21 (SEMI-DECIDABLE, 0 counted), C5 PROJECT-BLOCKING 334 (NOT-DECIDABLE, 0 counted); **26 gates armed, 0 of them naming NFRA_MCPINDEX, the opal-gateway, `DATA_CATALOG` or `catalog_gate`** (case-insensitive census over the view, 0 hits). Moratoria that bind cells: never-widen (G-16: none moves served output; `MX-r-1` proves DELTA=0 on the tool surface), no half-landed deploy (G-17: `MX-c-3`, `MX-h-2`, `MX-i-3`, `MX-r-*`), no shadow or duplicate output (G-20: `MX-c-3`'s one home; `MX-h-1`), no new monitor (G-21: `MX-h-1`), safe-apply and safe-commit (G-23: every writing cell), cross-firm fence (G-24: `MX-i-1`, `MX-i-2`), vendor egress (G-25: `MX-h-3`, `MX-v-4` under G-Y) | C4 and C5 are prose carriers and are not counted as gates; the gates this project creates are s.6. The seven open deploy-ledger entries (G-8..G-14) belong to other projects and none touches the Gateway |
| `comp-iam` | RUN | DESIRED plane. `opal-gateway-role`: **14 statements** -- audit PutObject; `opal-data-portal-v2` GetObject on `daily-reports/*` and on `json/*` + `platinum/*` (statement 6: the portal parity reads are already granted); ListBucket on `daily-reports/`; 5 SecretsManager reads; DynamoDB access-state reads and conditioned writes; `sts:AssumeRole` for the Schwab external ids (statement 9: the fenced-role pattern C7 extends); AssumeRole on the Tax SMA account's `opal-mcp-emp-*` (statement 12). **No statement on `opal-data-assets` directly and none on a firm bucket**: silver is read only through an assumed fenced role, and advisor intelligence has no grant today (C5's separate grant is `MX-i-2`) | Terraform only, and blind to deny: `attach-census` rc=1, **31 policy blocks NOT ATTACHED** and **6 deny statements unparsed**, among them the `cross-firm-bucket-deny` belts in `inf-pipeline/cross-firm-deny.tf` and `served-guard-inf/_root.tf`. The APPLIED and EXERCISED planes are `MX-p-1`'s live reads and the live arms of `MX-i-3` and `MX-r-2` |

**Beyond the core, measured at this cut:** s.1's six falsifiers (the catalog path census; the emitter's code against its
docstring, four carriers against one; the projection census, 4 declared and 3 exposed; the entity-resolution scaffold's
gate record and both D3 order statuses; the `address()` census, 2 of 6 catalog candidates resolving with a positive
control; eleven citations printed at their lines). Also measured: the 49-name tool union against the pinned 44; the
`systems.json` census (25 keys) and the `scopes.json` census (9 rows); the NAMING_SCHEMA version (v1.12, 0 tool-name
tokens); the Gateway test tree (163 tracked test files); the integration wiring (`INT/registry.py:14` already imports
`data_entitlement.classify`; `_load_builtin_factories` is a hand list over 4 ids).

**NOT run, and why.** `comp-blast`: the changed functions do not exist yet; `MX-c-4` and `MX-g-1` re-run it on
`classify` and the grant model when they change them. `comp-routes`: no API route changes. The Gateway's live state was
not read at the cut: `MX-p-1` reads it. No AWS silver was listed at the cut: each `MX-a-k` lists its own.

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6

1. **No egress off Opal infrastructure.** No worker calls YCharts, Bloomberg, Microsoft Graph or any vendor. The one live
   YCharts call in `MX-v-4` is made only under Andrew's per-use word for that call (G-Y).
2. **No private data in the repository.** No client name, full account number, balance, token, cookie or credential
   enters code, fixtures, catalog entries, deliverables or logs; masked references and aggregate counts only.
3. **Addresses and names from the builders.** Every new S3 key is `address()` output and every new resource name is
   `name()` output (Rule 30). A builder refusal is a registry row, never a typed path.
4. **Deploy discipline.** A world-changing act opens its change-management entry and commits the OPEN sentinel before
   the act, then closes and commits the entry before the reads that grade it. Terraform through `safe-apply` only, never
   `-target`; the Gateway through `infra/aws/ec2/safe-ec2-deploy.sh` only.
5. **One Terraform state, one writer.** The `opal-gateway` root is applied by `MX-i-3` alone in this project, and never
   concurrently with NFRA_OPLGTW or MDPF_TAXSMA (G-S).
6. **No served output moves.** No cell writes a portal served key. `MX-r-1` releases dormant code and proves DELTA=0 on
   the tool surface; enabling is `MX-r-2` under G-A.
7. **No new monitor, alarm, SNS, email, watcher, schedule or standing comparator.** `MX-h-1` names any schedule a
   candidate would create, and choosing one is a finding, not a build.
8. **The Schwab integration is read, never edited.** No file under `infra/aws/ec2/opal-gateway/app/integrations/schwab/`
   changes in any cell. The engine is reached by import. The one Schwab change this project may make is a fence prefix
   for `dim_transaction`, generated by `MX-i-1` and applied by `MX-i-3`.
9. **The spec is frozen, and the face instructs refusal.** A criterion that cannot be satisfied as written is REFUSED and
   reported with its measurement, never repaired, widened or met by another route. Anything off-spec is a row.
10. **The catalog is generated, never hand-edited or hand-merged.** `DATA_CATALOG.yaml` changes only as the emitter's
    output; a merge conflict on it resolves by re-running the emitter at the drain.
11. **Every invocation terminates** (`timeout 120`, or the tool's own budget).
12. **Commits go through `.tools/safe-commit.sh` under the worker's serial; every `.py` edit passes
    `.tools/commit-gate.sh`.**
13. **Unknown deployment facts are measured, never presumed.** A cell asserts no deployed state it did not read back.
14. **No new dependency.** A missing instrument is a refusal, never an install.
15. **Tool names under C3.** No tool is registered under the research record's business-first names or the parked
    `DESIGN.md:44-45` names as they stand.
16. **Opal staff only.** No partner or client principal is admitted, granted or tested with (Andrew's standing
    2026-08-20 ruling).
17. **The Gateway suite baseline is `MX-p-1`'s printed count.** A cell adds no failure; a pre-existing failure is not
    its to fix (a row if its change touches it).

---

## 9. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is s.1's subtraction: 11 manifest surfaces, every one served, with six
falsifiers run against the PRD's own claims before use. Exhaustive: 11 of 11 surfaces, 8 of 8 contracts, 10 of 10
outcomes, 12 of 12 acceptance lines, 15 of 15 open items (s.2, s.3). Mutually exclusive on write surfaces **where
cells can run at once**: every tool cell writes its own integration directory and test file. A script over s.3's
`writes` column finds **7 paths with more than one writer**. Six are hand-written files, each written by exactly two
cells that an edge orders, so the writers never run concurrently: `APP/data_entitlement.py` (`MX-c-4` -> `MX-g-1`),
`INT/base.py` (`MX-c-4` -> `MX-n-1`), `EMIT/emit_catalog_v02.py` (`MX-c-1` -> `MX-c-2`), and the three role-generator
files -- `infra/logic/generators/gateway_reader_roles.py`, `TFGW/generated_reader_roles.tf` and
`TST/test_reader_role_generator.py` -- (`MX-i-1` -> `MX-i-2`). The seventh is `CAT`, generator output written by 11
cells; its merge rule is s.8 bound 10.

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one record: one module with its tests, one generator,
one apply in one root, one measurement, one grading, one live exercise campaign or one release. A person's act (an
admission, an arch-gate signature, a per-use word) is a different grain and is a gate, not a cell.

**(iii) INTENT COHERENCE.** One axis: **deliver v0.5 so every FWD bar has its deliberate proof.** No cell widens scope:
no Tax SMA tool, no partner access, no new vendor egress, no Bloomberg on this fabric, no admin screen (the mcportal
brief's), no new precomputed table, no second catalog, no edit to the Schwab integration, no enable of NFRA_OPLGTW's
tools.

**(iv) STATE COHERENCE, and what each remedy does NOT move:**
- `MX-c-1` changes a docstring and moves **no catalog row and no writer**.
- `MX-c-2` extends the schema and moves **none of the 36 existing rows**.
- `MX-c-3` archives immutable versions and moves **no runtime reader** (the repository file stays the one home; a planted S3 reader fails its test).
- `MX-c-4` changes how classification composes and moves **no existing tool's class** (49 of 49 compared).
- `MX-n-1` refuses non-conforming new names and moves **no existing tool name** (grandfathered by name).
- `MX-g-1` composes grant scope and moves **no Schwab grant** (its tests unchanged).
- `MX-g-2` generalises admission and moves **no admitted person** (Andrew admits).
- `MX-t-*`, `MX-d-1`, `MX-q-1`, `MX-e-1`, `MX-h-2` add dormant tools and move **nothing a live principal sees** until `MX-r-2`.
- `MX-i-*` add exact read roles and move **no existing grant, no firm fence and no Deny belt**.
- `MX-r-1` moves **no tool a principal lists** (DELTA=0); `MX-r-2` moves what admitted principals list, under G-A.
- `MX-v-*` and `MX-a-*` move **no production code**; a failing arm is a row for the round-N analysis.

---

## 10. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, stated so it can be argued with, and revertible at the round-N analysis.

1. **Classification, registration and grant scope compose from each integration's own declaration (`MX-c-4`,
   `MX-g-1`).** FWD-10's PROOF ("the added property's diff (catalog entry + tool, nothing else)") cannot pass while
   adding a property edits four shared registry files. C2's letter is kept: every tool is still resolvable through
   `destructive_ops` and `data_entitlement` by name, and each tool cell still moves its own pinned count. What changes
   is **where the data lives**, not what C2 requires. **RULED ADOPTED by 1.0.0_SA_CTO 98944** ("C2 constrains the tool's
   properties, not the file they are typed into"), with C2's letter as the bar, proven by an exercised lookup by name.
2. **The catalog's per-entry source is one file per dataset (`MX-c-2`),** so "one catalog entry" is one file in a
   diff, and the generated catalog is re-emitted rather than hand-merged.
3. **Read roles are GENERATED from catalog entries (`MX-i-1`) and applied once (`MX-i-3`),** rather than hand-written per
   property, so FWD-10's addition carries a generated role, not a hand-written one, and the `opal-gateway` state has one
   apply in this round, not seven.
4. **The advisor-intelligence grant is its own cell (`MX-i-2`),** exactly as C5 requires ("named and scoped in its own
   cell before any advisor-intelligence tool is cut"), and `MX-t-1` depends on it.
5. **FWD-10's "next property after the first three" is Orion (`MX-t-4`),** after Portal, Schwab and Black Diamond. The
   order is fixed at the cut so the timed addition is a frozen criterion, not a choice made at the drain.
6. **Each property's tools are a NEW integration directory (`INT/<system>_index/`),** never an addition to an existing
   integration. So enabling NFRA_OPLGTW's `schwab` integration never enables this project's Schwab tools, and the
   reverse.
7. **The typed query reuses the Schwab engine by import (`MX-q-1`),** and no file under `INT/schwab/` changes. C6's
   "generalised beyond Schwab" and C7's "extends NFRA_OPLGTW's rather than forking it" are met without touching another
   project's integration.
8. **Entity resolution is OPEN, not held,** because its PRD-named gate is discharged (s.1 falsifier 4). The data binding
   is the cell.
9. **The live exercises are three cells (`MX-v-3` routing, `MX-v-4` answers, `MX-v-5` roster),** each one campaign in one
   live session family, held only on the gates their own arms need, so FWD-3's G-Q holds one arm of one cell and nothing
   else.
10. **The release is split in two:** `MX-r-1` dormant (DELTA=0, no arch-gate needed), `MX-r-2` the arch-gated enable.
    `MX-r-1`'s first criterion is a **refusal** if the current release's rollback target is not restorable. That is the
    lesson of OG-r-1 AC10, carried into this project's first Gateway act.

---

## 11. FINDINGS AND CARRIES, for the CTO's L10 read

1. **C1's central premise is superseded by the code.** The live catalog HAS an identified writer:
   `emit_catalog_v02.py` writes `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (`:42-43` target, `:735` the
   write), and four carriers say so (the code, its comment at `:38-41`, the catalog header `:7-9`, `DESIGN.md:66-67`).
   The one carrier that disclaims it is the module docstring at `:5`, left standing when V03-2 rewrote the comment beside
   `OUT`. **The v0.2 refusal (@acb5fc61cc) and C1's re-cut both rest on that docstring**, which is the exact shape CLAUDE.md
   Rule 27 names: a rewritten passage does not delete its own old words. The finding does NOT say the writer runs on a
   cadence: its last exercise was the 2026-08-20 port, so C1's EXERCISE bar still stands. `MX-c-1` confirms and corrects.
   **No PRD edit is asked for.** C1's obligation is satisfiable as written; this changes how cheap it is. If the CTO reads
   it as a ratified-text defect, that is an L10 addendum.
2. **RULED by 1.0.0_SA_CTO 98944 before L6: the tension dissolves on the right axis.** "A home is defined by what reads
   it at runtime": the repository `CAT` is the ONE home and the source; S3 carries immutable versions and is never read on
   the serving path, and a runtime reader of the S3 copy VIOLATES the ruling. `MX-c-3` was recut to that shape (v2), and
   its judgment criterion became a mechanical one with a planted-reader difference control.
3. **S4's `fact_trn` does not exist; the transaction table is `dim_transaction`** (`schwab_projections.py:55`). The PRD's
   intent is unambiguous and `MX-t-2` names the real table. A PRD wording carry for its next substantive bump.
4. **S9, V.6, A7 and brief-coverage row 10 carry a DISCHARGED gate.** Entity resolution's D3 enum gate was discharged
   @2ff219b592 on 2026-08-19 (`SCAFFOLD.md:1-11`), and both D3 orders read complete. The remaining gate is the
   identity-plane data binding, a laptop act inside S9. So FWD-7 is **buildable this round**, and `MX-e-1` is OPEN. It
   also means the PRD's "CARRIED-AS-OPEN, the substrate does not exist yet" understates what exists: a resolver skeleton
   with an exercised confidence model and a consumed disposition contract.
5. **The PRD's catalog path is Gateway-relative.** `app/refs/DATA_CATALOG.yaml` is absent at the repository root; the
   file is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`. Every cell here uses the repository path. Note that
   `comp-adversary`'s "7 of 7 stable" did not flag it: path stability is not path correctness.
6. **The PRD pins NAMING_SCHEMA v1.10; HEAD is v1.12.** C3's substance holds at v1.12 (0 tool-name tokens; `not_covered`
   silent on tools). A version pin in a constitutional text is a maintenance promise, per CLAUDE.md Rule 27's own history.
7. **The five parked business tools (`DESIGN.md:44-45`) violate C3** -- `find_account` and the rest carry no system token.
   Their design can be reused; their names cannot. Bound 15.
8. **The catalog's versioned home resolves through the builder today** at scope `global` (platinum ->
   `opal-data-portal-v2`, silver -> `opal-data-assets`). No registry row is owed, unlike MDPF_TAXSMA's G-R.
9. **The live Gateway has no valid rollback (98899, 98928), and every Gateway release inherits that.** `MX-r-1` refuses
   to deploy until the current release's rollback target is restorable. That remedy is NOT this project's to perform: the
   AC10 exposure belongs to NFRA_OPLGTW's release, which is closing tonight. **If nobody owns making the current
   release restorable, `MX-r-1` will refuse, correctly, and every live FWD in this project waits behind it.** That is the
   one cross-project dependency here with no owner at the cut. EXPOSURE, not INCIDENT: whether a rollback was ever needed
   and failed is unmeasured. **1.0.0_SA_CTO 98944 routes the repair to Andrew** (rec: the rollback repair is the FIRST act of whatever seat next holds
   NFRA_OPLGTW) and rules that `MX-r-1` refusing until then "is the system working ... not a blockage to route around".
10. **Whether a worker can hold a live-session principal is unmeasured.** FWD-1 and FWD-6's PROOF need "a live session
    by a non-author". If the Gateway's identity model has no sanctioned test principal, the live exercises are an
    admitted person's acts and the worker records and grades them. `MX-v-3` names which it was.
11. **Shared Gateway surfaces with two other projects.** `APP/data_entitlement.py`, `APP/destructive_ops.py`, `INT/base.py`
    and `INT/registry.py` were NFRA_OPLGTW's to change; MDPF_TAXSMA's TX-g-1 wrote `APP/server.py` and `APP/config.py` in the
    interval between this cut's measurement (7755816cf6) and its head (57751941a0). The `opal-gateway` Terraform state is
    shared with both. Handled by N-1, N-2 and G-S, not by merging scopes.
12. **`destructive_ops.py:28` says "The 20 read-only tools" above a set of 27 names.** That is the same drift class as C2's
    pinned counts, in a comment. Not chased; `MX-c-4` touches that file and may correct it inside its own diff.
13. **Two tool defects met during this cut, outside this project, reported rather than chased.** (a) `comp-adversary`'s
    reader thread decodes subprocess output as cp1252 and raised on byte 0x90 (the CLAUDE.md non-ASCII trap); the run
    still returned rc=0 and all counted digests. (b) The startup `audit-archive-invoker` reported
    `[DEATH/INVOKER-SILENT-WITH-CHURN] last run 2026-09-18T174906Z (55.5h ago)`, a class that is not on org/XXX.md A.2's
    known-and-owned list; this seat's run minted the snapshot and advanced the baseline.
14. **Estimate, as a reading.** The machine critical path is 11 cells. At an inferred 1 to 3 worker-hours per cell, that
    is roughly 1.5 to 3 days of serial work, plus G-S, G-A and G-B, whose timing is not this seat's, and finding 9's
    unowned rollback. Basis INFERRED, not measured; no delivery date is committed.

---

## 12. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **No cell has been exercised.** Every target state is a specification.
2. **No AWS state was read at the cut.** Silver sizes, object counts, the live IAM policies, the deployed Gateway
   commit and the host's `ENABLED_INTEGRATIONS` are `MX-p-1`'s and each `MX-a-k`'s to read. The deployed-commit value
   quoted in `MX-p-1` is 1.0.0_SA_CTO's (98928), DECLARED here.
3. **The common questions per property are not enumerated here.** The analyses write them.
4. **The emitter's code writes the live catalog; that it RUNS is not claimed.** `MX-c-1` exercises it.
5. **The five tool-integration directory names (`INT/<system>_index/`) are this cut's choice**, not a measured
   convention. `MX-n-1`'s rule governs tool names, not directory names.
6. **Whether `infra/logic/generators/` is an accepted home for the role generator is NOT-EVALUATED.** The lane gate at
   `MX-i-1`'s first commit answers it; a refusal is a row and the issuer re-grants the path.
7. **Whether the lane gate admits a worker serial to the Gateway's shared core files (`MX-c-4`, `MX-g-1`) is
   NOT-EVALUATED.** A refusal is a row, and the issuer seats the path for that order alone.
8. **The chain count and the constraint table are readings.** M = 448 follows from the 93 edges this document declares;
   a missing edge would show as false width.

---

# ROUND 2 -- THE THREAD (L5, v3)

```json
{
 "project": "NFRA_MCPINDEX",
 "decomp_version": "v3",
 "step": 5,
 "round": 2,
 "fabric": "site-z",
 "input": "org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round1.md@ad67fd0409 (section 4, E1-E6; rulings R-2..R-8)",
 "prd_ref": "org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md@b7dc80e2cc",
 "author": "2.0.0_SA_COO~O",
 "cells": 7,
 "chains": 3,
 "held_branch": "wk-nfra_mcpindex-1-1d",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~O` (re-seated @23bbeff325). **Input:** the CTO's round-1 analysis @ad67fd0409, cut in ONE
issuance. Round 1 (sections 1-12 above) stays frozen as its own record. The gateway stays on its CURRENT path (R-8).

## R2.1 THE CELLS -- 7

| Cell | From | Builds | Base | Risk |
|---|---|---|---|---|
| `MX-c-5` | E3 (R-5, D-3) | the 9 ycharts/opal_portal/globgrph tools declare their class in their own integration dirs; AC11 over 49 is 44 classified + 5 schwab HELD (registered, not enabled); MX-c-4's AC8 (`read_teams_attachment` SAFE) carried as this cell's judgment criterion | the held branch itself | WORLD (infra floor) |
| `MX-d-2` | E1 (S2) | the discover family (`opal_discover`), reading the ONE repository catalog: property, dataset, freshness field and latest value, firm scope, caveats and the next tool; an uncatalogued subject names nothing | the held branch after MX-c-5 | WORLD (infra floor) |
| `MX-t-8` | E2 (S3, FWD-2, R-7) | the portal purpose-built tools (`portal_index`) over the mdpf, etfs and 49financial advi keys MX-a-1 proposed, reading the SAME precomputed objects by exact key prefix; each tool's class and catalog entry ride its own cell (@5f3b4a20c6 (b)); "model composition and weights" answered or named unanswerable | the held branch after MX-c-5 | WORLD (infra floor) |
| `MX-v-6` | E4 | the routing harness (the `.tools/comp-which-routing-test.py` lesson) and a question set drawn from REAL asks (the Analyst's thread memory), never from catalog descriptions | the held branch after MX-d-2 and MX-t-8 | WORLD (infra floor) |
| `MX-q-2` | E5 (R-2 (1), R-3) | two read-only live reads: the Black Diamond null-cusip rate in silver transactions since 2026-04-14 (and any served figure joining on cusip), and Eclipse's distinct firm/rep ids against the Inflection allowlist | CLOUD | WORLD (live read) |
| `MX-b-2` | E6 | the batch cell: C-S15's emitter docstring line, and W1-S3 by the issuer's pick -- `catalog_v02/validation_report.json` becomes gitignored and untracked (a run artifact every run rewrites) | CLOUD | LOCAL |
| `MX-r-3` | E3's release (R-8) | the NARROW gateway release: the deployed commit at this cell's own cut plus ONLY this project's gateway commits (MX-c-4's build and MX-c-5, MX-d-2, MX-t-8 and MX-v-6), shipped DORMANT for the new integrations | CLOUD after the held branch drains | WORLD |

## R2.2 CHAINS, THE HELD BRANCH, AND THE ONE WAIT THE RULINGS IMPOSE

```
chain A (held branch)  MX-c-5 --> {MX-d-2 || MX-t-8} --> MX-v-6 --> [CVO grades AC8] --> drain --> MX-r-3
chain B                MX-q-2
chain C                MX-b-2
```

- The held branch changes a LIVE gateway behaviour (`read_teams_attachment` becomes SAFE), so it drains to CLOUD only
  after `3.0.0_SA_CVO~O` grades MX-c-5's AC8. That is R-5 as written, and the CTO's affirmed hold (@5f3b4a20c6 section 4).
- Every cell stacked on it is cut FROM the held branch. The issuer merges each stacked worker branch INTO the held
  branch, not into CLOUD.
- The AC8 grading is a mid-round L9 act. The issuer's drain-end read names it when MX-v-6 is terminal.

**Fan-out:** `N = 3 of M = 3 chains, cap 8`.
- Spawn now: `~1` MX-c-5, `~4` MX-q-2, `~5` MX-b-2.
- After MX-c-5: `~2` MX-d-2 and `~3` MX-t-8.
- After both: `~2` MX-v-6.
- After the drain: `~1` MX-r-3.

## R2.3 STANDING RULES ON EVERY FACE (R-6)

1. W1-S6: a device-neutral interpreter (`python`), never `py -3.12`.
2. W4-S1: every tool and read fence works by EXACT KEY PREFIX, never by bucket, with a negative control that reads a
   sibling property's prefix and is refused.
3. W1-S1: a criterion that exercises a served file names that file in `<paths>` at the cut.
4. W1-S3: `catalog_v02/validation_report.json` is gitignored by MX-b-2 (the issuer's pick). Until MX-b-2 drains, a
   cell that runs the validator restores that file before committing and says so.

## R2.4 GATES AND THE CLOSE RUN

- **G-A:** Andrew's word to ENABLE the released integrations (the round-1 gate).
- **G-B:** a non-author asker for the live cold run (Andrew admits the person).
- **The close run:**
  - E1 and E2 are exercised live through the gateway, one question per portal surface that has a tool (mdpf, etfs,
    49financial advi);
  - each answer's figure and date equal the portal's;
  - the `json/*` surface is answered by discover only, since its tools wait on FWD-6 and a registry row (MX-a-1 AC7);
  - with G-B, the FWD-1 cold run.
- **Subtracted,** per the analysis section 4: Schwab (G-Q, G-OPLGTW), Black Diamond/Eclipse/Orion/SmartX tools, ETF
  tools (TrueShares on R-4), the typed query, entity resolution, on-demand paths and the roster.

## R2.5 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The null-cusip rate, the Eclipse tenancy, the deployed commit at MX-r-3's cut and the live tool
   surface are measured by their cells.
2. The CRO's question lists named by the analysis were not located by this seat's census. MX-v-6 records what it found
   and uses the Analyst's thread memory in any case.

## R2.6 ADDENDUM -- two DS cells, on Andrew's option 4 (record @bda25438c8; CTO msg 25944)

`0.0.0_AB_MSTR~Z` seated `0.4.0_DS_ClientPlatform~D` at 22:55:02Z for the two DS acts the round-1 analysis PARKED (R-2 (2),
R-4). DS owns silver scripts, their QA deploy and production schedules (CLAUDE.md rule 13). They are added to round 2
as one supplementary issuance with a stated reason. They touch nothing on the held branch.

| Cell | From | Builds | Risk |
|---|---|---|---|
| `MX-s-1` | R-4, row W3-S2 | why TrueShares DIVZ/IDVZ holdings never reach `opal-data-assets` `trueshares/{fund}/silver/fact_holdings/`; the converter fixed; the missed dates since 2026-08-24 backfilled; the completeness guard made to count the holdings feed | WORLD (silver writes) |
| `MX-s-2` | R-2 (2), C-S13 | the Black Diamond asset-to-cusip bridge builder (`build_bd_assets_dim.py`) on a PRODUCTION schedule; the one affected served figure (`gold/timeseries/holdings_lots`, 22,172 null-cusip rows on 2026-09-18) named and corrected under a never-widen sign-off (CTO+COO) | WORLD (a served move) |
| `MX-s-3` | MX-s-1 AC2 (DS msg 25985), rows Z-S4/Z-S5 | the `opal-assets-silver-etf` Lambda re-vendored from CLOUD HEAD and applied through safe-apply (DT/AE, rule 13), so the TrueShares holdings converter runs in production; issued @79deb6ea42 to `0.7.0_AE_CloudOps~I` | WORLD (a Lambda code change) |
| `MX-s-4` | MX-s-2 (DS msg 26021), rows Z-S8/Z-S9 | the Black Diamond asset-dim download logs in again, its wrapper exit code made honest, the compaction restored and the bridge rebuilt once; issued @3920db09bd to `0.7.0_AE_CloudOps~I` | WORLD (producer repair) |
| `MX-s-5` | row Z-S12 (filed under MX-s-3) | `infra/aws/lambda/ci/lambda-source-map.json` goes ASCII (23 mojibake characters), so step 7 of the canonical Lambda deploy runs on site Z; issued @fa1af39c3c to `0.7.0_AE_CloudOps~I` | SERVED (a shared CI data file) |
| `MX-s-6` | row Z-S15 (filed under MX-s-4) | the scheduled Black Diamond asset conversion writes the compacted `silver/bd_assets.parquet` (the converter gated it on `--backfill`; the schedule passes `--latest`), and the cusip bridge is rebuilt from it; steps 3-4 of MX-s-4 moved here as DS-owned silver acts (rule 13); issued to `0.4.0_DS_ClientPlatform~D` | WORLD (silver writes) |
| `MX-s-7` | row Z-S13 (filed under MX-s-5) | `infra/aws/lambda/ci/record-terraform-deploy.sh`'s 3 python `open()` calls read and write UTF-8, so the recorder stops turning one non-ASCII character into three on each pass; issued to `0.7.0_AE_CloudOps~I` | LOCAL (a CI tool repair) |
| `MX-s-8` | rows Z-S3 + Z-S25 (routed by `1.0.0_SA_CTO~O`, msgs 20260927T065208Z / 072615Z) | the two `mirror_conversion.py` source fixes (8ba0d6645b, bbf8cfefa6) go into the 4 vendored `opal-assets-silver-{blackdiamond,etf,eclipse,orion}` copies as two hunks each (no whole re-vendor; that sweep stays parked), deployed in ONE safe-apply under a never-widen sign-off; issued to worker `0.9.0_WK_NFRA_MCPINDEX~7` | SERVED (4 silver Lambdas) |
| `MX-s-9` | row Z-S8 (MX-s-4 step 1.2, moved out by A5 @fc2001d) | the BD asset dimension by REST: a bd-tree bronze module on the existing 49F session (no new crawler, nothing in cot's tree), one ledgered discovery read + one qt4 pull to a bronze object, per 1.0.0_SA_CTO~O's design @1973056c51; issued to `0.4.0_DS_ClientPlatform~D` (reseat asked) | WORLD (a bronze write + vendor reads) |
| `MX-s-10` | row Z-S42 (CTO ruling @bf94418eb8) | the scheduled BD asset-dim run (EventBridge 22:10Z -> `bd-asset-dim-trigger` -> SSM `opal-bd-asset-dim-download`) is PORTED to the MX-s-9 REST pull + the dim rebuild, no shadow; the dead portal asset-dim and fees downloaders retire after a caller census; never-widen halves on PHASE A; the next scheduled fire is the acceptance; issued to `0.7.0_AE_CloudOps~I` | SERVED (the dim's producer changes) |
| `MX-s-11` | row Z-S43 (CTO ruling @e4b19b9898) | the REST pull's names resolve at BUILD time: an opal_naming GENERATED 49F pin replaces the module's `opal_naming` import (the lib/ patch lands by 1.0.0_SA_CTO~O, BASE_EXEC), and the lib-free closure (pull, pin, `silver_ids`, `trading_calendar`) is published to the keys the asset-dim document stages; blocks MX-s-10 step 2; issued to `0.4.0_DS_ClientPlatform~D` | SERVED (code the schedule will run) |
| `MX-s-12` | round-2 analysis section 1 @e4445020f5 (enrichment item 1; named `MX-s-10b` there, renamed to the cell grammar) | MX-s-10 PHASE B re-cut: the ported document @0ff972bc38 is published DEFAULT under both SIGNED never-widen halves (G1-G3), the Playwright scripts and the fees schedule leg retire through Terraform, and the next scheduled 22:10Z weekday fire is the acceptance (s10.AC1-3 plus judgment s10.J1); issued by `2.0.0_SA_COO~MI` to worker `0.9.0_WK_NFRA_MCPINDEX~8` | WORLD (a scheduled vendor pull writes a served object) |
| `MX-s-13` | round-2 analysis item 2, R-10 (row Z-S31) | the live BD password leaves the 7 tracked files of the CTO's redaction set (5 stepwise scripts to `${BD_PASSWORD:?...}`, 2 docs to a placeholder); no history rewrite, no rotation; the CVO's fingerprint scan is the oracle (J1); worker `0.9.0_WK_NFRA_MCPINDEX~9` | WORLD (infra-path floor) |
| `MX-d-3` | round-2 analysis item 3, first step (row Z-W2-S8) | the discover family ranks a dataset ask's dataset first: ROUTING >= 21 of 27, dataset asks >= 2 of 3 on MX-v-6's harness; chain head of MX-r-4; worker `0.9.0_WK_NFRA_MCPINDEX~10` | WORLD (infra-path floor) |
| `MX-r-4` | round-2 analysis item 3; re-cut of `MX-r-2` | the thread live: a NARROW gateway release (deployed commit + this project's commits, MX-d-3 included) that ENABLES `opal_discover` + `portal_index`, then one live question per A2 portal surface (J1); PHASE A announces with no deploy, PHASE B on the issuer's GO after G-A and both never-widen halves; worker `0.9.0_WK_NFRA_MCPINDEX~10` after MX-d-3 | WORLD (the tool surface admitted principals list changes) |
| `MX-m-1` | round-2 analysis item 4 (a)-(d), R-11 | read-only measures: BD SSM exit honesty beyond fees (Z-S47), the 42 cusip deltas in silver transactions, the CASH share of holdings_lots' null cusips, the lots_* consumer census (Z-W4-S2); worker `0.9.0_WK_NFRA_MCPINDEX~11` | LOCAL (reads only) |
| `MX-i-4` | round-2 analysis item 5 | least privilege on `bd_exporter_additional`: a printed caller census for `opal/bd/credentials`, then the one Resource element removed through Terraform if the census reads 0 live readers; after MX-s-12's acceptance; worker `0.9.0_WK_NFRA_MCPINDEX~8` continued | WORLD (an IAM narrowing; infra-path floor) |
| `MX-x-1` | round-2 analysis item 6 (rows Z-S22 + Z-W7-S2, one cause) | the deploy recorder derives bun/node with `command -v` and runs its JavaScript CHANGELOG writer only under a JS runtime; worker `0.9.0_WK_NFRA_MCPINDEX~12` | WORLD (infra-path floor) |
| `MX-x-2` | round-2 analysis item 6 (row Z-W3-S4) | the emitter writes `portal_*` rows to their own `portal_datasets:` section, each with its exact `s3_key`; `portal_index` reads it; the catalog is regenerated, never hand-edited; worker `0.9.0_WK_NFRA_MCPINDEX~13` | WORLD (infra-path floor) |

| `MX-i-5` | round-3 analysis item 1; R-15 (row Z-W8-S3) | disarm: the 4 dead BD Playwright schedules (allocation, realized, transaction, unrealized) DISABLED through Terraform, never deleted, each first proven dead at two grains; asset-dim is the negative control; never-widen halves before the apply; worker `0.9.0_WK_NFRA_MCPINDEX~16` | WORLD |
| `MX-d-4` | round-3 analysis item 2; R-13 + R-14 (Z-C-S28, Z-C-S29) | opal_discover names the purpose-built tool as `next_tool` (query_v0 only where none exists, labelled an HTTP route) and carries a measured `served_written_at` per servable row; chain head of MX-d-5 -> MX-r-5; worker `0.9.0_WK_NFRA_MCPINDEX~14` | WORLD (infra-path floor) |
| `MX-d-5` | round-3 analysis item 4 (Z-W10-S1 + Z-W2-S8) | routing precision: Q22 vocabulary on the existing mkt.01 row, a NOT_CATALOGUED rule for one-common-word matches graded on recall, the ETF ask not mis-routed (NOT_CATALOGUED while no platinum/etfs row exists); worker ~14 after MX-d-4 | WORLD (infra-path floor) |
| `MX-t-9` | round-3 analysis item 3a | a read-only purpose-built tool for the json/* model-benchmark table (mp.05, already approved) on the mdpf pattern, with the model-design caveat; worker `0.9.0_WK_NFRA_MCPINDEX~15` | WORLD (infra-path floor) |
| `MX-t-10` | round-3 analysis item 3b | a catalog row and a read-only tool for platinum/etfs -- RELEASED by A1 (G-W stands: Andrew 'Go with your recs', record @dc75ddbe32, platinum/etfs YES); worker ~15 after MX-t-9 | WORLD |
| `MX-t-11` | round-3 analysis item 3c | a catalog row and a read-only tool for platinum/advi (in refused_units) -- HELD (G-W) | WORLD, HELD |
| `MX-r-5` | round-3 analysis items 2+3a release and item 5 | a NARROW gateway release of MX-d-4, MX-d-5 and MX-t-9 (the MX-r-4 A1/A2 pattern: release tree at the live commit, rollback proof, deploy-only tree), G-A delta and never-widen halves; then the thread re-run over the 4 A2 surfaces with judgment `r5.J1`; worker ~14 after MX-d-5 | WORLD |
| `MX-s-14` | round-3 analysis item 6; R-15 | port the BD transaction leg to the REST pull on the 49F session (the MX-s-10/s-12 pattern); DEFAULT == $LATEST; re-enable its trigger only in PHASE B; acceptance the next scheduled 21:53Z fire; unblocks Z-W11-S2; worker `0.9.0_WK_NFRA_MCPINDEX~17` | WORLD |
| `MX-x-3` | round-3 analysis item 7 (row Z-W13-S2) | validate_catalog_v02.py `--offline` with zero AWS calls, the report dir created, and the live run's non-OK row identified; worker `0.9.0_WK_NFRA_MCPINDEX~18` | LOCAL |

**G-W (gate, round 4):** Andrew's word to widen the runtime catalog to a new served surface (`platinum/etfs`, `platinum/advi`), named verbatim at DATA_CATALOG.yaml:32 "WIDENING IS ANDREW-ONLY, unchanged. Version bumps carry his verbatim." Holds `MX-t-10`, `MX-t-11`. Card carried by `1.0.0_SA_CTO~O` (sent ~04:36Z; MSTR~Z not live).

Round 3's item 6 row Z-W3-S12 (the round-2 battery's `pytest_named` helper) is not a cell: the issuer fixed it in the
round-3 battery's own `_root.sh` (`deliverables/2.0.0_SA_COO~MI/round3/checks/`), which reads verdicts from pytest's
`-rA` summary.

**QUEUED, NOT ISSUED (Andrew-direct 2026-09-26 ~18:1xZ, "all recs approved", call 3 as ruled: (b) QUEUE; record
`org/tier2_senior/0.7.0_AE_CloudOps~I/deliverables/ANDREW_DIRECT_20260926_181xZ_ALL_RECS_APPROVED_THREE_OPEN_CALLS.md`
@ac15460755; owner `2.0.0_SA_COO~O`):** a sweep of the other stale converter snapshots. Of 7 `opal-assets-silver-*`
families, 3 carry vendored modules whose bytes differ from repo source: blackdiamond (2), eclipse (3) and orion (3).
Their manifests are self-consistent. When cut, this is one repair cell per family on the MX-s-3 pattern (re-vendor
from CLOUD HEAD, safe-apply, deployed-bytes check). It is NOT cut in this round. Its un-park condition is the
round-2 close or an Andrew word to DO it.

# ROUND 5 -- THE REINSTATEMENT (L5, 2.0.0_SA_COO~MI, 2026-09-30)

Source: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be
(1.0.0_SA_CTO~O's rulings B1-B9 on Andrew's reinstatement order), cut against PRD v0.6 @e91ce9a0d5. MX-t-10 and MX-s-14
stay round-4 orders: t-10 lands on B3 (Andrew's R20 acknowledgement), s-14 on its scheduled fires (B6, gates nothing here).

| Cell | Source | What | Risk |
|---|---|---|---|
| `MX-s-15` | ruling B4; order item 2 | Schwab `dim_transaction` declared beside the three `dim_*` tables on all 6 surfaces (datasets.json, query.py schemas + grains, data_entitlement, schwab_audit, the reader role's prefix list for both masters); one master, one date; how existing grants resolve it recorded, never changed; worker `0.9.0_WK_NFRA_MCPINDEX~19` | WORLD (infra-path floor) |
| `MX-q-3` | ruling B7; order item 3 | `query_v0` as ONE read-only MCP tool in portal_index on the same handler, gate and caps, under C2 in full; discover names it (`kind: mcp_tool`) where no purpose-built tool exists; the HTTP route stays; worker `0.9.0_WK_NFRA_MCPINDEX~20` | WORLD (infra-path floor) |
| `MX-r-6` | rulings B1, B2, B4, B7; order items 2, 3, 6 | the Schwab enable release (MX-r-5 pattern): `schwab` added to ENABLED_INTEGRATIONS (6 ids), the reader role's dim_transaction prefixes safe-applied, MX-s-15 + MX-q-3 shipped (MX-t-10 if drained, named at the GO); never-widen halves + G-A delta; then the FWD-1 cold run by an already-admitted non-author principal holding a Schwab grant (r6.J1); worker ~19 after MX-s-15 and MX-q-3 | WORLD |
| `MX-a-8` | ruling B5; order item 4 | Black Diamond's analysis record refreshed at today's silver (MX-a-3's structure, 9 sections, `read_at`), naming ONE first tool, its exact read fence and the firm scope rule; J1 by the CVO; worker `0.9.0_WK_NFRA_MCPINDEX~21` | SERVED |
| `MX-t-13` | ruling B5; order item 4 | the first BD tool from MX-a-8: a dormant `black_diamond` integration, one fenced reader role (C7) from the record's read fence, a catalog row through the emitter, C2 in full; worker ~21 after MX-a-8 | WORLD (infra-path floor) |
| `MX-r-7` | ruling B5; order item 4 | the BD release: the reader role safe-applied, `black_diamond` enabled (7 ids), never-widen halves + G-A delta; FWD-4 PROOF live (r7.J1); worker ~21 after MX-t-13 and after MX-r-6 is complete (one release at a time on the host) | WORLD |
| `MX-t-12` | order item 5 (carried from MX-t-11) | a catalog row and read-only tool for platinum/advi -- HELD on G-W (Andrew NOT YET; 1.0.0_SA_CTO~O msg 27022); issued to ~20, not spawned | WORLD, HELD |

**Chains (fan-out 3 of 3 live chains, cap 8):** [MX-s-15 -> MX-r-6] ~19 and [MX-q-3] ~20 join at MX-r-6;
[MX-a-8 -> MX-t-13 -> MX-r-7] ~21, whose release waits on MX-r-6 complete. MX-t-12 is HELD and not spawned.

**Order item 7** (the COO's close run on all of it) is the issuer's act at the drain, not a cell; 3.0.0_SA_CVO~O grades
a8.J1, r6.J1 and r7.J1 at L9. **FWD-8 (v0.6, B8):** no build item was ordered; the issuer's close run exercises A8's
market-data half through Bloomberg's standing read and names the substrate, and any gap goes to the round-5 L10 slug.

**NOT CLAIMED by this cut:** Orion, Eclipse and SmartX tools (they follow MX-t-13's pattern in later rounds); FWD-9
(deferred on Andrew's word, B2); any identity, grant or sign-in change (B2); G-C inside NFRA_OPLGTW's own OG-g-1 (B1).

# ROUND 6 -- THE ENRICHMENT CUT (L5/L6, 2.0.0_SA_COO~MI, 2026-10-01)

Source: `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round5.md` @1edec80f63 (1.0.0_SA_CTO~O's L10 on rounds
4+5, msg 27666), section 5's enrichment list, cut in ONE issuance. MX-t-12 is CANCELLED on its section 3 (Z-W20-S3).

| Cell | Source | What | Risk |
|---|---|---|---|
| `MX-d-6` | item 1 (Z-W21-S22, Z-W15-S3) | opal_discover reads `silver_datasets` beside its sections (fix the READER, not the row); Schwab catalog rows for its 4 served datasets through the emitter; every catalog row graded by REACHABILITY (discover names its read_tool on its own example question), the MX-d-5 ETF assertion retired; worker `0.9.0_WK_NFRA_MCPINDEX~22` | WORLD (infra-path floor) |
| `MX-g-3` | item 2 (ruling 27413; train R7) | G-RDR: portal_index and opal_discover take their S3 client from `internal_role.s3_client()` (query_v0 pattern; default client when the ARN is unset; fail closed when it raises); MCPMSP's census `unrouted=0`; worker ~22 after MX-d-6 | WORLD (infra-path floor) |
| `MX-r-8` | item 3 | the slot-4 opal-gateway release of MX-d-6 + MX-g-3 on the live ref after OG-rl-1 (MX-r-7 pattern, C1-C6, `DEPLOY_BASE_REF`, never-widen halves CTO + COO, G-A); no Terraform, no new `.env` key; BD ExternalId option A NOT folded; worker ~22 after MX-g-3 | WORLD |
| `MX-v-7` | item 4 | the thread re-run after MX-r-8 serves: the BD tool's figure + as-of against the source object by VersionId (v7.AC1), then r7.J1 re-graded and r6.J1 (Alyssa, the round's one essential wait) at L9 by 3.0.0_SA_CVO~O; worker ~22 after MX-r-8 | WORLD |
| `MX-x-4` | item 6 (Z-W21-S23, Z-W21-S21, Z-W21-S7) | the batch repair: safe-ec2-deploy.sh's manifest rewrite through a UTF-8 JSON parser; the halt gate's per-tree serial before the shared root; the catalog emitter's census/portal inputs as declared arguments, refusing on an absent census; worker `0.9.0_WK_NFRA_MCPINDEX~23` | WORLD (infra-path floor) |
| `MX-s-16` | item 7 (Z-S69; Z-S72) | one writer per BD silver table behind bd-silver-merge: PHASE A census + the Z-S72 diagnosis (bd-silver-merge fails 6 unrealized files nightly) + plan; PHASE B retires the documents' merge (and bd-allocation-processor's notification only on proof) under never-widen halves; worker `0.9.0_WK_NFRA_MCPINDEX~24` | WORLD |

**Chains (fan-out 3 of 3 chains, cap 8):** [MX-d-6 -> MX-g-3 -> MX-r-8 -> MX-v-7] ~22 (one write set:
opal_discover/integration.py is shared by d-6 and g-3, and r-8/v-7 consume them); [MX-x-4] ~23; [MX-s-16] ~24.
MX-r-8 also waits on the train (slot 4 after OG-rl-1; train R1).

**Not cells:** item 5 (the gateway suite green, or each red test named with its owner) is the issuer's drain check;
the MX-d-5 assertion retirement rides MX-d-6. Z-S57's channel resolver was issuer scratch and is fixed.
Z-W21-S19 and Z-W19-S13 are NFRA_OPLGTW's. `platinum/advi` waits on Andrew's R20 word (G-W). FWD-6..FWD-10 enter no
earlier than round 7.

# ROUND 7 -- THE ENRICHMENT CUT (L5/L6, 2.0.0_SA_COO~MI, 2026-10-02)

Source: `ROUND_ANALYSIS.round6.md` @361b186c92 (1.0.0_SA_CTO~O's L10 on round 6, msg 28126), section 5's enrichment
list, cut in ONE issuance into this D9 tree: the CTO's msg 28146 lifted the hold and deferred the D6 move (section 6 superseded).

| Cell | Source | What | Risk |
|---|---|---|---|
| `MX-s-17` | item 1(a) (Z-W24-S3) | disarm first: the realized and transactions documents' merge step repointed from `scripts/` to `code/silver/` (+ `code/silver/lib/`), the script bd-silver-merge runs; PHASE A diff + ANNOUNCE, PHASE B under never-widen halves; worker `0.9.0_WK_NFRA_MCPINDEX~24` | WORLD |
| `MX-s-18` | item 1(b) (Z-W24-S4, S5) + issuer-found hazard | the BD runner's OWN sentinel check: a measured `has_data_rows=0` transactions sidecar completes the day, a 0-row snapshot withholds, `OK` only after a `head_object` read-back; `data/cot/` byte-unchanged; the gold runner deploy's `s3 sync --delete` to `code/bronze/` excludes `cot_bronze_ingest.py`; zip + `safe-apply`; worker ~24 after MX-s-17 | WORLD |
| `MX-s-19` | item 1(c), criteria (iv)-(v) (Z-W24-S3, S8; Z-S69) | retire both documents' merge step (no-op version + trigger rule disabled, MX-s-16 pattern); census 4 of 4; acceptance on the scheduled runs of 2026-10-05 and 2026-10-06 (the first Mon/Tue empty window); worker ~24 after MX-s-18 | WORLD |
| `MX-f-1` | item 2 (Z-S74) | READ: the gold chain's freshness skip path with its code line and one scheduled run's log; RULE: weekly trading-day basis for `bd_silver_allocations` and `bd_silver_unrealized` in `comp-freshness` + `lib/trading_calendar.py`, proven by offline fixtures (never `COMP_FRESHNESS_PIPELINE`); no change to whether the gate blocks; worker `0.9.0_WK_NFRA_MCPINDEX~25` | LOCAL |
| `MX-m-2` | item 4 (FWD-4) | measure before build: Orion, Eclipse and SmartX served silver census (keys, newest partition, as-of, rows, catalog row; denominator per platform); worker `0.9.0_WK_NFRA_MCPINDEX~26` | LOCAL |
| `MX-x-5` | item 5 (Z-W23-S2; packet 6.5; Z-S75) | the batch repair: the halt-gate scoping fixture off `.agent_context`; proof-of-spec-check WARNs on a re-committed instance still carrying PENDING rows; both aws shims export UTF-8; worker `0.9.0_WK_NFRA_MCPINDEX~27` (worker-light) | LOCAL |

**Chains (fan-out 4 of 4 chains, cap 8):** [MX-s-17 -> MX-s-18 -> MX-s-19] ~24 (s-17 and s-19 write the same two
documents; s-19 consumes s-18's live sentinel; the CTO sequenced the disarm first); [MX-f-1] ~25; [MX-m-2] ~26;
[MX-x-5] ~27.

**Not cells:**
- Item 3, r6.J1 (Alyssa's cold run), is the one essential wait: graded at L9 by 3.0.0_SA_CVO~O against A5, booked
  through 0.0.0_AB_MSTR~Z. It rides MX-v-7's J2.
- Z-W21-S15's two MCPINDEX tests, ruled by the issuer: `test_mx_s15_dataset_registered` failed only in a sparse
  worktree (the issuer's drain re-runs it in the full tree); `test_schwab_host_inputs.py` exists only on the gateway
  release lineage, so it is carried to this project's next gateway release cut, with Z-W21-S12.
- Z-W22-S1 and Z-W21-S12 are DEFERRED as ruled. Z-W21-S19, Z-W19-S13 and ETFS_RIVALS-W5-S3 are NFRA_OPLGTW's.
  `platinum/advi` waits on G-W. FWD-6..FWD-10 enter after MX-m-2 measures.
- No gateway release this round (analysis section 4).

# ROUND 8 -- PRD v0.7: INDEX EVERY NEED IN ALYSSA'S WORKFLOWS (L5, 2.0.0_SA_COO~MI, 2026-10-09)

Source: PRD v0.7 @b06af7c0d2 (`1.0.0_SA_CTO~O`, msg 32348), FWD-11..FWD-18 and contract changes 1-6. Input list: brief
`docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md` @3455b1783a Part IV.A (29 candidates, E-1..E-29).
Second read of the same inputs: `deliverables/2.0.0_SA_COO~MI/ALYSSA_WORKFLOWS_INDEX_INPUT_MAP_20261009.md` @280fd3c814.
Issued in ONE issuance when `3.0.0_SA_CVO~Z` signs the ratified-text half (status at L5: brief SIGNED, ratified STALE).
Round 7 stays open on MX-s-19 alone. MX-s-19 shares no path with these cells, so the two rounds do not collide.

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-d-7` | FWD-11 (the thread), FWD-13; contract 4 | discover's `latest_value` is READ from the served artifact's own as-of field at answer time, claim `measured`; a held certification value is never shown as the as-of. Proven on three datasets: model benchmarks (held 2026-08-10, served 2026-10-07 at L5), `aum-metrics`, `aggregate-aua-timeseries`. Plus the thread route: "how did <model> do against its benchmark <period>" reaches `mdpf_get_model_benchmarks` with that true date | CLOUD | WORLD (infra floor) |
| `MX-c-6` | FWD-12, FWD-15, FWD-17, FWD-18; contracts 1, 5, 6 | the catalog holds all 29 needs as entries: need, source, status (SERVED / PARTIAL / GAP / DENIED), tool or none, owner or `unowned`, the browser workflow it retires (C# / W#), read or write class. GAP rows are a declared row type the catalog gate admits. The YCharts tools are vendor entries reading PARTIAL with their live error (Z-S85). The 8 unowned gaps are catalogued, never built. Written through the catalog's ONE writer (C1) | CLOUD | WORLD (infra floor) |
| `MX-d-8` | FWD-14, FWD-17, FWD-1 change (contract 1) | discover answers a GAP entry with its owner, and a write-class entry with its class and whether the CALLER's grant allows it. Alyssa's six phrasings ("account counts by partner", "cost basis", "statement", "stress test", "download the attachment", "S&P YTD") and the three write asks each reach their entry on the first try in the routing harness. No phrasing lands on a dataset whose meaning is a different need | after MX-d-7 and MX-c-6 | WORLD (infra floor) |
| `MX-r-9` | FWD-11, FWD-13, FWD-14, FWD-17 live | the gateway release of MX-d-7, MX-c-6 and MX-d-8 through the opal-gateway release train (`2.0.0_SA_COO~O` holds the queue). PHASE A: plan and ANNOUNCE by the worker. PHASE B: apply by a site-Z CloudOps lane under never-widen halves. Then the live reads: FWD-13's three comparisons, FWD-14's six discover calls, FWD-17's three answers | after MX-d-8 drains | WORLD |

**Chains (fan-out 2 of 2 chains at the cut, cap 8):** [MX-d-7 -> MX-d-8 -> MX-r-9] and [MX-c-6 -> MX-d-8].
- A2 (2.0.0_SA_COO~MI, 2026-10-09 ~04:3xZ) SUPERSEDES A1 @19248a86b8. A1's premise was wrong. It counted the prose
  `vintage_semantics`; the structured field it said was missing is already there. 37 of 37 artifact rows in
  `app/refs/DATA_CATALOG.yaml` carry `vintage_field`, which the emitter extracts at
  `workflows/atom_decomposition/emit_catalog_v02.py:770`. The three FWD-13 rows read `data_as_of`,
  `_provenance.source_vintages['global/aum-metrics']` and `as_of_last`.
- So MX-d-7 changes only the reader (`app/integrations/opal_discover/`) and writes no catalog file.
- MX-c-6 writes the catalog through its ONE writer: `catalog_entries/*.yaml`, the emitter, the catalog gate and the
  regenerated `DATA_CATALOG.yaml`.
- The two write sets are disjoint. MX-d-8 writes `opal_discover/` after both. MX-r-9 is one release of all three.

**The thread (FWD-11) at close.** Alyssa, in her own words, asks how a model did against its benchmark for a period; the
transcript is read beside the served artifact's date and the opalinvest.dev page. It is her act, graded at L9 by the
CVO and booked through `0.0.0_AB_MSTR~Z`. It is the round's one essential wait, and the same shape as r6.J1. FWD-12's
subtraction (the 29 entries against her two briefs) and FWD-18's count (denominator 14) are also read at L9 from the
served catalog, by a reader who is not the author.

**Not cells:**
- FWD-16 follows NFRA_OPLGTW's serve dates. E-1..E-8 enter as GAP entries owned by NFRA_OPLGTW in MX-c-6. On the
  day the first OPLGTW v2.x dataset serves, a cell turns its entry SERVED the same day (FWD-10's rule). Owner of the
  trigger: this lane's drive tick reads OPLGTW's serve dates.
- E-9, E-10, E-11, E-12, E-20, E-26, E-27, E-28: catalogued `unowned` in MX-c-6, never built here (contract 6).
- Z-S85 (YCharts time series 403; snapshot symbol key lost) belongs to the YCharts integration's owner. MX-c-6 catalogs
  the two tools as PARTIAL with the live error (FWD-15's ACCEPT); fixing them is not this round's.
- E-24's grant ("not measured") and the DENIED verdicts are `opalbloomberg`'s at L5. MX-d-8 reads the CALLER's grant at
  answer time, so Alyssa's own principal decides at r-9's live read and at the thread run (brief Part V, item 4).

**Bounds inlined at L6:**
- the catalog's ONE writer (C1);
- every tool name is generated or validated (C3, CLAUDE.md rule 30, which now REFUSES);
- no tool ships without its catalog entry and class (C2);
- egress is open except Bloomberg (law edit @4d77a9c3ea), but no cell calls a vendor beyond the live reads named;
- discover still reads NO body except the as-of field FWD-13 requires, and that read is the served object's own field.

# ROUND 9 -- PRD v0.8: THE OPERATIONS LEAD'S READERS, FWD-19 (L5, 2.0.0_SA_COO~MI, 2026-10-09)

Source: PRD v0.8 @0eff9e0e6d, landed @a71e82b221 (`1.0.0_SA_CTO~O`, msgs 32485 and 32502), FWD-19 and the v0.8 addendum's
contract changes 1-5. ADMITTED at L5: ratified-text SIGNED by `3.0.0_SA_CVO~Z` (current), brief SIGNED (auto).
Shape: OW-k-1's fixtures `tools/ops_kit/fixtures/trade_rec.json` and `billing.json` @cc539738c6 (12 rows each, top-level
`as_of` + `rows`). The trade_rec fields are `account custodian trade_date symbol side quantity opal_status
custodian_status matched`. The billing fields are `account household billing_period aum fee_rate_bps fee_amount status`.
**Issued in ONE issuance after round 8 drains** (the addendum's Order), and after MX-r-9 has left the release queue.
The write surface is disjoint from round 8's: new reader modules plus new catalog entries. The only shared file is the
catalog, and it has ONE writer, cut last.

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-o-1` | FWD-19 (trade rec); contracts 1-3 | FIRST the source census (C1's bar): every candidate producer of a per-trade Opal status and a custodian status, each with its denominator, and the surviving source read once. Candidates named by the PRD, which are candidates only: the trade engine's statuses and the custodian silver transactions. Then the reader: one gateway tool returning fixture-field rows inside the C4 envelope (firm or master scope, as-of read from the served object, completeness). C7 isolation applies: no row and no sum crosses a firm or master. The tool name is builder output (rule 30). The fixture is a test input only. If no source survives the census, the cell ships a GAP finding naming the owner and builds no tool | after round 8 drains | WORLD (reads live served data) |
| `MX-o-2` | FWD-19 (billing); contracts 1-3 | the same two acts for billing. Candidate: the Black Diamond fees read behind `blackdiamond_list_fees` (`app/integrations/blackdiamond/integration.py:48`). Census first, then a fixture-field reader or a GAP finding | after round 8 drains | WORLD |
| `MX-c-7` | FWD-19 catalog; contract 4 | the catalog's ONE writer adds six entries. The two readers' entries are SERVED with tool and class read, or GAP with the owner MX-o-1 or MX-o-2 named. The four items carried as GAP, `unowned`, with no tool: post model update rec, high cash account alert FA, assets transfer alert FA, restricted account alert FA. The three FA alerts are under the standing moratorium, so this cell builds nothing for them | after MX-o-1 and MX-o-2 | WORLD (infra floor) |
| `MX-r-10` | FWD-19 live | the gateway release of MX-o-1, MX-o-2 and MX-c-7 through the opal-gateway release train (`2.0.0_SA_COO~O` queue; PHASE A by the worker, PHASE B by a site-Z CloudOps lane under never-widen halves). Then, under an ALREADY ADMITTED principal, the on-demand live read of each SERVED reader: rows carry the fixture fields, and the envelope states scope, as-of and completeness | after MX-c-7 drains and MX-r-9 has released | WORLD |

**Chains (fan-out 2 of 2 chains at the cut, cap 8):** [MX-o-1 -> MX-c-7 -> MX-r-10] and [MX-o-2 -> MX-c-7].
- MX-o-1 and MX-o-2 each write their own new integration folder and its tests, so the write sets are disjoint. The one
  shared line, the tool registry hookup, is added at the merge (C10, `/dispatch` Step 5), never by a cell.
- MX-c-7 waits on both readers because an entry's status (SERVED or GAP) and its tool name come from the census outcome.

**Close.** FWD-19 is proven on demand at MX-r-10's live read under an admitted principal. The operations lead's own
session is the organic arm, not the proof. His admission is Andrew's act (C8). FWD-9's per-user scoping binds from that
admission, and his grant is written before his first data call. A reader that ends GAP leaves FWD-19 NOT done, and the
L10 slug says so.

**Not cells:**
- Trade-request intake and its C-NO-SEND fence belong to NFRA_OPSWKF (dell2).
- The ops kit's adapter swap from fixture to live read belongs to NFRA_OPSWKF FWD-7. dell2 is told the date through
  `0.0.0_AB_MSTR~Z` (target drain 2026-10-12).
- No alert, notification or monitor is built (moratorium; contract 4).
- The operations lead's admission and grant are Andrew's (C8).

**Bounds inlined at L6:** every round-8 bound (ONE catalog writer; builder-output names; no tool without its catalog
entry and class; vendor calls limited to the named reads). Also: a fixture value is never served as data; every answer
carries the C4 envelope.

## ROUND 9 AMENDED AT THE CUT (2.0.0_SA_COO~MI, 2026-10-10 ~23:4xZ) -- the round-8 L10 analysis's enrichment list

Source: `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b (`1.0.0_SA_CTO~Z`, msg 33065), section 4, E1-E3. E1 is the four
cells above, unchanged. The analysis adds two items:
- **E2** (one catalog cell plus a release) is FOLDED into the cells that already hold those write sets. The round has
  ONE catalog writer and ONE release, so E2 rides MX-c-7 and MX-r-10 rather than adding a second writer.
- **E3** (the batch repair) is one new cell.

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-7` (widened) | FWD-19 catalog, plus E2: FWD-18, FWD-11 | Adds E2 in the same one-writer pass. Drop C1 from E-25's retires. Add C3 to E-4, E-5 and E-9 (all GAP), so FWD-18 reads 3 of 14 with C3 carried (measured 4 of 14 at the base). Move "statement" and "S&P YTD" into E-9 and E-19's `example_questions` and retire the two discover word folds (`_YTD`, `_AMP_WORD`); one general exact-example rule is allowed, a word-specific mapping is not. Put E-13's unknown-model guidance in its `note` and surface it in discover's match (ruling 2a) | after MX-o-1, MX-o-2 and MX-x-6 | WORLD |
| `MX-r-10` (widened) | FWD-19 live, plus E2 live | Ships c-7's discover change too, under ruling 2c's procedure: the deploy tree's HEAD IS the deploy-only commit, and the stamped label is read back before the first leg closes. The live read adds "statement" -> E-9, "S&P YTD" -> E-19, FWD-18 3 of 14 from the deployed catalog, and an unknown model name reaching E-13 with the five model codes | after MX-c-7 drains | WORLD |
| `MX-x-6` (new, E3) | -- (repair) | Two repairs. The emitter refuses a `--census-dir` outside its own checkout (row Z-W29-S1). The gateway suite gets a failing-ID baseline per tree shape (full, sparse) and `suite_delta.py`, so drains grade by ID delta, never by count (rows Z-S88, Z-W28-S8). The schwab and grant failing IDs go to `2.0.0_SA_COO~O` at the drain | at issuance | WORLD (infra floor) |

**Chains (fan-out 3 of 3 chains at the cut, cap 8):** [MX-o-1 -> MX-c-7 -> MX-r-10], [MX-o-2 -> MX-c-7] and
[MX-x-6 -> MX-c-7]. The x-6 -> c-7 edge is a data dependency: c-7 runs the emitter that x-6 changes. Write sets stay
disjoint:
- x-6: the emitter, its test file and the gateway suite baseline;
- c-7: the catalog sources, the emitted catalog and discover;
- each reader: its own new folder.

**Not cells (analysis section 4):**
- J1 waits on Alyssa, booked through `0.0.0_AB_MSTR~Z` (HELD at Andrew).
- The deploy-wrapper fix for Z-S92 and Z-S94 belongs to `2.0.0_SA_COO~O`.
- Z-C-S42 belongs to `2.0.0_SA_COO~C`.
- Round 7 stays open on MX-s-19.

## STANDING BATTERY CLAUSES (the issuer's cut template, 2.0.0_SA_COO~MI) -- binding on every later round of this project

1. **A check excused from the base dry-run has its PASS arm exercised once, on a planted input, before the cut**
   (`ledger/ROUND_ANALYSIS.round9.md` @bc8e36fdd5 ruling 4; row Z-S100). The issuance commit's battery lines name the
   planted input and its reading beside each `not dry-run` check. Instance: r10.AC2's route counter read 0 in every world,
   because its PASS arm was never run before the cut.
2. **A round-close verdict on this project is read with the round-close suite's five known failures listed beside it,
   until that suite reads 24 of 24** (ruling 3; row Z-S97, owner `2.0.0_SA_COO~C`).

## PARKED AT ROUND_CLOSE (2026-10-11 ~15:2xZ, `ROUND_ANALYSIS.round9.md` section 3) -- no round 10 is cut

Un-park on ANY of:
- (a) a FWD-19 producer serves (billing: ADVI_BILLING, dell2; trade-rec fund grain: NFRA_OPSWKF, dell2). The issuer
  then cuts that one reader.
- (b) Andrew books Alyssa's run, and J1 is graded.
- (c) round 7's L8 lands after MX-s-19's 2026-10-13 runs (s19.PRE after 03:00Z).

## ROUND 10 (2.0.0_SA_COO~MI, 2026-10-13 ~20:0xZ) -- one short round for direction Z4: FWD-20 and FWD-21

Source: `ledger/CTO_RULING_ROUND10_Z4_ONE_SHORT_ROUND_20261013.md` (`1.0.0_SA_CTO~Z`, msg 33704) on PRD v0.9 @e581c26ab4
(ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO~Z` at 44d06588b5, msg 33712). It un-parks the project for one
round; the project re-parks at ROUND_CLOSE after it, with the round-9 un-park conditions (a)-(c) standing.

### R10.1 THE CELLS -- 2

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-8` | FWD-20, FWD-21 | The ONE catalog writer (contract 4 of the v0.9 addendum: the two outcomes write one file, so they are MERGED into one cell, never two writers). (1) A `tool_index:` section: one entry per tool the DEPLOYED gateway serves, partitioned (a) names its index / (b) reads data, no index yet, owner or "unowned" / (c) not a data read, each classified from its definition. (2) A `harvest_datasets:` section: one row per SERVE-NOW prefix of the servable-prefix list v3 @0b2778751a (16 prefixes; row 8 = six gold tables). (3) discover reaches `harvest_datasets` rows by their own text | at issuance | WORLD |
| `MX-r-11` | FWD-20, FWD-21 live | Release c-8's catalog and discover change onto the gateway host; read the partition and the three discover reads live; one (a) tool's depth and freshness re-read by a second instrument. Takes the gateway queue BEHIND NFRA_MCPORTAL's MP-z-5 (direction Z1, first on site Z) | after MX-c-8 drains, and after MP-z-5's ledger closes | WORLD |

**Chains (fan-out 1 of 1 chains, cap 8):** [MX-c-8 -> MX-r-11], worker `0.9.0_WK_NFRA_MCPINDEX~33`. One chain because
the round has one write surface (the catalog) and its release. PHASE A of MX-r-11 (deploy-only commit + ANNOUNCE) is the
worker's; PHASE B is re-addressed by amendment to `0.7.0_AE_CloudOps~MI` at the gateway slot (the MX-r-10 pattern).

### R10.2 CHOICES THIS CUT MAKES (the issuer's, inside its decomposition)

1. **The served-tool denominator** is the deployed commit's tool manager plus its enabled integrations
   (`services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`; `ENABLED_INTEGRATIONS` from that
   commit's `deploy-to-ec2.sh`), the same set MC Portal's `admin_gateway_breakdown._registered_tool_names()` reads.
   Measured at base 08b77fd98d against 185dc04888: **N = 67** (43 native + 24 from 7 integrations); the live host read
   the same 67 (ssm 6f80490b, 2026-10-13 ~19:5xZ).
2. **The link is the one MC Portal already reads** (`admin_gateway_breakdown._catalog_read_tool_rows`: any mapping with
   `read_tool` names an index by its `entity`/`key`). An (a) entry carries `read_tool: <tool>` and `entity: <a row id
   outside tool_index>`; (b) and (c) entries carry no `read_tool`, so the panel never shows a made-up index. Base:
   10 of 67 tools already have a link (the portal and silver read tools); 0 carry depth or freshness.
3. **Member by definition, never name** (the CVO's carried note, msg 33712): every entry names its `definition`
   (`<path>:<line>` in the deployed gateway tree), and the check confirms the tool is defined there.
4. **Depth and freshness of an (a) tool** are read at emission from the index's served artifact (read-only S3 listing),
   recorded with `claim`, `value`, `basis: s3://<bucket>/<prefix>`, `method` (key-date | last-modified) and `read_at`;
   where no artifact can be listed (a live-queried silver row), the claim is `absent` with its reason. discover's
   answer-time freshness (FWD-13) is unchanged.
5. **No existing gateway tool reads `opal-data-harvest`**: `comp-find 'opal-data-harvest' infra/aws/ec2/opal-gateway`
   reads 0 hits across 261 files (115 binary not searched), and `gateway_query_catalog` reads only the catalog's one
   `bucket` (`portal_index/integration.py:185`). So each harvest row is catalogued with `read_tool` null and
   `gap_owner: NFRA_OPLGTW` (the asset-manager principals, the research grant and its reader are that project's next
   round, direction Z5; contract 2 of the v0.9 addendum). The worker re-verifies before relying on this.
6. **The V1 rule is mechanical here:** a WITHHOLD prefix, `management/v1/`, the whole `amgt/harvest/gold/` prefix and
   any prefix not on the list get no row.

### R10.3 BATTERY (base 08b77fd98d; `deliverables/2.0.0_SA_COO~MI/round10/checks/`)

| check | base | planted PASS arm (standing clause 1) |
|---|---|---|
| c8.AC1 | FAIL: partition sum 0 of N=67 | planted tool_index (7 a / 53 b / 7 c): PASS; planted bad definition, bad link, missing entry: each FAIL |
| c8.AC2 | FAIL: 0 of 16 prefixes rowed; list parse 11 rows / 16 prefixes agrees with the grant section | planted 16 rows: PASS; planted WITHHOLD row, planted whole-gold row: each FAIL |
| c8.AC3 | FAIL: discover good 1 of 3 (the Schwab control holds: 8 matches, 3 of 3 silver) | stub discover answering harvest rows: PASS; stub with a harvest match on the Schwab control: FAIL |
| r11.AC1 | FAIL: no ledger entry at HEAD (12 of 12 sentinels scanned) | the MX-r-10 check, re-pointed |
| r11.AC2 | FAIL live: /health 200, partition 0 of 67, discover 1 of 3 | the two instruments above, shipped to the host |
| r11.AC3 | FAIL: no (a) entry with a measured s3 basis | grader on a planted listing: AGREE PASS; depth off by a day: DISAGREE FAIL |

### R10.4 WHAT THIS CUT DOES NOT CLAIM

- It does not grade whether an asset manager can READ the harvest data: that needs NFRA_OPLGTW's principals and grant
  (Z5). FWD-21's DONE WHEN is the discover route, and that is what this round proves.
- It does not prove the (a)/(b)/(c) classification is semantically right beyond its definition line; L9 (the CVO) reads
  a sample of the (c) members against their definitions.
- FWD-19 and FWD-11 stay parked (positioning ruling @f469cb665f). MX-s-19's s19.AC2 reads stay dated 2026-10-19/20.

## ROUND 11 (2.0.0_SA_COO~MI, 2026-10-14 ~01:0xZ) -- the round-10 analysis's two items: D1 (FWD-20 depth + durable key), H1 (FWD-21 on list v4)

Source: `ledger/ROUND_ANALYSIS.round10.md` @301af339c7 (`1.0.0_SA_CTO~Z`, msg 33843) on PRD v0.10, ADMITTED (msg 33847).
Graded so far: FWD-21 on v3 REALIZED; FWD-20 partition REALIZED; FWD-20 depth NOT_REALIZED, because "absent" on 11 of 11
was a wrong claim (row Z-W33-S1). The project parks after this round.

### R11.1 THE CELLS -- 2

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-9` | FWD-20 depth + Z-S106, FWD-21 (v4) | The ONE catalog writer again: D1 and H1 write the same two files, so they are MERGED into one cell. (1) Re-read each (a) depth FROM THE SERVED ARTIFACT: a named first-date field, or a dated series' first element, gives `measured`; a live-queried row's served window gives `inferred`; `absent` only where no served artifact carries any date. (2) discover answers depth at answer time, as it already does freshness. (3) The durable link key: a tool_index entry carries `index`, never `entity` or `key`; MC Portal's breakdown reader learns to read `index` (one token at `admin_gateway_breakdown.py:109`). (4) Harvest rows for the prefixes list v4 @7e0da2dfee adds: 24 of 24 top-level prefixes covered, plus row 12b's seven research tables | at issuance | WORLD |
| `MX-r-12` | FWD-20, FWD-21 live | One gateway release of c-9's files on the LIVE ref. Its deploy cone carries `infra/logic/registry` (analysis ruling 3, row Z-S92; now a cut-template rule). It queues behind any release in flight (NFRA_OPLGTW OG-ap-14) | after MX-c-9 drains, and after any in-flight gateway ledger closes | WORLD |

**Chains (fan-out 1 of 1 chains, cap 8):** [MX-c-9 -> MX-r-12], worker `0.9.0_WK_NFRA_MCPINDEX~34`. PHASE A of MX-r-12 is
the worker's; PHASE B is `0.7.0_AE_CloudOps~MI`'s (live).

### R11.2 CHOICES THIS CUT MAKES

1. **Body reads are allowed for ONE named date field per object.** MX-c-8's bound 4 forbade them, and that is why depth
   read absent. A cell reads the field and prints and stores only the date, never any other value.
2. **The durable key** keeps MC Portal's walker as the one reader. The change is generic (`index` beside `entity`/`key`).
   No open MC Portal order holds the file (43 scanned); `2.0.0_SA_COO~MP` is told at issuance.
3. **A harvest reader, if served.** NFRA_OPLGTW's `harvest_read`/`harvest_list` are in trunk, not in the deployed
   7eff14b2e6. If the deployed commit at the census serves a tool that reads `opal-data-harvest`, the rows name it as
   `read_tool`; otherwise they keep `gap_owner: NFRA_OPLGTW`.
4. **Grade on the tree AS SHIPPED** (the Z-S112 lesson). c9.AC1 overlays the worktree's three shippable files on the
   deployed tree.

### R11.3 BATTERY (base 099a64bd12; `deliverables/2.0.0_SA_COO~MI/round11/checks/`)

| check | base | planted arms (standing clause 1) |
|---|---|---|
| c9.AC1 | FAIL: (a) links valid 0 of 11; 11 entries carry a row identity | on the deployed tree with the walker's one-token change: `index` planted gives PASS 67 of 67; one `entity` re-planted gives FAIL |
| c9.AC2 | FAIL: 11 of 24 top-level prefixes, 0 of 7 research tables | 24 + 7 rows give PASS; `wsj/` removed gives FAIL 23 of 24 |
| c9.AC3 | FAIL: measured 0; the AUA answer carries no depth | AUA `as_of_first` = 2024-11-01 at `platinum/mdpf/global/`: AGREE by the aws CLI, and an answer-time depth plant gives PASS; value 2024-11-02 gives DISAGREE, FAIL |
| r12.AC1 | FAIL: no entry (19 of 19 sentinels) | the MX-r-11 check, re-pointed |
| r12.AC2 | FAIL live (ssm 0838b977): index rc=1 (links 0), discover 3 of 3 | the two instruments shipped to the host |
| r12.AC3 | FAIL (= c9.AC3 on the deployed bytes) | as c9.AC3 |

Drain hygiene (analysis ruling 4, row Z-S107): re-baseline `failing_ids_full.txt` at the drain; it is not a build cell.

### R11.4 THE GATE BRANCH, folded into `MX-c-9` as A4 (2.0.0_SA_COO~MI, 2026-10-14 ~02:5xZ, on `1.0.0_SA_CTO~Z`'s ruling msg 33936) -- one issuer per round, so it is a re-cut of the round's order, not a second issuance

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-9` A4 (was MX-g-1) | FWD-21 (row 12b) | `.tools/naming-gate.py` `judge()` gains ONE branch: a literal equal to `legacy_address(key)` for a `legacy_addresses.json` row whose reader is the committing project grades CONFORMANT. The committing project is derived from the staged paths' project home, never a free field. The six registry rows land in this cell's commit, before MX-c-9 A3's catalog | at issuance; merge held for dell1's answer, or until 03:40Z | WORLD (infra floor: a shared gate) |

Inside MX-c-9 the commits run gate + registry rows first, then the A3 catalog commit, with worker `~34` on both. MX-r-12 ships the 33-row catalog
already committed (A4), and the six rows ride the next gateway release. The gate's owner is NFRA_CTLPLN: at the drain,
the commit and test result go to `2.0.0_SA_COO~C` through `0.0.0_AB_MSTR~Z` (laptop CTO condition 3). Battery: g1.AC1 and g1.AC2 (now
limbs of c9.AC2) FAIL at base, and g1.AC2's negative arm (another project's home) is REFUSED at base, as it must stay.

## ROUND 12 (2.0.0_SA_COO~MI, 2026-10-14 ~05:0xZ) -- the round-11 analysis's D2: FWD-20 depth on EVERY (a) tool, plus research-table routing; then the project parks

Source: `ledger/ROUND_ANALYSIS.round11.md` @05caf1144b (`1.0.0_SA_CTO~Z`, msg 33989). PRD v0.10 is unchanged and ADMITTED.
Graded: FWD-21 on v4 REALIZED; FWD-20 partition REALIZED; FWD-20 depth NOT_REALIZED for a second round (10 of 11 (a)
tools read absent where v0.10's cases make them readable).

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-10` | FWD-20 depth, FWD-14 routing | The one catalog writer. v0.10's depth cases applied to EVERY (a) tool: measured from a first-date field or a series' first element; measured as a snapshot's as-of; inferred as a live-queried row's served window, with its basis; absent only where the served artifact carries no date. A multi-index query tool takes `per-link` depth from the rows it links. Discover answers each measured row's depth at answer time. Each of the 7 research tables gets example questions that route to it | at issuance | WORLD |
| `MX-r-13` | FWD-20, FWD-14 live | One catalog release on the LIVE ref, behind NFRA_OPLGTW r30, its tier fix and OG-mg-1 (analysis section 3). The cone carries `infra/logic/registry` | after MX-c-10 drains and the OPLGTW releases close | WORLD |

**Chains (fan-out 1 of 1, cap 8):** [MX-c-10 -> MX-r-13]. Worker `0.9.0_WK_NFRA_MCPINDEX~35` builds; `0.7.0_AE_CloudOps~MI`
releases.

**STANDING BATTERY CLAUSE 3** (analysis ruling 1, binding on every later round of this project): a check that grades a
claim about a SET grades EVERY member, with the denominator printed, and never a sample. c9.AC3 graded AUA alone and
passed while 10 of 11 claims were wrong.

### R12.1 BATTERY (base 66eda2801a; `deliverables/2.0.0_SA_COO~MI/round12/checks/`)

| check | base | planted arms |
|---|---|---|
| c10.AC1 | FAIL: valid 1 of 11 (absents on dated or unresolvable artifacts) | AUA measured; aum-metrics `total.series_start` and etfs `data_as_of` measured; the rest inferred: PASS 11 of 11 (aws CLI AGREE). etfs absent: FAIL 10 of 11; aum value off by a day: FAIL 10 of 11 |
| c10.AC2 | FAIL: anchor "security analysis research dossier" reaches harvest_packs (anchors 1 of 2) | stub routing to the dossier table: PASS 7 of 7, anchors 2 of 2 |
| c10.AC3 | FAIL: anchors measured 0 of 2 | stub answering three rows: PASS 3 of 3; one value off: FAIL 2 of 3 |
| r13.AC1 | FAIL: no entry (18 of 18 sentinels) | the MX-r-12 check, re-pointed |
| r13.AC2 | a live regression guard (partition and discover); it passes on the host now | the round-11 instruments |
| r13.AC3 | FAIL (c10.AC1 and c10.AC3 on the deployed bytes) | as c10 |

Drain hygiene: the Z-S107 suite re-baseline. After the round, the project parks at ROUND_CLOSE on the round-9 un-park
conditions.


## ROUND 13 (2.0.0_SA_COO~MI, 2026-10-14 ~14:0xZ) -- PRD v0.11 FWD-22: the one catalog at TABLE grain from the CRO's G1 harvest contracts

Source: PRD v0.11 @7878037d98 (`1.0.0_SA_CTO~Z`, msg 34078), the G1 enrichment list (6 items), and G1 @0d7c29b3c5
(`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`, 78 contracts). Andrew-direct
~12:4xZ (`ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md`); the gateway is to be live with the census
tables by Friday 2026-10-16. The ratified-text half is SIGNED by `3.0.0_SA_CVO~Z` at v0.11 (`prd-signoff.py status` ADMITTED); the brief half is
auto-signed. Later groups (G2 to G6) arrive as CONTRACTS-only enrichment lists and take the same pipeline: **the generator and the loader built here are
the pipeline they reuse**, so the schema below is written once.

### R13.1 THE CELLS -- 2 (and the release, which is round 12's `MX-r-13`, amended)

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-11` | FWD-22 items 3, 6 and the loader | The catalog's one writer accepts a TABLE-grain harvest row (6 new fields, one per dataset, any depth below the 24 served top-level prefixes) and refuses a bad one; the tool index lists `harvest_list` and `harvest_read` (member b) only once the census serves them (`pending_members.yaml`); a harvest row may name only a served tool (`harvest_read_tool_errors`, refusing the emit); the header becomes v0.5 carrying Andrew's verbatim; discover answers a row's `retired` flag (a retired row is never a tool target) and matches a row by its `nl_tags` | at issuance | WORLD |
| `MX-c-12` | FWD-22 items 1, 2, 4, 5 | `gen_harvest_rows.py` writes the 78 rows from G1 (grain, freshness, keys, size, producer claim, never-sum rules, tags, common queries, the retire list, the read_tool policy), preserving the round-12 routing text of the 39 existing rows; the catalog source rows become those 78 | at issuance | LOCAL |
| `MX-r-13` (round 12, AMENDED A2) | FWD-22 live | The one catalog release now ships the round-13 catalog and discover change too, behind OG-hv-2, OG-ap-18 and OG-ap-17 | after both cells drain and the OPLGTW releases close | WORLD |

**Chains (fan-out 2 of 2, cap 8):** [MX-c-11] and [MX-c-12] are independent: disjoint write sets (the emitter, validator, tool index,
discover and their tests, against the generator, `catalog_entries/` and its test), and no cell consumes the other's output. They meet only
at the drain, where the issuer regenerates the catalog (R13.4). A third chain does not exist: items 3 and 6 need the loader, items 1, 2, 4 and 5 need
the generator, and the release is not a build cell. Workers `0.9.0_WK_NFRA_MCPINDEX~36` (c-11) and `~37` (c-12), model haiku, effort high (MP-20261010);
`0.7.0_AE_CloudOps~MI` releases.

### R13.2 THE ROW SCHEMA (the issuer's choice inside its decomposition; written once, reused by G2 to G6)

A harvest source row (`catalog_entries/harvest_<slug>.yaml`) is the 11 fields of today (`HARVEST_FIELDS`) plus `table`, `layer`, `format`,
`contract`, `nl_tags`, `retired` (and `retired_reason` iff retired). `contract` = {`id`, `size`, `keys`, `freshness`, `partition`, `producer`}: G1's own objects
verbatim, each already carrying its `claim` (`measured` / `inferred` / `absent`), so a consumer can reject on the claim (CLAUDE.md "a value must carry its claim").
G1's `securities` object is named `keys` in the row. The rest is derived by rule from the contract and graded against G1 at the pin.

Rule 24 record (a schema an agent authors):
- (i) MECE over the declared domain: the domain is the 78 G1 contracts; the subtraction is `set(G1 prefixes) - set(row prefixes)` and its reverse, printed in c12.AC1 (base: 52 missing, 13 extra). Each layer value is one of four; a dataset has one row.
- (ii) Same grain: one row per dataset (table), where the base mixed 26 table rows with 13 source-level rows that stood for 50 tables. The source-level rows are deleted.
- (iii) Intent coherence: `retired` is one axis (is it a tool target), distinct from `read_tool` (which reader), so a retired row names no reader.
- (iv) State coherence: `read_tool` null (no reader deployed) is a different state from `retired` true (no reader wanted); retiring a row does NOT move `contract.freshness`, and a new deployment does NOT un-retire a row.
Word-boundary token census at HEAD 35f45893a7 (`\b(nl_tags|retired|table|layer)\b` over `emit_catalog_v02.py`: 10 hits; `\b(nl_tags|retired|contract)\b` over discover's `integration.py`: 1 hit): every hit is prose or a local variable of the gold-prefix check (lines 6, 86, 526, 556-559, 1058, 1068, 1519 of the emitter; line 41 of discover), and none reads a harvest row's key of those names. `format` and `contract` were not censused over the emitter (`format` is `str.format` noise there, so a token census is meaningless); MX-c-11 reports every reader of the six keys it finds.

### R13.3 BATTERY (base HEAD 35f45893a7, G1 pin 0d7c29b3c5, round-12 rows pin 8c74d1d902; `deliverables/2.0.0_SA_COO~MI/round13/checks/`)

| check | base | planted arms (clause 1: exercised at the cut) |
|---|---|---|
| c12.AC1 | FAIL: 39 files, prefix set unequal (52 missing, 13 extra), contract.id 0 of 78 | `plant_c12.sh`: the reference 78 rows PASS; dropping a row, a wrong contract.id, a legacy hyphen table typed as a literal prefix: each FAIL |
| c12.AC2 | FAIL: graded 26 of 78; fields failing on every row | the reference set PASS; an object count off by one, a producer text silent about an inferred claim, emptied nl_tags, an un-retired `publications/v1/`, a research-dossier retired with no evidence file, a dropped round-12 example question, a lost derived_from: each FAIL |
| c12.AC3 | FAIL: the generator is absent | the reference generator PASS under 5 deployed-tool sets (390 of 390 rows); a generator that always names `harvest_read` FAIL |
| c11.AC1 | FAIL at ACCEPT 0 of 78 (the loader refuses every table-grain row); REFUSE 11 of 11 holds trivially at the base | `plant_c11.sh`: the reference loader PASS (78 accepted, 11 refused); a lax loader that accepts everything FAIL |
| c11.AC2 | FAIL: arms B, C, F (3 of 6 pass at the base: A, D, E are the preserved behaviours) | the reference tool index PASS 6 of 6 |
| c11.AC3 | FAIL: 1 of 6 (the record file holds the verbatim; the emitter does not) | the reference header PASS 6 of 6 |
| c11.AC4 | FAIL: the three named tests are absent (0 of 3) | the named-test pattern (round 12's c10.AC2/AC3 used the same) |

The 13 stale source-level rows are not graded away by a delete-count; c12.AC1's `extra 0` is what removes them.

### R13.4 THE DRAIN (the issuer's acts, not a worker's)

After both cells merge (one commit per chain end, `safe-merge.sh`):
1. Regenerate the catalog: run the emitter (it writes `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`). Checks on the result: `version: 0.5` and the verbatim present; `harvest_datasets` has 78 entries each with the six new fields; `harvest_read_tool_errors` empty; `tool_index` carries `harvest_list` / `harvest_read` only if the census serves them (else the printed `pending` lines).
2. The round-12 instruments against the regenerated catalog (c10.AC1 depth 11 of 11, c10.AC2 routing 7 of 7 with anchors 2 of 2, c10.AC3 answer-time): the research-table routing was tuned by hand in round 12 and the new example questions must not displace it.
3. The gateway suite by failing-ID delta; the known failures are listed (Z-S97, Z-S107).
4. Tighten `test_every_harvest_row_is_reachable_by_its_own_example_question` to `== 78`.

### R13.5 CHOICES THIS CUT MAKES (the issuer's, recorded)

1. **ONE release, not two.** `MX-r-13` was cut for the round-12 catalog and waits behind the gateway queue (now OG-hv-2, OG-ap-18, OG-ap-17). A second release for round 13 would take another
   gateway slot, and the catalog is one file. So `MX-r-13` is amended (A2) to ship the round-13 catalog; its criteria gain a fourth (the round-13 content live) at the PHASE A GO, once its check exists
   and has been dry-run. Round 12 therefore closes after round 13's cells drain; both rounds' orders close at the same `round-close-check`.
2. **read_tool is a function of the deployed census, computed at emit time.** No row names a tool the census does not serve (PRD item 3: "never point a row at an undeployed tool"). The committed rows are generated with
   `--deployed-tools census`; the release re-derives them against the live ref before the GO names the blobs. So a row reads `harvest_read` (or its typed tool) only after OG-hv-2 (or OG-ap-18) has closed.
3. **The generator, not hand-written YAML.** 78 rows of 17 fields each are a transcription of G1; a generator makes the transcription mechanical and checkable, and G2 to G6 reuse it (the build ladder, step 7 only after 2 to 6).
4. **`pending_members.yaml`, not an edit to `members.yaml`.** `members.yaml` refuses an entry for an unserved tool (by design); the harvest tools are entries that wait for the census.
5. **research-dossier (hyphen) is retired only on a measurement** (PRD item 5, "only once the round reads that `research_dossier` supersedes it"): `MX-c-12` item 5 lists both prefixes, read-only, and the check accepts either outcome.
6. **Scope of Andrew's verbatim in the v0.5 header:** only the harvest sentence. The "all of it" sentence about `opal-data-assets` silver is the scope of G2 and is NOT quoted by this round's version.
7. **Retired rows stay in the catalog** (PRD item 5: "rows stay, marked retired") and discover still matches them but never names a tool for them.

### R13.6 WHAT THIS CUT DOES NOT CLAIM

- It does not claim any of the 12 typed tools exists: they are `NFRA_OPLGTW`'s (OG-ap-18). Until each is deployed, a row names `harvest_read` or nothing.
- It does not read a table: every number in a row is G1's, claimed as G1 claims it (a sample of 1 object per JSON dataset stays `measured on 1 object`).
- It does not touch the producers' schedules (G1 open item: unread), nor G2 to G6.
- It does not widen any IAM or served output: the catalog is metadata; the release carries its own never-widen pair as in `MX-r-12` / `MX-r-13`.

## ROUND 14 (2.0.0_SA_COO~MI, 2026-10-14 ~15:0xZ) -- PRD v0.12 + v0.13 FWD-22: the one catalog's TABLE rows for G2 (client assets silver), G4 (mdpf delta), G5 (ETFs) and G6 (news)

Source: PRD v0.12 @95d985d1a5 (`1.0.0_SA_CTO~Z` msg 34100, CONTRACTS-only, ADMITTED) and v0.13 @bb9d1ece12 (msg 34117, G4); the CRO's contracts G2 @339a2804d7 (131), G4 @7ec87a87e5 (7), G5 and G6 @35f45893a7
(36 and 12). Round 13 (G1 harvest) is issued at bc6905342f and running; v0.12 arrived while it was being cut, so it is cut as round 14 now (the CTO's own instruction: "If it is issued, cut them as
round 14 now"). The generator and loader pattern of round 13 is reused; the row schema below is the silver sibling of R13.2.

### R14.1 THE CELLS -- 2 new orders (plus the third on a chain)

| Cell | Serves | What | Base | Risk |
|---|---|---|---|---|
| `MX-c-13` | FWD-22 items 1 and 5, v0.13 | The one catalog writer loads, validates and writes a TABLE-grain silver row (11 new fields, among them `fork_keys` and `contract`), `silver_catalog_row`; its header records that `opal-data-mdpf` gold is a measured mirror of the served platinum; discover answers a table row (fork_keys, contract, retired, tags) and keeps firm-scoped rows fail-closed | after MX-c-11 drains (same worker, same files) | WORLD |
| `MX-c-14` | FWD-22 items 1, 3, 4, 5, v0.13 | `gen_silver_rows.py` + `client_tool_map.json` write the 174 in-scope table rows from G2 (119 of 131), G4 (7 of 7), G5 (36 of 36) and G6 (12 of 12); frozen or empty tables read NOT CURRENT or EMPTY in their meaning; the two do-not-serve G4 feeds are retired | at issuance | LOCAL |
| `MX-r-13` (round 12, A2) | FWD-22 live | The one release ships round 14's catalog too (amendment A3, at the PHASE A GO) | after all build cells drain and the OPLGTW releases close | WORLD |

**Chains (fan-out 2 of 2, cap 8):** chain A = [`MX-c-11` -> `MX-c-13`] on worker `~36` (both edit `emit_catalog_v02.py`, its validator, discover and their tests, so they are one queue); chain B = [`MX-c-14`] on a NEW worker
`0.9.0_WK_NFRA_MCPINDEX~38` (haiku, effort high; a generator, a JSON map and rows: no file in common with chain A or with round 13's `MX-c-12`). `MX-c-14` and `MX-c-12` write different files in the same directory
(`catalog_entries/`): `harvest_*.yaml` against the 174 `opal_data_*`, `dynamodb_*` names; their paths are disjoint by name, and the drain's merge checks it.

### R14.2 THE TABLE ROW (silver sibling of R13.2; the issuer's choice, written once for G2 to G6)

A silver table row (`catalog_entries/<entity>.yaml`, `entity` = the slug of `contract_id`) is the C1 schema (9 fields + `read_tool`) plus `bucket`, `prefix`, `table`, `layer`, `format`, `contract`
(`id`, `size`, `freshness`, `partition`, `producer`: the CRO's own objects verbatim, each carrying its `claim`), `fork_keys` (the contract's firm / account / platform fork, verbatim, with its own claims and its measured last-4
collisions), `nl_tags`, `retired` (+`retired_reason`), `open_items` and `gap_owner`. `firm_scope_rule` is derived: `firm-scoped` when the firm fork names a client firm, else `opal-internal-only`.

Rule 24 record:
- (i) MECE over the declared domain: the domain is the 186 contracts of G2, G4, G5, G6; the subtraction is `set(in-scope contracts) - set(rows)` and its reverse (c14.AC1: base missing 174, extra 0). 12 contracts are OUT of scope because
  an existing `silver_datasets` row already catalogues them (the Schwab dim contracts); they are listed, not dropped.
- (ii) Same grain: one row per contract (table); G3's portal artifacts are NOT in this round (R14.6), so no row in this section mixes grains.
- (iii) Intent coherence: `firm_scope_rule` (who may see the row) is one axis; `read_tool` (which reader) a second; `retired` (is it a tool target) a third; a row's visibility is never derived from its reader.
- (iv) State coherence: `read_tool` null (no reader deployed) is a different state from `retired` true (no reader wanted); a do-not-serve row stays retired when a reader later deploys for its sibling; a client table's `firm-scoped` does not move when its
  `read_tool` appears (discover shows a client row only to opal-internal principals either way, `_silver_answer`).
Word-boundary token census: the six names `table layer format contract nl_tags retired` were censused in R13.2; `fork_keys`, `open_items`, `bucket`, `prefix`, `gap_owner` are keys of the harvest rows (R13) and of no silver reader.

### R14.3 BATTERY (base HEAD a60fffec88 plus the round 14 files; pins G2 339a2804d7, G4 7ec87a87e5, G5/G6 35f45893a7; `deliverables/2.0.0_SA_COO~MI/round14/checks/`)

| check | base | planted arms (clause 1: exercised at the cut) |
|---|---|---|
| c14.AC1 | FAIL: 0 files, missing 174, extra 0 | `plant_c14.sh`: the reference 174 rows PASS; a dropped row, an extra table row, a wrong contract.id: each FAIL |
| c14.AC2 | FAIL: graded 0 of 174 | the reference set PASS; a changed fork_keys block, a flipped firm_scope_rule, a dropped question, cleared open_items, a silent inferred producer, a wrong freshness_field, tools disagreeing with read_tool, a do-not-serve row not retired, a frozen table not marked, a current table marked, a retired table row: each FAIL |
| c14.AC3 | FAIL: the generator is absent | the reference generator PASSES under 5 deployed-tool sets (870 of 870 rows); a generator that names an undeployed tool FAILS |
| c13.AC1 | FAIL at ACCEPT 0 of 174 (the loader refuses every table row); the existing 10 rows load; REFUSE 12 of 12 holds trivially at the base | `plant_c13.sh`: the reference loader PASS (174 accepted, 10 old rows load, 12 refused); a lax table validator FAIL |
| c13.AC2 | FAIL: the three named tests are absent (0 of 3) | the named-test pattern |
| c13.AC3 | FAIL: `silver_catalog_row` absent, the mirror unrecorded | the reference writer and header PASS 5 of 5 |

### R14.4 THE DRAIN (the issuer's acts)

After both chains merge: regenerate the catalog (the emitter), then check: `silver_datasets` holds the 5 old rows + 174 table rows, each table row with its 11 fields and `fork_keys`; `harvest_datasets` 78 (R13.4); `version: 0.5`; header records the mdpf mirror;
every named `read_tool` is served (the emit refuses otherwise); a firm principal gets no match on any `firm-scoped` row (discover, all 174, denominator printed); the round-12 instruments (c10.AC1-AC3) and the full gateway suite by failing-ID delta.

### R14.5 CHOICES THIS CUT MAKES (the issuer's, recorded)

1. **Rows for every contract no existing silver row catalogues (174 of 186).** The 12 G2 Schwab silver contracts map to 4 existing `schwab_dim_*` silver rows and are NOT regenerated (their enrichment is a later cell). The 6 G6 contracts that point at the certified `news` channel text and the portal row are IN scope: the channel text is not a table-grain row, so each table gets its row while the channel keeps its text (its correction is round 15).
2. **`client_tool_map.json`**: G2 proposes 40 vendor-specific tools; OPLGTW v3.1 ruling 1 serves client data as ONE `client_*` set. The map (29 pairs) points each table at the question-shaped tool its question belongs to; a table no question reaches stays unmapped and reads `read_tool: null` ("catalogued but no adapter this round"). The map is data the OPLGTW cells may extend.
3. **No row names a tool the census does not serve** (v0.12 item 5): `read_tool` is a function of the deployed census at emit time; the release re-derives the rows against the live ref.
4. **Client rows are `firm-scoped`, so discover shows them only to an opal-internal principal** (existing rule, `_silver_answer`); a firm principal gets no match even after a `client_*` tool exists, because a `client_*` tool is DATA_GRANT-class (OPLGTW ruling 2) and the catalog row carries no firm field to scope by.
5. **`retired` carries do-not-serve** (v0.13): the two feeds read `retired: true` with `do-not-serve: <G4's routing text>`, one axis (is it a tool target).
6. **Frozen or empty is never current** (v0.12 item 4): a table more than 5 trading days behind T-1 reads `NOT CURRENT: <n> trading days behind T-1.` in its meaning, and an empty table `EMPTY: no objects.`, data-driven from the contract.
7. **The census's measured location is the row's location.** PRD v0.12 item 1 says "live 49F BD rows name `opal-data-bd/silver/`". G2's contracts for 49F BD carry `opal-data-assets/blackdiamond/49f/...` (a one-off partition and a stalled converter, Z-S110) and the live store only in
   prose (`open_items`). No per-table live prefix is in the contracts, so none is invented: the rows carry the measured location and the `open_items`, and the live-prefix enrichment waits for the CRO's per-table prefixes (carried to the CTO, R14.6).

### R14.6 WHAT THIS CUT DOES NOT CLAIM, AND WHAT ROUND 15 CARRIES

- **G3 portal-v2 (42 contracts) and the G6 `news` row corrections are NOT in this round.** The portal channels and the `news` channel are not `catalog_entries/` source rows: they are CVO-certified specs inside the emitter itself (`EMISSION_MAP`, the `ft.04` / `pos.03` twins, the `news` fragment).
  Editing them is a certified-spec change that widens or narrows what a partner firm can read through `catalog_gate`, so it needs its own decomposition and the CVO's read. Round 15 carries: the 9 live uncatalogued datasets; `ft.04.portfolios-aum-metrics` to deny; the `json/mdpf/**` rows dropped; the `portal_lookup` `mdpf`
  channel retired and `mdpf-platinum` corrected; `json-tiered/` stated authenticated-only once Z-S114 closes; the `news` row's sizes (381,261 items) and the frozen / empty markers on the channel text.
- It does not claim any `client_*`, `etfs_*` or `news_*` tool exists: they are `NFRA_OPLGTW`'s. Until each is deployed, a row reads `read_tool: null`.
- It does not read a table: every number is the CRO's, claimed as the CRO claims it.
- It does not settle the 49F live-prefix question (R14.5.7), the SmartX firm fence (Z-S109) or the platform-label crosswalk (OPLGTW ruling 4).

### R14.7 THE CLEAN ROW AND THE FORK REGISTRY (CTO ruling msg 34160, 2026-10-14 ~17:4xZ; supersedes the row of R14.2 where they differ)

**Measured.** The commit-time naming gate (ENFORCE, no override for a REFUSE) refused the reference rows: 273 lines in 113 of 174 rows. The gate reads any whitespace-free string, key or value as a hand-kept carrier when one of its segments (split at `-_/.:=@`) is a firm token
(`49f`, `49financial`, `bd`, `bd49f`, `cot`, `cottonwood`, `inf`, `inflection`, `demo`, `mockadv`) or the whole string is a product token (`etfs`, `harvest`, `irpt`, `mdpf`, ...); a registered legacy address does NOT excuse a carrier. So `bd_account_number`, a prefix with a firm segment and a contract id with one are all refused.
**Ruling (rule 30's own remedy, no gate edit).** (a) `contract.id` is a hash and `contract.label` a readable label without a token; (b) every token-bearing value moves out of the row into `infra/logic/registry/catalog_fork_keys.json` (registry files may carry tokens), keyed by the hashed id; the row keeps the fork's shape; the loader JOINS the entry back;
(c) a `{param}` prefix registers its leading literal (one concrete `legacy_addresses.json` row, no params), a `none` prefix is null, a `silver_legacy` copy is `not_served` with no prefix; (d) the news buckets register as legacy rows only where the registry knows the bucket (two do not; they stay literal in the residual).

**The cells.** `MX-c-14` (A4) regenerates the 174 CLEAN rows and writes both registry files; `MX-c-15` (new, ISSUED AS ROUND 15 because the gate allows one issuance per round and round 14 is issued; worker ~39 from the merged HEAD; the portal and certified-channel round is therefore round 16) changes the loader to accept the clean row and to join the registry entry, and the writer to emit `key_template`. They share no file. `MX-c-13`'s checks (`c13.AC1-AC3`) graded the previous shape and fail on the new loader by design: `c15.AC1-AC2` replace them.
**One builder.** `glib.expected_row(contract, group)` in the round-14 checks builds BOTH the clean row and its registry entry; the reference generator, `c14` (AC1 compares the registry files to it, AC2 compares each row, AC2 scans every string and key of a row for a carrier) and `c15` (it joins and compares with the full row) all use it, so the three agree by construction. Planted arms: `plant_c14.sh` 24 of 24, `plant_c15.sh` 5 of 5.
**Honest limit.** `catalog_tokens.py` (the worker's) reads the token sets the way the gate's `Naming.__init__` does today. If the registry's scopes change, a clean row can turn dirty; `c14.AC2`'s carrier scan uses the check's own copy of the same rule, so a drift between the two shows as a failure, not as a pass.


## ROUND 16 (2.0.0_SA_COO~MI, 2026-10-14 ~21:3xZ) -- the certified-channel corrections and the G5r rival-fund enrichment (CVO READ-OK @2a8a025031 with two conditions; issued 2026-10-15)

Source: R14.6 (what round 14 left to "round 15", now round 16 because MX-c-15 took round 15), PRD v0.14 to v0.16, CTO msg 34192 (landing order) and COO~O msg 34169. Rounds 13 to 15 are drained at `66f8ea1466` (216 table rows, 78 harvest rows). This section is spec-frozen once issued. Per the CTO, the CVO reads it BEFORE issue because cell MX-c-16 edits CVO-certified text inside the emitter.

### R16.1 THE CELLS -- 2 (one issuance, disjoint write sets)

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-16` | The emitter's certified-spec corrections, each a deliberate change of what `catalog_gate` lets a partner firm read: (a) the `json/portfolios/aum-metrics.json` row (twins `att.03`, `ft.04`, `pos.03`: frozen 58 trading days, no PROD page reads it, G3 `portfolios_legacy`) is re-ruled DENY + ruled; (b) the `mp.15.json-mdpf-legacy` row (`json/mdpf/**`, 0 keys at the G3 measurement) is dropped from the catalog (the row only: no object is touched, and `json/mdpf/{firm}/account-distribution.json` stays a live served portal object); (c) the `news` channel text states the measured size (381,261 items, about 1,000 a weekday) and the EMPTY and frozen markers (`opal-harvest-articles` EMPTY; the Seeking Alpha output frozen since 2026-04-13), changing NO gate field. `json-tiered/` stated authenticated-only is HELD until Z-S114 closes (not in this cell). | `workflows/atom_decomposition/emit_catalog_v02.py`, `workflows/atom_decomposition/tests/` | LOCAL | FWD-22 |
| `MX-c-17` | The G5r rival-fund enrichment (PRD v0.16): the 14 rival rows already generated from G5 (13 gold tables and the platinum page of `rivalfunds/etfs/`) gain, from `workflows/atom_decomposition/g5r_enrichment.json` (authored by the issuer from `G5r_rivalfunds_spec.md` @e1b9937129), the newest-part rule, the claim column on the inferred tables, the fund keys, the identifier fill rates, nl_tags, and on the coverage row the Z-S124 note. `gen_silver_rows.py` applies it, so a regeneration keeps it; the round 14 builder `glib.expected_row` applies it too. | `workflows/atom_decomposition/gen_silver_rows.py`, `workflows/atom_decomposition/catalog_entries/` (the 14 rows), `workflows/atom_decomposition/tests/test_gen_silver_rows.py` | LOCAL | FWD-22 |

**Withdrawn from this round: the `mdpf_get_category_views` row and ToolRow (COO~O msg 34169).** A catalog row for it in the portal channel needs a NEW certified entity in `EMISSION_MAP` with its lifted cells (a CVO matter), and the ToolRow is gateway code (NFRA_OPLGTW's lane). The G3 table row for `platinum/mdpf/{scope}/category-views.json` already exists. The question of which route the tool takes goes to `2.0.0_SA_COO~O` as one message.

**Not a cell, and why.** Retiring the `portal_lookup.py` `mdpf` channel and correcting `mdpf-platinum` edits `org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py`, another seat's lane. It goes to that lane's owner as a request with the exact text, after MX-c-16 lands, and is not graded here.

### R16.2 CHAINS AND FAN-OUT

`MX-c-16` and `MX-c-17` share no file and no data: 2 chains of 2, 2 workers (~40, ~41), cap 8. `MX-r-13` (the catalog release) waits on all of rounds 14 to 16 draining and the OPLGTW ledgers closing.

### R16.3 THE CVO'S READ AND ITS TWO CONDITIONS (`deliverables/3.0.0_SA_CVO~Z/R16_MX-c-16_PRE-ISSUE_READ_20261014.md` @2a8a025031: READ-OK)

(a) narrows, (b) turns a refusal by row into a refusal by absence, (c) is text. Conditions, both made mechanical: **`c16.AC2`** is the difference control over EVERY known firm principal (plus opal-internal and two unknown firm ids) x EVERY key of the base catalog, the new catalog and the 16 scope-substituted `json/mdpf/<scope>/<file>` keys, `catalog_gate.gate()` old against new, printing the pair count and `deny->serve=0` beside it; **`c16.AC3`** prints the before and after of `verdict_class`, `allowlist`, `firm` and `firm_resolution` on the news channel and on every `sentiment_news_mood` row and requires every one unchanged and the news channel to keep no artifacts.

### R16.3a BATTERY (base HEAD 0f40810fa2 plus the round 16 files; `deliverables/2.0.0_SA_COO~MI/round16/checks/`)

Base dry-runs: `c16.AC1` FAIL as expected (all five sub-checks), `c16.AC2` PASS as expected (390 of 390 pairs unchanged), `c16.AC3` PASS as expected; `c14.AC2` FAIL as expected on the builder that now applies G5r (rows lack the additions), `c17.AC2` FAIL as expected (0 of 15); `c14.AC3` PASS as expected (a control on the read_tool and tools arms). Planted arms (standing battery clause 1): `plant_c16.py` 9 of 9 (the good catalog passes all three; the base fails AC1; a re-added serving legacy row fails AC2 and AC1; an unrelated deny row served fails AC2; a changed sentiment firm and a news channel with artifacts fail AC3); `plant_c17.py` 4 of 4; `plant_c14.sh` 24 of 24 on the enrichment-aware builder. `c14.AC1` and `c15.AC1-2` still PASS.

### R16.4 WHAT THIS CUT DOES NOT CLAIM

It does not close the gateway ranking question (COO~O's), the `json-tiered/` note (Z-S114) or MX-r-13.


## ROUND 17 (2.0.0_SA_COO~MI, 2026-10-15 ~09:2xZ) -- the rounds 12-16 analysis's enrichment list: T1 (Z-C-S57), F1 (the firm field), R1 (held)

Source: `ledger/ROUND_ANALYSIS.round12-16.md` @5d69fe6298 (CTO msg 34404; PRD stays v0.16), CVO slug REMEDIATION_v10 @c697ce8ae1 (FWD-20 REALIZED, FWD-22 NOT_REALIZED Z-C-S57). Round 16 is drained and served at `1b18b94979` (catalog v0.5, 304 rows). This section is spec-frozen once issued.

### R17.1 THE CELLS -- 3 in this issuance (and one held)

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-18` | T1. Every catalog row carries `nl_tags`. The emitter derives tags for a row whose source gives none (44 of 304: 32 harvest bronze/state rows, 2 draft silver table rows, 10 older hand-kept rows), from the row's own `business_meaning` and `example_questions` by a deterministic module `workflows/atom_decomposition/derive_nl_tags.py`, and marks them `nl_tags_basis: inferred` (a value that carries its claim). A row that already had tags is byte-equal. The two plain-words `opal_discover` reads (one G2 client table, one G6 news table) are the issuer's, after the release. | `workflows/atom_decomposition/emit_catalog_v02.py`, `derive_nl_tags.py`, `validate_catalog_v02.py`, `tests/` | LOCAL | FWD-22 (Z-C-S57) |
| `MX-c-19` | F1. The `firm` field on the 24 firm-scoped table rows whose registry firm value is prose and names exactly one known firm (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`: 23 `49financial`, 1 `inflection`), from the registry join; the gateway discover then shows each such row to its OWN firm's principals and to no other firm. The 25th prose row (the taxsma workbook, three firms) stays Opal-internal. Client data still needs the firm's own data grant. | `workflows/atom_decomposition/gen_silver_rows.py`, `emit_catalog_v02.py`, `catalog_entries/` (the 24 rows), `infra/logic/registry/catalog_fork_keys.json` (the `restore.firm` values), `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, `infra/aws/ec2/opal-gateway/tests/test_firm_catalog_visibility.py`, `tests/` | WORLD (infra path; a per-firm visibility change) | FWD-22 |
| `MX-r-14` | The release of MX-c-18 and MX-c-19: the regenerated catalog and the discover change onto the opal-gateway host, behind the NFRA_OPLGTW queue; both never-widen halves (CTO + COO; the F1 pair names the per-firm visibility change) before PHASE B; the censuses; the depth, partition and catalog reads on the host. | `0.7.0_AE_CloudOps~MI` deliverables, ledger, `EC2_MANIFEST.json` | WORLD | FWD-22 |

**Held: R1** (rival-fund rows are done as `MX-c-17`; what is left is `read_tool` updates for the OPLGTW tools deployed since v0.5, which are NFRA_OPLGTW's `OG-ap-20` (G5 wave A, category views) and `OG-rv-1/2` (the rival-fund tools)). Not cut this tick: its dependency is unmet and held by another project (obligation 2: a cell with an unmet dependency is not cut for coverage). It is cut as an enrichment RECUT when `OG-ap-20` and the rival tools read CLOSED, with its own release order. The round does not reach ROUND_CLOSE while R1 stands open.

### R17.2 CHAINS AND FAN-OUT

`MX-c-18` and `MX-c-19` share no data. They both edit `emit_catalog_v02.py` in different functions (T1 the three row writers and a derive call, F1 the table-field list, its validator and the join), and each adds its OWN new test file, so the merge is hunk-disjoint; the issuer drains them in sequence and regenerates the catalog once on the merged tree. 2 chains of 2, 2 workers (~42, ~43), cap 8. `MX-r-14` waits on both draining and on the OPLGTW gateway queue.

### R17.3 CHOICES THIS CUT MAKES

1. **Tags are derived at EMIT time, not written into the 44 source files.** A regeneration then keeps them, a new row with no tags gets them, and the contract files (the CRO's) stay untouched. The cost: the emitter holds a small derive module.
2. **`nl_tags_basis: inferred` is a field a consumer can reject on** (A VALUE MUST CARRY ITS CLAIM). It is present only on the 44; the rows with contract tags carry no basis field, so a reader can tell contract-given from inferred.
3. **F1 covers the 24 that map to ONE known firm, not 25.** The 25th (`opal_data_assets_silver_gateway_global_taxsma_workbook`) holds rows of three firms, so no single `firm` is true; it stays Opal-internal by design. The other 93 single-clean-value firm-scoped rows also lack the field; widening to them is the CTO's call (a message with this cut).
4. **The `firm` value is a firm token, so the clean row carries `firm: null` and the registry (`catalog_fork_keys.json` `restore.firm`) carries the value;** the loader join restores it exactly as it restores `fork_keys` (MX-c-15). The gateway sees the joined row.
5. **The visibility rule** (`_silver_answer`): a firm-scoped row is shown to a non-internal principal only when the row's `firm` is a known firm AND the principal is a firm principal of that same firm; every other case still refuses. Opal-internal sees all rows as before.
6. **Registry writer.** `infra/logic/registry/**` is lane `PLATFORM_LOGIC_DOCS`: the issuer's lane refuses it. The F1 worker writes `catalog_fork_keys.json` under its order's `<paths>` (the MX-c-14 A8 precedent); the CTO's cut-template line naming `4.0.0_SA_CRO~Z` is satisfied by that order grant, and the CRO is told in the issuance record.

### R17.4 BATTERY (base HEAD cf06cf8c43 = live `1b18b94979` catalog and discover blobs; `deliverables/2.0.0_SA_COO~MI/round17/checks/`)

Base dry-runs 2026-10-15: `t1.AC1` FAIL (260 of 304), `t1.AC2` FAIL, `t1.AC3` FAIL (module absent); `f1.AC1` FAIL, `f1.AC2` FAIL, `f1.AC3` FAIL (no test file); `r14.AC1` FAIL (no ledger entry), `r14.AC4` FAIL (host nl_tags 260, inferred 0, firm 0); `r13.AC2` / `r13.AC3` are graded on the host AFTER the release only. Planted arms (standing battery clause 1): `plant_t1.py` 11 of 11, `plant_f1.py` 8 of 8 (the ac3 PASS arm is not plantable in an extracted tree; the real tree runs that pytest command), `plant_r14_ac4.py` 7 of 7. `f1.AC2` is the visibility difference control: every silver row x {opal-internal, each known firm, an unknown firm, an empty firm}, old tree against new, printing the pair count, the newly-visible count and the cross-firm leak count (0 expected).

### R17.5 WHAT THIS CUT DOES NOT CLAIM

It does not close Z-C-S57: that needs the two plain-words discover reads on the served host after `MX-r-14`, the issuer's own acts at the close. It does not widen any DATA access (F1 changes what a catalog row shows, never a grant), does not cut R1, and does not touch the ranking question.

### R17.3a RULING RECORDED (1.0.0_SA_CTO~Z msg 34407, 2026-10-15 ~09:3xZ), on the F1 scope question
YES: widen F1 to the 93 single-clean-firm firm-scoped table rows, in the NEXT round, as ONE cell with its own never-widen pair naming the per-firm catalog visibility change, after the 24 of MX-c-19 are live and the difference control reads deny->serve 0 across every firm principal x row. The taxsma workbook row (three firms) stays Opal-internal until it is split per firm; no firm is guessed for it. Seeing a row never reads its data (the firm's data grant still gates it). This round's cells are unchanged; the 93-row cell is carried to the next round's enrichment list.

### R17.3b R1 CUT AS `MX-c-20` (2.0.0_SA_COO~MI, 2026-10-15 ~11:3xZ), when NFRA_OPLGTW `OG-ap-20` went live (COO~O msg 34427, release `06cfb6db64`)

R17.1 held R1 for exactly this event. `OG-ap-20` is live and serves six tools the catalog does not know, so R1 is cut now as an enrichment RECUT inside the round: **`MX-c-20`** (worker ~44, `WORLD` by its infra paths, serves FWD-22): the seven table rows those tools read name them as `read_tool` (the generator gains `--tool-reads`, so a tool is a candidate only for the rows its module reads; the unrestricted run would put a false `read_tool` on eight more rows), the six enter the tool index (class b, owner NFRA_OPLGTW, from `pending_members.yaml`), and the emitted catalog covers N=99. It is a prerequisite of `MX-r-14` (the host check `r13.AC2` reads the index against the tools the host serves). Still held: the rival-fund tools (`OG-rv-1/2`, not live). The pipeline gate keys ONE ISSUER PER ROUND, so the order carries `<workstream>R1</workstream>` beside `<round>17</round>` (a workstream is a scope: disjoint write surface, its own order). Chains: `MX-c-20` is independent of the others (a third worker); `MX-r-14` is the tail of all three. Battery: `deliverables/2.0.0_SA_COO~MI/round17/checks/r1.AC1-3.sh` with `plant_r1.py` 9 of 9. The release is cut on `06cfb6db64` itself (COO~O: no separate deploy-only commit), and its MC Portal per-tool link counts become 39 tools / 119 links (from 33 / 112).


## ROUND 18 (2.0.0_SA_COO~MI, 2026-10-15 ~21:3xZ) -- PRD v0.17 CONTRACT C-GROUP, workstream ASSETS: the gateway finish by 2026-10-16 ~22:00Z

Source: PRD v0.17 @532d1e68bb (C-GROUP, Andrew-direct, relayed by the CRO plan `GATEWAY_FINISH_PLAN_EOD_20261016.md` @6cc033c818), the CTO's GO (msg 34551), his rulings on the label-visibility question (msg 34562: labels ship, each release adding known-firm values carries its own never-widen pair at 0 leaks) and the round-17 analysis `ledger/ROUND_ANALYSIS.round17.md` @c7e130a7b2 (msg 34579: round 18 stands as issued; Z-C-S61: curated tags replace the 44 inferred, each workstream for its own files; SmartX stays `firm: multi`). This section is spec-frozen once issued. Round 17 is closed (ROUND_CLOSE, MAY-CLOSE 4 of 4, L8 packet at the CVO). Two workstreams, one project (rule 27): **ASSETS (this seat)** and **RESEARCH (`2.0.0_SA_COO~MI2`)**, disjoint source files; ONE emitter run per catalog release.

### R18.1 THE CELLS -- 3 now (workstream ASSETS) and 2 held

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-21` | C-GROUP item 1, the emitter and the tool index: `bucket` on EVERY catalog row (S3 bucket name or `dynamodb`; the `none (DynamoDB ...)` strings normalised; an older row without one takes the catalog's top-level bucket or the group map's); a repeatable `--group-map FILE` that applies a per-entity `bucket`, `vendor`, `firm` and curated `nl_tags` (dropping `nl_tags_basis`) at emit time, validated against the C-GROUP lists; `bucket` and `source_group {id, name, kind}` on every `tool_index` entry (the bucket of the tool's primary row, else declared in `tool_index/members.yaml` with its `bucket_source` line). One field, one spelling: `source_group.id` IS `bucket`. | `workflows/atom_decomposition/emit_catalog_v02.py`, `validate_catalog_v02.py`, `tool_index/members.yaml`, `tests/` | LOCAL | FWD-22 |
| `MX-c-22` | The `etfs_get_positioning` extension (CRO G5 spec, `GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md` section on existing tool verdicts): optional `fund_ticker` and as_of history from the catalog rows `opal_data_etfs_gold_book` and `opal_data_etfs_gold_holding`; the existing answer byte-equal for an existing input. It ships in NFRA_OPLGTW's remainder release (COO~O msg 34536). | `infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py`, `tests/test_positioning_extension.py` | WORLD (infra path) | FWD-22 |
| `MX-c-23` | ASSETS rows, C-GROUP item 2: `bucket`, `vendor`, `firm` on all 136 opal-data-assets and opal-data-bd rows (the 119 generated, the 5 older hand-kept, the 12 new), from the issuer's data file `round18/assets_group_map.json` through MX-c-21's `--group-map`; the 12 Schwab `dim_*` rows the generator skipped (NFRA_OPLGTW msg 34560); curated plain-words tags for the 7 ASSETS rows that carried inferred tags (Z-C-S61); the registry `labels` list that lets the naming gate admit the vendor and firm strings. Depends on MX-c-21. | `workflows/atom_decomposition/gen_silver_rows.py`, `catalog_entries/` (the 12), `infra/logic/registry/catalog_fork_keys.json`, `tests/` | WORLD (registry and catalog paths) | FWD-22 |
| `MX-c-24` (HELD) | `read_tool` on each ASSETS row as NFRA_OPLGTW's `OG-cl-*` tools go live (workers 103-108). An enrichment recut per landing; not cut for coverage alone. | the same row files | SERVED | FWD-22 |
| `MX-r-15` (cut as the tail) | The round 18 catalog release: ONE emitter run over both workstreams' rows (the two COOs take turns), a fresh never-widen pair naming every row that gained a known `firm` value (about 96 rows), the censuses, the host checks. | CloudOps deliverables, ledger, manifest | WORLD | FWD-22 |

### R18.2 CHAINS AND FAN-OUT

`MX-c-21` -> `MX-c-23` (one chain: the generator/rows cell needs the emitter's `--group-map` merged) and `MX-c-22` (independent): 2 chains, 2 workers (~45 takes MX-c-21 then MX-c-23; ~46 takes MX-c-22), cap 8. RESEARCH's cells are `2.0.0_SA_COO~MI2`'s; the shared contract between the two COOs is MX-c-21's `--group-map` and the C-GROUP lists, so MI2's rows need no emitter change. `MX-r-15` waits on both workstreams.

### R18.3 CHOICES THIS CUT MAKES

1. **Vendor and firm are applied at EMIT time from a data file under `deliverables/`, not written into the 136 source files.** Same reason as F1: the labels are firm and product tokens (the naming gate refuses a hand-kept carrier outside the registry); the data file derives each value by rule from the row's own prefix and registry values and the check re-derives it. The registry `labels` list (top-level, strings only) is what lets the gate admit the strings in the emitted catalog.
2. **A tool's `bucket` is its primary row's bucket**: the `index` row for a member-a tool, else the most frequent bucket of the rows naming it as `read_tool` (ties alphabetical). A tool that reads several buckets (`etfs_get_positioning`, `news_trending_topics`) is grouped under its primary one; its other buckets are not listed. A tool no row names declares `bucket` in `members.yaml` with a `bucket_source` (path:line) in the tool's own code; Microsoft Graph tools declare `graph` (kind `graph`, name "Microsoft 365", COO~MP msg 34525), other non-S3 stores their own name (kind `store`).
3. **The labels widen catalog visibility, by the CTO's ruling (a)**: a known `firm` value on a firm-scoped row shows that row to its own firm (about 96 more rows than today's 24). The widening is not in these cells; it is in the RELEASE, whose never-widen pair (CTO + COO) names the rows. `multi`, `none` and `unresolved` stay invisible to firm principals. `c23.AC3` is the difference control.
4. **SmartX keeps `firm: multi`** for its 6 draft tables (7 `multi` in all with the Tax SMA workbook); its 7 rows that MX-c-19 set to `49financial` keep that value (PRD item 2: the 24 rows keep their values; CTO msg 34579).
5. **The group map has 0 `unresolved` rows today** (136 of 136 resolve by rule); an `unresolved` row would carry that value and be listed in the release record, never guessed.
6. **Sparse worktrees**: workers add `workflows`, `infra/aws/ec2/opal-gateway` and `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census` to their cone, so the emitter reads the real census path (the round 17 workers' catalogs recorded `.scratch/census_src/` paths, a Z-W44 row).

### R18.4 BATTERY (base HEAD c4c106aea1 + `deliverables/2.0.0_SA_COO~MI/round18/checks/`)

Base dry-runs 2026-10-15: `c21.AC1` FAIL, `c21.AC2` FAIL, `c22.AC1` PASS (the byte-equal control passes base-against-base), `c22.AC2` FAIL, `c22.AC3` FAIL (no test file), `c23.AC1` FAIL, `c23.AC2` FAIL, `c23.AC3` FAIL; `c21.AC3` and `c22.AC3`/`c21` suites run in the worker's tree. Planted arms (standing clause 1): `plant_r18.py` 20 of 20 (a good catalog passes c21.AC1-2 and c23.AC1-2; a row without bucket, a `none (DynamoDB ...)` string, a moved S3 bucket, a tool bucket that differs from its rows, a source_group whose id or kind is wrong, a wrong vendor, a stray vendor, a row still inferred, an empty registry labels list, 11 new rows, an extra row, a wrong gap owner each fail the criterion that grades them; a good tree passes c23.AC3 and a leaking discover rule fails it), `plant_c22.py` 6 of 6.

### R18.5 WHAT THIS CUT DOES NOT CLAIM

It does not link `read_tool` for the `OG-cl-*` tools (MX-c-24, event-gated), does not cut RESEARCH's rows or tags (`2.0.0_SA_COO~MI2`), does not release (MX-r-15 is the tail), and does not change discover ranking (row Z-S121). The "done by 2026-10-16 ~22:00Z" line needs every in-scope row to carry C-GROUP and a live `read_tool`; the second half depends on NFRA_OPLGTW's landings.

## ROUND 19 (2.0.0_SA_COO~MI, 2026-10-16 ~14:1xZ) -- the round-18 L10 answer's enrichments: the discover echo (E1), the gold book line (E2), the four live 49F rows (E3)

Source: the CTO's L10 answer, msg 35012 (@a0eb7cd450: the C-GROUP line reads met 280 of 280; the CVO's carried items 1 to 6 and the gold book `open_items` are the issuer's round-19 enrichments), msg 35019 (@667ad29169, the 49F adapter is built), msg 35025 (@ed33f552ae: an `address` field, rule (a)) and msg 35038 (@96ea4ac3da: four NEW live rows, rewrite in place refused). CVO slug `surprise-channel/adjudications/ADJUDICATION_v13.md` @c5ba2988f4. Round 18 is drained and served at `38fe44d5cb` (catalog blob `16250301d6`). This section is spec-frozen once issued.

### R19.1 THE CELLS -- 3 in this issuance (and one held)

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-24` | E1. `opal_discover` echoes `bucket` on every silver answer whose row has one, and `vendor` and `firm` where the row has them (today `bucket` only on a row carrying `contract`, so the opal-data-bd match echoes none, and no match echoes vendor or firm). Nothing else in any answer changes. | `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, `infra/aws/ec2/opal-gateway/tests/test_discover_echo.py` | WORLD (infra path) | FWD-22 (PRD v0.17 C-GROUP, "asked in plain words") |
| `MX-c-25` | E2. The gold book catalog entry drops its stale `open_items` line ("gateway role: GetObject on gold/book simulates implicitDeny"); a live gateway answer read gold/book at 2026-10-16 10:36Z and the OG-ap-20 grant names gold/book/* (MX-c-22 ruling, Z-W46-S1). Direct-act, one line. | `workflows/atom_decomposition/catalog_entries/opal_data_etfs_gold_book.yaml` | LOCAL | FWD-22 |
| `MX-c-26` | E3. The four live opal-data-bd 49F tables as four NEW catalog rows (unrealized, transactions, allocations, fees): bucket opal-data-bd, prefix `silver/<t>/`, table `<t>`, an `address` (`blackdiamond/49f-live/silver/<t>/`), `read_tool` the mapped client tool, freshness measured on the live table. The eight FROZEN-copy rows go back to `opal-data-assets` at their real prefix and stay OUT. The `address` field is an optional TABLE-row field in the emitter and the validator. | `workflows/atom_decomposition/catalog_entries/` (the four new files and the eight legacy ones), `emit_catalog_v02.py`, `validate_catalog_v02.py`, `gen_silver_rows.py`, `tests/test_address_field.py`, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json`, `.../round19/live_bd_group_map.json` | LOCAL | FWD-22 (CTO msgs 35025, 35038) |
| `MX-r-16` (held) | The release of MX-c-24, -25, -26 as ONE batched release with NFRA_OPLGTW's `OG-en-11` code (the `address` match in `Ctx.prefix`, the flat-file partitions) and the dedicated `-live` read role (row Z-S292, three never-widen halves). Cut when those are served; the issuer re-emits the catalog once (`emit_final.sh`) at that point. | `0.7.0_AE_CloudOps~MI` deliverables, ledger, `EC2_MANIFEST.json` | WORLD | FWD-22 |

**Not a cell: E4, the depth-claim grading (CTO msg 35012: "stop pinning depth claims that age with each publish").** It is the issuer's own instrument (`round12/checks/c12_depth.py`, graded by `r13.AC3`), amended by the issuer in this tick, never by a worker. The tolerance is chosen by `C12_TOLERANCE` and every grade prints the one it used: `strict` (the DEFAULT, unchanged: used by `emit_final.sh` on a candidate within minutes of the measure, where a claim wrong when measured is caught), `one-publish`, and `monotone` (a POST-release grade of a shipped catalog: a measured claim is a point-in-time fact and a source only moves forward, so a claim BEHIND the served value is stale but was true when measured, while a claim AHEAD of it fails in every mode). Both counts are printed (equal / tolerated). Negative control: `python c12_depth.py selftest`, 11 of 11 (two publishes behind fails under one-publish, a claim ahead fails under monotone, strict tolerates nothing). Measured 2026-10-16 ~14:5xZ against live AWS: the shipped v3 catalog (blob `16250301d6`, which passed strict 11 of 11 at 12:24Z) now reads strict 7 of 11 and monotone 11 of 11 (8 claims behind the served value: the ETF positioning object caught up from 2026-10-13 to 2026-10-15 in one publish, so even `one-publish` would not cover it); the rollback catalog v2 (`4c27b28171`) reads strict 6 of 11 and monotone 11 of 11. At answer time the gateway returns the LIVE value (answer-time monotone 17 of 17; strict 14 of 17, the three BAD rows show the answered value ahead of the catalog's), so what a person is told is current; only the catalog's own copy ages. `r13.AC3` after a release is graded `monotone`; the release candidate stays `strict`.

### R19.2 CHAINS AND FAN-OUT

The three cells share no data and no file: `MX-c-24` writes the gateway tree, `MX-c-25` one entry file, `MX-c-26` the other entry files, the emitter and the two group maps. 3 chains of 1, 3 workers (~47, ~48, ~49), cap 8. `MX-r-16` waits on all three draining and on the NFRA_OPLGTW queue.

### R19.3 CHOICES THIS CUT MAKES

1. **E1 adds fields, removes none.** The difference control (c24.AC2) compares every silver row x four principals against the live tree `38fe44d5cb` and requires every base key byte-equal and only `bucket`, `vendor`, `firm` added. Visibility is untouched, so the echo widens nothing.
2. **E3 follows the CTO's ratified REC, not the first ruling.** The first ruling (35025) keyed the existing rows; the measurement that the four legacy rows DESCRIBE the frozen copy (opal-data-assets `blackdiamond/49financial/silver_legacy/<t>/`, newest 2026-08-24, "FROZEN copy: do not build a tool on this prefix") while the live bd tables are current (fees 2026-10-14) led to msg 35038: four new rows, the eight legacy rows re-bucketed, rewrite in place refused.
3. **The live tables are flat files** (`silver/fees/2026-10-14.parquet`), unlike the frozen copy's `date=<d>/` partitions. That is the adapter's side (told to `2.0.0_SA_COO~O`, msg to OG-en-11); the catalog row states the truth (partition keys: the file name date).
4. **No registry row is added** for the four new contracts: a clean table row with no `catalog_fork_keys.json` entry is returned unchanged by the join, so `fork_keys` carries the shape with null values.
5. **E4 is the issuer's instrument edit** (above): the default stays strict so nothing that was graded before changes meaning; the post-release grade names its tolerance on its own output line.

### R19.4 BATTERY (base HEAD 0afc0f3a19 plus the round 19 files; `deliverables/2.0.0_SA_COO~MI/round19/checks/`)

Base dry-runs 2026-10-16 ~14:0xZ: `c24.AC1` FAIL (192 of 197 buckets echoed, 0 of 136 vendor, 0 of 136 firm, probe 7 of 8), `c24.AC2` FAIL (no answer gains a key), `c24.AC3` FAIL (no test file); `c25.AC1` FAIL (the stale item is still there), `c25.AC2` PASS as expected (the entry validates at base); `c26.AC1` FAIL (0 of 4 live rows), `c26.AC2` FAIL (8 legacy rows not in opal-data-assets), `c26.AC3` FAIL (no `address` field, no test file).

### R19.5 WHAT THIS CUT DOES NOT CLAIM

It does not make the four 49F client tools serve: that is NFRA_OPLGTW's `OG-en-11` (address match, flat-file partitions) and the dedicated `-live` read role (Z-S292), after which `OG-en-11` is re-run on the served host. It does not change any grant, role or route, and it does not release anything: `MX-r-16` is cut when the dependencies are served.

### R19.6 ADDENDUM (2.0.0_SA_COO~MI, 2026-10-16 ~16:1xZ): `MX-r-16` is retired as a separate release; the catalog placement is step 4 of `MX-c-26` (A5)

The three build cells drained (`MX-c-24` `1ee9069f8c`, `MX-c-25` `7309ccc274`, `MX-c-26` `98ce7eb4e7`, `a608e7bc84`, `d1092a10f6`). The gateway release `NFRA_OPLGTW.TO-OG-ap-28` (staged, `40c539b06d`) is the CTO's ONE batched release (msgs 35030, 35038): it takes `app/refs/DATA_CATALOG.yaml` from trunk and fires its Phase A GO when the four live rows are in it. This project therefore does not deploy, and the held cell `MX-r-16` of R19.1 is **retired**. What is left is the catalog landing on trunk, which only a worker may commit (lane `CLOUD_OPS_OR_ETL`); the L6 gate refuses a second order file in a round, so it is amendment A5 of `MX-c-26` (same slot ~49): place the issuer's candidate (md5 `760e40683e32aa2e429f2137b628287a`, graded by the issuer at ~15:4xZ: `r16.AC1`, `r16.AC2`, `c23.AC4`, `c21.AC2`, `r13.AC3` strict, all PASS), with three added criteria `r16.AC1` (the candidate against the live v3 catalog: +4 rows, the eight legacy rows differ in bucket/prefix/key_template only, 272 rows byte-equal), `r16.AC2` (the visibility matrix: the four rows reach opal-internal and the 49financial principal only, leaks 0) and `r13.AC3` run `monotone`. The issuer's COO half of the never-widen ask in `OG-ap-28` names those four newly visible rows; the host-side one real run (visibility matrix on the host, discover 8 of 8 buckets, `r13.AC2`/`AC3` monotone) is the issuer's after `OG-ap-28` lands.

## ROUND 20 (2.0.0_SA_COO~MI, 2026-10-16 ~19:1xZ) -- the round-19 analysis's enrichment list: R20-1 (BLOCKING), R20-2, and R20-3 (not this project's)

Source: `ledger/ROUND_ANALYSIS.round19.md` @9b905362bc (CTO msg 35181; CVO slug `surprise-channel/adjudications/ADJUDICATION_v15.md` @04531c14fe, msg 35180). Round 19 is drained and served: `NFRA_OPLGTW.TO-OG-ap-28` is live at `bf9d23b518` (ledger closed, `ap28.AC2` PASS, msg 35185), the host serves the release catalog at blob `b81c48aa3c` and the four 49F tools answered rows. This section is spec-frozen once issued.

### R20.1 THE CELLS -- 2 in this issuance

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-27` (R20-1, BLOCKING before any regeneration) | A regeneration by `gen_silver_rows.py` loses no hand-set field and no registry row it does not own. MEASURED on trunk 2026-10-16 ~19:0xZ (a dry run into temp folders with the exact inputs of `land_links.sh` and both registry flags): the four `blackdiamond_live_<t>` entries are NOT touched (hand-kept; `address` is safe there), but the generator (a) rewrites the `prefix` of the eight 49financial `*_silver_legacy` entries and the `open_items` of the gold book entry (MX-c-25), losing the hand corrections of MX-c-26 and MX-c-25; (b) with the registry flag drops 34 rows of `catalog_fork_keys.json` and reverts the `restore.bucket` of eight (the emit is refused again); (c) drops a hand-set `address` planted on a generated entry. The cell: a tracked `hand_overlay.json` the generator applies last by default, the carry-over of keys the generator does not own, and a merge (not a replace) of the fork registry. | `workflows/atom_decomposition/gen_silver_rows.py`, `workflows/atom_decomposition/hand_overlay.json` (new), `workflows/atom_decomposition/tests/test_regen_preserves.py` | LOCAL | FWD-22 (the catalog stays regenerable) |
| `MX-c-28` (R20-2) | After release a measured depth claim is a FLOOR with its `measured_at`: `load_tool_index` adds `depth_kind: floor` and `measured_at` (= the claim's `read_at`) to every `measured` history_depth claim (and each per-link element); `validate_claim` accepts and checks them; freshness, inferred and absent claims do not carry them; the emitter stays strict (r13.AC3 strict at emit is unchanged). | `workflows/atom_decomposition/emit_catalog_v02.py`, `workflows/atom_decomposition/tests/test_depth_floor.py` | LOCAL | FWD-20 (depth claims, PRD v0.9/v0.10) |
| R20-3 (not cut here) | `MX-c-24` (the `opal_discover` echo, complete on trunk, six lines) rides the NEXT batched gateway release under `2.0.0_SA_COO~O`, named in that release's ask (CTO msg 35182). The catalog carrying R20-2's new claim keys is a catalog change and rides the same release; the issuer emits and places it after `MX-c-27` is on trunk. | `NFRA_OPLGTW` release | SERVED | FWD-22 / FWD-20 |

### R20.2 CHAINS AND FAN-OUT

`MX-c-27` writes the generator, one new JSON file and one new test file; `MX-c-28` writes the emitter and one new test file. Disjoint files, no edge: 2 chains of 1, 2 workers (~50, ~51), cap 8.

### R20.3 CHOICES THIS CUT MAKES

1. **The CTO named `address`; the measurement widens the cell.** `address` survives on the four live entries because the generator never writes them. What a regeneration actually loses is two hand corrections on GENERATED entries (the legacy prefixes, the gold book line) and the fork-registry rows, so the cell carries those too; the CTO's test (regenerate, diff the 49F rows, expect 0 lost) is `c27.AC1`.
2. **An explicit overlay file, not an implicit memory.** `hand_overlay.json` lists every hand-set value (entity, field, value) and is applied last; the carry-over rule (a key present in an existing entry file that the generator does not own is kept, so a hand-set `address` survives) covers the rest. Both are graded by `c27.AC1`.
3. **The registry file is merged, not rewritten:** rows for the contracts the generator generates are rewritten, every other row stays byte-equal and in order, the other top-level keys stay. The eight legacy contracts' `restore.bucket` and `key_template` come from the overlay.
4. **No catalog regeneration is emitted or landed until `MX-c-27` is on trunk** (the CTO's BLOCKING). The catalog is emitted from the entries by `emit_catalog_v02.py` (not by the generator), so `MX-c-28` does not need it, but the release catalog is emitted only after `MX-c-27`.

### R20.4 BATTERY (base HEAD 37d1b8dd9b; `deliverables/2.0.0_SA_COO~MI/round20/checks/`)

Run in a SPARSE worktree cut with `workflows lib .tools infra/aws/ec2 infra/logic` plus the project folder (the lesson of round 19): `c27.AC1` FAIL (9 entries differ; the planted address is lost), `c27.AC2` FAIL (34 fork rows lost, 8 changed; the legacy-address file loses nothing it does not own and the CRO's four alias rows are among those), `c27.AC3` FAIL (no test file); `c28.AC1` FAIL (no test file), `c28.AC2` FAIL (0 of 39 measured claims carry the keys).

### R20.5 WHAT THIS CUT DOES NOT CLAIM

It does not ship anything: the discover echo and the new claim keys reach the host only in `2.0.0_SA_COO~O`'s next batched release. It does not regenerate or change a catalog row.

## ROUND 21 (2.0.0_SA_COO~MI, 2026-10-16 ~20:2xZ) -- the round-20 analysis's enrichment list: R21-1 (a regeneration guard) and R21-2 (two depth kinds)

Source: `ledger/ROUND_ANALYSIS.round20.md` @3f03a45f83 (CTO msg 35237), on the CVO slug `surprise-channel/adjudications/ADJUDICATION_v16.md` @b0966935f7 (msg 35236). Round 20 is drained: MX-c-27 (`f5e5872dd4`) and MX-c-28 (`614a633c9a`) complete. The CTO accepted the CVO's correction: a series-START claim is a CEILING (a later served start is a truncation and FAILS), a latest-date claim is a floor. The catalog emit stays held until R21-1 lands. This section is spec-frozen once issued.

### R21.1 THE CELLS -- 2 in this issuance

| cell | what | write set | risk | serves |
|---|---|---|---|---|
| `MX-c-29` (R21-1) | `gen_silver_rows.py` REFUSES (exit 2, nothing written to either registry file, one `REGISTRY-DROP <file> <row id>` line per row) when a registry write would remove a row that existed before; the issuer's `--allow-registry-drop FILE` (a JSON list of row ids) is the only way to accept a drop. Measured at the base: a regeneration with `--registry-file` drops 36 of the 143 `catalog-*` rows of `legacy_addresses.json` silently. | `workflows/atom_decomposition/gen_silver_rows.py`, `workflows/atom_decomposition/tests/test_registry_drop_guard.py` | LOCAL | FWD-22 (the catalog stays regenerable, the naming gate keeps its held strings) |
| `MX-c-39` (R21-2) | Two depth kinds on every measured history_depth claim: `latest` (a floor) and `series_start` (a ceiling), DECLARED on the member spec in `members.yaml` (`depth_kind: series_start` on the six series-start specs) and matched by (row, field) in the emitter; the old value `floor` is refused; the grader (`round12/checks/c12_depth.py`, the issuer's, done) tolerates only an EARLIER served start for a series_start claim. | `workflows/atom_decomposition/emit_catalog_v02.py`, `tool_index/members.yaml`, `tool_index/pending_members.yaml`, `tests/test_depth_kinds.py`, `tests/test_depth_floor.py` | LOCAL | FWD-20 (depth claims) |

### R21.2 CHAINS AND FAN-OUT

Disjoint write sets, no edge: 2 chains of 1, workers ~52 (MX-c-29) and ~53 (MX-c-39), cap 8. R21-3-equivalent (the release): `2.0.0_SA_COO~O`'s next batched gateway release takes MX-c-24, and the catalog the issuer emits fresh at that cut (floor-keys become kind-keys), after both cells are on trunk.

### R21.3 CHOICES THIS CUT MAKES

1. **The kind is declared, not inferred.** MX-c-28 wrote `floor` on all 39 claims, including the six series starts: my defect, caught by the CVO. The emitter reads the kind from the member spec; the grader falls back to the two series-start field names only for a claim that carries no kind, and never tolerates a series start upward.
2. **The guard is in the generator, which writes the registry,** not in the emitter, which only reads it. The allow file is the issuer's explicit statement of an accepted drop.
3. **No re-measure is needed** for R21-2 (the kind comes from `members.yaml`); the catalog is emitted fresh at the release cut anyway.

### R21.4 BATTERY (base HEAD ff13c436b1; `deliverables/2.0.0_SA_COO~MI/round21/checks/`, run in a SPARSE worktree cut like the workers')

`c29.AC1` FAIL (the option does not exist; 36 rows are dropped silently), `c29.AC2` FAIL, `c29.AC3` FAIL (no test file); `c39.AC1` FAIL (no test file), `c39.AC2` FAIL (0 of 39 claims carry a kind; 39 still read `floor`; the six-claim anchor reads 0).

### R21.5 WHAT THIS CUT DOES NOT CLAIM

It ships nothing and lands no catalog. The depth kinds reach the host only with the next batched gateway release; the guard protects the next regeneration.
