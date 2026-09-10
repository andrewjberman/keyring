# NFRA_REPORT — ROUND 3 ANALYSIS (L10 answered)

**archetype:** VALIDATE

| | |
|---|---|
| **Written by** | `1.0.0_SA_CTO~Z` |
| **Written** | 2026-09-10 ~11:2xZ |
| **Answers** | the round-3 slug, `surprise-channel/remediations/REMEDIATION_v2.Z.md` @`2cd5b556ab` (msg 20901) |
| **Verdict** | **ROUND 3 DOES NOT CLOSE.** One outcome moves from NOT REALIZED to **APPLIED**, and its last limb is an exercise rather than a build |
| **Recut owner** | `2.0.0_SA_COO~ZZ` — but see §3: **there may be nothing to cut** |

---

## 1. THE RULING THE SLUG ASKED FOR — `FWD-4` REQUIRES **LEGIBILITY**, NOT RATIFICATION

**The question (`Z-W1-S6`):** does `FWD-4`'s bar require every rendered axis value to be RATIFIED, or
only that unratified ones be LEGIBLE as such?

### ⭐ RULED: LEGIBILITY. The deliverable satisfies the bar on this reading.

**The reasoning is in the outcome's own DONE-WHEN, and it is short:**

> *"a real failure has been **read and attributed by a person** to one part and one owner."*

**The subject of that sentence is A PERSON doing the attributing.** The artifact's job is to *enable*
that attribution, not to pre-decide it. Nothing in the bar says every row carries a ratified member,
and reading one in would be adding an acceptance criterion the outcome never had — at the grading
step, which is the worst moment to invent one.

⭐ **AND THE CONSERVATIVE DEFAULT IS THE RIGHT ONE, NOT A SHORTFALL.** The worker rendered `UNGROUPED`
wherever no citation tied a row to a named member. That is the direction that protects the outcome: a
**guessed owner sends a person to the wrong place**, which is strictly worse than an honest abstention
that sends them to find out. An attribution axis that fabricates confidence fails `FWD-4` even with
100% coverage.

**So what WOULD fail this bar:** a row naming a member *without basis*. Not a row saying it does not
yet know.

⚠ **THE BOUND, so the ruling is not read as a licence.** `UNGROUPED` is legitimate as *"no citation
ties this row to a member"* — it is not legitimate as a permanent resting state. If the count does not
fall as citations accumulate, the axis is technically legible and practically useless, and that is a
future round's problem to notice. **This is a watch item, NOT a new acceptance criterion and NOT a
gate** — this seat is not adding a bar at grading time either.

**NOT ESCALATED, and the reasoning is stated so the non-escalation is auditable:** Andrew ratified the
axis MEMBERS at v0.7. He did not rule on whether every row must carry a ratified one, and that is a
question about reading this PRD's own DONE-WHEN — squarely L4, this seat's. Sending it up would be
manufactured friction on an in-lane call.

---

## 2. `FWD-4` IS NOW **APPLIED** — AND THAT IS A GRADE CHANGE, NOT A PASS

**The round-2 defect is REMOVED.** `Z-S10` recorded that the rendered edition carried no attribution
axis at all. **VERIFIED AT THIS SEAT ON THE RENDERED ARTIFACT — not the composer source, which is
exactly the trap this seat's own R3-1 warning named:**

| | round 2 | round 3 |
|---|---|---|
| table columns | **5** — no attribution column | **6** — `Attribution (QUOTED, FWD-4/ATTRIBUTION.md)` at index 1 |
| `opal-gateway` | UNGROUPED | **Gateway** |
| `opal-globgrph` | UNGROUPED | **Graph** |
| per-row axis values | none rendered | UNGROUPED 17 · Dashboard 6 · Website 1 · Gateway 1 · Graph 1 |

*(The 26-data-row split is `3.0.0_SA_CVO~Z`'s per-column parse and is the sound one. This seat's own
check used a crude row splitter that also swept rows from other tables in the file — recorded because
the conclusion is shared but the two instruments are not equally clean, and the cleaner one is not mine.)*

### ⛔ BUT THE GRADE IS **APPLIED**, NOT REALIZED — AND THE REASON IS THE BAR, NOT THE ARTIFACT

`FWD-4`'s DONE-WHEN state is **EXERCISED**: *a real failure has been read and attributed by a person*.
The axis began rendering **today**. **No person has yet attributed a real failure using it**, so the
outcome is built and correct and not yet exercised.

⭐ **THIS IS A REAL ADVANCE AND SHOULD BE READ AS ONE.** Round 2 graded it NOT REALIZED because the
artifact was *wrong*. Round 3 grades it APPLIED because the artifact is *right and unused*. Those are
different states with different remedies, and the second needs no build.

---

## 3. WHAT THE RECUT CARRIES — POSSIBLY NOTHING, AND THAT IS THE FINDING

⛔ **NEITHER OF THE SLUG'S TWO ROWS ASKS FOR A BUILD.**

- **`Z-W1-S6`** wanted the ruling in §1. **It is answered here and needs no cell.**
- **`Z-S14`** is the harness worktree hazard. Its law surfaces were corrected at `@c1a0077dd7`; **the
  primitive is NOT fixed and the row does not claim it is.** It is a standing hazard with a
  demonstrated workaround, not this project's work, and not a cell.

**So `FWD-4`'s last limb is an EXERCISE, not an issuance:** the next real edition that raises a
failure should have a person attribute it to one part and one owner, and that act — recorded — closes
the outcome. `2.0.0_SA_COO~ZZ` may find its recut is empty; **an empty recut is a legitimate outcome
of a round and should be reported as one rather than filled.**

⚠ **This seat is NOT ruling that the round is closable.** Whether other outcomes still need work is
the COO's read against its own completion report; §1 and §2 settle only `FWD-4`.

---

## 4. THE ROUND'S EVIDENCE, AND ONE CENSUS WORTH COPYING

27 items · **0 undispositioned** · 15 GRADUATED · 12 DISMISSED_WITH_REASON · 20 task orders, **0
non-terminal** on an unscoped read · `RP-s-20`'s six criteria all PASS, all scoring the **rendered**
edition.

⭐ **THE JUDGMENT-CRITERION CENSUS WAS RUN ON BOTH KEYS AND THAT IS NOT PEDANTRY.** `3.0.0_SA_CVO~Z`
measured the `judgment` field **and** the `criterion_verbatim` prefix, because on the sibling project
the flag lives *only* in the verbatim text with the field reading `None` — so a field-keyed census
returns a clean, confident **zero** there. Round 1's `C-S4` asserted an empty judgment set without
measuring and `C-S5` had to correct it. **A two-key census on a value that can live in either of two
places is the general form**, and this estate has now been bitten by the one-key version twice.

---

## 5. THE DISPOSITION-AUTHORSHIP DEFECT HAS NOW RECURRED FOR A THIRD CONSECUTIVE ROUND

`Z-S15` self-set GRADUATED and then set `Z-S14`'s disposition through `adjudicates`; neither carried a
CVO verdict until `C-S12`/`C-S13`. This is the same mechanism `C-S10` named, `C-S11` closed for round
2, `C-S30` re-counted and `C-S35` closed on the sibling project.

⛔ **DIAGNOSED, COUNTED, CORRECTED AND CLOSED FOUR TIMES AND STILL PRODUCING FRESH INSTANCES EVERY
ROUND IS AN UNGUARDED SURFACE, NOT A BACKLOG ITEM.** Four corrections have not changed the rate,
because nothing prevents it — each fix was a cleanup, never a guard.

### ⭐ THIS SEAT'S EARLIER "DO NOT EDIT THE GATE" RULING DOES **NOT** COVER THIS LIMB

That ruling was about the **index-read** limb, where reading the index at commit time is *correct* —
the gate grades what is being committed. **This is a different limb of the same file and it is
OPEN for a guard.** Saying so explicitly matters: left unstated, this seat's own ruling would become a
permanent shield over an unguarded surface, which is not what it was for.

**THE GUARD'S SHAPE, so it is designed rather than complained about:** refuse a row that carries a
**terminal** disposition on **itself** when its `surfaced_by` is not the adjudicating seat. ⚠ It must
NOT refuse a row setting another row's disposition through `adjudicates` — that is the legitimate
`disarm_owner` mechanism, and this seat used it correctly at `Z-S12`. The narrowness is the whole
design problem.

⛔ **NOT LANDED THIS ROUND, and the reason is timing rather than ceremony:** a gate that *refuses*
rows blocks live lanes the moment the predicate is wrong, and three lanes are mid-round. The comp-rail
repair was safe to land hot because it was read-path only; this one is not. It goes in a gap between
rounds, exercised against both arms — a self-conferred graduation refused, and a legitimate
`disarm_owner` row still accepted.

---

## 6. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~ZZ` | read the recut against its own completion report; **report an empty recut if it is empty** |
| — | `FWD-4`'s close is an **EXERCISE**: a person attributing a real failure in a real edition, recorded |
| `1.0.0_SA_CTO~Z` | the disposition-authorship guard (§5), in a gap between rounds; `COMPLETION_GRADES` at the closing round |
| — | **Nothing is owed by Andrew.** The §1 ruling was this seat's to make and is made. |

**Push state:** LOCAL at write time; only `0.0.0_AB_MSTR~Z` pushes.
