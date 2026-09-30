# AMGT_HARVST task order -- `HVST-aa-3` -- ROUND 28 chain 3: REBUILD THE SERVED bbg SILVER `article` TABLE ON `q-2`'s PARSE, UNDER A PAIR THAT NAMES THE 11 HASH-KEYED EMPTY ROWS (FWD-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aa-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~78</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of bbg silver; this act is the one writer for its window.
comp-iam: RUN at L5 -- S3 GET/LIST on bbg bronze and silver; PUT of new bbg silver parts only, never-overwrite. NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a rebuild that "succeeds" while the empty rows are still what a reader serves. AC2 reads each of the 11 articles through the served readers, by story id, non-empty, and names what the 11 hash-keyed rows do.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/NEVER_WIDEN_HALF_COO_AA3.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.** The halves name the 11 hash-keyed rows' fate.
2. The issuer's checks exist in `.../round28/checks/`, and the act-start gate prints OK.
3. `HVST-aa-2`'s act is not in flight: the two acts do not overlap.

## 1. THE ACT

Rebuild bbg silver ONCE through the collector's own silver path, from CLOUD code carrying `q-2`'s parse:
`silver_from_bronze.article_rows` over every held bbg bronze article object, then `store.silver_append("bloomberg", "article",
rows, ("article_key",), store.stamp(<now UTC>))`.

The exact rows are the issuer's `aa3_common.rebuilt_rows()`, on the `o-4` pattern. Then run AC1 and AC2. Rollback is forward
only; a delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~78/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aa-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/checks/aa-3.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-aa-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/checks/aa-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round27.md` s.4 item 3, ruling 4.
- **The 11 rows' fate is carded to the CTO (issuer msg ~09:43Z).** `silver_latest` groups by `article_key`, so the tie-break
  cannot supersede rows keyed `bbg:<hash>` with rows keyed `bbg:<story id>`.
- **REC:** keep them, and have the AC prove them inert (0 mention pairs, in no served list); or the CTO rules a reader-side
  exclusion.
- The checks and halves are issuer-written on that ruling.

**AMENDMENT 1 (issuer, 2026-09-30 ~10:2xZ) -- the 11 rows ruled (@`803ea38a9e`, msg 27079); checks and COO half written.**
- **The ruling:** KEEP the 11 hash-keyed empty rows (no delete, no reader filter) and prove them inert. Any empty row reachable
  from a served list is a STOP.
- **COO half:** `round28/NEVER_WIDEN_HALF_COO_AA3.md`. The expected write is 11 NEW rows (`bbg:<story id>`) in 1 part, and keys go
  from 30 to 41.
- **Checks:** `aa-3.signing.py`, `aa-3.AC1.py` and `aa-3.AC2.py` FAIL at the base for the right reasons. The inert reads already
  hold at the base: 0 mention pairs on an empty row, and 32 of 32 bbg pairs are backed.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~78</slot>
<fabric>site-z</fabric>
