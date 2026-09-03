# CHANGE-MANAGEMENT HOLD — shared-infra: ms-heat-snapshots-expire-60d (S3 lifecycle expiry)

| | |
|---|---|
| **Opened** | 2026-09-03T11:20Z |
| **State** | OPEN — HOLD pending Andrew's explicit word (S3 delete/expiry, CLAUDE.md confirmation list) |
| **Seat** | `0.8.0_AE_CloudComp` (owner class, NFRA_GLOBGRPH) |
| **Authority** | `1.0.0_SA_CTO` DECISION on 93515 (msg 93528, 2026-09-03T11:17:27Z): *"it is NOT shipped as a passenger ... whether that retention is wanted is a data decision, and S3 deletes take Andrew's explicit word."* Relayed from `0.0.0_AB_MSTR~Z` (bus c4a47c90), sourced from `0.7.0_AE_CloudOps~S`'s pre-edit baseline read for TO-OP-S-8 (row NFRA_OPSEC202609-Z-S17). |
| **Pipeline** | `infra/aws/terraform/shared-infra` (`s3.tf`, resource `aws_s3_bucket_lifecycle_configuration.global_graph`) |
| **Declaring commit** | `4cd024c5c6` (2026-07-15T17:57:17-04:00, `0.8.0_AE_CloudComp~Z`) — verified by direct read, not by relay alone: `git show 4cd024c5c6 -- infra/aws/terraform/shared-infra` confirms the added `rule { id = "ms-heat-snapshots-expire-60d" ... }` block in `s3.tf`, homed in the EXISTING `global_graph` lifecycle resource (not a new resource — the commit's own message names a CTO rule-swallow check that fired against a 14th-resource shape and was withdrawn in favor of this in-place addition). |

## THE FACT (DESIRED vs APPLIED, unresolved for ~7 weeks)

`infra/aws/terraform/shared-infra`'s baseline plan at its committed state reads **0 add / 1
change / 0 destroy**: `aws_s3_bucket_lifecycle_configuration.global_graph` would gain rule
`ms-heat-snapshots-expire-60d` (prefix `warehouse/ms_heat/snapshots/`, `status = Enabled`,
`expiration { days = 60 }`), declared in Terraform on 2026-07-15 and **never applied, or applied
and changed out of band — the tree cannot tell which** (Rule 22a: DESIRED != APPLIED != EXERCISED;
no live `get-bucket-lifecycle-configuration` read has been taken by this seat to resolve which).
The pre-existing rule on this same resource, `abort-incomplete-mpu-7d`, is untouched by this
change either way.

This item was already known and deliberately scoped away from at least one prior apply: the
2026-08-19 `goldhome-repoint-49f-rp-ae-1-bucket-mint` ledger entry
(`org/critical_paths/change_management/20260819T0106Z_...`) ran a TARGETED apply specifically so
that *"the pre-existing staged global_graph ms_heat lifecycle row (@4cd024c5c6, 0.8.0~Z,
COO-banked) is not ratified as a side effect."* This is the first entry that names the pending
change itself, as directed by the CTO's decision above.

## WHY THIS IS A HOLD, NOT AN APPLY

A `lifecycle` `expiration` rule causes AWS to **delete objects** — here, `ms_heat` snapshots under
`warehouse/ms_heat/snapshots/` older than 60 days, on a served bucket. Whether that retention
window is wanted is a **data decision**, and per CLAUDE.md's own confirmation list, an S3 delete
takes Andrew's explicit word before it lands. Nothing is applied and nothing is reverted by this
entry — it exists so the pending state is attributable and so the never-widen rule has something
to read.

## THE SCOPE-AWAY OBLIGATION, until Andrew's word lands

Every `shared-infra` apply between now and Andrew's word must run through `safe-apply` **scoped
away** from `aws_s3_bucket_lifecycle_configuration.global_graph` (a `-target` apply excluding it,
or a plan that otherwise does not touch it). The acceptance check for such an apply is an
**UNSCOPED re-plan afterwards that still reads exactly this 1 change and nothing else** — a scoped
apply verified only by a scoped re-plan is the exact trap this estate has already measured and
named elsewhere (never re-derive that mistake here).

## REBUILDABILITY STATEMENT (Andrew's condition)

**Measured 2026-09-03T14:15:08Z by `0.8.0_AE_CloudComp~K`; conclusion: the
snapshots are rebuildable at the semantic/index-content level, so Andrew's conditional apply
path is admitted.** The boundary is explicit below: this is not a byte-for-byte serialization
guarantee and the current CLI has no one-command historical replay flag.

- **Producer and run.** `python .tools/comp-read
  org/modules/heatmap/ms_heat_index.py --for "what it reads, what it writes, and what its
  docstring says about retention"`, followed by pinned section reads, measures the non-dry-run
  path at `org/modules/heatmap/ms_heat_index.py:362-390`: `main()` calls `read_ms_nodes()`,
  `build_index(...)`, then `persist(...)`. `persist()` at lines 267-285 writes the current index
  to `s3://opal-313476888478-globgrph/warehouse/ms_heat/ms_heat_index.json` and appends a dated
  JSON object below `warehouse/ms_heat/snapshots/`; lines 27-36 and 265 name the same retention
  boundary and state that deletion is lifecycle-declared, never a code-side delete.
- **Recompute source.** The same `comp-read` instrument plus the pinned read at
  `org/modules/heatmap/ms_heat_index.py:88-132,138-216` measures that the index is recomputed
  from `MS_FILE` and `MS_FOLDER` rows in the canonical read-only Kuzu graph after
  `ensure_fresh(...)`; the run records its `graph_nodes_snapshot` and graph last-write vintage.
  A live `.tools/aws s3api list-objects-v2` read of each of the three recorded source snapshot
  IDs (`2968923625689391988`, `8723832531903082995`, `6901201222334213263`) returned
  `KeyCount=1`, `IsTruncated=false` for each exact
  `warehouse/globgrph/graph_nodes_.../metadata/snap-<id>-` prefix. The July 15 source metadata
  additionally reads `gc.enabled=false` and points at snapshot `2968923625689391988`. Thus the
  source graph vintages for every currently stored JSON snapshot remain present, rather than
  being assumed from a message or from the current graph alone.
- **Live snapshot-prefix denominator.** The live command `bash .tools/aws s3api
  list-objects-v2 --bucket opal-313476888478-globgrph --prefix
  warehouse/ms_heat/snapshots/ --max-keys 1000 --output json` returned
  `KeyCount=3`, `MaxKeys=1000`, `IsTruncated=false`: dated objects
  `20260715T213817Z.json` (2,585,175 bytes), `20260716T132023Z.json` (2,601,374
  bytes), and `20260717T180941Z.json` (2,626,103 bytes). Live reads of those objects record
  5,519 / 5,560 / 5,604 source rows respectively and carry the three source snapshot IDs above.
- **Append-only historical source.** `python .tools/comp-read
  infra/aws/globgrph/snap_store.py --for "the ms_heat_snap table: append-only or not, where it
  lives"`, followed by pinned reads at `infra/aws/globgrph/snap_store.py:1-35,47-54,79-93,
  212-268`, measures table id `globgrph.ms_heat_snap`: `ensure_table()` loads an existing table
  and never recreates it; `append_rows()` calls only `t.append(table)`. A live read of its newest
  metadata object reports location
  `s3://opal-313476888478-globgrph/warehouse/globgrph/ms_heat_snap_a1875ebc-9d80-4078-b8e7-19e6455265bd`,
  `gc.enabled=false`, current summary `operation=append`, two data files and 11,164 total rows.
  A live data-prefix listing returned exactly two partitions,
  `snapshot_date=2026-07-16` and `snapshot_date=2026-07-17`, matching the 5,560 + 5,604 rows.
- **Loss surface and why it does not reverse the conclusion.** Once the lifecycle fires, the
  standalone dated JSON object older than 60 days is gone; byte identity, original S3 ETag, and
  a ready-made one-command historical replay are not preserved by `ms_heat_index.py`. The
  `2026-07-15` JSON also predates the two populated `ms_heat_snap` partitions. Its exact source
  graph snapshot manifest nevertheless remains live with GC disabled, while the later two runs'
  per-node history is additionally retained in the append-only sibling. Therefore the functional
  artifact can be recomputed from the live graph for current state and replayed from the retained
  recorded graph vintage for each of the three existing snapshots; what is surrendered is the
  convenience and byte identity of the standalone JSON history, not the underlying graph input
  or the append-only analytic history. That bounded loss is consistent with the ruled 60-day
  retention and does not make the snapshots non-rebuildable.

## THE CARD TO ANDREW (open)

**Apply the 60-day expiry on `ms_heat` snapshots — yes or no?**
- **Yes** → the owner (`0.8.0_AE_CloudComp`, or the `~Z` lane that declared it) applies it under
  its own ledger entry; the re-plan should then read `0 to add, 0 to change, 0 to destroy`.
- **No** → the owner reverts the Terraform declaration so DESIRED matches APPLIED again; the
  re-plan should then read `0/0/0` from the other direction.

Either way, the plan returns to `0/0/0` and this HOLD closes. **Until then, the plan reading 1
change is the honest, correct state and should stay visible, not be papered over.**

## Progress

- [x] Pending change identified and independently verified against the declaring commit (not
      taken on relay alone)
- [x] Prior scoping precedent located (`20260819T0106Z_...`) confirming this is a known, banked
      item, not a fresh surprise
- [x] This ledger entry opened, naming the pending change, its commit, and the HOLD
- [x] Andrew's word — conditional apply admitted by his "recs approved" ruling; the measured
      rebuildability condition is satisfied in the section above
- [ ] Owning apply or revert, under its own ledger entry, citing this HOLD as closed
- [ ] Unscoped re-plan confirms `0/0/0`

## Not established

⚠ No live AWS read (`get-bucket-lifecycle-configuration`) has been taken to determine whether the
rule is already partially or fully applied out of band — the tree cannot currently distinguish
"never applied" from "applied then reverted/changed elsewhere." Not required to resolve the HOLD
(Andrew's word governs regardless of which), but named here rather than assumed.
