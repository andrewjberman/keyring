# AMGT_HARVST task order -- `HVST-ab-2` -- ROUND 29 chain 2: REBUILD THE SERVED `article_security_mention` GOLD UNDER A PAIR -- THE 11 bbg STORY-ID ARTICLES GAIN THEIR MENTION PAIRS, AND NOTHING ELSE MOVES (FWD-2, FWD-4, FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ab-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~82</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of harvest gold (the collector task is Disabled, 0 triggers). This act is the one writer for its window.
comp-iam: RUN at L5 -- S3 GET/LIST on harvest silver and gold; ONE PUT of a new article_security_mention snapshot part, never-overwrite. NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a rebuild that moves rows the pair does not name (a builder change since the served snapshot), or pairs on the 11 hash-keyed empty rows. AC1 compares the written snapshot row-for-row to the signed expected rows; AC2 reads the 11 story ids' pairs and the served Lenovo read.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/NEVER_WIDEN_HALF_COO_AB2.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's checks exist in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/checks/`, and the
   act-start gate there prints OK.
3. No other WORLD act of this project is in flight (`HVST-ab-3` does not overlap).

## 1. THE ACT (the command that reaches the put)

ONCE, from the code the halves name:
`python -m lib.research.harvest.publication_gold build-mention --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the UTC date of the act>`

It reaches `build_mention`, then `write_gold`: one never-overwrite put of
`article_security_mention/date=<as-of>/part-<stamp>.parquet`. Then run AC1 and AC2.

**Rollback:** forward only, because readers take the newest snapshot. A delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~82/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ab-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/checks/ab-2.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ab-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/checks/ab-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~82/AMGT_HARVST.TO-HVST-ab-2.mention-rebuild-bbg-eleven.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-ab-2.mention-rebuild-bbg-eleven`. Report once, with:
- the put key and ETag;
- the rows before and after;
- both criteria's output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round28.md` @`c907537920` section 4 item 2, ruling 2.
- **The expected diff** is the new bbg pairs for the 11 story-id articles (`aa-3`, `part-20260930T114206Z`), and nothing
  else. The served snapshot is `062354Z`.
- **The predecessor-code diff is required.** The halves name every commit to `publication_gold` / the mention builder since
  the served snapshot's code, read per file.
- **Checks are issuer-written before dispatch** (the `p-1` pattern).
  - `ab-2.signing.py` builds the snapshot in memory exactly as `build_mention` does, and SERIALIZES it through the real
    `write_gold` against a put-capturing client (the `aa-3` lesson). Its rows are the expected diff.
  - AC1 compares the put row-for-row to the signing rows, and its bytes to the dry run's.
  - AC2 checks three things:
    - each of the 11 story ids has at least one pair with a non-null `mention_count`;
    - the 11 hash-keyed empty rows have 0 pairs;
    - the served company query for 992_HK returns them.
- **NOT in this cell:** the `chatter_daily` rebuild that would read the new snapshot. It rides the next paired daily
  rebuild.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>29</round>
<slot>~82</slot>
<fabric>site-z</fabric>
