# Session log — 0.4.0_DS_ClientPlatform~A — 2026-07-29 1523Z-1645Z (respawn -> conformance design)
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), VALIDATE, IMPLEMENT, SCRIBE

**Window:** respawn 152355Z (MSTR, on CTO's time-critical request) -> 164500Z.
**Predecessor died holding the 15:45Z accrual clock** — third session-edge fire-owner loss today.

## Startup (grounded, none asserted)
- **No orphan watcher for `~A`** — `ps` showed watchers for 7 other serials, none for mine, and
  `get_agent_status` read NOT REGISTERED. Fresh session, no live peer, no kill needed. (Ran the
  whose-PID discriminator before reaching for a kill; the dual-COO and context-clear false
  positives both key on that.)
- Registered PID 25124. LD-0290 serial file written.
- **Monitor `b4r1n01rj` CONSUMER-confirmed by actual delivery** (3 messages arrived in-chat within
  seconds), not by a `ps` match — a match proves a process exists, not that anything reads its stdout.
- **PATH shims OK** — `comp-which`/`comp-grep` resolve via `~/bin`. My first `comp-grep` failure was
  MY error (`bash .tools/comp-grep` on a Python file), not a shim outage.

## What happened

### 1. Cleared CTO's blocking WI-2 grammar gate (161619Z ask -> 153358Z answer -> CLEARED 153517Z)
Key is `portal/gold/mdpf/{scope}/aum-metrics/{YYYY-MM-DD}.json` — **hyphen**. Grounded the pair CTO
wanted: **at source** (`build_portal_gold_accrual.py:235` builds the key from `t['name']`, while the
underscore `t['source']` is quarantined to the `:216` staging read — two separate fields, so the
underscore cannot transfer) **and on live state** (all 15 keys under `portal/gold/mdpf/` hyphenated,
zero underscores). Date component fails CLOSED via `_valid_date` `:178-185` + `:230` "NEVER fall back
to the run date."
**Residual reported, not smoothed:** `_valid_date` is NOT byte-equivalent to the publisher grammar —
exercised a 7-case matrix, exactly one divergence (`2026-W01-1`, accepted by `fromisoformat` on
py3.11+, rejected by `\d{4}-\d{2}-\d{2}`). Measured on local py3.12.10; the py3.9-runner half is
**INFERRED**, labelled as such.

### 2. Fired the composing slice producer on ANDREW-DIRECT (three routing changes, all CTO's)
GO 153813Z (me) -> DO-NOT-FIRE 153951Z (AE) -> **ANDREW-DIRECT ~1602Z reverses it back to DS**
(154232Z) -> TARGET CORRECTION 154540Z (the *composing slice* producer, not the generic one).
Ran `build_cottonwood_mdpf_slice.py` **dry-run first** (gates PASS), then `--upload`:

    ETag  dd4d21a84cc62b11bdaa385707447d66 -> a95153abc2e830a9bfd51344e140b1cd
    Size  37,237 B -> 80,429 B      LM 2026-07-29T15:52:29Z
    meta.composed_backfill  ABSENT -> PRESENT   (the STAGE6-REVAMP refusal predicate, CLEARED)

Dry-run reproduced my predecessor's independently-derived oracle exactly (`50 = 6 measured + 44
composed`, window 05-28..07-17, `model_aua_last_non_null 125,123,718.07`). **AD-HOC, not production
evidence.**

### 3. REFUSED a CTO instruction with source — accepted in full
CTO 160434Z measured my compose carried only the model leg (non_model 47->6, custody 56->38) and
instructed me to extend it. **I did not.** `non_model_aua` is a **DERIVED BALANCE**
(`custody - model`, `:407-409`, *"never fabricated"*); on splice dates custody is absent so the
balance is **UNDERIVABLE, not missing**. The **W-2b identity gate** `:668-676` fails the build on
exactly that shape. `:533-536` documents the exclusion, proof-backed by the 001511Z set-equality
result (*"its ~$334mm non_model never participated"*). CTO retracted (161556Z): *"I asked you to
fabricate a balance... a coverage-count comparison cannot distinguish 'not carried' from 'not
derivable.'"*

### 4. THE FINDING NOBODY ELSE HAD: provenance labels asserting estimates over None
`:587 row = dict(oo_prov[d])` copies the one-off's provenance row **verbatim**, including labels for
cohorts the compose deliberately does not carry. **Measured on the object I wrote: 44 of 51 splice
dates assert `non_model = "interpolated_estimate"` at `confidence 1.0` over a `None` value.**
CLAUDE.md's own clause, live: *provenance recording WHERE but not WHAT IT IS OF converts an absence
into a documented lineage.* The values are honest; the labels lie about them. Now the primary
data-side deliverable.

### 5. Refuted CTO's central premise — an `aws s3 ls` LOCAL-time misread
CTO: *"every cottonwood object is stale at 2026-07-28T20:35:22Z; nothing wrote cottonwood today; the
working writer skips cottonwood."* **`head-object` (UTC): 16:15:31-32Z, all four firms, canonical
hyphenated names.** `aws s3 ls` renders LOCAL on this UTC-4 host; `12:15:31` local IS `16:15:31Z`.
**The publisher does NOT skip cottonwood — Andrew's item (c) was already satisfied.** What skips it is
the *underscore* writer (chain revamp stage, 15:05:22Z), which refused on the un-composed slice — a
precondition my 15:52:29Z compose removed. Caught because the "stale" stamp and my own `date -u`
disagreed by exactly 4h. CTO owned it (163749Z).

### 6. Delivered the design (@bf8cb273f9, §5b @a42f9a9d8d) — ACCEPTED
**Recommendation: CONFORMANCE + one IAM grant + one label fix. NO modified publisher — and therefore
NO interim deviation to record**, which dissolves brief item (e). Answered the remaining questions:
- **Q1 (firm separation?) — NOT TRIGGERED, checked before answering.** The custody leg *already*
  reads `blackdiamond/cottonwood/silver/fact_holdings` (`:272`) and yields **38/450** in gold now.
  Same-firm tree; nothing crosses a boundary. **The whole server-side non-model target is already
  built** — `NOT_MEASURED` is already retired in the producer and survives only in the stale served
  copy.
- **Q2 (6-vs-38) — an ORDERING ARTIFACT, and it is a finding.** The balance is computed in the DAILY
  build (`:380-384`) where model holds only 6 measured dates; the compose splices 44 more at `:594`
  and **never recomputes**. 32 derivable dates sit empty. **Recommended NOT recomputing them**:
  `measured custody - interpolated model` is a hybrid needing a provenance decision and a render
  change first.
- **Q3 — honest limit stated:** custody begins ~06-09, so the band cannot span the 450-day axis under
  any fix.

## Two instrument findings
- **`comp-pipescript deployed` FALSE-POSITIVES `STALE` on CRLF.** It flagged
  `build_cottonwood_mdpf_slice.py` (local `54bdbe60` vs s3 `68539df8`); `git show HEAD:...| md5sum` =
  `68539df8` = **byte-identical to deployed**. It md5s the CRLF working tree against the LF object;
  `diff` showed `1,718c1,718` with identical content. Also: **passing a BARE BASENAME silently
  defaults to the bd tree and returns a clean-looking `0 MATCH / 0 STALE`** (AE's catch) — I hit that
  exact zero earlier and did not treat it as a pass.
- **AE's `dim_mdpf_account_distribution.py` STALE is REAL, but its md5 evidence could not establish
  that** (same CRLF mechanism produces an identical verdict). Confirmed soundly: HEAD blob
  `2b07e99d` != deployed `fca2b76c`, **83 genuinely differing content lines**, and decisively
  `_cottonwood_sidecar` / `COTTONWOOD_UNITS_KEY` / `cottonwood_fold` / `account_units.json` =
  **deployed 0, repo 2/5/1/1**. **The deployed aggregator structurally cannot include cottonwood** —
  CTO's vintage hypothesis REFUTED, and firing it would have reproduced 7,597 at rc=0.

## Reported, owned
- **15:45Z penny read: NO-OUTPUT / UNGRADED** (single reporter, handback settled with base). The
  bridge FIRED 15:45:21Z and wrote **0 of 11** — `AccessDenied ... "because no identity-based policy
  allows the s3:PutObject action"` = **MISSING GRANT**, categorically distinct from the 15:02Z
  legacy-emit **EXPLICIT DENY** (the intended writekill). Crash on object 1 => none landed.
- Folded base's finding: **the bridge has never written in its 2-run life, and its only pre-prod
  exercise was a DRY-RUN — so the IAM gap was structurally undetectable.** The grant's acceptance
  test must be an actual landed object. Second instance of the Aug-1 ETFS class; routed to CTO as a
  rule, not a fix.
- **Record correction issued:** base attributed the 15:52:29Z write to AE. It was mine; AE fired
  nothing.
- **Clock:** CTO's hand-typed stamps ran ~20min fast at 15:43Z, drifting to ~45min by 16:40Z. Flagged
  twice; he then caught and corrected a false *"the 17:15Z emitter has fired"* (it had not — 16:41Z).

## Blockers
None. Everything outstanding is HELD ON CTO WORD (sequencing, not a blocker): the label fix, WI-2,
retirement pair, coherence gate, backfill scoping. Freeze runs to post-17:15Z, which **has not
occurred**.

## Current State
- Composed cottonwood slice is CORRECT in staging: `s3://opal-data-assets/gold/mdpf_revamp/cottonwood/
  aggregate_aua_timeseries.json`, ETag `a95153abc2e830a9bfd51344e140b1cd`, 80,429 B, LM 15:52:29Z.
  model 50/450, custody 38/450 (06-09..07-27), non_model 6/450, `composed_backfill` present.
- **It cannot reach platinum**: the accrual bridge is IAM-blocked, so `portal/gold/mdpf/cottonwood/`
  still holds only the 00:35Z chain's keys, and the 16:15Z publisher faithfully republished the stale
  content (served: 37,518 B, model 2/450, non_model 0, custody 0).
- Design at `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_COTMDL/
  COTTONWOOD_PLATINUM_CONFORMANCE_DESIGN_20260729.md` @a42f9a9d8d — CTO-ACCEPTED.
- Label fix is SPECCED, NOT BUILT — blocked on a vocabulary call: reuse `absent` (my recommendation,
  interim) vs add `underivable` (precise, but **an enum change is a frontend contract change**
  needing DE).
- Nothing deployed this session. One ad-hoc write total (15:52:29Z), labelled AD-HOC.

## Next Steps
- **[0.7.0_AE_CloudOps~A]** the targeted IAM grant (CTO ruling 155914Z), `s3:PutObject` on
  `opal-data-assets/portal/gold/mdpf/*` — the full write set, not the single traceback key.
  **Acceptance = an actual landed, verified object. Never a dry-run, never rc=0.**
- **[0.4.0_DS_ClientPlatform~A]** (me): post-grant, re-run the accrual bridge (expect 11 planned /
  8 written / 3 R4 `aum-metrics` errors = the WI-2 declared-before-built gap); then the served-artifact
  acceptance read reporting **all three series counts**. Label fix on CTO word + DE vocabulary call.
- **[1.0.0_SA_CTO]** vocabulary ruling (`absent` vs `underivable`); whether to move the design under
  `docs/architecture/`; the dry-run-cannot-validate-permission rule.
- **[0.4.0_DE_ClientPlatform]** the 450-day-axis render call (§6f) and whether it wants the
  interpolated cohort distinguishable on screen (decides Q2 option A vs B).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-grep` | `aum.metrics`, `composed_backfill`, `aggregate_aua_timeseries.json` | PASS | Located the accrual bridge, the composing slice producer, and every `composed_backfill` writer/reader. First call failed as MY error (`bash`-invoking a Python file), not a tool fault. |
| `comp-pipescript deployed` | `dim_mdpf_account_distribution.py`, `build_cottonwood_mdpf_slice.py` | **FAIL (instrument)** | Bare basename silently defaults to the **bd** tree -> clean-looking `0 MATCH / 0 STALE`. Full path works but **false-positives STALE on CRLF** (see Instrument findings). Verdict is not evidence without a content diff. |
| `comp-pipescript postdeps` | `dim_mdpf_account_distribution` | FAIL (instrument) | "No dependencies declared" — from the wrong (bd) tree. A silent zero, not a pass. Carried finding: comp-pipescript is blind to the mdpf tree unless given a full path. |
| `comp-surface-check` | via `safe-commit` x2 | PASS | 1 changed file, no critical surface. |
| `comp-pulse` (risk-reflex) | both commits | CLEAN | DENOMINATOR 1 file vs 1484 danger nodes — a measured result. |

**What worked:** `comp-grep` localized the whole producer/bridge/publisher chain in three calls;
stage-2 raw drill-in (source reads + `head-object` + parquet-free JSON coverage counts) did the
actual grounding, exactly the two-stage pattern.
**What failed:** `comp-pipescript` gave me a reassuring zero on a bare basename and a false STALE on
CRLF — **both failure modes point the same way (toward "fine" or toward panic) and neither is
distinguishable from truth without an independent diff.**
**Gap found:** `comp-pipescript deployed` should compare **content**, not raw bytes (normalize line
endings), and should ERROR on an unresolvable bare basename rather than silently falling back to the
bd default. Filing both to CTO as tool findings.
