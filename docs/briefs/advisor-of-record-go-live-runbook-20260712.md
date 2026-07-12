# Advisor-of-record go-live runbook (INF udf7ADVISOROF -> served advisor SSOT)

**Owner:** 1.0.0_SA_CTO~B. **Status:** ASSEMBLING (all pieces IN FLIGHT + INERT/HELD). **LD:** LD-0277.
**Andrew GO given (directional) 2026-07-12** with 4 decisions folded in below. This runbook makes the
activation ONE atomic, pre-verified sequence -- never an ad-hoc last-minute assembly (NEVER#5: a begun
deploy FINISHES in-session or rolls back + escalates; the peer-sweep + AOR_FOLD_ACTIVE firebreak history
is the reason this is written before, not during).

## What activates

Migrate the served Inflection advisor attribution from the servicing Representative to the Orion
`udf7ADVISOROF` (advisor-of-record) custom field as SSOT. Net served effect at go-live:
- **Noel Soderblom** surfaces as a NEW advisor (card/profile), seeded from advisor-of-record.
- **Scanlan_IWM** folds into existing **patrick_scanlan**; **Soderblom_IWM** into **noel_soderblom**.
- The whole existing group re-keys by advisor-of-record (Joe Brandenburg $19.4M-by-rep -> $29.2M-by-AoR, etc.).
- Fallback: blank advisor-of-record -> keep the servicing-rep key (no stranding).
- Household headline = **advisor-of-record WINS** over servicing plurality (Andrew override).
- Keil / DeMuth **excluded** (Andrew: not interested in those advisors) -> their 9 accts keep servicing key.

Expected served numbers (firm-CONSERVED, reconciled to MSTR's live Orion rollup):
peter ~$135.24M / joe ~$29.19M / patrick ~$24.13M / **noel NEW ~$12.42M** / IWM ~$1.34M; firm $202.3M / 871 accts unchanged.

## Preconditions -- ALL must be GREEN before the flip (none skippable)

| # | Gate | Owner | State | Verify |
|---|---|---|---|---|
| P1 | Daily fold reproduces the 164 static movers + $ numbers + firm-conserved on the 20260710 snapshot | DS | pending | static frozensets = reproduction oracle; DS proves BEFORE wiring |
| P2 | CHANGE-3 daily fold (Option A: per-process lazy self-load, marker-checked, OFF=truly-inert) wired + re-reviewed CLEAN | DS + CTO~B | pending | /code-review CLEAN; 4 invariants (see below) |
| P3 | CHANGE-2 AoR-wins household rule + guard + hh286-class negative control, re-reviewed CLEAN | DS + CTO~B | pending | /code-review CLEAN; guard non-vacuous on live SSOT |
| P4 | Pull Lambda deployed + happy-path EXERCISED (200 + real roster + fresh marker), fail-safe proven | AE | **GREEN** -- inf-pipeline-v1.7.83; all 3 fail-safe paths (fresh/carry-forward/first-run-stale) exercised live; deployed-invoke wrote fresh roster 3118 accts/900 AoR @ 13:19:39Z | Rule 22a: exercised not asserted |
| P4a | S3-write IAM grant (BronzeAccountsRosterWrite: Put/Get/Head on accounts_roster.json + marker + latest/) safe-applied + simulate-principal-policy verified WITH a positive control, + deployed-Lambda INVOKE-confirm (role+code end-to-end, not local creds) | AE | **GREEN** -- get-role-policy shows the grant live; simulate ALLOWED + positive control on new_portfolio_accounts.json; deployed-invoke = the ROLE wrote it; 0-diff | the role's s3-accounts-v2 policy is FILENAME-scoped to new_portfolio_accounts.json (verified live) -> the pull's NEW keys 403 without this; local-creds exercise MASKS it (Rule 22a-IAM) |
| P5 | LIVE end-to-end: bronze roster -> silver advisor_of_record_raw -> gold daily fold reproduces the numbers on LIVE data (not just snapshot) | DS + AE | **UNBLOCKED** -- live roster landed @ 13:19:39Z, AE pinged DS; DS runs the serve-held silver+gold code against it (no deploy needed -- deployed silver stays sentinel-skipped) | grounded against live, not asserted |
| P6 | Conformance guard INF_D_10 exercised CLEAN under the ACTIVE-switch build | DS | 21/21 under INF_AOR_FOLD_ACTIVE=1 already; re-run on final build | non-vacuous (286 SSOT households iterated) |
| P7 | FE noel card held (portal 73ee2705 + comment-hygiene b005545e), DEV | RD | DONE + HELD (branch -r contains = empty) | unpushed until this sequence |
| P8 | NEVER#2 never-widen sign-off | base CTO principal + COO + Andrew final GO | pending | firm-total conservation shown; DELTA verified |

### CHANGE-3 Option A -- the 4 hard invariants (P2 gate)
1. **OFF-switch = truly inert, ZERO new dependency** -- lib does NOT even attempt the accounts_v2 load when AOR_FOLD_ACTIVE is off.
2. **ON-switch never derives off silent-null (THE firebreak)** -- marker-checked accounts_v2 load; stale+last-good -> carry-forward + LOUD ChainStepDegraded; stale+NO-last-good -> FAIL LOUD, never serve pre-fold.
3. **load-once-per-process, source invariant to caller** -- every producer process's first apply() loads the same marker-checked accounts_v2.
4. **reproduction proof before wiring** -- P1; static frozensets retire from runtime, survive as the test oracle only.

## The coordinated deploy -- ONE atomic go (only after P1-P8 all GREEN)

**Open a deploy-completion ledger entry** in `org/critical_paths/change_management/` at deploy-START
(NEVER#5 gate); close it at completion; unclosed at session end = COO alarm.

1. **Sign-offs banked:** base CTO principal + COO never-widen co-sign + Andrew final GO (P8). Do NOT proceed on 3-of-4.
2. **DS release commit (single push):**
   - remove `# DEPLOY-SERVE-HELD` sentinels from the AOR gold/silver files WITH a `SERVE-RELEASE-ACK: <reason>` in the commit (base CTO gates this diff -- the one audited moment committed-becomes-served, by design; serve-gate d7359a797).
   - flip `AOR_FOLD_ACTIVE=1` (env/config for the INF gold runners).
   - push CLOUD `--follow-tags` -> safe-deploy serves gold to `s3://opal-data-inf/code/gold/`.
3. **DT FE promote:** reconcile portal local DEV vs origin/DEV (behind 8 / ahead 6 -- pre-existing) FIRST; then promote the Noel FE commits DEV->PROD via the ephemeral worktree (`/prod-deploy`, Rule 19; portal main tree stays on DEV). RD does NOT push; DT owns the promote.
4. **Activation happens on the NEXT scheduled nightly INF gold run** (NEVER#4: validate on the scheduled artifact, no ad-hoc gold run to "prove" it).

## Served verification (after the nightly lands -- ground against SERVED, never self-report)

- `leaderboard.json` = **5** advisors incl `noel_soderblom` (was 4, no noel).
- household 286 headlines under **Noel** (the AoR-wins negative control).
- firm total CONSERVED ($202.3M / 871); per-advisor matches the expected numbers above.
- `advisor_nna_canonical.json` NNA path consistent (INF_C_01 fold landed).
- FE: Noel card renders in ADVI portal; allowlist shows 5 entries (maxEntries 5).
- conformance guard (INF_D_10) prints OK on the served surfaces.
- **Close the deploy-completion ledger entry.**

## Rollback (if any served-verify fails -- a begun deploy finishes OR rolls back, never half-lands)

1. flip `AOR_FOLD_ACTIVE=0` + re-add the `# DEPLOY-SERVE-HELD` sentinels (commit + push -> deployed-inert/skipped).
2. DT: revert the FE promote (PROD back to pre-Noel).
3. served reverts to pre-fold (4 advisors, servicing-rep attribution) on the next nightly.
4. RED-ALERT to COO; ledger entry -> rolled-back with the failure grounding.

## Current state (2026-07-12, this runbook's write time)

DS CHANGE-3c wiring committed `223a71982` (Option A daily self-load; static frozensets retired to
test-oracle; reproduction gate PASS + it caught a real pd.NA spurious-advisor bug, fixed) -- under my
independent /code-review gate now (wty8mrgmu). AE pull DEPLOYED (inf-pipeline-v1.7.83) + fully 3-layer
verified + INERT: the nightly now lands the bronze roster daily; silver+gold stay inert (switch OFF +
the serve-gate sentinel PROVEN -- AE's push swept DS's sentineled convert and safe-deploy SKIPPED it, so
deployed silver stays 0-raw-column). DS building CHANGE-2 (AoR-wins) on 223a71982. RD FE DONE + HELD.
P4/P4a GREEN; P5 unblocked (live roster available). Nothing flips until P1-P8 GREEN + the atomic sequence above.
