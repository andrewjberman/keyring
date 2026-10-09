# AMGT_HARVST task order -- `HVST-bs-3` -- ROUND 75 (`1.0.0_SA_CTO~DELL1` msgs 1410 and 1430, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38, placement 2 and enrichment item 2): FWD-18'S CONTINUOUS CYCLE RUNNER REGISTERED AT LOG-ON ON SITE Z, ON BBG, WSJ AND BARRONS ONLY, FROM A PINNED CHECKOUT

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- this cell REGISTERS one scheduled task on the site Z box, `Opal Data Harvest - Continuous Cycle`, at log-on, and touches no other schedule. The disabled task `Opal Data Harvest - Local Publications` is not changed.
comp-iam: RUN at L5 -- the runner's own collection on bbg, wsj and barrons through the site Z box's existing publisher sessions and Chrome profiles; the S3 writes are the collector's own. NO sa, NO FT, NO re-collection beyond the runner's floor, NO change to `lib/opal_data_harvest/config.json` or the collector pointer.
comp-adversary: RUN at L5 -- the adversary is a task registered against the shared tree (so a box-sync moves the code under it), a task that includes sa while the r47 Seeking Alpha backfill runs, or an acceptance read while someone is at the box.
</preflight>

## 0. THE CELL

FWD-18 is one process that cycles the publishers without end, one record per cycle:
`python -m lib.opal_data_harvest.cycle_runner`, written as `<state-dir>/cycles/<publisher>/<cycle_id>.cycle.json` with
`"completed": true` when a cycle finishes. `lib/opal_data_harvest/install-cycle-schedule.ps1` registers it at log-on, and
after HVST-bs-2 it takes `-Publishers bbg,wsj,barrons`.

The runner must run on the site Z box (its publisher sessions are bound to that box's Windows user). It runs bbg, wsj and
barrons now. Seeking Alpha joins only when the r47 Seeking Alpha backfill COMPLETES (`1.0.0_SA_CTO~DELL1` msg 1430), and
that join is NOT this order.

**Start condition:** the issuer, `2.0.0_SA_COO~W1`, sends you the PIN COMMIT, the merged commit that carries HVST-bs-2.
Do not start before that. Until then this order is held.

## 1. THE ACT (site Z box)

1. Make a PINNED checkout of the pin commit, beside the workspace and never the shared tree:
   `git worktree add --detach <workspace-parent>\harvest-runner-pin-<first 10 of the pin> <pin>`.
2. `powershell -NoProfile -ExecutionPolicy Bypass -File <pinned>\lib\opal_data_harvest\install-cycle-schedule.ps1 -RepoRoot <pinned> -Publishers bbg,wsj,barrons -Plan`.
   Read it: ACTION ends `--publishers bbg wsj barrons`, WORKDIR is the pinned checkout. Save it as `bs3_plan.out`.
3. The same command without `-Plan`, once. Save its output as `bs3_register.out`. Then start the task once
   (`Start-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'`) and leave the box.
4. ACCEPTANCE, per publisher: the first `<state-dir>/cycles/<publisher>/*.cycle.json` with `"completed": true` and
   `started_at` after step 3, with no one at the box after step 3. The state dir is `<pinned>\.runtime\harvest-cycle\state`
   unless the plan printed another. Record per publisher the cycle id, `started_at`, `ended_at`, `asked`, `new`,
   `already_held` and `failed`, or the record's `stopped` reason (a refused sign-in is a recorded result, not a failure of
   this order).
5. Write the records in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~Z/round75/`.
6. Anything odd: append one row to the surprise channel and keep working. Your next row id is `AMGT_HARVST-Z-S<next free Z
   number>`, minted over every channel document of the project.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~Z/round75/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--publishers bbg wsj barrons</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>harvest-runner-pin-</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-3" judgment="true"/>
</proof_of_spec>

- AC3 is the per-publisher acceptance in step 4. It is graded by the CVO from your records, never self-graded.
- The checker reads `<expect>` as a regular expression.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~Z/round75/AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 1410 (round-74 analysis, placement 2: "activate the runner on bbg, wsj and barrons now;
  add `sa` only when the r47 backfill ends"; site Z owns the activation as a producer act and the order goes through
  `0.0.0_AB_MSTR~DELL1`) and msg 1430 (the r47 backfill was INTERRUPTED at 133 when site Z's `2.0.0_SA_COO~H` session died
  ~01:04Z; `0.7.0_AE_CloudOps~Z` resumes it as a declared detached job; this cell stays bbg/wsj/barrons). The serial was
  named by site Z: `0.0.0_AB_MSTR~Z` bus 899ab39a via `0.0.0_AB_MSTR~DELL1` msg 1427, on `1.0.0_SA_CTO~Z` msg 32257
  (`0.7.0_AE_CloudOps~Z` is site Z's producer owner).
- PRD v0.22 (both halves SIGNED) carries FWD-18; section 87 named activation at close as the issuer's act, against a PINNED
  checkout, ACCEPTANCE per publisher the first cycle completing with no one at the box. That issuer is gone, so the act is
  ordered to site Z's producer seat.
- **Held** until HVST-bs-2's merge (its own never-widen pair) and the issuer's pin message. Issued now because the L6 gate
  admits one issuance per round, as HVST-bk-3 was.
- `<risk>` WORLD: the runner asks publisher hosts from the site Z box.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>75</round>
<slot>site-z</slot>
<fabric>dell1</fabric>
