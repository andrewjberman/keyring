# ws-charter cycle 0005 — 2026-06-03 1402Z

**CLASS:** CLEAN-SWEEP (sweep) + design-record bank (W5 edge-untier fast-follow)
**HALT:** clear. **Monitor:** PID 1082837 alive (stable — see infra note). **Inbox:** processed (DS W5 proposal→retract).

## Sweep findings (no CTO-pending action)

- **ADVI_FEREFI decompose VERIFIED sound.** COO registered project + dispatched W1 FE TO (`8c00d99c5`) from PRD `a2ba67707`. I independently re-verified COO's open-Q resolutions against live type defs:
  - Item 1: `GranularityOption = 'monthly'|'quarterly'|'annually'` → `'annually'` OK; `TimeWindow = '1Y'|'3Y'|'Max'` → `'3Y'` OK.
  - Item 4: `Interval = 'monthly'|'quarterly'|'yearly'` → `'yearly'` OK; `WindowKey = '1Y'|'3Y'|'max'` → `'max'` OK (correctly lowercase — NOT TimeWindow's capital `'Max'`; the Q1 mismatch risk I flagged is properly handled).
  - Item 5 prev===0: render "—" for %, keep $ delta; first period omits both. Sound.
  - Decompose is correct; no CTO intervention. Items 1-5 in RD-AI FE lane; #6 awaits Andrew greenlight → DS fee-data TO.
- **Monitor exit-143 root-caused + fixed fabric-side:** `6ff4d144d fix(kill-orphans, LD-0146): stop reaping live persistent-Monitor stream watchers`. My session flag was a real bug (kill-orphans sweep SIGTERM'd live stream watchers). Now stable.
- **Promote manifest unchanged:** 548c9d7d + ADVI_FEREFI (on build) — HELD for Andrew GO, gated on Andrew INFOTD/INFNNA smoke on live v2.1.112.

## W5 edge-untier — DESIGN RECORD (banked; fast-follow frontier, dispatch deferred)

DS received a STALE [DRIVE] ADVI_INFPRM.W5 dispatch (INFPRM now CLOSED, `bbb9f4355`); COO flagged it stale (`140110Z`), DS retracted (`140205Z`). The Distribution cross-advisor relationship-drill edge-untier is a **CTO/AE fast-follow frontier item**, NOT a live DS emit. Standing down — BUT DS's analysis is captured here so the frontier item picks up with the design already made:

1. **A DS emit IS required** (the split cannot collapse to edge+FE-only). FIRST-check: `relationship_stacked_periods` lives ONLY inside `book.json` (INF_D_02 top-level key ~line 2015); no existing per-advisor aggregate artifact (`timeseries.json`/`drilldown_summary.json`) carries it.
2. **Proposed artifact:** `s3://opal-data-inf/platinum/advisors/{advisor_key}/relationship_periods.json` (distinct path; `book.json` stays L1/.004a with `clients[]`). Shape = roster-free projection of the EXISTING `_compute_relationship_stacked_periods()` output, dropping `display_name`: `{advisor_key, firm_id, generated_at, data_as_of, relationship_stacked_periods:[{period,label,end_date,total_aua, stacks:[{client_key, aua}]}]}`. NO display_name / clients[] / account_id / household_name / tax / billing / fee.
3. **FE ground-truth:** `DistributionTab.tsx:2509-2512` (+ 2497) renders one `<Bar dataKey={s.client_key}>` per stack, labels via `pseudonymizeChildLabel(client_key)`; never reads `display_name`. So FE repoint = trivial path-swap IF the artifact keeps per-stack `{client_key, aua}`.

**CTO no-PII RULING (resolving the discrepancy DS raised):** **Option A** — keep opaque `client_key` + `aua` per stack, strip `display_name` — is the correct no-PII bar, **CONDITIONED on the re-identification guard holding** (no cross-advisor `client_key`→identifier map L0-reachable; the map lives only in admin-gated `.004a` `book.json clients[]` / `nna_clients.json`). My earlier verbal shorthand this session ("firm/segment rollups ONLY, no per-client rows") was OVER-STRICT and is **superseded** by the documented INFPRM W5 refinement (2026-06-02) — that documented ruling is canonical. Rationale: "no PII" ≠ "no per-household data"; an opaque surrogate `client_key` with AUA is non-identifying *as long as the re-id path is closed*. Option B (zero household ids) would force an FE viz redesign for zero security gain over a verified re-id guard. **Hard condition:** DS's `comp-pii` audit MUST prove the re-id guard before AE allowlists; if any L0-reachable `client_key`→name path exists, fall back to B (or add a guard) — do NOT emit under A with an open re-id path.

**Sequencing when frontier item activates (Andrew/COO prioritize):** CTO confirm shape → DS emit (`comp-pii` + `ds-commit-gate`) → AE allowlist the new path at edge (`book.json` stays admin-only) → RD~C trivial FE path-swap → CVO edge-model verify.

## Follow-on

- ACK DS stand-down; design banked here. No live DS task until Andrew/COO re-route the frontier item.
- Next promote still HELD for Andrew GO (INFOTD/INFNNA smoke).
