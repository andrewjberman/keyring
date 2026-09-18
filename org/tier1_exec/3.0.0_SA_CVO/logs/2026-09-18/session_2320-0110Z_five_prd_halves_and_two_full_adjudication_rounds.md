# Five L4-R halves and two full L8/L9/L10 rounds -- 3.0.0_SA_CVO

**archetype:** VALIDATE

**Date:** 2026-09-17 23:20Z - 2026-09-18 01:10Z
**Task Order:** none; five spine-owned L4-R deliveries and two L8 routings, all from `1.0.0_SA_CTO`
**Status:** COMPLETE for everything routed; one half owed back to the CTO by its own refusal

---

## What landed

| item | verdict | commit |
|---|---|---|
| LGIC_CANON v1.6 ratified-text | REFUSE | `462451b6f7` |
| LGIC_CANON v1.7 ratified-text | SIGN -> ADMITTED | `ecc5791362` |
| NFRA_SPMOVE v0.3 ratified-text | SIGN -> ADMITTED | `4bde3fce31` |
| NFRA_MCPINDEX v0.3 ratified-text | REFUSE | `7fef989e77` |
| NFRA_MCPINDEX v0.4 ratified-text | REFUSE (narrow) | `09653cd330` |
| LGIC_ENFORCE round 4 L8/L9/L10 | 4 PASS 1 FAIL, 0 undispositioned | `66a07704fe` |
| IRPT_BCKEND round 2 L8/L9/L10 | 11 PASS 1 FAIL, 0 undispositioned | `c1a8cd2543` |

Two rounds, 127 rows dispositioned (3 + 124), 17 judgment criteria graded, 7 CVO-owned questions
ruled, 3 new rows filed and graduated the same round they were raised.

---

## The instrument that did the work

**Print the bytes at the cited line. Do not search for the quote.** Four of the five most valuable
findings came from that one act and from nothing else.

- `LGIC_ENFORCE-S61`: a minted registry row quotes a phrase to `ADVI_HISTBF.json`. The file has held
  0 occurrences since 2026-05-04. The phrase lives verbatim in the sibling `ADVI_JWTRES.json` -- 1 of
  464 files under `org/projects/` -- so **a grep for it returns ONE CLEAN HIT and confirms the wrong
  object.** The row asserted a 2026-09-17 measurement for a read that could not have returned that
  string on that date. This is the defect that failed H24R4-AC4.
- `IRPT_BCKEND-S56`: four citations across three judgment records, true when written, wrong at HEAD,
  none carrying a vintage pin. Each had to be re-derived at TWO vintages to tell a stale pointer from
  a false claim -- which is the tax `CLAUDE.md` Rule 22 exists to avoid.
- `S25R4-AC5` does not exist. The routed judgment set for LGIC_ENFORCE round 4 named it; 20 criteria
  are declared across the five orders and exactly 5 carry `judgment="true"`, of which the real one is
  `S25R4-AC4`. **Both sets have five members, so the error survives a count check.**
- `NFRA_MCPINDEX` v0.3's ENDPOINT section was a paraphrase, not a transcription -- and the tell was a
  SIBLING ARTIFACT, not the document itself: `NFRA_SPMOVE` v0.3, cut by the same seat the same day,
  carries its cards byte-for-byte. That comparison is what made "the compressed shape is one PRD's,
  not the house form" a measurement rather than a preference.

---

## Three things worth carrying

**1. A denominator certifies the sweep, never the set -- and the wrong DOMAIN is the failure that
arrives looking clean.** Answering `W3-S13`'s CVO-addressed question, I censused `quarantine/` across
the four firm buckets and got a positive-controlled ZERO. The control was sound and the domain was
wrong: the writer targets `IRPT_EVIDENCE_BUCKET`, which the deployed function reads as
`opal-data-ycharts`. Re-run against the right bucket the answer was still zero, with its own positive
control -- but a wrong-domain read had already produced a confident, printed, positive-controlled
number, and I would have shipped it if I had not gone looking for the writer. **Find the WRITER before
you census the destination.**

**2. My own pre-commit simulation was scoped wrong once, and it failed LOUD only by luck.** Simulating
the resolver against the working tree, I built the file list by hand and read 73 undispositioned where
the real resolver reads 3 -- because `ADJUDICATION_v1.md` carries most of that project's dispositions
and my hand list omitted it. The fix is the rule: **resolve paths with the tool's own `_index_paths`
and substitute ONLY the bytes.** A check scoped to the wrong population is blinder than no check,
because it returns a number.

**3. A gate's OK is scoped to what it was HANDED.** My first IRPT commit hit
`fatal: Unable to create '.git/index.lock'` under 14b contention. The gate then graded the unstaged
content and its last two lines read `0 new row(s) of 195 total checked` and
`OK: 3 file(s), all new rows carry their step-7/step-10 fields` -- a clean tail on a run that had
staged nothing. The fatal was line 1 of 13; the OK was line 13. **Then I compounded it by reading that
log before the background job finished and concluding the commit had failed.** It had not:
`c1a8cd2543` is that first attempt. The repository was the authority the whole time, which
`safe-commit`'s own refusal text says in as many words: *a tool stdout line is the TOOL DESCRIBING
ITSELF; git log is the REPOSITORY ANSWERING.*

---

## The grades that will be read again

**`IB-s-14`'s v0.11 render arm is UNSOUND AT ITS VINTAGE** (`IRPT_BCKEND-C-S93`). Round 1's renderer
produced ONE document from THREE distinct bundles -- three raw sha256, one normalized content hash,
an identical 71,944-byte content stream -- and the arm passed because it compared each PDF only to
itself. A renderer whose output does not vary with its input cannot evidence that the input was
rendered, and every per-object check passed precisely BECAUSE the comparison was per-object. FWD-4 and
FWD-8's proof gap is not narrowed by it. Third instance of that class this week.

**A disarm owner that names a CELL is unownable the moment the cell ends** (`C-S97`). `W4-S25` and
`W4-S28` name `IB-rtb-1`; it closed terminal without touching either, verified at 0 occurrences of
each id in its instance. R-19 says the CVO writes on an OWNER'S WORD -- and a cell cannot give one.
Both owner fields are also prose carrying a CONDITION rather than an owner. Nothing in the fabric
notices this shape, which is why it is filed as structural rather than as two rows.

**53 ARMED rows graduated and not one disarmed.** No owner gave a word this seat could write on. The
five owned by terminated worker slots each carve out explicitly what they did NOT disarm; writing
those as whole disarms would retire exactly the half the carve-out exists to keep open.

---

## Where consistency cost a round trip, deliberately

`NFRA_MCPINDEX` v0.4's ten cards are RAW-IDENTICAL to the pin including indentation, 86 of 86 lines,
negative control clean. I refused it anyway, on two sentences in the section's preamble carrying
version history and this seat's own name. The line had to be drawn precisely, because `NFRA_SPMOVE`
v0.3 carries a preamble in the same position and I SIGNED it hours earlier: that one holds only the
pin, the count, Andrew's confirmation and the transcription statement. **The defect is the history and
the seat name, not the preamble.** A bar enforced selectively is not a bar, and a bar enforced without
saying where its edge is will be read as caprice by the next seat.

---

## Next

Event-driven. Owed elsewhere: the CTO's placement of `W4-S25`/`W4-S28` on live seats, the
`NFRA_MCPINDEX` two-sentence deletion, and `RT5-AC2`'s one-paragraph repair (the answer already exists
in IB-rt-6's own host measurement). `LGIC_LGCTFM`'s `V1R1-AC5` is judgment at L9 and is NOT yet owed --
round 1 is not terminal, and the ANDREW_CARD question is Andrew's under his ~23:5xZ word.

-- 3.0.0_SA_CVO
