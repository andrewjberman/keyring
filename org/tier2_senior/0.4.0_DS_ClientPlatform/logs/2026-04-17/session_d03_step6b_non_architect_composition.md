# Session — D_03 Step 6b Non-Architect Advisor Composition

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-17
**Started:** ~17:55 UTC (Eastern: ~1:55 PM)
**Status:** Patch committed + pushed + S3 synced. QA-runner fire deferred to COO for bundle/surgical decision (sister ~ABC B_01 cap on same 2026-04-15 date). DT given proactive heads-up for portal constitution re-run post-artifact.

## Origin

Andrew-directed handoff at ~17:55 UTC. Outstanding item on the
ADVI_ROLGAT permission-groups workstream:

> DS gold-gap patch for Alex Bright's Asset Mix + Top Holdings is still
> the only open item. Brief at
> `docs/briefs/ds-brief-advi-rolgat-composition-for-non-architects.md` —
> ready to apply.

Brief authored by 0.4.0_DT_ClientPlatform earlier on 2026-04-17.

## Problem (per brief)

`/advisor-intelligence` Book view rendered empty Asset Mix + Top
Holdings panels for any advisor whose primary role is `local_ops` or
`consultant` (Group 2 in `docs/architecture/ADVI_ROLGAT_PERMISSION_GROUPS.md`).

DT's evidence table:

| Advisor          | Roster role        | composition.json | summary.mix_keys | summary.concentration.items |
|------------------|--------------------|------------------|------------------|------------------------------|
| hunter_lloyd     | architect          | OK 4,302 B       | 4                | 9                            |
| chase_bertrand   | architect (roster) | OK 4,378 B       | 3                | 9                            |
| travis_penfield  | architect          | OK               | 3                | 9                            |
| alex_bright      | local_ops          | 404              | 0                | 0                            |
| alex_coggins     | implementor       | 404              | 0                | 0                            |

## Root Cause (verified by brief)

`data/black_diamond/scripts/gold/D_03.composition_artifacts.py` step 6
(line 708) iterates only the `architect` column of holdings_lots:

```python
architects = [
    a for a in lots['architect'].dropna().unique()
    if str(a).strip().lower() not in ('', 'nan', 'none', 'unassigned')
]
```

So `gold/entities/advisors/{id}/composition.json` was written only for
advisors who appear as architect on at least one relationship. D_04
reads composition.json to populate summary.mix + summary.concentration,
hence the 404 -> empty panel cascade.

## Fix

Surgical patch — appends step 6b after the existing architect loop,
between line 742 (end of step 6) and line 744 (start of step 7).

For each role in `[consultant, local_ops, implementor, additional_advisor]`:

1. Load `gold/views/account_team.parquet` via `_read_parquet(ACCOUNT_TEAM)`.
2. Iterate the role column; collect `{advisor_name -> set(relationship_id)}`.
3. Skip advisors already present in the architect set (they already have
   wider-scope composition from step 6 — the `architect_names` guard
   prevents both double-write and scope downgrade).
4. For each remaining advisor, filter holdings_lots to that advisor's
   relationship set, call `_build_composition` with the same args as
   step 6, and write to `advisor_composition_key(adv_id)` +
   `legacy_advisor_composition_key(adv_id)`.
5. ThreadPoolExecutor at `min(N, 8)` workers — same pattern as step 6.

Closing summary (~line 792) updated to print arch + non-arch counts:

```python
print(f'OK: firm_composition.json written. '
      f'Advisors: {written} (arch) + {non_arch_written} (non-arch) written, '
      f'{skipped + non_arch_skipped} skipped (empty book). ...')
```

`canonical_aua=None` for the non-architect branch — non-architect
tagged_aua comes from D_02, not from the per-architect lookup that step
6 uses.

## Compiler Validation

- `python -c "import ast; ast.parse(...)"` -> OK: parse clean.
- `comp-pipescript io D_03` -> ACCOUNT_TEAM already declared READ from
  C_07. No new graph edges; patch fits within existing IO manifest.
- `comp-pipescript deployed D_03` -> STALE pre-sync (expected). Post
  S3 sync verified MATCH downstream.

No COLUMN GAPS introduced — patch only adds reads of columns
`relationship_id`, `consultant`, `local_ops`, `implementor`,
`additional_advisor` from account_team, all of which D_00c and D_02
already consume.

## Deploy

Per memory rule "[DS owns full gold-script deploy cycle]":

1. **Commit.** SHA `09ac915b`, author `0.4.0_DS_ClientPlatform`,
   pathspec-constrained (`-- data/.../D_03.composition_artifacts.py`)
   per "[Always constrain commit pathspec]" rule.
2. **Push.** `origin/CLOUD` advanced `32fbb0d6 -> 09ac915b`.
3. **S3 sync.** `safe-ec2-deploy.sh bd-gold-layer-runner` ->
   `deploy-to-ec2.sh` -> `aws s3 sync` to `s3://opal-data-bd/code/gold/`.
   Wrapper auto-committed `EC2_MANIFEST.json` bump as `88fd8d1c`.
4. **Push manifest.** `origin/CLOUD` advanced `cb6d78e2 -> 88fd8d1c`.

PROD runner i-01003b035d2988dfb verified STOPPED before any decisions.

## Coordination — QA Runner Deferred

Did NOT fire `bd-gold-trigger` Lambda or QA runner directly. Reasons:

1. Sister instance `0.4.0_DS_ClientPlatform~ABC` shipped B_01
   confidence-tiered cap (commit `cb6d78e2`) earlier in the session and
   is also queued for QA runner fire on snapshot_date 2026-04-15 (per
   inbox msg `20260417T175837Z`). Both patches now sit on
   `s3://opal-data-bd/code/gold/`.
2. Memory rule "[EC2 single command discipline] — never run overlapping
   SSM commands, coordinate with AE, one at a time."
3. ~XYZ has CP-DS1 Run 9 coordination in flight on 2026-04-15 — risk of
   collision.

MCP to 2.0.0_SA_COO at 18:01Z requesting bundle vs. surgical decision:

- **Bundle.** Single QA-runner pass on bd-gold-qa-runner
  i-0090b823a4a0997e3 for 2026-04-15 — chain runs B_01 -> ... -> D_03
  -> D_04, validates both patches.
- **Surgical.** `--single D_03 --single D_04` for the alex_bright path
  only (no upstream dep on B_01 for composition.json).

## Proactive Downstream

Per memory rule "[Proactive downstream messages]" — heads-up to
0.4.0_DT_ClientPlatform at 18:01Z with the post-artifact portal
constitution invocation:

```bash
python .tools/frontend-dev.py \
  --constitution portal/.frontend-dev/testing/advi_rolgat_live_tier_validation.json \
  --base http://localhost:5175 \
  --login-email alex.bright@49financial.com \
  --login-password '49demo*1076!' \
  --scenario advisor-book-view-renders
```

DT to fire when alex_bright artifacts refresh.

## Acceptance (from brief, validation pending QA fire)

```bash
aws s3api head-object --bucket opal-data-bd \
  --key gold/entities/advisors/alex_bright/composition.json
# Expect: 200 with ContentLength > 1000

aws s3 cp s3://opal-data-bd/platinum/advisors/alex_bright/summary.json - | \
  python3 -c "import json,sys; d=json.load(sys.stdin); print('mix_keys=', len(d.get('mix',{})), 'conc_items=', len(d.get('concentration',{}).get('items',[])))"
# Expect: mix_keys >= 3, conc_items >= 9
```

Plus stdout grep on D_03 run log:

```
=== Step 6b: Non-architect advisor composition ===
  Processing N non-architect advisors...
  Non-architect composition: M written, K skipped (empty book)
OK: firm_composition.json written. Advisors: X (arch) + M (non-arch) written, ...
```

with M > 0.

## Out of Scope

- Backend payload strip in `opal-partners-data` is unchanged.
  Implementor JWTs still get `clients[]` + cost-basis stripped at
  request time per `ADVI_ROLGAT_PERMISSION_GROUPS.md`. Gold artifact
  stays complete; stripping is a per-request decision based on JWT
  claim, not a gold-time choice.
- Shared-role advisors (architect on some relationships AND
  consultant/local_ops/etc on others) keep their step-6 architect
  composition. The `architect_names` guard prevents step 6b from
  re-writing them with a narrower scope.

## Artifacts

- Code patch: `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` (+77/-1)
- Brief: `docs/briefs/ds-brief-advi-rolgat-composition-for-non-architects.md`
- Permission groups doc: `docs/architecture/ADVI_ROLGAT_PERMISSION_GROUPS.md`
- DT origin log: `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-17/advi_rolgat_dt1.md`
- Commits: `09ac915b` (D_03 fix), `88fd8d1c` (EC2_MANIFEST bump from safe-ec2-deploy)
- MCP out: COO (`20260417T180130Z`), DT (`20260417T180149Z`)
- MCP in: ABC sister B_01 cap (`20260417T175837Z`)
