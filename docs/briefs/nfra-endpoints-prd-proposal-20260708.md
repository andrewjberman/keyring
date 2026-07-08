# NFRA_ENDPOINTS -- Proposal Brief (DS-authored, for CTO)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-07-08 · **Status:** PROPOSAL --
requesting CTO architect a PRD, not a build in itself.
**Origin:** Andrew-direct, following the `data/black_diamond/API/` catalog build
(same-session): *"write a briefing on this and send to CTO because they should
make a PRD, NFRA_ENDPOINTS, that basically is an organizational process in the
local directory where we implement this across each of the /data sources, e.g.
Orion Eclipse SmartX Schwab etc."*

---

## 1. What just happened (the proof-of-concept)

Investigating a Cottonwood mgmt-fee question (`docs/briefs/data-platform-d2b-bd-rest-endpoint-catalog-20260708.md`),
COO directed standing up a coherent vendor-API catalog for Black Diamond:
`data/black_diamond/API/`. The shape that resulted:

```
data/black_diamond/API/
├── README.md                          -- index/navigation
├── AUTHENTICATION.md                  -- the auth/session model
├── domains/
│   ├── {domain}/
│   │   ├── DOMAIN.md                  -- what this sub-app/module is, how it was found
│   │   └── endpoints/
│   │       ├── README.md              -- the route catalog (method, auth, shape)
│   │       └── payloads/              -- REAL request/response examples
│   │           └── field_dictionary.csv/.md   -- (where field-level depth exists)
├── tools/                             -- the a-la-carte query harness
└── findings/                          -- dated investigation writeups
```

Three domains landed for BD: DataMining (active, 6 query types, a 741-field
dictionary), Billing/AR (a separate federated app, 112 routes cataloged),
Insurance Portfolio (discovered mid-build from a 3rd HAR capture). Full detail:
`data/black_diamond/API/README.md`.

**What made this valuable, concretely:** the field dictionary + query-type catalog
is what let a wrong first-pass conclusion ("no billing query type exists") get
overturned in the SAME session once a 6th query type surfaced -- the structured
catalog is what made the correction fast and the finding ($1,006,622.12 in real
mgmt fees) legible and reusable, not a one-off chat answer that evaporates.

## 2. The gap -- a live census, ground-truthed just now

| Vendor | Current state |
|---|---|
| **Black Diamond** | NOW has the full domains/endpoints/payloads/dictionary pattern (this session) |
| **SmartX** | `data/smartx/API/` exists -- README/AUTHENTICATION/QUICKSTART/testing docs -- but FLAT (no domain/endpoint nesting) and NO field-level data dictionary |
| **Schwab** | `data/schwab/` has its OWN distinct pattern (`DATA_DICTIONARY.md`, `SNOWFLAKE_SCHEMA.md`, `AWS_SNOWFLAKE_ARCHITECTURE.md`, `INDEX.md`) -- a real dictionary exists, differently shaped, no endpoint/payload catalog (Schwab is a file-feed, not a queried REST API, so this is a reasonable divergence, not a gap) |
| **Orion (via `data/inf/`)** | Scattered probe SCRIPTS (`probe_inflec_billing.py`, `probe_inflec_accounts_v2.py`, `probe_inflec_household.py`, etc.) + ad-hoc spike files (`billing_dim_spike.csv/json`) in `data/inf/manual_api/` + `data/inf/api-recon/` -- real discovery work has clearly happened (there's already a billing-dim probe!), but it's UNCATALOGED: no domain overview, no endpoint README, no field dictionary, knowledge locked inside script names and one-off CSV/JSON spikes |
| **Eclipse** | **No directory exists at all** -- zero structured knowledge, despite Eclipse being named repeatedly in existing architecture docs (D3 Orion/Eclipse spec, the DC-REV reverse-ETL blueprint) as a live open question (the trade/rebalance vendor-choice frontier) |

**The headline: every vendor integration has organically produced its own
ad-hoc shape (or none at all), at inconsistent depth, with no shared discovery
methodology.** Orion in particular already has real probe work (the
`probe_inflec_billing.py` name strongly suggests someone already chased a
parallel fee-data question for inf) that is sitting uncataloged and effectively
undiscoverable to another agent -- the same "wrong first-pass conclusion" risk
that almost closed the BD billing investigation prematurely this session could
easily be repeating right now for Orion, silently.

## 3. The proposal -- NFRA_ENDPOINTS PRD

Standardize the pattern proven on BD into the canonical, mandatory structure for
**every** `/data/{source}/API/` vendor catalog -- Orion, Eclipse, SmartX (retrofit),
Schwab (assess -- may stay divergent, it's file-feed not REST), and any future
vendor. Scope for the PRD (CTO to architect/ratify the details; this is DS's
proposed shape from having just built the reference instance):

1. **The directory convention** -- `domains/{domain}/DOMAIN.md` +
   `endpoints/README.md` + `endpoints/payloads/` (+ a field dictionary where
   field-level depth exists), lowercase folders / uppercase standalone docs
   (matching the repo's existing convention). One canonical shape, not
   per-vendor bespoke.
2. **The discovery methodology playbook** -- codify what worked this session so
   the NEXT vendor catalog doesn't reinvent it: (a) bundle-grep the vendor's own
   JS/webpack bundle for embedded route/host strings (found `billing.bdreporting.com`
   and 112 Billing/AR routes this way -- zero vendor spec existed); (b) capture +
   parse a live HAR of a human using the vendor UI (found qt6 "BI Billing" this
   way -- a query type invisible to any automated roster scan); (c) the "roster
   is a floor, not a ceiling" caveat -- a template/object HISTORY endpoint is
   never a reliable CATALOG of what a vendor supports.
3. **Firm-separation handling for shared tools** -- a vendor-catalog tool that
   spans multiple firms (BD serves both bd/49F and cot/Cottonwood) must be
   firm-parameterized with NO firm defaults (the commit-gate caught exactly this
   mistake on `bd_endpoint_sweep.py` this session) -- codify this as a standing
   rule for any `TOOLS/` script under a shared vendor catalog.
4. **Ownership + maintenance cadence** -- who authors/updates a vendor catalog
   (the pipeline-owning DS/AE lane, per the existing per-firm ownership model),
   when it's considered stale, and how a correction (like this session's
   IP-bound reversal) gets folded back in without losing the history of why the
   original claim existed.
5. **Sequencing** -- CTO decomposes into per-vendor TOs: retrofit SmartX (lowest
   effort, already has SOME structure), stand up Orion (real work already done,
   just needs cataloging -- likely the highest immediate value given the
   existing uncataloged probe scripts), stand up Eclipse (currently zero, and a
   named open architectural question), assess Schwab (likely stays divergent
   given its file-feed nature, but worth an explicit CTO call rather than a
   silent gap).

## 4. Why now (the case for prioritizing this)

This isn't a hypothetical -- within ONE session, this exact gap (uncataloged
vendor knowledge) produced a real wrong conclusion ("no billing query type
exists") that would have stood if Andrew hadn't independently pushed further.
Orion already shows the same failure-mode ingredients (real probe work,
zero catalog) that just bit us on BD. Standardizing NOW, while the BD instance
is fresh as the reference implementation, is cheaper than doing it after a
second uncataloged-vendor incident forces the same correction elsewhere.

## 5. Ask

CTO: architect + ratify `NFRA_ENDPOINTS` (naming convention matching the
`NFRA_*` infra-organization family, e.g. `NFRA_COMPRAIL`/`NFRA_GRAPHS`), using
`data/black_diamond/API/` as the reference instance. Decompose into per-vendor
TOs per sec.3 point 5. DS is available to execute the Orion retrofit first
(highest existing-value-to-uncover ratio) once architected.
