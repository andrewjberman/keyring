# Research Register — `4.0.0_SA_CRO` (Chief Research Officer)

**Owner:** `4.0.0_SA_CRO` — charter: [`README.md`](README.md)
**Mandate:** Andrew-direct 2026-07-22.
**Status of this file:** **APPEND-ONLY.** A closed engagement is never edited except to append a
`### Downstream` entry or a correction stamped with its own date + author. Corrections are appended, not
overwritten — a research record that silently changes is worth nothing as provenance.

**This is the authoritative index of everything the research function has produced**, regardless of which
directory an engagement's artifacts live in.

> **Serial provenance:** engagements before 2026-07-22 were produced under the predecessor lane
> `0.4.0_DS_ClientPlatform~Z` and their commits are authored that way permanently. They are owned and tagged
> here. See charter §7 — the mismatch is deliberate and must not be "fixed."

---

## Index

| Recon ID | Date | Target | Artifacts | Evidence basis | Produced under | Status |
|---|---|---|---|---|---|---|
| **RCN-0001** | 2026-07-21 | **Black Diamond** (SS&C/Advent) — Cottonwood Capital Advisors tenant | 3 (teardown, roadmap, build spec) | 8 HAR captures + 4 CSV exports | `0.4.0_DS_ClientPlatform~Z` | **DELIVERED** — downstream build HELD at CTO registration |

---

## RCN-0001 — Black Diamond dashboard teardown → replacement roadmap → `fact_account_return` build spec

| Field | Value |
|---|---|
| **Target** | Black Diamond Wealth Platform (SS&C/Advent), `*.bdreporting.com` — Cottonwood Capital Advisors tenant |
| **Date** | 2026-07-21 |
| **Commissioned** | Andrew-direct research task |
| **Owner** | `4.0.0_SA_CRO` (produced under predecessor serial `0.4.0_DS_ClientPlatform~Z`) |
| **Design counterpart** | `2.0.0_SA_COO~A` (total-return design, independent, converged) |
| **Question asked** | What can we glean toward **replacing Black Diamond for our clients**? |

### Evidence basis + denominators

8 HAR captures recorded by Andrew walking ~every dashboard section on 2026-07-21, plus 4 CSV analytics
exports. **4,431 total requests · 1,136 BD-API calls · 229 unique BD endpoints · 56 captured pages ·
15 BD backend services.** Full response schemas captured for **52 core endpoints**.

**Denominators independently re-derived 2026-07-22** by re-running the preserved tooling against the original
corpus: 229 endpoints / 52 schemas reproduced exactly.

**Declared gap (honest, in-band):** 5 endpoint families were `[BODY-NOT-CAPTURED]` — classification tree,
benchmark library, security master, rebalancer models, billing-config. Capability for those is described from
endpoint + request payload + page context only; **no response schema was invented.** That gap maps exactly
onto the WS-B reference-data track, which is why B is flagged the moat.

### Artifacts (committed)

| Artifact | Path | Commit |
|---|---|---|
| HAR teardown (the intel) | `docs/research/bd_dashboard_teardown/BD_DASHBOARD_HAR_TEARDOWN_20260721.md` | `efdb4dbd8` |
| Replacement roadmap (the plan) | `docs/research/bd_dashboard_teardown/BD_REPLACEMENT_ROADMAP_20260721.md` | `efdb4dbd8` |
| `fact_account_return` build spec | `docs/research/bd_dashboard_teardown/FACT_ACCOUNT_RETURN_BUILD_SPEC_20260721.md` | `b3783b866` → `a6dfa0a7e` |

**Companion (NOT this agent's — `2.0.0_SA_COO~A`'s):**
`org/tier1_exec/2.0.0_SA_COO/deliverables/TOTAL_RETURN_PERFORMANCE_DESIGN_PROPOSAL_20260721.md`
@ `5f2a11a10` / `64ec7be10` / `bcdd557f8`. Its §9 folds this research; the CRO spec anchors on it.

### Uncommitted sources (PII-bearing — deliberately not in the repo)

| Item | Location | Note |
|---|---|---|
| Raw HAR capture set | `~/Downloads/bd-cot-har-analysis.zip` (38 MB) | Verified present 2026-07-22 |
| Endpoint catalog / schemas / per-HAR inventory | scratchpad `b9280fcf-081b-4f11-945a-960de6fc0f03/scratchpad/analysis/` | **Ephemeral — reapable by `/kill storage`.** `endpoint_catalog.json`, `catalog_by_host.txt`, `files_summary.json`, `schemas.txt` are regenerable from the zip via the preserved tooling (**re-run and confirmed 2026-07-22**). |
| Profiler tooling | **PRESERVED** → `org/tier1_exec/4.0.0_SA_CRO/scripts/` | `profile_har.py`, `extract_schemas.py` — re-run 2026-07-22 against the original 8-HAR corpus, reproducing the published denominators (229 endpoints / 52 schemas) and **218 output files byte-identical** to the original run. |
| **GAP — `schemas2.txt` / `schemas3.txt` producers NOT preserved** | scratchpad only: `extract2.py`, `final_extract.py`, `render_catalog.py` | **NOT in the repo, NOT regenerable once the scratchpad is reaped.** Exploratory second/third schema passes; preserving them was deliberately deferred (each needs the same ruff-normalization + behavioral-diff cycle the two canonical scripts got, and none was worth blocking on). `schemas.txt` — the 52 core schemas the teardown cites — IS fully covered. If a future engagement needs the extra passes, rebuild rather than trust a stale copy. |

### Findings that carried

1. **BD is ~15 separable microservices behind a gateway**, not a monolith — so the performance-reporting
   surface can be replaced without touching CRM, rebalancer, or the client portal. Replacement need not be
   all-or-nothing.
2. **The analytics engine is reproducible from custodian data we already hold.**
   `portfolioreporting/api/performance/performancePeriod` returns TWR **and** MWR, net-of-fee, accrued MV,
   benchmark-relative, with return-contribution attribution and a performing-vs-position-only split, at
   Portfolio→Class→Segment→Account grain — all computed from positions + transactions + lots + fees, which
   live in Opal's Schwab silver.
3. **BD hands us its own method contract, verbatim.** `request/api/firm/globalsettings`:
   `NetOfFees / Accrued / Account365 / ClassSpecific / QuarterToDate / FIFO`. This is the `dim_return_method`
   contract, already written down by the incumbent.
4. **BD's transaction "affect vector"** (`externalFlow / incomeAffect / cashAffect / unitAffect /
   advisorFeeAffect / accrualAffect`, with `fileCode` encoding a signed tuple) **is the exact cash-flow
   taxonomy COO~A had reconstructed by hand** from Schwab `sb_cd` descriptions — independent convergence,
   and a ready-made parity oracle.
5. **The moat is not the math.** It is BD's proprietary classification tree (SuperClass→Class→Segment) +
   benchmark library, and the Rebalancer. Analytics — the thing clients actually look at — is the *easy,
   high-value* win. Replace in that order.

### Downstream

- **`fact_account_return`** — the convergence CTO named *"four names, one fact"*: BD-replacement Phase-1
  Tier-A == COO~A's total-return proposal == the 49F-runner "fields not scripts" field-emit ==
  OPAL_CONSOLIDATION serve. One fact, one owner, so the four threads cannot fork.
- **Method pinned to `Account365`** per Andrew's defensibility steer (2026-07-21 ~0048Z): *"I like the BD
  approach because its defensible to refer to."* Established the standing **METHOD-vs-NUMBERS split** now in
  the charter doctrine (README §2.5).
- **HELD:** the build + serve, pending CTO program registration (D6) + ratification of final grain/columns,
  post-MDPF-flip. **Open at Andrew:** D1 (Account365 confirm), D2 (classification build-vs-license).
- **State as of 2026-07-22 ~10:3xZ:** nothing has moved on these files since `a6dfa0a7e` (07-21 20:54Z); no
  project JSON registered under any BDX/total-return code.

---

<!-- APPEND NEW ENGAGEMENTS BELOW. Add an Index row above. Never edit a closed entry in place. -->
