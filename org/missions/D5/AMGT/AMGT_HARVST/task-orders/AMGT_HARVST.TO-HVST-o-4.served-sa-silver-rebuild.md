# AMGT_HARVST task order -- `HVST-o-4` -- ROUND 25 chain 3 of 4, cell 2 of 2: REBUILD THE SERVED sa SILVER UNDER A PAIR -- 5 rows gain `links` / `type` / `meta`, 6 missing articles gain rows (FWD-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-o-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~64</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of sa silver (the collector's Scheduled Task is Disabled, 0 triggers); this act is the one writer for its window.
comp-iam: RUN at L5 -- S3 GET/LIST on the sa bronze and silver prefixes; PUT of new silver parts only, never-overwrite (IfNoneMatch). NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a rebuild that "succeeds" while the readers still serve the old rows (the tie), or one that moves rows outside the pair. AC1 reads the rows back through the merged readers; AC2 compares every moved row to the halves' expected diff.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. `HVST-o-3` is `complete` and merged on CLOUD. The dispatch names its merge.
2. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/NEVER_WIDEN_HALF_COO_O4.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
3. The BEFORE state the halves name reads the same at the start of the act:
   `python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/o-4.signing.py` (no `--signing`)
   prints `BEFORE == signing ... OK` and writes `~64/o4_before.json`. Otherwise STOP and report.
4. `HVST-o-5` is `complete`. Its pair holds the sa root as a no-write control.

## 1. THE ACT

1. Print the BEFORE state.
2. Rebuild sa silver ONCE through the collector's own silver path, from CLOUD code at or after `3886894d16`:
   - the rows are `o4_common.rebuilt_rows()` (in `.../round25/checks/`), which is
     `lib/opal_data_harvest/silver_from_bronze.article_rows` over every stored sa bronze article object with `n-2`'s
     lineage rules;
   - write them with
     `lib/research/harvest/store.silver_append("seeking-alpha", "article", rows, ("article_key",), store.stamp(<now UTC>))`.

   Your act script lives in `~64/scripts/o4_act.py`. No hand-rolled writer, and no other source.
3. Run AC1 and AC2.
4. **Rollback** (named in the halves): forward only. A further rebuild corrects; a delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~64/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-o-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/o-4.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-o-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/o-4.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~64/AMGT_HARVST.TO-HVST-o-4.served-sa-silver-rebuild.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-o-4.served-sa-silver-rebuild`. Report once, with:
- the BEFORE and AFTER parts and ETags;
- the rows written;
- both criteria's output;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **Cut in this issuance; dispatched only after `o-3` drains and both halves are committed.** This is the `n-2` follow-on,
   `ROUND_ANALYSIS.round24.md` s.4 item 4.
2. **`o-4.AC1.py` and `o-4.AC2.py` are issuer-written after `o-3` drains.**
   - Their content is the expected diff read from the merged rule at signing: `n-2`'s AC2 measured 5 moved and 6 new
     (46 -> 52) under the base rule, and it is re-read under `o-3`'s tie-break.
   - They are dry-run at the base, where AC1 FAILS because the rows are not yet served.
   - The files do not exist at this cut, and the dispatch waits for them. This is the same recorded departure as `n-4`.

**AMENDMENT 1 (issuer, 2026-09-30 ~05:0xZ) -- checks written after `o-3` drained (@`592860d126`), dry-run at the base.**
- `o-4.signing.py`, `o-4.AC1.py` and `o-4.AC2.py` each FAIL at the base for the right reason: 0 of 3 parts, 0 of 5 MOVED
  served as rebuilt, a re-run would write 11.
- The COO half is `round25/NEVER_WIDEN_HALF_COO_O4.md`. The expected write is 11 rows (MOVED 5, NEW 6) in 3 parts, and
  keys go from 46 to 52.
- Dispatch also waits on `o-5`'s completion (section 0, item 4). The act's rows come from the issuer's `o4_common`, so the
  write and the check share one rebuild.
- Gate limb: `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>25</round>
<slot>~64</slot>
<fabric>site-z</fabric>
