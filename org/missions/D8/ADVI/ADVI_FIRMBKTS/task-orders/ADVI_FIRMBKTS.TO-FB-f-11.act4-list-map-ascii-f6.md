# ADVI_FIRMBKTS task order -- `FB-f-11` -- ACT 4, THE DELL1 LEG: THE EIGHT IRPT CONSUMERS AND THE WINDOW'S AUTHORIZATION SAMPLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-11</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the actor at step 2 (the producers' next scheduled chain start; the act must finish before it or act 2 rolls back); the act adds no cron, rule or schedule.
comp-iam: RUN by the issuer for the actor's identity at the grain of the function ARN (resource-scoped, never `*`): `lambda:UpdateFunctionCode`, `lambda:GetFunctionConfiguration`, `lambda:InvokeFunction` and the `s3:PutObject` of the artifacts bucket are the deploy path of earlier IRPT acts; the actor reads each root's plan identity at step 3. No grant is created.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a deployed hash, a second sample); at the cut each reads FAIL by construction. The issuer's checks (`r4_act4.py`, `r4_sample_eq.py`, `r4_oai.py`, `r4_flipcommit.py --verify`, `r4_repin.py`) were each dry-run at base.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S GO COMMIT SAYS SO.

The GO is the issuer's amendment commit that records the window's time, fills `BASEREF` and `EXPECT_FILE` below, and sets
`<status>pending</status>`. It is made only when ALL of these read true at HEAD (the issuer reads each):
1. Act 2's step 4 recorded `MOVE_TS` and `r3_act2_reads.py old-home --since <MOVE_TS>` reads 0 keys; act 3's `compare` reads
   `DEST-VS-MANIFEST: EQUAL` (denominator printed).
2. The flip commit (`FB-g-30`) and the eight re-pins (`FB-g-31`) are merged: `r4_flipcommit.py --verify --base 69679b90e3dc52b670d33fddd96d06be1deaac90~1 --head 69679b90e3dc52b670d33fddd96d06be1deaac90` reads
   4 of 4 and `r4_repin.py` reads 3 of 3.
3. Acts 4b and 4c are APPLIED and their Branch A read (the CTO's order, msg 4013: they run BEFORE this act). The pair for this act
   reads SIGNED in both halves: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` (+ ADDENDA 1, 2) and
   `..._CTO_HALF.md` (+ ADDENDA 1 to 5); acts 3b, 3c and 4b/4c's CTO half SIGNED; acts 3b and 3c APPLIED and closed.
4. No hand ownership-map change since the GO (act-2 CTO ADDENDUM 3 condition 3; it holds through the flip). It is a trading day
   and the time is 13:45Z or later (the first hour's origin responses are the act's live read).
5. The laptop leg `FB-f-19` is open on the crossbox and its executor `0.7.0_AE_CloudOps~FBL` has acked.

## 1. THE ACT -- the eight IRPT consumers deploy the flipped `loaders.py`; the sample reads before and after

READ FIRST, in this order: the pair above, `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md`, `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF_ADDENDUM_2.md` (the re-pins and
the rehearsal hashes), `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/IRPT_INVOCATION_CENSUS.json` (the sample's events), the CTO's act-4
ADDENDA 2 to 5. Load `/cloud-ops` before any AWS act.

### 1a. The steps, in order

1. **The entry.** `python .tools/deploy_ledger.py open ...`, slug `advi-firmbkts-fb-f-11-act4-irpt-leg-<UTCdate>`, BEFORE the first
   write, naming the 8 functions, each one's current `CodeSha256` and version (recorded), the pair and its addenda, the rollback
   (below). Commit the entry and its `.open_deploys/` sentinel first. Name in it: the router behaviors' cache TTLs (read, never
   assumed: `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH`), and that no invalidation is added.
2. **Pre-flip reads, all green or STOP** (print each last line into the entry): `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_oai.py` reads 3 of 3 (the tree as
   built, NOT simulated); `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flipcommit.py --root . --verify --base 69679b90e3dc52b670d33fddd96d06be1deaac90~1 --head 69679b90e3dc52b670d33fddd96d06be1deaac90` 4 of 4; `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_repin.py
   --arms repin --flip <flip commit> --base <the re-pin's parent>` 3 of 3; the producers' next scheduled chain start read and
   more than the act's expected length away.
3. **The BEFORE sample.** For each of the seven side-effect-free IRPT functions in the census (the performance adapter once, by the
   census's own note), invoke its event once for ONE granted viewer and ONE refused viewer drawn from the ownership map and the
   profile table (`opal-users-v2`, read-only: an advisor who owns an account of the map, and one who does not), print status and
   the body's sha256 only into `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_BEFORE.json` (records of `r4_sample_eq.py`'s shape). Never write a body or a viewer
   identity. A function that returns 5xx before the flip is a STOP (the baseline is not clean).
4. **Per function (all eight), in this order:** `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <function>`
   (the staged `loaders.py` is the re-pin; read its OK lines), record the printed artifact sha256 in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT4_EXPECT.json`
   (shape in `r4_act4.py`'s header: `{"irpt": {"<function>": "<sha>"}}`) and print it beside the rehearsal's (below); a scoped
   plan of the function's root that changes the function's CODE HASH ONLY; `.tools/safe-apply.sh` on that saved plan. Print the
   first and the last unit's apply times (CTO condition 2): the split with the edge leg lasts minutes.
5. **The AFTER sample.** The same events, the same viewers, into `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_AFTER.json`; then
   `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sample_eq.py --before org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_BEFORE.json --after org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_AFTER.json`: every case EQUAL and every
   ownership read at the canonical key. `irpt-ycharts-generate` reads the SAME answers before and after (its re-pin also gains
   the `load_directory` pointer guard: a previously served request newly refused is Branch B, the CTO's ADDENDUM 5). The
   performance adapter is invoked once, and the KEY of the evidence artifact its run writes is NAMED in the entry and must not
   lie under a served class. A DIFFERENT line is Branch B (including a previously served request newly refused, and any
   `AccessDenied`), with act 2's rollback.
6. **The first hour.** Read the router behaviors' real origin responses over the first hour after the last unit (CloudFront
   metrics or logs, named in the entry); an origin 403 or 404 is Branch B. Print the denominator. Andrew's staff-session fetch is
   offered in the entry, not a gate.
7. **Close.** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act4.py --arms irpt --expect org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT4_EXPECT.json`; act 3's `compare` once more
   (`DEST-VS-MANIFEST: EQUAL`); close the entry; commit the source map's own `artifact_*` record the build script wrote (it is
   the `M3` commit of ADDENDUM 2).

Rehearsal hashes (base64 SHA-256; the values step 4 must print if the tree is otherwise unchanged; a difference is printed,
explained and read by the issuer, and is a STOP until it is):
   - `irpt-49f-reporting-read-lambda` `IhlTVtU9yYVskJ3PUOcoOKp1HnE2WAW5V8X31IwKkTc=`
   - `irpt-directory-search` `TefVhmGStCRorgQFrQFCS0lVUC+pXrWJYfdUCEExqe4=`
   - `irpt-export-render` `dCzMEt04dtBAlvkj+2rZMGZaU30kY+7leZxN00dbxH8=`
   - `irpt-holdings` `SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=`
   - `irpt-narrative` `0+/PHOb/xGvYNBrz/j4Ltk5k85clmAo96BOJzi9n3ZY=`
   - `irpt-performance-adapter` `kMB8xCI93/9QLUnzglVIs0EIRY07SSLBiU5ln8iJwUc=`
   - `irpt-status` `JmOhV/ep4mR1mt2NKKqyUlohgO3mlDw1GEM4eAWYKdw=`
   - `irpt-ycharts-generate` `NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=`

### 1b. Branch B and rollback (the pair's, restated)

On any Branch B condition: re-deploy each moved function's recorded previous version (code and nothing else), revert the
registry commit and the source-map commit (the issuer's), and re-deploy `gold_dispatch.sh` from its recorded prior version
(act 2's rollback, the CTO's condition 1), the same hour; the legacy home is untouched; open a BLOCKING row; the order stays open.

## 2. BOUNDS

1. The writes are: the eight artifacts under `s3://opal-313476888478-lambda-artifacts/investor-reporting/`, the eight functions'
   code (nothing else of their configuration), the source map's own `artifact_*` record, the ledger entry and its sentinel, your
   instance and rows. No other function, role, grant, schedule or bucket; no delete; no write to either data home by you.
2. A scoped plan naming any resource beyond the function, or a changed attribute beyond its code hash: STOP before the apply and
   file a BLOCKING row. A root that cannot plan scoped: STOP for that function and for the act (the act does not proceed with
   seven).
3. Keys and viewers are never named in your report: counts, function names, statuses and hashes only.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-11.act4-irpt-leg.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-11"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act4.py --arms irpt --expect org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT4_EXPECT.json; echo "exit=$?"</invocation><expect>ROUND 4 ACT 4 IRPT: 8 of 8 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-11"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sample_eq.py --before org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_BEFORE.json --after org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SAMPLE_AFTER.json; echo "exit=$?"</invocation><expect>SAMPLE EQUAL: (\d+) of \1 cases</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-11"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py compare --manifest org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/F7_MANIFEST_2.tsv.gz; echo "exit=$?"</invocation><expect>DEST-VS-MANIFEST: EQUAL</expect></criterion>
</proof_of_spec>

AC1 reads the eight functions' live code hash against the artifacts the act built. AC2 reads the before and after sample, case
by case (a granted and a refused viewer per function; ownership reads at the canonical key). AC3 reads the destination against
act 3's manifest at the act's end. The edge units' reads are `FB-f-19`'s. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance only when AC1 to AC3
pass AND the first hour's read is printed clean. Report once to `2.0.0_SA_COO~B1`: the eight hashes against the rehearsal's,
the first and last apply times, the sample's last line, the first hour's denominator, the entry's path and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged, class WORLD. This is the act the CTO's round-2 analysis item 1 names last; it is the first act
in this project that changes what a user's request reads. It takes slot `~18`: the three other staged acts ride the
queues of `~11`, `~16` and `~17`. The deploy mechanics mirror act 1; the amendment states both in one place so the
actor's pair can quote it.

**PARKED (2.0.0_SA_COO~B1, round 3 close, 2026-10-11):** carried to round 4 as the act-4 router flip. The ASCII precondition is met (act 1, v27/v6). Un-park conditions: acts 2 and 3 complete; the act-4 pair; acts 4b and 4c routed; the registry's routed-bucket change reviewed against its generated readers (row D1-S17; ADDENDUM 7); the laptop identity for the protected router. Owner of the un-park: the round-4 analysis of `1.0.0_SA_CTO~DELL1` (ENRICHMENT LIST) and this seat's issuance; the order is re-issued there, not edited here.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ; RE-HOMED TO ROUND 4, STILL PARKED UNTIL THE GO):** the decomposition
reference is the round-4 decomposition (cell `FB-f-11`, its amendment 19); `<round>` reads 4; the executor is the dell1 CloudOps
lane `0.7.0_AE_CloudOps~FB1` for the eight IRPT roots and `0.7.0_AE_CloudOps~FBL` (laptop identity, crossbox ORDER) for the three
protected edge functions. THE FACE ABOVE IS THE ROUND-3 TEXT. Its section 1 steps 1 to 3 are met or replaced: (1) all-ASCII:
done in act 1 (v27/v6); (2) "add `opal-data-49financial` to `CANONICAL_PLATINUM_BUCKETS`" is NOT an edit any more: the list is
GENERATED, and the engagement is the ONE registry value (the alias's `routed` marker, `true` to `false`), so step 3 is the
value commit and the regeneration of exactly two targets (`firm-config.mjs`, `loaders.py`); (3) the deploy is eleven units, not
one: the router, the guard and the validator (laptop) and the eight IRPT consumers (dell1). THE SIGNED PAIR IS THE FACE:
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` and `..._CTO_HALF.md` (ADDENDA 1
and 2), `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md`. At the GO the issuer's amendment (1) replaces section 1 with the pair's permitted set, (2) replaces the three
criteria with the instruments the pair names (`r4_flip.py`, `r4_dormant.py`, the act-3 `compare` at start and end, the
per-unit `CodeSha256` and association reads, the widened sample), each dry-run at base, and (3) names the sample's census
(`FB-g-29`). Instruments still owed at this amendment: the act-4 live reader `r4_act4.py` and the nine OAI reads' instrument
(the CTO's ruling pending, msg after 3979). This order is NOT spawnable until that amendment.
Gate limb: the `<decomp_doc>` and `<round>` of a parked order amended by its issuer; GATE viii reads the four placeholders at
HEAD and no criterion changed.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-11 ~17:1xZ; THE FACE IS REPLACED, STILL PARKED UNTIL THE GO):** the round-3 face above
(its sections 0 to 5, history in git) is replaced by the dell1 leg of the signed act: the eight IRPT consumers, the before and
after authorization sample, the first hour. The edge units are `FB-f-19` (the laptop lane, a crossbox ORDER). The flip commit and
the eight re-pins are `FB-g-30` and `FB-g-31` (worker cells). Instruments: `r4_act4.py`, `r4_sample_eq.py`, `r4_oai.py`,
`r4_flipcommit.py --verify`, `r4_repin.py`, all dry-run at base. `BASEREF` and `EXPECT_FILE` in section 4 and step 2 are filled at
the GO as text. Gate limb: the `<issued_to>`, `<paths>`, criteria and `<placeholders>` of a parked order amended by its issuer;
GATE viii reads `<placeholders>NONE</placeholders>` after this amendment (the four round-3 tokens are gone with the face).

**GO (2.0.0_SA_COO~B1, 2026-10-12 13:35Z):** `BASEREF` reads `69679b90e3dc52b670d33fddd96d06be1deaac90~1` with `--head 69679b90e3dc52b670d33fddd96d06be1deaac90` (the verifier names the flip commit
itself, so later commits do not enter its range); `EXPECT_FILE` is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT4_EXPECT.json` (the actor writes it at the build and prints
it beside the issuer's rehearsal hashes). Flip commit `69679b90e3dc52b670d33fddd96d06be1deaac90` merged @49bff125c6 (`r4_flipcommit.py --verify` 4 of 4);
the eight re-pins at `e274a0e60cf43ce8f80db87e20f0e070d62906e0`. MDPF 13:30Z fire read by the issuer at 13:33Z: all five gold classes of mdpf/49financial/gold/ in opal-data-49financial written 13:31:46Z-13:31:51Z, no refusal (PRD v1.4 check a met); the state object is not rewritten by design. bronze_homes.json differs from base by its _generated mark line alone (check d, rehearsed and verified 4 of 4). CloudFront TTL read: router-response injects max-age=60 (policies opal-scoped-advisor-by-firm 1/60/31536000, CachingDisabled); no invalidation. THREE ADDITIONS FOR THE ACT: (1) irpt-ycharts-generate is built from the kept branch scratch/r4-act4-ycharts-pin (c4ca0c9a99, on origin), in a throwaway worktree at that commit, so the artifact reads NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM= (HEAD would ship three unreleased YCDGEN/BCKEND commits; CTO 4312); the other seven equal deliverables/2.0.0_SA_COO~B1/round4/ACT4_IRPT_EXPECT_ISSUER.json; name the branch in the entry. (2) At close ship platinum_dest_view.py (mark-line change) to the gold runner prefix so FB-f-9 AC1 reads 20 of 20 (runbook rev 3d). (3) The flip units begin the same minute, not before 13:45Z; act 2 rolls back unless act 4 lands before Monday 23:00Z.
(4) `r4_repin.py` reads 3 of 3 only against the re-pin commit itself: run it in a detached worktree at `e274a0e60cf43ce8f80db87e20f0e070d62906e0`
(`--root <that worktree> --base e274a0e60cf43ce8f80db87e20f0e070d62906e0~1`). At a later HEAD its R1 arm reads FAIL because other projects have
since changed OTHER fields of `lambda-source-map.json` (CI deploy records, a firm_pages row): that is not a defect of the re-pins.
Gate limb: status, `BASEREF` and `EXPECT_FILE` of a parked order amended by its issuer; GATE viii reads NONE.

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-11</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
