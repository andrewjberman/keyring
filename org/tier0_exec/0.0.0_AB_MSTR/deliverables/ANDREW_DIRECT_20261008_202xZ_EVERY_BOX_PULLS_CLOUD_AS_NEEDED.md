# ANDREW_DIRECT 2026-10-08 ~20:2xZ -- every box pulls CLOUD as needed

**Channel:** laptop terminal, to 0.0.0_AB_MSTR. **Recorded by:** 0.0.0_AB_MSTR, same turn.

## Andrew's words, verbatim

> "I want to make sure that every box in the organization does a pull from CLOUD as needed to get all the newest
> information onto their device"

## Placement (infrastructure; MSTR lane)

- The pull is each box's `box-sync.sh box` pass (takes origin/CLOUD into `box/<box>`, ~0.5-0.9 s shared-tree touch,
  pushes `box/<box>`), run by the box's "Opal box-sync" scheduled task (Andrew ~20:1xZ, "B") and verified by the box
  manager's `/govern` Step 3a.7.
- The laptop (integrator) MEASURES every box each `/govern` cycle: `origin/box/<box>` contains `origin/CLOUD`
  (`git merge-base --is-ancestor`), else "behind by N". A box behind for two cycles is chased over the bus.
- First read 20:26Z, origin CLOUD a8689cb259: dell1 and dell2 current; laptop 89 behind (its task runs 20:30Z);
  site Z 691 behind (no box pass yet since its 19:5xZ switch).
