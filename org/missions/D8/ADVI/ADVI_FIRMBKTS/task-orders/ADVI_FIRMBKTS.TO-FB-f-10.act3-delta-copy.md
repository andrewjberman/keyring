# ADVI_FIRMBKTS task order -- `FB-f-10` -- WINDOW ACT 3: THE DELTA COPY AGAINST A FRESH MANIFEST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~11</issued_to>
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
   `D=org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11`; `manifest --verify` it.
3. The residue bound before: `python r3_f7.py residue --record before --dir "$D"` (the counts under `gold/advi/` and
   `_campaign/`, unchanged by round 2's copy).
4. The delta: `DELTA_TOOL` over the second manifest, in bounded runs, until it prints its completion line. Read every plan
   line; a `refused`, `errors` or `stale-source` above 0 means STOP.
5. AC1-AC3. The residue bound after.

## 2. BOUNDS

1. The only writes are the delta tool's `copy_object` calls to keys the second manifest names, in
   `opal-data-49financial`. No other write, no delete, no overwrite of a key the manifest does not name, no touch of
   `opal-data-bd` beyond reading.
2. Keys carry client ids: your report names counts, never an id.
3. If any count differs from the pair's blast radius, STOP before the first write and file a BLOCKING row.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/ADVI_FIRMBKTS.TO-FB-f-10.act3-delta-copy.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-10"><invocation>cd /c/dev/wk-firmbkts-11 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py manifest --verify org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/F7_MANIFEST_2.tsv.gz; echo "exit=$?"</invocation><expect>MANIFEST VERIFIED: every key placed once by address()</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-10"><invocation>cd /c/dev/wk-firmbkts-11 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py compare --manifest org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/F7_MANIFEST_2.tsv.gz; echo "exit=$?"</invocation><expect>DEST-VS-MANIFEST: EQUAL</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-10"><invocation>cd /c/dev/wk-firmbkts-11 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py residue --check --dir org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11; echo "exit=$?"</invocation><expect>RESIDUE UNCHANGED: gold/advi/ and _campaign/ key counts equal before, after and now</expect></criterion>
</proof_of_spec>

AC2's expect is the destination-versus-manifest line alone: after act 2 the source's drift line is not the verdict (the
point of `FB-f-1`). Each invocation lists S3 pages only and terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance, the second
manifest and the residue records; report once: the pair's two blob ids, the manifest's sha256 and count, each plan line,
the output lines of AC1-AC3 (the `DEST` and `SOURCE` lines in full), the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged. Class WORLD. The F7 CTO half's condition 3 names this copy as step 3 of the one window; round
2's copy never overwrote a key, so this act is the first overwrite of keys at the new home, which the pair must say in
its own words. The CTO's exercised read at close is `compare` run again by the CTO, using `FB-f-1`'s instrument.

<status>staged</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-10</to_id>
<slot>~11</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
