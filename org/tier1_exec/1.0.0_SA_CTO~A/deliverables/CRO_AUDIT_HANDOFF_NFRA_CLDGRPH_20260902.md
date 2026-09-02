# CRO AUDIT HANDOFF -- NFRA_CLDGRPH (cloud-resident KuzuDB projection + gateway traversal)

**From:** `1.0.0_SA_CTO~A` · **For:** `4.0.0_SA_CRO`, ad hoc, on Andrew's word (2026-09-02: *"have them audit your
architecture and claims on an ad hoc basis"*) · **Written:** 2026-09-02 ~18:5xZ

## What you are auditing

`1.0.0_SA_CTO~A`'s step-2 endpoint, step-4 PRD and the refresh-mechanism architecture for the project that moves the
KuzuDB projection into the cloud. Andrew ratified the endpoint and three rulings on 2026-09-02; the architecture (marker-
downstream refresh, always-on serving plane, Cypher preserved, pull-style status read) is `1.0.0_SA_CTO~A`'s and is what
you are invited to falsify. `4.0.0_SA_CRO` wrote the step-1 brief this work stands on; the audit is of what was BUILT ON
it, not of the brief.

## The artifacts, in reading order

| # | path | what it is | vintage |
|---|---|---|---|
| 1 | `docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md` | the step-1 brief (`4.0.0_SA_CRO`) -- the measured substrate every claim below cites | @dfd24a010b |
| 2 | `org/tier1_exec/1.0.0_SA_CTO~A/deliverables/ENDPOINT_FORWARD_GLOBGRPH_CLOUD_COMPILE_20260902.md` | step-2 output + both Andrew-direct verbatims + the grounded refresh-mechanism ASSESSMENT + FRESHGUARD answered + surprise-channel observations | @ed0c95adb4 -> @3fd55f37d9 -> @082c90a610 |
| 3 | `docs/architecture/NFRA_CLDGRPH_PRD.md` | step-4 PRD v0.1 -- ENDPOINT (ratified), arc, territory, 9 acceptance properties, out of scope, rulings R1-R12, decomp inputs | this commit |
| 4 | `org/projects/NFRA_CLDGRPH.json` + `org/projects/REGISTRY.md` row + `org/missions/DIRECTIVES.yaml` D0 member | step-3 registration | this commit |

Adjacent, NOT authored for this purpose but load-bearing: `docs/architecture/NFRA_GLOBGRPH_PRD.md` (s.2a Item-2b, s.2b
F5/F6), `docs/architecture/NFRA_KUZUSPLIT_PRD.md` (O-1, O-4/P4), `docs/architecture/_PRD_TEMPLATE.md` @b3584ea86a,
`org/tier2_senior/0.7.0_AE_CloudOps~K/deliverables/D11_CARDS/kuzu_nessie_load.card.json` @5da9e7fffc.

## The claims worth attacking (each with the instrument that produced it)

1. **"Every Nessie writer ends by stamping ONE marker, so a consumer of the marker write is downstream of ALL of them."**
   Source: `_provenance.py:194` `stamp_marker`; callers by comp-find (`derive_runner`, `incremental_updater`, `cse_store`,
   `fedobs_observe`, `resource_summaries_store`); live marker read 2026-09-02 (writer `incremental_updater` @12:58:01Z,
   4/4 tables with `last_write_iso`). **Attack:** find a writer that commits to Nessie and does NOT stamp, or a stamp that
   precedes its commit.
2. **"The stitch never touches Nessie; portal-layer nodes enter via the nightly derive's producer fold."** Source:
   `stitch-produce.tf:21,77`, `derive_stitch.py:253`, `derive_runner.py:2175` `ingest_graphuni_producers`. **Bound I
   stated:** `derive_runner.py:2304` mentions a flag-gated REPLACEMENT for the graphuni producer chain that I did not
   trace. **Attack:** trace it; if the stitch has a second path into Nessie, claim 1's coverage argument needs it.
3. **"The projection's incremental engine already keys on the marker and reads only S3 (no Nessie REST, no Trino)."**
   Source: `kuzu_incremental_refresh.py:64` `_read_head_tables`, `kuzu_nessie_load.py:64` pyiceberg `StaticTable`.
   **Attack:** any read path in either file that needs the VPC.
4. **"The SQS+Lambda Andrew referred to is the AWS-layer incremental updater, not the stitch."** Source: `item2b.tf:175`,
   live census LAMBDA=1 (`opal-globgrph-incremental-updater`), SQS_QUEUE=2. **Attack:** a second Lambda or queue on the
   globgrph plane the `--corpus aws` census did not classify (its own DRIFT line: LIVE-no-DECLARED=20 of 250 scanned).
5. **"45 marker stamps / 102 invocations in 24h."** Source: CloudWatch `filter-log-events` on
   `/aws/lambda/opal-globgrph-incremental-updater`, patterns `MARKER_STAMPED` and `REPORT`, 24h window to ~18:0xZ.
   **Bound:** one day, one writer; nightly + producer stamps not counted. **Attack:** re-measure on a different day and
   count the non-Lambda writers.
6. **"FRESHGUARD legs 3 and 5 were torn down on Andrew's (A) remove-all-Class-A ruling; leg 4 is live."** Source:
   `git show 858554332d`; CTO GO 235109Z (`org/mcp/inbox/0.7.0_AE_CloudOps/read/20260717T235109Z_...`); today's marker.
   **Attack:** anything in the alarm class still live that the census missed (it found only two residual log groups).
7. **"O-4 was never specifically ruled."** Source: COO relay @c1eeaa102d ("proceed per PRD rec") vs `NFRA_KUZUSPLIT_PRD.md:106`
   (no rec on O-4). **Attack:** a ruling on O-4 anywhere the comp-find census (20 hits / 144,899 files) did not reach.
8. **Serving-plane sizing is UNMEASURED.** I asserted "a 47 MB embedded database needs a process holding it" and that
   per-query cold loads fail FWD-1's bar. Both are argument, not measurement. **Attack:** time a cold load.

## What I did NOT do (so you do not audit an absence as a claim)

No timing of any load, derive or stitch. No Lambda sizing. No network-reachability check gateway -> cluster. No
independent reproduction of the brief's F11/F12 (attributed to `3.0.0_SA_CVO`). The TO register was not read (step-2
refusal, by design). Nothing in `infra/` was changed.

## Surprise-channel observations already routed (msg 92653 to `3.0.0_SA_CVO`), not chased

- `warehouse/_branch_head.history/` is EMPTY (0 objects) although `_provenance._archive_superseded` (`:271`) promises an
  archive before every overwrite and refuses without it.
- FRESHGUARD leg-4 L4's ORIGINAL criterion reads TRUE on today's marker while the deploy-ledger entry stays HELD.
- CLAUDE.md s.5 cites `MDPF_DEBTCLEAN_PRD.md` s.11-12 for the moratorium; a word search for "moratorium" in that file
  returns 0 hits across 1,110 lines.

## Push state at handoff

All of the above is LOCAL on CLOUD at this device (push is integrator-only, LD-0367); `0.0.0_AB_MSTR`'s integration
window carries it. Verify the hash you read against `git ls-remote origin refs/heads/CLOUD` before citing a vintage.
