# AMGT_HARVST task order -- `HVST-au-2` -- ROUND 48 CHAIN B (round-47 analysis ruling 4; row Z-S88; CTO @acc5c6e750): A COVERED NAME'S EMPTY LISTING IS A SOFT BLOCK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-au-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~97</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants with fake clients. NO network, NO S3 call, NO collector run. Never run the backfill driver, `upload-harvest` or the collector for real, and never touch any `.runtime` directory.
comp-adversary: RUN at L5 -- the adversary is a soft_block that counts as concluded, a soft_block that stops the driver, a name never held before reading soft_block, or a no_new_articles job (non-empty listing) reclassified.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/worker.py`, the new-only status block (around lines 658-665):
- A job ends `no_new_articles`. If the client's `job_status` is `listing_empty_200` (a page-1 HTTP 200 with 0 parseable hits), the
  status is rewritten to `listing_empty_200`. That is HVST-al-1, row Z-W91-S20.
- `result["previously_stored"]` (set around line 494, `len(known_ids)`) counts the articles this publisher already held for the
  name before the job.
- Measured on site Z (row Z-S88): barrons `listing_empty_200` rose to 12 of the last 25 jobs, on names Barron's covers (ISRG,
  FIX, EXPD). That reads as a soft block, not an absence.

Elsewhere:
- `lib/research/harvest/publication_gold.py` `SUCCESSFUL_RUN_STATUSES` is an ALLOWLIST of statuses that count as concluded.
- `lib/opal_data_harvest/backfill_driver.py` `STOP_STATUSES` lists the statuses that stop a leg.
- Neither file is in your write set, and neither may change.

## 1. THE BUILD (LOCAL; fake clients only)

1. In `worker.py`, where a job would read `listing_empty_200`: if `result["previously_stored"] > 0`, the status is
   **`soft_block`**; otherwise it stays `listing_empty_200`. Add a comment naming row Z-S88 and the round-47 analysis ruling 4.
2. `soft_block` is NOT in `SUCCESSFUL_RUN_STATUSES` (so it never counts toward the 95% declared-set bar). It is NOT in the driver's
   `STOP_STATUSES` (so the leg keeps its pacing and continues). Both are proven by reading those sets in the plant, not by editing
   them.
3. **Plants** in `lib/opal_data_harvest/test_au2_soft_block.py`, using the worker's existing fake-client test pattern (find it in the
   existing `lib/opal_data_harvest/test_*.py` files that exercise `listing_empty_200`):
   - (i) an empty-200 job with `previously_stored > 0` reads `soft_block`;
   - (ii) the same job with `previously_stored == 0` reads `listing_empty_200`;
   - (iii) a job with a non-empty listing and no new articles still reads `no_new_articles`;
   - (iv) `soft_block` is outside `SUCCESSFUL_RUN_STATUSES` and outside the driver's `STOP_STATUSES`;
   - (v) a mutant that drops the `previously_stored` test makes (ii) fail.
4. The collector suite stays green: `python -m pytest lib/opal_data_harvest -q`. Report the count.

Worktree: given in your spawn prompt (sparse cone, cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_au2_soft_block.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~97/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-au-2"><invocation>python -m pytest lib/opal_data_harvest/test_au2_soft_block.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-au-2"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~97/AMGT_HARVST.TO-HVST-au-2.soft-block-status.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-au-2.soft-block-status`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-47 analysis @acc5c6e750 ruling 4 and enrichment item 2; decomposition section 61. The CTO's pause rule
(29759: pause at a majority of the last 25 barrons jobs) counts `soft_block` together with `listing_empty_200` once this lands.

**COMPLETE 2026-10-06 ~03:3xZ (issuer):**
- **Built:** worker ~97 @5235d0ba0f + @079559d648; merged on the landing branch @b4aa9aa26b. The channel conflict was resolved as a union: Z-W96-S1/S2 + Z-W97-S1.
- **AC1 PASS:** 5 of 5 (issuer re-run identical).
- **AC2:** the worker read 2 failures, both as-1 plants pinned at 191 (the issuer's at-5 defect, repaired @2148adb922). Issuer re-run on the landing branch: collector suite 665 passed, 3 skipped. **PASS.**
- **Row:** Z-W97-S1 (the as-1 pin, repaired).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>48</round>
<slot>~97</slot>
<fabric>site-z</fabric>
