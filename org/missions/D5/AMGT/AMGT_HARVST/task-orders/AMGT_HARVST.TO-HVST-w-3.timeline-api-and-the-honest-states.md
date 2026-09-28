# AMGT_HARVST task order -- `HVST-w-3` -- ROUND 8 cell 2 of 2 ISSUED: the timeline API and its HONEST STATES. FWD-6 is UNREACHABLE today and is deliberately NOT a criterion

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-w-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~24</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the API surface this cell adds; this cell arms nothing and deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- the routes are graded in-process against CONSTRUCTED rows. No AWS call, no vendor call, no live bucket read.
comp-adversary: RUN at L5 -- the adversary here is a FAILED CALL rendering as data. AC2 is written as that adversary's test and is the reason this cell exists in this shape.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO NETWORK. NO S3 WRITE, and no S3 DELETE.** Every criterion runs in-process against
   rows you construct. If you find yourself needing the live bucket, STOP and file a BLOCKING row.
2. **NO GOLD WRITE.** This cell READS the gold shape and serves it; it never builds or writes `chatter_daily`
   or `chatter_event`.
3. **PUT YOUR CHECK SCRIPTS IN**
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~24/scripts/` -- **never `.scratch/`**,
   which does not survive the drain.
4. **READ THE SPEC FIRST, AT HEAD, IN FULL:**
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md`
   (18,196 bytes). It is the contract. **You implement it; you do not re-decide it.**
5. **Your write surface is exactly the `<paths>` below.**

<paths>
lib/research/harvest/timeline_api.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~24/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL -- `HVST-w-3`: the three routes, and the states that must never look alike

**Build the timeline's SERVER SIDE: the three routes of the spec's section 5, and the honest-state discipline
of its sections 2, 3 and 6.** No `.tsx` in this cell (see clause 4 of BOUNDS for why the render half is split).

## 2. WHAT THE SPEC FIXES AND YOU MUST NOT RE-DECIDE

- **Three routes**, exactly these shapes:
  `GET .../security/{security_key}/timeline?from=&to=` -- `series` + `events` in ONE call;
  `GET .../security/{security_key}/timeline/day/{date}`;
  `GET .../security/{security_key}/timeline/event/{first_day}`.
- **`series` carries, READ STRAIGHT FROM `chatter_daily`:** `date`, `mention_score`, `articles_total`,
  `tier_a`, `tier_b`, `tier_c`, `tier_d`, `mention_count_total`, `publishers_distinct`, `trailing_7d_sum`,
  `trailing_30d_sum`, `cumulative_ytd`, `data_status`.
- ⛔ **`breakout_ratio` and `z_score` are COMPUTED AT SERVE TIME AND NEVER STORED** (`C-HV-ABSOLUTE-ONLY`).
  Storing either fails the cell.
- **`events` carries, READ STRAIGHT FROM `chatter_event`:** `first_day`, `last_day`, `days_span`,
  `articles_total`, `tier_a`, `tier_b`, `publishers_distinct`, `lead_article_key`, `lead_headline`. **No
  relative figure on this arm.**
- **Dense from `2026-01-01`, never a gap** -- a day with no coverage is a real zero row.
- **Day/event dissection order:** `signal_tier` (A,B,C,D), then `mention_count` DESC, then `published_utc`
  earliest-first. Each row carries `mention_in_title` and `mention_in_lead` **always present, unmarked when
  false, never omitted**.

⭐ **ONE OF THE SPEC'S OWN OPEN CALLS IS ALREADY ANSWERED BY THE PRODUCER -- USE IT, DO NOT MINT A SECOND ID.**
Section 7 leaves open "whether the build cell mints a stable synthetic `event_id`". **It already exists:
`lib/research/harvest/publication_gold._event_id(security_key, first_day, last_day)` =
`sha256("security_key|first_day|last_day")`.** The event route keys off THAT. A new id scheme here would be a
silent divergence from the producer, invisible in any test that only reads your own output.

## 3. THE ADVERSARY THIS CELL IS REALLY ABOUT -- a failed call rendering as data

The spec states this as its own reason for existing, and it names it as **a real graduated defect on this
page's other panels (`Z-S227`/`C-S400`)**. Get this right and the cell is worth cutting; miss it and the rest
does not matter.

**On ANY failure** (non-200, timeout, or an exception in the route) each of the three routes returns **ONE
shape**: `{"error": true, "error_code": <stable token>, "message": <short reason>}`.

⛔ **THREE THINGS THAT MUST BE IMPOSSIBLE:**
1. An `error: true` body **merged into `series`, `events` or `articles`** as if it were a data row.
2. An `error: true` body **degraded to an EMPTY `series`/`events`/`articles` array.** An empty array is the
   HONEST "the call succeeded and there is nothing in range" state. **A failure must never be reachable to
   that same encoding** -- that is the whole defect.
3. A failure rendering as a **zero-height line or a quiet day.** "We do not know what we hold" and "we hold
   nothing" are different facts.

**And the three day-states must never share an encoding:** quiet-`COMPLETE` (a real zero), `PARTIAL`, `DENIED`.
`DENIED`'s stored height is the count of what retrieval was DENIED for, not what happened.

## 4. BOUNDS

1. **NO `.tsx` IN THIS CELL.** The render half is split off deliberately, and the reason is a measurement, not
   scheduling convenience: see ISSUER NOTE 2. Build the API and its contract tests.
2. **You do not write gold.** If `chatter_daily`/`chatter_event` rows are needed, CONSTRUCT them in the test.
3. **Do not invent thresholds.** `C-HV-MENTION-GRADE`'s weights and `C-HV-EVENT-SPINE`'s thresholds are
   working defaults Andrew resets without a contract change. Serve what they currently produce.
4. **Three mechanical criteria, no fourth.** A fourth finding is a surprise ROW; you keep working.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~24/scripts/ac1_route_shapes.py</invocation><expect>ALL THREE ROUTES SERVE EXACTLY THE SPEC'S FIELD LISTS, over CONSTRUCTED chatter_daily/chatter_event rows. Print per route: the field names served, and the SET DIFFERENCE against the spec's enumerated list in BOTH directions -- missing fields AND extra fields, each with its count, so a superset is as visible as a subset. Print the dense-day denominator (days requested vs days returned, equal, no gap) and prove `breakout_ratio` and `z_score` appear on the `series` arm but are ABSENT from every constructed stored row -- print the stored row's keys to show it. The `events` arm carries NO relative figure: print its field set and show the intersection with {breakout_ratio, z_score} is EMPTY. The event route keys off `publication_gold._event_id` -- print the id it resolves and the same function's output for those arguments and show they are equal</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~24/scripts/ac2_failure_never_reads_as_data.py</invocation><expect>A FAILED CALL IS UNREACHABLE TO THE EMPTY-ARRAY ENCODING, proved by exercising each of the three routes under THREE injected failures (a raised exception inside the route, a timeout, and a malformed/unparseable upstream body) and printing, for each of the nine cases: the returned body, that it carries `error: true` with a NON-EMPTY stable `error_code`, and that it carries NO `series`/`events`/`articles` key at all. Then the CONTRAST that makes it a real test -- a SUCCESSFUL call over an empty range, printing its empty array and `error` absent. A pass requires the two shapes to be DISTINGUISHABLE BY A CONSUMER with no knowledge of the request: print the exact predicate a caller uses to tell them apart. 9 of 9 failure cases and the honest-empty control all present</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/harvest/tests/ -rA -k timeline 2>&amp;1 | tail -40</invocation><expect>the cell's own contract tests pass and are NAMED (`-rA`, never `-q`, because `-q` does not print a passing test's nodeid -- row Z-W21-S1). The suite must include a test that quiet-COMPLETE, PARTIAL and DENIED are served with three DISTINGUISHABLE encodings: print the three served values side by side and the predicate separating them. Also print the WHOLE-SUITE count before and after so this cell's additions are visible against the round-8 baseline `HVST-w-1` establishes, and so a new red test elsewhere is not hidden by a `-k` filter</expect></criterion>
</proof_of_spec>

## 6. WHAT THIS CELL DOES NOT DO, AND THE PART THAT IS NOT SCHEDULING

It builds no `.tsx`. It writes no gold and reads no live bucket. **And it does NOT carry FWD-6 as a criterion
-- see ISSUER NOTE 1, which is the reason and is measured.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. ⛔ **FWD-6 IS UNSATISFIABLE BY CONSTRUCTION TODAY AND ITS CRITERION WOULD HAVE PASSED VACUOUSLY.** Measured
   at the bytes before cutting: `publication_gold.EVENT_MIN_PUBLISHERS = 2`, `EVENT_MIN_ARTICLES = 2`,
   qualifying tiers `('A','B')`. **Only `sa` has landed listing rows** -- bbg in hard refusal since 09-15
   (`Z-S32`), ft/wsj/barrons unexercised in gold. With ONE publisher landed, `publishers_distinct >= 2` is
   structurally unreachable, so **`chatter_event` can hold ZERO rows for every security, Lenovo included.**
   The spec asks a build to "show at least the event runs `chatter_event` holds for Lenovo"; against an empty
   set that criterion PASSES while proving nothing -- and the spec itself blesses the empty render as "the
   correct, honest state." **FWD-6 is therefore named BLOCKED ON A SECOND PUBLISHER, with its cause printed,
   and is not a criterion of this cell.** It becomes gradeable the round a second publisher lands.
2. **FWD-5 is NOT asserted reachable either, and I did not measure it.** It needs a Lenovo day with
   `articles_total > 0` on landed gold. Round 7 measured population B at **1 of 89 securities with a
   non-empty span** and did not name which security that was. **Asserting FWD-5 is reachable without naming
   it would be the same vacuous-pass error as FWD-6, one step quieter**, so the `.tsx` half -- whose
   acceptance IS FWD-5 -- is split off rather than cut against an unmeasured population. The measurement that
   settles it is one read of `chatter_daily` for `992_HK_Equity` after `w-1` lands.
3. **This is the deferral from round 7 paying off.** Decomp 18e deferred `v-3` with the reason "a criterion
   written against an unread surface is the defect this project paid for twice." Reading the spec at HEAD is
   what produced notes 1 and 2 and the `_event_id` catch -- none of which would have survived to a round-9
   post-mortem cheaply.
4. **AC2 is the cell's reason to exist**, not its third criterion. The spec names the failed-call omission as
   a defect that already graduated on sibling panels; a build that gets the field lists right and this wrong
   ships the same defect again.

## 7. THE VERDICT -- `complete`. VALID (rc=0) ON THE INSTRUMENT, RE-RUN AFTER THE DRAIN

**Measured in the main tree at `4f08b0f239`, AFTER the merge, not before it:**

```
proof-of-spec-check | acceptance rows=3 | violations=0
artifact-resolution   0 resolved at pin / 4 PENDING co-committed (touched by instance commit 22f9eb2bfd)
invocation-alignment  3/3 match, 0 diverge
coverage              AC1,AC2,AC3 declared and checked
VALID (rc=0)
```

⚠ **THE POST-DRAIN RE-RUN IS THE POINT, NOT A FORMALITY.** Earlier tonight a commit that touched `HVST-v-2`'s
instance ALONE moved its "instance commit" forward past its own artifacts and turned 11 co-committed rows into
12 CCX-class violations. **A merge does not do that** -- it preserves the worker's commit as the one that
touched the instance, which is why these 4 rows still resolve. That is a measured difference between a merge
and a follow-up commit, and it is why this verdict was read after the drain rather than from the branch.

### WHAT THE CELL DID

| | |
|---|---|
| AC1 | 3 of 3 routes serve exactly the spec's field lists; **0 of 13 combined fields missing and 0 extra** (both directions checked, so a superset was as visible as a subset). `breakout_ratio`/`z_score` served-only, absent from every stored row. `events` carries no relative figure. The event route keys off the EXISTING `publication_gold._event_id` |
| AC2 | **9 of 9 injected-failure cases** carry `error: true` with a non-empty `error_code` and NO data key, and BOTH honest-empty controls (range and day) come back with `error` absent. **A failed call is structurally unable to reach the empty-array encoding**, with the consumer-side predicate printed |
| AC3 | 14 new tests named under `-rA`; whole suite **145 passed** (131 baseline + 14 new) with **no red elsewhere** |
| controls | mutant **FIRED-AS-EXPECTED**, determinism **STABLE** |

### WHAT IT DELIBERATELY DID NOT DO, and both were issuer decisions with reasons

- **FWD-6 was never a criterion.** `EVENT_MIN_PUBLISHERS = 2` with one publisher landed makes `chatter_event`
  empty for every security, so the criterion would have **passed vacuously**. Named BLOCKED ON A SECOND
  PUBLISHER.
- **FWD-5 was not asserted reachable** -- it needs a Lenovo day with `articles_total > 0`, and round 7 measured
  "1 of 89 securities with a non-empty span" without naming which. The `.tsx` half, whose acceptance IS FWD-5,
  is split off rather than cut against an unmeasured population.

**NO ROWS FILED, and that is a reported outcome rather than a silence:** the worker found no off-task surprise,
and the spec's section-7 open calls are explicitly delegated to the build cell, so they are not surprises.

<risk>LOCAL</risk>
<status>complete</status>
<round>8</round>
<slot>~24</slot>
<fabric>site-z</fabric>
