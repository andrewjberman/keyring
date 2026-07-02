"""
NFRA_COMPPROOF Workstream-B -- the PINNED top-20 incident corpus (authored data).

Andrew-direct cap (2026-07-01): top 20 incidents by severity, each occurred in 2026, each mined
from the REAL record (NO invented incidents). Source of truth:
docs/briefs/nfra-compproof-B-incident-corpus-top20-20260701.md (5402f130b). This module is the
STRUCTURED (machine-loadable) form the corpus-loader binds; each record is verified against its
`citation` (author role). The AUTHORED fields are the incident facts; the RUN fields
(graph_traversal_test / verdict / gap) are produced by the harness per blind-run, never pre-filled.

ISOLATION (the hard B gate, author != solver != judge): `true_root_cause` +
`how_it_was_actually_found` are the SEALED judge-view -- the corpus-loader NEVER folds them into the
solver-view. This module holds both; corpus_loader.py is what splits + strip-gates them.

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1, CTO arch 1315f9a03). 2026-07-01.
"""

from __future__ import annotations

# The comp-tool / graph surface a blind-solver is handed (the solver-view's tool list). Estate =
# live graph + comp-tools; NEVER the answer.
SOLVER_TOOL_SURFACE = [
    "comp-which", "comp-kuzu", "comp-blast", "comp-trace", "comp-xref", "comp-platinum",
    "comp-drift", "comp-freshness", "comp-pipescript", "comp-lambdamap", "comp-iam",
    "comp-routes", "comp-depth", "pipescript", "Grep", "Read", "aws (operational)",
]

# Each record: the AUTHORED incident facts. solver-visible = {id,rank,date,failure_class,
# symptom_as_first_seen}; SEALED (judge-only) = {true_root_cause, how_it_was_actually_found}.
INCIDENTS = [
    {
        "id": "ADVI_BREAKS", "rank": 1, "date": "2026-06-12",
        "failure_class": "stranded/half-landed deploy",
        "symptom_as_first_seen": "Served inf ADVI AUA is stale (frozen ~06-09/06-11); the 49F firm "
            "shows frozen numbers -- served ADVI ~$202M vs Orion ~$204.6M.",
        "true_root_cause": "One 06-11 v2-txn cutover bundle stranded across 4 layers: wrong bronze "
            "prefix; half-cutover quorum; silver->gold basename-collision silent-FATAL; eclipse "
            "cascade. The L3 FATAL was silent (on-instance, lock-held, no log/CW/SNS).",
        "how_it_was_actually_found": "HUMAN -- Andrew noticed the stale ADVI at 20:37Z, then hours "
            "of manual SSM/S3 grounding across a 5-failure rebuild.",
        "detection": "HUMAN", "severity_anchor": "SEV1 served-data staleness; L3 FATAL silent",
        "citation": "org/modules/graph/debtscan/2026-06-12_LIVE_inf-ADVI-stranded-deploy-P0.md",
    },
    {
        "id": "FROZEN_BUT_FRESH_3X", "rank": 2, "date": "2026-06-29",
        "failure_class": "frozen-but-fresh (content froze, timestamp advanced)",
        "symptom_as_first_seen": "cot platinum, bd xref, and inf holdings each look healthy "
            "(timestamps advancing) but downstream values are not moving.",
        "true_root_cause": "Value FROZE while the wrapper mtime/existence kept advancing -- every "
            "tool checked wrapper freshness, not CONTENT motion. Same class 3x in one day.",
        "how_it_was_actually_found": "mixed / by-eye; recurred 3x -> recognized as systemic; birthed comp-xray.",
        "detection": "by-eye", "severity_anchor": "served data-correctness; recurred 3x -> systemic",
        "citation": "NFRA_COMPDIFF.json origin; docs/architecture/NFRA_COMPDIFF_PRD.md",
    },
    {
        "id": "GLOBGRPH_SILENT_FREEZE", "rank": 3, "date": "2026-06-12/06-15",
        "failure_class": "silent substrate staleness",
        "symptom_as_first_seen": "Graph queries return plausible results but the unified graph "
            "answers seem to lag the live estate.",
        "true_root_cause": "incremental_updater parent=None writer bug froze the marker HEAD -- the "
            "unified GRAPH ITSELF was silently stale for 2.7 days.",
        "how_it_was_actually_found": "silent (marker not advancing) -- caught only when the HEAD-oracle vintage was checked.",
        "detection": "silent", "severity_anchor": "META-severe: the substrate every agent reasons from was wrong, invisibly",
        "citation": "org/critical_paths/change_management/20260615T1527Z_globgrph-writer-fix-rebuild_deploy_completion.md",
    },
    {
        "id": "BMKAUD_SEMANTIC_BREAK", "rank": 4, "date": "2026-06-01",
        "failure_class": "semantic value-break (structure fine, meaning wrong)",
        "symptom_as_first_seen": "Model Portfolios /performance 1M shows a fresh, valid number that "
            "looks off -- no alarm fired (structure valid float).",
        "true_root_cause": "A SmartX override replaced the canonical Yang-PKL benchmark AND SmartX "
            "1M (last-complete-cal-month) != Yang trailing-1M -- a semantic mismatch with valid structure.",
        "how_it_was_actually_found": "HUMAN -- Andrew by eye on a must-always-be-right surface; birthed GCONTR.",
        "detection": "HUMAN", "severity_anchor": "SEV1 must-always-be-right surface served wrong numbers",
        "citation": "NFRA_GCONTR.json origin; brief 48635a865",
    },
    {
        "id": "COT_AUA_FREEZE_0622", "rank": 5, "date": "2026-06",
        "failure_class": "frozen-but-fresh (as_of-keyed freeze)",
        "symptom_as_first_seen": "Served cot AUA is frozen at data_as_of 06-22 while the pipeline reports healthy.",
        "true_root_cause": "consolidated/orphaned-holdings as_of-date-keyed freeze -- the as_of key pinned the served AUA.",
        "how_it_was_actually_found": "freshness-guard miss -- localized via the consolidated/orphaned-holdings as_of keying.",
        "detection": "freshness-guard miss", "severity_anchor": "served AUA wrong for a live partner",
        "citation": "memory/reference_cot_aua_freeze_localization_consolidated_orphaned_holdings_asofdate_keyed.md; ADVI_COTETL.json",
    },
    {
        "id": "BD_MFA_P0", "rank": 6, "date": "2026-06-19",
        "failure_class": "source-dark / auth",
        "symptom_as_first_seen": "All 4 bd (49F Black Diamond) scrapers have gone dark since 06-19 -- bronze not updating.",
        "true_root_cause": "SS&C enabled email-OTP MFA -> the headless Playwright scrape can't pass it -> source went dark.",
        "how_it_was_actually_found": "pipeline-dark -- traced to the MFA enablement; birthed ADVI_BDAPIMIG.",
        "detection": "pipeline-dark", "severity_anchor": "full source outage for 49F bronze",
        "citation": "ADVI_BDAPIMIG.json origin",
    },
    {
        "id": "BNP_OVERRIDE_WIPE_22M", "rank": 7, "date": "2026-04-06",
        "failure_class": "missing post-step",
        "symptom_as_first_seen": "A +$22M phantom appears in canonical prices; BNP PARIBAS SA override value is wrong.",
        "true_root_cause": "build_canonical_prices_v2 -> inject_scoped_overrides post-step missing/stub -> the BNP override was wiped (+$22M phantom).",
        "how_it_was_actually_found": "data-correctness catch -- the postdeps-missing class.",
        "detection": "data-correctness catch", "severity_anchor": "$22M financial swing",
        "citation": "org/modules/graph/debtscan/2026-06-12_D2_composition_ds.md",
    },
    {
        "id": "INF_SPARSE_CUMSUM_15M", "rank": 8, "date": "2026-05-13",
        "failure_class": "sparse/lookup compute bug",
        "symptom_as_first_seen": "FE quarter-end deltas render +/-$15M phantom flows in an alternating pattern.",
        "true_root_cause": "inf-portal-advisor-publisher sparse-cumsum can_lookup.get(date,{}) -> 0.0 on "
            "no-activity dates -> phantom quarter-end deltas.",
        "how_it_was_actually_found": "HUMAN -- Andrew flagged the alternating pattern.",
        "detection": "HUMAN", "severity_anchor": "phantom financial flows on a demo surface",
        "citation": "org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-05-13/ADVI_INFLEC_partner_demo_marathon_session.md",
    },
    {
        "id": "STALE_HOLDINGS_371M", "rank": 9, "date": "2026",
        "failure_class": "stale-inclusion inflation",
        "symptom_as_first_seen": "AUA / mix headline is inflated ~$371M above the true active book.",
        "true_root_cause": "Zombie/stale accounts inflating AUA/mix -- the 45-day account_performance active gate was absent.",
        "how_it_was_actually_found": "gate-absence -- traced to the missing active gate.",
        "detection": "gate-absence", "severity_anchor": "$371M inflation of a headline number",
        "citation": "org/tier3_junior/0.4.2_RD_AdvisorIntelligence/threads/ADVI_MVPLVL-005-addendum-a-mix-timeseries-alignment.md",
    },
    {
        "id": "INF_AUA_STALE_202_201", "rank": 10, "date": "2026",
        "failure_class": "stale-inclusion / freshness",
        "symptom_as_first_seen": "Served inf AUA ($202M) diverges from the live frontier ($201M).",
        "true_root_cause": "Source-vs-served divergence -- the served headline is lagging the live compute.",
        "how_it_was_actually_found": "freshness -- source-vs-served comparison.",
        "detection": "freshness", "severity_anchor": "served headline lagging live",
        "citation": "memory/project_inf_served_aua_stale_202_vs_201_open.md",
    },
    {
        "id": "ETFS_RAW_VS_CANONICAL", "rank": 11, "date": "2026-06-25",
        "failure_class": "canonical-scoping gap (~2x wrong)",
        "symptom_as_first_seen": "A fact-check shows the displayed holdings figure is ~2x too high ($83.3M shown vs $42.2M true).",
        "true_root_cause": "raw holdings used where canonical holdings were required -- a canonical-scoping gap no comp-tool covered.",
        "how_it_was_actually_found": "DE fact-check.",
        "detection": "DE fact-check", "severity_anchor": "~2x financial error",
        "citation": "org/compiler-tools-log.md:8404",
    },
    {
        "id": "GCONTR_PHANTOM_DENY_SNS", "rank": 12, "date": "2026-06-18",
        "failure_class": "claimed-control != live-control",
        "symptom_as_first_seen": "Two controls are believed in place (an IAM Deny; an SNS publish) but the expected effect isn't happening.",
        "true_root_cause": "claimed != live TWICE: an IAM Deny declared-but-not-applied; an SNS publish that didn't deliver.",
        "how_it_was_actually_found": "comp-iam / live-state grounding; birthed COMPRAIL.",
        "detection": "comp-iam/live-state", "severity_anchor": "the claimed!=live class",
        "citation": "CLAUDE.md comp-iam note; NFRA_COMPRAIL.json origin",
    },
    {
        "id": "MDPF_AGG_FREEZE_177B", "rank": 13, "date": "2026-06-25",
        # RE-SEALED (F-fix, CTO-ratified 2026-07-02; TO-B2 CVO~B FINDING F). The integrity bar is met:
        # a seal changes ONLY on independent proof-of-defect (causally-impossible-on-the-merits), NOT
        # solver-disagreement. OLD cause "Aggregate froze on a trading-day-lag alarm mis-point; un-froze
        # via alarm repoint" (from a shallow read of org/compiler-tools-log.md:8170) is DEFECTIVE +
        # causally impossible: bd-49f-interim.tf:393-411 -- the silver-stale alarms' only actions are
        # alarm_actions/ok_actions = the bd_49f_cookie_alerts SNS topic (an email SIGNAL); an alarm is
        # not an actuator and categorically cannot un-freeze an aggregate. The authoritative CVO-verified
        # diagnosis (MDPF_ASSETS.FREEZE-DX_diagnosis.md:9) grounds the real mechanism: the convergence
        # gate correctly DEFERS on a genuinely-stale upstream (BD silver fees). "NOT an MDPF-side code
        # break." (The B-13 seal was itself an instance of B-17 COTETL_SEAL_MISINFERENCE -> seal-review gate.)
        "failure_class": "correct-defer on stale upstream (downstream victim)",
        "symptom_as_first_seen": "The MDPF aggregate AUA ($1.77B) is frozen.",
        "true_root_cause": "The MDPF daily-chain convergence gate CORRECTLY DEFERRED (fresh-custody "
            "protection) on a genuinely-stale upstream -- BD silver `fees` frozen at the 06-18 partition "
            "since the 06-19 BD-49F break; the served aggregate is a downstream victim, NOT a defect on the MDPF side.",
        "how_it_was_actually_found": "per-stage live freshness isolated the stuck input to BD silver "
            "fees; gate source + CloudWatch defer-decisions confirmed a correct defer (not a break).",
        "detection": "per-stage freshness + gate-source grounding", "severity_anchor": "$1.77B aggregate headline frozen",
        "citation": "org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-06-25/MDPF_ASSETS.FREEZE-DX_diagnosis.md:9; "
            "infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:393-411 (alarm=SNS-signal-only -> old cause causally impossible)",
    },
    {
        "id": "AUA_NNA_CONFLATION", "rank": 14, "date": "2026-03-06",
        "failure_class": "semantic value-break (conflation)",
        "symptom_as_first_seen": "An aggregate figure ($1.236B) is reported that looks wrong vs expectation.",
        "true_root_cause": "A prior agent conflated NNA with AUA -> the erroneous $1.236B; corrected to ~$1.545B.",
        "how_it_was_actually_found": "reconcile catch.",
        "detection": "reconcile catch", "severity_anchor": "$0.3B error on an aggregate",
        "citation": "org/daily_log/2026-03-06.md:13",
    },
    {
        "id": "DISTTAB_GRAIN_MISMATCH", "rank": 15, "date": "2026-05-14",
        "failure_class": "grain-mismatch compute bug (~3x wrong)",
        "symptom_as_first_seen": "DistributionTab median reads ~$30.5K vs an actual ~$101K (~3x low).",
        "true_root_cause": "HH-grain `count` used as the divisor against per-account-grain `aggCounts` -- a grain mismatch.",
        "how_it_was_actually_found": "phase-1 synthesis review.",
        "detection": "phase-1 synthesis", "severity_anchor": "~3x wrong displayed financial metric",
        "citation": "org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-05-14/ADVI_SHARED_phase1_synthesis.md:66",
    },
    {
        "id": "PMTRDX_WEIGHT_UNIT", "rank": 16, "date": "2026-06-17",
        "failure_class": "unit-mismatch compute bug (financial path)",
        "symptom_as_first_seen": "Live DDB trade records are wrong (AMZN/AMD weights off).",
        "true_root_cause": "weight_unit fraction vs x100 mismatch on the trade path -> mis-weighted trade records.",
        "how_it_was_actually_found": "financial-path review (AMZN/AMD remediated).",
        "detection": "financial-path", "severity_anchor": "live trade records mis-weighted",
        "citation": "org/critical_paths/change_management/20260617T1548Z_pmtrdx-001-weight-unit_deploy_completion.md",
    },
    {
        "id": "COTETL_SEAL_MISINFERENCE", "rank": 17, "date": "2026-06-22",
        "failure_class": "diagnostic-process failure (invented mechanism)",
        "symptom_as_first_seen": "Served cot AUA is stale; a plausible mechanism suggests itself.",
        "true_root_cause": "The symptom was grounded but the MECHANISM was INVENTED, escalated to 'proof', nearly "
            "driving a needless same-day fix -- the process failure, not a data bug.",
        "how_it_was_actually_found": "self-caught late; birthed the grounding doctrine (Rule 22).",
        "detection": "self-caught late", "severity_anchor": "diagnostic-PROCESS failure",
        "citation": "CLAUDE.md Rule 22; docs/architecture/NFRA_COMPRAIL_GROUNDING_DOCTRINE.md",
    },
    {
        "id": "DT_SHARED_REBASE", "rank": 18, "date": "2026-06-11",
        "failure_class": "history-integrity (shared-branch rebase)",
        "symptom_as_first_seen": "A shared-branch git operation completed 'successfully' with no visible error.",
        "true_root_cause": "git rebase on a shared branch rewrote multi-agent history -- it 'succeeded' only "
            "because the commits happened not to overlap (luck, not correctness).",
        "how_it_was_actually_found": "post-hoc; birthed the NEVER-rebase rule + headmove guard.",
        "detection": "post-hoc", "severity_anchor": "history-integrity near-miss",
        "citation": "CLAUDE.md NEVER-rebase rule",
    },
    {
        "id": "COO_GIT_SWEEP", "rank": 19, "date": "2026-04-27",
        "failure_class": "commit-scope integrity (cross-author contamination)",
        "symptom_as_first_seen": "A commit landed carrying files beyond the intended change.",
        "true_root_cause": "The staged index held files outside the declared pathspec -> cross-author "
            "contamination (3 CLASS-C sweep incidents).",
        "how_it_was_actually_found": "audit; birthed the safe-commit pathspec guard.",
        "detection": "audit", "severity_anchor": "commit-scope integrity",
        "citation": "memory/feedback_base_coo_git_sweep_incident.md",
    },
    {
        "id": "WRONG_CHANNEL_GO", "rank": 20, "date": "2026-05-23",
        "failure_class": "comms routing silent-drop",
        "symptom_as_first_seen": "An assignee never acts on a GO; a ~20min stall with no error surfaced.",
        "true_root_cause": "The GO MCP was addressed to the base serial when the assignee registered ~C -> "
            "broker suffix-strip -> the lane push never fired.",
        "how_it_was_actually_found": "MSTR stimulus-scan; birthed the exact-serial TO-pairing rule.",
        "detection": "MSTR stimulus-scan", "severity_anchor": "routing silent-drop",
        "citation": "org/XXX.md TO-pairing rule (CY-0017 anchor)",
    },
]

# CLASS probe (NOT a numbered incident -- the Andrew-pinned cap of 20 holds). The
# success-shaped-but-wrong canary the 3rd scorer axis (GROUNDING-RESILIENCE) runs. A tool returns a
# CONFIDENTLY-WRONG output (0-count / empty / rc=0 / silent syntax-slip) that a blind-trust solver
# records as truth; a grounded solver cross-checks (expected-nonzero / sharp test) and catches it.
SUCCESS_SHAPED_WRONG_PROBE = {
    "id": "PROBE_SUCCESS_SHAPED_WRONG",
    "kind": "grounding-resilience-canary",
    "description": "Feed the solver a tool-call that SHOULD return N but a slip returns 0/empty/rc=0 "
        "(anchors: the grep -E + BRE-`\\|` false-0 both MSTR+CTO hit this session; the rc=0-but-54%-"
        "households-missing STEP3 rebuild). Scored: does the solver cross-check the suspicious 0 "
        "(RESIST) or record it as truth (TRIP)?",
    "expected_nonzero": True,
}


def solver_visible_fields() -> tuple:
    """Incident fields a blind-solver MAY see. ONLY the symptom + date -- NOT the descriptive `id`
    (leaks mechanism terms, e.g. INF_SPARSE_CUMSUM), NOT `failure_class` (a root-cause classification),
    NOT `rank` (severity hint). The loader assigns an OPAQUE case_id (B-NN). Everything else SEALED."""
    return ("date", "symptom_as_first_seen")


def sealed_fields() -> tuple:
    """Judge-only fields -- NEVER folded into the solver-view. `failure_class` is a root-cause
    CLASSIFICATION (a hint toward the mechanism), so it is sealed too; the harness uses it only for
    post-run class-diversity aggregation, never solver-facing."""
    return ("true_root_cause", "how_it_was_actually_found", "failure_class")
