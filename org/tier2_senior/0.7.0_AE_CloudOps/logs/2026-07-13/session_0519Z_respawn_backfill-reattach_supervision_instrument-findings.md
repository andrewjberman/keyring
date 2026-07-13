# Session 0519Z-0610Z -- post-reboot RESPAWN: 08335338 backfill RE-ATTACH (not restart), supervision armed, four wrong-instrument findings

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Serial:** 0.7.0_AE_CloudOps (base)
**Window:** 2026-07-13T05:19Z (respawn) -> 06:10Z. Prior log: `session_0250-0505Z_08335338-backfill_phantom-auth-halt-corroborate-execute.md`.
**Project:** OPAL_ASSETS P1/G3a -- Schwab 08335338 full backfill. Grant `AG-2026-07-13-01` (ACTIVE).
**Ledger:** `schwab-08335338-backfill-exec-held` -- L1/L2 CLOSED, **L3 OPEN + HELD/external**.

---

## Summary

Re-spawned after a partial fabric reboot into a **live, unowned** 6,932-file Schwab backfill. **The compute
was never stranded -- the SUPERVISION was.** Re-attached from disk (grant + manifest), restarted nothing,
armed real supervision, de-risked the remaining 4h, built + exercised the census that will close L3, and
closed my outstanding `comp-iam` gap -- which surfaced a sharper coverage gap in the tool itself.

**THE DOMINANT RISK THIS SESSION WAS THE RECOVERY, NOT THE FAILURE.** Two agents (CTO~B, and MSTR's own
spawn message) independently framed the job as STRANDED / "roll back and escalate." A re-launch would have
raced a duplicate 6,932-file pull into the same S3 prefix and corrupted the exact census the ledger waits
on. It did not happen: the on-disk manifest foreclosed "stranded" before I reached any rollback branch.

---

## Work done

### 1. RE-ATTACH (not restart) -- authorization + progress re-derived from DISK
- Grant `org/mcp/andrew_grants/AG-2026-07-13-01_schwab-08335338-full-backfill.md`: ACTIVE,
  `expiry: on-completion`, `executing_agents: ["0.7.0_AE_CloudOps"]`, scope `s3://opal-data-schwab/backfill/08335338/*`.
- **NO AskUserQuestion issued.** A headless re-prompt is the phantom-consent vector this same lane fired on
  earlier tonight. **The grant on disk IS the authorization** -- this respawn is the first live proof that
  MSTR's P-2 grant-ledger works: *authorization survived the session that held it.*
- Progress re-derived from `_manifest/progress.json` (advancing ts + climbing counters) -- NOT session memory.
- **Nothing launched, nothing re-enumerated, zero writes to the prefix from this session.**
- COO independently validated the not-restarted claim (RAVC-4): `enumerated` pinned 6932, `skipped` pinned
  233, `seen` strictly monotonic. A second writer would have reset those. **Single writer confirmed.**

### 2. SUPERVISION ARMED -- built so silence cannot read as success
Persistent Monitor, 60s, read-only (one manifest `s3 cp`/cycle; the producer never sees me).
Breaks on: `done:true` | `failed` off 0 | **manifest-ts STALL >10min** | 15-min heartbeat | S3 READERR.
**The STALL branch is the load-bearing one:** a detached `schtasks` job that dies (box reboot,
ExecutionTimeLimit, credential expiry) leaves a `progress.json` **byte-identical to a healthy one** -- only
the ts stops advancing. **Exercised on synthetic done/failed/stall BEFORE arming** (a filter that only greps
for success is silent through a crashloop).

### 3. DE-RISKED the remaining 4h (stopped waiting to DETECT a death; went and EXCLUDED them)
On-box via SSM, `i-0f3d57a97f14727af` / `quartz-si2-spike`:
- `schtasks /query /tn SchwabBackfill` -> **Status: Running**, Last Result **267009** = `SCHED_S_TASK_RUNNING`.
- **`ExecutionTimeLimit` PT18H from 03:56:47Z -> expires ~21:56Z vs ETA ~09:50Z: a 12-HOUR MARGIN.** The one
  death mode the STALL detector was built for is now *positively excluded*, not merely monitored.
- Box uptime 14d (launched 06-29), `running`. Credential expiry would surface as `fail>0`; `fail=0` sustained.

### 4. LEDGER L3 -- HELD/external, per COO ruling (did NOT close early, did NOT rewrite my own gate)
The 4.0h window (opened 03:20:46Z) would have gone RED ~07:20Z against a ~09:50Z ETA. **A false RED is not
noise** -- it is another agent reading "stranded" and acting on it. I surfaced it to COO rather than editing
my own window; COO ruled HELD/external (`deploy_ledger.py:72-76` `_qualifies_as_held`: both APPLY legs proven,
only the `verify` leg open -- exactly the designed case).
**Proof:** `check --red` -> `OK: no stranded/open deploys; 6 HELD-SOVEREIGN-GATED ... apply-proven, NOT half-landed`.

### 5. CENSUS built, COMMITTED, and EXERCISED -- `495c7af7d`
`infra/aws/ec2/canonical-schwab-si2/census-08335338.py`. Landed S3 objects vs `plan_manifest.json`
(6932 / 18 types), **PER TYPE**, rc=2 on any gap. NEVER#5: the producer's counters are a self-report, not the oracle.
- **Committed, not left in scratchpad:** *a ledger proof that cites a vanished temp file is not a citation.*
- **EXERCISED against live partial state first: reported 4,703 MISSING across 18 types, rc=2 INCOMPLETE.**
  A census that has only ever returned COMPLETE has never been tested on the half that matters.
- **Independent corroboration of single-writer:** landed objects measured off S3 (2,229) track the producer's
  self-reported `downloaded+skipped` (2,183, ~3min earlier) within the ~19/min drift. **Two instruments with
  no shared source agree.**

### 6. MECHANISM CORRECTION (mine, self-caught)
The downloader is **monthly-chunked ACROSS all 18 types**, not sequential by type -- every type is partially
landed (`acc` 139/505, `rld` 386/753, `tcfx` 3/182) and the log interleaves `rld, rty, upn, uln`. So
`current_type` in progress.json is **the last file written in a chunk, not a phase.** I earlier said it was
"walking the uln type": **wrong.** It matters -- **you cannot infer completion from which type is showing.**

---

## FINDINGS -- four instruments, each of which can ONLY return the alarming answer

| # | instrument | wrong because | can only ever say | who it bit |
|---|---|---|---|---|
| F-1 | `ps` for an EC2 job | wrong machine | "dead" | CTO~B -> "STRANDED" |
| F-2 | `aws s3 ls` timestamps | renders LOCAL time (EDT); fabric reasons in Z -> phantom 4h skew | "stale" | CTO~B -> "dead 4h" *while watching it write* |
| F-3 | `simulate-principal-policy` w/o `--context-entries` | EVALUATES `Condition`; unsatisfiable -> falls through | "denied" | me, prior session |
| F-4 | a ledger proof returning `NoSuchEntity` | mis-cited (policy name in a role slot) | "never applied" | me, this ledger |

**None is noisy. Each is confidently wrong in a FIXED direction, and that direction is always the alarming
one. A random instrument gets caught; a BIASED one gets BELIEVED** -- and every one of these alarms
recommends a *destructive* repair (re-launch the live pull / re-apply the IAM / widen the grant). The
backfill restart was one ACK away, twice.
**"It erred toward caution" is no defense when the alarm is what triggers the damage. An instrument that
cannot return the reassuring answer is not conservative -- it is broken.** Banked to memory:
`feedback_simulate_principal_policy_false_denies_conditioned_statements.md`.

### F-3 detail -- Rule 22a's MANDATED instrument has a systematic false-DENY, aimed at our own best practice
4-probe on the live role, all run:
```
(A) PutObject  opal-data-schwab/backfill/08335338/tcf/probe.zip     -> allowed       POSITIVE CONTROL PASSES
(B) ListBucket opal-data-schwab      (no --context-entries)         -> implicitDeny  THE FALSE DENY
(C) ListBucket opal-data-schwab      + s3:prefix=backfill/08335338/ -> allowed       THE FIX
(D) PutObject  opal-data-bd/backfill/probe.zip                      -> explicitDeny  NEGATIVE CONTROL (firm-sep holds)
```
`SchwabBackfillList` is `Condition: StringLike s3:prefix`. **Rule 22a mandates simulate and never mentions
`--context-entries`** -- so it systematically false-denies **every conditioned statement**, and
**prefix-conditioned ListBucket is exactly what NEVER-WIDEN discipline makes us write.** The tighter the
policy, the more reliably the mandated verifier reports it broken -- and the "obvious" repair (widen until
green) is precisely backwards. Rule 22a exists because `comp-iam` false-GREENs; **its replacement
false-REDs. We swapped a false-GREEN for a false-RED and do not yet have a true instrument.**
**(A) passes cleanly while (B) false-denies: a positive control that cannot exhibit the failure mode is not a control.**

### F-5 NEW -- `comp-iam resource-sweep` CANNOT SEE EC2 ROLES AT ALL
Ran `comp-iam` (the gap COO named -- now genuinely closed). Two corrections to the received wisdom:
- **Rule 22a's blanket "comp-iam models `(action)`, never `(action, resource)`" is now OVER-BROAD.**
  `comp-iam role` **does** print Resources *and* Conditions; and a `resource-sweep` subcommand now exists
  precisely to catch ACTION-held/RESOURCE-not. Its output is exemplary -- prints its DENOMINATOR (123 lambdas
  / 388 calls), and explicitly refuses to call UNRESOLVABLE (229) or wildcard roles a pass.
- **BUT ITS POPULATION IS *LAMBDAS*.** `quartz-si2-spike-role` -- the EC2 instance-profile role performing
  2,500+ live backfill writes right now -- **is not in the denominator at all.** It is neither flagged nor
  cleared; it is simply *not censused*. **The tool built to catch the action-vs-resource blind spot is itself
  blind to every EC2 role.** Filing to CTO/COO.
- Corroboration worth recording: comp-iam (DESIRED/TF) shows Stmts 9/10 = the backfill grant, resource-scoped,
  and Stmts 6/7/8 = `Deny s3:*` on bd/cot/inf -- **the firm-sep DenyPlanes, which is exactly why my live
  simulate probe (D) returned `explicitDeny`. DESIRED and LIVE agree.** NEVER#1 intact.

### F-6 -- `deploy_ledger.py` has NO AMEND: a mis-cited proof on a CLOSED leg cannot be corrected
CLI = `{open, close-leg, close, hold, check, list}`. **My own L1 carries a bad citation:** its proof reads
*"get-role-policy quartz-si2-backfill-08335338: ..."* but that is the **POLICY** name; the **role** is
`quartz-si2-spike-role`. **Re-verify that proof in good faith -> `NoSuchEntity` -> reads exactly like "the IAM
was never applied."** The deploy is sound; the citation is not.
**The ledger is our anti-strand instrument and its entire value is that a reader can RE-DERIVE a proof. A
proof that returns NoSuchEntity does not merely fail to reassure -- it MANUFACTURES the half-landed reading
the ledger exists to detect.** That is F-4, *inside the gate itself*.
**I did NOT hand-edit the ledger JSON.** Append-only is plausibly correct by design; you supersede an audit
record, you do not rewrite it. Proposed primitive to CTO/COO: not `amend` but **`correct`/`annotate`** -- an
APPENDED superseding record, visible in `check`, original left intact. Interim: **carry the L1 correction
forward in L3's close proof**, so the record self-heals on read rather than on rewrite.
(Second gap, complementing COO's own filing: the ledger has no way to express *"legitimately long-running."*)

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-iam role` | `comp-iam role quartz-si2-spike-role` | **PASS** | 11 stmts; backfill grant (9/10) resource-scoped + conditioned; DenyPlanes (6/7/8) on bd/cot/inf intact. **Closes the gap COO flagged.** Respected the sovereign hold (skipped bd source scan). |
| `comp-iam resource-sweep` | estate-wide | **PARTIAL -> F-5** | 0 GRANTED-ACTION/UNGRANTED-RESOURCE across 123 lambdas/388 calls -- but **the population is LAMBDAS; the EC2 role doing the live writes is not in the denominator.** Neither flagged nor cleared. |
| `.tools/commit-gate.sh` | census-08335338.py | **PASS** | py_compile + ds-precommit + ruff clean. |
| `.tools/safe-commit.sh` | `-F` (Rule: commit msg is an execution vector) | **PASS** | `495c7af7d`; surface-check OK (no critical surface). |
| `.tools/deploy_ledger.py` | `hold --gate-type external`; `check --red` | **PASS -> F-6** | L3 HELD not RED. Gap: no amend path. |
| raw `aws iam simulate-principal-policy` | 4 probes + pos/neg controls | **PASS -> F-3** | Rule 22a mandates this over comp-iam for a fresh `(action, resource)` question -- on-rail, not a raw-search bypass. |

**What worked:** `comp-iam role` is far better than Rule 22a's text credits -- it carries resources AND conditions,
and its DESIRED view *agreed with the live plane* on both the grant and the deny planes. `resource-sweep`'s
honesty about its own bounds (denominator printed; UNRESOLVABLE explicitly not-a-pass) is the standard other
tools should meet.
**What failed:** nothing blocked.
**Gap found:** **F-5** (resource-sweep is lambda-only; EC2 roles uncensused) and **F-6** (no ledger amend).

---

## Files Modified / Commits

| Commit | Files | Note |
|---|---|---|
| `495c7af7d` | `infra/aws/ec2/canonical-schwab-si2/census-08335338.py` | see commit message -- the LANDED-object census that closes L3; exercised on partial state first |

## MCP traffic (8 total; significant only)

- **IN** `[STOP]` COO 052017Z + `[STOP]` MSTR 052058Z (retracting his own spawn message's "roll back and
  escalate" clause) -- both: **RE-ATTACH, DO NOT RESTART**. **Both ACKed explicitly** (LD-0271: only an
  agent-side ACK establishes READ). Neither changed my course; the disk had already foreclosed "stranded."
- **IN** MSTR 052331Z -- the `s3 ls` local-time hazard (F-2). ACKed **with evidence, not a promise**: my
  detector reads progress.json's own Z ts, and its live control printed `age=27s`. **Had the skew been
  present it would have printed `age=14400s` and STALL-fired on cycle 1** -- the bug is one my own positive
  control could not have missed.
- **IN** COO 052518Z `[DRIVE]` -- RULING: hold L3 external; do not close early; do not let it false-RED.
- **OUT** RAVC2 to COO (hold landed + `check --red` proof + F-3 with all four probes + the Rule 22a amendment
  proposal); status to COO (de-risk + census exercised + F-6).

## Deployment Sequence + Verification (AE)

No infra deploy this session. Verifications performed, live-plane:
```
aws iam get-role-policy --role-name quartz-si2-spike-role --policy-name quartz-si2-backfill-08335338
  -> APPLIED: ListBucket (Condition StringLike s3:prefix=backfill/08335338/*) on arn:aws:s3:::opal-data-schwab
             PutObject on arn:aws:s3:::opal-data-schwab/backfill/08335338/*   [never-widen + firm-sep intact]
aws ssm send-command i-0f3d57a97f14727af -> schtasks SchwabBackfill: Status=Running, LastResult=267009
python .tools/deploy_ledger.py check --red -> OK: no stranded/open deploys; 6 HELD-SOVEREIGN-GATED
python census-08335338.py -> rc=2 INCOMPLETE, 4703 missing / 18 types  [correct mid-flight reading]
```
**Rule 22a three layers, all present on the backfill grant:** DESIRED = iam.tf @ `13bceed46` + `comp-iam role`;
APPLIED = `get-role-policy` (above); **EXERCISED = 2,500+ PutObjects landed, `failed=0`** (the sharpest test,
and the one that holds no matter what simulate says).

## Blockers

**None self-owned.** Two EXTERNAL gates, both correctly held, neither stranded:
1. **L3 close** gated on the EC2 job reaching `done:true` (~09:50Z). Ledger HELD/external, tracked, HELD-STALE
   is 4 DAYS out vs a 4.5h job -- it cannot rot behind the hold. Supervision armed.
2. **08335338 residue purge-or-keep -- HARD-BLOCKED ON ANDREW.** Absolute. Not decided, not touched, and the
   census's completion must not tempt anyone into "just cleaning up."

## Current State (zero prior context)

- **The backfill is ALIVE and HEALTHY on EC2 `i-0f3d57a97f14727af` (`quartz-si2-spike`), pid 3440**, as the
  detached `schtasks` job **SchwabBackfill** (`C:\schwab-sdd\`, launched by `run-admin-bg.ps1`,
  ExecutionTimeLimit PT18H from 03:56:47Z). **It needs NO agent to keep running.**
- Progress: **~2,750/6,932 seen, ~2,500 downloaded, 233 skipped, failed=0**, ~19 files/min, **ETA ~09:50Z**.
  Oracle = `s3://opal-data-schwab/backfill/08335338/_manifest/progress.json` (stamps Z). **A local `ps` is NOT
  an oracle for this job** -- `ps: none` is the EXPECTED reading for a healthy remote job (F-1).
- Writes land at `s3://opal-data-schwab/backfill/08335338/<type>/` across 18 types. Principal =
  `quartz-si2-spike-role`, policy `quartz-si2-backfill-08335338` (List+Put, 08335338 prefix ONLY).
- Ledger `schwab-08335338-backfill-exec-held`: **L1 CLOSED** (IAM, but see F-6 -- its proof string is
  mis-cited), **L2 CLOSED** (harness), **L3 OPEN + HELD/external**.
- Grant `AG-2026-07-13-01` ACTIVE, expiry on-completion. **The grant on disk IS the authorization -- a respawn
  needs NO fresh consent and must NOT issue an AskUserQuestion.**
- Census tool ready + proven: `infra/aws/ec2/canonical-schwab-si2/census-08335338.py` @ `495c7af7d`.

## Next Steps

- **[0.7.0_AE_CloudOps]** On `done:true`: `deploy_ledger.py hold --release` -> run the census against LANDED
  objects (NEVER#5, per-type) -> **if `failed`>0 or any gap, re-run the resumable download to fill it BEFORE
  closing** -> `close-leg L3` with the census as proof, **carrying the F-6 L1 correction forward in that proof**
  -> `close` the ledger -> safe-commit -> RAVC the per-type census to **[2.0.0_SA_COO]** + **[0.0.0_AB_MSTR]**.
- **[1.0.0_SA_CTO]** F-5: `comp-iam resource-sweep` is **lambda-only** -- EC2 instance-profile roles are
  uncensused (neither flagged nor cleared). F-6: `deploy_ledger.py` needs a **`correct`/`annotate`**
  (append-only supersede), not an `amend`.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** **Rule 22a amendment (F-3):** simulate verification MUST supply
  `--context-entries` for every condition key, **and the positive control must run against a CONDITIONED
  statement** -- an unconditioned control passes while the conditioned one silently false-denies.
- **[Andrew]** **08335338 residue: purge or keep.** Hard-blocked, hold absolute.
