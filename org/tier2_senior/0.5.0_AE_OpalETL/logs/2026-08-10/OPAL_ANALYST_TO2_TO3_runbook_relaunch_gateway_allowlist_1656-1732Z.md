# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-10 1656–1732Z
**Archetype:** build/deploy (TO-2 runbook+relaunch coordination · TO-3 gateway allowlist)
**Project:** OPAL_ANALYST — TO-2 + TO-3 (parallel, per COO GOs 1653Z/1657Z)

## Summary
TO-2: RELAUNCH.md authored (@dc5b2f25d, TIER0_UTILITY lane override — TO-mandated path),
steady-state bound to the Q2 operator-started ruling @bc7eb60de, Q5 upload-guardrail duty
addendum folded (@b08b13bbf per COO routing); launch executed by the seat off the runbook;
all four smoke limbs PASS and ground-truthed beyond self-report. TO-3: identity_scope.py
per-identity server-side tool allowlist landed (@42444e64b) + wired at BOTH chokepoints,
deployed to i-07dccb1615503ac99 via safe-ec2-deploy (3 passes — see finding), Andrew's Q5
overlay row landed with # andrew-asked marker, and all Phase-3 controls EXERCISED PASS.
Both derivation findings adjudicated by CTO~Z @55d62ed46 (F1 corrected the PRD record; F2
resolved by Andrew Q5 @e77bec6e5).

## TO-2 Compiler Tools (each <run> vs <expect>)

| Phase | Run | Observed | Verdict |
|---|---|---|---|
| 1 | Read 0.0.3_BG prompt.md + PRD §4.2 | Runbook steps map 1:1 onto prompt.md On-Launch 1,2,2a,3,4,5 — no step invented/skipped; step-2a gate verbatim-carried; PRD §4.2 prerequisites all present | PASS |
| 3 | Live smoke via the seat (msg 20260810T171138Z) | (1) whoami == "Opal Bloomberg"/opalbloomberg@ (2) pinned Monitor b7043cgjl running, banner pin(server=opal-gateway-bbg, identity=opalbloomberg) + token selected opalbloomberg@ (3) serve DELIVERED 17:10:43Z msg id 1786381843024, from.displayName "Opal Bloomberg" on the SENT artifact (4) broker LIVE PID 22588; 08-07 message actioned + RAVC receipt 17:07Z | PASS 4/4 |
| 3+ | My ground-truth beyond the self-report (Rule 22b) | ps: pinned engine live PID 85065, arm line verbatim incl. TMPDIR, parent wrapper alive; broker get_agent_status corroborates PID 22588 | PASS |

Zero wrapper/scratch scaffolding in the arm path (AC-4). AC-1..4 MET; this log = AC-5.

## TO-3 Compiler Tools (each <run> vs <expect>)

| Phase | Run | Observed | Verdict |
|---|---|---|---|
| 1 | Derive tool needs from REQUEST_CATALOG.md + /bbg-teams-assist SKILL.md; comp-find "tier" gateway app | comp-find DENOMINATOR 159 hits / 30 files; chokepoints = tools._run (:64) + integrations/base.run_integration_tool (:93); derived rows (all frame (i)-(v)): whoami [prompt.md 2a], poll_addressed_teams_messages [TEAMS_DUTY], list_chats/read_chat_messages/send_chat_message [SKILL.md steps 1-2], list_teams/list_channels/read_channel_messages/send_channel_message [SKILL.md step 1 channels]. Frame-(iii) rows structurally absent. Clause-(iv): EMPTY at gateway layer (F1, adjudicated @55d62ed46 — carrier re-ruled to MSTR~Z honesty-layer flip) | PASS (one-pass approved-as-derived; findings surfaced same turn) |
| 2 | EC2-standard deploy | safe-ec2-deploy S3->SSM x3: 17:16Z (ssm:25cc4d7a) code; 17:25Z overlay-intended; 17:29Z (ssm:5033f07a) after include-list fix @2582eb244. Manifest entries committed (SHARED_CLOUD_OPS override, audited; wrapper auto-commit lane-blocked by design) | PASS |
| 3a | DENIED tool from opal-bloomberg key (list_recent_email) | {"error": "identity 'opalbloomberg@...' is scoped ... 'list_recent_email' is not on it (OPAL_ANALYST PRD 4.3; widening is an Andrew ruling...)", "guard_denied": true, "code": "identity_scope_denied"} | PASS (structured, quotable, names the policy) |
| 3b | ALLOWED tool same key (whoami) | Graph serves displayName "Opal Bloomberg", mail opalbloomberg@opalinvest.com | PASS |
| 3c | CONTROL: same denied tool from Andrew's key | list_recent_email returns mail data — Andrew's key unaffected by the layer | PASS |
| 3d | Overlay row (opal_data_refresh_upload, # andrew-asked @e77bec6e5) from bbg key | First run: STILL DENIED — caught the artifact gap (below). After fix: passes scope, integration confirm-gates ("confirm_required", nothing fired); (a)-recheck: all other tools still denied | PASS |
| build | pytest gateway suite | 34/34 (28 existing + 6 new test_identity_scope.py ACs) | PASS |

## Finding banked (instrument, not TO scope)
**The gateway deploy script's tar include list is EXPLICIT (`app deploy requirements.txt`)
— a new root-level file silently never ships, and the wrapper reports green.** Exercised
run (d) caught it; two manifest-recorded "successful" deploys carried no overlay. Fix
@2582eb244 (include-list token). The general lesson is CONTROLS_OVER_CARE's: the deploy
tool's green could not have said otherwise about a file it never packed — only the
exercised behavioral control discriminated.

## Acceptance
- TO-2: AC-1 runbook @dc5b2f25d + addendum @b08b13bbf; AC-2 broker LIVE + pinned monitor
  running; AC-3 serve as "Opal Bloomberg" + 08-07 msg actioned; AC-4 zero scaffolding;
  AC-5 this log.
- TO-3: AC-1 denied-tool structured refusal (exercised, above); AC-2 allowed set passes
  (whoami exercised; Teams serve set = the relaunched seat's live traffic through the same
  layer); AC-3 Andrew-key control unaffected (exercised, separate invocation); AC-4
  allowlist content = CTO~Z frame (i)-(v), one-pass approved-as-derived + Q5 overlay row
  Andrew-worded @e77bec6e5; AC-5 this log.
- Deploy ledger CLOSED: org/critical_paths/change_management/DEPLOY_20260810_m365-gateway_identity-scope_TO3.md

## Blockers
None.

## Next steps
- [2.0.0_SA_COO~Z] TO-2 flip on this log (hash in the report); TO-3 acceptance.
- [0.0.0_AB_MSTR~Z] Q1 carrier: agent-home honesty-layer flip (CTO re-ruling @55d62ed46) + seat refs twin duty text.
