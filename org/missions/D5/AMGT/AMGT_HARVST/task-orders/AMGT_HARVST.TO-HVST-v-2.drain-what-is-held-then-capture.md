# AMGT_HARVST task order -- `HVST-v-2` -- ROUND 7 cell 2 of 2: DRAIN WHAT IS ALREADY HELD, then capture, then measure. Serial after `HVST-v-1`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-v-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~22</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>MAIN_TREE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- the producer needs S3 GET/PUT on opal-data-harvest bronze and silver under the sa subtree. A refusal is a BLOCKING row, never a workaround.
comp-adversary: DECLARED-NOT-APPLICABLE -- a bounded producer run graded on its own output and on live S3 state.
</preflight>

## 0. THE STANDING CLAUSES, first because they are absolute

1. **NO S3 DELETE OF ANY KIND.** A key that lands wrong is a BLOCKING row, never a deletion.
2. **MECHANISM, and it decides your grade before your data does.** Every vendor byte comes from the EXISTING
   scripted producer invoked from the command line. ⛔ **Andrew's egress lift is on the AUTHORIZATION, NOT
   the mechanism. A candidate whose evidence depends on a vendor call made inside an agent turn is a FAIL ON
   MECHANISM EVEN IF THE DATA IS RIGHT.** You do not hand-fetch a URL, you do not paste a payload.
3. ⛔ **THE LEDGER IS A CONDITION OF THE WORD, NOT PAPERWORK.** Andrew-direct 2026-09-26: *"Egress is
   permitted for API calls this session -- no per-use word per vendor call, but every call is ledgered by
   the seat that makes it."* **A seat that cannot ledger its call does not have the word.** You append a row
   for AC2's call to `org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_22.md`
   (create it, same shape as the `2.0.0_SA_COO_Y` file beside it) **in the same commit as the evidence.**
4. ⛔ **YOU DO NOT RE-AUTHENTICATE. EVER.** If the saved session is expired, the producer's own recovery path
   (`worker.py:293`, `AuthExpired` -> `sessions.refresh()`) would launch a HEADED CREDENTIALED CHROME LOGIN
   solving a bot wall with a third-party vision model. **That is a human act, it is outside this cell, and
   the egress lift does not cover it** (entitlements are excluded by name). If you see it start, or if AC2
   fails on auth: STOP, file a BLOCKING row, and report. A zero is an acceptable outcome; a login is not.
5. **`COMPLETE` IS NOT A CRITERION OF THIS CELL.** `data_status COMPLETE` needs all five
   `ENABLED_PUBLISHERS` to cover the day. **`ENABLED_PUBLISHERS` IS NOT NARROWED** -- that is Andrew's call.

## 1. THE CELL -- `HVST-v-2`

**Drain the listing pages ALREADY HELD, then capture a bounded batch, then measure what moved.**

⛔ **THE ORDER OF AC1 AND AC2 IS THE WHOLE DESIGN, and round 6 paid for it.** 20 sa listing rows are ALREADY
on disk in the local outbox, captured at `02:17:52Z` and never written because `Z-S28` blocked the parquet
write. **They need NO vendor call.** Draining them first exercises `HVST-v-1`'s fix against REAL sa bytes --
so if the fix is wrong, this cell learns it BEFORE spending a vendor act rather than after.

**WHAT A LISTING ROW IS FOR:** `publisher_coverage` (`lib/research/harvest/publication_gold.py:485`) builds
each publisher's coverage SPAN from `listing_hit` rows, and `daily_rows` grades `data_status` from those
spans. No listing rows for a publisher means that publisher covers NO day, whatever articles it returned.

## 2. WHERE THIS CAME FROM

Round-6 analysis @`37217d8053`, enrichment item 2. Decomposition section 18 @`97af12ec2b`. **Serial after
`HVST-v-1`:** AC1a fired into a path that cannot reach silver produces an artifact nothing can read.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~22/
org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_22.md
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-v-2.drain-what-is-held-then-capture.md
</paths>

Plus `.scratch/r2/` in your worktree.

**NO `lib/` PATH IS IN YOUR WRITE GRANT.** If the producer needs a fix to run, that is a BLOCKING row and
the cell stops. `HVST-v-1` owns the code.

⛔ **THE RUNTIME ROOT GRANT -- READ THIS BEFORE YOUR FIRST INVOCATION. ROUND 6 DIED HERE.** The producer
resolves its runtime root to the WORKTREE (`publishers.py:22`), and a linked worktree has NO `.runtime` --
so it finds no session vault and falls through to the login in clause 4. **Every producer invocation in this
cell passes the absolute runtime root of the MAIN tree**, given in your spawn prompt as
`--runtime-root "<MAIN_TREE>/.runtime/opal-data-harvest"`. Read it there; never copy it into the repo.

## 4. BOUNDS

- **sa ONLY.** No bbg, no ft, no barrons, no wsj.
- **ONE invocation of the uploader for the held rows (AC1), ONE capture invocation (AC2), ONE uploader
  invocation for what AC2 captured (inside AC2).** No retry loop. If a call fails, that IS the result.
- **NO GOLD WRITE.** You do NOT rebuild `chatter_daily`. AC3 computes the grade change IN MEMORY.
- **Capture batch is bounded to the SIX pilot securities and `--max-jobs 2`.** Not the universe.
- No portal, no Terraform, no deploy, no schedule, no notifier.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~22;`.
- Your FIRST act prints `git rev-parse --abbrev-ref HEAD`, confirms `HVST-v-1`'s fix is present in this
  worktree (name how you confirmed it), and confirms every path in section 3 exists.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r2/ac1.py</invocation><expect>THE HELD ROWS REACH SILVER, with NO vendor call: the BEFORE state read live from S3 (sa listing_hit rows and bronze news_listing objects, with the five-publisher denominator), then `upload-harvest --max-objects 40 --runtime-root "<MAIN_TREE>/.runtime/opal-data-harvest"` run through the producer and its output recorded VERBATIM, then the AFTER state on the SAME instrument with sa's delta as a signed number. Expected: sa's 20 held listing rows land. If the uploader still raises, record it verbatim and STOP -- that is HVST-v-1 not working and it is a BLOCKING row, not something to work around</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --runtime-root "<MAIN_TREE>/.runtime/opal-data-harvest" --security-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --max-jobs 2 2>&1 | tail -25</invocation><expect>the producer's own output recorded VERBATIM whatever it says, then a SECOND `upload-harvest` run so the newly captured pages reach S3, also recorded verbatim. NO retry. ⛔ If the output shows an auth refresh or a browser starting, STOP per clause 4. AND the ledger row for this call is appended in the same commit -- name the file and print the row you wrote. NOTE the securities file named here is an ARRAY of six; if the flag refuses an array (it takes ONE object), that is a cut defect -- file a BLOCKING row and run the single-security file at org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/sa_one_security_992HK.json instead, recording BOTH attempts</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r2/ac3.py</invocation><expect>publisher_coverage and daily_rows run PURE and IN MEMORY over the post-run listing_hit rows (no gold write): the number of securities for which sa now yields a non-empty span with the denominator tested and each span printed as (start, end); and the data_status distribution BEFORE and AFTER with the count of (security, day) rows that moved DENIED -> PARTIAL, plus publishers_covered / publishers_enabled on a sample moved row. The string COMPLETE must appear ZERO times in any moved row</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-v-2" judgment="true" grader="3.0.0_SA_CVO">**JUDGMENT -- graded at L9 by `3.0.0_SA_CVO`, NEVER self-graded.** <expect>ARE THE LISTING ROWS THAT REACHED SILVER ACTUALLY ABOUT THE SECURITY THEY ARE FILED UNDER? Round 6 had NO plausibility oracle -- 0 of 8 judgment criteria graded -- and a mechanical delta counts rows without being able to see rows counted against the WRONG NAME. Lay out, for a sample the worker names and sizes itself, the security_key each row is filed under beside the article title and the vendor symbol the row came from, so a reader can judge whether the join is right. The worker PRESENTS this evidence and states its sample size and how it chose it; it does NOT grade it</expect></criterion>
</proof_of_spec>

Write `.scratch/r2/ac1.py` and `ac3.py` yourself. **Record each criterion's ACTUAL OUTPUT and its
DENOMINATOR.** **A ZERO DELTA IS AN ACCEPTED OUTCOME** and is reported as such, never explained away.

## 6. WHEN YOU ARE DONE

Write your proof-of-spec instance to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~22/`,
commit under your own author line (`-F <msgfile written by the Write tool, NOT printf/heredoc>`), and report
ONCE in your final message. **The ledger row and the evidence land in the SAME commit.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **AC1 before AC2 is the round-6 correction.** The held rows are free evidence that `v-1` works on real sa
   bytes. Spending the vendor act first and discovering the fix is wrong afterwards is the exact ordering
   mistake that made round 6's AC2 structurally `+0`.
2. **AC2 names the array hazard IN the criterion rather than assuming it away.** `--security-json` takes ONE
   OBJECT (`__main__.py:138` wraps it in a list), and the six-name file is an ARRAY -- this is the defect that
   killed slot `~19`. The criterion carries its own fallback and demands BOTH attempts be recorded, so the
   cell cannot silently become a one-security run.
3. **AC4 is the round's ONLY judgment criterion and it exists because L9 was VACUOUS.** It is placed on the
   one thing a green number cannot certify: that the rows are about the right company.
4. **Clause 4 is the hard stop.** The egress lift covers API calls; it excludes entitlements by name, and a
   credentialed browser re-login is not an API call.

<risk>WORLD</risk>
<status>pending</status>
<round>7</round>
<slot>~22</slot>
<fabric>site-z</fabric>

**RISK CLASS, and why WORLD:** AC2 makes a LIVE EXTERNAL VENDOR CALL to seekingalpha.com and both criteria
write NEW bronze and silver objects to `opal-data-harvest`. No served key is touched -- no gold write, chatter
pointers untouched -- so SERVED would understate the egress and LOCAL would be plainly false.
