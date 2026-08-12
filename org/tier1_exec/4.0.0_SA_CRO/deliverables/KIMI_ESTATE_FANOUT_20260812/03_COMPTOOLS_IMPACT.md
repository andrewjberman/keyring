# FANOUT 03 — comp-tools impact census (verbatim agent report, received 2026-08-12 ~20:35Z)

**Agent scope:** which tools break under the restructure (C4 dissolve / C3.ii inferential /
annotation layer / Subject axis), which are unaffected, what new capability is needed. **Evidence
class: agent-derived; the §1e crash was GROUND-CHECKED at the CRO seat (reproduced rc=1, control
rc=0) and FIXED same hour — SYSTEM_DEFINITIONS v2.1 is now all-ASCII, Subject/Function rc=0. The
code-side guard gap at `opal_estate_infrastructure.py:573` remains and routes to the tool lane.**

---

### Denominators (derived, not quoted)

| Denominator | Value | Source |
|---|---|---|
| `.tools/comp-*` glob entries | 97 | `ls` |
| …excluding `.py`/`.sh` helper siblings | 90 | `ls \| grep -v` |
| **Tracked+committed comp-* executables (gate-maintained)** | **90** | `comp-manifest-check completeness` → `registration-invariant PASS: 90 … (tools_index 76 + excluded 13 + entries-tools 78) … coverage-map 93` |
| **Registered / routable** | **76** | same run, final line |
| `comp-estate` argparse surface | 23 (22 flags + 1 positional) | `opal_estate_infrastructure.py:818-862` |
| comp-estate live key-scan roots | **4** (`data`, `infra/aws`, `org/modules`, `portal/scripts`) | `:90` |
| Resolver population | 29 `named_threads`, 138 `threads` | `estate-coverage-resolver.json` |

**Tools that read an ontology registry: 12 of 76 routable (16%).** All others structurally unaffected.

## 1. comp-estate — the only tool with C4/C3.ii awareness

Engine `org\modules\graph\opal_estate_infrastructure.py` (996 ln); legacy delegate
`org\modules\graph\estate_infrastructure_cli.py` (896 ln); shim `.tools\comp-estate`.

| Mode | Reads `c4_segments`? | Reads C3.ii verticals? | Reads resolver snapshot? | Verdict |
|---|---|---|---|---|
| `--segments` :644-686 | **YES** — `d["c4_segments"]` :660 | prints `verticals_served` :675 | no | **BREAKS** |
| `--matrix` :579-641 | no | **YES** :613-616, :634 | **YES** :590 | **BREAKS** |
| `--structure SYS` :689-730 | no | **YES** :718-720 | **YES** | **BREAKS** |
| bare / `--list` :916-918, :951 | no | **YES** — `threads_of()` :330-343 | **YES** | **BREAKS** |
| `<vertical>` traversal :932-950 | no | **YES** (`estate_infrastructure_cli.py:292`) | **YES** | **BREAKS** |
| `--layers` :493-518 | serves the *doc* verbatim | serves the *doc* verbatim | no | **BREAKS (content, not code)** |
| `--definitions` :521-576 | no (reads SYSTEM_DEFINITIONS :530) | no | no | **WAS BROKEN — fixed at CRO seat (see header)** |
| `--debt` / `--tool` / `--fe-reachability` / `--validate` / `--gate-b` | no | keyed on `named_thread` | **YES** | breaks only if vertical *names* churn |
| `--resource` / `--drift` / `--keys` / `--verify-served` / `--refresh` | no | no | naming only | **UNAFFECTED by C4/C3.ii** |
| `--census-drift` :733-794 | no | reads `lambda_to_named_thread` :750 | no (frozen taxonomy) | breaks if vertical names churn |
| `--head`, `--plane`, `--orphans-only`, `--self-test` | no | no | — | unaffected |

### 1a. `--segments` — the precise break, and it is a *silent* one

`:660` `segs = d["c4_segments"]` inside try/except that fails loud at :661-664 — deleting/renaming
the KEY → rc=2, loud. But the printer at :669-679 reads every field with defaulting `.get()`:
```python
body(f"  structures: {', '.join(v.get('registry', []))}")      # :672
body(f"  verticals: {', '.join(v.get('verticals_served', []))}")# :675
desc = " ".join(str(v.get("high_signal", "")).split())          # :676
```
**If `c4_segments` is RESHAPED rather than removed**, the tool emits blank lines at rc=0 — a
silent-degrade. (Source-confirmed; not exercised with a mutated catalog.)

Also: `:681` prints `denominator: {len(segs)} segments` — the catalog's own `non_summable_rule`
(`NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:483-492`) states per-segment membership overstates by 31% and
denominators must resolve against the grid. **The tool prints the forbidden denominator today.**
`:682-685` prints the ladder-rung claim the restructure dissolves; same text duplicated in
`cmd_matrix` :638-640 and `cmd_structure` :727-729.

### 1b. The Subject×Function grid is DECLARED and has ZERO readers — MEASURED

`c4_subject_function_grid` (RATIFIED 2026-08-12, catalog :392-492): repo-wide ripgrep over
`*.{py,sh,js,ts,json,md,yaml,yml}` → hits in exactly **two files** — the catalog itself and
SYSTEM_DEFINITIONS `authority:` pointers. **No code reads it.** Serving the grid is *new capability*,
not a modification of `--segments`.

### 1c. Live name drift already shipped — MEASURED both sides

| Surface | Name |
|---|---|
| `comp-estate --segments` live output | `estate-infrastructure` |
| `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:560` (the `c4_segments` KEY) | `estate-infrastructure` |
| `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:460` (`segment_definitions`) | `andrew-infrastructure` |
| `SYSTEM_DEFINITIONS.yaml` term `Segment` | `andrew-infrastructure` |

One file carries both names in two sections; the tool serves the old one. Nothing detects this (§1f).

### 1d. `--layers` serves a doc the restructure falsifies, with no drift check

`cmd_layers` :497-500 prints `infra\system\ontology\C0_C1_C2_C3_C4_SYSTEM_LAYERS.md` (164 ln)
verbatim. That file asserts: `:25` `C4 SEGMENTS 5 LEGISLATED, never discovered` · `:122-124`
verticals as C3.ii derived view · `:131` `C3.ii + C4: DECLARED, never discovered` · `:142/:144` the
change-authority table. R1/R2 make all four false. `cmd_layers` is the file's only programmatic
reader; no checker compares it to the catalog — wrong output, nothing fires.

### 1e. `--definitions` crashed on the two new ratified terms — MEASURED live, now fixed

`comp-estate --definitions Subject|Function` → rc=1 UnicodeEncodeError (U+26D4 via bare print at
`:573` on cp1252); control `Vertical` rc=0; bare `--definitions` escaped via `[:90]` truncation.
**Data-side fixed at the CRO seat 2026-08-12 (registry now all-ASCII; Subject/Function rc=0).**
Code-side hardening (the try/except guard `cmd_layers` already has at :505-514) still absent at
`:573` — routes to the tool lane.

### 1f. Nothing validates an `authority:` pointer — MEASURED

`check_system_definitions.py:31` — presence only; the anchor is never resolved. Exercised: 68/68
clean with a dangling anchor and the name split live.

## 2. comp-kuzu — PURE PASSTHROUGH, unaffected

Shim → `infra/aws/globgrph/kuzu_cli.py`. Ripgrep `segment|vertical|c4_|C4|named_thread|c3_` → **0
matches** (positive controls fired: `node_type` 7 in kuzu_nessie_load.py; `comp-kuzu` 20 in
comp-which). **No C4 node type exists in the graph** — `C2Motif` (19) and `C3System` (4) only,
`FROZEN_CONTROL` at `c2c3_liveness_acceptance.py:54`, loaded from static files COPY'd at
`Dockerfile:79`. Schema is two tables (`CloudNode`/`CloudEdge`); only freeform slot is `props STRING`.
Cypher is schema-agnostic; a Subject property or annotation node would be additive — but the graph is
not currently a C4 read path, so it cannot be the restructure's read path without new load code.

## 3. comp-which — ZERO segment/vertical vocabulary in routing

`.tools\comp-which` (167 KB): `grep -in "segment\|vertical"` → **0 lines** (controls: `comp-kuzu` 20,
`comp-estate` 17). Curated rules route on artifact shape (S3 key, lambda name, gold-script id, portal
component) — never on a segment or vertical name. Manifest-fuzzy backstop over
`graph-call-manifest.yaml` + `comp-coverage-map.yaml` (`comp-which:47`). **UNAFFECTED as written** —
a user typing a segment/Subject name today gets no route; pre-existing coverage gap, not a break.

## 4. The HUD hook — routes on file shape, not ontology

`.tools\hooks\comp-tool-hud.sh` (333 ln): `vertical` 0 · `c4` 0 · `segment` 2 (both shell-command
segments, unrelated). `comp-estate` appears only in advisory nudge text keyed on S3-key /
gold-script-id / portal-component / lambda-name patterns. **UNAFFECTED.**

## 5. The resolver / manifest chain — where C3.ii actually lives

```
estate-coverage-manifest.yaml (1208 ln, HAND-AUTHORED)
        +  org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/estate_census/  (FROZEN)
                    |  gen-estate-resolver.py
                    v
estate-coverage-resolver.json   (29 named_threads / 138 threads)
```

- Manifest: exactly ONE programmatic reader (`gen-estate-resolver.py:21,26`).
- Resolver: 7 readers + 1 writer — `opal_estate_infrastructure.py:82`,
  `estate_infrastructure_cli.py:54`, `pipeline_cli.py:1345` (comp-pipescript),
  `comp_legacywriter.py:197`, `.tools\freshness_manifest_gen.py:51`,
  `estate_report_runner.py:860`, + three CRO scripts.
- Thread schema: `thread_id, named_thread, family, owning_tool, status, reachability_status, reason,
  debtscan_flags, description, producers, served_artifacts, frontend_resolution`. **No subject field.
  No segment field. No vertical-level ratification state** — `named_threads` is a bare 29-string list.

### 5a. `--refresh` REGRESSES the vintage it exists to fix — SOURCE-CONFIRMED

`gen-estate-resolver.py:100-104` writes `last_review: "2026-06-15"` as a **string literal** and
full-overwrites. On-disk resolver carries `last_review = "2026-07-30"` plus a hand-appended
`generated_from` clause that appears nowhere in the generator — the committed snapshot was hand-edited
after generation. Consequence: `--refresh` rewrites 2026-07-30 → 2026-06-15 (58 days as of today),
instantly tripping the >14d STALE banner, and discards the hand-added provenance. **The prescribed
remedy for staleness makes the tool report itself more stale.** Also: `--refresh` re-joins a FROZEN
census (path pinned to `logs/2026-06-15/estate_census`) — not a re-measurement. A Subject seed map
has no seat in this chain.

### 5b. The staleness fuse — exact arithmetic

`STALE_AFTER_DAYS = 14` (`:86`); `last_review 2026-07-30` + today 2026-08-12 → days = 13, stale =
False, **trips 2026-08-14** (matches the standing AUG-13/14 memory trigger). Scopes NAMES only. A
**second independent hardcoded copy**: `comp_legacywriter.py:198` `_SNAPSHOT_MAX_AGE_DAYS = 14` with
its own reader :209-224. Two tools, two literals, no shared constant.

### 5c. PC-001/002/003 — the mechanism, located

`emit_header` (:136-151) prints naming source + last_review + age + "KEY SOURCE: LIVE re-derivation" +
4 scanned roots. **No warranted list** — scopes FRESHNESS only, exactly as CLAUDE.md states.
Served-name mechanism behind PC-003: `gen-estate-resolver.py:78` — manifest override *else* frozen
2026-06-15 census prose. Only S3 oracle is `--verify-served` (head-object per key); without it every
verdict prints `S3 NOT VERIFIED (repo-text claim…)` (:401). A render-time poison-phrase rewriter
(`estate_infrastructure_cli.py:199-208`) catches one literal phrase, not wrong names.

### 5d. Two hardcoded rosters that drift under inferential verticals

- `gen-estate-resolver.py:94-98` `CATALOG_ORDER` — hand-drawn 25-name list; still contains
  `attribution` (RETIRED 2026-07-30), missing `etf-reports`/`ceo-digest`/`ticketing` (admitted same
  day). New names fall to the sorted tail (:99).
- `.tools\freshness_manifest_gen.py:72` — hardcoded pipeline→named_thread map;
  `estate_report_runner.py:660-661` joins on producers[] leading token. **Both joins break on a
  named_thread rename, silently** (runner degrades to UNRESOLVED by design :653-656).

## 6. Other ontology-registry readers — all read the RULE BANK, none read C4/C3.ii

8 direct readers, none touching `c4_segments` or `c3_ii_semantic_verticals`: `comp_ontolint.py`
(:39,:188,:248 — relations/roles) · `comp_output_contract.py` (:40,:400-404 — canonical_source vocab)
· `comp_system.py` (:410,:442-444,:852 — counts) · `comp_legacywriter.py` (:761,:1425 — lifecycle
vocab) · `manifest_check_cli.py` (:1024,:1040,:1051-1060 — fail-closed BLOCK via output_contract) ·
`.tools\c3-walk-agenda.py` (:44,:62-76 — lifecycle enum BY REGEX, below) ·
`.tools\contract_declare_lint.py` (:63,:74,:77) · `archetype_census.py` (:19-20). Transitive via
comp_output_contract: comp_dataflow, comp_keys, comp_log_auto, comp_msbeff_rebaseline, routes_cli.

### 6a. `c3-walk-agenda.py` resolves the lifecycle enum by FIRST-MATCH regex

`:76` `re.search(r"^\s*enum:\s*\[([^\]]+)\]", text, re.M)` — returns the FIRST `enum: [...]` in the
rule bank. Current enum sites by line: **401 lifecycle** (the intended one) · 486 · 612 · 615 · 619 ·
623. Correct **today only by line ordering**. Any new axis enum inserted above 401 — e.g. a Subject
enum `[client, market, estate]` — **silently redefines the lifecycle vocabulary** for this tool.
Fails loud on NO match; cannot detect a WRONG match.

Token note: rule bank `:623` already binds `estate` as a **scope** value; the ratified Subject axis
binds `estate` as a **subject** value; the catalog's `terminology_law` (:580-590) declares `estate`
RESERVED. Two axes, one token, no lint spanning both.

### 6b. SYSTEM_DEFINITIONS.yaml — 3 readers, all additive-safe

`opal_estate_infrastructure.py:530` · `rcg\bin\lexicon.py:71,:92` (dashed+underscore variants) ·
`check_system_definitions.py:30`. Subject/Function flowed in with no code change.

## 7. Existing annotation-like capability (BUILD LADDER rung 2)

No `comp-annotate`, no annotate subcommand, no annotation node table in Kuzu. **Seven** existing
per-entity annotation stores:

| Store | Entity key | Freeform fields | Writer | Reader | Scale |
|---|---|---|---|---|---|
| `org\modules\graph\keep-dormant.yaml` | `<type>:<aws-id>` | `reason`, `rearm_condition`, `annotation_cite` (file:line), `revalidate_by` (**TTL**) | human, git-reviewed | `comp_debt\dormant_guard.py:50` | 7 entries |
| `org\modules\graph\nerves-risk-edges.json` | `file:<repo path>` | `claims[].quote`+`doc`+`line`+`confidence`, severity `HOLD\|RISK\|DOCTRINE` | `nerves_lexical.py:58` | `cli.py:490-527`, `comp_pulse.py:68,292-329` | **1,731 nodes / 8,098 claims** |
| `estate-coverage-manifest.yaml` → resolver | `thread_id`/`named_thread` | `reason`, `description`, `debtscan_flags[]`, `status`, `reachability_status` | manifest by hand | `comp-estate --debt` | 138 threads |
| `org\modules\graph\debtscan\suppression_v1.yaml` | resource **class** | `reason`, `evidence`, `confirmed_fp_count` | AE, exec-signed | consumer unconfirmed | class-scoped |
| `org\modules\graph\critical-surfaces.yaml` | surface id | `why`, `coverage_note`, `known_findings` | human | `estate_infrastructure_cli.py:63` | per-surface |
| `org\modules\graph\drift-topology.yaml` | `seam_id` | `invariant`, inline `#` | human | comp-drift (INFERRED) | 7 seams |
| `org\modules\graph\comp-tools.yaml` | tool name | `note`, `name_note`, `guardrails` | human | routers | ~24 of 90 tools |

Observations bearing on extend-vs-build:
- **`nerves-risk-edges.json` is the existing tribal-knowledge→entity mechanism**, already wired
  advisory into the commit path (`safe-commit.sh:459-472`, `comp-pulse diff`, `|| true`). Keys on
  **repo paths**, not world-model entities. Two measured defects: **gitignored** (`.gitignore:525`)
  while `nerves_lexical.py:32` claims "tracked"; and a non-ASCII/cp1252 crash class documented at
  `comp_blast_universe.py:65-72` that silenced warnings on 28 of 2,255 nodes — *"THE FAILING NODES
  ARE THE RISK-BEARING ONES"* (same encoding class as §1e).
- **`keep-dormant.yaml` carries the richest annotation schema** — 8 required fields enforced at
  `dormant_guard.py:266-297`, incl. >=40-char `reason`, a file:line citation, and a `revalidate_by`
  decay clock (:173-175) whose expiry renders STALE and never auto-promotes. Its declared consumer
  `fuse.py` **does not exist** (`comp_debt\signals\__init__.py:15`); no `.tools\comp-debt` shim —
  nothing consumes its rulings.
- **The resolver thread record already carries per-entity annotation fields** (`reason`,
  `description`, `debtscan_flags[]`) surfaced by `--debt`, with a hardcoded flag→English dict at
  `estate_infrastructure_cli.py:76-84`; header :74-75 declares these census-static.
- **Kuzu offers one freeform slot**: `props STRING` on both tables. No annotation table at any DDL
  site.

## 8. Summary — what changes

**BREAKS (5 modes, 1 tool):** comp-estate `--segments` (data source + silent-degrade printer +
forbidden denominator), `--matrix`, `--structure`, `--list`/bare, `<vertical>` traversal. Plus
`--layers` by content (no drift check).

**WAS ALREADY BROKEN, fixed at CRO seat:** `--definitions Subject|Function` (U+26D4/cp1252); code
guard at :573 still owed.

**BREAKS ON A named_thread RENAME (3 tools):** comp-pipescript (`pipeline_cli.py:1345`),
`freshness_manifest_gen.py:72`, `estate_report_runner.py:660`.

**FRAGILE, ORDERING-DEPENDENT:** `c3-walk-agenda.py:76` first-match enum regex.

**UNAFFECTED:** comp-kuzu, comp-which, the HUD, all 8 rule-bank readers. **64 of 76 routable tools
touch no ontology registry at all.**

**NEW CAPABILITY REQUIRED (nothing to extend):** a reader for `c4_subject_function_grid` (zero code
readers); a Subject value on any entity (no field exists in manifest/resolver/graph); an
inference/ratification path for C3.ii (only population writer joins a hand manifest to a frozen
2026-06-15 census); a world-model-entity annotation carrier (the seven stores key on AWS ids, repo
paths, thread ids, surfaces, seams, tool names — none on verticals or segments).

**Two incidental live defects:** `--refresh` regresses `last_review` (gen-estate-resolver.py:102);
`check_system_definitions.py:31` validates `authority:` for presence only (the
andrew-infrastructure/estate-infrastructure split passes 68/68 clean).
