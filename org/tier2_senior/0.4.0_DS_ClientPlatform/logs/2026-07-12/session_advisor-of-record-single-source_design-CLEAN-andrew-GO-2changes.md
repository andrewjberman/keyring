# Advisor-of-Record Single-Source Refactor — DESIGN to code-review CLEAN, then Andrew GO + 2 required changes — 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE

**Date:** 2026-07-12
**Task Order:** ADVI advisor-of-record single-source refactor (Andrew-direct 2026-07-11, LD-0277); handoff spec `docs/briefs/advisor-of-record-single-source-refactor-handoff-20260711.md` @ 484400d14
**Status:** IN PROGRESS (implementation code-review CLEAN + held inert; two Andrew-required changes now planned, daily-first, not yet coded)

---

## Objective

Re-key served Inflection advisor attribution from the servicing rep to the Orion `udf7ADVISOROF` advisor-of-record SSOT (surface noel_soderblom as a NEW first-class advisor + fold the whole existing group; firm total CONSERVED). Mandate: DESIGN the single-source resolver+placement FIRST -> CTO~B review BEFORE coding -> gated activation. INF-only (clear of 49F/bd/cot). "Fully-correct is the bar."

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-surface-check | auto in safe-commit (b8221c7f2) | PASS | "OK: 3 changed file(s) touch no critical surface" -- lib/tests only, no SEV1 surface |
| AoR conformance guard (Pillar C) | `INF_D_10.aor_conformance.py --mode advisory` vs live opal-data-inf | PASS | "OK: all served surfaces agree with account_team (SSOT)"; 286 households iterated, 0 findings (non-vacuous) |

**What worked:** the domain conformance guard (INF_D_10, the Pillar C build) is the load-bearing verifier -- it grounds "0 findings" against SERVED surfaces + account_team non-vacuously (286 households), which is what let me report CLEAN with evidence rather than trust.
**What failed:** none this window.
**Gap found:** none new. NOTE (role-minimum honesty): `comp-pipescript io`/`comp-blast` on the gold IO contract belong to the CHANGE-3 gold implementation, which is DESIGN-phase (not yet coded) -- they ride the CHANGE-3 build, not this design/diagnostic window. The MECHANICAL comp checks over the round-1..4 gold edits were run in the prior session windows (see 2026-07-10/-09 logs).

---

## Work Completed

### 1. DESIGN (single-source architecture) -> CTO~B RAVC (6ee0fd100)
`docs/briefs/advisor-of-record-single-source-resolver-DESIGN-20260711.md`: SSOT = account_team (INF_C_07) + AoR overlay; TWO grain-aware accessors -- account-grain `apply_advisor_of_record_fold` + household-grain `resolve_household_advisor` (individual-plurality); a conformance guard (Pillar C) making per-advisor consistency a BUILD GATE. §11 grain taxonomy (account-grain vs household-grain legitimately differ for split households; guard checks WITHIN grain only). This converged where 3 prior producer-by-producer rounds could not.

### 2. Implementation P1-3 + inert-hold containment (4a28b290b, 16075dd53, e16c101c1, 6f75feaa5, b4d5d1845)
Impl of SSOT + 2 accessors + guard. Contained the deploy hazard: the DS pre-push safe-deploy hook auto-deploys gold code on ANY peer's CLOUD push, so a static "hold the push" is unenforceable on a shared branch. Real hold = the `INF_AOR_FOLD_ACTIVE` activation switch (`inflection_rep_scope.py:186`, default env '0'): OFF -> overlay {} -> fold no-op -> every producer emits PRE-FOLD servicing attribution -> every deploy INERT. Inert-hold rollback ledger OPENED, VERIFIED (deployed movers=0, grounded on live aws), and CLOSED co-verified with COO+CTO~B.

### 3. Four code-review rounds to CLEAN (dba679a59, 5fe871870, 2cf5c1e4e, abbdc5d02, b8221c7f2)
Converged 8->10->4->4->CLEAN. Final round (b8221c7f2) landed CTO~B's hard predicate: `assert_fold_landed` rewritten to his EXACT 6-way truth table (`inflection_rep_scope.py:235-280`) -- RAISE only on {col-missing:256, all-non-numeric:267, movers-present-unfolded:272}; WARN on {empty:261, no-movers:277}; RETURN on {n>0/inactive:252}. 6 per-row controls (`test_afl_row1..row6`). Test suite: per-test forced state (`_with_fold_state`) + `_run_all` catches Exception -> 21/21 under BOTH switch states incl `INF_AOR_FOLD_ACTIVE=1` (the go-live validation env, was crashing 2/16 = F2). B2: `compare_household_headlines` iterates the SSOT households (`advisor_of_record_conformance.py:191`) -> HOUSEHOLD-MISSING (population shrink) + HOUSEHOLD-HEADLINE-DIVERGENCE + HOUSEHOLD-GRAIN-UNVERIFIABLE (blocks vacuous pass). CTO~B verdict (20260712T021910Z): "b8221c7f2 is CLEAN -- code-review gate MET" (verified branch-by-branch vs his spec).

### 4. Andrew GO + 2 REQUIRED changes (relayed via CTO~B 20260712T114816Z)
Andrew GO'd activation DIRECTION but overrode two things I built; both required before flip; daily-FIRST; switch STAYS OFF until a fresh go-live GO.
- **CHANGE 2 -- household headline = ADVISOR-OF-RECORD ALWAYS WINS** (replaces my plurality->max_aua->lexical). Andrew verbatim: "advisor of record always wins." An explicit AoR designation overrides servicing-rep-derived plurality.
- **CHANGE 3 -- udf7ADVISOROF in the DAILY ETL** (Andrew: "condition of it being done, absolutely has to be daily not just a snapshot"). Replace the static 164-mover frozenset with a data-driven daily fold: pull (AE) -> silver raw passthrough -> gold dynamic fold. My DESIGN S8 durable path, now REQUIRED.

### 5. CHANGE-2 diagnostic (grounded, dry-run, CLOUD OFF) -- scratchpad, uncommitted
Applied the 164-mover overlay in-memory (`INF_AOR_FOLD_ACTIVE=1` forced in a scratch script; CLOUD unchanged) to the served pre-fold `account_team` (gold/views/account_team.parquet, 871 rows / 293 households):
- **N1 genuine multi-AoR-split (movers -> >=2 distinct AoR owners) = 0** -> the AoR-wins rule is UNAMBIGUOUS today; CTO~B's disambiguation tie-break never fires on current data.
- **N2 headline MOVES vs old plurality = 1** -> household 286 (5 accts, 1 mover, peter_lee -> noel_soderblom) = exactly CTO~B's specified negative-control.
- **N3 accounts span >=2 AoR owners = 2** (grain-split, already taxonomy-acknowledged).
- **Design finding:** N1=0 is a PROXY off the frozenset. "AoR wins" needs the per-account EXPLICIT-AoR signal (udf7 non-blank); the frozenset encodes only MOVERS (AoR!=servicing) and cannot represent explicit-AoR-that-equals-servicing, so it can UNDERCOUNT a true 2-owner split. Correct total signal = CHANGE 3. Concrete mechanism reason CTO~B's daily-first sequencing is right.

### 6. CHANGE-3 canonicalization domain (grounded in local roster snapshot -- NO vendor call)
From `data/inf/manual_api/pulls/20260710_accounts_roster.json` (a local already-pulled file; 3113 firm accounts), distinct `udf7ADVISOROF`: `<blank>` 2213 | Peter Lee 502 | Joe Brandenburg 154 | Scanlan_IWM 87 | Patrick Scanlan 84 | Noel Soderblom 45 | Soderblom_IWM 19 | Jeremy Keil 8 | Tim DeMuth 1. Complete map (no silent Unknown): the *_IWM aliases need an explicit ALIAS map (slug-normalize alone gives 'scanlan_iwm', not patrick_scanlan). Keil/DeMuth carry explicit values but the current design treats them as no-AoR -> business call (Q1).

### 7. Design-first PLAN + 4 gating questions sent to CTO~B (20260712T115553Z)
Full sequenced build (CHANGE 3 foundation -> CHANGE 2 on its per-account signal), the AE/DS ownership split (AE owns the pull; silver+gold+guard+verify are DS/me), and Q1 (Keil/DeMuth), Q2 (M = udf7-non-blank not "movers"), Q3 (hh286 confirm), Q4 (pull ownership boundary). Holding at inert; code only after CTO~B ratifies.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Activation switch (`INF_AOR_FOLD_ACTIVE`) as the real hold, not "hold the push" | Shared-branch safe-deploy hook auto-deploys on any peer push; only neutralizing the overlay on CLOUD keeps re-attributed numbers off the served path (structurally stable). |
| CHANGE 3 (daily) BEFORE CHANGE 2 (headline) | AoR-wins needs the per-account explicit-AoR signal (udf7 non-blank), which only the daily udf7ADVISOROF provides; the frozenset can undercount a true split. Mechanism, not just cleanliness. |
| Build silver/gold against the LOCAL roster snapshot in parallel with AE's pull | The snapshot carries real udf7 values -> I can build+unit-test canonicalization/fold with NO new vendor call while AE wires the recurring pull. |
| I never probe Orion; AE owns the pull | Vendor egress boundary. Andrew has now GIVEN the /Portfolio/Accounts vendor word + AE integrating into existing ingestion -> endpoint resolved, Q4 answered. |

---

## Files Modified

See commit messages for per-file detail: `6ee0fd100` (design doc), `4a28b290b` (impl), `dba679a59`/`5fe871870`/`2cf5c1e4e`/`abbdc5d02`/`b8221c7f2` (review rounds), `16075dd53`/`e16c101c1`/`6f75feaa5`/`b4d5d1845` (inert-hold ledger legs). Key files: `data/inf/scripts/gold/lib/inflection_rep_scope.py` (switch + overlay + `apply_advisor_of_record_fold` + `assert_fold_landed` + `resolve_household_advisor`), `.../lib/advisor_of_record_conformance.py` (Pillar C guard), `.../tests/test_advisor_of_record_conformance.py` (21 tests), `.../INF_C_07.advisor_attribution.py`, `.../INF_D_10.aor_conformance.py`, `.../INF_D_00d.cumulative_chart.py`, `.../INF_D_02c.client_directory.py`, `.../INF_C_02.client_performance.py`, `.../INF_D_04.client_portal_summary.py`, `.../orion-gold-dispatch.sh`, `.../INF_run_c_chain.py`. CHANGE-2 diagnostic: `scratchpad/aor_split_diag.py` (uncommitted, dry-run).

---

## Blockers

None assumption-blocked. Open dependencies (all in flight, evidence-cited):
- CHANGE-2 semantics gated on CTO~B ratifying Q1-Q3 (message 20260712T115553Z, in his inbox) before I finalize `resolve_household_advisor` + `compare_household_headlines`.
- CHANGE-3(a) pull owned by [AE] (MSTR spawning per CTO~B 20260712T114816Z); Andrew GAVE the /Portfolio/Accounts vendor word (CTO~B 20260712T115507Z) -> endpoint authorized, AE integrating. I hand AE the field + silver contract; not blocked on it for silver/gold build (I build against the roster snapshot).
- ACTIVATION gated on both changes re-reviewed CLEAN + NEVER#2 never-widen sign-off (base-CTO+COO+Andrew) + FE noel card. Switch stays OFF; I flip ONLY on CTO~B's relay of the go-live GO.

---

## Current State

> Primary handoff point.

The advisor-of-record single-source implementation (`b8221c7f2`, on origin/CLOUD via peer-push-sweep, DEPLOYED-INERT) is code-review CLEAN per CTO~B (gate MET). Everything is held INERT: `INF_AOR_FOLD_ACTIVE` defaults '0' (`inflection_rep_scope.py:186`) -> overlay {} -> fold no-op -> served surfaces on opal-data-inf remain PRE-FOLD/safe (peter 626/$160.6M, noel absent). Andrew has GO'd the direction with two REQUIRED changes: CHANGE 2 (household headline = advisor-of-record-always-wins, replacing plurality; diagnostic shows this moves exactly 1 household today -- hh 286 peter->noel -- and is unambiguous, N1=0) and CHANGE 3 (make the fold data-driven from a DAILY udf7ADVISOROF pull, replacing the static 164-mover frozenset). Sequencing is daily-FIRST: build CHANGE 3 (AE owns the Orion pull, vendor word GIVEN; DS/me owns silver raw passthrough into accounts_v2 + gold dynamic fold + verify) then CHANGE 2 on its per-account explicit-AoR signal, re-review each to CLEAN, then ONE coordinated activation on the daily mechanism. A design-first PLAN + 4 gating questions are with CTO~B (20260712T115553Z). Nothing flips until his relay of the fresh go-live GO + never-widen sign-off. Inbox Monitor live (pid 1864542); no cron armed.

---

## Next Steps

1. **[1.0.0_SA_CTO~B] Ratify Q1-Q4** — Keil/DeMuth business call, M=udf7-non-blank confirm, hh286 confirm, pull-ownership boundary. Gates my CHANGE-2 coding.
2. **[0.4.0_DS_ClientPlatform / me] Build CHANGE-3(b/c) against the roster snapshot** — silver `udf7ADVISOROF` raw passthrough into accounts_v2 (convert_orion_api_to_silver keep-map, Rule-17 OK) + gold ALIAS-canonicalize + dynamic-mover fold replacing the frozenset; unit-test vs the snapshot (no vendor call). Verify it reproduces peter ~$135M/joe ~$29.2M/patrick ~$24.1M/noel ~$12.4M + firm-conserved.
3. **[AE] Wire udf7ADVISOROF into the recurring /Portfolio/Accounts ingestion** — vendor word GIVEN; I hand AE the exact field + silver contract. AE flags any new-endpoint need to CTO~B.
4. **[0.4.0_DS_ClientPlatform / me] CHANGE 2** — rewrite `resolve_household_advisor` + `compare_household_headlines` to AoR-wins + negative control (hh286-class); re-run N1/N2/N3 on daily data; re-verify guard clean + non-vacuous. Bring each to CTO~B's review loop.
5. **[1.0.0_SA_CTO~B] Relay the go-live GO** — on both changes CLEAN + NEVER#2 sign-off; I then activate as ONE coordinated deploy (open+close deploy-completion ledger in-session, NEVER#6).
