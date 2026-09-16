# POSN_ASTTAX — ROUND 4 L8 PACKET

**From** `2.0.0_SA_COO~Z` (L5/L6/L7 owner) **to** `3.0.0_SA_CVO~Z` for L8/L9/L10.
**2026-09-13T07:5xZ** · PRD **v0.6** `@ae66157381` (corrected `@ded02d9a9c`) · gate **ADMITTED**, both
halves SIGNED and current, read at the moment of compiling.

> **ROUND 4 IS 4 OF 4 CELLS TERMINAL AND DRAINED.** Every proof instance is VALID at HEAD, measured by
> this seat rather than taken from a worker's self-report.

---

## 1. THE CELLS

| cell | order | worker | verdict | drained | instance |
|---|---|---|---|---|---|
| `AT4-s-1` | `TO-U1-1` | `~15` | **FWD-6 BAR FAILS** — 9 of 11 readers | `a78bf850b0` | VALID |
| `AT4-s-2` | `TO-U2-1` | `~18` | **FWD-4 FAILS both ACCEPT clauses** | `0ade5ac466` | VALID |
| `AT4-s-3` | `TO-U3-1` | `~16` | premise CONFIRMED; hand-off delivered | `0a220e955b` | VALID ×2 |
| `AT4-s-4` | `TO-U4-1` | `~17` | retag set is **TWELVE**, not eleven | `ce9a363064` | VALID ×2 |

Statuses at HEAD: all four `complete` (`baaf6407ed`). **NEGATIVE CONTROL, run so the reading
discriminates:** the four CARRIED round-3 orders — `TO-S2-1`, `TO-S3-1`, `TO-T6-1`, `TO-T7-1` — all
still read `staged` at the same HEAD. The flip did not leak.

⚠ **Two cells carry a DOUBLED instance** (`~16`, `~17`): one at the order's `<to_id>` name, one at the
gate-derived full-stem name. They are **deliberately not byte-identical** for `~16` — 37,946 vs 37,964
bytes — and both read VALID by **different resolution routes** (derived: artifact rows pinned to
`a97b140b54`; original: PENDING co-committed). This is the recorded consequence of `Z-S51`'s defect,
not a duplication error.

## 2. THE TWO OUTCOMES THIS ROUND EXISTED TO SERVE

Round 4 was cut because `FWD-4` and `FWD-6` had **zero cut orders across three rounds**. Both now have
a measurement, and the two agree on the load-bearing fact:

```
FWD-6   11 readers / 4 surface families, from a denominator of 484 src/ code files
        five-class bar: 34 PASS / 21 FAIL of 55 cells -- 9 of 11 readers FAIL
        PRICE: 9 edit sites, 23 cells -- FROZEN 23 / OWNED 0
FWD-4   per class: FI/Cash FAIL+DISAGREE | Equity PASS+AGREE | Structured ABSENT 11 of 11
                   Commodities FAIL+DISAGREE | Alternatives PASS+AGREE
        exclusivity VIOLATED: orange500 keyed to Alternatives AND Commodities on one reader
        PRICE: 14 cells -- FROZEN 14 / OWNED 0
```

> **ZERO OWNED, twice, independently measured.** No work on the classifier, the DynamoDB registry or
> the lambdas moves a single cell of either outcome. Correctly-tagged data would arrive and the screens
> still would not show it.

⛔ **NO FWD IS CLAIMED REALIZED. 0 of 6.** These cells COVER their outcomes and do not SERVE them —
both bars are EXERCISED and this round's evidence is SOURCE-AT-PIN, because the portal is frozen and no
worker held a rendered DOM. That distinction is stated here rather than left for the grader to infer.

## 3. FINDINGS THE GRADER SHOULD NOT HAVE TO REDISCOVER

1. **`HoldingsTab.tsx:1392` and `SelectionTab.tsx:321` are the SAME LINE on two pages** — four
   identical `['Fixed Income', 'Equity']` literals in all. **This is why an outcome graded "do the
   views agree" returns PASS on a broken system**; the five-class bar was cut in its place and caught it.
2. **The colour leverage site is TWO files, not one** (`W18-S2`). C1/C2/C3 bind through
   `holdings-shared.tsx:67-110`, absent from `AT4-s-1`'s census, already drifted from `chartColors.ts`
   on 1 of 21 shared keys. **A fix landed only at `chartColors.ts` would verify clean and miss 3 of 11
   readers.**
3. **The ratified gold does not exist** (`W18-S5`) — 0 of 65 palette tokens; the amber base is already
   Cash on 6 readers. A colour DECISION, not a wiring change, and no cell owns it.
4. **The retag set is TWELVE** (`W17-S2`). `VNQ`: served `equity`, `sector` reads the literal
   `Real Estate`. **Without it `Alternatives` has ZERO members in the 285** — and it is the ONLY member
   that arms `C-RETAG-SAFETY` (`management_style` `unknown`). Round 3's control read *"0 of 11 trip the
   guard"*; it is **1 of 12**, and that one is the member eleven was missing.
5. **Two live ticker-keyed `asset_class` stores** (`W17-S3`), ruled by `1.0.0_SA_CTO~Z` at `Z-S48`:
   a second module also named `ETFClassifier` on `bd-securities`. **0 of 13 candidates agree**, and ten
   disagreements carry `alternatives` — *a ratified class* — so a bar shaped "is the served value one
   of the five" **passes on all ten**.
6. **A wrong-ZERO nearly shipped** (`~18`): a same-line instrument returned 0 hits for 7 of 12 files;
   probing each zero overturned **5 of 7**. Trusting them would have reported 5 readers as colourless.

## 4. THE ROWS

25 round-4 rows, deduped by id across 9 channel files (investigation plane taken as the original where
a row appears on two planes — the raw count of 205 includes cross-plane copies and is NOT the row count).

```
ROUND-4 ROWS                25
ARMED and UNADJUDICATED     12   ->  2.0.0_SA_COO~Z 8   |   1.0.0_SA_CTO~Z 4
ALREADY ADJUDICATED          5   ->  W16-S1/S2/S3 (Z-S49, GRADUATED), W16-S5 (Z-S50), W17-S3 (Z-S48)
```

Dispositions this seat has already made, so they are not re-litigated at L9: `Z-S49` GRADUATED the
three `W16` blockers (all ISSUER defects of this seat, all remedied and exercised); `Z-S50` ruled
`U3-AC4` **UNCOMPUTABLE-BY-CONSTRUCTION** against the worker's own more generous PASS — **the instance
records AC4 as PASS and was deliberately NOT edited to match; the ruling lives in the channel.** The
grader should read them together.

## 5. WHAT IS NOT CLOSED, STATED SO IT IS NOT DISCOVERED AT L10

- ⛔ **`Z-S46` STANDS: round 4 can be CUT but not CLOSED on today's terms.** The round-3 L10 exception
  is pinned to `total != 15`; the project now carries **19** orders (15 + 4; an earlier draft of this packet said 20 and that was this seat's arithmetic slip, caught by 1.0.0_SA_CTO~Z's independent census at 22328), so it is dead by its own guard, and
  the four carried orders remain non-terminal. **`_open_tos_for_project` will return 4 open and refuse
  the round-4 slug on the same limb.** Nothing in round 4 terminates them: `TO-T6-1` is the retag, held
  by a NO-GO, and the others sit behind that retag and the portal freeze.
- **Retag NO-GO stands.** `TO-T6-1` untouched and unspawned. A twelfth member does not license a retag.
- **Portal frozen.** Nothing written under `portal/` by any cell; gitlink `e85f6eb84f` unmoved.
- **No deploy, no promote.** The positioning deploy remains approved conditional on a two-seat
  never-widen sign-off that has **not** landed.
- **Andrew's RESERVED card is open** (05:14Z via `0.0.0_AB_MSTR~Z`): whether the freeze forbids portal
  SOURCE WRITES or only promote/gitlink/push. `FWD-4` and `FWD-6` cannot be SERVED until it is answered.

## 6. DELIVERY

⚠ `3.0.0_SA_CVO~Z` is **respawned but UNBOUND** — TUI and bridge running, no persistent thread, needing
one human keystroke that is with Andrew (`0.0.0_AB_MSTR~Z` 22318). **It cannot be reached by message.**
This packet is therefore committed as a durable artifact FIRST and handed second; if the send is not
consumed, the packet is still on the record and this path is where it lives. That is the fix for the
banked failure where a ruling existed only in mail.
