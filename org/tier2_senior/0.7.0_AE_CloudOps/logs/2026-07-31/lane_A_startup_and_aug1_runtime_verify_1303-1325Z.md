# ~A startup + Aug-1 ETFS chain re-verified AT THE RUNTIME LAYER; a 3-day-old miscitation on the fire's own record corrected

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE
**Serial:** `0.7.0_AE_CloudOps~A` (session 59c5ee8f, PID 33196, Monitor `b5guvgbz3`)
**Window:** 2026-07-31 ~1303Z -> ~1325Z (= 9:03 AM -> 9:25 AM ET)

## Startup

/watcher clean. Prefix RESOLVED to `/cygdrive/c` (measured, not assumed -- the hardcoded `/c/` form is
what killed two arms on the 07-25 respawn). No `inbox-watch.sh 0.7.0_AE_CloudOps~A stream` process
existed and the serial read NOT REGISTERED, so there was no orphan to reap and no PID ambiguity to
adjudicate -- the two exercised false-positives (dual-COO 07-14, MSTR self-reap 07-16) both need a
matching process to fire, and there wasn't one.

Monitor liveness was confirmed the only sound way: it **delivered both `[INBOX]` events to me**. That
observes a CONSUMER. I did not conclude "alive" from `ps` or from an empty inbox.

XXX.md 1b complete: LD-0290 serial file written; audit-archive-invoker ran (rc=1, 2 pre-existing
findings, snapshot correctly DEFERRED -- a lane is not GOVERNANCE_AUDIT-permitted); A.3 **94 of 94**
comp-tools resolve bare AND the mandatory exercise half passed (a forwarder produced its own banner --
resolution is not execution); owned-paths hook already wired; `.agent_context` set; **zero crons**
(CronList: none, correct for a Tier-2 lane). /cloud-ops loaded before any AWS call.

Inbox: 2 messages, both MSTR, both ACKed same turn (RAVC step 2).

## The regime I am under

Andrew-direct 0225Z, relayed by MSTR: **NFRA_VELOCITY is EXCLUSIVE**, not a priority. Everything
non-VELOCITY parks. MSTR carved out ONE exception by name: **the Aug-1 14:00Z ETFS month-end fire**,
because it is a partner-rebate basis. So my only live duty is that fire; I do not self-select VELOCITY
work from a backlog (P0-is-declared governs inside the program). TAP was already BLOCKED-SOVEREIGN on
Andrew's ~2046Z deferral, so exclusivity changed nothing for it.

## AUG-1 FIRE: VERIFIED READY (~24.7h out at time of verify)

Ground rule I held to: **a config read is not a behavioral claim.** Each leg verified at the layer that
can actually fail.

| Leg | How verified | Result |
|---|---|---|
| Orchestrator Lambda `etfs-reports-orchestrator` (TF-deployed) | **Downloaded the deployed zip, unzipped, grepped it** | md5 `8ffa0f7cccf35d6bab9a805be2605d78` == HEAD blob, 272 lines both sides. `_month_csv_keys` x2, `MIMEApplication` x3 PRESENT. LastModified 2026-07-29T03:09:32Z = 8 min after the applying commit |
| Renderer `render_month_end.py` (NOT TF-deployed; EC2 `aws s3 cp`s it at run time) | `head-object` on the artifact | ETag `d618e3b9931bde32c2d672363f8587ff` / Size 36767 / VersionId `chTZ82VfoorkM2F7oUOTcTNFyos6JUDu` -- identical to the predecessor's 07-30 pre-state on all three fields; == HEAD blob md5 |
| Trigger `etfs-reports-monthly-run` (EventBridge Scheduler) | `scheduler get-schedule` | State **ENABLED**, `cron(0 10 1 * ? *)`, TZ America/New_York, FlexibleTimeWindow **OFF**, target etfs-reports-orchestrator |

**The sharpest test, and why it is sharper than the obvious one:** the renderer's **VersionId is
UNCHANGED**. On a versioned bucket a re-upload mints a NEW VersionId *even for byte-identical content*.
So VersionId identity proves **no write occurred at all** -- strictly stronger than an md5 match, which
only proves the current bytes are right and is satisfied by a re-upload that destroyed the provenance.
That is exactly the provenance the step-2 NO-OP ruling exists to protect. Step 2 was not run and there
is nothing to run.

Aug 1 2026 is EDT, so 10:00 ET = **14:00Z exactly**, flex OFF, no jitter. Matches the recorded clock.

Positive controls run throughout: `_email_report` x4 in the deployed code; 710-line blob read on the
renderer (proving the retrieval returned a file, not an error message -- `git show` on a bad ref prints
to stderr and returns clean empty stdout).

## FINDING 1 -- the fire's own standing record cited the WRONG COMMIT for 3 days (corrected)

MEMORY.md read: *"CSV-attach patch LANDED+DEPLOYED @17bcbff520"*.

`@17bcbff520` is **DS~A landing a `.patch` FILE as a deliverable**. Its own commit message says so:
*"ready-to-apply diff for etfs-reports-orchestrator... Routed to AE lane: owned-paths gate correctly
blocked my direct infra commit... Apply must land before Aug 1 10:00 ET."* The **apply** is
**`@68661972ab`** (0.7.0_AE_CloudOps~A, 2026-07-28T23:01Z).

**The substance was right and the citation was wrong** -- it IS landed and deployed; I proved both this
session. But the failure mode is not cosmetic: a successor at hour ~24 who opens `@17bcbff520` to
confirm the deploy finds a patch file that that commit never applied, and the honest reading of that is
*"it never landed."* **That is a false alarm manufactured on a payment path at the worst hour** -- and a
false outage is not a safe error, it spends credibility and manufactures pressure to "fix" a chain that
is working. Corrected at source.

## FINDING 2 -- MEMORY.md is over its own cap, which drops the NEWEST entries first

Measured at session start: **17,811 bytes vs the 17,408 cap its own header declares = 403 OVER.** The
header records this exact failure happening on 07-31, where the 6 dropped lines were the 6 most recent
and included the live exclusive-regime directive. The current tail is the NFRA_VELOCITY GO, the VELOCITY
seam protocols, and the spawn-grounding lesson -- **the newest and most load-bearing lines are the ones
past the cap.**

I compacted **my own** line (the Aug-1 trigger) rather than touch another seat's standing record:
**17,621 = net -190 from where I found it**, overage 403 -> 213. **213 bytes still need to come out.**
Deleting other seats' entries is a coordinator's call, not mine, so it is flagged to MSTR, not fixed.
Caveat stated in the message: the file reported as modified on disk mid-edit, so another seat is editing
concurrently and my baseline may have moved.

## FINDING 3 (routed to CTO, not fixed) -- `/cloud-ops` SKILL.md instructs a BANNED action

The skill **every AE session loads** still says under Failure handling: *"Inbox watcher
AUTO-RESPAWN-INTERRUPT-LOST VERDICT: kill the listed PID + relaunch via Bash tool with
`run_in_background: true`."* That is precisely what XXX.md Step 1b C **bans**, for the stated reason:
the Bash tool notifies only on EXIT, stream mode never exits, so an agent that obeys it **goes silent
for the whole session** while every reachability probe still reads healthy.

My own `prompt.md` was corrected for this on 2026-07-10 and carries the fix explicitly. **The skill was
not.** Same class as the watcher-doc `/c/` prefix that bit two agents on the 07-25 respawn: the
correction landed on one copy and the other kept issuing the old instruction. *A retraction is only as
dead as its last-surviving copy.* Bounded severity (fires only on a watcher-failure path, and the result
is deafness rather than wrongness) -- routed to CTO to schedule, not fixed by me: it is a skill file, not
my lane, and we are under VELOCITY exclusivity. Same file also carries "portal-auth -- Portal Cognito"
against prompt.md's flat *"Opal does NOT use Cognito... never write Cognito in portal auth context."*

## Deployment Sequence + Verification (AE addition)

**NO DEPLOY THIS SESSION.** Zero Terraform, zero safe-apply, zero code deploy, zero tags, zero AWS
mutation. Every AWS call was read-only (`head-object`, `get-function`, `get-function-configuration`,
`scheduler get-schedule`) plus one authenticated GET of the Lambda code zip. One workspace commit (this
log). The staged step-2 script was **read, not executed**.

## Compiler Tools

| Tool | Why | Result | Note |
|---|---|---|---|
| `comp-which` (A.3 exercise) | XXX.md mandatory second half -- RUN one, score on OUTPUT | PASS | banner produced; 94/94 denominator printed |
| `comp-which "<ETFS renderer deployed / what fires it>"` | Rule 21 reflex before any raw call | ROUTED | -> `comp-trigger` (score 1.50 of 68 tools ranked) |
| `comp-trigger etfs` | what fires the month-end report | PASS | denominator printed: 142 events-rules + 12 schedules, us-east-1. Found `etfs-reports-monthly-run` ENABLED |
| `comp-glob` | locate orchestrator source | PASS | 2 files; also returned an explicit NO-MATCH-is-not-absence caveat on my second pattern |

**What worked:** comp-trigger named the scheduler and printed its denominator, which is what let me
state coverage rather than assert it. **Gap found:** `comp-trigger` renders `schedule: -` for
EventBridge **Scheduler** entries (it carries the expression for events-rules but not for schedules), so
it could not tell me the fire time, timezone, or flex mode -- the three things that decide whether the
Aug-1 clock is right. I went to `aws scheduler get-schedule` with a `# rail-checked:` marker. Worth
closing in the tool: a scheduler whose expression it cannot render is one it can only report the
existence of. **Raw-call justification:** all three aws inspections carried inline `# rail-checked:`
markers -- no comp-tool models deployed Lambda CODE CONTENT or a lambda-artifacts code object
(`comp-pipescript deployed` covers gold scripts under `opal-data-*/code/`, a different bucket and
prefix), and Rule 22a is explicit that a comp-tool cannot tell landed from planned.

## MCP traffic

4 messages. INBOUND: MSTR 022654Z (GO propagation + carve-out), MSTR 023001Z (VELOCITY GO exclusive) --
both ACKed same turn. OUTBOUND: 130607Z -> MSTR (ACK + my stated intent to re-ground the artifact before
the fire, offered for refusal if read as outside the carve-out); 132346Z -> MSTR (verify close + findings
1 and 2); 132403Z -> CTO (verify headline + finding 3 + the citation correction). All RAVC loops opened
this session are CLOSED in the outbound direction; nothing owed by me.

## Blockers

**None of mine.** The fire needs nothing before it fires. Two items are routed and are other people's
calls: the MEMORY.md 213-byte residual overage (MSTR) and the /cloud-ops skill drift (CTO). The $532K
orphaned INF gold-floor authorization remains PARKED under exclusivity with MSTR as carrier -- I did not
touch it, and its Aug-1 adjacency is INFERRED, not established.

## Current State (a successor starts HERE)

- **Aug-1 ETFS fire: VERIFIED READY at the runtime layer 07-31 1315Z.** All three legs above. **Do NOT
  re-verify by re-uploading anything** -- step 2 is a ruled NO-OP and a re-upload destroys the S3
  version-history provenance that proves the renderer untouched since 07-07, for zero gain.
- **If you re-check before the fire, the cheap sufficient test is the renderer's VersionId**
  (`chTZ82VfoorkM2F7oUOTcTNFyos6JUDu`). If it has changed, someone wrote to the artifact -- that is the
  finding, and md5 equality would NOT have revealed it.
- Post-fire: CloudWatch holds nothing useful; **only the EMAIL carries month + CSV count.** The 14:00 ET
  absence-guard (from `ed506fbd36`) is the pre-existing backstop.
- **TAP pilot: parked twice over** -- BLOCKED-SOVEREIGN on Andrew's word AND non-VELOCITY. Do not
  self-start. Read-first investment intact per the predecessor's log; have CTO re-verify map drift if
  days have passed.
- **Awaiting ESTATE VELOCITY tasking from MSTR.** Do not self-select from the 8 pending base-folder TOs.

## Next Steps

1. **[0.0.0_AB_MSTR]** ESTATE VELOCITY tasking for this seat; MEMORY.md 213-byte residual overage.
2. **[1.0.0_SA_CTO]** /cloud-ops SKILL.md banned-relaunch line + the Cognito line.
3. **[0.7.0_AE_CloudOps~A]** Hold the Aug-1 watch. Nothing to do before 14:00Z Aug 1 unless a signal
   arrives; the chain is verified and idle is the correct posture for it.
