# CTO RULING -- **R-OG-22 is CLOSED as a gate: the adopted remedy cannot work, because the limit is enforced AFTER the allocation**

**Seat:** `1.0.0_SA_CTO` · **2026-09-21 ~03:4xZ** · laptop · CLOUD
**Closes:** the open question at `R-OG-22` point 2 (`RULINGS_NFRA_OPLGTW_20260916.md:520-545`), carried at this
seat since 2026-09-16 and named as an open L4 question of mine in three consecutive `/self-drive` tick prompts.
**On evidence that has existed since 2026-09-20T11:05Z:** row `NFRA_OPLGTW-S57`, surfaced by `2.0.0_SA_COO~O`.

---

## 1. WHAT R-OG-22 RULED, AND WHAT IT LEFT OPEN

`R-OG-22` settled one half outright: **`job_memory_bytes` does not move** -- it is a multi-tenant ADMISSION
parameter and the export size is a single-feature contract term, so widening the shared parameter to fit one
feature re-prices every other tenant's admission. **That half stands untouched by this ruling.**

It left point 2 as a PREREQUISITE: *"BEFORE any contract number is lowered, the revision ANSWERS ONE QUESTION:
is 250,000 rows / 50 MiB a CONSUMER REQUIREMENT or an aspiration?"* -- with the reasoning that if a real
consumer needs 250k rows, **lowering the contract does not solve that consumer's problem, it relabels it.**

And it named a third branch **explicitly as an unconfirmed inference**: *"The measured evidence is more
consistent with 'the whole result set is materialised in memory' than with 'the contract is too big.' **I have
NOT confirmed that read** -- it is an inference from a ratio, and I am labelling it as one."* The ratio was
9,468,970 bytes of output against 214,065,152 bytes of peak RSS -- **about 22.6 to 1.**

## 2. THE MEASUREMENT THAT CLOSES IT -- `NFRA_OPLGTW-S57`

`2.0.0_SA_COO~O`, 2026-09-20T11:05Z, **at the source on the production path**:

> *"the export materialises the WHOLE result set -- up to THREE full-size in-memory representations at once
> (`rows`, `prepared`, `rendered`) -- and the `export_rows` LIMIT_EXCEEDED refusal is raised **AFTER** the
> allocation, not before it. So peak RSS is a function of the REQUESTED size even on requests that are
> ultimately REFUSED."*

⭐ **THE INFERENCE I LABELLED UNCONFIRMED IS CONFIRMED, AND WIDER THAN I GUESSED** -- not one materialisation
but up to three concurrent, with the ceiling enforced after the first.

## 3. ⛔ THE RULING: NO CONTRACT NUMBER IS LOWERED, ON **EITHER** ANSWER TO QUESTION 2

**The adopted rec was: lower `export_rows` / `export_utf8_bytes` to a measured-achievable pair. `S57`
falsifies that remedy's MECHANISM.**

**Because the limit is checked AFTER the allocation, lowering `export_rows` does not bound peak RSS.** A
request for 250,000 rows against a lowered cap of, say, 60,000 still **allocates for 250,000 first** and is
refused afterwards -- at the same peak RSS that caused the original `LIMIT_EXCEEDED`. ⛔ **THE LOWERED
CONTRACT WOULD HAVE CHANGED THE NUMBER IN THE SPEC AND NOT THE BEHAVIOUR ON THE HOST**, and the criterion
measuring it could well have gone green, because a conforming *test* request is small by construction.

**THEREFORE:**
1. **`job_memory_bytes` stays at 268435456.** Unchanged from `R-OG-22`.
2. ⛔ **`export_rows` / `export_utf8_bytes` are NOT lowered.** The rec is **withdrawn as a remedy** -- not
   because it was badly reasoned (it was the right move on the evidence available on 09-16) but because the
   mechanism it relies on has since been measured and does not exist.
3. ⭐ **THE REMEDY IS THE EXPORT IMPLEMENTATION, and it has TWO independent parts, either of which is worth
   doing alone:** **(a) enforce the limit BEFORE the allocation** -- a bounds check that runs after the
   allocation is not a bounds check; and **(b) stream, so peak RSS stops being a function of result-set size.**
4. **QUESTION 2 IS NO LONGER A GATE, and this does not widen `R-OG-22` -- it satisfies it.** That question was
   scoped, in its own words, to *"BEFORE any contract number is LOWERED."* **No contract number is being
   lowered, so the prerequisite is not triggered.** It survives as a SIZING INPUT to (b) -- what the streaming
   writer must comfortably serve -- and a sizing input is answered when the design is cut, not before.
   ⚠ **This is the narrow reading and I am stating it as such:** if a later seat proposes lowering a contract
   number after all, question 2 revives in full and this ruling does not excuse it.
5. **`R-OG-22` point 4 stands and now binds the streaming design instead:** the pair is **MEASURED, never
   interpolated**, and stated **with margin, never at the observed maximum.**

## 4. ⛔⛔ THE FINDING INSIDE THE FINDING, WHICH IS NOT ABOUT CAPACITY AT ALL

**A REFUSED REQUEST STILL COSTS THE FULL ALLOCATION.** That is a property of the live Gateway, it is
independent of every contract number, and it is independent of whether anyone ever lowers one: a caller can
drive peak RSS on a multi-tenant host with requests that are **rejected**, and the rejection is what the logs
will show.

⚠ **THIS IS AN EXPOSURE, NOT AN INCIDENT, AND THE DISTINCTION CARRIES DIFFERENT REMEDIES.** Nobody has
measured whether it has ever been hit. **I am NOT asserting it has been, and I am not sizing it here** --
`NFRA_OPLGTW` is out of the drive loop, its lane closed on Andrew's word at ~02:4xZ after its two acts, and
the estate is under a no-new-seats hold. **It is recorded so that the next seat to open this project meets it
as a known exposure rather than re-deriving it**, and so that remedy (a) -- check before allocate -- is
understood as closing *this* too, not only the capacity criterion.

⛔ **AND IT IS NOT A MONITOR ASK.** Standing moratorium: nothing here asks for an alert, an alarm or a
freshness check, and the remedy is a code change at the allocation site.

## 5. WHAT THIS UNBLOCKS, AND WHAT IT HONESTLY DOES NOT

- **`OG-r-2`'s re-cut no longer waits on a consumer question.** It waits on an implementation change, which is
  a different owner and a different kind of work, and it is **not scheduled by this ruling.**
- **`2.0.0_SA_COO~O` is not re-opened.** Its two acts finished at `98922`; the lane is closed and stays closed.
- ⚠ **NOTHING HERE TOUCHES THE FIVE SCHWAB TOOLS.** That chain needs `G-C`, `G-E`, and **Andrew's word**,
  because it changes what a live Gateway serves on a release the runbook itself marks as having no valid
  rollback. **Capacity was only one of the four stops `2.0.0_SA_COO~O` named, and removing one stop releases
  nothing.**

## 6. ⭐ THE KEEPABLE, AND IT IS ABOUT MY OWN RULING PRACTICE

**`R-OG-22` did the hard part right and still left the answer on the table for five days.** It hunted the
uncovered member by subtraction, found the third branch, labelled its own confidence honestly, and called the
branch *"a cheap thing to falsify."* **A seat then falsified it -- in fourteen hours, into a surprise row --
and the ruling that asked for it never read the answer**, because a ruling is a document and a row is a
different carrier, and nothing joins them.

⛔ **A RULING THAT NAMES A CHEAP FALSIFICATION HAS CREATED AN OBLIGATION ON ITSELF, AND NOTHING IN THE FABRIC
CARRIES IT BACK.** The row cited `R-OG-22` by name; the ruling could not cite the row, because the row did
not exist yet. **The arrow only points one way, and the seat that owes the re-read is the one that wrote the
ruling.** ⭐ This is the same shape as tick 2's runbook finding one level up: **the answer existed, in a
carrier the asking seat had no reason to open.**

**COST: one census of your own open questions against the surprise channel, per drive, not per tick.**
**NON-APPLICATION: a ruling that names no falsifiable inference -- there is nothing to come back for.**
