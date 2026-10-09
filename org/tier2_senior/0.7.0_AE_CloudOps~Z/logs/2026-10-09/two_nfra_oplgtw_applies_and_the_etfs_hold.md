# Two NFRA_OPLGTW applies landed (Tax SMA master, 49F dispatcher date gate); ETFS R28-aw1 held for its window

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~Z` | **Window:** 2026-10-09 ~01:4xZ -> ~05:0xZ (continues
`logs/2026-10-08/etfs_rivals_r28aw1_stop3_plan_read.md`) | **Device:** site Z

## Work completed

Three orders held this window. Two are deploys that landed; one is waiting on its own clock.

### 1. `NFRA_OPLGTW.TO-OG-ap-1` -- the Tax SMA master 08403355: COMPLETE, 3 of 3

Six ledger legs under `nfra-oplgtw-og-tm-1-taxsma-master`, all CLOSED with world read-backs, ledger
CLOSED, `<status>` flipped to `complete`. 13 `-target` resources across three Terraform roots, every
apply from a SAVED plan so the applied set equals the audited set, and every plan graded from
`show -json` rather than the rendered text, which hides unchanged attributes behind a redaction line.

- **L1** converter artifact rebuilt from box/sitez HEAD at sha256
  `AzrzJS+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE=`, the value row 13 requires. Uploaded with
  `--metadata content-sha256` because `modules/yang-lambda/main.tf:39` reads `source_code_hash` from
  that user-metadata key -- a bare `s3 cp` would have broken the apply. Verified on size AND metadata,
  never on `rc=0`.
- **L2** opal-assets targets 4-9: `3 added, 3 changed, 3 destroyed`. Notification 12 rules, the prior
  11 ids all present plus `silver-schwab-08403355`. The 6-8 replacement window measured ~1s at
  02:32Z with no bronze landing.
- **L3** SI2 box grant: exactly 3 `PutObject` prefixes added, 0 removed, the two existing masters' 6
  ARNs untouched.
- **L4** puller object ETag `e49aea76a8c634c9d49e6a7cccc51bdf`, 35853 bytes, SSE AES256; the diff
  from pin `4d0222ab81` is exactly the one authorized `ValidateSet` line.
- **L6** gateway roles: +4 `dim_*` and +1 `meta/complete/` Allow, 0 removed, 4 Deny statements intact
  on each role.
- **L5 (Leg A)** blocked, then landed. See Blockers 1.

### 2. `NFRA_OPLGTW.TO-OG-ap-2` -- the 49F dispatcher date gate: ledger CLOSED, AC1 PASS, AC2 refused

Two legs under `nfra-oplgtw-og-bf-1-y-dispatcher-gate`, both CLOSED, ledger CLOSED. Order of acts
exactly as both halves require: the `trading_calendar.py` source-map registration ALONE first
(`cdf66df55c`), then the build, then the ledger entry and sentinel committed (`26f9669e2a`), then the
upload, then the targeted apply, then read-backs, then Arm 1, then close, then the criteria.

- Plan was code-only on one resource: `source_code_hash`, `s3_object_version`, `last_modified` only;
  timeout 900, memory 256, role and all 5 environment keys identical before and after. Post-apply
  re-plan read `No changes`.
- **Arm 1** invoked ONCE at 04:15:47.767Z, RequestId `8f47201f-0cb4-4bed-892e-891404ddee22`:
  `dispatched: false` with `skip_reason` "accelerator marker date=2026-09-15 is not the production
  T-1 2026-10-08; historical record, not dispatched". The synthetic event was built from the
  handler's own parsing code (`lambda_function.py:184-195` requires a `versionId` and
  `unquote_plus`'s the key) rather than guessed. Controls: SSM `list-commands` for
  `advi-49f-chain-dispatch` read 181 before and 181 after with ZERO new CommandIds, host
  `i-01003b035d2988dfb` running before and after. **Arm 2 was NOT invoked** -- organic only.
- `W/ap2_arm1.json` written with request_id, invoked_epoch_ms and the response.

### 3. `ETFS_RIVALS.TO-APPLY-R28-aw1` -- unchanged, correctly held

Steps 1-3 stay done from last window; steps 4-6 wait on `2.0.0_SA_COO~RV`'s second GO inside
2026-10-09 11:15Z-12:55Z. `C:/tmp/rv-r8` is still detached at `39889dd4d7` with its five staged trees
and `C:/tmp/rv_apply28.tfplan` untouched, because `archive_file` zips at plan time and re-planning
would break the pairing step 5 depends on.

## Deployment sequence + verification (AE role-specific) -- ACTUAL output

```
L2  safe-apply opal-assets           04:32Z  Apply complete! Resources: 3 added, 3 changed, 3 destroyed
L3  safe-apply canonical-schwab-ec2  02:43Z  Apply complete! Resources: 0 added, 1 changed, 0 destroyed
L6  safe-apply opal-gateway          03:00Z  Apply complete! Resources: 0 added, 2 changed, 0 destroyed
L5  safe-apply canonical-schwab-ec2  04:29Z  Apply complete! Resources: 2 added, 0 changed, 0 destroyed
                                             [naming-plan-gate] CONFORMANT as EVENT_RULE (ADDITION)
ap2 safe-apply opal-assets           04:05Z  Apply complete! Resources: 0 added, 1 changed, 0 destroyed
                                             post-apply re-plan: No changes.
```

Criteria, all run after the ledger closes, as both orders require:

```
OG-ap-1 AC1  RESULT: PASS   (was FAIL while Leg A was blocked)
OG-ap-1 AC2  RESULT: PASS
OG-ap-1 AC3  RESULT: PASS   13 of 13 simulations as wanted
OG-ap-2 AC1  RESULT: PASS
OG-ap-2 AC2  RESULT: FAIL   refused as written -- see Blockers 2
```

## Compiler tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `--enumerate` over silver.tf, yang-lambda/main.tf, build-and-upload.sh, conversion_manifest.py, silver_registry.py, lambda_function.py, ap2_check.py, proof-of-spec-check.py, two backend main.tf | PASS | Three reads changed what I did: yang-lambda showed `source_code_hash` comes from S3 user metadata; build-and-upload.sh:510 showed the manifest limb needs an EXISTING file; ap2_check.py:64-72 is the whole of row Z-S71. |
| `comp-find` | `--name '*proof_of_spec*.schema.json'`, `--name '*proof_of_spec.json'` | PASS | Denominators printed; 1 hit across 203,334 files for the schema. |
| `deploy_ledger.py` | `open` x2, `close-leg` x8, `close` x2, `hold` (refused), `list` | PASS | See Blockers 1 for the hold refusal, which was correct. |
| `safe-apply.sh` | 5 applies across 3 roots | PASS | 5 of 5 rc=0 from saved plans. The 6th (pre-A1 Leg A) was rc=7, blocked. No HALTGT pass is cited as evidence, per cloud-ops. |
| `terraform` | init on 3 roots, plan -out + show -json + apply + re-plan | PASS | `-reconfigure` only for canonical-schwab-ec2, after confirming no local state and the canonical backend key; plain init elsewhere. Re-init again after worker ~39's drain added a module. |
| `proof-of-spec-check.py` | both instances | PASS | Caught 10 real schema violations on the first OG-ap-1 draft (phase enum, deployed_state enum, kind enum, composite `commit_or_etag`, missing `determinism`/`observed`, a disallowed `negative_control`, and the row-id form). Both instances now VALID rc=0. |
| `commit-gate.sh` | the one .py artifact last window | PASS | n/a this window; no .py edits. |
| `comp-iam` | NOT USED for the policy read-backs | SKIP | Deliberate: cloud-ops states it models `(action)` and never `(action, resource)` and is a FLOOR, so it cannot confirm a specific prefix landed, and it does not cover a non-Lambda EC2 box role. Read-backs used live documents under an audited `# rail-checked:` marker. AC3's own instrument, `simulate-principal-policy`, does model `(action, resource)`. |

Gap found: `safe-apply.sh` has no plan mode (it refuses any call without the word `apply`), already
row Z-W39-S6, so every plan ran `terraform` directly. And `deploy_ledger.py` has no window-extend
verb -- `window_hours` is written only at `open` -- which is why Blockers 1 ends in a hand edit.

## Blockers

1. **Leg A: BLOCKED, then RULED, then LANDED (closed within the window).** The LGIC naming plan gate
   refused Leg A pre-apply (`safe-apply` rc=7, DEC-6 ENFORCE): the rule name
   `canonical-schwab-si2-08403355-daily-pull`, which the halves and Andrew's "exactly same structure"
   require because it matches both siblings, is not `name()` output. Additions are enforced; the same
   root's 8 existing out-of-pattern names only WARN, and the gateway apply later WARNed rather than
   refused on two existing resources, which independently confirmed that reading. BOUNDS forbid
   overriding a gate and rule 30 routes a builder refusal to `infra/logic/registry/`, outside my
   paths, so I filed row `NFRA_OPLGTW-Z-S68` with three options and kept working on L6.
   Amendment A1 `@35d90ec7c0` ruled option (c); worker ~39 drained the builder-named TF `@897cbc6156`;
   the issuer's GO (msg 32372) named it; Leg A applied CONFORMANT at 04:29:02Z.
   While waiting I tried `deploy_ledger.py hold`, which REFUSED correctly -- an open APPLY leg cannot
   be HELD, because a half-landed deploy must stay RED. With no extend verb available I edited the
   sentinel's `window_hours` 6.0 -> 18.0 in place on A1's explicit instruction and logged the reason,
   which kept a sanctioned wait from firing a RED alarm at 08:05Z.

2. **OG-ap-2 AC2: REFUSED AS WRITTEN, row `NFRA_OPLGTW-Z-S71`.** The criterion filters
   `filter-log-events` by the RequestId. In Lambda only `START`, `END` and `REPORT` carry the
   RequestId; the function's own `print()` lines never do. So the `SKIP:` line the criterion requires
   is excluded by the criterion's own filter -- its query returns exactly those 3 runtime lines.
   Positive control, same log group and `--start-time` with the filter removed: 7 events including
   the SKIP line, with `dispatched: doc=` absent; and the invocation's own `--log-type Tail`
   LogResult, independent of CloudWatch Logs, carried the same line. The world meets AC2's intent;
   the retrieval cannot see it. Refused rather than marked PASS on evidence the check did not
   produce. `r32/checks/` is the issuer's, so the row names two one-line repairs and OG-ap-2's
   `<status>` stays `pending`.

3. **Records commit: BLOCKED on another lane, surfaced twice.** `missions-tree-check` refuses every
   commit staging `org/missions/` while an unrelated `org/projects/*.json` carries an INDEX-DRIFT.
   It fired on `NFRA_MCPORTAL.json` (cleared by MSTR~Z `@57b8eb4587` after I surfaced it) and again on
   `IRPT_ANLREQ.json` (`dep_stage` index='PRD' tree='EXECUTING'), still open. Remedy is R5,
   `0.0.0_AB_MSTR`'s lane, "never bypass"; I have not. Both ledger entries landed separately at
   `2dfe163f12`, so neither deploy is unrecorded; what waits is the two proof instances,
   `ap2_arm1.json`, rows Z-S70/S71 and OG-ap-1's `<status>` flip.

## Files modified

See commit messages: `cdf66df55c`, `049fe1c5e2`, `fcc486562c`, `26f9669e2a`, `19394419c5`,
`2dfe163f12`. Written and waiting on Blockers 3: both proof instances, `ap2_arm1.json`, the channel
rows and the OG-ap-1 `<status>` flip.

Note on the OG-ap-1 status flip: section 5 instructs the assignee to flip the ONE `<status>` tag when
all criteria PASS, and the TO protocol makes `complete` the assignee's own mark, but the order's
`<paths>` list does not itself name the task-order file. The flip rests on section 5; nothing else in
that file was touched. Recorded in the instance's `declared_exclusions`.

## MCP traffic

8 messages handled, all acked on read. IN: 32241 and 32279 (the two task orders), 32343 (OG-ap-1
amendment A1 ruling row Z-S68), 32372 (Leg A GO naming `@897cbc6156`), 32373 (commit the source-map
entry). OUT: the OG-ap-1 interim report and the combined final report to `2.0.0_SA_COO~O`; two
surfaces to `0.0.0_AB_MSTR~Z` (the two index drifts, plus the source-map-clean notice that released
site Z's box-sync); one FYI to `0.6.2_AE_PartnerETL` naming the puller bytes it now runs.

One send was REFUSED by the broker at 208 words against Rule 31's 150-word cap. That is the rule
working; I cut it to the single ask plus file citations and it went.

## Current state

- **Live, new:** EventBridge rule `schwab-canonical-si2-08403355-pull-daily` at
  `cron(45 10,22 * * ? *)` ENABLED, 1 SSM target on `i-0f3d57a97f14727af` running
  `-Master 08403355 -Target monolith`; first fire the next 10:45Z. Siblings untouched at
  `cron(15 10,22)` and `cron(45 9,21)`.
- **Live, changed:** converter `opal-assets-silver-schwab` CodeSha256
  `AzrzJS+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE=`, `OPAL_BUILD_COMMIT 47c3c75f11`, memory 3008;
  `advi-49f-gold-dispatch` CodeSha256 `EmlN9/zeB3rk90/QeJd7deRh01yiW3yKXEcLUQpFD0o=`, State Active,
  timeout 900, memory 256, 5 env keys; bucket `opal-data-assets` notification at 12 rules; the SI2 box
  role and the two gateway reader roles carry the new master's prefixes with their Deny controls
  intact.
- **Rollbacks, named and still available:** converter artifact version
  `7Db1UfM3EU_Z6q4cLQiV4wM3bYaAaFMF`; puller object version `auEPLgrK_QCZjOKseErSb7k3VAtXXEjR`;
  dispatcher artifact version `AQ2rQSyBdPpB0sWozwovunpWoL9TWVYA` (CodeSha256 `TjIWGFWk...`). All three
  buckets are versioned.
- **Both ledgers CLOSED**, sentinels removed, removals committed at `2dfe163f12`. No open deploy for
  this seat.
- **ETFS R28-aw1:** steps 4-6 pending the second GO inside 11:15Z-12:55Z; apply nothing if it lands
  after 12:50Z. The rollback note still stands: step 1 moved `C:/tmp/rv-r8` off `325bd4e0f8`, so a
  rollback needs a re-checkout there first.
- Broker: live, zero crons, inbox empty at last check, watcher re-armed on each 30-minute expiry
  (eleven arms this session, one script row at every census, nothing reaped).
- Push state, MEASURED: `2dfe163f12` and the five earlier commits are LOCAL on `box/sitez`;
  `git ls-remote origin box/sitez` read `65e15ac909` before the last three commits, and box-sync is
  the integrator's scheduled carry (CLAUDE.md Git section). I pushed nothing.

## Next steps

1. [`0.7.0_AE_CloudOps~Z`] On MSTR~Z clearing the `IRPT_ANLREQ.json` drift, commit the two proof
   instances, `ap2_arm1.json`, rows Z-S70/S71 and the OG-ap-1 `<status>` flip -- all written, one
   commit.
2. [`0.7.0_AE_CloudOps~Z`] On `2.0.0_SA_COO~RV`'s second GO, run ETFS R28-aw1 steps 4-6 inside
   11:15Z-12:55Z: NEVER-2 entry, live BEFORE reads, safe-apply the SAVED plan, AFTER reads, 0-diff
   re-plan, close L1, second report.
3. [`2.0.0_SA_COO~O`] Owns AC2's retrieval repair (row Z-S71) and then OG-ap-2's `<status>`; owns the
   Z-S70 follow-ups; owns the QA pull for OG-tm-1 Phase B and its AC2.
4. [`0.0.0_AB_MSTR~Z`] Owns the `IRPT_ANLREQ.json` R5 reconciliation.
