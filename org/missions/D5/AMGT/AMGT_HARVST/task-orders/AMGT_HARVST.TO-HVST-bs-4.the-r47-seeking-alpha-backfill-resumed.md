# AMGT_HARVST task order -- `HVST-bs-4` -- ROUND 75 (`1.0.0_SA_CTO~DELL1` msg 1430; site Z `1.0.0_SA_CTO~Z` msg 32271 via `0.0.0_AB_MSTR~DELL1` msg 1436): THE R47 SEEKING ALPHA BACKFILL RESUMED FROM ITS OWN CHECKPOINT ON THE SITE Z BOX, AS A DECLARED DETACHED JOB, UNTIL IT COMPLETES ANDREW'S ORDER

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the job is a declared detached process, not a scheduled task.
comp-iam: RUN at L5 -- the collector's own Seeking Alpha collection through the site Z box's existing sa session and Chrome profile, with its own S3 writes, resumed from its own checkpoint. NO other publisher, NO FT, NO change to `lib/opal_data_harvest/config.json`, the collector pointer or the checkpoint's contents.
comp-adversary: RUN at L5 -- the adversary is a relaunch from an empty checkpoint (a re-collection), a second sa process beside a live one, an undeclared process the reaper kills again, or a completion claimed from a stopped leg.
</preflight>

## 0. THE CELL

Andrew ordered a Seeking Alpha backfill to depth 2026-01-01 (2026-10-06). It is leg `r47_sa`: its checkpoint is under
`.runtime/harvest-backfill/` (`r47_sa` checkpoint), its runtime root is `.runtime/opal-data-harvest-sa`, and its run outputs
are `.runtime/harvest-backfill/r47_<leg>_run<N>.out`, all in the site Z workspace. It ran inside site Z's
`2.0.0_SA_COO~H` session. When that session died at about 01:04Z on 2026-10-09, the leg stopped with 133 done, and it has
not been relaunched. Andrew's order still stands. Resume the leg, do not restart it.

## 1. THE ACT (site Z box)

1. Confirm no `backfill_driver` process is running for sa, with a positive control on the process list (list any python
   process first). Save it as `bs4_before.out`. If one is running, stop here and report it.
2. Read the leg's last launch: its full argv from the newest `r47_sa*_run<N>.out` or the launch record beside it. Save it as
   `bs4_last_argv.txt`. Resume with THE SAME argv against THE SAME checkpoint. Do not use `--clear-stop` unless the
   checkpoint's own stop reason says the stop was transport-class, and say which in your report.
3. Launch it as a DECLARED detached job, so the process reaper does not kill it:
   `bash .tools/detached-job.sh run harvst-r47-sa -- <the argv>`, with output to the next `r47_sa_run<N+1>.out`.
   Save the declaration's output as `bs4_declared.out`.
4. Read the first PLAN or progress line it prints. It must start from the checkpoint (done count 133 or more), never from 0.
   Save it as `bs4_resumed.out`.
5. Re-declare before the 48-hour marker lapses, for as long as it runs (`detached-job.sh declare`).
6. On COMPLETION (the driver's own PAIRS completion line, every pair of the leg done or recorded with a stop status):
   write `bs4_completed.out` with that line and the done count, and tell `0.0.0_AB_MSTR~DELL1`, naming this order. That
   report is what lets the cycle runner add sa.
7. Write everything in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/r47/`. Anything odd: append
   one row to the surprise channel and keep working. Your next row id is `AMGT_HARVST-Z-S<next free Z number>`.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them as written. If an act would, stop and report it first.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/r47/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box, from the workspace root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/r47/bs4_declared.out</invocation><expect>harvst-r47-sa</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/r47/bs4_completed.out</invocation><expect>PAIRS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-4" judgment="true"/>
</proof_of_spec>

- AC3 (graded by the CVO, never self-graded): the resumed leg started from its checkpoint (step 4) and the completion is a
  completion, not a stop.
- The checker reads `<expect>` as a regular expression.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/r47/AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 1430 ("the r47 backfill was INTERRUPTED, not completed -- resume it from checkpoint
  133"; `0.7.0_AE_CloudOps~Z` resumes it as a DECLARED detached job and reports completion; the runner adds sa on that
  report). Site Z `1.0.0_SA_CTO~Z` msg 32271 via `0.0.0_AB_MSTR~DELL1` msg 1436: no new seat on site Z, so the project's
  issuer orders `0.7.0_AE_CloudOps~Z` for its site-Z producer acts, and the r47 restart is ordered by `2.0.0_SA_COO~W1`.
- Issued as its own WORKSTREAM `R47` (write surface `deliverables/0.7.0_AE_CloudOps~ZW/r47/`, disjoint from round 75's
  `bs-1` to `bs-3`), because the ruling arrived 2 minutes after round 75's issuance @c7909af157 and the L6 gate admits
  one issuance per round per workstream. It is not an enrichment cell: it resumes Andrew's own 2026-10-06 order.
- This is NOT a re-collection (R22): it resumes Andrew's own 2026-10-06 order from its checkpoint.
- Dependency: the `bo-1`/`bp-1` merge pair's C-a reads "no backfill_driver process", so that merge waits on step 6.
  `bs-3` does not wait on it (it registers bbg, wsj and barrons only).
- `- **AMENDMENT (2026-10-09 ~03:5xZ, issuer): re-addressed from `0.7.0_AE_CloudOps~Z` to site Z's AMGT_HARVST lane
  `0.7.0_AE_CloudOps~ZW`** (Codex seat), on Andrew-direct ~03:5xZ via `0.0.0_AB_MSTR~DELL1` msg 1590 ("dell1 runs its own deploys; only
  site-bound acts go to site Z, on the new per-project lanes"). The act is site-bound (that box's Windows user's sessions and
  tasks), so it stays at site Z. The deliverables path moves with the lane. This also clears row AMGT_HARVST-D1-S2's seating
  conflict: the lane holds AMGT_HARVST only.

<risk>` WORLD: the collector asks Seeking Alpha from the site Z box.


<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>75</round>
<workstream>R47</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>
