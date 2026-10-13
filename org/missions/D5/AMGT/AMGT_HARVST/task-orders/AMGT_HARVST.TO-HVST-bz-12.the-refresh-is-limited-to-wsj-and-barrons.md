# AMGT_HARVST task order -- `HVST-bz-12` -- ROUND 85 (row `AMGT_HARVST-D1-S16`, `HVST-bz-9`'s own scope): THE ONE REFRESH IS LIMITED TO THE TWO DOW JONES PUBLISHERS, `wsj` AND `barrons`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-12.the-refresh-is-limited-to-wsj-and-barrons</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~140</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO Secrets Manager call, NO sign-in, NO S3 call, NO collector or runner run against the world, NO scheduled task, NO site Z box.
comp-adversary: RUN at L5 -- the adversary is a refresh that still fires for a publisher outside the two (the Bloomberg-side branch reads a Google credential), a constant that is widened by a later edit without a test failing, and an existing bz-9 test that quietly stops testing the refresh because its publisher no longer qualifies.
</preflight>

## 0. THE CELL

`HVST-bz-9` (merged at `44aadb7f1d`) added `--refresh-once` to `lib/opal_data_harvest/backfill_driver.py`: a job refused as `expired` (status `sign_in_refused`) gets one `SessionManager.refresh(publisher)` per publisher per cycle and its pair is replayed once. It decides on the CLASS only (`refresh_wanted(checkpoint, pub, result)`),
for every publisher. But `SessionManager._refresh` (`lib/opal_data_harvest/auth.py`) signs `wsj` and `barrons` in through the Dow Jones script, and signs EVERY OTHER publisher in through `harvest_local_session.py`, whose credential for `bbg` is the secret `google/andrew-goldengate/credentials` (`lib/opal_data_harvest/credentials.py`). The ruling that ordered the refresh
closes on `wsj` and `barrons` only. This cell limits it to those two. A refusal of any other publisher is still RECORDED (the `REFUSAL` line and the checkpoint's `refusals`), and never refreshed.

## 1. THE BUILD (LOCAL, about 40 product lines)

Work in your worktree. Change only the files named in `<paths>`.
1. In `lib/opal_data_harvest/backfill_driver.py` add one module-level constant `REFRESH_PUBLISHERS = frozenset({"wsj", "barrons"})` with a one-line comment naming why (the other publishers' refresh seam reads a different credential), and make `refresh_wanted()` also require `pub in REFRESH_PUBLISHERS`.
   Nothing else in the driver changes: `note_refusal`, the class table, `spend_refresh`, the loop in `drive()` and the CLI flag are untouched.
2. In `lib/opal_data_harvest/test_bz9_refresh_once.py`: the arms that exercise a refresh with publisher `"sa"` (about lines 186-310; read them) must use `"wsj"` instead, so they still test the refresh. Change only the publisher name and the assertions that quote it. Keep every arm and every assertion otherwise as it is.
3. New tests in `lib/opal_data_harvest/test_bz9b_refresh_publishers.py` (reuse the fakes of `test_bz9_refresh_once.py`; no network):
   - (a) a loop over EVERY publisher in `credentials.PUBLISHERS` (`sa`, `ft`, `wsj`, `bbg`, `barrons`), flag ON, the fake collector returning `sign_in_refused` with a `refusal` on the first pair: `wsj` and `barrons` make exactly ONE refresher call and replay the pair; each of `sa`, `ft`, `bbg` makes ZERO refresher calls, prints one `REFUSAL <publisher> ... class=expired` line, does not replay,
     and stops the leg `sign_in_refused` as it does without the flag.
   - (b) the constant equals exactly `{"wsj", "barrons"}`.
   - (c) **A MUTANT:** with `REFRESH_PUBLISHERS` monkeypatched to `frozenset(credentials.PUBLISHERS)`, arm (a) FAILS (assert that it does, e.g. `bbg` then makes one refresher call). This proves (a) discriminates.
4. Do not run anything against a publisher, S3, Secrets Manager or the site Z box, and do not register or start a scheduled task. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/test_bz9_refresh_once.py
lib/opal_data_harvest/test_bz9b_refresh_publishers.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~140/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-12"><invocation>python -m pytest lib/opal_data_harvest/test_bz9b_refresh_publishers.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-12"><invocation>python -m pytest lib/opal_data_harvest/test_bz9_refresh_once.py lib/opal_data_harvest/test_ad2_no_sign_in.py lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_bx3_failure_reason_kept.py lib/opal_data_harvest/test_ae4_backfill_driver.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure and no skip-only run.
- **Dry-run at the base (issuer, dell1, 2026-10-13 ~22:5xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`100 passed`: 24 + 76).
- The full `lib/opal_data_harvest` suite on a CLEAN checkout of the merge `44aadb7f1d` has 4 failures (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`, three in `test_aw1_origin_load_wait.py`). Your worktree is clean, so the same four are expected. Run it before and after, and record both counts. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W140-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~140/AMGT_HARVST.TO-HVST-bz-12.the-refresh-is-limited-to-wsj-and-barrons.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bz-12.the-refresh-is-limited-to-wsj-and-barrons` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-bz-12.the-refresh-is-limited-to-wsj-and-barrons.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: row `AMGT_HARVST-D1-S16` (its notes call this cell `bz-9b`; the decomposition grammar refused a letter suffix, so the cell id is `HVST-bz-12`) (BLOCKING, INERT, this seat), decomposition section 105. The ruling it narrows: CTO msg 5143 / `ROUND_ANALYSIS.round84.md` section 2 item 1, which closes on `wsj` and `barrons`.
- **The miss was this seat's:** the bz-9 order said "any publisher whose class is expired", and the COO merge half read the diff for what it recorded, not for which credential the refresh seam could reach. Found while drafting the bz-10 pair, before anything was registered.
- Direct act: ONE cell, LOCAL, about 40 product lines, no L2, L4-R or L8 to L10 (dispatch skill, the DIRECT-ACT path); the merge still goes through `safe-merge.sh` under an addendum to the bz-9 pair (COO addendum, and the CTO's producer-half addendum).
- Slot ~140, worktree `C:/dev/wk-harvst-140`, branch `wk-AMGT_HARVST-140-r85`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>issued</status>
<round>85</round>
<workstream>REFRESH-REPAIR</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
