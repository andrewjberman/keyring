# L4-R review -- AMGT_CORPUS PRD v0.1, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` @`03918b5b3e`. **Half:** ratified-text, hash
`f00abf5e5303`. **Delivery:** `1.0.0_SA_CTO~Z` msgs 24365, 24366.
**Verdict: REFUSE.** Two defects, both bounded, both in what this half depends on. The design is sound and I say so
below; the CTO asked for a refusal to be cheap at v0.1, and these are cheaper now than at a cell.

## R1. The `brief_ref` pin does not resolve. Every SOURCE line in this half points through it.

`brief_ref` is `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md@42c05cd8a8`.

```
$ git cat-file -e 42c05cd8a8:docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md
fatal: path '...' exists on disk, but not in '42c05cd8a8'     rc=128
```

**Positive control, same commit, a different brief:** `42c05cd8a8:docs/briefs/amgt-resapp-security-analysis-20260910.md`
resolves rc=0. So the instrument is sound and the pin is wrong.

The brief was ADDED at `578f7072d1` ("brief(AMGT_RESAPP L1 MIDSTREAM, 4.0.0_SA_CRO~F): the Claude analysis layer"),
where it resolves and reads 35,894 bytes. `42c05cd8a8` is a drain of a different CRO branch.

This is not a header nit. Nine of nine FWDs in this half carry a `SOURCE` line citing the brief by outcome id or
part, and a reviewer who follows the PRD's own pointer to check one gets `rc=128`, not the text. **Fix:** re-pin to
`578f7072d1` (or to the commit at HEAD that carries the intended bytes), and state the byte count so a later reader
can tell a re-pin from a rewrite.

## R2. The Rule 24 record contradicts itself on O9, and the cover message contradicts the PRD

The PRD's subtraction record (`:184-190`) says: *"O9 is the addendum's (report versioning)"*, and closes with
*"13 brief outcomes -> 7 wholly the addendum's, 4 split, 2 wholly here, plus 1 minted = 9 FWD."*

The cover message says: *"2 wholly here (O9's reachability half, O13)"*.

Both cannot hold, and the PRD's own line does not add up on its own terms:
- wholly the addendum's, as the body names them: O1, O3, O6, O7, O10, O11, O12, **and O9** = **8**, not 7;
- split: O2, O4, O5, O8 = 4;
- wholly here: **O13 alone** = 1, not 2.
- 8 + 4 + 1 = 13, so the arithmetic closes only by moving O9 out of "wholly the addendum's".

**I ran the subtraction the other way, as asked** -- from the brief's own outcome list at `578f7072d1`, where all
thirteen headings O1..O13 are present, against BOTH carriers:

| brief outcome | where it lands | covered? |
|---|---|---|
| O1, O3, O6, O7, O10, O11, O12 | addendum | yes |
| O2 (measured half FWD-5), O4 (FWD-6/FWD-7), O5 (FWD-1/2/8), O8 (FWD-8) | split | yes |
| **O9** (prior report beside the current one) | **SPLIT in fact**: its reachability half is FWD-1/FWD-2/FWD-8 here; its rendering and versioning half is the addendum's | yes, but MISLABELLED |
| O13 | FWD-3 + FWD-4 here | yes |
| FWD-9 | minted, in no brief outcome | n/a |

**So no outcome is uncovered, and the endpoint itself is not missing a member.** The defect is in the RECORD, which
is the artifact a later seat reads when it asks whether the seam leaks. As written, O9 is assigned wholly to the
addendum in the PRD and wholly here in the cover, so a reader of either could conclude the other carrier owns the
corpus-side half and neither would fail. That is precisely the green the CTO named. **Fix:** state O9 as SPLIT with
its two halves named, and re-state the closing count as 7 wholly the addendum's, **5** split, 1 wholly here, plus 1
minted = 9 FWD.

## FWD-9, the mint: ACCEPTED as an outcome, and argued

A read-only constraint nobody exercises is a belief, and `C-CORPUS-READ-ONLY` alone would make it one. FWD-9's
DONE WHEN is a live negative control (the ingestion completes against a read-only copy) PLUS a code census with its
denominator. Those are two different instruments, and the second can see what the first cannot: a write path that
exists but did not fire on that run. Keep it as an outcome. Its ACCEPT sentence -- *"we can prove it rather than
assert it"* -- is the right standard for a file someone else's team owns.

## What holds (stated so it can be falsified cheaply)

- **Rule 30.** The PRD types no address. I ran `lib/opal_naming.py address()` for all **8 store-writing manifest rows**
  (R1-R4, R6-R9). **8 of 8 print, 0 refuse**, all under `s3://opal-data-harvest/amgt/harvest/...` at the scope, tier
  and partition named. R5, R10, R11 and R12 write no store.
- **No FWD is a wait.** Every DONE WHEN is an act a seat starts: a run, a query, a single induction command, a
  negative control. There is no scheduled fire and nothing is qualified as a wait.
- **The contracts carry their own falsifiers.** `C-FOLDER-LIST-IS-THE-DENOMINATOR` (fresh read, never a transcribed
  list, `0 of N` printed even when empty) is Andrew's ~18:3xZ word written as a mechanism.
  `C-TEMPLATE-IS-MEASURED` and `C-CITED-OR-ABSENT` make every derived artifact refutable against a named passage.
  `C-IDENTITY-VIA-THE-LAYER` forbids a second identity mechanism, which is the right call against this estate's
  history of parallel key paths.
- **`C-LOCAL-AND-DEVICE-DERIVED`** refuses loudly on a device without the library instead of reporting an empty
  corpus. That is the device-axis failure this estate has hit before, written as a contract.

## Carry items (not refusal grounds)

1. **Read surface for R1/R2.** Report bytes land in `opal-data-harvest`, the pool the page's adapter reads.
   `C-TIER-PLACEMENT` says the platinum report object is the addendum's, but nothing in this half says who may READ
   the raw report bytes, and these are the team's internal documents. One sentence naming the read surface (and that
   the page never serves bronze report bytes) would close it.
2. **`C-TIER-PLACEMENT` calls gold "firm-attributable"**, while the builder prints the GENERAL harvest home for
   every tier. That is conformant today, because the builder is the authority under Rule 30, but the sentence and
   the output describe different tenancies. Either cite the harvest-home decision or drop the attribution phrase.

-- `3.0.0_SA_CVO~Z`
