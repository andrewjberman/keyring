# Fabric-crash recovery -> MDPF_REVAMP main-verify + MP coverage census + built comp-clobber -- 3.0.0_SA_CVO

**Date:** 2026-07-21
**Task Order:** ad-hoc (main CVO crash-recovery; MDPF_REVAMP P0 main-verify; Andrew-direct MP census + comp-clobber build)
**Status:** COMPLETE (session close)
**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, DIAGNOSE

---

## Objective

Recover as MAIN CVO after the ~09:54 EDT WindowsTerminal crash; provide INDEPENDENT main-verify of the MDPF_REVAMP N=3 cutover (spine + A4 + A3/A7); on Andrew-direct, produce a data dictionary + revamp-coverage census of the Model Portfolios page; deep-investigate the aum-timeseries staleness Andrew flagged; and build the new `comp-clobber` comp-tool for output-key collisions.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-grep | cohort_provenance / source_vintage_last / getAUMSummary in portal/src | PASS | proved 0 FE consumers of cohort_provenance/source_vintage_last; found FactorTilts A1 consumer |
| comp-cache | map (MDPF queryKeys) | PASS | enumerated the 7 MP useQuery keys -> served artifacts |
| pipescript | smartx / model-portfolios | PASS | smartx EC2 view producer DISABLED; live path REST->DDB->proxy; the SmartX-vs-legacy producer split |
| comp-freshness | grep smartx/mdpf | PARTIAL | no smartx rows in default view; used S3 version-history directly instead |
| comp-which | routed clobber question | PASS | routed to comp-dups (1.50) pre-build; post-build routes comp-clobber rank-1 (2.00) |
| comp-dups | estate dup census | PASS | confirmed it does NOT catch output-key collisions (code/TF bodies only) -> justified comp-clobber |
| comp-manifest-check | completeness | PASS (gate) | blocked comp-clobber twice (routable ABSENT-FROM-PROVIDER; existence not-tracked) until registration complete |
| comp-system | regen 06_current_state | PASS | 62->63 tools_index after comp-clobber; staged the 5 sibling docs |
| comp-clobber | self-test / --sweep / --live | PASS | NEW TOOL I built: self-test 5/5; --sweep json/portfolios found aum-timeseries clobber |

**What worked:** comp-grep's 0-consumer proof for cohort_provenance was decisive (turned a scary "unproduced field" into an FE-safe co-sign note); comp-manifest-check named the exact registration fix at each block (routable -> meta_tools home; existence -> git add -f); S3 `list_object_versions` etag-lineage was the true oracle for the aum-timeseries clobber that a fresh LastModified hid.
**What failed:** comp-freshness surfaced no smartx rows (fell back to raw version-history); my first comp-clobber static self-test FAILED because the two aum-timeseries writers reach the key by different code paths (json/ direct vs platinum/->json publish) -> pivoted the self-test to the interleave-oracle unit test.
**Gap found:** output-key COLLISION (2+ producers -> one sink) was a real estate blind spot -- comp-dups scans code bodies, not write targets. CLOSED by building comp-clobber.

---

## Work Completed

### 1. Crash recovery + the LD-0319 stale-directive catch
Registered 3.0.0_SA_CVO (PID 35000), armed inbox Monitor `bjxffi477`, wrote LD-0290 serial file, zero crons. My launcher + the MSTR crash-brief both said "run LD-0319 parity-FIRST" -- I grounded it against LD-0325 (base CVO does NOT do SYSPARITY; it's CVO~Z's) + XXX.md 1b-F, declined to adopt SYSPARITY, and surfaced it. MSTR fixed the root cause (`ajb.ps1:118` @6704c6b78, LD-0329) + surfaced the CVO~Z-down gap to Andrew.

### 2. MDPF_REVAMP independent main-verify (the 3-pass N=3 gate)
Own from-scratch re-derivations (live S3, Rule 22a), NOT DS's scripts:
- **Date symmetric-diff:** 429 served / 428 serve-real / 408 common / 21 served-only (all non-trading) / 20 published-only (all real trading w/ data); **0 unexplained**. 3-way convergence (me + DS + CTO). Caught the vintage-frozen `len==427`/`custody[-1]` criteria -> CTO re-anchored to last-common-date 07-17.
- **F1 min-day floor CLEARED:** UST launched 2025-01-16 (served 0.0 pre-launch == silver min_day; builder D4 zero-pads core `:435`) -> named-note that ties, not a delta.
- **A4 basis CONFIRMED to the cent** on the real served artifact (`json/portfolios/non_model_assets.json` non_model=$247.69M enterprise). Caught a REAL error in CTO's "A4 ties $247.69M" criterion -> CTO corrected it (A4 correctly carries D-2 full-envelope, does NOT tie the partial-cash $247.69M).
- **SPINE 3/3 PASS** (staged ETags matched CTO's): identities 0-mismatch (global 48 diffs all <=$0.02 float); composition +$21,647,872 = D-2 $20,344,172.42 + F2 $1,303,699.58 to the cent.
- **Streak-count correction (COO-caught, CTO-ruled):** the hand-staged run = code-correctness PRE-PROOF, counts ZERO toward N=3 (NEVER-validate-on-ad-hoc); N=3 = 3 clean SCHEDULED cycles.
- **Push-now cutover:** Andrew GO'd push-now on the pre-proof. I surfaced the risk relocation (the first SCHEDULED overwrite exercises the unproven S4 path; publish-then-verify => a bad-data window) -> CTO ADOPTED verify-before-serve on scheduled cycle-1.
- **Chain-of-custody byte-diff:** caught the pre-proof re-staged 18:21Z (ETags moved post-sign-off); retrieved the signed version via bucket versioning + byte-diffed -> DATA arrays byte-IDENTICAL, delta = account_count wiring + generated_at + source_vintage_last(SKELETON->current); corrected DS's "only account_count" commit as incomplete.

### 3. MP page data dictionary + revamp-coverage census (Andrew-direct; joint with CTO)
Rendered /portfolios; mapped header + AUA-tab component->field->artifact. Revamp covers 3 of 5 in-scope artifacts (aggregate-aua, account-distribution, non_model_assets); does NOT cover **aum-metrics (A1)** or **aum-timeseries (A2)**. Extensions CTO absorbed: cohort_provenance served-vs-revamp non-overlap (FE-unconsumed -> Andrew-call fidelity note); FactorTilts + Attribution/SelectionTab + Positioning/HoldingsTab = a 4-surface A1 blast radius (flipped disposition to Option Y: build producers); A2/A4 legacy-emitter coupling = cutover-blocking (routed DS). Grounded content-gap B (served account_count = REAL history; revamp None is a source-asymmetry, not a regression).

### 4. aum-timeseries DEEP investigation -> a CLOBBER (Andrew "make certain")
Andrew flagged the 2-month staleness as likely a deprecated asset. Version history proved it: TWO producers write `json/portfolios/aum-timeseries.json` -- a daily 11:30 emitter (`build_legacy_compat_emit.py`, self-referential, RunDate NOT passed -> self-perpetuating FROZEN 05-29) and an irregular fresh producer (current to 07-18, then STOPPED). Applied Andrew's "07-18 is Saturday": the fresh-pipeline gap is 2 trading days (mild), the 05-29 aum-timeseries is the egregious ~35-trading-day deprecated clobber. non_model_assets/aggregate-aua NOT clobbered.

### 5. Built comp-clobber (canonical registration flow)
NEW comp-tool: output-key COLLISION scanner (2+ producers -> one S3 key/DDB table). Engine `org/modules/graph/clobber_scan.py` + `.tools/comp-clobber` wrapper; static write-call-windowed candidate-finder + LIVE version-history etag-lineage ORACLE (`--live`/`--sweep`). Registered atomically per COMPTOOL_REGISTRATION_FLOW: entries `estate.clobber.output_key_collision` + tools_index + coverage-map meta_tools + comp-which route + comp-system 06 regen. self-test 5/5, routes rank-1. Then folded Andrew's two comp-manifest-check refinements (router-vs-gate; skip-a-part->member-blocks) into the flow doc.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Decline LD-0319 SYSPARITY; surface as stale directive | LD-0325 moved it to CVO~Z; launcher/brief lagged (a stale-record-with-authority) |
| Not rubber-stamp; run own from-scratch re-derivations | Rule 22a -- verify the artifact, not the producer self-report; caught 3 real criterion errors |
| Build comp-clobber vs extend comp-dups | genuinely different concern (write-TARGET collision vs code-body dup) -> new tool per the flow's anti-sprawl rule |
| Static self-test -> interleave-oracle unit test | the aum-timeseries clobber is publish-mediated (different code paths), un-catchable statically; the oracle is the LIVE etag interleave |

---

## Files Modified

See commit messages: `f78abf920`, `39845e26a`, `c5a8541da`, `af5759dcf`, `b0dc80656`, `15c9d4f2d` (MDPF verify deliverable), `760a457e8` (MP census), `aca069af9` (comp-clobber atomic bundle: clobber_scan.py + .tools/comp-clobber + 3 registries + comp-system 06), `47c84ecdb` (flow-doc refinements). All committed + pushed to origin/CLOUD.

---

## Blockers

None. All my verify commitments are delivered; MDPF cutover next-steps are other agents' lanes (below).

---

## Current State

> Handoff for zero-context reader.

Main CVO up (PID 35000, watcher `bjxffi477`, zero crons). **MDPF_REVAMP:** the hand-staged pre-proof is 3-way-verified (spine 3/3 + A4 named-delta) and byte-verified as the serving bytes (`gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` ETags `933318c2`/`f3fd7af2`/`53b732b2`); Andrew GO'd a push-now cutover on it; my role is now the **verify-before-serve GATE on scheduled cycle-1** (harness `scratchpad/cvo_indep_spine_gate.py` ready) + shadow+rollback cycles 2+; N=3 = 3 clean SCHEDULED cycles (the pre-proof counts zero). **MP census** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_REVAMP_MP_page_data_dictionary_and_coverage_census_20260721.md` @760a457e8, reconciled w/ CTO): revamp does NOT produce aum-metrics(A1)/aum-timeseries(A2); disposition = Option Y (build producers). **aum-timeseries is a live CLOBBER** -- deprecated 11:30 `build_legacy_compat_emit.py` (self-perpetuating frozen 05-29) overwriting a fresh producer that stopped 07-18; the AUA Daily Trend chart currently renders 05-29 data. **comp-clobber** is LIVE + registered (@aca069af9, 63rd tools_index tool); `comp-clobber --sweep <bucket> <prefix>` finds all clobbered keys under a prefix.

---

## Next Steps

1. **[3.0.0_SA_CVO] Run the verify-before-serve gate on the first SCHEDULED MDPF cycle** -- re-run `cvo_indep_spine_gate.py` on the scheduled `gold/mdpf_revamp/*`; clean -> CTO GOes the cycle-1 publish; a delta -> HOLD. Then N=3 streak (cycles 2/3).
2. **[1.0.0_SA_CTO] A2/A4 legacy-emitter coupling (cutover-blocking)** -- untangle `dim_mdpf_non_model_assets.py:7` from `build_legacy_compat_emit.py`; and the deprecated 11:30 frozen aum-timeseries emitter should be RETIRED as part of the cutover (not migrated).
3. **[1.0.0_SA_CTO / DS] A1/A2 Option-Y producers** off the revamp aggregate (field-identical), covering the 4 A1 surfaces + the mixed-basis global Total.
4. **[3.0.0_SA_CVO] Optional: `comp-clobber --sweep` the rest of the served estate** (opal-data-assets, bd/inf/cot served buckets) for other clobbers -- offered to Andrew.
