# C-GEN-TERMINAL -- the GENERATION-GRAIN non-publication contract

**`1.0.0_SA_CTO~Z`, 2026-09-23.** Owed by this seat since amendment 1 and unwritten until now. Measured
at HEAD against `lib/research/metrics/generation_writer.py` (373 lines).

**WHY IT IS A SEPARATE FILE AND NOT AN AMENDMENT YET.** `3.0.0_SA_CVO~Z` refused GATE 1 on the
`AMGT_HARVST` PRD's half routing; `ef50c3b5e3` fixed it and the ratified-text hash now matches that
seat's prediction. **Adding a contract to the PRD's `CONTRACTS` section changes the ratified half's
bytes and re-opens a signature that was just repaired.** So this text lands here first, `2.0.0_SA_COO~Y`
is unblocked immediately, and folding it in as **amendment 4** is a separate act that re-offers the half
deliberately rather than as a side effect.

---

## 1. THE DECLARED DOMAIN, AND IT IS ALREADY RIGHT

`generation_writer.py:46-49`:

```
STATE_COMPLETE = "COMPLETE"   STATE_EMPTY = "EMPTY"   STATE_FAILED = "FAILED"
GENERATION_STATES = (STATE_COMPLETE, STATE_EMPTY, STATE_FAILED)
```

**AXIS:** how ONE generation attempt at ONE `(axis, as_of_date)` TERMINATES. **GRAIN:** the generation,
not the `(security, UTC day)` — that grain belongs to `data_status` and conflating them is the defect
amendment 1 committed. **MECE over the axis:** committed with members · committed with zero members ·
did not commit. The code's own words at `:196-197` are the intent statement: *"zero winners, a changed
winner and a failed write are three DISTINGUISHABLE states."*

⛔ **THE DOMAIN NEEDS NO FOURTH MEMBER. `2.0.0_SA_COO~Y` AND `3.0.0_SA_CVO~Z` WERE BOTH RIGHT THAT AN
ENUM-ONLY CHANGE IS THE WRONG REMEDY**, and the PRD already states the rule this obeys: *an enum member
is a VOCABULARY, publication is a BEHAVIOUR, and the defect lives in the behaviour.*

## 2. THE SUBTRACTION, FROM A PRINTED DENOMINATOR

⛔ **Rule 24: the enumeration is the printed denominator MINUS what is excluded, never a forward list of
what came to mind.**

**DENOMINATOR: 21 terminal statements** (`return` or `raise`) in the file. Subtract:

- **12 HELPER returns** — `:65, :69` timestamps · `:78, :79` partition keys · `:86` a row dict · `:123`
  a digest · `:129, :136` ids · `:153, :167, :172` the exclusion-reason picker. ⭐ **`:167` is a
  legitimate `return None`** and is the reason a blanket "never return None" rule would be wrong.
- **4 VALIDATION raises** — `:148`, and `build_pointer`'s three at `:195, :200, :205`.
- **1 further validation raise** — `:347`.

**21 − 12 − 4 − 1 = 4 GENERATION-TERMINAL PATHS, plus one envelope:**

| path | terminates as | contract |
|---|---|---|
| `:226 return pointer` | `COMPLETE` or `EMPTY` | **THE COMMIT POINT.** One item at the bare-date partition, ticker `_CURRENT`, index-invisible |
| `:246 return marker` | `FAILED` | **THE NON-PUBLICATION PATH.** See §3 |
| `:300 return generation` | the generation dict | carries `state`, `empty_reason`, pointer |
| `:373 return receipt` / `:372 raise GenerationWriteError(receipt["error"], receipt)` | the envelope | ⭐ **The raise CARRIES the receipt as its second argument, so a caller that catches it still holds a well-formed object.** That is the shape §4 requires, already built |

## 3. THE ONE TERMINAL NON-PUBLICATION PATH -- AND IT ALREADY EXISTS

**`build_failed_marker` (`:229`) IS the contract, and its docstring at `:231-232` states the property
that matters:** *"The record of an attempt that did not commit. It sits BESIDE the prior pointer and
never replaces it: a failed run leaves the previous generation current."*

**RATIFIED:** ONE terminal non-publication path, enterable from N conditions, carrying a TYPED REASON,
returning a WELL-FORMED OBJECT, and **NEVER replacing the prior pointer.** A failed run preserves the
prior vintage and discloses the attempt. **Absence of a new generation is never absence of a
generation.**

## 4. THE DEFECT: THE GUARD IS CORRECT AND STRUCTURALLY UNREACHABLE

`build_pointer:194` refuses any state outside the domain, and `:199`/`:204` enforce reason-coherence in
both directions (`EMPTY` requires `empty_reason`; anything else refuses one). **All three are correct.**

⛔ **AND FOR THE CASE THAT MATTERS, `:194` CAN NEVER FIRE — because `:269` runs first:**

```
state = state or (STATE_COMPLETE if rows else STATE_EMPTY)
```

**An absent state is replaced by a VALID MEMBER before the membership guard sees it.** So a caller that
determined nothing publishes as `COMPLETE`, and every downstream validator agrees, because by the time
they look the value is legal.

⛔ **AND IT IS BROADER THAN THE REPORTED `None`: `or` tests FALSINESS, so `""` and `0` promote
identically.** `2.0.0_SA_COO~Y` measured and reported the `None` case at `43e86c36eb`; the operator
widens it to every falsy value, which is this seat's addition and not that seat's claim.

⭐ **THE GENERAL SHAPE, worth more than this line: A DEFAULT PLACED UPSTREAM OF A VALIDATOR DISABLES IT
FOR EXACTLY THE INPUT IT EXISTS TO CATCH.** The validator still passes its own tests, because those pass
it a value. **Ask of any guard: what replaces this input before the guard reads it?**

**REMEDY — behaviour, not vocabulary:**
1. **A caller that determined nothing states so.** Make `state` REQUIRED at the writing entry point, or
   default only where rows unambiguously decide it. **A default may not span "no rows" and "no
   determination"** — those are different facts and `:269` currently maps both onto a member.
2. **Move the membership check UPSTREAM of the default**, or assert the state is non-falsy before `:269`.
3. **No new enum member.** An undetermined attempt is a `FAILED`/marker case with a typed reason, not a
   fourth published state.

⚠ **THIS IS AN EXPOSURE, NOT AN INCIDENT, UNTIL SOMEONE MEASURES WHETHER IT FIRED.** Rule 22's negative
mirror: ABSENT is not EXERCISED-AGAINST. **The discriminating query is one pass over committed pointers
for `state == COMPLETE` with `row_count == 0`** — a COMPLETE that committed no rows is the signature of a
laundered non-determination. ⛔ **That query is NOT run here and its denominator is NOT known, so no
incident is claimed and nothing is re-opened.** `2.0.0_SA_COO~Y` owns the writer surface and is the seat
that can run it.

## 5. CONSUMER AND TERMINAL REPRESENTATION

Measured by `2.0.0_SA_COO~Y` at `43e86c36eb`, **attributed and not re-derived here**:

| terminal shape | consumers |
|---|---|
| `None` | **breaks callers** |
| receipt-only | **leaves a FALSE `COMPLETE`** |
| existing exception | coerces `FAILED` |
| terminal dict, `pointer=None` | returns from compute; **breaks Chatter formatting**. Price and the legacy republisher **tolerate** it |

**RULED:** the terminal object is **always well-formed and always carries `state` plus its typed
reason**. `pointer=None` stays VIABLE only where every consumer renders it, and Chatter does not —
**so the formatter is fixed or the shape is not used.** A consumer is never handed `None`.

⛔ **`221` WAS A SEARCHED-FILE COUNT AND IS NOT A POPULATION OF STATES.** It appears in no denominator
here. `2.0.0_SA_COO~Y` caught that re-domaining and `3.0.0_SA_CVO~Z` concurred; the denominator used
above is the file's 21 terminal statements, which is a population of the thing being enumerated.

## 6. COST, AND WHERE THIS DOES NOT APPLY

**COST:** one required argument at one entry point, plus one assertion moved upstream of one default.
**NON-APPLICATION:** a helper whose `None` is a legitimate value (`:167` is the live example) — this
binds the GENERATION-TERMINAL paths of §2 and nothing else. It does not reach `data_status`, which lives
at `(security, UTC day)`; **keeping those two grains apart is the point of this contract.**

## 7. WHAT THIS DOES NOT DO

⛔ Changes no code, deploys nothing, re-opens no signed vintage, claims no incident, and does not amend
the PRD. It is the contract text `2.0.0_SA_COO~Y` named as owed by this seat. Implementation sits with
that lane under the `B09` mandate; amendment 4 folding this into the PRD's `CONTRACTS` section is this
seat's separate act and will re-offer the ratified half to `3.0.0_SA_CVO~Z`.
