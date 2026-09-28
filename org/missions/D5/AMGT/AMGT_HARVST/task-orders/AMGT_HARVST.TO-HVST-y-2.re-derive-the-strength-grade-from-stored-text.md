# AMGT_HARVST task order -- `HVST-y-2` -- ROUND 10 cell 2 of 3: re-derive FWD-4's strength grade FROM THE STORED TEXT and match it against what is stored

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-y-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~29</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the read surface; this cell arms nothing, deploys nothing and WRITES nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the gold article_security_mention snapshot and on silver article text. NO PUT. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a HIGH MATCH RATE that hides a systematic tier collapse. AC2 exists to separate agreement from a degenerate distribution.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO S3 WRITE. NO S3 DELETE.** This cell READS and compares. If a criterion seems to need a
   write, it does not -- STOP and file a BLOCKING row.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~29/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~29/AMGT_HARVST.TO-HVST-y-2.re-derive-the-strength-grade-from-stored-text.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-y-2.re-derive-the-strength-grade-from-stored-text`.
4. **Change no producer.** A defect you find is a surprise ROW, not an edit.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~29/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL -- FWD-4, and why FWD-5 and FWD-7 rest on it

**FWD-4 is the strength grade.** FWD-5's "strongest first" ordering and FWD-7's "chatter by strength" both read
`signal_tier`, so **if the stored tier does not describe the stored text, both inherit the error silently.**

**`publication_gold.assign_tier` is PURE and TOTAL** -- evaluated A, then B, then C, then D, first match wins,
over exactly four inputs, and its own docstring says it *"never reads a whole article row"*:

```
A  mention_in_title AND mention_in_lead
B  mention_in_title OR mention_in_lead OR share >= share_b
C  mention_count >= 2
D  otherwise
```

**So the grade is re-derivable.** Recompute the FOUR inputs from the STORED article text in silver, run
`assign_tier` on them, and compare to the STORED `signal_tier` on the gold `article_security_mention` row.

## 2. BOUNDS

1. **Three mechanical criteria, no fourth.** The round's judgment criterion is on `HVST-y-1`, not here.
2. **Re-derive from the STORED TEXT, never from the stored booleans.** Reading `mention_in_title` back and
   feeding it to `assign_tier` proves only that the function is deterministic -- it is a tautology, and it is the
   failure mode this cell exists to avoid.
3. **Use the producer's own weights and `share_b` defaults.** Do not invent a threshold; `C-HV-MENTION-GRADE`'s
   values are Andrew's to reset.
4. **A MISMATCH IS A FINDING, NOT A FAILURE OF THIS CELL.** Report it with its rows named. The cell fails only if
   it cannot measure.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-y-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~29/scripts/ac1_rederive_tier.py</invocation><expect>THE STORED TIER IS MATCHED AGAINST A RE-DERIVATION FROM THE STORED TEXT, with a printed denominator. Print: the number of gold article_security_mention rows examined out of the total in the newest snapshot; how many had their silver article text AVAILABLE (a row whose text cannot be read is UNMEASURABLE and is counted separately, never as a match or a mismatch); then AGREE / DISAGREE counts over the measurable rows, and EVERY disagreeing row named with its article_key, its stored signal_tier, the re-derived tier, and the four inputs that produced the re-derivation. A bare match rate with no disagreement list FAILS this criterion. State plainly which of the four inputs you recomputed from text and which you could not</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-y-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~29/scripts/ac2_distribution_and_totality.py</invocation><expect>AGREEMENT IS SEPARATED FROM A DEGENERATE DISTRIBUTION -- a 100% match on a corpus that is 100% one tier proves nothing. Print the tier distribution of the STORED grades and of the RE-DERIVED grades side by side (counts per A/B/C/D with the denominator), so a collapse to a single tier is visible. Then prove assign_tier's TOTALITY as its docstring claims: enumerate the (mention_in_title, mention_in_lead, mention_count>=2, share>=share_b) truth-table -- 16 combinations -- and show each maps to EXACTLY ONE tier with no combination unmapped and none mapping twice. Print all 16 rows</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-y-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~29/scripts/ac3_score_consistency.py</invocation><expect>THE STORED WEIGHT AND SCORE AGREE WITH THE STORED TIER. For every measurable row, show the weight assign_tier returns for the stored tier equals the weight the row carries (or state that the row carries no weight column, which is itself the finding); and at the DAY grain show that chatter_daily's mention_score equals the tier-weighted sum of its own day's rows, with the denominator of (security, day) pairs checked and every disagreeing pair named. If mention_score is not reproducible from the stored rows, say so with the arithmetic shown for one failing day -- that is FWD-4's answer either way, and a criterion that only reports "consistent" without showing one worked example FAILS</expect></criterion>
</proof_of_spec>

## 4. WHAT THIS CELL DOES NOT DO

It writes nothing, changes no producer, and does not re-grade FWD-5 or FWD-7 -- it establishes the grade those
two rest on. It makes no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Clause 2 of BOUNDS is the cell's real risk.** The tempting implementation reads `mention_in_title` off the
   gold row and feeds it back to `assign_tier` -- which always agrees, because it is the same number twice. **The
   criterion demands the inputs come from the TEXT.**
2. **AC2 exists because a high match rate is not evidence on a degenerate corpus.** Round 7 already measured that
   about half the LNVGY rows are sector pieces, so the tier distribution is the thing to look at beside the rate.
3. **UNMEASURABLE is a third bucket, not a mismatch.** A row whose silver text is unreadable must not be counted
   as either -- that conflation is how a coverage gap becomes a quality claim.
4. **s.14x honoured:** `assign_tier`'s signature, purity and totality claim were read at the bytes at this cut;
   all three invocations name scripts the criterion creates.

## 5. THE VERDICT -- `complete`. VALID (rc=0), and FWD-4's answer is POSITIVE and non-degenerate

**Measured at the merged HEAD after the drain (`0c6699f60d`):** violations 0, invocation-alignment 3/3.
**VALID (rc=0).**

| | |
|---|---|
| AC1 | **263 of 263** newest-snapshot rows examined, **263 measurable, 0 unmeasurable**, **263 AGREE / 0 DISAGREE** between the stored `signal_tier` and a re-derivation from the STORED TEXT |
| AC2 | stored and derived distributions IDENTICAL and **NOT degenerate** -- `A 66 / B 64 / C 45 / D 88` on both sides -- and `assign_tier`'s totality proved over **16 of 16** truth-table combinations, every one mapped exactly once |
| AC3 | row grain 263/263 with 0 mismatches; **day grain 50,997 of 50,997** `(security, day)` pairs consistent, with one worked example shown |

⭐ **THIS IS THE FIRST UNAMBIGUOUSLY POSITIVE MEASUREMENT THIS PIPELINE HAS PRODUCED, AND AC2 IS WHY IT IS
BELIEVABLE.** A 100% match rate is worthless on a single-tier corpus; the four-way distribution rules that out.
**FWD-4's grade does describe the text it claims to** -- so FWD-5's "strongest first" and FWD-7's "chatter by
strength" rest on something real.

### THE ROW IT FILED IS AGAINST MY ORDER, NOT THE CODE

`AMGT_HARVST-Z-W29-S1`: the only committed `securities.json` (`deliverables/~4/`) is **stale at 6 of the 55
`security_key`s the newest gold carries**, and ⛔ **this order named NO ALIAS SOURCE**, so the worker had to
choose one. It used a live `universe_securities.build()` read **and said so** rather than quietly picking. **The
gap is mine: a criterion that needs an identity source must name it.** STAYS ARMED.

<risk>LOCAL</risk>
<status>complete</status>
<round>10</round>
<slot>~29</slot>
<fabric>site-z</fabric>
