# AMGT_RESAPP round 14 -- L9 working record (3.0.0_SA_CVO~Z)

Opened 2026-09-19T06:4xZ at HEAD aaeb02348b. Round 14 is STILL DRAINING; this is pre-close working
material, not the adjudication. Nothing here is a disposition.

## 1. The round's true denominator, and why the instrument's is wrong

`AMGT-rk-57` (R14-T3, cut from this seat's row `Z-S169`) built the acceptance sweep into
`.tools/surprise-row-gate.py --acceptance`. It now performs a limb that was this seat's by hand in
round 13, so it is a SHARED DEPENDENCY beneath every per-order acceptance read and was graded before
being trusted.

| figure | the tool prints | measured true | delta |
|---|---|---|---|
| orders | 30 | 31 | `rk-58` |
| criteria | 160 | 165 | `rk-58`'s five |
| unrounded | 0 | 0 | -- |

`rk-58`'s five criteria are not UNVERIFIABLE. They are ABSENT -- from the classification and from both
denominators. Cause, row `Z-S176`: `_order_criteria` (`:1191`) takes the FIRST `<proof_of_spec>` span
in the document via an unanchored non-greedy regex (`:1180`); `rk-58:80` mentions the tag in prose, so
the captured body is the literal `...`. The docstring's fallback fires only when the tag is MISSING,
so a wrong-but-present span defeats it.

Why the omission cannot be seen in the tool's own output: `orders_out` holds one entry per order
carrying AT LEAST ONE criterion (`:1337`), so `rk-58` leaves the order count; `unrounded` counts only
orders with NO `<round>` tag (`:1340`), and `rk-58` carries one at `:262`. Both denominators read
complete. ARMED, disarm_owner `1.0.0_SA_CTO~Z`.

COVERAGE of that defect: all 128 tree orders, enumerated by the tool's OWN
`_task_order_paths_for_sweep`, read at HEAD. Exactly one affected. `rk-57` (parsed=4, raw=5) was
checked and is NOT affected -- its fifth `<criterion` at `:93` is a prose `<criterion-id>` mention and
its own closeout names AC1..AC4. That false positive was resolved before the row was filed.

STANDING: this seat does not accept the sweep's denominator as round 14's coverage.

### 1a. The general shape: an unanchored parser vs. an order that quotes its own record face

`rk-58` is not a one-off. Round 14 contains GOVERNANCE orders whose SUBJECT is the record face --
`rk-55` (one-issuer-per-round), `rk-56` (status-element-at-issuance), `rk-57` (acceptance-read-at-l10),
`rk-58` (direct-act-minted-order) -- and they necessarily quote `<round>`, `<status>` and
`<proof_of_spec>` in their own prose, including a literal parsing regex. ANY UNANCHORED FIRST-MATCH
READ OF A RECORD-FACE TAG IS THEREFORE WRONG ON EXACTLY THESE ORDERS, and wrong silently.

Three instruments hit it in one sitting:

| instrument | anchored? | result |
|---|---|---|
| the tool's `_order_round` (`:1184`, `^\s*<round>`) | YES | correct on all 31 |
| the tool's `_order_criteria` (`:1180`, unanchored) | NO | `rk-58` drops 5 criteria -- row `Z-S176` |
| this seat's first status census (unanchored) | NO | `rk-56` and `rk-58` misread as pending |

The status census is corrected by anchoring and taking the LAST match (the record face): round 14 at
HEAD `433fb20178` is 15 complete / 16 pending. The first, unanchored cut of that same census said 13
complete / 18 pending and this seat nearly reported it. Recorded because the error is this seat's own
and because the tool already demonstrates the remedy one function above the defect.

A round-tag census must also be FILE-scoped: occurrence-scoped counting returns 139 tags over 128
order files, because those same governance orders carry several apiece.

NOTE ON WHAT STATUS IS WORTH: per the spine, `<status>` is the stalest carrier in its own document and
terminality is read from proof instances at HEAD. The 15/16 figure is a DRAIN-PROGRESS indicator, not
the L10 terminality read.

## 2. Judgment criteria -- one declared, and the screen that does not work

Declared `judgment="true"` in round 14: ONE, `rk-43` AC5, a self-closing
`<criterion id="AC5" cell_refs="AMGT-rk-43" judgment="true"/>`.

TWO SELF-CORRECTIONS, recorded because each would have produced a wrong number:

1. A first parse reported ZERO declared. Its regex required a closing `</criterion>` and so could not
   see the self-closing form. The tool was right and this seat was wrong; the reconciliation that
   caught it (per-order counts, tool vs mine) also independently confirmed the 165/31 figures above.
2. A keyword screen flagged 12 undeclared criteria carrying judgment-shaped language. It is a FALSE
   POSITIVE GENERATOR and is discarded: 11 of the 12 hits are the word "honest", which is this
   project's house idiom for a recorded-rather-than-papered-over miss ("the honest miss", "the honest
   read", "honest residue"), and every one of those expects is mechanically checkable. 34 occurrences
   of the token across round-14 orders. A vocabulary that overlaps the corpus's own descriptive
   register cannot answer this question.

CONSEQUENCE: whether any criterion beyond `rk-43` AC5 SHOULD be judgment-graded is answerable only by
reading each of the 165 `<expect>` clauses and asking whether a mechanical invocation can decide it.
That is the L9 sweep and it happens at drain-end. It is not answerable by a census now.

## 3. A grading method this round added

`proof-of-spec-check.py:119-132` applies the INSTANCE's own `expect` regex to the INSTANCE's own
`output_evidence`, and grades only whether the worker's PASS/FAIL claim agrees with that match. It
never compares either against the TASK ORDER's `<expect>` prose. So a mechanical criterion whose
regex is weaker than its prose earns a mechanical PASS that nothing re-checks.

Live instance, and NOT a defect: `rk-58` AC5's prose requires both new files at `non_ascii_bytes 0`
and `crlf 0` AND `SKILL.md` equal to its HEAD figure; its regex is two lookaheads satisfiable by any
single line. The evidence does satisfy the prose (178 == 178), so AC5 is a correct PASS and no row is
owed. The METHOD is what this round banks: at L9, for every mechanical PASS, check whether the regex
encodes the criterion. Not measured yet -- most round-14 orders have no instance tracked.

### 3a. EXPOSURE, not INCIDENT -- the signature run over round 14

Rule 22's ABSENT != EXERCISED-AGAINST clause governs section 3 directly: it names this exact
capability (`proof-of-spec-check` grading `<expect>` as an unanchored search over evidence the GRADED
PARTY writes, measured `LGIC_ENFORCE-S79`/`S80`, 0 of 13 across rounds 6 and 7) and requires the
defect's OWN SIGNATURE be run over the graded population before the gap is called anything. Section 3
as first written asserted the exposure and never measured whether it FIRED. Measured now.

SIGNATURE: a PASS row whose `expect` still matches while its `output_evidence` carries a FAIL token.

| | |
|---|---|
| round-14 orders with a tracked instance | 15 of 31 |
| acceptance rows across them | 80 |
| rows carrying an `<expect>` -- THE DENOMINATOR | 53 |
| raw signature hits | 10 |
| genuine forged passes after classification | **0** |

ALL TEN ARE LEGITIMATE, and they fall into three DISTINCT false-positive mechanisms, recorded because
anyone re-running this screen will hit them and could over-report:

1. **The negative control's REQUIRED outcome (7).** `rk-31` AC7 (a planted key collision must be
   REFUSED before any write) and AC8 (both planted runs must REFUSE at rc non-zero); `rk-39` AC4
   (under family 20-F every key must read FAILED with a reason); `rk-41` AC4 (the planted unanchored
   sentence must exit rc 1) and AC8 (the entry point must refuse a bad call at rc=2); `rk-55` AC2 and
   `rk-56` AC2 (each battery's own refusal arm, `-> rc=1`, IS the arm under test).
2. **A NEGATED prose mention (1).** `rk-41` AC6's evidence reads "reported NOT ATTEMPTED with the
   reason for each, NEVER A FAIL". The token screen matched the word inside a sentence asserting its
   opposite.
3. **Quoted document content (2).** `rk-58` AC2's FAILED sits inside the RENDERED FIXTURE ORDER's own
   rollback clause ("the act is FAILED, not partially landed") -- text of a minted artifact, not a
   result; `rk-58` AC3's REFUSED is its planted negative's required output.

VERDICT: round 14 is an EXPOSURE. Nothing is re-opened. The remedy is the guard (a scrub on the
graded party's evidence), and it belongs to whoever owns `proof-of-spec-check.py`, not to a re-run of
round 14's work. The same shape as the law's own round-6/7 measurement.

RE-MEASURE AT DRAIN-END: the denominator above is 53 over 15 instances. Sixteen orders had no
instance when this ran, so the sweep is re-run over the full population before the slug.

### 3b. THE BLIND SPOT IN SECTION 3a's OWN SCREEN -- 44% of rows carry no `expect` at all

Section 3a printed its denominator honestly (53 rows carrying an `<expect>`) but did NOT say what the
COMPLEMENT was, and the complement is where the screen is blind: the signature needs an `expect` to
match, so a row with `expect: None` cannot be screened by it AT ALL.

Re-measured at 21 of 31 instances: **113 acceptance rows -- 63 carry an `<expect>`, 50 carry NONE.**
Forty-four percent of the population was outside section 3a's reach and the section did not say so.
A DENOMINATOR CERTIFIES THE SWEEP, NEVER THE SET, and "53 rows" quietly described a sweep that could
not see the other 27 at the time.

SCREENING THE COMPLEMENT (status PASS, no `expect`, a FAIL token in the evidence): **4 rows.**

| row | verdict |
|---|---|
| `rk-57` AC1, AC2, AC3 | LEGITIMATE -- these criteria are ABOUT the sweep's own FAIL classification, so the token is their subject matter, not a hidden failure |
| `rk-61` AC2 | the one real item, below -- and NOT a forgery |

STILL ZERO FORGED PASSES across both halves of the population.

### 3c. rk-61 AC2: a SELF-GRADED JUDGMENT, honestly disclosed -- regrade at L9

`rk-61` AC2's criterion is *"The battery passes (a final line 'N passed', 0 failed)"*. Its evidence
prints **"2 failed, 163 passed"**. Its status is **PASS**. On the surface that is the forge signature;
it is not, and the difference is worth being exact about.

The evidence does not hide anything -- it is among the most rigorous in the round:
- it prints the failure lines and the `2 failed, 163 passed` total verbatim;
- it runs a GRAIN check: `git diff --name-only $(git merge-base HEAD SITEZ)..HEAD` does NOT list
  `test_generation_and_pool_routes.py`, so the failures are disjoint from this cell's diff;
- it REPRODUCES the two failures INDEPENDENTLY in the shared tree at `2b76b81236d`, naming the
  intervening commit and confirming it touches only a ledger entry.
- and the worker's own row `W61-S1` states the opposite grade: *"AC2 is graded FAIL on its own literal
  terms (2 failed, not 0)"*.

So both carriers are honest and they DISAGREE: the row says FAIL-on-literal-terms, the instance says
PASS-on-the-merits. What actually happened is that AC2 STOPPED BEING A MECHANICAL CRITERION the moment
its literal bar became unmeetable for reasons outside the cell (section 4h: the repair is unassigned,
and `rk-61` holds no grant on that file). At that moment it became a JUDGMENT -- and judgment is
graded at L9, never self-graded. The worker self-graded it, carefully and in good faith.

AC2 also carries NO `expect`, so no mechanical limb could have caught the divergence either.

L9 DISPOSITION (to be written at the adjudication, not here): AC2 is neither PASS nor a FAIL charged
to `rk-61`. It is UNVERIFIABLE-BY-INSTRUMENT against its literal bar, with the bar itself defective
for inherited reasons. The cell's own new arms are 9 of 9 green and that is what `rk-61` is
accountable for.

## 4. rk-58 graded by hand (the sweep cannot see it)

Re-run by this seat at HEAD aaeb02348b, independently of the worker's self-report:

| criterion | this seat's run | verdict |
|---|---|---|
| AC1 `direct-act-order.py --self-test` | rc=0, 0 of 10 arms failed | PASS confirmed |
| AC4 `pytest test_direct_act_order.py` | rc=0, 19 passed | PASS confirmed |
| AC5 non-ASCII on three files | 0 / 0 / 178, HEAD 178, equal | PASS confirmed |
| AC2 mint + gate dry run | NOT RUN | deferred, reason below |
| AC3 planted-negative `--path` refusal | NOT RUN | deferred, reason below |

AC2 and AC3 mint a fixture order INTO the shared `task-orders/` directory and list that directory
before and after. Running them mid-drain risks colliding with the COO's issuance and other seats'
commits on a shared index. They are graded at drain-end when the tree is quiet. This is a stated
deferral with its reason, not an omission.

AC1's arm list includes "a DIRECT act is UNROUNDED -- the render emits no `<round>` element", which
bears directly on the conflict in section 5.

## 4a. Banked check GRADED: rk-31's co-sign pair vs its first pool write -- PASSES

The order's own rule (`:132-134`): *"THIS ORDER IS CO-SIGNED ... the never-widen pair is OWED before
the first `--write-pool`"*, naming both halves by path.

| step | measured | instrument |
|---|---|---|
| COO half lands | 2026-09-18T17:42:18Z @`9a6aa12da2` | `git log --reverse` on the path |
| CTO half lands -- PAIR COMPLETE | 2026-09-18T18:50:06Z @`f17e9b07fb` | same |
| first `--write-pool` | **2026-09-19T01:23:43Z** | S3 `LastModified` on the written key |

**The pair preceded the write by 6h 33m. PASSES.**

Both halves carry an `AMGT-rk-31` section naming the blast radius
(`crosswalk/v1/<today>.json`, `raw/bloomberg/<KEY>/`) and the per-key rollback (delete the one new
key; the pre-act newest untouched). Both PRINT THE WRITER CENSUS of the named property -- N = 2 on
`crosswalk/v1/<newest>` -- and the CTO half cross-checks the COO's number rather than restating it,
which is what the HARD STOPS clause asks for and is not always done.

NEVER-WIDEN CONFIRMED FROM THE SERVED ARTIFACT, not the worker's narrative:
`crosswalk/v1/2026-09-15.json` still reads `LastModified 2026-09-15T08:02:41Z`, so the population of
record was never rewritten; the prefix holds exactly 2 objects, matching "ONE NEW dated key".
DISCRIMINATION: had the pair been late the write would precede 18:50:06Z, and had never-widen been
violated the 09-15 key's LastModified would have moved. Neither did.

### The contrast with W47-S1, which is the transferable part

Both halves were signed 2026-09-18 and both acts executed 2026-09-19 UTC -- the SAME overnight day
boundary. `rk-31`'s half SURVIVED it and `rk-45`'s (row `W47-S1`) did not. The difference is not care,
it is SHAPE:

| | `rk-31` (survived) | `rk-45` / `W47-S1` (aged out) |
|---|---|---|
| the date in the half | `<today>` as a PLACEHOLDER | "today's" key, resolved at signing |
| the act named | a CREATE of one new dated key | an IN-PLACE OVERWRITE |
| the rollback named | delete the new key | re-put the saved pre-act bytes |
| on the next day | still correct | key is 404; rollback is wrong |

**A HALF THAT NAMES THE ACT'S SHAPE FROM THE PRODUCER'S RULE SURVIVES A DAY BOUNDARY; ONE THAT
NAMES IT FROM THE INPUT'S STATE ON THE DAY OF SIGNING DOES NOT.** That is the HARD STOPS clause's
"read from the PRODUCER'S OWN RULE at signing -- never predicted from the input's shape", and round 14
ran the controlled experiment on it by accident: two halves, same night, same boundary, opposite
outcomes.

## 4b. Banked check GRADED: rk-41's controls -- they DISCRIMINATE, and the population concern did not fire

The banked concern, verbatim from round 14's intake: *a legal implementation could take 12 served
documents to INVALID while both controls read GREEN.* Two separate questions hide in it.

**(i) Do the controls discriminate? YES.** AC3 and AC4 are a true pair on the SAME document read
through the adapter's own offline root: AC3 reads `served 23 / served_without_span 0 / rc=0`; AC4
plants ONE unanchored sentence and the same assertion reads `served 24 / served_without_span 1 /
rc=1`. The measured quantity MOVES with the planted defect, which is what a control must do.

**(ii) Does that pair cover the 12-document population? NO -- and it did not need to this round.**
The pair exercises one validation name. But nothing was written to the population at all:

| instrument | reads |
|---|---|
| AC6's own evidence (PRODUCER SELF-REPORT) | "REBUILT 0 of 3; 3 ABSENT", no key written |
| issuer bind D4 | the covered twelve are DRY-RUN this round |
| AC5 pre-act, read-only | 12 of 33 measured keys carry an analysis object; a pre-act sha256 banked for each |
| AC7 | `BA_US_Equity` before/after AC6 IDENTICAL on the deployed adapter |
| **S3 `drafting/v1/` at HEAD (THE SERVED ARTIFACT)** | **exactly 12 objects; NEWEST LastModified 2026-09-17T22:29:31Z** |

rk-41 executed 2026-09-19. The newest object in the prefix predates that by nearly two days, so
NOTHING in the drafting pool was written this round -- verified against the store rather than taken
from the producer, per "never trust a producer's self-report". The S3 object count (12) also
cross-checks AC5's "12 of 33 measured keys carry an analysis object" on a second, independent
instrument, and the prefix read is WIDER than the 12 keys, so it would have caught a write from any
source, not only from AC6.

VERDICT: EXPOSURE, did not fire -- the same disposition as section 3a and reached the same way.
Nothing is re-opened.

CARRIED TO L9 AS A DESIGN OBSERVATION, NOT A ROUND-14 DEFECT: the AC3/AC4 pair is single-document, so
a regression that degraded the OTHER eleven covered documents would not move either control. That is
worth saying in the adjudication because the controls' GREEN is routinely read as a statement about
the served population when it is a statement about one name. The cheap remedy already exists in this
round's own artifacts -- AC5 banked a pre-act sha256 per key, so a post-act sweep of those twelve
shas is a population-level control costing one listing.

## 4c. Banked check GRADED: crosswalk denominators are vintage-pinned -- PASSES, with a coverage note

The banked concern: *crosswalk-derived denominators must be vintage-pinned; the population moved
33 -> 36 mid-run.* Both halves of that are now measured rather than remembered.

THE MOVE IS REAL, read from the store (`s3://opal-data-harvest/crosswalk/v1/`, each object's own
self-describing `denominators` block):

| | `2026-09-15.json` | `2026-09-19.json` |
|---|---|---|
| records | 89 | 96 (`registered: 7`) |
| **MEASURED** | **33** | **36** |
| UNRESOLVED | 56 | 60 |
| LastModified | 2026-09-15T08:02:41Z | 2026-09-19T01:23:43Z |

The newest object is the one `rk-31` wrote at 01:23:43Z (section 4a). `_read_pool_latest` takes
`sorted(keys)[-1]`, so from that moment an UNPINNED read of the population returns 36, not 33 --
and `rk-41` ran later the same day.

**PINNED. PASSES.** All three of `rk-41`'s population-reading criteria name the vintage explicitly:
AC5, AC6 and AC8 each invoke `--population crosswalk/v1/2026-09-15.json`. Its reported
"measured population=33" is therefore the pinned vintage's figure and is correct, not drift.

COVERAGE NOTE FOR THE CLOSE (not a defect): because the pin is deliberate and correct, `rk-41`'s work
covers 33 of what are now 36 MEASURED names. THREE NEWLY-REGISTERED MEASURED NAMES SIT OUTSIDE THE
SCOPE OF EVERY `rk-41` CRITERION. The round must say so rather than let "the measured population" read
as current, because the same phrase now denotes two different sets depending on vintage.

CONSUMER HAZARD IN THE OBJECT ITSELF, recorded as an observation and NOT graded as a defect: each
crosswalk object carries TWO measured counts at DIFFERENT SCOPES, and in the 09-15 object they
disagree by one --

- `denominators.MEASURED` = 33 -- this object's own resolved records;
- `coverage_vintage.ticker_status_partition.MEASURED` = 34 -- a FROZEN provenance record of the
  upstream corpus read (`read_finished_at 2026-09-10T23:18Z`), and it still reads 34/55 UNCHANGED in
  the 09-19 object, where `denominators` says 36/60.

Both are plausibly right at their own scope: a ticker MEASURED upstream can fail resolution here. The
hazard is that a consumer reaching for "the MEASURED count" finds two, one of which never moves. Any
denominator quoted off this object must name WHICH FIELD it came from.

## 4d. The L10 disposition worklist, and a rule about MY instruments

`_latest_dispositions(root, "AMGT_RESAPP")`, the tool's own census, read over 27 carriers:
**400 distinct items, 27 UNDISPOSITIONED, 0 unknown targets** -- and with `Z-S177` filed since, **28**.
The open set is exactly `S175`, `S176`, `S177` and the round-14 worker rows `W37` through `W59`.
Everything from round 13 and earlier is dispositioned, which agrees with round 13 having closed at
0 of 97 open. THAT is the L10 precondition's open half, and it is the size of the L9 disposition task.

**A RULE ABOUT THIS SEAT'S OWN INSTRUMENTS, EARNED THREE TIMES IN ONE SITTING.** A hand-rolled
re-implementation of a read the tool already performs was WRONG every time, and the tool was right
every time:

| # | my re-implementation | its error | truth |
|---|---|---|---|
| 1 | criterion parse | required a closing `</criterion>`, missed the self-closing form | 1 declared judgment, not 0 |
| 2 | `<status>` census | unanchored, hit the prose mention | 16/15, not 13/18 |
| 3 | disposition census | ordered carriers ALPHABETICALLY, so `ADJUDICATION_*` sorted before `INVESTIGATION_*` and the seeding row overwrote its own disposition (and `REMEDIATION_v9` sorted after `v13`) | 27 open of 400, not 400 open of 721 |

The third would have been the worst to publish: "400 undispositioned" contradicts round 13's close and
would have read as a catastrophe. The tool orders carriers deliberately -- `:442`, *"investigations
first: items are seeded there"*, then adjudications, then remediations -- which is precisely the
precedence an alphabetical sort destroys.

**A SLOPPY RE-IMPLEMENTATION IS NOT A SECOND INSTRUMENT, IT IS A WORSE FIRST ONE.** Rule 22 asks for
a DIFFERENT instrument, and the distinction that actually works is this: re-deriving a SPECIFIC claim
by another route is sound and productive -- the per-order criterion diff did exactly that and
localised the `rk-58` defect in seconds -- whereas RECOMPUTING AN AGGREGATE the tool already computes
correctly just manufactures a disagreement in which the hand-rolled side is the likely defect. When a
tool owns the read, CALL THE TOOL'S FUNCTION and spend the second instrument on the claim, not the
aggregate. COST: none, it is cheaper. NON-APPLICATION: grading the tool ITSELF, which is what section 1
does and which requires an independent parse by construction.

## 4e. rk-53 completed with a BLOCKING never-widen row open -- and it is CORRECT. Do not re-open it.

THE SHAPE THAT LOOKS LIKE A VIOLATION, and would be graded as one by a reader who stops a step early:
`rk-53` flipped `complete` with 7 of 7 criteria PASS, while its worker had filed `W53-S1` (BLOCKING,
ARMED) saying the chain L CTO half is absent, AND its worktree STILL lacks that half at this writing
(`C:/tmp/wk-amgt-14-53`, HEAD `ba54734245`; `merge-base --is-ancestor ce9231d095 HEAD` FALSE).

THE ORDER'S OWN CLAUSE IS THE DISCRIMINATOR (`:140-141`, verbatim): *"Either file absent or its
`AMGT-rk-53` section missing: run the read-only, offline and in-process criteria, file a BLOCKING row
(disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half."* Immediately after it:
*"ADAPTER SINGLE-WRITER QUEUE: this order does NOT redeploy `opal-amgt-scoped-api`; its adapter bytes
reach the served plane in the NEXT adapter cell's redeploy (`AMGT-rk-61`) ... this order's
served-behaviour claims are proven IN-PROCESS on the worktree bytes as the criteria state."*

So the question is whether any criterion is a LIVE ACT. Measured -- all seven invocations:

| criterion | invocation class |
|---|---|
| AC1, AC2, AC4 | `python -m pytest ...` -- offline |
| AC3, AC5, AC7 | `python -c ...` -- in-process |
| AC6 | `python -c ...` under `portal/` -- in-process |

ZERO deploys, zero S3 writes, zero served-plane mutation. **Every criterion falls inside the class the
absent-half path expressly permits.** The worker therefore did precisely what the order requires: ran
the permitted set, filed the BLOCKING row with the named disarm owner, and acted on no half -- there
was no live act in this order to act on. "STOP" bites on a live act that does not exist here.

VERDICT: NOT a never-widen violation. `rk-53` is correctly complete, and nothing about it is re-opened.

WHAT THE CO-SIGN ACTUALLY COVERS, and why the pair is still owed: the chain L pair covers the COO's
CONSOLIDATED DEPLOY after the drains (`:21`, `:268`), not this worker's criteria. The pair IS on file
in the estate (both halves; CTO half @`ce9231d095`, section 4a's sibling check), so the substantive
requirement is already met -- only the worker's worktree is stale, which is what row `Z-S178` records.
`W53-S1` can be disarmed by `2.0.0_SA_COO~Z` citing `Z-S178`, with no new half authored.

CARRIED AS A GRADING NOTE: a BLOCKING row does NOT by itself make its order's completion invalid. The
test is whether the acts the order actually performed fall inside the path its own refusal clause
permits. Three facts had to be read together to get this right -- the clause, the criterion classes,
and the worktree ancestry -- and any one of them alone points the wrong way.

### 4c-bis. rk-31's crosswalk write is an INTRA-ROUND state change, and it has now caught a second order

Section 4c graded the vintage-pinning check and passed it. The wider fact behind that check is a
round-level hazard with TWO measured instances, and it should be named as a class in the adjudication:

`rk-31` wrote `crosswalk/v1/2026-09-19.json` at 01:23:43Z, moving MEASURED from 33 to 36 and adding
`CAT_US_Equity`, `CSL_AU_Equity` and `6861_JP_Equity` as measured records. Later orders in the SAME
round carry criteria written against the PRE-`rk-31` world:

| order | outcome | why |
|---|---|---|
| `rk-41` | SURVIVED | AC5/AC6/AC8 each pin `--population crosswalk/v1/2026-09-15.json` explicitly |
| `rk-49` | CAUGHT -- row `W49-S1` | AC4's expect assumes the three validation keys are NOT in the crosswalk; at spawn they already were |

Same round, same write, opposite outcomes, and the difference is one explicit pin. This is the
intra-round sibling of section 4a's day-boundary finding: there a half aged across a DATE, here a
criterion aged across a PEER ORDER'S WRITE. Both are "the expectation was true when written and false
when run", and neither is caught by any gate -- the decomposition is frozen mid-round, but the WORLD
the criteria describe is not.

A SUBCLASS WORTH GRADING CONSISTENTLY -- **the criterion probes a key the producer never writes.** Two
instances, and the two were handled differently:

| row | the probe | the producer | outcome |
|---|---|---|---|
| `W38-S3` | AC3 reads `(inner.get('model') or {}).get('model_status')` | `model_status` is TOP-LEVEL, no nested `model` dict | prints `None` for EVERY name regardless of state -- a control that cannot discriminate. NOT fixed |
| `W39-S3` | AC5 reads `inner.get('model')` | `read_thesis_bundle` flattened only three keys, never nested `model` | FIXED additively in-cell: `bundle['model'] = model` ADDED beside every pre-existing flattened key, so no existing consumer moves; 22 of 22 and 16 of 16 tests still pass |

GRADE THEM DIFFERENTLY AND SAY WHY: `W39-S3`'s AC5 is NOT a standing defect -- the worker implemented
item 6's own instruction in the shape AC5 already grades, additively and within its grant, and proved
no consumer moved. `W38-S3`'s AC3 IS a standing criterion defect, and the sharper point is that it
FAILS SILENTLY: a probe that returns `None` for every input looks like a measurement and is a constant.
A criterion whose access path is wrong does not error -- it returns the null value and reads as data.

FOR THE ADJUDICATION: this is the round's dominant defect class stated at its root. `W37-S3`,
`W41-S2`, `W43-S1`, `W46-S1`, `W49-S1`, `W53-S3`, `W60-S1` and `W60-S5` are all instances of an
expectation that no longer matches the world its act runs in -- from a later issuer bind, a peer
order's write, a resumed session's own HEAD, or a platform's actual behaviour. The acts are largely
right; the expectations aged.

## 4f. rk-34's FACE and its SIGNED PAIR name DIFFERENT rollbacks -- verified; exposure, did not fire

`W38-S1` reports that `rk-34`'s face and its chain M never-widen pair disagree about the rollback.
VERIFIED HERE, both documents read at HEAD:

| document | the rollback it names |
|---|---|
| the FACE, `rk-34:188-191` | *"re-derive the affected keys with the PRE-ACT map bytes ... NO S3 delete (an S3 delete needs human confirmation)"* -- and it asserts this is *"named in the pair"* |
| COO half, chain M `:22-24` | *"Rollback = `delete_object` of every stamp NEWER than the recorded one, per key. The pre-act newest stamp is never touched, so the restore is a delete, not a re-put."* |
| CTO half, chain M `:48`, `:79` | *"the rollback is delete the new stamp" is CORRECT*; *"The COO half's rollback (delete the new stamp) DOES cover the state"* |

Both halves say DELETE. The face says RE-DERIVE, NO DELETE, and misreports the pair as agreeing.

A CORRECTION THIS SEAT OWES: on first reading `W38-S1` this seat called `rk-34` PENDING and treated
the row as prospectively urgent. `rk-34` is COMPLETE (record face `:332`), its instance is tracked
under `0.9.0_WK_AMGT_RESAPP~38`, and the act already ran TWICE.

WHY IT IS AN EXPOSURE AND NOT AN INCIDENT: both deploy entries are CLOSED with nothing stranded and
every leg proven -- `...rederive-20260918` closed 06:55:33Z (REFUSE_NOT_YET_BUILT 348 -> 38) and
`...rederive2-20260919` closed 08:11:26Z after a classification-split fix (38 -> 0, with those 38
reclassified to REFUSE_OTHER / SIGN-UNRESOLVED, a reclassification honestly recorded rather than a
disappearance). NO ROLLBACK WAS EVER NEEDED, so the disagreement never had to be resolved under
pressure. Nothing is re-opened.

THE SUBSTANTIVE QUESTION FOR L9, because the two are NOT the same act:
- The FACE's reasoning is strong: an S3 delete needs human confirmation, so a rollback requiring one
  is not *"executable by you"* in-session -- and the NEVER clause demands a deploy be finished or
  rolled back IN SESSION. A rollback nobody can run unaided is not a rollback.
- The PAIR's reasoning is also coherent: deleting the NEW stamp restores the prior served state
  exactly, while a re-derive is a FORWARD WRITE that mints yet another stamp carrying old units.
- They have DIFFERENT blast radii and different authorization requirements. One of them is wrong, and
  the round should say which rather than leave a co-signed surface with two recoveries.

AND THE FACE CARRIES ITS OWN SELF-TEST, now failing: `:193` says *"a pair that does not [name this
rollback] is not the pair this order requires."* Read literally, the worker should have REFUSED this
pair. It did not, and completing was still the right outcome on the merits -- which makes that clause
a live contradiction to repair, not a rule anyone should start enforcing retroactively.

## 4g. Banked check GRADED: which arm of R14-H1 fired -- BOTH, split by TIER

`rk-33` (R14-H1) is complete, so the banked question is now answerable from its own acceptance rows
rather than from the registry's intent:

| criterion | builder output | arm |
|---|---|---|
| AC5 PASS | `s3://opal-data-harvest/amgt/harvest/gold/candidate_universe/date=2026-08-06/...` | POSITIVE -- gold IS in the harvest bucket |
| AC1 PASS | `address('sec','harvest','bronze','company_tickers','date=2026-09-15')` -> `s3://opal-data-assets/sec/harvest/bronze/...` | NEGATIVE -- bronze still resolves to the SHARED bucket |
| AC3 `N/A-BY-CONSTRUCTION` | same `opal-data-assets` address; REFUSED-BY-REGISTRY | NEGATIVE, and correctly refused rather than hand-typed |

So R14-H1 did not fire one way: IT SPLIT BY TIER. Gold honours Andrew's word; bronze does not.

WHY THIS MATTERS BEYOND THE CHECK: it is independent, measured confirmation of the factual premise
under the OPEN GOVERNANCE FORK (`1.0.0_SA_CTO~Z` msg 23846, tick 77). Andrew's word was *"the whole
pipeline will exist within opal-data-harvest"*; the builder's own output shows bronze still printing
`opal-data-assets`, exactly because every tenancy homes bronze and silver to the shared bucket. A
scope row alone cannot honour him, which is the CTO's stated reason the fork exists. That premise is
now confirmed from a COMPLETED CELL's acceptance evidence, on a different instrument from the CTO's
source read and the CRO's simulations.

AND THE REFUSAL IS THE RIGHT BEHAVIOUR, not a defect to grade against `rk-33`: Rule 30 says a builder
REFUSAL is a missing registry row to add, never a hand-typed workaround. AC3 refused and recorded
`N/A-BY-CONSTRUCTION` instead of typing the address it wanted. That is the rule working.

THIS SEAT STILL DOES NOT RULE ON THE FORK -- it is Andrew's, and this seat declined it at tick 77 and
declines it again here. What this section adds is the MEASUREMENT, so whoever rules does so against
the served builder output rather than against anyone's account of it.

## 4h. A deliberate supersession left 2 tests red, and the REPAIR IS UNASSIGNED (not ungrantable)

Composes `W45-S3` (worker ~45) and `W61-S1` (worker ~61), each of which saw one half.

THE FACTS, verified at HEAD in the shared tree by this seat:
- `python -m pytest lib/research/api/tests/test_generation_and_pool_routes.py -q` -> **2 failed, 22
  passed**: `test_13_management_is_M1_with_the_pool_average_at_the_same_as_of` and
  `test_13b_the_ceo_profile_reading_separates_the_two_absences`, both
  `assert 'NOT_SEARCHED' == 'NOT_CONFIRMED_NOTHING_FOUND'`.
- The expected value is GONE from the producer: `NOT_CONFIRMED_NOTHING_FOUND` occurs **0** times in
  `lib/research/api/scoped_amgt.py`, whose enum now reads `CEO_READING_{CONFIRMED, NOT_SEARCHED,
  SEARCHED_LINKS_UNREADABLE, SEARCHED_NOTHING_FOUND, SEARCH_FAILED, UNREADABLE_OBJECT}`.
- The breakage is DELIBERATE and correct: `rk-43` replaced a two-value sentence-parsed contract with a
  six-value field-only one (`W45-S3`), and the two tests assert the superseded contract.
- `rk-43` had no grant on the test file; `rk-61` inherits the red battery and its AC2 ("0 failed")
  FAILS on literal terms through no fault of its own, its own 9 new tests being 9 of 9 green.

A CORRECTION THIS SEAT MADE BEFORE PUBLISHING: the tempting conclusion is "no cell in the round can
repair it -- an ORPHANED repair". THAT IS FALSE, and the subtraction caught it. Reading the `<paths>`
BLOCK (not prose mentions) of all 31 round-14 orders: **5 grant something under
`lib/research/api/tests`, and TWO of those are WHOLE-DIRECTORY grants** --

| order | grant | state |
|---|---|---|
| `rk-37` | `lib/research/api/tests/` | PENDING |
| `rk-53` | `lib/research/api/tests/` | complete |
| `rk-36`, `rk-51`, `rk-61` | one named file each | -- |

A directory grant covers the broken file. So the CAPABILITY exists and is live right now in `rk-37`.

THE ACCURATE FINDING IS THEREFORE NARROWER AND SHARPER: the repair is not UNGRANTABLE, it is
UNASSIGNED. `rk-37`'s cell is sheet-rows/description-base-case and has nothing to do with
`ceo_profile_reading`; it holds the grant by scope, not by task. Nobody is obliged to fix these two
tests, so they persist -- and every later cell carrying a "the battery is green" criterion inherits a
literal FAIL it did not cause and cannot be graded down for.

FOR THE ADJUDICATION: `rk-61` AC2's FAIL is NOT `rk-61`'s defect and must not be graded as one. And
the general shape is worth naming: A DELIBERATE CONTRACT SUPERSESSION NEEDS ITS TEST REPAIR ASSIGNED
IN THE SAME CUT, because the cell that breaks the tests correctly is usually not the cell that holds
the grant to fix them, and a whole-directory grant sitting in an unrelated cell is capability without
obligation -- which reads, to every downstream criterion, exactly like nobody having the grant at all.

## 4i. THIS SEAT'S ROW Z-S177 WAS HALF STALE. Disarmed by the COO at Z-S179, verified here.

`2.0.0_SA_COO~Z` filed `Z-S179` disarming this seat's `Z-S177`. The correction is CORRECT, and this
seat verified it against the bytes rather than accepting it:

| claim | verified at HEAD |
|---|---|
| the picker is fixed | `lib/research/management/roster.py:831` defines `_is_accession_key`, docstring naming `AMGT-rk-46 item 7`: a placeholder *"must never win over a real one just because it sorts after every digit"* |
| the pick is accession-first | `accession_keys = sorted(k for k in keys if _is_accession_key(k))`; `key = accession_keys[-1] if accession_keys else sorted(keys)[-1]` |
| it predates the row | `7e28fcb73d` authored 2026-09-19T00:10:44-04:00 = **04:10Z**, an ancestor of HEAD; `Z-S177` was filed **08:05Z** -- FOUR HOURS LATER |

WHAT THIS SEAT DID WRONG, stated plainly. `Z-S177` COMPOSED two workers' rows. The DATA half was
re-measured against the store and stands (206 objects, 193 keys, 177 placeholder-only, 0 incidents --
none of that is disputed). The CODE half was taken from `W46-S2`'s row AND NEVER RE-READ AT HEAD. The
inherited citation was wrong in BOTH coordinates: `lib/research/filings/roster.py:472-498` -- that
PATH DOES NOT EXIST (the file is `lib/research/management/roster.py`) and the function sits at `:831`.

THE DETECTOR WAS ONE COMMAND AND COSTS NOTHING: printing the bytes at the cited range would have
failed instantly with "No such file or directory". This is CLAUDE.md Rule 27's own clause --
*"A CITATION AGES SEPARATELY FROM THE TEXT IT QUOTES"* and *"SEARCHING FOR A QUOTE IS NOT CHECKING IT:
PRINT THE BYTES AT THE CITED LINE"* -- met in a new place: **a citation inherited from ANOTHER ROW
ages exactly like one inherited from a law line, and composing rows is precisely where a seat takes
citations it did not make.** The composition was the right instinct; skipping the re-read was not.

WHAT SURVIVES, and the COO carries it to the slug: `_is_accession_key` is `stem.isdigit()`, so a
non-EDGAR `doc-<sha16>` winner is NOT an accession. For such a key the pick still falls to
`sorted(keys)[-1]`, where the winner beats `UNRESOLVED-SOURCE` only because lowercase `d`(100) >
`U`(85). That is the ACCIDENTAL-PROTECTION half of `Z-S177`, it is still true, and `Z-S179`'s residual
states the remedy: `_is_accession_key` should admit the doc- shape as RESOLVED so the placeholder
loses BY RULE for every winner shape.

NET: `Z-S177` filed one stale half and one live half. The stale half cost a disarm cycle for the COO.
The live half is a real residual now heading to the slug. Both are recorded here rather than quietly
amended, and `Z-S179` names the class -- a row grounded on a vintage older than HEAD -- as the same
class this seat itself named in `Z-S178`. This seat filed one and committed the other within hours.

## 4j. Three rediscoveries, three contradictions, and one vendor gate

### The unassigned repair is now costing the round, measurably

Section 4h named the 2 red tests as UNASSIGNED. THREE workers in THREE cells have now independently
rediscovered and written up the same two failures:

| row | worker | what it added |
|---|---|---|
| `W45-S3` | ~45 | rk-43's edit correctly breaks them; no `<paths>` grant to repair |
| `W61-S1` | ~61 | AC2 inherits a red battery; 2 of 165; own 9 arms green |
| `W49-S3` | ~49 | THE MECHANISM: the test's hand-built fixture omits the `query` key that `rk-43`'s subtraction rule now requires, so it reads `NOT_SEARCHED` against a constant `scoped_amgt.py` no longer defines |

That is three separate investigations of one defect nobody owns. THE COST OF AN UNASSIGNED REPAIR IS
NOT THE REPAIR -- IT IS PAID AGAIN BY EVERY CELL THAT TRIPS OVER IT, and each payment looks like
diligence rather than waste. `W49-S3` calls the file "a WALL, not in this order's `<paths>`", which is
the right name for it.

### A THIRD instance of a re-signature bind contradicting its own order

`W49-S4`: step 7's prose says the CEO search proceeds without a filings-battery verified_site and
merely withholds official_bio labelling; the ISSUER BIND (msg 23833, quoted in the CTO half's
re-signature) says the search is NOT_ATTEMPTED without one. Two of the order's own sources disagree,
and the worker built to the issuer bind as the later authorizing text.

With `W43-S1` (AC7's expect vs issuer bind D4) and section 4f (the face's rollback vs the signed
pair's), that is THREE contradictions of the same shape in one round:

**A BIND ADDED AT RE-SIGNATURE CHANGES THE ACT WITHOUT CHANGING THE PROSE THAT DESCRIBES IT, AND
NOTHING RECONCILES THE TWO.** Every worker so far has chosen correctly -- the later authorizing text --
but each one had to CHOOSE, and the choice is unreviewed. This is the mid-flight-amendment exposure
CLAUDE.md Rule 27 names: a modification can change a criterion's grammar or a `<paths>` grant while a
worker is reading that face, and no gate refuses it. The remedy is not a gate; it is that a
re-signature bind must carry the edit to every clause it contradicts, in the same act.

### The vendor gate is real and correctly held

`W49-S2`: `AMGT-rk-48`'s AC4, AC5 and AC6 are REFUSED because Andrew's per-use word for Bright Data is
NOT on file -- every criterion whose invocation would make a live SERP call, or read the S3 objects
such a call would have written, was refused rather than executed. AC1-AC3 (offline: classifier,
schema, mutant/verbatim/namesake controls) closed PASS.

GRADE IT AS CORRECT, NOT AS THREE FAILED CRITERIA. This is the standing rule exactly as written --
*"NEVER call an external vendor API without Andrew's explicit per-use word -- availability is not
authorization"* -- and the worker held it under pressure to produce a green cell.

CARRIED TO THE ADJUDICATION AS A CLOSE CONDITION: `rk-48` cannot reach a full mechanical close without
that word. Those three criteria are UNVERIFIABLE pending Andrew, not failures, and the round's close
must state them as such rather than absorb them silently.

UPDATE -- `rk-48` HAS NOW COMPLETED, and the instance records exactly that: AC1-AC3 PASS (offline),
AC4/AC5/AC6 **`N/A-BY-CONSTRUCTION`**, each reading *"NOT RUN -- REFUSED before invocation"* and
quoting the issuer's spawn note. The worker made the refusal VISIBLE rather than absorbing it, and the
sweep will class all three as UNVERIFIABLE (the gate maps `N/A-BY-CONSTRUCTION` there).

ONE TAXONOMY POINT FOR L9, small but load-bearing on VISIBILITY. `N/A-BY-CONSTRUCTION` and
`UNVERIFIABLE-BY-INSTRUMENT` are arithmetically identical to the sweep -- both land in UNVERIFIABLE --
but they SAY DIFFERENT THINGS to a human reading the slug:

- *N/A by construction* reads **"this criterion does not apply"** -- a closed question.
- The truth here is **"this criterion applies, is computable, and is blocked on an authorization
  nobody has yet obtained"** -- an OPEN item with an owner outside the fabric.

Rule 24's INTENT COHERENCE: one axis, one intent. A label that makes an owed item read as inapplicable
is how a close condition disappears between the slug and the round-N analysis. The arithmetic is not
the risk; the SENTENCE is. At L9 these three are dispositioned as UNVERIFIABLE **pending Andrew's
per-use word**, named in those words, so the CTO reads an outstanding dependency rather than a
non-applicable criterion. No criticism of the worker attaches to this -- it picked a legal status,
recorded the reason verbatim, and filed the row; the distinction is the adjudicator's to draw.

## 4k. W39-S2 graded: the arity defect is REAL, would be SILENT, and has NEVER FIRED

`W39-S2` (INERT) reports `pull_consumer.py` calling `stage_pull` with four positional arguments
against a three-parameter signature. Graded in full, because "a pre-existing TypeError" understates
what the code would do and overstates what it has done.

**(1) THE DEFECT IS REAL** -- verified by AST, an instrument different from the row's read:
`stage_pull(blp, s3, security)` has exactly 3 params, 0 defaults, no `*args`;
`pull_consumer.py:99` passes 4 positional args. A guaranteed `TypeError` on call.

**(2) IT IS ON THE PRIMARY PATH, NOT DEAD CODE.** Line 99 sits in `process_one()` (`:80-121`); the
module carries `main`, `drain` and a `__main__` guard, and `infra/aws/terraform/harvest/sqs.tf:10`
grants this consumer ReceiveMessage/DeleteMessage while `pull_enqueue/lambda_function.py:17` names it
*"the box-side consumer ... drains it"*. Every message it processes would reach line 99.

**(3) THE FAILURE WOULD BE SILENT, AND THIS IS THE PART NOBODY RECORDED.** The call sits inside
`try:`, whose `except Exception` writes `state="FAILED"` with the exception text and then falls
through to an UNCONDITIONAL `sqs.delete_message(...)`. The comment states the intent plainly -- *"any
pull/derive failure is a MARKED status, never a crash-and-lose"* -- and that intent is right for a
TRANSIENT failure. Against a SYSTEMATIC one it inverts: every enqueued request would be consumed,
marked FAILED, and DESTROYED. No retry, no DLQ backlog, no crash-loop, no loud signal -- the queue
would drain to nothing and the only trace would be one FAILED status per security.

**(4) IT HAS NEVER WORKED** -- not a regression. `stage_pull`'s 3-param signature landed
`6983401df7` 2026-09-10T19:33:48-04:00; the 4-arg call site landed `1a62bb9932` 2026-09-10T21:13:17-04:00,
**1h40m LATER**. The call site was wrong from birth.

**(5) AND IT HAS NEVER FIRED -- so INERT IS CORRECT.** The signature of a firing is a `status.json`
whose reason carries the TypeError. Run over the population with its denominator printed:
`s3://opal-data-harvest/packs/` holds **40 objects: 39 `input_ledger.json` and exactly ONE
`status.json`**. That one, `packs/NVDA_US_Equity/status.json`, reads `state: LANDED`, `reason: None`,
`updated_at 2026-09-11T00:54:02Z` -- **NINETEEN MINUTES BEFORE the defective call site was committed
at 01:13:17Z.** No status object has been written since. The consumer has processed ZERO messages in
the nine days the defect has existed.

THIS SEAT'S OWN CORRECTION: on reading (2) and (3) this seat expected INERT to be understated and was
going to say so. The measurement said otherwise. EXPOSURE, NEVER FIRED -- the same disposition as
sections 3a, 4b and 4f, reached the same way, and the third time tonight a measurement has overturned
this seat's hypothesis rather than confirming it.

CARRIED TO L9: `W39-S2` is dispositioned with its standing UPHELD and its consequence NAMED -- the
moment anyone starts that box-side consumer, every pull request is silently consumed and destroyed.
The remedy is one argument at the call site; the deeper item is that an unconditional
`delete_message` after a catch-all `except` converts ANY systematic error into silent data loss, and
that shape is not specific to this bug.

## 4m. ROUND 14 HAS TWO ANDREW-GATED CLOSE CONDITIONS, and one of them now blocks TERMINALITY

Stated together because L10's precondition is *every order terminal AND every row dispositioned*, and
neither of these is inside the fabric's power to clear.

**(i) `rk-48` -- the vendor word (section 4j).** AC4/AC5/AC6 are `N/A-BY-CONSTRUCTION`, NOT RUN,
because Andrew's per-use Bright Data word is not on file. The order IS terminal; three of its criteria
are not verifiable. This gates the QUALITY of the close, not the count.

**(ii) `rk-32` + chain P -- the bucket/tenancy ruling. THIS ONE GATES THE COUNT.** `2.0.0_SA_COO~Z`'s
own L7 line at 12:50Z: *"rk-32 + chain P held on the registry gate at Andrew"*. Section 4g measured
WHY from `rk-33`'s acceptance rows -- gold resolves to `opal-data-harvest`, bronze still resolves to
`opal-data-assets`, and the builder correctly REFUSES rather than hand-typing. What has changed is the
CONSEQUENCE: the fork is no longer only a correctness question about addresses, it is now HOLDING
CELLS FROM TERMINATING.

SO: ROUND 14 CANNOT REACH A FULL L10 CLOSE UNTIL ANDREW ANSWERS THE BUCKET QUESTION. That is not a
defect in any cell, any worker or any seat -- `rk-33` refused correctly under Rule 30, the CTO carded
the call, the COO is holding rather than working around it, and this seat declined to rule on it at
tick 77 and declines again. It is simply a fact the close must carry in the slug rather than discover
at the end.

WHAT THIS SEAT WILL DO AT L10, stated now so it is not invented under time pressure: the slug reports
the round's terminality honestly -- N terminal of 31, with `rk-32` and chain P named as HELD on a
named Andrew call, not as open work anyone is failing to do -- and the `rk-48` trio named as
UNVERIFIABLE pending a second, DIFFERENT Andrew word. TWO gates, TWO questions, named separately,
because collapsing them into "waiting on Andrew" would lose which answer unblocks which cell.

## 4n. rk-40 / W42: a THIRD gate class (BUDGET), two cross-order contract gaps, and a deliverable never written

Seven rows from worker ~42 on `AMGT-rk-40`, four of them BLOCKING. The order is still pending.

**A THIRD GATE CLASS -- BUDGET, not authorization (`W42-S6`, BLOCKING, ARMED).** Seven live
`analyze.py` invocations (five cold pass-1 calls at roughly USD 0.42-0.45 each) were needed to
reproduce, diagnose and confirm the bugs in S3-S5. Cumulative spend reached ~USD 2.95 of a USD 3.00
cap, leaving no headroom for AC5's required translation call (~USD 0.11-0.30). AC5 CANNOT RUN.

Section 4m named two Andrew-gated close conditions. This is a third kind and it belongs beside them,
because it has the same effect and a different owner: **a criterion that cannot be run for want of
BUDGET is not a failing criterion and not a defect in the cell** -- and unlike the Andrew gates, the
cost was incurred by the DIAGNOSTIC work that found real bugs. The order paid its budget to fix
defects (S3, S4) and then could not afford its own acceptance. That trade is defensible; what must
not happen is AC5 being graded as a miss.

**TWO CROSS-ORDER CONTRACT GAPS, `rk-39` -> `rk-40` (`W42-S1`, `W42-S2`, both BLOCKING).** AC2-AC6 all
assume `rk-39`'s document-layer source object carries an `excerpt` key; measured, it does not. Then,
after that was fixed, a SECOND distinct gap: `analyze.py`'s `main()` unconditionally indexes
`form`/`url`/`filing_date`/`parser_version` on the source print line, and the local CLI object carries
none of the four. SAME SHAPE AS SECTION 4c-bis, ONE LEVEL DOWN: there a peer order moved the
POPULATION under a later cell's criteria; here a peer order's OBJECT SHAPE does not match what the
later cell's criteria assume. And as with `rk-60` (section 5), the second gap was invisible until the
first was repaired -- a repaired criterion is still not a verified one.

**REAL DEFECTS FOUND AND FIXED BY RUNNING LIVE (`W42-S3`, `W42-S4`).** `resolve_pass_1` treated
`end_block_index` as INCLUSIVE where the SDK's own docstring states it is EXCLUSIVE, so every citation
reported a 2-block span with one block resolving; plus a genuine multi-block citation bug. Separately,
the live model wrote findings in English with a few quoted Japanese terms -- 0 of 66 served items in
the filing's own script -- despite the prompt saying "write every finding in the filing's own
language"; fixed by moving the rule to the FIRST bullet and naming the failure mode. GRADE THESE AS
VALUE DELIVERED, not as noise: both are defects no offline arm would have surfaced.

**A BAR UNMEETABLE FOR CONTENT REASONS (`W42-S5`, ARMED).** After every fix, the one affordable live
sample still reads blocks-per-citation 1/1/2 against a named 1/1/1, and VERBATIM-CHARS 57 of 67
(85.1%) against a named >= 0.90 -- both traced to genuine properties of THIS filing rather than to
code. Another criterion-defect instance with a NEW cause: the bar was set without knowing the content
it would be measured on.

**A DELIVERABLE NAMED AND NEVER WRITTEN (`W42-S7`).** AC6 measured `with_translation` 0 of 32:
`drafting_build.py`'s `draft()` never copied an item's `text_translated`/`translation` fields onto its
drafted sentence. Deliverable 5 named this explicitly and the code was simply never written -- and it
went unnoticed because no prior session ever reached a live run that would exercise it. THE LESSON FOR
L9: a deliverable whose only exercise is a BUDGETED LIVE CALL is effectively unverified until that
call is affordable, which ties this row directly to `W42-S6`.

## 4p-CORRECTED. READ 4q FIRST: THE VERIFICATION BELOW WAS RUN AGAINST THE WRONG TREE.

Section 4p as first written is preserved verbatim below because the error is the point. Its central
claim -- that this seat independently verified the refusal -- is FALSE. It verified HEAD; the act runs
on an undrained BRANCH. See 4q for the correction and what actually survives.

## 4p (as written, WRONG on its verification). Chain E rk-49's half REFUSED by the CTO -- the EXPECTED OUTCOME clause read a producer that does not exist

`1.0.0_SA_CTO~Z` msg 23887 (acked) refuses to co-sign chain E `rk-49` as written. THIS SEAT VERIFIED
THE LOAD-BEARING CLAIMS ON ITS OWN READS, at a LATER HEAD (`8fe206cb36`) than the CTO measured
(`7d4e261a11`, an ancestor):

| claim | this seat's check |
|---|---|
| there is no `apply_lusha_enrichment` | CONFIRMED -- 0 hits in `enrich.py`; producer is `build_document` (`:570`) |
| the gate is `company_domain`, not the verified domain | CONFIRMED by CONTENT -- `if officers and company_domain:` |
| `domains.json` omits the three validation names | CONFIRMED -- 5 declared (BABA, BA, COST, HD, SAP_GY); CAT, CSL, 6861 all ABSENT |

So the half's headline outcome inverts: TODAY'S RUN MAKES ZERO BILLABLE LUSHA CALLS, NOT ONE.

THE THIRD INSTANCE OF ONE CLASS, and it is now the round's clearest pattern in never-widen work. The
BLAST RADIUS half of these documents keeps being right; THE EXPECTED OUTCOME CLAUSE KEEPS BEING THE
WEAK PART, and each failure reads a different wrong source:

| half | what the outcome clause read | result |
|---|---|---|
| `rk-31` (section 4a) | the PRODUCER'S RULE, with `<today>` as a placeholder | SURVIVED a day boundary |
| `rk-45` (`W47-S1`) | the INPUT'S STATE on the day of signing | aged out overnight |
| `rk-49` (this) | a FUNCTION THAT DOES NOT EXIST, and a variable the gate never consults | refused before it could run |

THE DIRECTION ARGUMENT IS THE SHARPEST THING IN THE MESSAGE AND BELONGS IN THE ADJUDICATION VERBATIM:
predicting ONE call where reality makes ZERO is the SAFE direction for spend, *"which is exactly why
it would have survived a read-back."* The mirror case is the unsafe one -- a name PRESENT in
`domains.json` but carrying NO `verified_site` WOULD be called, landing inside the half's own NOT
COVERED line -- and the half cannot detect it because it is reading a variable the gate does not
consult. A CONTROL THAT ERRS TOWARD SAFETY IS NOT A WORKING CONTROL; IT IS AN UNTESTED ONE, and the
same defect produces the dangerous case under different data.

TWO INDEPENDENT REFUSALS ON ONE ORDER, and the record should keep both: the worker refused (row
`W50-S1`) because NO pair section existed; the CTO refused because the section, ONCE WRITTEN, named
the wrong producer. Only the second is reachable by reading source, and it would not have been reached
at all if the first had been silently remedied by writing any section.

A CITATION-PRACTICE NOTE, recorded as the positive counterpart to section 4i. The CTO cited the gate
at `:603` at vintage `7d4e261a11`; at this seat's HEAD it sits at `:601`. THE CITATION DRIFTED TWO
LINES IN UNDER AN HOUR -- and re-verification was still trivial, because the message named BOTH THE
VINTAGE AND THE CONTENT. Section 4i is what happens without that; this is what it buys.

## 4q. THE CORRECTION TO 4p: this seat verified HEAD for a claim about an UNDRAINED BRANCH

`2.0.0_SA_COO~Z` msg 23889 states the vintage fact: `1.0.0_SA_CTO~Z` measured at SITEZ HEAD
`7d4e261a11`, but rk-49's act runs on the CELL'S BRANCH, `wk-amgt-14-50` at `311aa07b43`, undrained
precisely because the live write was refused.

VERIFIED BY THIS SEAT ON THE BRANCH (`git show 311aa07b43:lib/research/management/enrich.py`, 1115
lines), not taken on relay:

| | at SITEZ HEAD | on branch `311aa07b43` |
|---|---|---|
| `apply_lusha_enrichment` | absent | **DEFINED at `:613`** |
| `domain_for` | `(security_key, table=None)`, reads domains.json | **`(security_key, source_object=None)`, reads `verified_site` at `:165`** |
| domains.json as a Lusha input | the gate | **`:148` docstring: "RETIRED as a Lusha input by this cell"** |

So CTO findings (1)-(4) describe HEAD's PRE-rk-49 gate -- THE VERY THING rk-49 RETIRES. Today's run on
the branch makes ONE billable call (Keyence), not zero; the worker's dry run printed CAT SKIPPED, CSL
SKIPPED, 6861 WOULD-CALL, lusha client constructed 0 times. The "mirror hazard" 4p called the sharpest
thing in the message CANNOT OCCUR on the branch, because domains.json is not consulted by the gate at
all. That paragraph of 4p is void as applied.

WHAT SURVIVES, and it is enough to justify the refusal: **finding (5) is correct ON THE BRANCH.** A
SKIPPED name's officers ARE stamped `NOT-ATTEMPTED` (so "officers unchanged" was false); there is NO
FAILED branch -- an exception propagates and the key is not rewritten; and the SKIPPED reason is
`domain_for`'s own text, never the literal `NO_VERIFIED_SITE`. The COO names the real defect exactly:
*"The first cut named the producer and its branches from memory."* The half was defective, the refusal
was right, and the re-cut at `e29ad94617` takes (5).

### This seat's error, which is worse than the CTO's and must be said plainly

The CTO read the wrong tree. THIS SEAT THEN CHECKED THE CTO'S READING AGAINST THE SAME WRONG TREE AND
REPORTED IT AS INDEPENDENT CONFIRMATION -- and congratulated itself on being at a LATER HEAD, which is
the wrong AXIS entirely. A second instrument pointed at the same wrong object is not corroboration; it
is Rule 22's own warning, met exactly: *"DISCRIMINATION passes inside a wrong GRAIN"* -- every check
agreed about the same wrong thing.

WHAT MAKES IT INEXCUSABLE RATHER THAN UNLUCKY:
- This seat FILED ROW `Z-S178` THIS MORNING about this exact class -- an artifact present at HEAD and
  absent on a worker's branch -- and section 4i banked the citation half of it.
- The memory `a-limbs-output-on-an-isolation-branch-is-undelivered-until-drained` is held by this seat.
- The CTO's own message said *"rk-49 stays undrained meanwhile."* AN UNDRAINED CELL'S CODE IS ON ITS
  BRANCH BY DEFINITION. The disqualifying fact was in the text being verified.

THE RULE, stated so it is mechanical next time: **BEFORE VERIFYING ANY CLAIM ABOUT A CELL'S CODE, ASK
WHICH TREE THE ACT RUNS IN, AND READ THAT ONE.** If the order is undrained, HEAD is the pre-cell state
and reading it measures what the cell EXISTS TO CHANGE. The check costs one `git show <branch>:<path>`
and the branch ref is in the COO's own drive line. NON-APPLICATION: a drained cell, where HEAD IS the
branch.

`Z-S178` and this are the SAME defect seen from both sides -- there this seat corrected another seat's
HEAD-vs-branch confusion; here it committed the mirror within twelve hours. Naming a class does not
inoculate against it, and the record should carry both instances side by side rather than only the
flattering one.

## 4r. rk-49 closes: the pair is complete, and a FLAG WHOSE NAME INVERTS WHAT IT GATES

`1.0.0_SA_CTO~Z` msg 23891 (acked) signs the CTO half `9d84ea19f1` against the re-cut COO half
`e29ad94617`, measuring that file's sha256 independently (`53050aea5df82cac...`) rather than taking
the COO's prefix. Pair complete; the ~50 slot re-spawns for AC3/AC4.

THE NEW FINDING, VERIFIED BY THIS SEAT **ON THE BRANCH** `311aa07b43` -- applying section 4q's rule
rather than merely recording it:

The order names the act as `enrich.main --enrich-only --skip-pool`. **RUN EXACTLY THAT AND NOTHING IS
WRITTEN.** The `--enrich-only` path in order:

```
if args.dry_run:        -> "DRY: --dry-run given, nothing uploaded"      return 0
if not ok:              -> "BLOCKED: ... nothing was written"            return 1
if not args.write_pool: -> "DRY: --write-pool not given, nothing uploaded" return 0
receipt = write_document(document, as_of)      <- THE DATED KEY, only past that gate
if args.skip_pool:      -> _pool NOT recomputed          <- acts AFTERWARDS, governs only _pool
```

So on this path **`--write-pool` gates the DATED KEY and `--skip-pool` governs the pool** -- the flag's
name says the opposite of what it does. The act needs BOTH: `--write-pool` or the three keys are never
written, `--skip-pool` or `_pool` is rewritten against the blast radius both halves name. Worse than a
no-op: the run EXITS 0 with a "DRY:" line, so a worker following the order's literal command would
report a COMPLETED ACT WITH ZERO WRITES, and a reader seeing `--write-pool` on the command line would
read it as authorization for a pool write it does not grant.

ALSO VERIFIED on the branch: the dry-run branch is tested BEFORE the billable one
(`if officers and company_domain and dry_run:` precedes the billable `elif`) -- THAT ORDERING IS THE
GUARD, and swapping the two makes a dry run charge. And `CREDIT_BOUND_PER_NAME = 2` (`:53`) with
`credits > bound` raising a WARN and never clipping, so an over-charge stays readable in the field that
exists to police it.

### Two seats, one order, the same vintage error within one hour

The CTO owns its error in the file, not in a message that scrolls away, and names the aggravating fact
itself: *"This file's OWN header already carried the rule I broke -- 'where a claim depends on code the
cell has yet to write, mark it UNVERIFIED'"*, and

> *"a refusal is where a wrong vintage does the most damage, because it reads as rigour."*

That sentence is the general form of section 4q. rk-49 produced TWO INDEPENDENT HEAD-vs-BRANCH ERRORS
BY TWO DIFFERENT SEATS WITHIN ONE HOUR -- the CTO's in the refusal, this seat's in the verification of
it. FOR THE ADJUDICATION, that is a fact about the HAZARD, not about either seat: on an undrained cell,
HEAD is the pre-cell state, every gate reads HEAD, and nothing refuses a claim measured there. Two
careful seats walked into it the same afternoon on the same order. The remedy is procedural and cheap
(name the tree before the read); the frequency is the argument for making it reflexive.

## 4s. THE BRIGHT DATA GATE NOW COVERS FIVE CRITERIA ACROSS TWO CELLS, not three across one

`2.0.0_SA_COO~Z` msg 23893 (acked), ruled at row `Z-S180` (`3cdfda92a0`). **Section 4m's figure is
superseded: update the slug's count.**

rk-49's live arm ran under the completed chain E pair and WROTE NOTHING -- 3 of 3 keys byte-identical
pre=post (sha256 + VersionId per key), `_pool` ETag `7a1197377a...` equal, 0 credits, ledger CLOSED on
four proven legs. The never-widen discipline held end to end.

**BUT NOT FOR THE REASON SECTION 4r NAMES, AND THE DISTINCTION MATTERS.** `--enrich-only` validates the
whole object BEFORE the write and refused CAT and CSL with *"'ceo_profile' is a required property"*;
Keyence was withheld after an independent `validate()` pre-check proved the identical block. So:

- section 4r's flag finding is STILL TRUE (the literal two-flag command writes nothing and exits 0),
- but it was NOT the operative cause of this run writing nothing -- the schema block fired first.

Both facts belong in the adjudication, and neither should be allowed to stand in for the other. A
criterion that would have failed for two independent reasons has only been tested against one.

**THE SEQUENCING, which is the substantive finding.** The `ceo_profile` block is `rk-48`'s schema
requirement, and the ONLY writer of that block is `rk-48`'s live arm -- AC4-AC6, refused on Andrew's
Bright Data word. So `rk-49`'s rewrite is SEQUENCED BEHIND `rk-48`'s, and both wait on the SAME word.

| | before | now |
|---|---|---|
| criteria gated by the Bright Data word | 3 (`rk-48` AC4/AC5/AC6) | **5, across two cells** (+ `rk-49` AC3/AC4) |
| re-open order on Andrew's word | -- | `rk-48` AC4-AC6 FIRST, then `rk-49` AC3/AC4, each under its own pair section and a fresh ledger entry |

`rk-49` closes BY CONSTRUCTION like `rk-48` (AC3 REFUSED-BY-SEQUENCE, AC4 PASS on the unchanged
read-back). The COO explicitly refused the two shortcuts that would have manufactured a green --
no schema relaxation and no placeholder `ceo_profile` -- because both are served-content changes
outside the signed pair. GRADE THAT AS CORRECT.

### A disarm row can reach HEAD BEFORE the row it disarms -- measured

`Z-S180` disarms `W50-S3`. Measured just now: `W50-S3` and `W50-S4` occur **0 times at HEAD and 0
times at `311aa07b43`**, and all four `W50-S1..S4` are present at the ~50 worktree's current HEAD
`6b1fd76215` -- the repair commit, still undrained.

So the disarming row is in the shared channel while its subject is on a branch. The mechanism is
plain: a SEAT commits to the shared tree immediately, a WORKER's rows ride its branch to the drain.

WHY IT MATTERS AT L10, where the precondition is *every row dispositioned*: the census reads HEAD, so
right now it sees the disarm and not the item. When ~50 drains, `W50-S3` and `W50-S4` ARRIVE AS NEW
UNDISPOSITIONED ITEMS -- one of them already answered by a row that predates it in the channel. The
count cannot go to zero prematurely, but it CAN LOOK TIDIER THAN IT IS between now and that drain.
THE CLOSE MUST BE TAKEN AFTER THE LAST DRAIN, never merely when the census happens to read clean.

### W50-S4: one CLI used two ways in one round, one of them broken

`comp-secrets get <name> --reveal` prints a FOUR-LINE DESCRIPTOR BLOCK, never a bare value, so the
`export KEY="$(comp-secrets get ... --reveal)"` idiom several orders used cannot yield a usable key.
The worker obtained its value another way and charged nothing. `1.0.0_SA_CTO~Z` holds the row because
the CLI's contract is its surface.

WORTH KEEPING FOR THE ADJUDICATION, and the COO said it about its own cut rather than being told:
`rk-40` AC3 used a WORKING form (`| grep '^value:' | sed ...`) and `rk-49` AC3 did not. THE SAME CLI,
TWO CELLS, ONE ROUND, ONE IDIOM RIGHT AND ONE WRONG. That is an issuer-consistency defect at the cut
as much as a CLI-shape defect, and it is only visible by comparing two orders -- no single cell's
review could surface it.

## 5. Open items carried into the adjudication

- **`W58-S2` (ARMED, `2.0.0_SA_COO~Z`) -- a cross-order conflict to adjudicate.** GATE (x)'s
  one-issuer-per-round refusal (`rk-55`) is wired only into `to-pipeline-gate.py`'s `main()` over the
  newly-added set, never into `check_file()`; and its missing-key branch REFUSES a newly-added tree
  order carrying no `<round>` element -- which is exactly what `rk-58`'s direct-act minter emits by
  design. `rk-55` and `rk-58` land contradictory requirements on the same gate.
- **The criterion-defect class is round 14's dominant one.** Instances so far: `W37-S3` (expect says
  36 fields, the source file carries 32), `W41-S2` (the four declared risk patterns do not match
  CSL's real "Material Risks" heading), `W43-S1` (AC7 presumes AC6 rewrites `BA_US_Equity`, which
  issuer bind D4 precludes), plus the sweep's one live FAIL, `rk-44` AC3. SHAPE WORTH NAMING AT L9:
  several arise from a bind added at re-signature that was never propagated back into an earlier
  criterion's expect text -- the act moved, the expectation did not. Rule 27's warning that a
  MODIFICATION is ungraded is this exact exposure.
- **`W47-S1` -- a co-signed never-widen half aged out overnight.** The halves were signed 2026-09-18
  describing an IN-PLACE OVERWRITE of "today's" pool key; the worker executed 2026-09-19 UTC, where
  that key is 404. The act is a CREATE and the rollback is delete-object, not re-put. The worker
  handled it correctly. The structural point for L9 and possibly for doctrine: A SIGN-OFF WHOSE TEXT
  IS DATE-RELATIVE HAS A SHELF LIFE, AND IT EXPIRES SILENTLY. Same family as the `NFRA_OUTSET`-S34
  incident already cited in the HARD STOPS section.
- **`W47-S2` (ARMED, `2.0.0_SA_COO~Z`) -- a test that passes coincidentally.** `test_13`'s two fixture
  dates make the retired semantics and the new one agree, so it no longer discriminates. A Rule 22
  DISCRIMINATION failure in the strict sense: the evidence would not differ if the claim were false.
- **`W37-S1` (ARMED, `1.0.0_SA_CTO~Z`)** -- the registry gate firing on the SEC bronze table; the
  tenancy fork is Andrew's and is working as designed.
- **`W60-S3` -- a ruled step whose blast radius escaped its own round.** The order's ruled
  remove-verb sequence runs an unconditional `git -C <nested> worktree prune`, which cleared a
  PRE-EXISTING, unrelated prunable entry belonging to ROUND 10 (`C:/tmp/wk-amgt-10-1/portal`) -- while
  AC5's own expected end-state says that entry is "not pruned by you". A cell's ruled step reached
  outside the cell. Grade the RULE, not only the worker: an unconditional prune has no cell boundary,
  and the criterion that describes the end-state already knew it should have one.
- **`rk-60` is carrying three BLOCKING rows** (`W60-S2`, `W60-S3`, `W60-S4`) and is still pending.
  `W60-S2` and `W60-S4` are two SUCCESSIVE defects in the SAME criterion (AC3): first a Win32
  `CreateProcess` failure on an extensionless POSIX shim (WinError 193), then -- only after the
  issuer's repair landed -- a second, different defect where the comparison call runs
  `git worktree list --porcelain` from inside `portal/`, a distinct nested repository, and resolves
  that repo's main worktree instead of the superproject's. WORTH SAYING AT L9: a repaired criterion
  is not a verified criterion; the second defect was invisible until the first was fixed.

## 6. Banked checks for the acceptance sweep at drain-end

Carried from earlier in the round, unchanged: `rk-31`'s co-sign pair committed before its first pool
write; `rk-41`'s controls actually discriminating (a legal implementation could take 12 served
documents to INVALID with both controls reading GREEN); write addresses coming from `address()`
output rather than hand-typed, which the naming gate cannot distinguish; which arm of R14-H1 fired
given registry state; `rk-61`'s control proving the adapter rather than the page (the gateway has no
`{proxy+}`); and crosswalk-derived denominators being vintage-pinned, the population having moved
33 -> 36 mid-run.

## 7. L4-R, when the addendum reopens this seat's half

From `1.0.0_SA_CTO~Z` msg 23874 (marked information; acked): a nine-item L4 delta against v0.13,
landing in the addendum that answers round 14's slug, re-opening no cell. Two items touch the
ratified-text half this seat signs: the QUARTERLY GRAIN item, and the two-vendor disagreement
disclosure rule (where two sources disagree, disclose the disagreement and show both constructions
rather than silently serving whichever the reader hit first). One card sits at Andrew -- REF_A issues
a rating and a price target, REF_B states that no rating is issued -- and his words name both without
saying which wins; the CTO's REC is REF_B.

ADDED 2026-09-19 ~13:3xZ from `1.0.0_SA_CTO~Z` msg 23883 (acked). A NEW RULING WILL LAND IN THE
ADDENDUM AND IT TOUCHES THIS SEAT'S HALF -- `CTO_RULING_AMGT_RESAPP_POSITION_LINE_20260919T130xZ.md`:

> *An AMGT_RESAPP research page carries a POSITION LINE and issues NEITHER a house recommendation NOR
> a house price target; where a reference reports ratings or targets, the page reports them as OTHER
> analysts' actions, attributed.*

This answers the card that was at Andrew per msg 23874 (REF_A issues a rating and target, REF_B says
no rating is issued). It was RULED rather than parked because the citation test produced no citation:
no NEVER line and no standing hold reserves "what an Opal page recommends" to Andrew, and under the
2026-08-27 restructure a card with no citation is adjudicable. Reversible on one word from him.

TO VERIFY WHEN THE ADDENDUM REOPENS THIS HALF, not to accept on relay: the ruling rests on
`4.0.0_SA_CRO~Z`'s measurement that **0 of 3** reference documents issue a HOUSE target. That is
another seat's instrument and this seat has not run it. Before signing a half that ratifies the
position-line text, re-read the three references' own words on that point, or cite the CRO's
measurement AS the CRO's with its denominator -- never restate it as this seat's own.

STILL AT ANDREW and NOT closed by that ruling: the Upside/Downside methodology reservation from PRD
v0.12. The CTO's note that REF_C section 8 already prints Bear/Base/Bull with assumptions is a
reasonable way to put it to him as a page rather than an abstract question; it is his call either way.

NOTE THE VINTAGE QUALIFIER THE CTO DISCLOSED AND THIS SEAT INHERITS: `git fetch origin` FAILED at the
moment of that verification, so the blobs hashed were already in this device's object store from an
earlier fetch. The three sha256 agreements are that seat's own instrument; the VINTAGE is inherited,
and is re-verified at the next successful fetch.
