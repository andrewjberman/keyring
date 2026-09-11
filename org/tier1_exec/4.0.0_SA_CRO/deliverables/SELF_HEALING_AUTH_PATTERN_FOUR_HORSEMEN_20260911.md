# The Self-Healing Auth Pattern — What It Actually Is, and How It Maps to the Four Horsemen

**Author:** 4.0.0_SA_CRO
**Date:** 20260911
**Status:** BRIEF — memorializing an existing, live pattern and specifying how it applies to the
SA/FT/Bloomberg/WSJ harvesters' bucket/pipeline/infra setup (full-stack vision doc, Part B).

---

## 0. Correction before anything else: this is Inflection's pattern, not Cottonwood's

Andrew's framing was "we had created a self-healing auth pattern I believe for Cottonwood." Checked
directly rather than assumed: **the real, live, original pattern belongs to Inflection (INF)**,
authenticating against **Orion** (a custodian platform), not Cottonwood. `cot-bd-session-trigger`
(`infra/aws/terraform/cot-pipeline/lambdas.tf:9`) is explicitly labeled *"Analog of inf-jwt-trigger
for Black Diamond OIDC session refresh"* — Cottonwood COPIED the pattern for its own Black Diamond
integration, but that copy is **staged, not applied**: blocked on Andrew's own §6.1 GO ruling, an
unauthorized `blackdiamond/cot/credentials` secret write, and a missing `user-data.sh`
(`cot-pipeline/ec2.tf:6-10`). Worth a separate word to Andrew that Cottonwood's own copy is stuck —
not this brief's scope, flagging so it doesn't get lost.

**This brief describes the INF original** — live, deployed, confirmed via `comp-find --corpus aws`
(real Lambda ARN `arn:aws:lambda:us-east-1:313476888478:function:inf-jwt-trigger`, `drift=DECLARED`)
— since that's the actual working mechanism to imitate, not the blocked copy.

**Already memorialized** — this exact pattern already has a home: `docs/architecture/ADVI_JWTRES.md`,
plus task orders `ADVI_JWTRES.001` (freshness check) and `.002` (auto-recovery). Andrew's instinct
that "this should be memorialized somewhere" was right; it already is. This brief's job is the
mapping onto the four horsemen, not re-documenting INF's own pattern from scratch.

**Why it exists — the origin incident**, cited in `jwt_freshness.py:1-6`: 2026-04-30 09:09Z, the
Orion JWT expired 14 minutes before a scheduled Lambda deploy, and five Inflection bronze pulls
silently returned `{ok:0, fail:5}` — discovered only after the fact, not at the time. The pattern
exists specifically to make that class of silent failure impossible.

---

## 1. The real mechanism, in full (two halves)

### 1a. Preemptive half — refresh on a schedule, before anything needs it

EventBridge cron, 12:00 UTC daily, invokes `inf-jwt-trigger`
(`infra/aws/terraform/inf-pipeline/lambdas.tf:308-321`). That Lambda:
1. Starts the `inf-exporter` EC2 instance.
2. Writes an S3 "mode marker" telling the box what to do on boot.

On boot, a systemd service (`inf-jwt-fetch.service`) reads the marker, runs a Playwright OTP login
to Orion (`bun run orion_export.ts`), writes the fresh JWT to **both** Secrets Manager
(`orion/jwt/current`) and S3 (`opal-data-inf/orion/jwt/current.json`), then self-shuts-down the EC2.

### 1b. Reactive/self-healing half — the part Andrew specifically described

Every downstream pull Lambda (`inf-accounts-v2-daily`, `inf-api-positions`, etc.) imports
`jwt_freshness.py` and calls `recover_or_exit()` at startup, BEFORE attempting its actual pull:

- If the current JWT has **< 30 minutes remaining**, it does NOT just fail or wait passively. It:
  1. **Snapshots the current `issued_at_iso`** (the timestamp the current JWT claims to have been
     minted).
  2. **Async-invokes `inf-jwt-trigger` itself** — the SAME Lambda from §1a, triggered on-demand
     instead of waiting for the next 12:00 UTC cron fire.
  3. **Polls S3 every 30 seconds, up to 15 minutes**, waiting for `issued_at_iso` to ADVANCE past
     its snapshot.
  4. On advance, reloads the fresh JWT and **continues the SAME invocation** with it, running the
     original data pull that triggered the freshness check in the first place.

**Correction to Andrew's own framing, stated plainly rather than silently kept:** this is not "an
EC2 sign-in that rolls into a SEPARATE retry Lambda pull" — it's **one Lambda invocation that blocks
inline on the EC2 sign-in, then continues itself.** Functionally self-healing either way — the pull
that would have failed instead succeeds, automatically, with no human and no next-scheduled-run
needed — but the actual shape is a single blocking call-and-continue, not a two-Lambda chain.

**The single most valuable, portable idea in this whole pattern:** step 3 doesn't just wait a fixed
amount of time and assume the refresh worked — it **polls for proof that the underlying credential
actually advanced** (`issued_at_iso` moved forward), not just that time passed. A refresh that
silently failed (bad OTP, site changed, network issue) is caught here — a fixed-sleep-then-retry
approach would not catch it.

---

## 2. Mapping onto the four horsemen — platform by platform, not a blanket answer

None of SA/FT/Bloomberg/WSJ literally carry "a bearer JWT" the way Orion does, so this is a
conceptual transfer, not a copy-paste. Applying Rule 24 discipline here — subtracting from what
actually exists per platform rather than assuming the pattern applies uniformly:

### WSJ — the pattern DOES NOT APPLY, and that's correct, not a gap

WSJ's mechanism is Bright Data Web Unlocker only — cookieless, stateless, no persistent session at
all (confirmed earlier this session: WSJ is loginless by design, scoped to public news). There is
no credential to go stale. **Explicitly out of scope** — naming this so nobody later wonders why
WSJ has no freshness check.

### SA and FT — the pattern maps directly, and the "re-auth" half already exists

Both already have proven, working re-authentication flows built this session
(`sa_harvest_session.py`, `ft_harvest_session.py`) — these ARE the equivalent of Orion's
`orion_export.ts` OTP-login step. Both platforms park a session (cookie jar) to Secrets Manager
after a successful login, same shape as `orion/jwt/current`.

**One real structural difference from INF that changes the design, not just the labels:** INF's
PULL step runs in a Lambda (which cannot run Playwright), so it MUST hand off to a separate EC2 for
re-auth and poll a shared store (S3/Secrets Manager) to get the result back. SA/FT/Bloomberg's PULL
step is **already EC2-shaped** (per the full-stack vision doc's B1 — Playwright doesn't fit Lambda).
So the four-horsemen version can be SIMPLER than INF's: **the freshness check and the re-login can
run in the SAME EC2 process**, inline, with no cross-process polling handshake needed — check
session validity → if stale, re-run the platform's own login flow right there → proceed to pull —
because the box that needs the fresh session IS the box that can mint one, unlike INF's Lambda/EC2
split.

**What still transfers exactly, even without the cross-process split:** the "prove advance, don't
assume" principle. Instead of `issued_at_iso`, each platform's own tracked cookies already carry an
equivalent signal — **Bloomberg's `TRACKED_COOKIE_NAMES` already includes `_last-refresh`**
(established this session, `bloomberg_harvest_session.py`) — exactly the kind of value a freshness
check should snapshot-then-confirm-advanced after a re-login, the same shape as `issued_at_iso`.

### Bloomberg — the pull-vs-refresh split DOES come back, for a different reason than INF's

Bloomberg has two separate credential surfaces that need to be told apart:
1. **The `_user-jwt`/`_last-refresh` cookie jar** (this session's harvest mechanism) — same
   treatment as SA/FT above: EC2-local, inline re-login on staleness.
2. **The blpapi Terminal session** (price/reference data, `integrations/bloomberg/READ_HERE.md`) —
   fundamentally different. This is a **two-phase BUDGETED sign-in** per the estate's own standing
   documentation, machine-bound to whichever box holds the terminal session, and — unlike Orion's
   OTP or SA/FT's captcha-solvable logins — not confirmed to be fully headless-automatable (the
   budgeted/two-phase framing implies a human or a constrained retry allowance is part of the
   design, not an unlimited automated retry loop). **Do not build an `inf-jwt-trigger`-style
   unattended auto-recovery for the Terminal session without confirming that's actually safe against
   whatever budget/rate-limit reasoning produced the "two-phase budgeted" design in the first
   place** — this is a real difference from INF's Orion login, not an oversight to just port over.

---

## 3. What this means for the bucket/pipeline setup (full-stack vision doc, Part B)

Andrew's own framing — "that is also something that will have to be involved when setting up the
bucket structure... the pipelines, and the associated resources" — is confirmed correct. Concretely,
each platform (SA, FT, Bloomberg's cookie-jar half) needs the INF-pattern's two stores, scaled down
to the inline-EC2 shape from §2:

- **Secrets Manager: current session per platform** — already exists for FT (`astn/ft/session`);
  needs the equivalent for SA and Bloomberg's cookie-jar credential if not already present under a
  parking secret from this session's harvest work.
- **A small freshness-check library, shared across the four-horsemen EC2 box** — following the same
  "prove once, reuse everywhere" precedent this session already set with `press_and_hold_lib.py`
  (shared SA+Bloomberg) and `nopecha_hcaptcha_lib.py` (shared FT+Bloomberg): a
  `session_freshness_lib.py` that each platform's harvester imports, checks its own tracked cookie
  set for staleness (age threshold + the "prove advance" cookie, e.g. `_last-refresh`) before
  starting a day's active-monitor-set sweep, and re-runs that platform's own login flow inline if
  stale — never a separate Lambda round-trip, per §2's structural note.
- **No new S3 marker/polling mechanism needed** — because the re-auth is inline on the same box,
  the cross-process S3-polling handshake that INF needs (Lambda can't run Playwright, so it must
  signal a separate EC2 and wait) has no reason to exist here. This is a genuine simplification, not
  a missing piece — worth stating so nobody builds the S3-polling machinery reflexively just because
  INF has it.
