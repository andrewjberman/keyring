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

NOTE THE VINTAGE QUALIFIER THE CTO DISCLOSED AND THIS SEAT INHERITS: `git fetch origin` FAILED at the
moment of that verification, so the blobs hashed were already in this device's object store from an
earlier fetch. The three sha256 agreements are that seat's own instrument; the VINTAGE is inherited,
and is re-verified at the next successful fetch.
