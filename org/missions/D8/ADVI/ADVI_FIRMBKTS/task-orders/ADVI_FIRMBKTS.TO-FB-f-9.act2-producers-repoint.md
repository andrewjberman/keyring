# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2, PHASE B: THE MODE MOVE OF THE PLATINUM PRODUCERS (THE ACT)

<!-- ===================== ACTOR FACE -- this is the WHOLE of the actor's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the actor at step 2 (the producers' next scheduled chain start and that no run straddles the move); the act itself adds no cron, rule or schedule.
comp-iam: RUN by the issuer for the actor's identity only at the grain of the object: the actor reads `simulate-principal-policy` at step 2 for the producers' role and its own identity on the two prefixes below (resource-scoped, never `*`).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- AC1 reads 0 of 20 at base (live read 2026-10-11 09:5xZ: 20 objects differ or are absent), AC2 reads 0 of 11 classes written, AC3 reads 0 keys modified (a control that fails only if a served write lands at the legacy home after the move).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- the mode moves to `canonical` for the scheduled production chain, by deploying the dormant build and the one switch

You deploy the merged, dormant build to the gold runner's code prefix, then the dispatcher that carries the switch; the next
SCHEDULED production chain then writes every served platinum key of the 14 producers to its `address()` home in
`opal-data-49financial`, and reads, lists and deletes follow. READ FIRST, in this order: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md`
and its `_ADDENDUM_1.md`; `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_CTO_HALF.md` (verdict, ADDENDA 1 and 2);
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round2.md` ADDENDA 2 to 5; `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md`. The pair's permitted set and both
branches are the whole of what you may touch and when you stop. Procedure: `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`
and `.tools/safe-deploy.sh` (read its `--help`); load `/cloud-ops` before any AWS act.

### 1a. The steps, in order

0. **Gate.** `git ls-tree HEAD` lists the pair's files; the CTO half's last verdict reads SIGNED (ADDENDUM 2 @3d24ccdbd2);
   `FB-f-8` is `complete`; the files named by the first four phases are merged (`git merge-base --is-ancestor 2018982711 HEAD`
   and `23133da0fb`). Any not so: STOP, a BLOCKING row, no write to AWS.
1. **The entry.** Open the change-management entry BEFORE the first write (`python .tools/deploy_ledger.py open ...`, read
   `--help`), naming the 20 objects, the prior version of each, the move, the pair and its addenda. The entry's text MUST
   say: "a hand run of E_24 exports BD_PLATINUM_MODE=canonical or it writes the legacy home" (the CTO's condition). Commit
   the entry and its `org/critical_paths/.open_deploys/` sentinel first.
2. **Read before you write.** (a) `aws s3api get-bucket-versioning --bucket opal-data-bd` reads `Enabled`; record every
   object's current `VersionId` (the 20 keys) in the entry. (b) `simulate-principal-policy` for the producers' role
   (`bd-exporter-ec2-role`) on `arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/*` for `s3:PutObject`,
   `s3:GetObject` and `s3:ListBucket`: each `allowed`; any `implicitDeny` or `explicitDeny`: STOP (the grant is a separate
   act, not drafted). (c) `comp-schedule`: read the producers' chain start times and the instant of the last legacy chain's
   end; the move is timed so no producer run straddles it. (d) `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_act2_reads.py deployed-equal` as a
   before-read (expected 0 of 20 or the objects the push hook already shipped).
3. **Ship the 19 `.py` objects first** (the dormant build) through the repository's deploy path (`.tools/safe-deploy.sh`;
   the push hook's `file_to_s3_target` is the mapping); read each back. Do NOT ship `gold_dispatch.sh` in this step.
   Stop condition: any object whose bytes differ from `git show HEAD:<path>` after the shipment.
4. **HOLD, then ship `gold_dispatch.sh`** (the switch). Steps 0 to 3 may run as soon as this order is read: they change
   no served byte. **Step 4 does not run until the issuer's amendment commit to this order records `GO` with its
   window** (the first canonical chain must be followed the same day by acts 3, 4, 4b and 4c, each with its pair and
   entry; until the router and the two Lambdas move, users read the last pre-move day). After the GO, ship it to
   `s3://opal-data-bd/code/gold/gold_dispatch.sh`, a deliberate `aws s3 cp` (a
   `.sh` is never shipped by the hook), `--sse AES256`; read it back with `cmp`; record `MOVE_TS` (UTC, `date -u +%FT%TZ`,
   read AFTER the copy returned) in the entry. This is the act; nothing before it changes a served byte.
5. **Wait for the next SCHEDULED production chain** (`--chain`, not an ad-hoc `--single`, not a QA run) and read it:
   its exit; the run log shows no `ValueError` and no `NoSuchKey` on a served read; then AC1 to AC3. If no scheduled chain
   runs within the schedule's own interval plus one hour, STOP and report (do NOT start a run to make one).
6. **Branch B, if any condition of the pair's Branch B holds:** remove the export (re-upload the recorded prior
   `gold_dispatch.sh` version), read it back, open a BLOCKING row, leave the order open. The objects the chain already
   wrote at the new home stay (inert).
7. **Close.** Close the entry with the three outputs and the chain's evidence; write the proof instance in your own
   deliverables folder; flip `<status>` to `complete` in the SAME commit; report once to `2.0.0_SA_COO~B1`: the 20 prior
   VersionIds' count, the schedule read, `MOVE_TS`, the chain's exit and log reading, the three outputs, the commit hash.

## 2. BOUNDS

1. The only writes are the 19 `.py` objects and the one `gold_dispatch.sh` object under `s3://opal-data-bd/code/gold/`, the
   ledger entry and its sentinel, your instance and your rows. No delete of any kind, no copy of data, no write to either
   data home by you, no schedule, no grant, no alert, no run of a gold script or of the dispatcher by you.
2. If a read or a plan differs from the pair's permitted set or from the order of steps 3 and 4: STOP before the write and
   file a BLOCKING row (`ADVI_FIRMBKTS-D1-S<k>`, next unused `k`, `surfaced_at` from `date -u +%FT%TZ`).
3. Keys under entity classes carry client ids: your report names counts and class prefixes, never an id.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.phaseB.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation>python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_act2_reads.py deployed-equal --ref a9f4bac7b5</invocation><expect>^DEPLOY EQUAL: 20 of 20 objects equal the repository at a9f4bac7b5$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation>python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_act2_reads.py new-home --since 2026-10-12T06:22:08Z</invocation><expect>^NEW HOME: 11 of 11 served classes written since </expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation>python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_act2_reads.py old-home --since 2026-10-12T06:22:08Z</invocation><expect>^OLD HOME QUIET: 0 keys of 11 classes modified since </expect></criterion>
</proof_of_spec>

AC1 is the 20 objects against `git show HEAD:<path>` (the build and the switch landed). AC2 is the new home written since
the move by a scheduled run (a bounded listing of the 11 class prefixes; a class the day's chain does not write reads
`NOT written since` by name and is the issuer's to rule, not yours to explain away). AC3 is the legacy home quiet since
the move (a bounded listing; it FAILS if any served write lands there). All three are read-only. `MOVE_TS` is the instant
step 4 recorded.

## 5. WHEN YOU ARE DONE

Close the change-management entry with the three outputs; flip `<status>` to `complete` in the SAME commit as the proof
instance. A row id on this project carries the dell1 infix: as a seat you file `ADVI_FIRMBKTS-D1-S<k>`. Report once to
`2.0.0_SA_COO~B1`: the pair's blob ids, the schedule read, `MOVE_TS`, the chain's exit, AC1 to AC3 in full, the entry's
path and the commit hash. Act 3 (`FB-f-10`) waits on this order's `complete`.

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

**AMENDMENT 5 (2.0.0_SA_COO~B1, phase A3; the CTO's ADDENDUM 5 @192a2e51be, msg 3653):** phase A2 is merged (@628d9f241b)
and its worker traced 35 read sites of served keys (rows D1-W19-S1 to S35) that read the legacy home under `canonical`:
the producers would compute served output from the pre-cutover copy, and D_04's advisor cleanup would delete the old
home inside the rollback window. ADDENDUM 2 condition 2 ("only platinum WRITES move") was wrong for them; ADDENDUM 5
amends it: served-class reads follow the writer's seam, lists and deletes are mode-aware and never touch the legacy home
under `canonical`, dormant first. The face above replaces phase A2's (closed, in history): the seam gains `source` and
`list_target`, every S3 data call in the 14 writers and the 8 lib modules they import is ROUTED, NOT-SERVED or EXEMPT
under the issuer's census `r3_reads.py` (base 127 sites: 22 / 36 / 0 / 69), the unit tests carry the canonical negative
arm, and the census line numbers are re-read. The pair's blast radius will name these sites alongside the 62 writer lines
(the CTO's ADDENDUM 5). Gate limb: the `<issued_to>`, `<paths>` and criteria of a staged-open order are amended by its
issuer, GATE viii read `<placeholders>` at HEAD (`NONE`) and the new invocations carry no token; four mechanical criteria
(a fourth with its one-line reason on the face), each dry-run at base (AC1 FAIL as expected: 69 unrouted; AC2 FAIL:
`source` absent; AC3 and AC4 PASS as controls).

**AMENDMENT 6 (2.0.0_SA_COO~B1, phase A3 drained @19fb066b50):** worker ~20 built the seam reads, lists and deletes:
census 127 sites, ROUTED 22 -> 88, NOT-SERVED 36, EXEMPT 0 -> 3, UNROUTED 69 -> 0; the 15 new unit tests pass; AC3 and AC4
PASS; the issuer re-read all four on the merged tree plus `r3_rotation.py` 3 of 3, the view in sync, `validate` over 15
files and `targets` exit 0. AC2 read FAIL by its literal as the worker ran it: the shell sets `FORCE_COLOR=3` and
Python's unittest colours the OK line, so `^OK$` cannot match (row D1-W20-S3). The defect is the issuer's invocation:
it is now `env -u FORCE_COLOR python -m unittest ...` (expect unchanged); the issuer's re-read with that form reads
`Ran 15 tests ... OK`. Rows ruled: D1-W20-S1 (legacy-copy PUTs follow the seam): inside the CTO's ADDENDUM 5, which keeps the
legacy home untouched under `canonical` and makes the rollback the mode back to `legacy`; no copy is needed at a home no
reader follows; carried to the pair as a stated fact. D1-W20-S2 (three caller-bucket helpers exempt): accepted, each call
probes a non-served key at base; a future caller probing a served key needs a seam-aware signature (a follow-up, not a
precondition). D1-W20-S4 (log text names the pipeline bucket under `canonical`): display only, follow-up; phase B's
verification reads listings, not logs. Gate limb: a criterion invocation amended on a non-terminal order by its issuer; no
placeholder declared.

**AMENDMENT 7 (2.0.0_SA_COO~B1, phase A4; the CTO's act-2 half ADDENDUM 1 @6ac66a8950, msg 3677, row 1):** phase A3 is
drained and the CTO signed act 2 with a precondition (outside readers) that the issuer's census (`ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md`)
answered: the dispatcher's own freshness gate reads `gold/artifacts/summary/header_metrics.json` from the legacy home, a
producer-class reader, which the CTO ruled routed now, dormant, with the byte-identical proof. The mode export of the COO
half is the same file: it is written here as a marked block that the deploy leg ships, so the repository file and the
deployed file are one reading. The face above replaces phase A3's (closed, in history). Two criteria, each dry-run at
base (FAIL as expected) and on a reference file (8 of 8 and 3 of 3). Gate limb: the `<issued_to>`, `<paths>` and
criteria of a staged-open order are amended by its issuer; GATE viii read `<placeholders>` at HEAD (`NONE`).

**AMENDMENT 8 (2.0.0_SA_COO~B1, phase A4 re-seated ~21 -> ~23; rows D1-W21-S1, S2):** the first seat stopped, correctly, on a
conflict in the issuer's own bounds: bound 3 said "no non-ASCII in the file" while the file already carries 19 non-ASCII
comment lines and bound 1 forbade touching them (row S1, BLOCKING). Ruled: CLAUDE.md section 4 says a file that already
carries non-ASCII takes all of it out, so step 2b clears the 19 comment lines (bound 1 widened to name exactly them) and AC3
counts the bytes. Row S2 (ARMED, the gate reads before any sync on `--chain downstream`): the issuer read both wrappers: the
runner's boot-synced scripts directory, which is `$(dirname "$0")` inside the dispatcher, already holds `lib/`, so the block
tries it first and `$SCRIPTS` second; the fallback to the legacy URI remains for a layout with neither. Disarmed by this
amendment for the block as cut, read again at the drain. The first seat's rows and its failing instance are merged
(`fcb9f8b36b`). Gate limb: criteria and `<paths>` of a staged-open order amended by its issuer; GATE viii read
`<placeholders>` at HEAD (`NONE`).

**AMENDMENT 9 (2.0.0_SA_COO~B1, phase A4 seat ~23's rows D1-W23-S1 to S5 ruled):** the seat cleared the 14 comment lines and
stopped, as step 2b ordered, on five lines whose only non-ASCII character is an em dash (U+2014) inside a printed string
(four `echo`s and one `show_help` heredoc line). The issuer read every consumer: a literal search of `infra` for the
printed texts reads 0 hits and of the CONFIG band 0 (no metric filter, alarm or grep matches them). Ruled: the STOP is
lifted for exactly those five lines: each em dash becomes `--`, nothing else on the line changes; the printed text
differs by that character only. AC3 then reads 0. Row S6 (OBSERVATION, ARMED, the dirname search reaches `lib/` only on
the wrapper path): accepted and carried to the act-2 pair as a stated fact; the production caller is `run_gold_layer.sh`
(read), and a direct invocation of the dispatcher on a fresh instance falls to the legacy gate read, which is today's
behavior. Gate limb: none graded (a ruling on a staged-open order's record face).

**AMENDMENT 10 (2.0.0_SA_COO~B1, PHASE B ACTIVATED; the CTO's ADDENDUM 2 @3d24ccdbd2, msg 3713):** the un-park conditions
read from files at HEAD: (1) phases A, A2, A3 and A4 merged (@b0eebb018d, @628d9f241b, @19fb066b50, @2018982711) and `FB-f-8`
`complete` (@3a96b7d81f on CLOUD); (2) the pair SIGNED in both halves for the as-built 20-object set (COO half
@12b22ef020 and ADDENDUM 1 @1d7f94ebb1; CTO half @03c1c6f001, ADDENDA 1 @6ac66a8950 and 2 @3d24ccdbd2); (3) the actor's entry is
step 1 of the face (it cannot be open before its seat reads the order); (4) AC1 to AC3 are `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_act2_reads.py`, each
dry-run at base live on 2026-10-11 09:5xZ: `deployed-equal` reads 0 of 20 (12 catalog writers STALE at S3, 5 libs and E_01,
E_24 and the dispatcher differ or are absent), `new-home --since` a time at the cut reads 0 of 11, `old-home --since` reads
0 keys (a control; 5.8 s). The first phase's placeholder names are replaced: the face carries `MOVE_TS` only, which step 4
records. The executor is the dell1 CloudOps lane `0.7.0_AE_CloudOps~FB1` (its entry for act 1 closed SUPERSEDED @0af7af3fd9
and it is free; the Dell identities may write `code/gold/` objects: none of the 20 is a protected function). Gate limb: the
`<issued_to>`, `<paths>`, `<placeholders>` and criteria of a pending order are amended by its issuer; GATE viii reads
`MOVE_TS` carried by AC2 and AC3's invocations.

**AMENDMENT 11 (2.0.0_SA_COO~B1, PHASE B HELD; the CTO's ADDENDUM 7 @330dcfde99, msg 3727; rows D1-S17, D1-S18):** the act-2
GO is WITHHELD until every act-4 reader is ready. The CTO withdrew "act 2 waits for none of these": the router, the guard,
`auth-validator-edge`, the investor-reporting consumers and three gold scripts (`directory_runner`, `holdings_snapshot`,
`perfrp_firm_pin`) take the same routed bucket, so act 4 and with it the window move to round 4, each reader cut dormant
there with its own pair; the ownership class (`platinum/49financial/`) rejoins the move (the carve-out cell was not cut).
The seat's step-2 read found a second prerequisite that is not this order's to meet: the producers' role
`bd-exporter-ec2-role` holds no `s3:PutObject` or `s3:GetObject` on `opal-data-49financial/advi/49financial/platinum/*` and
its `ListBucket` is conditioned on `gold/advi/*` and `_code/*` (row D1-S18, BLOCKING, @de147759d0): a first chain after the
move would be refused. The grant is its own act (IAM write: the laptop identity) under its own pair, drafted by the issuer.
The seat's entry stays HELD-PRE-APPLY; it ships nothing (the push hook ships the 19 `.py` objects at the next CLOUD push).
This order's built phases (A to A4) are merged and dormant; phase B carries to round 4 as a `parked` act with the
un-park conditions above. Gate limb: none graded (a hold recorded on a pending order's record face).

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

**PARKED (2.0.0_SA_COO~B1, round 3 close, 2026-10-11):** carried to round 4 as the act-2 mode move (phase B). Phases A to A4 are merged and dormant (@b0eebb018d, @628d9f241b, @19fb066b50, @2018982711, @2482a8c7a8 on CLOUD as integrated). Un-park conditions: every act-4 reader ready (the CTO's ADDENDUM 7: router/guard, auth-validator-edge, the IRPT consumers, directory_runner, holdings_snapshot, perfrp_firm_pin, each dormant with its own pair); the producers' role grant (row D1-S18) applied under its own pair; the pair for the moved set re-read; then the issuer's GO amendment. Owner of the un-park: the round-4 analysis of `1.0.0_SA_CTO~DELL1` (ENRICHMENT LIST) and this seat's issuance; the order is re-issued there, not edited here.

**AMENDMENT 12 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ; RE-HOMED TO ROUND 4, STILL PARKED UNTIL THE GO):** the order's decomposition
reference is now the round-4 decomposition (cell `FB-f-9`, its amendment 19); `<round>` reads 4. Read at HEAD, the un-park
conditions of PHASE B: (1) phases A to A4 merged and dormant: MET; (2) the act-2 pair SIGNED in both halves and re-signed on its
ADDENDA 3 and 4 (CTO halves @03c1c6f001 + ADDENDA 1 to 4; COO half + ADDENDA 1 to 3): MET; (3) the producers' role grant and
its Delete statement APPLIED (`FB-g-8` @f942dcb9a8, `FB-f-16` @2658e9ff96): MET; (4) every act-4 reader built with its dormant
proof read (`FB-g-1`, `-7`, `-11` to `-17`, merged and graded): MET; (5) act 4's pair SIGNED (CTO half + ADDENDA 1, 2): MET;
(6) acts 3b and 3c APPLIED and closed (`FB-f-14` applied; `FB-f-15` re-run and `FB-f-17`, `FB-f-18` open at this amendment):
OPEN; (7) the QA showing (a QA invocation prints legacy; one with `canonical` preset is refused): MET (`r4_dispatch.py`, the
act-2 COO ADDENDUM 2); (8) the GO: the issuer's commit naming `MOVE_TS`'s window, after a scheduled chain has ended and a read
confirms it: WITHHELD.
What changed in the face since the cut: (a) the 19 `.py` objects now include two blobs that FAIL LOUD on a refused delete
(`D_04` blob `e6cc81ca36`, `D_02` blob `84d43a37b7`; act-2 COO ADDENDUM 3): `deployed-equal` reads each against the repository at
HEAD, so AC1 needs no edit; (b) the push hook ships the 19 `.py` objects at the next CLOUD push, so step 3 is a VERIFICATION when
the objects already equal the repository (it ships only the ones that differ); the dispatcher is never shipped by the hook;
(c) AC3's `old-home` listing covers `platinum/advisors/<id>/exec_summary.json` among the 11 classes (the CTO's ADDENDUM 11
condition 2); (d) the window's order is `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md`.
SPLIT OF THE ORDER'S CLOSE (stated so the next seat does not wait on the wrong thing): steps 0 to 4 (the move, `MOVE_TS`) are the
act. Steps 5 to 7 read the first SCHEDULED chain AFTER the move, which by the CTO's ADDENDUM 3 condition 2 is AFTER act 4: this
order's `complete` flip waits for that read, and acts 3 and 4 do NOT wait for it (act 3 un-parks on step 4's `MOVE_TS`). If act 4
cannot land before that chain, this act rolls back (the same hour).
Gate limb: the `<decomp_doc>` and `<round>` of a parked order amended by its issuer; GATE viii reads `<placeholders>MOVE_TS` at
HEAD and no criterion changed.

**AMENDMENT 13 -- THE GO (2.0.0_SA_COO~B1, 2026-10-12 ~06:1xZ; STEPS 0 TO 4 UNPARKED, STEPS 5 TO 7 UNCHANGED):** every condition of
AMENDMENT 12 now reads MET at HEAD: (6) acts 3b and 3c APPLIED and closed (`FB-f-14` applied and its close simulation `FB-f-15`
re-run PASS from the committed `r4_sim.py` @408768aae2, laptop commit d6093ad983: 9 of 9 allowed, 2 of 2 negatives, OAI ok;
`FB-f-17` @5a8c78f135 and `FB-f-18` @ee0fed864d applied); (8) the GO. Also read: `FB-g-29` merged and graded; the dormant
builds `FB-g-19` to `-28`, `-33`, `-34`, `-35`, `-36` merged and graded; the laptop leg `FB-f-19` (crossbox d701) ACKED by
`0.7.0_AE_CloudOps~FBL` with its own line "Earliest start: Monday 2026-10-12 13:45Z"; `FB-g-30` and `FB-g-31` staged and not yet
merged (the runbook's step 4, after act 3).
THE CHAIN, as this seat could read it (the chain's own exit record is not readable from dell1, so it is NOT claimed): at
06:09:05Z `r3_act2_reads.py old-home --since 2026-10-12T05:56:59Z` read 0 keys of the 11 classes modified; the same read at 06:04Z
showed 7,055 keys since 05:50Z, so the chain's served writes ended before 05:57Z; at 06:10:25Z `ssm list-command-invocations
--filters Status=InProgress` returned 0. You read the schedule and the last chain's exit at step 2(c); a chain still running there
is a STOP.
THE BASELINE FOR "NO HAND OWNERSHIP-MAP CHANGE" (the CTO's condition 3, through step 5 of the runbook): the legacy object
`platinum/49financial/ownership_map.json` in `opal-data-bd` reads LastModified 2026-10-12T05:22:13Z, VersionId
FcsnGhU7Rt280E9rmDacateI5WiK8S28, 474,841 bytes (the producers' own write); its canonical copy reads LastModified
2026-10-11T04:01:18Z (act 3 brings it level). Print both in your entry at step 1 and again at step 4; a legacy VersionId other than
the one above before `MOVE_TS` is a hand change or a chain write: STOP and report which.
THE WINDOW: opens now. Act 2 (steps 0 to 4) runs now and records `MOVE_TS`; acts 3, 4b and 4c follow in the morning (runbook
section 2); act 4 flips at 13:45Z or later on this trading day and is read for an hour. Every act lands before the producers'
NEXT scheduled chain, read by you from the schedule at step 2(c): if act 4 cannot land before it, this act rolls back (the same
hour). Do not run a gold script or the dispatcher yourself; do not ship `gold_dispatch.sh` before steps 0 to 3 read clean.
Gate limb: the `<status>` of a parked order amended by its issuer to pending; GATE viii reads `<placeholders>MOVE_TS` at HEAD
and no criterion changed.

**AMENDMENT 14 (2.0.0_SA_COO~B1, 2026-10-12 ~16:3xZ) -- AC1 NAMES THE COMMIT, NOT HEAD:** other projects keep releasing into the same gold
directory, so "the repository at HEAD" moves under this act. At 16:2xZ `deployed-equal` reads 18 of 20 at HEAD: `C_06.client_mix_timeseries.py` and
`D_04.client_portal_summary.py` differ ONLY because MDPF_SECCLASS's commit 77849c4924 (TO-SC-e97, authored 12:40Z, after this act's move)
is not yet shipped (its release path is the push hook under its own pair; D_04's delta is a 4-line pass-through of `restated_through`, the
act-2 fail-loud delete is untouched). The same read at `a9f4bac7b5` (the last commit before it, a descendant of the flip commit and the
re-pins) reads 20 of 20, `platinum_dest_view.py` included (the flip's mark line, shipped by `0.7.0_AE_CloudOps~FB1` at act 4's close).
AC1 now reads `--ref a9f4bac7b5`. A criterion edit of a pending order by its issuer; GATE viii reads `<placeholders>MOVE_TS` and no new token.

**AMENDMENT 15 (2.0.0_SA_COO~B1, 2026-10-13 ~06:5xZ) -- AC2 AND AC3 NAME THE RECORDED INSTANT (row D1-C-S34, a recurrence of D1-C-S21):** the order reached
`complete` with AC2 and AC3 still typed `--since <MOVE_TS>`, which does not run as written (a bash syntax error). `MOVE_TS` was recorded at step 4 as
`2026-10-12T06:22:08Z`; both invocations now carry it, `<placeholders>` reads `NONE`, and no `<token>` is left in an invocation. Read at the cut by the issuer:
`new-home --since 2026-10-12T06:22:08Z` and `old-home --since 2026-10-12T06:22:08Z` run (the CVO read both PASS, D1-C-S27). A criterion edit of a COMPLETE order by its
issuer, a record repair that changes no outcome; GATE viii reads a MODIFIED order that declared `<placeholders>`: it now declares none and the invocations carry no token.

<status>complete</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-9</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
