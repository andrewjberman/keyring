# AMGT_RESAPP task order -- `AMGT-ay-2` -- /freshness AS ONE PRECOMPUTED SNAPSHOT: THE REFRESH STEP WRITES IT, THE ROUTE READS IT (FWD-7, CTO RULING 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~258</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: RUN by the issuer at the cut -- the snapshot is a NEW key. Its read and write by the function are listed for ay-5's pair, which carries any grant leg and simulates it. This cell writes no store.
comp-adversary: RUN by the issuer at the cut -- a /freshness cache miss on deployed 0MZWPl7n takes 7,488 ms in the handler (Init 653 ms) for a 2,850,172 B body; the walk's first visit took 9.1 s. r75 c59 local FAILS (no snapshot builder).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r75-258` (branch `wk-AMGT_RESAPP-258`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r75-258`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ay-2` (round 75, decomposition s.83)

CTO ruling 3. `read_coverage_freshness` (`lib/research/api/scoped_amgt.py` ~`:5598`) lists four store prefixes, reads the
universe, the covered names and the pack ledgers on every miss. The route holds the view for 60 s in-process (ax-1).
1. **The builder:** a new module `lib/research/freshness/snapshot.py` with:
   - `build_freshness_snapshot()`, which returns the view `read_coverage_freshness()` computes, plus `generated_at`;
   - `write_freshness_snapshot(client)`, which writes it as ONE JSON object.
2. **The address.** It is `lib/opal_naming.py address()` output (CLAUDE.md rule 30), never a hand-typed key. If the builder REFUSES,
   a registry row is missing. Do not work around it: file a row naming the missing registry entry and the address you need, and use
   the builder's output shape in tests. The registry row is added under ay-5's pair. Report the address and its tier home.
3. **The refresh step writes it.** The step that refreshes the pack ledgers (the refresh path in `scoped_amgt.py`, ~`:5758`) calls
   `write_freshness_snapshot` after its ledger write.
4. **The route reads it.**
   - `/freshness` serves the snapshot object with one GET, and adds `snapshot: {"object", "generated_at"}` to the body.
   - An absent or unreadable snapshot falls back to the computed view and says so in plain words. It never answers 500.
   - Keep the 60 s hold.
5. **Plant tests** in `lib/research/api/tests/test_freshness_snapshot.py`:
   - the route serves the snapshot with one GET and no listing;
   - absent, it falls back;
   - the refresh step writes once.

This cell writes NO store object. The first write is ay-5's leg, under a pair. List the function's new read and write (bucket, key)
in your report.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W258-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. Values EQUAL: the snapshot's rows equal the computed view's rows (AC1).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/freshness/
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~258/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ay-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where local; echo "exit=$?"</invocation><expect>the snapshot builder's rows EQUAL the computed view on every row; C1 PASS; R75 C59 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_freshness_snapshot.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~258 <0.9.0_WK_AMGT_RESAPP~258@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~258/AMGT_RESAPP.TO-AMGT-ay-2.freshness-snapshot.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the snapshot address and the function's new read/write (bucket, key);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-74 analysis item 3, ruling 3. The page's DEV push waits on this. Served by ay-5 (first write under the pair).

<status>pending</status>
<round>75</round>
<slot>0.9.0_WK_AMGT_RESAPP~258</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-06 ~10:2xZ) -- on rows Z-W258-S1 (ARMED) and Z-W258-S2. Same worker, same branch.**

The issuer confirmed S1's premise failure: `lib/research/ledger/ledger.py` `record_run` has no production caller (only its own
`rerun` and tests). No step refreshes the pack ledgers, so nothing re-writes the snapshot after ay-5's first write. The write cadence
goes to the CTO. This amendment DISARMS the hazard, in which a stale snapshot is served as current:
1. **A maximum age.** The route serves the snapshot only while its `generated_at` is within 24 hours (one trading day). Past that it
   treats the snapshot as absent: it computes the view, says so in plain words in `snapshot_fallback`, and never answers 500.
   - Every body that serves the snapshot carries `snapshot: {"object", "generated_at", "age_hours"}`.
   - Add plant tests for an aged snapshot (it falls back) and a fresh one (it is served).
2. **The mount test (S2).** `lib/research/api/tests/test_scoped_amgt_mount.py` compares terraform's mounted routes with the handled
   routes. Since ax-5 it fails 19 vs 18 on `GET /api/scoped/amgt/security/{proxy+}`. Apply the same rule as the terraform guard
   (ax-5 AMENDMENT 2): compare the NON-greedy keys for equality, and allow at most one greedy key, which must sit under
   `/api/scoped/amgt/security/`. The test file is in your paths.
3. **Criteria unchanged** (c59 local; your test file). Also report the full api suite's last line: it must read 0 failed.

Gate limb: GATE (viii) on a modify.

