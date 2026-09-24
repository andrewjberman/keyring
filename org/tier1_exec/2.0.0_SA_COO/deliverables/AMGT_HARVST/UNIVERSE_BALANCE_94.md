# The AM-research universe: where all 94 folders stand

Measured 2026-09-24 18:27Z by `2.0.0_SA_COO~Y` over the **LIVE** research directory -- Andrew's definition
(msg 25683: *"The 93 group, you are correct, the 93 are the ones"*) -- not the 2026-09-10 builder snapshot.

## Population

| | n | of 94 |
|---|---|---|
| live folders on disk | **94** | -- |
| in the 2026-09-16 universe snapshot | 89 | 95% |
| NOT in it (the builder is stale) | 5 | 5% |

The five the snapshot lacks are `AMD Advanced Micro Devices`, `Alphabet GOOGL US`, `Eli Lilly LLY US`,
`Quanta Services PWR`, `UnitedHealth Group UNH US`. All five resolve trivially against the SEC table
(AMD 2488, GOOGL 1652044, LLY 59478, PWR 1050915, UNH 731766). ⚠ The count moved DURING this session:
93 at 14:58Z (`2.0.0_SA_COO~X`'s census), 93 at 17:45Z, **94 at 18:0xZ** -- the directory is live and a
folder was added mid-measurement, so any count quoted without its clock is already wrong.

## Identity, as the pipeline currently stands

| | n | of 94 |
|---|---|---|
| resolved (carries a `security_key`) | **33** | 35% |
| NOT resolved | **61** | 65% |

## Documents

| | n | of 94 |
|---|---|---|
| holding at least one file | 93 | 99% |
| EMPTY | 1 | 1% |
| holding a FactSet ONE PAGER `.xlsx` | 49 | 52% |
| holding any `.xlsx` | 55 | 59% |
| holding any `.docx` | 52 | 55% |
| holding any `.pdf` | 76 | 81% |
| total files across all folders | 353 | -- |

The one empty folder is `Air Liquide AI FP`.

## The cross -- identity against documents (sums to 94)

| | n |
|---|---|
| resolved + has docs | 33 |
| resolved + NO docs | **0** |
| unresolved + has docs | **60** |
| unresolved + NO docs | 1 |

**So 60 of the 61 unresolved folders hold documents.** The identity gap is not a content gap.

## The resolver has exactly ONE input path, and this proves it

| | n |
|---|---|
| resolved + has a ONE PAGER | **33** |
| resolved + NO ONE PAGER | **0** |
| unresolved + HAS a ONE PAGER | **16** |
| unresolved + no ONE PAGER | 45 |

**Nothing has ever resolved without a FactSet ONE PAGER workbook -- 33 of 33.** That is the single
path, measured rather than read off the code.

⛔ **And 16 folders HAVE that workbook and still failed**, which is the sharpest actionable number here:
AstraZeneca, Canadian National, Clorox, Copa, JD.com, Michelin, Mitsubishi UFJ, Nestle, Nokia, Orange,
Rio Tinto, Sanofi, Schlumberger, Shopify, Tokyo Marine, Total Energies.

**WHY, and I had this wrong before I checked.** I expected a FORM rejection -- the workbooks write
FactSet style (`AZN-GB`, `NESN-CH`, `ORA-FR`) while the resolver wants Bloomberg style `<ROOT> <CC>`.
The data says otherwise: for 7 of 8 sampled, `bloomberg_ticker.value` is **None** and the status reads
`UNRESOLVED` -- **the resolver's scan found NO ticker cell at all**, where an independent scan this
session found one in each. Only `Schlumberger SLB` shows the form rejection I predicted (*"the
identifier 'SLB' carries no exchange code (expected '<ROOT> <CC>')"*).

⚠ **So the gap is in the SCAN step, not the validation -- and the discriminator between "the scan is
narrower than mine" and "those workbooks landed after the 2026-09-10 run" is NOT yet measured.** It is
one re-run of the builder to settle, and the builder must be re-run anyway because it is stale by five
folders.

## What closing the gap looks like from here

| arm | closes | evidence |
|---|---|---|
| workbook `Ticker:` cell | 17 | the cell is there and agrees with the folder |
| folder name + SEC ticker table | 20 | ticker parsed from the name, confirmed against a cik |
| ADR link to an existing universe line | 13 | already resolved on the HOLDINGS side |
| the 5 outside the snapshot | 5 | all US-listed, in the SEC table |
| **needs a human** | **2** | Manila Electric, Tokyo Electron -- no universe line, no 20-F |

Every arm above is a PROPOSAL. Nothing in this session was written to the universe or the crosswalk.
