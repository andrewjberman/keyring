# NFRA_OPLGTW task order -- `OG-bh-1` -- full history backfill for the Tax SMA master 08403355, same shape as 08242234 / 08335338 (Andrew-direct 2026-10-09 ~06:3xZ, FWD-13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bh-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-bh-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~46</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- three daily-pull rules on the SI2 box: 08335338 09:45/21:45Z, 08242234 10:15/22:15Z, 08403355 10:45/22:45Z (schwab-canonical-si2-08403355-pull-daily, live since 2026-10-09 04:29Z, OG-ap-1); every run of this cell starts outside [09:15,11:35) and [21:15,23:35) UTC. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE for Phase A (one SSM RunPowerShellScript command to i-0f3d57a97f14727af under the operator's IAM user, invocation reads, S3 reads). Phase B's identities (the box's write grant on schwab/08403355/, the silver converter's role) are read live and named in the never-widen ask before any write.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is Andrew-direct 2026-10-09 ~06:3xZ, verbatim in org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261009_063xZ_08403355_BACKFILL_SAME_SHAPE.md @98c4e6a47f.
EGRESS CLASS, declared: VENDOR (Schwab SDD) FROM THE SI2 BOX ONLY. Phase A: one list request (enumerate). Phase B: the downloads the signed ask names. No egress from the workstation.
</preflight>

## 1. THE CELL -- `OG-bh-1` (decomposition addendum R3-T.32)

Andrew, verbatim: *"That means doing full backfill, it probably doesnt go even 1 year, i expect maybe april 2026. then
including it on whatever system is pulling the 0824 and 0833 masters, running it through bronze/silver same format same
everything exactly how its done already"*. The schedule, grants, silver conversion and reader roles for `08403355`
already exist (OG-tm-1, applied by OG-ap-1); the first scheduled pull is 10:45Z 2026-10-09. What does not exist is the
HISTORY: every date the source serves before that, through bronze, then silver, then the completion record, exactly as
the other two masters carry it.

Read first: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` (the puller; `-Master` already admits `08403355`;
`-Mode enumerate|download`, `-LookbackDays`, `-MaxFiles`), `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf`
lines 58-150 (how SSM runs it: register a Scheduled Task as `/RU Administrator /IT /RL HIGHEST`, prove it started, wait,
print the log, unregister; a task that never starts = the Administrator console is logged off = STOP + BLOCKING row),
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/g5_enumerate.result.md` (the 30-day list-only run
for this master: 226 files, 13 types, FILES) and `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`.

### PHASE A -- census and plan; NO write

1. **The census run.** One SSM command, the OG-en-1 pattern: copy the S3 code object
   (`s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1`) to `C:\schwab-sdd\og-bh1\sdd-census-bh1.ps1`
   and make ONE `-replace` edit, asserted to match once, inside the `if ($Mode -eq 'enumerate')` block: log one line
   `DATE <YYYY-MM-DD> <n>` per business date in the plan (n = files for that date), so the output stays under SSM's
   24,000-character cap. Run `-Master 08403355 -Mode enumerate -Target monolith` with NO `-SnsTopicArn` and a
   `-LookbackDays` wide enough to reach the source's start (start at 400; if the vendor refuses the window, halve until it
   answers and record each refusal). If the earliest DATE line sits at the window's edge, widen once and re-run: the
   census must show the source's start, not the window's. Unregister the task; delete `C:\schwab-sdd\og-bh1\`.
2. **The census record**, `W/bh1_census_record.json`:
   `{"instance_id": "i-0f3d57a97f14727af", "command_id": "...", "started_utc": "...", "lookback_days": <int>,
     "refusals": [{"lookback_days": <int>, "line": "..."}], "enumerated": <int>, "earliest_served": "YYYY-MM-DD",
     "served_dates": ["YYYY-MM-DD", ...], "by_type": {"<type>": <int>}, "task_unregistered": true, "copy_deleted": true}`
   `served_dates` is every DATE line of the run, through the run's last date.
3. **The plan.** Read how 08335338's dates go from bronze to silver to completion record today (the puller's S3 write,
   what starts `opal-assets-silver-schwab`, what writes `meta/complete/`), and how that master's history was first
   loaded. The backfill uses that SAME path; no new code, no new Lambda, no new layout. If the path needs any deploy or
   Terraform apply, name it as a separate leg (site Z's applier is `0.7.0_AE_CloudOps~Z`, never you).
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-bh-1.md`, in the form of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/NEVER_WIDEN_ASK_OG-bf-1.md`: the exact write set
   (bronze keys, silver partitions, completion records and manifests, counts, all under `schwab/08403355/` only); every
   writer of each prefix (N writers = N rules read, N printed); every `ObjectCreated` consumer of those prefixes and what
   ONE historical date causes in each, both branches (state whether any 49F accelerator or gold dispatch is wired to
   `schwab/08403355/`; OG-tm-1 wired none); the run order, batch size and quiet windows; the rollback per key (versioned
   objects: the previous version or absence); how the backfill and the 10:45Z/22:45Z scheduled pulls avoid the box-wide
   SDD session lock and each other. Halves owed: `1.0.0_SA_CTO~O` and `2.0.0_SA_COO~O`.
5. Commit Phase A, run AC1, and REPORT. Then STOP: the issuer continues you with the signed halves' commits.

### PHASE B -- only after both halves are signed at HEAD (the issuer's continuation names their commits)

6. Open the NEVER-2 ledger (`python .tools/deploy_ledger.py open --slug nfra-oplgtw-og-bh-1-taxsma-history ...`) and
   commit the entry and its sentinel before the first write.
7. Write `W/bh1_backfill_record.json` with `started_utc` before the first write; run the signed write set exactly, in the
   signed order. Record `backfilled` (dates whose completion record now qualifies) and `unavailable`
   (`{date: reason}`) -- a date the source served that cannot be completed stays unavailable, never guessed.
8. Read every written date back; close the ledger and commit BEFORE the criteria. Never leave it half-landed: finish, or
   roll back per the ask and file an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~46/`.

## 2. BOUNDS

- Phase A: `-Mode enumerate` only; nothing lands in S3; the S3 code object, the installed puller, the repo puller, every
  Terraform file and every EventBridge rule are untouched.
- Only `schwab/08403355/`. Nothing under `schwab/08242234/` or `schwab/08335338/` is written. No other firm.
- No `-SnsTopicArn`. No change to the box's scheduled tasks other than registering and unregistering your own.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; RDP or touch the SI2 GUI; deploy.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-bh-1-taxsma-history.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~46/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

AWS: `.tools/aws` (the repo's shim) for `ssm send-command`, `ssm get-command-invocation`, `s3api` reads (Phase B: the
signed writes only).

Rows: id `NFRA_OPLGTW-Z-W46-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bh-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bh1.sh AC1; echo "exit=$?"</invocation><expect>(?s)08403355: invocation .* status Success .*DATE lines [1-9]\d*; .*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-bh-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bh1.sh AC2; echo "exit=$?"</invocation><expect>(?s)08403355: served dates [1-9]\d* .*backfilled [1-9]\d*; .*open 0; backfilled-but-not-qualified 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-bh-1" judgment="true"/>
</proof_of_spec>

- `AC1`: the census is re-read from the SSM invocation itself, outside the pull windows; earliest date = the source's.
- `AC2`: every date the source serves is QUALIFIED for 08403355 under the gateway's own rules, or named unavailable.
- `AC3` (judgment, graded by `3.0.0_SA_CVO~Z` at L9): "EXACT SAME" -- 08403355's bronze key grammar, silver datasets
  and columns, and completion-record shape equal 08335338's for the same date. Record it under
  `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO; never PASS or FAIL it yourself.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bh-1.taxsma-history-backfill.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If AC1 and AC2 PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the SSM command ids; earliest_served and the served-date count; per-date backfilled
   and unavailable counts; the ledger's close; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Andrew-direct 2026-10-09 ~06:3xZ at the 2.0.0_SA_COO~O terminal (record @612b71ba28, follow-up @98c4e6a47f): full
  backfill, no 13-month cap, same path as the other two masters. Cut after the site Z reboot as the record says.
- The 49F accelerator question is open with Andrew and is NOT in this order: "EXACT SAME" as 08242234 means none.
- The 10:45Z scheduled day is the parallel QA arm (OG-tm-1 AC2); this order does not wait for it.
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>33</round>
<slot>~46</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
