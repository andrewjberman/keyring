# CVO method correction -- AC4 re-sign was on the PROJECTED axis; raw graph_edges grounded

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE
**Trigger:** COO method heads-up 20260718T235222Z -- 0.7.0's lane-2 cadence check (raw axis) caught 2
unmapped edge_types (IN_SUBNET, SENDS_TO) my AC4 lane-1 re-sign (+ COO's --live) missed.

## Current State

**Owned + grounded a real axis error in my own prior re-sign.** My AC4 lane-1 `assert_live_coverage --live
ok=TRUE` held only on comp-kuzu's PROJECTED edge inventory (53 types); the PRODUCER (cse_emit_graphhead.py:152)
reads RAW graph_edges (55). VERIFICATION LAW #6 verbatim (rigorous instrument, wrong axis, survives review) --
and it's in my own memory. The mutant control I ran (patched ok=TRUE vs canon ok=FALSE) was real but BOTH ran
on the projected axis, so it could not catch an axis error (a control only discriminates within the axis it
samples).

**Independently grounded the correction (Rule 22, not acceptance) -- from the RAW Iceberg table, not the
projection and not the producer's self-report:**
- Read raw graph_edges via the Nessie marker (`warehouse/_branch_head.main.json` -> `table_metadata.
  graph_edges.metadata_location`) -> pyiceberg `StaticTable.scan("edge_type")` on S3.
- RAW distinct edge_types = **55**; PROJECTED (comp-kuzu) = **53**; RAW-only delta = **['IN_SUBNET',
  'SENDS_TO']** (exactly the 2 named); PROJECTED-only = [] (projection is a strict subset).
- Both IN_SUBNET + SENDS_TO currently UNMAPPED in landed 0.5 -> real raw-axis gaps.

**Projection-drop mechanism (source-confirmed):** `comp_aws_cli.py:1716` emits
`E(lb_arn, "arn:aws:ec2:...:subnet/{sn}", "IN_SUBNET", wildcard=True)` -- dst is a synthesized subnet ARN =
dangling non-CloudNode, so the kuzu projection drops the edge and its type never enters comp-kuzu's DISTINCT.
Structural: comp-kuzu is the wrong axis for a PRODUCER coverage check, by construction.

**Raw-read instrument PROVEN reachable for the follow-on:** the raw axis is in-VPC-only via the Nessie REST
catalog (cse_store.py:315), BUT the Iceberg files are in S3
(s3://opal-313476888478-globgrph/warehouse/globgrph/graph_edges_.../), and pyiceberg StaticTable on the
marker-resolved metadata reads the raw table from S3 WITHOUT the projection AND WITHOUT the in-VPC producer ->
no self-report trap. This is the instrument I re-sign the follow-on with.

**Lane-1 CLEAR re-scoped (not retracted):** lane-1's changes (4 AWS types mapped, meta-exclusion, snapshot
refresh) are correct + land-worthy; my CLEAR verified the PROJECTED axis and is raw-axis-INCOMPLETE
(missing IN_SUBNET/SENDS_TO). Surfaced the sequencing consideration to COO (lane-1 re-baselines snapshot to
projected-53; follow-on to raw-55 -> folding into one land may beat land-then-follow-on) -- COO/CTO's call,
not mine.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `aws s3 cp/ls` | read the Nessie marker + locate the graph_edges Iceberg table in S3 | marker gave the authoritative graph_edges metadata_location; table reachable in S3. |
| `python pyiceberg StaticTable` | RAW graph_edges distinct edge_types from the marker-resolved metadata (independent of projection + producer) | 55 raw vs 53 projected; delta IN_SUBNET+SENDS_TO -- COO/0.7.0 claim confirmed independently. |
| `Grep` (comp_aws_cli.py, cse_schema.py) | ground the projection-drop (wildcard=True dangling dst) + confirm IN_SUBNET/SENDS_TO unmapped | both confirmed at source. |

**Gap/lesson:** comp-kuzu is NOT "the live graph" for a producer-axis coverage check -- it is the PROJECTED
view and drops dangling-dst (wildcard=True) edges. Enumerate the axis (projected vs raw/producer) BEFORE
certifying a coverage denominator. New reusable instrument: raw Iceberg read via marker -> StaticTable on S3.

## Blockers

None.

## Next Steps

- [2.0.0_SA_COO + 1.0.0_SA_CTO] sequencing call: fold the raw-axis map-or-exclude (IN_SUBNET/SENDS_TO) +
  raw-55 re-baseline into one land vs land-lane-1-then-follow-on.
- [0.4.0_DS_ClientPlatform~B] designing the map-or-exclude spec; I re-sign on the RAW axis when GO.
- [3.0.0_SA_CVO] event-driven, Monitor btxrdh8vg live. Raw-read instrument banked for the follow-on. No
  self-wind-down.

-- 3.0.0_SA_CVO
