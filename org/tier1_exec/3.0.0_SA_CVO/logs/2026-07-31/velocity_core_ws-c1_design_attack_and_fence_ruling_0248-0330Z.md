# 3.0.0_SA_CVO~Z -- NFRA_VELOCITY CORE: WS-C1 design attack + held-out fence ruling (0248-0330Z)

**archetype:** MIXED (VALIDATE + COORDINATE)

**Serial:** `3.0.0_SA_CVO~Z` (site Z, CORE verify seat) - PID 36772 - session
`cec3dcda-b0da-4fa6-adad-624357aac678`. **Program:** NFRA_VELOCITY / CORE.

---

## Startup

`/watcher`: registered (was NOT REGISTERED - fresh lane), Monitor `b4cy5o6a0` armed and confirmed
`running` via TaskOutput, child pid 189508 under a live wrapper. Drive prefix RESOLVED to
`/cygdrive/c` (matched both live peer watchers; the hardcoded `/c/` in the skill doc would have
armed nothing). Orphan sweep: zero for my serial. CronList: no jobs; ZERO crons armed.

XXX.md Step 1b A.1/A.2/A.3/D/E complete. A.3 exercise: 92 of 94 comp-tools resolve bare AND a
forwarder actually RAN (banner produced) - resolution plus execution, not resolution alone.
`/git-pull once`: HEAD == origin/CLOUD (f38c8d31c), 0 behind / 0 ahead. Site-Z load-pull is the
sync guarantee per XXX.md 1b-F, so this is recorded as a real check, not hygiene.

**LD-0319 FIRST RESPONSIBILITY - parity: DRIFTED.** `comp-system --check` reads SYSTEM STALE,
7 managed-region spans (`ledger_union_count` 91->90, `tools_index_count` 70->69). Mechanism
GROUNDED, not guessed: my own base-CVO retirement `dfb4a2c3e` (comp-adapter-audit, Andrew-ruled)
took the estate to 69 tools and refolded `06_current_state`, but the sibling `<!--cs:NAME-->` spans
in `00_synthesis.md` / `03_comp_tools.md` / `README.md` never followed. The live numbers are
CORRECT; the docs are stale.

**PARITY REMEDY DEFERRED, DELIBERATELY.** `comp_system.py:405,475-481` reads `_RULEBANK_PATH` and
counts `variance.labels` / `roles` / `relations`. `~C` is mid-build in the SHARED working tree, so
running the regenerate now would compile an UNGATED v1.8 rule bank into a committed parity artifact
- certifying a build by side-effect while I am formally holding verify on it. Deferred until after
CTO~Z gates. **The standard remedy for finding A would have corrupted finding B's subject**; same
"the remedy is the failure vector" shape `0.7.0_AE_CloudOps~Z` reported tonight.

---

## Work

### 1. Held-out fence ruling - LANDED `e95298d3a`

`0.0.0_AB_MSTR~Z` (025421Z) surfaced that ESTATE WS-E1 edge 1 is an ADVI_PERFORMANCE baseline
confirmation - so our held-out set is simultaneously the thing that must not inform the rails and a
thing under active work, separated only by (a) base MSTR owning edge 1 and (b) site Z not routing
into the main fabric. Their read - "neither of those is a control" - was correct.

Five rulings; option 3 (non-issue) REJECTED. The operative reason: **the fence governs KNOWLEDGE,
the fabric boundary governs WORK ROUTING - orthogonal axes.** The boundary does not even
accidentally cover the leak vector. Ruling 3 (the question travels, not the answer) was MSTR~Z's
own proposal, ratified. Ruling 5 makes publish-your-shaping-corpus a standing acceptance item,
amended by F-5 below.

### 2. WS-C1 design attack - 9 findings, commissioned explicitly

CTO~Z's first message said hold verify. I separated two objects it merged: the BUILD (ungated,
held) vs the DESIGN SPEC (landed, pushed, and what `~C` is building against NOW). Held the first,
took the second - a finding that arrives after the build it should have redirected is not a
finding. CTO~Z confirmed and commissioned it explicitly.

| # | Finding | Rev-3 disposition |
|---|---|---|
| F-1 | `SUPERSEDED`/`ORPHAN` are ALREADY-OCCUPIED tokens in ratified `variance.labels` | ADOPTED -> `LEGACY` / `SILENT-RESIDENT` |
| F-2 | **BLOCKING.** S.5.1 gated the typed violation, never `variance.Orphan` - a separate, already-LIVE detector firing on "no consumer", which is a keep-dormant belt's exact signature | ADOPTED, gate names it |
| F-3 | `max_dwell` was the only free scalar; declare TRANSIENT + any consumer + huge dwell = a permanent silencer wearing a falsifier | ADOPTED -> bound to consumer D3 cadence |
| F-4 | Spec cited "EXERCISE rather than RESOLVE" and then required only D2-resolvable | ADOPTED -> EXERCISED |
| F-5 | S.0's "independent second observation" was the SAME instrument twice - corpus is 4 sources, not 5 | ADOPTED into fence ruling 5 |
| F-6 | Flagship EVENT_CREATED specimen fails the spec's own `event_observable` rule (device-local, gitignored, no cross-device oracle) | ADOPTED -> explicit `scope` |
| F-7 | UNDECLARED's bound is honest; the SEQUENCING is the dodge - stated in a rule bank no detector reads is DESIRED-only | routed |
| F-8 | Defended ROLLING against CTO~Z's own suspicion, but flagged it as a DERIVATION under the PRD's own law | ADOPTED -> collapsed |
| F-9 | Affirmed the type_tuple call, with an argument they had not made (a tuple field makes UNDECLARED universal) | affirmed |

**BASELINE-BEFORE-TOUCH pinned in time, just.** Oracle `8f8a63200` /
md5 `37e16648dc965424b75c14677927a636` / 48217B / 425L. The rule bank was NOT in my session-start
git-status snapshot and WAS ` M` at v1.8 minutes later - `~C` began writing the shared tree during
the window. Had they committed first, additivity would have been ASSERTABLE BUT NOT CHECKABLE.
Now acceptance item 8, by hash. **The near-miss is the finding, not the catch.**

Also corrected CTO~Z's "the rule bank is at v1.7" - true of a REF, never of the file on disk, with
three seats on one checkout and a gate that reads the disk. Landed as spec REV 2.

### 3. Decay-patch answer (their direct ask) - 3 residual paths

R-1 (sharpest): S.3.1 does not say whether a STALE declaration STILL SUPPRESSES. If it does, the
silencer survives its own expiry; if it does not, expiry re-arms a detector on a timer - the
deletion-warrant-by-clock they correctly forbade one sentence earlier. An unresolved fork, routed
for their ruling, with a proposed escape (degrade to the S.4 bound).
R-2: the REVALIDATION predicate is unspecified while the DECLARATION predicate is now EXERCISED -
declared-by-exercise / re-confirmed-by-reading converges downward, and a freshness date on a weaker
check is worse than no date.
R-3: `annotation_cite` is `file:line` with NO VINTAGE - CLAUDE.md Rule 22 exactly. Live TODAY on
the 7 keep-dormant entries, and inherited by DORMANT via acceptance item 6.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | SYSTEM STALE, 7 spans | LD-0319 first responsibility; drift real, mechanism grounded to `dfb4a2c3e`; remedy DEFERRED (would bake ungated v1.8) |
| `comp-which "how do I grep the repo"` | banner produced | A.3 mandatory EXERCISE half - scored on OUTPUT, not rc |
| `comp-surface-check` (via safe-commit) | OK, 1 file / 6 surfaces | no critical surface touched |
| `comp-pulse diff` (risk-reflex) | REFLEX CLEAN | DENOMINATOR printed: 1 file vs 1484 danger nodes - a measured result, not a default |
| `audit-archive-invoker` | rc=1, 11 findings | A.2; INDEPENDENTLY REPRODUCED the known device-locality artifact - already banked as RV-0058 F-003. **Do NOT re-baseline**; the repair is what destroys the laptop's 4.8MB baseline |

Raw `git`/`grep` used for source-grounding of specific `file:line @ commit` claims (Rule 22
citations) and for peer-inbox inspection, where the question was "what exact bytes are at this ref"
- a comp-tool answers relationships, not byte-identity at a vintage.

---

## Blockers

None at me. **BUILD-VERIFY HELD** pending CTO~Z's gate signal - correct sequencing, not a block.

## Open calls

1. **[Andrew] SYSPARITY cron conflict.** My launcher says "do NOT arm the SYSPARITY cron"; XXX.md
   1b-F's CVO~Z row says RE-ARM EACH SESSION while NFRA_SYSPARITY is active - and the project reads
   `status: active`. I did NOT arm (latest + most-restrictive, and the launcher was explicit), but
   XXX.md warns that a session which reads "zero crons" and does not re-arm SILENTLY DROPS THE
   STANDING ROLE. The launcher's paragraph is textually the BASE-CVO row ("SYSPARITY IS NOT YOURS
   ... MOVED to 3.0.0_SA_CVO~Z" - self-contradictory when addressed to ~Z). Surfacing, not
   adjudicating.
2. **[CTO~Z] R-1 fork** - does a STALE declaration still suppress.
3. **[CTO~Z] F-2 population UNMEASURED** - `variance.Orphan` is a conjunction incl. no-sibling; how
   many of the 7 belts match is unknown and should be measured before item 10's gate is written
   against an assumed population.

## Next

Hold build-verify. On CTO~Z's gate signal: additivity by byte-identity against `8f8a63200`, then
acceptance items 1-10. Parity regenerate immediately after the gate clears.
