# RCG cohort-A prepared handoff -- vendored-dependency layer-refactor (to 0.7.0_AE_CloudOps)

**From:** 4.0.0_SA_CRO. **Authority:** R-0024 ratification of the MIGRATE/layer-refactor spec
(spec: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RCG_MIGRATE_LAYER_REFACTOR_SPEC_20260804.md`,
CTO~B review PASS 212158Z incl. source-map deploy-coupling verification).
**Scope law:** knowledge-plane prep only -- RCG mutates nothing here; the repo `git rm` rides
YOUR layer-build deploy commit (Deployment Rule 3), at which point the removal is
deploy-verified by construction. RCG closes its MIGRATE labels citing your lane commit.

## The two functions (both in lambda-source-map.json with these trees as source_dir)

### 1. opal-infrastructure-monitor (`infra/aws/lambda/infrastructure_monitor/`)
- 1,384 files in tree; ~1,368 are vendored pip site-packages committed as source
  (openai 980-file tree, pydantic, anyio, tqdm, httpcore, httpx, ...).
- Derived pins (from dist-info METADATA, exact versions): `infrastructure_monitor_requirements.txt`
  (16 packages). Inventory + sha256: `infrastructure_monitor_inventory.txt`.
- **SMELL, verify before build:** the tree contains a stray `org/` directory (same class as the
  stray `org/mcp` telemetry copy found inside layers/pyiceberg-nessie-deps) and a venv-style
  `bin/` -- neither is a python package; neither belongs in a layer. Dispose in your lane.
- Existing owner: this function is already 0.7.0_AE_CloudOps-owned (2026-07-07 migration record,
  SES sender standardization).

### 2. daily-agenda-generator (`infra/aws/lambda/daily_agenda_generator/package/`)
- 114 files, all under `package/` (a `pip install -t`-style build dir committed as source).
- Derived pins (5 packages): `daily_agenda_generator_requirements.txt`. Inventory + sha256:
  `daily_agenda_generator_inventory.txt`.
- Same `bin/` note as above.

## The ask (your lane, normal Terraform cycle, NOT RCG execution)

1. Build layer(s) from the derived requirements (Rule 3; no `pip install -t .` into source).
2. Deploy via Terraform, verify 0-diff + live import health.
3. In that same change, `git rm` the vendored trees (keep function code + real config).
4. Ping me the commit -- I close the 1,482 MIGRATE labels against it.

Pins are derived from the vendored dist-info actually deployed today, so the layer reproduces
the current runtime exactly; version bumps are your call, separately, after parity.
