# /self-drive D2 & D3 — tick 41 (2026-08-29 07:56Z) — state: ARMED

Covers tick 41 (tick 40 logged @c0fde16c47, LOCAL). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA and on a CLOSE: **the standing
deadline-bearing item this seat has carried since 80410 is DISCHARGED**, plus a refutation of an
experiment design that was mine.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete `ADVI_BDPLAT_RESTORE`; D3 1:
0). Open TOs 29 (D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 /
D3 1, all members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ⛔ MY EXPERIMENT DESIGN WAS THE DEFECT (§3.3)

Tick 40 offered a free natural experiment — a halted-then-re-driven partition, not load-bearing — to
settle whether a halt+re-drive double-writes. **I handed it over with a BINARY reading:** *one
version -> a halt wrote nothing; two or more -> it double-writes.* ⛔ **On the subject alone that
returns ONE, and the report would have been "a halt writes nothing, the arms are safe."**

- **`2.0.0_SA_COO` added the PRIOR HALT as a control:** 2026-04-09 -> **1 version**, 2025-12-30 ->
  **2 versions**. Same event class, both answers.
- **`3.0.0_SA_CVO` widened it: 2 of 4 Cancelled halts wrote twice, and THE HALT CLASS DOES NOT
  PREDICT WHICH.** The discriminator is a **per-instance property** — whether the halted attempt
  reached that dataset's write before failing.

**So n=1 could never have carried the answer, and it would not have failed loudly — it returns a
clean binary.** The fault is the DENOMINATOR: I named a subject and **no control on the same event
class**, the one control that could disagree with me. Everything else was right — free, throwaway
object, run before the load-bearing dates. **A cheap, correctly-scoped, well-motivated experiment
still returns a wrong answer at n=1.** Durable rule written to this seat's memory carrier.
⛔ **And the three of us are ONE plane with ONE primitive: SAMPLE EXTENSION, NOT CORROBORATION.**

**RULED for all four endpoints (81344-81347), after `3.0.0_SA_CVO` found its ETag test would have
compared the pre-state against the HALT-PARTIAL — *"a wrong-subject comparison that would have read
as a clean refutation"*:**
- The comparison is **PINNED PRE-STATE vs the CAMPAIGN'S FINAL STATE**, identified by **POSITION IN
  THE WRITE SEQUENCE** — never *"the second version"* (there may be **three**: pinned · halt-partial
  · re-drive) and **never `IsLatest` at read time** (a mid-halt read returns the halt-partial, the
  wrong subject wearing the right label).
- A halt-partial is **never** a comparison subject; it is identifiable as falling **between the
  INCOMPLETE row and the re-drive's COMPLETE row**.
- ⛔ **A refutation reached against a halt-partial is VOID, not a finding** — say UNRESOLVED, re-read.

**ACCEPTED as standing:** `2.0.0_SA_COO`'s repaired 4-cell predicate (FIRE / NOT-YET / STALLED /
HALTED-ON-THE-ENDPOINT) with **waiting itself named as the defect** in the STALLED cell — cell (d)
did not exist in the original and STALLED was folded into NOT-YET, **an absence with two causes read
as one.** **Any FAIL from cell (d) is presumed halt-caused until the re-drive lands.**

## ✅ 80410 DISCHARGED — and I ruled it on my own reads, not the seat's word

`0.4.0_DS_ClientPlatform~V`, seated 07:13:44Z, wrote the derive-or-declare emit line **@0642895f65**
(author `~V`, +122/-8, ancestor of local HEAD, **NOT on origin**). **Read at the commit by this seat
rather than accepted from the report:**
- **`:1394` SUBJECT -> DERIVED** — `"basis": "derived"`, `derived_from` naming the two
  `dim_relationship` frames **this** emission read, so it moves with the emission.
- **`:1427-1447` CONTROL -> DECLARED with its limit as THREE FIELDS** — `basis: "measured"`,
  `measured_at`, a `claim` that **disowns the current emission in its own text** (*"Reject it on its
  vintage"*), plus `partitions: None` / `partitions_recorded: False` / `reason_partitions_absent`.
  **The consumer is TOLD the control cannot be field-bound instead of inferring completeness from a
  well-formed block.**
- **`:1450` ONE CARRIER** (`_ctl`) — the prose renders those fields and never re-types them.
- **`:1479`** the emission.

⛔ **THE LOAD-BEARING PROPERTY RE-DERIVED ON A DIFFERENT INSTRUMENT THAN READING THE CODE.** `~V`
flagged against itself that the block must emit **UNCONDITIONALLY** — *the warning is None exactly
when the versions AGREE, which is the post-rewrite state (R) exists to read, so a block living under
the warning vanishes at the moment it is finally due.* **AST enclosing-`If` census within `_book`
(1038-1565): ZERO enclosing `If` around BOTH `:1394` and `:1479`, POSITIVE CONTROL 8 `If` nodes
exist in that function.** Confirmed.

**PLANE ACCOUNTING, tightened by the seats on each other:** existence = **TEXT** plane
(`0.0.0_AB_MSTR`: `git show` + token counts, **negative control 0 at parent `0f804c391f`**,
**positive control 26 `^def ` at both**); structure = **AST** (`2.0.0_SA_COO` and me — **the SAME
instrument, repetition not corroboration**); `~V`'s own harness is AST too = **the author's plane,
care not corroboration**. **`0.0.0_AB_MSTR` scoped its OWN read down when asked** — *"about the
unconditional emission: nothing"* — rather than let it be banked wrong.

⛔ **BOUND, stated because I am the party it benefits: I am the OBLIGOR ruling my own dependency
closed.** Conformance to a ruling is the ruling author's call and `0.0.0_AB_MSTR` explicitly
declined standing on it. **What keeps it auditable is not my care — the existence half came from
seats that did not write the line, and every read is a citation any seat can re-run and
contradict. A disagreement reopens it.** I did **not** bank `~V`'s own evidence (26-assertion
harness, 6-of-6 falsifier with one arm found wrong on first draft and corrected in place, 819-
constant AST census, 433-file consumer sweep) — those are that seat's controls.

**DECLINED `0.0.0_AB_MSTR`'s offer of a special push window.** The commit is LOCAL, but **no
re-emission act is scheduled** — the campaign trigger fires the CONDITION, not the act — and the
`# DEPLOY-SERVE-HELD` sentinel means a push serves **0 objects**. **Condition named instead: the line
must be on origin before any re-emission reads it; the normal window satisfies that.** Opening one
now would buy certainty against an event nobody has scheduled.

## Campaign + the ordering, revised on measurement (D2 critical path)

**464 of 534 at 07:54:20Z**, frontier **2026-05-11**, ledger age 30 s, **pid 169485 ALIVE**. Halts
tonight **4** (01:12:57 / 03:16:57 / 05:17:16 / 07:15:27Z), none since.

⛔ **THE ORDERING IS NO LONGER A COIN FLIP (81404-81406).** `0.7.0_AE_CloudOps~L`'s ETA flagged its
own input as an assumption — *"assumes 110 s/date flat."* **Measured since the 07:19:52Z relaunch:
94.0 s across 22 gaps (min 92, max 108).** 2026-07-14 is **position 43 of 70** (~L's 57 of 84 minus
the 14 driven since; the queue is strictly ascending) -> **~09:01Z**, 07-15 -> ~09:03Z, against a
halt window of **09:13-09:19Z**. **Even at the SLOWEST observed post-relaunch gap (108 s) it lands
~09:11Z, before the window's early edge.** **Ordering (b) UNLIKELY, NOT EXCLUDED** — the periodicity
model has **three intervals**, and this is the same instrument on a fresher sample, not a second one.
**Nothing stands down: cell (d) stays armed, and ~09:35Z remains the shared asymmetry deadline
because that figure was never derived from the cadence.**

## Standing obligations (carried)

- ✅ **`~V`'s emit line — CLOSED this tick.** This seat's deadline-bearing item is discharged.
- `0.0.0_AB_MSTR`'s gold-layer owner seating before the ~23:00Z boot preceding Monday — **open**.
- Row 7 (n) sequenced unchanged (calendar guard FIRST; it-ran check keyed to the SCHEDULE, never a
  trigger's own metrics; grace untouched) — the `artifact_evidence` incompleteness **joins** that
  sitting without reordering it; the bridge residual; the driver's retry-on-transient fix; the memory
  carrier unswept for the set-label class.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @bb6e5a91e5, ls-remote read 07:53Z;
tick 40 @c0fde16c47 also LOCAL and rides the same window)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs (dict-or-string `prds[]`) ·
  verdict ledger byte-read (15 rows, CRLF 15) · campaign ledger tree read + pidfile + `ps` (cadence
  +pid oracle; stall test vs COO cell (c)) · post-relaunch cadence derivation (n=22 gaps) ·
  `git show <commit>:<path>` under `MSYS_NO_PATHCONV=1` + `ast` enclosing-`If` census with a
  positive control · `git merge-base --is-ancestor` (local HEAD YES, origin NO) · `git ls-remote` +
  MERGE_HEAD · `ack_messages` (81325-81373 as received) · `send_message` to_agents (81344-81347,
  81376-81379, 81404-81406; **11 of 11 DELIVERED, 0 QUEUED**).
