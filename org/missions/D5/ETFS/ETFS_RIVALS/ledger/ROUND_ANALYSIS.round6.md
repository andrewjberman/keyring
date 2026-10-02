# ETFS_RIVALS -- ROUND 6 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~20:4xZ

**Input:** CVO slug msg 28734, `surprise-channel/remediations/REMEDIATION_v6.Z.md` @eda0cb33b7.
**Review:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R6_REVIEW_20261002.md`.
**Counts:** orders 59/59 terminal; channel 139/139 dispositioned, 0 open.

## 1. WHAT THE ROUND DELIVERED

- **The apply at pin eb6e9f04ff reads PASS on the APPLIED plane** (pair COO 03036ef58b / CTO 15f3366309).
  - The 10-02 page is published: 13 of 13, read back, 1,833,385 B.
  - The census states are counted, Unclassified is never ranked, names come through display_name, and exits are priced.
  - The layout pass (Andrew ~17:0xZ) is live.
- **Judgment criteria (L9):**
  - ui-2, ui-3 and ui-4: PASS;
  - r-6: PASS on the prompt (24/24 accounts in display form), with its names residue going to ui-5;
  - ui-5: NOT_EVALUATED until the 2026-10-05 vehicle page;
  - **ap-1: FAIL.** The accounts are good (24/24 PASS, median 179 words), but no scheduled path produces them.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **C-S24 (P1) is the round-7 lead cell.** The 09:00 ET sweep runs the AI stage as ITS OWN STEP, with a stated deadline, then republishes the page. The AI gate does NOT go on the publish-page Lambda. | `sweep.py:469-472` skips publish whenever the marker exists, and the gateless morning publish always writes it, so no scheduled path reaches the AI stage. Gating the morning page write would put up to 48 vendor calls with 120 s timeouts in front of it (CVO~RV's "not recommended", agreed). |
| 2 | **ap-1 is proven BY THE TRIGGER ITSELF.** The positive control is a deliberate invoke of the SWEEP Lambda with its own EventBridge schedule payload, never an `only:[publish-page]` fire. The organic 2026-10-05 09:00 ET sweep, with no seat act, is the acceptance. | No FWD is a wait: the mechanism is driven deliberately, with the organic case as the acceptance (spine L2). An `only` fire bypasses the very lines that failed. |
| 3 | **P2 provenance:** `run_path: "scheduled"` is reserved for the schedule. An `only` / ad-hoc fire stamps `"ad_hoc"`. The 09-30 manifest's claim is corrected forward in the next write (no rewrite of the stored object). | A value must carry its claim (CLAUDE.md). The 09-30 manifest said "scheduled" for an `only` fire, which is how the FAIL hid. |
| 4 | **A standing rule for ETFS_RIVALS' L5 from round 7 on** (CVO~RV section 5): every outcome that claims production names its ORGANIC trigger, and the trigger's own invocation is its evidence. A deliberate fire is the positive control only. | That would have caught C-S24 at the cut. It costs one line per production outcome. It does not apply to an outcome that claims no schedule. |
| 5 | **W4-S9 is ARMED. The issuer act I-1 is owed now by `2.0.0_SA_COO~RV`:** one marker batch above 45 dates, so W4-S9 is disarmed this round and not carried. | An ARMED hazard disarms same-turn through its owner. |
| 6 | **ui-5 is graded on the 2026-10-05 vehicle page.** If P1 (the Lambdas at the pin) holds, nothing is owed before then. | The Bloomberg names arrive with that run; it is a named wait with its trigger. |

## 3. ENRICHMENT LIST (round 7, ONE issuance by `2.0.0_SA_COO~RV`)

1. **C-S24:** the sweep's own AI step, with a deadline, then a republish. Plants:
   - a marker present still reaches the AI stage;
   - a deadline overrun publishes without accounts and records FAILED;
   - one run per page day (CALL 5).
2. **Provenance:** `run_path` takes "ad_hoc" for an `only` fire, under the A1 manifest contract.
3. **Page-size headroom:** the trend sparks (320,789 B of growth) move behind the holding popover, or are capped. A planted heavy day
   refuses loudly and keeps the prior page.
4. **The census understates 33 GICS rows** (ETFT 9, PCLG 11, TSEL 9, WCMG 4): the census reads the rankings' own classification.
5. **The same-date tie in the name pick** (57 + 17 cells): one deterministic tie-break.
6. **The 33-item walk register (PRD v0.13):** every RFW item not yet REALIZED on the served page is cut or named with its
   remaining cause. RFW-D06 is graded per fix landed, against the census measures.

## 4. ACTS FOR ANDREW (cited; no decision listed)

- A dedicated OpenAI project key for `rivalfunds/openai-api-key`: his OpenAI console. The current value is a labelled copy.
