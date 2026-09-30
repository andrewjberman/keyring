# AMGT_HARVST task order -- `HVST-p-1` -- ROUND 26 chain 1 of 4: REBUILD THE SERVED `article_security_mention` GOLD UNDER A PAIR -- the rebuilt sa rows and the Lenovo backfill rows gain `mention_count` (FWD-2; inputs to FWD-4 and FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~66</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of harvest gold (the collector task is Disabled, 0 triggers; the chatter producer reads legacy). This act is the one writer for its window.
comp-iam: RUN at L5 -- S3 GET/LIST on harvest silver and gold; ONE PUT of a new article_security_mention snapshot part, never-overwrite. NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a rebuild that writes rows the pair does not name (a builder change since signing), or a count "populated" by a default. AC1 compares the written snapshot row-for-row to the signed expected rows; AC2 reads mention_count on every row and on the named new articles.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P1.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's checks exist in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/`.
3. `p-1.signing.py` (without `--signing`) prints `BEFORE == signing ... OK`. Otherwise STOP and report.

## 1. THE ACT (the command that reaches the put, named per the round-25 ruling 1)

ONCE, from code the halves name:
`python -m lib.research.harvest.publication_gold build-mention --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the UTC date of the act>`

It reaches `build_mention` and then `write_gold`: one never-overwrite put of `article_security_mention/date=<as-of>/part-<stamp>.parquet`.
Then run AC1 and AC2. **Rollback:** forward only, because readers take the newest snapshot. A delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~66/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-p-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-1.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-p-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-1.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~66/AMGT_HARVST.TO-HVST-p-1.mention-rebuild.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-p-1.mention-rebuild`. Report once, with:
- the put key and ETag;
- the rows before and after;
- both criteria's output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- `ROUND_ANALYSIS.round25.md` @`300ea99310` s.4 item 1. It also serves the ANDREW-DIRECT @`8135566a29`: the new articles gain
  `mention_count`.
- **Checks are issuer-written before dispatch, with the signing snapshot (the `o-4` / `o-5` pattern).**
  - `p-1.signing.py` builds the snapshot in memory exactly as `build_mention` does, with a stub put-count client.
  - Its rows ARE the expected diff.
- **Order.** `p-3`'s `chatter_daily` rebuild reads the newest mention snapshot, so `p-3`'s gold step is signed after this
  cell drains.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>26</round>
<slot>~66</slot>
<fabric>site-z</fabric>
