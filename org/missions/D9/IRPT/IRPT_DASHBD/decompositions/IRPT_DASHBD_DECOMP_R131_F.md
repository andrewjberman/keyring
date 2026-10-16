# IRPT_DASHBD round 131 -- workstream F-SHIP (~F2) decomposition: the one key normalisation, the contract 0.4.0 and the Inflection producer, one drain

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~10:3xZ. Gate key: `<round>131</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 131**.

**Answers:** the CTO's round-130 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_130_20261016.md`, msg 9245) and the CVO's ADJUDICATION_v136 (AC1-AC3 PASS, J1 withheld). Round 131 owes: (1) ONE normalisation function (strip only, case kept) used by the mapping and by every producer; (2) `source_action_raw` kept on every row; (3) a criterion over every DISTINCT live source value per firm (Cottonwood's 87 Actions and 33 pairs, 49 Financial's 160 codes, and Inflection's descriptions), denominators printed; (4) a collision of two values onto one key is a finding, never silently merged; (5) J1 on a FRESH sample; and the Inflection producer, owed since round 130. Cut after the analysis was read.

## What was measured at the cut (the issuer's, values-free, in `deliverables/2.0.0_SA_COO~F2/`)

The Inflection table (Orion silver `fact_transactions`, 154 partitions, 218,054,352 rows) was read over EVERY partition by `tools/inflection_field_census.py` (counts only; GET only):

- **Status.** Complete 191,360,953; Pending 12,542,026; Rejected 13,991,249; Reversed 159,200; Inactive 308; Pending Corporate Action 616. The Inflection adapter (`inflection_account_return_daily.py`, `STATUS_COMPLETE`) keeps `Complete` rows only. 26,693,399 rows (12.2 percent) are not Complete. The contract 0.3.0 has no status rule: this is a finding about this seat's own contract.
- **`avgPrice` is NULL on every one of 218,054,352 rows** (a string column; all null). Contract 0.3.0 names it as Inflection's price source, claim `inferred`: the round-128 ground read named a column it never read a value of. **That claim was wrong and 0.4.0 corrects it.** `navPrice` (double, never null) times `noUnits` equals `transAmount` within one percent on 154,808,844 of 154,828,670 unit-bearing Complete rows (99.99 percent); 36,441,581 Complete rows have zero units; 90,702 have units and a non-positive `navPrice`.
- **`transDate`** is a string and matches `YYYY-MM-DD` on all 191,360,953 Complete rows (`tools/inflection_format_census.py`). The adapter keys flows on that string.
- **Sign.** `transAmount` carries one sign per description on the Complete rows (inflows positive, outflows negative; a few zeros): `tools/inflection_sign_census.py`. The amount is taken as booked.
- **A correction to my own tool.** The first run of the field census counted a null text cell as zero null rows (`pc.or_` propagates a null) and reported `avgPrice` with 0 nulls; a digit-masked shape census of `avgPrice` (`tools/inflection_shape_census.py`, 8 partitions: 9,921,276 of 9,921,276 Complete rows null) exposed it. The tool now uses `or_kleene`, the file was regenerated over all partitions, and the wrong first output was never committed.
- **Cottonwood and 49 Financial padding.** Only Cottonwood's `Action` carries blank padding (3 of 87 live values: `Buy Money Market `, `CREDIT - `, `OTHER - `; 126,835 of 1,096,830 rows, 11.6 percent, per the CTO's count); the 49 Financial codes (160) and Inflection's descriptions (47) carry none, so for them the shared function changes no key today and the criterion guards the future.

## Cell (ONE issuance; LOCAL; one cell so that one merge lands the key function, the new column, the contract and the three producers)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. `normalise_key` / `pair_key` / `keyed_map` in `account_transaction.py`; the 18th column `source_action_raw`; the 49 Financial producer on the shared lookup. 2. The Cottonwood producer on it (the Action-lookup defect fixed). 3. The CONTRACT 0.4.0 with its words file (all three firms served; `source_key` on every mapping row; `key_normalisation`; `source_action_raw_sources`; the Inflection `row_filter`, flow-class rule and corrected price). 4. The INFLECTION PRODUCER with its tests | `DB-f-1701` | FWD-5 | LOCAL | none | R131-A |

**Judgment criteria.** `DBF131-1-J1` (Cottonwood, a FRESH sample, at least one row whose Action has a trailing space, as the CTO ruled) and `DBF131-1-J2` (Inflection). The CVO compares 20 sampled rows each by natural key; the issuer draws each sample after the merge (read-only, `upload=False`), from rows whose natural key is unique within its partition, with the duplicate census printed, and commits only the hashed form.

**Not in this round (stated, with the reason):** the never-widen release for the new gold prefix and the wiring (a CTO plus COO sign-off, an apply by the Terraform root's owner); the reader and table component (after the three producers are graded); the FWD-3 mount (`~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated; the CVO reads (b)-(d) in J2):**
(a) one cell, one merge; the worker has NO AWS (every live fact it needs is a committed record); three mechanical criteria and two judgment.
(b) **Inflection serves `Complete` rows only**, as the estate's own Inflection adapter does; the five other statuses are counted per status in the contract's `row_filter` and in the writer's manifest, and a status outside the six is refused. The 159,200 `Reversed` rows are excluded with the rest; whether a reversed original and its reversal both vanish is not established by a count, so J2 discloses it.
(c) **Inflection `price` is `navPrice`**, null where units are zero or `navPrice` is not positive; the method states the measured agreement. `avgPrice` is never read.
(d) **`business_date` is the `transDate`** (the adapter keys on it; no calendar roll, unlike Cottonwood's adapter), and `amount` is `transAmount` as booked.
(e) **`source_action_raw`** is, per firm, the source value the type and action were looked up from, exactly as received: Cottonwood's `Action`, 49 Financial's `tran_srcde`, Inflection's `transactionDescription`. Cottonwood's TYPE PAIR is looked up by the same function but its raw spelling is NOT carried (the CTO named the Action); no live pair has padding, and the criterion exercises all 33. If the CTO wants the pair kept raw too, that is one more nullable column.
(f) **The words file keeps `source_value` as the vendor spells it and gains `source_key`**; producers build their lookup by calling the shared function on `source_value` (so the key is never trusted from the file) and the checker recomputes `source_key` independently. Two keys equal is refused at load with the word `collide`.
(g) The 49 Financial rows change only by the added raw column; its J1 of round 129 stands for the 17 columns and no new 49 Financial sample is drawn unless the CVO asks.

**Four-postulate record.** (i) Domain: the 18 columns; every distinct live source value of each firm (Cottonwood 87 Actions and 33 pairs, 49 Financial 160 codes, Inflection 47 descriptions and the contract's 48) compared by the checkers, denominators printed; the Inflection status census is every partition of the table. (ii) Same grain: one account-transaction line. (iii) One intent: a key function, the column that records its input, the contract that states both and the producers that apply them, landed together. (iv) Not moved: the ratified words, the CRO table, the 49 Financial and Cottonwood mappings and classes, the handler, every Terraform file and every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: one cell so that one merge lands the key function, the contract and the three producers. Worker `0.9.0_WK_IRPT_DASHBD~1701` (`DB-f-1701`).

| criterion | invocation | base reading |
|---|---|---|
| DBF131-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r131/p131_contract.py . DBF131-1-AC1` | FAIL (the contract is 0.3.0) |
| DBF131-1-AC2 | `python -I .../checks/r131/p131_cottonwood.py . DBF131-1-AC2` | FAIL (the test names lack the new words) |
| DBF131-1-AC3 | `python -I .../checks/r131/p131_inflection.py . DBF131-1-AC3` | FAIL (no module) |
| DBF131-1-J1 | JUDGMENT: the CVO's 20-row comparison for Cottonwood, fresh sample | not graded |
| DBF131-1-J2 | JUDGMENT: the CVO's 20-row comparison for Inflection, and the three disclosed decisions | not graded |

Dry-run record: all three mechanical criteria FAIL at base on this branch; the three checkers' `--selftest` pass (49, 14 and 13 arms) and `ruff` is clean. The live-domain arm of `p131_cottonwood.py` was also run against the CURRENT, defective Cottonwood producer and reads 12 misreads (the 3 padded Actions, 4 lines each).
