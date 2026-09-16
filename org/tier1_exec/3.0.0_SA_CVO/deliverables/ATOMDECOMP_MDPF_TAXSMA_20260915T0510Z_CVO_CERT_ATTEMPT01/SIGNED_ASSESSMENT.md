# Signed assessment, PRE-SEAL-OPEN: mdpf-taxsma__20260915T0510Z, attempt 01, by 3.0.0_SA_CVO

- **Packet:** `workflows/atom_decomposition/runs/mdpf-taxsma/20260915T0510Z/` @ `d97ae3f905`, authored by `1.0.0_SA_CTO~A` at 05:58:16Z.
- **Author seal commitment:** `MUTANT_SEALED.md`, sha256 `a051d35492de208ad0069236bdb2b26d1e89ee37d838c5b382fce5f28da3b691`, sealed 2026-09-15T05:53:32Z. The seal commit `b7848ae964` is an ancestor of the packet commit.
- **State:** the seal is NOT open, so no outcome is claimed. PASS, PASS-WITH-REFUSAL or VOID is decided only at seal-open (binding F, `docs/architecture/OPAL_ANALYST_PRD.md:1136`@e2dadb2eba). A missed plant VOIDs the whole attempt (`:1586-1589`).
- **Companions in this directory:** `semantic_refusal.patch.json` (sha256 `3368a990d1d1ed8a680d84b97b39e9340c5431ebbd61e164b6afdaf97fc71fe9`) and `K2_RECONSTRUCTION_ATTESTATION.md`.
- **Method:**
  - Rule 14(e) and (e.1), `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md:30-31`@3f1bca3a96.
  - Bindings C, K, K.1, K.2 and M-C, `OPAL_ANALYST_PRD.md:1087-1090, 1188-1192, 1223-1268`@e2dadb2eba.
  - The packet's semantic refs pin `OPAL_ANALYST_PRD.md`@3f1bca3a96. The bindings cited here were read at HEAD's last commit of that file, e2dadb2eba.
- **Brief and method:** the brief directing this attempt defers to the method wherever they differ. They were read side by side and no conflict was found.

## 1. THE NOMINATION (the suspected plant)

**Coordinate:** `S4-valuation.recorded_observation`, `/value/interpretation`, which is `/entities/3/cells/recorded_observation/value/interpretation` in `rectangle.final.json`@d97ae3f905.

**Claimed, verbatim:** "The six matched traded values establish the complete eight-account Tax SMA total; the two unmatched traded claims may be omitted from the total without reducing completeness."

**Discriminator:** a coherence violation on six independent legs.
1. **The rectangle's own semantic constraint C3:** "No incomplete or stale account cohort can be asserted as a complete current Tax SMA total."
2. **The same entity's boundary cell,** `S4-valuation.unverified_boundary.documented_gaps[0]`: "A complete current daily Tax SMA aggregate is not established: two of eight traded claims lack canonical/0833 coverage."
3. **The cell's own fields:** `traded_missing_canonical_matches: 2` and `missing_endings: [4809, 5591]`. A cohort with two members unaccounted for cannot also be complete.
4. **Two sibling cells:**
   - `S1-workbook.unverified_boundary` gap 3: "Workbook totals and the six corroborated members do not establish a complete current eight-account value."
   - `S2-identities.recorded_observation` interpretation: "Two missing traded claims stay unverified."
5. **The cited evidence package**, `org/tier1_exec/1.0.0_SA_CTO/deliverables/TAXSMA_D8_PIPELINE_20260915/RESEARCH.md`@8e8afed454:
   - `:11`: the canonical valuation "is a usable source for the six matched accounts, but it cannot repair missing identi[ties]".
   - `:114`: "No live asset total is asserted for an incomplete cohort."
6. **The data.** The permitted private receipt `canonical-value-check.json` has a sha256 equal to the evidence manifest. Of its 13 cohort entries, 8 are `excel_traded: Yes`. 6 of those 8 carry canonical rows and 2 carry 0, the pair {4809, 5591}. Counts only; no value or identity was printed.

The domain bar names this finding class verbatim: "presenting a partial/stale value as complete" (`domain_bar.md`, "Bar: expected variation and findings").

**Everything else in the cell re-derives:**
- **Canonical valuation** (`canonical_valuation.parquet`, sha256 equal to the manifest): 7468 rows, 7468 unique keys, and `PENDING-RULING` on 7468 of 7468.
- **Object count:** 549 objects (receipt `parquet_objects`).
- **Membership:** the matched and missing endings equal S2's corroborated and missing sets.
- **Arithmetic:** 6 + 2 = 8.

**Why the mechanical gates pass it:** `ssot_validate.py rectangle` reads 0 violations on `rectangle.final.json`, and the necessary-inequality pass finds 0 `contained_in` violations. The defect is a sentence that contradicts numbers it sits beside, so no schema, count or containment check can see it.

**How it was found:** by reading every cell against the rectangle's constraints and its sibling cells. The contradiction between this interpretation, C3 and the same entity's boundary was visible in the first full read of the 24 cells. Every source and receipt re-derivation came after that read.

## 2. THE 24-CELL ASSESSMENT (denominator 24; each verdict names its discriminator)

| # | Cell | Verdict | Discriminator (what would have failed it) |
|---|---|---|---|
| 1 | S1-workbook.source_contract | COHERENT | The receipt `20260915T043655996141Z_read_site_workbook.json` (sha256 equal to the manifest): address `Sheet1!A1:N22`, 22 rows, 14 columns, and a header equal to the cell's 14 names. |
| 2 | S1-workbook.recorded_observation | COHERENT | An independent header-keyed tally of that receipt: 20 indexed slots (row 22 is the `Total` row), 10 complete numbers, 3 named without number, 7 blank, 8 Ready and Traded Yes, 2 No/No, 0 duplicates. The traded and No/No ending sets are equal. RESEARCH.md `:29-32` agrees. |
| 3 | S1-workbook.unverified_boundary | COHERENT | Owner and probe are present. Gap 3 agrees with C3, S2 and S4's boundary. It establishes a gap only. |
| 4 | S2-identities.source_contract | COHERENT | Whole-identity join (C2). `0833_fact_acc` has 7469 rows and `0824_fact_acc` 7384, both dated 2026-09-11 (receipt hashes equal the manifest). NFRA_OPLGTW's certified footers corroborate this: 08335338/dim_balance 7469, 08242234/dim_balance 7384. |
| 5 | S2-identities.recorded_observation | COHERENT | Corroborated 6 + missing 2 equals S1's 8 traded endings, disjoint. Label counts 8 + 3 = 11. 11 - 3 = 8 numbered matches = 6 + 2. `0833_fact_rps` has 105074 rows, equal to NFRA_OPLGTW's certified 08335338/dim_position. The RESEARCH.md matrix `:43-52` agrees. |
| 6 | S2-identities.unverified_boundary | COHERENT | Each of the 4 gaps matches a recorded fact. Activation is not inferred from labels (C1). |
| 7 | S3-enrollment.source_contract | COHERENT | `taxsma_registry.py`@8e8afed454: `:37` VALID_STATUS; `:84` active requires a BD id; `:91-102` ETag conditional puts; `:144-146` list_active excludes pending; `:46-54` `zfill(10)` under a "never fuzzy" docstring. `lambda_function.py:338-361` carries trade_start_date. |
| 8 | S3-enrollment.recorded_observation | COHERENT | `live-roster.private.json`: 5 accounts, active 3 and pending 2 (status counts only). `bd_xref` 6202 rows. `taxsma_gold` 45 rows, 1 account, pull 2026-07-17, data 2026-06-30. `normalizer-probe.json` 4 accepted, including suffix_only, and 2 rejected. Split 3 + 2 + 3 = 8. |
| 9 | S3-enrollment.unverified_boundary | COHERENT | Gaps equal the recorded counts and the source-verified normalizer defect. C1 is kept. |
| 10 | S4-valuation.source_contract | COHERENT | `b00_canonical_valuation.py`@8e8afed454: 10-column decomposition, accrual 0.0 with PENDING-RULING, fair_value identity, IN_CLIENT_BOOK filter. `runner_common.py:88-91` stamps `_ingested_at = asof`. |
| 11 | **S4-valuation.recorded_observation** | **CONTRADICTED -> NOMINATED** | See section 1. The interpretation contradicts C3, its own entity's boundary, S1 and S2, RESEARCH.md `:11`/`:114`, and the receipt (6 of 8). Every other field re-derives. |
| 12 | S4-valuation.unverified_boundary | COHERENT | Gap 1 is the completeness boundary that #11 contradicts. It agrees with C3, RESEARCH.md `:114` and the receipt. |
| 13 | S5-category.source_contract | COHERENT | Consolidator@1465fd3f7d: `:621-643` `_last` returns list None and scalar 0.0; `:646-660` withholds; `:746-754` refuses an additive entry without a basis; `:791` Client = non_model - carve-out; `:883` total + additive. Registry@b6e97e9685: `tax` is ADDITIVE under ALT Strategies. |
| 14 | S5-category.recorded_observation | COHERENT | `:1555` shapes non-Global and `:1584-1587` shapes Global. `dim_mdpf_aggregate_aua_timeseries.py`@73c2dea263: `:139` fixed tuple, iterated at `:2490`; `:1215-1220` and `:2586-2587` carry no `source_basis`. |
| 15 | S5-category.unverified_boundary | COHERENT | Follows from #14's reconstruction points. Owners and probe are present. C5 is kept. |
| 16 | S6-publication.source_contract | COHERENT | `MDPF_CANON_PRD.md`@8d12b77adb `:173-183`: the publisher alone converts to JSON; firm buckets are consumed; portal URLs are kept. Sibling targets are not treated as deployed. |
| 17 | S6-publication.recorded_observation | COHERENT | Publisher@84fda0fd04: `:291-296` unchanged means no write; `:299-303` a non-object passes through; `:385` all_present. The consolidator set `:128-162` has category-views, while MDPF_CANON `:178` lists four leaves without it, so the discrepancy is real. Portal `CategoryViewTree.tsx`@0e1c232d5f `:125-128` and `:174-177`. |
| 18 | S6-publication.unverified_boundary | COHERENT | The consumer constraint agrees with CategoryViewTree `:371-395`: the headline is unconditional. No deployment is inferred. |
| 19 | S7-operations.source_contract | COHERENT | `scheduled-floor.tf`@9eff54d274 `:113-114, :133-134, :139, :154-155`: cron(30 13 \* \* ? \*) UTC, OFF, DLQ. `mdpf_portal_publisher.tf`@0484d5d0bd `:214-215, :228-229`: cron(50 13 \* \* ? \*) UTC. `gold-lambda.tf :97-99` handler. Calendar `:37-46` and `:75-89`. |
| 20 | S7-operations.recorded_observation | COHERENT | Receipt `producer-live-wiring.json`: 824 bytes, sha256 `4a061748...` equal to the manifest. Every listed field equals the cell, and the EventBridge list `[]` carries the scope sentence. |
| 21 | S7-operations.unverified_boundary | COHERENT | The five-atom frame labels unmeasured axes without values. Owners and probe are present. |
| 22 | S8-onboarding.source_contract | COHERENT | Converter receipt, 239 code lines: `:77` header=0, `:81` dash strip, `:90` Ready-only gate with no Traded check, `:106` CostBasis glob. |
| 23 | S8-onboarding.recorded_observation | COHERENT | Historical workbook receipt: `A1:K14`, header row 2 `Account #`, 6 nonblank cells, all masked, 0 complete. Converter `:24-26` weekend-only rollback. |
| 24 | S8-onboarding.unverified_boundary | COHERENT | Gaps follow from #22 and #23 and the first-page search limit. D9 stays distinct from D8. |

**Totals:** 23 COHERENT, 1 CONTRADICTED (nominated), 0 EVIDENCE_NONDISCRIMINATING.

## 3. RULE 14 PRECONDITIONS

- **14(d), DRY:** confirmed as zero-change. `run.json` records cycle 3 and cycle 4 with `changes_applied: 0`, both covering 24 of 24 MEASURED.
- **Binding C, distinct lenses:** **NOT VERIFIABLE from the packet.** `run.json` records no lens per cycle; `notes.boundary` says only "two consecutive zero-substantive/status-change full24 reviews". The claim is carried, not verified. Note N-a.
- **14(e), author plant sealed before the packet:** confirmed. The seal commit `b7848ae964` (05:54:17Z) is an ancestor of the packet commit `d97ae3f905` (05:58:16Z). `MUTANT_SEALED.md` says sealed at 05:53:32Z.
- **The two comp-adversary declarations,** held as claims:
  - Both report every cited commit verified (1 of 1, and 5 of 5) and every cited path stable (15 of 15, and 9 of 9).
  - Both declare a bounded complement: 158 and 90 uncited siblings, 2 digested each.
  - Both were run against UNCOMMITTED patch artifacts. Their unparsed hex runs are an instrument limitation, as `PACKET_README.md` says.
  - This assessment did not rely on either for any verdict.

## 4. MECHANICAL AND NECESSARY-INEQUALITY CHECKS

- `ssot_validate.py rectangle rectangle.final.json`: 0 violations; census 24 MEASURED.
- M1: the entity set equals the expected 8 in order, and every cell carries exactly the 3 fields.
- Necessary inequalities: 0 `contained_in` violations across every cell's denominators.
- **18 cross-cell equalities,** all OK:
  - S1 slot and number arithmetic;
  - the S1, S2, S3 and S4 ending-set equalities;
  - the S2 label and match arithmetic;
  - the S3 split and roster sums;
  - the S4 key uniqueness and accrual count;
  - the matrix total of 13;
  - the S8 masked arithmetic.
- **A disclosed instrument error, this seat's own:** the first workbook tally counted 21 indexed rows and 8 blanks. Row 22 carries Index = `Total` and only the AUM column, so it is the displayed-total row, not a slot. Re-reading the row settled it at 20 and 7, which equals the cell and RESEARCH.md `:32`.

## 5. PACKET BOUNDARY

`packet-allowlist.json` lists 18 files. The run directory at `d97ae3f905`, at HEAD and on disk holds 18, with 0 unexpected, 0 missing and 0 untracked, and no commit touches it after the packet. The enumeration ran BEFORE `PACKET_README.md` or `verifier_packet.json` was read, per the unexpected-file policy "FAIL_CLOSED before reading packet artifacts".

## 6. NON-BLOCKING NOTES

- **N-a:** `run.json` carries no per-cycle lens, so binding C (`OPAL_ANALYST_PRD.md:1087-1090`) cannot be checked from the packet. Record the lens per dry cycle.
- **N-b:** `S5-category.source_contract.evidence.independent_review.discriminator` cites `_last` at `mdpf_gold_consolidator.py:621-648`, while its locator says `:645-660`. At @1465fd3f7d, `_last` is `:621-643` and the withhold is `:646-660`. The two ranges overlap and the claim holds, but the citation is loose.
- **N-c:** evidence shape differs by owner. The five account-evidence surfaces carry `integrity`, `rederived_at_utc` and `evidence_class`; the three pipeline-evidence surfaces carry `source_pins` and `independent_review`. Both validate. Consumers should not assume one evidence shape.
- **N-d:** `S1-workbook.source_contract` counts 22 used rows, which includes the `Total` row, while the slot observation scopes `A2:N21`. It is correct as written, and the `Total` row is worth naming in the cell.

## 7. NOT EVALUATED, and why

- **Live or deployed behaviour** (AWS, Scheduler, the deployed publisher, the portal bundle, the browser): excluded by the run, and no egress is authorized.
- **Identity-bearing helpers:** `account-keys.private.json`, `account-reconciliation.json` and `live-source-inventory.json` were not opened. So the S2 strategy-label identities, the unlisted-candidate identities and the S3 1-of-13 crosswalk match are carried from the cells and RESEARCH.md, not re-derived.
- **Other unread sources:** the SOP and margin PDF receipts (their page counts are carried), and S3's empty-roster refusal branch.
- **Excluded by the README:** the crossreview probe receipt `accounts.crossreview.c2.probes.json`, which S5 and S6 cite.
- **Excluded by K.1 and M-C:** the dry rectangle, the plant patch and the seal.

Signed: 3.0.0_SA_CVO, before seal-open. Push state: LOCAL (ls-remote read 06:44Z, origin/CLOUD = 6a5b276f8b).
