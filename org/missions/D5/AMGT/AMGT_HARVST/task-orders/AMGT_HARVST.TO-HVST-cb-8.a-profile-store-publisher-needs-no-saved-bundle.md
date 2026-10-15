# AMGT_HARVST task order -- `HVST-cb-8` -- ROUND 87, workstream PROFILE-STORE: A PUBLISHER WHOSE SESSION LIVES IN ITS BROWSER PROFILE NEEDS NO SAVED BUNDLE TO START A JOB

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-8.a-profile-store-publisher-needs-no-saved-bundle</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~145</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and one test only. NO publisher host, NO Secrets Manager call, NO sign-in, NO browser launch, NO S3 call, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is a rule keyed on publisher names, a change that lets a publisher WITH a bundle-seeded tab (`bbg`, `ft`) start without a stored session, a change to the `--no-sign-in` guarantee (no sign-in, no browser, no credential read), and a test that cannot fail.
</preflight>

## 0. THE CELL

A collector job asks `TokenFirstSessions.get(publisher)` (`lib/opal_data_harvest/sessions.py`) for a stored session before it opens the publisher's tab. When none is stored it calls `refresh`, which under `--no-sign-in` raises `SignInRefused("sign-in refused: --no-sign-in")`. For `wsj` and `barrons` the stored session is never used: their contract is `transport` tab with `seed_from_bundle` false, so the session lives in the persistent BROWSER PROFILE and the bundle is ignored (`publishers.py` `_ensure_session`). MEASURED on dell1 (2026-10-15 20:23Z, the runner's first pass; run record `20261015T202310Z-wsj-23b255623f`): the runner's runtime root held no saved session, so every job ended `sign_in_refused` with `token_source` None and `request_attempts` empty: no request, no tab, no profile read. The same publishers' jobs ran fine from a runtime root that held an old bundle.
HVST-ca-1 (`d0c48b3946`) made `SessionManager.refresh` (in `lib/opal_data_harvest/auth.py`) take the in-profile renew for exactly such a publisher: contract `transport` tab, `seed_from_bundle` false, AND `publisher in verification.ACCOUNT_CHECKS`. This cell makes the SAME predicate decide that `get()` needs no stored session.

## 1. THE BUILD (LOCAL, about 25 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/opal_data_harvest/auth.py`: factor the predicate that `SessionManager.refresh` already tests into a module-level function `profile_is_store(publisher)` returning True iff the publisher's contract (`publishers.REGISTRY["publishers"].get(publisher)`) has `transport == "tab"` and `seed_from_bundle` explicitly False and `publisher in verification.ACCOUNT_CHECKS`. `SessionManager.refresh` calls it in place of its inline test; its behaviour does not change.
b. In `lib/opal_data_harvest/sessions.py` `TokenFirstSessions.get(publisher)`: when `_stored_envelope` found nothing (`envelope is None`) AND `auth.profile_is_store(publisher)` is True, return a profile-store envelope WITHOUT calling `refresh`: `{"publisher": publisher, "bundle": {}, "network_auth_corroborated": False, "renewed_by": "profile", "captured_at": <now, UTC ISO>}`; set `self._described[publisher] = {"token_source": "browser_profile", "signed_in": False}` and record `{"event": "profile_store_used", "publisher": publisher, "token_source": "browser_profile", "signed_in": False}`. When a stored envelope IS found the existing code runs unchanged. Every other publisher, stored or not, takes the existing code byte for byte. Touch nothing else in the file; the `--no-sign-in` branches of `refresh` and `repair_verification` stay.
c. The envelope's EMPTY `bundle` must not break the paths that read it: read `verification.repair` (the Barron's challenge repair loads the saved cookies) and `publishers.py` for `["bundle"]` and `bundle[` uses, and for each tell in your report whether an empty bundle is safe for a tab publisher with `seed_from_bundle` false. If one is NOT safe, do not change it: file a row naming the line and keep the rest.
d. New test `lib/opal_data_harvest/test_cb8_profile_store_envelope.py` (no network, no browser, no Secrets; use a temp directory as the runtime root, and fake `SecretsReader`/`inner` objects as `test_ab1b_trust_token_and_backoff.py` and `test_ad2_no_sign_in.py` do):
   - (1) a loop over EVERY publisher in `publishers.REGISTRY["publishers"]` with an EMPTY vault and `no_sign_in=True`: for a publisher where `auth.profile_is_store` is True, `get()` returns an envelope with `bundle` equal to `{}` and the fake `refresh` is called ZERO times and no credential is read; for every other publisher `get()` raises `SignInRefused` exactly as before; the set where it is True is computed from the contract and asserted equal to `{"wsj", "barrons"}` as a second assertion;
   - (2) a publisher WITH a stored envelope returns it unchanged (token source as before);
   - (3) with `no_sign_in=False` and an empty vault, a profile-store publisher still returns the profile envelope and calls no refresh (the renew happens later, on a refusal, in the worker);
   - (4) `describe_token` names `browser_profile` for it, and the event `profile_store_used` was recorded;
   - (5) **A MUTANT:** with `auth.profile_is_store` monkeypatched to always False, arm (1) FAILS (assert that it does). This proves (1) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/auth.py
lib/opal_data_harvest/sessions.py
lib/opal_data_harvest/test_cb8_profile_store_envelope.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~145/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-8"><invocation>python -m pytest lib/opal_data_harvest/test_cb8_profile_store_envelope.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-8"><invocation>python -m pytest lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_ad1_token_store.py lib/opal_data_harvest/test_ad2_no_sign_in.py lib/opal_data_harvest/test_bz9_refresh_once.py lib/opal_data_harvest/test_bz9b_refresh_publishers.py lib/opal_data_harvest/test_ab1b_trust_token_and_backoff.py lib/opal_data_harvest/test_ae5_challenge_path.py lib/opal_data_harvest/test_ca1_profile_renew.py lib/opal_data_harvest/test_ab1_live_reach_and_seed.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^144 passed, 4 subtests passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `144 passed, 4 subtests passed`: the base's own count.
- **Dry-run at the base (issuer, dell1, 2026-10-15 ~20:4xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`144 passed, 4 subtests passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. On a clean main checkout one failure is known (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** `auth.py` and `sessions.py` may carry mixed line endings. Edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W145-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~145/AMGT_HARVST.TO-HVST-cb-8.a-profile-store-publisher-needs-no-saved-bundle.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-8.a-profile-store-publisher-needs-no-saved-bundle` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-8.a-profile-store-publisher-needs-no-saved-bundle.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO addendum 2 (`ROUND_ANALYSIS.round85.ADDENDUM_2_R86_CODE_CELL.md`) allowed the round-86 cell and asked that a third tab publisher get the same rule; this is the sibling defect it did not reach, read in the first dell1 cycle (SC1 msg 6206; rows `AMGT_HARVST-D1-S19`, `-S20`). The CTO required the read before a code change: it is in (`cycle_runner.log` lines 245-252 and 502-509, run record `20261015T202310Z-wsj-23b255623f`).
- **The operational unblock meanwhile** is amendment 1 of `HVST-cb-2` (seed the runner's saved-session directory); this cell removes the need. It reaches the runner by a RE-PIN, which needs its own pair half (cb-9) and the executor's act; until then the seeded directory keeps the runner running.
- The real-job criterion is the issuer's again (the 120 s cap): after the merge, run one `wsj` job with `--no-sign-in` from a worktree whose runtime root has NO saved session and whose profile is signed in; PASS needs `complete_candidates` with accepted > 0 and `token_source` `browser_profile` in the run record.
- Direct act: ONE cell, LOCAL, about 25 product lines; no L2, L4-R or L8-L10.
- Slot ~145, worktree `C:/dev/wk-harvst-145`, branch `wk-AMGT_HARVST-145`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>pending</status>
<round>87</round>
<workstream>PROFILE-STORE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
