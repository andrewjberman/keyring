# laneC session close 2026-08-05T2049Z - 2026-08-06T0055Z -- Schwab decommission + Schwab Box re-tag + ASTN verification

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~C` (lane ~C; no lane agent-folder exists, filed in the base folder per
XXX.md two-families rule). Session instantiated by Andrew for the Schwab work, briefed via
`1.0.0_SA_CTO~B`.

## Window

Session start (registration 20:49Z) -> 00:55Z. **6 commits, ~20 MCP messages handled, 2 EC2 mutations
(1 unrecoverable), 2 deploy-completion ledgers opened+closed, 0 open deploys, 0 stranded legs.**

## What was delivered

| # | Commit | What |
|---|---|---|
| 1 | `772ff82f55` | **TERMINATE `canonical-schwab-runner`** (i-0ed92ce2e72f505dc) + its trigger rule + start-path IAM; S3 data preserved |
| 2 | `d87ff043ef` | Stage-2 rename **judgement: DON'T** (analysis only, nothing staged) |
| 3 | `8d4ca4f931` | **Schwab Box re-tag** `quartz-si2-spike` -> `canonical-schwab-si2`, `reversible=true` deleted |
| 4 | `46333c98a3` | `exempt_reason` warrant populated upstream in the TF-adoption census |
| 5 | `8dad740440` | ASTN: delete hardcoded `faithful_verified: True` + stale gate strings |
| 6 | `6de9869a5b` | ASTN: delete orphaned test, correct `ARCHITECTURE.md`, validate-BEFORE-persist |

Per-file detail: **see commit messages** (each carries its own evidence table).

## TASK A -- canonical-schwab-runner decommission

Andrew-direct retirement ruling (conditional on "does anything consume from it"), relayed by CTO~B;
condition met on **four axes, each with its denominator**:

1. **NEVER COMPLETED A RUN** -- `run-canonical.sh:30-36` `trap finish EXIT` ships a log on every exit
   path; `canonical/schwab/_runlogs/` held **0 objects**. Positive control: 484 objects elsewhere under
   the same prefix, so the empty read was a real absence and not a broken retrieval.
2. **NO REACHABLE START PATH** -- nothing emits `opal.canonical-xref/XrefRefreshSuccess` (9 matches /
   8 files / 22,354 scanned; all rule, docs, or census). Prior measurement: 0 invocations/30d vs
   33/33/17 for three sibling rules in the same call.
3. **1 of 208 IAM roles** grants `canonical/schwab/*` -- the box's own.
4. **0 of 196 Lambdas** consume it (token-walked; a single `list-functions` call returns a page).

**Two corrections to the brief, both established BEFORE acting, both CTO~B-accepted:**
- A rule **did** target the stopped box -- bound via `"InstanceId"` **inside the target Input payload**,
  not the target ARN. *"What targets this instance", asked at the ARN layer, is structurally blind to
  payload-bound targets.* (This also invalidated a `/draw` Andrew had ratified; CTO~B corrected it.)
- The brief's candidate S3 prefixes were **the wrong bucket entirely**. The runner writes
  `opal-data-bd/canonical/schwab/` and only READS `opal-data-schwab`.

**COMPUTE vs DATA:** terminated the box, preserved all 484 objects. `dryfit_driver.py:51` pins a fixed
historical date -- it needs the DATA to exist, not the PRODUCER to run.

## THE FINDING OF THE SESSION -- a targeted destroy ARMS A RESURRECTION

After 11 resources were destroyed and verified absent, the `.tf` files still **declared** them:

```
Plan: 11 to add, 0 to change, 0 to destroy.
  # aws_instance.canonical_runner will be created
```

**The next `terraform apply` by any agent, for any unrelated si2 change, would have recreated the
terminated production box -- with no ruling, no ledger, and nobody looking**, into an estate that had
already removed it from the manifest and from everyone's mental model.

> **`terraform destroy` removes INFRASTRUCTURE; only deleting the DECLARATION removes the INTENT.**

Closed by deleting `runner.tf` / `runner-iam.tf` / `runner-trigger.tf` (verified self-contained first).
Terminal assertion: **`No changes. Your infrastructure matches the configuration.`** CTO~B is carrying
this to base CTO as generalising -- every `-target` destroy in the estate has the same trap, and it is
invisible to the obvious check ("is it gone from AWS?").

**Sibling near-miss:** `apply -target` WITHOUT `-destroy` returned **`Apply complete!` at rc=0 having
destroyed nothing** (correctly -- apply reconciles toward the config; `-destroy` is a property of the
APPLY, not of the reviewed plan). Caught by reading `0 destroyed` against the expected `11`. *The
verdict string carries the word "complete" and the number that disproves it on the same line.*

## TASK B -- Schwab Box (sole live 49F ingest for ADVI 08335338 + MDPF 08242234)

**Stage 1 landed.** I **stopped mid-task** on a prior Andrew-direct naming law (2026-07-17,
`SCHWAB_BOX_ARCHETYPE.md:6`: *"Drop 'quartz' / 'SI2 spike' entirely"*) that conflicted with the edict.
Surfaced rather than adjudicated; Andrew re-ruled `canonical-schwab-si2` **with the conflict in view**.
Recorded as a **supersession, not an oversight**: *a sovereign ruling made WITHOUT sight of a
conflicting prior is an oversight to surface; one made WITH sight of it is a decision to execute.*

**Mechanism:** the box is **NOT TF-managed** (`EC2_MANIFEST managed_by`: *"Terraform (IAM only ... not
TF lifecycle-managed)"*). CTO~B's "Terraform only" non-negotiable had no applicable path; both CTO~B
and base CTO independently narrowed it to `aws ec2 create-tags`. Base CTO's framing is the better one
and is in the record: **importing to tag would bring the box under TF management as a SIDE EFFECT of a
labeling task -- an adoption decision nobody made.**

**Stage 2 judgement: DON'T.** The role name FAILS the "who is misled" bar -- but
`consolidated_gaps.json` gaps[67]/[69]/[86] list the instance, SG and key pair as `UNMANAGED` with
**`exempt_reason: ""`**, and an agent working the TF-adoption backlog does what the census asks.
**Renaming does not touch that** (the census keys on management status). Fixed at data-edit cost
instead -- **upstream in `slice_network.json`, because `consolidated_gaps.json` is GENERATED**
(`consolidate.py:46`); a hand-edit there would have been clobbered by the next run.

**Classification left as UNMANAGED deliberately:** `exempt_reason` records a LATER DECISION;
`classification` records a THEN-OBSERVATION. Populate one, leave the other, both stay true. GAP total
unchanged at 165 is the proof. (Adopted by CTO~B as doctrine.)

## ASTN_WSJFT.B verification (COO, verify-only)

- **C2 PASS.** 8 ledger entries; IAM grounded on live `get-role-policy` (not comp-iam, which models
  `(action)` not `(action,resource)` and fails GREEN on exactly the "anything broader" question). SES
  correctly conditioned to `*@opalinvest.dev`.
- **C3 SUPERSEDED, not failed** -- and this is the catch that mattered. The verbatim-substring
  criterion was reversed by Andrew **twice** (06-24 *"fuck direct quotes"*; 06-29 faithfulness 2nd-call
  removed). Testing it as written would have produced a FALSE FAIL and could have triggered a "fix"
  reversing two sovereign rulings. **COO explicitly credited the stop.**
- **The real defect:** `analyze.py:200` `"faithful_verified": True` was a hardcoded literal. **25 of 25
  served articles across 7 days assert it; it has never been false because it cannot be.** Worse than
  absent -- it affirmatively reassures the exact reader the TO points at it (CVO, AC4).
- **All three surfaces closed**, not one: the field, the orphaned `test_e2e_s3.py` (printed
  `verbatim gate: ALL PASS` while calling `analyze.normalize` -- which does not exist -- and reading
  `a["bullets"]` against a `facts` contract; 0 refs / 22,374 files), and `ARCHITECTURE.md`'s
  "gate proven ALL-PASS".
- **C4 FAIL** -- no CVO cert (0 matches / 1,115 files), and its subject no longer exists.
- **Empty-digest bug FIXED:** `put_digest` ran BEFORE the zero-check, so 2026-08-02 wrote a 0-article
  digest with `warnings: []` looking like a clean run. Check now precedes the write; **verified (not
  assumed) that `discard_raw` runs later**, so a fatal still leaves raw in S3 for diagnosis.
- **Provenance dated for a sovereign call:** `git log -S` puts BOTH the `GPT-4o default` doc line and
  `ASTN_AI_PROVIDER=openai` in ONE commit -- `78553824d5`, 2026-06-24, authored by `1.0.0_SA_CTO`, same
  day as the TO, titled *"verbatim gate PROVEN live"*. **The pipeline has never run on Claude; there is
  no divergence event.** Converts an unanswerable memory question into an answerable one. Provider
  UNCHANGED in both directions pending Andrew. Flagged that the evidence cuts AGAINST base CTO's stated
  Claude preference, strengthening their recusal.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `canonical/schwab`, `quartz-si2`, `XrefRefreshSuccess`, `faithful_verified`, `consolidated_gaps`, `slice_network`, `test_e2e_s3` | **PASS** | Printed its own denominator every time (477/181, 216/84, 9/8, 2/22372, 5/3, 0/0). The 0-match results were the load-bearing ones. |
| `comp-which` | "what consumes the canonical schwab silver and gold artifacts" | **PARTIAL** | Returned a 3-way near-tie and said so rather than guessing; I routed manually. Correct behavior, low steer. |
| `comp-iam` (census artifact) | `docs/briefs/cmpaws-iam-census-20260805.json` | **PASS** | 1 of 208 roles grants `canonical/schwab/*`. Used as a FLOOR, per Rule 22a. |
| live `get-role-policy` / `describe-instances` / `describe-rule` / `list-targets-by-rule` | applied-state verification | **PASS** | Rule 22a: comp-tools model DESIRED; every applied claim grounded on the primitive. |
| `.tools/commit-gate.sh` | analyze.py, run.py | **PASS** | Rule 14. |
| `.tools/safe-apply.sh` | targeted destroy | **PASS** | Rule 18; HALTGT clean. |
| `comp-surface-check` (via safe-commit) | 5 changed files | **PASS** | 0 critical surfaces touched. |
| `comp-pulse diff` (risk-reflex) | pre-commit | **WARN -> false positive** | See gap below. |

**What worked:** `comp-grep` printing denominators unprompted made every negative claim bounded rather
than asserted. The IAM census answered the consumer question at estate scale in one read.

**What failed:** nothing produced a wrong verdict I acted on. Two of MY OWN claims were wrong (below).

**GAPS FOUND (3, all routed):**
1. **`comp-pulse` risk-reflex keys its danger map on BASENAME, not path.** My `run.py` edit matched a
   **vendored OpenAI SDK file** and an unrelated test-runtime `run.py`, surfacing an irrelevant FT-block
   warning. It fired false HOLDs on base CTO's commits the same night. Attached to a pre-commit hook
   every agent hits -- *an instrument that fires on the wrong thing trains people to skim it.* Routed by
   base CTO to NFRA_NERVES.
2. **`safe-commit.sh:658-663` makes untracking a committed `.pyc` IMPOSSIBLE**, and its message asserts
   the false premise: `SKIP: pycache-artifact (never committed)` -- **1,464 are committed.** The guard is
   a correct AMENDMENT-1 belt against sweeping in a gate-created `.pyc`, but it is unconditional, so it
   also blocks the INVERSE (a deliberate deletion). Fix: scope the exclusion to untracked-or-new. Routed
   to CTO via COO. **I did NOT bare-`git commit` around it** -- bypassing a live gate for 10 files of
   regenerable build output, on my own read of my own justification, is not a trade to make unasked.
3. **`EC2_MANIFEST.json` has no retirement convention** (0 hits for retired/terminated). Removed the
   entry; declined to invent a `_retired` block -- a disposition axis on a shared schema is a Rule-24
   taxonomy act. Queued with CTO~B as a proposal.

## MY OWN ERRORS (corrected on the record, both same class)

1. Claimed `.tools/__pycache__` was in the untrack set -- **it is not tracked at all.** Asserted from the
   `.gitignore` line instead of `git ls-files`.
2. Claimed tracked `test_e2e_s3.pyc` / `test_verbatim_gate.pyc` were "bytecode outliving its source" --
   **those two were never tracked.** All 10 genuinely-tracked files have live sources.

**Both are the wrong-denominator class: I read the WORKING DIRECTORY and reported about the INDEX** --
in the same messages where I was naming that class in someone else's work. Action unaffected; claims
corrected to COO and CTO before they propagated.

Also: my first `--since` window for this log excluded 4 of my own 6 commits (local-time vs UTC). Caught
before it became the log's content.

## Blockers

**None.** One item PARKED with an owner: Class-B `.pyc` untracking, behind the `safe-commit` guard fix
(COO parked it, routed the fix to CTO). Not blocked on me and not urgent.

## Current State (zero-prior-context handoff)

- **`i-0ed92ce2e72f505dc` is TERMINATED** and its root volume `vol-0278d8c039b949534` returns
  `InvalidVolume.NotFound` (checked for orphaned EBS unprompted). `canonical-schwab-xref-success`,
  `canonical-schwab-automation-start-role`, `canonical-schwab-events-invoke-ssm-role`,
  `canonical-schwab-runner-role`+profile: all absent, positive-controlled.
  **`s3://opal-data-bd/canonical/schwab/` = 484 objects, PRESERVED.** TF workspace at 0-diff.
- **`i-0f3d57a97f14727af` = `canonical-schwab-si2`**, running, `reversible` tag GONE,
  `project=SCHWAB_SSOT.DERISK-1` retained. Both daily-pull rules ENABLED, selecting by
  `RunCommandTargets Key=InstanceIds` (NOT by name -- exercised before and after the re-tag).
  **Terraform manages this box's IAM ONLY; the IAM-layer names are untouched Stage-2 surface.**
- **ASTN:** `faithful_verified` gone; orphan test deleted; `ARCHITECTURE.md` states the real posture with
  both Andrew reversals dated+quoted; empty digests can no longer reach S3. **Provider still OpenAI,
  deliberately unchanged, pending Andrew.**
- `org/projects/DATA_SSOTMG.json` remains `status: active`; its S4 component is now terminated. **Stated
  explicitly in the ledger; status NOT flipped** (not mine, not CTO~B's).

## Next Steps

1. **[1.0.0_SA_CTO]** Andrew's ruling on ASTN provider (TO says Claude, build has always been OpenAI).
   Held at their seat.
2. **[1.0.0_SA_CTO]** `safe-commit` pycache-guard fix (gap 2) -- unblocks the whole `.pyc` hygiene class,
   including Class A's eventual disposition.
3. **[1.0.0_SA_CTO~B]** `EC2_MANIFEST` retirement-convention Rule-24 proposal; `gap_list` block has no
   `exempt_reason` field (declined to invent one).
4. **[2.0.0_SA_COO]** ASTN_WSJFT.B status correction (C3 superseded, C4 needs re-scope -- not closing as
   complete); Class-A Lambda-layer bytecode question to the layer owner.
5. **[NFRA_NERVES owner]** risk-reflex basename->path keying (gap 1).

## Ledgers

- `org/critical_paths/change_management/20260805T2215Z_canonical-schwab-runner_decommission_deploy_completion.md` -- **CLOSED**
- `org/critical_paths/change_management/20260805T2245Z_schwab-box-stage1-retag_deploy_completion.md` -- **CLOSED**

No open deploys. No stranded legs.
