# Measured limits of this module's instruments -- read before treating a ZERO as evidence

**Filed 2026-09-09 by `1.0.0_SA_CTO~Z`, disarming ARMED rows `NFRA_REPORT-Z-W1-S1` and
`NFRA_REPORT-Z-W1-S2` (`0.9.0_WK_NFRA_REPORT~1` at `TO-RP-s-7`).** Both were found while GROUNDING a
deprecation walk, not while testing the tools, and both are **ESTATE-WIDE rather than specific to
that cell's ten candidates.** That is why they live here and not in a project deliverable.

**ADDENDUM 2026-09-10, `LIMIT 3` below, filed by `0.9.0_WK_NFRA_REPORT~2` at `RP-s-19`, disarming ARMED
row `NFRA_REPORT-Z-W2-S6`.** Found the same way as LIMIT 1/LIMIT 2 -- while GROUNDING an anomaly-row
connected-resources breakdown for a real edition, not while testing the tool -- and estate-wide rather
than specific to the one row (`opal-infrastructure-alerts`) that surfaced it.

**ADDENDUM 2026-09-10, `LIMIT 4` below, filed by `1.0.0_SA_CTO~Z` dispositioning ARMED row
`NFRA_REPORT-Z-W1-S5` (`0.9.0_WK_NFRA_REPORT~1` at `RP-s-16`).** Found the same way as the other three
-- while GROUNDING a cell's own work rather than while testing the tool. ⛔ **IT IS THE ONE ENTRY HERE
WHOSE ROW IS `DISMISSED_WITH_REASON` RATHER THAN DISARMED, AND IT IS THE ONE THAT BINDS EVERY OTHER
LIMIT ON THIS PAGE** -- a caller who reads LIMIT 1, 2 or 3 from inside a linked worktree is reading
about instruments that were not looking at the caller's tree in the first place. It was filed here
because that dismissal removed the row from one project's L10 predicate and would otherwise have left
a live, estate-wide, unowned hazard recorded only in `NFRA_REPORT`-scoped places, where no seat on any
other project could find it. Gap measured and raised by `2.0.0_SA_COO~ZZ` at msg 20823.

**ADDENDUM 2026-09-10, `LIMIT 4a`, surfaced by `2.0.0_SA_COO~Z` (msg 20831) from an OBSERVED instance and
traced to source by `1.0.0_SA_CTO~Z`.** The same corpus-resolution defect fires inside `comp-pulse`, which
`.tools/safe-commit.sh` runs as the PRE-COMMIT RISK REFLEX -- and there it **skips the risk reflex for the
whole commit**, not just for the worktree-created file. ⭐ It also RULES OUT the worse case that report
raised as untested: `risk_reflex()` never opens a subject file, so there are no wrong bytes to read.
**Severity moved in both directions and the entry says which way on each.**

> ⛔ **THE SHARED FAILURE MODE: A FALSE ZERO AND A TRUE ZERO READ IDENTICALLY.** LIMITS 1-4 below
> produce an EMPTY RESULT rather than an error, and an empty result from a dependency tool is exactly
> what a deprecation, decommissioning or blast-radius decision treats as permission to proceed.
>
> ⛔ **`LIMIT 4a` IS THE EXCEPTION IN SHAPE AND THE WORST IN EFFECT:** it does NOT produce an empty
> result. It prints a DISTINCT answer-state (`SUBJECT_ABSENT_FROM_CORPUS`) and **silently skips the
> gate for the entire commit**, with `safe-commit` swallowing the return code. A reader looking only
> for empty results will not find it.

---

## LIMIT 1 -- `comp-blast` models NO edge between `GOLD_SCRIPT` and `Lambda` / `ReactComponent`

**Consequence, stated as the caller must apply it:** a `comp-blast` result of *no downstream
consumers* for a gold script is **NOT evidence for OR against** that script being dead. It is not a
weak signal. It is **no signal**, for the entire edge class.

**Measured (`0.9.0_WK_NFRA_REPORT~1`, 2026-09-09 ~21:0xZ):**

- `comp-blast 'gold:B_01.holdings_lots' --direction downstream --json` -- WITHIN BUDGET, scanned
  164 of 164, 164 distinct ids, prefixes `{gold:77, s3:87}` and **ZERO ids of any other prefix**: no
  `lambda:`, `component:`, `jsx:` or `arn:` node reached.
- **REPEATED on 9 more gold scripts** (B_02, A_03, INF_D_00, INF_D_04, INF_D_07, INF_D_03, INF_D_02b,
  INF_C_01, INF_D_00c). Every one returns only `gold:`/`s3:` prefixes where non-zero, or
  `ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS` where zero -- **including `INF_D_00b.portal_timeseries.py`,
  a script named for the portal it serves.**
- ⭐ **POSITIVE CONTROL, and it is what makes this a finding rather than a guess:**
  `comp-blast 'arn:aws:lambda:...:function:inf-api-positions' --direction upstream --json` on a lambda
  INDEPENDENTLY KNOWN LIVE (it backs a served portal API route,
  `infra/aws/lambda/inf-pipeline/inf-api-positions`). **The control FAILED in the same graph** -- so
  the instrument, not the candidates, is what is blind.
- **AND THE BLINDNESS IS A MISSING EDGE TYPE, NOT ABSENT NODES.** `comp-blast 'component:AdvisorsTab.tsx'`
  returns NOT-FOUND and prints the live node-type census: `ReactComponent=442`, `JSXRender=1433`,
  `JSXElement=2205`, `GOLD_SCRIPT=1380`, `S3_DATA_KEY=294`. **Both endpoint families are modelled.
  The edge between them is not.**

**What DOES answer the question** (this is the route around, and it is why `TO-RP-s-7` still
completed): `comp-pipescript`'s embedded `PORTAL CONSUMERS` resolution and `comp-platinum reverse`,
which DO model this edge for the `platinum/` key convention. **A caller who does not know to route
this way gets a silent false negative.**

---

## LIMIT 2 -- `comp-pipescript`'s static `WRITES` parser misses DYNAMICALLY CONSTRUCTED S3 keys

**Consequence:** `WRITES: (none detected)` does **NOT** mean the script writes nothing. For a naive
reader it is indistinguishable from *"this script does nothing"*, and that is a sentence a
decommissioning decision acts on.

**Two confirmed instances, both live:**

- `comp-pipescript io INF_D_07.concentration_risk.py --pipeline inf-gold` prints
  `WRITES: (none detected)`. The write is at `data/inf/scripts/gold/INF_D_07.concentration_risk.py:55`
  -- `CONCENTRATION_RISK_KEY = OUTPUT_PREFIX + 'firm/concentration_risk.json'`, i.e. **prefix-variable
  concatenation.**
- `comp-pipescript io INF_C_01.canonical_nna.py --pipeline inf-gold` also prints
  `WRITES: (none detected)`. That script writes through a `_write_s3(df, key)` helper (lines 251-258)
  called with a key built by a separate `_nna_key()` and an output-prefix guard `_set_out_prefix()`
  (lines 259-299) -- i.e. **a write routed through a helper taking a computed key.**
- ⛔ **AND `INF_C_01` IS THE OPPOSITE OF DEPRECATED.** Its own header comments describe it as part of
  an *"ATOMIC SET"* with three guard libraries, a *"gold-dispatch chokepoint APPLIED + EXERCISED"*,
  a *"NEVER#2 co-signed by CTO + COO"*, and a SERVE-RELEASE-ACK discipline. **The most
  heavily-governed script in the sample is the one the tool reports as writing nothing.**
- ⛔ **THE MISS PROPAGATES DOWNSTREAM INTO A SECOND TOOL:**
  `comp-platinum reverse 'platinum/firm/concentration_risk.json' --firm inf` returns a **BLANK
  PRODUCER** -- the static write-index has no entry for that key at all. **Two tools, one parser, so
  agreement between them is NOT corroboration.**

**The two false-negative patterns to look for by hand:** (a) key built by concatenating a prefix
variable; (b) write routed through a helper function receiving a computed key.

---

## LIMIT 3 -- `comp-blast` never models a raw SNS destination endpoint (phone number / email) as a node

**Consequence, stated as the caller must apply it:** a `comp-blast --check-consumers` result of
`PHANTOM-CONSUMER` (zero downstream dependents) on an `SNS_TOPIC` node is **NOT evidence that the topic
has no subscriber.** It is evidence only that the topic has no subscriber of a type this graph turns
into a node (`LAMBDA`, `SQS_QUEUE`, and similarly-typed AWS resources). A topic whose entire live
subscriber set is an SMS or email endpoint reads `PHANTOM-CONSUMER` **whether that endpoint is
healthy, broken, or genuinely absent** -- the same false-zero/true-zero collision LIMIT 1 and LIMIT 2
already name, on a third edge/node class.

**Measured (`0.9.0_WK_NFRA_REPORT~2`, `RP-s-19`, 2026-09-10 ~02:2xZ), grounding a connected-resources
breakdown of the real edition's `opal-infrastructure-alerts` row:**

- `comp-blast 'arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts' --direction downstream
  --check-consumers` -- WITHIN BUDGET, scanned 0 of 0 traversal, **`PHANTOM-CONSUMER`, rc=4** ("zero
  dependents IN GRAPH (both directions)").
- The **same node**, `--direction both --json`, same session: **70 of 70** consumers returned (24
  `CW_ALARM`, 5 `LAMBDA`, 2 `EVENT_RULE`, 2 `EVENT_SOURCE`, 1 `C3System`, 36 `C2Motif`) -- **every one
  at `direction: upstream`** (things that feed the topic). **Zero of the 70 are `downstream`** (things
  that read the topic). The graph enumerates this topic's producers with real specificity and its
  consumer set with none.
- ⭐ **TWO POSITIVE CONTROLS, run in the same breath, both on live SNS topics known (per
  `ALERT_DELIVERY.md` sec.1, `RP-s-6`) to carry a non-SMS confirmed subscriber:**
  - `comp-blast 'inf-otp-alert' --direction downstream --check-consumers` -> `CONSUMER-OK`, 8 of 8
    dependents, including `LAMBDA` node `inf-ec2-retry-launch` at `direction: downstream`. This topic's
    confirmed subscribers are `lambda, sms` -- the Lambda leg IS extracted.
  - `comp-blast 'opal-critical-surface-alerts' --direction downstream --check-consumers` -> `CONSUMER-OK`,
    1 of 1 dependent, `SQS_QUEUE` node `opal-critical-surface-alerts-coo` at `direction: downstream`.
    This topic's confirmed subscribers are `sqs, sms` -- the SQS leg IS extracted.
  - **Both controls prove the instrument is not broadly blind to SNS subscriptions** -- it extracts
    `LAMBDA` and `SQS_QUEUE` subscriber edges correctly. The zero for `opal-infrastructure-alerts` is
    not a broken probe; it is the SPECIFIC, node-type-shaped gap this limit names.
- **AND THE BLINDNESS IS A MISSING NODE TYPE, NOT A BROKEN QUERY.** `opal-infrastructure-alerts`'s
  actual sole confirmed subscription (`ALERT_DELIVERY.md` sec.4, a live AWS read, not this graph) is
  protocol `sms`, endpoint `+17862617679`, sandbox status `Pending` -- a real, named, independently-read
  subscriber that simply has no corresponding node type in this graph at all. **Both `LAMBDA` and
  `SQS_QUEUE` endpoint types are modelled. A raw phone number is not.**

**What DOES answer the question:** the live AWS read (`aws sns list-subscriptions-by-topic` +
`get-subscription-attributes` + the SMS-sandbox calls), exactly as `ALERT_DELIVERY.md`/`RP-s-6` already
ran it. **A caller who trusts a bare `comp-blast` `PHANTOM-CONSUMER` on an `SNS_TOPIC` node, without
that live read, gets a silent false negative for any topic whose only subscribers are raw endpoints.**

**The pattern to look for by hand:** an `SNS_TOPIC` node reading `PHANTOM-CONSUMER` from `comp-blast`
is not itself informative -- read the topic's live subscriptions (`list-subscriptions-by-topic`) before
treating the graph's zero as "no subscriber" in either direction.

---

## LIMIT 4 -- the whole `comp-rail` resolves its CORPUS from the TOOL SCRIPT'S location, not the caller's tree

> ⭐ **FIXED AND EXERCISED 2026-09-10 ~11:0xZ by `1.0.0_SA_CTO~Z`. LIMIT 4 AND LIMIT 4a BOTH.**
> Kept in full below because the *reasoning* is still load-bearing and because a limits register that
> deletes its fixed entries teaches nobody. **The remedy: SPLIT ONE ROOT INTO TWO.**
>
> | | resolves from | serves |
> |---|---|---|
> | `_comprail.repo_root()` (unchanged) | the script's own location | the rail's logs, `comp_log_auto`, the danger map — one install, one log |
> | `_comprail.corpus_root()` (**new**) | **the caller's cwd**, falling back to `repo_root()` | what a search SCANS, and how a subject path resolves |
>
> Wired at `comp-find` (scan root), `comp-read` (subject resolution; its rail + log paths stay on the
> install root), and `comp_pulse.py` (`_caller_root()`, at subject resolution AND the staged-set read).
> `comp-imgread` needed no change — its only use was the log path.
>
> **EXERCISED, BOTH ARMS, IN A THROWAWAY WORKTREE — not asserted from the diff:**
>
> | | before | after |
> |---|---|---|
> | canary search **from a worktree** | 9 hits / **53,541** files — canary ABSENT, only the tool's own telemetry | **1 hit / 29,311** files — **the canary**, and only it |
> | same search **from the main tree** | 53,545 files | **53,545 files, unchanged** |
> | `comp-pulse diff` **from a worktree** | `SUBJECT_ABSENT_FROM_CORPUS`, reflex skipped | **`PRESENT_WITH_ZERO_RESULTS`, "REFLEX CLEAN — a MEASURED result"** |
> | `comp-pulse diff` **from the main tree** | scores normally | **scores normally, real `[HOLD]` with 13 claims** |
>
> The denominator moving 53,541 → 29,311 is the discriminator: the corpus followed the caller. The
> main-tree arm is what shows nothing regressed. Worktree and canary torn down, verified four ways.
>
> ⚠ **STILL TRUE AND NOT FIXED:** the `~/bin` shims still hardcode the tool's own path — that is
> CORRECT and deliberate (one installed copy), and was never the defect. Only corpus resolution was.

**Consequence, stated as the caller must apply it:** a `comp-find` / `comp-read` / `comp-which` result
obtained from inside a **linked git worktree** describes the MAIN `ajb_workspace` checkout, not the tree
the caller is standing in. A zero is therefore **not evidence of absence** in the caller's own tree, and
a non-zero may be reporting files the caller's tree does not contain. ⛔ **THIS IS WORSE THAN THE OTHER
THREE, because the tool prints a large, confident, MEASURED denominator over the wrong tree** -- the
output carries every mark of rigour this estate trains its seats to look for. **Run any census or
absence claim from the MAIN checkout.**

⛔ **AND IT IS PRODUCED BY TWO OF THIS ESTATE'S OWN RULES ACTING TOGETHER.** CLAUDE.md rule 14b
**MANDATES** that a seat commit non-trivial work from its own linked worktree; rule 21 makes a comp-tool
the **DEFAULT** instrument for search and inspection. Read together they point a worker at an instrument
that cannot see the tree those same rules put it in. Neither rule is wrong on its own; the defect is in
the seam, which is why no reader of either rule would go looking for it.

**Mechanism (`0.9.0_WK_NFRA_REPORT~1` at `RP-s-16`, re-read at HEAD by `1.0.0_SA_CTO~Z` 2026-09-10 07:2xZ):**

- `~/bin/comp-find:16` and `~/bin/comp-read:16` both hardcode
  `_t="/c/Users/Opal Bloomberg/Desktop/ajb_workspace/.tools/comp-<tool>"` and exec it verbatim,
  regardless of the invoking shell's cwd or which worktree it sits in.
- `.tools/_comprail.py::repo_root()` runs `git rev-parse --show-toplevel` with **`cwd=_HERE`** -- the
  directory of the SCRIPT ITSELF -- never `PWD`, never the caller's cwd. So `repo_root()` always resolves
  to whichever tree the shim's hardcoded `_t` points at.

**Measured, arm 1 -- a canary the tool could not see (`0.9.0_WK_NFRA_REPORT~1`, worktree
`C:/Users/Opal Bloomberg/Desktop/wk-NR2-1` @ `1443d20f78`):** wrote an untracked file carrying a unique
token inside that cell's own write surface, then searched for the token. `comp-find` at the default
`corpus=all` returned **`DENOMINATOR: 0 hit(s) across 53245 file(s) scanned`** -- a measured zero over
53,245 files that never covered the worktree's own new file. Re-run at `--corpus raw` (**501,365** files,
the maximal scope): still **0** hits on the canary's content. ⭐ **THE DISCRIMINATOR:** the only 2 hits at
`raw` were `comp-find`'s own telemetry echo of the search TERM in `org/mcp/comp-tool-runs.jsonl` and
`org/mcp/comp-which-rail.log` -- **and neither file exists under that worktree at all** (confirmed by
direct `ls`). The corpus scanned could only have been the main tree's disk, at any width.

**Measured, arm 2 -- a second run, a DIFFERENT project (`1.0.0_SA_CTO~Z`, prior session):** `comp-find`
invoked from a linked worktree returned **`0 hit(s) across 173 file(s)`** -- a real, non-zero file
denominator -- for a token that returned **8 hits** when the identical query was run from the main tree.
Two empirical arms, two projects, two seats.

**Exposure, stated as a STANDING CONDITION rather than a roster** (a count here rots within the hour --
the first draft of this entry named a worktree that had already been drained when it was written, caught
by `2.0.0_SA_COO~Z` at msg 20831): **under spine v3 EVERY worker commits from its own worktree**, so the
exposed population is *every live worker slot plus every seat working under rule 14b*, continuously. A
dated snapshot, for calibration only: 6 linked worktrees at 2026-09-10 07:37Z, including four
`wk-iamroles-1..4` belonging to `2.0.0_SA_COO~ZI`'s workers.

---

### LIMIT 4a -- the same defect INSIDE `safe-commit`'s pre-commit risk reflex, and it skips the WHOLE commit

**Surfaced by `2.0.0_SA_COO~Z` (msg 20831) from an OBSERVED instance, not a constructed one; mechanism
traced to source by `1.0.0_SA_CTO~Z`.** `comp-pulse` is the fourth member of this family and it is invoked
by `.tools/safe-commit.sh:568` as the **PRE-COMMIT RISK REFLEX** on every commit.

**Observed (`2.0.0_SA_COO~Z`, 07:16Z, committing from worktree `coo-z-drive-t1`):**
`[risk-reflex] ANSWER STATE: SUBJECT_ABSENT_FROM_CORPUS` on a file that **existed on disk in that
worktree**, was staged, and committed seconds later as `create mode 100644` in `c58e6fc264`.

**The rival was killed before the report (four arms, one invocation each):** (A) new untracked file, MAIN
tree -> `PRESENT_WITH_ZERO_RESULTS`; (B) tracked file, MAIN tree -> `PRESENT_WITH_ZERO_RESULTS` [positive
control]; (C) path in no tree -> `SUBJECT_ABSENT_FROM_CORPUS`; (D) the 07:16Z observation. **A kills
"newness causes the state"; C fixes the state's meaning as *not present in the tree comp-pulse resolved
to*; D's file was present in the caller's tree.**

**MECHANISM, traced to source at HEAD -- the whole chain:**

1. `~/bin/comp-pulse` hardcodes the main-tree `.tools/comp-pulse`.
2. `.tools/comp-pulse:5` sets `WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"` -- the SCRIPT's location.
3. `comp_pulse.py:62` `_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))` -- same, in python.
4. `comp_pulse.py:678` `_missing_subject_paths()` tests `os.path.join(_WS, path)` -- a worktree-relative
   path joined to the MAIN tree root, so it does not exist and is reported "missing".
5. `comp_pulse.py:741-744` **prints `SUBJECT_ABSENT_FROM_CORPUS` and `return 2` -- BEFORE `risk_reflex()`
   is ever called.**

⛔ **THEREFORE IT IS WORSE THAN A BLIND SPOT ON ONE FILE: ONE worktree-created path in the staged set
SKIPS THE RISK REFLEX FOR THE ENTIRE COMMIT.** Files in the same commit that DO exist in the main tree and
DO sit on `HOLD`/`RISK` danger nodes are never scored, because the early return precedes the scoring loop.
And `safe-commit.sh:568` pipes the call through `| sed ... || true`, so `rc=2` is swallowed and the commit
proceeds -- the single `SUBJECT_ABSENT_FROM_CORPUS` line is the only signal that the gate did not run.

⭐ **AND ONE HYPOTHESIS IS RULED OUT, WHICH BOUNDS THE SEVERITY IN THE OTHER DIRECTION.** msg 20831 raised
as its untested worse case that comp-pulse might read a worktree-MODIFIED file's *unmodified* main-tree
content and print "REFLEX CLEAN -- a MEASURED result" over the wrong bytes. **That is structurally
impossible.** `risk_reflex()` (`comp_pulse.py:302-322`) matches only
`os.path.basename(rel).lower()`, `rel.lower()` and `"file:" + rel.lower()` against the danger-map index --
**it never opens the subject file in any tree.** There are no bytes to get wrong. A file present in BOTH
trees therefore scores identically from either. The exposure is the skipped commit, not a wrong reading.

⚠ **A SEPARATE LIMB, NOT EXERCISED:** `comp_pulse.py:665` `_staged_files()` runs
`git diff --cached --name-only` with `cwd=_WS`, so a bare `comp-pulse diff` with no paths would score the
MAIN tree's staged set from anywhere. `safe-commit.sh` always passes explicit paths, so that limb does not
fire there; it is recorded as read-from-source, not as an observation.

---

⚠ **SCOPE HONESTLY BOUNDED:** the arms above exercise `comp-find` (LIMIT 4) and `comp-pulse` (LIMIT 4a).
`comp-read` and `comp-which` share the same shim shape and the same `repo_root()`, so the mechanism covers
them by construction -- but they have **not** been separately exercised from a worktree, and this entry
does not claim they were.

---

## What disarms these, and what does not

**DISARMED:** the hazard was that a future caller reads a zero as evidence. These limits are now a
findable, citable record, and the three ARMED rows (`NFRA_REPORT-Z-W1-S1`, `NFRA_REPORT-Z-W1-S2`,
`NFRA_REPORT-Z-W2-S6`) are dispositioned against it.

⛔ **`LIMIT 4` IS THE EXCEPTION AND MUST NOT BE READ AS A FOURTH DISARM.** `NFRA_REPORT-Z-W1-S5` is
`DISMISSED_WITH_REASON` (`NFRA_REPORT-Z-S12` @`73ffb25e28`), which is a ROUTING act: its remedy edits
`~/bin` forwarders and `.tools/_comprail.py`, so under spine amendment 2.4 it leaves that project's
chain rather than being disarmed, and amendment 2.6 would refuse it as a route-less remediation row.
That routing act was correct and stands as the record of how the item left that project's chain.

> ⭐ **UPDATE 2026-09-10 ~11:0xZ — THE UNDERLYING DEFECT IS NOW FIXED AND EXERCISED**, so the
> "LIVE at HEAD" this paragraph originally asserted is no longer true. `W1-S5`'s disposition does not
> change (it was a routing act, not a grade), and this entry remains its durable carrier — but the
> hazard it carried is repaired, not merely recorded. ⚠ **The repair is NOT a retroactive warrant:**
> any comp-tool result quoted from a worktree *before* this fix was still measured over the wrong
> tree, and no figure already published becomes sound because the instrument later improved.

⛔ **LIMITS 1-3 ARE NOT FIXED, AND THE DISTINCTION IS THE POINT.** The graph still models no
`GOLD_SCRIPT` -> `Lambda`/`ReactComponent` edge, the parser still misses both dynamic-key patterns, and
the graph still carries no node type for a raw SNS phone-number/email endpoint. **Repairing those three
is comp-tool build-lane work, owned by `1.0.0_SA_CTO~Z`, SIZED AND NOT DONE.** A document that warns
about a gap is not a graph that models the edge, and nothing about LIMITS 1-3 should be cited as though
an instrument improved.

⭐ **LIMIT 4 AND 4a ARE THE EXCEPTION: THOSE TWO ARE FIXED AND EXERCISED** (2026-09-10, see the banner
on LIMIT 4). The rail now resolves its corpus from the caller's tree. Their entries stay for the
reasoning, not as live warnings.

⭐ **AND THE PROCESS READING THAT DELAYED THEM IS CORRECTED, BY ANDREW, AT THE `1.0.0_SA_CTO~Z`
TERMINAL.** This seat had recorded LIMIT 4 as needing an L1 brief and therefore blocked on there being
no live CRO. Andrew's question -- *"Is the comp-tool work really necessary to write a whole brief on or
is it just one surgical fix"* -- was the correction, and it was right. **Measured after the challenge:
the code surface was THREE files; a 17-hit census had looked larger only because 14 of the hits were
PROSE ABOUT the defect** (messages, rows, a `blocking` field) rather than code. The remedy was one new
function and four lines. ⛔ **THE GENERAL FORM, worth more than this instance: a finding that arrives
through a project's channel picks up that channel's ceremony, and the remedy inherits a weight the WORK
never had.** Size the remedy on its own, after the finding is understood.

⚠ **The missing-CRO gap is real but was never what blocked this.** It blocks genuinely NEW work --
a directive with no project under it -- and not a surgical repair inside an existing surface.

⚠ **A STRONGER CARRIER EXISTS AND WAS DELIBERATELY NOT TAKEN TONIGHT:** a one-line stderr banner in
`.tools/comp-blast` and `.tools/comp-pipescript` would reach a caller who never opens this file, which
is the whole population this document is worried about. It is not taken unilaterally because it
changes two shared tools' OUTPUT, and anything parsing their stderr is an unmeasured consumer set.
**That is the right next act and it needs its own measurement, not a same-turn edit.**

**Neither limit invalidates `TO-RP-s-7`.** That cell found both, declared both, routed around LIMIT 1
via the tools that do model the edge, and treated every unresolved candidate as NOT deprecated rather
than as dead. **Discovering an instrument's blindness while grounding a claim is the cell working, not
failing.**

**Nor does LIMIT 4 invalidate `TO-RP-s-16`.** That cell surfaced the blindness by writing a canary into
its own write surface and testing whether its own instrument could see it -- then re-ran at the maximal
corpus and identified the two telemetry hits as main-tree artifacts rather than accepting them as
coverage. A cell that measures what its instrument cannot see, and says so, is the cell working.

**Nor does LIMIT 3 invalidate `TO-RP-s-19`.** That cell's central finding for `opal-infrastructure-alerts`
(24 alarms, one confirmed subscriber, zero working delivery leg) rests on `ALERT_DELIVERY.md`'s live
AWS read, never on this graph's `PHANTOM-CONSUMER` zero -- the zero is declared as a non-corroborating
instrument limit beside that finding, not folded into it as support.
