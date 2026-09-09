# CTO ADJUDICATION -- NFRA_OUTSET round 3, S24: the seam prefix switched group A on and group B's stand-in off; the honest FAILED is the interim, and group B's publish becomes a row

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~15:5xZ · **On:** `2.0.0_SA_COO` 94533 (drive tick 11.5), substrate
`0.7.0_AE_CloudOps~W`'s 94532 and row S24 @`65f88454c7` · **Prior:** @`98722f9355` (S23: drift is a device property), PRD v0.5
@`1ac8679844`, the round-2 analysis @`d6fd9eca07` (*a seam is two ends and a clock*).
**Verified at this seat before ruling:** `estate_report_runner.py:1409-1436` walks `OUTSET_GROUP_B_SOURCES` under the ONE seam
prefix, only absence advances, and a configured-and-empty prefix returns `INSTRUMENT_FAILED` by design ("never a silent
fall-through to the host stand-in"); `:1614` `OUTSET_FEDOBS_KEY = "comp_fedobs_coevolution.json"` (OS-s-14, file-pair grain from
the CSE log); the runner's own `reproduce` line names the producer: `python .tools/comp-fedobs coevolution --json`, published
through `org/modules/heatmap/outset_seam.py`. `infra/aws/globgrph/emit_fedobs_snap.py:39,50,56,115` -- the fedobs nightly writes a
STAGED HEALTH SNAPSHOT (`fedobs_coevolution_snap`, `_coevolution_payload`) to `opal-313476888478-globgrph`; that is a different
artifact at a different grain from the seam file the consumer was built for.

---

```
+-- CALL 1 of 1 -- S24 --------------------------------------------------+
  **The one seam prefix governs BOTH group A and group B. With it
  configured, group A turned ON (INSTRUMENT_UNAVAILABLE -> OK on the
  creation-boot read) and group B's declared host stand-in turned OFF:
  neither group-B key has a producer (W2-S15), so the runner returns
  INSTRUMENT_FAILED by contract and tomorrow's served report renders B
  FAILED. Accept the honest FAILED as the interim, and place the group-B
  publish as a row?**
  --------------------------------------------------------------------
  **REC --** (1) ACCEPT the honest FAILED for 09-10: a named absence under
  a configured seam beats a rendered stand-in; no revert, no ceiling
  raised, no stand-in re-enabled; the CVO reads B FAILED-BY-CONTRACT.
  (2) PLACE the group-B publish as a manifest row: comp_fedobs_coevolution
  .json to the seam from the fedobs producer's own existing nightly run,
  file-pair grain declared; the resource-grain producer (W2-S15) later.
  --------------------------------------------------------------------
  **RULING -- (1) ADOPTED as written. (2) ADOPTED as row OS-s-23 in PRD
  v0.6 NOW, with the mechanism sharpened: the seam artifact is DERIVED and
  published by the cloud-side publisher OS-s-21 already built, not copied
  from the fedobs nightly and not added to the fedobs ECS producer.**
+---------------------------------------------------------------------+
```

## WHY (1): both behaviours are correct by their own contracts, and the reader is better served by the truth

Group A now composes its key (the switch worked: the creation-boot read went UNAVAILABLE -> OK, real even though the run's
artifact is QA and the accept is the 09-10 fire). Group B under the same prefix says: *a publish was expected here and none
exists.* That is what happened. Reverting the prefix would put A back to UNAVAILABLE; re-enabling the stand-in under a configured
seam would render a host number under a "seam configured" run and tell the reader nothing about the missing publish -- the
runner's own comment at `:1425-1428` refuses exactly that. **INSTRUMENT_FAILED with the keys it looked for is the honest reading
until the publish exists.** No ceiling moves, nothing is reverted, and `3.0.0_SA_CVO` reads B on 09-10 as FAILED-BY-CONTRACT, not
as a regression of OS-s-20.

## WHY (2)'s mechanism is sharpened -- three facts the rec's "from the fedobs producer's own nightly run" runs into

1. **The nightly does not produce the seam artifact.** `emit_fedobs_snap.py` writes a staged health snapshot of the coevolution
   SIGNAL, gated on its health, to the globgrph bucket. The consumer OS-s-14 built reads `comp_fedobs_coevolution.json` -- the
   FILE-PAIR rows `comp-fedobs coevolution --json` derives from the CSE log (35,752 rows at OS-s-14, the rows W2-S21 taught the
   extractor to keep). Copying the snap would be the wrong shape; deriving inside the ECS producer would be a code change to a
   producer that runs on the SHARED image, i.e. an IMAGE ACT under R13 naming every family that pulls the tag. Neither is the cheap
   answer.
2. **A copy of an already-served artifact to a second key is a duplicate output path** (CLAUDE.md s.5). The seam artifact is
   not a copy: it is a DERIVED artifact that exists nowhere else, so publishing it creates one path, not two.
3. **The publisher already exists.** OS-s-21's cloud-side freshness publisher (CodeBuild on a blobless clone under a
   minimum-Put role, @`9ba4fdd9e9`) runs the tool surface on a schedule before the 13:00Z run. `comp-fedobs coevolution` reads
   the CSE log from the cloud, so it is clone-invariant like freshness and belongs to the same publisher.

## THE ROW -- OS-s-23, PRD v0.6, placed now (the v0.5 pattern: Andrew's 2026-09-03 scope-change word, cut by the loop)

| field | value |
|---|---|
| surface | THE GROUP-B PUBLISH: `outset/comp_fedobs_coevolution.json` at the seam -- `comp-fedobs coevolution --json` (file-pair grain from the CSE log) published through `outset_seam.py` by OS-s-21's cloud-side publisher as a SECOND ARTIFACT on the same fire, after the fedobs nightly (04:30Z) and before the 13:00Z run |
| claim | **absent** -- neither group-B key has a producer (W2-S15); under the configured prefix group B reads INSTRUMENT_FAILED by contract (S24) |
| lane / verb | `0.7.0_AE_CloudOps` (the publisher's role: its Put widened to the group-B key ONLY; one read line on the CSE log's location) / build |
| depends_on | OS-s-21 (the publisher and its role); OS-s-20 (DONE on the act) |
| accept | EXERCISED on a served day: group B renders from the seam artifact with its grain disclosed (`[grain=file-pair, NOT resource-grain]`, the runner's own line) and a NON-ZERO row count equal to the artifact's row count read independently at the CVO (W2-S21's lesson as the control), with a vintage inside the ceiling and later than that day's fedobs nightly; NEGATIVE ARM: with the publish disabled the stratum reads INSTRUMENT_FAILED by contract, never the stand-in; OUT-OF-CORPUS printed if the CSE log the tool read was empty |
| bound | the fedobs ECS producer and the shared image are NOT touched (R13); the snap on the globgrph bucket is not copied; the search order of `OUTSET_GROUP_B_SOURCES` (resource grain first) stays; **W2-S15, the resource-grain producer (`comp_cochange.json`), is a LATER row, named here and not cut**; the publisher's trigger is its own schedule -- a failed nightly leaves a stale CSE-log vintage on the artifact and the ceiling convicts it honestly |

## ON THE RESERVED ITEM (MSTR's card to Andrew, not this seat's)

The freshness publisher clones `origin/CLOUD` and cannot find its entrypoint until the assignee's commits reach origin; the push
hold LD-0522 is Andrew's. The architectural read, stated for the record and not ruled (it is inside the assignee's cell, and the
COO has named it to the assignee): **an S3-sourced entrypoint is Rule 12's own shape** (local -> S3 -> the box pulls its scripts) --
the way every gold runner on this estate deploys -- and it removes the push dependence from BOTH publishers. It also makes OS-s-23
independent of the same hold. That is the shape I would expect the lane to choose; it is the lane's call.

## WHAT THIS RULING DOES NOT DO

Revert the prefix · re-enable the stand-in · raise a ceiling · touch the fedobs ECS producer or the shared image · cut OS-s-23
(the COO's) · explain group C's FAILED -> OK flip on the creation-boot read (the assignee said it is unexplained; a row of its own,
not a finding of this ruling) · move OS-s-20's accept (the 09-10 fire, against the pinned baseline).

## Push state
LOCAL on commit; origin/CLOUD @`58adeff90c` by this seat's ls-remote at 15:22Z; LD-0522 hold standing.
