# AMGT_RESAPP -- HAND-OVER TO THE ~W LANES (2.0.0_SA_COO~W, 3.0.0_SA_CVO~W)

**From** `1.0.0_SA_CTO~W`, 2026-09-14 ~23:3xZ, on Andrew's word at this terminal (record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_232xZ_W_LANES_FOR_AMGT_RESAPP_CANONICAL_FLOW_AND_COMP_STATE_SPAWN_VIA_MSTRZ.md`).
**Instruments:** `/canonical-flow AMGT_RESAPP --report-only` and `comp-state --project AMGT_RESAPP`,
both run at HEAD `2fd0846492` on the SITEZ branch, 2026-09-14 23:0x-23:2xZ. Every figure below carries
its denominator or its vintage; a figure without one is a claim and is labelled as such.

This document is the whole context a fresh lane needs. Read it, then read the three artifacts it
names as the trigger, the slug and the decomposition. Nothing here is a task order and nothing here
is a GO: the COO cuts, the CVO grades, the CTO reads the slug. Andrew's original scoping word for the
COO lane, verbatim: *"i will spawn COO~W and they will take over operations and execute with their
subagents."*

---

## 1. SEATING

| limb | lane | state |
|---|---|---|
| L2 / L4 / L10 (CTO) | `1.0.0_SA_CTO~W` | this seat. `1.0.0_SA_CTO~Z` is LIVE (PID 6552 at 23:0xZ) and is the owner of record on every prior round; it holds POSN_ASTTAX and is informed by broadcast, not stood down by this seat. |
| L5 / L6 / L7 / the recut (COO) | `2.0.0_SA_COO~W` | to be provisioned by `0.0.0_AB_MSTR~Z`. Replaces `2.0.0_SA_COO~ZZZ`, NOT REGISTERED, closed down on Andrew's word at 15:19Z (msg 22817). One project per Tier-2 seat instance: this lane holds AMGT_RESAPP and nothing else. |
| L8 / L9 / the slug (CVO) | `3.0.0_SA_CVO~W` | to be provisioned. `3.0.0_SA_CVO~Z` is LIVE (PID 9404) but a fabric-wide STOP on that seat stands from `0.0.0_AB_MSTR~Z` (no respawn, re-attach, keystroke or peek; Andrew directs it himself). Nobody at these lanes touches `~Z`. |

Loops: **zero crons at launch, both lanes.** The `org/XXX.md` Step 1b-F row for the 10-minute
`/canonical-drive` over AMGT_RESAPP names `2.0.0_SA_COO~ZZZ`. A `~W` arm needs Andrew's word by
name; when he gives it, `1.0.0_SA_CTO~W` lands the row. Until then: event-driven, inbox Monitor only.

---

## 2. WHERE THE PROJECT IS (measured, not claimed)

```
home        org/missions/D5/AMGT/AMGT_RESAPP/          placement SITEZ (D5 row, Andrew-direct 2026-09-10)
brief       docs/briefs/amgt-resapp-security-analysis-20260910.md@19ce7d5b4d
PRD         prd/AMGT_RESAPP_PRD.md  v0.5 @cc7cb09e06   both L4-R halves SIGNED at current bytes -> ADMITTED
endpoint    15 outcomes FWD-1..FWD-15; 14 bars EXERCISED, FWD-9 APPLIED; 0 of 15 REALIZED
decomp      decompositions/AMGT_RESAPP_DECOMP.md  v1.0 (s.17 = round 9); last moved IN the round-9 issuance 7ee9d0d418
orders      47 of 47 terminal (44 complete + 3 superseded), 0 open; round-9 fanout 1 of 1 chains, cap 8
proofs      45 of 45 VALID at HEAD by .tools/proof-of-spec-check.py
branches    5 worker branches wk-amgt_resapp-{7-1,7-2,8-1,8-2,9-1}, ALL MERGED into HEAD
edits       0 dirty of 273 tracked under the tree; 0 stashes
channel     investigations/INVESTIGATION_v1.md: 152 rows, 0 open, 87 ARMED (comp-surprise, 23:14Z)
slug        surprise-channel/remediations/REMEDIATION_v9.md @1ae76e9c83  (3.0.0_SA_CVO~Z, 14:47Z)
answer      ledger/ROUND_ANALYSIS.round9.md @e9d1c6e6a5             (1.0.0_SA_CTO~Z, 15:10Z)
stamps      prd/stamps/ ladder L8/L9/L10 stops at r8; r9 stamps ABSENT (the CVO's act, skipped in the shutdown)
dep_stage   ROUND_CLOSE (claimed) -- AGREES with the measurement
MEASURED    L10 ANSWERED for round 9.   CLASS: ROUND-UNCUT.   NEXT ACT: the COO's round-10 issuance.
comp-state  flat org/projects/AMGT_RESAPP.json BEHIND (last touched 09-13 06:26Z; the L10 events postdate it) -- the
            CTO regenerates it from the tree in the same commit as this hand-over
```

**Round 9 in one line:** the single cell (`rh-1`, exercise the served route end to end) passed
5 of 6 criteria mechanically and the CVO graded the judgment criterion AC6 **FAIL**: the served
Lead Panel renders the SAME 205-byte HTML for a settled request ERROR and for successful EMPTY data,
so a user cannot tell a failure from "nothing today". The CTO's round-9 analysis ACCEPTS the FAIL,
finds the coverage subtraction EMPTY (15 declared, 0 unserved, run-time negative controls), rules
**NO PRD ADDENDUM**, and authorizes round 10 on the COO's recut: **ONE issuance covering every cell.**

---

## 3. ROUND 10 -- WHAT THE ANALYSIS NAMES, PLUS ONE MEASURED FACT

The analysis (s.6) names two rows as the substance:

| row | where | what |
|---|---|---|
| `AMGT_RESAPP-Z-C-S169` | adjudications/ADJUDICATION_v9.md (CVO, ARMED, disarm_owner the COO) | at portal `a845a8be` LeadPanel passes `isLoading` but no `error` to RankedList, so a failed ranked read renders as "the daily job wrote no row". Split the error boundary from empty data. |
| `AMGT_RESAPP-Z-S72` | investigations/INVESTIGATION_v1.md (COO~ZZZ, ARMED) | the assembled route renders in a real browser and renders EMPTY, 25,476 bytes byte-identical on two runs. Exercise it with traceable real input, recording response state, populated output, navigation and marking. |

**The slug says the empty page's "claimed daily-job cause was not measured." `1.0.0_SA_CTO~W`
measured it on the live plane at 23:1x-23:2xZ:**

```
producer   Lambda amgt-resapp-chatter-axis   State Active, LastModified 2026-09-11T18:13:38Z, python3.12
schedule   EventBridge Scheduler amgt-resapp-chatter-axis-daily   ENABLED
runs       log streams dated 2026/09/11, /12, /13, /14 (4 of 4 newest); today's last event 10:03:07Z
today      3 of 3 invocations in the 09-14 stream END IN
           [ERROR] ResourceNotFoundException ... Query ... Requested resource not found
           at /var/task/lib/research/metrics/chatter_axis.py:153 default_article_count -> client.query
read side  the IAM grant in infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf (Sid ReadArticlesTickerDateIndex)
           names table opal-amgt-articles -- DELETED in the 09-11 harvest rename; the live table is opal-harvest-articles
write side the same file grants WriteSecurityMetrics on aws_dynamodb_table.security_metrics.arn, a resource declared
           ZERO times in the estate (open row C-S49, round 5, owner 4.0.0_SA_CRO~Z) -- the module cannot plan as-is
table      opal-harvest-security-metrics (hash axis_date, range ticker): 52 rows, 52 scanned, 3 distinct axis_date:
           CHATTER#2026-09-11 = 10, PRICE#2026-09-10 = 32, TRENDING_CHATTER#2026-09-12 = 10; 0 rows for 09-13 or 09-14
LIMIT      only the 09-14 log stream was opened; the 09-12 and 09-13 streams were listed, not read. The zero rows
           after 09-12 are consistent with the same failure on those days and are not proof of it.
```

**Consequence for the cut (the CTO's REC, the COO's call):** `Z-S72`'s exercise cannot show a
populated page until the producer is repointed at the harvest tables and its IAM reconciled. That is
an EXISTING-cell recut of `AMGT-rd-5` (the chatter axis writer), which the COO owns; the C-S49 row
itself stays at the CRO lane as the harvest migration's unfinished consolidation, and the recut cites
it rather than re-filing it. So round 10 is three cells, not two: the error/empty boundary
(`Z-C-S169`), the producer repoint (`rd-5` recut, code + IAM + re-zip via `lambda_src/build_zip.py` +
`safe-apply` of the amgt-resapp root with its deploy-completion entry), and the exercise (`Z-S72`),
with the exercise dependent on the other two. A QA ad-hoc invocation of the repointed producer is
PERMITTED (ad-hoc runs for QA); the scheduled fire stays the acceptance. The measurement is filed as
row `AMGT_RESAPP-Z-S88` on the investigation channel so the cut can cite it.

**Bounds carried forward verbatim from the slug and the analysis:** no new grant, no freeze
exception. **PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO** until Andrew names it. No push,
no gitlink move, no deployment of the portal, no worktree release of `refs/drains/rg-2-portal`.
LD-0521 holds: no round-11 issuance before the round-10 slug. `C-SERVER-SIDE-RANKING` and the
standing monitor/alarm moratorium bind the producer cell (a scheduled producer is required; a
monitor is forbidden). No cell may grade an EXERCISED outcome REALIZED on its own artifact.

---

## 4. WHERE THE FRONTEND IS, AND WHY A CENSUS OF THE PORTAL READS ZERO

```
shared portal checkout + workspace gitlink   e85f6eb84f   0 files under src/pages/SecurityAnalysis/
refs/drains/rg-2-portal (portal repo)        a845a8be     26 files under src/pages/SecurityAnalysis/  <- THE WHOLE PAGE
refs/drains/rg-1-portal                      83995ea9     (round-8 predecessor)
read-only view worktree                      C:/tmp/portal-resapp-view @a845a8be  (vite :5175; built for Andrew; still present)
```
Every portal-touching order pins `a845a8be75`. A worker's portal work happens on a branch cut from
that ref inside the worker's own worktree; the shared checkout and the gitlink DO NOT MOVE. The
drain contract for a portal-touching round is in the decomposition s.16d / s.17e (Z-S19, Z-S33,
Z-S34: two superproject branches, one gitlink, a plain safe-merge cannot drain a portal branch).

**Two facts from `1.0.0_SA_CTO~Z` (msg 22931, 23:38Z, answering the broadcast with an explicit CLEAR):**
- **Scope record alignment.** That seat's record of Andrew ~16:5xZ at its terminal
  (`ANDREW_DIRECT_20260914_165xZ_SITEZ_POSN_ASTTAX_ONLY_BREAKDOWN_BEFORE_WORKERS.md` @f529179076) reads
  "this device, this session: POSN_ASTTAX only, no other projects". His ~23:2xZ word at the `~W`
  terminal is LATER and his own, so AMGT_RESAPP work on this device under the `~W` lanes stands on it;
  nothing at `1.0.0_SA_CTO~Z` holds or narrows it, and its `/self-drive AMGT & POSN` is NOT armed this
  session, so there is no loop at that seat for a `~W` loop to collide with.
- **Portal sequencing the round-10 recut will meet.** `0.0.0_AB_MSTR~Z`'s portal cross-fabric plan v2
  (`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/PORTAL_REPO_CROSS_FABRIC_INTEGRATION_PLAN_20260914.md`
  @9e0c1080a0, calls C1-C4 open at Andrew) orders: laptop reconcile (IRPT vs d13) -> ONE integration
  merge off `origin/DEV` carrying site-Z AMGT (`refs/drains/rg-2-portal` @a845a8be, which contains
  DEV; the cross-fabric overlap measured as `src/App.tsx` only) -> POSN after its round 5. **Any AMGT
  round-10 portal cell lands on a ref that plan names**; the COO reads the plan before cutting a
  portal cell. Localhost login on this device needs `VITE_AUTH_API_URL` empty (the dev env has no auth
  line; the laptop's gitignored `.env.local` sets it) -- the POSN view on :5173 runs with it, and an
  AMGT view on another port needs the same.

---

## 5. RESIDUE THE COO INHERITS (report first, touch by the rules)

- **UNFINISHED-EDITS, 1 file, HAZARD.** `infra/aws/terraform/harvest/s3.tf` is MODIFIED and
  uncommitted in the shared tree since 2026-09-11T19:17:02Z (mtime), on NO ref: it renames the
  bucket `opal-data-research` -> `opal-data-harvest` (2 lines). A `safe-apply` of the harvest root
  with that edit present would DESTROY and recreate a versioned bucket holding this project's
  `derived/model_block/` output. Author unknown (the shared tree carries no author). Per
  `/canonical-flow`: the COO finishes or discards it, one commit, with the CVO validating; a touch no
  open order explains is a surprise row. CTO REC: discard the working-tree edit and land the
  rename, if Andrew still wants it, under the harvest migration's own cell (rows Z-S12, C-S49,
  owner `4.0.0_SA_CRO~Z`), never as a stray apply. `1.0.0_SA_CTO~W` did not touch it.
- **5 merged worker worktrees** at `C:/tmp/wk-amgt-{7-1,7-2,8-1,8-2,9-1}`, each dirty only with
  ` M portal` (the gitlink) and `?? .scratch/`. Prunable by the COO after its own read.
- **8 OPEN rows in REMEDIATION_v9** (17 rows: 9 closed, 8 open; owners 14 `~ZZZ`, 3 `~Z`). A
  disarm is a NEW citing row, so a successor lane carries a dead lane's rows by filing under its own
  serial; `Z-S67`'s disarm is the CTO's and `Z-S71` is CARRIED (analysis s.7).
- **Contention.** `2.0.0_SA_COO~Z` is LIVE and driving POSN_ASTTAX round 5 in the shared tree:
  142 commits on the branch between 15:00Z and 22:28Z, drains every few minutes. Rule 14b binds:
  every worker in its own linked worktree from the CURRENT branch (never the harness worktree
  option), the COO's own multi-file commits in a linked worktree merged back with `safe-merge.sh`,
  and the APPEND-ONLY channel files committed in the shared index (never isolated).

---

## 6. FOR `3.0.0_SA_CVO~W` SPECIFICALLY

- Engagement begins at L8 of round 10, not before; L8 reads worker rows only (investigations/),
  adjudicates into `adjudications/ADJUDICATION_v10.md`, the one slug into
  `remediations/REMEDIATION_v10.md`, to `1.0.0_SA_CTO~W` and to no one else.
- The ratified-text half of L4-R is SIGNED by `3.0.0_SA_CVO~Z` at the current bytes and needs no
  re-sign unless the PRD's ENDPOINT or CONTRACTS bytes change (a header-only bump re-opens nothing).
- The round-9 stamps `L8.r9` / `L9.r9` / `L10.r9` are ABSENT from `prd/stamps/`; the ladder is a
  known-lagging carrier (row Z-S44). Not a blocker; note it when stamping round 10.
- Round 9's evidence lives in the tier-1 home `org/tier1_exec/3.0.0_SA_CVO/deliverables/`
  (`AMGT_RESAPP_ROUND9_CVO_{AUDIT,VERIFY,RENDER,COMPILE}_20260914_Z.*`), committed at 1ae76e9c83.

---

## 7. THE RECEIVING CHECK, STATED HONESTLY

`.tools/receiving-check.py` on `ledger/ROUND_ANALYSIS.round9.md` returns **UNCHECKED** (no checker
exists for a round analysis on this device). Accepting the analysis as the round-10 trigger is
`1.0.0_SA_CTO~W`'s judgment, made after reading it in full: its coverage table re-derives with
`to-check.py`'s parser (47 of 47 terminal), its negative controls were established at run time, and
its s.6 recommendation is consistent with the slug it answers. The COO runs the same command on the
decomposition before cutting and states its own verdict the same way.
