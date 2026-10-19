# RESEARCH 2026-10-19 -- NFRA_FIDUPL: Fidelity G numbers and the firm split (read-only)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Asked by:** 1.0.0_SA_CTO~DELL1 msg 8470 | **Order:** Andrew-direct ~19:0xZ (relay
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md`): "We need to assess the
structure of this, if there are clear differentiated masters that tie to different firms, or if there is just one".
**Inputs:** the three HARs and five export files already on dell1. There was no new sign-in. G number values are not printed here; each
is counted and shown by its label only.

## 1. How many G numbers this login sees: 31 (measured)

**Source:** `GET /ssc/worklist/wc/channel/worklist/criteria-fields.json`, section "Access Attributes", field `gnumber` ("G Number(s)",
MultiSelectLookUp). It lists 31 options. Every value has the form `G` followed by 8 digits, and each carries a `description`. The login's
default (`defaultGNumber.json`) is the one labelled ALONGSIDE, LLC. HAR2 shows the same 31; HAR3 shows only the default.

| Label (`description`) | G numbers | In Opal's registry? |
|---|---|---|
| ALONGSIDE, LLC (the login's default) | 1 | `alongside` (FIRM, landed bd84d81948) |
| COTTONWOOD CAPITAL ADVISORS (PRIMARY, SECONDARY, SHIPLEY, RUBOTTOM, BASS, ADVISOR PAYS, unlabelled) | 7 | `cottonwood` |
| INFLECTION WEALTH MANAGEMENT | 5 | `inflection` |
| 49 FINANCIAL | 1 | `49financial` |
| KEIL FINANCIAL PARTNERS (team and per-advisor) | 5 | **no** |
| ABIDING WEALTH PARTNERS | 4 | **no** |
| LIGHTHOUSE WEALTH PARTNERS | 4 | **no** |
| VM WEALTH PARTNERS | 3 | **no** |
| one labelled with an individual advisor's name only | 1 | **no** |
| **Total** | **31** | 13 map to three registry firms, plus 1 umbrella; 17 map to no registry firm |

**Each G number's label names exactly one firm** (measured from the `description`). One Cottonwood label is misspelt "CAPTIAL"; it is
the same firm. So at the G-number level the answer to Andrew's question is **"clear differentiated masters that tie to different firms"**,
plus one umbrella G number for Alongside.

## 2. Which export field carries the G number: none of the files on hand (measured)

| File (Standard Format A, 2026-10-16) | Rows / accounts | Tokens matching a login G number |
|---|---|---|
| `FI101626.naa` (accounts) | 5,007 accounts | **0** |
| `FI101626.ipn` (positions) | 97,438 rows, 4,873 accounts | **0** |
| `FI101626.trn` (transactions) | 401,593 rows, 4,955 accounts | **0** (2 G-shaped tokens, neither a login G number) |
| `prices.txt` (custom) | 2,464 | **0** |

**Denominator: 0 of 5,007 accounts carry a G number in the files on hand.** Accounts per G number therefore **cannot be measured**
from them.

- The one `.naa` field shaped like an identifier (`[26:36]`, a letter plus 9 digits) is unique per account (5,007 distinct). So it is
  not a grouping key.
- No other `.naa` field, and none of the `accountList.json` fields, groups accounts by firm. `regRep` has 2 values; `fbsiShortName` has
  1,034.
- The custom `account.txt` (141 columns) was never handed over. The `status.json` row for it lists no column names. **It may carry a
  G number column; that is unmeasured.**
- The per-account API (`verify.json`) carries `gnumberAssociations`, an empty list on the one account captured. That is a per-account
  call, so it is not a way to attribute 4,959 accounts.

## 3. What this means for the landing (inferred; the CTO rules)

- **The per-firm homes already resolve.** No new rows are needed for Opal's three firms:
  - `address('fidelity','inflection','bronze',...)` returns `s3://opal-data-assets/fidelity/inflection/bronze/...`
  - `address('fidelity','cottonwood','bronze',...)` returns `s3://opal-data-assets/fidelity/cottonwood/bronze/...`
  - `address('fidelity','49financial','bronze',...)` returns `s3://opal-data-assets/fidelity/49financial/bronze/...`

  All three were measured this turn.
- **Direct per-firm landing needs per-firm FILES, not just per-firm G numbers.** One export profile covers the whole Alongside book, and
  its standard files carry no G number. So the export cannot be split by field today. There are two candidate mechanisms, both
  unmeasured:
  - **(a) One scheduled export profile per firm, filtered to that firm's G numbers.** The export wizard's step 3 "Choose Filter" was
    never captured, so whether it offers a G-number filter is unknown. If it does, each profile's files land straight at
    `fidelity/<firm>/bronze` and no split is needed.
  - **(b) A G-number column in the custom `account.txt`.** If it is there, the full pull stages under `fidelity/alongside` and is split
    on that column.
- **Until (a) or (b) is measured, stage under `fidelity/alongside`.** This is Andrew's stated fallback: "use alongside as a staging bucket
  for the full pull, and afterward we effectively parse out".
- **The book contains firms Opal has no registry row for (17 of 31 G numbers).** These are Keil, Abiding, Lighthouse, VM and one
  advisor-named G number. Their accounts are inside the same full pull. Whether Opal lands, keeps or discards another firm's client data
  is not a split detail. It touches the cross-firm rule, and it is **Andrew's to say**. Option (a) avoids pulling those accounts at all.
  The split under option (b) would still stage them under `fidelity/alongside`.

## 4. The two reads that settle it (a person in Wealthscape, about 2 minutes each)

1. Open the Export Custom wizard, step 3 "Choose Filter", and see whether "G Number" is a filter.
2. Hand over the custom `account.txt` (or a screenshot of its column list from step 2) to see whether a G number column exists.

## 5. Registry act this turn

The `alongside` row note gains one line, as the CTO asked in msg 8474: `opal-data-alongside` is never provisioned, and Fidelity lands in
opal-data-assets. **No per-firm or per-G-number rows are added.** The firm scopes already exist, and MASTER rows for G numbers would be
built before anything lands per G.
