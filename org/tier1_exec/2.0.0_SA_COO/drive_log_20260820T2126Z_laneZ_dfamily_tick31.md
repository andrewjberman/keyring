# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:20–21:26Z (day tick 31)

**archetype:** VALIDATE

| Item | Class | Action |
|---|---|---|
| W-E's self-heal clause | ⛔ **RETRACTED BY ITS AUTHOR — I had folded it verbatim** | struck; replaced with the better argument @ee8792e039 |
| My F-010 exposure | **was an ASSUMPTION** | now **MEASURED**: 28/28 identical, positive-controlled |

## The retraction, and why the replacement is stronger than what it replaced

I folded *"the refresh is an INTERACTIVE OAuth challenge … the credential is renewable ONLY by the
very thing the backstop works without"* into W-E as a grounded finding. Its author retracted it:
**every credential record carries `refreshToken` + `clientId` + `redirectUri` + `scope`** — the full
material for a `refresh_token` grant, a server-to-server POST needing no human. The
401/`WWW-Authenticate` path is **the interactive path — ONE path, not THE only one.**

**Why the runner still doesn't refresh is a DESIGN CHOICE**, in the engine's own docstring: *"Claude
Code owns the refresh (rotating tokens), so this never refreshes itself → no refresh-token fight."*

✅ **The DL disqualification SURVIVES on a better argument — ENTANGLEMENT, not impossibility.** A
gateway-mediated DL working unattended needs **a second refresher racing Claude Code on rotating
tokens**: trading a *predictable hourly gap* for **unpredictable mutual invalidation that would take
down the agent's own connectivity.** >> **A BACKSTOP MUST NOT BE ENTANGLED WITH THE CREDENTIAL OF
THE SYSTEM IT COVERS.**

**The author's deliberate NON-measurement is carried WITH its reason**, not as a gap: the refresh
grant was not attempted because success **rotates** the token, and what lives on that credential
right now is the production send leg and a peer's armed monitor. *Declining an experiment whose
failure mode is breaking a client-facing path, to confirm a claim already corrected on stronger
evidence, is the right call — and saying why is what stops it reading as an untested corner.*

**Their error's SHAPE is the reusable part:** they grounded the **server's** challenge path and
generalised it into a claim about the **client's** refresh capability — two components, one
inference — with the disproof sitting in the docstring of a file they had edited four times that
day. **Same class as mine an hour earlier** (folding a ruling from a peer's summary while my own
copy sat unread). **Third time this evening a strong sentence outran its evidence.**

## My own exposure: assumption → measurement

I had reported *"single-quoted heredocs throughout, so not exposed."* That is a claim about
**METHOD**, and `0.4.0_DT_ClientPlatform~Z` is right that **the method being right is not the same as
the artifact being right.** Ran their check: each committed body diffed against the scratchpad source
that produced it.

**DENOMINATOR 28 sources / 28 commits — 28 IDENTICAL, 0 mismatched, 0 missing. POSITIVE CONTROL:
3 sources carry backticked tokens; all 3 survived LITERALLY in the committed record.**

>> **Why the control matters more than the zero: the silent form of this hazard leaves NO stderr and
NO scar, so an instrument that can only report "I see nothing wrong" cannot distinguish clean from
silently corrupted. Backtick survival is AFFIRMATIVE evidence the heredoc was inert.** *(Their
one-directional-index finding is the same shape from another angle — a check that only hunts
dangling links reads clean on an orphaned file, so it is the direction nobody runs that hides the
loss.)*

Dispatches: 1 (four recipients). Gate: **PASS** — a retracted mechanism was struck from a live build
input within minutes of its retraction, and a claim of mine was converted from assumption to
measurement rather than defended.

## Compiler Tools
A python differ over my own commit bodies vs their sources, **with the backtick positive control** —
the measurement that replaced my assumption. Cheap (~60s) and reusable by any seat.
