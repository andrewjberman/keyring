# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2: THE PLATINUM PRODUCERS' PER-OUTPUT DESTINATION (PHASE A2: TWO DORMANT READ FIXES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~19</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A2 adds or changes no cron, rule, schedule or cadence and edits no launch or runner file.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- `r3_rotation.py` reads 1 of 3 arms at base (R1 and R2 FAIL by construction, R3 PASSES as a control) and 3 of 3 on a reference edit of the two files in a fixture root (the same edit this face orders). Blindness: the arms read the calls' keyword arguments as syntax; they do not run a writer, so dormancy rests on the module's identity (R3 and `r3_producers.py` D1 over all 52,910 manifest keys).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-9` phase A2 (round 3, enrichment item 1, step 2; the CTO's ADDENDUM 2)

Phase A built the per-output destination: DORMANT, merged. Two reads that FOLLOW a platinum write were left on the legacy
bucket, and they read wrongly once the mode is `canonical`. You fix both, so that with the mode unset each does exactly
what it does today. You run nothing and move nothing.

### 1a. The facts you start from

- `lib/platinum_dest.py`: `destination(legacy_key, mode=None)` returns `(bucket, key)`; mode unset or `legacy` returns
  `(S3_BUCKET, legacy_key)`. Every writer's put already goes through it (imported in each script as
  `platinum_destination`).
- `D_04.client_portal_summary.py`, the prior-week rotation (about line 2466): it computes
  `rot_bucket, rot_key = platinum_destination('platinum/firm/leaderboard.prior_week.json')` and calls
  `s3.copy_object(Bucket=rot_bucket, CopySource={'Bucket': BUCKET, 'Key': 'platinum/firm/leaderboard.json'}, Key=rot_key, ...)`.
  The CURRENT leaderboard (the copy's source) is written, in `canonical` mode, to its destination, so the source read from
  `BUCKET` is the stale legacy copy. Row `ADVI_FIRMBKTS-D1-W16-S7`.
- `D_00f.advisor_nna_canonical.py`, the write-success sentinel (about line 939):
  `head = s3.head_object(Bucket=S3_BUCKET, Key=OUTPUT_KEY)`, run right after `_write_json_s3(artifact, OUTPUT_KEY)` whose
  put goes to `platinum_destination(OUTPUT_KEY)`. In `canonical` mode the sentinel heads the legacy bucket and fails loud
  on a write that landed. Row `ADVI_FIRMBKTS-D1-W16-S8`.

### 1b. The steps

0. Work in `/c/dev/wk-firmbkts-19`. Begin every shell call with `cd /c/dev/wk-firmbkts-19 &&`.
1. **D_04.** Immediately before the existing `rot_bucket, rot_key = ...` line, add
   `src_bucket, src_key = platinum_destination('platinum/firm/leaderboard.json')`, and change the `CopySource` to
   `{'Bucket': src_bucket, 'Key': src_key}`. Change nothing else in the block (the `except` arms, the print lines).
2. **D_00f.** Immediately before the `head_object` call, add
   `head_bucket, head_key = platinum_destination(OUTPUT_KEY)` and make the call
   `s3.head_object(Bucket=head_bucket, Key=head_key)`. The log lines keep naming `OUTPUT_KEY`.
3. **The census line numbers.** `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json` names each writer line by number, and
   AC3 re-reads each against the file. Your two edits add one line each, so every census line number after the insertion
   point in that script moves by +1. Re-read each entry of the two scripts that sits after your insertion and set its
   `line` to the line now holding the same statement (a text read, never a count by arithmetic alone); change no other
   field. Make the same change in `PRODUCER_CENSUS.md` if it prints those numbers.
4. **Find, do not fix, the same shape elsewhere.** The check prints "read-after-write candidates": every `head_object`,
   `copy_object` or `get_object` call in the 14 census writers whose text carries `platinum` and whose Bucket is
   `S3_BUCKET` or `BUCKET`. If it lists any, or you find a read of a platinum key a writer wrote earlier in the same run
   by another route (a helper that reads it back), file ONE row per site (`class` OBSERVATION, the file and line, what it
   reads and what the mode does to it) and change nothing at that site.

## 2. BOUNDS

1. Repository files only: no AWS call, no run of any gold script, no edit to a launch, runner or schedule file, no change
   to `lib/config.py`, `lib/platinum_dest.py` or any registry file. The mode is never set by this cell.
2. With the mode unset every line you touch names the same bucket and key it names today: if an edit would change a
   `legacy`-mode result, STOP and file a BLOCKING row.
3. Reads stay on `S3_BUCKET` except the two above. No new bucket name is typed anywhere.
4. Do not edit the census except the line numbers of step 3, nor any check. Client ids appear in keys: your report names
   counts and script paths, never a key. No non-ASCII in code; LF line endings. If something cannot be met within your
   paths, file a surprise row and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~19/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/` and `round3/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~19/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-19 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_rotation.py --root /c/dev/wk-firmbkts-19; echo "exit=$?"</invocation><expect>ROUND 3 ROTATION AND SENTINEL: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-19 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_producers.py --arms static --root /c/dev/wk-firmbkts-19; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCERS STATIC: 4 of 4 arms</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-19 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_census.py --census org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json --root /c/dev/wk-firmbkts-19; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCER CENSUS: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 is the two fixes (R1, R2) with their dormancy control (R3), FAIL at base. AC2 is the phase A build still dormant and
identical in `legacy` (PASS at base as a control: the edit must not break it). AC3 is the census still reading the
writer lines at their numbers (PASS at base; it FAILS if step 3 is skipped, because the insertion moves the lines). Each
invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~19`.
Commit the two scripts, the census files, your rows and then the instance (its artifact rows pin to the commit that holds
them, so the instance comes second). **Do not flip this order's `<status>`:** phase B (the act itself) is the issuer's
to amend. A row id on this project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W19-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the AC1 output in full, the candidates list (count and the file and
line of each), and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the census and the CTO's ADDENDUM 2 @650fbc3bcd, msg 3577):** the order was cut
staged as ONE act (repoint). The census read the seam as inseparable per output (`separable_per_output: false`), the CTO
ruled form A, and the build is its own work product with its own checkable proof. The order now carries PHASE A (the
dormant build, spawned now, one criterion) in its face; PHASE B (the act: the mode moves to `canonical`, cutover step 2)
is staged below with its un-park conditions and will be amended in when its pair signs. Why one order and not two: the
decomposition is frozen mid-round (rule 27) and the act is the same cell; phase A's close does not flip the order.
Gate limb: the new `<paths>` and criterion are an amendment of a staged order; GATE viii read `<placeholders>` at HEAD
(the earlier four tokens) and the declaration is now `NONE` because the face carries no token.

**AMENDMENT 2 (2.0.0_SA_COO~B1, the CTO's ADDENDUM 3 @a67e04d469, msg 3604):** the worker built phase A (AC1 4 of 4, 58 of
58 writer lines routed) and the commit-time naming gate refused the hand-kept table and generator (26 REFUSE, row
D1-W16-S10); the CTO ruled form (1): a registry file plus a generated whole-file view, built inside FB-f-9, no R20 entry,
the census and the pair at 62 writer lines. The face now orders that, with AC2-AC4 beside AC1. The worker's other rows
(S5-S9) are folded: S5, S6 become the four extra writes; S7 and S8 (canonical-mode reads of the stale legacy prior-week
source and of D_00f's sentinel) and S9 (D_00f follows `BD_S3_BUCKET` after the seam) are PHASE B's to read into the pair
and its legs, not phase A's. A generated view's mark carries the registry hash, so it goes stale when scopes.json or
tiers.json moves (the existing bronze_homes.json is stale that way today): AC2 is re-read at the merge. Gate limb: GATE
viii read `<placeholders>` at HEAD (`NONE`) and the added invocations carry no token.

**AMENDMENT 3 (2.0.0_SA_COO~B1, after the worker's second report, rows D1-W16-S11..S14):** the worker's build passed
AC1-AC4 and the issuer's own read found what they do not see: (1) `python lib/opal_naming.py targets` exits 1 with the
JSON view UNCLASSIFIED (row S13), a builder gate this merge would leave failing; (2) the deploy plane's
`file_to_s3_target` ships `.py` files only, so a JSON view in the gold lib directory would NOT reach the runner at
phase B's code sync and `canonical` mode would have no table there. Both end if the generated view is a `.py`
module in the same directory: it is then a SHIP target on the s3 plane by the plane's own rule. The CTO's ADDENDUM 3
ruled the form (a registry file and a generated whole-file view), not the extension; this is the issuer's ruling
inside the cell. S11 and S12 (served writes outside the ruled 62) are folded into the census; S14 (AC4 binds the
census to line numbers) is accepted as the cost of an honest re-read. Gate limb: GATE viii read `<placeholders>`
(`NONE`) and the added invocation carries no token.

**AMENDMENT 4 (2.0.0_SA_COO~B1, phase A2; rows D1-W16-S7 and S8, which phase A's worker named for phase B):** phase A is
merged (@b0eebb018d, AC1-AC5 PASS, 66 writer lines, the JSON view removed @cb5525f0e7). Reading S7 and S8 against the
mode move, both are CODE changes: the rotation's copy source and D_00f's sentinel read the legacy bucket, which
`canonical` mode stops refreshing, so at act 2 the first would archive a stale leaderboard as `prior_week` and the second
would fail loud on a landed write. Code is a worker's, not the executor's, so they are cut here as a dormant phase A2
(slot ~19, a fresh instance and deliverables folder; the face above replaces phase A's, which is closed and in history)
with the issuer's own check `r3_rotation.py` and a read-after-write candidate list that is informational, not graded.
S9 (D_00f follows `BD_S3_BUCKET`) is not a code change: it is read into phase B's pair as an environment condition (no
runner overrides the default). Gate limb: the `<issued_to>`, `<paths>` and criteria of a staged-open order are amended by
its issuer, GATE viii read `<placeholders>` at HEAD (`NONE`) and the new invocations carry no token; three mechanical
criteria, each dry-run at base (AC1 FAIL as expected, AC2 and AC3 PASS as controls).

**PHASE B (STAGED; NOT A FACE).** Un-park conditions, all required, each read from a file at HEAD:
1. Phase A merged with AC1 `4 of 4`, and `FB-f-8` (act 1, the advTenant deploy) is `complete`.
2. The never-widen pair for the mode move reads SIGNED in both halves
   (`ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md`, `..._CTO_HALF.md`). The blast radius per ADDENDUM 2: the 14
   scripts plus the 9 runner and launch files that carry the mode value (`gold_dispatch.sh:77`,
   `ec2/bd-gold-layer-runner/run-gold-layer.sh:13` and `setup-instance.sh:29`, `ec2/bd-gold-qa-runner/setup-instance.sh:36,122`,
   `ec2/canonical-schwab-runner/setup-instance.sh:13,26` and `user-data.sh:28`, the three `lambda/bd-pipeline` runners);
   rollback is the mode back to `legacy`, the same hour. The pair covers BOTH branches and reads the expected outcome
   from the module's own rule, not from the input's shape.
3. The actor's change-management entry is OPEN and committed first (the code sync of the dormant build to the runner is
   its own leg).
4. The amendment adds AC2-AC4: the writers' code at the runner equals the build (a hash read), the new home is written
   by a scheduled run since the mode moved (a bounded listing), and the old home is quiet for the served classes since
   (a bounded listing). Each is dry-run at base before the GO.
Placeholders then: `WRITER_GATE_CHECK`, `NEW_HOME_FRESHNESS_CHECK`, `OLD_HOME_QUIET_CHECK`.

**ISSUER NOTES:** class WORLD by the floor of phase B; phase A is repository files and is spawned the turn it is cut,
like `FB-e-6`. The producers rewrite the served keys daily in a window that closes about 06:15Z; the mode move is timed
so no producer run straddles it. After the mode moves and before act 4 the router still serves the OLD home, so users
read the last pre-move day: acts 2-4 close together (round-2 analysis, section 2 item 1). The census row D1-W16-S2 (ARMED,
disarm owner this seat) is closed by phase A's `D_00f` change and by AC1's D3.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-9</to_id>
<slot>~19</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
