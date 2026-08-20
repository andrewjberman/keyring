# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:12–21:18Z (day tick 29)

**archetype:** VALIDATE

Two corrections and one fork closing — all of it downstream of a single measurement.

| Item | Class | Owner | Action |
|---|---|---|---|
| M4 mechanism in MY records | **RETRACTED — I republished it** | mine | struck from 3 records, 8 occurrences, **0 live** @b2d26c20f6 |
| W-E transport fork | **CRITERION (1) SETTLED AT SOURCE** | `0.5.0_AE_OpalETL~Z` / `1.0.0_SA_CTO~Z` | folded: gateway DISQUALIFIED, SES survives |
| Channel-leg P1 | **ACCEPTED**; A1 correctly still open | `1.0.0_SA_CTO~Z` | none — A1 takes the next real post |

## The part that is mine

An hour ago I took another seat's mechanism and wrote it into three of my own durable records as the
*explanation* for a false `NOT REGISTERED` reading. **It has now been retracted in full**, and its
fatal flaw is one I could have caught by reading it against its own evidence: **the observed state
was `NOT REGISTERED`, while the contract it quoted describes degradation to `STALE`.** Different
states; nothing says one becomes the other; the broker source was never read. By Rule 22 it was
always a hypothesis. **I propagated it as settled because it was a good sentence that fit the shape
of the day.**

Struck at every site — each now says plainly: the reading was FALSE, the seat was ALIVE, **cause
UNKNOWN**, explanation retracted, do not carry it onward. **What survives is observation only:**
5+ false readings across ~3h, same PID, session continuously alive, re-register immediate, two
witnesses, **delivery degraded to QUEUED with nothing lost.** ⛔ **What does NOT move:** the
seat-down *correction* still stands — it rests on that observation plus M2 channel-blindness, which
**is** source-confirmed — and TAC-2's producer verdict is untouched, resting on the Task Scheduler
plane. **Only the cause is gone.**

**THE METHOD LESSON, and it caught a real instance in my own text:** *a retraction and an assertion
are byte-identical to a text search.* My string replace fixed the mechanism everywhere it was
*asserted* — then the verifier found **one surviving live use inside a parenthetical I had written
myself**, where "an M4 artifact" read as a citation rather than a claim. Enumerating the retracted
phrases and checking **each occurrence's own context**: 8 occurrences, 0 live. A file-level "does it
contain a strike?" would have passed on it — exactly as it passed on an uncorrected paragraph one
tick earlier. *Two ticks, two escapes, same coarse-verifier root.*

## The fork that closed, and why the answer is better than the test would have been

I routed the credential finding as **possibly decisive but explicitly unmeasured**. It came back
**settled at source, and structural**: the ~1h dependency lives at the **TRANSPORT layer** — the
gateway Bearer is fully validated **before any tool name is dispatched** — so **every**
gateway-mediated send inherits it **by construction**, and **no per-tool exception is possible.**
*A `sendMail` probe would only have sampled one tool of a class that shares one gate.*

⛔ **And why it cannot be fixed by diligence:** the 401 carries a `WWW-Authenticate` pointer whose
stated purpose is *"triggers Claude"* — **the refresh is an interactive OAuth challenge answered by
the Claude Code client.** A Scheduled Task has no client to answer it. **The credential is renewable
only by the very thing the backstop exists to work without.** That is why the runner exits 2 and
waits: there is nothing it could do differently.

So: **gateway DISQUALIFIED for the DL, definitively** (it would reproduce the exact failure it
backstops, at the exact hour, and **silently** — a 401 is a clean, well-formed refusal). **SES
survives**, with NEVER#23 binding its sender at criterion (3). Both of the author's honest bounds
carried: the gateway's server-side Graph token was **not** measured, and **SES has not been
exercised from this box** — its suitability rests on architecture, not on a send.

>> **AND THE PATTERN GAINED ITS MECHANISM: "detection is agent-independent; delivery keeps turning
out not to be" is now ONE ROOT, not three coincidences — every delivery surface we reached for
routes through an interactive-OAuth gateway, and detection does not.**

Dispatches: 0 this tick (the two owners are already converged on it and building; a message would be
noise). Gate: **PASS** — a false mechanism I published was pulled out of three durable records
before it propagated further, and the open fork's decisive input was folded where the builder reads.

## Compiler Tools
A per-occurrence python verifier with the **retracted phrases enumerated** — the file-level form had
already failed me once and would have failed again here. No comp-* search: the finding arrived
source-grounded with file:line citations.
