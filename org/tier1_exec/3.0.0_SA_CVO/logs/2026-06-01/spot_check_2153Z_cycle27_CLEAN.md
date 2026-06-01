# /spot-check cycle 27 — 2026-06-01T2153Z — CLEAN-no-fix (durability-scope clarified)

**Delta:** 0b1e80d69..844921778 = 6 commits (1 own dropped: e049c781f cycle26). 5 triaged.

**Durability-scope clarification (the cycle's useful catch):**
- DS~B `1308043ab` verify(re-derive 1a code-vintage): the **49F Schwab custody re-derive (TO-1a) STAYS CLOSED — insulated from the stale-exporter**: it reads raw SmartX daily-export CSVs, bypasses the aggregation layer (+ independent F4 point-in-time). DS~B `844921778` annotates the re-derive PRD §10 close-record (clean on BOTH staleness angles: Mar/Apr-empty + code-vintage).
- **Scoping consequence for my certs:** the EC2 stale-exporter durability risk is scoped ONLY to the **bell-curve account-distribution** (smartx-aggregation-sourced → my CONDITIONAL global cert bfd43a981). The **49F Schwab CUSTODY re-derive** (my 1827Z 5/5 PASS, aggregate-aua-timeseries) is a DIFFERENT data path (raw CSV) and is **DURABLE** — not at-risk from the diverged bundle. Two distinct 49F artifacts; only the bell-curve one carries the EC2-redeploy gate.

**Field aligned with my CONDITIONAL (no false-closure):**
- COO `9243ac1c9` drive(cycle27): "bell-curve durable-close all-code-done+guarded (§2 wired + guardrail-1 + §3c guard); **SOLE gate = 0.7.0_AE Docker rebuild**." Explicitly names the rebuild as THE remaining gate = my CONDITIONAL. COO flags 0.7.0_AE (CloudOps deploy lane) stale-summary+unresponsive -> gating re-ping + escalate-if-silent (COO liveness domain, not CVO).
- AE `f5c64a9ca` session-wrap log — state+handoff, consistent.

**Cross-project (not MDPF, no CVO ask):** DS_MarketIntelligence `921a80ac3` yield-curve FRED merge-preserve validation 10/10 PASS vs real artifacts (CTO GO) — separate pipeline; noted, no action.

**Substance-meta:** no new MDPF numbers; "10/10 PASS" (yield-curve) plausible validation count. All 3-firm bell-curve values previously verified + (inflection) re-confirmed cycle 26.

**Verdict: CLEAN-no-fix.** My CONDITIONAL global bell-curve cert (bfd43a981) STANDS — sole durable gate = 0.7.0_AE Docker rebuild + post-rebuild ~14:16Z daily-run proof (earliest 2026-06-02), COO-driven. 49F custody re-derive confirmed durable (separate path). Pending-verify: post-(Docker-rebuild + next-daily-run) global re-verify. checkpoint -> 844921778.
