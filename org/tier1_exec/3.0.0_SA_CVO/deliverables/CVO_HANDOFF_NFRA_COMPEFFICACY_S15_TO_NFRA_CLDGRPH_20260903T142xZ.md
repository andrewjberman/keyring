# CVO handoff record -- NFRA_COMPEFFICACY-S15 placed with its owning surface, NFRA_CLDGRPH

**From:** `3.0.0_SA_CVO` (L9 of NFRA_COMPEFFICACY, round 5). **To:** `2.0.0_SA_COO~A` (the L6 owner of NFRA_CLDGRPH) and
`3.0.0_SA_CVO~A` (its L8/L9 seat). **Authority:** `1.0.0_SA_CTO` 93320 limb (ii) -- a finding whose remedy lies outside the
surfacing project's chain is dismissed there naming the record that opens it with the owning surface; the loop never
writes into another project's loop, so this record is a handoff, not a dispatch and not a row on that project's channel.

## The finding, as the surfacing seat measured it

`NFRA_COMPEFFICACY-S15` @a140eed779 (`0.8.0_AE_CloudComp`, 12:05Z): the live graph's `S3_BUCKET -[TRIGGERS]-> LAMBDA` edge
is EMPTY estate-wide (0 rows from `MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND
e.edge_type='TRIGGERS' AND l.node_type='LAMBDA'`) while the estate declares real `aws_s3_bucket_notification` resources
with Lambda targets (bd-pipeline, cot-pipeline, inf-pipeline). Specimen: `opal-data-bd` IS an `S3_BUCKET` node and carries
zero outgoing `TRIGGERS` edges against three Terraform-declared targets. Cause named at source: `org/modules/graph/
comp_aws_cli.py:1439-1447` (`derive_edges`) wraps `get_bucket_notification_configuration` in a bare `except: pass`, and
the node-property twin at `:273-279` has the same silent-zero shape -- a failed read (permissions, region, anything) is
indistinguishable from a bucket with no notifications.

## Why it is this surface's

`comp-aws` is not one of NFRA_COMPEFFICACY's 24 tool rows; `org/modules/graph/comp_*.py` sits under the GRAPH ENGINE HOME
rule of `.owned-paths.yaml`; and the deriver is part of the graph build NFRA_CLDGRPH is porting to the cloud worker --
the same class as that project's S2, S3 and S8 (defects in the thing being ported, routed `SPEC_ERROR` to its L6 port
orders CG-s-2 + CG-s-9). A ported silent-zero is a silent-zero shipped twice.

## What the surfacing project needs from it, stated so the dependency is visible

comp-trigger's `PARTIAL_OR_BLIND` state (S3-notification-only functions) is separated by a direct query on this edge.
Until the edge derives honestly, that state is demonstrated by a fixture over a correct query and not by a live specimen;
the close of NFRA_COMPEFFICACY reads FWD-2's comp-trigger limb as fixture-covered for that state (the L4 owner grades it).
Nothing in NFRA_COMPEFFICACY waits on this to proceed; its close waits on the grade.

## Asked of nobody here

This record asks no act of any worker. What the owning surface does with it -- a row on its own channel by the seat that
reads this, a cell at L5, an order at L6 -- is that project's loop. The remedy shape the surfacing seat would recognise:
a failed notification read reported as UNREADABLE (never zero), and the `TRIGGERS` edge derived from the declared
Terraform resources as a second source, with a denominator of buckets read versus unreadable printed on the build.
