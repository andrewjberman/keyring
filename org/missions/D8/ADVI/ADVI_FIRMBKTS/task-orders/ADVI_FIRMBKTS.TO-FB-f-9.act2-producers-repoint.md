# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2: THE PLATINUM PRODUCERS' PER-OUTPUT DESTINATION (PHASE A: THE DORMANT BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~16</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A adds or changes no cron, rule, schedule or cadence and edits no launch or runner file; the writers run exactly as they do today (the mode is unset).
comp-iam: DECLARED-NOT-APPLICABLE -- phase A is repository files only: no AWS act and no grant. Whether each producer role may write the new prefix is read at phase B.
comp-adversary: RUN by the issuer -- r3_producers.py static reads 0 of 4 at base (the module is absent, D_00f carries one literal bucket name) and 4 of 4 on a reference build in a fixture repository (a mutant that returns the legacy bucket in canonical mode reads 2 of 4: D1 and D3 fail). Blindness: the lens cannot run a writer, so per-script dormancy is read from the module's identity over all 52,910 manifest keys and the per-script static arms, not from a dry run of each script.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-9` phase A (round 3, enrichment item 1, step 2; PRD F10; the CTO's ADDENDUM 2)

The platinum producers of `opal-data-bd` get a per-output destination: DORMANT, so that today's writes are byte-for-byte
what they are now, and a single environment MODE later moves only the platinum writes to their `address()` keys in
`opal-data-49financial`. You build it; you run nothing and move nothing.

The CTO's ruling (`ledger/ROUND_ANALYSIS.round2.md` ADDENDUM 2), which binds every line you write:
1. **The destination is `lib/opal_naming.py address()` output** for the firm's platinum key. No bucket name is typed in any
   script. The environment value carries a MODE only (`legacy` | `canonical`), never a bucket. A mode the code does not
   know is a refusal.
2. **Only platinum WRITES move.** Every read, and every non-platinum write, stays on `S3_BUCKET` exactly as today.
3. **`D_00f`'s hard-coded bucket goes through the same seam** in the same cell. After the cell, a census of the 14 writers
   prints 0 literal bucket names on a platinum write path.
4. **Dormant proof:** with the mode unset, every writer names the identical destination key and bucket as today.

### 1a. The facts you start from

- `deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json` names the 14 writer scripts and, per script, each platinum
  write line, its key expression, and how the bucket is chosen. All 14 are under
  `data/black_diamond/scripts/gold/`. Read it first.
- `data/black_diamond/scripts/gold/lib/config.py:14` defines `S3_BUCKET` (env `BD_S3_BUCKET`, default the old bucket); every
  script imports it and uses it for reads and writes. `D_00`, `D_00b` and `D_00c` write through `lib/gold_utils._save_json`;
  `D_04` through `_write_json_to_s3`; `D_02` through its own `_save_json`; `D_00f` uses a literal bucket.
- The served classes and their destination patterns are the round-1 table's (`deliverables/mapping.json`, `bucket ==
  "opal-data-bd"`, `disposition == "MOVE"`, `dest.tier == "platinum"`: 11 classes). The F7 copy placed every served key by
  `address()` using that table (`deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py`, `classes()` and `place()`): your
  canonical destination for a key MUST equal that placement for all 52,910 manifest keys.

### 1b. The steps

0. Work in `/c/dev/wk-firmbkts-16`. Begin every shell call with `cd /c/dev/wk-firmbkts-16 &&`.
1. **The registry rows (the CTO's ADDENDUM 3, ruling (1)).** Add ONE new registry file
   `infra/logic/registry/platinum_destinations.json`: one row per served class of the round-1 table (the 11 classes with
   `bucket == "opal-data-bd"`, `disposition == "MOVE"`, `dest.tier == "platinum"` in `deliverables/mapping.json`; add the
   4 served writes the census omitted, rows `D1-W16-S5` and `S6`, to the classes they belong to). A row names the legacy
   bucket, the legacy prefix (ending in `/`), the destination `source`, `scope` (a `scopes.json` key, never a bucket),
   `tier`, `table` and the partition template, the reader project and the evidence, with a closed field set the
   validator enforces. Wire the file into `lib/opal_naming.py`: the registry file list (an OPTIONAL file like
   `legacy_addresses.json`), a validation rule (a row is refused for a missing or extra field, an unknown bucket or
   scope, a prefix not ending in `/`, a repeated prefix, or a destination `address()` refuses), and one new generated
   WHOLE-FILE view (read how `BRONZE_HOMES_PATH` is wired in `VIEWS`, `WHOLE_FILE_TARGETS`, `TARGET_REGISTRY_KEYS` and
   `_blk_bronze_homes`) emitted to `data/black_diamond/scripts/gold/lib/platinum_dest_view.json`, carrying the standard
   GENERATED mark. The view holds, per class, the legacy prefix and the destination bucket and key template as
   `address()` builds them (never typed). Generate it with `python lib/opal_naming.py generate --out <dir> --target
   data/black_diamond/scripts/gold/lib/platinum_dest_view.json` and place the output at that path.
2. **The module.** Create `data/black_diamond/scripts/gold/lib/platinum_dest.py` exposing `destination(legacy_key,
   mode=None) -> (bucket, key)`:
   - mode `None` reads the environment variable `BD_PLATINUM_MODE` (unset means `legacy`);
   - `legacy`: returns `(S3_BUCKET, legacy_key)` unchanged (import `S3_BUCKET` from `lib.config`);
   - `canonical`: for a key of a served class returns the destination from the VIEW (the JSON file beside the module,
     read once and memoized; the module imports nothing from `lib/opal_naming.py`, which is not on the gold runner);
     for any other key returns `(S3_BUCKET, legacy_key)` unchanged;
   - any other mode raises `ValueError`.
   The earlier uncommitted table `lib/platinum_dest_table.json` and generator `lib/gen_platinum_dest_table.py` are
   DELETED (they were hand-kept carriers the naming gate refused; they were never committed).
2a. Route every platinum write of the 14 writers through `destination()`: the shared helpers (`lib/gold_utils._save_json`,
   D_04's `_write_json_to_s3`, D_02's `_save_json`, D_03/C_06/C_07/D_01/C_05/C_08/E_01/E_24's own put lines) and
   `D_00f`'s literal, now 62 writer lines in all (the census's 58 plus the 3 served `D_00` `gold/views/` writes at lines
   1106-1108 and `C_06` line 381). Change only the bucket and key a platinum `put_object`/`upload`/`copy` receives; leave
   reads, non-platinum writes, schedules and everything else as they are. A copy whose source is a platinum key reads the
   source from `S3_BUCKET` (legacy key) and writes to the destination. Leave a line the gate flags OUT-OF-PATTERN as a
   WARN (an existing touched line, `D_04` line 2468): never rewrite its key text.
3. Add a test file `data/black_diamond/scripts/gold/tests/test_platinum_dest.py` (unittest style, no new dependency) for:
   legacy identity, canonical equality with a sample of each of the 11 classes, non-platinum identity, an unknown mode
   refused.
3a. Amend `deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json` and `.md` to 62 writer lines (add the four served
   writes, with their lines and key text re-read from the files), so `r3_census.py` still reads 3 of 3.
4. Run AC1-AC4 (section 4). Read each line they print. Repair only what they name.
5. Print, per writer script, one line: `<script>: platinum write lines routed=<n>, literal bucket names=0` from your own
   `grep` over the script (denominator: the amended census's writer-line count for that script; 62 in all).

## 2. BOUNDS

1. Repository files only: no AWS call, no run of any gold script, no edit to a launch, runner or schedule file, no change
   to `lib/config.py`. The mode is never set by this cell. The registry file and `lib/opal_naming.py` are LGIC_ENFORCE's:
   add the one file, the one validation rule and the one view; touch no other registry row or emitter.
2. The module names no bucket in a string literal; the scripts name none either (D_00f's literal goes through the seam).
3. Behavior with the mode unset is unchanged: if routing a write would change what it does in `legacy` mode, STOP and file
   a BLOCKING row for that line.
4. Do not edit the census, the manifest, `mapping.json` or any check. Client ids appear in keys: your report names counts
   and script paths, never a key.
5. Only the files in section 3 change. No non-ASCII in code; LF line endings. If something cannot be met within your
   paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/logic/registry/platinum_destinations.json
lib/opal_naming.py
data/black_diamond/scripts/gold/lib/platinum_dest_view.json
data/black_diamond/scripts/gold/lib/platinum_dest.py
data/black_diamond/scripts/gold/lib/gold_utils.py
data/black_diamond/scripts/gold/tests/test_platinum_dest.py
data/black_diamond/scripts/gold/C_05.client_tax_liability.py
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/C_07.advisor_attribution.py
data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py
data/black_diamond/scripts/gold/D_00.portal_aggregates.py
data/black_diamond/scripts/gold/D_00b.portal_timeseries.py
data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py
data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py
data/black_diamond/scripts/gold/D_01.partner_analytics.py
data/black_diamond/scripts/gold/D_02.advisor_client_detail.py
data/black_diamond/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/E_01.account_quality_tiers.py
data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the census, the manifest, `mapping.json`, `lib/opal_naming.py`, the checks under
`deliverables/2.0.0_SA_COO~B1/round2/checks/` and `round3/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-16 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_producers.py --arms static --root /c/dev/wk-firmbkts-16; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCERS STATIC: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-16 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_view_sync.py --root /c/dev/wk-firmbkts-16; echo "exit=$?"</invocation><expect>VIEW IN SYNC: data/black_diamond/scripts/gold/lib/platinum_dest_view.json</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-16 &amp;&amp; timeout 100 python lib/opal_naming.py validate; echo "exit=$?"</invocation><expect>VALIDATE: OK .* over all 15 registry file</expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-16 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_census.py --census org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json --root /c/dev/wk-firmbkts-16; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCER CENSUS: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 carries its own difference control (D4: non-platinum keys unchanged in canonical mode) and its dormancy proof (D1:
legacy identity over all 52,910 manifest keys, canonical equal to the F7 placement). AC2 is the view being the builder's
own output (the naming gate grades it through its mark); AC3 the registry validating with the new file; AC4 the census
re-read at 62 lines (AC3 and AC4 read PASS at base only by the file count and the census as they stand: AC3 reads 14
files at base and FAILS as it should; AC4 reads the 58-line census and PASSES as a control). Four criteria are carried
because the registry file and the view are the CTO's ADDENDUM 3 deliverables and nothing else reads them. Each
invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16`. Commit the registry file, the `opal_naming.py` change, the view,
the module, the routed scripts, the test, the amended census, the instance and your rows together, on your branch. **Do not flip this order's `<status>`:**
phase B (the act itself) is the issuer's to amend and the order stays open until it is done. A row id on this project
carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W16-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` (your
earlier sessions filed S1 to S10: the next unused is S11). Report once: the 14 per-script lines of step 5, the AC1 output in
full, the generator's command if you used one, and the commit hash.

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
<slot>~16</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
