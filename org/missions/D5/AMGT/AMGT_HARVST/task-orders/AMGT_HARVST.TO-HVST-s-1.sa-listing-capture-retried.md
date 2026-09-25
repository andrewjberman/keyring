# AMGT_HARVST task order -- `HVST-s-1` -- ROUND 6, the only cell: RETRY sa's listing capture, now that the mid-loop persist defect is fixed. ONE bounded vendor act. PARTIAL-shaped -- `COMPLETE` is NOT a criterion of this cell and must not be written as one

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~20</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- the producer needs S3 GET/PUT on opal-data-harvest bronze and silver under the sa (seeking-alpha) subtree only; a refusal is a BLOCKING row, never a workaround.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

## 0. THE STANDING CLAUSES, first because they are absolute

1. **NO S3 DELETE OF ANY KIND.** Not `delete_object`, not `delete_objects`, not "cleaning up" a bad write. A key
   that lands wrong is a BLOCKING row, never a deletion. A sibling project's worker deleted 123 objects to escape a
   never-overwrite guard; do not recreate those conditions.
2. **MECHANISM (R-21b), and it decides your grade before your data does.** Every vendor byte in this cell comes
   from the EXISTING deterministic scripted producer invoked from the command line. **A candidate whose evidence
   depends on a vendor call made in an agent turn is a FAIL ON MECHANISM EVEN IF THE DATA IS RIGHT.** You do not
   hand-fetch a URL, you do not paste a payload, you do not "just check" an endpoint.
3. **ONE BOUNDED VENDOR ACT.** `--publishers sa` and nothing else. No bbg, no ft, no barrons, no wsj. No retry
   loop around the producer: if it fails, that IS the result, and you record it.
4. **`COMPLETE` IS NOT A CRITERION OF THIS CELL.** `data_status COMPLETE` needs all five `ENABLED_PUBLISHERS` to
   cover the day. sa plus wsj is 2 of 5. If you find yourself writing `COMPLETE` into an expectation, stop -- that
   is a criterion that cannot pass the day it is written.
5. **`ENABLED_PUBLISHERS` IS NOT NARROWED.** Do not remove a publisher to make anything reachable. That is
   Andrew's call and is carded when proposed.

## 1. THE CELL, inlined in full -- `HVST-s-1`

**Retry seeking-alpha's listing capture, and measure what it moves.**

**WHY THIS IS THE CELL, and why it waits on nobody.** Four publishers hold ZERO silver `listing_hit` rows
(barrons, bbg, ft, sa; only wsj has any, at 20) while only THREE refusals were ever recorded. The fourth is sa,
and row `Z-S14`'s own evidence line reads **"upstream_unavailable (HTTP 502 from seekingalpha.com, 24 accepted of
which 3 genuinely new)"**. **A 502 is an OUTAGE, not an access decision** -- the one failure class of the four that
a retry addresses. bbg's verification challenge, ft's 403 and barrons' post-auth rejection are decisions no retry
moves.

**WHY THE ZERO EXISTS AT ALL, which is what makes the retry worth making.** sa's 502 raised MID-LOOP, and at that
vintage `_write_harvest_listings` sat AFTER the per-article loop -- so every listing page already captured for
that job was discarded (row `Z-W15-S1`). That is why sa shows 44 silver ARTICLE rows and 0 `listing_hit` rows.
**The persist now sits in a `finally` WRAPPING the loop** (`lib/opal_data_harvest/worker.py:223`, with row
`Z-S10`'s guard at `:245-261` reading `already_propagating` BEFORE attempting the persist). So a retry today both
gets further AND keeps whatever it captured.

**WHAT A LISTING ROW IS FOR.** `publisher_coverage` (`lib/research/harvest/publication_gold.py:485`) builds each
publisher's coverage SPAN from `listing_hit` rows, and `daily_rows` grades `data_status` from those spans. No
listing rows for a publisher means that publisher covers NO day, whatever articles it returned. That is the whole
causal chain from this cell to the grade.

## 2. WHERE THIS CAME FROM

Round-5 L10 analysis @`4aa2c9d11d` section 6 (`1.0.0_SA_CTO~Z`), as amended @`a6c25f4b18`; decomposition section
17 @`2429ff2f19` with 17f @`05957c2ebb`. Round 4's precondition on any further vendor act is MET AND MEASURED, not
waived: **bronze `news_listing` holds 2 objects, ALL wsj**, so no rebuild from held data exists for the other four.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~20/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-s-1.sa-listing-capture-retried.md
</paths>

**NO `lib/` PATH IS IN YOUR WRITE GRANT.** This cell changes no code. If the producer needs a fix to run, that is
a BLOCKING row and the cell stops.

**READ-ONLY REFERENCES:**
- `lib/opal_data_harvest/__main__.py` -- the CLI and its flags; `--harvest-grammar` is what wires the client.
- `lib/opal_data_harvest/worker.py` -- the persist, now in a `finally` at `:223`.
- `lib/research/harvest/publication_gold.py` -- `publisher_coverage` and `daily_rows`, both PURE.

## 4. BOUNDS

- sa ONLY. **ONE invocation of the CAPTURE (`run`, AC1a) and ONE of the UPLOADER (`upload-harvest`, AC1b).**
  No loop, no second attempt on failure of either. ⛔ **AMENDED BY AMENDMENT 1 (section 7), and the amendment
  is the reason:** this line read "one invocation of the producer", and slot `~19`'s row `Z-W19-S1` correctly
  quoted it as EXCLUDING the upload step -- which is exactly why the original cell could not reach the S3
  surfaces its own criteria measure. The capture and the S3 write are TWO COMMANDS; the bound is one act each,
  not one act total.
- **NO GOLD WRITE.** You do NOT rebuild `chatter_daily`. AC4 computes the grade change IN MEMORY from the pure
  functions. A gold snapshot is a separate act with its own never-widen question.
- No portal, no Terraform, no deploy, no schedule, no notifier.
- Work ONLY in the worktree whose absolute path is in your spawn prompt. Every Bash call begins
  `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~20;`.
- Your FIRST act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that every
  path in section 3 exists. If any is absent, STOP with a BLOCKING row.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/s1/ac0.py</invocation><expect>the BEFORE state read from S3 at run time and NOT copied from this order: silver listing_hit rows per publisher with the five-publisher DENOMINATOR, and bronze news_listing object counts per publisher with their denominator; sa's listing_hit count printed explicitly; plus the deployed persist location confirmed by printing the bytes at worker.py around the `finally`</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-s-1" superseded_by="AC1a+AC1b" status="SUPERSEDED -- DO NOT RUN"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --security-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --max-jobs 2 2>&1 | tail -25</invocation><expect>SUPERSEDED BY AMENDMENT 1 (section 7) -- DO NOT RUN THIS INVOCATION: the securities file it names is an ARRAY and crashes at worker.py:330, and `run` alone writes no S3. Run AC1a THEN AC1b instead. Retained verbatim so the superseded bytes carry their own marker. ORIGINAL TEXT: the producer's own run output, recorded VERBATIM whatever it says -- a success and a failure are both results. If it raises, the traceback is the evidence and AC2 records the zero honestly. NO retry.</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/s1/ac2.py</invocation><expect>the AFTER state on the SAME instrument as AC0, with the DELTA printed per publisher: silver listing_hit rows and bronze news_listing objects. sa's delta stated as a signed number against its AC0 value. A delta of ZERO is a legitimate outcome and is reported as such, never explained away</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/s1/ac3.py</invocation><expect>publisher_coverage run PURE over the post-run listing_hit rows: the number of securities for which sa now yields a non-empty span, with the denominator of securities tested; each span printed as (start, end). If sa yields none, that is the finding and is printed as "sa spans 0 of N"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/s1/ac4.py</invocation><expect>daily_rows run PURE and IN MEMORY (no gold write) over the same inputs: the data_status distribution BEFORE and AFTER, and the count of (security, day) rows that moved DENIED -> PARTIAL, with publishers_covered / publishers_enabled printed on a sample moved row. The string COMPLETE must appear ZERO times in any moved row; if it appears, STOP and file a BLOCKING row</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/s1/ac5.py</invocation><expect>"outside_allowed []" -- no file outside section 3 changed, and NO lib/ file changed at all; plus a delete census proving zero delete calls were made, with a POSITIVE CONTROL showing delete_object and delete_objects RAISE when deliberately tripped</expect></criterion>
</proof_of_spec>

Write `.scratch/s1/ac0.py`, `ac2.py`, `ac3.py`, `ac4.py`, `ac5.py` yourself. **Record each criterion's ACTUAL
OUTPUT and its DENOMINATOR.** No judgment criterion in this cell.

## 7. AMENDMENT 1 -- AC1 IS REPLACED, BY THE ISSUER, BECAUSE THE ORIGINAL COULD NOT HAVE PASSED

**The first attempt (`0.9.0_WK_AMGT_HARVST~19`, row `Z-W19-S1`) executed this order exactly as written and the
cell failed AT THE CUT. No vendor call was made. Both defects are the issuer's, not the worker's**, and they are
recorded in decomposition section 17g:

1. **`--security-json` takes ONE SECURITY OBJECT, and its own `--help` says so.** `__main__.py:138` reads
   `securities = [json.loads(...)]` -- it WRAPS the parsed value in a list. The six-name file is an ARRAY, so the
   wrap produced `[[...]]` and `Worker.run()` raised `TypeError` at `worker.py:330`. ⛔ **THIS IS MISUSE OF A
   DOCUMENTED FLAG, NOT A CODE DEFECT -- do not "fix" `__main__.py`.**
2. ⛔ **`run --harvest-grammar` DOES NOT WRITE S3.** It persists listing pages to a LOCAL sqlite/file outbox
   (`worker.py:91-108`). The bronze/silver listing writes happen only in `HarvestUploader._run_listings`
   (`uploads.py:253-283`), reached ONLY via the separate `upload-harvest` command. The original AC2 measured S3
   surfaces after a command that does not touch them, so its delta was pinned at `+0` before anything ran.

**AC1 IS REPLACED BY AC1a AND AC1b. AC0 and AC3-AC5 are unchanged. AC2 is unchanged in text and now measures
after AC1b rather than after AC1.**

<proof_of_spec_amendment_1>
  <criterion id="AC1a" cell_refs="HVST-s-1" status="NOT_EXERCISED -- UNEXERCISABLE BY ANY SEAT (see AMENDMENT 2, section 8)"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --security-json org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/sa_one_security_992HK.json --max-jobs 1 2>&1 | tail -25</invocation><expect>the producer's own output recorded VERBATIM whatever it says -- success and failure are both results. NO retry. The securities file is a single JSON OBJECT, which is the shape the flag documents</expect></criterion>
  <criterion id="AC1b" cell_refs="HVST-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest upload-harvest --max-objects 40 2>&1 | tail -25</invocation><expect>the uploader's own output recorded VERBATIM. THIS is the command that writes bronze/silver; it is never offline-safe and always builds a real S3 client (row W10-S6). If AC1a captured nothing, this legitimately uploads nothing and says so</expect></criterion>
</proof_of_spec_amendment_1>

**GATE LIMB THAT GRADES THIS MODIFICATION (Andrew-direct card 3, 2026-09-24):** this order declares
`<placeholders>NONE</placeholders>` at HEAD, so **`to-pipeline-gate.py` GATE (viii) -- the `<placeholders>`
declaration -- grades it as a staged MODIFICATION.** No other limb reads a modified order; LIMB 6 and the rest
are NEWLY-ADDED only. No CTO ruling is sought and none is owed.

**Re-issued to slot `~20`.** The `~19` instance stands as filed: its criteria passed on their own terms and its
finding is what produced this amendment.

## 6. WHEN YOU ARE DONE

Write your proof-of-spec instance to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~20/`,
commit under your own author line, and report ONCE in your final message. **If the producer fails, you have still
completed the cell** -- the failure, recorded with its denominator and its before/after delta, is the result the
round asked for. Do not retry, do not widen, do not fix code to make it pass.


## 8. AMENDMENT 2 -- AC1a IS RECORDED `NOT_EXERCISED` AND THE CELL IS TERMINAL AT `closed`, NOT `complete`

**AC1a was never run, by either slot, and it cannot be run by any seat.** It is therefore recorded as
UNEXERCISABLE with its precise reason, and this order goes terminal. **The authority is the issuer's own:
Rule 27 -- the issuer amends its own task-order criteria without a CTO ruling (Andrew-direct 2026-09-24).**
`1.0.0_SA_CTO~Z` confirmed the split rather than granting it (msg 25933): the criterion is mine, the ENDPOINT
consequence -- whether FWD-1's sa limb reads NOT REALIZED with a named cause -- is the CTO's, written in the
round-6 analysis.

**THE REASON, stated once and precisely.** AC1a's invocation does not perform "one bounded vendor act". Reaching
the fetch requires a session envelope; a worker worktree has none; and the producer's own recovery path escalates
to a **headed, credentialed Chrome login against seekingalpha.com whose bot wall is solved by a third-party
vision model**. That is a HUMAN act with its own authorization, not a scripted producer call:
- `worker.py:152` `self.sessions.get(publisher)` -> `auth.py:23-24` `saved or self.refresh(publisher)` ->
  `auth.py:86-89` -> the login script. This is the STARTUP branch.
- `SessionVault.load` (`storage.py:51-55`) tests `path.exists()` with **no expiry check**, so pointing
  `--runtime-root` at the main tree disarms that startup branch -- **and only that one.**
- `worker.py:293` calls `self.sessions.refresh(publisher)` on `AuthExpired` **on the first attempt, for ANY
  publisher.** Its sibling at `:275` (`VerificationRequired`) IS guarded to bbg/barrons; this one is not. So a
  ten-day-old session does not fail closed -- **it fails INTO the login.**
- No switch disables it: a census over `lib/opal_data_harvest/` for a no-refresh control returns **4 hits of 43
  files, every one a `credentials_entered` telemetry field.**
- And the only non-vendor alternative is measured absent: `harvest_listing_outbox` holds **2 rows, both wsj,
  both uploaded, sa ZERO** (beside `harvest_raw_outbox` sa 3 / wsj 11) -- sa's ARTICLES persisted, its LISTINGS
  did not. Only a FRESH capture can produce an sa listing row.

⛔ **WHY TERMINAL RATHER THAN HELD, which is the part worth keeping:** a criterion that no seat can exercise is
named UNEXERCISABLE; it does not sit holding a round open. Held, this ONE criterion blocks round 6, which blocks
round 7's decomposition, which blocks two cells (the timeline BUILD and the ft/barrons diagnostic) that need no
Andrew word at all -- **a whole project stalled on a login.** That is the shape Rule 27's L2 already forbids
("NO FWD IS A WAIT"), arriving one level down as a criterion instead of an outcome.

⭐ **AND IT CARDS RATHER THAN HOLDS, WHICH ARE NOT THE SAME THING.** The sa re-login **remains an open card at
Andrew and is not decided here.** Making the cell terminal decides only that NOTHING WAITS ON IT -- which is the
entire point of carding. If he authorizes the login, sa's retry returns as a cell of a later round with the human
act named in it; if he does not, sa is recorded tried-and-blocked with its cause. **Both branches stay open; only
the stall is closed.**

**STATUS IS `closed`, DELIBERATELY NOT `complete`.** Both are terminal to the gate
(`surprise-row-gate.py:152` `TERMINAL_TO_WORDS`), but `complete` would assert this cell reached its endpoint and
it did not: sa still holds **0 listing_hit rows**, AC2's delta is **+0**, AC3 reads **sa spans 0 of 6**, and AC4
moved **0 of 1608** rows DENIED -> PARTIAL. `closed` says terminal without claiming an achievement, and that
distinction is exactly what the round-6 analysis has to grade.

**WHAT STANDS UNCHANGED:** slot `~20`'s instance is VALID and is NOT rewritten -- AC1a stays **FAIL** in the
worker's own proof-of-spec, because that is what the worker honestly measured and an issuer does not edit a
worker's grades. This amendment records the ISSUER's disposition of the criterion, beside the worker's record of
its attempt. AC0, AC1b, AC2, AC3, AC4 and AC5 all PASS with their denominators. Row `AMGT_HARVST-Z-W20-S1`
remains BLOCKING/ARMED and is the CVO's to disposition at L9 -- a worker's row cannot be graduated by this seat
(`surprise-row-gate.py:115-116`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **`--max-jobs 2` and the six-name securities file are deliberate.** The cell needs to prove the persist keeps
   pages, not to backfill the universe. A small bounded run makes a 502 recoverable information rather than a
   spent grant, which is what round 4's analysis warned about.
2. **AC4 is IN MEMORY on purpose.** Observing the grade move does not require writing gold, and a gold write is a
   served-output question this cell has no sign-off for. The pure functions make the observation free.
3. **A zero delta is an ACCEPTED outcome and the order says so twice.** If sa 502s again, the cell has still
   measured that the retry class does not move it, which converts sa from "untried" to "tried and recorded" -- and
   that is a different and more useful state than the one round 6 started in.
4. **No `lib/` write grant.** The temptation on a failing producer is to fix it in the same breath; that would be
   a second cell inside this one and would put a code change on a path this cell cannot grade.

<risk>WORLD</risk>
<status>closed</status>
<round>6</round>
<slot>~20</slot>
<fabric>site-z</fabric>

**RISK CLASS, and why WORLD rather than LOCAL:** this cell makes a LIVE EXTERNAL VENDOR CALL to
seekingalpha.com and writes NEW bronze and silver objects to `opal-data-harvest`. Nothing it does touches
a SERVED key -- there is no gold write and the chatter pointers are untouched -- so SERVED would understate
the egress and LOCAL would be plainly false. The act reaches outside Opal infrastructure, which is the
line the autonomy rule draws, so it is graded at the class that engages every limb.
