# CTO~Z session close -- 2026-09-01T21:43Z -> 2026-09-02T15:00Z

**serial:** 1.0.0_SA_CTO~Z (site-Z lane; base folder, lane named here per XXX.md)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (portal promote, gate edits, production MFA enablement), VALIDATE
(served-plane and fresh-scan verification, proven-red suites), COORDINATE (three integrator legs,
merge window hold), RECORD (four Andrew-direct rulings, verbatim)

This is the HANDOFF. Substance already sits in two delta logs this session; this file consolidates
the end state for a reader with zero context and points at where each act is recorded.
  delta 1  logs/2026-09-02/ctoZ_partner_mfa_push_cottonwood_pages_gate5_sms_watch_2143-1445Z.md @0bb357bbea
  delta 2  logs/2026-09-02/ctoZ_all_recs_approved_executed_1445-1455Z.md @705e1b0db1
  ruling   deliverables/ANDREW_DIRECT_20260902_ALL_RECS_APPROVED_OPEN_CALLS_CTOZ.md @98fd4ca0d4

## Andrew-direct this session (all recorded verbatim in the deltas + ruling record, all broadcast)
1. Cottonwood dashboard gains Attribution + Factor Tilts, then /prod-deploy.   (09-01 ~21:5xZ)
2. "fix the gate so DT can push portal prod"                                    (09-01 ~22:4xZ)
3. SMS-permission watch into comp-schedule; D12 owner on site Z must know.     (09-02 ~14:0xZ)
4. "global MFA push on the client side ... MFA is required for all users"      (09-02 ~14:0xZ)
5. "all recs approved" on the four /open-calls cards                            (09-02 ~14:4xZ)

## Commits this session, author 1.0.0_SA_CTO~Z (all ON ORIGIN, is-ancestor of origin/SITEZ read 15:0xZ)
  2df2b212de  audit-archive-invoker durable findings (the A.2 tool's own auto-commit at startup)
  f28fb28718  portal pointer -> 793c17dd; PROD 4b88e55e / portal-v2.1.175
  5fb8143d72  GATE 5: DT may push PROD in the portal repo (by origin remote)
  26221d9c2e  gate test suite made hermetic (totals depended on runner identity)
  99b5b51c57  .open_deploys/d12-sms-origination-identity-activation.json -> comp-schedule G-7
  0bb357bbea  delta log 1
  98fd4ca0d4  SITEZ shared; DT carve-out PROD|DEV; /prod-deploy Step 1a payload check + Step 0 override
  705e1b0db1  delta log 2
Portal repo: DEV 793c17dd (firmAccess: cottonwood += /attribution, /factor-tilts); PROD 4b88e55e
(merge of DEV, tag portal-v2.1.175, CI run 33565904844 success). Pushes were 0.0.0_AB_MSTR~Z's legs.

## Compiler Tools (cited from context, none re-run for this table)
| tool | target | result | note |
|---|---|---|---|
| comp-read | TenantLayoutConfig, firmAccess, portal_data_proxy, auth.ts, sms.ts, 005_backfill, gate, comp-schedule | PASS | --enumerate 'firm' on the proxy: 0 of 2444 lines |
| comp-find | cottonwood, AC4, '/factor-tilts', ALLOWED_PATHS, mfaRequired, SP-1, requireMFA | PASS | denominators printed each run |
| comp-schedule | --self-test 5/5; live view 19->20; --drift clean | PASS | tool is python, not on PATH bare |
| test_never_rules_gate.sh | 71/12 -> 79/12 -> 76/15 (pinned) -> 94/2 | PASS | proven-red vs old hook both times |
| bun run typecheck | portal | PASS rc=0 | |
| commit-gate / msg-verify | 8 commits | PASS | one ASCII-gate refusal (fixed), one WARN on a pre-existing non-ASCII test line |
| aws (operational) | dynamodb scan x5 (LastEvaluatedKey absent each), update-item x17, describe-table, sesv2 get-account | PASS | |
What failed: heredoc-carried python mangled backslashes twice (nothing written -- asserts first);
in-place hook write crashed Bash at a peer seat mid-save (banked as memory).
Gap found: GATE 1's -c pull.rebase one-shot matcher does not fire on any device (2 arms, surfaced).

## Blockers
None at this seat. Nothing is BLOCKED; everything open is owned elsewhere (Next Steps).

## Current State (zero-context handoff)
- **Cottonwood:** Attribution + Factor Tilts LIVE. Read from the served bundle index-C3xFrccZ.js:
  all four FIRM_ALLOWED_PATHS sets, cottonwood alone carries the two paths. No new data exposure
  (every fetcher takes zero args; proxy has no firm gate).
- **MFA:** opal-users-v2 (us-east-1) 32 of 48 PROFILE rows mfaEnabled=true, all mfaChannel=email:
  15 internal + 17 partner-firm humans. The 16 OFF are 13 test/demo/fixture, 2 service
  (svc-bbgtml@ = Bloomberg upload, cot-verify-internal@), 1 disabled -- by Andrew's rulings. No
  phone on any row; SMS gated on SP-1. requireMFA in CONFIG#defaults is unread by the handler.
  Reversible per row: mfaEnabled=false.
- **Gates (live by reading, no push needed):** SHARED_BRANCHES = CLOUD|DEV|PROD|SITEZ|main|master.
  GATE 5 admits MSTR anywhere; DT on portal PROD|DEV push (origin remote Opal-Capital/portal).
  Session serial file (XXX.md A.1) is load-bearing for any push from this device.
- **/prod-deploy skill:** Step 0 names GATE 5 + the audited-override path for Andrew-directed
  non-DT; Step 1a requires origin/DEV..HEAD to carry only the DT's own commits.
- **comp-schedule G-7:** AWS toll-free provisioning (SP-1) + SP-2 env var + SP-3 sandbox-exit
  review, HELD-SOVEREIGN-GATED, author 1.0.0_SA_CTO~Z (--owner will not show it to AE; broadcast did).
- **Fabric:** zero crons at this seat; watcher task ba9ps95uv, parent-tied pid 49253. Live seats
  at close: 0.0.0_AB_MSTR~Z and this seat; COO~Z/CVO~Z/AE~Z/DE~Z down all session (their mail QUEUED).

## Next Steps
- **[3.0.0_SA_CVO~Z]** class the -c pull.rebase NEVER#7 evasion (19347); disarm the SITEZ ARMED item.
- **[0.4.0_DE_ClientPlatform~Z]** stale-bundle hazard for 17 partner users; SF-2 part 2/2 (the consumer
  of the enrolment API, without which the 18907 sms lockout path stays unremediated).
- **[0.7.0_AE_CloudOps~Z]** G-7 SP-1/SP-2 legs when AWS provisioning lands; MANIFEST add for
  org/commit-msg-ascii-override-audit.log with rv0057-f001.
- **[0.0.0_AB_MSTR~Z]** push of this close log.
- **[Andrew]** nothing open at this seat.
