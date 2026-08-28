# 0.4.0_DE_ClientPlatform~Z — 2026-08-28 15:30–16:00Z — TO-12-DE shipped, TO-S1-DE block CONFIRMED by my own instrument

**Archetype:** BUILD-GENERAL (render-layer removal) + a measured block confirmation.

---

## Current State

**`ETFS_POSITIONING.TO-12-DE` — COMPLETE at this seat, 5/5 AC measured.** The per-book as-of
dates no longer render under the ETFs stacked bars.

- `portal` @`27c60ecb` (dates off) + a follow-up docblock commit carrying Andrew's VERBATIM words.
- Push state, MEASURED: **LOCAL**. `git ls-remote origin DEV` reads `2858e7f5`. The push leg is
  the integrator's (LD-0367).
- Proof-of-spec instance filed:
  `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ETFS_POSITIONING.TO-12-DE_PROOF_OF_SPEC.json`
- Read before/after PNGs filed beside it under `ETFS_POSITIONING.TO-12-DE_evidence/`.

**`D1_CATVIEWS.TO-S1-DE` — NOT STARTED, and the block is REAL. I confirmed it myself rather
than accepting the face or the peer's report.**

---

## What I did, and the one number that decided the second task

**TO-12-DE.** One value: `PER_BOOK_AS_OF.etfs` `true` -> `false` (`bookSet.ts:372`). Flipped,
not deleted — the same display landed at `@46f3863e` 04:41Z and is off ~11h later; a flag is one
value from restoration, a deletion makes the return trip a rebuild.

**TO-S1-DE — THE MEASUREMENT.** The TO's face says it is blocked on `TO-M1-DS` because L2 renders
`--`. The COO's 13335 says the release condition is the L2 values rendering populated **on the
served plane, read by my own eyes** — explicitly NOT the DS lane's completion report. So I read it:

```
authenticated GET /api/general/mdpf/{firm}/category-views.json   as_of 2026-08-27
                          cottonwood   inflection   49financial   global
L2 members                    15           15            15          15     = 60
carrying an `aum` FIELD        0            0             0           0     = 0 of 60
```

⛔ **THE KEY IS ABSENT, NOT NULL.** `{"n": "Fixed Income", "served": false}` — there is no `aum`
key at all. So a suppression rule shipped today would hide **60 of 60** L2 members across every
firm. The block is not a formality; it is arithmetic.

⛔ **AND ANDREW'S OWN WORKED CASE IS UNSATISFIABLE TODAY, WHICH IS THE SHARPER FINDING.** `TS1-AC2`
requires *"Opal Fixed Income RENDERS for Cottonwood and IS ABSENT for Inflection"* — **both
directions, because an absence with no positive control proves nothing.** The positive half cannot
be produced: Cottonwood's `Fixed Income` member carries no amount either. Worse for the premise,
both firms carry the **same four** unmapped Custom members, and Inflection's `Custom` L1 is
**$43.47M against Cottonwood's $8.43M**. Nothing in today's artifact distinguishes the two firms
at L2 in the direction his example assumes. **That is a question for the producer TO, not
something a render change can reach.**

---

## Compiler Tools

`comp-which` exercised at startup (A.3): **105 of 105** comp-tools resolve bare, and one RAN
(produced its own banner) — resolution is not execution, so the exercise half is the one that counts.
For the work itself I used native `Grep`/`Read`: the question was "how many places render a date in
this panel", a text-local census where the answer IS the denominator (1 of 1 `DataAsOf` usage), and
that 1-of-1 is what licensed a one-value change instead of a hunt.

---

## Controls I ran, and the one that caught something

| control | result |
|---|---|
| typecheck mutant | `etfs: 'MUTANT_NOT_A_BOOLEAN'` -> **rc=2, TS2322 at bookSet.ts(372,3)** — the exact line this diff edits. The instrument fails on this change's own subject. Reverted; rc=0. |
| two instruments on AC1 | READ screenshot **and** region-scoped DOM count. They fail differently (CSS-hidden text vs canvas-drawn text). Both: 4 before, 0 after. |
| commit verified from the REPOSITORY | `git log -1` on the hash, with a bogus-hash negative control that failed. safe-commit's own text warns that grepping its stdout returns PASS on a FAILED commit. |
| **`grep -n '^  etfs:'`** | **9 hits — and line 155 is ALSO `  etfs: true,` in a DIFFERENT Record.** A `replace_all` on that literal would have silently flipped an unrelated capability. Caught because a scripted revert asserted `count==1` and got **2**; I reverted via `git checkout --` from the commit instead of a text substitution. |

---

## Blockers

**None at this seat.** `TO-S1-DE` is blocked on `TO-M1-DS`, which is DS-class, actively worked by
`0.4.0_DS_ClientPlatform~Z`, and **not mine**. The producer writes once daily at 13:50:50Z, so the
release condition cannot be met before tomorrow's write regardless of when M1 lands.

---

## Next Steps

- [`2.0.0_SA_COO~Z`] **BLOCKING-CLASS, and it is the issuer's call, not mine:** `TO-12-DE` as cut
  **cannot produce a VALID proof-of-spec instance.** `proof-of-spec-check.py` enters alignment
  ENFORCE on the mere **presence** of a `<decomp_ref>` element; TO-12-DE carries one whose *text*
  says *"NO CELL ADDED AND NONE CLAIMED"*. Its five criteria therefore carry no `cell_refs`, and
  the checker refuses all five — *"never retrofitted: a derived cell_ref makes alignment LOOK
  satisfied while being FALSE."* **The trigger is the tag; the disclaimer is the prose inside it.**
  I did not invent five cell_refs to clear it. Remedy is (a) drop the `<decomp_ref>` element, or
  (b) name the cells. The five acceptance rows PASS independently on their own evidence.
- [`3.0.0_SA_CVO~Z`] Certification of `TO-12-DE`. Look first at **AC3** — I recorded a 14px upward
  reflow of everything below the removed line rather than claiming "nothing moved", and at **AC2**,
  where I state the empty diff is known BY CONSTRUCTION and explicitly decline to present one read
  as a before/after pair.
- [`0.4.0_DS_ClientPlatform~Z` / issuer] The `TS1-AC2` premise problem above — his worked case may
  not be expressible in the artifact's current shape. Surfaced, not chased.
- [integrator] Both portal commits await the push leg.
