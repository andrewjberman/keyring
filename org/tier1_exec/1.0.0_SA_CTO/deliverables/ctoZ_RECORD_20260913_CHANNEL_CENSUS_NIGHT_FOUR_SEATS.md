# RECORD -- the channel-census night: what four seats measured, and the one carrier that was missing

**Landed by `1.0.0_SA_CTO~Z`, 2026-09-13 ~01:5xZ.** A RECORD, not an analysis. It exists because
`2.0.0_SA_COO~Z` said this in terms (msg 22074):

> *"THIS MESSAGE IS THEREFORE A SESSION-ONLY ITEM UNLESS ONE OF YOU LANDS IT -- said plainly because
> that is the silent-hole shape, and I would rather name it than let it be discovered."*

It named `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z`. This is that landing. **Nothing here is new work,
no seat is asked for anything, and no number below is this seat's own except where marked.**

---

## 1. WHAT HAPPENED, IN ONE PARAGRAPH

Over roughly ninety minutes, four seats each measured how many surprise-channel obligations name
them as `disarm_owner`. Every one had been reporting a number an order of magnitude too small, every
one found it in **itself**, and no gate fired on any of them. The cause is one property of the
surface: **channel obligations live in three plane directories across two roots, and every reader
defaulted to one.** Then the corrections themselves committed the same error twice more.

## 2. THE MEASUREMENTS, WITH THEIR OWNERS AND THEIR OWN LIMITS

| seat | had been reporting | measured | domain of the measurement |
|---|---|---|---|
| `2.0.0_SA_COO~ZZZ` | 9 carried obligations | 30, then **53** | two documents, then the AMGT channel |
| `1.0.0_SA_CTO~Z` | 3 armed rows | 16, then **104** | AMGT channel, then both roots, repaired parser |
| `4.0.0_SA_CRO~Z` | **none** (stated to Andrew, more than once) | **5** | both roots, all planes, 2293 rows |
| `2.0.0_SA_COO~Z` | ~1 | 54 on POSN, then **149 / 113 armed** | POSN tree, then both roots |

⛔ **Every figure above is a CANDIDATE count.** `hazard_standing` is set at surfacing and is
immutable, so none of these is a live-obligation count and no seat has claimed otherwise.

## 3. THE FOUR INSTRUMENT DEFECTS, EACH FOUND BY ITS OWN OWNER

1. **One plane of three.** Readers globbed `investigations/` and reported on "the channel".
   Obligations also live in `adjudications/` (where the CVO files dispositions by design) and
   `remediations/` (where remedy rows live by design).
2. **One root of two.** A sweep partitioned by plane directory **structurally cannot reach the
   legacy flat channel**, whose 25 files sit directly under the project code with no plane subdir.
   `0.0.0_AB_MSTR~Z` stated both roots and executed one -- *inside the broadcast warning about
   wrong domains* -- and corrected itself when `4.0.0_SA_CRO~Z` and `2.0.0_SA_COO~Z` both caught it
   within minutes. Headline moved from 12 of 63 to **12 of 88 = 14%**.
3. **A regex that could not see nested objects.** `2.0.0_SA_COO~Z`'s first census returned **ZERO**
   because its pattern matched only brace-free row blocks. A proper JSON parse over the same seven
   files returned 54. ⛔ *A census that returns zero is the most dangerous result an instrument can
   give -- a wrong non-zero gets argued with; a wrong zero reads as all-clear and gets acted on.*
4. **First-bracket-to-last, on multi-fence files** -- **this seat's**. A channel file is no longer
   one fenced block, so that span crosses a second fence and the **whole file** fails, surfacing as
   29 awkward unreadable files rather than ~1,200 missing rows. Per-fence parsing takes this seat
   from 1,075 rows / 29 unreadable / 85 ids to **2,262 / 3 / 104**, reconciling against
   `4.0.0_SA_CRO~Z`'s 2,293 with a residual of exactly the three files still unread, all named.
   **648 fenced blocks across 88 files: the average channel file carries seven, not one.**

## 4. THE COMMAND, AS CORRECTED BY THE SEATS THAT GOT IT WRONG FIRST

```
org/missions/D*/*/*/surprise-channel/*/*.md    AND    org/surprise_channel/*/*.md
```
- **Do NOT partition by plane directory** -- that is exactly what the legacy root lacks.
- **Parse each FENCED BLOCK separately**, not first-bracket-to-last, and not by regex.
- **Print the FILE count, the ROW count, the DISTINCT-ID count and the UNPARSEABLE count.** A census
  that reports rows without reporting what it could not read is asserting completeness it did not
  measure.
- **Positive control:** `disarm_owner` must spread over many owners. A uniform answer is also the
  shape of a broken field. Measured: 79-163 distinct owners depending on the sweep.
- **`4.0.0_SA_CRO~Z`'s addition, adopted:** print DISTINCT IDS beside the row count. *The id is the
  item; the plane is a facet; a row count is not an obligation count.*

## 5. THE THREE SENTENCES WORTH KEEPING

⭐ **A number repeated verbatim each tick reads as re-measured.** Every one of these was CORRECT when
first derived. Nothing decays visibly, nothing errors, and the stale figure arrives wearing the same
confidence as a fresh one. *That is why "be thorough" is not the fix and a re-run trigger is.*

⭐ **A scope sentence written over the wrong domain is precise about the wrong thing.**
(`4.0.0_SA_CRO~Z`, on its own carefully-scoped disarm row, which could not have named a graduated
twin because the read behind it never reached that plane.)

⭐ **A correction is written in the vocabulary of the thing it corrects, so it inherits the
surrounding frame and misses the field next door** -- and a corrected report is trusted MORE than the
one it replaced, which is what makes the residue expensive. (`0.0.0_AB_MSTR~Z`, on doing it twice in
one night.)

⚠ **And the omission direction is the one that bites:** an obligation absent from its owner's own
list is an obligation **no cell is written for**, and nothing downstream would notice. The surplus
direction merely wastes a read.

## 6. WHAT IS NOT CLAIMED, AND WHAT IS STILL OPEN

- **No live count exists for any seat.** Every figure is at-surfacing. Reading each id to a standing
  is per-seat work and only `1.0.0_SA_CTO~Z` has done it, for AMGT_RESAPP alone (12 read: 2
  discharged, 10 live).
- **No rate is claimed** for how many of the estate's rows are stale, and nobody has censused
  `3.0.0_SA_CVO~Z`.
- **Three files still fail this seat's parser:** `AMGT_RESAPP/.../ADJUDICATION_v5.md`,
  `org/surprise_channel/ADVI_49F/INVESTIGATION_v1.md`, `org/surprise_channel/D1_CATVIEWS/
  INVESTIGATION_v1.md`.
- **Twenty-nine ids carry no `project` field at all** in this seat's sweep -- named, unresolved.
- **`2.0.0_SA_COO~Z` holds 94 ids outside its own project and is deliberately not chasing them.**
  That is the correct call and it is recorded here so the decision is visible rather than silent.
- **Owed by this seat:** read POSN_ASTTAX's twenty-five and record each
  DISCHARGED-with-citing-row or LIVE-with-condition.

⛔ **NO REMEDIATION IS PROPOSED AND NONE IS AUTHORIZED.** Andrew's 02:22Z priority ruling stands:
*"no it should not disrupt from the work of the fabric."* Round 8 is mid-flight. This is a record so
that the next seat does not re-derive it, not a work item.
