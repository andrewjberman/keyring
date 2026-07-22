# MDPF_3FIRMS PRD authored + registered; MDPF_REVAMP superseded — session 1816–19:1xZ

**archetype:** MIXED (EXPLORE → SCRIBE)
**Author:** `1.0.0_SA_CTO` | **Commit:** `88c80b003` (pushed CLOUD)

## What happened

1. **Startup under the LD-0333 restart** (@e064ce80f): predecessor's registration was a dead-PID
   leftover (7560, process gone) — re-registered PID 7176, Monitor `b8y7gi8rh` armed + exercised by a
   live delivery inside a minute. LD-0290 serial written. Zero crons.
2. **Hold mechanics executed as the single authorization path:** retracted my own 181903Z PROCEED to
   0.8.0 ([STOP], clock collision ~60s); withdrew COO's pre-hold WS-5 TF apply GO + Andrew's 1425Z D2
   GO at 0.7.0 (agent NOT REGISTERED = dead; hazard inert; withdrawal sits unread at his inbox root —
   luck, not a control; respawner must point him at it before any apply). Open-deploy ledger read
   4/4 HELD-SOVEREIGN-GATED — no stranded leg, NEVER#5 not in tension. 0.8.0 stand-down validated
   clean (last commit 18:17:24Z vs hold ~18:19Z).
3. **Andrew advisory landed (~18:5xZ): create MDPF_3FIRMS superseding MDPF_REVAMP.** Researched at
   max fidelity (Andrew switched the session to Fable/max mid-research), authored + committed:
   - `docs/architecture/MDPF_3FIRMS_PRD.md` v1.0 — fee-basis law (Global radial = full(49F) +
     model(INF) + model(COT), basis-labelled), 6-leg grounded channel census, RF-1..RF-15 roll-forward
     ledger, firm-registry architecture (one enumeration, 7 hardcoded consumer sites today),
     WS-B/S/G/P/F with TO candidates + compiler mandates, sequencing per the advisory (B→S per-leg
     pipeline; G gated on ALL B+S with the null-composition decision FIRST per CVO STOP-BEFORE-BUILD;
     P builds on G; F = one flip, Cottonwood inside, single binding pin at END).
   - `org/projects/MDPF_3FIRMS.json` + first-ever REGISTRY rows for both (REVAMP was JSON-only —
     RF-15 drift closed).
   - `MDPF_REVAMP.json` → complete-as-superseded 2026-07-22, 2-step atomic in the same commit.

## Load-bearing findings (each changed the PRD)

- **Cottonwood zero-date-overlap resolved to mechanism:** DS measured holdings (06-09..07-20) vs
  assignment (07-21..22) sharing zero dates and correctly declined to guess. Bronze object stamps show
  `HOLDINGS_DAILY_{D}.xlsx` lands D+1 ~03:30Z — the series are ADJACENT, not disjoint; first overlap
  07-21 lands tonight on the standing schedule. 3F-B5 is verification, not repair.
- **Schedule census (applied truth):** all six legs live+ENABLED except — no smartx-named ingest rule
  (mechanism exists, partitions current through today; 3F-B2 names it) and no visible eclipse puller
  rule (3F-B4).
- **DDB `opal-assets-daily-aua`:** 588 rows, run_date×cohort_id, in-row dual-purpose staleness
  contract (99 = sentinel shared with 14 live alarms — never "cleaned" without them); SMA cohort rows
  exist → A4-consistency check named in 3F-G5.
- **DS's "tooling not equipped" claim reviewed (Andrew's ask):** it is a REAL runner-IAM denial on
  `blackdiamond/cottonwood/silver/*` (grant enumerates five ARNs), not a tooling defect; §3.1 answers
  DS's architectural question — silver IS the canonical firm-total source for all three firms; the fix
  is the grant (3F-S3, Rule 22a verification specified).
- **Server-vs-client (Andrew's suspicion "all client-side"):** REFUTED for trend/distribution —
  per-firm artifacts are served at `/api/general/mdpf/{firmId}/*` and Global is its own artifact; FE
  computes derivations on top. Complete locus table = 3F-P1.
- **`PUBLISH_MAP` 9-entry hardcode confirmed at `opal-assets-mdpf-portal-publisher/lambda_function.py:37`.**

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-surface-check check` | CRITICAL SEV1 model_portfolios.headline/.benchmark via ModelPortfolios.tsx — §8.7 mandate on every FE TO |
| `comp-cache collisions` | no mdpf-family collisions |
| `pipescript model-portfolios` | 8 threads; MA-08 orphan (out of scope); YANG stays phase-2 |
| `comp-glob` / `comp-grep` ×7 | producer/dispatcher/publisher/crosswalk located; PUBLISH_MAP:37; FE scoping mechanics; DS claims found |
| `comp-which` | routed the pipeline question to comp-surface-check |
| raw `aws` (rail-marked ×5) | EventBridge schedule census; S3 depth probes ×6 legs; DDB describe+scan; cottonwood bronze tails |

## Open at session state

- **COO decomposition HELD pending Andrew's cascade GO** (LD-0333 single-path). Handoff briefing
  delivered in-chat, dispatch withheld.
- Open decisions D-1..D-5 staged at Andrew in PRD §6 (none block WS-B/WS-S).
- 0.7.0 dead with GOs withdrawn (respawn note above); 0.8.0 holding with two intact uncommitted
  changesets (his comp-iam vintage gate: REFUSE proven / ACCEPT unproven — first item on resume).
