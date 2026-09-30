# AMGT_CORPUS ROUND 11 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~10:2xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND11_DRAIN_END_PACKET.md` @`b7a1f3040b` (read to EOF, 5,591 B), msg 26560.
**L7 RE-MEASURED not adopted:** `m-1` and `m-2` read `complete` on their LAST `<status>` tag; 1 judgment criterion (`m-2` AC5).

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **97 items, 32 UNDER_INVESTIGATION.** New and ARMED this round: `Z-W1-S14`.

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S14` (ARMED: the `/4` bump turned two method-version tests red outside the grant) and its carrier `Z-S57` | **GRADUATED** | AMENDMENT 1 granted and ruled them (@`e119939999`); m-2 AC1 12 passed, corpus suite 441 passed. **The second round running in this class** (round 10's `Z-W1-S13`). The packet's own cutting lesson is the fix: a `METHOD_VERSION` bump ruled at the cut grants the pinning tests in the same order |
| `Z-W2-S11`, `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | no landed remedy |

**The SHOP carve-out, read against round 10.** At round 10 this seat suggested, as optional, that a `$` on a USD listing could safely set
USD, 3 names. The intersection rule built from that suggestion also moved SHOP (`$` on a CAD listing) to CAD. The CTO refused
that move, because Shopify reports in USD and the payload cannot tell CAD from USD. **The refusal is right, and my round-10 wording
only bounded USD listings; it did not name the non-USD dollar case.** The served result (`currency_set 5`: BZLFY, CPA, SPOT, UNVGY ->
USD; ML -> EUR; SHOP null with its own reason) is the conservative shape the criterion protects.

## 2. L9 -- `m-2` AC5: "is every placed value in the column the pdf page shows it in, and is every unplaced name still honestly ABSENT?"

This seat opened the bronze PDF page 0 cited by each served Base case and read word positions (`get_text("words")`) for
**3 of the 6** names. The scenario table's values sit on a regular grid of 15 slots about 38 points apart (Upside 5, Base 5,
Downside 5):

| name | Base-block slots on the page (x-centre: value) | empty slot | served Base EPS |
|---|---|---|---|
| HEI_US | 324: 6.03, 361: 6.80, 399: 7.73, 437: 8.99 | **~475 = 5th Base slot = 2030E** | `6.03 / 6.80 / 7.73 / 8.99 / null` |
| TSM_US | 322: 96.97, 358: 121.83, 396: 146.93, 433: 129.07 | ~475 = 2030E | `96.97 / 121.83 / 146.93 / 129.07 / null` |
| V_US | 323: 12.87, 361: 14.56, 399: 16.38, 437: 18.66 | ~475 = 2030E | `12.87 / 14.56 / 16.38 / 18.66 / null` |

The Price rows agree the same way (HEI `301 / 319 / 363 / 422` then nothing before the Downside block at 514). **Every served value
equals the page's value in the same slot, and the blank is the slot the page leaves empty.**

**VERDICT: MET on 3 of 3 read** (HEI, TSM, V). The other three (8035_JP, BZLFY_US, SNPS_US) were not opened here. "Every unplaced name
honestly ABSENT" is vacuous: all 6 were placed (`placed 6 ambiguous 0 no_positions 0`).

⚠ **One reading for the team, not a defect of the extraction:** TSM's Base EPS falls **146.93 -> 129.07** from 2028E to 2029E (Price
2,939 -> 2,581), while its Upside and Downside rows rise every year. The page says exactly that; the extraction reproduces it. It is
flagged because a Base case that dips once while both bounds climb may be a typo in the team's pack. It is the team's to say.

⚠ **An instrument trap met and avoided on the way:** the first read took the EPS row nearest the page top. That is the summary table
at y≈174, whose TSM values (96.49, 121.09...) differ from the served Base. The scenario table is the one under the header row at
y≈431. Grading against the wrong table would have read a false mismatch.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W1-S14` GRADUATED; the older set CARRIED as before. **MET**
3. **Every judgment criterion graded** -- 1 of 1, MET on 3 of 6 read. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S14",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T10:25:00Z",
    "one_line": "L9 round 11: m-2 AC5 MET on 3 of 6 read by position on the bronze PDF page 0 -- HEI, TSM and V: the scenario table is a 15-slot grid ~38pt apart, each served Base value equals the page's value in its slot, and the one empty slot (~475) is the 5th Base slot, 2030E. Z-W1-S14 graduates (second round in the method-version-test class). The SHOP carve-out the CTO added is right; my round-10 '$ on USD' suggestion did not name the non-USD dollar listing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-m-1 and TO-CRPS-m-2 read 'complete' on their LAST <status> tag; judgment=\"true\" on m-2 AC5 only.",
        "L8: _latest_dispositions('.', 'AMGT_CORPUS') 97 items, 32 UNDER_INVESTIGATION; new ARMED Z-W1-S14, graduated with its carrier Z-S57 (AMENDMENT 1 @e119939999; corpus suite 441 passed).",
        "L9, this seat's fitz word-position read of each served Base citation's bronze PDF page 0, scenario rows below the header at y 431: HEI EPS row x-centres 134..284 (Upside 6.04..11.07), 324 6.03, 361 6.80, 399 7.73, 437 8.99, then 513..664 (Downside 5.78..8.15); TSM 322 96.97, 358 121.83, 396 146.93, 433 129.07, then 511..661; V 323 12.87, 361 14.56, 399 16.38, 437 18.66, then 513..665. The slot at ~475 is empty on all three.",
        "Served read_dossier Base EPS at method amgt-corpus-dossier/4: HEI {2026E 6.03, 2027E 6.80, 2028E 7.73, 2029E 8.99, 2030E null}; TSM {96.97, 121.83, 146.93, 129.07, null}; V {12.87, 14.56, 16.38, 18.66, null}.",
        "Instrument note: the page's first EPS row (y≈174) is the summary table; its TSM values 96.49/121.09/146.95/131.64 differ from the scenario table's Base, which is the served source."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S14",
      "AMGT_CORPUS-Z-S57"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @b7a1f3040b asserts 2 orders terminal and VALID, the /4 rewrite landed as re-signed with the move diff at 0 afterwards, and all six blank Base cells placed at 2030E by x-coordinate.",
    "world_is": "True on the 3 of 6 names this seat read by position: every served value is in the slot the page shows it in, and the blank is the empty 2030E slot. TSM's Base dip in 2029E is the team's own figure, reproduced faithfully.",
    "notes": "FOR THE ROUND-11 ANALYSIS: (1) the method-version-test class has now recurred in two rounds; the cut should grant the pinning tests in the order that rules the bump; (2) the move-diff instrument should compare every served case key, as the packet says; (3) optional -- ask the team whether TSM's Base 2029E dip (146.93 -> 129.07) is intended."
  }
]
```
