# NFRA_OPLGTW task order -- `OG-ap-31` -- APPLY: the round-39 batched gateway release -- windowed 49F partitions, units and currency, numbers and `as_of`, the owner exemption on the browser deny guard, the discover echo (FWD-21, FWD-22; PRD v3.14; CTO round-38 analysis E1 to E4 and E6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-31</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-31</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this release changes NO IAM and adds no env key. The dedicated 49F live role is live from `OG-ap-29`; the adapter reads the same four prefixes through it, now more than one dated file per call. You re-read the role with `iam get-role` in Phase A.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-38 analysis (`ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e: E1 to E4, E6) and the CTO ruling `CTO_RULING_OPLGTW_EMAIL_DENY_SIDE_EFFECT_OF_OG_MG_1_20261016_Z.md` item 2.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-31` (decomposition addendum R3-T.101, round 39, workstream ENRICH-R39-C)

APPLY: ONE code-only release on the live ref (read it, do not assume it: `services.opal-gateway.deployed_commit` at HEAD; it was `bf9d23b518` when this order was cut). No Terraform, no IAM, no new env key, no change to `deploy-to-ec2.sh` or `EC2_MANIFEST.json`, one deploy. The builds are merged to trunk (`box/sitez`): `OG-en-13` (units, currency, numbers, `as_of`, duplicate profile rows), `OG-en-15` (49F transactions and fees read every dated partition in the window, at most 60; exact-duplicate removal instead of the `transaction_id` rule), `OG-en-14` (the email-deny guard takes a route class: a master_admin passes the four internal browser routes, a denied non-admin stays refused) with its repair `OG-en-16` (a test-order fix), and `NFRA_MCPINDEX.TO-MX-c-24` (the opal_discover bucket/vendor/firm echo, six lines in `app/integrations/opal_discover/integration.py` plus tests; CTO R20-3). The GO message names `trunk_sha`, the one trunk commit you take from.

### PHASE A (only on the issuer's GO message, which names `trunk_sha`): re-cut, ask. NO deploy, NO apply IN ANY FORM

1. **Live ref.** Read `services.opal-gateway.deployed_commit` at HEAD and one SSM md5 read of the host against it over `app/`, `deploy/`, `dashboard/` and `lib/`. A mismatch is a STOP and a BLOCKING row. Record `tools_list_before` (the public `tools/list` count to a master_admin stand-in; it read 103 at the last release) and the `.env` key count (65) for AC2. `MUSE_CLIENT_ID` must be ABSENT (names only). `iam get-role gateway-49f-blackdiamond-live-read-role` resolves.
2. **Re-cut** in `C:/tmp/og-rel-batch3`, branch `rel-nfra-oplgtw-batch3`, at the live ref, with `infra/logic/`, `org/missions/DIRECTIVES.yaml`, `org/mcp/naming-gate.enforce` and `infra/aws/globgrph` in the sparse cone. **Enumerate the seams first**: every app module a taken file imports; print each as in-base or in-take-list; a missing seam is a STOP and a row. The take list is the union of the `<paths>` of the complete orders `OG-en-13, 14, 15, 16` and `NFRA_MCPINDEX.TO-MX-c-24` (read each order's `<paths>`; app files and tests only). **Files that differ between the live ref and `trunk_sha` and belong to NO order named here are NOT part of this release** (for example `admin_people_access.py`, `family_depth.py`, `harvest_*.py`, `refs/silver_families.json`, `refs/partner_roster.json`, the yearinreview files, `tools.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, `EC2_MANIFEST.json`); a taken file that imports one is a missing seam: STOP. The shared files (`app/data_entitlement.py`, `app/server.py`, `app/client_adapter_bd49f.py`) may carry hunks other orders wrote: print `git diff <live ref> <trunk_sha> -- <file>` hunk counts and attribute EACH hunk to one of the named orders; a hunk no named order wrote means the file is taken BY HUNK (3-way against the base), never whole; an unattributable hunk you cannot place is a STOP and a row. Tests: the files named by those orders' `<paths>`, run in the release tree after the take.
   **The naming gate.** The live ref already carries the two registry files (`infra/logic/registry/catalog_fork_keys.json`, `legacy_addresses.json`) from `OG-ap-28`'s prelude. If the ENFORCE gate refuses any string because a registry file at the live ref is older than the one at `trunk_sha`, add ONE prelude commit under the audited `GIT_COMMIT_AUTHOR_OVERRIDE=PLATFORM_LOGIC_DOCS` carrying exactly those registry files byte-equal to `trunk_sha` (as `OG-ap-28` did); otherwise no prelude. `ap31.AC1` requires every registry file in the diff to be byte-equal to trunk's blob.
   Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only; the naming gate runs in ENFORCE and must print NO REFUSE (if it refuses a string, STOP and file a BLOCKING row naming the (name, type)). Write `W/ap31_release.json` = `{"base_sha", "release_sha", "trunk_sha"}` (FULL 40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`).
   Run in the release tree: every taken test file; the pinned-count tests; the host-shaped import check. A failing taken test that also fails at the live ref is recorded by name and carried (the gateway set carried 4 red tests at the last release); a failing taken test that passes at the live ref is a STOP. Run the touched test files together in BOTH orders (a test must not depend on what ran before it; `OG-en-16` repaired one such dependency).
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-31.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file (no manifest or deploy-script change); (2) the `widening`, stated plainly: NO new IAM, NO new env key, NO tool added or removed; the 49F transactions and fees answers now read up to 60 dated files per call (more S3 reads of the same four prefixes through the same dedicated role, master_admin only) and stop dropping rows that share a `transaction_id`; answers gain `weight_unit`/`weight_unit_basis` (allocation: `null` with `not_established`, because the live scale could not be established, row Z-S313), `currency`/`currency_basis` (transactions and fees, `source_absent`), `exact_duplicates_removed`, `partitions_in_window`, `partitions_read`; figures serve as JSON numbers at 6 decimals (weights) and 2 (money) and `as_of` is the partition date; the browser deny guard exempts the master_admin owner roster (`MASTER_ADMIN_EMAILS`) on the four internal routes and nothing else (a denied non-admin, Alyssa, stays refused); the discover answers echo bucket, vendor and firm; (3) the `order` of acts (one deploy, then the served read); (4) `both branches` (owner on the browser routes: the guard does not read the store; a denied non-admin: refused 403, an unreadable store: 503); (5) the `rollback` (redeploy the base `bf9d23b518`); (6) the `triggers`; (7) the gate lines (WARN/RAISE) the release commit printed. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

4. PRECONDITIONS: re-read the live ref and the `.env` (65 keys, `MUSE_CLIENT_ID` absent); else STOP. Ledger `nfra-oplgtw-gateway-release-batch3`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-batch3` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>` under the stale-base guard (the declared base equals the live ref read at upload; no other release in flight). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read**, through the INSTALLED code on the host and the public endpoint, writing `W/CODE3_SERVED.json` = `{"body": {"read_at", "live_commit", "health_status": 200, "env_key_count": 65, "reader_env_keys_present": 7, "registry_count": 103, "per_tool_good": 27, "host_md5": {"equal": N, "differ": 0}, "tools_list_before": N, "tools_list_after": N, "muse_env_present": false, "arms": {"e1_window_spans_partitions": bool, "e2_allocation_unit_and_currency": bool, "e3_numbers_and_as_of": bool, "e4_owner_browser_guard": bool, "e6_discover_echo": bool}, "arm_counts": {...}}}`. Counts and booleans only; every arm is one real call by an Opal stand-in principal (never a seat's identity). `e1`: a master_admin stand-in asks `client_get_transactions` (and `client_get_fees`) for a window of 13 months; the answer reports `partitions_read` of 2 or more, `partitions_in_window`, and `window_partial` false if `partitions_in_window` is 60 or fewer, else true with `partitions_read` 60. `e2`: the allocation answer's rows carry `weight_unit` null with `weight_unit_basis` `not_established`; the transactions and fees answers (and rows) carry `currency` null with `currency_basis` `source_absent`. `e3`: the serialized text of the holdings, allocation, transactions and fees answers has no figure as a string, no exponent in any number token, at most 6 decimals on weights and 2 on money, and `as_of` equals `partition_date` when the caller gave none. `e4`: on the host, in the gateway venv, `data_entitlement.email_denial(<the owner email>, route_class="internal_page")` returns `None` with a stand-in store that holds a deny record for it, `email_denial("alyssa@opalinvest.com", route_class="internal_page")` against the LIVE table returns 403, and with `route_class=None` the owner's stand-in deny still returns 403 (no existing caller changed); no table is written. `e6`: re-run the discover after-arm of `2.0.0_SA_COO~MI` (`org/missions/D9/NFRA/NFRA_MCPINDEX/` and `deliverables/2.0.0_SA_COO~MI/round19/post_release/` hold its method): the bucket is echoed in 8 of 8 answers and vendor and firm in 2 of 2. No object content, account number or person's name is printed; the account stays `****<last4>`.
6. **Standing clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once per phase. After the close, `2.0.0_SA_COO~O` tells `2.0.0_SA_COO~MI` and `~MP` the live commit.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no catalog edit, no env key, no deploy-script or manifest change, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; print an `.env` value, a credential, an account number, a person's name or email beyond the roster addresses named above, or object content; set `MUSE_CLIENT_ID`; override a gate other than the audited lane escape named in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch3.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`. The manifest is NOT in your paths: it changes only at the close, when the deploy wrapper writes `deployed_commit` and the checksums.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-31"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap31.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the batch set 0 \(want 0\); terraform files differing 0 \(want 0\); tools.py or destructive_ops.py touched 0 \(want 0\).*deploy script or manifest changed 0 \(want 0\); data copies committed 0 \(want 0\); registry files in the diff \d+, not byte-equal to trunk's 0 \(want 0\); ask has the three halves yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-31"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap31.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*tools/list before (\d+) after \1 \(want equal\); MUSE_CLIENT_ID present False.*reader env keys 7 of 7; registry 103 \(want 103\); per-tool 27 of 27; host md5 differ 0 \(want 0\); arms true 5 of 5.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-31" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the named orders' files, no Terraform, no tool added, no deploy-script or manifest change, and any registry file in the diff is byte-equal to trunk's. `AC2`: the release landed and closed; the installed code shows every round-39 arm through real calls; the tool list and the env are unchanged.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the 49F transactions and fees windows and figures read as an analyst would want (the window answered, units and currency stated or honestly absent, numbers readable). Graded on bodies the issuer relays; never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-31.round-39-batched-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39, workstream ENRICH-R39-C (decomposition addendum R3-T.101). The release rides after `OG-ap-30` (landed) and `OG-en-16` (merged `19db3a905b`). Queue on the gateway host: THIS only.
- Staged: the GO for Phase A is the issuer's message citing this order and naming `trunk_sha`, sent when this order is committed (all four builds and the repair are merged). The three halves are signed on the ask your Phase A drafts, not on this order.
- Finish-by: none stated for round 39; the CTO's round analysis lists E2 to E4 and E6 as "next release".
- Pre-cut: `ap31.AC1` and `ap31.AC2` base FAIL as expected (`ap31_release.json`, the ask and `CODE3_SERVED.json` absent). `ap31.AC1` PASS arm exercised on a git-plumbing release commit built from the live ref (12 files: PASS) with three control arms failing for the right reason (tools.py touched, the deploy script changed, a registry file not byte-equal); `ap31.AC2` served-record arm exercised: a good record OK, an arm false NO, a `tools/list` drift NO.
- `OG-en-15` replaced a `transaction_id` dedupe that was dropping real rows (rows Z-S314, A2): the release changes the count of transactions an analyst sees for the same account. The ask states it.

- A1 (issuer, 2026-10-16 ~22:4xZ, after Phase B): the evidence AC3 is graded on, and the CVO's re-grade of `OG-ap-28` AC3 (relay msg 35275), needs SIX unscrubbed answer bodies from THIS release, captured as `OG-ap-28` A5 had them: one per 49F live tool (`client_get_holdings`, `_transactions`, `_allocation`, `_fees`, master_admin stand-in) with the transactions and fees asked for a 13-month window, one EMPTY-news answer showing `coverage_floor`, one chatter answer showing `trading_days_behind_t1`. Same applier (this order is in flight, rule 34). Account numbers stay masked `****<last4>`; no phone, e-mail or person's name. CLIENT DATA: ONE file under `W`, `CVO_AC3_BODIES_OG-ap-31.json`, git-excluded and NEVER committed, imaged or mailed; the proof records only its byte count, sha256 and per-capture row counts and partition counts. Read-only; no gate limb graded (a note on a completed order).

<status>complete</status>
<round>39</round>
<workstream>ENRICH-R39-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
