# AMGT_CORPUS task order -- `CRPS-ap-5` -- ROUND 40: FWD-20 -- a zero-dominated row's unit reads in plain words

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check calls one function.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV ba391aff -- page_check ap5 build 1/3 control 3/3 (the fallback arm already holds).
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 40, continuing in the same worktree and on the same portal branch after `CRPS-ap-2`.

**Your portal.** The nested `portal/` repository in your worktree, on its own portal branch based on origin/DEV `ba391aff`. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink. `portal/node_modules` is a LINK to a tree that already holds the dependencies: NEVER run `bun install` (site rule: a registry fetch is egress). If `bun run typecheck` cannot run because the link is missing, say so in your report and go on; the issuer typechecks at the drain. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas and white panels; reuse the classes already in the file.

## 1. THE CELL -- `CRPS-ap-5`

On the Model tab a row's label carries its unit in brackets, from `rowUnitWords` (`portal/src/pages/SecurityAnalysis/tabs/
ModelTab.tsx`, about lines 160-182). A row the producer classes as zero-dominated is served with the unit text
`ZERO-DOMINATED: no magnitude: 10 of 10 fiscal years are zero`. `rowUnitWords` has no branch for it, so the catch-all lowercases
the served text and ASML's label reads "Minority (non-controlling) interest (zero-dominated: no magnitude: 10 of 10 fiscal years
are zero)". The sibling class is already worded by the page: `UNRESOLVED` reads "unit not resolved" (about line 165).

**Build, in `rowUnitWords` only (CTO ruling, msg 31013):**
1. One branch for a unit beginning `ZERO-DOMINATED`. Read the two counts from the served text ("<n> of <m>"). When n equals m the
   words are `zero in all <m> years`; when n is below m, `zero in <n> of <m> years`. `marked` is false.
2. A `ZERO-DOMINATED` text the branch cannot parse falls back to the served text, lowercased, as today: never a blank.
3. The served text is not changed anywhere, and no other branch moves.

## 2. BOUNDS

1. Change `rowUnitWords` only. No edit to `modelSheet.ts`, to any producer file, or to any `__harness__/` file.
2. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
3. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
4. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
5. Rows are `AMGT_CORPUS-Z-W4-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-ap-5.zero-dominated-in-plain-words.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-5.zero-dominated-in-plain-words.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md` and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs" ap5 portal</invocation><expect>(?m)^ap5 build 3/3 control 3/3$</expect></criterion>
</proof_of_spec>

- AC1 (the real `rowUnitWords`): build -- 10 of 10 reads "zero in all 10 years", 7 of 10 reads "zero in 7 of 10 years", an
  unparseable zero-dominated text falls back to the served text lowercased; control -- UNRESOLVED, PERCENT and RATIO read as
  before.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) if the link allows it, and `node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs`;
   report each one's last line. If a harness line that passed before your change now fails, fix your change, not the harness.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python
   .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change and why, AC1's output lines, the typecheck and harness lines, your portal and outer commit hashes, the
   portal branch name, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 3, settled as a PAGE cell by `1.0.0_SA_CTO~Z` msg 31013 (the served class token stays). Base portal origin/DEV `ba391aff`: ap5 build 1/3 control 3/3. Queued behind ap-2 on slot ~4. The reading is graded on ap-8's walk of ASML.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~4</slot>
<fabric>site-z</fabric>
