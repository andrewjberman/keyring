# /self-drive D2 — tick 118

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~14:0xZ
**Ticks covered:** 118 · **Carrier:** `org/XXX.md:633` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO` (running, tick 1)

```
COMPLETION: 2 of 10 -> NOT DONE            ledger: 36 -> 37
OPEN CALLS: 0 pitched -- the tick's call was RULED here on a peer's measurement, then CORRECTED
register open_tos: 19 -> 17
```

---

## The tick found a REGRESSION, and it followed a fix this seat RULED

`0.7.0_AE_CloudOps~M` enumerated five chain runs:

```
  09-01 12:45Z SCHEDULED    built=0  refused=11    post-fix
  09-01 09:46Z ACCELERATED  built=0  refused=11    post-fix
  08-31 / 08-28 / 08-27     built=6  refused=5     pre-fix
```

**Six families that built every day now build zero.** Not *"five leaves still absent"* — six that
worked and stopped. That seat went looking to incriminate **its own accelerator** and the test cleared
it: two triggers, three hours apart, same date, same staging, same outcome.

### What this seat added, read from the log at source

```
  EMITTER_REFUSED perfrp_activity_relationship -> -
  ... ELEVEN LINES, EVERY REASON FIELD "-"
  STAGE OK ... built=0 refused=11 (publisher rc=1; refusals are a DECLARED round-1 state, not a failure)
```

**90937's default re-applied: a refusal nobody can cite is an UNMET PRECONDITION by default.** Nothing
declares these. And the prose is falsified independently of the blank fields:

>> **THE SAME SENTENCE COVERED `built=6` FOR THREE DAYS AND NOW COVERS `built=0`. A description
   equally true of both outcomes describes neither.** It read as reassuring precisely because nothing
   could make it false. <<

### ⛔ And the net that my own grading hid

```
  pre-fix    6 BUILT  + 5 crashing
  post-fix   0 BUILT  + 11 refusing cleanly
```

**Six working families traded for tidier failure output.** I graded that fix a success on *"9 of 11
would-publish."* **The QA measurement counted refusals becoming well-formed and never counted BUILDS
LOST** — a verdict vocabulary with no seat for *worse in the dimension nobody scored*.

## ⛔⛔ Then I corrected the ruling twice, three minutes later, on `0.7.0_AE_CloudOps~M`'s 91726

```
  A  POST-FIX, IN-PROCESS   built 9   <- REFUTES "the fix broke it"
  B  POST-FIX, IN-CHAIN     built 0
  C  PRE-FIX,  IN-CHAIN     built 6   <- REFUTES "it is the invocation"
```

**It is an INTERACTION.** The fix-as-leading-hypothesis is **withdrawn**.

### The correction that matters more: MY TEST WAS BROKEN

I named *"run the FIXED emitter ad-hoc against a date that BUILT 6 pre-fix"* — pinning **the code
version and the date**, leaving **the invocation path free.**

>> **Run the obvious way — in-process — it reproduces measurement A, builds 9, and CLEARS THE FIX.**
   I would have reported the fix exonerated and the cause moved to the data, **and been wrong on a
   test I designed so the result could not be ambiguous.** <<

**I varied the axis I suspected and left the axis that actually differs unpinned.** Verification
independence is PER AXIS; an interaction is invisible to any test moving only one factor. **The test
could not have failed toward the truth.**

**CORRECTED:** run the chain **IN-CHAIN, at the PRE-FIX emitter pin, on today's date** — invocation
held constant, one factor moved. The in-process arm must not be substituted; that is measurement A.

### ROLLBACK DEFAULT: WITHDRAWN, and stated as a withdrawal

91727 s.5 pre-registered rollback. Withdrawn — a rollback does not remedy an interaction, and it would
reinstate five crash families to fix something the code demonstrably does not do alone. **Said out
loud rather than quietly dropped: a pre-registration is exactly what a lane acts on without
re-checking. That is why I wrote it, and why leaving it standing would be worse than never writing it.**

## A hypothesis that died before it was sent

The log carries `PENDING-BACKFILL bmv_rolls_from_prior_emv: requires consecutive-day valuations` a few
lines above the refusals; the manifest date is **Monday 2026-08-31**, prior trading day **Friday
08-28**. A clean Monday-shaped story — and it explained the timing too.

```
  comp-find "REFUSE-NO-BMV" --corpus all   ->  5 hits / 141,795 files scanned
  ONLY first-party hit: c04_validation_battery.py:66   -- THE VALIDATION BATTERY, NOT THE EMITTER PATH
```

⛔ **ADJACENCY IN A LOG IS NOT A CALL GRAPH.** A chain log interleaves stages. **And a hypothesis that
explains the timing too is the most dangerous kind — the extra coincidence it accounts for reads as
corroboration.** Published dead at 91752 so nobody else chases it. ⚠ It does **not** clear the trading
calendar generally; it establishes only that *this string* is not the one.

## RESERVED cards still at Andrew

- D3's order relative to D8 · whether the flow-ingestion defect widens the ruled 22.
- **The PERFRP publish card, ONE card TWO limbs:** (a) did 08:5xZ narrow the 04:0xZ ratification;
  (b) is the attached condition PER-FAMILY or PER-SET (per-set is unsatisfiable by construction).

## Compiler Tools

`directives-check.py --json` + completion scan (denominators printed) · `aws s3api list-objects-v2`
to locate the chain logs, then `s3 cp` + direct read of `chain_20260901T094639Z.log` ·
`aws scheduler get-schedule` with a fabricated-name negative control · `comp-find --corpus all` for
the REFUSE-NO-BMV census (denominator printed) · `git merge-base --is-ancestor` with a fabricated-sha
control. No `head` on any census.

**PUSH STATE, MEASURED:** `a21267939d`, `4022ebae4a`, this log LOCAL. `origin/CLOUD` = `c85701ebca`
(fetch 13:4xZ) — perishable, ages the moment an integrator runs.

**State:** `ARMED` · next tick on the cron.
