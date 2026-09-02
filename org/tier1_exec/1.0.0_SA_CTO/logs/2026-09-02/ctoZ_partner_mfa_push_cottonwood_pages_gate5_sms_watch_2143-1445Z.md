# CTO~Z session log -- Cottonwood pages promote, GATE 5 DT carve-out, SMS watch armed, partner-firm MFA push

**serial:** 1.0.0_SA_CTO~Z
**window:** 2026-09-01T21:43Z -> 2026-09-02T14:45Z
**archetype:** IMPLEMENT (production MFA enablement, gate edit, portal promote)
**secondary_archetypes:** VALIDATE (served-plane reads, fresh-scan verification), COORDINATE (three integrator
legs, D12 seats), RECORD (Andrew-direct rulings x4, verbatim)

## Andrew-direct instructions this window, VERBATIM (recorded per XXX.md; each broadcast same turn)

1. "What I need from you here is a solo project, just a few switches that need to be flipped and a
   /prod-deploy portal promote after. We want to add the "Attribution" and "Factor Tilts" pages to the
   Cottonwood dashboard."
2. "this should not require MSTR to push, portal prod-deploy is always allowed by DT, its part of the
   prod-deploy skill." then "fix the gate so DT can push portal prod"
3. "We need to keep an eye out for the SMS permissions from AWS. I would check out comp-schedule and
   identify wherever the underling schedule document is and make a note in there that we need to stay on
   top of that, whoever is responsible for D12 (which is likely going to stay on sitez fabric), needs to
   be aware of that, because we need to assess when that goes through"
4. "I think we are ready for global MFA push on the client side, we need to flip the switches so that
   MFA is required for all users."

## DONE

**1. Cottonwood gains Attribution + Factor Tilts -- LIVE, served-plane verified.** portal DEV 793c17dd
(firmAccess.ts, FIRM_ALLOWED_PATHS['cottonwood'] += '/attribution','/factor-tilts', 10 insertions).
NOT the AdvisorIntelligence tenant layout -- TabType holds neither; both are top-level Analysis-section
routes with no dev/admin/tier flag, so isPathAllowedForFirm is the single gate (one [DEF] in the corpus).
No new data exposure: all 5 fetchers take zero args; portal_data_proxy contains 'firm' 0 times in 2444
lines. Predicate exercised 10/10 with negatives (correlations/ticket-center still denied; inflection/49f/
demo no spill). Promote: merge 4b88e55e, parity gate 0 bytes, CI run 33565904844 success (1 of 1 workflow
on the sha), tag portal-v2.1.175 peeled = PROD head. SERVED: entry chunk index-CQCRJQRU -> index-C3xFrccZ;
all FOUR firm allowlists read out of the live bundle, cottonwood HAS both paths, the other three do not.
Passengers disclosed: 5 non-directed commits rode (D12 SF-2 "part 1/2", SF-3, 3x perfrp from laptop
lane 0.4.0_DE~D). Pointer bump f28fb28718. All three pushes were 0.0.0_AB_MSTR~Z's legs.

**2. GATE 5 now admits DT pushing PROD in the PORTAL repo** @5fb8143d72 (on origin). Four conjuncts:
DT serial, branch PROD, origin remote Opal-Capital/portal, verb push. Repo test is BY REMOTE not path
(Step 4 pushes from an ephemeral worktree). DEV deliberately NOT widened. 8 test arms (1 pos / 7 neg),
PROVEN-RED against the old hook. Pickaxed: no DT/prod-deploy carve-out ever existed -- unimplemented
intent, not a regression. Suite hermeticity fix @26221d9c2e: totals depended on runner identity (GATE 5
denying pull-arms on identity masked GATE 1 never firing -- "green for the wrong gate"); pinned, now
76/15 for every runner.

**3. SMS provisioning watch ARMED** @99b5b51c57 (on origin) as .open_deploys/d12-sms-origination-
identity-activation.json. comp-schedule STORES NOTHING (compiles from carriers) -- zero armed gates
mentioned SMS before this. Now G-7, 19->20 armed, C2 2->3, not a drift candidate. Holds SP-1 (toll-free
+ carrier verification, ~1-3wk, Andrew-gated), SP-2 (SMS_ORIGINATION_IDENTITY on Andrew GO), SP-3
(sandbox-exit review). Hazard recorded from sms.ts:38-44: sandbox exit is account-level and out-of-band;
nothing in the estate observes it. LIMITATION: --owner derives from `author` only (comp-schedule:229), so
--owner 0.7.0_AE_CloudOps will not surface it; awareness discharged by broadcast 19316-19320.

**4. Email MFA ENABLED on 9 partner-firm humans** -- direct conditional update-item on opal-users-v2,
SET mfaChannel='email', mfaEnabled=true (the two fields setMfaPreference writes), condition
(attribute_not_exists(mfaEnabled) OR mfaEnabled=false) AND status='active'. cottonwood christa.bass /
jay.rubottom / stephen.shipley; inflection noel / patrick / joe / peter; 49financial lizah.okoniewski /
dan.wohlgemuth. APPLIED 9 / SKIP 0 / ERR 0. FRESH FULL SCAN: 48 PROFILE rows (LastEvaluatedKey absent),
24 ON all email (15 internal + 9), 9/9 targets ON, STRAY none, svc-bbgtml@ + cot-verify-internal@ OFF.
updatedAt did NOT move -- the write sets only the two MFA fields; the values are the evidence.
Classified by FIRM roster (MEMBER# rows joined to PROFILE.userId) + createdBy + lastLogin +
mustChangePassword, not by email substring. Two 49F rows key as USER#usr_<id>; PKs read from the scan,
never constructed. EXCLUDED per Andrew's 09-01 rulings: 13 test/regression/demo/fixture, 2 service, 1
disabled. FORKED TO ANDREW (8): six 49F seed-script accounts with real advisor names
(createdBy=advi_rolgat_seed_test_accounts), travis.penfield (createdBy None), patricia@thewhitelabel-
creative.com (contractor, active). SES production access true, 50k/day, HEALTHY. requireMFA in
CONFIG#defaults is false AND unread by the auth handler -- there is no global switch; enforcement is
per-account (auth.ts:104).

## Findings surfaced, NOT chased

- **NEVER#7 is OFF on site Z.** never-rules-gate.sh:370 guards GATE 1's whole rebase block by
  SHARED_BRANCHES, which omits SITEZ. Exhibited by exercise: 27 rebase arms, 15 fail, the 12 that
  deny target `git -C portal` (branch DEV, shared). Same missing token leaves the SITEZ push ungated
  (0.0.0_AB_MSTR~Z 19296). {OBSERVATION, ARMED}, owner ANDREW -- a one-token fix with fabric-wide blast.
- /prod-deploy SKILL.md names GATE 5 zero times; a DT still meets the integrator denial at Step 1a
  (portal DEV push). Andrew-directed non-DT still denied on PROD.
- SF-2 fix surface for the 18907 lockout path is in PROD with ZERO consumers (MSTR~Z 19321).
- org/commit-msg-ascii-override-audit.log is audit-log-shaped but not in the archive MANIFEST (new A.2
  row; owner 0.7.0_AE_CloudOps, sequenced behind rv0057-f001).

## Corrections this seat made to its own claims

- Told Andrew AC4 was overdue; it was scored 14:42Z on 09-01 (@9da4da99cd). Read stale next-steps.
- Reported 12 suite failures; the true count is 15 (my run masked 3 behind GATE 5). MSTR~Z was right.
- Wrote in 19291 that the PROD push was outside GATE 5; retracted in 19292, source-confirmed :88.
- Invited a hold on the LEG 2 push that nobody asked for; retracted in 19298.

## Compiler Tools

- comp-read: TenantLayoutConfig, firmAccess, portal_data_proxy (--enumerate 'firm' -> 0/2444), auth.ts,
  types.ts, sms.ts, 005_backfill_mfa_defaults.py, never-rules-gate.sh, comp-schedule, safe-commit.sh.
- comp-find: cottonwood, AC4, '/factor-tilts', ALLOWED_PATHS, mfaRequired, SP-1, requireMFA.
- comp-schedule --self-test 5/5, live view, --drift.
- test_never_rules_gate.sh: baseline 71/12 -> 79/12 -> (pinned) 76/15; NRG_HOOK proven-red run.
- bun run typecheck rc=0. commit-gate on .sh files clean. aws (operational): dynamodb scan/update-item,
  describe-table, sesv2 get-account. One rail block (grep on types.ts) correctly routed to comp-read.

## Current State

- opal-users-v2: 24/48 email-MFA. 8 accounts at Andrew's fork. SMS channel: 0 phones on any row.
- portal: PROD 4b88e55e / portal-v2.1.175 served. DEV 793c17dd. Main tree on DEV.
- GATE 5 DT carve-out live (hooks bind by reading). Suite pinned.
- G-7 SMS watch armed in comp-schedule.
- Zero crons at this seat. Watcher task ba9ps95uv, parent-tied pid 49253.

## Next Steps

- **[Andrew]** the 8-account MFA fork; SITEZ in SHARED_BRANCHES; portal DEV for DT; Andrew-directed non-DT.
- **[0.4.0_DE_ClientPlatform~Z]** stale-bundle hazard for the 9; SF-2 part 2/2 (the consumer).
- **[0.7.0_AE_CloudOps~Z]** MANIFEST add for commit-msg-ascii-override-audit.log with rv0057-f001; owns G-7's
  SP-1/SP-2 legs when AWS provisioning lands.
- **[0.0.0_AB_MSTR~Z]** push of this log.
