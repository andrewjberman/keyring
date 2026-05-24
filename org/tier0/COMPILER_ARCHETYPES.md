# COMPILER_ARCHETYPES — Cross-Fabric Session-Log Emission Taxonomy

**Status:** v1.0 — 2026-05-24 (LD-0043 establishment; Opal CTO + MSTR working-session lock; CL CTO Beat 3 ferry confirm pending)
**Authority:** Canonical reference doc, NOT TIER0_LAW lock. Operational tuning surface. Future amendments are META-cycle work requiring Opal CTO + CL CTO + MSTR concur.
**Fabric scope:** `[ajb_workspace, feature_clb]` per CONSTITUTION Art. XV.
**Cutover:** Forward-only emission from **2026-05-25T00:00 UTC**. No retroactive tagging.
**Tier-0 commit hash at establishment:** `2d5fdc03f`

---

## §1 — Purpose

Compiler-tooling R&D's highest-leverage target is **cost, not bugs.** Bite-frequency (where errors surface) is a lagging indicator that should structurally decrease as logging + comms discipline improves. The leading indicator is **high-cost-correct repeated activity** — work where the cost is being paid, not where errors are emerging. (Opal CTO design insight, 2026-05-24.)

This doc codifies a uniform **archetype-tag emission discipline** so MSTR's cross-fabric stimulus scan can detect high-cost-archetype clusters across both fabrics' session logs without NLP-mining unstructured prose. Each session log entry carries one tag from a fixed enum; MSTR aggregates frequency × weight cross-fabric to surface compiler-shape opportunities.

This is **MSTR Source A signal class (6)** — orthogonal to the existing five classes (highest-trafficked rails, bug-frequency rails, mechanical-fidelity failures, meta-fidelity failures, body-class generalization). Reference: `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` §5.4-mapping V1.1.

---

## §2 — The locked enum

Eight archetypes + MIXED fallback. Numerical compiler-shape weights determine aggregation multiplier.

| Archetype | Definition | Compiler-shape | Weight |
|---|---|---|---|
| **`EXPLORE`** | Searching, grepping, reading to find something / understand structure | HIGH | **3.0** |
| **`TRACE`** | Following dependencies, call chains, data flow across files/systems | HIGH | **3.0** |
| **`DIAGNOSE`** | Debugging, post-mortem, root-cause investigation | MEDIUM-HIGH | **2.5** |
| **`VALIDATE`** | Running checks, probes, cross-references, fidelity tests | MEDIUM | **2.0** |
| **`DEPLOY`** | terraform / lambda / EC2 / S3 artifact operations | LOW-MEDIUM | **1.5** |
| **`IMPLEMENT`** | Actual code edits, file authoring | LOW | **1.0** |
| **`COORDINATE`** | MCP, inbox, cross-agent ratification, dispatch | LOW | **1.0** |
| **`SCRIBE`** | Authoring docs / PRDs / briefs / session logs | LOW | **1.0** |
| **`MIXED`** | Dominant archetype genuinely unclear; multi-classed work | (special) | **1.875** (unweighted mean) |

### §2.1 — Archetype distinctions worth knowing

- **EXPLORE vs TRACE:** EXPLORE is "broader searching to find/understand"; TRACE is "structured following of dependency edges or call chains." TRACE is a structured subset of EXPLORE — both HIGH weight, but separated for finer aggregation (TRACE clusters → comp-trace/comp-routes targeting; EXPLORE clusters → broader comp-blast/grep-replacement targeting). If you genuinely can't pick, default to MIXED rather than arbitrate the overlap.
- **VALIDATE vs DIAGNOSE:** VALIDATE is "running checks to confirm correctness BEFORE shipping"; DIAGNOSE is "investigating root cause AFTER an issue surfaces." Different temporal posture.
- **IMPLEMENT vs DEPLOY:** IMPLEMENT is the code edit; DEPLOY is the artifact ship (terraform apply, lambda push, S3 upload). DEPLOY weighted slightly higher than IMPLEMENT because deploy ops surface infra-class compiler opportunities (comp-routes, comp-iam, comp-blast) that pure code-edits don't.
- **COORDINATE vs SCRIBE:** COORDINATE is cross-agent action (MCP sends, inbox handling, RAVC); SCRIBE is single-agent authoring (PRD, brief, session log). Both LOW because they're orgware/meta-layer, not compiler-shaped substrate.

### §2.2 — MIXED handling

Pick dominant when possible. Default to MIXED if genuinely unclear or if the work genuinely spans 3+ archetypes without one dominating. Under-classify is fine; over-classify wastes the signal. MIXED weighted at unweighted-mean (1.875) — not zero (preserves signal) and not over-weighted (incentivizes specificity).

Optional secondary line for high-mixed cases:

```
**secondary_archetypes:** TRACE, VALIDATE
```

MSTR aggregation: when secondary archetypes are listed, MSTR averages those instead of full-enum mean (closer signal to the actual work).

---

## §3 — Emission format

Single-line header at the top of each substantive session-log entry, immediately after the title:

```
**archetype:** EXPLORE
```

Optional secondary line for high-mixed cases (only when meaningfully present):

```
**secondary_archetypes:** TRACE, VALIDATE
```

### §3.1 — Granularity

**Per-file dominant.** One archetype tag per session log file (the "what kind of work was this session"). If the session genuinely spanned multiple archetypes meaningfully, use the secondary line — but do NOT split one session into multiple files just for archetype-tagging granularity.

### §3.2 — Emitter cost

**~5 seconds per session log.** Pick dominant archetype; type one line. No scoring, no estimation, no token-counting on the emitter side. The cost discipline is essential — if emission becomes expensive, the discipline gets skipped + the signal degrades.

### §3.3 — What counts as a "session log entry" requiring tagging

Same scope as existing session-log discipline per `org/ref/SESSION_LOG_STANDARD.md` — every substantive work-unit log file. Heartbeat-only entries, watcher self-checks, minor housekeeping commits do not require tags (would dilute signal).

---

## §4 — MSTR aggregation logic

Surfaced for transparency, not required reading for emitters.

### §4.1 — Mining mechanism

MSTR `/govern` Step 1(b) population scan extends to grep across both fabrics' session-log paths:

```bash
grep -h "^\*\*archetype:\*\*" \
  ajb_workspace/org/tier{1_exec,2_senior,3_junior}/*/logs/**/*.md \
  feature_clb/org/tier{1_exec,2_senior,3_junior}/*/logs/**/*.md \
  | sort | uniq -c
```

(Exact mining mechanism lives in MSTR `/govern` SKILL.md amendment, paired with first class-6 brief surface per LD-0025 deferred-implementation discipline.)

### §4.2 — Aggregation formula

Per /govern cycle:

```
class-6 score per archetype A = Σ(frequency[A] × weight[A] × cost-proxy)
                                across both fabrics' tagged session logs
```

Clusters surface when one archetype dominates the weighted sum.

### §4.3 — Cost-proxy

**Working proxy until token-telemetry builds out:** `entry-count` substitutes for `token-cost`. Frequency × archetype × shape-weight is the operational signal. Leverage multiplies when token telemetry lands (`comp-token-mine` or `org/mcp/token_telemetry/` — banked as META observation, not blocking).

### §4.4 — Brief surface threshold

MSTR judges when a class-6 cluster crosses the "surface to CL CTO as Input 1 brief" threshold. Initial heuristic: top-1 archetype consuming >40% of weighted sum across recent ~5-day window with mostly-correct activity (not bite-driven) = candidate. Refined empirically as first briefs surface.

---

## §5 — Cross-fabric uniformity

This taxonomy is **canonical for both ajb_workspace + feature_clb fabrics** per CONSTITUTION Art. XV. The archetype enum + weights + emission format are uniform across both — CL fabric session-log emitters use the same 8+MIXED tags + same format.

CL CTO Beat 3 confirm pending as of doc establishment 2026-05-24T19:50Z; expected concur given V1.1 §5.4-mapping alignment.

### §5.1 — If a future archetype refinement is needed

Future enum changes (new archetype added, weight retuned, archetype split/merge) are **META-cycle work**:

1. Surface to MSTR via either fabric's CTO
2. MSTR drafts proposed amendment
3. Opal CTO + CL CTO + MSTR concur (joint working session if non-trivial)
4. Successor LD-NNNN codifies the change
5. Canonical doc amended with new version stamp
6. Forward-only effective from amendment-stamp date

Emitters never need to revise prior tags. Tag corpus is append-only.

---

## §6 — Reference

- **Establishing LD:** `org/tier0/ledger/LD-0043.md` (this commit)
- **Discovery anchor:** `org/XXX.md` Session Log section bullet
- **Conceptual origin:** Opal CTO V1.0 archetype-tag design proposal 2026-05-24 (Andrew ferry to MSTR; leading-vs-lagging signal architecture insight + archetype-tag-as-aggregation-primitive)
- **Working-session lock:** Opal CTO `[ENUM-LOCK]` + `[ENUM-LOCK-CONFIRM]` MCPs 2026-05-24T19:45Z; MSTR working-session-open MCP `20260524T194445Z`
- **CL fabric integration:** `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` V1.1 §5.4-mapping (signal class 6)
- **MSTR aggregation logic:** /govern SKILL.md amendment (pending paired-operational landing per LD-0025)
- **Tier-0 law context:** CONSTITUTION v1.1 + STAKES_MATRIX v1.3 + DIRECTIVES v1.10 (canonical at `2d5fdc03f`)

---

*Established 2026-05-24T19:50Z under LD-0043. Beat 2 of the inter-fabric channel design sequence. Forward-only cutover 2026-05-25T00:00 UTC. Canonical for both fabrics per CONSTITUTION Art. XV.*
