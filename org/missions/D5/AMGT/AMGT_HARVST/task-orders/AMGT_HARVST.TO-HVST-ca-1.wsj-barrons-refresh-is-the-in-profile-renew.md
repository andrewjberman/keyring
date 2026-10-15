# AMGT_HARVST task order -- `HVST-ca-1` -- ROUND 86: A TAB PUBLISHER THAT DOES NOT SEED FROM A BUNDLE IS REFRESHED BY THE IN-PROFILE RENEW (WSJ AND BARRON'S)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ca-1.wsj-barrons-refresh-is-the-in-profile-renew</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ca-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~141</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO Secrets Manager call, NO sign-in, NO browser launch, NO S3 call, NO collector or runner run against the world, NO scheduled task, NO site Z box.
comp-adversary: RUN at L5 -- the adversary is a rule keyed on the names `wsj` and `barrons` (a third tab publisher would silently keep the bundle refresh), a renew that is called for a publisher whose bundle IS seeded (`bbg`, `sa`, `ft`), and a test whose fake renew can never be reached so that it passes whatever the code does.
</preflight>

## 0. THE CELL

For `wsj` and `barrons` the contract (`lib/opal_data_harvest/contracts.json`) says `"transport": "tab"` and `"seed_from_bundle": false`. A job for such a publisher reads a persistent browser PROFILE (`lib/opal_data_harvest/tab_transport.py`, profile root `default_profile_root()`), and the saved bundle is never loaded into it (`publishers.py` `_ensure_session`, the `seed_from_bundle` test).
But `SessionManager.refresh(publisher)` in `lib/opal_data_harvest/auth.py` only runs the sign-in script and saves a bundle. So a refresh does not cure an expired profile: measured on dell1, a refreshed `wsj` job was still refused `expired` ("Dow Jones session is logged out", `publishers.py` `DowJones.check`), and after
`lib/opal_data_harvest/verification.py` `renew(tab_session, publisher)` ran in the profile (it signs in INSIDE the profile; the browser jar is the store) the same job ended `complete_candidates` with 5 accepted.

This cell makes the refresh of such a publisher BE the in-profile renew. Two callers reach `SessionManager.refresh`: the worker's `AuthExpired` branch (`worker.py`, the `except AuthExpired` block) and the cycle driver's `--refresh-once` refresher (`backfill_driver.py`, `Collector.refresh`). Fixing `SessionManager.refresh` fixes both; change neither caller except as 1.c says.

## 1. THE BUILD (LOCAL, about 60 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/opal_data_harvest/auth.py`: `SessionManager.refresh(publisher)` checks the publisher's contract (`publishers.REGISTRY["publishers"][publisher]`). When `contract.get("transport") == "tab"` AND `contract.get("seed_from_bundle", True) is False` AND `publisher in verification.ACCOUNT_CHECKS` (AMENDMENT 1, 2026-10-15 ~16:5xZ: `sa` is also tab with `seed_from_bundle` false but has no measured account check, so `renew` would raise for it; it keeps the existing refresh until its own proof, and the set the rule selects is exactly `wsj` and `barrons`), it opens `tab_transport.TabSession(publisher, str(tab_transport.default_profile_root()), publishers.TAB_ORIGINS[publisher])`,
   calls `verification.renew(tab_session, publisher)`, ALWAYS closes the tab session (`finally`), and returns an envelope the existing callers can use (`{"publisher": ..., "bundle": <the last saved bundle for it or {}>, "network_auth_corroborated": <renew's renewed or not-stale result>, "renewed_by": "browser", "captured_at": <now, UTC ISO>}`); it does NOT call the sign-in script and does NOT save to the vault on this path.
   If `renew` returns a record with `renewed` false and `stale` true, raise `AccountUnavailable("Dow Jones in-profile renewal did not log in")` (imported from `.transport`). Any other publisher takes the existing code, byte for byte.
   KEY THE TEST ON THE CONTRACT FIELDS AND THE ACCOUNT-CHECK TABLE ONLY, never on a publisher name.
b. `SessionManager` keeps the last renew record in `self.last_renewal` (None when the bundle path ran). The record holds field names and hashes only; never print or store a cookie or a credential.
c. In `lib/opal_data_harvest/worker.py`, in the `except AuthExpired` block, right after `envelope = self.sessions.refresh(publisher)`, set `result["profile_renewal"]` to a dict of exactly `renewed`, `stale`, `operator_input_detected`, `post_renewal_status` copied from `getattr(self.sessions, "last_renewal", None)` (or leave the key out when it is None), and add the same four fields to the `retry_after_reauth` event the block already records. Change nothing else in the worker. The `--no-sign-in` branch above it stays as it is.
d. New tests in `lib/opal_data_harvest/test_ca1_profile_renew.py` (no network, no browser: monkeypatch `verification.renew` and `tab_transport.TabSession` with fakes that count calls, and `tab_transport.default_profile_root` to a temp dir):
   - (a) a loop over EVERY publisher in `publishers.REGISTRY["publishers"]` (`sa`, `ft`, `wsj`, `bbg`, `barrons`): the fake renew is called exactly ONCE for a publisher whose contract is tab with `seed_from_bundle` false AND that is in `verification.ACCOUNT_CHECKS` (`wsj`, `barrons`) and ZERO times for every other (`sa`: tab, seed false, no account check; `ft`, `bbg`: seeded); the expected set is computed from the contract and the table inside the test, and asserted equal to `{"wsj", "barrons"}` as a second assertion;
   - (b) a synthetic publisher added to COPIES of the registry and of `ACCOUNT_CHECKS` with `transport` tab, `seed_from_bundle` false and an account check gets the renew; one with tab and `seed_from_bundle` true (or absent) does not; one with tab, seed false and NO account check does not (it takes the old refresh);
   - (c) the tab session is closed when renew raises; and `renewed` false with `stale` true raises `AccountUnavailable`;
   - (d) the worker: a fake client whose first attempt raises `AuthExpired` for `wsj` with the real `SessionManager.refresh` wired to the fakes: `auth_refreshes` is 1, the pair is replayed once, `result["profile_renewal"]` carries the four fields, and with `no_sign_in=True` the same job ends `sign_in_refused` and the fake renew is called ZERO times (reuse the fakes of `test_worker.py` and `test_bz9_refresh_once.py`);
   - (e) **A MUTANT:** with `SessionManager.refresh` monkeypatched to the old behaviour for `wsj` (the bundle path only), arm (a) FAILS (assert that it does). This proves (a) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or the site Z box; do not launch a browser; do not register or start a scheduled task. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/auth.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_ca1_profile_renew.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~141/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ca-1"><invocation>python -m pytest lib/opal_data_harvest/test_ca1_profile_renew.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ca-1"><invocation>python -m pytest lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_ad1_token_store.py lib/opal_data_harvest/test_ad2_no_sign_in.py lib/opal_data_harvest/test_bz9_refresh_once.py lib/opal_data_harvest/test_bz9b_refresh_publishers.py lib/opal_data_harvest/test_ab1b_trust_token_and_backoff.py lib/opal_data_harvest/test_ae5_challenge_path.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed, 4 subtests passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2's pattern matches only a run with no failure (the 4 subtests are the base's own).
- **Dry-run at the base (issuer, dell1, 2026-10-15 ~16:3xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`113 passed, 4 subtests passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. A clean checkout carries 4 known failures (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`, three in `test_aw1_origin_load_wait.py`); add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W141-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~141/AMGT_HARVST.TO-HVST-ca-1.wsj-barrons-refresh-is-the-in-profile-renew.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ca-1.wsj-barrons-refresh-is-the-in-profile-renew` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ca-1.wsj-barrons-refresh-is-the-in-profile-renew.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO `ROUND_ANALYSIS.round85.ADDENDUM_2_R86_CODE_CELL.md` (msg 6081) on the first read `ledger/ROUND86_FIRST_DELL1_READ_20261015.md` @06d5850df2; answered row `AMGT_HARVST-D1-S17` (Z-S121). The ruling keys the cell on the contract fields (1.a), allows at most three mechanical criteria, and names a third: a real expired-then-renewed job with no person at the keyboard, recording `operator_input_detected`.
- **That third criterion is the ISSUER'S, not the worker's** (the CTO to be told): the worker runs every invocation under `timeout 120` and a headful sign-in job takes about two and a half minutes, so it cannot be a worker criterion. It is `deliverables/2.0.0_SA_COO_W1/round86/ca1_real_job.py` (AC3): run by the issuer from a linked worktree of the merged head at the drain; its last line is `AC3 RESULT: PASS`, `FAIL ...` or `NEEDS-PERSON` (a true `operator_input_detected` reports that and does not pass).
- Direct act: ONE cell, LOCAL, about 60 product lines; no L2, L4-R or L8-L10 (dispatch skill, the DIRECT-ACT path). The close is the issuer's AC3 run plus the merge through `safe-merge.sh`.
- **The order runs no vendor call, so it spawns now.** `0.0.0_AB_MSTR~DELL1` has not confirmed that site Z (`~ZW`) stopped wsj and barrons (relay 6085: ruled, not applied); the CTO's hold (addendum 2) is on dell1 JOBS and RENEWS for those two, which this build never makes. AC3 (a real job and a renew) is held until that confirmation.
- Slot ~141, worktree `C:/dev/wk-harvst-141`, branch `wk-AMGT_HARVST-141`.
- **AMENDMENT 1 (issuer, 2026-10-15 ~16:5xZ), from the worker's first report (rows `D1-W141-S1`, `D1-W141-S2`):** (1) my face assumed `sa` was bundle-seeded; the contract says `sa` is tab with `seed_from_bundle` false, so the literal rule reaches it and `verification.renew` has no account check for it. The rule now also requires `publisher in verification.ACCOUNT_CHECKS` (the CTO's ruling keys on the contract fields; this adds the capability the renew needs, and leaves `sa` on its present path until round 87's `sa` proof; the CTO is told). (2) The sparse worktree lacked `org/tier1_exec/4.0.0_SA_CRO/scripts` (test_ad1 reads `sa_rest_fetch.py`); the issuer added it to the worktree's sparse set, `test_ad1_token_store.py` now `13 passed`. The paths grant is unchanged.

**COMPLETE 2026-10-15 ~17:0xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~141` (worker-light, haiku, high), branch `wk-AMGT_HARVST-141`, first report FAILED both criteria (rows `D1-W141-S1` sa scope, `D1-W141-S2` sparse set; both were defects of this order, repaired by AMENDMENT 1 `f94a1a7d09`), resumed on the same context; head `356932e3a9`.
- **AC1 PASS:** `8 passed` (worker; this seat re-ran in the worker's worktree `8 passed in 0.19s`). **AC2 PASS:** `113 passed, 4 subtests passed` (worker; this seat `113 passed, 4 subtests passed in 3.61s`; base the same). Proof instance VALID rc 0 with `--governing-order`, re-run by this seat. `round-close-check --round 86` before this flip: MAY-CLOSE.
- **Diff read by this seat:** `auth.py` (+38: the renew path keyed on `transport` tab, `seed_from_bundle` false and `ACCOUNT_CHECKS`; the old path byte for byte otherwise; tab session closed in `finally`), `worker.py` (+9/-3: `profile_renewal` on the result and the retry event, empty when the bundle path ran).
- **What this does NOT prove:** a real job refused expired, renewed in the profile with no person at the keyboard, and ended complete. That is AC3 (`deliverables/2.0.0_SA_COO_W1/round86/ca1_real_job.py`), the issuer's run at the drain, held for site Z's read-back relayed by `0.0.0_AB_MSTR~DELL1`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>complete</status>
<round>86</round>
<workstream>PROFILE-RENEW</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
