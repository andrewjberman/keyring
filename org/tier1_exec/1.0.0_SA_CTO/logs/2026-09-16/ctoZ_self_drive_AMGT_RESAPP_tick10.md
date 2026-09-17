# `/self-drive AMGT_RESAPP` -- ticks 9-10 (`1.0.0_SA_CTO~Z`, 2026-09-16 07:0x-07:2xZ)

**archetype:** VALIDATE · **state:** `ARMED` · **job:** `a99eff47` · **ticks covered:** 9, 10

## Completion test

**NOT DONE** -- `status: active`, `dep_stage: EXECUTING`, **16 of 16 orders pending**, 0 of 1 complete.

## Delta: three ISSUER CRITERIA DEFECTS ruled

Two of the first three completions carried criteria **REFUSED AS WRITTEN**. Both workers built the thing,
proved what they could, **refused rather than silently substituting**, filed rows, and left the orders OPEN.
**No worker failed.**

| defect | what the criterion names | what is true |
|---|---|---|
| `rk-1` AC4 | gitlink `e85f6eb8` | the UNMOVED gitlink is `be8cf218`; `e85f6eb8` was correct **one round earlier** (round 11 `rj-1` AC6), 217 commits back |
| `rk-3` AC1 | `s3://opal-data-harvest/rankings/` | a plane the estate has **never written rankings to**; the criterion's own positive control lives in DynamoDB |
| `rk-3` AC3 | rawPath `/lead-panel/rankings` | missing the deployed route's `/api/scoped/amgt` prefix and segments -- **404s before any ranking logic runs** |

⭐ **ONE SHAPE: each criterion was cut against a world that was not READ AT THE CUT.** In all three the work is
**done and proven** -- the DEV merge builds (`tsc` rc=0, `vite` rc=0, 53 assets); the Price generation exists
and SERVES through the same function the deployed lambda calls -- and the criterion points elsewhere.

**RULED: issuer repairs, under a stated test --** *a repair is legitimate when it asserts the SAME PROPERTY
against the RIGHT OBJECT, illegitimate when it weakens the property.* Applied out loud per criterion: AC4's
property (the gitlink did not move) is already proven; AC1's is **strengthened**, since a check against a plane
nobody writes is vacuous; AC3's is **strengthened**, since a criterion that 404s before the logic runs cannot
discriminate a working route from a broken one. ⭐ **The mirror of a criterion that cannot fail: this one cannot
PASS. Both are non-discriminating.** No proven work is re-run.

## ⛔ MY OWN SYSTEMIC CENSUS WAS NOT SOUND, AND THAT IS THE TICK'S REAL FINDING

I ran the "is it systemic" sweep that paid off on the paths grant. **It does not pay off here.**

```
orders carrying a pinned world-fact: 6 of 16   |   hash 2 · s3 0 · rawPath 6
```

**Wrong in both directions.** It reports **zero** s3 paths while `rk-3` AC1 demonstrably checks one -- **one of
the three known defects is invisible to my instrument.** It false-positived `rk-8` (`:r,`, an artifact of my
own regex). And **most pins it found are correct, not defects**: `rk-2`/`rk-6`/`rk-15`'s rawPaths are the real
deployed shapes, which the CRO audit invoked for 200s (and the 500 on `/print`, that cell's whole point).

**A "6 of 16" headline would have been a confident, measured-looking number answering the wrong question.** The
denominator certifies the sweep, not the set. **I reported that rather than the number.**

⭐ **A CRITERION'S CORRECTNESS CANNOT BE ESTABLISHED BY READING IT -- only by RUNNING it against the live
world.** All three defects were found by workers running them; my static read found one, missed one, invented
one.

**RECOMMENDED, not ordered:** dry-run the remaining thirteen orders' invocations against the live world **now**,
before those workers spend effort. It is `rk-9`'s own mandate applied before rather than after.

## Not ruled

Not grading `rk-1` or `rk-3` -- instances are VALID rc=0 with FAIL-by-output recorded; verdicts are
`3.0.0_SA_CVO~Z`'s at L9. Rows `W23-S1`, `W26-S1/S2/S3` stand; their disposition is L9's. No ratified text moved.

## The staged-index reading that would have been a wrong act

Nine files staged in the **shared** index, `rk-3`/slot-`~26` artifacts -- which reads like a worker writing
outside its worktree. **`MERGE_HEAD` was present at `9d5ec84fef`, exactly `~26`'s tip, with the staged count
falling 9 -> 6 between reads.** That is the COO **mid-drain**, not a stray write. ⭐ **A merge state I did not
create is a peer's work in progress** -- asked whose, left it alone, raised nothing.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criteria pin census (own regex) | 6 of 16 | **UNSOUND -- missed 1 of 3 known defects, 1 false positive.** Reported as such |
| `MERGE_HEAD` + staged delta | present, 9 -> 6 | the discriminator between an in-flight drain and a stray write |
| `rev-list --count HEAD..<branch>` | ~24, ~26, ~28 ahead | normal drain cycle, live owner -- not the stranding class |
| `prd-signoff status` | ADMITTED, both current | nothing owed |

**Gap found:** in **my own instrument**, not the estate's. A static read of a criterion cannot verify what the
criterion points at.

## Owed next

Nothing by this seat. Issuer repairs + the recommended dry run; then drains; then L8/L9. Cards at Andrew
unchanged.

Push state: **LOCAL on SITEZ.**
