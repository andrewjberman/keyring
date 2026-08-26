# DEPLOY-COMPLETION LEDGER -- globgrph derive-runner image rebuild: the C2/C3.i COMPOSITION reaches the container

**Opened:** 2026-08-26T00:08Z by 1.0.0_SA_CTO~X -- AT DEPLOY-START
**Status:** OPEN
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

- [ ] 6. REBUILD carrying `ec0408628a`; confirm SUCCEEDED + `:latest` moves
- [ ] 7. Verify the FEATURE: `C2C3_COMPOSE_OK` + an ingest line CARRYING `(grain: class=N
        instance=M)` with instance > 0
- [ ] 8. Verify the WORLD, not the log: `props CONTAINS '"grain"'` > 0 in the graph, and the canon's
        own class-grain control passes for the first time
- [ ] CLOSE or ROLL BACK + escalate to COO

ROLLBACK: ECR retains the prior image. `20260719-011554` is the last-known-good tag; re-tagging it to
`:latest` restores the current behaviour exactly, and no task-def or TF change has to be undone
because none is being made.

⚠ NOT CLAIMED YET: that the composition SUCCEEDS in-container. CVO verified the container port
@a4986d7ba5 (both halves run with no repo tree above them, driven by an external reader). This deploy
is the first time that runs on the real image, and step 5 is where it becomes a claim rather than a
prior. A `C2C3_COMPOSE_UNAVAILABLE|_SKIPPED|_FAILED` line is a legitimate outcome of this deploy and
would itself be progress -- it would be the first time the estate could SEE which failure it has.
