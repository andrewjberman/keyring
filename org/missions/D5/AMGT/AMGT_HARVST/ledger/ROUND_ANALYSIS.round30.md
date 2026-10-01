# AMGT_HARVST -- ROUND 30 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~20:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27354, *"L10 slug AMGT_HARVST round 30 @140726069e"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v40.md` (read to EOF, 5,705 B).
**Bound by:**
- the cloud-collection ruling `CTO_RULING_CLOUD_COLLECTION_DESIGN_20260930.md` s.0 (items 1-4, 3a, 3b; last @`70b0cb4d4f`);
- `4.0.0_SA_CRO~Z`'s bot-ops playbook @`7bcc258369`, on Andrew's word that `2.0.0_SA_COO~H` "goes through the motions".

**Round 30 is CLOSED:**
- 3 of 3 orders complete;
- `Z-W37-S4` and `Z-W84-S3` GRADUATED;
- 0 judgment criteria.

**The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **ac-3:** the paired `chatter_daily` rebuild landed at `part-20260930T181745Z` (52,143 rows). The 5 expected rows carry `bbg`, and
  **the deployed `/timeline` now serves `publishers_found_codes`.** 992_HK 08-13 is found `[bbg, sa, wsj]` and covered `[bbg, wsj]`.
  `C-HV-COVERED-VS-FOUND` works end to end on the served plane.
- **ac-2, the sa probe:**
  - the account read returned 200 `authorized: true`;
  - one live listing returned 20 hits, all dated, 0 pre-floor;
  - 2 requests, 0 sign-ins and 0 refreshes.
  - **Seeking Alpha is active and paid**, as Andrew said. `Z-W37-S4` is graduated. The 09-30 402 was not a lapsed account.
- **ac-1:** the `bot_check` and `unclassified` attempt classes (v0.10-v0.11) are built. The collector suite reads 335 passed and 0
  regressed.

## 2. RULINGS

1. **sa collection runs now, measured-first, as batch 1 of its own.** sa is the one publisher with a measured working REST path on its
   stored token. It is outside the playbook's hard stop (bbg, wsj, barrons).
   - **Batch 1 is 10 of the collector's resolved securities that carry an `sa_symbol`,** with the pre-run page print, under a pair and
     R-21. This follows round-28 ruling 3: Andrew's *"we want to be sensitive about our data quota"*.
   - It paces at 15-25 s and stops at the first `bot_check`, `unclassified` or 402 (v0.11).
   - The measured pages per name re-base the sa ceiling before batch 2.
   - It is also the first job that can make sa a UNIVERSE-scope publisher over batches (v0.8), which is the path to a non-empty declared
     set for FWD-7.
2. **bbg, wsj and barrons follow the playbook, not a cell of this seat's.**
   - The playbook's 05:00 ET first-light test is `2.0.0_SA_COO~H`'s act on Andrew's word, recorded at ruling s.0 item 3b.
   - Its outcome (REST in the tab or page parsing, per publisher) enters the round-31 analysis.
   - No traffic goes to those three from the site Z box before first light.
3. **FT follows the playbook's warm-up + REST lane.** CRO trial 1 measured FT at 200 for 12 minutes after warm-up.
4. **Restated counts at the cut (the CVO's s.3 item 3; the fourth instance in two days).** An order's premise count is re-measured at
   the cut, with the instrument named beside it: "four kept bodies" was 2. This is DISCIPLINE for the issuer's cut, not a gate limb.
5. **`Z-W85-S2`** (sa `check()` hard-codes account `1btfwdu`) joins round-31 cell 1. The check reads `{user_id}` from
   `contracts.json`.

## 3. FWD GRADES

- **2 of 9 REALIZED** (FWD-4 and FWD-8, standing).
- **FWD-3 moved:** covered-vs-found is live on the served route. The "second run fetches nothing held" half stands as round 28.
- **FWD-7** remains bound by reach. sa batch 1 is its first route.
- **FWD-1** needs five publishers' bronze on one run. sa is now proven live; bbg, wsj and barrons wait on first light.
- **FWD-10 is proposed**; its DONE WHEN is Andrew's to confirm.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 31 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **Token store:** wsj and barrons bundles into Secrets; ft's bundle expiry measured; `Z-W85-S2`'s `{user_id}` from `contracts.json` | WORLD (Secrets writes), pair | No publisher traffic. The local file stays until a cloud read of the Secret is proven. |
| 2 | **sa batch 1:** 10 resolved `sa_symbol` names, pre-run page print, stop at first challenge (ruling 1) | WORLD, pair + R-21 | The output is the measured pages per name. The positive arm is shown before the cut: the serializing dry run's put count per name. |
| 3 | **The residential-IP assignability read** (cloud ruling s.0, cell 4) | LOCAL read | This is from the ASTN and BD boxes' configuration, with no vendor call. |

**Fan-out:** 1, 2 and 3 are independent. The warm-up in the harvester (cloud cell 2) waits on the first-light outcome, and it is
round-31 analysis input.

**NOT cells:**
- bbg, wsj and barrons (the playbook's first light is COO~H's own act on Andrew's word);
- batches 2+ (they wait on the measurement);
- the cloud host (phase 2).

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **Confirm FWD-10's DONE WHEN** [Rule 27 L2].
- **Portal PROD promotion** (FWD-5/6) [CLAUDE.md Portal].

## Compiler Tools

- The CVO's v40: the S3 parquet re-read; the deployed `/timeline` invoke; `ac2_probe.json`.
- This seat ran no new instrument for this analysis. The playbook and CRO trials were read, not re-run: the box's IP is under the hard
  stop.
