# CARD TO ANDREW -- the sequence's ORDER puts the LGIC scope's own unblocker LAST in the slot queue

**Raised by:** `1.0.0_SA_CTO`, 2026-09-19 ~14:3xZ, `/self-drive LGIC` tick 89.
**This is NOT a re-ask of the seating call (CALL 2, surfaced 2026-09-18 ~08:4xZ).** That card asks
*whether* `ADVI_FIRMBKTS` gets a lane. **This card is about the ORDER**, which is a different question and,
by the skill's own rule, **only Andrew's word changes it** (`SEQUENCE.yaml` order changes are his; either CTO
executes). I am raising, not editing.

---

## The measurement

`python .tools/sequence-check.py` -- **denominator 10 projects; `NEEDS-SLOT` = 3, `LANE-DARK` = 1**, COO
capacity **AT CAP 3/3**.

| # | project | stage | flag | state |
|---|---|---|---|---|
| 1 | `MDPF_CANON` | **0** | NEEDS-SLOT | PRD v2.6 ADMITTED, hold MET |
| 2 | `NFRA_MCPINDEX` | **0** | NEEDS-SLOT | PRD v0.5 ADMITTED |
| 3 | **`ADVI_FIRMBKTS`** | **2** | NEEDS-SLOT | PRD v1.2 ADMITTED, both halves SIGNED, hold MET, `coo_lane` null |

**The rule that consumes this order** (`/self-drive` §0.7.6, from Andrew-direct 2026-09-14 ~07:0xZ): *"When a
slot frees, the next one goes to the FIRST `NEEDS-SLOT` project in the sequence's order."*

⛔ **So `ADVI_FIRMBKTS` is THIRD OF THREE, and stage 2 is behind all of stage 0 and stage 1 by construction.**

## Why that is the LGIC scope's problem and not a scheduling preference

**Stage 1 is LGIC. Stage 2 is the D8 migrations "built on Platform Logic." The document reads: finish LGIC,
then run the migrations.** ⛔ **But two of stage 1's own terminal outcomes cannot close until a stage-2 project
RUNS** -- so a reader driving the sequence in its stated order waits for LGIC to finish before seating
`ADVI_FIRMBKTS`, **and LGIC never finishes.**

**This is not a cycle** -- `ADVI_FIRMBKTS`'s own hold is *"`LGIC_ENFORCE` PRD admitted?"*, which is **MET**. It
is a legitimate INTERLEAVE that the stage ordering cannot express: `LGIC_ENFORCE`'s PRD -> `ADVI_FIRMBKTS`
executes -> two LGIC outcomes close.

### The two gated outcomes, at their TRUE depths -- corrected this tick against my own carrier

⚠ **I had recorded both as "gated on `ADVI_FIRMBKTS`" as though at the same depth. I printed the bytes and they
are not**, and the difference is the whole practical point:

| outcome | what its ACCEPT actually requires | depth |
|---|---|---|
| **`LGIC_LGCTFM` FWD-6** | *"the 49 Financial migration's decomposition starts from the run's plan instead of rebuilding the inventory from scratch"*; DONE WHEN *"EXERCISED -- a real migration's decomposition has been cut from it"* (PRD `:115-124`) | ⭐ **L5.** It closes when a SEATED lane CUTS A DECOMPOSITION. It does **not** wait for the router repoint or for any migration to execute. |
| **`LGIC_CANON` FWD-5** | the `ADVI_FIRMBKTS` **router repoint to land** (carded steps 10 and 16, `C6_RUN_RECORD.json`) | deep in that project's **L7** |

⭐ **THE CONSEQUENCE THE OVERSTATEMENT HID, AND IT ARGUES FOR THE SEAT MORE STRONGLY THAN THE OVERSTATEMENT DID:
seating `ADVI_FIRMBKTS` closes one LGIC outcome ALMOST IMMEDIATELY -- at its first L5 act -- and the other much
later.** The seat buys more, and sooner, than "it gates two final outcomes" suggested.

⛔ **The quote and the line numbers in my prior carrier were CORRECT; the implication was MINE.** An inherited
universal carries no denominator beside it to interrogate, which is why it survived several restatements. It is
corrected in `LGIC_CANON`'s `blocking` field this tick, against itself.

---

+-- CALL 1 of 1 ---------------------------------------------------+
  **When the next COO slot frees, does it go to `ADVI_FIRMBKTS` (stage 2) ahead of the two stage-0
  `NEEDS-SLOT` projects -- or does the stated order stand?**
  Stage 0 is *your* seat priority, so the order is doing exactly what you set it to do. The cost of it
  standing is that the LGIC scope cannot reach DONE, because its last two outcomes need a stage-2 project
  to run first.
  --------------------------------------------------------------------
  **REC --** **`ADVI_FIRMBKTS` takes the next free slot**, ahead of `MDPF_CANON` and `NFRA_MCPINDEX`.
  It is the only `NEEDS-SLOT` project whose seating CLOSES OUTCOMES IN ANOTHER STAGE rather than opening
  new work, its PRD is ADMITTED with both halves signed and its hold is MET, and **one of the two outcomes
  closes at its first L5 act** -- so the payback starts immediately rather than at the end of its L7.
  If the answer is that stage 0 stands, the honest consequence is that **LGIC holds at
  `HELD-AT-STOP`** rather than DONE, and I will record it that way instead of driving a scope that cannot
  complete.
+---------------------------------------------------------------------+

**NOT ASKED HERE:** whether the cap of 3 moves. **That is your number and I am not proposing a fourth lane** --
this card is about which project takes the NEXT slot under the cap as it stands.

**Routed to `0.0.0_AB_MSTR`** (which seats) and `2.0.0_SA_COO~G` (which holds LGIC and would hand off).
**PUSH STATE** stated in the tick log at write time.
