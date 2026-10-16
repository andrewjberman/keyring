# TO IRPT_BCKEND.TO-IB-pn-2 -- RE-APPLY the Scope account feed with the corrected script: Orion pair (b) ADDENDUM 3 (signed halves at blob d4b8c52eee; CTO half @39356eb170, COO half @144f32010c)

<to_id>IRPT_BCKEND.TO-IB-pn-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~N2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed ADDENDUM 3, `deliverables/2.0.0_SA_COO~N2/ORION_PAIR_B_ADDENDUM_3_SCOPE_FEED_RUNNER_LAYOUT.md` (blob `d4b8c52eeeccbd176e22d7acbc072033d5ccbefc`; READ IT ALL, its sections 1 to 6 are the specification), COO half `deliverables/2.0.0_SA_COO~N2/NEVER_WIDEN_ORION_PAIR_B_ADDENDUM_3_SCOPE_FEED_RUNNER_LAYOUT_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ORION_PAIR_B_ADDENDUM_3_SCOPE_FEED_RUNNER_LAYOUT_CTO_HALF.md` (its four conditions), and ADDENDUM 1 (blob `1e138cbeeaa12d4bf972cf579851546a7e3b3b37`) for every act, the key set, the blast radius, the rollback and the stop rule that ADDENDUM 3 does not change | **Decomp cell:** `IB-pn-2` (`IRPT_BCKEND_DECOMP_R9_N.md`) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pn-2` (inlined).** The first apply of the Scope account feed (your order IB-pr-596) uploaded a script that died at import on the runner: the first scheduled chain ran the step at 11:51:47Z on 2026-10-16 and it exited 1 in 0.1 s (`IndexError: 2`, `_HERE.parents[2]`; row `IRPT_BCKEND-D2-S221`, your msg 9366); you restored the saved dispatch copy (Branch B) and left the script, calendar and sidecar objects in place, inert. The repair is merged (`IRPT_BCKEND.TO-IB-pn-1`, merge `7b47813ad1`): `data/inf/manual_api/pull_inflection_scope_account_returns.py` at HEAD has git blob `233cf1e604751619ef2b1132c8c6bdb863f2bc13` and sha256 `4527c57f6eed54ac62d732468419a83adce08fec80916f333800db5d2d0a8d32`. **This order lands the corrected script on the chain, once, and reads the first scheduled run from its STEP LOG.** It writes ONLY: the script's code object (replaced), the dispatch object (by one row and its chain entries, from the saved copy), and, by the chain's own first run, the feed's two prefixes under `orion/inflection/`. **Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33).** No request content, account or household identifier goes in any record: counts and hashes only.

**Do, in this order. A STOP is reported to the issuer and writes nothing further.**

1. **Gates, measured now (READ ONLY).** (a) Both halves SIGNED at the addendum blob: `git hash-object` of ADDENDUM 3 equals `d4b8c52eeeccbd176e22d7acbc072033d5ccbefc`. (b) Order `IRPT_BCKEND.TO-IB-pn-1` reads `<status>complete</status>` and the repository script at HEAD hashes to the sha256 above. (c) **One change at a time:** if any ledger under `org/critical_paths/change_management/` naming `orion-gold-dispatch`, `inf-gold` or the chain's code objects reads OPEN (the ledger `irpt-scope-account-feed-ib596-20261015` is OPEN at L4 and belongs to your IB-pr-596 apply; the issuer `2.0.0_SA_COO~P2` closes it once the failed first run is graded, so while it reads OPEN this is a STOP: report that to `2.0.0_SA_COO~N2` and wait), or another seat's window is open on the chain, STOP and report which. (d) **The live dispatch object equals the repository copy before the feed's catalog row** (Branch B restored it; read the live object's sha256 and compare with `git show` of the repository dispatch script at the commit before the IB-pr-586 merge; record both). A difference is a STOP and a row. (e) **The runner role** still simulates allowed for `secretsmanager:GetSecretValue` on the Orion session secret, `s3:PutObject` on the feed's two prefixes in the address bucket, `s3:GetObject`/`ListBucket` on the roster and positions prefixes. (f) **The bound:** read the household count from the newest roster snapshot (distinct household ids holding at least one account in the positions silver); `request_bound` = that count; state it in the record BEFORE any write. (g) **The live notification filter** of the address bucket does not match the feed's bronze key `orion/inflection/bronze/scope_account_returns/date=<day>/scope.json.gz`.
2. **Name the rollback copies BEFORE any write.** Save the live feed-script code object and the live dispatch object to scratch outside the repository; record `replaced_script.sha256`, `replaced_script.saved_copy_sha256` (equal) and `dispatch_edit.saved_copy_sha256`; record the current version ids of both keys.
3. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, naming the script key, the dispatch key, both saved copies and this order; commit its `.open_deploys` sentinel at once.
4. **Branch A, the writes (S3 code objects only, each read back).** (a) Upload the corrected repository script to the same code key it replaces (the chain's `manual_api` code prefix); read it back and record `uploaded_sha256`; it MUST equal `4527c57f6eed54ac62d732468419a83adce08fec80916f333800db5d2d0a8d32`, otherwise STOP and restore the saved copy. (b) **The import smoke (ADDENDUM 3 section 4 step (d); the gate that was missing the first time).** On the runner, in a scratch directory laid out as the runner's flat directory (every script of the LIVE `code/gold/`, `code/manual_api/`, `code/silver/` and `code/bronze/` prefixes flattened by basename, as `sync_scripts()` does, plus the sidecar and the calendar object already beside the script), execute the uploaded script's top level with the runner's own Python and call `source_prefixes()`. **No Orion request, no secret read, nothing written to S3.** Any exception is a STOP: restore the saved script copy, report the exception's last line. Record `import_smoke` `{ran_on_runner, built_from_live_prefixes, exit_code, orion_requests}`. (c) **Only after the smoke passes, edit the dispatch object by exactly the feed's change:** the difference between the repository dispatch script at HEAD and the live object must be exactly the one catalog row `INF_API_PULL_SCOPE_ACCTS|pull_inflection_scope_account_returns.py|--upload` and its chain entries (the IDs added to `CHAIN_PULL`, `CHAIN_INCREMENTAL` and every other chain that carries `INF_API_PULL_PERF`, except single-stage group chains) as IB-pr-586 made them; upload that file as a new version; read back its sha256 against the repository file; record `rows_added`, `chain_entries_added`, `chains_carrying_perf` (equal) and `other_lines_changed` (0).
5. **Do not trigger the chain.** The first scheduled chain after the apply (about 11:32Z on 2026-10-17, or the next scheduled one) runs the step. Report to the issuer once at the apply and once at the first-run read.
6. **The first-run read (Branch A's proof; READ ONLY), taken from the STEP LOG, never from the chain's exit** (row W404-S9: a failed pull step reads as a green chain). The step's own log shows exit 0 and NOT `TOLERATING`; the log carries no `SKIPPED:` line and `DAYS: complete=<n> skipped=0`; the day's silver object: the DENOMINATOR is the accounts in roster membership intersected with the positions silver for the pull date (print it; zero is a STOP); every one carries a daily factor (`RETURNED`) or an `ABSENT` row with a reason class (`NO_GROUP`, `GROUP_NO_SERIES`, `NO_START_DATE_AT_SOURCE`, `SERIES_ENDED_AT_SOURCE`); `returned` plus `absent` equals the denominator; no zero return written; the stored column is `daily_factor`; the request count from the log is within `request_bound`; every request carried `calcGrossOfFees` false; no key outside `orion/inflection/`. A tolerated failure, a skipped day, a zero or a bound breach is a STOP, a row, and Branch B.
7. **On any trigger of Branch B:** restore the saved dispatch copy and the saved script copy as new current versions, remove nothing else (the feed's keys are production output: removing them is Andrew's act and never a condition of the rollback; list them by key count), read back that both sha256 equal their saved copies, set `rollback_performed` true and report at once.
8. **Do NOT close the ledger entry** until the first-run read is written; then close nothing yourself: the issuer closes it. **Write the record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IBN2-1_apply_record.json` with exactly these keys (counts, hashes and flags only): `{"gates":{"addendum_blob":"d4b8c52eeeccbd176e22d7acbc072033d5ccbefc","both_halves_signed":true,"dispatch_object":{"live_sha256":"<64 hex>","repository_sha256":"<64 hex>","equal":true},"other_open_ledger_on_chain":false,"runner_role":{"secret_read_allowed":true,"feed_prefix_write_allowed":true},"household_count":<n>,"request_bound":<n, equal>},"ledger_entry":"org/critical_paths/change_management/<file>","apply":{"replaced_script":{"sha256":"<64 hex>","saved_copy_sha256":"<64 hex, equal>"},"script":{"uploaded_sha256":"4527c57f6eed54ac62d732468419a83adce08fec80916f333800db5d2d0a8d32"},"import_smoke":{"ran_on_runner":true,"built_from_live_prefixes":true,"exit_code":0,"orion_requests":0},"dispatch_edit":{"saved_copy_sha256":"<64 hex>","rows_added":1,"chain_entries_added":<n>,"chains_carrying_perf":<n, equal>,"other_lines_changed":0},"rollback_performed":false},"first_run":{"read_from_step_log":true,"exit_code":0,"tolerated_failure":false,"skipped_days":0,"requests_made":<n>,"calc_gross_of_fees_false_on_every_request":true,"keys_outside_inflection_scope":0,"coverage":{"denominator":<n>,"returned":<n>,"absent":<n>},"zero_returns":0,"stored_value":"daily_factor"}}`. Write the `gates` and `apply` parts at the apply and the `first_run` part after the first scheduled run; the criteria run only when the whole record exists.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IBN2-1-AC1" cell_refs="IB-pn-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r2/pn2_cells.py" . IBN2-AC1</invocation><expect>IBN2-AC1 PASS</expect></criterion>
<criterion id="IBN2-1-AC2" cell_refs="IB-pn-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r2/pn2_cells.py" . IBN2-AC2</invocation><expect>IBN2-AC2 PASS</expect></criterion>
<criterion id="IBN2-1-AC3" cell_refs="IB-pn-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r2/pn2_cells.py" . IBN2-AC3</invocation><expect>IBN2-AC3 PASS</expect></criterion>

<expected_criteria>IBN2-1-AC1, IBN2-1-AC2, IBN2-1-AC3</expected_criteria>

What the checks grade: AC1 the gates (the addendum at its blob, both halves bound to it, IB-pn-1 complete, the live dispatch object equal to the repository copy, no other open ledger on the chain, the bound equal to the household count); AC2 the apply (the uploaded script's sha256, the replaced object saved, the import smoke over the live prefixes clean, the dispatch object changed by exactly one row and its entries, no rollback); AC3 the first scheduled run from the step log. Do not edit the checks. If the order STOPS, the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the chain's code bucket objects named in step 4 (the script object replaced, the dispatch object a new version from the saved copy), the ledger entry, your record folder; reads: S3 versions and heads, bucket notification configuration, IAM simulation, the roster and positions silver (schema and counts), the feed's day keys, CloudWatch logs and the chain's step log. **No Lambda invoke, no chain trigger, no IAM, schedule, Terraform, runner or catalog change beyond the one dispatch row and its entries; no key outside `orion/inflection/` written by the step; no existing key changed; no deletion.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: a half not signed at the blob; IB-pn-1 not complete; an open ledger or window on the chain; the live dispatch object differs from the repository copy; a missing grant; the feed's bronze key matching a live notification filter; the household count exceeding what you state; an uploaded script whose sha256 differs; ANY exception in the import smoke; a first-run tolerated failure, skipped day, zero, bound breach or key outside the Inflection scope. A STOP is reported, not worked around; a bound is raised only by a CTO half.
- **Feed keys are production output, not test objects:** Andrew's 2026-10-16 word on synthetic and test deletes does not cover them (CTO half condition 4).
- **Row ids:** put the row text in your report; the issuer appends it as `IRPT_BCKEND-D2-S<k>`. **Report under 150 words.**
- **Your queue:** after your open ledger entries on the chain's code objects are closed (single executor per artifact family, CVO ruling msg 8750); the split-pair apply and the exemption-pair apply are not on this chain's code objects and do not wait on this order.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pn-2.apply-addendum-3-scope-feed-corrected-script.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R9_N.md</decomp_doc> round 9, workstream ~PO, cell `IB-pn-2`.
<owned_cells>IB-pn-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBN2-1-AC1, IBN2-1-AC2, IBN2-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pn-2.apply-addendum-3-scope-feed-corrected-script.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one S3 code object (the feed script) is replaced by the corrected bytes and the chain's dispatch object gains one catalog row and its chain entries; the first scheduled chain writes the feed's two prefixes under orion/inflection/ (new keys). The blast radius, Branch A, Branch B and the stop rule are ADDENDUM 3 sections 4 and 5 and ADDENDUM 1 sections 3 to 5; nothing reads the feed's keys until the B-IN adapter is cut.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the runner role's grants are simulated at the start and a missing one is a STOP.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created; the chain runs at its measured time.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- pn2_cells.py dry-run at base on dell2 2026-10-16 ~14:2xZ: AC1, AC2, AC3 FAIL (no record). control_pn2.py in a temp root it built itself: a synthetic good record passes all three; twenty negatives (dispatch differs, another ledger open, bound not the household count, halves flag, wrong upload hash, smoke exit nonzero / not on live prefixes / an Orion request, replaced object not saved, two rows added, other dispatch lines changed, rollback performed, tolerated failure, read from the chain exit, skipped day, coverage not summing, a zero, requests over the bound, a key outside scope, a summary stored) each fail only their own arm; 0 unexpected.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD. Not measured by me: the live dispatch object's hash, the deployed script object's bytes, the runner role's grants, the live notification filter, the household count, the live code prefixes' contents (all read by the seat at its own start and each a STOP).
authority: workstream ~PO is this seat's under the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; write surface `infra/aws/terraform/inf-pipeline` and the feed's prefixes are named there; the signed halves are the sign-off.
</preflight>
