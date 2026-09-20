# /self-drive LGIC -- tick 158 (2026-09-20 ~20:2xZ-21:0xZ) -- FOUR ROWS RULED, AND THE TALLY I HAD BEEN PUBLISHING FOR EIGHT TICKS WAS WRONG BY TWENTY

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## The reads

| read | result |
|---|---|
| **orders** | **0 genuinely open of 170**; control `MDPF_TAXSMA` **25 of 27** (non-degenerate; known over-count) |
| **inbox** | `98754`, `98761` READ + acked |
| **disk** | **20.31 GB** (down from 27.7 -- round-7 applies consuming it, as budgeted) |
| **armed rows** | ⛔ **re-censused: 433 rows / 130 ARMED / 35 owned by this seat** -- see §2 |

## ⭐ 1. `LGIC_ENFORCE-S57` RULED AND DISARMED @`d4c6300dd6`

The row routes ONE question here: does Rule 30's *"a builder REFUSAL is a missing registry row to
add"* GRANT the refused seat the row-add? **Ruled NO**, and `2.0.0_SA_COO~G` had it right on the
bytes -- the sentence's contrast is *registry row* vs *hand-typed workaround*, both answers to WHAT
the remedy is. It names no serial, and reading a grant out of that silence is an agent-made lane
widening.

**The half the row did not reach, measured at HEAD, is what settles the route:**

- **ABSOLUTE FOR A SEAT.** `owned-paths-validate.py:218-220` -- a non-worker serial fails
  `_WORKER_SERIAL_RE` and returns False *before any grant is read*; clauses 1-4 cannot reach
  `infra/logic/**`. 6 registry files x 4 serials: CTO/COO~G/worker **REFUSED**, CRO **PERMIT**
  (positive control). ⭐ **So a "seat-facing route" is not a thing this mechanism can express.**
- **CONDITIONAL FOR A WORKER, and EXERCISED.** `_worker_orders` never asks who ISSUED the order or
  what lane the issuer holds. `LGIC_CANON.TO-CN-o-5-r4` granted
  `infra/logic/10_ONBOARDING_CHECKLIST.md` to `0.9.0_WK_LGIC_CANON~1`.
- ⭐ **ALREADY ON THE RECORD at `LGIC_CANON-S21` (another seat's row), so NO NEW ROW WAS FILED.** A
  433-row census ran **before** the novelty was claimed. *Last tick I over-billed a finding as
  "sharper than the caveat" and was falsified; "novel" now gets a denominator.*
- **EXPOSURE, not INCIDENT:** 718 order files / 19 codes / **45 non-terminal**, and **0 of the 45**
  names any `infra/logic` path. CN-o-5-r4 is `complete` and a terminal order grants nothing, **so the
  exercised route and the zero agree and each explains the other.**

> ⛔ **The consequence, stated so it is CHOSEN and not stumbled into: "route it to the CRO" is a
> DISCIPLINE AT THE CUT, NOT A GATE.** A COO naming a registry path in a worker cell's `<paths>`
> obtains exactly the write the lane refuses that COO itself -- correctly, because Rule 27 says the
> order IS the grant. **No gate proposed, deliberately.** `2.0.0_SA_COO~G` adopted the framing at
> `98761` and its `EN-n-2` decomposition §0t already carries it.

## ⛔⛔ 2. THE CORRECTION THAT MATTERED MORE THAN THE ROW -- `LGIC_ENFORCE-S131` @`b5ab0cd5f6`

**CARRIED, in `98703` and `98743`: "15 armed rows, 5 decided, 10 remain."
MEASURED this tick on the schema's own fields: 433 rows, 130 ARMED, and 35 ARMED with
`disarm_owner` == this seat.** The carried 15 was a count of rows I had **TOUCHED**, not rows I
**OWN**.

> ⭐⭐ **A RESIDUAL COMPUTED BY SUBTRACTION NEVER REVISITS ITS OWN DENOMINATOR.** Every tick I
> subtracted the rows decided since and got a figure that was internally correct, so an error in the
> STARTING population was invisible to the arithmetic permanently. **The tell is not a suspicious
> number -- it is the ABSENCE of any tick that re-derived it.** COST: one census per DRIVE, not per
> tick. NON-APPLICATION: a residual whose population is closed and stated by the object itself.

⛔ **SECOND TIME IN ONE DRIVE, BOTH TIMES UPWARD: tick 149 carried 3 and measured 15; this tick
carried 15 and measured 35.** At tick 149 I wrote the lesson down -- *"a carried list has no
denominator and no owner field"* -- put it in `MEMORY.md`, **and then rode the carried 15 for eight
further ticks.** Worse: that same file already held the figure **"73 armed rows"** in an unrelated
entry, so a number that should have made 15 look wrong was in my startup context the whole time.
⭐ **A LESSON WRITTEN DOWN IS NOT A CONTROL; ONLY A RE-MEASUREMENT IS.**

**How to read the 35:** an **UPPER BOUND** on the undecided, never a count of open decisions -- seven
of them are rows I have already ruled that still read ARMED because R-19 gives the clock to the CVO.
**That gap is exactly what the carried tally was silently made of.** The row also DECLARES its weak
proxy instrument (28 named / 7 unnamed over 1,088 deliverables + 6,284 subjects) rather than quoting
it as a decision count -- `S62` and `S116` were decided and read UNNAMED.

## ⭐ 3. `S112` + `S113` + `S114` RULED AS ONE CHAIN @`0efda18ca1`

Re-measured here, not adopted: `scopes.json` carries `49f` as a whole value and **not `f49` even as a
substring** (S114 confirmed, S113's reason falsified); 25 system keys, **0 of 10** R1 tokens among
them; `unresolved` = exactly `astn, trade, news`.

### ⭐⭐ `sentiment` RESOLVES, on a third instrument
S114 left one member undecided. `sentiment_query_api/index.js:28` defaults `ARTICLES_TABLE` to
**`opal-news-articles`**; its evidence tree sits under `runs/news-subsystem/`; its analysis code lives
**inside** `tools/news_scanner/`; **0 of 403** `project.json` paths carry `SENT`. **It is a COMPONENT
OF THE NEWS SUBSYSTEM**, inheriting `news`'s recorded missing-owning-directive finding -- class (A),
not (F). ⭐ **It is the token CANON's step-13 census halts on, read for a day as an independent
unknown when it is the news problem under a second name.**

**Partition now closed against its denominator: (A) 4 · (B) 1 · (C) 3 · (D) 1 · (E) 1 · (F) retired =
10.** Naming one owner for R1 **misroutes NINE of ten.**

### ⛔ And it falsifies a figure I published, IN BOTH DIRECTIONS
`98512` sized step 13's registry half as *"SEVEN undeclared tokens ... Absorbable; not a project"*.
**SEVEN overstates the registry-row work by six** (only `portal` is a row) **and understates the real
work**, because `unresolved` is a **BLOCKED list, not a FIXED one** -- `news` still raises 81 times
while declared -- and that class is now **FOUR**, closable by no registry row.

> ⭐ **THE KEEPABLE IS NOT "RECOUNT": "absorbable" was a claim about the REMEDY and I priced it off a
> count of the RULE FAMILY. A SIZING INHERITS THE GRAIN OF WHATEVER IT COUNTED, AND NOTHING IN THE
> NUMBER ANNOUNCES WHICH GRAIN THAT WAS.** COST: name the remedy class before quoting a size.
> NON-APPLICATION: a set whose members share one remedy by construction.

**Card-2 convergence (S113 left it here): its withdrawn ground is RESTORED**, and on a stronger basis
-- not "the population is measured" but "four of ten need an OWNING DIRECTIVE, which no cell, seat or
registry row can create." That is absorbability **measured and found ABSENT**. ⛔ **No new card minted,
card 2's text not re-opened: this changes its SIZING, not its existence.**

## ⚠ 4. THE ZERO-FROM-THE-WRONG-PLACE CLASS HIT THREE SEATS IN ONE HOUR, INCLUDING TWICE HERE

| seat | the zero | caught by |
|---|---|---|
| `3.0.0_SA_CVO` | `reg query HKCU\Environment` -- searched the ENV namespace for a `terraform.rc` carrier | a third read; retracted at `98754` |
| `2.0.0_SA_COO~G` | three silent zeros, incl. `os.walk` over an MSYS path Python cannot resolve | **a SIZE contradicting a COUNT** -- 8.5 GB cannot contain zero of what makes it big (`S130`) |
| `1.0.0_SA_CTO` | order census `0 codes` on `task_orders/` for `task-orders/` | a positive control |
| `1.0.0_SA_CTO` | `SYSTEM KEY COUNT: 0` -- `systems` is a LIST, my reader tested for a dict | **a registry cannot have zero entries**; re-read with `mdpf` as control |

⭐ **In none of the four did the instrument complain.** My second one is the worse of my pair: it
would have "confirmed" the R1 absence **VACUOUSLY, by finding nothing to compare against** -- a
control that is not weak but EMPTY.

## Open calls at Andrew -- **2** (sizing of card 2 corrected, existence untouched) · `MEMORY.md` 24.35 KB (trimmed under ceiling)

## Compiler Tools

`get_delivery_state` · `ack_messages` x2 · order census + control · 4-project row census (433 rows, all
three fence shapes) · `owned-paths-validate --check-agent` x24 with a positive control · source reads at
`:123`, `:176-206`, `:209-235`, `:275-334` · `_worker_orders` over 19 codes · `git ls-tree`/`ls-files` ·
registry `json.load` x2 (one re-read after a vacuous zero) · **3 commits** · `send_message` x4 (12
delivered, 0 refused) · `Monitor` re-arm · `MEMORY.md` anchor-edit.

**PUSH STATE at write time:** `d4c6300dd6` and `b5ab0cd5f6` **on origin**; `0efda18ca1` + this commit
LOCAL; origin/CLOUD `b5ab0cd5f6` (ls-remote read).
**state: ARMED**
