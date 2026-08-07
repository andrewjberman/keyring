# Briefing: Bronze timing-provenance census — the four clocks, and which feeds cannot detect a vendor restatement

**Date:** 2026-08-07
**Author:** `0.7.0_AE_CloudOps`
**Trigger:** the 09:00 ET Model Portfolio (MDPF) production cycle refused to build Cottonwood
**Scope:** every bronze dataset in the S3 bucket `s3://opal-data-assets`
**Status:** findings + recommendations. NOTHING WAS CHANGED. No gate edited, no schedule moved,
no code deployed.

---

## 1. Why this was written

At 09:00 ET today the Model Portfolio gold build fired on schedule for the first time
unattended, and refused to build the Cottonwood scope:

```
VALUE_DATE COLLISION WITH DIFFERENT DOLLARS at value_date=2026-08-05:
  {'2026-08-06': 133,821,362.30, '2026-08-07': 134,113,436.27}
-- a differing-dollars collision is a DATA QUESTION (drift between two runs valuing
   the same snapshot), never silently chosen and never averaged.
```
Raised at `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:280`.

Because Cottonwood is a required leg of the global composite, the global fold was skipped too.
Result: **6 of 12 objects built; `errors=['cottonwood','global']`.**

**Nothing bad was published.** The gate's `drop-rather-than-fabricate` behaviour held; the
served platinum objects under `s3://opal-data-portal-v2/platinum/mdpf/` remained at the
previous night's verified 03:52Z set.

Andrew's question — *"this should be a single path from a single data source, where would two
figures be coming from"* — is what this census answers.

---

## 2. What actually happened (measured, not inferred)

The path IS single. The **source described the same day twice and said something different the
second time.**

| Pipeline ran (partition) | Pulled (ET) | Valuing | Cottonwood Opal total |
|---|---|---|---|
| `date=2026-08-05` | 08-05 09:35AM | 2026-08-03 | $132,521,716.52 |
| `date=2026-08-06` | 08-06 11:51PM | **2026-08-05** | **$133,821,362.30** |
| `date=2026-08-07` | 08-07 09:00AM | **2026-08-05** | **$134,113,436.27** |

Directory: `s3://opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/`

Two separate problems, and **the second is the one that stopped the build**:

1. **The valuation date did not advance.** Friday's 9am pull is still valuing Wednesday.
2. **The same valuation date returned different dollars** — $292,073.97 apart.

### Which models moved, and the control group

Only **3 of 10** model portfolios changed. The other seven are identical to the cent.

| Model | Aug-6 delivery | Aug-7 delivery | Delta |
|---|---|---|---|
| Opal Short-Term | $16,582,075.21 | $16,702,033.32 | **+$119,958.11** |
| Opal Intermediate-Term | $76,344,673.23 | $76,464,631.33 | **+$119,958.10** |
| Opal Ultra Short-Term Income | $1,731,257.18 | $1,783,414.94 | +$52,157.76 |

Two portfolios of very different size ($16M and $76M) moved by the **same dollar amount, one
penny apart**. That is not a market-price signature — prices move a portfolio in proportion to
its size. An identical dollar delta across two portfolios is the signature of a specific holding
or transaction being booked into both.

### The cause, with its own control group

The raw vendor payload carries a Black Diamond–side modification timestamp. Comparing the two
deliveries at directory
`s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_model_detail/`:

```
MOVED (dollars changed):
  Opal Intermediate-Term        aug6 = 08-06 01:02:05AM ET -> aug7 = 08-07 01:01:54AM ET  CHANGED
  Opal Short-Term               aug6 = 08-06 01:02:04AM ET -> aug7 = 08-07 01:01:56AM ET  CHANGED
  Opal Ultra Short-Term Income  aug6 = 08-06 01:02:04AM ET -> aug7 = 08-07 01:01:56AM ET  CHANGED

DID NOT MOVE (control):
  Blended Opal / Satellite 50   07-29 09:23:00AM ET  ->  07-29 09:23:00AM ET   SAME
  Opal - Beecherl Legg          07-29 09:23:12AM ET  ->  07-29 09:23:12AM ET   SAME
  Opal - Cash + Satellite 50    07-29 09:23:55AM ET  ->  07-29 09:23:55AM ET   SAME
  Opal - Income                 07-29 09:19:44AM ET  ->  07-29 09:19:44AM ET   SAME
```

**Vendor timestamp advanced if and only if the dollars changed** — no exceptions in either
direction. The unchanged models are frozen at a July 29 stamp, which gave the test a control
group for free.

**Verdict: vendor-side restatement by SS&C, not an Opal pipeline defect.**

### A timing model that needed correcting

The prior working assumption — from the era of downloading CSV (comma-separated values) files by
hand — was that Black Diamond publishes between 12:00 and 16:00 ET. **On the API path that is not
what happens.** Measured across four consecutive pull days:

```
pull day     latest vendor updatedAt (ET)
2026-08-04   01:01:59 AM
2026-08-05   01:02:26 AM
2026-08-06   01:02:05 AM
2026-08-07   01:01:56 AM
```

A machine batch inside a ~30-second band, every day at ~01:02 ET. **Our 09:00 ET pull already
sits ~8 hours after it.**

> **Consequence: moving the Opal schedule will NOT fix this.** We are not pulling too early.
> SS&C revises prior-day values in an overnight batch **without advancing the valuation date**,
> and will do so again.

---

## 3. The general finding: four clocks, only one detects a restatement

Census of `s3://opal-data-assets`: **270,662 bronze objects → 53 distinct dataset shapes → 45
non-probe datasets → 45 of 45 sampled** (newest object per dataset).

Every timing field found falls into one of five kinds, and they are not interchangeable.

| Clock | Example fields | The ONLY question it answers |
|---|---|---|
| **A — when we pulled** | `pulled_at`, `pull_date`, `run_date`, `completed_at`, smartx `timestamp`, S3 LastModified | "When did we ask?" — our diligence, never their state |
| **B — what day it describes** | `as_of`, `dataDate`, `dataAsOfDate`, `asOfDate`, `snapshot_date`, `Rate Date`, Schwab `H1` field 5 | "What day is this about?" — the label, not its stability |
| **C — when the vendor last touched it** | `updatedAt`, `lastUpdate`, `editedDate`, `updatedOn`, `lastSeenDate` | **"Did they CHANGE something they already gave us?"** |
| **D — business event dates** | `Trade Date`, `Settle Date`, `Open Date`, `transDate`, `startDate`/`endDate`, `openDate` | "When did money move?" — a fact, not provenance |
| **E — our own coverage sidecars** | `_meta/holes.json`, `window-coverage-*.json`, `_BRONZE_COMPLETE.json`, `_retry_net` | "What did WE miss?" — our gap, not their revision |

**Clock A and Clock B were both present and both healthy this morning, and neither could have
detected the problem.** Only Clock C could, and only because this particular endpoint happens to
carry it.

---

## 4. The coverage gap — the actionable part

**Clock C is not universal, and its absence is invisible.** These feeds carry no vendor-side
mutation timestamp at all. If the vendor restates a day it already sent, nothing in the payload
can reveal it:

| Feed (directory under `s3://opal-data-assets/`) | A | B | **C** |
|---|---|---|---|
| `blackdiamond/cottonwood/bronze/allocations/` (.xlsx) | yes | yes | **NONE** |
| `blackdiamond/cottonwood/bronze/holdings/` (.xlsx) | yes | yes | **NONE** |
| `blackdiamond/cottonwood/bronze/unrealized/` (.xlsx) | yes | yes | **NONE** |
| `blackdiamond/cottonwood/bronze/realized/` (.xlsx) | yes | yes | **NONE** |
| `blackdiamond/cottonwood/bronze/transactions/` (.xlsx) | yes | yes | **NONE** |
| `blackdiamond/49f/bronze/reporting_{allocation,costbasis,performance}/` | yes | yes | **NONE** |
| `pathfinder/filepoint/bronze/{dailynav,holdings}/` (.csv) | yes | yes | **NONE** |
| `trueshares/{DIVZ,IDVZ}/bronze/netassets/` (.html) | yes | yes | **NONE** |
| `schwab/08242234/bronze/tcfx/` (nested .zip -> pipe-delimited) | yes | yes | **NONE** |
| `orion/inflection/bronze/{performance,transactions}/` | yes | yes | **NONE** |

Feeds that DO carry Clock C: `blackdiamond/cottonwood/bronze/rebalancer_model_detail/`
(`updatedAt`), `blackdiamond/cottonwood/bronze/rebalancer_models/` (`lastUpdate`),
`orion/inflection/bronze/{assets,positions}/` (`editedDate`),
`eclipse/inflection/bronze/_history/closed_trades/` (`editedDate`),
`smartx/account/*/bronze/detail/` (`updatedOn`),
`smartx/allocation/*/bronze/holdings/` (`lastSeenDate`),
`smartx/platform/bronze/nonzerosleeve/` (`asOfTimestamp`).

> **Today's catch was luck of the feed.** `rebalancer_model_detail` is an API endpoint that
> happens to carry `updatedAt`. The five Cottonwood **spreadsheet** feeds sitting beside it in the
> same bronze tree carry nothing equivalent — a silent restatement there would be
> indistinguishable from a normal day.

---

## 5. Why the raw payload was still there to read

`CLAUDE.md` Rule 17a: **bronze is raw and untouched, byte-for-byte as the source delivered it.**

Nobody trimmed the Black Diamond API response at ingest to "just the fields we use." That is the
only reason `updatedAt` was still on disk months later, when it turned out to be the field that
answered the question. Had bronze been slimmed at ingest — the exact thing Rule 17/17a prohibits —
this morning's failure would have been unattributable, and the likely conclusion would have been
"our pipeline is flaky."

**No egress was spent.** Andrew granted vendor-API egress for the session; it was not needed,
because the stored raw payload already contained the answer.

---

## 6. Recommendations — decisions, not actions taken

1. **Use Clock C as the collision discriminator where it exists.** Today the gate calls a
   differing-dollars collision "a data question" because two numbers appear with no principled way
   to choose. `updatedAt` answers it: the later vendor stamp is authoritatively newer. That
   converts *refuse and stop* into *take the newer value AND record that the vendor restated* — a
   grounded choice with an audit trail rather than a silent one.
   **This changes a gate the CTO ruled (`CTO condition 1, 234639Z`). It is a decision, not a
   cleanup.**

2. **Decide whether Cottonwood restating a closed day is normal for SS&C.** If it is, this gate
   will trip regularly and needs a standing rule. If it is not, the $292,073.97 restatement is
   worth a question to the vendor. This is a business judgement, not an engineering one.

3. **Treat the ten Clock-C-less feeds as a known blind spot.** They are not broken; they are
   undetectable. Anything derived from them cannot answer "has this been revised?" — and no
   instrument currently says so at the point of use.

4. **Do not move the Opal schedule in response to this.** The 09:00 ET pull is already ~8 hours
   after the vendor's ~01:02 ET batch. Rescheduling addresses a cause that is not operating.

5. **Separately open the value-date staleness question.** Friday's 9am pull valuing Wednesday is a
   distinct issue from the collision and is not addressed by any of the above.

---

## 7. Honest limits of this census

- **One newest file per dataset.** A dataset whose payload shape changed over time would show only
  its current form.
- `smartx/allocation` is 240,301 of the 270,662 objects — one dataset, one sample. Its `/data/asOf`
  and `/timestamp` are consistent in the file read, not proven across all of them.
- Schwab `.TCFX` is a nested zip containing a pipe-delimited fixed-format file. The `H1` header
  record and the `H2` column legend were read; the full record specification was not.
- The 13,364 `.zip` and 4,730 `.gz` objects were not opened beyond one member / one line each.
- The correlation in section 2 is between `rebalancer_model_detail` (where the vendor timestamps
  live) and the dollar column of `dim_model_portfolio`. The match is exact — 3 for 3 with a clean
  control group — but the two artifacts were not formally linked in code. **This should be closed
  before anyone changes a gate on the strength of it.**

---

## 8. Reproducing this

The census scanner is at `.scratch-bronze/scan.py` (DIRECTORY `.scratch-bronze/` is untracked
scratch, not a landed tool). It reads a manifest of one newest object per bronze dataset and
extracts timing fields across `.json`, `.jsonl.gz`, `.csv`, `.xlsx`, `.zip` and `.html`.

**It has NOT been promoted to a comp-tool or a standing check** — per `CLAUDE.md` BUILD LADDER
rung 1, that would need to be asked for. If a recurring "which feeds can detect a restatement"
check is wanted, that is a small build on top of this and a decision for the CTO to route.

Two operational notes banked while building it, both the documented MSYS argument-mangling class:
- `aws s3 cp` to a `/cygdrive/c/...` absolute destination **fails silently** — the file never
  lands and the command reports success. Relative-under-cwd and `C:\...` both work.
- A manifest written by native Windows Python carries CRLF; read from bash, every S3 key acquires
  a trailing `\r` and every download 404s.
