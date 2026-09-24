# H03 2a -- `served` LEG, CVO CLOSE

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~10:1xZ.** Ledger `amgt-h03-leadpanel-y-20260924`, leg `served`
(*"CVO review and served row reconciliation; E0 separately owned"*) -- the last open leg, and CVO-owned.
`daily` closed at 10:06:11Z on `0.7.0_AE_CloudOps~A`'s RAVC2. **Everything below is measured at this
seat**, not read from that report.

## VERDICT: **BOTH CONTROL ARMS PASS. THE LEG CLOSES.**

## ARM (a) -- the 09-23 pointers are byte-identical, at the fire boundary

Re-verified **after** the 10:00Z run, with the canonical sha256 **read from the pin artifact rather than
retyped**:

| item | |
|---|---|
| `TRENDING_CHATTER#2026-09-23` | **MATCH** `64e3bddb…d367f9` |
| `BREAKOUT_CHATTER#2026-09-23` | **MATCH** `887bd7c3…51116d` |

⚠ **A FALSE ALARM OF MY OWN, CAUGHT AND WORTH RECORDING.** My first probe reported BREAKOUT as a
mismatch. **The defect was in the probe:** I had retyped the pin from memory as `887bd7c3084bd…`,
inserting a `4`. Reading the pin **from the committed artifact** returned MATCH. Had that first read been
published it would have raised a served-output alarm eight minutes before the producer ran, on a night
that already had a real one. **A coordinate retyped from memory is not a coordinate** -- which is why the
pin record carries the canonical sha in the first place.

## ARM (b) -- a fresh same-day `_CURRENT`, present as EXPECTED

| axis | day | generation_id | rows | state |
|---|---|---|---|---|
| TRENDING_CHATTER | 09-23 | `20260923T100026Z-d09ee37a8f3b` | 2 | COMPLETE |
| TRENDING_CHATTER | **09-24** | **`20260924T100014Z-d09ee37a8f3b`** | **2** | **COMPLETE** |
| BREAKOUT_CHATTER | 09-23 | `20260923T100028Z-25147d66b259` | 0 | EMPTY |
| BREAKOUT_CHATTER | **09-24** | **`20260924T100014Z-25147d66b259`** | **0** | **EMPTY** |

The letter's arm (b) asked for a fresh `#2026-09-24 _CURRENT` with `row_count 2`. **Present, and 2.**

## ⭐ THE CORROBORATION NOBODY SPECIFIED, RE-DERIVED AND EXTENDED HERE

**`payload_hash` is IDENTICAL across the two days for BOTH products** while `generation_id` moved.
**The generation is FRESH and the CONTENT is unchanged** -- which is R-19's nonpublishing claim
**measured rather than asserted**: had 2a changed what the producer emits, the hash would have moved.

⭐ **And the id is SELF-CHECKING against the payload it names**, a property this seat pinned pre-apply:
the `generation_id` suffix equals the `payload_hash` prefix, verified on all four items
(`d09ee37a8f3b` / `25147d66b259`). **So the identical-payload finding cannot be an artifact of reading
the same field twice** -- two independent fields agree.

## THE HOUR AXIS -- BOTH HALVES NOW HELD, AND THE FLIP IS MEASURED

The BEFORE half (`PRE_10Z_HOUR_AXIS_CAPTURE_20260924_Z.md`, 02:39Z) could not be retaken. The AFTER half,
10:10Z, same instrument (direct invoke, deployed `opal-amgt-scoped-api` `CodeSha256 DEQQiCH+…`):

| route | 02:39Z (before) | 10:10Z (after) |
|---|---|---|
| `trending/chatter` | 200, **`dated` TRUE**, rows **2** | 200, **`dated` FALSE**, rows **2**, `COMPLETE`, gen `20260924T100014Z` |
| `breakout/chatter` | 200, `dated` FALSE, rows 0 | 200, `dated` FALSE, rows 0, `EMPTY`, `NO_SIGNAL_IN_WINDOW` **189 of 191** |
| `gainers/securities` | **400** refused | **400** refused |

⭐ **`dated` FLIPPED TRUE -> FALSE ACROSS THE 10:00Z BOUNDARY WHILE THE ROWS STAYED THE SAME TWO.**
Before the fire the route served the previous generation through the dated fallback; after it, today's own
generation. **The 400 control held at BOTH hours**, so the 200s are answers rather than artifacts at
either end.

⛔ **AND THIS DEMONSTRATES, RATHER THAN ARGUES, THE CLIENT-TYPE GAP THIS SEAT RAISED AT 02:39Z.** A reader
sees **the same two rows** either side of 10:00Z. The **provenance differs**, `dated` is the only served
field that says so, and `RankingSet` omits it (`types.ts:181`). The information needed not to be misled by
a fresh `generated_at` **is computed, served and paid for, and discarded at the type boundary** -- now
shown across the real boundary instead of inferred from a source read.

⚠ **ONE HALF OF THE PREDICTION IS NOT VERIFIABLE FROM MY OWN BEFORE-CAPTURE, and I will not claim it.**
The Lead Panel mandate predicted breakout would read **ABSENT** before 10:00Z and **EMPTY-with-reason**
after. My 02:39Z capture recorded `dated`, `requested_as_of`, rows and `generated_at` -- **it did not
record `state` or `empty_reason`**. So the ABSENT -> EMPTY transition is **UNMEASURED** at this seat; only
the `dated` flip is. The after-state EMPTY/`NO_SIGNAL_IN_WINDOW` is measured and stands on its own.

## SERVED ROW RECONCILIATION

| axis | pointer `row_count` | rows the route returned | |
|---|---|---|---|
| TRENDING_CHATTER | 2 | **2** | RECONCILED |
| BREAKOUT_CHATTER | 0 | **0** | RECONCILED |

`generation_id` on both served payloads equals the `_CURRENT` pointer's. **The route is serving the
generation the pointer names.**

## WHAT THIS CLOSE DOES NOT COVER

- **E0** -- separately owned by the leg's own text, not graded here.
- **No browser re-walk.** Direct invoke bypasses CloudFront and `auth-validator-edge`; this is
  route-proof, **not render-proof**.
- **The chatter water.** The identical payload across two days is consistent with the known-stale
  upstream, which is **2b**, unowned, and NOT a defect of this act.
- **The `dated` type gap** is a client-side finding for the RESAPP round, not a defect of 2a.

-- `3.0.0_SA_CVO~Z`
