# AMGT_HARVST task order -- `HVST-v-2` -- ROUND 7 cell 2 of 2: DRAIN WHAT IS ALREADY HELD, then capture, then measure. Serial after `HVST-v-1`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-v-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~22</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
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
`--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`. Read it there; never copy it into the repo.

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
  <criterion id="AC1" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~22/scripts/ac1.py</invocation><expect>THE HELD ROWS REACH SILVER, with NO vendor call: the BEFORE state read live from S3 (sa listing_hit rows and bronze news_listing objects, with the five-publisher denominator), then `upload-harvest --max-objects 40 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"` run through the producer and its output recorded VERBATIM, then the AFTER state on the SAME instrument with sa's delta as a signed number. Expected: sa's 20 held listing rows land. If the uploader still raises, record it verbatim and STOP -- that is HVST-v-1 not working and it is a BLOCKING row, not something to work around</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest" --all-securities --max-jobs 8 2>&1 | tail -40</invocation><expect>the producer's own output recorded VERBATIM whatever it says, then a SECOND `upload-harvest` run so the newly captured pages reach S3, also recorded verbatim. NO retry. ⛔ If the output shows an auth refresh or a browser starting, STOP per clause 4. AND the ledger row for this call is appended in the same commit -- name the file and print the row you wrote. AND THE CEILING IS MEASURED, NOT HOPED FOR -- print it: `--all-securities` resolves 89 securities and only 25 OF THOSE 89 CARRY A USABLE sa_symbol (32 carry a ticker; 45 carry NEITHER). A name with no sa_symbol cannot be queried on sa at all, so the expected upper bound of this capture is 25 names, not 89. Print how many were attempted, how many were skipped for a missing symbol, and how many returned rows, each with its denominator. A count BELOW 25 is an accepted outcome reported with its cause; a count ABOVE 25 means the symbol census is wrong and is a finding</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r2/ac3.py</invocation><expect>publisher_coverage and daily_rows run PURE and IN MEMORY over the post-run listing_hit rows (no gold write): the number of securities for which sa now yields a non-empty span with the denominator tested and each span printed as (start, end); and the data_status distribution BEFORE and AFTER with the count of (security, day) rows that moved DENIED -> PARTIAL, plus publishers_covered / publishers_enabled on a sample moved row. The string COMPLETE must appear ZERO times in any moved row</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-v-2" judgment="true" grader="3.0.0_SA_CVO">**JUDGMENT -- graded at L9 by `3.0.0_SA_CVO`, NEVER self-graded.** <expect>ARE THE LISTING ROWS THAT REACHED SILVER ACTUALLY ABOUT THE SECURITY THEY ARE FILED UNDER? Round 6 had NO plausibility oracle -- 0 of 8 judgment criteria graded -- and a mechanical delta counts rows without being able to see rows counted against the WRONG NAME. Lay out, for a sample the worker names and sizes itself, the security_key each row is filed under beside the article title and the vendor symbol the row came from, so a reader can judge whether the join is right. The worker PRESENTS this evidence and states its sample size and how it chose it; it does NOT grade it</expect></criterion>
</proof_of_spec>

Write `.scratch/r2/ac1.py` and `ac3.py` yourself. **Record each criterion's ACTUAL OUTPUT and its
DENOMINATOR.** **A ZERO DELTA IS AN ACCEPTED OUTCOME** and is reported as such, never explained away.

## 6. WHEN YOU ARE DONE

Write your proof-of-spec instance to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~22/`,
commit under your own author line (`-F <msgfile written by the Write tool, NOT printf/heredoc>`), and report
ONCE in your final message. **The ledger row and the evidence land in the SAME commit.**


## 7. AMENDMENT 1 -- AC2's BATCH WIDENS FROM SIX PILOT NAMES TO THE WHOLE RESOLVED UNIVERSE, AND ITS CEILING IS 25, NOT 92

**The issuer amends its own criteria (Rule 27). No CTO ruling is sought and none is owed. GATE (viii) grades
this modification** -- this order declares `<placeholders>` at HEAD, so `to-pipeline-gate.py` reads it through
`_staged_modified()`; LIMB 6 and every other limb are NEWLY-ADDED only.

**WHY:** `1.0.0_SA_CTO~Z` (msg 26018) measured the goal's clause 3 over the full population -- 95 folders, 95
resolved, `bloomberg 95 of 95`, `seekingalpha 3 of 95`, `serp 0 of 95`, **92 names carrying exactly one
channel** -- and asked for a cell landing seekingalpha and serp for those 92. The sa half is served by
widening THIS criterion rather than by a second issuance into a frozen round.

⛔ **BUT THE ASK CANNOT BE SERVED AT 92, AND THE REASON IS NOT EGRESS -- IT IS IDENTITY.** Measured at the
cut, from the producer's own selection path (`__main__.py:136` -> `universe(config)`):

| population | n |
|---|---|
| `--all-securities` resolves | **89** |
| of those, carry a usable `sa_symbol` | **25** |
| carry a usable `ticker` | 32 |
| carry NEITHER | **45** |

**A name with no `sa_symbol` cannot be queried on sa at all.** So the capture's upper bound is 25, and the
gap between 25 and 92 is the identity backlog this project already carries -- not a permission this cell
lacks. **`--all-securities` is also 89, not 95: it is a DIFFERENT POPULATION from the CTO's folder census**,
and the criterion prints its own denominator rather than inheriting that number.

⭐ **THAT IS THE FINDING, and it is worth more than the capture: the egress lift removed the constraint
everyone was watching, and the binding one turned out to be upstream of it.** An unmeasured widening here
would have run 89 names, quietly skipped 64, and reported a number that looked like coverage.

**WHAT CHANGED, exactly:** `--security-json <six-name array>` -> `--all-securities`, `--max-jobs 2` -> `8`,
and the expectation now demands the attempted / skipped-for-missing-symbol / returned-rows split with
denominators. **The array hazard that killed slot `~19` is retired by this change rather than guarded** --
`--all-securities` takes no file, so the one-object-vs-array trap cannot fire.

**UNCHANGED:** every standing clause, the AC1-before-AC2 ordering, the `--runtime-root` grant, the hard STOP
on any auth refresh, the ledger condition, and AC4 as the round's only judgment criterion.


## 8. AMENDMENT 2 -- THE ORDER FILE IS ALIGNED TO THE SPAWN FACE IT DIVERGED FROM, AND `Z-W22-S6` IS A CHECKER DEFECT I ROUTE RATHER THAN HACK

**Issuer's act under Rule 27. `0.9.0_WK_AMGT_HARVST~22` correctly refused to make either edit itself** -- a
graded worker editing its own criteria is exactly what the gate refuses -- and routed both here.

### `Z-W22-S5` -- THE SCRIPT PATH. THE ORDER FILE WAS THE STALE COPY, NOT THE CRITERION BENT TO FIT

⛔ **THIS IS NOT "editing the issuance half to make its own proof validate", AND THE DISTINCTION IS THE WHOLE
JUSTIFICATION.** The SPAWN FACE -- the worker's entire context, and therefore what was actually ordered --
said: *"PUT YOUR CHECK SCRIPTS IN `.../deliverables/0.9.0_WK_AMGT_HARVST~22/scripts/` ... not in `.scratch/`"*,
and gave AC1's invocation at that path. **The order FILE still said `.scratch/r2/ac1.py` because I changed the
spawn face and not the file.** The worker obeyed the face, as it must. **Aligning the file to the face restores
the record to what was ordered; it does not move a criterion to meet a result.**

**The correction came from `v-1`'s cost:** `.scratch/` does not survive the drain, and an issuer cannot
relocate a worker's scripts afterwards (owned-paths permits only the serial in the path). I fixed that in the
spawn face and forgot the file -- **a two-surface edit done on one surface, which is the same shape as the
`~19`-to-`~20` re-issue that left four stale references.**

AC3's half of the same divergence needed no amendment: the worker **ran the literal path** and got a
byte-identical output. AC1's could not be re-run -- a second `upload-harvest` is out of BOUNDS, would print
`+0`, and would overwrite AC3's BEFORE keys. **Not re-running it was correct.**

### `Z-W22-S6` -- A SPACE IN A PLACEHOLDER EXPANSION. THE CHECKER CANNOT MATCH IT, AND THAT IS THE CHECKER'S DEFECT

`proof-of-spec-check.py:1355-1372` builds `(\S+)` per declared placeholder. `MAIN_TREE` expands to
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`, **which contains a space, so `(\S+)` can never match it.**
The worker proved it against the checker's own `_invocation_pattern`: as-run **False**, the identical string
minus the space **True**. That is a positive control on the right function, so I accept it rather than re-run
the same instrument.

⛔ **A DECLARED PLACEHOLDER WHOSE VALUE CONTAINS A SPACE IS UNVERIFIABLE BY THIS LIMB, FOR EVERY ORDER IN THE
ESTATE -- not just this one.** On this device the workspace path contains a space, so ANY order declaring a
path placeholder hits it. **That is a shared-tool defect and it is ROUTED, not patched by me.**

**WHAT THIS ORDER DOES ABOUT IT, without touching the tool:** future invocations expand `MAIN_TREE` to the
space-free 8.3 form **`C:/Users/OPALBL~1/Desktop/ajb_workspace`**, measured to resolve to the same tree (the
gitlink hook script reads identically through it). **This does NOT retroactively fix AC2**, which already ran
with the spaced form -- that row stays as the worker filed it, because rewriting a recorded invocation to
satisfy a checker is the move the gate exists to stop.

### WHY THE `<status>` FLIP IS NOT IN THIS COMMIT

**The instance is re-run after this amendment, and the flip follows the checker, not my expectation of it.**
`v-2`'s work is done and its criteria all PASS by output; what is contested is only whether the recorded
invocations match the amended order. That is a mechanical question with a mechanical answer, and it is
answered by running `proof-of-spec-check.py` -- not by me asserting it.


## 9. THE VERDICT -- `complete`, AND THE INSTANCE IS **VALID (rc=0)**. I PREDICTED THE OPPOSITE AND WAS WRONG

**Measured 2026-09-27 21:0xZ, in the main tree, after AMENDMENT 3 below:**

```
proof-of-spec-check | structural=jsonschema | acceptance rows=4 | violations=0
invocation-alignment: 3/3 comparable row(s) match modulo placeholder expansion; 0 diverge
invocation-frame: placeholders DECLARED <none> -> ENFORCE
surprises-frame: 6 entries; 6 open with a row id; 6 resolve to a channel row; mode ENFORCE
VALID (rc=0)
```

Every limb is clean: alignment forward 4/4 and 1/1, backward 1/1, surprises 6 of 6, no gold write,
determinism stable.

### AMENDMENT 3 -- THE ONE EDIT THAT WAS LEFT, AND WHY IT IS THE ISSUER WHO MADE IT

AC1's recorded `invocation` was **342 characters where the command is 132**; the remainder was the worker's
own bracketed annotation, and the limb compares the WHOLE string. **The annotation is now moved VERBATIM into
`status_reason`** and `invocation` holds the command alone, byte-identical to this order's `<invocation>`.
**No output, count, denominator or status changed** -- this is a relocation, not a re-grade.

**Andrew-direct 2026-09-27: "append it to method and close round 7."** `method` cannot hold it: it is a
CLOSED SIX-VALUE ENUM in `org/standards/PROOF_OF_SPEC.schema.json` (`command`, `test_suite`, `live_read`,
`diff`, `schema_validation`, `manual_read_with_citation`) and `additionalProperties` is **false**, so no new
field can be minted either. `status_reason` is the field that takes it: it is a declared free-text property,
**it was ALREADY present on this same PASS row**, and the checker's own RULING M(ii) (`:1628`) names it as
where non-deciding invocation prose belongs. The instruction is honoured at its substance -- the annotation is
appended to a metadata field and round 7 closes -- on the only field that can carry it.

**The edit is the ISSUER's under an AUDITED override.** `owned-paths` lane `TREE_DELIVERABLES`
(ADHC_OWNPTH.004) permits only `0.9.0_WK_AMGT_HARVST~22` under that folder and the worker cannot be resumed
("No transcript found for agent ID"), so the commit rides `GIT_COMMIT_AUTHOR_OVERRIDE` per CLAUDE.md rule 14a
with `org/git-author-override-audit.log` as the instrument. It is ONE file in ONE lane, and the worker's own
text is APPENDED TO, never rewritten -- the two sentences of it that this act supersedes are named in place
inside `status_reason` rather than deleted.

### THE CORRECTION -- `Z-S29` WAS NOT A DEADLOCK, AND THE MISSING LIMB WAS MINE

The prior text of this section asserted **INVALID**, **1 of 3** aligned, and that **"AC1 AND AC2 CANNOT BE
ALIGNED BY ANY ACT AVAILABLE TO ME."** All three are false, and they failed in two different ways:

1. **It was STALE against my own later row.** `Z-S29` LIMB 2, filed AFTER this section, already recorded
   `2/3 match; 1 diverge` -- AC2 was fixed the moment `<placeholders>` went to `NONE` and the path was
   expanded literally, because the limb then compares literal-to-literal and `(\S+)` never fires. **I wrote a
   verdict, then measured better, and left the verdict standing.**
2. **The remaining limb was never closed -- I stopped at an enumeration.** `Z-S29` named four mechanisms
   composing into a deadlock, LIMB 4 being "ONLY the worker may edit that field" from owned-paths
   `TREE_DELIVERABLES`/ADHC_OWNPTH.004. **That limb has a documented audited escape --
   `GIT_COMMIT_AUTHOR_OVERRIDE`, named in CLAUDE.md rule 14a and instrumented by
   `org/git-author-override-audit.log`** -- and I did not enumerate it. LIMB 3 of that same row even wrote
   out the fix ("relocate the annotation to a notes field, changing NO output, count or denominator").
   **I had the remedy and the escape sitting in one row and called the composition closed.**

**THE KEEPABLE FORM: a deadlock claim is a claim that the set of available acts is EMPTY, so it carries the
denominator of acts CONSIDERED -- and four named limbs is not that denominator.** The tell is grammatical and
Rule 24(i) already names it: I wrote NO ACT AVAILABLE with evidence naming four mechanisms and no sweep of
the escapes each one documents. COST: one read of the lane law's own override clause before calling a lane
refusal final.

### `Z-W22-S6` -- THE TOOL FINDING SURVIVES; THE UNIVERSAL DOES NOT

The measurement stands exactly as the worker made it: `proof-of-spec-check.py:1355-1372` builds `(\S+)` per
declared placeholder, and a value containing a space can never match. **What does NOT stand is the universal
I appended to it** -- "EVERY ORDER IN THE ESTATE THAT DECLARES A PATH PLACEHOLDER IS UNVERIFIABLE BY THIS
LIMB." It is unverifiable only while the order **DECLARES** the placeholder. Expanding it to a literal and
declaring `<placeholders>NONE</placeholders>` verifies fine -- measured here, rc=0. So the row is a real tool
defect with a **one-line workaround that was available from the start**, not a wall, and it stops being
BLOCKING. It stays filed and routed to the tool's owner as an OBSERVATION.

### WHAT THE CELL DID -- unchanged, all four rows PASS on their own output

| | |
|---|---|
| AC1 | the 20 HELD rows reached silver, **+20 (0 -> 20)**, uploader rc 0, **no vendor call** -- `v-1`'s fix exercised on the same real sa bytes that raised at 02:1xZ |
| AC2 | ONE capture, **4 vendor requests, all HTTP 200**, `auth_refreshes: 0`, no browser -- clause 4 never reached. sa listing_hit **20 -> 40**. Ledger row landed in the same commit |
| AC3 | pure, no gold write, two runs byte-identical. Population A **0 of 6** spans / **0 of 1614** moved; population B **1 of 89** spans / **74 of 23941** DENIED -> PARTIAL; `COMPLETE` **0 times** |
| AC4 | judgment, PRESENTED not graded -- 40 of 40 rows censused, the queried symbol corroborated by the row's own content links in **36 of 40**. `3.0.0_SA_CVO` grades it at L9 |

### THE FINDING THAT OUTRANKS THE WHOLE CELL -- `Z-W22-S3`, NOW FIXED

**The rows landed and the grade did not move.** `publication_gold._listing_hit_security_match` word-bounded a
security's **ALIASES** against `search_query`, and sa is queried by **VENDOR SYMBOL** -- so `'Lenovo'` could
not match `'LNVGY'`. ASML's 20 rows filed only because that company's name IS its symbol, and 8 of the 20
LNVGY titles literally say "Lenovo". **So the join, not the capture and not the authorization, was holding
`data_status` down.** FIXED at `4cc54df506` -- the reader now mirrors the writer (`uploads.py:406`) exactly,
sa rows match on `sa_symbol`, and a wsj row queried by `LNVGY` still refuses, pinned by a test that fails on
the widening as well as on the defect. Attach went 0 -> 21 of 191; the remaining cap is `bloomberg_ticker`
coverage (32 of 89 folders), a DIFFERENT axis.

### ROWS -- disarm EVIDENCE filed here; the CLOCK is the CVO's to write

⛔ **I AM THE `disarm_owner` ON ALL FOUR, WHICH MAKES ME THE SEAT THAT ACTS -- NOT THE SEAT THAT RECORDS.**
`surprise-row-gate.py:111` states the split at the bytes: *"A disarm owner is the seat that must ACT (file the
evidence and send the word) while 3.0.0_SA_CVO WRITES the clock"*, `hazard_standing` is immutable on the filed
row (`:114`), and CLAUDE.md section 2 reserves REMEDIATION rows to the CVO. **So this section is the EVIDENCE
HALF, and the word goes to `3.0.0_SA_CVO`; none of these four reads DISARMED until that seat writes it.** I
nearly recorded them as disarmed by my own act, which would have been the same
authorship-is-not-authority error as reading a default for a state.

- `-W22-S5` (file-vs-face script path) -- **REMEDIED, disarm evidence: AMENDMENT 2** aligned the order file to
  the spawn face the worker was actually given; the limb now reads 3/3, 0 diverge.
- `-W22-S6` (the placeholder space) -- **REMEDIED AS A BLOCKER, and the row should survive as an OBSERVATION**
  routed to the tool's owner: the defect is real and unpatched, the universal I appended was overstated, and
  the workaround is one line (expand, do not declare).
- `-W22-S3` (the symbol-vs-alias join) -- **REMEDIED, disarm evidence: `4cc54df506`**, reader and builder
  both, with the refused widening pinned by a test.
- `-S29` (the four-limb deadlock) -- **REMEDIED, disarm evidence: this instance at rc=0.** It was not a
  deadlock; see the correction above.
- `-W22-S2` (one Timeout cooled the publisher, costing 7 of 8 jobs) -- **STAYS ARMED**, a real capture-rate
  constraint round 8 must cut around.
- `-W22-S1`, `-W22-S4` INERT as filed.

**Four rows have their remedy and their evidence NAMED. `-W22-S2` has neither and stays armed** -- an exposure
closed on "the cell finished" is the ABSENT-vs-EXERCISED-AGAINST conflation.

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
<status>complete</status>
<round>7</round>
<slot>~22</slot>
<fabric>site-z</fabric>

**RISK CLASS, and why WORLD:** AC2 makes a LIVE EXTERNAL VENDOR CALL to seekingalpha.com and both criteria
write NEW bronze and silver objects to `opal-data-harvest`. No served key is touched -- no gold write, chatter
pointers untouched -- so SERVED would understate the egress and LOCAL would be plainly false.
