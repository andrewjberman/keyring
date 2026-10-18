# TO SOC2_MSLOGS.TO-R2-r2 -- the round-2 release: apply, re-derive the 8 days, prove the streaming derive on the busiest day, bring the memory down

<to_id>SOC2_MSLOGS.TO-R2-r2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.7.0_AE_CloudOps~SOC21</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-r-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-2, FWD-7 | **depends_on:** `SM-s-2`, `SM-d-2`, `SM-n-2`, `SM-k-2`, `SM-c-2`, `SM-t-2`, `SM-e-2` complete and MERGED, and the issuer's `exposure` hookup landed. **FLIPPED to `pending` by the issuer 2026-10-17 ~09:0xZ after the seven merges (TO-R2-c2 bae1c4c71c, TO-R2-t2 765639cc1e, TO-R2-e2 96d701d119 and its hookup amendment f26a3da767, TO-R2-k2 e36ce35f08, chain A s2/d2/n2 8ed6ce721a) and the drain checks (the twelve modes of `s1_check_r2.py` OK, 361 tests, ruff, `thread_trace_r1.py` THREAD-R1-OK).**

---

## WORKER FACE

### THE CELL

`SM-r-2`: the live change of round 2. The system already runs from round 1 (bucket `opal-data-trino`, door `globgrph-trino-access-lambda` with aliases `collector` and `member`, the hourly collector `m365-metadata-trino-collector-lambda`, the group `globgrph-trino-access-group` holding `Andrew_Berman` alone, an MFA Deny on each alias).
The merged tree changes: the door's CODE (a streaming derive, the builder-derived prefixes, `client_ip` from `ClientIPAddress`, the new `exposure` op), one new Terraform resource (the collector's async retry set to 0), and text. You apply that, prove it from live reads, and bring the door's memory down once the streaming derive is proven.
Read first: `decompositions/SOC2_MSLOGS_DECOMP_R2.md` (rulings 4, 6, 7), the round-1 release order `task-orders/SOC2_MSLOGS.TO-SM-r1.release-switch.md` (its items 2-5, 7e and 7f are your pattern, including the ledger and the `s1_check_r1.py` reads), `infra/aws/terraform/trino/access.tf` and `collector.tf`.

You run as the box identity, deliberately NOT a member of the group: you read no stored object and invoke no door op. Your reads are describes, lists and log filters. The acts that need a member's MFA session (the re-derive, the exposure read) are Andrew's; you prepare the exact commands and read their effects in the logs.

### ITEMS, in this order. Stop at the first that fails and write what stands.

1. **Preconditions.** From the repository root these print their OK tokens (all in `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/`): `s1_check_r2.py silverip`, `derive`, `naming`, `paging`, `desktop`, `retire`, `exposure_door`, `exposure_client`, `hookup`, `retry`, `tfvalidate`, `text`; and `python -m pytest infra/aws/lambda/globgrph-trino-access/tests data/m365_metadata/scripts/tests -q` passes.
   Otherwise STOP and report.
2. **Open the ledger** before any write: `python .tools/deploy_ledger.py open --slug soc2-mslogs-r2-streaming-derive-20261017 --title "SOC2_MSLOGS round 2: door code, collector retry 0, memory down after the streaming proof" --author 0.7.0_AE_CloudOps~SOC21 --leg ...`
   (legs: apply-code, rederive-proof, memory-down, memory-proof). Blast radius: the code of the door and of the collector, ONE new resource (`aws_lambda_function_event_invoke_config.collector`), the door's configuration (memory only, in the last legs). Rollback: re-apply the previous commit's zips and `terraform` state for that one resource (`git revert` of the round-2 merge range and the same apply). Stored objects are write-once and stay.
3. **Build the two zips:** `bash infra/aws/lambda/globgrph-trino-access/build.sh` and `bash infra/aws/lambda/m365-metadata-collector/build.sh`. Read the door zip's file list: it must hold `handler.py`, `silver_builder.py`, `names.py` and `exposure.py`.
4. **Plan, read it, apply once.** `terraform -chdir=infra/aws/terraform/trino plan -out=<file under your scratch>`. It must contain ONLY: the code hash of the two functions, the door's aliases moving to the new published version, and ONE create (`aws_lambda_function_event_invoke_config.collector`). NO destroy, NO replace, NO create of anything else. Otherwise STOP, write the plan summary in your report and a surprise row.
   Then ONE apply: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/trino apply <that plan file>` (never bare `terraform apply`, never `aws lambda update-function-code`). Write the UTC apply time (`date -u +%FT%TZ`) to `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/apply_r2_at.txt` and commit it. Then `s1_check_r1.py applied` (both Denies stand; the functions run the built zips).
5. **Read the retry setting back live:** `aws lambda get-function-event-invoke-config --function-name m365-metadata-trino-collector-lambda --query MaximumRetryAttempts --output text` prints `0`.
6. **Hand Andrew the re-derive** (the issuer cards him; you give the issuer the exact text in ONE broker message): from the repository root, with his MFA session (`--profile <his profile> --mfa-code <six digits>`), `python data/m365_metadata/scripts/silver/read_timeline.py --derive <the 8 most recent Eastern dates, newest first>`. It re-derives the 8 days through the member alias, so silver carries `client_ip` for Exchange rows and each day exercises the streaming derive at the door's current memory (10240 MB).
7. **Read the streaming proof from the door log** (describe/filter only): for each of the 8 derive invocations after `apply_r2_at.txt`, the `REPORT` line's `Max Memory Used` and `Duration`, and whether any ended `Runtime.OutOfMemory` or timed out. The BUSIEST day is the one with the greatest Max Memory Used. Write the 8 figures into your report (counts and megabytes only; no account, no record).
8. **Bring the memory down, one leg.** Let `M` be the busiest day's Max Memory Used. Set `memory_size` of `aws_lambda_function.access` in `access.tf` (that line alone; the issuer rules this inside its own decomposition, so `access.tf` is in your `<paths>` for this one edit) to the smallest of 2048, 3008, 4096, 6144 that is at least `2 x M`; if none of those qualifies, leave 10240 and STOP with a surprise row (the streaming derive is not bounded enough).
   `terraform fmt -check`, `terraform validate`, `s1_check_a1.py tf` is NOT used (its floor is round 1's 10240): instead `python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py tfvalidate`; the plan shows that one function's configuration (and the aliases if they move) ALONE; one `safe-apply`; `s1_check_r1.py applied`.
9. **Prove the lowered door.** The issuer cards Andrew for one more re-derive of the busiest date alone (same command as item 6 with that one date). Read that invocation's `REPORT`: it ended without `Runtime.OutOfMemory` and its Max Memory Used is below 80 percent of the new `memory_size`. Close the ledger with the read-backs.
10. **Exposure live (Andrew's read):** give the issuer, in the same message as item 9, the one-line command for Andrew to run the exposure read on his own account for one day: `python data/m365_metadata/scripts/silver/read_exposure.py --profile <his profile> --mfa-code <six digits> --account <his address> --start <ISO> --end <ISO> --desktop`. You do not run it.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~S1, 2026-10-18 ~08:1xZ) -- the apply ledger closes now; the memory leg gets its own ledger when Andrew has run item 6

Your message 7962 is right: the apply (item 4) landed and was read back (AC1, AC2 OK), the door runs the new code at 10240 MB, and nothing is half-landed. Items 6 to 10 wait on Andrew's MFA session, an act no seat can take for him (the open call dell1-20261017T131441Z-89c9 carries it).
A ledger entry held open for days over that wait is the wrong carrier. So:
1. **Close `soc2-mslogs-r2-streaming-derive-20261017` now** with the apply-code leg as the completed leg and legs rederive-proof, memory-down and memory-proof struck as DEFERRED, in the way `deploy_ledger.py` admits (if the tool has no such form, close it as complete at the apply and say so in the close note). Close note: the state is stable, nothing to roll back; the remaining legs reopen under a NEW entry.
2. **Items 7 to 9 stay in this order**, run as written, when Andrew reports he has run the derive: then open a NEW ledger (slug `soc2-mslogs-r2-memory-down-<date>`, legs memory-down, memory-proof) BEFORE the item 8 apply, and close it at item 9.
3. **Until then you take no action** beyond reading the door log when I message you. The order stays `pending`; AC1 and AC2 are met now, AC3 and AC4 are judgment rows the CVO grades after items 6 to 10.
The issuer rules this inside its own order (no ENDPOINT change, no served-data move).

### ACCEPTANCE

<criterion id="R2-r2-AC1" cell_refs="SM-r-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_r1.py applied</invocation><expect>R1-APPLIED-OK</expect></criterion>
`R2-r2-AC1` -- both functions run the built zips, the door may invoke the collector, and both MFA Denies stand (the round-1 live read, valid for round 2's rebuilt zips).

<criterion id="R2-r2-AC2" cell_refs="SM-r-2"><invocation>aws lambda get-function-event-invoke-config --function-name m365-metadata-trino-collector-lambda --query MaximumRetryAttempts --output text</invocation><expect>0</expect></criterion>
`R2-r2-AC2` -- the collector's asynchronous retry attempts read 0 on the live function.

<criterion id="R2-r2-AC3" cell_refs="SM-r-2" judgment="true"/>
`R2-r2-AC3` -- JUDGMENT (the CVO grades): the eight days derived through the streaming derive, the busiest day's Max Memory Used is stated, the door's memory came down to the stated value, and the busiest day derived again at that value without running out of memory (items 6 to 9).

<criterion id="R2-r2-AC4" cell_refs="SM-r-2" judgment="true"/>
`R2-r2-AC4` -- JUDGMENT (the CVO grades, on Andrew's read): the timeline shows the client address on Exchange rows, and the exposure read lists what one real window opened and what left, or says what the feed does not record (item 10).

<expected_criteria>R2-r2-AC1,R2-r2-AC2,R2-r2-AC3,R2-r2-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- You apply ONLY through `bash .tools/safe-apply.sh`, under the ledger entry you opened (NEVER-2); a half-landed apply is finished in-session or rolled back and escalated loudly.
- No door op is invoked by you and no stored object is read. No alarm, no SNS, no notification resource (C-NOALERT). Never print a secret, a session key, an account or a record.
- If the plan holds anything not listed in item 4, or the API refuses a setting, STOP and write what stands in your report and a surprise row (id `SOC2_MSLOGS-D1-SOC21-S<k>` in the investigation file below, `surfaced_at` = `date -u +%FT%TZ`).
- Commit only through `.tools/safe-commit.sh` with `--author "0.7.0_AE_CloudOps~SOC21 <0.7.0_AE_CloudOps~SOC21@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/terraform/trino/access.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/soc2-mslogs-r2-streaming-derive-20261017.json
org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-r-2`.
<owned_cells>SM-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-r2-AC1 to R2-r2-AC4 (AC3 and AC4 are judgment rows: `UNVERIFIABLE-BY-INSTRUMENT`, graded by `3.0.0_SA_CVO`). Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/SOC2_MSLOGS.TO-R2-r2.release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-r2-AC1,R2-r2-AC2,R2-r2-AC3,R2-r2-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to the issuer per milestone (apply time; the exact commands for items 6, 9 and 10; the 8 memory figures; the memory decision), and a final report with the check lines, the plan summaries, the ledger read-back and the commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at item 5 (the retry setting read back live); the hourly rule is untouched.
comp-iam: RUN at item 4 (`s1_check_r1.py applied` reads the door role policy and both alias Denies). No IAM change in this round.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release moves code the workers' checks graded; its live reads are the AC1 and AC2 invocations and the CVO's judgment rows.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis section 3 items 2 to 4 (@843819d1ab); Andrew-direct 2026-10-17 ~00:55Z ("use the biggest lambad memory possible should be 10gb or so") set the maximum until the streaming derive is proven; this release is the proof and the reduction.
