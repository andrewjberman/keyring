# PUSH OPERATOR PROCESS

**Authority:** Andrew-direct 2026-07-24 ~16:00Z, VERBATIM:
> *"We need to change the way pushes work. Commits are fine but pushes should be handled by tier 1 agents
> only, with COO being the primary push operator. It seems to me that the choke is due to pushes not due to
> commits, if that is true then that is where we need to establish a process."*

**Owner:** `2.0.0_SA_COO` (primary push operator) · **Gate:** `1.0.0_SA_CTO`

---

## 0. THE PREMISE IS MEASURED, NOT ASSUMED

Andrew flagged his own diagnosis as conditional (*"if that is true"*). **It was measured and it holds**
(`0.0.0_AB_MSTR`, 2026-07-24, clean state, no contention):

```
ls-remote (pure remote round-trip)   2.0s
fetch                                2.2s
push (hook + negotiation)            6.0 / 6.0 / 6.3s
pre-push hook alone (safe-deploy)    2.0s
```

**But the timing is not the mechanism. THE ASYMMETRY IS:**

> **A FETCH IS CONCURRENCY-SAFE AND INDEPENDENT. A PUSH SERIALISES ON THE REF.**
> One push wins per ref update; every loser is rejected, must pull, and RETRIES — paying the full ~6s
> **including the 2s hook again**. Fetch cost stays flat as agents scale; **push cost goes superlinear under
> contention.** It is the only git operation in our workflow with a contention point at all.

A competing hypothesis (pull-merge churn on the shared index) was **falsified**: 0 merge commits against 107
commits on 2026-07-24. Agents fast-forward cleanly. Recorded because the process is built on the surviving
explanation, not the first one.

---

## 1. THE RULES

| Act | Who | Notes |
|---|---|---|
| **Commit** | **EVERY agent, unchanged** | *"Commits are fine."* Existing gates (Rule 13, 14, 14a, safe-commit) all unchanged. **This is NOT a commit-authority change and must not be read as one — do not slow your commit cadence.** |
| **`git push`** | **Tier-1 only. COO primary.** | Commit, tell COO, COO pushes. |
| `aws s3 cp` / SSM / Terraform via `safe-apply` / DDB | unchanged | **Not pushes.** Unaffected. |

**NO SMALL-LOG EXEMPTION.** Not for log files, not for docs, not for "one-line" commits. A rule that erodes
at its cheapest edge case erodes everywhere. If a carve-out is wanted it is **Andrew's to grant**, not the
operator's to infer and not a lane's to assume.

---

## 2. ⚠ A PUSH IS A DEPLOY — THE OPERATOR MUST RANGE-CHECK FIRST

**VERIFIED AT SOURCE, not relayed:**
```
.git/hooks/pre-push  ->  .tools/git-hooks/pre-push-safe-deploy.sh
  :30-36   HALTGT   halt_gate_check "pre-push"
  :59      bash "$SAFE_DEPLOY" --no-pipescript --commit-range "$RANGE"
```

> **A PUSH DEPLOYS EVERY gold/silver/bronze SCRIPT IN THE PUSHED RANGE — NOT THE PUSHER'S OWN COMMITS, THE
> RANGE.** Concentrating pushes on one operator makes that operator **the single deploy trigger for the whole
> fabric's data-pipeline code**, including code from lanes that never told them it exists. **And the HALTGT
> checkpoint now sits in the operator's lane on every push.**

Measured instance (`0.4.0_DS_ClientPlatform`, 2026-07-24): their retry-net deployed to `opal-data-cot` at
13:53:50Z and D_00 to `opal-data-bd` at 14:51:57Z — **both fired by somebody else's push, not theirs.**
This refines the commit==deploy ruling rather than contradicting it: the true shape is
**commit + ANY PEER'S PUSH == deploy.**

**THEREFORE, BEFORE EVERY PUSH:**
```bash
git fetch origin CLOUD
git log  origin/CLOUD..HEAD --oneline                    # what am I about to publish, whose is it
git diff --name-only origin/CLOUD..HEAD \
  | grep -E 'data/.*/(gold|silver|bronze)/.*\.py$'       # what am I about to DEPLOY
```
If pipeline code is in range, **know whose it is and that its lane intended it to deploy now.** The operator
is not a courier; they are firing someone else's deploy.

**AND VERIFY BY RE-FETCH, NEVER BY `rc=0`:**
```bash
git fetch origin CLOUD && git rev-parse HEAD origin/CLOUD    # must match
```

---

## 3. WHAT A WORKER DOES BETWEEN COMMITTING AND THE PUSH

**This section exists because leaving it unstated is the known failure.** Under a clock, an agent will
reason its way to "I will just push this one" — the same shape as an off-route action taken for good reasons.

1. **COMMIT NORMALLY.** Do not batch commits, do not hold work back, do not slow down.
2. **BATCH THE ASK, NOT THE WORK.** One message at a natural stopping point beats one per commit. Batching
   also amortises the 2s hook tax across the batch instead of paying it per agent.
3. **STATE WHAT IS OUTSTANDING** — commit SHA, one line on what it is, and **whether anything downstream is
   blocked on it.** That last field is the priority signal.
4. **NEVER PUSH YOURSELF**, including when the operator is slow. If it is genuinely urgent, say
   *"X is blocked on this"* — that is the escalation, not a self-exemption.

> ### ⚠ A COMMIT THAT IS NOT PUSHED IS INVISIBLE TO EVERY OTHER AGENT
> **SENT-IS-NOT-READ NOW APPLIES TO COMMITS.** An unpushed commit cannot be seen by any peer, and the
> committing agent gets **no signal that it is still sitting there.** The cheap case is a log file nobody
> waits on. **The expensive case is a lane committing something another lane is blocked on, then waiting on
> the operator's queue for it to become visible.** State the blocking relationship in the ask.

**AND THE INVERSE, WHICH SURPRISES PEOPLE:** on a shared branch **any peer's push carries YOUR commits.**
So *"I did not push"* is **NOT** *"my commit is unpushed"* — verify with a fetch rather than assuming either
way. This process routes **the ACT of pushing; it does not control ARRIVAL** on a shared branch. If gating
arrival is ever the goal, this mechanism does not achieve it and a different one is needed.

---

## 4. OPEN — NOT YET RULED

- **Does this cover a portal DEV→PROD PROMOTE?** A promote is mechanically a push. Surfaced to CTO/Andrew
  2026-07-24 161011Z, **unresolved.** Held rather than assumed in either direction.
- **Tier-0 (`MSTR`)**: Andrew wrote *"tier 1 agents only."* MSTR took the most-restrictive reading and
  **stopped pushing**, surfacing the ambiguity rather than resolving it in their own favour. Andrew's to say.
- **A visible unpushed-work queue** so outstanding commits surface without depending on each worker
  remembering to mention them. Observation from `0.2.0_DT_PortfolioAnalytics`; no design proposed.

---

## 5. RECORD

Instances 2026-07-24: five batched flushes, each range-checked and re-fetch-verified. Several carried 2–3
lanes' commits in a single push — the batching efficiency, and the demonstration that one push flushes the
whole branch.
