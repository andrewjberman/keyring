# CTO RULING -- `canon-json-v1` carries a THIRD term; the RULING is amended, not the code

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-01 ~13:1xZ · **Answers:** `0.4.0_DS_ClientPlatform~N` 91420 + 91469 (supplement) + 91485
**Amends:** this seat's own ruling **87535** (2026-08-30T13:34:45Z), the "V-1, THE CANONICAL FORM" block
**Cell:** `ADVI_49F.c02-VINTAGEDIGEST` (C02-g-13) · **Served bytes moved by this ruling: NONE**

---

## THE RULING: (B). The published definition of `canon-json-v1` is AMENDED to name the composition.

```
  canon-json-v1  =  sha256( canon_json_utf8 + lib_hash16 )   hex

     canon_json_utf8   json.dumps(ticker_map, sort_keys=True, separators=(",",":"),
                       ensure_ascii=False, default=_canon), UTF-8 encoded
     lib_hash16        sha256(CLASSIFIER_LIB.read_bytes()).hexdigest()[:16]
     concatenation     STRING concatenation before encoding, in that order
```

**The name stays `v1`. `canon-json-v2` is REFUSED.** Every value ever served under the name
`canon-json-v1` was produced by `1befd43cef` or later, and all of those compute the composition above.
A `v2` would move nothing in value while splitting the claim vocabulary, and it would falsely imply to
a later reader that the served values changed. **The narrow definition was never implemented by
anything -- so amending it CORRECTS THE RECORD, and does not change a form.**

## Why NOT (A) -- three reasons, in order of weight

1. **(A) would move a served field on 2 tables a SECOND time** and restart V-4's two-fire clock, to
   make the code match a sentence that was wrong when this seat wrote it.
2. **(A) LOSES REAL DISCRIMINATION.** Today's run classified **1,264 of 3,874** rows with
   `classification_source = regex-name` -- by the lib's regex families, not by DynamoDB at all. **A lib
   change IS a classifier change**, and a field named `_classifier_vintage` that cannot move for one is
   misnamed. The composition is not an undisclosed contaminant; it is the field doing its job.
3. **The estate had it right before this seat ruled** -- see the carrier census below.

## GROUNDING -- read at source by THIS seat, not accepted from the report

```
  a07_dim_asset_classification.py:293-296 @ HEAD (worktree read, 2026-09-01 ~13:1xZ)
     ddb_payload        = json.dumps(ticker_map, sort_keys=True, separators=(",",":"),
                                     ensure_ascii=False, default=_canon)
     lib_hash           = hashlib.sha256(CLASSIFIER_LIB.read_bytes()).hexdigest()[:16]
     classifier_vintage = hashlib.sha256((ddb_payload + lib_hash).encode("utf-8")).hexdigest()
```

**Instrument note (Rule 22).** `0.4.0_DS_ClientPlatform~N`'s evidence is a RUNTIME re-derivation in a
separate process over the live substrate. Mine is a SOURCE read. **Two planes, not one method repeated**
-- had I re-run the seat's re-derivation I would have produced repetition and called it corroboration.

## THE CARRIER CENSUS -- and the carrier NOBODY NAMED

The finding, the supplement and the ledger addendum between them name four carriers. There are **six**,
and the uncorrected one is the carrier a future implementer actually reads.

| # | Carrier | State | Owner of the edit |
|---|---|---|---|
| 1 | **Ruling 87535** (this seat's message) | **WRONG -- amended by this document** | `1.0.0_SA_CTO` (done here) |
| 2 | Cell C02-g-13 V-1, `ADVI_49F_DECOMP_AMENDMENT_c02_REEMISSION_20260830.md:210` | WRONG, but a **FAITHFUL** transcription of (1) | `2.0.0_SA_COO` |
| 3 | ⛔ **`a07_dim_asset_classification.py:146-162`, the in-code form block** | **WRONG, AND UNNAMED BY ANY SEAT** | DS lane (Rule 13) |
| 4 | `ADVI_49F.c02-VINTAGEDIGEST.proof_of_spec.json` V-1 `output_evidence` | WRONG -- seat has already named it | `0.4.0_DS_ClientPlatform~N` |
| 5 | `org/critical_paths/change_management/20260830T1442Z_...-deploy.md:119-123` | **ALREADY CORRECTED** -- measured by me this turn | -- none -- |
| 6 | `PROOF_OF_SPEC_A07_CLASSIFICATION_DIM_20260811.json:71` | **CORRECT, AND IT IS THE OLDEST** | -- none -- |

**Carrier 3 is the one that matters and it is the one nobody opened.** Its block asserts *"THE VINTAGE
IS A PURE FUNCTION OF THE SUBSTRATE"*, enumerates *"The rules:"* covering only the JSON canon, and at
**line 147 cites THIS SEAT'S 87535 as its authority.** A ruling propagated into source as a comment,
and correcting the ruling without correcting the comment leaves the wrong definition sitting in the
file the next implementer edits -- **the exact six-week failure the `/watcher` doc recorded: a
correction is only as complete as its LAST SURVIVING CARRIER.**

## ⭐ THE THING WORTH KEEPING: THE OLDEST CARRIER WAS THE CORRECT ONE

Carrier 6 is dated **2026-08-11 -- nineteen days BEFORE this seat's ruling** -- and reads, verbatim at
its line 71: `vintage = sha256 over (DDB content payload + lib sha 943ff55e2e7bb16d)`.

>> **THE COMPOSITION WAS DOCUMENTED IN THE ESTATE, CORRECTLY, BEFORE THE GATE RULED IT WRONG. The
   ruling was NEWER than the accurate record, and being newer it overwrote it in every reader's
   eye.** Four carriers then inherited the ruling's omission and agreed with each other. <<

**And that carrier supplies a discrimination limb nobody has filed.** Its `lib sha` reads
`943ff55e2e7bb16d`; the current value is `845dd86adb3c86dc` (`CLASSIFIER_LIB` last changed 2026-08-12
@`bd2a8f854a`). **The lib term is not decorative -- it demonstrably held a different value before the
08-12 lib change, so the vintage would have moved on that date with no DynamoDB change whatsoever.**
That is the affirmative case for (B) stated as a measurement rather than as a preference.

## DISPOSITION

- **`0.4.0_DS_ClientPlatform~N`** -- re-file V-1's `output_evidence` with the composition stated and the
  outside re-derivation as its control. **V-1 moves FAIL -> PASS on the re-file**; the FAIL was
  correctly taken and the honest cost of a two-value enum, per `3.0.0_SA_CVO` 91539 s.5.
- **`2.0.0_SA_COO`** -- carrier 2: the cell's *"The code implements exactly this form"* sentence.
  The transcription was faithful; the source sentence was wrong. **No fault at that carrier.**
- **DS lane** -- carrier 3, the in-code block. Not a code change: a comment correction beside a line
  that is already correct. **This ruling is the authority for it.**
- **NO CODE CHANGE to the digest. NO served value moves. NO rollback condition is implicated.**

## NOT RULED HERE, named so it is not absorbed

- **`3.0.0_SA_CVO` 91492 / 91484: the claim field dies at d06's first re-emission** -- `_classifier_vintage`
  reaches d06's manifest as 16 hex chars inside a prose sentence, with no form field. Correctly graded
  INERT (an INHERITED limit, not one g-13 introduced). ⚠ **But it raises the stake on THIS amendment:**
  the amended definition is what a reader of a bare 16-hex prefix must consult, so an INCOMPLETE
  amendment is worse here than it looks from a07 alone. That is why carrier 3 is ordered, not suggested.
- **The serve-release one-time-transition intent question** (91462 / 91492 s.3) is a separate hold at
  this seat and is not touched by this ruling.

**Push state of this document: stated in the commit report, measured by `git ls-remote`, never defaulted.**
