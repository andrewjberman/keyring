"""
NFRA_TOOLHEALTH.TH-A -- the per-TOOL/per-CLASS EFFECTIVE-probe corpus (the sealed answer-key).

Generalizes the COMPPROOF-B1 per-INCIDENT corpus to per-TOOL: for each comp-tool (or tool-class),
a small set of REPRESENTATIVE blind questions the tool CLAIMS to serve, each with a SEALED expected
answer (the distinctive terms a correct, reached answer must contain). The probe (tool_probe.py) runs
the tool against the LIVE estate with an answer-FREE payload and scores REACH x USABILITY -> EFFECTIVE.

ISOLATION (inherited from B1, HARD): the sealed `answer_terms` / `answer_substr` are NEVER handed to
the tool run -- only `question` + `run` (the invocation) are. tool_probe.probe_payload proves the strip.
A tool that could see its own expected answer = a VOID EFFECTIVE verdict (measures nothing).

Field contract per probe:
  probe_id      : opaque stable id (TOOL/CLASS-NN) -- what the emitted row keys its provenance on.
  tool          : the canonical comp-tool under test (comp-*/pipescript) -- the emit key TH-B reads.
  tool_class    : the CLASS of question the tool claims to serve (routing / freshness / impact / ...).
  question      : the plain-English blind question (solver-visible; carries NO mechanism/answer).
  run           : the argv list actually executed (subprocess) -- the tool invocation, answer-free.
  answer_terms  : distinctive tokens a REACHED answer must contain (>=THRESHOLD present => reach=yes).
  answer_substr : optional exact substring that alone proves reach (case-insensitive) -- OR-ed with terms.
  reach_threshold: how many distinct answer_terms must appear for reach=yes (default 1).
  usability_timeout_s: > this wall-clock (under load) = too-slow => FUNCTIONAL PARTIAL, not EFFECTIVE.
  expected      : self-test label only (effective|fix|unknown) -- NEVER fed to the run, NEVER scored-against.
  live_estate   : True if the run reaches AWS/live estate (needs creds); False = local (graph/cache/router).

Author: 0.8.0_AE_CloudComp~D (NFRA_TOOLHEALTH.TH-A, COO~B GO 2026-07-02). Reuses B1 un-forked.
"""

from __future__ import annotations

import os
import sys

# sovereign_held lives one dir up (compproof -> graph); reach it for the by-construction sovereign assert.
_GRAPH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _GRAPH not in sys.path:
    sys.path.insert(0, _GRAPH)
from sovereign_held import is_held_path, is_held_bucket  # noqa: E402


# The probe corpus. Kept SMALL + representative (per-tool, per-class) -- this is a RECURRING probe, not
# an exhaustive test suite; each entry is one class-representative question the tool claims to answer.
TOOL_PROBES = [
    {
        "probe_id": "comp-which/routing-01",
        "tool": "comp-which",
        "tool_class": "tool-routing",
        # Clean isolation: the question names NO tool + shares NO token with the sealed answer "comp-blast".
        "question": "Which comp-tool tells me what downstream breaks if I change a gold-script function?",
        "run": ["comp-which", "what downstream depends on a gold-script function I want to change"],
        "answer_terms": ["comp-blast"],
        "answer_substr": "comp-blast",
        "reach_threshold": 1,
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": False,
    },
    {
        "probe_id": "comp-which/routing-02",
        "tool": "comp-which",
        "tool_class": "tool-routing",
        # "stale" deliberately avoids the token "fresh(ness)" so the sealed answer "comp-freshness" does
        # NOT leak into the payload (isolation-clean per the strip gate). Unambiguous freshness intent
        # (no "platinum" token, which biases the router toward comp-platinum).
        "question": "Which comp-tool checks whether served gold data has gone stale?",
        "run": ["comp-which", "how do I check whether served gold data is stale"],
        "answer_terms": ["comp-freshness"],
        "answer_substr": "comp-freshness",
        "reach_threshold": 1,
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": False,
    },
    {
        "probe_id": "comp-freshness/single-artifact",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        # POSITIVE control (expected effective): does comp-freshness reach a usable freshness verdict for a
        # TARGETED single artifact? REACH keys on the RESOLVED artifact_id `inf_orion_api_performance` --
        # NOT the column headers (status/age_h/fail_at_h), which comp-freshness prints UNCONDITIONALLY (even
        # a header-only / no-row result would false-match them; found live 2026-07-12, same class as the
        # discrimination fail_at_h bug). The id is NOT in the run argv (which carries only the s3 PATH), so
        # its presence PROVES the tool resolved config -> a real data row; a header/empty output never
        # contains it. rc 0 (PASS) and 1 (a FAIL verdict) are BOTH usable (usability gate); rc 2 = fall-back.
        # opal-data-inf is IN-SCOPE (sovereign hold 2026-07-09); corpus sovereign-safe BY CONSTRUCTION below.
        "question": "Report the freshness STATUS of a single named served artifact.",
        "run": ["comp-freshness", "artifact", "s3://opal-data-inf/silver/api_dims/performance/"],
        "answer_terms": ["inf_orion_api_performance"],   # the RESOLVED-row id, not a header token
        "answer_substr": "inf_orion_api_performance",
        "reach_threshold": 1,
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": True,
    },
    {
        "probe_id": "comp-freshness/frozen-vs-fresh-discrimination",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        "kind": "discrimination",
        # THE HONESTY KEYSTONE (the un-gameable NEGATIVE case; replaces the bd latency FIX-catch with a
        # false-GREEN catch -- a stronger, honester FIX-signal). A REACH x USABILITY probe is a SOFT exit-0
        # proxy for a PLAUSIBLE-BUT-WRONG answer, so it CANNOT catch the paradigm lie: comp-freshness saying
        # FRESH on a frozen-content / fresh-mtime artifact (its as_of/partition-key reader is ANTI-CORRELATED,
        # test_freshness_partition_key_anticorrelated.py). This probe STAGES that exact lie: write a synthetic
        # artifact with a FROZEN content date + a FRESH mtime to an IN-SCOPE scratch prefix, run comp-freshness
        # on it, and score effective by whether the tool CAUGHT the freeze (STALE => yes) or LIED (GREEN =>
        # no). The ORACLE = the content date the probe WROTE (grounded OTHER than comp-freshness, which reads
        # mtime) -- the anti-Goodhart anchor. Guaranteed cleanup; sovereign-safe scratch target. CTO gate
        # 2026-07-12: B1 per-run fixture (a committed fixture's mtime AGES; the per-run write IS the fresh mtime).
        "question": "Does comp-freshness catch a KNOWN-FROZEN artifact (content 30d old) whose S3 mtime is fresh?",
        "fixture": {
            "scratch_bucket": "opal-data-inf",          # IN-SCOPE only (asserted); never bd/schwab
            "scratch_prefix": "_toolprobe_scratch/",     # dedicated + namespaced; never a served/canonical key
            "content_as_of_days_ago": 30,                # the FROZEN content date = the independent oracle ground-truth
        },
        # VERDICT is the RC, not a substring (a `fail_at_h` header would false-match a "fail" term). comp-
        # freshness single-artifact: rc 0 = PASS (=> false-GREEN on the frozen fixture => effective=no),
        # rc 1 = a FAIL/STALE verdict (=> CAUGHT => yes), rc 2 = config/AWS error (=> VOID/unknown).
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 60,
        "expected": "fix",   # self-test label: PRE-fix the discrimination catches comp-freshness's false-GREEN
        "live_estate": True,
    },
    {
        "probe_id": "comp-freshness/partition-key-frozen-vs-fresh",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        "kind": "pk-discrimination",
        # SENSOR-COMPLETENESS (CTO D2, 2026-07-12). The keystone discrimination probe above measures the
        # AD-HOC `artifact`-mode MTIME-only miss (defect a; cmd_artifact:1058 permissive-default, no
        # _pk_check). This case measures the SIBLING partition-key miss (defect b): comp-freshness's
        # PARTITION-KEY mode reads _max_partition_date, whose `_DATE_KEY_RE.search(line)` (:347) takes the
        # FIRST date on an `aws s3 ls` line = the LastModified column, NOT the filename date-key -- so a
        # silver/<t>/<STALE-date>.parquet rewritten with a FRESH mtime reads GREEN (the FIX-TO defect,
        # 23a7be2a1). GREY-BOX BY NECESSITY: comp-freshness has NO config-override / partition-key CLI flag,
        # so the ad-hoc CLI cannot reach partition-key mode for a scratch fixture -- the probe stages a real
        # in-scope partition-keyed S3 fixture and exercises the REAL _check_artifact (partition-key path),
        # scoring on its computed STATUS (not a substring). The ORACLE = the FROZEN date-key filename the
        # probe WROTE (2001-01-01), independent of comp-freshness (which reads LastModified). VALIDATED live
        # 2026-07-12: the fixture reads status=PASS, partition_as_of=<today> (the mtime) -> effective="no".
        # POST the FIX-TO land, _max_partition_date reads 2001 -> status=FAIL -> effective="yes" (the loop
        # closes on defect b). FIXED date-key -> object never accumulates (overwrite, no delete).
        "question": "Does comp-freshness's PARTITION-KEY mode catch a frozen date-key (silver/<t>/<stale>.parquet) whose S3 mtime is fresh?",
        "fixture": {
            "scratch_bucket": "opal-data-inf",                    # IN-SCOPE only (asserted); never bd/schwab
            "scratch_prefix": "_toolprobe_scratch/pk/silver/toolprobe/",  # a silver/<table>/ shape; dedicated
            "frozen_date_key": "2001-01-01",                      # FIXED old date-key = the oracle; no accumulation
            "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR",
        },
        # VERDICT is comp-freshness's computed result["status"] (from _check_artifact), NOT a substring:
        # PASS => false-GREEN on a frozen date-key => effective="no"; WARN/FAIL/ESCALATED => CAUGHT => "yes";
        # a partition-UNCHECKED / MISSING / ERROR / staging failure => VOID/unknown (never a silent no).
        "usability_timeout_s": 60,
        "expected": "fix",   # self-test label: PRE-fix the partition-key mode false-GREENs the frozen date-key
        "live_estate": True,
    },
    {
        "probe_id": "comp-iam/resource-scoped-grant-discrimination",
        "tool": "comp-iam",
        "tool_class": "iam-grant-oracle",
        "kind": "iam-discrimination",
        # EFFECTIVE-axis probe for comp-iam, a SECURITY GRANT ORACLE (CTO 2026-07-12). The Rule-22a
        # resource-blindness (`s3:GetObject [GRANTED]` for a bucket the role never held; extract_iam
        # Operation had NO resource field) is FIXED (resource_verdict :927 compares the ARN; CVO P1/P1a
        # 2026-07-10). So this is NOT a lie-catcher -- it scores effective="yes" TODAY and stands as a
        # REGRESSION GUARD: a resource-awareness regression on a grant oracle is a SILENT FALSE-GRANT (the
        # worst class). It checks whether comp-iam DISCRIMINATES a resource the role HOLDS from one it does
        # NOT: held -> GRANTED, not-held -> UNGRANTED-RESOURCE. The ORACLE is simulate-principal-policy (the
        # LIVE-APPLIED IAM decision, grounded OTHER than comp-iam's TF-DESIRED model -- Rule 22a's mandated
        # technique), WITH a POSITIVE CONTROL on the held resource (else a 403/typo reads as implicitDeny and
        # the negative proves nothing). VALIDATED live 2026-07-12: comp-iam held=GRANTED/notheld=UNGRANTED-
        # RESOURCE; oracle held=allowed/notheld=implicitDeny -> effective="yes". IN-SCOPE ARNs only (inf held,
        # cot not-held); NO bd/schwab (asserted). READ-only: no S3 write, only IAM TF-parse + simulate.
        "question": "Does comp-iam DENY (UNGRANTED-RESOURCE) an action on a resource the role does NOT hold -- matching the live simulate-principal-policy implicitDeny -- rather than resource-blind false-GRANT it?",
        "fixture": {
            "role_name": "orion-crawl-harness-role",
            "role_arn": "arn:aws:iam::313476888478:role/orion-crawl-harness-role",
            "action": "s3:GetObject",
            "held_resource": "arn:aws:s3:::opal-data-inf/orion/toolprobe-regression-key",   # POSITIVE control (role HAS inf/orion/*)
            "notheld_resource": "arn:aws:s3:::opal-data-cot/toolprobe-regression-key",       # the discrimination (role has NO cot grant)
        },
        # VERDICT: comp-iam's resource_verdict string vs the simulate-principal-policy decision. effective=
        # "yes" iff comp-iam DISCRIMINATES (held GRANTED, not-held UNGRANTED-RESOURCE/UNGRANTED) AND the
        # oracle grounds it (held allowed, not-held *Deny); "no" iff comp-iam FALSE-GRANTS the not-held where
        # the oracle denies (resource-blind regression); VOID iff the positive control fails / the tuple
        # went stale / comp-iam returns UNRESOLVABLE/GRANTED-BROAD (honestly could not determine).
        "usability_timeout_s": 60,
        "expected": "effective",   # comp-iam is resource-aware TODAY -> yes; the probe is the regression guard
        "live_estate": True,
    },
    {
        "probe_id": "comp-aws/garbage-reject-and-unscored-discrimination",
        "tool": "comp-aws",
        "tool_class": "cloud-compiler-cert",
        "kind": "cmpaws-discrimination",
        # EFFECTIVE-axis probe for comp-aws (ADHC_CMPAWS), a cloud-state CERT compiler (CTO gate 2026-07-12).
        # comp-aws is ALREADY honest about garbage / no-oracle -- so this scores effective="yes" TODAY and
        # guards the regression: a garbage class SCORED as a verdict, or an UNMEASURED class recorded as a
        # false PASS. Verdict is the RC CONTRACT (RC_INVALID=2 / RC_UNSCORED=4 / RC_OK=0 / RC_FAIL=1), NOT a
        # substring. Three cases roll into one tool verdict:
        #   A GARBAGE class     -> expect rc 2 (rejected). effective="no" if it SCORES it (rc 0/1).
        #   B no-oracle class   -> expect rc 4 (UNSCORED, "UNMEASURED never success"). "no" if false PASS (rc 0).
        #   C real-oracle class -> expect rc {0,1} (a REAL verdict = the POSITIVE control: not reject-all).
        # ORACLE = the class CLASSIFICATION, grounded OTHER than comp-aws's scoring: A is a HARDCODED garbage
        # string (CTO hardening -- fully independent of comp-aws's CLASSES, so a CLASSES-list corruption
        # cannot fool BOTH the scoring and the probe); B/C are hand-picked KNOWN classes (sns=no-oracle,
        # s3=real-oracle, per the live grounding). MAINTENANCE: legitimate coverage growth (sns GETS a
        # certified scorer) makes B's rc flip 4->{0,1} -> update no_oracle_class to another scorer-less class
        # (a definition-corruption is out-of-scope for a regression guard, per CTO -- acceptable, noted).
        # READ-only (score is offline-adjudicating); calls comp_aws_cli.py directly (bash wrapper unusable on Windows subprocess).
        "question": "Does comp-aws score REJECT a garbage class (rc2), declare a no-oracle class UNSCORED (rc4, never a false PASS), AND still produce a real verdict for a real-oracle class (rc0/1)?",
        "fixture": {
            "garbage_class": "zzqq-nonexistent-class-9x7",   # HARDCODED garbage (CTO hardening) -- independent of CLASSES
            "no_oracle_class": "sns",                         # KNOWN no-oracle (maintained fixture; see MAINTENANCE)
            "real_oracle_class": "s3",                        # KNOWN real-oracle = POSITIVE control (a real verdict)
        },
        "score_timeout_s": 180,   # the real-oracle case DERIVES live; garbage/no-oracle reject/unscore fast
        "expected": "effective",  # comp-aws is rc-honest TODAY -> yes; the probe is the regression guard
        "live_estate": True,
    },
    {
        "probe_id": "comp-surface-check/sev1-detection-discrimination",
        "tool": "comp-surface-check",
        "tool_class": "critical-surface-detection",
        "kind": "surfacecheck-discrimination",
        # EFFECTIVE-axis probe for comp-surface-check, the SEV1 critical-surface DETECTION gate (Rule 20).
        # DETECTION-CORRECTNESS regression guard (CTO~D B2 ruling 2026-07-12, framing APPROVED w/ the
        # mandatory scoping annotation). The tool's detection is honest today (path-match vs the registry),
        # so this scores effective="yes" and guards a detection regression -- a registry-parse break /
        # path-match bug / severity-resolution error is a SILENT FALSE-CLEAN on a must-always-be-right
        # surface (the worst class for a gate). SCOPE (MANDATORY -- in _SURFACECHECK_SCOPE + every emitted
        # effective_evidence): effective="yes" attests DETECTION-CORRECTNESS ONLY -- NOT that the SEV1
        # surfaces are GATED in the real commit flow (that wiring-blindness is LD-0273, arch-gated CTO).
        # Two axes, two records; this bool must NEVER be read as "surfaces protected".
        # ORACLE = critical-surfaces.yaml MEMBERSHIP (read by the probe, not the tool's stdout); the runner
        # asserts sev1_path IS registered + noncritical_path is NOT, at run-time (non-vacuous both ways).
        # VERDICT = the RC contract of `check --mode blocking` (SEV1->rc!=0, non-critical->rc0), NEVER a
        # substring. READ-only, parent-scoped (argv carries only the PATH, no verdict leak); no S3/estate/bd.
        "question": "Does comp-surface-check FLAG a registered SEV1 surface (block-with-ack, rc!=0 blocking) AND CLEAR a non-critical file (rc0) -- discriminating, not flag-all/flag-none?",
        "fixture": {
            "sev1_path": "portal/src/pages/ModelPortfolios.tsx",          # POSITIVE control: registered SEV1 (asserted vs the registry at run-time)
            "noncritical_path": "org/modules/graph/comp_tool_health.py",  # the discrimination: NOT registered (asserted)
            "registry": "org/modules/graph/critical-surfaces.yaml",       # the INDEPENDENT oracle (read by the probe, never the tool's stdout)
        },
        "usability_timeout_s": 60,
        "expected": "effective",   # comp-surface-check detection is honest TODAY -> yes; the probe is the regression guard
        "live_estate": False,      # local/parent-scoped: path-match vs the registry; no AWS/S3/estate, no bd
    },
    {
        "probe_id": "comp-pipescript/io-dependency-traversal",
        "tool": "comp-pipescript",
        "tool_class": "gold-dag-io",
        # EFFECTIVE-axis probe for comp-pipescript (the gold-layer I/O-manifest / DAG tool, NON-preventive).
        # HONEST measurement (CTO~D 2026-07-12): does `comp-pipescript io <script>` genuinely SURFACE the
        # script's real I/O + dependency chain -- NOT a predetermined verdict. Scored on a DISCRIMINATING,
        # source-grounded fact (CTO~D refinement, the comp-freshness lesson): INF_A_04's READ INPUT KEY +
        # its PRODUCER edge, which appear in the io output ONLY IF pipescript traversed THIS script's deps
        # (a boilerplate header would false-match reach). ORACLE = INF_A_04's SOURCE directly (ACCOUNTS_DIM_
        # KEY:53 -> it reads gold/dimensions/accounts_dimension_latest.parquet, which INF_A_00 writes as its
        # OUTPUT_KEY) -- grounded OTHER than pipescript's own stdout (Rule 22a / FP-R0). pipescript DERIVES
        # this edge by source-parsing all gold scripts (not a stale graph cache), so it is robust; a genuine
        # graph-vintage miss would VOID (rc!=0 / usage error), never score a silent no. ISOLATION: the terms
        # are NOT in the run argv (the filename is INF_A_04.client_dimension.py; the write key "client_
        # dimension" is deliberately NOT an answer_term to avoid an argv leak). HONEST SCORING: today it
        # REACHES the read + producer edge -> yes->KEEP; a DAG-detection regression (missed read / dropped
        # producer edge) would score no->FIX (comp-pipescript is non-preventive -> the flip is real).
        "question": "Does `comp-pipescript io INF_A_04` surface its REAL read input (accounts_dimension_latest.parquet) AND the producer edge (<- INF_A_00), from source?",
        "run": ["comp-pipescript", "io", "data/inf/scripts/gold/INF_A_04.client_dimension.py"],
        "answer_terms": ["accounts_dimension_latest.parquet", "INF_A_00"],
        "reach_threshold": 2,      # BOTH the read input AND its producer edge -> a real dependency traversal, not a header
        "usable_returncodes": [0],
        "expected": "effective",   # comp-pipescript's gold-DAG traversal is correct TODAY -> yes (HONEST result, not a target); regression guard
        "live_estate": False,      # local: pipescript source-parses gold scripts; no AWS estate; inf script only -> sovereign trivially green
    },
    {
        "probe_id": "comp-kuzu/cloud-estate-query-reach",
        "tool": "comp-kuzu",
        "tool_class": "cloud-estate-graph-query",
        "kind": "kuzu-discrimination",
        # EFFECTIVE-axis probe for comp-kuzu (the GLOBGRPH cloud-estate graph query tool, NON-preventive).
        # HONEST QUERY-REACH measurement (CTO~D B2 + 4-case refinement 2026-07-12): does a reasonable,
        # correct-dialect targeted query REACH an edge that IS confirmed in the graph? The 4-case runner
        # SEPARATES comp-kuzu's reach from GLOBGRPH's ingestion coverage -- confirmed+found->yes / confirmed+
        # missed(current)->no (a REAL query-reach/dialect failure, the .id-vs-.name class) / NOT-ingested->
        # VOID (ingestion gap, not the tool's fault) / BEHIND|UNKNOWN+miss->VOID. ORACLE grounded from SOURCE
        # independently of comp-kuzu: inf-gold-layer-runner (inf-pipeline/ec2.tf:6 -- the dedicated inf gold
        # EC2 runner, instance i-0ed5afded2ebd4ed4) WRITES opal-data-inf, confirmed-in-graph by confirm_query.
        # SOVEREIGN: the queries are IN-SCOPE inf BY DESIGN (comp-kuzu is whole-estate) + the runner's held-
        # marker guard; never bd/schwab/49F. VINTAGE: the runner reads the stderr provenance header (a
        # BEHIND/UNKNOWN + miss VOIDs). ISOLATION: the answer_term (inf-gold-layer-runner) is NOT in the
        # target_query -> it appears in the RESULT only on a real traversal (the .id-vs-.name reach lesson).
        "question": "Does a reasonable targeted comp-kuzu query REACH the confirmed-in-graph edge inf-gold-layer-runner WRITES opal-data-inf?",
        "fixture": {
            "confirm_query": "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE a.name='inf-gold-layer-runner' AND b.name='opal-data-inf' AND e.edge_type='WRITES' RETURN b.name",
            "confirm_expect": "opal-data-inf",   # the specific edge is ingested iff the confirm result is non-empty
            "target_query": "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE b.name='opal-data-inf' AND e.edge_type='WRITES' AND a.node_type='EC2_INSTANCE' RETURN a.name",
            "answer_term": "inf-gold-layer-runner",   # NOT in the target_query -> result-only (isolation-clean)
        },
        "usability_timeout_s": 150,   # each comp-kuzu invocation reloads the Kuzu DB (~30-60s); this runs 2 queries
        "expected": "effective",   # comp-kuzu's query engine reaches a well-formed query TODAY -> yes (HONEST result); the probe is the query-reach regression guard
        "live_estate": True,       # reads the canonical Kuzu DB (local file, no AWS call); in-scope inf query only
    },
    {
        "probe_id": "comp-blast/impact-reach-discrimination",
        "tool": "comp-blast",
        "tool_class": "impact-blast-radius",
        "kind": "blast-discrimination",
        # EFFECTIVE-axis probe for comp-blast (the "what breaks if I change X" impact tool, NON-preventive).
        # HONEST IMPACT-REACH (CTO~D B2 2026-07-12): does the downstream blast radius of gold:INF_A_00.
        # accounts_dimension REACH a KNOWN downstream dependent grounded from SOURCE? comp-blast is graph-
        # backed (like comp-kuzu) -> the runner SEPARATES reach from graph coverage: NOT-FOUND -> VOID (a
        # graph-coverage/staleness issue -- comp-blast is itself honest here, "a NOT-FOUND, not a 'nothing
        # breaks' clear"), NEVER a silent reach 'no'. ORACLE: INF_A_00.accounts_dimension is consumed by
        # INF_C_00.canonical_performance (+ INF_A_04/C_02/C_03/C_05) -- the accounts_dimension.advisor_key
        # readers named in INF_A_00's OWN source comment, INDEPENDENT of comp-blast. answer_term
        # INF_C_00.canonical_performance is NOT in the query (gold:INF_A_00...) -> result-only (isolation-
        # clean); a boilerplate would not name a specific downstream. SOVEREIGN: in-scope inf node BY DESIGN
        # + the runner's held-marker guard. NON-preventive -> the effective bool flips KEEP<->FIX.
        "question": "Does comp-blast's downstream radius of gold:INF_A_00.accounts_dimension REACH the source-grounded consumer INF_C_00.canonical_performance?",
        "fixture": {
            "query": "gold:INF_A_00.accounts_dimension",
            "answer_term": "INF_C_00.canonical_performance",   # source-grounded consumer, NOT in the query
        },
        "usability_timeout_s": 150,   # comp-blast builds the trace graph on-demand (~34s)
        "expected": "effective",   # comp-blast's impact traversal is correct TODAY -> yes (HONEST result); the probe is the impact-reach regression guard
        "live_estate": False,      # local trace-graph build over repo source; no AWS; inf node only -> sovereign green
    },
    {
        "probe_id": "comp-trace/upstream-reach-discrimination",
        "tool": "comp-trace",
        "tool_class": "dependency-path-trace",
        "kind": "graphreach-discrimination",
        # EFFECTIVE-axis probe for comp-trace (bidirectional dependency PATH walk, NON-preventive). HONEST
        # REACH (CTO~D batch 2026-07-12): does an UPSTREAM trace of gold:INF_A_04.client_dimension REACH its
        # real producer INF_A_00.accounts_dimension? Graph-backed -> NOT-FOUND / "Multiple matches" ->
        # VOID (graph coverage/ambiguity, not a reach miss). ORACLE from source (INF_A_04 reads
        # accounts_dimension_latest :53, produced by INF_A_00 :90), independent of comp-trace. answer_term
        # INF_A_00.accounts_dimension NOT in the query (gold:INF_A_04...) -> result-only. --all avoids the
        # prefix-multiple-match ambiguity. SOVEREIGN: in-scope inf node + held-marker guard.
        "question": "Does comp-trace UPSTREAM of gold:INF_A_04.client_dimension REACH its real producer INF_A_00.accounts_dimension?",
        "fixture": {
            "cli_args": ["trace", "gold:INF_A_04.client_dimension", "--direction", "up", "--all"],
            "answer_term": "INF_A_00.accounts_dimension",
            "void_markers": ["Multiple matches for"],
            "oracle_note": "INF_A_04 reads accounts_dimension_latest (source :53) produced by INF_A_00 (:90); independent of comp-trace",
        },
        "usability_timeout_s": 150,   # comp-trace builds the trace graph on-demand (~34s)
        "expected": "effective",   # comp-trace's path walk reaches the real producer TODAY -> yes (HONEST); regression guard
        "live_estate": False,      # local trace-graph build over repo source; no AWS; inf node only -> sovereign green
    },
    {
        "probe_id": "comp-xref/symbol-reference-reach-discrimination",
        "tool": "comp-xref",
        "tool_class": "symbol-cross-reference",
        "kind": "graphreach-discrimination",
        # EFFECTIVE-axis probe for comp-xref (SYMBOL cross-ref -- where is X referenced, NON-preventive).
        # HONEST REACH (CTO~D batch 2026-07-12): does an xref of the accounts_dimension_latest S3 key REACH
        # a real reader (INF_C_00.canonical_performance)? Graph-backed -> NOT-FOUND -> VOID (graph coverage,
        # not a reach miss). ORACLE from source (INF_C_00.canonical_performance's OWN code reads
        # accounts_dimension; also named in INF_A_00's advisor-of-record reader comment), independent of
        # comp-xref. answer_term INF_C_00.canonical_performance NOT in the query (accounts_dimension_latest
        # .parquet) -> result-only. SOVEREIGN: in-scope inf key + held-marker guard.
        "question": "Does comp-xref of accounts_dimension_latest.parquet REACH its real reader INF_C_00.canonical_performance?",
        "fixture": {
            "cli_args": ["xref", "accounts_dimension_latest.parquet"],
            "answer_term": "INF_C_00.canonical_performance",
            "oracle_note": "INF_C_00.canonical_performance reads accounts_dimension (consumer's own source); independent of comp-xref",
        },
        "usability_timeout_s": 150,   # comp-xref builds the trace graph on-demand (~34s)
        "expected": "effective",   # comp-xref's symbol lookup reaches the real reader TODAY -> yes (HONEST); regression guard
        "live_estate": False,      # local trace-graph build over repo source; no AWS; inf key only -> sovereign green
    },
]


def _scratch_uri(p: dict) -> str | None:
    """The scratch write-target a discrimination probe stages its fixture at (for the sovereign assert)."""
    fx = p.get("fixture")
    if not fx:
        return None
    return "s3://%s/%s" % (fx.get("scratch_bucket", ""), fx.get("scratch_prefix", ""))


def assert_sovereign_safe(probe_list: list | None = None) -> None:
    """SOVEREIGN-SAFE BY CONSTRUCTION (CTO 2026-07-12): NO probe may target a held bd/schwab path or bucket
    -- not in its `run` argv, not in its discrimination fixture scratch target. A held target would make the
    recurring probe read opal-data-bd on a re-run. This fails the corpus LOAD (never a silent bd read), and
    is the same canonical sovereign_held predicate the whole estate uses. Vigilance-independent."""
    offenders = []
    for p in (probe_list if probe_list is not None else TOOL_PROBES):
        for tok in list(p.get("run", [])):
            s = str(tok)
            if is_held_path(s) or is_held_bucket(s):
                offenders.append("%s run: %s" % (p.get("probe_id"), s))
        su = _scratch_uri(p)
        if su and (is_held_path(su) or is_held_bucket(su)):
            offenders.append("%s scratch: %s" % (p.get("probe_id"), su))
        # iam-discrimination fixtures carry ARNs (role + resources), not a scratch uri -- assert none is bd.
        fx = p.get("fixture") or {}
        for fld in ("role_arn", "held_resource", "notheld_resource"):
            s = str(fx.get(fld, ""))
            if s and (is_held_path(s) or is_held_bucket(s)):
                offenders.append("%s %s: %s" % (p.get("probe_id"), fld, s))
    if offenders:
        raise ValueError("SOVEREIGN VIOLATION -- probe corpus targets a held bd/schwab path (re-point to "
                         "inf/cot/mdpf):\n  " + "\n  ".join(offenders))


def probes() -> list:
    """All probe dicts (the corpus). Sovereign-asserted on every access -- a held target fails the load."""
    assert_sovereign_safe()
    return list(TOOL_PROBES)


def solver_visible_fields() -> tuple:
    """Probe fields the tool-run MAY see. ONLY the question + the invocation -- NEVER the answer or the
    self-test `expected` label. (Mirror of corpus.solver_visible_fields for the B1 isolation invariant.)"""
    return ("probe_id", "tool", "tool_class", "question", "run", "usability_timeout_s", "live_estate")


def sealed_fields() -> tuple:
    """Judge-only fields -- NEVER folded into the tool-run payload (the sealed answer + the self-test
    label). tool_probe.probe_payload proves these do not leak into what the tool sees. For a discrimination
    probe the tool run is `comp-freshness artifact <fixture s3 uri>` (built dynamically) and the VERDICT is
    the tool's RC (0=PASS => false-GREEN on the frozen fixture; 1=FAIL/STALE => caught) -- so the judge
    criterion is sealed by construction (never in the run argv, and never a substring of the tool's own
    stdout, which would false-match a `fail_at_h` column header); the tool must DERIVE freshness from the
    artifact content, not be told the verdict."""
    return ("answer_terms", "answer_substr", "reach_threshold", "expected")
