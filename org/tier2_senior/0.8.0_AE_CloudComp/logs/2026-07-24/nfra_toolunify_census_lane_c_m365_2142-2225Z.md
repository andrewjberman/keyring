# NFRA_TOOLUNIFY census — Lane §2.C M365/Microsoft surface (session log)

**archetype:** TRACE
**secondary_archetypes:** EXPLORE (live-state grounding across gateway/graph/heat/taxonomy), SCRIBE (deliverable authoring)
**Agent:** 0.8.0_AE_CloudComp~C | **Date:** 2026-07-24 | **Window:** ~21:42–22:25Z
**Dispatch:** `1.0.0_SA_CTO~Z` DISPATCH NFRA_TOOLUNIFY census — LANE M365, ACK'd 214406Z
**Deliverable (disk-only, CTO~Z owns the commit per their 221705Z policy note):**
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/C.md` + `C.sidecar.json`

## What happened

Fresh-session startup (watcher self-heal, register, `/cloud-ops`, `org/XXX.md` protocol) surfaced a
same-fabric DISPATCH before Step 2 logs finished: 5-lane read-only estate census under
`1.0.0_SA_CTO~Z` (off-main-fabric, per `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md`).
My scope (§2.C): determine whether M365 is a real plane or a stub in the estate.

Grounded via this lane's own prior build history (NFRA_MSGRAPH S1–S3, 06-26 through 07-15/16/17 logs
+ deliverables, all self-authored) plus live state pulled fresh this session — comp-kuzu (current
vintage, 4.0h old), live S3 object listings (UTC via `s3api`, not the local-time-mangled CLI `ls`),
live CloudWatch/Lambda sweeps, and a live `comp-which`/`comp-heat --help` check. Read gateway source
(`tools.py`, `graph.py`, README) as static census, never invoked a live `mcp__m365__*` tool or Graph
call (vendor-egress discipline + census BINDING §2 held throughout).

**Headline finding:** the graph-ingestion substrate is live and growing (5,669 `layer='ms'` nodes,
+149 in 9 days) and deliberately narrow-scoped (one SharePoint site, by a recorded Andrew decision —
not a stall). The heat analytic built on top of it (`ms_heat`/`ms_heat_snap`) is real but has been
dormant for 7 days with zero scheduled trigger anywhere in the repo, and its 07-16 "born healthy"
freshness alarm no longer exists in live AWS (0 matching alarms, 0 matching Lambda functions,
live-checked twice). The project's own stated headline deliverable — S4 agent-findability tooling
(`comp-ms-find` / a `comp-which` MS route) — was never shipped: live-checked this session, `comp-which`
returns zero curated matches for an MS/SharePoint findability question. This is the most parsimonious
explanation for the heat analytic's dormancy: its only consumer never got built. Also found: the
canonical GLOBGRPH 7-layer taxonomy (`docs/architecture/NFRA_GLOBGRPH_PRD.md` §1) does not include M365
as a declared layer at all — it rides in as a `layer='ms'` property value on the shared `CloudNode`
label, structurally present but taxonomically undocumented. A 2026-06-26 RESCOPE proposal to generalize
MS-heat into an estate-wide `heat_index` was never implemented (no such table found; the 07-17
decommission-tooling assessment, same lane, independently re-derives the identical gap three weeks
later). Full detail, denominators, and the could-not-determine list are in the deliverable.

Mid-task, `1.0.0_SA_CTO~Z` sent a deliverable-commit-policy note (221705Z): `org/tier1_exec/1.0.0_SA_CTO/**`
is owned-paths-gated to their BASE_EXEC lane — write to disk + notify, they consolidate the commit.
Honored: both files written, nothing staged/committed on that path, no `--author` override attempted.

## Compiler Tools

| `<run>` | Observed output | Verdict |
|---|---|---|
| `comp-kuzu "MATCH (n:CloudNode) WHERE n.layer='ms' RETURN n.node_type, count(*)..."` | provenance `current` (pin==marker HEAD), age 4.0h; MS_FILE 4618/MS_FOLDER 1034/MS_USER 15/MS_SITE 1/MS_LIBRARY 1 = 5,669 total | OK — the load-bearing live-population number for the verdict. |
| `.tools/comp-heat --help` | subcommands `{freshness,drift,score,federated}` — estate OBJECT/git write-freshness, explicitly distinct from `comp-freshness` (data-pipeline) | **GAP finding** — the dispatch's suggested METHOD tool does not actually cover `ms_heat`; pivoted to direct source-read + live S3/CloudWatch/Lambda primitives instead (comp-tool-first, raw-call-verifies, two-stage discipline). Logged for the ~D tool-census lane, not chased further myself. |
| `.tools/comp-which "find documents in the shared sharepoint site by heat or recency"` | "NO CURATED RULE MATCHED... FUZZY GUESSES, not a routing decision"; top score 0.47 (comp-cache, unrelated) | OK — this IS the finding: confirms S4 (comp-ms-find) never shipped, live, first-hand. |
| `aws s3api list-objects-v2 --bucket opal-313476888478-globgrph --prefix warehouse/ms_heat/` (via `.tools/aws` shim) | latest object 2026-07-17T18:09:45Z (UTC, explicit) | OK — grounds the 7-day dormancy without the local-time `s3 ls` mangle (Verification Law 11). |
| `aws cloudwatch describe-alarms --alarm-name-prefix opal-globgrph-freshness` | `[]` (empty, twice: exact name then prefix sweep) | OK — clean negative, corroborated by a second independent check (0 Lambda functions matching `freshness`). |
| pyiceberg direct `RestCatalog` load of `ms_heat_snap` | `nessie.opal-globgrph.local:19120` — VPC-internal private DNS, unreachable from this session | Expected miss, disclosed as could-not-determine rather than silently dropped; S3 JSON mirror used as the corroborating proxy instead. |
| `git rev-parse HEAD` | `9da59d7cede73ecb0509e14ac347142dedc31047` | OK — vintage stamp for the whole report. |

No comp-tool gap blocked the census; the one real gap (`comp-heat` not covering `ms_heat`) was routed
around with source + live primitives per the two-stage discipline the census plan itself mandates.

## RAVC / next

- ACK sent 214406Z on receipt. Deliverable + sidecar written to disk this window; NOTIFY going to
  `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` this same turn with headline findings (per their commit-policy
  note — they consolidate into their owned lane).
- **CTO~Z committed @`2cd5f023e`** 222630Z: positive feedback, both structural findings (undeclared-layer
  ontology gap + dormant-heat-no-consumer) marked load-bearing for the unity architecture.
- **CVO~Z independent verification PASS** 222709Z: re-derived 3/4 claims exact-to-source (node count
  5,669 digit-for-digit; `comp-ms-find` structurally absent across the full 91-tool set, not merely
  unrouted; the undeclared-layer finding confirmed at the PRD's own schema line
  `NFRA_GLOBGRPH_PRD.md:210`) and elevated the undeclared-layer finding to "the biggest thing in this
  lane" / an ontology-level finding, not an M365 curiosity — flagging it to CTO~Z as such. Correctly
  declined to certify claim #4 ("zero scheduled trigger") as independently negative-proved — corroborated
  via their own source-read, but proving an absence needs the search space enumerated, not an
  absence-of-instance. Fair; nothing-to-rework.
- **Closed the claim-#4 gap same window** (222709–223131Z): full EventBridge enumeration — 1 event bus
  (`default`), 141 rules total (0 duplicates, properly paginated after catching a `--query length(Rules)`
  per-page-under-auto-pagination trap that would have silently reported a 100-row floor), 0 rule names
  contain "heat" in any case. Cross-checked against the already-source-read `derive-runner-nightly` (the
  one plausible un-named host). Claim #4 upgraded from corroborated to independently proven. Addendum
  §6a added to `C.md` + `eventbridge_enumeration` block added to `C.sidecar.json` (both disk-only,
  CTO~Z's commit); both CTO~Z and CVO~Z notified 2231Z.
- **CVO~Z independently re-ran the enumeration** 223700Z: exact match (1 bus, 141 rules, 141 distinct, 0
  heat matches), formally upgraded claim #4 to PROVEN, lane CLOSED on their bar. Added one thing my run
  lacked: a **positive control on the listing itself** — re-querying for rules known to exist (the 4
  globgrph-prefixed ones), confirmed returned, which is what makes "0 heat matches" a MEASURED zero rather
  than a broken-query false negative. Also flagged my pagination-trap catch (`--query length(Rules)`
  applying per-page under CLI auto-pagination, yielding a plausible-wrong 100-then-41 instead of the true
  141) as a general estate hazard worth escalating into CTO~Z's consolidated method section.
- **Folded both into the deliverable same window** (223700–223812Z): §6a of `C.md` now states the
  positive control explicitly + a suggested one-line method-section addition; `C.sidecar.json` gained a
  `positive_control` block crediting CVO~Z. Both CTO~Z and CVO~Z notified 2238Z; CTO~Z's escalation-or-not
  call left to them (not mine to insert into a doc I don't own).
- No blockers. Status: **lane CLOSED, hardened twice past the initial PASS** — CVO~Z independent
  re-derivation + a positive control now on record, CTO~Z has the full addendum chain. Standing by,
  event-driven, isolated census group (no main-fabric contact), for any further CTO~Z dispatch in this
  census.
