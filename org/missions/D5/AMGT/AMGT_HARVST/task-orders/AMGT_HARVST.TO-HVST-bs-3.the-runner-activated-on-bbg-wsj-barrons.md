# AMGT_HARVST task order -- `HVST-bs-3` -- ROUND 75 (`1.0.0_SA_CTO~DELL1` msgs 1410 and 1430, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38, placement 2 and enrichment item 2): FWD-18'S CONTINUOUS CYCLE RUNNER REGISTERED AT LOG-ON ON SITE Z, ON BBG, WSJ AND BARRONS ONLY, FROM A PINNED CHECKOUT

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
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

**Start condition, MET (AMENDMENT 1):** the PIN COMMIT is **c1be67f53c**, the merge of HVST-bs-2, on origin `box/dell1`.
Both halves of this act's pair are signed. Start once your tree carries c1be67f53c (`git cat-file -t c1be67f53c` reads
`commit`).

## 1. THE ACT (site Z box)

1. Make a PINNED checkout of the pin commit, beside the workspace and never the shared tree:
   `git worktree add --detach <workspace-parent>\wk-harvest-runner-pin-c1be67f53c c1be67f53c`. The `wk-` prefix is required:
   site Z's reaper (`.tools/kill-maint.ps1`) exempts only a `wk-*` worktree or a declared detached job, and stops any
   other process outside a claude tree about 31 minutes after it starts.
2. `powershell -NoProfile -ExecutionPolicy Bypass -File <pinned>\lib\opal_data_harvest\install-cycle-schedule.ps1 -RepoRoot <pinned> -Publishers bbg,wsj,barrons -Plan`.
   Read it: ACTION ends `--publishers bbg wsj barrons`, WORKDIR is the pinned checkout. Save it as `bs3_plan.out`.
3. The same command without `-Plan`, once. Save its output as `bs3_register.out`. Then start the task once
   (`Start-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'`) and leave the box.
4. ACCEPTANCE, per publisher: the first `<state-dir>/cycles/<publisher>/*.cycle.json` with `"completed": true` and
   `started_at` after step 3, with no one at the box after step 3. The state dir is `<pinned>\.runtime\harvest-cycle\state`
   unless the plan printed another. Record per publisher the cycle id, `started_at`, `ended_at`, `asked`, `new`,
   `already_held` and `failed`, or the record's `stopped` reason (a refused sign-in is a recorded result, not a failure of
   this order).
5. Write the records in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round75/`.
6. Before you close: run `powershell -NoProfile -ExecutionPolicy Bypass -File .tools/kill-maint.ps1` (DRY-RUN by
   default; never pass `-Execute`). It must list the runner's python process as `EXEMPT`. Save it as `bs3_gc_dryrun.out`.
7. Anything odd: append one row to the surprise channel and keep working. Your next row id is `AMGT_HARVST-Z-S<next free Z
   number>`, minted over every channel document of the project.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them as written. If an act would, stop and report it first.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round75/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--publishers bbg wsj barrons</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-c1be67f53c</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-bs-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round75/bs3_gc_dryrun.out</invocation><expect>EXEMPT PID</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-3" judgment="true"/>
</proof_of_spec>

- AC3 is the per-publisher acceptance in step 4. It is graded by the CVO from your records, never self-graded.
- The checker reads `<expect>` as a regular expression.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round75/AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons.proof_of_spec.json`
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
- `- **AMENDMENT (2026-10-09 ~03:5xZ, issuer): re-addressed from `0.7.0_AE_CloudOps~Z` to site Z's AMGT_HARVST lane
  `0.7.0_AE_CloudOps~ZW`** (Codex seat), on Andrew-direct ~03:5xZ via `0.0.0_AB_MSTR~DELL1` msg 1590 ("dell1 runs its own deploys; only
  site-bound acts go to site Z, on the new per-project lanes"). The act is site-bound (that box's Windows user's sessions and
  tasks), so it stays at site Z. The deliverables path moves with the lane. This also clears row AMGT_HARVST-D1-S2's seating
  conflict: the lane holds AMGT_HARVST only.

<risk>` WORLD: the runner asks publisher hosts from the site Z box.
- **AMENDMENT 1 (2026-10-09 ~03:0xZ, issuer):** the pin is c1be67f53c (bs-2 merged, ledger closed @b19aa746cc). Pair:
  COO half `deliverables/2.0.0_SA_COO_W1/round75/NEVER_WIDEN_HALF_COO_BS3_RUNNER_ACTIVATION.md` @d0493b37a5; CTO half
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_BS3_RUNNER_ACTIVATION_20261009.md` @37aefc2855
  (`1.0.0_SA_CTO~Z`, via `0.0.0_AB_MSTR~DELL1` msg 1514), which adds C-e: the pinned worktree is named
  `wk-harvest-runner-pin-c1be67f53c` and a reaper dry run lists the runner EXEMPT before close. This amendment carries C-e
  into step 1, a new step 6, AC2's expect and a new AC4. bbg stays on `1.0.0_SA_CTO~DELL1`'s ruling (msg 1512):
  bloomberg.com web collection is not a Terminal draw.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>75</round>
<slot>site-z</slot>
<fabric>dell1</fabric>
