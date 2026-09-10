# Deploy Completion Record
**Date opened:** 2026-09-10T05:18:38.858554+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T052413Z
**Deploy:** EG-s-25 DEPLOY: aws s3 cp of render_month_end.py to the artifact prefix the box pulls by key at run time -- NOT Terraform, NOT a served report key. BLAST RADIUS, named as the act's and not the producer's decision: EXACTLY ONE key, s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py. Nothing else in the prefix is written, and platinum/reports/ is not touched by this cell at all. WHO IT REACHES: the next run of the renderer on instance i-070477bf35fc54409, which pulls this key fresh each fire (orchestrator _render_command, aws s3 cp at :207) -- so the next monthly cron fire and EG-s-21's single permitted driven run. The change is ADDITIVE and backward compatible (a new key in coverage_verdict.json, no new CLI flag, no changed flag), so an OLD orchestrator against these NEW bytes behaves exactly as before. ROLLBACK, exact key-and-bytes, from TWO independent sources that were verified byte-equal BEFORE the copy: .tools/aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key ec2/etfs-reports/render_month_end.py --copy-source 'opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py?versionId=FVBt9YneBrdWknuYkwRZKKoGrU2blLVk' ; or re-upload git blob 2946fb67c6707b4ec800204d3cefed133cf014ee. Both read sha256 55701125e86740f3bf51a715aba8f68e8441d3eb7bffc99a43b7d3ff29b973e9, 62880 B. AUTHORITY, stated exactly rather than claimed: the L6 issuance at d30e3ca107 names this act, this key and this rollback and is the COO half; there is NO CTO half and this worker cannot obtain one (a worker has no send). The face itself rules this prefix a CODE location and not served output, so CLAUDE.md's never-widen trigger does not fire on it; the gap between that ruling and the face's own words 'with a never-widen sign-off' is filed as a surprise row.
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the PRIOR object and its rollback, proven BEFORE the copy | prior sha256 recorded, and the rollback source read BACK from S3 by versionId and cross-checked against an independent git blob | PRIOR OBJECT AND ROLLBACK PROVEN BEFORE THE COPY. Prior served object: 62880 B, LastModified 2026-09-10T00:18:17.000Z, ETag 545afb2105518af0bc1c1b6bdb4c7ba5, versionId FVBt9YneBrdWknuYkwRZKKoGrU2blLVk, sha256 55701125e86740f3bf51a715aba8f68e8441d3eb7bffc99a43b7d3ff29b973e9. get-bucket-versioning on opal-313476888478-lambda-artifacts returns Status Enabled, so the prior version is retained natively and the rollback is an exact key-and-bytes restore rather than a reconstruction. TWO INDEPENDENT ROLLBACK SOURCES, read and compared at 05:1xZ BEFORE the copy: (1) s3api get-object --version-id FVBt9YneBrdWknuYkwRZKKoGrU2blLVk rc 0 -> 62880 B sha256 55701125...b973e9; (2) git cat-file blob 2946fb67c6707b4ec800204d3cefed133cf014ee -> 62880 B sha256 55701125...b973e9. IDENTICAL. The prior bytes were also already byte-equal to the repo build input, so the archive predates this order and lives in git permanently. | CLOSED 20260910T052038Z |
| L2 | verify | the copy landed at ec2/etfs-reports/render_month_end.py | served bytes sha256 EQUAL to the committed bytes at the commit that carries them, both printed | THE COPY LANDED AND THE SERVED BYTES ARE THE COMMITTED BYTES. put-object rc 0 at 2026-09-10T05:19:33Z. The bytes uploaded were the COMMITTED BLOB (git cat-file blob HEAD:data/etfs/scripts/presentation/render_month_end.py at commit c2787650f5), NOT the worktree checkout -- checked because an autocrlf box can hash a checkout that differs from the record; here both read pure LF and are identical, and that was measured rather than assumed. Served object after the copy: 66756 B, LastModified 2026-09-10T05:19:37.000Z, ETag 71691dafd40df6f4a51179cd53a5439d, new versionId V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH. Read BACK with get-object: sha256 b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f, 66756 B -- EQUAL to the committed bytes on both sha256 and length. Verified against the SERVED artifact, never against the producer's own rc. | CLOSED 20260910T052038Z |
| L3 | verify | nothing else moved in the artifact prefix | full listing of ec2/etfs-reports/ before and after with denominators; exactly one key changed | NOTHING ELSE MOVED IN THE ARTIFACT PREFIX. Full listing of ec2/etfs-reports/ before and after: DENOMINATOR 7 keys before, 7 after, 0 added, 0 removed. Keys changed: EXACTLY 1 of 7 -- ec2/etfs-reports/render_month_end.py, Size 62880 -> 66756, ETag 545afb2105518af0bc1c1b6bdb4c7ba5 -> 71691dafd40df6f4a51179cd53a5439d, which IS this deploy. The other 6 of 7 keys are byte-identical on ETag and Size across the window. | CLOSED 20260910T052038Z |
| L4 | verify | no send, no invoke, no served-report write | AWS/SES metrics zero in the window, zero Lambda invokes by this seat, and platinum/reports/ unchanged with its denominator | NO SEND, NO INVOKE, NO SERVED-REPORT WRITE. (1) SES: AWS/SES Send, Delivery and Reputation.BounceRate, Sum, period 300, over the 25-minute window containing the deploy -- 0 datapoints and Sum 0 on 3 of 3 metrics. (2) SERVED REPORTS: s3://opal-data-etfs/platinum/reports/ listed before AND after the act -- DENOMINATOR 36 keys before, 36 after, and 0 of 36 keys differ on Size, ETag or LastModified. This cell wrote nothing there. (3) INVOKES: this cell fired NO lambda invoke of any kind; the only AWS verbs it used are s3api list-objects-v2, head-object, get-object, put-object and get-bucket-versioning, plus cloudwatch get-metric-statistics -- all enumerated in the committed evidence ledger's steps array, which records argv, rc and UTC for every command. The renderer's own producer-probe path was never reached because no run was fired: the test suite stubs every probe and drives an _ExplodingLam that raises if invoke is ever called, and the whole suite passes. etfs-reports-orchestrator was NOT invoked in any mode. No box run. | CLOSED 20260910T052413Z |
| L5 | verify | the verdict did not move | class counts and the verdict value identical over the same inputs before and after the change, denominator printed, the forced case excluded and said so | THE VERDICT DID NOT MOVE, measured OLD-BYTES vs NEW-BYTES rather than asserted. The OLD module is the exact pre-deploy object read back from S3 by versionId FVBt9YneBrdWknuYkwRZKKoGrU2blLVk (sha256 55701125...b973e9); the NEW module is the committed file now served. BOTH were loaded with identical sys.path seeding so the comparison is not old-code-on-a-broken-path vs new-code-on-a-good-one. Real coverage_gate run in both over IDENTICAL fixture inputs, zero AWS calls. SCENARIO 1, complete month 21 of 21 present: 5 of 5 pre-existing keys (month, verdict, per_partner, holes, unresolved) IDENTICAL; 10 of 10 class counts IDENTICAL; verdict PUBLISH both sides. SCENARIO 2, holed month 16 of 21 with 5 class-C holes: same 5 of 5 keys IDENTICAL; 10 of 10 class counts IDENTICAL (C 5 both sides); verdict REFUSE both sides. Keys ADDED by the change: exactly ['forcing']. Keys REMOVED: none. THE FORCED CASE IS EXCLUDED FROM THIS COMPARISON AND THE REASON IS STATED: the old code cannot express a forcing record at all, so there is nothing on the old side to compare a forced run against; arm (d) asks whether adding the record disturbed the DECISION, which is an unforced-vs-unforced question. The class-C rule at the verdict line is EG-s-4's and is ABSENT FROM THE DIFF. | CLOSED 20260910T052413Z |

## Log

- 20260910T051838Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~5 with 5 leg(s)
- 20260910T052038Z LEG L1 closed: PRIOR OBJECT AND ROLLBACK PROVEN BEFORE THE COPY. Prior served object: 62880 B, LastModified 2026-09-10T00:18:17.000Z, E
- 20260910T052038Z LEG L2 closed: THE COPY LANDED AND THE SERVED BYTES ARE THE COMMITTED BYTES. put-object rc 0 at 2026-09-10T05:19:33Z. The bytes uploade
- 20260910T052038Z LEG L3 closed: NOTHING ELSE MOVED IN THE ARTIFACT PREFIX. Full listing of ec2/etfs-reports/ before and after: DENOMINATOR 7 keys before
- 20260910T052413Z LEG L4 closed: NO SEND, NO INVOKE, NO SERVED-REPORT WRITE. (1) SES: AWS/SES Send, Delivery and Reputation.BounceRate, Sum, period 300, 
- 20260910T052413Z LEG L5 closed: THE VERDICT DID NOT MOVE, measured OLD-BYTES vs NEW-BYTES rather than asserted. The OLD module is the exact pre-deploy o
- 20260910T052413Z CLOSED -- all 5 legs proven

---

## CARRIED DETAIL -- appended AFTER `close` (row `W1-S16`: the ledger re-renders this file from its sentinel on every call)

### THE ACT, IN ONE LINE

`aws s3api put-object` of ONE key: `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py`,
at 2026-09-10T05:19:33Z. Not Terraform (the box pulls this key by name at run time), and not a served
report key (the artifact prefix is a code location).

| | before | after |
|---|---|---|
| bytes | 62,880 | 66,756 |
| sha256 | `55701125e86740f3bf51a715aba8f68e8441d3eb7bffc99a43b7d3ff29b973e9` | `b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f` |
| ETag | `545afb2105518af0bc1c1b6bdb4c7ba5` | `71691dafd40df6f4a51179cd53a5439d` |
| S3 versionId | `FVBt9YneBrdWknuYkwRZKKoGrU2blLVk` | `V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH` |
| LastModified (UTC, s3api) | 2026-09-10T00:18:17.000Z | 2026-09-10T05:19:37.000Z |

The bytes uploaded were the **committed blob** at `c2787650f5`, not the worktree checkout -- checked,
because an autocrlf box can hash a checkout that differs from the record. Here both read pure LF and
are identical, and that was MEASURED rather than assumed. The served object was then read BACK and its
sha256 compared to the committed bytes: EQUAL on hash and on length.

### THE ROLLBACK, FROM TWO INDEPENDENT SOURCES VERIFIED BEFORE THE COPY

`opal-313476888478-lambda-artifacts` has versioning **Enabled** (measured, not assumed -- and it is the
opposite of `opal-data-etfs`, which is Disabled), so the prior bytes are retained natively:

```
.tools/aws s3api copy-object --bucket opal-313476888478-lambda-artifacts \
  --key ec2/etfs-reports/render_month_end.py \
  --copy-source 'opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py?versionId=FVBt9YneBrdWknuYkwRZKKoGrU2blLVk'
```

The second source is `git cat-file blob 2946fb67c6707b4ec800204d3cefed133cf014ee`. Both were read at
05:1xZ **before** the copy and both produce 62,880 B at sha256 `55701125...b973e9` -- identical. The
prior deployed bytes were already byte-equal to the repo build input, so the archive predates this
order and lives in git permanently.

### BLAST RADIUS -- the ACT's, not the producer's decision

**Exactly one key.** The artifact prefix held 7 keys before and 7 after; 1 of 7 changed and it is this
one; 0 added, 0 removed. `platinum/reports/` held 36 keys before and 36 after with **0 of 36** differing
on Size, ETag or LastModified.

**Who it reaches:** the next run of the renderer on the reporter box, which pulls this key fresh on every
fire (`_render_command`, `aws s3 cp ... render_month_end.py`). That is the monthly cron fire and
`EG-s-21`'s single permitted driven run. **The change is additive and backward compatible** -- one new
key inside `coverage_verdict.json`, no new CLI flag and no changed flag -- so an OLD orchestrator running
against these NEW bytes behaves exactly as before. That matters tonight because `EG-s-24` is deploying
the orchestrator in parallel on another slot: the two land in either order without a coupling.

### AUTHORITY, STATED EXACTLY RATHER THAN CLAIMED

The L6 issuance at `d30e3ca107` names this act, this key and this rollback, and places the deploy inside
the cell. That is the COO half and it carries the blast radius and the per-key rollback, which is the
substance CLAUDE.md asks a never-widen sign-off to name. **There is no CTO half, and this worker cannot
obtain one** -- a worker subagent has no send. The face itself rules the artifact prefix a CODE location
and not served output, so the never-widen trigger ("move served output") does not fire on this act; the
gap between that ruling and the face's own words "with a never-widen sign-off" is filed as surprise row
`ETFS_GUARDRAIL-W5-S4` rather than resolved by this worker in either direction.

### WHAT THE DEPLOYED CHANGE DOES, AND WHAT IT DELIBERATELY DOES NOT

It adds `forcing` to `coverage_verdict.json`: `forced` (an explicit boolean on BOTH branches),
`mechanism` (`--fixture-remove` or the literal `none`), `fixture_remove_spec`, `fixture_remove`,
`removed_slice_count`, `run_id`, `run_id_source`, `disclosure_version`. It changes **no** decision: the
verdict was compared OLD-BYTES vs NEW-BYTES over identical inputs across a PUBLISH scenario and a REFUSE
scenario -- 5 of 5 pre-existing keys and 10 of 10 class counts identical in both, exactly one key added.

Untouched by this cell, deliberately: `infra/aws/lambda/etfs-reports-orchestrator/` (`EG-s-24`, live on
`~4`), `data/etfs/scripts/coverage/` (`EG-s-23`, live on `~1`), the class-C verdict rule (`EG-s-4`'s),
and every key under `platinum/reports/`. No send, no invoke, no box run.
