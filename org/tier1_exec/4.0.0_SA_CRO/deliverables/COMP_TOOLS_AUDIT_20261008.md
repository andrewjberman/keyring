# Comp-tool audit -- does it work, is it used, and is the router dialled in

**Author:** `4.0.0_SA_CRO`, 2026-10-08 ~22:5xZ. **For:** Andrew. **Order:** Andrew-direct ~21:3xZ, verbatim in
`ANDREW_DIRECT_20261008_213xZ_COMP_TOOLS_AUDIT_DELETE_UNUSED_REVIEW_COMP_WHICH_ROUTER.md` (same folder).
**Evidence (same folder):**
- `COMP_TOOLS_USAGE_CENSUS_20261008.md`: per-tool use from four sources, laptop plus site Z.
- `COMP_TOOLS_HEALTH_CENSUS_20261008.md`: per-tool safe exercise, no writes.
- `COMP_WHICH_ROUTER_REVIEW_20261008.md`: the rail and the router, designed vs used.
**Nothing was deleted.** One live hazard was disarmed (section 4).

---

## 1. Conclusion

1. **Almost everything runs; most of it is not used.**
   - Health: 57 of 105 tools proven working, 45 load but their real path was not exercised, 3 had no safe path, and
     0 are broken.
   - Use over 30 days (100 tools): 24 used weekly, 27 monthly, 7 run only inside hooks, gates or other tools, and
     41 have no use in any source. One (comp-aws) is already deprecated.
2. **Four tools carry nearly all the traffic:** comp-read (4,890 runs in 30 days), comp-pulse (10,245, almost all from
   the commit hook), comp-find (2,668) and comp-which (4,863). After them come comp-iam, comp-surprise, comp-pipescript,
   comp-kuzu, comp-routes and comp-system. Most of the rest are one-project instruments built for a round and not used
   since.
3. **The router is not dialled in.** The rail works as a fence; comp-which barely works as a router.
   - Last 7 days: 88 organic comp-which calls on the laptop and 21 on site Z, against 911 and 1,403 rail denials.
   - Over 30 days, 41% of laptop questions and 59% of site Z questions found no tool.
   - 58% of questions are rituals: "read this exact file", where the path is already known.
   - Of 7,713 comp-find and comp-read runs, 55 started from a comp-which suggestion.
   - The project that built the rail set "comp-tool use up, raw bypass down" as its acceptance (COMPRAIL AC5). This data
     does not meet it.
4. **The dormant tools cost routing quality.** comp-which offered 28 dormant tools in 30 days that nobody then ran:
   comp-clobber 224 times, comp-lease 222, comp-assets 77, comp-to 72, comp-dispatch 71. Retiring dead tools makes the
   router's answers better, not only the folder smaller.

---

## 2. The list (keep / fix / retire)

### KEEP -- in use (24 weekly + 27 monthly + 7 hook-wired = 58)

Full rows in the usage census. Hook- and gate-wired, keep even with no agent use: comp-glob, comp-grep, comp-missions,
comp-pii, comp-constants, comp-shell and pipescript.

### FIX -- in use, with a defect (health census section "defects")

| Tool | Defect | Fix |
|---|---|---|
| comp-describe | its self-test cannot be reached through the wrapper (exit 2) | forward `--self-test` |
| comp-depth | exits 0 on an unknown subcommand | exit 2 on usage |
| comp-ledger-agreement, comp-which-routing-test | the registry name does not resolve to a command; only the `.py` file exists | add the `comp-*` wrapper, or register the real name |
| comp-schedule, comp-estate | self-tests take 127 s and 62-90 s | a fast self-test arm |
| comp-pulse, comp-which, comp-estate, comp-system, comp-blast | 25-48% nonzero exits in 30 days | read each against its output contract; a nonzero may be a finding, not a failure |

### RETIRE -- no use in 30 days in any source and nothing in use calls them (41)

**R1 -- delete outright (not tools, or superseded): 4**

| Tool | Why |
|---|---|
| comp-stitch-refresh | un-retired twin of the retired local stitch publisher; disarmed today (section 4) |
| comp-v5-composite-test | a one-off live Lambda test from June, not a comp-tool |
| comp-dups (27 lines), comp-honesty (15 lines) | stubs; no runs |

**R2 -- retire from the router now, delete after two quiet weeks: 37.** All are dormant; every one either works or loads:
- comp-arity, comp-assets, comp-axes, comp-canon-motif, comp-chainrun, comp-claimlink
- comp-clobber, comp-cochange, comp-coverage, comp-deadgrant, comp-debris, comp-denytest
- comp-depth, comp-dispatch, comp-drift, comp-fedobs, comp-firmsep-sweep, comp-genesis
- comp-gitdrill, comp-icedrill, comp-imgread, comp-incrparity, comp-kit-striplist-gate, comp-learns-score
- comp-learns-status, comp-lease, comp-ontolint, comp-parity, comp-passcraft, comp-perf
- comp-residue, comp-tool-health, comp-tool-health-gate, comp-toolgraph, comp-tooltip, comp-whoread
- comp-to: it is named in `org/XXX.md` step E ("Start a TO with comp-to") but has no run in 30 days. Removing it
  needs the law-lock order for that file.

"Retire from the router" is the registry's existing `status: retired` (do-not-call; comp-which stops offering it). A
retired tool stays on disk and in git, so it can be restored in one commit. Deleting after two weeks removes the files.
Git history keeps them either way.

**Blind spots on "unused":** dell1 and dell2 usage logs do not exist in the archive, and Codex seats' typed commands are
not in the transcripts. Their runs are still caught when a wrapper logs (laptop). The two-week retire-before-delete
covers this.

---

## 3. The router: what to change (highest value first)

1. **End the read-a-known-file ritual.** A question naming an existing path goes straight to `comp-read <path>`. Say in
   rule 21 and the seat prompts that a known path needs no router. This is 58% of today's comp-which traffic, and it
   misroutes (an inbox read is ranked to comp-iam).
2. **Make routing measurable.** Log the asking seat and a route id on every route, and carry the route id onto the tool
   run that follows. Then "was the routed tool used?" is a query; today it cannot be answered (`.tools/comp-which:1780`).
3. **Separate real asks from tests.** Flag curated hits apart from fuzzy ones, and tag routing-test and harness rows. The
   route counts above include harness probes.
4. **Curate rules for the top no-fit questions:** inbox and handoff reads, commit and evidence verification, holdings and
   custody, "the canonical source of X".
5. **Narrow the deny to the case it was built for:** blind recursive repo grep. Let the overridden shapes pass: paths
   outside the repo, worktree and scratch paths, exact one-file line reads and census pipes. Those make up 1,177
   overrides and 1,097 census denials in 30 days. A denial also aborts every other command in the same Bash call. That
   happened twice in this session, and both times it pushed the search to the unlogged native tools rather than onto a
   comp-tool.
6. **Retire the dead tools (section 2)** so the router stops offering them, and finish COMPEFFICACY FWD-8 (the ratified
   short list), so a seat starts from the dozen tools that matter.
7. Then re-measure COMPRAIL AC5 in two weeks: organic comp-which use, no-fit share, and route-to-run follow-through.

---

## 4. Done today

- **comp-stitch-refresh disarmed** @42f4e0a2b7. Its lines 82-83 still ran `aws s3 cp` of the stitch artifact and marker
  to `s3://opal-313476888478-globgrph/stitch/`. That overwrites the cloud producer's served stitch, which NFRA_CLDGRPH S29
  made the only writer on 2026-09-09. Its twin `.tools/stitch-refresh` was retired then; this copy was missed. It now
  refuses first, exit 3. It had no runs in 30 days.

---

## 5. Not measured

- dell1 and dell2 usage; Codex seats' typed commands.
- Whether the 45 PARTIAL tools' real paths work. They load and print help; the real path would call AWS, rebuild a cache
  or need arguments.
- Whether each routed tool answered the question it was routed for. Not measurable until recommendation 2.
