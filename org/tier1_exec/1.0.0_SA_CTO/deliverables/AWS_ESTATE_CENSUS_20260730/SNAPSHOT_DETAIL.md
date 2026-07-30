# EBS Snapshot / AMI Mass — full detail (Andrew-requested 2026-07-30)

**Authoritative count 2026-07-30: 1,016 snapshots + 312 AMIs** (describe-snapshots/-images; RE's 976
was index lag). **Actual July cost: $14.92 / 289.7 GB-month (Cost Explorer)** — this is an
INVENTORY-NOISE problem, not a cost problem.

## The generator (found in the graph, not by hand)

`infrastructure-snapshot-daily` (EventBridge rule) → `infrastructure-daily-snapshot` (Lambda,
role `infrastructure-snapshot-role`, policy `InfrastructureSnapshotPolicy`). It mints BOTH
modalities daily with ~30–31d rolling retention (June residue confirms rotation deletes):

| Cohort | n | GB (upper bound) | What |
|---|---|---|---|
| AMI rotation | 312 AMIs + 311 snaps | 5,556 | 10 instances x ~31 days: `snapshot-i-<id>-YYYY-MM-DD` |
| Volume rotation | 688 snaps | 24,216 | 23 volumes x ~31 days: "Daily snapshot YYYY-MM-DD" |
| DLM (separate policy) | 7 snaps | 210 | opal-website-wp, 7d retention |
| Orphans | 9 snaps | 234 | 5 June "pre-delete insurance" (moltbot, cost-audit-20260605) + 4 rotation debris of a deleted volume |
| Non-rotation AMIs | 2 | — | `bd-exporter-template-20260205` (KEEP — backs a live instance), `demo-transform-runner-pre-decommission` |

The 10 AMI-rotation instances: bd-49f-auto-login, bd-assets, bd-gold-layer-runner,
bd-transactions, bd-allocations, bd-gold-detail-generator, bd-gold-qa-runner, bd-fees,
seeking-alpha-scraper x2. **The BD estate + scrapers — and their volumes are ALSO in the 23-volume
rotation: the same data is backed up twice daily, once as AMI, once as snapshot.**

## The three decisions (each one sentence from Andrew)

1. **Retention:** 30d x daily for both modalities is ~1,000 standing objects. 7d (matching the DLM
   choice already made for the website) → ~230 standing objects, same protection class.
2. **Modality dedup:** AMI-rotation instances are double-covered. Pick one (AMI = relaunchable
   machine; snapshot = data only). Halving modality ≈ halves the mass again.
3. **The 9 orphans:** insurance snaps 55d past their deletions + rotation debris. Delete now?

## Ontology offtake (world-model design input)

- **Generator-vs-leaf principle:** 1,000 of these resources are ONE generator's rotation. The graph
  should model the GENERATOR (it already does: the Lambda + rule are CloudNodes) plus a rotation
  COHORT node with count/retention/cost — never 1,000 leaf nodes. Leaf-indexing rotation output is
  how AWS's own inventory (RE) drowned.
- **Purpose-expiry class:** "pre-delete insurance" resources carry an implicit expiry nobody tracks.
  A world-model property (`expires`, `insurance_for`) closes the class.
- Backing artifacts: `snapshots.json`, `images.json`, `snapshot_kill_candidates.json`,
  `analyze_snapshots.py` (rerunnable).
