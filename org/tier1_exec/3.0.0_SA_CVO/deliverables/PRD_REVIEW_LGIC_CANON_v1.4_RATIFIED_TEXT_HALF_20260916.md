# PRD review -- LGIC_CANON v1.4, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97517.
PRD: `org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md` @ `96ebbde746`, ratified-text half_hash `1cd7a3546d93`.
Previous signature: v1.1 @ `56608aadd4`, half_hash `43fa46d2a86f`.

## VERDICT: SIGN -- with one finding against the BRIEF half that its own hash cannot surface

## What changed (measured)

| commit | ratified-text | brief |
|---|---|---|
| 56608aadd4 (v1.1, signed) | 43fa46d2a86f | ef2339f180c1 |
| d9977a0f40 (v1.2) | 43fa46d2a86f | 5443fa0e7bc0 |
| 5b2336a5e4 (v1.3) | 43fa46d2a86f | 8336e1f07e9e |
| 96ebbde746 (v1.4) | **1cd7a3546d93** | 8336e1f07e9e |

The ratified-text section diff from v1.1 to v1.4 is ONE hunk: FWD-5's DONE WHEN, ACCEPT and SOURCE.
CONTRACTS and FWD-1..4 and FWD-6 are byte-unchanged.

## Why it signs

- **Andrew's words are verbatim.** The call-2 sentence in SOURCE matches his record
  `ANDREW_DIRECT_20260916_182xZ_RESERVED_GROUP_FOUR_CALLS_RULED.md` @ `50d1b9403e`. The record wraps it
  across quoted lines; the words are identical.
- **The re-qualification is what he said and no wider.**
  - The run is a LGIC_LGCTFM practice wave over an existing firm's subject.
  - No demonstration firm is made up.
  - The first genuinely new firm re-runs it as confirmation only.
- **ACCEPT got stronger, not weaker.** *"the firm's people see their dashboard at the end exactly as
  before"* makes a practice wave over a LIVE firm carry its own no-regression bar. That is the bar a
  run over served output needs, and it can fail.
- **The EXERCISED bar is still a driven act, not a wait.** That was the point of lifting G-N.
- **No seat names, no version notes, no revision history** in either section. Checked by the same
  per-line serial and version-note census I used on NFRA_OPLGTW.

## FINDING (brief half, not a condition of this signature)

The brief half's hash is `8336e1f07e9e` at v1.3 and v1.4 alike, so `prd-signoff status` reads
`4.0.0_SA_CRO`'s signature CURRENT. Its bytes did not move. **But what they describe did.** A census of
the whole PRD @ `96ebbde746` for the old subject:

- `:212-221` -- the checklist's first end-to-end run is *"`ADVI_FIRMBKTS`'s first cutover"*, and it carries
  *"The call this PRD does not make"* (whether a cutover meets FWD-5), with a REC. **Andrew has now made
  that call, differently.**
- `:268` -- item 7, *"The checklist's first real run, at `ADVI_FIRMBKTS`'s first cutover (C6)"*
- `:283` -- the decomposition row: C6's subject is *"`ADVI_FIRMBKTS`'s first firm cutover"*
- `:352` -- the dependency row: *"`ADVI_FIRMBKTS`'s first cutover ... C6"*

So C6's cell text names a subject the endpoint no longer names, and 97523 sequences C6 after LGIC_LGCTFM
round 1. **A signature bound to a half's bytes cannot see a half whose REFERENT moved.** Nothing re-opens
it, and `2.0.0_SA_COO~G` would cut C6 from these rows.

REC to `1.0.0_SA_CTO`: restate `:212-221`, `:268`, `:283` and `:352` to the practice wave in a v1.5. That
moves the brief hash and re-offers the half to `4.0.0_SA_CRO` by mechanism rather than by message. The
ratified text does not change, so this signature carries.

-- 3.0.0_SA_CVO
