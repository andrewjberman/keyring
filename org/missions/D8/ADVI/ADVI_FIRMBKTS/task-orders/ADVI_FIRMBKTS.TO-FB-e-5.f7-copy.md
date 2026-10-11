# ADVI_FIRMBKTS task order -- `FB-e-5` -- F7: COPY 49 FINANCIAL'S SERVED PLATINUM KEYS TO THEIR NEW HOMES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~8</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; the copy is one run.
comp-iam: RUN by the issuer -- simulate-principal-policy on user/cloudops-dell1-agent-user reads allowed for s3:PutObject and s3:GetObject; the destination bucket policy's admit list names that user (denominator: 7 admitted patterns on the policy). No grant, role or policy is created.
comp-adversary: RUN by the issuer -- r2_f7.py manifest --verify 52,910 of 52,910 placed, 0 refused, 0 destination collisions on the issuer's L5 manifest; compare reads present 0, missing 52,910 before the copy; at base every criterion reads FAIL (manifest absent). Blindness: the lens cannot see the producers' next write window (about 05:30Z-06:15Z); the copy refuses a key whose source moved (stale-source) rather than copy it.
EGRESS CLASS, declared: NONE (S3 to S3 inside the account).
</preflight>

## 1. THE CELL -- `FB-e-5` (round 2, enrichment item 4; PRD F7)

You COPY (never move) the 11 served platinum classes of `s3://opal-data-bd/` into `s3://opal-data-49financial/` at the
keys `lib/opal_naming.py address()` builds from the round-1 table, with the issuer's instrument `r2_f7.py`. 52,910 objects
at the cut; 0 exist at the destination. This is a NEW served write: it runs under the never-widen pair
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND2_F7_COPY_COO_HALF.md` and `..._CTO_HALF.md`, whose blast radius
is the whole of what you may touch. Nothing reads the new keys (no router, guard or grant points at them), so the copy
changes nothing a user can see.

### 1a. The steps, in order. The directory `D` below is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8`.
The instrument is `C = org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py`; run every command
from the repository root with `python "$C" ...`.

0. **The pair.** `git ls-tree HEAD -- org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND2_F7_COPY_COO_HALF.md
   org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND2_F7_COPY_CTO_HALF.md` must list BOTH blobs, and the CTO
   half's verdict line must read `SIGNED` (read the file). If either is absent or does not read SIGNED: STOP, a BLOCKING
   row, your final report. You write nothing to AWS.
1. **Before.** `python "$C" residue --record before --dir "$D"` (counts under `gold/advi/` and `_campaign/` of the
   destination bucket, read-only), then `python "$C" manifest --out "$D/F7_MANIFEST.tsv.gz"` writes the manifest
   (a read-only listing of the 11 source prefixes). The destination prefix is checked empty by the first `COPY PLAN`
   line in step 3 (`already-present=0`).
2. **AC1:** the manifest verifies (section 4). If it does not, STOP: nothing is copied.
3. **The copy.** `python "$C" copy --manifest "$D/F7_MANIFEST.tsv.gz" --budget-seconds 100`. It is resumable: run it again
   until it prints `COPY PASS COMPLETE`. Read every `COPY PLAN` line: `already-present` must be 0 on the first run; a
   `refused-or-conflict` above 0, an `errors` above 0 or a `stale-source` above 0 means STOP and report (the producers
   are writing, or a second writer exists); never force, retry around it, or delete anything.
4. **AC2:** the compare reads `COPY-COMPLETE`.
5. **After.** `python "$C" residue --record after --dir "$D"`, then AC3.
6. Commit the manifest, the two residue records, the proof instance and the status flip together.

## 2. BOUNDS

1. The only AWS writes are `copy_object` calls made by `r2_f7.py copy`, to keys the manifest names, into
   `opal-data-49financial`. No other write, no delete, no overwrite of an existing key, no change to a policy, lifecycle,
   notification or configuration, no touch of `opal-data-bd` beyond reading. The copy uses `CopySourceIfMatch`: you add
   nothing to it.
2. **CLIENT DATA:** keys carry client and advisor ids. They appear in the manifest and nowhere else; your report names
   counts, never an id.
3. Only the files in section 3 change. Never edit the checks, the pair or the table.
4. No non-ASCII; LF line endings. If an item cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the pair under `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/`, the issuer's checks under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/`, `deliverables/mapping.json` and
`census.json`, `lib/opal_naming.py`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py" manifest --verify "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz"; echo "exit=$?"</invocation><expect>MANIFEST VERIFIED: every key placed once by address()</expect></criterion>
  <criterion id="AC2" cell_refs="FB-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 115 python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py" compare --manifest "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz"; echo "exit=$?"</invocation><expect>COPY-COMPLETE: every manifest key present and equal</expect></criterion>
  <criterion id="AC3" cell_refs="FB-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py" residue --check --dir "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8"; echo "exit=$?"</invocation><expect>RESIDUE UNCHANGED: gold/advi/ and _campaign/ key counts equal before, after and now</expect></criterion>
</proof_of_spec>

AC2 is the seam against the real neighbour (the destination bucket as it stands) and AC3 is the negative arm: the residue
count under the two tier-first prefixes does not move, with its denominator printed. Each invocation lists S3 pages only
(about 60 calls) and terminates well inside the bound. The copy itself is not a criterion: it is your act, in
100-second runs.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.proof_of_spec.json`. **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, only when AC1, AC2 and AC3 pass. A row id on this project carries the dell1 infix and your
slot: `ADVI_FIRMBKTS-D1-W8-S<k>`, with `surfaced_at` from `date -u +%FT%TZ`. Report once: the pair's two blob ids and the
CTO half's verdict line, the manifest's sha256 and object count, each `COPY PLAN` and `COPY RUN` line, the output lines of
AC1-AC3 (the `DEST` and `SOURCE` lines of the compare in full), the residue numbers, the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged: the cell is spawned the turn the CTO half is a file at HEAD and reads SIGNED, and before
about 05:30Z (the producers' write window runs to about 06:15Z; the copy refuses a moved source, so a late start costs a
re-cut, not a wrong byte). Class WORLD although the gate's floor reads LOCAL (paths: deliverables only, no deploy verb in
an invocation): it is a new served write, and the class decides which limbs engage. The CTO's exercised read at close is
`compare` run again by the CTO. The snapshot caveat is row D1-S4: this copy does not authorize a router flip.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>complete</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-5</to_id>
<slot>~8</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
