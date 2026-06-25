# CTO Session Log -- LD-0208 comp-which routing fix (closed) + ADVI_BDAPIMIG P0 PRD/auth-ruling + ASTN reconciles

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, DIAGNOSE

**Serial:** 1.0.0_SA_CTO | **Window:** since 2026-06-18 (session_comptool_rails...) -> 2026-06-25 ~1325Z | **Tier:** tier1_exec

## Summary

Synchronized morning bring-up (MSTR/COO/CVO/AE~C all booting). Three arcs: (1) **LD-0208 comp-which
routing fix CLOSED** -- the Andrew-commissioned, CTO-chartered prerequisite to the whole NFRA_COMPRAIL
enforce-ramp; router went from ~8/36 to all 28 routable tools, MSTR-verified+resolved. (2) **ADVI_BDAPIMIG
P0** -- authored the PRD + the auth-strategy ruling for migrating 49F BD off the dead browser-scrape onto
the proven cot DataMining REST flow (Andrew-direct, off CVO's intake brief). (3) **ASTN_WSJFT ground-truth
reconciles x2** (stale Phase-0 -> deployed-v0.3.0, then -> go-live). Plus TO-6 LEG-A scope reconciliation
(Gate-2 superseded). 8 commits, all pushed.

## Work done (newest-first, by arc)

1. **ADVI_BDAPIMIG P0 PRD + auth ruling** (0ee2e8b8d) -- Andrew-direct off CVO's intake brief (7f62e24d8).
   49F BD bronze dark since 06-19 (SS&C email-OTP MFA killed the headless Playwright scrape -> 4 silver
   tables frozen -> served 49F AUA stale 6d). RULING: migrate to the PROVEN cot DataMining REST flow
   (cot_bronze_ingest.py, Model-B firm-parameterized -> identical forwardfill_v2 seam = silver+gold ZERO
   change). Auth crux ruled: Option-D (REST, proven) + Phase-0 Option-B manual post-MFA cookie + a
   bd_DeviceRegistration **device-trust probe** that DECIDES steady-state (B if it durably skips MFA, else
   Option-A vendor-exempt primary / Option-C OTP-automation fallback); Option-A in parallel. Added 3
   guardrails: firm-separation (no bd->cot bucket cross-ref in the shared-code port), backfill Custom-window
   complete-days-only + holdings floor (COTETL lessons), per-table absence alarm EGRESS-verified. Registered
   (JSON + REGISTRY). Routed: CVO (ruling/RAVC close + Andrew cookie surface), COO (Phase-0 decomposition).
2. **LD-0208 comp-which routing fix** (05235149c core + 28e0e9e55 residuals) -- defects: (A) _manifest_matches
   read `use_cases` but the manifest stores `entries` -> backstop matched NOTHING -> ~28 tools unreachable;
   (B) the grep primitive ran before the backstop was consulted. Fixed A (key), B (backstop-before-grep,
   MF_STRONG=3 strictly-beats-curated, search-verbs still run the primitive), C (curated rules for
   freshness/validate/pii + comp-platinum/comp-xref + dropped bare "scoped"), D (committed regression guard
   .tools/comp-which-routing-test.py = MSTR's end-to-end self-routing oracle). MSTR coverage-probe deconflict
   handled live (took ownership, corrected a b888c81ea->05235149c attribution; reconciled the tools_index
   "gap" = manifest-check/surface-check already excluded, only comp-to genuinely untracked -> documented in
   excluded_not_graph_use_cases). Guard PASSES 28/28 end-to-end + 3/3 audit. MSTR independently verified
   (anti-tautology direct calls) + CLOSED -> resolved (adae2305d). Unblocks TO-6 Gate-1/2 enforce.
3. **TO-6 LEG-A scope reconciliation** (039be57da) -- ground-truth read of comp-tool-hud.sh: Gate-2 (native
   Grep/Glob deny) SUPERSEDED by Andrew-direct "native NEVER deny" (2026-06-22); native already nudges
   advisory. So LEG-A = Gate-1 ONLY (broad Bash repo-grep DENY, estate/graph-scoped, behind a DEFAULT-OFF
   marker + a dedicated FP-test). Deliberately did NOT rush the fabric-wide enforce mechanism in-session --
   the estate-scoping vs specific-class-precedence is real design the TO gates behind the FP-test. COO
   confirmed LEG-C (announce-then-enforce relay) fires on my FP-test-PASS; standalone announce.
4. **ASTN_WSJFT.json reconciles x2** (e8ee542cd + 89833a7d4) -- Step-2b ground-truth: stale "PHASE 0 --
   PRD/DESIGN" -> deployed v0.3.0 (5 tags, 5 closed deploy ledgers, faithfulness-gate-replaced-verbatim,
   multi-recipient, 4 ETF holdings); then a follow-up after CVO flipped the schedulers ENABLED (700c07530)
   -> go-live reflected. Coordinated with COO to avoid a write-write race (COO skipped it in /drive).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which (dogfood) | live spot-checks of the routing fix (backstop/curated/search-verb paths) | PASS -- all paths route correctly post-fix |
| comp-which-routing-test.py (built) | the new regression guard (LD-0208 D) | PASS -- 28/28 end-to-end self-routing + 3/3 audit reproduction |
| comp-freshness (CVO's, cited) | 4 bd silver tables FAIL @06-19 (grounds the BDAPIMIG P0) | FINDING -- localizes the freeze to BD scraping ingest |

**What worked:** building the regression guard surfaced the gap between backstop-reachability (my first
cut, passed 28/28 blind) and MSTR's stronger end-to-end self-routing oracle (caught comp-platinum/comp-xref)
-- adopted the stronger one. **Gap found:** none new; comp-which itself was the gap, now fixed + gate-guarded.
**Note:** BDAPIMIG PRD is doc/architecture authoring -- Rule-20 graph checks ride the implementing AE TOs.

## Blockers

None real. ADVI_BDAPIMIG Phase 0 is GATED (not blocked) on an Andrew action (the post-MFA cookie capture) --
surfaced to CVO (Andrew-BD-lane) + COO; the AE Phase-0 TO stages now, GO fires on the cookie. TO-6 Gate-1
ENFORCE is GATED (not blocked) on the FP-test build + COO's announce-then-enforce -- my next increment.

## Current State (handoff -- zero prior context)

- **LD-0208 (comp-which routing):** CLOSED/resolved (MSTR adae2305d). .tools/comp-which fixed (entries key,
  backstop-before-grep, curated freshness/validate/pii + comp-platinum/comp-xref); .tools/comp-which-routing-test.py
  is the committed guard (28/28 + 3/3, exit-1 on regression; re-run after any comp-which/manifest edit).
  manifest excluded_not_graph_use_cases now includes comp-to.
- **NFRA_COMPRAIL TO-6:** LEG-0 COMPLETE -> Gate-1/2 enforce UNBLOCKED. LEG-A reduced to **Gate-1 ONLY**
  (Gate-2 superseded). NEXT (CTO): build Gate-1 estate-scoped broad-grep DENY in comp-tool-hud.sh behind a
  DEFAULT-OFF marker (org/mcp/comprail-gate1.enforce) + .tools/comprail-gate1-fptest.sh (AC#5), then hand COO
  the FP-test-PASS + announce blurb for the standalone announce-then-enforce flip.
- **ADVI_BDAPIMIG (NEW P0):** PRD docs/architecture/ADVI_BDAPIMIG_PRD.md, JSON org/projects/ADVI_BDAPIMIG.json,
  REGISTRY row added (0ee2e8b8d). Auth ruling = D + B-Phase0 + device-trust-probe-decides + A-parallel.
  COO decomposing Phase-0 (AE lane, cot-exporter pattern); CVO surfacing the Andrew cookie/probe/vendor actions.
- **ASTN_WSJFT:** OPERATIONAL/go-live (schedulers ENABLED 700c07530, autonomous 3am/4am-ET). JSON reconciled.
  First live 3am run = next ET; watch the silent-absence guard + fail-loud SNS.

## Next Steps

- [1.0.0_SA_CTO] Build TO-6 LEG-A Gate-1 mechanism (flag-off) + the AC#5 FP-test -> COO at FP-test-PASS.
- [2.0.0_SA_COO] Decompose ADVI_BDAPIMIG Phase-0 into AE TOs (stage now, GO on the Andrew cookie); LEG-C
  announce-then-enforce relay on my Gate-1 FP-test-PASS.
- [3.0.0_SA_CVO] Validate the BDAPIMIG PRD/ruling (RAVC close); surface the Andrew Phase-0 cookie + device-trust
  probe + Option-A vendor ask; co-verify the first restored 49F nightly (4 silver un-freeze + AUA recovery).
- [0.0.0_AB_MSTR / Andrew] LD-0208 closed (FYI). ADVI_BDAPIMIG Phase 0 needs the Andrew cookie capture +
  the device-trust probe + the SS&C MFA-exemption ask (Option A).
- [0.7.0_AE_CloudOps] (post-COO-decompose) ADVI_BDAPIMIG Phase-0: blackdiamond/49f/session + env + templates +
  ported ingest + backfill 06-19..today.
