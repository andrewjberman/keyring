# Deploy-Completion Ledger -- Advisor-of-Record Fold: INERT-HOLD (rollback leg)

- **Opened:** 2026-07-11T23:03Z
- **Owner:** 0.4.0_DS_ClientPlatform (INF pipeline + DS deploy owner)
- **Co-signers:** 1.0.0_SA_CTO~B (deploy route + design gate), 2.0.0_SA_COO (never-widen + finish-or-rollback)
- **Class:** ROLLBACK / hold -- restoring served output to pre-fold (NOT a forward serve). Per COO co-sign, a
  restore needs NO NEVER#2 never-widen sign-off; the FORWARD serve (go-live) does.
- **Status:** OPEN

## Trigger (what happened)

Pushing the completed advisor-of-record single-source implementation (`4a28b290b`, 2026-07-11 22:49 UTC) to
`origin/CLOUD` tripped the DS pre-push `safe-deploy` hook (Rule 13 commit->deploy), auto-deploying the whole
folded gold chain (the 4 foundation commits `51d9f93b2..ccbf38b42` + my completion) to `s3://opal-data-inf/code/gold/`.
The INF gold runner syncs code from `code/gold`, so the NEXT code-executing run would serve re-attributed
per-advisor numbers (noel surfaced, peter -~$25M) WITHOUT: the NEVER#2 never-widen sign-off, the FE noel card
(parked -> gold-alone drops Peter with $12.4M into a hidden advisor), or a CLEAN /code-review.

## Grounded facts (verified, not self-report)

- **Foundation fold WAS deployed to code/gold on Jul 10** 22:02-23:37 UTC: `INF_C_01`/`INF_B_00`/`INF_D_02b`
  (foundation-folded, untouched by my push) carry `apply_advisor_of_record_fold` in code/gold with Jul-10
  LastModified (aws-verified). This SUPERSEDES the handoff spec's "undeployed" (stale; CTO~B corrected the record).
- **SERVED output is still PRE-FOLD -> NO NEVER#2 breach yet:** `platinum/firm/leaderboard.json` LastModified
  Jul-10 14:49 UTC, data_as_of 2026-07-10, exactly 4 advisor_ids {inflection_wealth_management, joe_brandenburg,
  patrick_scanlan, peter_lee}, NO noel; served advisor book dirs = those 4 + `unknown`, no `noel_soderblom/`. The
  last nightly (14:49 UTC) ran BEFORE the code deploy, so nothing has served the fold.
- **Next code-executing run ~2026-07-12 ~15:00 UTC** (~16h): path `inf-gold-full-on-bronze-complete` (event on
  bronze-complete ~14 UTC); `inf-gold-incremental-daily` cron(0 18) is DISABLED (COO-grounded). Window, not tonight.

## Rollback mechanism (agreed: empty-overlay activation switch on CLOUD -- STABLE)

Restoring code/gold once is UNSTABLE: while the populated overlay is on origin/CLOUD, the next push by any agent
re-trips safe-deploy and re-deploys the movers. So the hold lives ON CLOUD: `lib/inflection_rep_scope.py` gains an
`AOR_FOLD_ACTIVE` switch (`os.environ.get('INF_AOR_FOLD_ACTIVE','0')=='1'`), default **OFF**, gating assembly of
`ADVISOR_OF_RECORD_FOLD`. OFF -> overlay `{}` -> every `apply_advisor_of_record_fold()` no-op -> producers emit
PRE-FOLD attribution -> every future safe-deploy inert. The 164 mover frozensets are PRESERVED (go-live = flip the
one flag). Verified locally: OFF -> 0 movers, `INF_AOR_FOLD_ACTIVE=1` -> 164 movers.

## Completion checklist (close ONLY when all verified)

- [x] Ledger opened before touching code/gold (this entry).
- [ ] Empty-overlay switch committed to CLOUD + pushed (deploys inert lib to code/gold).
- [ ] VERIFY (Rule 22, grounded aws): re-read `code/gold/lib/inflection_rep_scope.py` shows the switch; dry-run the
      fold with env unset = 0 movers; pre-fold per-advisor numbers (peter 626/$160.6M, noel absent).
- [ ] Confirm the conformance guard stays advisory (does not hard-fail on an empty-noel artifact).
- [ ] COO sign-off (never-widen + finish-or-rollback) recorded.
- [ ] Close.

## Forward path (separate gate -- NOT this ledger)

Finish the refactor with the overlay EMPTY on CLOUD (Phase 1-3 deploys stay inert). GO-LIVE = re-populate (flip
`INF_AOR_FOLD_ACTIVE=1`) + CLEAN /code-review + NEVER#2 never-widen sign-off (base CTO + COO + Andrew, CTO~B carries)
+ FE noel card, ALL in ONE coordinated deploy. Follow-up (COO, non-blocking): the pre-push hook auto-deploying gold
CODE on a normal push conflates "committed" with "cleared-to-serve" -- a safe-deploy-hook design finding for CTO.
