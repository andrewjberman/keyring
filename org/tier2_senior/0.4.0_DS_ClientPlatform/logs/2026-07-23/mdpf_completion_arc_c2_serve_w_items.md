# MDPF completion arc -- C2 definition, 4-channel contracts, all-firms SERVE, W-2b/W-6/W-7 (1410Z-2100Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE, VALIDATE

## Window

Since d93e078b9 (~1410Z, "Global serve arc banked at the Andrew-definition gate") -> 2026-07-23 ~2100Z.
17 commits (a6e472cf6 .. b607758a4), ~35 MCP messages handled, 3 publish events (6-key serve + 2
re-emits), 1 deploy-completion ledger opened+closed, ~10 Andrew-direct rulings executed.

## What happened (the arc, compressed)

1. **The 49-source definition closed to spec.** Candidate table from the 08242234 silver ->
   Andrew ruled C2 (full envelope, cash in). Decisive grounding: legacy $1,644,993,954.34 =
   positions-ex-CASH valued on the 07-15-STALLED legacy silver (tie to the cent on legacy rps
   AND canonical dim_position at 2026-07-15); D-2's "~40% of cash leg" retracted as a date-axis
   artifact. Landed @9bd23d904 + spec docs @ec7cf1159.
2. **Four channel derivation contracts + D1 handed to 0.7.0** (49F/INF/COT/Global; measured
   depths: orion 2020-04-28 zero-gap, eclipse launch 2026-05-15 + 6 named gaps, COT run-time-
   enumerated). D1 bound = ABSOLUTE REALITY (@47b9992c2). Item-9 = 5-core aggregate confirmed;
   INF launch-seam 3-day expected-delta named in advance.
3. **Smartx crux + variance overlay + convergence-why** (Andrew dispatches): model history
   reproducible to inception (settled history 0 restatements); the displaying legacy understates
   deep history up to +41.5%, collapsing at its own method boundaries (overlay @720433fb3);
   mechanism = monthly-statement roll-forward information lag (SMARTX_BIBLE/CANONICAL_DATA_LOGIC
   grounded, decomposed ~3pts staleness + ~10pts unreported-cohort).
4. **NNA excusals on raw vendor facts.** Andrew challenged "how do you know they left" -> pulled
   the FULL orion roster (GET /Portfolio/Accounts): explicit cancelDate 2026-07-08 (Saarinen x3,
   single edit action) / 2026-07-14 (609). All four excusals vendor-record-grounded @8ba56144e.
   INF_C_01 unblocks at tomorrow 1347Z.
5. **Production scripts per Andrew's schedulable-by-construction order** @e32613db0:
   stage_mdpf_revamp_trio.py + verify_mdpf_revamp_conditions.py -- exercised incl. negative
   control (rc=2) before first use; they then ran the real serve legs 3x tonight.
6. **ALL-FIRMS SERVE FIRED + PUBLISHED** (CTO 184804Z on COO counter-sign 184724Z): 6 keys
   opal-data-portal-v2, per-key staged-md5==served-ETag, ledger opened-at-fire closed-at-publish
   @5b4b6964f. Global measured frontier $1,951,676,164.42 (cottonwood=measured after the band
   extension; the $124M frontier-absence question grounded as the designed band-coverage rule,
   fixed UPWARD through the production path). Count meta made self-describing @c29fbc7b2.
7. **Convention PRD (@e1d525341, CTO) work items landed same-night:** W-2b three-quantity
   convention in the COT artifacts (frontier total ~~$458,189,558.77~~ **[SUPERSEDED
   2026-08-03 @387fa87c90: KNOWN-WRONG as an anchor -- naive relationship-grain
   double-count +$205,070.77; collapsed truth $457,984,488.00; both tie legs shared the
   derivation]** / model $124,376,009.73 /
   non_model $333,813,549.04 all MEASURED, identity 0 violations, provenance-inheriting balance)
   @bb3267fa5; W-6 bell-curve (the fold was IN the numbers -- under-telling meta, third instance;
   in-band cottonwood_fold marker + republish to the DE-pinned legacy key, pre-overwrite bytes
   audited) @34e38a8e5; W-7 count choppiness (client-side sum over mixed-None cells fabricating
   partials 0/94/255; producer-composed account_count_total + count_provenance, 407 valued/40
   honest-None, zero partials) @b607758a4.
8. **W-7 bonus catch, live:** the cross-axis gate REFUSED the first re-stage -- correctly. The
   self-referential rolling carry (count import reads our own published artifact post-cutover)
   let the frontier stamp advance the re-derived count_coverage_end past the served-real end.
   Fix at mechanism: declared cce carries via the served meta (added for DE hours earlier,
   became load-bearing same night); stamp date excluded from fallback max.
9. **Also delivered:** firm-isolation design exploration (@041f72323: today = one shared auth
   path, isolation UI-only; scoped-router precedent; 4 options rec A-then-C; /json-tiered
   NO-AUTH flag to CTO~B; 3 Andrew flags), generation-contracts preamble (@077c06738),
   validation-scope principle banked to memory (serve window 2024-11+, coverage checks over
   archaeology), certification two-limb relation for the staged-vs-DDB layers.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-routes | behaviors | PASS | grounded the serving path for the isolation design; found the scoped-router precedent + the /json-tiered no-auth behavior |
| comp-grep/comp-glob | ~6 calls (schwab_canonical, accounts_v2, SMARTX_BIBLE, WS-E, bdmp, partner_custody_total) | PASS | producer/formula grounding throughout the C2 + convergence arcs |
| comp-validate | build_cottonwood_mdpf_pair | FAIL (coverage) | tree registry hardcoded BD/INF/COT -- mdpf/assets producers invisible; flagged to CTO, RULED no-extension (bridge validated by heavier co-sign machinery); class banked to the ~Z frozen-enumeration sweep |

What worked: comp-routes gave the whole serving topology in one call. Gap found: comp-validate
tree registry (ruled, not fixed -- generator-era remediation).

## Briefs Written (DS)

| Deliverable | Path |
|---|---|
| C2 spec + D-2 retraction | deliverables/MODELPORTFOLIOS_GLOBAL_VIEW_BASIS_DEFINITIONS_20260723.md |
| SmartX variance overlay (re-runnable) | deliverables/smartx_backfill_variance_overlay_20260723.py |
| NNA excusals evidence sweep (re-runnable) | deliverables/nna_excusals_evidence_sweep_20260723.py |
| Generation-contracts preamble | deliverables/MDPF_GENERATION_CONTRACTS_PREAMBLE_20260723.md |
| Firm-isolation design exploration | deliverables/MDPF_FIRM_ACCESS_ISOLATION_DESIGN_20260723.md |
| 4 channel contracts + D1 + amendments | MCP messages 160023Z/160530Z/160926Z/162649Z/164113Z (contract text in fabric record) |

## Blockers

None BLOCKED on my side. Held-on-others (evidence-cited, not assumption): DE W-3b/W-7 render
wiring (v2.1.147 or next head) is the only distance to Andrew's three on-screen items; the
13:00Z-tomorrow smartx-Lambda clobber of json/portfolios/account-distribution.json needs an
owner (flagged 200514Z to COO/CTO/0.7.0, rec = DE re-point, stopgap = Step-4 write skip).

## Current State (zero-context handoff)

- SERVED (opal-data-portal-v2): json/mdpf/aggregate-aua-timeseries.json md5 55a8b379... (Global,
  measured frontier $1,951,676,164.42, account_count_total+count_provenance present);
  json/mdpf/{49financial,inflection,cottonwood}/aggregate-aua-timeseries.json;
  json/portfolios/aum-metrics.json; account-distribution on BOTH json/mdpf/global/ and
  json/portfolios/ keys (identical bytes md5 14d668ef..., cottonwood_fold marker present).
  Pre-W6 legacy distribution bytes audited at gold/mdpf_revamp/_audit/.
- STAGED == SERVED for every key (opal-data-assets gold/mdpf_revamp/*).
- DDB opal-assets-daily-aua @v0.33.0: 4-channel canonical base landed by 0.7.0 (C2 custody 541
  ties, COT cohorts consume my re-staged artifacts, measured-only law). Two-limb certification
  relation staged-vs-DDB verified (equality on measured/absent; band dates differ by exactly the
  band estimate -- designed).
- PRODUCTION SCRIPTS (data/mdpf/scripts/gold/): stage_mdpf_revamp_trio.py,
  verify_mdpf_revamp_conditions.py (conditions i-vi incl. W-7 no-partial-total), mutants
  tests/test_global_fold_flag2.py 8/8. Cron-ready; scheduling = config per Andrew.
- Excusals: lib/nna_coverage_excusals.json carries 237/609/560/703/1225 all vendor-grounded.
- HEAD @b607758a4 pushed. Serve chain state: DE render wiring -> DT DEV cfb0afb7+ -> PROD
  promote -> COO live-confirm.

## Next Steps

1. [0.4.0_DE_ClientPlatform] W-3b + W-7 render wiring against the field contracts (202608Z,
   205812Z); spot pins provided for render evidence.
2. [0.7.0_AE_CloudOps or 0.4.0_DE] OWN the 13:00Z smartx-Lambda Step-4 clobber before tomorrow
   morning (my 200514Z rec).
3. [0.4.0_DS] 07-24 ~02:10Z: verify the mdpf nightly ran the NEW 6d block (MEMORY.md trigger);
   1347Z: confirm INF_C_01 clears on the excusals.
4. [0.4.0_DS] W-1 canonical-form assessment + W-5 convention record on COO's formal TOs;
   generation contracts on DE's read-surface enumeration.
5. [2.0.0_SA_COO] Andrew's three isolation-design one-liners (identity source / portal-vs-
   delivery / aggregate-Opal-only) when bandwidth.
