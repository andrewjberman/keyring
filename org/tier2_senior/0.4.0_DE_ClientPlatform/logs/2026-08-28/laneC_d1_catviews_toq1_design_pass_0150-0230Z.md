# laneC -- D1_CATVIEWS.TO-Q1-DE: the formatting/design pass on Asset Category Views (0150-0230Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Seat:** `0.4.0_DE_ClientPlatform~C` (new lane, seated this session; spawn audit carried only `~Y`/`~Z` for this base)
**TO:** `D1_CATVIEWS.TO-Q1-DE.formatting-and-design-pass` @`2a1ab2f003`, issued by `2.0.0_SA_COO~Z`, dispatch msg 11997
**Commits:**
- portal `f93fb832` on `DEV` -- `design(D1_CATVIEWS.TO-Q1-DE): the formatting pass on Asset Category Views ...`
- workspace `ad7580bee8` on `SITEZ` -- `deliver(D1_CATVIEWS.TO-Q1-DE): the design pass + 11 READ renders ...`

**Push state, MEASURED by ls-remote at 0226Z:** portal HEAD is LOCAL (`origin/DEV` = `f1180aadac`);
workspace HEAD is LOCAL (`origin/SITEZ` = `b2d2d6d7c4`). Push is the integrator's act. Both lines are
perishable and age the moment an integrator runs.

---

## What the window contains

Andrew's item-1 second half, VERBATIM: *"appropriately improving the formatting/design of the frontend
for that function."* No metric attached, so none invented -- his eye is the bar and the deliverable is
the rendered artifact. Five ACs, all met. Deliverable at
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/d1_catviews_toq1_design_pass_20260828/`
(11 PNGs + `TQ1_AC_RECORD.md` + one instrument).

## The finding

`L0_LABEL` maps `SMA -> 'SMAs'` precisely so the plural reads as a plural, and the card label carried a
CSS `uppercase` that painted it `SMAS`. The SOURCE IS CORRECT AND THE RENDER IS WRONG -- a grep for the
label finds `'SMAs'` and reports health. Found in the first read of the first screenshot.

The TO justifies the read-screenshot instrument on the CONTRAST class. That is true and not exhaustive:
a CSS transform overriding an authored string is equally invisible to every static check here and is not
about colour at all. Surfaced to `3.0.0_SA_CVO~Z` as widening the instrument's stated justification.

Same class, same read, but LATENT: three `PanelHeader title=` strings authored pre-shouted while
`PanelHeader` already applies `uppercase` (`PanelHeader.tsx:70`). Renders identically today. Labelled
latent rather than claimed as a visible win.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 EXERCISE limb -- scored on OUTPUT (its own banner), not on rc. 105 of 105 comp-tools resolve bare. |
| `to-check.py` | `--all --assignee 0.4.0_DE_ClientPlatform~C` | PASS | total=1, scanned=2151, unresolved_serials=0. |
| `to-check.py` | `--all --assignee 0.4.0_DE_ClientPlatform` | PASS | total=8, projects=7, unresolved_serials=5 (residue disclosed on the tool's own face). |
| `audit-archive-invoker.py` | XXX.md A.2 | WARN (expected) | 18 findings = 5 COVERAGE + 13 INTEGRITY. Direction test on the shrink class: 8 of 8 shrank, 0 grew, 0 unchanged -> device-axis, not tamper. NOT chased. |
| `safe-commit.sh` | 2 invocations, `-F` msgfiles written by the Write tool | PASS | Both `[msg-verify] MATCH`. Portal needed per-invocation `GIT_COMMITTER_*` (banked trap: the submodule has no committer identity). |
| `commit-gate` (via wrapper) | portal `.tsx` diff | N/A by design | Printed *"checked 0 of 1 file(s) -- NOTHING WAS CHECKED"*. Recorded because the TO predicted it; NOT cited as validation. |
| risk-reflex (`comp-pulse diff`) | pre-commit, portal | PASS | CLEAN on a printed denominator: 1 file vs 1351 danger nodes, map 26.1h old. |
| `ui-smoke.mjs` | 12 renders, 1440x900 fullPage | PASS | The load-bearing instrument. Every PNG READ, none merely captured. |
| `tsc -b` (`bun run typecheck`) | 4 runs incl. a mutant control | PASS | Control failed rc=2 naming `CategoryViewTree.tsx:48`, then rc=0 on revert. |

**What worked.** The mutant control. A clean `tsc` pass is worth nothing here until the instrument is
shown to fail ON THE FILE UNDER TEST, and injecting the mutant into `CategoryViewTree.tsx` specifically
(not some other file) is what makes the subsequent rc=0 mean something.

**What failed.** `--click "Primary > $43.00M"` timed out twice before I worked out the accessible name
excludes the chevron -- it is `aria-hidden`, so the name is `Primary $43.00M`. The failure handler's
own dump of control names showed `Primary>$43.00M` (raw `textContent`), which is a THIRD string and
sent me to the wrong hypothesis first.

**Gap found.** No comp-tool covers "render this route and look at it"; `comp-which` correctly has no
answer for it, and `0.0.0_AB_MSTR~Z` (msg 11858) named this case explicitly as one where the raw path
is the legal one. Recorded rather than worked around.

## Instrument written (not committed to the repo)

`absent_by_scope` is set ONLY on an HTTP 404 (`aum.ts:873`), and the repo's fixture proxy
DELIBERATELY never 404s -- an unknown firm gets a shape, because there a 404 would look identical to
"the fixture is not wired up". Correct for its job and structurally unable to reach that branch. Wrote
a 404 front door to exhibit it, filed it beside the evidence as `_instrument_notfound-proxy.mjs`, and
did NOT add it to the portal repo.

## The diagnosis that cost the most, and it was self-inflicted

`TaskStop` on a backgrounded `vite --port 5175` killed the wrapper and left the CHILD alive (pid 10420)
holding `[::1]:5175`. My fixture proxy then bound `0.0.0.0`/`[::]` on the same port SUCCESSFULLY,
because the orphan held only the more specific address. Both listened; requests split
nondeterministically. One render silently showed the `unavailable` fallback and read exactly like a
component I had just broken -- and I diagnosed it as my own regression first, then as a dead proxy,
before finding two PIDs on one port.

Transferable: **a port probe returning 200 does not tell you WHICH listener answered.** The
fixture-proxy header already warns that a cached bundle talking to the real origin renders the SAME
EMPTY PANEL as a working fixture; this is that same failure reached by a route the header does not name.
This is the watcher-orphan shape on a different process class. Surfaced to `3.0.0_SA_CVO~Z` as
{OBSERVATION, INERT}.

## Files Modified

See commit messages: `f93fb832` (portal), `ad7580bee8` (workspace). One code file total:
`portal/src/components/CategoryViewTree.tsx` (+107 -39).

**AC4 measured, not asserted:** 1 file changed repo-wide; `src/api/endpoints/aum.ts` and
`src/pages/ModelPortfolios.tsx` UNCHANGED (`git diff --quiet`); ZERO occurrences of
fetch/axios/url/request/api/endpoint/useEffect/localStorage in the diff. The file is CRLF while the
workspace is LF -- edits applied by normalising to LF for matching and restoring CRLF on write;
verified 0 LF-only lines left behind, so the `-39` is real re-writes and not a line-ending churn diff.

## Instrument traps hit (both previously banked, both fired anyway)

1. **Harness heredoc unescaped `\r\n`** into real newlines and corrupted the very block written to
   handle line endings -- the same shape `~Z` banked on 08-27. Repaired by regenerating that code with
   `chr(13)`/`chr(10)` so it carries no backslash escapes at all and cannot be damaged the same way.
2. **LF patterns against a CRLF file** matched 0 times. Caught only because the patch script asserts
   every needle matches EXACTLY ONCE and exits non-zero otherwise -- the guard cost nothing and turned
   a silent no-op that would have read as success into a loud failure on the first edit.

## Blockers

**None.** D1_CATVIEWS remains NO-SHIP and `category_views` unpublished. That gate blocks SHIP, not
BUILD; it is not this lane's, it was not touched, and no met condition was read as a lift.

## Current State

- TO-Q1-DE **complete at this seat**; `3.0.0_SA_CVO~Z` certifies. Report delivered to
  `2.0.0_SA_COO~Z` (id 12054) and `3.0.0_SA_CVO~Z` (id 12055), 2 DELIVERED / 0 QUEUED / 0 REFUSED.
- Both commits LOCAL as measured above. Nothing pushed by this seat.
- Portal main tree is on `DEV`, clean apart from a pre-existing untracked
  `.frontend-dev/runners/__pycache__/`. CWD returned to the workspace root.
- **Still running from this session** (deliberately left up so a certifier can re-render):
  `vite` on 5185 (pid 23224) and the category-views fixture proxy on 5175. The 404 proxy on 5176 is
  also up. Anyone reaping these should kill the CHILD pids, not just the task wrappers -- see the
  diagnosis section.
- Inbox Monitor armed all session (task `br8lxsqfh`, `parent-tied: pid 393789`). 3 messages received,
  all read and ACKed via `ack_messages` (11770, 11858, 11997).

## Next Steps

- [`3.0.0_SA_CVO~Z`] Certification. Record sections 2 (the instrument-justification claim) and 7
  (what I left alone) are where I would look first for disagreement.
- [`2.0.0_SA_COO~Z`] Two surprise-channel items, neither blocking, neither chased: the shared
  `AUMGrowthMetrics` N/A hierarchy (absence rendered as the loudest thing in its tile, wider than this
  TO), and the `TaskStop`/vite-orphan port collision above.
- [integrator] Both commits await the push leg.
