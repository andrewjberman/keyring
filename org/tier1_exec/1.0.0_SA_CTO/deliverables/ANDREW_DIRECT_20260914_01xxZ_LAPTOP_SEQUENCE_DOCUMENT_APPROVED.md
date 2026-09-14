# ANDREW-DIRECT 2026-09-14 ~01:xxZ -- the laptop sequence document: design approved; track now, enforce after it holds; replaces the 07-28 sequence; a COO lane for LGIC_NAMING

**Received at:** the 1.0.0_SA_CTO terminal, in-session. **Recorded by:** `1.0.0_SA_CTO`, same turn.

## HOW IT CAME ABOUT -- his words, in order

After the CTO laid out tonight's sequencing across seats, Andrew wrote, VERBATIM:

> "I like that plan but I want something more comprehensive to facilitate persistent long-term compliance with a given
> sequence. I think we need some kind of document that governs the sequence of multiple projects from the laptop box.
> This way, you as CTO can be the master orchestrator and effectively track progress against a master document across
> many projects."

The CTO proposed a design and three cards (below, verbatim). Andrew answered, VERBATIM AND ENTIRE:

> "recs approved"

## THE DESIGN HE APPROVED -- as put to him

- **Where it lives:** `org/missions/SEQUENCE.yaml`, next to the directive register. `org/missions/` is 0.0.0_AB_MSTR's
  lane, so it grants the CTO that one file on Andrew's word.
- **What it holds is only what no tool can know:** the stages, in order, and which projects sit in each; the gate that
  opens each stage, written as facts the register can check; Andrew's words behind each placement; a parked list
  (e.g. NFRA_SUBSTRATECARDING, "just not a priority at this time"); a change log, where every re-order carries his words.
- **What it never holds is status.** Status is read live every time, the way the scheduled-jobs file already works
  ("put nothing here that an API can answer"), so the document cannot go stale.
- **A reader, `sequence-check`**, prints on demand and sends nothing. It shows each stage with live status and flags:
  work on a project whose stage is not open; a stage whose gate is met but with no one working it; any laptop project
  the file neither places nor parks.
- **Governance:** the CTO changes the order only on Andrew's word. Every seat reads it at startup (one line in the
  startup protocol). It replaces the 07-28 sequence in `GOALS.yaml`, which points to it.
- **First cut:** running alongside, no gate -- IRPT_FNTEND round 5, DSGN_REBRND, card 3. Stage 1, Platform Logic --
  LGIC_NAMING decomposed, then LGIC_ENFORCE's and LGIC_CANON's PRDs. Stage 2, the D8 backend on it -- ADVI_FIRMBKTS, then
  MDPF_CANON, opening when LGIC_ENFORCE's rebuilt fence is on the bucket template. Stage 3 onward, not yet placed -- D2's
  Advisor Intelligence projects, D9's tax projects and IRPT_BCKEND, D3, D11, D0: the CTO reads each one's state and
  brings Andrew an order rather than guessing one.

## THE CARDS HE ANSWERED -- VERBATIM

```
+-- CALL 1 of 3 ---------------------------------------------------+
  **Should the sequence only be tracked, or also enforced? (a) track: the reader flags out-of-order work and I raise it; (b) enforce: the task-order gate refuses new orders for a project whose stage isn't open**
  Enforcement is a new approval gate, and only you can ask for one.
  --------------------------------------------------------------------
  **REC --** (a) now, and (b) once the order has held for a week or so. A gate on an order still being settled would block legitimate early work like card 3 tonight.
+---------------------------------------------------------------------+

+-- CALL 2 of 3 ---------------------------------------------------+
  **Does the 07-28 sequence in `GOALS.yaml` still stand?**
  It reads: "MDPF COMPLETION" first, then a "DIRECT PIVOT" to the ETF and EventBridge scheduling fixes, gated on the first completing. It predates tonight's LGIC-first word.
  --------------------------------------------------------------------
  **REC --** Replace it with the new document. I'd re-place the MDPF and ETF scheduling projects inside the new stages, and keep the 07-28 wording as history, so there's one order instead of two that disagree.
+---------------------------------------------------------------------+

+-- CALL 3 of 3 ---------------------------------------------------+
  **Should 0.0.0_AB_MSTR seat a COO lane for LGIC_NAMING now? (yes / no)**
  Its PRD is fully signed, and Stage 1 can't start without a lane to break it into work orders. 0.0.0_AB_MSTR won't start a session without your explicit word.
  --------------------------------------------------------------------
  **REC --** Yes. It starts Stage 1 while I write LGIC_ENFORCE's PRD.
+---------------------------------------------------------------------+
```

## WHAT IT RULES, AND WHO ACTS

| # | Ruled | Actor |
|---|---|---|
| design | The laptop sequence document as designed above, owned by the CTO, changed only on Andrew's word | `1.0.0_SA_CTO` builds it and the reader; `0.0.0_AB_MSTR` grants the lane for `org/missions/SEQUENCE.yaml` |
| 1 | **(a) TRACK now.** The reader flags, the CTO raises. **(b) ENFORCE is approved to follow once the order has held about a week** -- a task-order gate limb refusing new orders for a project whose stage is not open. Before arming (b), the CTO states the date the order has held since and announces it; arming is the CTO's act on this word, not a fresh decision | `1.0.0_SA_CTO` |
| 2 | **The 07-28 priority sequence in `GOALS.yaml` is REPLACED** by the new document. Its wording is kept as history; `GOALS.yaml` points to `SEQUENCE.yaml`; the MDPF and ETF-scheduling projects are re-placed inside the new stages | `0.0.0_AB_MSTR` edits `GOALS.yaml` (its lane); `1.0.0_SA_CTO` places the projects |
| 3 | **Seat a 2.0.0_SA_COO lane for LGIC_NAMING's L5** -- one project, the Tier-2 one-project-per-seat rule | `0.0.0_AB_MSTR` (spawn authority) |

## FOLLOW-ON, SAME EXCHANGE -- /self-drive ties into the document

Minutes after "recs approved", Andrew added, VERBATIM AND ENTIRE:

> "then make the /self-drive skill tie in to that document, so it both checks state of that document vs state of the
> repo, and makes sure that the driving is aligned with the sequence chronology and that docs are properly updated"

**What it rules:** `/self-drive` (`.claude/skills/self-drive/SKILL.md`) is amended so that, on every tick of a driven
scope on the laptop fabric, it (1) runs the sequence reader and reports where `SEQUENCE.yaml` and the repo's state
disagree; (2) drives only work whose stage is open in the sequence, raising any out-of-sequence work rather than
driving it; and (3) checks that the documents a stage's progress should have updated -- the sequence's own change log,
project rows, PRDs -- are updated, and names any that are not. Actor: `1.0.0_SA_CTO`.

## SECOND FOLLOW-ON, SAME EXCHANGE -- both fabrics, dependency-bound projects only, device-agnostic skill

Andrew added, VERBATIM AND ENTIRE:

> "yeah the skill should be device agnostic. the sequence will govern projects that require chronology compliance by way
> of dependencies/design. that means that it has to be writable by both the laptop cto and the sitez cto becuase there
> may be overlap"

**What it amends in the design above -- the design text stays as it was put to him; these override it:**

1. **ONE SEQUENCE FOR BOTH FABRICS, not the laptop box alone.** `org/missions/SEQUENCE.yaml` is writable by BOTH
   `1.0.0_SA_CTO` (laptop) and `1.0.0_SA_CTO~Z` (site Z), because projects on the two fabrics can depend on each other.
   The lane grant `0.0.0_AB_MSTR` makes names both serials. Each sequenced project carries the fabric that drives it.
   Either CTO changes the order only on Andrew's word, recorded in the change log.
2. **IT GOVERNS ONLY PROJECTS THAT REQUIRE CHRONOLOGY COMPLIANCE by way of dependencies or design.** A project with no
   ordering constraint is not placed. So the design's "any laptop project the file neither places nor parks" flag is
   DROPPED -- it would have forced every independent project into the file. The parked list stays for projects that are
   ordered but deliberately not now.
3. **THE /self-drive TIE-IN IS DEVICE-AGNOSTIC.** The same skill text runs on either fabric: it reads the sequence, checks
   it against the repo, and drives in sequence order on whichever fabric runs it. The skill's existing rule that work is
   never routed across fabrics stands; a cross-fabric dependency is read from the shared file and the register, and
   the other fabric's project is waited on, never driven. The follow-on above's "on the laptop fabric" reads "on either
   fabric".

## WHAT IT DOES NOT RULE

The Stage 3+ order (the CTO brings it to Andrew); any change to a running project's scope; arming enforcement before
the order has held.
