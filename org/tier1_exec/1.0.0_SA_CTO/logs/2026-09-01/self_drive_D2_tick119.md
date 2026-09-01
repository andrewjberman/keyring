# /self-drive D2 — tick 119

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~14:2xZ
**Ticks covered:** 119 · **Carrier:** `org/XXX.md:633` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO`

```
COMPLETION: 2 of 10 -> NOT DONE      ledger: 37      open_tos: 17
OPEN CALLS: 0 pitched -- the tick was spent WITHDRAWING a claim this seat amplified
```

---

## The tick's content: I amplified a claim that was retracted four minutes after it was made

`3.0.0_SA_CVO` 91764 asserted the empty `asof` **was** the 6-to-0. I wrote the same sentence on its
evidence at 91768 and carried it to Andrew as **root cause found**. That seat retracted at 91799.

**Confirmed by my own read**, from the chain log already sitting on my disk:

```
  CHAIN START date=2026-08-31 mode=production stages=17    <- NOT EMPTY
  prev_dim:   date=2026-08-28, 8,633 rows
```

- The empty `asof` belongs to an **11:06Z manual publish of SEVEN keys** (the never-widen explicit
  `--keys` list — readable off the row count).
- The 6-to-0 is **the CHAIN, ELEVEN families, on a REAL date.**
- **Two invocations.** The empty `asof` fully explains the seven-key publish and **is not established
  as the cause of the regression.**

⛔ **I also used the words "ROOT CAUSE", which Rule 22 RESERVES for STATE at EXERCISED.** I had a
manifest field and an inference. That word should not have left this seat.

## ⛔⛔ AND THE FALSIFIER WAS IN MY OWN HANDS FOR FORTY MINUTES

I downloaded `chain_20260901T094639Z.log` at ~14:0xZ and grepped it for
`perfrp_projection|REFUS|BUILT|would_publish|reason`. **I never grepped it for `date=`. The line that
refutes the empty-date story is the FIRST LINE OF THE FILE.**

>> **Twenty minutes earlier I wrote the memory rule against exactly this** — *an output answers the
   question you brought to it; RE-READ YOUR OWN PRIOR OUTPUT WHEN THE QUESTION CHANGES.* The question
   changed from *why do they refuse* to *what date did it get*, the artifact was on disk, and I did
   not re-read it. **WRITING A RULE IS NOT INSTALLING IT.** <<

That is the third instance of this class today and **the first one where the rule already existed.**

## ⭐ One positive result from the same read, which nobody had stated

```
  prev_dim: date=2026-08-28    <- FRIDAY, resolved for a MONDAY run
```

**The chain's trading-calendar handling is CORRECT on the exact boundary that would have broken it.**
That closes the Monday/weekend hypothesis **at the chain level as a MEASURED CLEARANCE**, where tick
118's `comp-find` could only establish that the BMV string lived in `c04`. An absence of evidence
became evidence of correctness.

## Where the question now sits (not mine to place)

`3.0.0_SA_CVO` 91842 verified the same-binding claim through the CALL SITE: `main()` prints `date`
and passes the same local into `_run_perfrp_projection`, so **`--asof 2026-08-31` DID reach the
publisher.** The retraction stands as correct.

⭐ **And that verification carries its own instrument lesson worth keeping:** that seat first grepped
for reassignments of `date` between the two line numbers, found three, and nearly reported the
opposite — **because `:365` executes LATER, inside a function called at `:540`. A line-number range
assumes linear execution, and a function body is not linear with its caller.**

**NEW LEADING CANDIDATE, stated by CVO as a HYPOTHESIS and not a finding:** the chain passes
`--staging-root`; the in-process reproduction that built 9 did not. **That is the uncontrolled
variable between B and A.**

⚠ **Standing instruction to `2.0.0_SA_COO` repeated here because it is the expensive one:** DO NOT
SCOPE ONE REMEDY on either the empty-`asof` sentence or mine. A remedy scoped to the empty `asof`
would fix the seven-key publish, leave the 6-to-0 untouched, **and show a closed finding in the
ledger.**

## Also this tick — `comp-schedule`, at Andrew's pointer

Ran the gate ledger. **19 gates armed; 135 project `blocking` fields carrying prose it refuses to
count.** Both DRIFT CANDIDATES were `owner=CTO` and I settled both: **NEITHER IS DRIFT.**

- **G-4 CORRECTLY ARMED** — two conditions, only the first satisfied; the second is a live halt whose
  own text reads *"LIFTING THIS SENTINEL IS ITSELF THE DEPLOY. Do not remove it to 'unblock'
  anything."* **Acting on the candidate would have performed the deploy the sentinel exists to
  prevent.** The author wrote the countermeasure into the artifact, aimed at a reader who sees
  SATISFIED and reaches for it. **That reader was me.**
- **G-3 FALSE POSITIVE** — it is G-4 counted twice, through `comp-schedule`'s **own build log**
  quoting the sentinel. The tool excludes `org/mcp/inbox` (*"agents quoting a sentinel are not a
  sentinel"*) but not agent LOGS. ⛔ **The tool's own build log is now an input to the tool** — every
  logged run adds sentinel-shaped text to the next run's corpus. Monotonic. Routed to CVO at 91830.
- **Not settled, and named:** G-1, `owner=CTO`, **last-verified 2026-07-12 — 51 days.** Exactly the
  class Andrew commissioned the tool for. G-4 is the standing warning against assuming it is stale.

## RESERVED cards still at Andrew

- D3's order relative to D8 · whether the flow-ingestion defect widens the ruled 22.
- The PERFRP publish card, ONE card TWO limbs: (a) did 08:5xZ narrow the 04:0xZ ratification;
  (b) PER-FAMILY or PER-SET (per-set is unsatisfiable by construction).

## Compiler Tools

`directives-check.py --json` + completion scan (denominators printed) · **re-read** of
`chain_20260901T094639Z.log` for `date=` (the read tick 118 should have done) · `.tools/comp-schedule`
· direct source read of `convert_transactions_to_silver.py:94-125` · `git ls-remote`. No `head` on any
census.

**PUSH STATE, MEASURED:** `72322d7f9c`, `a21267939d`, `4022ebae4a`, this log LOCAL.
`origin/CLOUD` = `c85701ebca` (fetch 13:4xZ) — perishable.

**State:** `ARMED` · next tick on the cron.
