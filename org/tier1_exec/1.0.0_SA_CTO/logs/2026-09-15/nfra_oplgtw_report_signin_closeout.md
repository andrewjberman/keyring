# NFRA_OPLGTW L4 and report sign-in repair - 1.0.0_SA_CTO~A
**archetype:** MIXED

**Date:** 2026-09-15
**Task Order:** ad-hoc NFRA_OPLGTW registration/PRD and Andrew-direct responsive report/OIDC repair
**Status:** COMPLETE
**Window:** 2026-09-14T19:11Z -> 2026-09-15T04:25:37Z
**Coverage:** 15 exact-seat commits, 17 significant inbound messages, 8 named deploy/ruling/validation milestones. Routine ACKs and outbound status traffic are excluded from the message count. This log's own commit is excluded.

No exact-seat prior log was found across the latest two dated directories (2026-09-14 and 2026-09-13). The latest base-CTO wind-down log belongs to a different serial; this record covers the current exact-seat session from Andrew's 15:11 ET commission.

## Objective

Register the CloudOps brief as D9/NFRA/NFRA_OPLGTW and prepare its signed PRD under the canonical workflow. Subsequently fulfill Andrew's direct request for a report that resizes across devices and repair the HTTP 500 encountered during Microsoft sign-in at mcp.opalinvest.dev.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | Natural-language routing before inspections | PARTIAL | Several questions had no curated match; unrelated fuzzy candidates were not treated as authoritative routes. |
| comp-find | Scoped content queries against exact inbox files, contracts, and evidence | PASS | Located exact subjects and clauses without substituting other inbox messages. |
| comp-find | Scoped query against private apply_alb.py outside the repository | FAIL | git ls-files rejected the out-of-repository scope; the exact known local file was read directly. |
| comp-blast | sg-02571ff2f33d2f9d4 | WARN | PRESENT_WITH_ZERO_RESULTS, zero extracted downstream edges; not proof of no consumers. Live ALB association supplied the missing operational context. |
| comp-tagauthz | check --default-tags-tree infra/aws/terraform/opal-gateway --from-plan <private scoped plan JSON> | PASS | Gate found no overwritten access-granting tags among 0 candidate resources. Boundaries, session policies, resource policies and other named exclusions were not swept. |
| comp-pulse | diff <explicit commit pathspecs>, via safe-commit | PARTIAL | Stale danger-map/absent-subject advisories were retained. Deleted sentinel and template paths cannot establish a clean risk census. |

**What worked:** Exact scoped lookups, live AWS readback, canonical safe-apply, and the targeted tag/tombstone gates produced usable evidence. The saved-plan digest preserved the precise adjudicated change.

**What failed:** Generic routing often lacked a curated fit. Private scratch files were outside comp-find's repository scope. Generic commit gates checked no language-bearing files in the documentation-only closeout; their successful wrapper exit is not test coverage.

**Gap found:** Graph and generic gate coverage did not independently establish the SG's live consumers, certification-JSON validity, or end-to-end authentication. Specific integrity checks, AWS evidence and Andrew's real sign-in supplied those bounded checks. No tool was rerun merely to populate this table; org/compiler-tools-log.md was not edited.

## Work Completed

### 1. NFRA_OPLGTW registration, approved endpoints and L4 closure

Read the brief at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/SPEC.md` and checked the repository /endpoints --forward claude and /canonical-flow authoring routes. Registered the project in D9/NFRA, Opal Workflows, and recorded Andrew's approval of all eight endpoint bars. Each bar still requires a deliberate walkthrough or controlled test at delivery.

The initial PRD was revised to v0.2 to restore brief requirements, signed on both reviewed halves, and ratified. The evidence run is `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/`; consumers must use `rectangle.final.certified.json`, not the historical verifier mutant. CVO's documentary CERTIFIED PASS is pinned at `a5a686e63a6ebfbd0528286e33f968da4e0290b9`; the run-home certification copy is `64e8c5fea3e77cafa4f5606340bfbae24ffbcfd2`. Neither proves live access, effective grants, query accuracy or downloads.

Own commits: commission `45ce4e5b73`, endpoint approval `4498e665cc`, registration/initial PRD `2af252cb39`, v0.2 restoration `059526828b`, evidence repair `e0171ca585`, certified closure `bc3f6698a8`, ratification/L4 handoff `f0aa50dbc0`. L4 closeout names `2.0.0_SA_COO` as next owner for L5; handoff was delivered at 23:38:02Z.

### 2. Responsive report publication and Gateway source

`daily_reports/scripts/render_daily_report.py` and the canonical template now produce the same responsive document under both legacy desktop/mobile filenames. Above 940px it uses the rail and selected stage; below 940px all eight items expand. Tick density changes at 600px; resize/rotation retains the document and selection. The obsolete fixed mobile template was removed; the publisher's entry no longer selects by user agent. The 52-character card cap remains enforced.

Published both dated and latest report objects plus the latest entry using the existing publisher. All four report bodies were 51,754 bytes with ETag `f299cf256de264e16ecec4ff9c979b2e`, and readback SHA-256 matched tested bytes. Private presigned URLs and rollback bytes were retained outside the repository. Evidence is under `org/tier1_exec/1.0.0_SA_CTO/deliverables/DAILY_REPORT_RESPONSIVE_20260915/`.

324 local and 498 live browser checks passed their layout/diagram/script-exception assertions. Live resource errors were retained: an unsigned favicon request produced S3 403, while report documents and embedded diagrams succeeded. MSTR independently validated seven widths and all eight diagrams. Eight Gateway regression checks passed for `infra/aws/ec2/opal-gateway/app/sprint_view.py`, which skips the legacy narrow hop for the responsive marker and preserves archive behavior.

Own commits: report source/evidence `1339794f8f`, publication receipt `bc635c5685`, exact-two-file Gateway source `ee268aa92a`, source handoff/pre-fix diagnosis `bd110eec90`. The Gateway source commit used the explicitly authorized audited one-commit CLOUD_OPS_OR_ETL lane override. Another seat's live index lock was allowed to finish; no lock deletion or process termination occurred. No Gateway service deployment was needed.

### 3. Diagnose and repair live OIDC HTTP 500

The ALB callback at 03:24:55.786498Z returned 500, target `-`, action `authenticate`, error `AuthTokenEpRequestTimeout`; it did not reach the healthy Gateway target. ALB SG `sg-02571ff2f33d2f9d4` allowed only TCP8080 to `172.31.0.0/16`, preventing outbound HTTPS calls to Microsoft's OIDC endpoints.

Andrew's existing item-1 approval (`cfcb13e03f`) and CTO Msg96866 authorized this seat to own the repair. Opened the canonical ledger before deployment, committed the exact `alb.tf` change alone, and stopped when the full plan also proposed two WAF description updates. CTO Msg96877 explicitly approved the existing targeted saved plan SHA-256 `00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b` and required leaving the WAF differences alone.

Canonical safe-apply succeeded: 0 added, 1 in-place change, 0 destroyed. Live readback at 04:03:48Z confirmed TCP443 to `0.0.0.0/0`, preserved TCP8080 VPC egress, and unchanged ingress. The SG-only re-plan at 04:04:12Z exited 0 with no changes or resource drift. The two empty WAF IP sets retain their deliberately unapplied description-only differences; no full-tree zero-diff claim is made.

Andrew answered "Report loads" after opening a fresh report URL and signing in. CloudWatch recorded ELBAuthSuccess=1 in the post-apply 04:04Z minute. The callback at 04:04:58.944981Z returned 302 with error reason `-`; the delivered post-apply window contained 11 requests, zero parse errors and zero AuthTokenEp errors. Logs can lag, and the report-visible result is Andrew's direct confirmation, not an inferred /sprint 200 from that excerpt.

All four ledger legs were proven and the entry CLOSED at 04:06:35Z. CTO and MSTR were notified; exact completed messages were archived. Own commits: ledger opening `f98358be5b`, alb.tf-only source `d9d51fc43d`, plan-stop/scoped review `d99298c036`, applied/exercised closeout `1e89254fbbf6928cb52a6d87cbb264d8b0d87b12`.

### 4. Session remote access and significant traffic

At Andrew's request, session remote control was enabled on the existing shared app-server and pairing was offered. No separate daemon or second Codex session was started. The last observed paired-client count was zero; expired pairing codes are not recorded here. No fresh pairing operation was requested by this log invocation.

17 significant inbound notifications covered: two CRO brief-half decisions; five CVO evidence/certification/lock-completion messages; five MSTR direct-authority/validation/lock messages; one COO direct-authority relay; and four CTO source-commit/apply/scoped-plan/exercise messages. Material late messages are Msg96860, 96861, 96864, 96866, 96868, 96877 and 96884. Their asks were completed or routed within Andrew's authorization. The current exact-seat root inbox sweep found no unread message files.

The eight counted milestones are endpoint approval, documentary certification, L4 ratification/handoff, responsive publication, MSTR layout validation, targeted-plan adjudication, ALB deployment, and real-user sign-in validation.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Retain exact serial 1.0.0_SA_CTO~A throughout | Launcher identity remains authoritative even though the repository home is shared with base CTO. |
| Complete PRD/L4 without implying implementation | The signatures and CVO verdict certify documentary evidence; live endpoint bars remain delivery obligations. |
| Publish one responsive document under both legacy filenames | Existing links keep working through resizing and rotation. |
| Stop the full Terraform plan, then apply only the expressly approved saved scoped plan | Two unrelated WAF description updates were outside the repair authority. |
| Close only after APPLIED and EXERCISED proofs | Actual user sign-in and live auth telemetry were available; no synthetic browser success was substituted. |
| Keep commits local and preserve push/merge holds | Existing authorization permits local scoped commits but keeps CLOUD push and SITEZ merge held. |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/NFRA_OPLGTW.json`, `org/missions/D9/NFRA/NFRA_OPLGTW/project.json`, `org/standards/NFRA_OPLGTW_CONTRACT.json` | D9/NFRA registration and contract, with registry/directive consistency updates | Yes - `2af252cb39` |
| `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, `prd/L4_CLOSEOUT.md`, evidence pointer/stamp | v0.2 restoration and ratified L4 handoff | Yes - `059526828b`, `f0aa50dbc0` |
| `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/` evidence and closure files | Repaired documentary evidence and certified consumable audit trail | Yes - `e0171ca585`, `bc3f6698a8` |
| `daily_reports/scripts/render_daily_report.py`, `publish_daily_report.py`, `check_responsive_report.py`, templates, dated HTML outputs, README | Responsive rendering, publishing and checks | Yes - `1339794f8f` |
| `infra/aws/ec2/opal-gateway/app/sprint_view.py`, `tests/test_sprint_view.py` | Responsive marker handling and regression checks | Yes - `ee268aa92a` |
| `infra/aws/terraform/opal-gateway/alb.tf` | Approved HTTPS egress block only | Yes - `d9d51fc43d` |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/DAILY_REPORT_RESPONSIVE_20260915/` evidence files | Publication, diagnosis, scoped authority, apply, user verification and final closeout | Yes - `1339794f8f`, `bc635c5685`, `bd110eec90`, `d99298c036`, `1e89254fbb` |
| `org/critical_paths/change_management/20260915T0343Z_opal-gateway-alb-oidc-egress_deploy_completion.md` and its canonical sentinel | Opened before deployment; all legs proven; CLOSED and sentinel removed | Yes - `f98358be5b`, `d99298c036`, `1e89254fbb` |

## Blockers

No live blocker remains for this seat's completed L4 authoring, report publication or sign-in repair. NFRA_OPLGTW L5 is a handed-off next stage, not a verified blocker: the last verified closeout names the COO and leaves dep_stage at PRD until its decomposition/battery exists. This logging tick does not claim a fresh downstream status census. CLOUD push and CLOUD-to-SITEZ merge remain explicit holds; no active Master local-commit merge window was present in the current context or exact-seat unread inbox.

## Current State

NFRA_OPLGTW is registered in D9/NFRA with PRD v0.2 RATIFIED/ADMITTED and L4 complete at `f0aa50dbc0`; the next recorded owner is `2.0.0_SA_COO` for L5, consuming the certified rectangle under `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/`. The responsive report is live at `https://mcp.opalinvest.dev/sprint`, and Andrew has confirmed it loads after sign-in following the SG repair in `infra/aws/terraform/opal-gateway/alb.tf` (`d9d51fc43d`). `org/tier1_exec/1.0.0_SA_CTO/deliverables/DAILY_REPORT_RESPONSIVE_20260915/ALB_EGRESS/CLOSEOUT.md` and the CLOSED deploy ledger contain the APPLIED/EXERCISED evidence committed at `1e89254fbb`; the known WAF description differences remain outside scope. No Gateway service deployment, CLOUD push or SITEZ merge occurred, and this one-shot log does not arm a cadence or alter launcher-owned runtime helpers.

## Next Steps

1. [2.0.0_SA_COO] Consume the existing L4 handoff and assign the NFRA_OPLGTW L5 lane/decomposition when the canonical sequence permits; preserve the distinction between documentary certification and live endpoint validation.
2. [1.0.0_SA_CTO] Retain the completed repair receipts and adjudicate any future WAF-description reconciliation as separate work; it is not a defect in this completed SG repair.
3. [1.0.0_SA_CTO~A] Honor existing push/merge holds and respond to new authorized work. No further repair action or recurring log is armed by this invocation.
