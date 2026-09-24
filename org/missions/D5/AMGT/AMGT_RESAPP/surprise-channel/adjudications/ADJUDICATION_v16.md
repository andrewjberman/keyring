# AMGT_RESAPP round 17: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T16:3xZ at HEAD `bf9d2334da`. LOCAL on SITEZ.
**Inputs:** the COO's drain-end packet `ledger/ROUND17_L8_PACKET_20260921.md` @`bf9d2334da`; the two round-17 orders
and every AMGT tree order read at HEAD; the channel census; two live read-only checks from this seat.

## Round state and the L10 read

**2 of 2 terminal** (`rk-69` @`84dc36f89b`, `rk-70` @`7c0ea66fe3`), each `<status>complete</status>`.

**Acceptance.** Round 17: PASS 8 / FAIL 0 / UNVERIFIABLE 0 of 8 over 2 orders; the order files carry 8 criterion ids
(4 + 4). **Judgment census from the order files:** 0 of 2 declare one. No judgment grade is owed.

**`S176` is closed, on a second instrument.** The COO proved `rk-69` by diffing HEAD's parser against the new one. This
seat counted distinct criterion ids inside each order's line-anchored `<proof_of_spec>` block with its own regex over
**all 138 AMGT tree orders: 669 ids; the merged parser reads 669; 0 disagreements.** Round 14 now reads PASS 131 /
FAIL 1 / UNVERIFIABLE 33 of **165 over 31** -- the true population, which the sweep had understated since round 14.
Every slug from here prints one count, not two.

**Channel:** 3 UNDER_INVESTIGATION (unchanged); no worker row filed; no new self-graduated disarm record (the round-16
contract is holding); `_graduated_without_row` 23, unchanged.

## A live check: W38-S5's trigger has now occurred, two minutes after its guard merged

This seat ran `rk-70`'s new `_latest_stamp` over every key under `s3://opal-data-harvest/raw/bloomberg/`, read-only:
**37 keys, 37 resolved, 0 `NoRawStampError`, 2 resolved to a stamp OTHER than the bare newest:**

| key | bare newest stamp | its contents | the guard's pick |
|---|---|---|---|
| `6861_JP_Equity` | `20260921T162534Z` | `exec_officers.json` only, written 16:25:37Z | `20260919T152125Z` |
| `CSL_AU_Equity` | `20260921T162530Z` | `exec_officers.json` only, written 16:25:35Z | `20260919T152121Z` |

At `7328e6d7f6` (C-S328's census) zero keys had a non-raw newest stamp. Two do now, written by the Bloomberg-fallback
writer C-S328 named (`bloomberg_fallback.py:68`) -- the condition C-S328 said "one fallback roster run after a pull"
would create, most likely from today's management activity. **`rk-70` merged at 16:23:41Z (@`7c0ea66fe3`); both
stamps landed 16:25:35-37Z.** The trigger never met the unguarded picker, so this is still an EXPOSURE that did not
fire, and the guard is now doing live work: without it, a derive on either name would crash on `NoSuchKey`.

## A correction to this seat's own label

ADJUDICATION_v14 held `W37-S1` open on "the bucket/tenancy word". Andrew ruled that on 2026-09-18
(`ANDREW_DIRECT_20260918_214xZ_...` @`7633c267c2`); what remains is doctrine authorship in `infra/logic/**`, which
`.owned-paths.yaml` PLATFORM_LOGIC_DOCS grants to `4.0.0_SA_CRO` and `~A`-`~D` only (read at `8fcffdcb7b`), then an R20
acknowledgment card. **`W37-S1`'s holder is a laptop CRO lane, not Andrew and not MSTR.** Its disposition is unchanged.

## Owed next from this seat

`rk-48` AC4-AC6 and `rk-49` AC3/AC4, graded against the MINTED direct-act criteria (@`71f9a1e027`: `--value-only`
with an empty-key guard, `as_of` pinned to `2026-09-19`), when the direct act reports; then `W49-S2` and `W49-S4`.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S347",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T16:35Z",
    "one_line": "L9 GRADE RECORD for round 17: 2 of 2 terminal, acceptance 8/0/0 of 8, no judgment criterion; S176 closed on a second instrument (669 of 669 criterion ids across 138 AMGT orders); W38-S5's trigger occurred live two minutes after rk-70's guard merged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at bf9d2334da: rk-69 4 and rk-70 4 distinct criterion ids, parser reads the same, judgment=\"true\" in 0 of 2; --acceptance --round 17: PASS 8 / FAIL 0 / UNVERIFIABLE 0 of 8 over 2 order(s).",
        "Independent count over every AMGT tree order: distinct criterion ids inside the line-anchored <proof_of_spec> block = 669; _order_criteria = 669; 0 of 138 orders disagree. --acceptance --round 14: 165 criteria over 31 orders.",
        "Live read-only: new _latest_stamp over 37 raw/bloomberg keys resolves 37, raises 0; 6861_JP_Equity and CSL_AU_Equity resolve to their 2026-09-19 raw stamps past newer stamps holding only exec_officers.json (16:25:35-37Z). rk-70 merged 16:23:41Z (7c0ea66fe3)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells pass on their own criteria and on a live read neither the workers nor the COO ran; the exposure rk-70 closes materialised minutes after it closed.",
    "notes": "Grade carrier only. S176 and W38-S5 keep their GRADUATED dispositions (C-S323, C-S328); their REMEDIATION rows, owed at the true L10 close, now read REMEDIATED by rk-69 and rk-70.",
    "dismissal_reason": "Grade record: this row carries the round-17 L9 grade and dispositions no item; the enum has no record value."
  }
]
```
