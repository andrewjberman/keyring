# ANDREW-DIRECT 2026-08-24 ~23:0xZ -- THE PROVIDER'S "AS OF" IS THE PROVENANCE STAMP, AND IT IS MAINTAINED FROM BRONZE INGESTION ONWARD

**Seat:** `1.0.0_SA_CTO~Z` (site Z) · **Recorded + broadcast same turn** · Lands directly on
`ETFS_INGEST-Z-S16`, open and BLOCKING at the time of his word.

## HIS WORD, VERBATIM AND COMPLETE

> *"Yes it is crucial that appropriate timestamps are measured when presenting infromation, all
> downloaded information from the providers platforms (trueshares and pathfinder) should have some
> kind of "as of" field so it is clear when that data is from, that needs to be what is used for any
> date stamping on provenance. it is fine to track metadata of when we've updated data or performed
> operations on it, but that is a very different figure than the actual data "as of" provenance
> timestamp. Just something that needs to be accounted for and maintained from bronze ingestion
> onward"*

## WHAT IT RULES

| # | ruling |
|---|---|
| 1 | **Every provider download carries an "as of" field** -- named for both channels, TrueShares AND Pathfinder. |
| 2 | **The PROVIDER's as-of is what date-stamps PROVENANCE.** Not our run date, not our partition key, not our selection target. |
| 3 | **Our operation metadata is legitimate AND is a different figure.** Tracking when we updated or operated on data is fine; it is never the provenance stamp. **Two fields, never collapsed.** |
| 4 | **Maintained from BRONZE INGESTION ONWARD** -- the whole chain, not one tier. |

**This SUPERSEDES-BY-RATIFYING my §5 spec reading of two hours earlier** (*"`date` should be the
issuer's delivered holdings date, `data_as_of` may legitimately differ per issuer, and the two must
never be silently collapsed"*), and it **WIDENS** it in two ways I did not have: the provider's
as-of is named as *the* provenance stamp rather than merely a field to preserve, and the obligation
is stated as a chain property from bronze onward rather than a silver-layer cell.

## MEASURED AGAINST THE LIVE ESTATE, 23:0xZ -- AND THE SHAPE OF THE GAP IS THE USEFUL PART

**THE SERVING END ALREADY IMPLEMENTS HIS CONTRACT. Nobody needs to build it.** Census of every
date-bearing field in the live served payload (`platinum/etfs/positioning_data.json`, 76,149 B):

```
generated_at   2026-08-24T23:00:44Z   <- OUR OPERATION TIME       (his "metadata", correctly separate)
data_as_of     2026-08-21   (n=5)     <- THE DATA'S AS-OF          (his "provenance stamp")
data_date      2026-08-21
prior_date     2026-08-20   (n=4)
```

⛔ **THE DEFECT IS AT THE SOURCE, EXACTLY WHERE HIS WORD PUTS THE OBLIGATION.** The served
`data_as_of` is correct in SHAPE and, for TrueShares rows, will be wrong in VALUE:

```
BRONZE   divz_holdings.csv   Date = 8/24/2026 on EVERY row   <- the provider's own as-of, PRESENT
SILVER   those same rows     date = data_as_of = 2026-08-21  <- the NET-ASSETS PAGE as-of, substituted
                                                                (lambda_function.py :526 -> :902)
         filepoint rows      date = data_as_of = holdings Date  <- CORRECT BY CONSTRUCTION (:612 -> :665)
```

**The provider's as-of is in the bytes we store and silver overwrites it with a different
measurement.** Filepoint is correct by construction and needs no change (DS~Z, source-confirmed);
the value defect is TrueShares-only.

## ⏰ THIS HAS A CLOCK ON IT, AND TONIGHT IS WHEN IT IS CHEAP

**Today the defect is INVISIBLE at the serving end**: DIVZ and IDVZ are `book_only` shells with 0
holdings, so no TrueShares row reaches `data_as_of`. **Tomorrow's 13:00Z fire selects T-1 = Monday
2026-08-24 and those 73 rows flow through** -- at which point the served provenance stamp for two of
four funds carries a date the provider never asserted.

⚠ **And the failure is the silent direction:** a wrong `data_as_of` does not error, does not change
a byte count, and reads as a plausible date. **It is the false-outage generator NEVER#1 exists to
prevent, pointed the unusual way -- the rows would look stale because WE stamped them so.**

## SEPARATELY MEASURED, AND IT BEARS ON HIS "different figure" CLAUSE

The served body is **fully deterministic except for one field**. Diffing tonight's published object
against DE~Z's pinned 12:30Z baseline: **identical length (76,149 B both), different sha256, and
exactly ONE differing leaf -- `/generated_at`** (`12:30:42Z` -> `23:00:44Z`).

**So the operation timestamp is the sole source of non-reproducibility in the served artifact** --
which is fine under his ruling (metadata is legitimate), but has a consequence worth stating: **a
size-based comparison reports "unchanged" on an object that demonstrably changed.** COO~Z's decision
earlier tonight to reject a matching 76,149 as *"suggestive"* and verify on sha256 is what makes
that measurable rather than a guess.

## Grounding

Bronze CSV read at source (both funds, all rows, distinct `Date` = `8/24/2026`); silver partition
read via pandas (187 rows, 4 funds); served payload downloaded and diffed field-by-field against the
git-tracked pin; `:526`/`:902`/`:612`/`:665` source-confirmed by DS~Z and re-derived at this seat.
