# NFRA_OPLGTW round 2 -- DRAFT package, `2.0.0_SA_COO~O`, 2026-09-18 ~23:00Z

⛔ **THIS IS A DRAFT, NOT AN ISSUANCE.** No task order here is cut, no cell is seated, and nothing in this
file authorizes a worker. Round 1 is still open (3 orders). It exists so the round-2 recut is ONE issuance
on the tick round 1 closes, per Rule 27's L10 obligation.

⚠ **THAT WARNING WAS TRUE WHEN WRITTEN AND IS NOW STALE -- ALL THREE RULINGS HAVE LANDED**, and a draft that
keeps warning about a resolved fork is as misleading as one that pre-picks a branch. Updated 2026-09-20
~11:1xZ by `2.0.0_SA_COO~O`:

| call | ruling | state |
|---|---|---|
| 1 -- export vs the job cap (`OGR2-AC4`) | **R-OG-22** | RULED, and it REFUSED THE BINARY -- see R2-a |
| 2 -- the "zero failures" bar (`OGR2-AC6`) | **R-OG-23**, **R-OG-23A**, **R-OG-23B** | RULED and CLOSED -- see R2-c |
| 3 -- the vacuous AC2 pass | **R-OG-24** | RULED -- see R2-b |

⛔ **THE FORKS BELOW ARE COLLAPSED TO THE RULED BRANCHES.** Where a ruling left a genuine question open, it is
marked OPEN AT THE CTO and named -- that is not the same as a fork this draft may choose between.

## What round 1 leaves

| item | source | state |
|---|---|---|
| Export at contract scale does not fit the job cap | `OGR2-AC4` FAIL, measured | needs a spec decision (call 1) |
| `OGR2-AC2` passes on a job 13.6 MB over the cap | row `S48`, my drain read | needs a spec decision (call 3) |
| "zero failures" bar vs episodic 5xx | rows `W2-S10` + `S49` | needs a spec decision (call 2) |
| Conditional-`UpdateItem` consume (branch 2) | `R-OG-21A`, round-1 carry | ready to cut |
| A LOGIN-PATH health check | my own 16:xxZ defect | ready to cut |
| Sentinel `"*"` + populated-roster cleanup, 8 rows frozen | round-1 carry | ready to cut |
| The 19 unexplained 5xx of 09-04/09-09/09-10 | row `S49`, NOT established | investigate, or disposition as out of scope |

## The cells, as drafted

### R2-a -- export limits reconciled with the job cap (**R-OG-22 RULED; the binary below was REFUSED**)

⛔ **READ THIS BEFORE THE TWO BRANCHES BELOW -- R-OG-22 RULED AGAINST THE FRAME, NOT JUST INSIDE IT.**
1. **`job_memory_bytes` STAYS at 268435456. Not a revision candidate.** It is a multi-tenant ADMISSION
   parameter; the export size is a single-feature contract term. Widening the shared parameter to fit one
   feature re-prices every other tenant's admission. **Settled; no revision may quietly take that route.**
2. ⭐ **THE THIRD BRANCH, which my call never named: CHANGE NEITHER NUMBER -- MAKE PEAK RSS STOP BEING A
   FUNCTION OF EXPORT SIZE.** R-OG-22 reached it by Rule 24 subtraction off a 22.6:1 ratio and LABELLED it an
   unconfirmed inference. **`S57` @`0e86a5f889` CONFIRMED IT AT THE SOURCE, and wider:** `integration.py`
   `export_query` holds up to THREE concurrent full-size representations (`:872` `rows`, `:897-903`
   `prepared`, `:904` `rendered`), and `:885` raises `LIMIT_EXCEEDED` **AFTER** `:872` has already
   materialised the set -- so an over-ceiling request pays the full memory cost and is THEN refused.
   ⚠ `S57` is a SOURCE READ, not a memory profile; it does not claim those three lines are the whole ratio.
3. ⛔ ~~**OPEN AT THE CTO:** is 250,000 a CONSUMER REQUIREMENT or an aspiration?~~ **RULED 2026-09-20 by
   msg 98499 -- 250,000 IS AN AUTHORED ENGINEERING BOUND, NOT AN ELICITED CONSUMER REQUIREMENT**, and is to be
   treated as one until a consumer record exists. Provenance: `git log --all -S'export_rows'` on the contract
   returns ONE commit, `2af252cb39`, authored by **`1.0.0_SA_CTO~A`** -- a lane of the CTO's own serial, the
   same lane ruled unseated earlier that day -- "Register D9 NFRA_OPLGTW and author its Gateway PRD", never
   modified since. ⚠ **STATUS, NOT TRUTH:** absence of a record is not absence of a consumer; what flips is
   the DEFAULT TREATMENT, not the fact.
   ⭐⭐ **AND THAT PUTS A BRANCH ON THE TABLE THAT NOBODY HAS COSTED, INCLUDING R-OG-22 ITSELF.** R-OG-22
   framed the set as "streaming is the only member that serves the requirement". **If the bound has no
   consumer behind it, the cheapest remedy is NEITHER streaming NOR re-architecture -- it is LOWERING THE
   BOUND to a figure the current in-memory path serves comfortably. A requirement must be met; an authored
   bound can be RE-AUTHORED.**
   ⛔ **THE NEW NUMBER IS NOT SET AND IS NOT THIS DRAFT'S TO SET.** The CTO carded it to Andrew on a
   **MISSING-INPUT** basis, explicitly distinguished from a reserved class: the class is adjudicable (no
   NEVER-class citation exists for an export ceiling), but a defensible ceiling needs one fact about real
   consumers that **the repository has now been measured not to contain**.
   ⭐ **AND `S59` MAKES THE FALLBACK CHEAP ENOUGH THAT THE DECISION IS LOW-STAKES EITHER WAY** -- if the
   answer is "a consumer does need 250k", the streaming branch costs a producer change and no writer change.
4. **ON THE RE-AUTHORING PATH** (now the live one per point 3), the pair is stated **WITH MARGIN, never at
   the observed maximum** (the largest completed run sat at 214065152 against a 268435456 cap), and it is
   **MEASURED, never interpolated** -- ⛔ **AND THE PRD MAY NOT BE CITED AS A CONSTRAINT ON THE PRODUCER**,
   ratified by 98499 so nobody re-cites it: `NFRA_OPLGTW_PRD.md:181` constrains ORDER, not RESIDENCY, and
   expects local export files to exist; it does not mandate the in-memory form --
   62,500 rows completing does NOT license "125,000 probably completes".

**The two branches below are kept as the original text for provenance and are SUPERSEDED by the four points
above.** Nothing in this cell is cut against them.

**Measured inputs, from `CAPACITY.json` @`0279872d7a`:** contract asks 250000 rows / 52428800 bytes; the
export peaked at `270581760` against the `268435456` cap and ended LIMIT_EXCEEDED. The largest export that
COMPLETED: 62500 rows / 9468970 bytes at `214065152` peak RSS.

- **If the CTO lowers the export limits** (my rec): the cell amends `org/standards/NFRA_OPLGTW_CONTRACT.json`
  `limits.export_rows` / `export_utf8_bytes` to a pair measured achievable, re-runs the OG-r-2 export arm at
  the NEW pair, and re-grades AC4 against it. **The new pair is the CTO's number, not mine** -- 62500 rows is
  the largest MEASURED success, not a maximum; the cell measures the interval between 62500 and 250000 rather
  than adopting the one datapoint it happens to hold.
- **If the CTO raises `job_memory_bytes` instead:** the cell re-prices admission first (R2-b), because two
  jobs at a raised cap must still fit `1936322560` minus the OS reserve. Raising the cap without that
  arithmetic is the branch I recommend against.

### R2-b -- admission arithmetic priced against real child behaviour (**R-OG-24 RULED**)

⭐ **R-OG-24 adopted the rec: the bar IS "never exceeds", so the AC2 PASS is VACUOUS, and the defect is in a
SHARED LIMB -- which makes it bigger than AC2.** AC2 becomes a DISCLOSED FAIL and joins AC4 as the second
input to R-OG-22's revision. Nothing there re-grades a criterion or moves a cap. ⛔ **The `cap_respected`
repair AND ITS CONSUMER CENSUS are named in the ruling as `2.0.0_SA_COO~O`'s to place in a cell** -- the
census is not optional trimming, it is the half that finds the OTHER criteria the shared limb contaminated.

Today's reserve: existing peak RSS x 1.25 + 134217728 = `375753728`, from a measured existing peak of
`193228800`. **The measurement `S48` adds: a child can reach `282021888`, about 1.05x the per-job cap, before
the guard ends it.** Two such children reach `564043776`. The cell re-derives the reserve from the MEASURED
overshoot rather than from the cap, and re-runs the OG-r-2 admission arm.

Independent of the ruling: the cell fixes `onhost_bench.py:418-421` so `_cap_respected` reads
`peak_child_rss_bytes` on BOTH branches and records the overshoot explicitly. **That is a measurement defect,
not a spec question, and it does not wait on anyone.**

### R2-c -- the "zero failures" bar (**R-OG-23 / 23A / 23B RULED; this cell is now CONCRETE, not forked**)

⭐ **THE BAR IS NOT WEAKENED. The literal "zero failures" stands, graded on a CONTIGUOUS window that CONTAINS
no named incident.** R-OG-23A corrected my own loose phrasing: naming an incident does NOT make its day
countable as clean -- **a named incident DISQUALIFIES any window containing it**, because the opposite reading
would let "zero failures" be satisfied over any data by naming and excising every failure, i.e. a condition
satisfiable by shrinking its own denominator, shrunk by the party that benefits.

**THE WINDOW IS DETERMINED AND NON-VACUOUS, so this cell needs no judgment call:** `S52` named all 19 (every
one a `POST /graph/cypher` 502 on the graph endpoint, two instruments agreeing, cause pinned to a graph-store
swap window outside this project's boundary). `S53` then ran the check R-OG-23A's own span assertion did not
-- a zero-failure window with ZERO TRAFFIC passes vacuously -- and measured **09-11..09-17: RequestCount
3323/1123/1142/4309/2778/5017/1781, every bucket non-zero, 19473 requests, and NO 5xx datapoint over the
identical span.** R-OG-23B ratified that the ruling had asserted the span from the failure series alone.

⭐ **SO THE CELL IS: re-grade AC6 on 09-11..09-17 with the literal bar intact, and record the incident
register the bar reads from.** ⛔ **AND IT PRINTS TWO NUMBERS, NEVER ONE** -- the failure count AND the
traffic denominator that makes a zero mean something. That is `S53`'s carry and it is the whole reason this
window survives scrutiny.

`S49` establishes the shape: four non-zero days of fifteen, eleven true zeros, ELB-side 5xx absent entirely,
and today's two attributable to our own DeleteItem outage. My revised rec is to keep the literal zero and
grade on a window free of NAMED incidents. The cell implements whichever bar the CTO rules, and in EITHER
branch it records the incident register the bar reads from.

### R2-d -- conditional-`UpdateItem` consume (branch 2), ready

`oauth_as.py:649`/`:772` consume by conditional DELETE, which is why the runtime role needed `DeleteItem`.
Branch 2 marks `consumed_at` by conditional `UpdateItem` instead and lets the grant narrow again. The cell
carries the R-OG-21A record, re-runs OG-a-1's durable tests, and exercises the login path end to end AFTER
the grant narrows -- **the narrowing is the act that can break login, so its acceptance is a real login, never
a test double.** Ordering: after R2-e, so a broken login is detected by a monitor rather than by Andrew.

### R2-e -- a LOGIN-PATH health check, ready, and it is mine to own as a defect

**`/health` 200 + `/mcp` 401 + ALB healthy was GREEN for the entire 10h35m outage**, and on that reading I
told Andrew the gateway was "up and healthy" while no one could sign in. The cell builds a check that
exercises the login PATH -- register, authorize, callback, token -- against a synthetic principal, and fails
when the sequence fails.
⚠ **The standing moratorium (CLAUDE.md: never build an alert/monitor unless Andrew explicitly asks) binds
this cell.** It is drafted as a CHECK whose result lands in an existing gate or an owned blocking item, NOT
as an alarm, an SNS topic or a notification. **If the cell cannot be built without a notification surface, it
becomes a card for Andrew and stays uncut.**

### R2-i -- contract-read provenance disclosure (NEW, RULED DIRECTION from msg 98487)

⭐ **RULED BY `1.0.0_SA_CTO` (98487): THE DEFAULTS DO NOT CHANGE AND THE READ DISCLOSES.** Fail-closed was
REFUSED as the remedy -- it is a behaviour change on a production serving path (today a contract lacking
`export_rows` serves with a sane ceiling; fail-closed would refuse) and nobody ratified that availability
change. ⭐ **And the mirroring convention is a GOOD PROPERTY, not the defect: it makes a missing key degrade
to CORRECT behaviour rather than wrong behaviour, which most defaults do not do.** The defect is PURELY
EPISTEMIC -- HELD and ABSENT are indistinguishable TO A READER while the served result is identical.

**So the cell PRESERVES the mirroring and ADDS the distinguishability**: when a contract read falls back to
its literal default, that fact is recorded at the call site so a later reader can tell which state produced
the value. Same ceiling, same refusal, same latency, same everything a consumer sees. Governing law is the
estate's own -- **a value must carry its claim, in a field a consumer can reject on**, and the consuming half
is the whole mechanism.

⛔ **NOT AN ALERT, ALARM, NOTIFICATION OR MONITOR, and the ruling says so explicitly** -- it is a provenance
field on a value the code already computes. **Wiring it to a send is a separate call and it is Andrew's.**

⭐ **FIXED ONCE AT THE PATTERN, NOT TWICE AT THE INSTANCES** (98487 adopting `S58`'s reasoning): the two known
instances (`export_rows`:845, `ticket_seconds`:790) are the same shape, and `S58`'s 24 unmeasured keys make
the instance count a **FLOOR, not a total** -- a per-instance fix would need re-running every time the census
widens; a shared read helper would not. **The cut, its shape and its timing are this lane's under Rule 27.**

### R2-j -- SIZING the email-to-`principal_key` re-key (NEW, from ruling 98508 on `S61`)

⭐ **THE DIRECTION IS ALREADY DECIDED AND THIS CELL DOES NOT RE-OPEN IT.** Ruling 98508 (carrier
`CTO_RULING_NFRA_OPLGTW_S61_..._20260920.md` @`7bf359863c`): **AUTHORIZATION KEYS ON `principal_key`, NEVER
ON `email`** -- and it is NOT a design fork, because `app/context.py:44` already DECLARED the rule on the
type itself (`email ... never an authorization key`) and the code departed from it.
⛔ **THE DISCRIMINATOR WORTH KEEPING: A DESCRIPTION OF A VIOLATION IS NOT AN AUTHORITY FOR IT.**
`config.py:233`'s SECURITY-CRITICAL marker makes that text IMPORTANT, not NORMATIVE -- it describes what the
code does; `context.py:44` declares what the field may be USED FOR.

**WHAT THE CELL DOES -- SIZING ONLY, which is the half the ruling explicitly did NOT supply** ("THE
DIRECTION FOLLOWS FROM THE CONTRACT; THE SIZING DOES NOT, and this ruling supplies only the first"):
enumerate every call site that resolves or consumes a tier, determine whether `principal_key` is AVAILABLE
at each, and state what the roster becomes (`MASTER_ADMIN_EMAILS` / `WRITE_CAPABLE_EMAILS` are email lists;
a principal-keyed roster is a different object with a different provisioning story). Known starting set from
`S61`, a FLOOR not a total: `guard.py:75`, `integrations/base.py:128`, `token_broker.py:143`, `tools.py:124`.
⚠ **`token_broker.py:143` is the one that sets the urgency** -- it feeds `_scopes_for_tier()`, so the
email-derived tier decides SCOPES MINTED INTO A TOKEN, and a token OUTLIVES the request that minted it.
⛔ **IT IS A MEASUREMENT CELL AND CUTS NO CODE.** The re-key itself is a separate cell that this one sizes.

### R2-f -- sentinel `"*"` and populated-roster cleanup, ready but VALUE-BLOCKED

The correctness half proceeds: an EMPTY roster means UNCONFIGURED and fails CLOSED, never tenant-wide.
⛔ **The VALUE half does not.** Andrew's ~18:1xZ word set the audience as "all opal employees"; his ~21:1xZ
word DEFERRED the population question, which sets priority and not the value. **So the cell ships the
fail-closed behaviour and leaves the roster value unset. No wildcard is written on a deferral.**

### R2-g -- the 19 unexplained 5xx -- ⛔ **DISCHARGED; THIS CELL NO LONGER EXISTS**

`S49` did not establish the cause of 09-04 (3), 09-09 (3) and 09-10 (13). **`S52` @`5f57597894` named all 19**
-- every one a `POST /graph/cypher` 502, one endpoint, 19 of 19, retention checked FIRST so a zero would have
meant zero; corroborated against `S49`'s CloudWatch day-buckets on an instrument sharing no mechanism; cause
pinned at the minute (`/graph/health` 200 beside `/graph/cypher` 502, retry 200 six seconds later = a swap
window on the graph store, **outside this project's boundary**). R-OG-23 s.3's naming obligation is
discharged. ⛔ **DO NOT RE-CUT THIS CELL.** Its content folded into R2-c's window determination.

### R2-h -- the export path's whole-result-set materialisation (NEW, from `S57` + `S59`)

Candidate cell, drafted only. Falsify or confirm by MEASUREMENT what `S57` established by SOURCE READ: profile
the allocation on the production export path and size the three representations against the 22.6:1 ratio, so
the streaming branch of R-OG-22 is costed rather than asserted. ⚠ **It does NOT answer R-OG-22's question 2**
(consumer requirement vs aspiration) -- that is about a consumer and stays the CTO's at L4. ⛔ **And it is a
MEASUREMENT cell, not a rewrite:** re-architecting the exporter to stream is not drafted here and is not this
lane's to choose.

⭐ **`S59` @`(this commit)` MAKES THE BRANCH MUCH CHEAPER THAN "RE-ARCHITECT THE EXPORTER", AND THE CELL MUST
BE SIZED AGAINST THE CHEAP SHAPE, NOT THE EXPENSIVE ONE:**
- `export.py:203-210` `write_csv` ALREADY consumes **row by row** (`for row in rows: writer.writerow(...)`) and
  never indexes or `len()`s its input. **If `export_query` YIELDED instead of RETURNING a list, the writer
  needs no change at all.**
- `export.py:257-264` `generate_csv` calls `export_query` at `:261` and `write_csv` at `:264` -- so the
  download route CALLS the in-memory path and then writes its result. **One path, not two**; the file write
  happens AFTER the memory cost, not instead of it. (The `:915` docstring names a second caller, which was a
  reason to CHECK for a second path, never evidence one existed.)
- ⛔ **AND THE PRD DOES NOT MANDATE THE IN-MEMORY FORM** -- kill this misreading before anyone cites it.
  `NFRA_OPLGTW_PRD.md:181` says "Generate and validate a bounded CSV completely before starting its response;
  then reauthorize and stream without buffering it on the event loop" and expects local export files to exist
  and be deleted. **That constrains ORDER, not RESIDENCY**, and the response layer already satisfies it.
- **PROVENANCE of the 250000, for R-OG-22 question 2:** `git log --all -S'export_rows'` on the contract returns
  EXACTLY ONE commit -- `2af252cb39 [1.0.0_SA_CTO~A] Register D9 NFRA_OPLGTW and author its Gateway PRD`. The
  value was AUTHORED at PRD time and never modified. ⚠ **That is not proof no consumer needs 250k** -- absence
  of a record is not absence of a consumer -- but the archive supports "authored" and holds nothing supporting
  "elicited", so the question now belongs to Andrew or a named consumer rather than to the repository.

## Fan-out, when this is cut

⚠ **RE-DERIVED TWICE ON 2026-09-20 -- at ~11:1xZ (R2-g discharged, R2-h added) and again at ~11:3xZ when
R2-i landed from ruling 98487. The count is now EIGHT: R2-a, R2-b, R2-c, R2-d, R2-e, R2-f, R2-h, R2-i.**
⭐ At the first re-derivation it came back SEVEN, unchanged from the original -- **by coincidence, since one
cell left and one arrived. A number that did not move is exactly the one to re-derive rather than carry**,
and it has now moved.

R2-d, R2-e, R2-f, R2-i and R2-j have no unmet dependency today.

⛔ **CORRECTION, 2026-09-20 ~12:1xZ, AND IT IS MINE: I WROTE "EIGHT CELLS IS AT THE CAP OF 8" AND THAT
CONFLATED TWO DIFFERENT THINGS.** The cap bounds **CHAINS (concurrent fan-out)**, never the CELL COUNT.
Rule 27: *"fan-out derived from the decomp's dependency chains and stated as `fanout:` data in the issuance
commit, default cap 8"*; `/canonical-drive` obligation 2: *"fan-out `N of M chains, cap K`"*. **N of M
CHAINS.** ⚠ I stated the wrong reading to `1.0.0_SA_CTO` in msg 98507 and it was repeated back to me in
98508, so the error had already propagated one hop before I caught it -- corrected in both places.

**CHAINS (the thing the cap actually bounds), NINE cells in SIX chains:**
| chain | cells |
|---|---|
| 1 | R2-h -> R2-a -> R2-b (the materialisation measurement feeds the bound decision feeds the reserve; **R2-h sits at the head, where R2-a used to**) |
| 2 | R2-e -> R2-d |
| 3 | R2-c (alone; R2-g, its former chain partner, is DISCHARGED) |
| 4 | R2-f (alone) |
| 5 | R2-i (alone; touches no other cell's surface) |
| 6 | R2-j (alone; a measurement, see below) |

**SIX chains against a default cap of 8 -- comfortably UNDER, and adding R2-j did not change that.** The
`fanout:` line is re-derived from the decomp at HEAD at issuance time and restated in the issuance commit;
this table is the draft's estimate, never the issuance's authority. Slot ~2 carries the benchmark cells,
having built the harness; ~6 carries nothing new until its walkthrough orders clear.

## What must be true before this is cut

1. Round 1 CLOSED -- **TWO** open orders terminal (`TO-OG-v-4`, `TO-OG-v-5`; it was three when this draft was
   written and `TO-OG-r-2` has since closed SUPERSEDED), every row dispositioned, the L10 slug delivered.
   ⛔ **LD-0521: a round-2 issuance cut before round 1's slug DEADLOCKS round 1's L10**, because the refuser
   counts open orders per project. This draft is not an exception to that and becomes an issuance only after.
2. ~~The CTO's three rulings landed, so the forks above resolve.~~ **MET 2026-09-20** -- R-OG-22, R-OG-23/23A/23B
   and R-OG-24 are all landed and the forks are collapsed above. What remains open is R-OG-22's question 2,
   which is the CTO's at L4 and gates only the CONTRACT-LOWERING branch of R2-a, not the issuance.
3. The fan-out re-derived from the decomposition at HEAD, not from this table. **Still binding** -- the
   re-derivation above is of THIS table's cells and is not a substitute for reading the decomp at HEAD.
4. ⛔ **NEW, and it is a trap rather than a condition: any pre-provisioned worktree is RE-CUT AT HEAD at
   hand-off time, never reused.** `C:/tmp/wk-oplgtw-6v4p2` is clean but PINNED at `a5714553c2`; an order whose
   inputs must exist AT HEAD cannot be graded from a worktree that predates them, and the failure looks
   exactly like a genuine absence. Same class as S54's path-vs-party distinction: the pin is a LOCATION IN
   TIME and it does not follow the order.
