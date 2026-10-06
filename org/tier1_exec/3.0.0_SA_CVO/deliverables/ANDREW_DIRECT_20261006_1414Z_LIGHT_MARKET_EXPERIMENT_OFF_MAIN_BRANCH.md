# ANDREW-DIRECT 2026-10-06 14:14Z -- the light /market is an experiment, kept off the main branch without his explicit approval

**Channel:** typed at the `3.0.0_SA_CVO` terminal (laptop), after he looked at the light /market on port 5174 (served by
this seat from portal DEV `cf3f10c6`, which carries `4ca437eb`). Clock read at recording: 14:14Z (10:14 AM Eastern).
**Recorded by:** `3.0.0_SA_CVO`, same turn.

## Verbatim

"I just saw it, it is an interesting idea, but lets keep this off the main branch. i am interested in this experiment but
it must be noted to be kept off the main branch without explicit approval."

## What was in front of him

The /market page as the first light-panel page: DSGN_REBRND R17, delivered by `2.0.0_SA_COO~D` in portal `4ca437eb`
(with the role tokens and light scope of `14dcce76`), on CTO ruling 105547. Graded by this seat
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_FWD3_PINS_GRADE_20261006.md`, the 4ca437eb addendum; row
DSGN_REBRND-S28 ARMED for its tooltips).

## What it states (as written)

- He finds the light-panel page an interesting idea and is interested in the experiment.
- It is kept off the main branch.
- It stays off the main branch until he explicitly approves otherwise.

## What it does not state, and is not decided here

- Which branch "the main branch" names. At this recording the change is ALREADY on portal `DEV` (`4ca437eb` is an ancestor
  of `origin/DEV` `cf3f10c6`); it is not on `PROD`. Whether his word asks for it to come out of `DEV`, or only never to reach
  `PROD`, is put to him in the same turn.
- How it is taken off, and where the experiment lives instead. That is the portal lane's and the CTO's, not this seat's.

## Routing

One line to `1.0.0_SA_CTO` naming this record (it changes `2.0.0_SA_COO~D`'s work on DSGN_REBRND R17).

## Clarification, 14:39Z at the same terminal -- VERBATIM

Asked which branch "the main branch" names (portal DEV, where the change already is, or PROD), he answered:

"it should be off portal dev and off production."

So the light-panel /market (portal `4ca437eb`, with the role tokens and light scope of `14dcce76`) comes OFF portal `DEV`
and does not reach `PROD`, until his explicit approval. At this recording `origin/DEV` reads `cf3f10c6` and carries both commits;
`PROD` does not carry `4ca437eb`. How it comes off DEV, and where the experiment is kept, is the portal lane's and the CTO's.

## Direction, 14:43Z at the same terminal -- VERBATIM

After this seat said the removal was the CTO's to place with 2.0.0_SA_COO~D, he answered:

"i took COO~D offline, you do it"

So 3.0.0_SA_CVO takes the light-panel /market off portal DEV itself, on his word, and keeps the experiment on its own
branch. This is outside this seat's usual verifier-only lane, and it is done because he said so.

## Done, 15:05Z -- and checked first that it had not been done

Andrew: "verify it has not already been done, if not, then you do it." At 14:4xZ origin/DEV was cf3f10c6 and still set
`data-surface-world="light"` on /market; no remote branch and no worktree held a revert.

- Two reverts on a branch from cf3f10c6: 0bb079b8 (reverts 4ca437eb) and 84ca4161 (reverts 14dcce76). Every src file the
  two commits touched now equals its state at 14dcce76^ (0 differ); the instrument scripts are kept.
- Checks before the push: `tsc -b` rc 0; `vite build` 22.2 s; `bun test` src/lib and src/ui/components 23 pass, 0 fail;
  /market 1159 siblings and /attribution 215, 0 below 4.5:1, the page on its dark panels again.
- The light version is kept whole on `origin/experiment/light-market` @cf3f10c6.
- Portal DEV fast-forwarded cf3f10c6 -> 84ca4161 under the audited `never-override` (PUSHPULL_AUTHORITY), citing his
  words; the push carried exactly the two reverts. CI - Build & Validate on 84ca4161: success. PROD never carried it.
- Told 1.0.0_SA_CTO and 0.0.0_AB_MSTR (msgs 105610, 105611).

-- 3.0.0_SA_CVO
