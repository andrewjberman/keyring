# 0.8.0_AE_CloudComp~Z -- TO-7 P2 FIRED + the coevolution OOM ROOT-CAUSED to a semantic bug (the next work item)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE

---

## Summary (window: ~14:25Z -> ~16:33Z; continues drive_forward_to7p1_landed_to4_measured_ds_consult_1300-1415Z.md)

Andrew directed the open items forward. Closed: the DS RAVC-4 finding on my own fold (exit-2 durable consumer), TO-7 P2 (two delta siblings FIRED + lake-verified), and -- the load-bearing outcome -- the fedobs coevolution OOM ROOT-CAUSED to a semantic bug, not a scale problem: the co-change self-join includes graph_head, whose single backfill run_id holds 56,115 subjects = 1,574,418,555 pairs = 100.00% of the explosion. Fix is a one-predicate exclude (`source <> 'graph_head'`), 1.57B -> 2,345 pairs, and MORE correct. Two /draw diagrams delivered to Andrew (the log grain + the full delta estate). Push-discipline binding hit mid-window (Andrew 15:43Z) + COO's shared-worktree correction. NEXT SESSION STARTS HERE: sorting the co-change semantic fix.

## Work completed

### DS RAVC-4 fold finding -- fixed @ 38f55d8ef
- DS validated my 604d34668 against the bytes: my message said "asserts ==" but the code warns-
  and-ships (0 asserts). Declarative drift on my OWN fix-for-declarative-drift. Fixed both ways:
  record corrected + the coverage WARN given a DURABLE CONSUMER (exit 2 on a cluster-coverage gap
  -- the scheduled wrapper's exit-status outlives a reader; warn-and-ship kept, write still lands).
  DS re-validated the bytes (return 2 :404 + sys.exit :409), RAVC CLOSED both halves.

### TO-7 P2 -- FIRED + lake-verified (CTO GO 152434Z)
- Built-to-gate first (gate was UNMET: ms_heat twin alarm absent + codeheat still =1 -> 0.7.0's
  batch unfired), then CTO fire-GO'd (P1 precedent = the pattern). Both DDLs fired in-VPC (run-
  task exit 0), both stage-then-ingest write-paths as built (rider R2):
  - globgrph.code_heat_snap: 24,101 rows @ 2026-07-16 (INDEPENDENT StaticTable, not self-report:
    ajb 22,975 + portal 1,126; cold 18,486/warm 3,672/hot 1,943). New `bool` type for `tracked`.
  - globgrph.fedobs_coverage_snap: 7 rows == the served signal exactly (cloudedge 3,783 @ 0.1…).
  - snap_store self-test 10/10; both tables stamp opal.naming_authority=CTO-interim-20260716T1307Z.
- fedobs_coevolution_snap DEFERRED (its source OOMs -- see below); emit_fedobs_snap.py honest-
  degrades (skips an errored signal, never fabricates).
- Twin choreography: committed twins @ c934701a6 -> 0.7.0 flagged they'd land BREACHING (tables
  didn't exist yet) -> I BACKED THEM OUT @ 528c430bc (R1: twin-ships-with-table) so 0.7.0's
  ms_heat twin lands clean -> after the fire, RE-ADDED @ 6c65fb7a8 (heartbeats now exist -> land
  HEALTHY). ms_heat twin landed born-OK 16:15Z (0.7.0 d89cc4fc9 / globgrph-v0.1.18).

### THE COEVOLUTION OOM -- root-caused (the next work item)
- Andrew asked (correctly) whether the co-change definition is "too loose." IT IS. Grounded:
  fedobs_observe.py:59-63 defines co-change as a self-join `FROM ev a JOIN ev b ON a.run_id=b.run_id
  AND a.subject_ref<b.subject_ref` -- "two subjects share a run_id." Cost O(k^2) per run_id.
- MEASURED run_id cardinality (StaticTable over cse): 123 distinct run_ids; the ONE graph_head
  BACKFILL run_id (graphhead-dee5b483) has k=56,115 subjects -> 1,574,418,555 pairs = 100.00% of
  ALL 1,574,420,900 pairs. Every other run_id combined = 2,345 pairs.
- SEMANTIC DIAGNOSIS: run_id means different things per producer. git run_id = a commit (real co-
  change); agent run_id = an audit session (reasonable); graph_head run_id = the WHOLE nightly
  materialization -> "co-occur in a session" degenerates to co-EXISTENCE (everything in the graph
  pairs with everything), which is both meaningless and O(56k^2). graph_head is a STATE producer,
  not a CHANGE producer -- it never belonged in a co-change signal.
- FIX (one predicate, not a memory raise): `WHERE run_id IS NOT NULL AND source <> 'graph_head'`
  -> 1.57B -> 2,345 pairs (~670,000x), stops OOMing at ANY log size, and the signal gets MORE
  correct (measures actual co-change). Routed to CTO (holds the fedobs disposition) pending
  Andrew -- NEXT SESSION EXECUTES THIS.

### /draw x2 (Andrew) + the 24-column layout
- Diagram 1: the cse log grain + (source,event_date) clustering + interval/scale.
- Diagram 2 (corrected to Andrew's actual ask): the full delta estate -- tier 1 event log + tier
  2 the 3 snapshot siblings, with REAL example rows pulled live; the LEDGER-vs-BALANCE-SHEET analogy.
- The 24 cse columns laid out (partition keys / identity / query dims / 7 fidelity JSON blocks).

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| snap_store.py (P2) | --self-test | PASS 10/10 | +2 surfaces + bool type |
| code_heat_emit / emit_fedobs_snap | --sibling stage | PASS | 24,101 + 7 rows staged (write-path exercise) |
| aws run-task (bootstrap) | ensure+ingest x2 | exit 0 | in-VPC DDL fire, both tables |
| pyiceberg StaticTable | cse + 3 snap tables | PASS | INDEPENDENT counts + the run_id-cardinality root-cause (56,115 -> 1.57B pairs) |
| comp-glob/grep | fedobs_observe coevolution SQL | PASS | the co-change JOIN predicate, source-grounded |
| terraform validate | globgrph module | PASS | twin backout + re-add |
| commit-gate | all P2 .py | PASS | 2 ruff nits fixed (semicolon, f-string) |

**Gap found:** none new. **The finding:** the coevolution OOM is a SEMANTIC bug (wrong producer
in the co-change population), diagnosed by exercising run_id cardinality, not a resource limit.

## MCP traffic

~18 handled. Significant IN: CTO P2 fire-GO (152434Z) + P2 rulings; MSTR LD-0299 amend-2 (OOM = his
assessment gap, severity inversion; e74f1902c); 0.7.0 twin-hunk flag (151325Z) + ms_heat twin
born-OK (161500Z) + predicate note; COO push-binding (155322Z) + shared-worktree correction
(163238Z). Significant OUT: P2 fire RAVC (CTO/MSTR), twin-backout resolution to 0.7.0, the co-change
root-cause (to COO; CTO route held for Andrew), 2 diagrams to Andrew.

## Blockers

NONE. Push-discipline binding active (batch pushes; a local commit is NOT unpublished in the shared
worktree -- COO 163238Z). My 6c65fb7a8 (twin re-add) is inert (commit != apply) and auto-publishes.

## Current State (zero-context handoff)

- **Wave NFRA_GRAPHFEED.W1: TO-2/4/5/6 CLOSED · TO-7 P1+P2 FIRED+verified · TO-1 pinned 07-17
  03:30Z · TO-3 row ~20:17Z tonight.** Effectively 6/7.
- **The delta estate is LIVE (globgrph namespace):** tier-1 cse event log (56,497 rows) + tier-2
  siblings ms_heat_snap (5,560/day) + code_heat_snap (24,101/day) + fedobs_coverage_snap (7/day),
  all snapshot_date-partitioned, each with a freshness twin.
- **THE NEXT WORK (this session's reason to reinstantiate):** the fedobs coevolution co-change fix.
  Query @ infra/aws/globgrph/fedobs/fedobs_observe.py:59-63. One-predicate fix `source <>
  'graph_head'`. CTO holds the fedobs-producer disposition; MSTR amend-2 named it. fedobs_
  coevolution_snap re-enters snap_store.SURFACES + gets its stager once coevolution is healthy.
- **Key commits:** 38f55d8ef (exit-2), c934701a6 (P2 code), 528c430bc (twin backout), 6c65fb7a8
  (twin re-add, inert). Tables verified via StaticTable, git-independent.

## Next Steps

1. **[me, next session]** THE COEVOLUTION SEMANTIC FIX -- add `source <> 'graph_head'` to the
   coevolution SQL (fedobs_observe.py:59), coordinate the derive-image path w/ 0.7.0 (fedobs
   producer runs on the derive image), exercise the query returns (expect ~2,345 pairs, no OOM),
   RAVC to [1.0.0_SA_CTO] (his disposition) + [0.0.0_AB_MSTR] (amend-2). Then re-enable
   fedobs_coevolution_snap (SURFACES entry + stager + twin) -- the deferred P2 surface.
2. **[me, ~20:17Z]** TO-3 second comp-axes row (>=24h) -> close to MSTR.
3. **[me, 07-17 03:30Z]** TO-1 final strictly-increasing fire + the ms_heat day-2 cluster-fix read
   (clustered_n==total_n, DS 262cda2e8) -> closes to MSTR + DS + CTO.
