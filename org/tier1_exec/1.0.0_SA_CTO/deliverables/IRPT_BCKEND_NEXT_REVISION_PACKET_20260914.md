# IRPT_BCKEND -- THE NEXT PRD REVISION'S INPUTS (v0.14 -> v0.15), READY FOR ROUND 2's L10

**Seat:** `1.0.0_SA_CTO`, the author of IRPT_BCKEND's L4 · **Stamp:** 2026-09-14 ~14:1xZ.
**Authority:** Andrew-direct ~13:4xZ, *"recs + sequence approved"*, `/next-calls` OPTION 2 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_134xZ_NEXT_CALLS_RECS_AND_SEQUENCE_APPROVED.md`).

**What this is:** a document, not a PRD edit. IRPT_BCKEND is mid-round, and a round's specification is frozen, so
nothing here lands until round 2's slug reaches this seat. At that point this is the L10 answer's first draft, and the
slug may add to it.

**What this is not:** a re-measurement. Every figure below is cited to the read that produced it, with its vintage.

---

## 0. WHERE ROUND 2 STANDS -- READ FROM THE ORDERS, NOT FROM A REPORT

- **29 of 31 orders are complete.** Two remain:
  - `IB-rt-6` is PENDING. Its gate has been satisfied since 2026-09-12T05:48:29Z, and the 09-12 02:40 amendment granted its IAM path in `<paths>`. It was handed to worker slot ~2, which ran under `2.0.0_SA_COO~B`'s session, and that session is not live. **By its own face, nothing else in the round moves until it closes.**
  - `IB-rtb-1` is STAGED behind `IB-rt-6`, by its own text.
- **The 09-12 contradiction report reads rt-6 as "IAM-blocked".** That was true when the report was written; the amendment since has overtaken it. What blocks the round now is the missing seat.
- **Placement:** `org/missions/SEQUENCE.yaml` v3 (@`4acacb9bba`) puts IRPT_BCKEND in stage 3, fifth for a free COO seat. Moving it earlier is Andrew's word.

---

## 1. THE THREE CANON CONTRADICTIONS -- `infra/logic/03_CONTRADICTION_REPORTS/IRPT_BCKEND.md` v2.1 (@`a4cc0cb681`)

Today's LGIC_NAMING rulings (v1.4, ADMITTED) turn two of the three into direct answers.

| # | the contradiction | proposed v0.15 answer | lands in | half |
|---|---|---|---|---|
| 1b | The served platinum key has no tier segment (`<firm bucket>/investor-reporting/...`), which contradicts R1 | Adopt the ruled five-segment key from `LGIC_ENFORCE`'s `key()`, with `{source}` as the registry's product key for investor reporting (the registry's row, not typed here). **It costs nothing now:** no production directory artifact has ever existed for any firm (`W2-S47`), so no served byte moves, and `key.legacy_served_paths` does not apply (a path is legacy only if the frozen portal requests it) | CONTRACTS (the firm-bucket destination), PATHS | ratified-text + brief |
| 2 | There is no gold parquet artifact between silver and the served JSON for derived client data (R11 + R14) | Name the gold artifact per firm, at `{source}/{firm}/gold/{table}/date=YYYY-MM-DD/`, in the firm bucket (R5/R6 client gold). Its accrual basis is `SPEC_IRPT_GOLD_ACCRUAL_MDPF_20260912.md`. The platinum JSON is then produced FROM it at one boundary (R12) | DECISIONS, the cell that writes gold, PATHS | brief |
| 3 | Vendor PDFs and ZIPs land in `opal-data-ycharts`, which partly contradicts R4 | Land vendor deliverables at bronze in the monolith, `opal-data-assets/ycharts/{firm}/bronze/...`, keyed by `key()`. If SSE-KMS isolation is the reason to keep the vendor bucket, the revision says so as an R20 exception with its reason. **Andrew's ~13:4xZ ruling (W4-S20):** the four noncurrent synthetic-export versions there are deleted too, after a same-day re-read, with a human confirming at the delete | DECISIONS, PATHS | brief |

**Two neighbours, now decidable:**
- **Row 7, where the runners deploy:** the runners deploy to `opal-data-mdpf/code/scripts/assets_gold/...`, a product bucket, while their output is per-firm platinum. `LGIC_NAMING` S7 (ruled at v1.3) gives code a home in the code tier, beside the gold it builds: `{source}/{firm}/code/gold/{file}`. The row resolves once row 2 names the gold's home.
- **Row 11, `FIRM_BUCKET_MAP`:** the live map names the legacy buckets. It is repointed by `ADVI_FIRMBKTS`'s cutover through `LGIC_ENFORCE`'s registry. SEQUENCE v3 records that dependency on the OUTCOME, and this revision cuts the gate on the cell that carries it (the MDPF_CANON pattern).

---

## 2. ROUND 4's THREE CARRIED ITEMS -- `ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md` s.6, items 4-6

| item | what | lands in | half |
|---|---|---|---|
| 4 | **RULING L:** a target-basis snapshot without a named model revision is UNCERTAIN, in the contract, on the producer side | CONTRACTS (`HoldingsSnapshot`) | ratified-text |
| 5 | **The smoke-map seam's producer side (S40 / W2-S15).** `_contracts/tests/test_seam_paired.py` read 14 failed, 39 passed at round 4's read, because the test asserts flat-slug keys while the consumer's map carries the v1 DECLARED paths. Row `IRPT_BCKEND-S51` carries it. **Not re-measured here** | a repair cell | brief |
| 6 | **The producer's copy of `StatusEnvelope` never received v0.14's amendment:** `business_date` is REQUIRED on every state there, against the consumer's conditional rule (row `IRPT_BCKEND-S51`). One contract, two copies, out of sync | CONTRACTS (`StatusEnvelope`: one copy, or a stated pin between them) | ratified-text |

---

## 3. THE FIVE CONTRACT GAPS FROM IRPT_FNTEND ROUND 5 -- row `IRPT_BCKEND-S52` (@`d4fe023415`)

| gap | proposed v0.15 answer | contract |
|---|---|---|
| The window reason code `REQUESTED_WINDOW_ANSWERED` is defined nowhere | Name every window reason code in the contract. Windows are compared by trading day (IRPT_FNTEND RULING T) | `StatusEnvelope` / `PerformanceReport` |
| No `report_title`; no analysis-POST request schema | Add `report_title` and the POST's request schema, with its producer and consumer fixtures | `AnalysisRequest`, `AnalysisReport` |
| No scope-level `node_kind` | Add it at the scope level | `HoldingsSnapshot` / `ResolvedScope` |
| The Global view's resolve-scope reaches 1 of 2 firms' Holdings (FWD-11 stays PARTIAL) | Global answers every permitted firm, and says partial with a reason when one is unavailable | `ResolvedScope` |
| `ADVISORY` reaches a READY answer outside its enum | Either the enum grows or the producer stops emitting it. The revision picks one, from the producer's rule | the enum's owner contract |

---

## 4. TODAY'S RULINGS THAT BIND IT

- **`LGIC_NAMING` v1.4, ADMITTED:**
  - the entity partition (S6);
  - the code tier (S7);
  - legacy served paths kept byte-for-byte (S8);
  - legacy membership as data (S10).

  Every new address comes from `LGIC_ENFORCE`'s builders, so the key-bearing cells wait on its E3, as ADVI_FIRMBKTS and MDPF_CANON already do.
- **`ADVI_FIRMBKTS` v1.2's tenant boundary** (DEC-3; CONTRACTS, SIGNED): a scoped request is served when the path's firm resolves, through the registry, to the caller's validated tenant bucket, the staff `?firm=` proxy included. Investor Reporting's `/api/scoped/` behaviour inherits it.
- **Andrew ~13:4xZ:** ruling 8(b), W4-S20, above.
- **Andrew ~14:5xZ, verbatim:** *"No, we need the logic projects done first because that will establish the patterns for the new backend properly"* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_145xZ_LOGIC_FIRST_THE_BACKEND_FOLLOWS_ITS_PATTERNS.md`). The backend waits for Platform Logic, and v0.15 is built ON its patterns: the ruled key string from `LGIC_ENFORCE`'s builders, the identity registry and its generated views, and the canon's tier and home rules. It never works around them. Every s.1 answer above is written to that rule, and any item round 2's slug adds is held to it.

---

## 5. WHAT THE REVISION COSTS, AND WHAT IT DOES NOT CLAIM

- **Both halves re-open.** CONTRACTS changes on at least `HoldingsSnapshot`, `StatusEnvelope`, `AnalysisRequest`, `ResolvedScope` and the platinum destination. The brief half changes on the gold, the vendor bronze, the code home and the repair cell.
- **Not claimed:**
  - the seam test's state today;
  - which enum owner decides `ADVISORY`;
  - the investor-reporting product's registry key (that is `LGIC_ENFORCE`'s row);
  - any item round 2's slug adds.
