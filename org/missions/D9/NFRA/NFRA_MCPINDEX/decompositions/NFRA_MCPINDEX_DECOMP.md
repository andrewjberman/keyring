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
