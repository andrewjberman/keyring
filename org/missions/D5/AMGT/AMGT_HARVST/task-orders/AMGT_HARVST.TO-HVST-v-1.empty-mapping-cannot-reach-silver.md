# AMGT_HARVST task order -- `HVST-v-1` -- ROUND 7 cell 1 of 2: disarm `Z-S28`, so a listing page carrying an EMPTY MAPPING can reach silver. PUBLISHER-NEUTRAL or it is not the fix

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-v-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~21</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell makes no AWS call and no vendor call. It edits a pure row-builder and runs tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- a source change graded by its own tests, not a produced artifact.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO NETWORK. NO S3 WRITE.** This cell is pure: it changes a row-builder and runs tests
   against payloads already on disk. If you find yourself needing the network, STOP with a BLOCKING row.
2. **NO S3 DELETE OF ANY KIND**, here or anywhere.
3. ⛔ **DO NOT TOUCH `lib/research/harvest/store.py`.** `silver_append` there is the chokepoint EVERY silver
   table in the estate writes through, including pipelines this project does not own. A fix at that depth is
   a blast radius this cell has no sign-off for. **It is not in your write grant and editing it fails the
   cell even if the tests pass.**

## 1. THE CELL -- `HVST-v-1`

**Make a listing row carrying an empty mapping writable, for every publisher.**

**THE DEFECT, already isolated -- you are not being asked to find it (row `AMGT_HARVST-Z-S28`):**
seeking-alpha's listing payload carries `themes` = `{}` on all 20 rows. Arrow types that column `struct<>`,
and parquet refuses it: *"Cannot write struct type 'themes' with no child field to Parquet. Consider adding a
dummy child field."* So sa's captured listing pages cannot reach silver at all.

**IT IS EMPTINESS, NOT STRUCT-NESS, and the isolating pair is already run:** selecting `themes` (`struct<>`)
alone REFUSES; selecting `links` (`struct<self: string>`) alone WRITES FINE. Every column also passes
`pa.array()` individually -- the failure is at the PARQUET WRITE, not at type inference.

⛔ **PUBLISHER-NEUTRAL OR IT IS NOT THE FIX.** Do NOT special-case `themes`, and do NOT special-case sa.
**ft, barrons and bbg have NEVER written a listing_hit row**, so the first time any of them does, an empty
mapping in THEIR payload fails identically -- and invisibly, because the capture returns rc=0 and only the
upload raises. The fix coerces an EMPTY MAPPING to null wherever it appears in a listing row, for any
publisher and any field name.

**WHY NULL AND NOT A DUMMY CHILD FIELD:** an empty mapping carries no information, so null loses nothing and
reads correctly downstream. A dummy child field invents a column name that would then be real, queryable and
wrong. **A POPULATED mapping must still write as a struct, unchanged** -- that is what AC2 measures.

## 2. WHERE THIS CAME FROM

Round-6 analysis `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round6.md` @`37217d8053`,
enrichment item 1: *"Z-S28 disarm -- sa's listing pages reach silver. BLOCKING. Everything below fires into
this path."* Decomposition section 18 @`97af12ec2b`.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_silver_from_bronze.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~21/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-v-1.empty-mapping-cannot-reach-silver.md
</paths>

Plus `.scratch/r1/` in your worktree for check scripts.

**READ-ONLY REFERENCES:**
- `lib/opal_data_harvest/uploads.py` -- `HarvestUploader._run_listings` at `:253-283`, the caller that raised.
- `lib/research/harvest/store.py` -- `silver_append` at `:348`. **READ ONLY. Not yours to change.**
- The held payloads: `.runtime/opal-data-harvest/harvest_listing/` (sa and wsj pages already on disk).

## 4. BOUNDS

- No network, no vendor call, no S3 write, no deploy, no schedule, no notifier.
- Work ONLY in the worktree whose absolute path is in your spawn prompt. Every Bash call begins
  `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~21;`.
- Your FIRST act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and confirms
  every path in section 3 exists. If any is absent, STOP with a BLOCKING row.
- ⚠ **`.runtime/` IS DEVICE-LOCAL AND IS NOT IN YOUR WORKTREE.** Read the held payloads through the ABSOLUTE
  path to the main tree given in your spawn prompt. Do not copy them into the repo and do not commit them.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria, per the build-TO rule

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r1/ac1.py</invocation><expect>THE DEFECT REPRODUCED AND THEN GONE, on the REAL held sa payload, both arms in one output: BEFORE the change, building the listing rows and calling pyarrow's parquet writer raises ArrowNotImplementedError naming a struct with no child field; AFTER the change, the same payload writes and the row count is printed (expected 20). The BEFORE arm must be produced by running the pre-change code path, never by quoting this order</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r1/ac2.py</invocation><expect>THE POSITIVE CONTROL, and it is the criterion that can fail this cell: wsj's held listing payload produces a BYTE-IDENTICAL row set and an IDENTICAL arrow schema before and after the change -- print both schemas and the comparison verdict, plus the row count. AND a populated mapping still writes AS A STRUCT: construct a row whose mapping has at least one key, show its arrow type is struct with that child, and show it writes. A fix that re-types a column wsj already writes is a silver schema change wearing a bug fix's clothes and must be caught here</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/ -q 2>&1 | tail -15</invocation><expect>the opal_data_harvest suite runs and its pass/fail counts are printed as a BOUND -- the number of tests passing, stated with the count, and zero regressions against the pre-change run of the same command (print both numbers). Your new test for the empty-mapping case is part of this suite. ⛔ **THIS CLAUSE ORIGINALLY READ "and is named in the output" AND WAS UNSATISFIABLE AS WRITTEN -- SEE AMENDMENT 1. `pytest -q` names a nodeid only for a FAILING test, so a PASSING new test can never appear.** The substitute oracle is a `-v` run naming the test, recorded beside the `-q` bound</expect></criterion>
</proof_of_spec>

Write `.scratch/r1/ac1.py` and `ac2.py` yourself. **Record each criterion's ACTUAL OUTPUT and its
DENOMINATOR.** No judgment criterion in this cell -- its correctness is mechanically decidable, which is
exactly why `v-2` carries the round's judgment criterion instead.

## 6. WHEN YOU ARE DONE

Write your proof-of-spec instance to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~21/`,
commit under your own author line with `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~21
<0.9.0_WK_AMGT_HARVST~21@opal.agent>" -F <msgfile written by the Write tool, NOT printf/heredoc> -- <paths>`,
and report ONCE in your final message.

**A `.py` edit passes `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39) -- that is universal
and it will run on your commit.

If you find something odd that is off-task, append ONE row to
`org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md` (`class` is
OBSERVATION or BLOCKING -- there is no DEFECT value) and KEEP WORKING.


## 7. AMENDMENT 1 -- AC3's "named in the output" CLAUSE WAS UNSATISFIABLE WHEN I WROTE IT. AC3 PASSES. `Z-W21-S1` IS DISARMED

**The issuer amends its own criteria (Rule 27); GATE (viii) grades this modification.**

`0.9.0_WK_AMGT_HARVST~21` reported AC3 as passing its BOUND while refusing to self-grade one clause, and
routed the call here: *"If the issuer reads that clause as load-bearing, AC3 is a FAIL and the order stays
open on it -- that call is the issuer's at L9, not mine."* **That was exactly right, and the answer is that
the clause was defective at the cut.**

⛔ **`pytest -q` PRINTS A NODEID ONLY FOR A FAILING TEST.** A test that PASSES cannot be named in `-q`
output, ever. So the clause demanded evidence its own named invocation is structurally incapable of
producing -- **my third cut defect of the night, and the same family as the other two: a criterion written
against behaviour I had not exercised.** The worker measured it honestly (0 grep hits in both the tailed and
the untailed stream) instead of quietly substituting a different command and calling it a pass.

**RULING: AC3 PASSES.** Its substance is the BOUND and the regression comparison, and both are met and
printed: pre-change `3 failed, 160 passed`, post-change `3 failed, 161 passed`, **+1 with zero regressions**,
against a collected denominator of 162 the worker re-measured with `--collect-only` after catching its own
error (the summary line's failed+passed overstates the population by 2). **The clause is rewritten rather
than waived, so the next reader of this order is not misled into thinking `-q` can do this.**

⭐ **`AMGT_HARVST-Z-W21-S1` IS DISARMED BY THIS AMENDMENT** -- the hazard was "a criterion demands what its
invocation cannot print", and the criterion no longer does. Disarm owner `2.0.0_SA_COO~Y`, disarmed in the
same turn it was read, per the standing rule.

## 8. `Z-W21-S2` IS NOT MINE TO FIX AND IS NOT DISARMED -- IT IS ROUTED

**The graded suite is ALREADY RED AT HEAD: 3 failures before this cell touched anything.** So AC3's
"zero regressions" is measured against a red baseline, which is the correct comparison for THIS cell and is
still a weaker guarantee than a green one. Worse, the worker measured that **one failure changed its CAUSE
between two runs at the same nodeid** (`KeyError 'bundle'` then `FileExistsError [WinError 183]`) -- a
flapping failure, not a stable one.

⛔ **THAT IS A PRE-EXISTING CONDITION OF `lib/opal_data_harvest`, NOT AN ARTEFACT OF THIS ROUND**, and it is
not in this round's write grant. It stays **ARMED** and is carried into the round-7 analysis. **I am not
disarming a hazard I have not remedied** -- an exposure closed by "nothing went wrong in my cell" is the
ABSENT-vs-EXERCISED-AGAINST conflation.

## 9. DECLARED EXCLUSION, recorded so no one reads this cell as wider than it is

**`article_rows` (the silver `article` table) was deliberately NOT changed.** An empty mapping in an ARTICLE
payload still fails at the same parquet writer. The worker declared it rather than silently widening its own
grant, which is the right call: this cell's domain was the LISTING path. **It is an open exposure on a second
table, not a fixed one**, and it belongs to the round-7 analysis alongside `Z-W21-S2`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The store-level fix was considered and refused.** `silver_append` (`lib/research/harvest/store.py:348`)
   is where a truly universal coercion belongs, and it is the chokepoint every silver table writes through --
   which is precisely why it is out of scope here. That is a never-widen conversation, not a rider on a
   BLOCKING disarm. If the narrow fix proves insufficient, that is a finding for the round-7 analysis.
2. **AC2 is the criterion that matters.** AC1 only shows the bug is gone; AC2 shows nothing else moved. The
   failure mode this cell could plausibly introduce is a silent silver schema change on wsj, which no
   mechanical column downstream would flag.
3. **No judgment criterion here, deliberately** -- correctness is decidable from the two arms. The round's
   judgment criterion sits on `v-2`, which is where a green number can be green over the wrong rows.

<risk>LOCAL</risk>
<status>complete</status>
<round>7</round>
<slot>~21</slot>
<fabric>site-z</fabric>

**RISK CLASS, and why LOCAL:** no vendor call, no network, no S3 write, no served key. The cell edits a pure
row-builder and runs tests. Its blast radius is bounded by the write grant, and the one real hazard -- a
schema change reaching wsj's existing silver rows -- is measured by AC2 rather than by a class.
