# ANDREW-DIRECT — OPAL_LCLRPO: workspace polish (cold-material archival + function canonization)

**Received:** 2026-07-15 ~19:1xZ (US ET ~3:1x PM), direct terminal prompt to `0.0.0_AB_MSTR`,
while the NFRA_GRAPHFEED wave (LD-0299) runs at 0.8.0~Z.

**VERBATIM:**

> "While 0.8.0_AE makes their way through that project, I have a different project I need from
> you. I would call it OPAL_LCLRPO. The premise is we want to polish up the ajb_workspace
> significantly. There are several components of this. First we want to either get rid of, or
> /archive, material we dont actively use. ANything that hasn't been touched in 4 months is
> likely not important for us. I believe we can use our comp tools to establish file edits for
> filesystem heat to identify what is untouched. I see folders like /goldfish and so on that
> have never been used. There is a lot of junk floating around and we need to tighten up
> significantly. With that in mind, we want to start canonizing a lot of our functions, this
> work will be hand in hand with this new project that CTO is going to create OPAL_STNDRD,
> based off this document: BRIEF_CONSOLIDATION_RESOURCE_STANDARDIZATION_20260715.md."

**Reading (MSTR, operational — scope surfaced, not adjudicated):**
1. **OPAL_LCLRPO is MSTR-owned** ("I need from you"), running in parallel with NFRA_GRAPHFEED.
2. Component A — **cold-material archival**: identify everything untouched ~4 months
   (≈ pre-2026-03-15) via the comp heat tools (comp-heat freshness = the purpose-built
   instrument: per-path hot/warm/cold + ranked COLD SUBTREES); disposition = remove OR archive
   (root `archive/` convention exists). Named example: `goldfish/` (root, never used).
3. Component B — **function canonization**, hand-in-hand with CTO's forthcoming **OPAL_STNDRD**
   per `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/BRIEF_CONSOLIDATION_RESOURCE_STANDARDIZATION_20260715.md`.
4. Standing law that binds the execution: never-auto-delete + blast-radius verify-before-
   recommend (comp-heat/DEBTSCAN doctrine); recursive deletion = human-confirm class (CLAUDE.md
   Agent Autonomy); shared-worktree discipline (live agents mid-flight; moves coordinate via
   comp-blast + cross-domain MCP); git mv to preserve history on archives.

---

## FOLLOW-ON ANDREW-DIRECT — 2026-07-15 ~19:4xZ (owners-before-Batch-1)

**VERBATIM:**

> "I think we first need to decide who those lane owners are so we have them spawned, then once
> that is established, we can proceed Batch-1"

**THE OWNER MAP (decided from `.owned-paths.yaml`, the authoritative lane registry):**

| Family | Registry lane | Named owner | Live at decision |
|---|---|---|---|
| goldfish/ | BASE_EXEC | CTO + COO co-ack | LIVE |
| tools/* legacy, research/, timeseries*, tests/cloudfront, docs legacy sets, org/daily_log | ANY (intentionally multi-agent; no single owner) | CUSTODIAL: MSTR executes, CTO+COO ack | LIVE |
| infra legacy (orchestration/testing/prompts/linting) + infra/aws/lambda/market_query + infra/aws docs/scripts junk | CLOUD_OPS_OR_ETL (infra/** catch-all) | 0.7.0_AE_CloudOps | LIVE |
| infra/architectural_docs/ | ANY_EXEC_OR_AE | 1.0.0_SA_CTO | LIVE |
| data/smartx/ (VERIFY-class, not Batch-1) | SHARED_OPAL_ETL | 0.5.0_AE_OpalETL | LIVE |
| data/yang_pkl/ (held on Andrew ask #3) | POD2 | 0.2.0_DT_PortfolioAnalytics | LIVE |
| timeseries/ deployed-verification (VC) | — (source-map hit) | 0.7.0_AE_CloudOps verifies | LIVE |
| **data/seeking-alpha/** | **POD1** | **0.1.0_DS_MarketIntelligence — POD1 entirely DOWN → SPAWN required** | **NOT LIVE** |

**Execution:** spawn `0.1.0_DS_MarketIntelligence` (the one missing owner); clearance RAVC to
every named owner; Batch-1 (source-map-clear families only) proceeds on ACKs per Andrew's
"once that is established, we can proceed Batch-1". B2 deletions + yang_pkl still await
Andrew's words (asks #2/#3 open).

---

## SOVEREIGN CLEARANCE — 2026-07-15 ~20:1xZ (data/seeking-alpha; POD1 clearance waived)

**VERBATIM:**

> "We dont need 0.1.0_DS to tell you about data/seeking-alpha/ i can tell you as sovereign we
> dont need that"

**Effect:** `data/seeking-alpha/` (73 files) is SOVEREIGN-CLEARED for Batch-1. Disposition stays
ARCHIVE (reversible git mv) per the standing batch discipline — "we dont need that" is the
clearance; a DELETE of the archived copy can ride the B2 word later if wanted. The
0.1.0_DS_MarketIntelligence clearance ask is MOOT; the lane (spawned ~20:0xZ solely for this)
STANDS DOWN — MSTR kill + COO informed (supersedes the route-or-stand-down COO was holding).
