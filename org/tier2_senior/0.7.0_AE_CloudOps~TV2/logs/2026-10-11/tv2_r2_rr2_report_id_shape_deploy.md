# The ticket report route now refuses a request id the report reader could not open — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R2-rr2.report-id-shape-check-code-dell2 (read at 95a7b74437)
**Status:** COMPLETE

---

## Objective

Deploy the code of `opal-ticket-api` at box/dell2 pin `a366ce52ec` with one `safe-apply`, so that
`POST /api/scoped/tickets/{ticketId}/report` refuses a `request_id` that does not fully match
`REQ-[0-9a-f]{24}`. Code only: no env, route, IAM or grant. Cell `R2-rr-2`, the apply of `R2-rr-1`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open --slug tckt-vnext-r2-rr2-report-id-shape-20261011 --lambda opal-ticket-api` + 5 `close-leg` + `close` | PASS | opened BEFORE the first AWS write; closed with all 5 legs proven; `.open_deploys` row read back ABSENT against a 16-row positive control |
| safe-apply.sh | `-chdir=infra/aws/terraform/ticket-center apply <planfile>` | PASS (on the 2nd invocation; the 1st FAILED CLOSED and applied nothing) | see **What failed** |
| terraform plan / replan | `.tools/terraform.exe -chdir=... plan -out=<planfile>`, then `plan` | PASS | branch A exactly: 0 add / 1 change / 0 destroy; replan "No changes." |
| r2_checks.py rr-shape | `python .../R2_CHECKS/r2_checks.py rr-shape` | PASS | `RR-SHAPE-OK passed=4 of 4`, rc 0, at the pin before the upload |
| build-and-upload.sh | `BUILD_ONLY=1 bash ...` then the real run | PASS | the `BUILD_ONLY=1` limb is real: it printed both hashes and uploaded nothing |
| comp-find | `'s3_object_version\|source_code_hash\|aws_s3_object' infra/aws/terraform/modules/yang-lambda/*.tf` | PASS | 4 hits / 3 files scanned; this is what settled the one judgement in leg S2 |
| proof-of-spec-check.py | on the instance | PASS | INVALID twice on schema enums, then VALID (rc=0) |
| safe-commit.sh | 3 commits, `-F` message files written by a non-shell writer | PASS | `msg-verify MATCH` on each |
| commit-gate.sh | via safe-commit | WARN | checked 0 of N files each time — no `.py/.sh/.tf` in any commit. Recorded as NOT evidence of a clean gate, in the gate's own words |
| comp-schedule / comp-iam / comp-adversary | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's own preflight: no schedule, no new AWS call in the 4 inserted lines, refusal arms tested at the build |

**What worked:** `comp-find` over the module answered the one question that mattered and that the order's
own wording could not — whether branch A can literally mean `source_code_hash` only. `deploy_ledger.py`
committing the OPEN entry itself, under its own commit, removed any chance of an open deploy existing
only in my working tree. The `BUILD_ONLY=1` limb let the STOP condition be checked before anything
moved.

**What failed:** my first `safe-apply` invocation. I rode `MSYS_NO_PATHCONV=1`, which CLAUDE.md's Git
section bans for this wrapper **by name**. It mangled every seat-gate's argv to
`C:\c\dev\ajb_workspace\.tools\<gate>.py` — Windows python resolving a leading `/c` against the drive
root — so `apply-who-check` and `crossbox-deploy-check` gave no verdict and the naming limb failed
closed under `LGIC_ENFORCE DEC-6` with rc=2. The gate behaved correctly: it refused an instrument it
could not evaluate, and nothing was planned further or applied. The lesson is the one already written
down; I did not need to rediscover it.

**Gap found:** none in the tools. One gap in a record, filed as `TCKT_VNEXT-D2-S25`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Open-deploys union across every live worktree | 18 trees (denominator), 359 rows summed, 80 distinct basenames; **0** entries naming a ticket function at box/dell2 HEAD against a 19-row negative control. The 3 tckt entries in the union are this lane's own, visible only on stale worker trees, each with a closing commit and a completion record |
| 0 | Open the NEVER-2 ledger FIRST | `20261011T0403Z_tckt-vnext-r2-rr2-report-id-shape-20261011`, 5 legs, committed by the tool |
| 1 | STOP 1 — the pin | `git diff a366ce52ec HEAD` over both ticket trees = **0 paths**; positive control over `org/` = **119**; 0 dirty rows |
| 2 | STOP 2 — the rollback target | live package downloaded from `Code.Location`: 1 member, sha256 `670686262068808f...57a8` = the required value. Whole-package hash in base64 equals the live `CodeSha256`, so the object read IS the running artifact |
| 3 | AC1 + BEFORE state | `RR-SHAPE-OK passed=4 of 4`. `CodeSha256 HK82TEd0SQWe...`, 8 env keys, `opal-tickets` ItemCount 19, `TCK-20261009-a1052909` = status `open` / assignee NULL / created_by `svc-commentary`, 23 attributes |
| 4 | Build + upload | version `RI4EX8i.EL18LgmpA54Fixk.hmjLsH4h`, 29119 B, content-sha256 `W03VREoMEmxNaRoADDDWrXE3IycD9c5vodB+rHBAtg0=`. Downloaded back out of S3 and opened: **1 member, no `tests/`**, hashing to `ca3be343...` |
| 5 | Plan, then ONE safe-apply | `Plan: 0 to add, 1 to change, 0 to destroy` — one resource, three attributes, 28 unchanged attributes and 4 unchanged blocks. `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` |
| 6 | Five after-reads | all pass — see Verification |
| 7 | Close the ledger, commit, report | 5 of 5 legs proven; `5660c698f1`, `68d3261a5d`, `c760683930` |

---

## Verification

```
(a) CodeSha256  W03VREoMEmxNaRoADDDWrXE3IycD9c5vodB+rHBAtg0=   == uploaded zip
    deployed package re-downloaded from Code.Location:
      members: 1 ['lambda_function.py']
      deployed lambda_function.py sha256: ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade
      required (the pinned build)       : ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade
    LastModified 2026-10-11T04:19:14Z | runtime python3.11 | timeout 30 | memory 256 (all unchanged)

(b) env  before count: 8 | after count: 8
         key names identical member for member: True
         values identical: True

(c) POST https://opalinvest.dev/api/scoped/tickets/TCK-20261009-a1052909/report  (no Authorization)
    HTTP 401  {"error":"Missing or invalid Authorization header"}
    control: GET /api/scoped/tickets -> HTTP 401 (a non-000 proves the client reached CloudFront,
    and proves ONLY that -- the authorizer fronts the whole /api/scoped prefix)

(d) opal-tickets  ItemCount 19, TableSizeBytes 22349  (both unchanged)
    TCK-20261009-a1052909: 23/23 attributes, WHOLE ITEM identical: True
      report_ref {request_id: test-f10-20261009-one} -- the malformed id it KEEPS

(e) No changes. Your infrastructure matches the configuration.
```

---

## Decisions Made

1. **Branch A cannot literally mean `source_code_hash` only**, and I did not decide that on my own
   authority. `modules/yang-lambda/main.tf:17` reads the artifact through `data "aws_s3_object"` and
   `:38`/`:39` set both `s3_object_version` and `source_code_hash` from it, so every code deploy moves
   both plus the computed `last_modified`. The SA1 deploy of this same function was accepted with the
   identical three attributes. This plan is strictly NARROWER than that precedent, so it is branch A in
   the sense the order means. Recorded in leg S2 rather than left implicit.
2. **The ledger was opened before the pre-checks**, not after, because this order's step 0 and both
   signed halves say the ledger opens first. The SA1 precedent ran its pre-checks first on the grounds
   that they are pure reads; where the order and the precedent differ, the order wins.
3. **`lambda-source-map.json` was not touched.** It is outside the order's `<paths>`. Its drift became
   row S25 rather than a rider on this deploy.
4. **AC2 was not self-graded.** Both halves are evidenced in the proof_of_spec and the verdict is left
   to the CVO at L9, which is what `judgment="true"` means.

---

## Files Modified

| File | Commit |
|------|--------|
| `org/critical_paths/change_management/20261011T0403Z_tckt-vnext-r2-rr2-report-id-shape-20261011_deploy_completion.md` | opened by the tool, closed at `5660c698f1` |
| `org/critical_paths/.open_deploys/tckt-vnext-r2-rr2-report-id-shape-20261011.json` | created by the tool, removed at `5660c698f1` |
| `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/TCKT_VNEXT.TO-APPLY-R2-rr2.report-id-shape-check-code-dell2.proof_of_spec.json` | `68d3261a5d` |
| `org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md` | `68d3261a5d` (row S25) |
| `org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-APPLY-R2-rr2.report-id-shape-check-code-dell2.md` | `c760683930` (`pending` -> `complete`) |

No AWS resource other than `opal-ticket-api`'s code was touched, and the plan is the evidence.

---

## Blockers

None. Nothing is stranded: no open deploy entry remains for this slug, and the rollback source is
retained as non-latest S3 object version `TNDfJSNhCarmtqRmFU.jsPUaiO7BLSsK` (28994 B, handler
`670686262068808f...57a8`), so the rollback the CTO half names is executable by the same method without
a rebuild.

---

## Current State

The report-id shape check is LIVE on `opal-ticket-api`, verified by content against the pinned build
input. The route's auth surface is intact. The table and the control ticket are untouched. The order is
`complete`; AC2 awaits the CVO at L9.

**What this deploy does NOT establish:** neither live arm of the new check — a well-formed id stored, a
malformed one refused — was exercised against the deployed route. Both need an in_progress ticket held
by an internal assignee and are cell `R2-tr-1`'s under its own pair. The refusal is proven at the build
only (4 of 4). And per the CTO half's own section 2, that every id the analysis service ISSUES carries
the `REQ-<24 hex>` shape is **inferred from the reader, not measured** — the minting site was read by
nobody. That is the CTO half's condition 3, graded at `R2-tr-1`'s first exercise.

---

## Next Steps

1. Report once to `2.0.0_SA_COO~V2` with push state measured by `git ls-remote` — this seat's single
   send for this order.
2. `R2-tr-1` exercises both live arms under its own pair. If its journey gets a 400 from this route on
   an id the analysis service issued, the CTO half's condition 3 makes that **Branch B at once**:
   re-apply the `5a36586b5f` build and file a BLOCKING row; the journey is not re-run around it.
3. Row `TCKT_VNEXT-D2-S25` sits `UNDER_INVESTIGATION` for the channel's owner. No act proposed.
