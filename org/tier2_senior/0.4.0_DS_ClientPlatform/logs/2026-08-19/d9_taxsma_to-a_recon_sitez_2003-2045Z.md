# Session log — 0.4.0_DS_ClientPlatform~Z — D9_TAXSMA.TO-A-SITEZ state-assessment recon
**archetype:** DIAGNOSE

**Window:** 2026-08-19 20:03Z–20:45Z (site Z). **TO:** D9_TAXSMA.TO-A-SITEZ (P1-program,
START-NOW, read-only). Kickoff triple: prd=docs/architecture/D9_TAX_SMA_OPS_PRD.md,
workstream=(a) §4.1 TO-A only, head_version=@fac13ccc3a.

## What happened

1. Startup per org/XXX.md: /watcher (registered PID 12692, Monitor blpcf6tot confirmed
   running), serial file, audit-archive-invoker (18 standing cross-device findings, persisted by
   the invoker, pre-existing), PATH 91/97 + exercise PASS, owned-paths hook present,
   .agent_context + comp-to set. Kickoff read; TO flipped staged->pending in-tree — safe-commit
   REFUSED on MSTR's TIER0_EXEC lane (anticipated by the kickoff); edit left UNSTAGED for
   MSTR's own commit, MSTR notified in the ack.
2. PRD + atom-decomp run read PINNED @fac13ccc3a (git show; 172 + 71 lines).
3. Phase-1 mandate executed: comp-estate (no taxsma thread: 29 verticals/138 chains, 0 hits;
   --resource taxsma: none) -> comp-find census (49/49 filename hits enumerated, ~26,352 files
   scanned); comp-pipescript deployed (both chain scripts NOT-IN-TREE in every tree of its
   universe — no `assets` tree in the enum; coverage-gap finding); TRIGGER CENSUS on the
   producer: DESIRED no-schedule == APPLIED no-trigger (no policy/rules/ESMs) == EXERCISED
   once-ever (1 log stream, 1 invocation datapoint in 50d) => verdict NEVER-SCHEDULED.
4. Live S3: chain tree conforming to 17b; all tiers single build-day vintage 2026-07-17; gold
   one account; roster 07-21, 3 accounts (2 pending_resolution on the D2/D3 sovereign word).
5. SharePoint leg (envelope held, no delta from MSTR's baseline): Intake Logs = 1 file ever
   (07-15); Short Sale census 39 items; mailbox probe: FIS feed ALIVE through 08-19 => pt1
   operator cadence idle, not a dead feed. Master Tax SMA Accounts.xlsx (08-13) read in full:
   11 accounts/$27.71M/5 traded 08-05 vs roster 3 vs gold 1. SOP docx read in full (3pp):
   no enrollment-handoff step.
6. MAP-VS-TERRITORY finding: WS-4/WS-R5 roles (recorded REMAINING, Andrew+CTO-gated) are LIVE,
   Created 2026-08-15T02:32Z inside the OPAL_GWRENAME S3 apply window; live policy == DESIRED
   lean-SPLIT exactly (least-privilege holds); no WS-4 go-live record found. Gate-sequencing
   finding, recorded not fixed.
7. Mid-pass rulings folded in: COO~Z 201546Z (#42 artifact classified, not re-opened);
   Andrew ~20:12Z relay @1e0ec3b079 ((c1) WAIVED ahead of the meeting — rows reclassified
   WAIVED-BY-RULING); MSTR~Z 202732Z (#42 DISPOSED — Andrew ruled SUPERSEDED by D7+D9
   @3c8c3f1035 — part 6 cites, no recommendation; #48 rec unchanged). Ingest pointer
   (Downloads pair + SMARTX CSVs, Andrew YES, laptop CTO executes) ferries later — slot noted.
8. Deliverables written: D9_TAXSMA_TO-A_STATE_ASSESSMENT_SITEZ_20260819.md (all 7 contract
   parts), D9_TAXSMA_TO-A_LIVE_TRUTH_TABLE.json (machine table), proof instance
   D9_TAXSMA.TO-A_PROOF_OF_SPEC.json (validated rc=0 before its commit), this log.
   Lane-committed only, never pushed (MSTR~Z integrates).

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-estate | `--list` / `--resource taxsma` | 29 verticals/138 chains, NO taxsma thread; no chain references 'taxsma' -> routed to comp-find per TO |
| comp-find | `--name "*taxsma*"` (+ --page 2) | 49/49 hits, 26,352-26,357 files scanned; located chain scripts, producer lambda dir, TF, TO #42 file, Yang spec, 4 open drift findings |
| comp-find | `'opal-assets-bd49f-reporting-pull' infra/` | 41 hits/7,816 files; resolved producer TF + source-map + census rows |
| comp-find | `'monolith' infra/aws/terraform/opal-assets/` | 134 hits/16 files; monolith bucket = opal-data-assets (monolith.tf:59) |
| comp-pipescript | `deployed <both chain scripts>` (flagless rc=2 REFUSED as designed; `--pipeline mdpf` scoped; no-arg sweep) | NOT-IN-TREE both; "NOTHING VERIFIED... could not place"; GAP: no `assets` tree in --pipeline enum (Rule-22 coverage defect, routed in deliverable H8) |
| comp-which | `"what schedules or triggers invoke ..."` | near-tie comp-aws/comp-estate/comp-iam; census snapshot insufficient for live discrimination -> live primitives with `# rail-checked` markers |
| comp-to | `D9_TAXSMA.TO-A-SITEZ.state-assessment-recon` | session TO_ID set race-free |

Raw-primitive calls (all `# rail-checked`, read-only): lambda get-function-configuration /
get-policy / list-event-source-mappings, events list-rule-names-by-target, logs
describe-log-streams, cloudwatch get-metric-statistics, iam get-role x3 (+1 positive control) /
list-role-policies / get-role-policy, s3 ls/cp. Gateway MCP: whoami, find_sharepoint_site,
list_site_files x2, search_site_files x2, search_email, read_site_workbook, read_document.

Gap found: comp-pipescript's pipeline universe lacks `data/assets` (H8 in the deliverable);
comp-estate carries no taxsma thread (expected — chain never registered as a vertical).

## Blockers
None of mine. Sovereign-pending (not blocking TO-A): D2/D3 egress word; #42/#48 disposition
(part-6 rec routed via MSTR); WS-4 landed-unratified finding (H5) routed via MSTR ferry.

## Next steps
1. [MSTR~Z] commit the in-tree TO status flip (my serial is refused on TIER0_EXEC — deliberate).
2. [Andrew via MSTR] part-6 disposition on #48 only (#42 already ruled SUPERSEDED
   @3c8c3f1035); H5 WS-4 ratify-or-rerun-sequence call.
3. [COO~Z] flip mechanics on disposition; H7 (4 overdue drift advisories, theirs).
4. [(c1) owner when cut — waived @1e0ec3b079] WS-5 + multi-account + guardrail test set;
   H8 comp-pipescript assets-tree gap to CTO routing.
