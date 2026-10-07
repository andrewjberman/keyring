# FINDING -- on dell2, `bun run` of a file outside a node_modules tree fetches packages from npm, silently (egress)

**Author:** `4.0.0_SA_CRO~DELL2`, 2026-10-07 12:09Z (08:09 ET). **For:** the seat that owns dell2's portal toolchain bring-up
(`0.0.0_AB_MSTR~DELL2`, msg 469, ruling 106207) to file as a row. Under the row-id rule in
`CTO_RULINGS_FOR_THE_DELLS_20261007_0850Z_TRADING_CALENDAR_AND_ROW_IDS.md` section 2, this file is delivered and the owning
seat mints the id. **Class:** HAZARD, ARMED until bun auto-install is disabled for agent shells.

## What happened (my act)

- I wanted to render the upload review card with four finding codes. I wrote a scratch script in the session scratchpad
  (outside the portal tree) and ran it as `bun run <scratchpad>/render_card.ts` from `C:\dev\ajb_workspace\portal`.
- The script imported `react-dom/server` by bare name. Bun found no `node_modules` beside the script, so it auto-installed
  the package from the npm registry. It printed nothing to say so.
- **Measured:** two new entries appeared in bun's global cache at 2026-10-07 08:08:42 EDT, the second the script ran:
  `C:\Users\Test\.bun\install\cache\react@19.3.0@@@1\` and `react-dom@19.3.0@@@1\`. Every other entry there is dated 03:58-03:59
  EDT, from the earlier pack placement. The portal pack holds 19.2.4; 19.3.0 was never on this box.
- The run then failed with "Invalid hook call": two copies of React were in play, 19.3.0 from the cache and 19.2.4 from portal's
  `node_modules`. That failure is how I noticed.
- This is egress off Opal infrastructure, which CLAUDE.md "Agent Autonomy" excludes and msg 469 forbids ("never npm or bun
  install"). The forbidden act happened without any install command being typed.

## The hazard

- `bun` auto-installs by default whenever an imported package cannot be resolved from the file's own directory upwards. Any seat
  that runs `bun run` or `bun test` on a file outside `portal/` can trigger it. The same applies to a linked worktree whose
  `node_modules` has not been linked yet, which is the case msg 469 names.
- It is silent: there is no prompt and no line in the output.

## Proposed disarm (proposed only; not implemented, per CLAUDE.md "do not manufacture friction")

- Turn auto-install off for every agent shell on the Dells, either with the `--no-install` flag or with
  `[install] auto = "disable"` in a `bunfig.toml`. Neither was tested here. The owner picks one and proves it with a negative
  control: a bare-import script run from the scratchpad must FAIL to resolve, not fetch.
- Until then: run portal scripts and tests only from inside `portal/` with `bun --no-install`.

## Cleanup

- The two cache entries are left in place. Deleting them is a deletion; it needs a human's word or the owner's act. They are
  inert unless another bare-import run resolves to them.
- This seat has not run bun outside `portal/` again.
