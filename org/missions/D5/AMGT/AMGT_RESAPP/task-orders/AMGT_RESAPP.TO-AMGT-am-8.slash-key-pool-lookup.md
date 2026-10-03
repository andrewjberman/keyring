# AMGT_RESAPP task order -- `AMGT-am-8` -- THE PEERS ENGINE FINDS A SLASH KEY'S POOL MODEL BLOCK (Z-W4-S6: BP and NG serve stale 09-25 labels)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~209</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- `lib/research/peers/engine.py:165` tests `security_key in pool_index` with the RAW key, while `universe.model_block_pool_index()` keys by the slash-safe store segment; BP/_LN_Equity and NG/_LN_Equity miss and fall back to the 09-25 repo file (CORPUS row Z-W4-S6, CTO msg 28541).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-209` (branch `wk-AMGT_RESAPP-209`, cut from the issuance commit with `--portal-ref a730d8ce`). Work and
commit only there.

## 1. THE ACT -- `AMGT-am-8` (round 63, decomposition s.71)

1. In `lib/research/peers/engine.py` (~line 165), the pool lookup takes the slash-safe form
   (`crosswalk_module.slash_safe_key(security_key)`), or the index is keyed by the raw key, whichever matches what
   `universe.model_block_pool_index()` and `universe.read_model_block_from_pool` agree on. A slash key (`BP/_LN_Equity`,
   `NG/_LN_Equity`) then reads its POOL model block, not the repo file. Check the other lookups in `lib/research/peers/` against the
   same index for the same defect, and name each one fixed.
2. **The plant:** `lib/research/peers/tests/test_engine_slash_key_pool_lookup.py`. A slash key present in a planted pool index reads
   the POOL block (a mutant restoring the raw-key lookup reads the repo file and FAILS); a plain key is unchanged.
3. **Where it is served:** report whether the peers engine runs at REQUEST time in the scoped API package or only when the
   `peers/v1/` objects are BUILT.
   - Request time: the fix serves through the round's code redeploy, and you are done.
   - Build time: write a read-only plan
     `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~209/peers_slash_plan.json`, listing every `peers/v1/` object
     whose stored labels the fix changes (re-built by the producer's own code from stored inputs). Never write the pool.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/peers/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~209/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/peers/tests/ lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, the new test included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/peers/tests/test_engine_slash_key_pool_lookup.py; echo "exit=$?"</invocation><expect>every test in the plant passes (a slash key reads its POOL block; a plain key is unchanged), and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~209 <0.9.0_WK_AMGT_RESAPP~209@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~209/AMGT_RESAPP.TO-AMGT-am-8.slash-key-pool-lookup.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, each lookup fixed, where the engine is served (request or build time), the
plan if any, and any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~15:5xZ) -- the rebuild plan for the two served peers objects

Your report placed the fix at BUILD time: `scoped_amgt.read_peer_set` only reads stored `peers/v1/` objects. The two objects the route
serves for the slash keys, `peers/v1/BP-SLASH-_LN_Equity/2026-09-24T2252Z.json` and `peers/v1/NG-SLASH-_LN_Equity/2026-09-24T2252Z.json`,
carry the 09-25 repo model block's labels. So:
1. Re-build both objects with the FIXED producer (`lib/research/peers/`), from STORED inputs only (the pool model blocks, the stored
   universe rows). No vendor call, no pool write. Write each to a LOCAL pool directory
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~209/peers_pool/peers/v1/<slash-safe key>/2026-10-02T<HHMM>Z.json`.
2. Rewrite `peers_slash_plan.json` as
   `{"entries": [{"security_key", "store_key": "peers/v1/<slash-safe key>/2026-10-02T<HHMM>Z.json", "exists_now": false, "sha256": <of the object bytes>, "served_field_changes": [{"json_path", "before", "after"}]}]}`.
   `served_field_changes` lists the fields the peers route will serve differently, measured by diffing the served body of the current
   object against the new one. At least one field must show the 09-25 label replaced by the newer model block's.
3. A test proving the rebuild reads the pool block for a slash key (your plant already does: name it).
The keys are NEW (newest as_of wins), so nothing existing is overwritten. am-7 is amended to PUT them.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 28541 ruling 2 (Z-W4-S6 is RESAPP's; no CORPUS path grant). Served by am-6 if request-time, or by am-7
extended to the plan (an amendment) if build-time.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~209</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~16:1xZ):** ACCEPTED, AMENDMENT 1 included. Worker ~209 `a0f3f2d087` (drained
`2e43f485b9`) and `c003078cd3` (drained `6899726ed8`). Re-graded on the shared tree: AC1 in the union run 589 passed exit=0; AC2
3 passed. Plan `peers_slash_plan.json` frozen at sha256 `ccb09b8ab20a7caff35bdf19970444b423da5d5b9dbe302a17002a8b969fec22` (BP and NG, 26 served_field_changes each, new keys
`2026-10-02T1543Z`). Served by am-7 (AMENDMENT 1).

<status>complete</status>
