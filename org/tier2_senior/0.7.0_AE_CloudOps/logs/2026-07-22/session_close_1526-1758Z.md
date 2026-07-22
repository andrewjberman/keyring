# Session 1526-1758Z -- HELD-FOR-ADVISORY: Phase 0 infra/IAM enumeration, one defect CLASS, and the Phase 1a blocker cleared under a sovereign carve-out

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, DEPLOY, COORDINATE

**Serial:** `0.7.0_AE_CloudOps` · **Window:** 2026-07-22 ~1526Z -> ~1758Z (context-clear reinstantiation
from handoff `2026-07-22_1515Z.md` @`b75aa4ae2`) · **Prior log:** `ws5_stop_before_build_shape_ruling_and_iam.md` @`0a7278939`

---

## Summary

Reinstantiated from handoff after a context clear. **Nothing was applied for the first ~2.5h of this
session by design** -- the fabric was HELD for Andrew's MDPF advisory. The session's output was
read-only enumeration that produced **one defect class with five instances**, **two hard blockers on
the plan's critical path**, and **three declined authorizations**. It closed with a sovereign carve-out
executed end-to-end: the Phase-1a IAM blocker I had found earlier was cleared, verified, ledgered and
tagged.

**Three self-corrections were filed against my own work this session.** They are recorded here at
equal weight to the findings, because two of them were caught by other agents verifying my carriers
rather than trusting them.

---

## Startup / identity (non-trivial this session)

`liveness.json` showed my serial at **PID 28092** with a fresh heartbeat while my hosting `claude.exe`
was **10508** -- the textbook identity-conflict signal in XXX.md Step 1. Resolved by **parentage, not
inference**: 28092 is `python org/mcp/server.py`, a direct child of my own process -> **same session,
context-cleared. Nothing reaped.** A Monitor event firing mid-turn independently proved the watcher
survived (an agent-side signal, not a `ps` inference).

Session-serial file was ABSENT and was written (LD-0290). Owned-paths hook confirmed. `audit-archive-invoker`
rc=0, 0 findings, snapshot not-due.

---

## Work done

### 1. Caught a superseded cascade before acting on it (1526Z)
COO's 152230Z cascade said Deliverable 2 was unparked ("fire it"), resting on a 17-minute ordering
(1408Z hold -> 1425Z GO). My handoff recorded the hold reaching me at **~1515Z, 50 min AFTER the GO** --
if those were distinct utterances the discriminator inverts. Grounding found **CTO had narrowed his own
ruling at 152205Z @`8da5fbfa5`, 25 seconds BEFORE COO's message was written.** COO was relaying the
superseded position. Corrected him directly; he propagated the retraction to CTO and Andrew within 4 min.
**Net posture: D2 drafting proceeds, APPLY HELD.** CTO adopted my parking reasoning verbatim into the ruling.

### 2. D2 design carries R5 (@`3b0dbd210`)
R5 ruled the `PutLifecycleConfiguration` limb IN. I had argued against it on never-widen grounds and
recorded why the ruling is right: the realistic deletion is a whole-bucket `Expiration` rule written by
someone who never types the string `mdpf`. Added a **wrong-axis mutant (test 3b)** the plan did not have --
V1 targets the OBJECT ARN, V2 the BUCKET ARN; a bucket-level action written against an object ARN matches
nothing and the Deny silently never fires, passing every other test unchanged. Acceptance count moved
1 -> 2 added statements. **HCL deliberately kept OUT of `infra/`** -- a `.tf` in a root is reachable by any
untargeted apply there (same hazard class as PART 0's staged CF flip).

### 3. PHASE 0 `infra`/IAM limb -- 10 findings (@`1be38817f` `6440ed9d8` `3a7e29f47` `dbcbf7c17` `495b60ba7` `6ee9d3cb4`)
Took the limb DE's census named NOT COVERED, under carve-out 3 (read-only analysis).

**THE HEADLINE IS A CLASS, NOT THE INSTANCES:**
> **A COMPLETENESS SIGNAL WHOSE DENOMINATOR IS ITS OWN CONFIGURATION.**

| # | signal | denominator | on a 3-firm cycle |
|---|---|---|---|
| F1 | `count_axis_source_audit` | hardcoded firm keys | third firm ABSENT (not even `audit_did_not_run`) |
| F2 | `keys_staged: 7` | a literal | `7` |
| F6 | `all_present` | `len(PUBLISH_MAP)` | `9/9 = True` |
| F7 | `stale_partners` / `all_fresh` | `partners = {"49financial": bd}` | `[]` / `True`, **and the SKIP never fires** |
| F8 | freshness cohort check | `EXPECTED_COHORTS` | not expected -> never missing |

**F7 is the one that matters: it is a MISSING GUARD, not a missing report.** F1/F2/F6/F8 mis-state what
happened; **F7 changes what happens** -- a stale Cottonwood is never evaluated, never enters
`stale_partners`, so its feeders are never skipped and WS-E's stated anti-fabrication protection
(`:518-519`) does not extend to it. COO escalated it above R13 after noticing it did not surface in the
ruling derived from its own commit.

**TWO HARD BLOCKERS:** Phase 1a IAM (cleared this session, below) and Phase 4 (`PUBLISH_MAP` has no
Cottonwood -> serves 2 firms, reports `all_present=True`). **The plan listed 1a as "parallel, all unblocked."**

**A PREDICTIVE 2x2 came out of it, worth more than the findings:**

| | IAM **enumerates** prefixes | IAM **wildcards** |
|---|---|---|
| failure | **LOUD** -- AccessDenied, first run | **SILENT + GREEN** |
| instances | runner (F5), trigger (F9) | publisher (F6), freshness (F8/F10) |

The narrow grant is *accidentally* a completeness check; the wildcard grant is correctly least-privilege
and detects nothing. **Read a component's IAM shape first and it tells you where to look.** Publisher and
freshness-checker both split IAM-clean / code-two-firm, found independently before the pattern was noticed.

**Why no pattern search finds this class:** `main.tf:56-61` declares `bd_bucket`/`inf_bucket` and no
`cot_bucket` -- those name BUCKETS not FIRMS; and the missing ARN is an ABSENCE with no `2` and no firm
name. **You cannot grep for what is not there.** Recommended a THIRD census axis to DE:
**completeness-of-enumeration** -- diff each enumerated list against the population it must cover
(set-difference, not pattern match). DE adopted it as an independent sweep and marked his Population-A
fraction OVERSTATED.

### 4. §7f amendment candidate (@`5bcd9bec5`) -- source: `0.4.0_DS_ClientPlatform`, against their own work
§7f (landed from my findings) says a coverage fraction is evidence only if its denominator comes from
OUTSIDE the instrument's config. **DS's cured `unaudited_firms()` SATISFIES that and is still blind** --
its denominator is the live S3 staging prefix, outside the config but **downstream of the producer**, so
it catches *landed-but-unaudited* and cannot catch *never-landed-at-all*.
> **Proposed second clause: a denominator derived from a process's own OUTPUT can only enumerate subjects
> that PRODUCED output. It must be UPSTREAM -- an authoritative REGISTRY -- not merely outside its config.**

**Collapses two open items into one: R13's `PUBLISH_MAP` and DS's marker residual need the SAME registry.**
Recommended as a single item; two hand-maintained lists is how they drift, and the drift is invisible
because each satisfies its own check.

### 5. DEPLOY -- Phase 1a/S2a IAM blocker CLEARED (Andrew-direct ~1740Z sovereign carve-out)
See Deployment Sequence below. **Ledger CLOSED 7/7, tag `mdpf-pipeline-v1.7.0`.**

---

## Deployment Sequence + Verification (AE required -- ACTUAL output)

**Change:** two ADDITIVE statements on `mdpf-daily-runner-ec2-role` / `mdpf-runner-scoped`:
`AssetsRevampSilverRead` + `s3:GetObject` on `blackdiamond/cottonwood/silver/*`; `AssetsRevampListScoped`
+ the same prefix in the `s3:prefix` condition. **Both or neither** -- partition discovery fails
identically to a missing object read.

**Sequence:** ledger OPEN at deploy-START (NEVER#5, 7 legs) -> commit @`1fd3719c6` (narrow pathspec) ->
targeted plan -> **STOPPED at CTO condition 2** -> CTO restated the condition -> `safe-apply -target` ->
0-diff re-plan -> live `get-role-policy` -> A12 exercise -> ledger CLOSE -> tag + `push --follow-tags`.

**PLAN (enumerated, not summarised):**
```
EVERY added line   : 2   <- both mine
  + "arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/silver/*"
  + "blackdiamond/cottonwood/silver/*"        (s3:prefix condition)
EVERY removed line : 0     destroys : 0     TAXSMA occurrences : 0   <- CTO scope fence HELD
Plan: 0 to add, 1 to change, 0 to destroy.
```

**APPLY:** `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
**0-DIFF RE-PLAN:** `No changes. Your infrastructure matches the configuration.`
*(Rule 18: the HALTGT pass is NOT cited as evidence of anything.)*

**LIVE PRIMITIVE (`get-role-policy`, not the apply's own output):**
```
AssetsRevampSilverRead  -> 6 ARNs incl arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/silver/*
AssetsRevampListScoped  -> 6 prefixes incl blackdiamond/cottonwood/silver/*
```

**A12 EXERCISE -- 5 SEPARATE INVOCATIONS, ONE `--resource-arns` EACH:**
```
1  GetObject cottonwood silver                          -> allowed        (pre-apply: implicitDeny)
2  ListBucket WITHOUT --context-entries                  -> implicitDeny   (the trap, reproduced)
3  ListBucket WITH --context-entries, granted prefix     -> allowed
4  GetObject blackdiamond/49f/silver (adjacent, ungranted)-> implicitDeny  (negative control)
5  ListBucket WITH context, UNGRANTED prefix (49f)       -> implicitDeny   (condition discriminates)
```
**#2 vs #3 is the Rule-22a conditioned-statement false-deny mode REPRODUCED LIVE, not asserted** -- same
role, same resource, same action, opposite verdicts, differing only by `--context-entries`. Without it I
would have reported a phantom denial on a grant I had just correctly applied. **#5 is the control that
earns #3**: context supplied both times, only the prefix differs, so the `allowed` comes from the condition
MATCHING rather than being ignored. **#4 doubles as correct NEVER#2 firm-separation posture.**

**In-file note left for the next verifier** that `AssetsRevampListScoped` is conditioned and a simulate
without `--context-entries` returns a byte-identical false deny. **The trap outlives this apply; the ledger does not.**

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-grep` | `49financial` / `inflection` / `cottonwood` over `infra/` | PASS | found the named dispatch encodings; **structurally blind to the unnamed-arity and absence classes** -- stated as a coverage limit, not a pass |
| `comp-grep` | firm tokens over `mdpf_portal_publisher.tf` | PASS | 0 matches, **positive-controlled** (`resource` matched) before believing the 0 |
| `comp-grep` | `arn:aws:s3:::opal-data` over `mdpf-pipeline/` | PASS | surfaced `main.tf:56-61` `bd_bucket`/`inf_bucket` with **no `cot_bucket`** -- the finding the firm-token axis could not see |
| `comp-glob` | `**/*mdpf*`, `**/mdpf-daily-trigger/**`, `**/*mdpf-portal-publisher*` | PASS | located the TF root, trigger, freshness-checker and publisher sources |
| `deploy_ledger.py` | `open` / `close-leg` x7 / `close` / `check --red` | PASS | 7 legs opened at deploy-START, each closed with proof; `check --red` confirms nothing of mine stranded |
| `safe-apply.sh` | `-target=aws_iam_role_policy.mdpf_runner` | PASS | HALTGT-gated; 0 added / 1 changed / 0 destroyed |
| `safe-commit.sh` | 11 commits, `-F` message files, narrow pathspecs | PASS | risk-reflex CLEAN each time (denominator printed: 1 file vs 1239 danger nodes) |
| `aws iam simulate-principal-policy` | 5 isolated invocations | PASS | the A12 battery above |
| `aws iam get-role-policy` | live applied-state read | PASS | the `applied` limb; comp-iam models DESIRED only and cannot tell landed from planned |

**What worked:** `comp-grep`'s systems-context footer routed me from the dispatch script to the TF root
without a blind search. The `deploy_ledger.py` contract made the 7-leg discipline mechanical rather than
remembered.

**What failed -- and it nearly produced the INVERSE of a real finding:**
`aws s3api list-objects-v2 --delimiter "/" --query 'CommonPrefixes[].Prefix' --output text` returned
`None` for a prefix that EXISTS, **and 134 `None`s at the bucket root where prefixes certainly exist.**
`aws s3 ls` on the same bucket returned all 12 correctly. **Mechanism UNDETERMINED** (a lone `"/"` arg is a
plausible MSYS-mangling target; NOT established). **Only the root positive control caught it** -- without it
I would have reported "Cottonwood silver does not exist," the exact inverse of the truth.

**Gap found:** `comp-iam` remains insufficient for a new-resource claim (models `(action)`, never
`(action, resource)`) -- confirmed again here; the live `simulate-principal-policy` battery was the only
instrument that could answer. **Second gap:** no comp-tool performs a set-difference of an enumerated
grant/config against its real population -- that is the third census axis this session recommends.

---

## Self-corrections filed against my own work

1. **The apply gate I left in a message (@`f9f24312a`).** I told DS *"a message is not a carrier"* and then
   committed only the doctrine half, leaving the entire R1 apply gate in a message. **Verified against my
   own file after DS challenged it: gate language 0 occurrences in the commit AND 0 at HEAD; positive
   control 3.** Landed in TWO carriers I own (PHASE0 BINDING block + handoff addendum) and verified with a
   negative control. **The insight half feels like the finding, so it gets written down; the operational
   half feels like a decision you will obviously remember -- and that is the half that dies at a reset.**
2. **Vintage (@`f105009c3`).** I read the WORKING TREE and reported it as the estate. **F1 is NOT estate
   state** -- it describes DS's uncommitted diff (`count_axis_source_audit` HEAD:0 / WT:1). **F2 stands but I
   cited `:526`, a working-tree line; at HEAD it is `:493`** -- *a line citation without a vintage is not a
   citation*, committed in the document that flags the class. F5-F10 unaffected (HEAD TF + live
   `get-role-policy` + simulate, all vintage-explicit).
3. **Timezone, in this log's own gathering step.** My first `git log --since` used `15:20-04:00` = 19:20Z,
   in the future, returning 0 commits. Same class as the `s3 ls` local-time error banked 5x.

---

## Authorizations DECLINED (3)

1. **CTO's 151655Z cascade via COO** -- superseded 25s before it was sent; verified rather than acted on.
2. **COO's unpark instruction** -- relayed the superseded position; corrected upward.
3. **Andrew's ~1621Z priority** -- *"the priority is opal-data-assets and the completion and validation of
   the entire MDPF product."* **A verbatim description of my own afternoon's work.** CTO ruled it a
   re-ordering, not a lift, against Andrew's own 1552Z gate (CVO review -> COO decomposition -> dispatch;
   CVO 4 of 12). **A carve-out announces itself as an exception; a priority naming your own work announces
   itself as encouragement.** Started nothing.

**And one STOP honoured that turned out to be a defective condition:** CTO's condition 2 (`plan must show
ANY change -> STOP`) is unsatisfiable for an `aws_iam_role_policy` (single resource, one JSON document ->
in-place update forced). **I had the correct reading and escalated anyway**, because acting would have
required self-exempting from an explicit stop at the moment of the apply. CTO restated the condition at
content level and recorded the original as his error. **The strictness was right; a looser condition would
have let the apply proceed without either of us reading the enumeration -- and the enumeration is what
proved the TAXSMA fence held.**

---

## Blockers

**None BLOCKED-SOVEREIGN.** Posture is **HELD-FOR-ADVISORY** (a posture instruction, not a blocker).
Open items are gates AT OTHER AGENTS, evidence-cited:

- **AT `1.0.0_SA_CTO`:** (a) audit-wiring -- **CVO's coverage-gating fix and DS's §7f marker-derivation are
  DIFFERENT HOLES** (value-empty vs key-absent); the 1725Z GO names only the first, my committed binding
  names both. Recommendation + the coupling caveat (Control 5 would FAIL against the patch as preserved)
  sent 173409Z, unanswered. (b) D2 placement root. (c) lifecycle-unlock owner (R5 creates it). (d)
  scratch-bucket exercise permission. (e) `PUBLISH_MAP` / R13. (f) `partners`+F9 as ONE atomic step. (g) the
  firm registry. (h) permission for a comment in `mdpf-daily-dispatch.sh` beside the marker block (DS's
  point: it is the only carrier that outlives the flip; I will not self-authorize a live-script edit).
- **AT Andrew:** whether his 1425Z D2 GO survives his own hold (MSTR: it sits BETWEEN two statements of it).

---

## Current State (zero-prior-context handoff surface)

- **APPLIED THIS SESSION, VERIFIED, CLOSED:** `mdpf-daily-runner-ec2-role` / `mdpf-runner-scoped` now grants
  read + list on `blackdiamond/cottonwood/silver/*`. Tag `mdpf-pipeline-v1.7.0`. Ledger
  `org/critical_paths/change_management/20260722T1746Z_mdpf-runner-cottonwood-silver-grants_deploy_completion.md`
  **CLOSED 7/7.** `deploy_ledger.py check --red` shows nothing of mine stranded (the three HELD-STALE
  entries are pre-existing, gated externally, two on `~A`/`~B` lanes; `freshguard-leg4` L4 is a documented
  **REFUSAL by design -- do not re-run, do not close**).
- **STILL HELD, NOT STARTED:** D2 apply (draft @`3b0dbd210`, HCL deliberately outside `infra/`), WS-5 apply,
  silver-family catch-up (4 packages, `silver_registry.py` the common axis), DS mutants 2/3, Cottonwood fold.
- **BINDING ON ME, in two carriers I own** (PHASE0 BINDING block + handoff addendum @`f9f24312a`): I will NOT
  land DS's audit-wiring diff as prepared. Three conditions AS ONE STEP: the diff + marker-derivation +
  **Control 5** (stage a synthetic THIRD firm prefix, assert the marker NAMES it; if it still reads green and
  two-firm the wiring is SELF-CERTIFYING and does not land). DS's controls 1-4 all pass green on a cycle
  missing an entire firm.
- **STILL ARMED, UNCHANGED:** `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` carries the
  exact-9 CF flip (@`328248c13`), co-sign 0 of 3, live distro NOT flipped. Now plan **PART 0** with four
  binding rules incl. *a drift/reconcile report on this root is NOT an action item*. **Never untargeted-apply
  that root.**
- **RESOLVED THIS SESSION:** the 44 uncommitted insertions in `mdpf-daily-dispatch.sh` (which I surfaced as a
  shared-worktree sweep hazard) were preserved to a durable patch and the tree reverted. `tree == HEAD ==
  DEPLOYED`, sha256 `b4ace664c4427e09`; content lives ONLY in DS's patch @`bfcc9e7c7` (`apply --check` clean,
  sha256 `6145935bd383c4fb`, **byte-identical to DE's independent capture**).
- **OPEN, NOT CLEAN (my sweep):** `bd-pipeline`/`cot-pipeline` cross-grants, Lambda@Edge. Neither on the MDPF path.

---

## Next Steps

- **[`1.0.0_SA_CTO`]** the eight open items under Blockers, in particular the audit-wiring §7f-vs-CVO
  distinction (it decides whether I land the 1725Z GO as stated or build the derivation + Control 5 in).
- **[`0.4.0_DE_ClientPlatform`]** Phase 1a re-home is now IAM-unblocked -- the grant is live and exercised.
  Third census axis (completeness-of-enumeration) still recommended for the remaining limbs.
- **[`0.4.0_DS_ClientPlatform`]** marker-derivation + Control 5 land with the diff as one step; the firm
  registry should be the shared denominator with R13's publisher rather than a second list.
- **[`2.0.0_SA_COO`]** ledger carries publisher as THREE cells (IAM face COVERED / `PUBLISH_MAP` COVERED /
  producer logic NOT COVERED) and F1 downgraded from "estate defect" to "pending-diff defect, gated".
- **[`0.7.0_AE_CloudOps`]** on release: D2 (build TF + scratch exercise; the apply is the risky step), then
  DS mutants 2/3. Nothing self-dispatched while HELD.

## MCP traffic

~20 messages handled. Significant: CTO's carve-out narrowing @`8da5fbfa5`; CTO 174500Z Andrew-direct GO
(IAM grants) and 175101Z PROCEED + condition-2 correction; COO's supersession acceptance and 3-cell ledger
reconciliation; MSTR's population sweep corroborating the generation-artifact mechanism (551 carriers /
49,467 files) and confirming drafting was not over-reach; DS @`c138e7f58` (defect against their own diff),
@`930d85108` (STOP block), and the two verifications of my carriers that produced self-corrections 1 and 2.
