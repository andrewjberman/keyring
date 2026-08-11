# 49F GOLD ANALYTICS RUNNER -- GROUP C SPEC (FLOW LEDGER / GIPS TWR ENGINE / VALIDATION / LINEAGE)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0755Z** · **archetype:** IMPLEMENT (design)
**Commission:** @5e4b8dda98, sequential -- GROUP C, follows A @9c294bbf15(+@6fba62393b) and
B @d57bbf7229. For CTO review.
**Bound truth:** classification table @a876ee6ae9 (187 codes / 2,982,720 rows, full-universe;
TPFEE/SMFEE VERIFIED @5bb3b2626d) · pair-matching engine @5bb3b2626d (`pair_match_engine.py`,
committed + re-runnable) · the four estate truths (gross_amount is THE money column · code
universe 157 · 680K sweep rows INTERNAL · reinvestments = the empty category) · GIPS sec4-sec10
verbatim · feasibility method tier: **DAILY TWR, one tier above the GIPS monthly minimum;
Modified Dietz NOT NEEDED** @e323c1cfac.

---

## 0. WHAT GROUP C IS

Group C is where the money math lives: the sec4 external-cash-flow ledger, the sec5/sec6 daily
TWR engine, the sec9 validation battery, and the sec10 output contract. **Everything consumes
A's frame (boundary_version, calendar, classification reference) and B's valuation plane
(fair_value, flags, integrity) -- C never re-derives them.** The standard's canonical decision 4
binds the whole group: **realized/unrealized/tax-lot/cost-basis facts are VALIDATION inputs,
never return inputs** -- the attribution families (fact_rld/rlu/rly/rtu/rty/uln/ult/upn/upt)
enter ONLY at C_04.

## 1. THE FIVE GROUP C ARTIFACTS

Home: `{PRODUCT_ROOT}/canonical/{artifact}/date={D}/` (+ per-period partitions where the grain is
a period, stated per row). Existing-corpus disposition per instruction 4 is stated per row.

| # | Script | Inputs | Output / grain | Contract |
|---|---|---|---|---|
| C_00 | `c00_flow_ledger.py` (NEW; ABSORBS `pair_match_engine.py` as its resolution stage) | `fact_trn` x `ref_txn_classification` (A_05) x `dim_boundary` (A_02) x B_01 prices (in-kind valuation) | `flow_ledger` -- (account_id, date, txn_ref) | Sec4 verbatim, per row: signed amount from **`gross_amount`** (the measured money column -- net_amount is $0.00 on 1.9M cash rows and computes zero external flow silently), sign = capital-in positive / capital-out negative; direction for the 5 generic-EXTERNAL codes resolved per-code via debit_credit AT BUILD and recorded in the table -- **AMENDED (CTO review 072553Z): the resolution VERIFIES the semantic boundary with a printed census -- debit_credit is direction-semantic on CASH rows and POSITION-SIDE on IC rows, so every row of those 5 codes is verified cash-class before direction is read, and any IC-class row under them fails LOUD to UNRESOLVED (the trap's boundary lives in the artifact, not the builder's memory)**; **cash vs in-kind designation, in-kind valued qty x same-date close** (B_01; zero-price in-kind rows carry qty-only + a flag, per the specimen's boundary note); CONDITIONAL-BY-COUNTERPARTY resolved by the PAIR-MATCH stage (exact-amount same-day cross-account opposite-DC; matched -> INTERNAL, unmatched -> EXTERNAL-BY-DEFAULT -- conservative toward external, the standard's safe direction); one-sided in-kind direction corroborated via NEXT-DAY POSITION DELTA (dim_position) per the named follow-up; reversal linkage columns (`r_dc`/`r_cc`/`r_cy`, `tranproc_date`, `cycle_id`) carried through -- SPECIMEN-PENDING status until the 525-partition reversal scan lands (refinement cell 5, run once at build); final class enum: EXTERNAL / INTERNAL / FEE-MANAGEMENT / FEE-ADMIN / UNRESOLVED + `resolution_provenance` (code-rule / pair-match / position-delta / swb-columns / **same-account-type-transfer / text-counterpart** -- the last two ADDED per the 50%-external-by-default ruling, CTO 105759Z + DS 105703Z, all-firms class default: **same-account-type-transfer** = single-account `TRF FDS FRM/TO TYPE n` grammar -> INTERNAL by construction, the class the different-accounts pair-matcher was structurally BLIND to (40 rows netting $0.00 exact); **text-counterpart** = 8-digit account extraction from detail text WITH the in-book existence guard against A_02's universe -- unmatched-in-book stays external-by-default; the 4 genuine ACAT legs remain the conservative default's correct territory). Unknown codes fail LOUD to UNRESOLVED (the table is a first-match rule list, not a roster) |
| C_01 | `c01_nna_canonical.py` (**EXTRACT c03_nna, RE-BASED**) | C_00 | `nna_canonical` -- (account_id, date) + rollups | NNA = the ratified calculated exception (flow class, @d272021791 -- distinct from the non-fee residual, never re-merged). **Re-based ON the flow ledger** so ONE flow truth feeds both NNA and TWR -- the existing c03's own logic survives where it agrees; where it disagrees with C_00 the DIFF is the migration finding, not silently either. **ADVREVIEW F-4 ACCEPTED (per-consumer conservatism): C_00's EXTERNAL-BY-DEFAULT is conservative for TWR but ANTI-conservative for NNA (an unmatched intra-book transfer read as external INFLATES the client-facing flow number) -- so C_01 consumes `resolution_provenance` and books EXTERNAL-BY-DEFAULT rows into a SEGREGATED line (`nna_unresolved_direction`) with its census; the headline NNA carries matched+code-resolved flows only. TWR keeps the safe default; NNA stops inheriting its bias** |
| C_02 | `c02_twr_engine.py` (NEW; c00_account_gains/c01_account_performance map INTO it per the quality partition -- their period-resolution + refuse-on-no-BMV blocks are EXTRACT-grade, their return math is superseded by the GIPS forms) | B_00 `fair_value` + C_00 external flows + A_04 calendar | `twr_daily` -- (account_id, date); `twr_periods` -- (account_id, period) | Sec6 verbatim: **EOD flow convention (default, DECISION-FOR-REVIEW): r(t) = [EMV(t) - CF(t)] / BMV(t) - 1**, one documented convention applied consistently; BMV = prior-trading-day fair_value (A_04 prev-resolution; REFUSE-not-fabricate on missing BMV, the existing corpus's own proven guard); **zero/near-zero denominator -> subperiod marked UNCOMPUTABLE, never forced**; period returns by GEOMETRIC LINKING only ("Never sum daily or monthly returns"): TWR(a,b) = PRODUCT(1+r(t)) - 1 for MTD/QTD/YTD/ITD + rolling 1y; **GROSS and NET pair per sec8**: net retains FEE-MANAGEMENT debits; gross adds back FEE-MANAGEMENT (VERIFIED family: MGFEE/TPFEE/SMFEE); transaction costs remain deducted in BOTH (embedded in trade amounts -- sec8's "gross-of-fees does not mean before every cost"); FEE-ADMIN treatment = RULED POLICY (below) |
| C_03 | `c03_twr_lineage.py` (NEW, thin) | C_02 + C_00 + B_01/B_03 flags + C_04 grades | `twr_lineage` -- (account_id, period) | Sec10 verbatim, every field: boundary_version · period start/end · BMV/EMV · external-flow total + flow refs · subperiod + linked return · method (**TRUE_TWR-daily**) + flow-timing convention · gross/net designation · base currency USD + FX policy N/A-BY-BOUNDARY · valuation coverage + source lineage · unresolved-flow count + stale-price count · reconciliation variance + data-quality status. **Acceptance status per the sec10 enum, MECHANICALLY derived**: TRUE_TWR (complete inputs) / INDICATIVE_ONLY (named limitation present) / UNSUPPORTED (missing BMV-EMV, material unresolved flows, invalid denominators -- the hard-stop conditions AS a status, per account-period, never a global verdict). ESTIMATED_TWR_MODIFIED_DIETZ structurally unreachable (daily tier) and stated so |
| C_04 | `c04_validation_battery.py` (**EXTRACT c04_recon_guard as the seed, WIDENED to sec9's nine**) | B_00/B_03 + C_00/C_02 + attribution families (validation-only) | `validation_battery` -- (account_id, period, check) | Sec9, each check a graded row: position-tie (consumes B_03, never recomputes) · cash-txn-vs-balance roll · every-movement-classified (C_00 UNRESOLVED census) · BMV-rolls-from-prior-EMV across boundary events · missing/stale/zero price flags (B_01) · matched-internal transfers NET TO ZERO · large/anomalous return census (ex-ante threshold, ruled) · Schwab-native return tie = **UNAVAILABLE-BY-MEASUREMENT** (no computed-returns table in all 20 silver tables -- documented, not skipped) · **Economic P&L identity: EMV - BMV - SUM(CF) explained by realized + unrealized-change + income + fees within documented tolerance** -- THE consumption point for fact_rld/rlu/uln/upn, validation-only per canonical decision 4 · **monthly cross-check vs `fact_rly`/`fact_rty` (RULED C-side, CTO 072235Z): vendor MONTHLY aggregates are a genuinely INDEPENDENT DERIVATION from our daily-compounded TWR -- the tie is EVIDENCE precisely because the legs differ in derivation (the shared-derivation law satisfied by construction)** |

## 2. RULED POLICIES (sec8 -- each a DECISION-FOR-REVIEW with a stated default; the engine reads them from a POLICY block in the product root, never hardcodes)

1. **Flow-timing convention:** default **EOD** (r = (EMV-CF)/BMV - 1) -- matches Schwab EOD
   statement-close valuations with same-day-dated flows; documented in every lineage row.
2. **Dividend recognition:** GIPS PREFERS ex-date accrual; the estate ships cash receipts.
   Default: **cash-receipt basis, DOCUMENTED as the convention** in lineage (upgrade path to
   ex-date accrual named as a future policy flip, not built now -- YAGNI until Andrew wants it).
3. **FEE-ADMIN ($34,305 / 2,597 rows -- measured-small):** default **retained in BOTH gross and
   net** (custody/admin class, sec8's "document whether included" satisfied by the policy block).
4. **Anomalous-return threshold (sec9):** default |r(t)| > 5% on a single account-day flags for
   census (not suppression). **RULED (072553Z): confirmed ex-ante with the B_03-class qualifier --
   post-backfill the |r(t)| distribution reports and any re-set is a RULED event on the
   distribution; a threshold is never tuned to quiet its own census.**
5. **B_03 tie tolerance consumption:** C_04 inherits whatever CTO rules on the B review -- one
   tolerance, two consumers, zero re-derivation.

## 3. THE QUALITY PARTITION OF THE EXISTING C-CORPUS (instruction 4, applied)

**EXTRACT (quality structure):** c03_nna's flow logic (re-based on C_00) · c04_recon_guard (the
battery seed) · c00/c01's period-resolution + REFUSE-on-no-BMV guards (into C_02's frame).
**SUPERSEDED (methodologically replaced, not "wrong"):** c00_account_gains / c01_account_performance
/ c02_client_performance RETURN MATH -- gains-based measures are exactly what canonical decision 4
demotes to validation; their economic content survives as C_04's P&L-identity inputs. Each
superseded piece gets its verdict + grounding recorded at build (certified-cells-never-catalog:
the partition table is the deliverable, per-script rows with evidence).

## 4. WHAT GROUP C DOES NOT DO

No serving (D owns every emitter; C outputs are gold-tier canonicals). No composite/firm-level
GIPS presentation (the .rtf's own scope note: calculation feasibility, not firm-wide compliance --
composites ride dim_relationship in a FUTURE group Andrew commissions or doesn't). No household
grain in v1 beyond what C_01's rollups already carry (A_01 unlocks it; the projection is D's).
No alarms/monitors (moratorium); the battery emits DATA.

## 5. ACCEPTANCE (machine-checkable)

- C_00: every fact_trn row on the partition lands in exactly ONE final class (row-count identity,
  in == out + declared exclusions; UNRESOLVED census printed with the materiality frame);
  pair-match determinism (two same-input runs); the IC-trap mutant (a direction-keyed matcher on
  l_s/debit_credit position-side rows) MUST fail loud, not return 0.0% clean.
- C_01: diff-vs-existing-c03 printed on the same partition (the migration finding surface).
- C_02: the GIPS formula identities on synthetic fixtures (known BMV/EMV/CF -> known r, both
  conventions; geometric-vs-summed divergence fixture proves linking); zero-denominator fixture
  -> UNCOMPUTABLE, never a number; gross-net spread == fee add-back identity on a sampled account.
- C_03: every lineage field non-null or explicitly N/A-BY-BOUNDARY; acceptance-status derivation
  is a pure function of its inputs (mutant: inject one unresolved material flow -> UNSUPPORTED).
- C_04: all nine checks emit a grade (SKIPPED is not a grade; UNAVAILABLE-BY-MEASUREMENT is);
  the P&L identity control on one known account-month with hand-derived components.
- All: provenance cols, manifests, boundary_version stamps, policy-block vintage stamped.

-- 3.0.0_SA_CVO
