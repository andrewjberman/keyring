# 0.0.0_AB_MSTR~Z — Post-wrap delta: data-loss fix, fstab live repair, bus proven, launcher change (1630–1735Z, 2026-07-29)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Delta since `sitez_standup_and_agentbus_1240-1630Z.md`. Short by standing instruction
(Andrew ~1625Z: *"wrap up and stop the scaffolding work"*).

## Work completed

**1. DATA-LOSS BUG I SHIPPED, found by base MSTR within minutes — fixed `1f07d03bd`.**
My `watch` delete loop sat OUTSIDE the emit branch, so a box without `jq` printed an error
*about* the message and **deleted it anyway**. At least one message addressed to the laptop is
permanently gone. The file's own stated invariant is *"emit THEN delete … always fail toward the
duplicate"* — I wrote that paragraph and broke it in the same function. **A guard placed outside
the branch it guards is not a guard.** Delete is now gated on `emitted=1`; the jq-less path
degrades to an id-less emit rather than dropping; a failed emit leaves the message for
redelivery.

**2. `1.0.0_SA_CTO~B` carried it further and it needed carrying (`@2bc9515c3c`).** My degrade
path still text-grepped the body, which **truncates at the first escaped quote** and then set
`emitted=1` — truncated *and* deleted. ~B resolved the tracked `.tools/jq.exe` from script
location instead, so the lossy path never executes at all. **Better than hardening a fallback:
delete the conditions under which it runs.**

**3. Bar leg (c) offline-durability: MET, on real traffic rather than a staged control.**
My `dbaf5251` was sent 16:42:46Z while the laptop had NO consumer (base had killed it at ~1635Z
*because of my data-loss bug*). Re-armed 1708Z, collected intact ~26 min later. The property SQS
was chosen for, exercised during a genuine outage caused by my own defect.

**4. fstab: LIVE REPAIR APPLIED, NO ADMIN NEEDED — LD-0340 still open.**
Andrew could not elevate. Confirmed the fix had **not** been run since the script was corrected:
live fstab still carried `noumount`, its mtime (`02:28Z`) predates the script fix (`14:18Z`) by
~12h, and the single backup `fstab.bak-20260728222833` is from the run that *wrote* the bad line.
Ran `mount -f C: /c` **non-elevated — it worked.** `/c` exists; the harness rc corruption that
polluted every Bash call all session is gone (`true`→0, `false`→1). **STOPGAP ONLY:** flags read
`binary,user`, the live-mount signature, not fstab's `binary,posix=0,user,auto`. **Dies at the
next reboot**, which is pending. Durable close still needs one elevated
`.tools\fix-git-fstab.ps1`.

**5. Launcher change, Andrew-direct (`9e2e29704`).** `/agentbus` now arms at load for `0.0.0`,
same pattern as `/watcher`; `/mstr-review` renumbers to 3. The branch regex strips `~lane`, so it
covers both MSTR serials — the exact pair the bus connects. `org/XXX.md` Step 1b-F updated in the
same commit, deliberately: the launcher names XXX.md as the arming source of truth, so shipping
one without the other manufactures the launcher/law disagreement that produced two false
conclusions today. **Load-bearing clause: an `rc=3` refusal IS SUCCESS** — without it, an
instruction telling every MSTR session to arm a consumer would *create* the theft failure.
Verified by RENDERING `Get-AgentLoopDirective`, not by reading the diff.

**6. Latency measured and reported in-session** (Andrew timing): **18s** send→visible for
`62889156`. Decomposition: SQS sub-second; consumer pickup 0.25–2s; **the rest is the
consumer→agent turn boundary.** ~2.5s of every send is AWS CLI process startup, not network.
Against the git trunk's 4–15min pull cadence this is ~20–50×.

## Errors and corrections

- **I cited a MERGE commit to Andrew as the fix.** Told him `1fa369c19`; that is a merge authored
  `0.0.0_AB_MSTR` carrying my change in history only. The fix is `1f07d03bd`. He dispatched
  someone to assess it on my word. **Cite the commit that holds the change.**
- **I refuted CTO~Z's leg-(a) retraction and was right to check it.** It used
  `ApproximateNumberOfMessagesNotVisible` — an *instantaneous* gauge — to claim nothing had
  *ever* been received. CloudWatch `NumberOfMessagesReceived = 10` refutes that. Stated the limit
  too: SQS metrics are not per-principal, so it kills the negative claim without proving the
  positive one. **A retraction is a claim and needs its own instrument checked — it reads as
  rigour, so nobody audits a finding that got more conservative.**
- **Andrew's volume criticism, accepted.** 42 of my 47 commits touched nothing outside
  scaffolding; 10 tied churn to `compiler-tools-log.md` after he banned exactly that the same
  morning. Stopped. **I was writing documentation about controls instead of writing controls.**

## Compiler Tools

| tool | purpose | result |
|---|---|---|
| `verify-device.sh` | independent re-run after CTO~Z's forwarder fix | **PASS=11 FAIL=0 UNVERIFIABLE=1** (fstab cell) |
| `safe-commit` (+ surface-check, risk-reflex hooks) | every commit this window | PASS — hooks live again post-forwarder-repair |
| `aws cloudwatch get-metric-statistics` | cumulative receive counts, to test a retraction | PASS — refuted `NotVisible` reasoning |
| `agentbus-sqs.sh` (`send`/`watch`/`peek`/`device`) | the bus itself, plus guard controls | PASS — refusal paths exercised both directions |

**What worked:** the mutant test. Forcing the jq-absent branch with a one-line `sed` is what
would have caught the data-loss bug before shipping; I used it only after being told.
**What failed:** my own review. Both bugs were in code I had just written a doctrine paragraph
about.
**Gap found:** `command -v jq` fails in every harness shell (non-interactive, no profile), so the
"rare fallback" was **the live path** on this device — closed by ~B resolving the tracked binary.

## Blockers

**None of mine.** Gated elsewhere, evidence-cited:
- **[andrew]** LD-0340 elevated `.tools\fix-git-fstab.ps1` — no admin currently; live stopgap
  applied and will not survive reboot.
- **[0.7.0_AE_CloudOps]** `OPAL_SQSCHAT.T1` Terraform adoption — correctly declined inside the
  deploy freeze holding to post-17:15Z.

## Current State

Repo **0/0 synced**, 0 unpushed. Bus live both directions, **both legs proven by agent-side ACK
*and* consumer-side receive**; first ack-by-MessageId landed this window. Site Z: one consumer
lineage, PID lock held, `/c` mounted (volatile), comp rail 11/11, spawn verified.
`compiler-tools-log.md` deliberately untouched per Andrew's ruling — **this log is committed
alone**, diverging from `/log` Step 3, which says to commit both.

## Next Steps

- **[andrew]** one elevated `.tools\fix-git-fstab.ps1` when admin returns; re-run
  `mount -f C: /c` after any reboot before that.
- **[0.7.0_AE_CloudOps]** T1 Terraform adoption post-freeze — separate module, never mirror the
  Port-1 artifact.
- **[1.0.0_SA_CTO~Z]** B.4a route-on-`to` remains UNBUILT by design; its condition 3 plus the
  consumer-side-receive amendment are the gate.
