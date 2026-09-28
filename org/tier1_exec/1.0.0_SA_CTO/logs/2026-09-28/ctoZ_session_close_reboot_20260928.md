# Session log -- `1.0.0_SA_CTO~Z`, 2026-09-26 ~22:2xZ to 2026-09-28 ~17:1xZ -- SESSION CLOSE for the site-Z reboot

**archetype:** MIXED

**Restart map:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SITEZ_AMGT_REBOOT_STATE_20260928.md` -- read it first.
**Andrew-direct records this session:** `ANDREW_DIRECT_20260927_1723Z_OPEN_CALLS_RECS_APPROVED_PYTHON_PATH_AND_SERP_AFTER_IDENTITY.md`
(@`a89b7619ca`); `ANDREW_DIRECT_20260928_161xZ_CLOSE_OUT_SITEZ_FABRIC_FOR_REBOOT.md`.

## What this session did

- **Found the fabric-wide MCP outage's cause:** bare `python` -> a gutted Python 3.14 (stdlib emptied 2026-09-26
  17:02Z). Andrew approved taking it off PATH (his admin act, not yet run). Set user `PY_PYTHON`/`PY_PYTHON3`=3.11 so
  `py.exe` and the comp-* `.cmd` shims work.
- **AMGT_HARVST, rounds 7-10 analysed** (`ledger/ROUND_ANALYSIS.round7..10.md`), PRD v0.3 addendum
  (`C-HV-EVENT-SPINE` counts publishers over tier-A only; CVO~O re-signed), timeline placement ruling (above the header
  feed), never-widen CTO half for the `chatter_event` rebuild, portal `92a2576254` reviewed and approved -- and found
  the timeline's backend route was never mounted, so the portal push is held until round 11's `z-0`.
- **Routing while CVO~Z / COO~Z / COO~X were wound down:** HARVST L8-L10 routed to `3.0.0_SA_CVO~O` (standing, until
  CVO~Z is re-seated).
- **Shared tools fixed:** `missions-tree-index.py` (sparse-cone false orphans, @`454fc37e30`); `comp-find` (unknown
  flags silently scoped searches to nothing, @`2d2f697a82` + regen @`f4d0ef436b`); `prd_signoff_lib` status wording
  (@`ea81ad7be3`).
- **Rulings for peers:** placeholder-with-space workaround ratified; dead-seat base slices are read by the next
  session of that serial; the patch-target audit is one cell (`z-3`).
- **Closed a false open deploy** (`amgt-crosswalk-0924-rollback`, closed in the world 09-24, never committed) @`c292ef25b7`.

## My own errors, recorded

- Round-8 finding 1 ("the repair cell did not repair") was wrong on both horns -- corrected in place on COO~Y's measurement.
- Round-10's FWD-4 paraphrase ("headline / opening") turned WHETHER facts into text and sent COO~Y to a false fork.
- Round-10 said FWD-5 waited only on Andrew's portal word; the backend route was missing. Found while signing, corrected.
- One commit message was written with shell `printf` (Rule 14a names a non-shell writer); plain ASCII, no harm, noted.

## Compiler Tools

`comp-find` used as the search rail throughout -- and it was the tool that turned out to be broken: `--width`
silently emptied its scope (MSTR~Z's find), fixed here with a zero-file-pathspec refusal whose TRUE-negative arm still
reads rc=0. `prd-signoff.py status` read before and after the v0.3 addendum, and its "current" disproved against
`half_hashes()` computed at both pins. `missions-tree-index.py check` compared byte-for-byte before/after on a full
checkout plus a real sparse-cone worktree (27 -> 0 orphans) and a planted-mutant negative control. The rail FP-test
(`comprail-gate1-fptest.sh`) read 0/53 under the broken Python and 53/53 under 3.11 -- an instrument failure first, a
gate result second. Gaps: `safe-commit.sh` and the rail hook both depend on bare `python`, so a gutted interpreter
fails them silently or loudly depending on the shell.
