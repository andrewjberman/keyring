# LGIC_NAMING — DECOMPOSITION (L5)

```json
{
 "project": "LGIC_NAMING",
 "directive": "D14",
 "macro": "LGIC",
 "fabric": "laptop",
 "decomp_version": "v5",
 "step": 5,
 "prd_ref": "org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@f0a830c15f",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO, current at v1.7", "brief": "SIGNED 4.0.0_SA_CRO @f0a830c15f (v1.7, review @cd596cf4a4)"},
 "author": "2.0.0_SA_COO~G",
 "cells": 14,
 "chains": 5,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~G`, seated by `0.0.0_AB_MSTR` (msg 96524, LD-0563 @`de2d8fd79d`) on Andrew-direct
2026-09-14 ~01:xxZ card 3, *"recs approved"* (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_01xxZ_LAPTOP_SEQUENCE_DOCUMENT_APPROVED.md` @`cc79b6191a`).
L5 is the COO's; no seat certifies this before L6.
**Input:** the PRD's SURFACE MANIFEST at `d6e0c3b74a`, ADMITTED (`prd-signoff.py status LGIC_NAMING` read 2026-09-14
~06:5xZ: both halves SIGNED, current). The L4 to L5 handoff arrived as `1.0.0_SA_CTO`'s hand relay (96538), because the
notifier's COO delivery was still addressed to the base serial.
**Sequence:** stage 1 of `org/missions/SEQUENCE.yaml`, `sequence-check --project LGIC_NAMING` flags none.
**v2, cut before any L6 issuance** on `1.0.0_SA_CTO`'s ask (96570), after PRD v1.3 re-opened and re-closed the brief
half; section 0 is the re-read, and v1's text below is amended in place where v1.3 reaches it.
**v3, cut before any L6 issuance** on `1.0.0_SA_CTO`'s ruling of row S10 into PRD v1.4 (96578); section 0b is that
re-read, amended in place where v1.4 reaches (3 cells).
**v4, the round-2 recut**, on `1.0.0_SA_CTO`'s round-1 analysis (L10, 96705 @`de52d3db04`; SC1 corrected
@`2706014705`) and PRD v1.6. Section 0c is the cut: 8 cells re-run, 4 of them in a clean-context seat. Round 1's text
below stands as its record.
**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md`).

**The rulings that reach every cell, from the PRD preamble:** the SOURCE-FIRST key string
`{source}/{scope}/{tier}/{table}/{partition}` (Andrew ~03:2xZ); the short forms `49f`, `inf`, `cot` beside the long
forms, and `bd` refused in every slot (~03:5xZ card 2); the per-slot split (S4, ratified at L4 by `1.0.0_SA_CTO`);
remediation shape (a). **S13 binds every cell: no cell renames a live name, and no cell creates, changes or applies an
AWS resource.**

---

## 0. v2 -- THE RE-READ AGAINST PRD v1.3

**What moved** (`git diff d6e0c3b74a 7bd4ef6f27`): the PRD's S1 paragraph and its `prd_version`; in
`NAMING_SCHEMA.json`, four `key` fields -- `partition` gains the entity form `{entity}={id}`, `table_case` bounds
kebab-case to NEW served leaves, and `legacy_served_path` and `code` are new -- plus the version, `ratified_by` and
changelog lines. The rulings behind them are `1.0.0_SA_CTO`'s adjudication of rows S6, S7 and S8 (96570, record @7bd4ef6f27).
**Nothing else moved:** not the SURFACE MANIFEST, the CELL CANDIDATES, ENDPOINT, CONTRACTS, the resource grammar, the
kind list or the 33-type partition. So section 1's domain, the 14 cells, the edges, the 5 chains and the distinct-worker
constraint all stand as cut in v1.

`comp-adversary` re-run on v1.3 (read-vintage HEAD `@b09ed6c736`, 2026-09-14T10:57:58Z): 6 of 6 cited commits verified;
11 cited paths, 9 stable and 2 GONE (`GRADING_RULE.md` and `TENSION_RANKING.md`, which this project mints). The brief and
the `.tf` no longer read as moved. L4-R: ADMITTED at v1.3 (`prd-signoff.py status LGIC_NAMING`, read ~10:5xZ; the brief
half re-signed by `4.0.0_SA_CRO` @81c9fdb639, the ratified-text half carried from v1.2).

**Which cells a v1.3 field reaches, by subtraction** (the 14 cells, minus those whose face or acceptance never reads
the changed `key` block):

```
  cells ........................................................ 14
  minus cells whose inputs never read the key block ............ -9
      LN-e-3, LN-e-5          compare and score strings; read no schema field
      LN-e-4                  the names only, by construction
      LN-f-1                  IAM roles: the resource grammar, unchanged
      LN-l-1                  a comment citing S1; S1's five-segment string is unchanged
      LN-h-1, LN-h-2, LN-h-3  grade from GRADING_RULE.md only; reached THROUGH LN-g-1
      LN-t-1                  the brief's IV.7 at its pin
  ------------------------------------------------------------
  cells a v1.3 field reaches ................................... 5
      LN-g-1                  grades S3Key names: the four new key forms need worked cases
      LN-e-1, LN-e-2          name items from the data file: the item set gains the two new forms
      LN-l-2, LN-l-3          read and score key segments: the address set gains the two new forms
```

What each of the five gains is written into section 3 and section 3a in place, each marked (v1.3).

**The one v1.3 change that is more than new forms.** `key.legacy_served_path` makes a platinum key's verdict depend on
whether it is a LEGACY served path, and nothing in `(name, type)` -- the grade's signature, CONTRACTS row 2 -- says
which. No field of v1.3 lists the legacy set. Two graders reading the same rule could therefore differ on the same key,
which is FWD-5's failure. v2 closes it for this round by requiring LN-g-1's written rule to **enumerate the legacy served
set it applies**, source named and denominator printed, so LN-h-1 and LN-h-2 grade from one list. Whether the set
becomes a data field, or `grade()` gains it as an input, is the contract's question: row `LGIC_NAMING-S10`, for
`1.0.0_SA_CTO`.

**Gate G-A is DISCHARGED** (@3514843a12, 96551; measured at HEAD, `docs/architecture/MDPF_CANON_PRD.md:16-18`). FWD-4's
second clause no longer waits on another project.

---

## 0b. v3 -- THE RE-READ AGAINST PRD v1.4

**What moved** (`git diff 7bd4ef6f27 e04b802fe9`): one clause of S1 and `prd_version`. In `NAMING_SCHEMA.json`:
`key.legacy_served_path` gains "MEMBERSHIP is data"; `key.legacy_served_paths` is new -- home
`deliverables/LEGACY_SERVED_PATHS.json`, producer cell LN-g-1, claim "absent until LN-g-1 lands it", and a RAISE until
then; `key.code` gains a legacy root `code/` key's verdict (OUT-OF-PATTERN, its canonical form the code-tier key). It is
`1.0.0_SA_CTO`'s answer to row `LGIC_NAMING-S10` (96578, record @e04b802fe9). **Unchanged:** ENDPOINT, CONTRACTS, the
grade's signature `(name, type)` and its three verdicts. `comp-adversary` was not re-run: the diff adds no cited path or
commit, only field names inside the data file already cited.

**Which cells v1.4 reaches, by subtraction** (the 14 cells, minus those whose inputs never read legacy membership or the
legacy-root verdict):

```
  cells ........................................................ 14
  minus cells that never read membership ....................... -11
      LN-e-1, LN-e-2          mint NEW names; the list governs only paths that already exist
      LN-e-3, LN-e-5          compare and score strings
      LN-e-4                  the names only
      LN-l-2, LN-l-3          label segment roles; a legacy bare-id path and a hive path both put the id in
                              the partition slot, so membership moves no label
      LN-l-1                  a comment citing S1
      LN-f-1                  IAM roles: the resource grammar
      LN-h-3                  compares two gradings; reads neither the rule nor the list
      LN-t-1                  the brief's IV.7 at its pin
  ------------------------------------------------------------
  cells v1.4 reaches ........................................... 3
      LN-g-1                  writes the list; grades a legacy root code/ key as ruled
      LN-h-1, LN-h-2          grade with the rule AND the list
```

**`1.0.0_SA_CTO` asked about LN-e-1, LN-e-2, LN-l-2 and LN-l-3 by name (96578). None is reached.** Membership decides
whether an EXISTING served path keeps its bytes, and none of those four cells grades an existing path.

**What the three gain** (in place in section 3, each marked (v1.4)):
- LN-g-1 gains its second write surface, `deliverables/LEGACY_SERVED_PATHS.json`: every served path below
  `{source}/{scope}/platinum/` that the frozen portal requests, with the portal vintage it read and the denominator
  printed. `GRADING_RULE.md` cites the file and carries no second copy of the list. Its worked cases gain a
  **discriminating pair**: two same-shaped platinum paths, one on the list and one off it, graded CONFORMANT and
  OUT-OF-PATTERN respectively. The pair proves that membership CHANGES the verdict, not merely that the list exists.
  The legacy root `code/` worked case carries the ruled verdict.
- LN-h-1 and LN-h-2 grade with `GRADING_RULE.md` and `LEGACY_SERVED_PATHS.json`.

**The RAISE window never opens for the graders.** `grade.unplaceable` RAISES on a membership-turning key until the list
lands. LN-h-1 and LN-h-2 are spawned only after LN-g-1's branch is merged (section 5), so the list is at HEAD before
either starts.

**Nothing structural moved:** the same 14 cells, edges, 5 chains and distinct-worker constraint. Section 1's domain
holds, because the list sits inside manifest row 2 (`deliverables/`). Rectangle row 6 stays "unchanged": the standards
file names the list's home, and no worker writes the standards file.

**L4-R at the cut:** ADMITTED at v1.4. `prd-signoff.py status LGIC_NAMING` (read ~11:4xZ) reads both halves SIGNED
current; the brief half was re-signed by `4.0.0_SA_CRO` @254ac1f2ab. The only open call on L6 is Andrew's (tree-row
blocking item 5).

---

## 0c. v4 -- THE ROUND-2 RECUT (L10: 1.0.0_SA_CTO's round-1 analysis)

**Input.** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md` @`de52d3db04`
(msg 96705), with its SC1 correction @`2706014705` (96725); PRD v1.6 @`2706014705`, ADMITTED (`prd-signoff.py status
LGIC_NAMING`: both halves SIGNED current; the brief half by `4.0.0_SA_CRO` @8e08704fb0, review @d60eefad00);
`NAMING_SCHEMA.json` v1.6. The analysis leaves the cells, their split and their order to the COO (s.7). All 14 of round
1's orders are terminal: RULING T flipped the last three @`a67425668b`.

**What re-runs: 8 of the 14 cells, by subtraction.**

```
  cells ........................................................ 14
  minus cells the analysis rules no re-run for .................. -6
      LN-g-1                  FWD-5 is exact; no re-run is ruled (s.5)
      LN-h-1, LN-h-2, LN-h-3  "No re-run is ruled for FWD-5's exactness" (s.5)
      LN-l-1                  the notice meets its clause (s.1, FWD-4)
      LN-t-1                  FWD-6 REALIZED (s.1)
  ------------------------------------------------------------
  cells round 2 re-runs .......................................... 8
      LN-e-1, LN-e-2, LN-e-3  FWD-1 on v1.6 (s.2; s.7 item 2)
      LN-e-4, LN-e-5          FWD-2 under Q, R, B and C (s.3; s.7 item 3)
      LN-l-2, LN-l-3          FWD-4 on the full layout briefing, K (s.4; s.7 item 4)
      LN-f-1                  FWD-3's qualification: the RAISE disposition (s.1; s.7 item 6; row W1-S5)
```

The analysis's item 5, the N6 answer format's step column (row `LGIC_NAMING-W5-S5`), is a FORMAT change with no cell in
this round, because no N6 grading re-runs. It is written into section 3a.4 for the next N6 run.

**The clean-context seat (RULING B), and where this cut widens it.** A worker subagent preloads the workspace CLAUDE.md
and the auto-memory (row S12), so a worker cannot be a blind party. The seat is
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/blind_seat.py`. It runs `claude -p` with NO tools (`--tools ""`) in a fresh
empty folder outside the workspace, with no CLAUDE.md up its parent chain and in no git repository. Its whole input is
one prompt, built from committed sources at the recorded base.
- **A worker OPERATES the seat with one command.** It cannot shape the prompt or edit the reply: the checker
  (`fixed_inputs/r2/check_ln_r2.py`) re-derives the prompt with the same builder and re-parses the verbatim reply,
  which the seat record hashes. With no tools, the seat cannot read the channel, so RULING C holds by construction.
- **Widened by this cut, from the reader to all four blind cells.** LN-e-1 and LN-e-2 (the namers, blind to each
  other) and LN-l-2 (the layout reader, which must meet the other buckets fresh) are seated the same way as LN-e-4.
  The reason is measured. A worker namer's worktree holds round 1's answer files and the round-1 analysis, whose s.2
  table prints the ruled name of all 18 items; blindness to those would bind by instruction only. A seat with no tools
  cannot open either. The analysis seats "the reader, and any cell whose criterion says blind"; section 5 gives
  LN-e-1, LN-e-2 and LN-l-2 blind constraints. The widening is surfaced to `1.0.0_SA_CTO` with the issuance.
- **The canary rides in every seat.** Each prompt opens with two questions whose answers exist only in the workspace
  CLAUDE.md (the Git Bash utilities version) and the auto-memory (the second fabric's broker port). A reply that
  carries either fact is not blind. That cell's canary criterion then FAILs, and its dependants are not spawned. On a
  leak in LN-e-4, FWD-2 returns to `1.0.0_SA_CTO` (s.3). One smoke seat with the same flags, run before this cut
  (session `dca841de`), answered both canaries `unknown`.
- **The seat is proved in LN-e-1 and LN-e-2 before any FWD-2 cell** (s.7 item 1): LN-e-4 spawns only after both of
  their canaries read blind.

**The briefing carries two of the 18 answers verbatim** (row `LGIC_NAMING-S15`, filed with this cut): i05 `opal-data-cottonwood`
at `05_IDENTITY_SPINE.md:68`, where the registry names the bucket, as a registry should; and i15
`orion-inf-build-gold-profile` at `NAMING_SCHEMA.json:125`, where SY1's example is item i15's ruled name. The schema is
the namers' ratified input, and this cut does not edit it. L9 reads those two agreements with the row in view.

**The re-run cells.** These replace section 3's rows for round 2; round 1's rows stand as its record. Every file named
here is under `exercises/r2/`.

| cell | round 2 | acceptance, one clause per line |
|---|---|---|
| `LN-e-1` | namer A, in a seat | the seat is proved clean (the record's ten conditions) · the canary finds no workspace-only fact · one name, or RAISE, for every item · the base carries `NAMING_SCHEMA.json` v1.6 |
| `LN-e-2` | namer B, in a seat | as LN-e-1 |
| `LN-e-3` | the namers' comparison | the two answer files are identical on every item · the two seats received the identical prompt, in two sessions |
| `LN-e-4` | the reader, in a seat | the seat is proved clean · the canary finds no workspace-only fact · a mark on every one of namer A's round-2 names: the firm, exactly as spelled, or none (Q) |
| `LN-e-5` | the reader's scoring | the mark equals `N3_KEY_R2.json` (firm or none) on every item · no token is read as two different referents (R) |
| `LN-f-1` | the firm patterns, with RAISE | round 1's four criteria, and J1, on `n4-firm-patterns.md` · the shape gains `raise` beside `attributed` and `excluded`: a RAISE carries its GRADING_RULE step, and no exclusion's reason is a RAISE |
| `LN-l-2` | the layout reader, in a seat | the seat is proved clean · the canary finds no workspace-only fact · a role list or DOES-NOT-FIT on each of the seven addresses, briefed with `N5_R2.json` (every tier's slots, code included; K) |
| `LN-l-3` | the layout scoring | every label equals round 1's `N5_KEY.json` · the legacy negative control reads DOES-NOT-FIT |

**Edges and slots.** Spawn after drain, as in section 5.

```
  LN-e-1 --+--> LN-e-3
  LN-e-2 --+
  LN-e-1 -----> LN-e-4 -----> LN-e-5
  LN-l-2 -----> LN-l-3
  LN-f-1        (no edge)
```

| slot | cells | spawned |
|---|---|---|
| ~1 | LN-e-1 (operates its seat) | at issuance |
| ~2 | LN-e-2 (operates its seat) | at issuance |
| ~3 | LN-l-2 (operates its seat) | at issuance |
| ~4 | LN-f-1 | at issuance |
| ~5 | LN-e-4 (operates its seat) | after LN-e-1 drains and both namer canaries read blind |
| ~6 | the scorer: LN-e-3, LN-l-3, LN-e-5, each as its inputs drain | when the first input drains |

**Fan-out:** 4 workers at issuance and at most 5 at once. With LGIC_ENFORCE's 3 level-0 workers, that is 7 of the
sequence-wide cap of 8. A seat is a process its operator starts, not a worker, so the slot count is the worker count.

**LGIC_ENFORCE.** The analysis orders LN-f-1's RAISE "before LGIC_ENFORCE's E9 consumes the list". No LGIC_ENFORCE task
order reads `n4-firm-patterns.md` by path. The one citation, in EN-f-1's face, uses round 1's measured 12 of 68 as
context, and EN-f-1 builds its fence from `fence_patterns()`. LN-f-1 spawns at issuance, and E9 (EN-s-1) sits at
LGIC_ENFORCE level 3 or later, so the order holds by timing. No edge is added to that frozen decomposition.

**L4-R at the cut:** ADMITTED at v1.6.

---

## 0d. v5 -- THE ROUND-3 RECUT (L10: 1.0.0_SA_CTO's round-2 analysis)

**Input.**
- The analysis: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` @`02f08322af`
  (msg 96818). It names what this issuance carries (s.5) and leaves the split and the order to the COO.
- PRD v1.7 @`f0a830c15f`, ADMITTED (`prd-signoff.py status LGIC_NAMING`; msgs 96821, 96823, 96826):
  - the ratified-text half is SIGNED by `3.0.0_SA_CVO`, current;
  - the brief half is SIGNED by `4.0.0_SA_CRO` @`f0a830c15f`, review @`cd596cf4a4`.
- `NAMING_SCHEMA.json` v1.7.
- All 22 of the project's orders are terminal. Round 2's last two closed by RULING T @`b9fa612c43`, and since @`fa6521ea12`
  the L10 precondition reads terminality from the proof instance.

**What re-runs: 6 of the 14 cells, by subtraction.**

```
  cells ........................................................ 14
  minus cells the analysis rules no re-run for .................. -7
      LN-h-1, LN-h-2, LN-h-3  FWD-5 is exact; no round-3 cell serves it (s.1)
      LN-l-1, LN-l-2, LN-l-3  FWD-4 REALIZED on the reading limb, 6 of 6 (s.1)
      LN-t-1                  FWD-6 REALIZED (round 1)
  minus the cell whose re-run waits on a non-zero count ......... -1
      LN-f-1                  s.5 item 3: "re-grades only if that count is not zero"; the count is 0 of 68 (below)
  ------------------------------------------------------------
  cells round 3 re-runs .......................................... 6
      LN-e-1, LN-e-2, LN-e-3  FWD-1 on v1.7 (s.2; s.5 item 1)
      LN-e-4, LN-e-5          FWD-2 under RULINGS DM and POS (s.3; s.5 item 2)
      LN-g-1                  the grading rule, re-cut to v1.7 (s.2 carrier 4; s.5 item 3)
```

**The count that settles LN-f-1, measured at this cut.**
- The two mechanical v1.7 steps were applied to round 2's 68 attributed canonical forms (`exercises/r2/n4-firm-patterns.md`):
  - FN1b's subtraction: drop a function token already written in the system or scope slot;
  - the own-kind bar: drop the resource's own kind.
- **0 of 68 change.** No function token equals its system or scope token, in the short form or the long, and none is
  `role`, IAM_ROLE's own kind (`kind.by_type`).
- So LN-f-1 does not re-run this round.
- LN-g-1 prints the same count from its re-cut rule, and the checker recounts it independently (`g1-count`).
  - A difference is a surprise row.
  - A non-zero count moves LN-f-1's re-grade to the next issuance.

**Row `W4-S1`, the bd paraphrase, which is this seat's.**
- Round 2's LN-f-1 face paraphrased R3 as a POSITION test. R3's own text is ADJACENCY to a firm token.
- The paraphrase retires with that face.
- The re-cut rule states the adjacency test in one added sentence (LN-g-1, item 4).
- Any later LN-f-1 face quotes R3 instead of paraphrasing it.

**The briefing (RULINGS DM and POS), and the one choice this cut makes.** `fixed_inputs/r3/blind_seat.py` is round 2's
seat with a new builder.
- **The namers** read the schema (v1.7) and the identity registry's three ROW files -- `scopes.json`, `systems.json` and
  `tiers.json` -- and never the seed `05_IDENTITY_SPINE.md`.
  - The schema's `rows_owner` gives the registry the ROWS: firms, products, vendors and subsystems. Those three files
    carry them.
  - `exemptions.json` and `remediations.json` are enforcement data, not identity rows. `LGIC_ENFORCE`'s fence cell writes
    `exemptions.json` in this same window, so a briefing that carried it could differ between seats spawned at different
    bases.
  - Measured before the cut, the two files spell 0 of the 18 ruled names, so leaving them out withholds no answer.
  - This choice is surfaced to `1.0.0_SA_CTO` with the issuance.
- **The reader** is told:
  - the slot order of each name family: the schema's `resource`, `iam_policy`, `secret` and `key` grammar lines and
    `bucket.data_bucket`, verbatim;
  - `firm_forms`;
  - the same three registry files.

  POS names `resource.grammar`. The reader's 18 names span five families (resource, IAM policy, secret, S3 key and
  bucket), and POS's reason -- position is the grammar the outcome tests -- holds for each family's grammar. The reader is
  never given the item set or the key.
- **Unchanged from round 2** (s.0c): the seat, its canary, the no-tools launch and the checker's re-derivation of prompt
  and reply.

**The briefing carries 1 of the 18 ruled names verbatim**, measured at this cut over the four briefing sources against
the round-1 analysis's s.2 table.
- `scopes.json` names i05's bucket `opal-data-cottonwood`, as a registry should. Row `LGIC_NAMING-S15` covers i05, and L9
  reads its agreement with the row in view.
- The schema v1.7 spells 0: EX1 moved SY1's example off i15's ruled name.
- The new example, `blackdiamond-cot-build-silver-profile`, is in no item set.

**The re-run cells.** These replace section 0c's rows for round 3; rounds 1 and 2 stand as their record. Every exercise
file is under `exercises/r3/`.

| cell | round 3 | acceptance, one clause per line |
|---|---|---|
| `LN-e-1` | namer A, in a seat | the seat is proved clean · the canary finds no workspace-only fact · one name, or RAISE, for every item · the base carries `NAMING_SCHEMA.json` v1.7 |
| `LN-e-2` | namer B, in a seat | as LN-e-1 |
| `LN-e-3` | the namers' comparison | the two answer files are identical on every item · the two seats received the identical prompt, in two sessions |
| `LN-e-4` | the reader, in a seat | the seat is proved clean · the canary finds no workspace-only fact · a mark on every one of namer A's round-3 names |
| `LN-e-5` | the reader's scoring | the mark equals `N3_KEY_R2.json` (unchanged) on every item · no token is read as two different referents |
| `LN-g-1` | the grading rule, re-cut to v1.7 | the printed FORMS CHANGED count equals the checker's recount · the header names v1.7 · J1 at L9: R5's two steps and their reason, R3's adjacency sentence, and no other step moved |

**Edges and slots.** Spawn after drain, as in section 5.

```
  LN-e-1 --+--> LN-e-3
  LN-e-2 --+
  LN-e-1 -----> LN-e-4 -----> LN-e-5
  LN-g-1        (no edge)
```

| slot | cells | spawned |
|---|---|---|
| ~1 | LN-e-1 (operates its seat) | at issuance |
| ~2 | LN-e-2 (operates its seat) | at issuance |
| ~3 | LN-g-1 | at issuance |
| ~5 | LN-e-4 (operates its seat) | after LN-e-1 drains and both namer canaries read blind |
| ~6 | the scorer: LN-e-3, then LN-e-5, each as its inputs drain | when the first input drains |

**Fan-out:** 3 workers at issuance, and at most 4 at once. `LGIC_ENFORCE` holds at most 4 live workers now (three re-runs
and EN-d-2), so the sequence-wide peak is 8 of the cap of 8.

**Andrew-direct ~05:0xZ (msg 96910, relayed by `1.0.0_SA_CTO`): LGIC is aimed at the MDPF, ADVI and IRPT pipelines.** No
round-3 cell takes its population from the estate: the N3 items are the analysis's fixed 18. The aim lands in
`LGIC_ENFORCE`'s next cut and in `LGIC_CANON`.

**L4-R at the cut:** ADMITTED at v1.7.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Written as the printed denominator MINUS what is excluded, never as a forward list.

```
  SURFACE MANIFEST rows at d6e0c3b74a ................................ 7   (denominator, parsed)
  minus the row marked "excluded" .................................... -1  (any live rename, registry row,
                                                                               builder, flagger, IAM change)
  minus rows whose kind is "read" / "read only" ...................... -2  (infra/logic/*; the live plane)
  minus the row DELIVERED AT L4 ...................................... -1  (org/standards/NAMING_SCHEMA.json,
                                                                               candidate N1 -- measured below)
  minus the row whose writer is ANOTHER PROJECT's owner .............. -1  (docs/architecture/MDPF_CANON_PRD.md
                                                                               s.3 -- "MDPF_CANON, at its own L4")
  ------------------------------------------------------------------
  WRITE SURFACES FOR THIS ROUND'S CELLS .............................. 2
     row 2   org/missions/D14/LGIC/LGIC_NAMING/deliverables/          (N2, N3, N4, N6, N7)
     row 3   infra/aws/terraform/shared-infra/s3-49financial.tf,
             the 2026-08-18 template comment only                     (N5)
```

The project's surprise channel (lane ANY, append-only) is written by any cell that files a row. It is a carrier, not a
deliverable surface, and every task order names it in `<paths>`.

**Falsifier 1: the domain against every path the PRD cites, not just the manifest.** `comp-adversary compose` over the
PRD (read-vintage HEAD `@d65f700ae0`, 2026-09-14T07:17:34Z) enumerated **10** cited repo paths: 6 stable, 4 flagged. The
two GONE are `deliverables/GRADING_RULE.md` and `deliverables/TENSION_RANKING.md`, which this project mints (row 2), so
their absence is correct. The two MOVED are the brief (consumed at its pin, §6) and the `.tf` (row 3, re-measured in
§2). No flagged path falls outside the manifest. The tool printed the six stable paths as a count, not by name, so this
falsifier covers the flagged four by name and the stable six by count only.

**Falsifier 2: the node-type domain the grade rests on.** Today's live plane (`comp-find --corpus aws`, vintage
*"Built from the estate as of 2026-09-14 05:54:17 UTC"*, manifest `fb5ab9e54b85`, 2,531 nodes) carries **33** node
types; `NAMING_SCHEMA.json` partitions **33** (18 `kind.by_type` + 15 `types_not_graded_by_kind`, overlap 0). Set
difference in both directions: **empty**. The PRD's type domain still is the plane's.

**N1, measured at the cut (no L7 cell, per the PRD's row):** `NAMING_SCHEMA.json` at HEAD parses, and **15 of 15**
probes for the S1-S13 enumerations are present (`key.grammar`, `bucket.data_bucket`, `resource.grammar`, `firm_forms`,
`resource.scope_when_shared`, `system.classes`, `kind.by_type`, `cadence.values`, `secret.grammar`,
`log_group.grammar`, `iam_policy.grammar`, `refused_tokens.bd`, `grade.verdicts`, `not_covered`,
`renames_authorized`).

**Status vocabulary.** Four values, and NOT-EVALUATED is one of them, so non-evaluation cannot be encoded as a verdict:

| value | meaning |
|---|---|
| `MEASURED` | evidence in hand at the cut, instrument named |
| `DECLARED` | the PRD or brief asserts it; not independently measured here |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply to this surface |

---

## 2. THE RECTANGLE

| # | write surface | current state | target state | collision set | evidence at cut | cell |
|---|---|---|---|---|---|---|
| 1 | `deliverables/GRADING_RULE.md` | `MEASURED` absent (comp-adversary GONE; `git ls-files` on the project folder lists `prd/`, `project.json`, `surprise-channel/` only) | the written, hand-applicable rule with worked cases | none, sole writer | `MEASURED` | LN-g-1 |
| 1b | `deliverables/LEGACY_SERVED_PATHS.json` (v1.4) | `MEASURED` absent at HEAD; the data file's own claim is "absent until LN-g-1 lands it" | a closed list of every served path below `{source}/{scope}/platinum/` that the frozen portal requests, with the portal vintage read and the denominator printed | none, sole writer | `MEASURED` | LN-g-1 |
| 2 | `deliverables/TENSION_RANKING.md` | `MEASURED` absent | the ten IV.7 rows, each with a cost line | none, sole writer | `MEASURED` | LN-t-1 |
| 3 | `deliverables/exercises/` (11 files, one per cell, named in §3) | `MEASURED` absent | exercise inputs, answers, scorings | none: no file has two writers | `MEASURED` | LN-e-1..5, LN-f-1, LN-l-2, LN-l-3, LN-h-1..3 |
| 4 | `s3-49financial.tf`, the `# Grammar (template = opal-data-{firm_id} ...)` comment | `MEASURED` at HEAD: the block spans `:8-14`. The PRD's `:8-13` omits the continuation line `:14`. Lines 1-16 are unchanged since the PRD's pin; the file moved after it at `:17-19` and `:24-38` (`37931439cf`, `0.7.0_AE_CloudOps`, the read-logging postcondition). | the comment states it is replaced by S1, citing this PRD; the diff is comment lines only | **three writers of one file:** `0.7.0_AE_CloudOps` (landed); `LGIC_ENFORCE` cell E5 (the bucket policy near `:93`, an APPLIED change, not yet cut); LN-l-1 (comment `:8-14`). Disjoint line ranges; only E5 is applied | `MEASURED` | LN-l-1 |
| 5 | `docs/architecture/MDPF_CANON_PRD.md` s.3 | `DECLARED`: the PRD says s.3 carries the older layout; this seat did not open s.3 | the replacement notice | N/A | `NOT-EVALUATED` | **none**: gate G-A (§6), row `LGIC_NAMING-S4` |
| 6 | `org/standards/NAMING_SCHEMA.json` | `MEASURED` delivered at L4 (§1) | unchanged | N/A | `MEASURED` | **none** (N1) |

**Worker admission is `NOT-EVALUATED` and is load-bearing.** Rows 1-4 sit in lanes that refuse a worker by lane
(`TREE_DELIVERABLES` for a file directly under `deliverables/` with no serial folder; `CLOUD_OPS_OR_ETL` for
`infra/aws/**`). A worker is admitted only by the `<paths>` block of its non-terminal order at HEAD
(`.tools/owned-paths-validate.py`, the `worker_grant` limb, `:114-120`). That cannot be exercised before an order
exists, so L6 exercises it on HEAD bytes after the issuance commit (gate G-C).

---

## 3. THE CELLS — 14

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1 (`PREFIX-<axis>-<digits>`), prefix `LN`. Axes:
`g` the grading rule, `e` the naming and reading exercises, `f` the firm patterns, `l` the key layout, `h` the
hand-grading agreement, `t` the tension ranking. Every file under `exercises/` is
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/`.

Each acceptance line below is **one criterion**. `J` marks a judgment criterion: no verdict at L7, graded by
`3.0.0_SA_CVO` at L9.

| cell | what it is | PRD candidate | serves | writes | acceptance, one clause per line |
|---|---|---|---|---|---|
| `LN-g-1` | the written grading rule, its worked cases, and (v1.4) the legacy served list | N2 | FWD-5 | `deliverables/GRADING_RULE.md`; (v1.4) `deliverables/LEGACY_SERVED_PATHS.json` | every worked case carries exactly one of CONFORMANT / ALIAS / OUT-OF-PATTERN with its canonical form, or a stated RAISE, or NOT-GRADED for an excluded type · a worked case for each of the **25 graded types** (§3a.5) · a worked case for each of the 3 verdicts · a worked case for each of the 5 census residue classes (camel IAM names, purpose-first policies, library-first layers, `default` security groups, workstream-coded schedules) · every worked case is a live name at a stated vintage · no worked case is a name in the N6 discriminating sample (§3a.4) · (v1.3) a worked case for each of the four v1.3 key forms -- a new family's entity partition `{entity}={id}`, a legacy served path (a bare entity-id segment and a snake_case leaf), a code-tier key `{source}/{scope}/code/{built_tier}/{file}`, and a legacy root `code/` key -- each with its verdict stated · (v1.4) `LEGACY_SERVED_PATHS.json` lists every served path below `{source}/{scope}/platinum/` that the frozen portal requests, with the portal vintage it read and the denominator printed · (v1.4) `GRADING_RULE.md` cites that file and carries no second copy of the list · (v1.4) a discriminating pair of same-shaped platinum paths, one on the list graded CONFORMANT and one off it graded OUT-OF-PATTERN · (v1.4) the legacy root `code/` worked case is graded OUT-OF-PATTERN with the code-tier key as its canonical form, as ruled |
| `LN-e-1` | namer A | N3 | FWD-1 | `exercises/n3-namer-a.tsv` | one name for every item of the fixed item set (§3a.1), briefed only with `NAMING_SCHEMA.json` and `infra/logic/05_IDENTITY_SPINE.md` · the record states its worktree base commit |
| `LN-e-2` | namer B | N3 | FWD-1 | `exercises/n3-namer-b.tsv` | as LN-e-1, blind to it |
| `LN-e-3` | the namers' comparison | N3 | FWD-1 | `exercises/n3-compare.md` | the two answer files are identical on every item · neither namer's recorded base commit contains the other's answer file |
| `LN-e-4` | the blind reader | N3 | FWD-2 | `exercises/n3-reader.tsv` | a mark on every name in the reader set (§3a.2): the token that is the firm or product, or `none`. Briefed with the names and nothing else |
| `LN-e-5` | the reader's scoring | N3 | FWD-2 | `exercises/n3-reader-score.md` | the reader's mark equals the item's scope on every name · no token is marked as two different referents across the set |
| `LN-f-1` | one pattern per firm | N4 | FWD-3 | `exercises/n4-firm-patterns.md` | exactly one pattern for each of the 4 firm keys (`49financial`, `inflection`, `cottonwood`, `demo`), written from S3-S5 · each pattern catches the canonical form (by LN-g-1's rule) of every live `IAM_ROLE` the census attributes to that firm, denominator printed · no pattern catches a principal attributed to another firm |
| `LN-l-1` | the template's replacement notice | N5, the `.tf` half | FWD-4 | `s3-49financial.tf` | the comment block states it is replaced by S1 and cites this PRD · the diff against the base touches comment lines only |
| `LN-l-2` | the cross-bucket reader | N5, the reading exercise | FWD-4 | `exercises/n5-reader.tsv` | a segment role on every segment of every address in the address set (§3a.3), briefed only with the `opal-data-assets` layout |
| `LN-l-3` | the cross-bucket scoring | N5 | FWD-4 | `exercises/n5-reader-score.md` | every label equals the ruled string's role for that segment · the legacy negative-control address is marked as not fitting the layout |
| `LN-h-1` | grader A | N6 | FWD-5 | `exercises/n6-grader-a.tsv` | a verdict, RAISE or NOT-GRADED, and a canonical form, for every name in the sample (§3a.4), using `GRADING_RULE.md` and (v1.4) `LEGACY_SERVED_PATHS.json` only · the record states its worktree base commit |
| `LN-h-2` | grader B | N6 | FWD-5 | `exercises/n6-grader-b.tsv` | as LN-h-1, blind to it |
| `LN-h-3` | the grading agreement | N6 | FWD-5 | `exercises/n6-compare.md` | the two gradings agree on every name, verdict and canonical form · the discriminating sample and LN-g-1's worked cases share no name · neither grader's base commit contains the other's answer file · `J`: every disagreement or RAISE is traced to the line of `GRADING_RULE.md` it exposes |
| `LN-t-1` | the costed ranking | N7 | FWD-6 | `deliverables/TENSION_RANKING.md` | ten rows in the brief's IV.7 order at `@1b42dbe758`, each with one cost line (what breaks, what someone does by hand, or what it blocks) · `J`: each cost line is one a reader can dispute |

**Coverage of the PRD's candidates: 7 of 7.** N1 → delivered at L4, no cell (the PRD's own row) · N2 → LN-g-1 ·
N3 → LN-e-1, LN-e-2, LN-e-3, LN-e-4, LN-e-5 · N4 → LN-f-1 · N5 → LN-l-1, LN-l-2, LN-l-3, and its `MDPF_CANON_PRD.md`
half as gate G-A, not a cell · N6 → LN-h-1, LN-h-2, LN-h-3 · N7 → LN-t-1.
**Coverage of the outcomes: 6 of 6.** FWD-1 LN-e-1/2/3 · FWD-2 LN-e-4/5 · FWD-3 LN-f-1 · FWD-4 LN-l-1/2/3 and G-A ·
FWD-5 LN-g-1, LN-h-1/2/3 · FWD-6 LN-t-1.

### Why the re-cuts

- **N3 → five cells.** The candidate bundles five acts by at least three people: two namings that must be blind to each
  other, a comparison, a reading that must be blind to both, and a scoring. A worker cannot grade its own blind answer,
  so every comparison and scoring is its own cell.
- **N5 → three cells and a gate.** The candidate bundles an edit here, an edit in another project's PRD, a reading and
  a scoring. The edit in `MDPF_CANON_PRD.md` belongs to that file's owner at that project's L4, per the PRD, so it is a
  gate and not a cell (§6, row `LGIC_NAMING-S4`).
- **N6 → three cells.** Two blind gradings and their comparison, for the same reason as N3.
- **N2, N4, N7 stay whole.** Each is one act by one worker on one file.

### 3a. THE FIXED INPUTS L6 CUTS INTO THE FACES

Decided here, so no worker chooses its own test. L6 inlines each one verbatim, in the faces named, and nowhere else.

1. **N3 item set** (identical in the LN-e-1 and LN-e-2 faces; the answer key only in LN-e-5's face). At least 16 items,
   each described in plain words that never spell a schema token (no `cot`, `49f`, `-role`), covering: each of the 4
   firms in a resource's scope slot; at least one shared (unscoped) resource; at least one product-scoped resource;
   **the resource that publishes Cottonwood's model-portfolio figures** (FWD-1's own example); a Black Diamond
   integration resource for 49 Financial (the `bd` trap); an EVENT_RULE or SCHEDULE (cadence in the last slot); a
   SECRET; an S3 bucket; a full S3 key address; (v1.3) a new per-entity served file (the entity partition); (v1.3) a code bundle in its code
   home (the code tier); an IAM policy; an IAM role; a dead-letter queue. **Systems only from the
   registry seed** (products `mdpf`, `etfs`; vendors `schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`,
   `pathfinder`, `trueshares`, `ycharts`). The seed has no system axis for platform subsystems (`05_IDENTITY_SPINE.md`
   §5; brief Part VI), so such an item would only RAISE and none is included.
2. **N3 reader set** (LN-e-4's whole face). Namer A's names only, item ids removed, order shuffled by a stated seed.
3. **N5 address set** (LN-l-2's face; the expected labels only in LN-l-3's face). At least six addresses conforming to
   the ruled string, in `opal-data-49financial` and in `opal-data-mdpf`. They are **target-state specimens, stated as
   such**: both buckets are tier-first today (`09_NAMING_CENSUS.md` §5; `01_CENSUS.md`). (v1.3) At least one specimen uses the entity partition and at least one the code tier. Plus **one live legacy
   tier-first address** from the 2026-08-18 template layout as the negative control. The reader's briefing is the
   `opal-data-assets` layout, explained with at least three real `opal-data-assets` addresses.
4. **N6 sample** (identical in the LN-h-1 and LN-h-2 faces; LN-g-1's face lists the discriminating names as forbidden
   worked cases). Rule: per node type, sort that type's live names ascending (byte order) at a stated vintage and take
   positions 1, ceil(n/2) and n when n >= 4; positions 1 and n when n = 3; position 1 when n = 2; and when n = 1 the
   single name, flagged OVERLAP because LN-g-1 needs it too. At vintage 2026-09-14 05:54:17 UTC that is 27 types x 3 +
   `ROUTE53_RECORD` 2 + `VPC_ENDPOINT` 2 + `CLOUDFRONT_DISTRIBUTION` 1 = **86 discriminating names**, plus **3 OVERLAP**
   (`ECS_CLUSTER`, `LOAD_BALANCER`, `STATE_MACHINE`), reported apart from the agreement denominator. The 8 NOT-GRADED
   types are in the sample, so both graders must return NOT-GRADED there. (v4) **From the next N6 run, the answer format gains a fifth column
   `step`**, required on every RAISE row: the `GRADING_RULE.md` step that raised (row `LGIC_NAMING-W5-S5`; round-1
   analysis s.5). Round 2 runs no N6 grading.
5. **N2's graded-type domain, by subtraction.** 33 node types minus the 8 marked NOT GRADED (`IAM_USER`, `KMS_KEY`,
   `CLOUDFRONT_DISTRIBUTION`, `SERVICE_PRINCIPAL`, `VPC_ENDPOINT`, `ROUTE53_RECORD`, `API_ROUTE`, `EVENT_SOURCE`) =
   **25 graded types**: the 18 of `kind.by_type` plus 7 graded by their own grammar (`EVENT_RULE`, `SCHEDULE`,
   `LOG_GROUP`, `S3_BUCKET`, `S3_BUCKET_POLICY`, `S3Key`, `SECRET`). Every one has at least one live node at the
   vintage above. ⚠ **This is wider than the PRD's fixture text, which names the 18 of `kind.by_type`.** The reason:
   N6 samples every type, so a type N2 never worked is a type where the two graders can agree only by luck, and a
   disagreement there cannot be traced to a line of the rule. Revertible at the round-N analysis.

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D14 is placed LAPTOP (Andrew-direct 2026-09-12 ~17:2xZ, recorded on the tree row's
`fabric_ruling`); every read and write surface above is in this workspace or the live plane read through
`comp-find --corpus aws`. **No cell is owned by a seat**; every cell is served by a worker at L7
(`0.9.0_WK_LGIC_NAMING~<n>`).

---

## 5. DEPENDENCY EDGES, CHAINS, AND THE DISTINCT-WORKER CONSTRAINT

Edges are keyed to **observed completion**: `A -> B` means B's acceptance cannot be evaluated until A's artifact is at
HEAD.

```
  LN-g-1 --+--> LN-f-1
           +--> LN-h-1 --+
           +--> LN-h-2 --+--> LN-h-3
  LN-e-1 --+--> LN-e-3
  LN-e-2 --+
  LN-e-1 -----> LN-e-4 -----> LN-e-5
  LN-l-2 -----> LN-l-3
  LN-l-1        (no edge)
  LN-t-1        (no edge)
```

**CHAINS (connected components of the undirected edge set): M = 5.**

| chain | cells | write surfaces |
|---|---|---|
| A, the rule | LN-g-1, LN-f-1, LN-h-1, LN-h-2, LN-h-3 | rows 1, 3 |
| B, naming and reading | LN-e-1, LN-e-2, LN-e-3, LN-e-4, LN-e-5 | row 3 |
| C, the cross-bucket reading | LN-l-2, LN-l-3 | row 3 |
| D, the notice | LN-l-1 | row 4 |
| E, the ranking | LN-t-1 | row 2 |

No file has two writers inside the project, so no edge here is a write collision. The one collision is across
projects, on the `.tf` (rectangle row 4).

### The distinct-worker constraint, which is the non-obvious part of this cut

The PRD's exercises only prove anything if certain cells are served by **different workers**:

| cell | must not share a worker with | why |
|---|---|---|
| LN-e-2 | LN-e-1 | two namers who never confer (FWD-1) |
| LN-e-4 | LN-e-1, LN-e-2, LN-e-3 | the reader must not have seen the item text or which name answers which item (FWD-2, "unaided") |
| LN-h-1, LN-h-2 | LN-g-1, LN-f-1, and each other | "two workers who did not write N2" (the PRD's N6 row), blind to each other |
| LN-l-2 | every cell whose face carries the schema or S1: LN-g-1, LN-e-1, LN-e-2, LN-f-1, LN-l-1, LN-h-1, LN-h-2 | the reader learns one bucket's layout and meets the others fresh (FWD-4) |

The scorers (LN-e-3, LN-e-5, LN-l-3, LN-h-3) are mechanical and may share one worker. A scorer is never the worker it
scores.

⛔ **The spine's queue rule and this constraint disagree, and the decomposition resolves it by spawn timing.** The
spine's L6 puts two task orders on one chain in one worker's queue. On chain A that would hand LN-h-1 to LN-g-1's
worker: the author of the rule would grade its own rule. So this decomposition serialises dependent cells by
**spawn after drain**. A slot for B is spawned only once A's branch is merged. It does not use a shared queue. Row
`LGIC_NAMING-S3` carries the tension to the CVO and the CTO.

**Blindness is enforced by instruction plus two mechanical checks.** Each namer and each grader records its worktree
base commit; LN-e-3 and LN-h-3 each check that neither base contains the other's answer file. The two namers are spawned
from one base commit, and so are the two graders.

**The fan-out this decomposition supports: N up to 8 over M = 5 chains, cap 8. N exceeds M, and the reason is
blindness.** A slotting that satisfies every constraint above (L6's to choose and defend):

| slot | cells, in order | spawned |
|---|---|---|
| 1 | LN-g-1, then LN-f-1 | at issuance |
| 2 | LN-e-1, then LN-l-1, then LN-t-1 | at issuance |
| 3 | LN-e-2 | at issuance, from slot 2's base |
| 4 | LN-l-2 | at issuance |
| 5 | the scorer: LN-e-3, LN-e-5, LN-l-3, LN-h-3, each as its inputs drain | when the first input drains |
| 6 | LN-e-4 | after LN-e-1 drains |
| 7 | LN-h-1 | after LN-g-1 drains |
| 8 | LN-h-2 | after LN-g-1 drains, from slot 7's base |

Where a slot's continuation turns out to be a cold start, the constraint still holds, because a cold start is a fresh
context. The constraint binds on context, never on the slot number.

---

## 6. BATTERY DISPOSITION

### `comp-adversary`: RUN

`comp-adversary compose org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md`, read-vintage HEAD `@d65f700ae0` at
2026-09-14T07:17:34Z, artifact-vintage `d6e0c3b74a`.

| source | denominator | result |
|---|---|---|
| cited-commit verification | 6 attempted | **6 verified, 0 unverifiable** |
| cited-path vintage | 10 attempted | 6 stable, 2 MOVED-SINCE-AUTHORING, 2 GONE |
| uncited neighborhood | **1,597** siblings | cap declared (25 shown); 12 digested, 1,585 not digested (budget) |

**All four flags resolved at the cut, none a live defect:**

1. `deliverables/GRADING_RULE.md` and 2. `deliverables/TENSION_RANKING.md`: **GONE and correctly so**, because LN-g-1 and
   LN-t-1 mint them.
3. `docs/briefs/d14-naming-schema-brief-20260913.md`: MOVED after the PRD, at `2b64208047` (an L1 note in IV.2 on the
   five-segment key) and `9ba5e5370d` (the REFS PROJECT line). Measured by `git diff 1b42dbe758 HEAD`: **IV.7, which
   LN-t-1 consumes, is untouched.** Every cell consumes the brief at its pin `@1b42dbe758`.
4. `infra/aws/terraform/shared-infra/s3-49financial.tf`: MOVED after the PRD, at `37931439cf`. Measured by
   `git diff -U0 d6e0c3b74a HEAD`: hunks at `:17-19` and `:24-38` only, so **the template comment LN-l-1 edits
   (`:8-14`) is byte-unchanged** since the pin.

**Blindness, stated because the tool states it:** `T11: decomposition neighborhood NOT RESOLVED (artifact carries no
<decomp_ref>)`, so the 1,597-sibling complement is filesystem adjacency, not the dependency chain the spine asks a lens
to walk. Re-running it against a task order (which carries `<decomp_ref>`) at L7 resolves T11; this cut does not rely on
it.

### `comp-schedule`: RUN, and APPLICABLE

Self-test **PASS 6/6**. The first full view at the default 90 s budget returned **PARTIAL_OR_BLIND** (C1 scanned
145,919 of 196,642 files; C2-C5 NOT-SCANNED). It is recorded here because a partial view read as clean is exactly this
tool's failure mode. The re-run at `--budget 540` scanned **5 of 5 carriers** (C1 138, C2 6, C3 12, C4 21, C5 334):
**25 gates armed, none naming LGIC_NAMING or any surface in §2.**

**The promises-to-check-later this project creates, registered here:**

| gate | owner | the condition that clears it |
|---|---|---|
| **G-A** the `MDPF_CANON_PRD.md` s.3 replacement notice. **DISCHARGED @3514843a12** (96551; measured at HEAD: `docs/architecture/MDPF_CANON_PRD.md:16-18`) | `1.0.0_SA_CTO` (owner of that file, lane `docs/architecture/**` ANY_CTO) | s.3 states it is replaced by S1, citing this PRD. **FWD-4's second clause cannot grade REALIZED before it**, and MDPF_CANON reads `dep_stage: REGISTERED`, held in sequence stage 2. Row `LGIC_NAMING-S4`. |
| **G-B** `LGIC_ENFORCE` E9's comparison half | `LGIC_ENFORCE`'s COO lane (not seated; the request is at Andrew, per 96538) | LN-g-1's records land -- the rule and, since v1.4, `LEGACY_SERVED_PATHS.json`, which `grade()` itself reads -- and LN-h-3's. Not a gate on this project; recorded so the consumer's wait is visible from the producer's side. |
| **G-C** worker admission on `infra/aws/**` and on files directly under `deliverables/` | `2.0.0_SA_COO~G` | after the issuance commit, `owned-paths-validate --check-agent` on HEAD bytes PERMITs each slot on a path its order names and REFUSES it on one it does not |
| **G-D** the three-writer `.tf` | whoever cuts `LGIC_ENFORCE` E5 | nothing orders the two edits (disjoint lines); recorded so E5's cut reads LN-l-1's comment edit |

### `comp-iam`: DECLARED-NOT-APPLICABLE

`comp-iam` cross-references source-code operations against Terraform policies. **The reason is measured on the write
set, not on a token sweep.** A token sweep is the wrong instrument here, because this PRD names AWS resources on every
page: it is a naming schema for them. The write set is 13 markdown or TSV records under `deliverables/` plus one
comment-only hunk in one `.tf`. No cell adds an operation, a policy, a principal or a resource. LN-f-1 **writes** IAM
patterns as text and applies none. LN-l-1's second criterion enforces the comment-only diff mechanically. A checker
handed an empty set returns a vacuous pass that reads as clean, which is why this is NOT-APPLICABLE and not RUN-and-green.

⚠ **The bound on that reason:** it covers these cells. `LGIC_ENFORCE` E5 applies a policy change to the same `.tf`; its
IAM surface is `LGIC_ENFORCE`'s battery.

### Beyond the core

`comp-find --corpus aws` is an instrument inside cells (LN-g-1, LN-f-1, the §3a.4 draw), not a battery lens. No lens of
the admitted catalogue is claimed beyond the three above.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is §1's subtraction: 7 manifest rows placed exactly once each (1
excluded, 2 read, 1 delivered at L4, 1 written by another project's owner, 2 write surfaces), with two falsifiers run
before use (every cited path; the node-type set). **Exhaustive:** 7 of 7 candidates and 6 of 6 outcomes are covered
(§3). **Mutually exclusive:** yes on files (14 cells write 14 distinct files); deliberately not on outcomes, since
FWD-5 is served by four cells: the rule, two gradings and their comparison.

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one record, graded by a match or by a CVO
judgment. The re-cuts in §3 restore this grain where the candidates bundled acts by different people.

**(iii) INTENT COHERENCE.** One axis: **proving the schema by hand, before any machine exists.** No cell builds a
tokeniser, mints a registry row, renames a live name or changes an AWS resource. Those are `LGIC_ENFORCE`'s, or a
remediation's where the resource lives.

**(iv) STATE COHERENCE, and what each remedy does NOT move:**

- LN-g-1 moves the written rule. It does **not** move `NAMING_SCHEMA.json`: a worked case that exposes a schema defect
  is a row, never an edit, because the data file is L4's.
- LN-e-3 moves FWD-1's evidence of **agreement**. Identical strings do **not** prove conformance, since two namers can
  agree on a wrong name (§9).
- LN-f-1 moves a written pattern. It does **not** move any IAM policy, or the fence in `s3-49financial.tf`, which is
  `LGIC_ENFORCE` E5's.
- LN-l-1 moves a comment. It does **not** move a resource; the next plan reads no difference.
- LN-t-1 moves the ranking's cost lines. It does **not** re-rank or mint a remediation.
- LN-h-3 moves the agreement verdict. A disagreement does **not** move `GRADING_RULE.md` mid-round, because the round
  is frozen: it is a row for the round-N analysis.

---

## 8. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, stated so it can be argued with, and revertible at the round-N analysis.

1. N3 is cut into five cells, N5 into three plus a gate, N6 into three (§3).
2. Scoring is separated from answering in every exercise, so no worker grades its own blind answer.
3. N2's worked cases cover the 25 graded types, not the 18 of `kind.by_type` (§3a.5).
4. The N3 reader is briefed with the names and nothing else: the strict reading of FWD-2's "without looking anything
   up".
5. Every exercise input is fixed here and cut at L6 (§3a).
6. The fan-out may exceed the chain count, on the distinct-worker constraint (§5, row `LGIC_NAMING-S3`).
7. N5's `MDPF_CANON_PRD.md` half is a gate, not a cell (§6 G-A, row `LGIC_NAMING-S4`).
8. (v2) LN-g-1's rule must enumerate the legacy served set it applies (row `LGIC_NAMING-S10`). **Superseded at v3:**
   `1.0.0_SA_CTO` ruled it into PRD v1.4, so the list is now the PRD's requirement, landing as
   `LEGACY_SERVED_PATHS.json`, and no longer this decomposition's choice.
9. (v3) LN-g-1's worked cases include a discriminating pair (on the list / off it), so the list is proved to CHANGE a
   verdict, not merely to exist.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **`MDPF_CANON_PRD.md` s.3 was not opened.** That it carries an older layout is the PRD's assertion (`DECLARED`).
2. **Worker admission is not exercised** (gate G-C). It cannot be until an order is at HEAD.
3. **Blindness is partly by instruction.** After the issuance every task order is at HEAD, and a worker told not to
   read another cell's face or answer file could still read it. The two base-commit checks catch a leak through the
   answer files only.
4. **Agreement is not conformance.** FWD-1's bar is two identical strings; whether the agreed names are CONFORMANT is not
   a criterion here.
5. **The chain count and the constraint table are readings.** M = 5 follows from the edge set this document declares,
   and the distinct-worker table from the PRD's fixture text. Both are written out so they can be argued with.
6. **No cell has been exercised.** Every target state is a specification. No effort or duration estimate appears here,
   deliberately.
7. **(v3) The legacy served set is resolved at v1.4** (row `LGIC_NAMING-S10`, ruled): it lands as data at
   `LEGACY_SERVED_PATHS.json` and `grade()` reads it. Until LN-g-1 lands it, a membership-turning key RAISES. This
   decomposition does not claim the list's completeness: that is LN-g-1's measurement, with its denominator.
