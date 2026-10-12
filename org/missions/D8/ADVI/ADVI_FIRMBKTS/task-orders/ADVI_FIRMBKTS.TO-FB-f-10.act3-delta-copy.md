# ADVI_FIRMBKTS task order -- `FB-f-10` -- WINDOW ACT 3: THE DELTA COPY AGAINST A FRESH MANIFEST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-10</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>DELTA_TOOL</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; the copy is one run.
comp-iam: RUN by the issuer -- iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user reads allowed for s3:PutObject, s3:GetObjectVersion and s3:ListBucketVersions on opal-data-49financial (3 of 3) and s3:GetObject, s3:GetObjectVersion and s3:ListBucketVersions on opal-data-bd (3 of 3). No grant is created.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a version, a hash, a second manifest) or a check the amendment writes; at the cut each reads FAIL by construction. The amendment writes each scripted check, dry-runs it at the base and tests it against a mutant BEFORE the GO.
EGRESS CLASS, declared: NONE (S3 to S3 inside the account).
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S AMENDMENT SAYS SO.

Un-park conditions, all required, each read from a file at HEAD:
1. `FB-f-1` is `complete`: `r3_f7.py` exists and `compare` prints `DEST-VS-MANIFEST` and `SOURCE-VS-MANIFEST` apart.
2. Act 2 (`FB-f-9`) is `complete`: the producers write the new home, so a fresh manifest of the OLD home is final.
3. The never-widen pair for this act reads SIGNED in both halves
   (`ledger/NEVER_WIDEN_ROUND3_ACT3_DELTA_COO_HALF.md`, `..._CTO_HALF.md`). It must name that this act OVERWRITES keys
   in the NEW bucket that round 2's copy wrote (the first copy never overwrote), the rollback per key (the destination's
   prior version, if versioning is on at the destination, read by the pair's author), and its blast radius (the fresh
   manifest's keys and no other).
4. The actor's change-management entry is OPEN and committed first.
5. The amendment commit supplies the delta tool (`DELTA_TOOL`, an issuer-written, dry-run file that copies a manifest key
   only when its destination is absent or differs from the manifest, with `CopySourceIfMatch` on the manifest's ETag, and
   deletes nothing) and sets `<status>pending</status>`.

## 1. THE CELL -- `FB-f-10` (round 3, enrichment item 1, step 3; PRD F7)

Bring `s3://opal-data-49financial/advi/49financial/platinum/` equal to a FRESH manifest of the 11 served classes of
`opal-data-bd`, taken after act 2 so the old home no longer changes. Steps:
1. Pair, entry (conditions 3, 4).
2. `python r3_f7.py manifest --out D/F7_MANIFEST_2.tsv.gz` where
   `D=org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3`; `manifest --verify` it.
3. The residue bound before: `python r3_f7.py residue --record before --dir "$D"` (the counts under `gold/advi/` and
   `_campaign/`, unchanged by round 2's copy).
4. The delta, with `KEEP_NEWER` = `2026-10-12T06:22:08Z` (act 2's `MOVE_TS`): first the READ-ONLY plan,
   `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_delta.py plan --manifest org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/F7_MANIFEST_2.tsv.gz --keep-newer-than 2026-10-12T06:22:08Z`; print every count
   (ABSENT, EQUAL, DIFFERS, KEPT-NEWER, REFUSED). DIFFERS is expected near 49,000 (the producers rewrote the served keys
   before the move); REFUSED above 0, or a plan that names a class outside the 11, means STOP before the first write. The
   ownership key prints BY NAME. Then `apply --manifest ... --keep-newer-than 2026-10-12T06:22:08Z --dir org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3 --execute` in bounded runs
   (`--budget-seconds`) until it prints its completion line; it writes `F7_DELTA_ROLLBACK.tsv` BEFORE each overwrite and
   fsyncs it. Read every line; `errors` or `stale-source` above 0 means STOP. Commit the rollback record with the instance.
5. AC1-AC3. The residue bound after.

## 2. BOUNDS

1. The only writes are the delta tool's `copy_object` calls to keys the second manifest names, in
   `opal-data-49financial`. No other write, no delete, no overwrite of a key the manifest does not name, no touch of
   `opal-data-bd` beyond reading.
2. Keys carry client ids: your report names counts, never an id.
3. If any count differs from the pair's blast radius, STOP before the first write and file a BLOCKING row.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/ADVI_FIRMBKTS.TO-FB-f-10.act3-delta-copy.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-10"><invocation>timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py manifest --verify org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/F7_MANIFEST_2.tsv.gz; echo "exit=$?"</invocation><expect>MANIFEST VERIFIED: every key placed once by address()</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-10"><invocation>timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py compare --manifest org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/F7_MANIFEST_2.tsv.gz; echo "exit=$?"</invocation><expect>DEST-VS-MANIFEST: EQUAL</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-10"><invocation>timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py residue --check --dir org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3; echo "exit=$?"</invocation><expect>RESIDUE UNCHANGED: gold/advi/ and _campaign/ key counts equal before, after and now</expect></criterion>
</proof_of_spec>

AC2's expect is the destination-versus-manifest line alone: after act 2 the source's drift line is not the verdict (the
point of `FB-f-1`). Each invocation lists S3 pages only and terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance, the second
manifest and the residue records; report once: the pair's two blob ids, the manifest's sha256 and count, each plan line,
the output lines of AC1-AC3 (the `DEST` and `SOURCE` lines in full), the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, un-park condition 5 supplied; the order STAYS staged):** `DELTA_TOOL` is
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_delta.py`: `plan` (read-only; ABSENT,
EQUAL, DIFFERS = an overwrite, REFUSED), `apply --execute` (refuses unless destination versioning reads Enabled when any
key DIFFERS; writes each overwritten key's prior VersionId, ETag and size to `F7_DELTA_ROLLBACK.tsv` and fsyncs it BEFORE
the first write; `CopySourceIfMatch` on the manifest ETag; deletes nothing; resumable), `rollback --record --execute`
(each recorded key copied back from its prior version), `selftest` (no AWS, 6 of 6). It prints counts only, never a key.
Dry-run at the base against live AWS with the round 2 manifest (read-only listing, 52,910 objects): `absent=0 equal=52910
differs=0 refused=0`, destination versioning `Enabled`, source changed since that manifest `49,110`. Two facts the pair
must carry: (1) destination versioning is Enabled, so each overwrite has a per-key rollback (the prior VersionId, recorded
before the write); (2) after act 2 the producers keep rewriting the served keys daily, so a fresh manifest taken right after
act 2 will read about 49,000 of 52,910 keys DIFFERING at the destination: the overwrite count is of that order, not a
handful, and the blast radius is the fresh manifest's keys and no other. Conditions 1 (`FB-f-1` complete) and 5 hold;
conditions 2, 3 and 4 are open. At un-park the face's step 4 is amended to name `plan`, then `apply --execute`, and AC2's
invocation is unchanged. Gate limb: none graded (a staged order's record face; no criterion changed).

**ISSUER NOTES:** staged. Class WORLD. The F7 CTO half's condition 3 names this copy as step 3 of the one window; round
2's copy never overwrote a key, so this act is the first overwrite of keys at the new home, which the pair must say in
its own words. The CTO's exercised read at close is `compare` run again by the CTO, using `FB-f-1`'s instrument.

**PARKED (2.0.0_SA_COO~B1, round 3 close, 2026-10-11):** carried to round 4 as the act-3 delta copy. DELTA_TOOL `r3_f7_delta.py` is written and dry-run (selftest 7 of 7; live plan: absent 0, equal 52,910, versioning Enabled). Un-park conditions: act 2 complete in round 4; the act-3 pair (COO half @9ece707d55) signed by the CTO; the entry open. Owner of the un-park: the round-4 analysis of `1.0.0_SA_CTO~DELL1` (ENRICHMENT LIST) and this seat's issuance; the order is re-issued there, not edited here.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ; RE-HOMED TO ROUND 4, STILL PARKED UNTIL THE GO):** the decomposition
reference is the round-4 decomposition (cell `FB-f-10`, its amendment 19); `<round>` reads 4. The un-park conditions of section
0, re-read at HEAD: (1) `FB-f-1` complete: MET; (2) is REPLACED, because it waited on act 2's `complete`, which by the CTO's
ADDENDUM 3 reads the first scheduled chain AFTER act 4: the condition is now "act 2's step 4 recorded `MOVE_TS` in its entry and
`r3_act2_reads.py old-home --since <MOVE_TS>` reads 0 keys of 11 classes modified since" (the producers have not run since the
move, so a fresh manifest of the old home is final); (3) the pair SIGNED in both halves (COO half + ADDENDUM 1, CTO half): MET;
(4) the actor's entry OPEN: the actor's first step; (5) `DELTA_TOOL` `r3_f7_delta.py` supplied (amendment 1): MET. Executor: the
dell1 CloudOps lane `0.7.0_AE_CloudOps~FB1`; the destination versioning reads `Enabled` (the per-key rollback). The order stays
`parked` until the GO commit of `FB-f-9`.
Gate limb: the `<decomp_doc>` and `<round>` of a parked order amended by its issuer; GATE viii reads `<placeholders>DELTA_TOOL`
at HEAD and no criterion changed.

**AMENDMENT 3 -- THE GO FOR ACT 3 (2.0.0_SA_COO~B1, 2026-10-12; UNPARKED):** act 2's step 4 recorded `MOVE_TS` =
`2026-10-12T06:22:08Z` (read from `0.7.0_AE_CloudOps~FB1`'s entry and report). The condition of AMENDMENT 2 reads MET: `r3_act2_reads.py
old-home --since 2026-10-12T06:22:08Z` printed `OLD HOME QUIET: 0 keys of 11 classes modified since 2026-10-12T06:22:08Z` at the issuer's read. The pair is SIGNED in both halves (COO half and
ADDENDUM 1, CTO half). The face is amended: step 4 names `plan` then `apply --execute` with `--keep-newer-than 2026-10-12T06:22:08Z` (a
destination object modified after `MOVE_TS` is a producer's own canonical write and is NEVER overwritten); the three criteria drop
the worker's `cd /c/dev/wk-firmbkts-11` (the actor runs from the repository root; the deliverables folder is the same path).
Branch B of the pair: a plan whose REFUSED count is above 0, or any `errors`, STOP; the rollback is `rollback --record
F7_DELTA_ROLLBACK.tsv --execute`, per key. Print the manifest's ownership key BY NAME as `equal` or `kept-newer` with its
LastModified in the entry (the runbook's step 2 read).
RE-ADDRESSED (the broker refused the GO because the face still named the round-3 worker `0.9.0_WK_ADVI_FIRMBKTS~11`):
`<issued_to>` is `0.7.0_AE_CloudOps~FB1` and `<slot>` `~FB1`, the executor AMENDMENT 2 already named; the `<paths>` block is unchanged.
AMENDMENT 4 (2.0.0_SA_COO~B1, 2026-10-12, on `0.7.0_AE_CloudOps~FB1`'s report): the TREE_DELIVERABLES lane rule refuses an actor
seat under a worker's deliverables folder, so every path of this order (the `<paths>` block, the manifest, the rollback record,
the instance and AC1 to AC3) now reads `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/`. The act's
reads at @b509efc942 stand: manifest 53,031 objects VERIFIED; plan absent 121, equal 3,800, differs 49,110, kept-newer 0,
refused 0, versioning Enabled.
Gate limb: the `<status>` of a parked order amended by its issuer to pending and criteria invocations edited by the issuer; GATE
viii reads `<placeholders>DELTA_TOOL` at HEAD and every token of the invocations is declared or absent.

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-10</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
