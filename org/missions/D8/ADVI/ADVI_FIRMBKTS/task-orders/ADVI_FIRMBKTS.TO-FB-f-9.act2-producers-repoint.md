# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2: THE PLATINUM PRODUCERS' PER-OUTPUT DESTINATION (PHASE A3: READS, LISTS AND DELETES FOLLOW THE SEAM, DORMANT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~20</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A3 adds or changes no cron, rule, schedule or cadence and edits no launch or runner file.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- `r3_reads.py` reads 127 S3 data call sites in the 14 writers and the 8 gold lib modules they import at base: ROUTED 22, NOT-SERVED 36, EXEMPT 0, UNROUTED 69 (so AC1 FAILS at base by construction). Blindness: the census resolves a key only through module constants, `lib.s3_layout` names, f-string prefixes and one-return key builders; a key it cannot resolve counts UNROUTED until you route it or mark it, never silently NOT-SERVED. It reads syntax, not behavior: dormancy rests on the seam's identity in `legacy` mode (the unit tests), not on a run of each script.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-9` phase A3 (round 3, enrichment item 1, step 2; the CTO's ADDENDUM 5, which amends ADDENDUM 2 condition 2)

Phases A and A2 are merged: every platinum WRITE of the 14 writers goes through `lib/platinum_dest.py destination()`. The
CTO has ruled that READS, LISTS and DELETES of a served-class (platinum) key follow the same seam: one `BD_PLATINUM_MODE`
moves a key's write and its readers together, and a list or delete path never touches the legacy home under `canonical`.
You build that, DORMANT: with the mode unset every call you touch names the same bucket, prefix and key it names today.
You run nothing and move nothing.

### 1a. The facts you start from

- `lib/platinum_dest.py`: `destination(legacy_key, mode=None) -> (bucket, key)`; `legacy` (mode unset) returns
  `(S3_BUCKET, legacy_key)`; `canonical` returns the new home for a key under a served class prefix (the 11 classes of
  `lib/platinum_dest_view.py PLATINUM_CLASSES`: rows `(legacy_prefix, bucket, key_template)`, the template ending in
  `{tail}`) and `(S3_BUCKET, legacy_key)` for any other key. An unknown mode is a `ValueError`.
- The census `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py` (read it first; run it with `--list`) prints every S3 data call site in the 14 writers
  and the 8 lib modules they import, with its class. A site is ROUTED when its `Bucket` is bound from a seam call
  (`platinum_destination`, `platinum_source` or `platinum_list_target`, by name, directly or through a tuple unpack),
  NOT-SERVED when its key resolves statically outside every served prefix, EXEMPT when its line or the line above carries
  `# seam: exempt <reason>`, UNROUTED otherwise. At base: 127 sites, 22 / 36 / 0 / 69.
- Worker 0.9.0_WK_ADVI_FIRMBKTS~19 filed 35 read sites by hand (rows `ADVI_FIRMBKTS-D1-W19-S1` to `S35` in
  `surprise-channel/investigations/INVESTIGATION_v1.md`; read them). They are a subset: the census is the denominator.
  S35 is `D_04.client_portal_summary.py` listing `platinum/advisors/` and deleting stale keys on the legacy bucket.

### 1b. The steps

0. Work in `/c/dev/wk-firmbkts-20`. Begin every shell call with `cd /c/dev/wk-firmbkts-20 &&`.
1. **The seam, `lib/platinum_dest.py`.** Add, beside `destination`:
   - `source(legacy_key, mode=None) -> (bucket, key)`: for a READ; the same resolution as `destination` (reads follow
     writes).
   - `list_target(legacy_prefix, mode=None) -> (bucket, prefix, to_legacy)`: for a LIST or PAGINATE. In `legacy`:
     `(S3_BUCKET, legacy_prefix, identity)`. In `canonical`, when `legacy_prefix` starts with a served class prefix:
     `(class bucket, key_template with {tail} replaced by legacy_prefix[len(class_prefix):], to_legacy)` where
     `to_legacy(dest_key)` returns `class_prefix + dest_key[len(template_root):]` (`template_root` = the template without
     its trailing `{tail}`) and raises `ValueError` for a key outside `template_root`. When `legacy_prefix` is a PROPER
     prefix of a served class prefix (a listing that would span served and non-served keys): `ValueError`. Otherwise
     `(S3_BUCKET, legacy_prefix, identity)`.
   - Both read the mode exactly as `destination` does and refuse an unknown mode.
   - A DELETE of a key you listed uses `destination(legacy_key)` for its bucket and key (the listing returned legacy-shaped
     keys through `to_legacy`).
2. **Unit tests, `tests/test_platinum_dest.py`** (unittest, standard library; add cases, keep the existing ones). Put them in
   three `unittest.TestCase` classes named exactly `TestSource`, `TestListTarget` and `TestCanonicalNegativeArm`:
   (a) `legacy`: `source` and `list_target` return `(S3_BUCKET, key)` and `(S3_BUCKET, prefix, identity)` for one key of
   each of the 11 classes; (b) `canonical`: `source(k) == destination(k)` for those 11, and `list_target` returns the
   class bucket and a prefix that is NOT the legacy prefix, with `to_legacy(dest_prefix + tail)` equal to the legacy key;
   (c) a prefix spanning two classes raises `ValueError`; (d) a non-served prefix is the identity in both modes; (e) the
   NEGATIVE ARM: with a recording fake client (a class whose `get_object`, `head_object`, `list_objects_v2`,
   `get_paginator(...).paginate`, `delete_object` and `delete_objects` record the `Bucket` and `Prefix`/`Key` they get),
   drive each routed LIST and DELETE helper that is a module-level function of the 14 writers or the libs (import the
   script with `importlib.util.spec_from_file_location`; replace its module-level `s3` and bucket names with the fake;
   mode `canonical`) and assert the recorded calls name 0 legacy served prefixes. A list or delete that sits inline in
   `main()` and cannot be driven is named by file:line in your report; the census still covers it.
3. **Route every UNROUTED site** the census lists, in the 14 writers and the lib modules, until it reads UNROUTED 0:
   - a read of a key: `b, k = platinum_source(<the key expression>)` and `Bucket=b, Key=k` (a helper such as `_read_json`
     or `_read_parquet` is routed once, inside the helper, so every caller follows);
   - a list or paginate: `b, p, to_legacy = platinum_list_target(<prefix>)`; page results come back with `to_legacy`
     applied so the rest of the function sees legacy-shaped keys exactly as today;
   - a delete: `b, k = platinum_destination(<legacy key>)`; D_04's advisor cleanup (row S35) lists through the seam and
     deletes through `destination`, so under `canonical` it never lists or deletes the legacy prefix;
   - a PUT the census lists as UNROUTED is a served write the earlier phases missed, or a non-served write whose key the
     census could not resolve: route it through `platinum_destination` (identity for a non-served key) unless the key is a
     plain non-served literal, and file a row if it changes the writer census count;
   - a call on a bucket that is NOT the pipeline bucket (a literal or another config bucket), or a key that is provably
     non-served but dynamic: add `# seam: exempt <one-line reason>` on the call line. Prefer routing: the seam is the
     identity for a non-served key, so routing it costs nothing.
   Import the seam names in each edited script as `from lib.platinum_dest import destination as platinum_destination,
   source as platinum_source, list_target as platinum_list_target` (only the names it uses).
4. **The census line numbers.** `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json` names each writer line by number
   and AC4 re-reads it against the file; your insertions shift lines. Re-read each entry of every script you edited and
   set its `line` to the line now holding the same statement (a text read); change no other field. Same for
   `PRODUCER_CENSUS.md` where it prints numbers.

## 2. BOUNDS

1. Repository files only: no AWS call, no run of any gold script, no edit to a launch, runner or schedule file, no change
   to `lib/config.py`, `lib/platinum_dest_view.py`, `lib/opal_naming.py` or any registry file. The mode is never set here.
2. With the mode unset every line you touch names the same bucket, prefix and key as today, and the pages a listing
   returns are the same: if an edit would change a `legacy` result, STOP and file a BLOCKING row.
3. NO new delete and NO widened delete: a delete you route deletes exactly what it deletes today, moved to the key's
   seam destination. Do not add a delete, a copy or a write that does not exist at base.
4. Reads of non-platinum tiers (bronze, silver, gold canonical) stay on `S3_BUCKET`: the seam is the identity for them.
5. Do not edit a check or the census beyond step 4's line numbers. No bucket name typed anywhere. Client ids appear in keys:
   your report names counts and script paths, never a key. No non-ASCII in code; LF line endings. If something cannot be
   met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/lib/platinum_dest.py
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
data/black_diamond/scripts/gold/lib/advisor_nna_attribution.py
data/black_diamond/scripts/gold/lib/display_label.py
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/lib/exclusions.py
data/black_diamond/scripts/gold/lib/floored_percentiles.py
data/black_diamond/scripts/gold/lib/gold_utils.py
data/black_diamond/scripts/gold/lib/helpers.py
data/black_diamond/scripts/gold/lib/mix_views.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~20/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/` and `round3/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~20/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-20 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py --root /c/dev/wk-firmbkts-20; echo "exit=$?"</invocation><expect>ROUND 3 READ CENSUS: ALL SITES ROUTED, NOT-SERVED OR EXEMPT</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-20 &amp;&amp; timeout 110 python -m unittest discover -s data/black_diamond/scripts/gold/tests -p "test_platinum_dest.py" -k TestSource -k TestListTarget -k TestCanonicalNegativeArm 2&gt;&amp;1 | tail -n 3</invocation><expect>^OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-20 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_producers.py --arms static --root /c/dev/wk-firmbkts-20; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCERS STATIC: 4 of 4 arms</expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-9"><invocation>cd /c/dev/wk-firmbkts-20 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_census.py --census org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json --root /c/dev/wk-firmbkts-20; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCER CENSUS: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 is the CTO's AST census (UNROUTED 0), FAIL at base (69). AC2 runs the three new test classes (the legacy identity, the
canonical equality and the canonical negative arm); at base none exists, so it selects no test and does not read OK. AC3 is the
phase A build still dormant and identical in `legacy` over all 52,910 manifest keys (PASS at base as a control). AC4 is
the census still reading the writer lines at their numbers (PASS at base; it FAILS if step 4 is skipped, because your
insertions move lines): a fourth criterion, carried because the line binding is the census's own design. Each
invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~20`.
Commit the seam, the tests, the routed scripts and libs, the census files and your rows, then the instance second (its
artifact rows pin to the commit that holds them). **Do not flip this order's `<status>`:** phase B is the issuer's to
amend. Row ids: `ADVI_FIRMBKTS-D1-W20-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the AC1
output in full, the census counts before and after, the list of sites you could not drive in the negative arm (file:line),
which of the 35 rows each fixed (by row id), and the commit hash.

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
<slot>~20</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
