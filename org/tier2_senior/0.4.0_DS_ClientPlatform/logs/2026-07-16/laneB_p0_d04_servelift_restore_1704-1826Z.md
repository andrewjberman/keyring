# The Restore That Never Fired: D_04's Jul-9 Header Cured 11/11 at the Artifact Level — 0.4.0_DS_ClientPlatform~B

**archetype:** MIXED (DIAGNOSE -> DEPLOY -> VALIDATE)
**Date:** 2026-07-16 (17:04Z–18:26Z)
**Task Order:** ad-hoc P0 (Andrew-direct instantiation ~17:0xZ, relayed 0.6.2 170320Z: "fixed within this session and validated at the portal artifact level")
**Status:** COMPLETE — CTO gate CLOSED 182432Z

---

## Objective

PartnerAnalytics served "as of Jul 9, 2026" while every sibling number on the page was current: INF_D_04
stranded 4 trading days (11 artifacts, atomic, since 07-10T14:51Z). Fix this session; validate at the
portal artifact level.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript deployed | `deployed INF_D_04.client_portal_summary.py` | FAIL | swept bd only, printed sovereign-hold SKIP (stale gate — block lifted 07-14), matched nothing for inf even with COMP_PIPESCRIPT_INCLUDE_HELD=1; fell back to rail-checked boto3 full-body GET compares |
| comp-pipescript io | `io INF_D_04.client_portal_summary.py` | PARTIAL | 13 READS / 11 WRITES enumerated with portal consumers — but WRITES glob `partner_analytics_{*}` over-matched INF_09's base `partner_analytics.json`; symmetric to the READS referenced-not-required bite 0.6.2 hit |
| comp-which rail | rail-checked markers on 9 raw inspections | PASS | every raw boto3/aws inspection carried `# rail-checked:` with the specific gap |

**What worked:** `comp-pipescript io`'s portal-consumers section grounded the blast radius in one call.
**What failed:** `comp-pipescript deployed` has no working inf-tree filter path this session (bd-only sweep + stale sovereign-hold gate) — deploy-verify done by full-body GET compare instead.
**Gap found:** io manifest WRITES are glob-matched-not-owned (miss #1 of the validation); a script census must come from the DISPATCHER's chain IDs, never manifest globs. Carried by 0.6.2 to the marker-census cell.

Appended one line to org/compiler-tools-log.md.

---

## Work Completed

### 1. Fork resolved at source: (b) NEVER DISPATCHED — deliberately
0.6.2's brief (97e9fb72b) left fork (a) runs-and-raises vs (b) never-dispatched. Resolved three ways, all
agreeing: (i) main()-order analysis — the suspect AoR guard sits at Step 4 AFTER three writes, so a raise
there cannot produce the observed all-11 atomic strand; (ii) live account_team.parquet carries the stamped
column (870/874) so all three raise paths were dead anyway; (iii) the dispatcher's own chain literals
exclude INF_D_02c/INF_D_04/INF_09 — the GLDRNS.B1 window exclusion (CTO ruling 194d3d674, landed
d9e74e097 by this lane's prior session) whose restore clause ("at the migrated-vintage serve-lift bundle")
never fired when the window completed. CTO independently read the 13:47Z nightly log (line 112) and
confirmed. The AoR raise hypothesis is dead as proximate cause.

### 2. Serve-lift restore executed under CTO's four-step ruling + NEVER#4 ruling (172125Z)
- Condition verified at source: all three scripts consumer-migrated (D_04 @ 8bd1d1b62 :62/:3348; D_02c @
  dbd10d7aa :61/:180; INF_09 @ 5581c0de1 :73/:406), zero live resolve_household_advisor calls, py_compile
  3/3, libs deployed==repo 5/5.
- Restore committed `1ca265e6d`: trio re-added to CHAIN_COMPUTE/INCREMENTAL/GOLD_D, literals byte-match
  pre-exclusion originals (diffed vs d9e74e097^); comment blocks flipped to restore records.
- Rule-13 deploy 17:32Z: dispatcher + 3 scripts to code/gold/, 4/4 verified full-body GET compare.
- Pushed origin/CLOUD 0a4fed471 (single work-package push).

### 3. Three ruled supervised singles; pre-registered deltas; every claim on the SERVED object
| Dispatch | SSM | Result |
|---|---|---|
| `--single INF_D_04` 17:44:48Z | 5141a028 | rc=0 25.3s; 10 surfaces rewritten; data_as_of 07-09→**07-15** == siblings, page-consistent; attribution == C_07 stamp (patrick exact-to-the-cent) |
| `--single INF_D_02c` 18:07:19Z | d190a477 | rc=0 1.2s; client_directory rewritten; snapshot_date=07-16 == accounts_v2 frontier; 296 HH, 5/5 advisors |
| `--single INF_09` bare shell 18:11:17Z | 7b904298 | **FAILED-CLOSED exit=1, ZERO writes** — fold-mode chokepoint refused (parquet stamped ACTIVE, shell presented OFF). The guard's exercised-RED, on the record |
| `--single INF_09` w/ INF_AOR_FOLD_ACTIVE=1 18:20:48Z | f08640e9 | rc=0 9.9s; base partner_analytics rewritten; mode accepted + fold path consistent (movers-only re-key 0 = post-stamp steady state) |

Negative controls after EVERY dispatch: gold/meta sentinels (complete/failed/pull) + dispatch-lock at
pre-dispatch mtimes; --single writes no sentinel (pre-verified at :1874-76 before firing). Door 6 never
touched. Zero unruled retries.

### 4. Validation misses that were MINE, characterized instead of iterated (condition e)
4 of 32 registered checks missed; all four grounded as registration/census artifacts: (1) base
partner_analytics.json is INF_09's single write (docstring + f-string cited), not D_04's — my census
over-expansion; (2-4) as_of_by_dim.nna=07-14 is the pipeline's historical normal (identical
one-trading-day offset in the healthy 07-10 before-state) — my registered numeral was wrong. Also caught
CTO's own (b)-condition error BEFORE dispatch: his "data_as_of → 07-16" was wall-clock; the measured
sibling vintage is 07-15 (T-1, NEVER#1). Amended at his gate, accepted verbatim.

### 5. Convention items banked (future-pass cell, not tonight)
(1) INF_09 carries zero `orion_normalize_as_of` refs — the 07-02 label normalization reached D_04, never
INF_09 (its data_as_of sits one day forward of normalized siblings; label, not data). (2) Recovery singles
on mode-stamped consumers must carry the trigger env (lambdas.tf:107 exports INF_AOR_FOLD_ACTIVE=1) —
complete exhibit tonight. (3) advisor summary.json data_as_of inherited verbatim from D_02 book.json.

### 6. Side items
- Committed 0.7.0's three eclipse-catalog pointer banners under my author @ `b06048dd5` (owned-paths
  routing, links verified resolving).
- Deploy-completion ledger opened+closed all-legs-proven:
  `org/critical_paths/change_management/20260716T1825Z_inf-d04-servelift-restore_deploy_completion.md`.
- 0.6.2 corrected their brief's "1:1" claim on my finding (coincidence-of-counts; stranded set = the
  excluded trio's union) — their correction message is the record.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Hold code until the (a)/(b) discriminator | Two candidates were different fixes; S3 cannot separate them; editing correct code was the live risk |
| Amend CTO's pre-registered 07-16 to measured 07-15 at his gate, not at the keyboard | Registering his literal would have manufactured a false (e)-STOP; T-1 law; his condition, his amendment |
| STOP at 4 validation misses; characterize, then route | Condition (e); all four proved to be my registration artifacts — iterating would have hidden that |
| --single INF_D_04 over --from slice | --from re-runs the already-fresh tail; minimal blast honors "ONE dispatch" |
| No INF_09 re-dispatch without CTO's word | A re-dispatch is a retry under (c) even when the mechanism is understood |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| data/inf/scripts/gold/orion-gold-dispatch.sh | trio restored to 3 chain literals + restore-record comments | 1ca265e6d (pushed) |
| data/inf/API/{AUTHENTICATION,domains/eclipse/{DOMAIN,endpoints/README}}.md | 0.7.0-authored pointer banners | b06048dd5 (pushed) |
| org/critical_paths/change_management/20260716T1825Z_inf-d04-servelift-restore_deploy_completion.md | ledger open→closed | this batch |
| s3://opal-data-inf/code/gold/{orion-gold-dispatch.sh, INF_D_04, INF_D_02c, INF_09} | migrated-vintage deploy | 4/4 GET-verified |

---

## Blockers

None. P0 closed at CTO's gate 182432Z.

## Next Steps

- **[me]** Eclipse _history GO (CTO 164833Z, five conditions) — unblocked, next package this session.
- **[1.0.0_SA_CTO]** Nightly #2 (07-17 13:47Z) revalidates the trio under the trigger's own env — his read, INF_09's leg specifically.
- **[1.0.0_SA_CTO]** Future-pass cell post-nightly-#2: INF_09 normalize gap · trigger-env runbook line · D_02 book.json inheritance · marker-census fix (chain:"full" cannot enumerate its run set; git_sha:"unknown").
- **[0.6.2_AE_PartnerETL]** Brief correction commit (their record).
