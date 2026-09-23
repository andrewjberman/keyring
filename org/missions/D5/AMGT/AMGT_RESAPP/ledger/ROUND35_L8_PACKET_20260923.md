# AMGT_RESAPP round 35 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `5f007c467f`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-23 ~06:0xZ.

**DRAIN-END: 1 of 1 terminal, 0 open, 0 worktrees.** All six criteria PASS, rc=0, **111 tests pass in the merged
shared tree.**

## 1. WHAT THE CELL BUILT, verified on this seat's own instrument

| check | result |
|---|---|
| AC0 -- does a WINNING step 5 need a `bronze_sink`? | ⭐ **NO.** `build_battery_source_object(security_key, battery)` takes none. **So Rule 30 never fires and the `infra/logic/**` lane gap was never on this cell's path.** |
| the widening | step 5 is now `(keys, run_date, http_get, timeout=60)`, call site updated -- **two lines, as ruled** |
| steps 1-4 | **signatures BYTE-IDENTICAL** at `:718`, `:796`, `:900`, `:1007`; step list `[1,2,3,4,5]` unchanged |
| dispatch | on `keys["exchange"]` -- the **RECORD-LEVEL** field (36 of 96), not `identity.exchange` (4 of 96), and **`domicile` never read even when present** |
| three branches | HK dispatches (1 fetch); unregistered venue refuses (0 fetches); **absent/unparseable key refuses WITHOUT dispatching** (0 fetches) |
| ⭐ test (c) | a synthetic `SC 13D` (Lenovo filer about ANOTHER issuer) **passes (a) and (b) and is REJECTED on (c) alone**; a genuine annual document accepts on all three |
| spend | `http_fetches 1`, `bloomberg_calls 0`, `s3_deletes 0` |

## 2. ⛔ AND THE CELL'S REAL RESULT: THE ADAPTER DOES NOT RESOLVE A FILING

AC4's live fetch returned **HTTP 200 with `recordCnt=0`.** The route is built, dispatches correctly, is
negative-controlled on three branches and holds the binding guard -- **and it returns nothing for Lenovo.**

⛔ **SO THE THREE THINGS THIS CELL WAS CUT TO UNBLOCK ARE NOT UNBLOCKED:**

| held thing | state after this cell |
|---|---|
| Lenovo's FILINGS stage -> the Thesis tab | **still UNRESOLVED** |
| `rk-127`'s first HELD marker | **still no run produces a CHANGED-HELD** |
| `rk-49` (Lusha) | **still no verified site** |

⭐ **THIS IS THE THIRD HALF-FIX IN SIX ROUNDS AND I AM LABELLING IT AS ONE**, exactly as with `rk-124`'s server
half and `rk-127`'s mechanism. **Correct code that changes nothing a user sees.**

⚠ **ROW `Z-W128-S1` (ARMED) IS THE PART THAT MUST NOT BE SOFTENED:** the HKEXnews search taxonomy is
**undocumented and returned 0 records under EVERY parameter combination tried** -- *"a future cell aiming to make
this route WIN should not assume query-tuning alone resolves it."* ⛔ **The next cell here is a RESEARCH question
about HKEX's own interface, not a tuning pass**, and sizing it as tuning is how a round gets spent for nothing.

## 3. MY ORDER DEFECT -- two `AC1` blocks, and the checker COLLAPSED them silently

⛔ **The order carried SEVEN `<criterion>` blocks and SIX distinct ids.** I added a new `AC1` when editing and left
the original in place. Row `Z-W128-S2`: `proof-of-spec-check.py`'s invocation-alignment limb **collapses same-id
blocks to the LAST-DECLARED one**, so it graded six and returned **rc=0** -- ⭐ **while the issuance gate's own
NOTE printed "7 mechanical criteria".**

⭐ **TWO TOOLS, TWO DENOMINATORS, NEITHER FLAGGING THE DISAGREEMENT** -- and the one that graded is the one that
saw fewer. **Same family as the sibling project's finding that invocation-alignment certifies AGREEMENT and never
RUNNABILITY: a checker that compares two artifacts cannot notice that one of them lost a row.** The cheap
discriminator is one line: count `<criterion id=` occurrences against `len(set(ids))` at the cut.

## 4. WHAT THE PRE-CUT MEASUREMENT BOUGHT, stated once because it is the round's method

**Six findings, from reading, before any order existed** (s.43a and the two that followed): the seam was a wired
stub not a gap; its key was empty on 0 of 96; the key was **wrong in principle**; the ownership blocker was a
**code comment, not a contract**; my own coverage number was wrong **9x** (right field name, wrong DEPTH); and the
seam **could not fetch at all**, which my own BOUNDS then forbade fixing.

⭐ **The cell changed shape three times and cost zero drains.** ⚠ **And the gate still caught a seventh defect I
had missed -- no `<paths>` block at all** -- which I found only by asking the REPOSITORY whether the commit landed
rather than reading the tool's tail.

## 5. What this seat asks of L9/L10

1. **Grade the cell on what it BUILT, and grade the ROUTE as UNRESOLVED.** Both are true and the packet separates
   them.
2. ⛔ **Rule `Z-W128-S1`'s consequence:** whether the next HKEX attempt is a research cell or is dropped. **Do not
   let it be sized as query-tuning.**
3. **`Z-W128-S2` needs an owner** -- the duplicate-id collapse is a checker limb, estate-wide, not this project's.
4. **The `infra/logic/**` lane gap stays on Andrew's card** even though this cell did not need it -- Rule 30 is
   still unsatisfiable from site Z for any cell that DOES.

**Push state: LOCAL on SITEZ @`5f007c467f` plus this commit.**

-- `2.0.0_SA_COO~Z`
