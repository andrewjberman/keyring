# DEPLOY-COMPLETION LEDGER -- globgrph derive-runner image rebuild: the C2/C3.i COMPOSITION reaches the container

**Opened:** 2026-08-26T00:08Z by 1.0.0_SA_CTO~X -- AT DEPLOY-START
**Status:** **CLOSED 2026-08-26T02:15Z -- LANDED CLEAN, AND CONFIRMED BY THE PRODUCTION NIGHTLY, NOT
BY MY OWN RUN.** The 02:00Z scheduled derive (`ac07c74af8934ed48905f87ca61f8ee4`) fired unattended on
the fixed image and reproduced the result exactly:
```
    INFO: C2C3_COMPOSE_OK elapsed=2.3s nodes=6230 edges=18859
    INFO: C2C3_MOTIF_INGEST specs=3 nodes=6253 (C2Motif=6245 C3System=8)
          (grain: class=46 instance=6207) edges_resolved=23908/23983 (99.7%)
    OK: ICEBERG_NODES_WRITTEN count=27061
    OK: DERIVE_RUNNER_COMPLETE date=20260826
```
**Two independent runs -- one driven, one scheduled -- agree to the node.** Nothing half-landed; the
rollback taken mid-flight was reverted by the fixed rebuild, not left standing.
**CURRENT LEG (read this before the body):** the 00:2xZ rollback was a MID-FLIGHT SAFETY ACT, not the
end of the deploy. Sequence: build -> verification run FAILED at import -> **rollback to known-good
(hazard closed)** -> defect FIXED @ec0408628a -> **rebuilt @ tag `20260826-004846`** -> verification
run `3884ee43679149bf913d356dc146d685` **RUNNING NOW** (confirmed `lastStatus=RUNNING` at 00:5xZ; it
has already emitted `DERIVE_RUNNER_START`, which the failed run never reached). Steps 7-8 outstanding.
⚠ This header was ambiguous until 00:5xZ and `2.0.0_SA_COO` correctly flagged it (71980): the body
said "ROLLED BACK ... hazard closed" while the header said OPEN, which reads as a stale status field
on the ONE artifact class whose alarm keys on that field. Their conclusion -- that the act had
terminated -- was wrong, and they asked to be corrected rather than have me edit to satisfy them. The
header was right; the BODY was the defect, because it narrated a rollback without saying a second leg
had begun. Fixed here rather than by changing Status.
**Authority:** Andrew-direct 2026-08-26 ~00:0xZ, verbatim: *"Ok we need to get that resolved now, get
that code in the container"* -- said on the measurement below, at the CTO~X terminal.

## THE DEFECT THIS CLOSES

The estate does not track C2/C3.i resolution because **the code that produces it is in the repo and
not in the running container.**

MEASURED (read-only, 2026-08-25 ~23:3xZ, 1.0.0_SA_CTO~X):
```
deployed derive emits : INFO: C2C3_MOTIF_INGEST specs=2 nodes=23 (C2Motif=19 C3System=4) ...
current source emits  : ... (grain: class={n_class} instance={n_inst}) ...   <- ABSENT from deployed
```
That segment is UNCONDITIONAL in the source f-string (derive_runner.py:1827-1831), so its absence in
the running output is discriminating: the running bytes predate it. `specs=2` confirms from the other
side -- only the two frozen class specs are folded, with no `c2_individuate.compose() [LIVE]` source.

CONSEQUENCES, all one cause:
  - `grain` absent from all 20,800 graph nodes (5 serialisations tried; instrument positive control
    `props CONTAINS '"'` -> 20,797/20,800, so the query works and the zero is a MEASUREMENT)
  - graph holds only 19 C2Motif + 4 C3System (the frozen class layer)
  - ZERO instance-grain nodes, against a live local composition of 6,207 C2 / 1,257 C3.i
  - `comp-estate --layers` prescribes a class-grain positive control that CANNOT PASS on this
    vintage, so a seat following the canon exactly gets "you have learned nothing" and correctly stops

⛔ **AND THE DETECTOR SHIPPED IN THE SAME COMMIT AS THE FEATURE.** `_compose_c2c3_live()` carries a
four-way WARN taxonomy (`C2C3_COMPOSE_UNAVAILABLE|_SKIPPED|_FAILED|_MALFORMED`) plus
`C2C3_INSTANCE_GRAIN_ABSENT`, written precisely so "no instance layer" could never be mistaken for
"composition ran and found none." **ZERO of those lines appear in 36h of logs** -- because the code
that prints them is the code that is not deployed. The alarm and its subject were one commit, so the
silence is total and reads as health. CLAUDE.md Rule 22a CODE-currency class; caught by the estate's
own instrument (an expected log's ABSENCE is evidence too).

## VINTAGE

| thing | vintage |
|---|---|
| ECR `opal-globgrph-derive-runner:latest` | 2026-07-19T01:15:54Z (tag `20260719-011554`) |
| S3 source zip `build-source/derive-runner-source.zip` | 2026-07-19T01:15:10Z, 301,435 bytes |
| compose + grain landed in SOURCE | 2026-08-07 `627186582f` (0.7.0_AE_CloudOps, globgrph item 5) |
| drift | **37 days** image-to-now; feature has been un-deployed for **19 days** |

## THE ACT

Rebuild the derive-runner image from current source and push `:latest` + a timestamp tag.
Path (TF-declared, derive-build.tf): source zip -> `s3://opal-313476888478-globgrph/build-source/
derive-runner-source.zip` -> CodeBuild `globgrph-derive-build` -> ECR `opal-globgrph-derive-runner`.

NO Terraform change. NO task-definition change. NO code change. This is a REBUILD of an image whose
Dockerfile already carries every COPY line the feature needs (`c2_individuate.py`, `c3_cover.py`,
`NFRA_MOTIF_P1_canonical_ab_catalog.py`, `ENV OPAL_MOTIF_CATALOG`) -- landed 08-07 and never built.

## BLAST RADIUS -- STATED, BECAUSE `:latest` REACHES FIVE TASK-DEFS

The Dockerfile says so on its own face: derive (item2a.tf), comp_learns_producer, cse_producer,
fedobs_producer, resource_summaries_producer all run this ONE image and pick up `:latest` on their
next scheduled fire.

COPY sources: 28. **All 28 present on disk (0 missing). 0 dirty** -- nothing uncommitted ships.
CHANGED since the image build: **10 files / 58 commits**
```
  20  kimi_subdivision_harness/c2_individuate.py      <- the feature
   9  .tools/safe_deploy_core.py                      <- flag-gated OFF (EXTRACT_PIPELINE_CLOUD)
   7  infra/aws/globgrph/derive_runner.py             <- the feature
   7  kimi_subdivision_harness/c3_cover.py            <- the feature
   5  org/modules/graph/debtscan/summary_corpus.py    <- resource_summaries_producer's dep
   3  org/modules/graph/surface_check_cli.py
   2  org/modules/graph/critical-surfaces.yaml
   2  infra/aws/globgrph/_provenance.py               <- derive + cse_store
   2  infra/aws/globgrph/extract_pipeline_cloud.py    <- flag-gated OFF
   1  org/modules/graph/comp_aws_cli.py
```
Of the four NON-derive producers, only `resource_summaries_producer` has a changed dependency
(`summary_corpus.py`). `comp_learns_produce.py`, the three `cse_*` files and `fedobs_observe.py` are
UNCHANGED since the built image.

NEW PIP DEP: `kuzu==0.11.3` (added 08-07 for item 5, never built). The Dockerfile carries CVO's
measured resolution analysis in-file: kuzu declares **zero** transitive deps, positive-controlled
against pyiceberg's 31 -- so it structurally cannot move boto3/pyiceberg/pyarrow/pyyaml/httpx under
the other four producers. That is a wheel-metadata read; **the first real build is what confirms it**,
and confirming it is part of this deploy.

THE BAKED-ARTIFACT TRAP, CHECKED: the harness dir holds untracked `c2_instances.json` /
`c3_structures.json` -- composition OUTPUTS. The Dockerfile warns explicitly that COPYing the output
rather than the code would be a third baked artifact. The zip is built from the EXPLICIT COPY LIST,
never a directory glob; both outputs confirmed absent from that list (grep -c -> 0).

## PLAN / STATE

- [x] 1. Source zip from the explicit COPY list: 30 entries, 390,065 bytes. Controls: composition
        OUTPUTS absent (0), all 4 feature files present.
- [x] 2. Uploaded + VERIFIED AGAINST S3 (never the cp's own rc): 390,065 B @ 2026-08-26T00:10:26Z.
- [x] 3. CodeBuild `468a0667-238e-4f6d-a321-ef9b2f7f0ce2` -> **SUCCEEDED**.
- [x] 4. ECR `:latest` moved -> tag `20260826-001149`, digest `sha256:27001934...`.
        **PIP RESOLUTION CLAIM CONFIRMED BY THE REAL BUILD** (the item this ledger booked as
        unconfirmed): kuzu-0.11.3 installed and every shared pin HELD -- pyarrow-19.0.1,
        pyiceberg-0.9.1, boto3-1.38.0, httpx-0.27.2, pyyaml-6.0.2. kuzu moved nothing; the other
        four producers are safe on their next fire.
- [x] 5. **FAILED, AND THE FAILURE IS THE FINDING.** Verification run
        `a9435ade7f6345e2a49189e8545629e4` (nightly's exact live params, mirrored from the rule
        target) -> STOPPED, `EssentialContainerExited`, exit 1, 7 log lines, ZERO stages run:
```
    File "/app/derive_runner.py", line 1385, in <module>
        _APP.parents[2] / "org" / "tier1_exec" / "3.0.0_SA_CVO"
    IndexError: 2
```
        `_APP` is `/app` in-image -> ONE parent -> `parents[2]` raises AT MODULE IMPORT, so it never
        reaches the fail-soft guard inside `_compose_c2c3_live()`. **The feature has never once
        imported in the environment it was written for** -- landed 08-07, image built 07-19.
        CVO's container port check @a4986d7ba5 verified the COMPOSITION MODULES standalone; it did
        not exercise derive_runner's own module-level path resolution. Verified one seam away.

### ROLLED BACK -- 2026-08-26T00:2xZ, hazard closed

I built and pushed before finding this, which made the derive WORSE than I found it: the old image
ran fine WITHOUT the feature, the new one could not import, and the nightly was ~1h40m out.
`:latest` restored to the known-good July image and **VERIFIED BY DIGEST, not by tag listing**:
```
    latest            sha256:dc6cf568bb9cb565fc1298a41711edc5459ea7a6a57df3bda525dfd99f96ae63
    20260719-011554   sha256:dc6cf568bb9cb565fc1298a41711edc5459ea7a6a57df3bda525dfd99f96ae63
```
The 02:00Z nightly therefore runs exactly what it ran last night. **The four sibling producers were
never at risk** -- separate entrypoints (`cse_store.py`, `comp_learns_produce.py`,
`fedobs_observe.py`, `resource_summaries_store.py`), none imports `derive_runner`.

⚠ **MY FIRST RETAG WAS ITSELF THE SAME CLASS AS THE BUG.** Round-tripping the manifest through
`echo "$M" > file` appended a trailing newline, so ECR hashed different bytes and minted a THIRD
digest (`sha256:32cb12d0...`). Redone with exact bytes. *A digest without its normalisation is not
an identity* -- and verifying by DIGEST rather than by tag is the only reason I caught it. One stray
untagged manifest remains, referencing the same layers: surfaced, NOT deleted.

### FIX LANDED

`ec0408628a` (LOCAL on CLOUD, rides integration -- integrator seat is unmanned, 88+ commits queued).
Guard the repo-checkout entry on `len(_APP.parents) > 2`. Both arms tested with a FIRING negative
control (old form on `/app` -> IndexError, so the test distinguishes fixed from unfixed):
`CONTAINER /app -> 1 dir` (= where the Dockerfile COPYs the modules) · `REPO -> 2 dirs`.

⚠ **LANE:** `infra/aws/globgrph/` is `CLOUD_OPS_OR_ETL` (any AE agent) and this seat is CTO. The
owned-paths gate REFUSED correctly; landed under the audited `GIT_COMMIT_AUTHOR_OVERRIDE`, singular,
one lane per commit. **An AE seat should own this file going forward** -- flagged, not assumed.

- [x] 6. REBUILT carrying `ec0408628a` -> CodeBuild `cf19c0c6-11a1-4b24-971a-a1261f754b62` SUCCEEDED;
        ECR `:latest` -> tag `20260826-004846`.
- [x] 7. **FEATURE VERIFIED.** Run `3884ee43679149bf913d356dc146d685` -> `DERIVE_RUNNER_COMPLETE`,
        task STOPPED **exitCode=0**. Lines that had NEVER existed in `/ecs/globgrph/derive-runner`:
```
    INFO: C2C3_COMPOSE_OK elapsed=6.5s nodes=6230 edges=18859 producer=3.0.0_SA_CVO c2_individuate
    INFO: C2C3_MOTIF_INGEST specs=3 nodes=6253 (C2Motif=6245 C3System=8)
          (grain: class=46 instance=6207) edges_resolved=23908/23983 (99.7%) edges_unresolved=75
```
        Every discriminator moved as the diagnosis predicted: `specs` 2->3 (the LIVE compose source
        joined the two frozen specs), `nodes` 23->6253, and **the `(grain: ...)` segment EXISTS** --
        the exact segment whose ABSENCE was the original evidence that the running bytes predated the
        source. `instance=6207` matches the 6,207 composed LOCALLY off the same graph hours earlier,
        independently, so container and local derivation AGREE rather than one confirming the other
        by construction.
- [ ] 8. **BLOCKED ON LOCAL TOOLING, NOT ON THE DEPLOY. NOT CLAIMED.**
        `props CONTAINS '"grain"'` > 0 in the graph + the canon's class-grain control passing.
        Kuzu is embedded/single-writer; a query chain from my own cancelled background task holds the
        DB and THREE different instruments block behind it (`comp-kuzu` 900s TIMEOUT,
        `c2c3_liveness_acceptance.py --snapshot` 420s TIMEOUT, `kuzu_cli.py` direct 110s TIMEOUT).
        Self-inflicted: I fired concurrent reads at a projection that was rebuilding after my own
        derive. One orphaned child reaped; the rest are a single chain that will exit on its own.
        ⚠ NOTE ON WHAT STEP 8 EVEN IS: the local Kuzu DB is a PROJECTION of the Iceberg `graph_nodes`
        table, so "visible in comp-kuzu" is a third copy, not bedrock. It is nonetheless the copy
        every estate consumer reads, which is why it stays a required step and is not waved through.
        RESOLUTION PATH, no action needed: the 02:00Z nightly fires on the NEW image and produces a
        fresh derive + refreshed projection.

## STEP 8 RESOLVED AS A **SEPARATE FINDING**, NOT A DEPLOY RESIDUAL

⛔ **MY STEP-8 ZERO WAS A STALE-PROJECTION ARTIFACT AND I WITHDRAW IT AS EVIDENCE.**
```
    Iceberg graph_nodes (the warehouse, written twice)   27,061 nodes
    canonical Kuzu projection (what I queried)           20,800 nodes   <- PRE-DERIVE
```
The projection never advanced past my derive, so its `grain=0` was a read of the OLD graph and says
nothing about this deploy. The write side is evidenced independently: `ICEBERG_NODES_WRITTEN=27061`
(vs 20,800 before, delta ~= the 6,253 C2C3 nodes) on BOTH runs, `PROPS_CARRIED graph_nodes rows=27061`
listing `anchor_types` -- a **C3System-only prop**, so C2C3 props demonstrably reached the write -- and
`_props_and_guard` RAISES `SCHEMA_SEAM_SILENT_DROP` and refuses a lossy commit, so `grain` could not
have been dropped at the seam.

⛔ **AND THE METHOD FAILURE IS MINE, NAMED SO IT IS NOT REPEATED.** I ran five serialisations plus an
instrument positive control (`props CONTAINS '"'` -> 20,797/20,800) and reported the zero as a
MEASUREMENT. **Every one of those controls lived INSIDE the same projection**, so they agreed with each
other and were all about the same possibly-stale copy -- CLAUDE.md's wrong-plane form exactly: no
control inside the wrong plane can catch a wrong-plane error. I quoted that rule earlier the same night
and then walked into it.
⛔ **WORSE, THE TOOL WAS TELLING ME.** `kuzu_cli` mode `inc` is *incremental-OR-**serve-labeled-stale***
and comp-kuzu prints provenance **on STDERR** (`c3_cover.py` says so in its own comments). Every step-8
read I ran was `--json | tail`, which DISCARDS stderr. **I built a pipeline that threw away the one
field that would have contradicted me.** Same family as tonight's marker-grep and the orphan watcher:
the instrument reads cleanest exactly when it is least informative.

**THE STANDING FINDING, routed separately and NOT holding this ledger:** the canonical graph surface --
the estate's cross-layer grounding instrument -- can serve a projection that lags the warehouse, and it
labels that staleness only on a stream the callers' own idiom drops. That is an estate-wide grounding
concern, it long predates this deploy, and it belongs to whoever owns NFRA_GLOBGRPH / comp-kuzu.

⚠ **WHAT IS STILL NOT PROVEN, STATED PLAINLY:** I have not READ the 6,207 instance-grain nodes back out
of the warehouse with an independent reader. The write-side evidence above is the RUNNER describing
itself, twice, in agreement -- strong, and not the same as a consumer read. When the canonical
projection catches up, `props CONTAINS '"grain"'` > 0 and the canon's class-grain control passing are
the reads that settle it. This does not hold the deploy open because it is a READ, not a change.

## DISPOSITION AT SESSION END

**The ACT is discharged.** The code is in the container, it ran end-to-end, exit 0, with the
decisive log evidence above. No TF change, no task-def change, no code change beyond `ec0408628a`.
Rollback remains one retag with nothing to undo.
**STEP 8 IS THE ONLY RESIDUAL** and it is a READ, not a change -- nothing is half-landed, and no
state is left inconsistent by it being unverified. If this seat's session ends before the read
lands, step 8 HANDS OVER to whoever reads this (or resolves itself at 02:00Z); it is not an
in-flight deploy leg and must not be treated as one.
⛔ Per `1.0.0_SA_CTO` 71969: an unclosed ledger at session end is a COO alarm BY DESIGN. This block
is the explicit hand-over that ruling asks for, not an attempt to pre-empt the alarm.

ROLLBACK: ECR retains the prior image. `20260719-011554` is the last-known-good tag; re-tagging it to
`:latest` restores the current behaviour exactly, and no task-def or TF change has to be undone
because none is being made.

⚠ NOT CLAIMED YET: that the composition SUCCEEDS in-container. CVO verified the container port
@a4986d7ba5 (both halves run with no repo tree above them, driven by an external reader). This deploy
is the first time that runs on the real image, and step 5 is where it becomes a claim rather than a
prior. A `C2C3_COMPOSE_UNAVAILABLE|_SKIPPED|_FAILED` line is a legitimate outcome of this deploy and
would itself be progress -- it would be the first time the estate could SEE which failure it has.
