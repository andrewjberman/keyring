# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain L (lists). One co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z`. **Counterpart:** `2.0.0_SA_COO~Z`'s COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_COO_HALVES.md` (written @`d2c9ade7ec`, rollback
re-cut @`f85523e95e` on this seat's msg 23830) -- APPLIED/EXERCISED. **This plane: DESIRED** -- the SOURCE DIFF and THE
PRODUCER'S OWN RULE, read at HEAD by this seat. Neither half stands alone; the worker reads BOTH before its first live
act and STOPS with a BLOCKING row if either is absent or lacks the `AMGT-rk-53` section.

⚠ **WHY THIS FILE IS LATE, stated plainly:** chains I, M, F, E, P were co-signed from the batch at `9a6aa12da2` and T from
`0d619b8db7`; **chain L's COO half landed outside both and this seat did not write its twin until `2.0.0_SA_COO~Z` named
the gap** (its 06:47Z message, 15 of 31 drained). `rk-53` is spawned and the worker touches nothing served, so nothing
was unsigned that ran -- but the pair was incomplete while the cell was live, and that is the failure this file closes.
`rk-54` is a MEASURE cell writing nothing live and is not co-signed; that partition is the issuer's.

## `AMGT-rk-53` -- no rank without signal: `empty_reason` on the ONE generation carrier (R14-L1; FWD-15, L2, L5, V8/D25, `C-SERVER-SIDE-RANKING`)

### 1. THE ACT
The worker does NOTHING on the served plane: it builds the carrier, the filter, the adapter fields, the tests and the
page's EMPTY branch, and proves the behaviour IN-PROCESS on its own worktree bytes. Agrees with the COO half exactly,
including that this half therefore covers **two LATER acts by other actors**, not the worker's.

### 2. THE SOURCE DIFF, read at HEAD
| what | state at HEAD | measured |
|---|---|---|
| `lib/research/metrics/generation_writer.py` | **DOES NOT EXIST** | file absent |
| the chatter product loop | ranks straight from `rank_top_n(normalized, as_of_counts, TOP_N)` with **no signal test between scoring and ranking** | `chatter_axis.py:812-826` |
| `empty_reason` anywhere in the research library | **0 hits across 160 files scanned** (`comp-find 'empty_reason' lib/research`) | the field is new on every writer and every reader |
| `generation_fields()` in the adapter | EXISTS and already carries the pointer's fields, with *"Every one is None when there is no pointer -- nothing here is stamped from this process"* | `scoped_amgt.py:404-417` |

So the cell adds a filter, a field, and ONE carrier where two writers each roll their own; `generation_fields` is
extended, not invented, and its existing docstring already states the discipline the new field must follow -- **the value
comes from the pointer, never stamped by the responding process.**

### 3. ⭐ THE PRODUCER'S RULE, AND THE THING THE COO HALF UNDERSTATES
The COO half says the existing test arm *"ASSERTS that defect"*. Read at source, it is sharper than that:
`test_chatter_axis.py:355-364` is named
`test_compute_chatter_axis_all_zero_signal_ranks_trending_and_empties_breakout`, and its docstring **DEFENDS** today's
behaviour in terms -- *"TRENDING a deterministic TOP_N set, every score at SCORE_MIN -- **ranking an all-zero signal is
not the same as declining to rank**"* and *"An empty product here is the correct answer, which is exactly why a reader
must consult `row_count` rather than assume a non-empty list."*

⛔ **SO THE CELL REVERSES A DELIBERATE PRIOR READING, NOT A BUG.** That matters three ways and the cut should carry all
three: (1) the rewrite of that test is the VISIBLE RECORD of the reversal and must read as one, not as a repair --
whoever reads it later is entitled to know the old answer was argued, not overlooked; (2) the two products still degrade
DIFFERENTLY and both answers stay honest -- Breakout was already EMPTY-with-reasons, and this cell brings Trending onto
the same rule rather than inventing one; (3) the authority for the reversal is Andrew's own L2 (*a ranking never includes
a member with no signal*), carried into `C-SERVER-SIDE-RANKING` at v0.11, and the per-subject definition this half binds
is the one the PRD states: CHATTER needs at least one article in the window; PRICE needs at least two observations, the
movement gate's own `INSUFFICIENT_OBSERVATIONS` test.

**Per branch, from the new rule:** a product WITH signal ranks as today and carries no `empty_reason`; a product with NO
signal in the window is EMPTY with `empty_reason NO_SIGNAL_IN_WINDOW` and zero members; a FAILED run is neither -- it
stays a failure and the prior generation stays `_CURRENT`, which `C-RANKING-GENERATION` already requires and this cell
does not touch. The COO half covers the first two; the third is named here so no one reads EMPTY as the failure state.

### 4. THE TWO LATER ACTS, and what the DESIRED plane adds to each
1. **`opal-amgt-scoped-api` (carried by `rk-61`).** Concur. One qualifier from chain T's half, repeated because it binds
   here too: `rk-61`'s pre-build `git log <merge-base>..SITEZ -- lib/research/api ...` **printing nothing is a
   PRECONDITION, not a formality** -- it is the only check that `rk-53`'s adapter bytes are the ones being deployed and
   that no third cell slipped in between. If it prints anything, the redeploy is a different act than either half signed.
2. **`amgt-resapp-chatter-axis`, by `2.0.0_SA_COO~Z`.** Concur, and the DESIRED-plane point the APPLIED plane cannot
   state: the served effect arrives **on the Lambda's NEXT SCHEDULED RUN, not at the apply.** The apply changes the code;
   the generations and `_CURRENT` pointers only move when the schedule fires. So a post-apply read of the served rankings
   is NOT a discriminator for this act, and the change-management entry should say which run is the first to carry the
   new rule, with the schedule read by name into the entry (which the COO half already requires).

### 5. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 1 writer of `_CURRENT`** after this cell -- the chatter-axis Lambda through the one carrier,
with price generations in a different partition. I concur on the POST-cell state and add the pre-cell one, because it is
the reason the cell exists: TODAY the two products' generation writes are two implementations, which is exactly how
`empty_reason` could be present on one and absent on the other. **The census is only N = 1 BECAUSE the cell lands the
single carrier; a partial landing -- filter without carrier, or carrier without both writers converted -- leaves N = 2
and the field optional.** That is the state the cut must not stop in.

### 6. WHAT THIS HALF DOES NOT COVER
Any deploy by the WORKER; any pool write (the dry run reads four prefixes and writes nothing); a portal push or promote
(PROD HELD); `movement_gate.py`'s `MIN_ABSOLUTE_JUMP`, which is the COO's card-B direct act under its own pair;
`handler()` itself (`rk-61`'s region); and any THIRD deploy of either function. Each is a new act needing a new pair.

Signed `1.0.0_SA_CTO~Z`, 2026-09-19 ~06:5xZ, against the COO half at `f85523e95e`.
