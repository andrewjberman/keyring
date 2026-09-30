# AMGT_HARVST task order -- `HVST-n-3` -- ROUND 24 chain 3 of 5, cell 1 of 2: WHY THE SERVED RANK HOLDS 2 ROWS, AND THE `gold` RANK'S EXPECTED DIFF (FWD-7, read-only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~58</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the chatter axis is a SCHEDULED producer (infra/aws/terraform/harvest/chatter-axis-schedule.tf); this cell changes nothing on it. The flip is HVST-n-4's.
comp-iam: RUN at L5 -- S3 GET/LIST, Lambda GetFunctionConfiguration, and a read-only Invoke of the served rankings route only. DynamoDB reads only if the cell's role reaches them; otherwise read through the served route. NO PUT, NO env change, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a "gold" rank computed by a script's own formula instead of the producer's gold branch, or a population explanation guessed from code without reading the served list's actual filter. AC2 runs the producer's own gold branch in memory; AC1 prints the population rule from the code path the served route takes, with the served list beside it.
</preflight>

## 0. THE STANDING CLAUSES

1. **READ-ONLY. NO ENV CHANGE (`CHATTER_AXIS_SOURCE` stays `legacy`), NO S3 WRITE, NO DYNAMODB WRITE, NO VENDOR CALL, NO
   DEPLOY.** The flip is `HVST-n-4` (WORLD), and it depends on this cell's numbers.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~58/scripts/`; outputs named `n3_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~58/AMGT_HARVST.TO-HVST-n-3.served-rank-population-and-gold-diff.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-n-3.served-rank-population-and-gold-diff`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~58/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE QUESTION (`ledger/ROUND_ANALYSIS.round23.md` @`d1ec6f4118`, s.2 ruling 4)

**Measured last round:**
- The served chatter rank is produced by `amgt-resapp-chatter-axis` with `CHATTER_AXIS_SOURCE=legacy`
  (`chatter-axis-schedule.tf:70`; `select_source` in `infra/aws/terraform/harvest/lambda_src/lambda_function.py` ~:102;
  `lib/research/metrics/chatter_axis.compute_chatter_axis` ~:587).
- It is read through `GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}` (`lib/research/api/scoped_amgt.py`
  ~:4322, `read_rankings` ~:644).
- It holds 2 rows (TRENDING x CHATTER: BA and HD, score 0) at as-of 2026-09-29, and BREAKOUT x CHATTER is absent.
- A rank list of 2 cannot show "a company named once in passing ... no longer outranks".

**Measure, and do not change:**
1. Why the served list holds 2 rows. Give the population rule, meaning the window, filters and thresholds on the code
   path the served route takes, with the step where rows drop out and the count at each step.
2. The rank the producer's own `gold` branch computes on the same window and as-of, set beside `legacy`'s. That is the
   expected diff the flip's pair will name.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~58/scripts/n3_ac1_served_population.py</invocation><expect>the served rankings route read (both movements x CHATTER, with the as-of and generation printed), and the population rule on its code path with a step-by-step count from the covered denominator (191) down to the served rows (2 at the last read), each dropping step named by file:line; CHATTER_AXIS_SOURCE printed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-n-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~58/scripts/n3_ac2_legacy_vs_gold.py</invocation><expect>the producer's own compute path run IN MEMORY for source=legacy and source=gold on the same window and as-of (no env change, no write), the two ranked lists printed side by side for every movement x CHATTER with row counts, every company whose rank moves named with old and new rank, and the passing-mention test (named-in-passing companies that outrank subject companies under legacy but not under gold) listed; denominators printed</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No flip, no env change, no write, no deploy, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):** from `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.3 item 3. If AC1 shows the population is
short because of the window or its filter, the grading population is set before `n-4` is signed (ruling 4). `n-4`'s COO
half is written from AC2.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>24</round>
<slot>~58</slot>
<fabric>site-z</fabric>
