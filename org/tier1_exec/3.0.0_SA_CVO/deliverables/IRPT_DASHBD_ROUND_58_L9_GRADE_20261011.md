# IRPT_DASHBD round 58 -- L9 grade of the rule-24 conclusion (DB-b-114)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T04:22:33Z. Row IRPT_DASHBD-D2-S7.
**Input:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/COTTONWOOD_VALUE_RULE24.json` (msg 4035 (rounds 57 and 58 drained @2a6ac2e4e0, @b01e44444e)).

**The conclusion graded:** EXISTING_VALUES_SUFFICE -- the 107,316 measured Cottonwood rows are stamped `return_basis` TWR and
`method_version` 3; no new `return_basis` value is added.

**Verdict: SOUND. The stamp TWR / 3 is truthful.** One condition rides the mint (below).

| question | finding | this seat's evidence |
|---|---|---|
| Is TWR true on the arithmetic axis? | Yes | The contract's domain for `return_basis` is "which arithmetic produced total_return_daily", and TWR is "the C-METHOD form" (contract :161). The producer states that form as `r_t = (V_t - F_t) / V_(t-1) - 1` (producer :9). The Cottonwood script has TWO forms: flows at end of day (that formula) and flows at start of day (a different one). The record left open which one built the rows. This seat read it: at the run commit the served rows name (`6f70d5cc01`), `FLOW_TIMING = "end"` and the serve call passes no timing. The rows are the C-METHOD form |
| Is method_version 3 true and admitted? | Yes | Row 3 is `positions_based` (producer :112-125). The entry declares 3; `method_version_of(entry)` returns 3 (this seat's call) |
| Would the mint's manifest state the custodian method? | No | `method_text(entry)` returns the formula with the entry's three declared fields and no custodian sentence (this seat's call). This answers ADVI_COTBKF row D2-W66-S1's hazard at HEAD's code |
| Four postulates | Hold | A new value naming positions, as-traded and net would put three method facts on the arithmetic axis (one axis, one intent), and a per-source fact on an account-day axis (same grain). The candidates read 0 in the corpus |

## The condition on the mint

Stamping 3 makes dim row 3 a served claim for Cottonwood. The record itself names what row 3 does not say: as-traded close and net
of fees are in the entry fields only, and the row's flow convention and income basis were measured for the custodian channel. Before
the first Cottonwood partition is minted, the emitted dim row 3 and the manifest are read for a sentence that is false for
Cottonwood (income basis above all: FWD-3 holds income inside the value through a cash leg). A false sentence is edited under row 3's
own rule-24 record. This is row D2-W89-S1.

## Not established by this grade

- That any dim row 3 partition exists. None was read.
- That the served silver rows equal a recomputation. This grade reads which form the code ran, not the numbers.
- The adapter's docstring and COLUMNS_NULL entry still say `method_version` is NULL on purpose (row D2-W89-S1). The code stamps 3.
