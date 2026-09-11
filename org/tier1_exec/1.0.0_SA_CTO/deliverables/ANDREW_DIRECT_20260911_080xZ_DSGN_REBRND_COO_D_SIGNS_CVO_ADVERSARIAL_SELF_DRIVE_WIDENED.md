# ANDREW-DIRECT 2026-09-11 ~08:0xZ -- THE D13 PROJECT IS `DSGN_REBRND`; `2.0.0_SA_COO~D` SIGNS ITS BRIEF HALF; `3.0.0_SA_CVO` CRITIQUES ADVERSARIALLY TO A STAMP; THE SELF-DRIVE LOOP WIDENS TO IT

**Terminal:** `1.0.0_SA_CTO`, as the arguments of `/endpoint --forward`. **Recorded by:** `1.0.0_SA_CTO`, same turn.

## VERBATIM AND ENTIRE

> --forward docs\briefs\portal-visual-elevation-brief-20260911.md. This is D13 project. If you alredy wrote it, great,
> write the PRD, get the signoff from 2.0.0_SA_COO~D specifically, and have 3.0.0_SA_CVO critque adversarially as well
> and work toward agreement/stamp, then move it along to COO~D. Furthermore you will need DSGN_REBRND (what i weould call
> this project) included in your /self-drive loop for this session.

## WHAT IT SETTLES

1. **The project's name is `DSGN_REBRND`.** It was minted `DSGN_PORTALVIS` at L3 (`7bcba4d345`, LOCAL, no task order
   and no PRD yet), so the rename is one commit across the CTO's own L3 carriers: the tree row
   `org/missions/D13/DSGN/DSGN_REBRND/`, the derived `org/projects/DSGN_REBRND.json`, the `DIRECTIVES.yaml` D13
   members line, and the two CTO records that named the old code. Nothing downstream cited it.
2. **The brief half of the PRD is signed by `2.0.0_SA_COO~D` itself.** The L4-R rule in `.tools/prd_signoff_lib.py`
   refuses, by default, the COO instance holding a project's round (separation of duties: that lane decomposes the
   brief half it would be signing). That default was this seat's design on his 05:3xZ word ("If CRO is not online, can do
   COO in their stead"), never his ruling. His word here names the round holder as the signer for THIS project, so the
   mechanism carries a **project-level designation** on the tree row -- `l4r_brief_signer` with `serial`,
   `authority` (this record, pinned) and the quoted clause -- which the library admits ONLY when the authority field is
   present; the separation-of-duties default is unchanged for every other project. The library, the stamp tool, the
   notifier and the L6 gate all read the same field, so the notifier routes the brief half to `2.0.0_SA_COO~D`, the
   stamp admits its signature, and the gate grades it SIGNED. `4.0.0_SA_CRO` is not asked for this half.
3. **`3.0.0_SA_CVO` reads the whole PRD adversarially** -- not only the ratified-text half it stamps -- and the CTO
   corrects same-turn until the CVO stamps ENDPOINT + CONTRACTS. A brief-half finding from the CVO is a correction the
   CTO makes before `2.0.0_SA_COO~D` signs; the CVO's stamp is still only on its own half.
4. **Then L5 goes to `2.0.0_SA_COO~D`** -- the notifier's ordinary release once both halves read SIGNED.
5. **The `/self-drive` loop's scope widens** from `D9 IRPT` to `D9 IRPT + DSGN_REBRND` for this session: the carrier
   clause in `org/XXX.md` 1b-F is amended, the scratchpad state carries three projects, and each tick measures
   DSGN_REBRND's L4-R halves and its L5/L6 movement alongside the two IRPT projects.

## WHAT IT DOES NOT SETTLE

- Whether a round-holding COO lane may sign the brief half on any OTHER project. Not asked; the default refusal stands.
- The D13 directive document (`docs/architecture/D13_DESIGN_PRD.md`, ABSENT) -- `0.0.0_AB_MSTR`'s, unchanged.
