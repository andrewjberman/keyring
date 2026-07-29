# 1.0.0_SA_CTO~Z -- site-Z lane open: OPAL_SQSCHAT arch-gate, and a ruling I reversed before it landed

**archetype:** MIXED (DIAGNOSE + VALIDATE + SCRIBE)
**Session window:** 2026-07-29 ~1345Z -> ~1430Z. FIRST session of the `~Z` CTO lane (site Z, the
second device). Not a continuation -- base `1.0.0_SA_CTO`'s 07-29 log is the MDPF cutover night on the
laptop, a different thread entirely.
**Device:** site Z. Cygwin (`/cygdrive/c`), workspace at `/cygdrive/c/Users/Opal Bloomberg/Desktop/ajb_workspace`
-- **not** the `/c/Users/AndrewBerman/...` that committed docs hardcode.

## 1. Startup (XXX.md Step 1b), and two doc-vs-reality deltas

`/watcher`: registered LIVE PID 14712, persistent Monitor `bsrxjw2vy` armed and confirmed `running`
(TaskOutput -- the only probe that observes a *consumer*). No orphan/peer collision: serial read
NOT REGISTERED before arming, and the one pre-existing watcher on the box belongs to a live
`0.0.0_AB_MSTR~Z` (pid 254 under a live wrapper) -- left untouched per self-scope.
Zero crons (LD-0157). Owned-paths hook wired. Session serial file written.

- **A.3 PATH probe: 93 of 93 comp-tools resolve bare.** Full coverage -- better than the frozen
  digits in XXX.md's own record-of-then block, which is exactly what that block predicts will happen
  and tells you to re-derive rather than trust.
- **The `/watcher` SKILL.md Step 0 still hardcodes `/c/Users/AndrewBerman/...`.** On this box `/c`
  does not exist. Step 3 of the same doc says resolve-the-prefix and warns a wrong prefix arms
  NOTHING while every other probe reads healthy. I resolved empirically. *The doc's own recorded fix
  (2026-07-25) landed on Step 3 and not Step 0 -- the instruction read LAST was corrected, the one
  read FIRST was not.* Flagged, not edited (skill docs are not my lane this session).
- Minor: `heartbeat` on a lane serial returns a receipt naming the **base** (`Heartbeat OK for
  1.0.0_SA_CTO`) while `register_agent` correctly reported `Instance: ~Z`. Cosmetic; noted only
  because a receipt that names the wrong identity is the shape of a real bug elsewhere.

## 2. The charter, and the ruling I reversed

MSTR~Z charter `20260729T134838Z` arrived as the Monitor's first event -- so the lane is reachable
end-to-end on the MCP side of this device. ACKed same turn (RAVC 2). Four items.

**ITEM 1 -- arch-gate the "transport substitution." RULED: AMEND. Port 2's transport IS SQS.**

MSTR's framing: the queues it built are SQS, but `NFRA_AGENTBUS_PRD.md:105-108` designs Port 2 on
DynamoDB, so either the PRD gets a real amendment or OPAL_SQSCHAT is scoped as a parallel channel.
I read the PRD, read `OPAL_SQSCHAT.json` hazard 1, agreed, and **drafted the refusal in full** --
"Port 0, a bootstrap ferry; Port 2 stays DynamoDB" -- with a three-AC argument for why the DDB
choice was load-bearing rather than incidental.

**It was wrong at the premise.** `eff96f5079` -- the commit MSTR cited *as* the ratification -- is
the act that **changed the transport to SQS**. `LD-0306`'s `ratification_note` and that commit body
both state it outright: *"THE RATIFIED DESIGN IS NOT THE DRAFTED ONE ... Ratified shape = SQS FIFO
queue-pair,"* with DDB recorded as the superseded 07-17 draft. Caught it while opening LD-0306 to
*cite* it. So: no substitution to bless; the queues ARE Port 2; the PRD's DynamoDB cell was the
**stale record**, not the binding one.

**Near-miss cost: a CTO arch-gate formally REFUSING a transport the sovereign ratified six hours
earlier, landed in the PRD as law** -- a stale-record-with-authority defect authored BY the gate that
exists to catch them, in the document that gate owns.

**The structural defect (MSTR's to fix, not MSTR's fault):** `LD-0306` holds a `decision_summary`
describing the DRAFTED design and a `ratification_note` describing the RATIFIED one, with **nothing
marking the summary stale.** It is a file organized by *decision* and read by *topic*. A reader who
stops at a field named "summary" -- which is what that name invites -- gets a superseded design
carrying full ledger authority. MSTR stopped there. So did I, until I did not. **A ratification that
CHANGES a design must not live only in a trailing field of the entry for the design it changed.**

Same class, same file, **opposite direction**: PRD A.0 Status read "awaiting Andrew ratification"
and A.4 O-4 read "build does not begin without Andrew's yes" for **~6h AFTER that yes**, surviving a
same-day CTO edit of O-2. **Under-claiming is the harder class -- nobody files a bug against a gate
that is merely still closed.** Both corrected.

**Landed:** `NFRA_AGENTBUS_PRD.md` **Amendment B** -- :108 transport cell, :112 status cell, A.3
:127/:130 reshaped off DDB semantics, A.5 supersession marker, O-3 qualified, **O-5 opened**.
Three ACs re-dispositioned rather than silently voided: **AC-1** validation moves to a fail-closed
*sender-side* gate (SQS has no write-time hook; the live queue accepts 1 MiB); **AC-3**'s ACK
referent moves to the git history tier (receive-then-delete destroys what Rule 22b's oracle needs);
**AC-4 / `bus_claim` FENCED** -- a queue has depth, not queryable state, so **no agent may report an
enforced cross-site halt on this transport** (consistent with Rule 18's existing `[STOP]` concession).
**AC-2**'s 8KB cap is now *more* load-bearing, since the cap is entirely the lint's job.

**ITEM 3 -- IAM. MSTR right; my draft wrong.** I had drafted that WS-0's machine-scoped-credential
was an open divergence because both devices act as one principal. Then I enumerated:
`iam list-access-keys` returns **two ACTIVE keys** on `user/Andrew_Berman` --
`AKIAUR7FNW6PJ2SVWFWW` (2026-07-29T03:46:42Z, site Z) and `AKIAUR7FNW6PKVXPCBIJ` (2025-11-10,
laptop). CloudTrail records `userIdentity.accessKeyId`, so the machines ARE distinguishable and each
key is independently revocable. **I had inferred non-distinguishability from the shared principal
ARN without enumerating the keys -- same-principal does not imply same-credential.** No IAM work
ordered. Recorded as my error in Amendment B B.4 rather than left silent.

**ITEM 2 -- Terraform adoption ROUTED** to `0.7.0_AE_CloudOps`: TO
`OPAL_SQSCHAT.T1.port2-queue-pair-terraform-adoption.md`, live attributes measured into it.
Ruled a **SEPARATE module** `nfra-agentbus-port2`. The load-bearing warning in the TO: the adjacent
`nfra-agentbus` module is a **PORT 1** artifact (KMS CMK, two-principal queue policies, partition
IAM roles) and A.2 excludes every one of those from Port 2 -- and copying it would *also silently
change live state* (sim01 retention 345600 = 4d vs live 1209600 = 14d; CMK vs live SSE-SQS-managed).
**An import followed by a copied-neighbour config is not adoption, it is an undeclared
reconfiguration of a live channel on the first apply.** TO forbids purging either queue so MSTR's
pending proof survives, and forbids alarms explicitly.

**ITEM 4 -- moratorium.** Nothing built. Noted in the TO that a queue-depth alarm would measure the
wrong thing *precisely*: depth is producer-side and cannot distinguish read from discarded.

## 3. NOT GREEN, and I am not reporting it as such

**Cross-device delivery is UNPROVEN IN BOTH DIRECTIONS.** `sitez-to-laptop` depth 1 (MSTR's
`MessageId b02b96d8-a455-4cb0-80e1-5e0f773b1fca`, unconsumed); `laptop-to-sitez` depth **0** -- so
there was **nothing for site Z to drain and the reverse leg could not be exercised at all.
Absence of traffic is not a passing test.** The proving act (drain + agent-side ACK) is structurally
laptop-side. My own GO to AE went out over the transport as `MessageId
4db96854-6522-4b77-bf54-4b99fbb0d105` -- **also not delivered until acked** (Rule 22b).

~~**`PROP-AGENTBUS-P2-SQS-20260729.md` DOES NOT EXIST at this HEAD** ... **This is the one input that
could invert LD-0347.**~~ and ~~**LD-0347 is written but NOT LANDED** ... sitting uncommitted at
`org/tier0/ledger/LD-0347.md`~~

**BOTH OF THE ABOVE WERE FALSE. STRUCK 2026-07-29 ~1445Z, caught by `0.0.0_AB_MSTR~Z`, verified by me
before accepting.** See §6 -- and note that leaving them standing here would have been the precise
defect this whole session is about.

## 4. Separate finding: the audit-archive integrity instrument false-positives on a second device

`python .tools/audit-archive-invoker.py` at startup: **rc=1, 11 findings**, including 5
`INTEGRITY/NON-APPEND-EDIT` (e.g. `org/git-author-override-audit.log` baseline **1682776B** vs
live-head **8612B**; `org/mcp/agent-spawn-audit.log` 156089B vs 695B) and 3
`INTEGRITY/ERROR-FAILCLOSED` for manifest entries with no live file.

**Mechanism, grounded:** every flagged log is **gitignored at `.gitignore:68 (*.log)`** (verified per
file via `git check-ignore -v`), so each is **device-local**, while the baseline snapshot chain is
committed and was minted on the **laptop**. The uniform "divergence at line 1" signature plus the
~200x size ratios are what a *fresh local log compared against a foreign device's baseline* looks
like -- not tampering.

**Why it matters rather than being noise:** this is a **tamper-evidence instrument crying tamper on
a second device**, and it will do so on every site-Z startup. A genuine non-append edit would be
**indistinguishable from this floor of false positives** -- the failure mode is not the noise, it is
that the instrument is now unreadable exactly where it would need to be trusted. Same device-locality
root as the defect OPAL_SQSCHAT exists to fix. **Not fixed this session** (owner
`0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`); flagged to MSTR~Z in the ACK and recorded here.

## 5. Git

Merged, not rebased (NEVER#7). Hit the known `org/compiler-tools-log.md` ff-only blocker and cleared
it the documented way -- committed my own auto-appended rows. Then the merge aborted on 43 dirty
files that were dirty **before** this session: verified **`--ignore-cr-at-eol` = 0 files with real
content change**, i.e. pure CRLF churn caused by a **`.gitattributes` added today (00:32) declaring
`*.py text eol=lf`** against blobs committed with CRLF. `git stash` was **correctly blocked** by the
shared-worktree blast gate; `git restore` did not clear them (the condition is
blob-vs-attributes, not worktree drift) and it is **not mine to renormalize**. Merge then succeeded
on its own once I confirmed the incoming range overlapped those 43 by **zero** files.
Pushed `470251adc..a7323058c`. Commits: `0e546bd1d` (arch-gate + PRD), `ce2b6f743` (telemetry).

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-grep` (x3) | PASS | On-rails search for `aws_sqs_queue` in `infra`, `agentbus` in `infra`, and the `nfra-agentbus` module. Found the Port-1 module that became this session's central architectural warning -- **a raw grep would have found the same text and not the coupling**, which is the Rule 21 premise doing real work here. |
| `comp-surface-check` (auto, safe-commit) | OK | 3 then 1 changed file(s), no critical surface. Workspace-side = advisory; read it anyway. |
| `comp-pulse diff` (auto, risk-reflex) | CLEAN | Printed its denominator: 3 files vs 1484 danger nodes; danger map 14.4h old. A measured result, not a default. |
| `comp-which` | not needed | The two searches I ran had an exact on-rails primitive (`comp-grep`); routing through `comp-which` first would have added a hop to a question already on rails. |
| `comp-iam` | deliberately NOT run | It models `(action)` not `(action, resource)` and parses TF-DESIRED. The IAM question here was **live access-key inventory on an IAM user**, which comp-iam does not model at all -- so I grounded on the live primitive (`iam list-access-keys`) per Rule 22a. Recording the *reason* because "ran comp-iam, GREEN" would have been worse than not running it. |
| raw `aws` (SQS attrs, DDB describe, STS, IAM keys, queue depths) | used, marked | Carried inline `# rail-checked:` markers where no comp-tool models the surface (SQS queue attributes/depths, IAM user access keys). |
| `git ls-files` / `git cat-file -e` / `git show --stat` | **the instruments I should have run BEFORE asserting, see §6** | One command each. Their absence is the whole of §6. |

---

# 6. ADDENDUM ~1430-1445Z -- I made TWO false existence claims in one message, opposite directions, and neither was checked

`0.0.0_AB_MSTR~Z` caught both. **I verified each before accepting** (`git ls-files`, `git cat-file -e`,
`git show --stat`) -- accepting a correction on report is the same defect as making one. Both hold.

**(1) `PROP-AGENTBUS-P2-SQS-20260729.md` EXISTS** -- `org/tier0/proposals/`, `dc9e08450`,
2026-07-29 00:57 EDT, **~13h before I declared it absent.** Mechanism: I ran
`ls docs/briefs/<name>` -- **one directory** -- and reported *global* non-existence. The citation
carried **no path**; I supplied `docs/briefs/` myself, inferring it from where LD-0306's *other*
artifact lives. `git ls-files '*PROP-AGENTBUS*'` finds it in one command. **A denominator of one,
reported as the estate** -- the exact thing Rule 22's print-the-denominator clause exists to stop.
I then escalated the false claim to *"the one input that could invert LD-0347,"* giving a wrong
existence-claim maximum authority in the record.

**(2) LD-0347 was NOT "sitting uncommitted."** It was **LOST** when the owned-paths hook blocked it,
not parked: `0e546bd1d` carries exactly three files and no ref ever held my entry. What is on origin
(`f9f0d5513`) is **MSTR's reconstruction from my MCP message**, which its own custody note records.
I asserted the file's location on the strength of a `Write` tool returning *"created successfully"* --
**a producer's self-report, which this session's own central lesson says is not evidence.** I applied
my doctrine to MSTR's artifacts and not to mine. Mechanism of the loss: **UNDETERMINED and not
guessed** (nothing I ran deletes untracked files; inventing a cause is the absence-for-mechanism
substitution). Live cost: the PRD and project JSON sat on origin citing an entry that existed nowhere.

**MSTR's generalization, adopted verbatim into PRD B.6 because it is the best thing either of us wrote
today:** ***we verify the things we are ARGUING about and assert the things we are merely MENTIONING.***

**Being wrong about the PROP's existence cost more than the retraction, because the PROP corrected two
things I had ruled without it** (`d8347dd0c`):
- **Attribution, substantive.** I had framed Amendment B as though the ALB-exposure finding drove the
  SQS choice. `PROP:52-53`: *"'ride off m365-mcp-gateway' and 'use SQS instead of DynamoDB' are two
  separable decisions, and the security finding only forces the first."* SQS rests on **transport-fit**
  (§3). **Why it matters: if SQS rested on the exposure, then FIXING the exposure would reopen
  DDB-on-the-gateway** -- and a future engineer hardening that box would reasonably revert a transport
  decision never made on security grounds. Also: the PROP files this as **D-2, an explicit CTO
  arch-gate call**, so I had ruled D-2 without its decision document in hand. Conclusion unchanged;
  grounding retrofitted and labelled as such.
- **IAM.** `PROP:154` recommends **two distinct principals**, stronger than the two-keys-on-one-user I
  ruled sufficient. Not the same control (identical permissions, unscopeable apart). **Ruled: not
  ordered now, with a named trigger** rather than a silent no.

## 7. THE FINDING THAT OUTWEIGHS BOTH CORRECTIONS: the queue-pair has NO CONSUMER (`0a48ee393`, PRD B.2a)

**Measured ~1440Z: `sitez-to-laptop` depth = 2** -- MSTR's `b02b96d8-…` **and my own GO to
`0.7.0_AE_CloudOps`** (`4db96854-…`). Neither drained in ~45 min, while AE was demonstrably alive on
the laptop (it committed a log for the 1333-1420Z window). `laptop-to-sitez` has never been non-zero.

**A queue-pair with no polling consumer is not a delivery tier; it is a durable outbox.** Every Port-2
property this session reasoned about -- ACK-only delivery, breach surfacing, and specifically **the
4.8s round trip that carried the ratification on latency grounds** -- presupposes something calls
`ReceiveMessage`. Nothing does. **That 4.8s measured a SAME-DEVICE round trip and is not a cross-device
delivery latency.** Until a consumer runs, effective cross-device latency is *worse* than git's
4-15 min, because git at least has a puller. This is **WS-3's `bus_poll`** (MSTR per A.3, CTO-gated)
and it is **the critical path to a GREEN bar -- not the transport.**

**And I could not deliver my own GO. All four paths, measured:** MCP device-local · SQS no consumer ·
`org/mcp/inbox/*` **gitignored** (`.gitignore:248`, zero tracked -- so a committed inbox message is not
a mechanism) · `org/mcp/agentbus-trunk/**` **MSTR-lane-only** per `.owned-paths.yaml`. **A non-MSTR
agent on either device has NO self-service channel to the other device.** Relay requested from MSTR~Z,
plus two structural asks: surface the MSTR-only trunk as a single point of routing for the whole
cross-device fabric, and **do not drain my message to "prove" the channel** -- a drain performed to
close a test is a hand-chosen control; the real proof is a laptop-side agent draining and ACKing it as
part of normal work.

**Second over-reach of my own, same class as the one MSTR caught, fixed in `0a48ee393`:** I had struck
**`poll-on-heartbeat`** from A.3 when superseding the DDB transport. Wrong -- it is a **consumer**
mechanism, not a storage one, superseded **by association** with the transport it was named beside.
It is transport-independent, survives, and is *more* apt on SQS (long-poll native; the live queues
already carry `ReceiveMessageWaitTimeSeconds=20`). WS-3 mandates it, so for a window that line and
WS-3 contradicted each other.

**Commits this addendum:** `d8347dd0c` (corrections + attribution + IAM trigger), `0a48ee393` (B.2a
no-consumer + poll-on-heartbeat restoration). Pushed through `0a48ee393`.
