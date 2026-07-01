# NFRA_COMPPROOF — Workstream B incident corpus (PINNED: top 20 by severity, 2026)

**Andrew-direct cap (2026-07-01):** B is capped at the **top 20 incidents by severity**, each
**must have occurred in 2026**, and each **must be mined from the real record** (the brief leash:
NO invented incidents). This is the PINNED FLOOR + CAP for B's corpus. The catalog-author verifies
each citation against source and strips the root-cause before the blind-solver ever sees it
(author != solver != judge — the hard B gate).

**Severity lens (composite):** client-facing data-correctness impact x financial magnitude x
silence/duration (a SILENT failure is worse — it is exactly what the graph is supposed to catch) x
P0/SEV1 designation x whether detection was HUMAN/by-eye (human-detected = every automated guard
already missed it = maximum benchmark value).

**How each is scored in B:** REACH x USABILITY. From the symptom only, can a blind agent reach the
true root cause via graph traversal + comp-tools TODAY, fast enough to have actually used it?
SOLVED / PARTIAL / MISS. Every PARTIAL/MISS -> a gap or new-tool charter (feeds Workstream D).

---

## The pinned 20 (rank 1 = most severe)

| # | Incident (date) | What happened (symptom -> root cause) | Detection | Severity anchor | Citation |
|---|---|---|---|---|---|
| 1 | **inf-ADVI 4-layer stranded-deploy P0** (2026-06-12) | One 06-11 v2-txn cutover bundle stranded across 4 layers (wrong bronze prefix / half-cutover quorum / silver-gold basename-collision silent-FATAL / eclipse cascade); served ADVI $202M vs Orion $204.6M | **HUMAN** (Andrew noticed stale ADVI 20:37Z) | SEV1 served-data staleness; L3 FATAL silent (on-instance, lock-held, no log/CW/SNS) | `org/modules/graph/debtscan/2026-06-12_LIVE_inf-ADVI-stranded-deploy-P0.md` |
| 2 | **Frozen-but-fresh 3x** (2026-06-29) | cot platinum + bd xref + inf holdings: value FROZE while timestamp kept advancing — invisible to every tool (all check the wrapper mtime/existence, not content motion). SAME class 3x in one day | mixed / by-eye | data-correctness on served; recurred 3x -> systemic; birthed comp-xray | `NFRA_COMPDIFF.json` origin; `docs/architecture/NFRA_COMPDIFF_PRD.md` |
| 3 | **NFRA_GLOBGRPH silent 2.7-day freeze** (2026-06-12 -> 06-15) | `incremental_updater` parent=None writer bug -> the marker HEAD froze; the unified GRAPH ITSELF was silently stale 2.7 days | silent (marker not advancing) | META-severe: the substrate every agent reasons from was wrong, invisibly | `org/critical_paths/change_management/20260615T1527Z_globgrph-writer-fix-rebuild_deploy_completion.md` |
| 4 | **BMKAUD benchmark semantic-break** (2026-06-01) | Model Portfolios /performance 1M: a SmartX override replaced the canonical Yang-PKL benchmark AND SmartX 1M (last-complete-cal-month) != Yang trailing-1M; STRUCTURE fine (fresh/valid float) so no alarm | **HUMAN** (Andrew by eye) | SEV1 "must-always-be-right" surface served wrong numbers; birthed GCONTR | `NFRA_GCONTR.json` origin; brief `48635a865` |
| 5 | **cot AUA freeze @ data_as_of 06-22** (2026-06) | Served cot AUA frozen at 06-22 while the pipeline reported healthy; consolidated/orphaned-holdings as_of-keyed freeze | freshness-guard miss | served AUA wrong for a live partner; ADVI_COTETL AUAFIX | `memory/reference_cot_aua_freeze_localization_consolidated_orphaned_holdings_asofdate_keyed.md`; `ADVI_COTETL.json` |
| 6 | **49F Black Diamond MFA P0** (2026-06-19) | SS&C enabled email-OTP MFA -> headless Playwright scrape can't pass it -> ALL 4 bd-scrapers dark since 06-19 (source went dark) | pipeline-dark | full source outage for 49F bronze; birthed ADVI_BDAPIMIG | `ADVI_BDAPIMIG.json` origin |
| 7 | **$22M BNP-override wipe** (2026-04-06) | `build_canonical_prices_v2 -> inject_scoped_overrides` post-step missing/stub -> BNP PARIBAS SA override wiped, +$22M phantom | data-correctness catch | $22M financial swing; the postdeps-missing class | `org/modules/graph/debtscan/2026-06-12_D2_composition_ds.md` (verbatim incident text) |
| 8 | **inf sparse-cumsum +/-$15M phantom NNA** (2026-05-13) | `inf-portal-advisor-publisher` sparse-cumsum `can_lookup.get(date,{})` -> 0.0 on no-activity dates -> FE quarter-end deltas render +/-$15M phantom flows | **HUMAN** (Andrew flagged the alternating pattern) | phantom financial flows on a demo surface | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-05-13/ADVI_INFLEC_partner_demo_marathon_session.md` |
| 9 | **$371M stale-holdings AUA inflation** (2026) | Zombie/stale accounts inflating AUA/mix without the 45-day `account_performance` active gate | gate-absence | $371M inflation of a headline number | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/threads/ADVI_MVPLVL-005-addendum-a-mix-timeseries-alignment_*.md` |
| 10 | **inf served AUA stale $202 vs $201** (2026, open) | Served AUA stale; source-vs-served divergence ($202M served vs $201M live frontier) | freshness | served headline lagging live | `memory/project_inf_served_aua_stale_202_vs_201_open.md` |
| 11 | **ETFS raw-vs-canonical holdings bug** (2026-06-25) | Fact-check found true $42.2M not $83.3M — raw holdings used where canonical holdings were required (~2x wrong) | DE fact-check | ~2x financial error; canonical-scoping gap (no comp-tool covered it) | `org/compiler-tools-log.md:8404` |
| 12 | **GCONTR phantom-Deny + SNS publish-not-delivers** (2026-06-18) | Claimed-control != live-control TWICE in one session: an IAM Deny declared-but-not-applied; an SNS publish that didn't deliver | comp-iam/live-state | the claimed!=live class; birthed COMPRAIL | CLAUDE.md comp-iam note; `NFRA_COMPRAIL.json` origin |
| 13 | **MDPF $1.77B aggregate freeze** (2026-06-25) | MDPF aggregate AUA froze; un-froze via trading-day-lag alarm repoint | alarm-repoint | $1.77B aggregate headline frozen | `org/compiler-tools-log.md:8170` |
| 14 | **AUA/NNA conflation $1.236B -> $1.545B** (2026-03-06) | A prior agent conflated NNA/AUA -> erroneous $1.236B figure; corrected to ~$1.545B | reconcile catch | $0.3B error on an aggregate | `org/daily_log/2026-03-06.md:13` |
| 15 | **DistributionTab grain-mismatch** (2026-05-14) | HH-grain `count` used as divisor against per-account-grain `aggCounts` -> median read $30.5K vs actual $101K (~3x wrong) | phase-1 synthesis | ~3x wrong displayed financial metric | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-05-14/ADVI_SHARED_phase1_synthesis.md:66` |
| 16 | **PMTRDX trade-weight unit bug** (2026-06-17) | Financial trade path: `weight_unit` fraction vs x100 mismatch -> real DDB trade records wrong (AMZN/AMD remediated) | financial-path | live trade records mis-weighted | `org/critical_paths/change_management/20260617T1548Z_pmtrdx-001-weight-unit_deploy_completion.md` |
| 17 | **COTETL canonical-seal mis-inference** (2026-06-22) | Grounded the symptom but INVENTED the mechanism, escalated to "proof," nearly drove a needless same-day fix | self-caught late | diagnostic-PROCESS failure; birthed the grounding doctrine | CLAUDE.md Rule 22; `docs/architecture/NFRA_COMPRAIL_GROUNDING_DOCTRINE.md` |
| 18 | **DT shared-branch rebase** (2026-06-11) | `git rebase` on a shared branch rewrote multi-agent history; "succeeded" only because commits didn't overlap (luck) | post-hoc | history-integrity near-miss; birthed the NEVER-rebase rule + headmove guard | CLAUDE.md NEVER-rebase rule |
| 19 | **base-COO git-sweep CLASS-C** (2026-04-27) | Staged index held files outside the declared pathspec -> cross-author contamination (3 CLASS-C sweep incidents) | audit | commit-scope integrity; birthed safe-commit pathspec guard | `memory/feedback_base_coo_git_sweep_incident.md` |
| 20 | **AE~C wrong-channel GO (suffix-strip)** (2026-05-23) | GO MCP addressed to base serial when assignee registered `~C` -> broker suffix-strip -> push never fired the lane -> ~20min stall | MSTR stimulus-scan | routing silent-drop; birthed the exact-serial TO-pairing rule | `org/XXX.md` TO-pairing rule (CY-0017 anchor) |

---

## Runners-up (the bench — swap-ins if Andrew wants B purely data/pipeline, dropping the process-class #17-20)

- NFRA_INFRPT DR-snapshot ~4-month gap (0 restore points ~4mo) — `20260616T2001Z_nfra-infrpt-dr-snapshot-backup`.
- advisor_intelligence `canonicalWindowKey` stale on SEV1 (2026-06-12) — `20260612T2024Z_advisor_intelligence_all_approval.md`.
- yang deep-tail band-overshoot $22.4M @ 2024-11-01 (2026-06-16) — `compiler-tools-log.md:6300`.
- cot device-trust cookie-stale reinject (2026-06-26) — `20260626T2302Z_cot-device-trust-reinject`.

## Coverage note (why this set is a good benchmark, not just a bug list)

The 20 span distinct FAILURE CLASSES on purpose — stranded/half-landed deploy (1,18), frozen-but-fresh
(2,5,13), silent substrate staleness (3), semantic value-break (4,14), source-dark/auth (6,12), missing
post-step (7), sparse/lookup compute bug (8,15,16), stale-inclusion inflation (9,10,11), diagnostic-process
(17), and comms/commit discipline (18,19,20). B measures whether the graph + comp-tools can reach root cause
across ALL these classes, not just the ones the program was built around. Class-diversity is the point:
the MISSes tell us which classes the substrate is blind to.

## Live-surfaced class addition — "success-shaped-but-wrong" (bench + TO-B1 harness probe; NOT in the capped 20)

A CLASS, not a historical incident, so it does NOT occupy a numbered slot — the Andrew-pinned cap of 20 holds.
**tool-output-silently-wrong -> MISS-by-mis-grounding:** a tool returns a CONFIDENTLY-WRONG output (0-count /
empty / rc=0 / silent syntax-slip) that a blind-trust agent records as TRUTH. Live evidence, THIS session, on the
COMPPROOF work itself: BOTH MSTR and CTO independently hit the same `grep -E` + BRE-`\|` dialect bug — the pattern
silently matched a literal pipe, false-negativing every check to a 0-count; each was saved ONLY by grounding the 0
against an expected-nonzero, not by trusting the tool. Pairs exactly with the ADVI_BREAKS rc=0-but-54%-households-
missing STEP3 case (both = "success-SHAPED but wrong; only grounding catches it").

This adds a THIRD scorer axis (CTO owns, TO-B1 arch-lead): **REACH x USABILITY x GROUNDING-RESILIENCE** — does the
blind-solver catch a success-shaped-wrong tool output, or record it as phantom truth? Operational home = the TO-B1
harness probe (a canary: feed a tool an input that SHOULD return N but a slip returns 0/empty/rc=0; the grounded
solver cross-checks and catches it, the blind-trust solver records the phantom). This line is the authoritative-doc
pin; the harness is where it runs. The meta-test caught its own two authors before it was even built.
