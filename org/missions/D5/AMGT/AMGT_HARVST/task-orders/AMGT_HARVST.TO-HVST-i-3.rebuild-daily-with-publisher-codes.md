# AMGT_HARVST task order -- `HVST-i-3` -- ROUND 19 chain 1 of 1, cell 3 of 4: REBUILD `chatter_daily` WITH THE PUBLISHER CODES. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-i-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~46</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the gold write path; no scheduled producer writes the chatter_daily prefix; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the pool universe, silver and the three gold prefixes; ONE PUT on amgt/harvest/gold/chatter_daily. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild whose moved cells exceed the pair (an existing column moving under a schema change), and a put the pre-put read did not see coming (another act moving the newest part or the reader in the same window: round 18 row Z-S41). AC1 is that test; the dry step re-reads the reader's CodeSha256 as well as the ETags.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-i-2` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge named).
2. BOTH never-widen halves are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round19/NEVER_WIDEN_HALF_COO_I3.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** Where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind.** ONE PUT, on `chatter_daily` only. No mention put, no event put. On a failed read-back
   (`HarvestStoreError`), report it verbatim and STOP; the distrusted object stays.
2. **NO VENDOR CALL. NO CODE CHANGE** -- `i-2` changed the rule.
3. **THIS TABLE IS SERVED TO USERS:** the deployed scoped API serves the newest `chatter_daily` part as the `/timeline`
   `series`. The put changes what the timeline reads, although the deployed code does not serve the new column until
   `HVST-i-4`.
4. **Securities input:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`
   (written by `i-1`).
5. **AC1 is write-once.** Make the pre-put arm a SEPARATE dry step that you run FIRST. It must accept no arguments that
   rerun it silently (round 18 row `Z-W45-S4`). It records to an `i3_*` file the three newest keys and ETags, the
   scoped API's CodeSha256, and the halves' values beside each, and it prints STOP on any difference. Never pipe the
   act's output through `head`. Post-act verification is a separate read-only script.
6. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/`; outputs named
   `i3_*` -- **never `.scratch/`.**
7. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/AMGT_HARVST.TO-HVST-i-3.rebuild-daily-with-publisher-codes.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-i-3.rebuild-daily-with-publisher-codes`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `python -m lib.research.harvest.publication_gold build-daily` ONCE, with `--securities-json <the file above>` and
`--as-of <today UTC>`. `write_gold` makes ONE conditional put (`IfNoneMatch="*"`) at
`amgt/harvest/gold/chatter_daily/date=<as-of>/part-<run_stamp>.parquet`.
- **At the cut (7 daily parts):** the newest part is `date=2026-09-29/part-20260929T192649Z.parquet` (51,952 rows).
- Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-i-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/i3_ac1_post_act_verify.py</invocation><expect>THE REBUILD LANDED INSIDE THE PAIR ON THE SERVED PLANE, read after the act from S3: (a) the newest chatter_daily part is the one this cell wrote, with its ETag and row count, and the BEFORE state recorded by the dry step equal to the halves; the newest mention and event parts unchanged (key and ETag); (b) every PRE-EXISTING column equal to the prior newest part on every row, and the new column publishers_covered_codes equal to the pair's expected values -- ANY cell the pair did not name printed as OUTSIDE THE PAIR (a run with one such cell FAILS); (c) every prior daily part still exists with its ETag unchanged</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-i-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/i3_ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: the chatter_daily rows built IN MEMORY from the same inputs equal the SERVED newest daily part ROW BY ROW -- equal keys and every field value including publishers_covered_codes, denominator printed, any difference printed in full</expect></criterion>
</proof_of_spec>

## 4. WHAT THIS CELL DOES NOT DO

No delete, no mention or event put, no code change, no deploy, no vendor call, no portal work.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `i-1`/`i-2` (`~46`), continued.** The pair is written after `i-2` merges, from the merged rule and
   `i-2`'s AC2.
2. **Daily only.** The codes live on `chatter_daily`; mention and event rows do not carry them, and nothing else in the
   rule changes. So one put is the smallest act that serves the change.
3. **The dry step re-reads the reader** because of round 18 row `Z-S41`: RESAPP ww-1 redeployed the scoped API
   between that pair's signing and its puts.
4. **Base:** AC1 FAILS at the base by construction (no new part, no column). AC2 FAILS at the base (the served part
   lacks the column that the in-memory build now carries).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>19</round>
<slot>~46</slot>
<fabric>site-z</fabric>
