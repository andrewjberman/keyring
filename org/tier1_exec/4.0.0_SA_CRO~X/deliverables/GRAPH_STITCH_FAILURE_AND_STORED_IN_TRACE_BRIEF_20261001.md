# The dependency graph: last night's failed stitch build, and the absent STORED_IN edges

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103742 (RULINGS batch 85 item 3 @afc17452e8), on rows `ESTATE_GOVERNANCE-S16` and
`ESTATE_GOVERNANCE-S17` (`org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md` @22746eedf5, `3.0.0_SA_CVO`).

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (read 12:47Z to 13:15Z). Read-only: build and run logs, the
published stitch artifact, the served graph through `comp-kuzu`, image and schedule metadata, and source at CLOUD. No
build, no re-run, no write.

## The two answers

**1. Why the 03:00Z build exited 2.** The producer built its graph and then refused to emit it. Its size check
(the grain sentinel) found one class out of band, and `derive_stitch.py:773-777` returns 2 on any violation. The log
line:

    GRAIN-SENTINEL: FAIL (1 violation group(s))
      [AC-GRAIN.2] SCHEDULE: count 26 vs baseline 10 = 2.60x (outside [0.4, 2.5]x band)
    ERROR: GRAIN_SENTINEL_FAIL -- refusing to emit grain-violating stitch graph

The baseline is `org/modules/graph/grain_baseline.json` (`SCHEDULE`: 10; the file's base certification is dated
2026-06-11, and whether `SCHEDULE` was among its later recertifications was not read); the band is
`org/modules/graph/grain_sentinel.py:66-67` (0.4 to 2.5). Two schedules were created on 2026-09-30 at 10:40:19Z,
`etfs-rivalfunds-daily` and `etfs-rivalfunds-sweep-daily`. That took the live count from 24 (2.4x, inside the band;
the 09-30 build read `GRAIN-SENTINEL: PASS`) to 26 (2.6x, outside it).

**This is not a one-night failure.** Nothing about tonight differs: the count is still 26 and the baseline is still
10. Every nightly build fails the same way until the `SCHEDULE` baseline is recertified. That file has been
recertified for exactly this cause before (its last three commits are recertifications or their sign-off).

**The served graph's vintage now.** The projection reads "built from the estate as of 2026-10-01 12:52:57 UTC.
Stitch source: stitch-codebuild built 2026-09-30T03:01:20Z". The nightly derive ran at 02:12Z today and folded the
09-30 stitch. The derive runs before the stitch build each night (02:12Z, then 03:00Z), so the stitch layer is a day
old on a good night; it is one further day old for every failed build.

**2. Where STORED_IN is dropped.** At the fold, inside the nightly derive, and the cause is not in the code at
CLOUD: **the running derive is older than the fold it is supposed to run.**

- The producer emits them. Both builds print `'stored_in': 137`, and the published artifact
  (`s3://opal-313476888478-globgrph/stitch/stitch_graph.json`, written 2026-09-30T03:01:34Z) holds 137 `STORED_IN`
  edges, each from an `S3Key` node to a bucket ARN (`derive_stitch.py:339`).
- The fold rejects them. The derive's log at 2026-10-01T02:12:06Z:
  `STITCH_INGEST nodes=446 edges=728 ... skipped_edge_unresolved=2019`. The artifact holds 2,747 edges of the five
  stitch types; 728 + 2,019 = 2,747. The served graph holds exactly 728 edges on the `inter` layer: `DERIVES_FROM`
  218, `READS` 292, `WRITES` 218. So all 137 `STORED_IN` (and the 20 inter `ROUTES_TO`) are among the 2,019.
- The reason is the endpoint test. At CLOUD the fold admits an edge whose ends match EITHER identity of a node, its
  short id or its ARN (`infra/aws/globgrph/derive_runner.py:2535-2549`, `_stitch_endpoint_keys` at `:2441-2457`). That
  widening arrived in commit d4b17b4f6f, 2026-09-10T05:57:41Z, the same commit that made the producer emit the ARN.
  Its own comment says the two must move together: "either alone reads as a regression to zero" (`:2448-2449`).
- The image the derive runs was pushed 2026-09-10T01:09:39Z
  (`opal-globgrph-derive-runner@sha256:17ccc9b0..`, task definition `globgrph-derive-runner:9`), 4 hours 48 minutes
  BEFORE that commit. In the file as it stood then the test is `source in ids and target in ids`, short ids only
  (line 2348 of the parent revision). A bucket's ARN is not a short id, so every `STORED_IN` edge fails it.
- The producer, by contrast, runs source at HEAD every night (CodeBuild, marker `git_sha 0c955d54..`). One plane
  moved; the other was never rebuilt.

Corroboration from the run itself: the fold at CLOUD prints an `ENDPOINT_CANONICALIZE` line on every derive
(`derive_runner.py:2426`, called at `:2751`). The log of today's derive holds 0 lines matching `ENDPOINT_`; the
positive control, `STITCH_INGEST`, is present in the same window.

Row S16 records "the running updater equals HEAD". That read compared the incremental-updater Lambda. The fold does
not run there; it runs in the derive's container, which is the unit that is stale.

## Start-to-finish walk

### 1. Estate snapshot and source -> `derive_stitch.py` (CodeBuild `opal-stitch-produce`, 03:00Z) -- INCOMPLETE

What exists: nine successful nightly builds of the last ten; the producer runs CLOUD source.

The exact gap: the build refuses to emit when any class leaves a fixed band around its certified baseline. Estate
growth of two schedules stops the whole stitch layer.

Close: recertify `SCHEDULE` in `grain_baseline.json` (a signed act by its owner). Proof: tomorrow's 03:00Z build
reads `GRAIN-SENTINEL: PASS` and writes a marker dated that night. The sentinel's own report line also says 24 of 59
live node types are not band-checked at all.

### 2. Stitch artifact -> the fold in the nightly derive (ECS `globgrph-derive-runner`, 02:12Z) -- MISMATCHED

What exists: `fold_stitch_document` at CLOUD, correct for the producer's output.

The exact mismatch: the deployed image predates the fold's half of commit d4b17b4f6f. The producer names a bucket
by ARN; the deployed fold resolves by short id only.

Close: rebuild and deploy the derive image from CLOUD (`globgrph-derive-build`, last run 2026-09-10T01:08:31Z), under
its deploy ledger. Proof: the next derive logs an `ENDPOINT_CANONICALIZE` line and a `STITCH_INGEST` whose
`edges=` rises by the 137, and `comp-kuzu` counts 137 `STORED_IN`.

### 3. Derive output -> the served projection -- WORKS

The projection worker loaded 62,488 edges today and skipped 403 for a missing endpoint. It loads what the derive
committed. The 27 `SERVED_FROM` edges that land on bucket-POLICY nodes are plausibly the same stale image: commit
d4b17b4f6f's subject names `SERVED_FROM` as moved onto the ARN too. Its diff for that builder was not read here.

## Recommended completion sequence (PROPOSAL -- the CTO rules)

1. The `SCHEDULE` recertification, today: it is the only thing between the estate and a stitch layer that ages a day
   every night.
2. The derive image rebuild and deploy. It also carries whatever else landed in `infra/aws/globgrph/` since
   2026-09-10T01:08Z; that list was not enumerated here and belongs in the deploy's packet.
3. An owner. The graph pipeline has no project and no seat (row S16's own note), and both findings are the kind an
   owner's routine catches: a baseline that estate growth will trip again, and an image that lagged its source for
   three weeks while a row recorded "equals HEAD".

## Acceptance

One trace of one edge: a named data key's `STORED_IN` edge in the artifact, the derive's ingest line admitting it,
and the same edge returned by `comp-kuzu`, at a stitch vintage dated that night.

## Evidence anchors and limits

Source at CLOUD HEAD at 13:1xZ. Machine-readable evidence:
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/graph_stitch_trace_20261001/EVIDENCE.json`.

Limits. The deployed image was not pulled and its `derive_runner.py` was not read: that it lacks the widened test
rests on three things that agree -- the push time against the commit time, the absent log line with its positive
control, and the fold's counts matching the short-id rule to the edge. Which of the 2,019 unresolved edges are which
type is derived by subtraction from the served counts, not read from the fold. The 24-to-26 step in `SCHEDULE` is
read from the two schedules' creation times and the two builds' sentinel lines; the 09-30 snapshot's own count was
not opened.

- `infra/aws/globgrph/derive_stitch.py:52`, `:91`, `:108`, `:339`, `:773-777`
- `infra/aws/globgrph/derive_runner.py:2275`, `:2441-2457`, `:2535-2549`, `:2562-2566`, `:2738`, `:2751`
- `infra/aws/globgrph/kuzu_nessie_load.py:259-263`
- `org/modules/graph/grain_sentinel.py:66-67`, `org/modules/graph/grain_baseline.json`
- CodeBuild `opal-stitch-produce` builds 88fdb880 (FAILED) and a6a66cd3 (SUCCEEDED); log group
  `/ecs/globgrph/derive-runner`; log group `/aws/ecs/opal-globgrph-projection-worker`

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z, recorded in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this surface reached this seat as msg 103742.

> You have 4.0.0_SA_CRO~X as your research partner so as you see projects developing, if you assess there needs to be
> higher resolution on any part of the development process, you have CRO~X run /closer trace on the given surface and
> assess the strategic way forward.
