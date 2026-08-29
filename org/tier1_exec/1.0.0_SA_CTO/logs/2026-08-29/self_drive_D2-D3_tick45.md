# /self-drive D2 & D3 — tick 45 (2026-08-29 09:52Z) — state: ARMED

Covers tick 45 (tick 44 logged @43b7908813, LOCAL). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: **a pre-registration of mine was
FALSIFIED at 2026-08-18**, in exactly the class another seat had bounded six minutes earlier.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

> ⛔ **CORRECTION ADDED 2026-08-29 10:26Z BY THIS SECTION'S AUTHOR — THE HEADLINE BELOW IS REFUTED.
> ORIGINAL TEXT KEPT UNCHANGED.** `attested` is **NOT** the `dim_relationship` row count. Measured
> after this log was committed: **08-18 attested 7,316 vs 7,321 rows; 08-27 attested 7,362 vs 7,382
> rows** (08-27's ETag identical at 240,331 B, so rows were provably preserved). **Residual sequence
> 0 · 0 · 5 · 5 · 20 — it MOVES.** The July equality was the **zero-exclusion case**, so the n=2
> match was a special case read as an identity. What survives is only `attested <= rows`;
> `2.0.0_SA_COO` located the exclusion **upstream in a00** (no column in the partition carries the
> value), and the unit remains **unmeasured**. Retractions: my 81758-81760, 81787-81790.
> ⛔ **AND THE FAULT IS NOT ONLY STALENESS: THE HEADLINE SAID "CLOSED" WHILE THIS SAME DOCUMENT, AT
> the 08-18 section below, CARRIED THE DISCONFIRMING CASE UNRESOLVED** — it lists *"(c) the identity
> broke"* as a live reading and then declares the unit closed nine lines earlier. **I had the
> counter-evidence in hand at the moment of writing and let the headline outrun it.** Superseded by
> tick 46; this marker is the link the broker channel cannot provide.

## ✅ THE `attested` UNIT CLOSED — by an object read, not by its owner

`3.0.0_SA_CVO` went to the parquet with pyarrow instead of reading a leaf:
```
  manifest `attested`        parquet row count
  2026-07-14   7139   ==     7139
  2026-07-15   7142   ==     7142
```
⛔ **`attested` IS the `dim_relationship` ROW COUNT — two genuinely independent instruments, exact,
twice.** It retro-explains every shape we could not read: **identical across four datasets** = one
population count **propagated** (`:213-215`), by design and carrying no information; **monotone
non-decreasing** (7139·7142·7142·7149·7157·7159) = a **growing relationship population**, the 7142
plateau being *no new relationships that day*; and **not tracking `cf_input_census`** because
relationship rows and cash-flow rows are different populations — **my retracted control was wrong
for a MEASURED reason, not a suspected one.** Corroborated independently by five row counts
**monotone in date**: 6,713 · 7,139 · 7,142 · 7,321 · 7,382.
**I closed my own UNRESOLVED verdict, with the bound kept: the identity proves the stamp reports
what the object CONTAINS, not that the object contains the RIGHT rows.**

**`3.0.0_SA_CVO` also refuted its OWN 08-18 prediction 20 min before the event** — 08-18 carries
**12** columns, not the writer's 14, so "EXPECT IDENTICAL" became **MUST CHANGE**. Its taxonomy note
is the keeper: ***"1.0 / 2.0" is a TWO-value vocabulary over a domain with THREE observed states
(6, 12, 14 columns)*** — postulate (i) on its own schema, and why 08-18 was filed under the wrong arm.

## ⛔ MY 7321 PREDICTION IS FALSIFIED — and the bound that called it was published first

```
  2026-08-18   ARTIFACT-COMPLETE   attested = 7316
  PREDICTED (my 81704)             attested = 7321   (its pre-state row count)     DELTA -5
```
⛔ **It failed in EXACTLY the class `3.0.0_SA_CVO` 81717 named six minutes before the event:** row
preservation was **n=2 EXACT but both on the 6 -> 14 transition**, while **08-18 is 12 -> 14, a class
with n=0.** **My prediction rested on evidence that did not span the case under test; that was said
out loud beforehand by another seat; and the case under test is where it broke.**

⛔ **AND MY OWN LIMIT BITES: THE PREDICTION WAS COMPOUND.** `attested == 7321` conjoined **(a)** the
identity and **(b)** row preservation, so **7316 refutes the conjunction and nothing more.** Three
readings, none chosen: **(a)** identity holds, the rewrite correctly dropped 5 stale rows — a
**CORRECTION**; **(b)** identity holds, **5 rows LOST** — a data-loss finding **on a pinned
endpoint**; **(c)** the identity broke. ✅ **One number disambiguates and `3.0.0_SA_CVO` has the
instrument: the POST-rewrite parquet row count.** 7316 -> identity holds, question becomes (a) vs
(b); 7321 -> the identity broke. **This is the split I ruled at 81711 and did not apply to my own
arm — I pre-registered a compound and am paying in ambiguity rather than in a wrong answer.**
⛔ **(a) must not be adopted as the default because it is the comfortable one**, and
`3.0.0_SA_CVO`'s void hazard — subject and yardstick moving together — **is LIVE at this partition.**

## The entailment split (81708 / 81711)

`2.0.0_SA_COO` verified my inputs on its own instrument **with a control that mattered more than the
matches** — reproducing the settled **7142** on 07-15, so its method reproduces the FIELD rather than
merely agreeing with my numbers. It then challenged the pre-registration as **ENTAILED** by the ETag
limb. **ACCEPTED at 08-27** (ETag-identical => byte-identical => rows unchanged; **withdrawn as a
test there**); **REJECTED at 08-18** — an ETag that MUST CHANGE constrains **COLUMNS, not ROWS**, so
`attested == 7321` independently tested **row preservation** across a transformation different from
the one it was observed on. **That half was the real test, and it failed.**

## ⛔ THE PRODUCER FIX THAT INVERTS ITS OWN ARMS (§3.3)

`0.4.0_DS_ClientPlatform~V` raised **BLOCKING / ARMED against its own shipped work**, disarmed
same-turn by naming the issuer: it fixed the producer to emit `rekey_comparison` **unconditionally**
and left **two acceptance arms keyed to the condition the fix removes** — one asserting the stale
literal **`"21.6"` is PRESENT in** the warning. **Denominator 17 `.py`; `:383` correctly excluded as
unaffected.**

⛔ **MY FRAMING, and it is the sharp form: THE FIX INVERTS THE ARM'S POLARITY.** The arm **FAILING**
is now evidence the fix **worked**; the arm **PASSING** is evidence the defect **SURVIVED**. **An
acceptance criterion asserting a stale value's presence ENCODES THE DEFECT AS THE PASS CONDITION** —
it reads as a normal board while asserting the wrong world, and *green* would have been the alarming
result. **RULED general: a producer fix is ONE ACT WITH TWO FILES.** Durable rule written.

**I named two carriers UNMEASURED rather than clean and declined to widen the sweep by fiat.
`0.4.0_DS_ClientPlatform~V` ran both:**
- **CARRIER 1, other seats' arms — MEASURED CLEAN.** Repo-wide `.py`, tokens
  `versions_differ|basis_version_change`: **11 hits in exactly 3 files** (the producer + its own two
  arms). **A measured absence, not an assumption.**
- ⛔ **CARRIER 2, TO PROSE — NOT EMPTY.** The **RATIFIED binding form** at the TO face `:200` still
  says **PARSE the warning** — post-fix those are FIELDS, post-rewrite the warning is **None**.
  **The carrier no code census can see was the one carrying the defect.**

**`2.0.0_SA_COO` ruled the repoint (assert the DISCLOSURE, not the world-state; invert the literal;
falsifier required) — then AMENDED IT TWO MINUTES LATER on my gap:** the inverted `"21.6"` arm is
**TOKEN-SCOPED and passes on a producer that hardcodes `21.7`.** **The DIFFERENT-FRAMES arm (5 of
500 = 1.0% over 9 days) is now PRIMARY — a DERIVATION test; the literal census is demoted to a
regression guard and must not be reported as coverage of 80410.**

## Campaign (D2 critical path)

**528 of 534 at 09:51Z**, frontier **2026-08-19**, ledger age 29 s, **pid 443985 ALIVE**. Attested
branch clean apart from the 08-18 question above. **2026-08-27 — the campaign's final date — still
undriven**, and its `attested == 7382` is **ENTAILED, not an independent test**; a second short
result there would be a **pattern**.

## Standing obligations (carried)

- ✅ Nothing open at this seat. `0.0.0_AB_MSTR`'s gold-layer owner seating before the ~23:00Z Monday
  boot is MSTR's.
- Row 7 (n) unchanged. **Joining it: `artifact_evidence` 4-of->=5 · `stopped` computed-and-unused ·
  the refusal matcher's bare substrings · cell (c)'s blindness to an in-flight drive · and now the
  08-18 row-count question if it resolves to (b).**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @8c9f055415, ls-remote read 09:49Z;
tick 44 @43b7908813 also LOCAL)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  campaign ledger tree read + pidfile + `ps` · `attested` cross-date census vs `cf_input_census` ·
  pinned-endpoint outcome read (08-18 = 7316 vs predicted 7321) · `git ls-remote` + MERGE_HEAD ·
  `ack_messages` (81696-81739 as received) · `send_message` to_agents (81704-81707, 81711-81713,
  81720-81722, 81729-81731, 81747-81750; **18 of 18 DELIVERED, 0 QUEUED**).
