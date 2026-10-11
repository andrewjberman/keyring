# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2: THE PLATINUM PRODUCERS' PER-OUTPUT DESTINATION (PHASE A4: THE DISPATCHER'S GATE READ AND THE MODE EXPORT, DORMANT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~23</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A4 edits one shell file in the repository; it adds or changes no cron, rule, schedule or cadence and deploys nothing (a `.sh` is never deployed by the push hook; the act deploys it by a deliberate leg).
comp-iam: DECLARED-NOT-APPLICABLE -- repository file only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- `r3_dispatch.py --arm export` and `--arm gate` read FAIL at base (both blocks absent) and 8 of 8 and 3 of 3 on a reference file carrying the two blocks (the same blocks this face orders). Blindness: the arms run the two marked blocks in bash with stub variables; they do not run `gold_dispatch.sh`, so the block's PLACEMENT in the file (after argument parsing; inside the freshness function) is your reading, stated in your report with line numbers.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-9` phase A4 (round 3, enrichment item 1, step 2; the CTO's ADDENDUM 4 carrier and the act-2 CTO half's ADDENDUM 1 row 1)

The dispatcher `data/black_diamond/scripts/gold/gold_dispatch.sh` is the one switch for the platinum mode (ADDENDUM 4) and its freshness gate reads
a served key from the legacy home. You edit that one file in two places, DORMANT: with the mode unset the file's behavior
is byte-identical to today's. You run nothing and deploy nothing.

### 1a. The facts you start from

- `lib/platinum_dest.py` (merged): `source(legacy_key, mode=None) -> (bucket, key)`; the mode is read from the environment
  variable `BD_PLATINUM_MODE` (unset = `legacy`, `legacy` returns `(S3_BUCKET, key)` where `S3_BUCKET` is `BD_S3_BUCKET`
  defaulting to `opal-data-bd`).
- `data/black_diamond/scripts/gold/gold_dispatch.sh` sets `SCRIPTS="/tmp/gold_layer_scripts"` near its top (the directory the runner syncs `code/gold/`
  into, including `lib/`), parses its arguments into the shell variables `MODE` (`chain`, `single`, `group`, `from`) and
  `DRY_RUN` (`0` or `1`), and at about line 249, inside the freshness check, reads the gate's date with
  `gold_as_of=$(aws s3 cp "s3://${BD_S3_BUCKET}/gold/artifacts/summary/header_metrics.json" - ...)`.
- That key is a served-class key: written at the new home under `canonical`, so the legacy read would return a frozen
  `data_as_of`. The chain's QA runner is the same script with `GOLD_KEEP_ALIVE=1` (the runner script
  `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` reads it) and a marker file `/tmp/GOLD_QA_REBUILD`.

### 1b. The steps

0. Work in `/c/dev/wk-firmbkts-23`. Begin every shell call with `cd /c/dev/wk-firmbkts-23 &&`.
1. **The mode export.** After the argument parsing (the point where `MODE` and `DRY_RUN` are final, and before any use of the
   mode by a child), add exactly this marked block (the check reads it by its two marker lines):
   ```
   # >>> PLATINUM-MODE (ADVI_FIRMBKTS FB-f-9) >>>
   if [ "${MODE:-}" = "chain" ] && [ "${DRY_RUN:-0}" = "0" ] && [ "${GOLD_KEEP_ALIVE:-0}" != "1" ] \
      && [ ! -f "${GOLD_QA_MARKER:-/tmp/GOLD_QA_REBUILD}" ] && [ -z "${BD_PLATINUM_MODE+x}" ]; then
       export BD_PLATINUM_MODE=canonical
   fi
   # <<< PLATINUM-MODE (ADVI_FIRMBKTS FB-f-9) <<<
   ```
   The block never overrides a value already set, and it fires only for a scheduled production chain. NOTE: while this
   file is not deployed the block does nothing on the runner; it is the deployed file that moves the mode.
2. **The gate read.** Replace the `gold_as_of=$(aws s3 cp "s3://${BD_S3_BUCKET}/gold/artifacts/summary/header_metrics.json" -
   ...` read so that its location comes from this marked block, placed immediately before it inside the same function, and
   the `aws s3 cp` reads `"$gold_hm_loc"`; keep the rest of the pipeline (`| python3 -c ...`, the redirections) byte-for-byte:
   ```
   # >>> GATE-READ-LOCATION (ADVI_FIRMBKTS FB-f-9) >>>
   gold_hm_loc=""
   for _gd in "$(dirname "$0")" "$SCRIPTS"; do
       gold_hm_loc=$("${GOLD_PYTHON:-python3}" -c 'import sys; sys.path.insert(0, sys.argv[1]); from lib.platinum_dest import source; b, k = source("gold/artifacts/summary/header_metrics.json"); print("s3://%s/%s" % (b, k))' "$_gd" 2>/dev/null) && [ -n "$gold_hm_loc" ] && break
       gold_hm_loc=""
   done
   [ -n "$gold_hm_loc" ] || gold_hm_loc="s3://${BD_S3_BUCKET}/gold/artifacts/summary/header_metrics.json"
   # <<< GATE-READ-LOCATION (ADVI_FIRMBKTS FB-f-9) <<<
   ```
   Why two directories (established by the issuer, read this): on a runner `run-gold-layer.sh` syncs `code/gold/` into
   `/home/ubuntu/gold-layer/scripts` at boot (lines 88-90) and runs `./run_gold_layer.sh` from there (line 115); that
   wrapper sets `SCRIPT_DIR` to its own directory and runs `bash "$SCRIPT_DIR/gold_dispatch.sh"`, so `$(dirname "$0")`
   inside the dispatcher is the boot-synced directory and holds `lib/` BEFORE the dispatcher's own later sync into
   `$SCRIPTS` (`sync_scripts`, about line 664, called at about lines 473 and 532). On `--chain downstream` the gate runs
   before any `sync_scripts`, which is why `$(dirname "$0")` comes first. If no directory holds the lib, the location
   falls back to today's legacy URI (the check's third case). In your report state whether the loop's first directory
   holds `lib/platinum_dest.py` in the layout above, by reading the two scripts' lines.
2b. **ASCII.** The file already carries non-ASCII characters on 19 comment lines (lines 44, 49, 146, 154, 324, 369, 487,
   517, 559, 921, 1074, 1125, 1132, 1389, 1410, 1443, 1482, 1484, 1500: dashes, a section sign and similar). CLAUDE.md
   section 4: a file that already carries non-ASCII takes ALL of it out or every reader explicit, never a subset. Replace
   each non-ASCII character on those lines with its plain ASCII equivalent (an em or en dash with `--`, a section sign
   with `sect.`, a multiplication sign with `x`, an arrow with `->`, any other with the nearest ASCII word), and touch
   nothing else on the line. They are comments, so the file's behavior is unchanged. If any is inside a string a command
   prints or a pattern a command matches, STOP and file a BLOCKING row for that line.
3. **Shell syntax.** `bash -n data/black_diamond/scripts/gold/gold_dispatch.sh` exits 0.
4. **Find, do not fix, the same shape elsewhere in this file.** List every other `aws s3 ls`, `aws s3 cp`, `aws s3 sync` or
   `aws s3api` in `gold_dispatch.sh` whose key is under one of the 11 served legacy prefixes
   (`gold/artifacts/`, `gold/entities/{accounts,advisors,clients}/`, `gold/platinum/firm/`, `gold/views/`,
   `platinum/{49financial,accounts,advisors,clients,firm}/`): file ONE row per site (OBSERVATION: line, what it reads,
   what the mode does to it) and change nothing at that site.

## 2. BOUNDS

1. One file changes: `data/black_diamond/scripts/gold/gold_dispatch.sh`. The diff against base is the two marked blocks, the
   one replaced `aws s3 cp` argument and the 19 comment lines of step 2b (ASCII characters in place of the non-ASCII ones),
   nothing else.
2. With the mode unset and a non-chain mode, a dry-run, `GOLD_KEEP_ALIVE=1` or the QA marker, the file does exactly what it
   does today. Under a scheduled chain with the mode unset the only difference is the exported variable (the point of the
   act). No new delete, copy, write or alert. No change to any other file, launch script or schedule.
3. LF line endings; the file reads 0 bytes above 127 when you are done (AC3). If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~23/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~23/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-23 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_dispatch.py --arm export --root /c/dev/wk-firmbkts-23; echo "exit=$?"</invocation><expect>ROUND 3 DISPATCH EXPORT: ALL CASES PASS</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-23 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_dispatch.py --arm gate --root /c/dev/wk-firmbkts-23; echo "exit=$?"</invocation><expect>ROUND 3 DISPATCH GATE: ALL CASES PASS</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-23 &amp;&amp; python -c "import sys; b=open(sys.argv[1],'rb').read(); print('non-ascii-bytes=%d' % sum(1 for x in b if x &gt; 127))" data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^non-ascii-bytes=0$</expect></criterion>
</proof_of_spec>

AC1 runs the export block under eight environments (a scheduled chain reads `canonical`; `single`, `group`, a dry-run,
the QA keep-alive and the QA marker read unset; a value already set is kept), FAIL at base. AC2 runs the gate block with the
mode unset (today's URI, byte-identical), with `canonical` (the module's own answer for the key) and with the lib absent
(today's URI), FAIL at base. AC3 counts the bytes above 127 in the file (19 lines at base, so FAIL at base): a third criterion, carried because CLAUDE.md
section 4 makes it the only safe state of a file that already carries non-ASCII. Each invocation terminates
inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~23`.
Commit the file and your rows, then the instance second (its artifact rows pin to the commit that holds them). **Do not
flip this order's `<status>`.** Row ids: `ADVI_FIRMBKTS-D1-W23-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`.
Report once: the AC1 and AC2 outputs in full, the line numbers of the two blocks and of the sync, the sites of step 4
(count and line numbers), `bash -n`'s exit, and the commit hash.

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
<slot>~23</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
