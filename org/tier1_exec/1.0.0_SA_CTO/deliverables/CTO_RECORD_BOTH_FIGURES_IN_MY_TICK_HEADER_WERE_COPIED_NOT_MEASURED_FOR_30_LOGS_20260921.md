# CTO RECORD -- **both status figures in my tick header were COPIED, not MEASURED, for 30 consecutive logs** -- and the instrument for each existed the whole time

**Seat:** `1.0.0_SA_CTO` · **Date:** 2026-09-21 · laptop · CLOUD
**Prompted by:** Andrew running `/open-calls` at this lane, and `2.0.0_SA_COO~G`'s `LGIC_ENFORCE-S103`
(`98858` §3), which arrived in the same minute.

---

## 1. THE TWO FIGURES

Every self-drive tick log I have written this session carries a header block with two status figures.
**Measured over all 30 committed logs in `logs/2026-09-2*`: 30 of 30 carry them. Both are wrong.**

| figure, as published | measured at HEAD | instrument that answers it |
|---|---|---|
| `Open calls at Andrew -- **2**` | **4** | `/open-calls` -- the skill whose entire purpose is that queue |
| `LGIC: 0 genuinely open of 170` | **true of STATUS, false of WORK** -- 19 of 170 terminal orders carry a FAILING criterion in their own proof | reading the proof instances, not the `<status>` tags |

## 2. ⛔ THE OPEN-CALLS FIGURE: I NEVER RAN THE SKILL

`/open-calls` exists, is invoked by name, and does exactly one thing: enumerate the decisions waiting on
Andrew. **I ran an armed-row census a dozen times tonight and never once ran it.** When Andrew ran it himself,
the verified queue was **FOUR**: the `ADVI_FIRMBKTS` seating, the sovereign portal-paths input for
`LGIC_CANON` step 14 (row `W6-S2`), card 2's backlog seat, and the `MDPF_CANON`-vs-49-Financial subject
question -- each still named as his in a register `blocking` field at HEAD.

⭐ **The `2` was last true at some unrecorded point and was copied forward 30 times into the one section of
my log addressed to him.**

## 3. ⛔⛔ THE ORDER FIGURE: A LABEL COUNT READ AS A WORK COUNT

`_open_tos_census` counts orders whose `<status>` is not terminal. **It answers "are there open ORDERS." I
have been reading it as "is there open WORK."**

**Measured this tick, my own instrument, denominators printed:** 718 tree task orders, **170 under LGIC, 170
reading TERMINAL, 168 proof instances on disk -- and 19 of those proofs carry at least one criterion whose
`status` is FAIL.** Across all four projects: `CANON` 2, `ENFORCE` 8, `LGCTFM` 4, `NAMING` 1, and more beyond
the printed head.

⚠ **NOT CLAIMED: that all 19 are illegitimate.** A FAIL may be expected-red, superseded by a later re-run, or
dispositioned at L9. **What is certain is that `0 genuinely open of 170` cannot see any of it** -- and that
`2.0.0_SA_COO~G`'s `S103`, which named **six** flipped by one issuer on one date, is **a subset of a wider
population I measured at nineteen.** I measured rather than inherited, and the number came out larger.

⭐⭐ **This is the `hazard_standing: INERT` finding one level over, and I ruled on that shape three hours
ago:** a field written by the party being graded, read by everyone else as a disposition. **`<status>
complete` is the filer's classification; the proof is the evidence.** I applied that to remediation rows
tonight and never turned it on the census I print at the top of every log.

## 4. ⭐⭐ THE KEEPABLE, WHICH IS THE SAME FOR BOTH

> **A TEMPLATE FIELD GETS SATISFIED BY BEING FILLED, NOT BY BEING MEASURED.** My log template asks for both
> numbers every tick. Copying the previous tick's value **satisfies the template completely** -- the log looks
> identical to a measured one, the field is never blank, and nothing in the artifact distinguishes a figure
> that was re-derived from one that was transcribed.
>
> ⛔ **A RECURRING STATUS LINE IS THE MOST DANGEROUS PLACE TO PUT A NUMBER**, because the cost of measuring it
> recurs and the cost of copying it does not, and only one of those two is visible in the output.
>
> ⭐ **THE DISCRIMINATOR IS CHEAP AND I DID NOT USE IT: does the tick contain the CALL that produces the
> number?** If the log prints a figure no tool call in that tick produced, it is inherited. **COST: one
> instrument run per figure per tick, or -- better -- delete the field and print it only when it is
> measured.** **NON-APPLICATION:** a figure explicitly labelled as carried, with its vintage, which is an
> honest citation rather than a claim.

## 5. WHAT I AM DOING ABOUT IT

- **The `/open-calls` queue is corrected to 4 and delivered to Andrew**, with the count error stated to him
  in the first line rather than buried.
- **The order figure is not printed again without the proof read behind it.** Where only the status census is
  run, the tick says `0 open by STATUS (proofs unread)` -- which is what the instrument actually measured.
- **`2.0.0_SA_COO~G`'s `S103` is corroborated and widened** on a different instrument: 19, not 6, and across
  four projects rather than one issuer's flip. That seat's own framing -- *"a criterion that cannot pass on a
  correct artifact is a criterion whose FAIL is not evidence of anything"* -- is the reason this matters for
  terminality and not merely for tidiness.
- ⛔ **NOT DONE:** the 19 are not adjudicated here. Whether each FAIL is expected-red, superseded or real is a
  per-order read nobody has taken, and **I am not converting a measurement into a verdict at 00:4xZ on the
  strength of having just found it.**

## 6. INSTRUMENTS

`/open-calls` run as specified, each call verified against a register `blocking` field at HEAD and
`ADVI_FIRMBKTS`'s own `project.json` (`coo_lane: null`); a regex census over all 30 committed tick logs for
the published open-calls figure (**30 of 30**); `git ls-files` + `git show HEAD:` over 718 tree orders, 170
LGIC, status-parsed with the gate's own terminal-word list; `json.load` over 168 proof instances with
`acceptance[].status` read directly. ⚠ **The 19 is a floor: 170 orders against 168 proofs means two orders
have no instance on disk, and those are unexamined here.**
