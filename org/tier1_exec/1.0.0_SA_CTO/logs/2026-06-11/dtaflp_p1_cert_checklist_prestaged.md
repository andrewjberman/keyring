# NFRA_DTAFLP P1 — CTO cert checklist (PRE-STAGED, pre-mv baseline)

**Staged:** 2026-06-11 (ws CTO 1.0.0_SA_CTO), in response to COO /drive heads-up
`20260611T130227Z` — DTAFLP P1 GLOBGRPH gate PASSED, AE being spawned to execute
P1 (`git mv data/orion → data/inf`, ~190 files). My step-4 role = P1 cert on AE's RAVC2.

**This doc is captured BEFORE AE's mv** so the cert is a real before/after diff
(AC3 requires a before/after vendor count). Cross-check AE's flagged-18 against the
candidate list in §3 for completeness; verify the §1 baselines collapse to 0.

P1 TO: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_DTAFLP.P1.ae-orion-inf-rename.md`
PRD §4/§6/§9: `docs/architecture/NFRA_DTAFLP.md`

---

## §0 — Scope reminder (the landmine)
Rename ONLY the path **prefix** `data/orion/` → `data/inf/`. PRESERVE every
`orion` that names the **vendor/API/source** (Orion Advisor Tech). A blind
`sed orion→inf` corrupts the live integration. `black_diamond` STAYS this phase
(reduced-scope P1; bd handled later). `data/cot/` already abbreviated.

---

## §1 — Pre-mv BASELINE counts (captured 2026-06-11, on origin/CLOUD pre-mv)

### 1a. `data/orion/` path-prefix refs — MUST collapse to 0 (Classes A+B+C)
| Disposition area | files (pre-mv) | after-cert target |
|---|---|---|
| Class-A compiler core (`org/modules/graph/*.py,*.yaml`) | 54 | 0 (AE wiring) |
| Class-A `.tools`/config/CI/`.owned-paths.yaml`/`.gitignore`/`.github`/EC2_MANIFEST | 8 | 0 (AE + CTO owned-paths) |
| Class-A bundled provenance (`infra/aws/lambda/inf-pipeline/**`, `ec2/inf-bronze-runner/**`) | 29 | 0 (DS provenance sweep) |
| Class-B comp-build generated (gold-nan/postmerge/shadow/comp-shell) | 47 | 0 (regenerated, not hand-edited) |
| Class-C `data/orion/**` self-refs | 49 | 0 (move with folder) |
| **Live total (A+B+C)** | **~187** | **0** |
| Class-D docs/history (full-tree git grep = 739; D = 739 − 187) | ~552 | STAY (history-class, excluded) |

**Cert test:** post-mv `git grep -l "data/orion/" -- <live areas excl docs/history> | wc -l` = **0**.
The Windows-backslash form `data\orion\` must ALSO be 0 (see §3 #13 — a `/`-only grep misses it).

### 1b. VENDOR-form `orion` refs — MUST be IDENTICAL before/after (AC3)
Baseline LINE count (`_orion_api|orion_export|orion_billing_dim|orion_tax_dim|convert_orion_api|Orion API|orion_api_silver`): **1618 lines**.
**Cert test:** post-mv same grep = **1618** (a delta ⇒ vendor corruption ⇒ BLOCK).

---

## §2 — Vendor / name PRESERVE watchlist (these `orion` occurrences STAY)
- `_orion_api_silver_lib.py`, `convert_orion_api_to_silver.py`, `orion_export.ts`,
  `orion_billing_dim.py`, `orion_tax_dim.py`, Orion endpoint URLs/clients — vendor API.
- **`orion-gold-dispatch.sh`** — KEEP the filename (firm-abbrev, COO ruling; P1 TO explicit).
  All refs to it stay: EC2_MANIFEST dispatch_script, extract_pipeline.py parser,
  pipeline_cli.py map key `"orion-gold-dispatch"`, comp-tools.yaml, test_multi_pipeline.py.
- **`bronze/orion-api/`** — S3 KEY prefix inside `opal-data-inf` bucket (vendor bronze path),
  NOT a local folder; STAYS (aws-shapes fixtures, comp-tools.yaml:449-450).
- `cli.py:179` `'orion' in nid` — node-id heuristic tied to the KEPT dispatch name; STAYS
  (JUDGMENT — confirm node ids aren't path-derived; if they are, re-evaluate).

---

## §3 — Candidate path-COMPONENT refs (the "18" AE flags — cross-check for completeness)
These are `orion` as a discrete **path segment** that a `data/orion/` prefix-grep MISSES.
A naive sed leaves these stale → broken paths. CTO owns these in the cert pass.

**Split-component form** (`/ "data" / "orion" / "scripts" /`):
1. `.tools/comp-freshness:56` — `WORKSPACE/"data"/"orion"/"scripts"/"gold"`
2. `.tools/silver-dtype-migrate.py:32` — `os.path.join(REPO,"data","orion","scripts","silver")`
3. `org/modules/graph/extract_pipeline.py:1093` — `workspace_root/"data"/"orion"/"scripts"/"gold"`
4. `org/modules/graph/extract_s3.py:431` — `workspace_root/"data"/"orion"/"scripts"/"gold"`
5. `org/modules/graph/pipeline_cli.py:1428` — `_WORKSPACE/"data"/"orion"/"scripts"/"silver"`
6. `org/modules/graph/pipeline_cli.py:1429` — same (silver)
7. `org/modules/graph/pipeline_cli.py:1754` — `_WORKSPACE/'data'/'orion'/'scripts'/'gold'`
8. `org/modules/graph/pipeline_cli.py:2110` — same (gold)
9. `org/modules/graph/validate_cli.py:46` — `_WORKSPACE/"data"/"orion"/"scripts"/"gold"/gold_validate_config.yaml`
10. `org/modules/graph/validate_cli.py:528` — `_WORKSPACE/'data'/'orion'/'scripts'/'gold'`

**Regex-embedded alternation** (`data/(?:black_diamond|orion|schwab)/scripts/...`):
11. `org/modules/graph/pipeline_cli.py:138` — orion token in path regex (→ must match data/inf)
12. `org/modules/graph/pipeline_cli.py:186` — same regex, second occurrence

**Windows-backslash form** (a `/`-grep cannot see this):
13. `org/modules/graph/vectorize-audit/INF_B_00.yaml:2` — `script_path: data\orion\scripts\gold\INF_B_00...`

**Deploy-map KEY (AE-owned per P1 TO, but component-form — confirm AE updated it):**
14. `.tools/safe_deploy_core.py:23` — `"orion": ("opal-data-inf","inf")` PIPELINE_MAP key
    → key must become `"inf"` (AE's explicit Class-A wiring; verify in cert).

**Test fixtures referencing the orion path (verify updated or intentionally pinned):**
15. `.tools/test_safe_deploy.py:200,241` — "INF-PATH orion->opal-data-inf" case (string asserts the routing)

> Candidate set ≈ 13 true component-form refs + the deploy-map key + the test fixture.
> AE's flagged-18 is authoritative; if AE flags <my candidates, I chase the delta.
> #4 ds-precommit-check.py / safe_deploy_core.py COMMENTS mentioning "orion" as a bare
> word (not a path) are prose — opportunistic, non-breaking, not cert-gating.

---

## §4 — Cert dimensions (the 4 gates I sign on AE's RAVC2)
1. **0-residual** — `data/orion/` (both `/` and `\` forms) = 0 in live code (A+B+C); docs/history excluded.
2. **18 component-refs** — every §3 candidate retargeted to `data/inf` (cross-check AE's flagged list; no miss).
3. **comp-build** — 0-error regen + `comp-trace`/`comp-blast` spot-check on a bd + an inf gold node PASS at new paths (AC4); `comp-pipescript deployed` MATCH on a bd + inf script (AC5).
4. **vendor-untouched** — §1b count IDENTICAL (1618); §2 watchlist intact (AC3); `test_safe_deploy.py` + `parity-gates.sh` PASS.

**Sign criteria:** all 4 PASS → CTO cert RAVC2 ACK to COO; then CVO AC10 0-residual = binding close-gate after P3.
**Any fail:** BLOCK + specific residual list back to AE; no cert.

---

## §5 — Status
PRE-STAGED, awaiting AE P1 RAVC2 (event-driven; AE spawned by MSTR per COO /drive 1302Z).
Baseline frozen at this commit. When AE files: re-run §1/§4 greps post-mv, diff, sign or block.
