# NEVER-WIDEN -- CTO HALF: `HVST-cm-1`, drain the one queued BP/ pull through the box consumer (round 98)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~16:2xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round98/NEVER_WIDEN_HALF_COO_CM1_DRAIN_THE_QUEUED_BP_PULL.md` as committed
at 605cf47891, sha256 `688cd3187e2d019089ee64bc7d889be1c2e978ffad5be4697cdf9d37f26274a3`. Any edit to that file voids this half.

## What I read at signing

- **The act is my round-97 ruling:** one drain, through `pull_consumer.py --once` only (C-1, C-4), with no direct Terminal or blpapi call
  beyond the read-only `bloomberg_health()` and one confirming read after a sign-in.
- **W1's two facts, which this half acts on:**
  - **The consumer is a person-started poller, not a service.** That is why the request sat. It is the CAUSE C-5 names.
  - **On an unhealthy Terminal the consumer writes FAILED and DELETES the message.** So the health read comes FIRST, and the sign-in
    (READ_HERE section 2, at most ONE submit, C-3) comes only then. The consumer is never started against an unhealthy Terminal.
- **The served move:** BP's newest bronze pull and newest derived model block, which the gateway serves (`harvest_get_fundamentals` and
  `harvest_security_coverage`). Add-only under the canonical partitions; N = 1 writer of each in this act.
- **Accepted consequence:** the BP dossier written at 15:51Z falls one model block behind until the scheduled refresh (round-97 item
  4). The lag is stated, not hidden.

## Blast radius

- One Bloomberg request (refdata, histdata and bestdata for one security) through the sanctioned queue.
- Add-only S3 objects under BP's canonical partitions, plus the status object updated in place (its prior bytes are saved first).
- No other security, no dossier write, no gateway or host change, no IAM or schedule change.

## Both branches

Branch D and Branch F are as the COO half states them. A refused or blocked drain leaves the request queued, records
`BLOCKED_TERMINAL`, and retries nothing.

## Conditions of this signature

1. **The health read decides whether the consumer starts at all:**
   - if `bloomberg_health()` is not ok, and the one sign-in submit is not used or fails, do NOT start the consumer;
   - the message must not be deleted by a FAILED run;
   - record `BLOCKED_TERMINAL` and stop.
2. **C-1 to C-6 bind as written**, including site Z told first (C-6) and the NEVER-2 close COMMITTED (C-2).

## Routed, not conditions (round-99 rows)

1. **Requests strand by design:**
   - `pull_enqueue` requests drain only when a person starts the poller, so every gateway pull request waits on an operator;
   - either the status says plainly "waiting for an operator run", or the consumer is scheduled under its own pair (with the Terminal
     health read first);
   - a design fork, to be ruled at round 99 with the CRO's past patterns if needed.
2. **Delete-on-unhealthy loses requests:** a FAILED run against an unhealthy Terminal should leave the message for the next run, not
   delete it.

## VERDICT: SIGNED (CTO).
