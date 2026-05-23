# CVO Verify-Channel Verdict — LD-0018 — 2026-05-23 ~15:30Z — **YELLOW** (latent RED in producer)

**Charter:** MSTR `LD-0018` (commit `b3e374ab9`) — Andrew sovereign instruction `2026-05-23T~14:45Z`:
> "If i recall correctly, they only recorded billing data back to mid-2025 maybe September. We imputed it backward through some mechanism, it's worth having CVO review this methodology."

**Subject:** the fee-billing pre-Sep-2025 imputation methodology that resolves DS INF_C_08 fee-billing-gap finding (commit `c02c9c1ed`, VALFIN.001 Phase-1).

**Verdict shape:** GREEN producer / RED latent defect inside the producer / YELLOW overall because the defect is **DORMANT** (zero downstream consumers wire the rule); plus a META-class **NAMING-vs-SEMANTIC** asymmetry with Andrew's mental model.

---

## MECHANICAL — what was located + does it still work?

The methodology Andrew is recalling lives in `data/orion/scripts/gold/INF_C_09.fee_status_audit.py:1-299` — the "Brief B #2 backfill rule" authored by 0.4.0_DS_ClientPlatform 2026-05-12 per RD 0.4.2 Brief B #2+#3. **Quoted in docstring lines 9-15:**

> "For any date D prior to `first_known_fee_status_date`, assume the account was at `fee_status_at_first_known`. Between `first_known_fee_status_date` and the latest observation, use the historical billing dim row directly. After the latest observation, hold the latest known status."

**4-check on the producer artifact `s3://opal-data-inf/gold/views/fee_status_audit.parquet`:**

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | `aws s3 ls` confirms key (16,073 bytes) |
| FRESH | PASS | LastModified 2026-05-23 10:31:16Z (today) |
| SCALED | PASS | 867 rows × 8 cols for 168-advisor / ~861-account scope; sane size |
| NOT-FROZEN | PASS | Dispatched in `CHAIN_GOLD_C` + `CHAIN_FULL` (`orion-gold-dispatch.sh:163,219,228`); runs daily |

**Producer is mechanically sound. INF_A_02 (fee_RATE history, separate from fee_STATUS audit) is a deprecated no-op (`INF_A_02.fee_rate_history.py:1-66`) — INF_C_08 zero-stubs all fee_efficiency metrics because of that empty fee_rate_history; that is the DS-surfaced gap, and it is a DIFFERENT mechanism from INF_C_09.**

---

## NOVEL — empirical probe of the imputation logic

**Probe goal:** Does the imputation rule, applied to the audit table, produce a defensible fee-status history? Sharpest-test-bind: pick the 4 question that breaks first.

### Probe 1 — audit table empirical shape (today)

```
SHAPE: (867, 8)
first_known_fee_status_date:
  min:  2023-05-25
  max:  2026-05-22
  532 of 867 (61%) cluster at 2023-05-25
has_state_changes:
  True   598 (69%)
  False  269 (31%)
current_fee_status:
  True   732 (84%)
  False  135 (16%)
observation_days median: 1094 (3 years)
```

The docstring (`INF_C_09.fee_status_audit.py:24-34`, written 2026-05-12) says:
> "Real fee data starts 2026-04-01 (~6 weeks of history)"

The empirical audit table says: **most accounts have a 3-year observation window starting 2023-05-25.** This is a >2.5-year asymmetry between the producer's self-described expected behavior and its current output. Sharpest-test-bind is: are those 2023-05-25 observations real fee data, or are they the placeholder-zero rows the docstring explicitly warned about?

### Probe 2 — direct partition inspection

```
2023-05-25: rows=532, is_fee_earning_true=0, fee_amount_sum=$0,        ending_mv_sum=$37,477
2024-01-15: EMPTY (0 rows)
2026-04-01: rows=760, is_fee_earning_true=628, fee_amount_sum=$1,270,986, ending_mv_sum=$123,125,326
2026-05-22: rows=867, is_fee_earning_true=732, fee_amount_sum=$1,859,729, ending_mv_sum=$141,751,481
```

**The 2023-05-25 partition is exactly the placeholder pattern the docstring warned about: 532 rows of `is_fee_earning=False`, `fee_amount=$0` — schema-only rows with no real billing. The first partition carrying actual fees is 2026-04-01.**

### NOVEL finding — **latent RED in INF_C_09's per-account aggregation**

`INF_C_09.fee_status_audit.py:138-144` filters with `if df.empty:` (true only for 0-row parquets). The 2023-05-25 partition has 532 rows, so `df.empty=False`, so its 532 placeholder-zero rows get included in the per-account stack (lines 145-147). That makes the per-account `groupby('account_id').min('snapshot_date')` resolve to **2023-05-25 for 532 accounts whose actual first real billing date is 2026-04-01 or later**.

**Direct consequence: 61% of the audit table has the WRONG `first_known_fee_status_date`, all set to the same placeholder-pollution date. `fee_status_at_first_known=False` for those 532 because the placeholder rows carry `is_fee_earning=False`.**

Any downstream consumer that APPLIES the Brief B #2 rule on this audit table would conclude: "Account X was non-fee-earning from 2023-05-25 through 2026-03-31 (~34 months), then flipped to fee-earning on 2026-04-01." This is **structurally false** — the account simply wasn't observed in any partition during that period (the partition existed but had no rows for that account); the placeholder-zero row at 2023-05-25 created a false first-observation anchor.

### NOVEL finding — **the imputation rule has ZERO downstream consumers**

Grep for `fee_status_audit` or `first_known_fee_status` across `data/`, `infra/aws/lambda/`, `portal/src/`:
- **Producer:** `data/orion/scripts/gold/INF_C_09.fee_status_audit.py` (only)
- **Dispatch catalog:** `data/orion/scripts/gold/orion-gold-dispatch.sh:163,219,228,916,933` (registration only)
- **Docs/briefs:** `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/briefs/2026-05-12_advisor_analytics_fee_split_DS_briefing.md`, `docs/architecture/ADVI_PRODUCT_VALIDATION.md`, `org/projects/ADVI_INFLEC.json` (documentation only)
- **Consumer code:** **none.** No Lambda, no other gold script, no portal component reads the audit table.

The Brief B #2 backfill rule was **published but never wired**. The audit artifact is freshly written each day and ignored.

---

## META — failure-mode surface + asymmetry-with-Andrew

### META-1: Naming-vs-Semantic asymmetry with Andrew's recall (LD-0012-class)

| Dimension | Andrew's mental model (verbatim) | Empirical reality |
|---|---|---|
| Data start | "mid-2025 maybe September" | 2026-04-01 (~7 months later) |
| Mechanism | "imputed it backward through some mechanism" | Audit table exists, rule documented; **no consumer applies it** |
| What is imputed | (implied: fee values back to mid-2025) | Only `is_fee_earning` **bool**, not fee_amount / fee_bps / fee_schedule |

Andrew's "imputed it backward through some mechanism" is **aspirationally true** (the methodology was authored as Brief B #2 → INF_C_09 → produces the lookup) but **operationally false** (no system consumes the lookup, so no actual imputation happens at read-time anywhere). This is the same shape as LD-0012's `capital_gains_ttm` — a field name implying one semantic, the code/wiring producing another.

### META-2: structural fragility once a consumer IS wired

The Brief B #2 hold-backward / hold-forward rule has known failure modes the docstring does NOT enumerate but the empirical data exposes:

1. **State-changes are the majority case, not the edge.** `has_state_changes=True` for 598 of 867 accounts (**69%**). Hold-status is a backward-extrapolation that ASSUMES state stability; the empirical population says state-stability is the minority condition.
2. **Placeholder-zero pollution silently inflates first-known.** Already demonstrated in NOVEL Probe 2. The producer's filter (`df.empty`) is too weak; the correct filter is `df.empty or (df['fee_amount'].sum() == 0 and ~df['is_fee_earning'].any())` — i.e., reject partitions that have no real billing.
3. **Fee-VALUE imputation is not addressed.** "Was account fee-earning?" (bool) is necessary but insufficient for any downstream wanting "what was the fee revenue from account X in 2024?" The rule's scope is narrower than its name suggests.
4. **Advisor reassignment / fee-schedule migration are silent.** A fee-paying account in 2024-Q3 that moved to a different fee schedule in 2025-Q2 reads as "still fee-earning" under the rule, but the SCALE of fee revenue is unknown to the rule. For VALFIN-class validations that ask "did fee revenue track AUA correctly?" the rule provides only the binary.
5. **Account close/reopen with different terms.** Audit table aggregates min/max snapshot_date per account; a close/reopen pattern looks like one continuous observation window with bracketing state changes; the audit doesn't distinguish.

### META-3: VALFIN Phase B/C unblock-status

DS's INF_C_08 "fee billing gap" finding (zero-stubbed `fee_data_available=False`, `fee_efficiency_score=0.0` for all 168 advisors) is **real and unfixed by INF_C_09**. The DS finding and the INF_C_09 publisher are answering different questions:
- INF_C_08 wants per-account `fee_rate` (basis points / annual) — driven by `gold/dimensions/fee_rate_history.parquet`, which is a 3,566-byte zero-row stub from the deprecated INF_A_02 (verified at `INF_A_02.fee_rate_history.py:1-66`).
- INF_C_09 produces per-account `is_fee_earning` STATUS audit — which exists and is fresh but is consumed by nothing.

**For VALFIN Phase B/C (portal type swap + collapse old key):**
- If the portal type swap depends on fee-rate or fee-revenue values: still blocked on the fee_rate_history empty stub (separate, not LD-0018 scope).
- If the portal type swap depends on fee-status booleans: technically unblocked by INF_C_09's audit existing, **but the consumer wiring has to be added AND the placeholder-zero pollution has to be fixed first** to avoid silently shipping the 61%-wrong first-known dates.
- If the portal type swap is fee-independent: unblocked.

DS or COO should clarify which class VALFIN Phase B/C falls in; the answer drives whether this verdict unblocks or punts.

---

## Verdict — **YELLOW**

- MECHANICAL: **GREEN** — producer artifact exists, fresh, scaled, dispatched in chain.
- NOVEL: **RED (latent)** — placeholder-zero partition pollution causes 61% of audit rows to carry a wrong `first_known_fee_status_date=2023-05-25`. Latent because **no consumer applies the rule**, so the false output doesn't propagate.
- META: **YELLOW** — methodology concept defensible for the narrow STATUS-only question it was built to answer; Andrew's mental model of "imputed backward through some mechanism" is aspirational, not operational, today; multiple failure modes if/when a consumer is wired (69% has-state-changes population; fee-VALUE not covered; placeholder pollution bug must be fixed before any consumer goes live).

**Overall: YELLOW** — usable as-is **only because no one is using it**. The moment a consumer is wired, the latent NOVEL-layer defect becomes a live RED.

---

## Findings list (mechanism-specific, per-driver, P0/P1/P2)

| ID | P | Driver | Mechanism | File:Line | Fix |
|---|---|---|---|---|---|
| LD-0018.F1 | **P1** | DS (0.4.0_DS_ClientPlatform) | INF_C_09 placeholder-pollution: `if df.empty:` filter too weak; doesn't catch 532-row $0-fee placeholder partitions | `data/orion/scripts/gold/INF_C_09.fee_status_audit.py:138-144` | Add post-filter `df = df[df['fee_amount'] > 0]` OR strengthen empty check to `df.empty or (df['fee_amount'].sum() == 0 and not df['is_fee_earning'].any())`. Backfill audit table after fix; expected `first_known_fee_status_date` shifts from 2023-05-25 to 2026-04-01 for ~532 accounts. |
| LD-0018.F2 | P2 | DS / RD-0.4.2 / Andrew | Brief B #2 rule has NO downstream consumer; orphaned publisher. | `data/orion/scripts/gold/INF_C_09.fee_status_audit.py:1-299` (publisher); 0 consumers found in `data/`, `infra/aws/lambda/`, `portal/src/` | Either (a) wire a consumer (the originally-envisioned Lambda billing aggregator / FE historical reporting), OR (b) deprecate INF_C_09 as unused / move to a parked scripts dir, OR (c) document explicitly that it's a Phase-2-staged producer for future consumption. |
| LD-0018.F3 | P2 | RD-0.4.2 / Andrew | Brief B #2 rule does NOT impute fee-VALUE; only fee-STATUS bool. Any downstream that needs revenue/rate history backward is still blocked on `fee_rate_history.parquet` being empty (the deprecated INF_A_02 stub). | `data/orion/scripts/gold/INF_A_02.fee_rate_history.py:1-66` (deprecated noop); `data/orion/scripts/gold/INF_C_08.advisor_fee_efficiency.py:177-178` (zero-stub fallback) | If the underlying business question is "fee revenue trajectory," a separate Brief B' rule for fee-VALUE imputation is needed — not just status. Decide whether to scope. |
| LD-0018.F4 | P2 | All consumers (when wired) | 69% of accounts (`598/867`) have `has_state_changes=True` in observation window. The hold-status rule's central assumption (status stability) is violated by the majority. | (logic, not file) | Either accept the rule as a coarse approximation (document explicitly), OR augment audit table with per-account state-change-timeline so a consumer can pick the change-closest-to-D status instead of first-known. |
| LD-0018.M1 | P2 | MSTR → Andrew | Andrew's recall ("back to mid-2025 maybe September") is ~7 months earlier than reality (~2026-04-01) for the first-real-billing date. The "imputed it backward" mechanism exists as a publisher but is not wired into any consumer. | (mental model) | Surface to Andrew via MSTR: current state is "audit table published, rule documented, no consumer applies it" — not "fee data imputed back to mid-2025." Decide whether to (a) wire a consumer per F2, (b) park the publisher, or (c) accept the as-is "documented-but-unused" state. |

---

## Routing

- **MSTR** (this verdict, 0.0.0_AB_MSTR) — verdict file commit + GREEN/YELLOW/RED line + M1 mental-model clarification
- **COO** (2.0.0_SA_COO) — CC; LD-0018 resolution; charter F1 fix to DS (substance routing per CLAUDE.md Rule 13)
- **DS_ClientPlatform** (0.4.0_DS_ClientPlatform) — F1 + F2 findings; producer fix authority + consumer-wiring decision lives here

CVO routes findings; does not push code (verifier-not-fixer per Operating Doctrine §1-§9; substance-meta findings always route via safe-deploy chain per `/spot-check` SKILL §2d).

— 3.0.0_SA_CVO
