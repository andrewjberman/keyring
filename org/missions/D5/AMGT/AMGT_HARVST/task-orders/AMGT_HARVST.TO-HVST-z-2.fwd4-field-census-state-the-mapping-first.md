# AMGT_HARVST task order -- `HVST-z-2` -- ROUND 11 cell 2 of 4: FWD-4's FIELD clause. STATE THE MAPPING BEFORE COUNTING ANYTHING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-z-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~33</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates; this cell reads and counts, writes nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention gold snapshot. NO PUT. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a census that reports a GAP it does not have, or invents a column mapping to make a ratified clause pass. AC1 is written so neither is possible.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO S3 WRITE OR DELETE.** This cell reads and counts.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~33/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~33/AMGT_HARVST.TO-HVST-z-2.fwd4-field-census-state-the-mapping-first.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-z-2.fwd4-field-census-state-the-mapping-first`.
4. **Change no producer and no schema.** A defect is a surprise ROW.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~33/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL -- FWD-4's FIRST clause, which `HVST-y-2` never exercised

FWD-4's DONE WHEN has **two** clauses. `y-2` exercised the second superbly (the grade re-derived from stored text
and matching, 263 of 263, non-degenerate). ⛔ **The FIRST was never measured**, and this cell closes it.

**READ FWD-4's DONE WHEN IN THE PRD YOURSELF, at the bytes** (`prd/AMGT_HARVST_PRD.md`), before anything else.
⚠ **DO NOT work from a summary of it, including this order's.** The issuer compared the schema against the round-10
analysis's SHORTHAND for this clause rather than the clause, and manufactured a fork that did not exist
(decomp `s.23.6`). **The ratified text reads:** *"whether the company is IN the headline, IN the opening, how often
it is named, how much of the article names it, which other covered companies it names, and a strength grade"*.

⭐ **"In the headline" and "in the opening" are WHETHER facts, not text.** That is the distinction the issuer got
wrong, and it is why AC1 exists.

## 2. AC1 COMES FIRST AND MAY CHANGE WHAT AC2 COUNTS

**For each of the SIX ratified facts, name the column that carries it -- or state it is ABSENT and say where the
fact actually lives.** `1.0.0_SA_CTO~Z`'s mapping (20260928T121201Z), to be VERIFIED at the bytes, not assumed:

| ratified fact | expected column |
|---|---|
| in the headline | `mention_in_title` |
| in the opening | `mention_in_lead` |
| how often named | `mention_count` |
| how much of the article | `blocks_hit` / `blocks_total` |
| other covered companies | `co_mentioned_securities` |
| a strength grade | `signal_tier` |

⛔ **AND ONE ABSENCE IS THE CONTRACT WORKING, NOT A GAP:** there is **no `share` column and there must not be** --
`C-HV-ABSOLUTE-ONLY` BARS a ratio from gold, so share is computed at serve time from `blocks_hit`/`blocks_total`.
**Reporting it as a missing field would be wrong.** If you find any OTHER fact unmapped, say so plainly -- that is
a real finding, not a failure.

## 3. BOUNDS

1. **Two mechanical criteria, no fourth and no judgment** -- the round's judgment criterion is on `HVST-z-1`.
2. **Non-null is the test, not "plausible".** A column present but null on a row does not carry the fact.
3. **A list column carries the fact when it is PRESENT, including when EMPTY** -- an article naming no other covered
   company has an honest empty `co_mentioned_securities`. ⛔ **Do not count an empty list as a missing field**; that
   would turn a true negative into a gap.
4. **Report UNMEASURABLE rows as a third bucket**, never as carried and never as missing.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-z-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~33/scripts/ac1_state_the_mapping.py</invocation><expect>THE MAPPING, STATED BEFORE ANYTHING IS COUNTED, and verified at the bytes. Print FWD-4's DONE WHEN clause (i) VERBATIM as the PRD carries it, then one line per ratified fact naming the GOLD_MENTION_SCHEMA column that carries it -- read from the schema object itself, not from this order's table -- or naming it ABSENT with where the fact actually lives. Print the schema's full field list beside it with its count, so a reader can check the mapping rather than trust it. Then state in one line whether clause (i) is CLOSABLE by a census of this table: yes with the column set named, or no with the unmapped facts named. ⛔ `share` is EXPECTED ABSENT by C-HV-ABSOLUTE-ONLY and must be reported as contract-compliant, NOT as a gap -- a census calling it missing FAILS this criterion</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-z-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~33/scripts/ac2_census_non_null.py</invocation><expect>EVERY ROW OF THE NEWEST SNAPSHOT CARRIES EVERY MAPPED FACT, with denominators. Over AC1's mapped column set, print: the row count of the newest article_security_mention snapshot; per column, how many rows carry it NON-NULL out of that denominator; and EVERY row that is missing any mapped fact, named by article_key and security_key with the missing column. A list column counts as carried when PRESENT even if EMPTY -- print the empty-vs-null split per list column so the distinction is visible rather than assumed. Report UNMEASURABLE rows separately. State the verdict as "clause (i) MET over N of N rows" or "NOT MET, with the M failing rows named" -- and if M is 0, say so with N printed, because a bare "met" without its denominator is not a measurement</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

It writes nothing, changes no schema or producer, and does not re-exercise clause (ii) -- `y-2` did that. It does
not grade FWD-4; it measures the clause the grade needs.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. ⛔ **AC1 EXISTS BECAUSE I MADE THE MISTAKE IT PREVENTS.** I compared the schema to the analysis's paraphrase and
   reported three facts missing; the CTO's read of the ratified text dissolved it. **A criterion that states its
   mapping before counting is correct whether the mapping holds or not**, which is why the cut survived my being
   wrong about the cause.
2. **BOUNDS 3 is the subtle one.** An empty `co_mentioned_securities` is an honest "no other covered company", and
   counting it as a missing field would manufacture a gap -- the same error shape as reporting `share` absent.
3. **The worker is told to read the PRD itself and NOT to trust this order's summary.** That is the only instruction
   that would have saved me.

<risk>LOCAL</risk>
<status>pending</status>
<round>11</round>
<slot>~33</slot>
<fabric>site-z</fabric>
