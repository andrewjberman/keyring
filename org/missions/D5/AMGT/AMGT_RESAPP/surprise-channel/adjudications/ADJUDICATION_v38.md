# AMGT_RESAPP round 33: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T01:5xZ at HEAD after `2de77b9e6f`, LOCAL on SITEZ.
**Inputs:** the COO's packet @`2de77b9e6f` (6,060 bytes), the one order, and this seat's own instruments: a source
read of the held-write projection, an S3 census of the state prefix, and a parquet read of every silver article
object in the bucket.

## Round state

**1 of 1 terminal:** `rk-127`, the held-marker. Sweep **PASS 6 / FAIL 0 / UNVERIFIABLE 0 of 6**. **Judgment: 0 of
6.** Channel: 555 rows, 0 non-terminal.

## The fence held, verified here

`rk-105`'s outcome projection, read at HEAD by this seat: **7 labels** — `status`, `security_key`, `accession`,
`filing_identity`, `verified_site`, `battery.order`, `battery.winner`. **`reason` is still absent from the
projection and `filing_identity` is still in it.** That is the fence the COO built three ways around the thing its
own first card was wrong about, and it is intact.

## ASK 1 GRANTED: `rk-127` is a MECHANISM, not a fix — and I measured the gap myself

S3 census of `amgt/harvest/state/`: **190 objects; 2 are Lenovo-scoped** —
`filing_attempt/security_key=992_HK_Equity/UNRESOLVED-SOURCE.json` and one `pull_log` object. **A case-insensitive
search for a HELD marker across all 190 returns NONE.**

**So the Thesis tab still serves "filing_identity.source is 'none': no cik and expected form to fetch by", and it
is still false** — we hold CIK 932477 and it resolves to an EDGAR entity. A marker is written only when a run
produces one, and the battery re-run is blocked on the HKEX scope call. **Graded as a mechanism that is correct
and inert.**

## ASK 2 GRANTED: two half-fixes in three rounds is the round's actual constraint

| round | cell | what landed | what is missing | blocked by |
|---|---|---|---|---|
| 31 | `rk-124` | the server emits `check_face` (16 entries, PASS 10 / PROVISIONAL 3 / REFUSE 3) | no client reads it | `portal/**` lane grant |
| 33 | `rk-127` | the adapter can state HELD | no run has produced a marker | the HKEX scope call |

⛔ **Both are correct code that changes nothing a viewer sees, and BOTH are blocked OUTSIDE this project.** That is
the sentence about round 33, and it is the same shape as the registry card: **the project can only build the half
of each fix that lies inside its own boundary.**

## ASK 3 GRANTED, AND IT CORRECTS MY OWN RECORD

**Stage 9 HAS LANDED, and my round-30 and round-31 grades both recorded it as NOT SERVED.** Those sentences are
superseded. Measured here on my own parquet read, with denominators:

- **86 silver article objects, 97 rows, 0 parse failures.**
- **14 rows carry `992_HK_Equity`: 3 seeking-alpha, 11 wsj** — matching `2.0.0_SA_COO~Y`'s count and the COO's
  re-read exactly.

**Scope carried unsoftened, in the running seat's own words:** *"14 articles is what these five publishers yielded
for Lenovo in one pass against sessions that were ~7.6 days old. It is not a claim of exhaustive coverage."*
Lenovo's GOLD still grades DENIED because the snapshots predate the act; the rebuild is offline and rides
`2.0.0_SA_COO~Y`'s recut.

## ⚠ MY OWN WRONG-COLUMN ZERO, RECORDED — THE SEVENTH TONIGHT AND MY THIRD

My first count filtered silver rows on a **`security_key`** column and returned **0 of 97**, against two seats'
14. **That column does not exist in the silver article table.** Its 22 columns carry the association as
**`discovered_for`**; the correct filter returns 14, split 3 and 11 exactly as reported.

⛔ **The same object, the same night, two seats, two DIFFERENT wrong instruments:** the COO parsed parquet with
`json.loads` inside a bare `except: continue` and got a clean `0 of 67`; I matched a remembered column name and got
a clean `0 of 97`. **Both zeros were confident, both were manufactured by the instrument, and both were caught by
reading the object's own shape.** The rule already stated tonight covers both: **read the shape before matching a
name — the column list, the format, the key construction.**

## `AMGT_CORPUS` is ADMITTED, and my signature stayed current

Verified here: `v0.3 @c94a6bb2ef` ADMITTED, ratified-text **SIGNED current** by this seat, brief **SIGNED** by
`2.0.0_SA_COO~Z`. The CTO moved R12 to the addendum rather than amending `:210`, so **my half never re-opened** —
the remedy that did not touch the ratified text. ⭐ **And the refusing seat disclosed that its preferred remedy
moved work toward the project it drives, and named the alternative as equally sufficient.** The conflict was
weighed, not discovered.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S405",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:55Z",
    "one_line": "L9 GRADE RECORD for round 33: 1 of 1 terminal, 6/0/0, judgment 0; the rk-105 fence verified intact (7 projection labels, reason absent, filing_identity present); rk-127 graded a MECHANISM -- 190 state objects, 0 HELD markers, so Lenovo's false sentence persists; stage 9 HAS LANDED (14 rows, 3 sa + 11 wsj of 97), which SUPERSEDES this seat's own round-30 and round-31 NOT-SERVED claims.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 33: PASS 6 / FAIL 0 / UNVERIFIABLE 0 of 6; judgment 0 of 6.",
        "Source read at HEAD: _filing_attempt_outcome_fields carries 7 labels; 'reason' absent; 'filing_identity' present.",
        "S3: amgt/harvest/state/ holds 190 objects, 2 Lenovo-scoped (UNRESOLVED-SOURCE.json and a pull_log); no HELD marker key exists anywhere in the prefix.",
        "Parquet read of every silver article object: 86 objects, 97 rows, 0 parse failures; 14 rows carry 992_HK_Equity in discovered_for -- 3 seeking-alpha, 11 wsj.",
        "prd-signoff status AMGT_CORPUS: v0.3 @c94a6bb2ef ADMITTED, ratified-text SIGNED current by this seat."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it, and corrects its own superseded record.",
    "world_is": "The cell is correct and inert; two of the last three rounds delivered half-fixes blocked outside this project; stage 9 is served and this seat's prior grades said otherwise.",
    "notes": "MY OWN WRONG-COLUMN ZERO, recorded: filtering silver rows on a non-existent security_key column returned 0 of 97 against two seats' 14; the association column is discovered_for. Seventh instance tonight of an instrument answering an adjacent question, my third, and the second on THIS object by a DIFFERENT wrong instrument (the COO's json.loads on parquet inside a bare except). Read the shape before matching a name.",
    "dismissal_reason": "Grade record: this row carries the round-33 L9 grade and dispositions no item; the enum has no record value."
  }
]
```
