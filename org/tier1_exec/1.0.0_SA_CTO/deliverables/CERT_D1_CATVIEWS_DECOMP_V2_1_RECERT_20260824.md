# CERT -- D1_CATVIEWS decomp v2.1 (re-opened @337ce327b6): CERTIFIED ON THE ENUMERATION, alternate signer, with TWO P1 corrections (neither invalidating)

**Signer:** `1.0.0_SA_CTO` (base) -- **ALTERNATE SIGNER OF RECORD** per the pipeline's self-certification break:
the v2 cert @60d4e2f1b4 was CVO's; a DECOMP-INVALIDATING re-open requires a DIFFERENT independent seat for the
re-certification; the CRO class is off-limits this session (Andrew ~19:3xZ), leaving base CTO. CVO endorsed the
routing (66975). **Archetype:** VALIDATE. **Bar applied:** CVO's published v2 bar (66358/66357) including check 7
(oracle viability, sampled), applied by a different hand -- the bar is the fabric's, not the signer's.
**Subject:** `workflows/atom_decomposition/runs/d1-catviews/20260824T195537Z/DECOMP.md` at @337ce327b6.
**Push state:** this cert lands LOCAL, rides MSTR integration; hash + stat read AFTER commit (the 50379f8d2b rule).

## VERDICT: CERTIFIED on the enumeration. The three (i) cells + the re-open are correctly formed. TOs for the (i) cells may cut AFTER the two P1 corrections land (both are one-commit issuer acts; nothing else waits).

## MECHANICAL (measured at this seat, independently -- my own extractor, run cold)

| check | measured | verdict |
|---|---|---|
| ids declared vs mentioned | 31 extracted (backtick+bold forms) vs s.4 declared 31; symmetric differences EMPTY; 0 duplicates | PASS |
| arithmetic | 14 carried + 13 (h) + `D1-inv-4` + {`D1-i-1`, `D1-i-2`, `D1-inv-5`} = 31; closes | PASS |
| by group | a1 b1 c2 d1 e3 f1 g2 h13 i2 inv5 | PASS (matches s.4's decomposition) |
| re-open form | s.(i) header declares SCOPE RE-OPENING (not amendment), names the finder (DS~F 66916), the mechanism, and the invalidating class (postulate-(i)); the v2 cert marked SUPERSEDED on the face | PASS |
| cohort/certifier disclosure | REDUCED COHORT solo-authored, disclosed (line 24); certifier-of-record line untouched -- THIS cert documents the alternate-signer basis | PASS |
| s-rulings both directions | carried g-1 boundary (stored 5-enum + Primary/Custom NOT re-opened) intact; no ruling re-opened as a cell by (i) | PASS |
| oracle viability (check 7, SAMPLE -- denominator stated) | 1 sharp probe at this seat: `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py:1-7` read directly -- "Assembles the FLAT function package FROM A PINNED COMMIT -- never from the working tree... Every byte comes out of `git show <pin>:<path>`". The mechanism i-1/i-2/inv-5 rest on is REAL AT SOURCE. CVO independently confirmed the same file + the three-derivation ledger (66975); the finding seat's ledger citation stands. NOT exhaustively re-derived: the per-module channel census is i-1's own deliverable, not this cert's | PASS (sampled, stated) |
| CE against the re-opened layer | (i) enumerates: the two channels per module (i-1, denominator in-cell), the re-pin+TF act (i-2, AE-CLASS -- the seam assignment that was the original gap), and the guard invariant (inv-5). **DE-half path-to-live CHECKED AND DISTINCT, not assumed:** the portal D1 work renders from the DEV working build (no pinned-package shape; PROD exposure rides the separate ruled promote), so no analogous (i) cell is owed on the DE side -- stated here so the absence is a decision on the record | PASS |

## P1 CORRECTIONS (issuer acts, one commit; the run STANDS; neither re-opens enumeration)

1. **`R-i1` FOUR-POSTULATE RECORD IS MISSING.** Surface (i) MINTS an axis -- CODE-CHANNEL per module
   `{s3-code-channel, lambda-zip}` (i-1's own frame) -- and the bar's check 4 requires a Rule-24 record for every
   enumeration minted; s.3 carries R-h0..R-h4 only. Owed BEFORE the (i) TOs cut (they are gated on this cert
   anyway, so the record rides the cut commit). Postulate (iv) preview the record must confront: the two channel
   values do NOT move together under the obvious remedy -- `safe-deploy` moves the s3 channel, only re-pin+TF moves
   the ZIP -- which is not a defect of the axis, it is THE FINDING, and the record should say so.
2. **s.4's "Criteria: 0 -- NO TOs CUT YET" IS FALSE AS WRITTEN.** TO-R1-DS/-DE were cut ~20:28Z against the
   certified 28 with criteria + cell_refs; the sentence is v2-vintage prose that survived the re-open. Restate:
   criteria EXIST on the certified-28 (the two round-1 TOs); the 3 (i) cells carry 0 criteria pending the
   post-re-cert cut -- that split IS the alignment state, and the current sentence hides the half that exists.

**P2 (prose, non-blocking):** line 37's "**Total: 28 cells**" is v2-history narrative that a grep-reader will take
as the current total against s.4's 31 -- annotate it "(v2 total; re-opened to 31, s.4)".

## SCOPE OF THIS CERT
The enumeration and the re-open's form. NOT the sizing of i-1's census, NOT the execution of i-2 (AE-class, future
seating), NOT a re-derivation of CVO's certified 28 (their cert was true of what it read; the territory, not the
check, was short -- CVO's own sharper statement, 66975, and their bar's check 8 is the systemic remedy). The
scorecard row for this act: decomps invalidated 1 / re-certified 1, alternate signer, two P1s, zero cells changed
by certification.
