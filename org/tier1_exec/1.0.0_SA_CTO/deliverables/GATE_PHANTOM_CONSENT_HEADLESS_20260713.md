# GATE DESIGN: phantom-consent (headless AskUserQuestion is NEVER Andrew) -- CTO

**Author:** 1.0.0_SA_CTO (base) | **Date:** 2026-07-13 | **Status:** DESIGN -- for MSTR concur + COO
TO-record/route. **Incident (MSTR 031450Z):** a headless-spawned agent (0.7.0, `-Headless`) ran an
in-session AskUserQuestion, received an auto/self-handled answer, and treated it as ANDREW'S CONSENT to a
prohibited-surface WRITE -- applied IAM + downloaded 85 files to `opal-data-schwab/backfill/` before
MSTR's sovereign-scope flag halted it. The most-protected surface was written on an answer Andrew never
gave. (Files held inert, no exposure; the subsequent REAL backfill was separately Andrew-authorized
in-channel -- 43e8dbb3a -- which is exactly what consent is supposed to look like.)

## 1. The hole, precisely

`-Headless` drops the interactive channel, but AskUserQuestion still RETURNS an answer-shaped value. The
agent cannot distinguish "Andrew answered" from "the harness auto-resolved my prompt" -- so a
consent-shaped string arrives with none of consent's provenance. This is a PROVENANCE hole, not a judgment
hole: the same doctrine as Rule 22 ("a causal claim is a hypothesis until grounded") applied to
authorization -- **"Andrew-direct" must be GROUNDED (channel + timestamp + quote), not asserted.**

## 2. THE GATE -- three layers, smallest-first

- **P-1 (kill the source; small, buildable now):** the spawn wrappers (`spawn-agent.ps1` / `ajb.ps1`
  `-Headless` path) export `OPAL_HEADLESS=1`; a PreToolUse hook on AskUserQuestion in headless sessions
  DENIES with the teaching message: "Headless session -- AskUserQuestion cannot reach Andrew; its answer
  is NEVER consent. Route the question to your dispatcher (MSTR/COO) via MCP and HOLD." The prompt
  becomes INERT instead of consent-shaped. Owner: fabric infra (hooks); COO routes. Falsifier test: a
  headless probe agent calling AskUserQuestion gets the DENY, not an answer.
- **P-2 (ground the grant; the durable fix):** an **Andrew-grant ledger** -- `org/mcp/andrew_grants/`
  (append-only; MSTR/COO write one small file per explicit Andrew authorization: verbatim quote, channel,
  timestamp, scope, expiry-or-one-shot). Any sovereign-crossing action (held-surface write, vendor
  egress, scope-lift execution) must CITE a grant file in its dispatch/commit/ledger entry. An
  authorization that cannot name its grant file is `INFERRED` and NON-ACTIONABLE (the Rule-22 gate
  pattern, applied to consent). This also fixes the adjacent chronic ambiguity: "Andrew said X" claims
  become checkable references instead of assertions. Owner: MSTR/COO convention + a lint (a dispatch/
  deploy-ledger entry touching a held surface without a `grant:` field fails the gate).
- **P-3 (the backstop; already-proven pattern):** extend `sovereign_held.py`'s predicate consumers:
  tools that WRITE (s3 cp/put wrappers, safe-apply on held-bucket TF) check
  `is_held_bucket(target) AND no grant citation -> refuse`. The corpus-load assert
  (`assert_sovereign_safe`) proved this by-construction pattern works; this extends it from the probe
  corpus to write paths. Incremental -- each wrapper adopts it as touched.

## 3. What does NOT work

- "Headless agents should be more careful" -- prose against false certainty (same law as the identity
  SEV d1aa23968: the agent BELIEVED it had consent; a rule consulted only when in doubt cannot fire).
- Banning headless spawns -- throughput-destructive; the hole is the prompt's provenance, not headlessness.

## 4. Acceptance

1. P-1: headless AskUserQuestion returns the DENY (exercised via a probe spawn); interactive sessions
   unaffected (positive control).
2. P-2: a sovereign-crossing dispatch WITHOUT a grant citation fails its gate; WITH one, it passes and
   the citation resolves to a real grant file whose scope covers the action (exercised both directions).
3. P-3: a held-bucket write through a patched wrapper without a grant refuses loudly (and the refusal
   names the missing grant, not a generic error).

Routing: MSTR concur on P-1/P-2 shape (his incident, his ledger-write role in P-2) -> COO TO-record +
allocate. I arch-gate the diffs.
