# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2045–2120Z

**archetype:** IMPLEMENT
**Project:** OPAL_ANALYST channel-leg P1 + D7 fuse hardening (inside the Andrew-direct exclusive focus)

## Summary

**Channel-leg P1 landed and accepted** (`3e8de96ed1`, accepted @d6918a99e1). `teams-watch.py` was
structurally channel-blind while the estate's client-ticket buzzes post to a channel — a defect
that demonstrated itself inside the water test, with a correct buzz waking nobody. The leg adds a
`--channels` direct bounded read per cycle (no change-signal exists for channels), per-channel
cursors in their own file, failed-read holds scoped to the failing key, ids-never-names config
with refuse-if-unset, and — deliberately — **no self-identity filter**, because the ticket buzz is
posted *as* the pinned identity and filtering it would rebuild the exact deafness. `fresh_messages`
is reused byte-unchanged so the two surfaces cannot drift apart in semantics.

**Then all eight fuse artifacts gained a LIVE PRODUCTION header** (`ab4f76c878`), per ruling 3a's
recommendation routed to this seat. Nothing in the tree marked these files as live production; now
each says so in its own text, names the task and cadence, and points at bar A5–A7 with
revert-first. The next editor will not have read tonight's messages, but cannot avoid reading the
file they are editing.

## The part worth carrying: A7 was discharged as a MECHANISM, not a discipline

Ruling 3a asks a human to remember something under time pressure on a five-minute fuse. Instead:
develop entirely off-tree, then land via a **self-reverting script** — save → compile → battery
against the *deployed* path → real runner exercise, with any failed gate restoring HEAD. Channel
leg: **21:01:44 → 21:01:46, two seconds**, no instant of exposure. Headers: 21:11:30 → 21:11:32,
exercised *through the real `.cmd` wrapper* so the wrapper edit was exercised too. The gate's own
read: "Prose asks people to remember; a control does not care whether they do."

## Evidence

| Bar | Result |
|---|---|
| A2 two-in-one-window (channel) | both emitted, oldest-first, framed, pre-cursor excluded, cursor = max message ts |
| A3 chat path | BARE stdout **byte-identical** to HEAD on a real 2-message chat cycle; zero channel lines unarmed |
| A4 mutant | empty set → loud exit 2; restored → hears both. Plus per-channel cursor isolation, first-arm seeds at NOW (0 of 10 historical), bad path → exit 2 named. **17/17** |
| Discriminating control | same battery vs HEAD's blind engine **FAILS 10** including "0 of 2 in-window fresh" |
| A5/A6/A7 | runner exercised post-edit (`INTAKE PASS OK`, rc=0), in the deployed tree, inside one act |
| A1 | OPEN and correct — next real post after BG's re-arm (armed, `channels=1` verified, no backfill) |

**Harness defect I caught in my own battery:** two refusal checks reported FAIL while the engine
was *right* — `run()` catches `SystemExit` and returns the code, so the `try/except SystemExit` I
wrapped around it could never fire. Same class as my TO6 harness defect, inverted. Fixed to read
the returned code; both then passed.

## A measured production finding, and a design question it settled

The 21:04:46Z fire exited 2 — the gateway OAuth credential has a **~1h TTL refreshed only as a
side effect of an agent MCP call**. My edit was exonerated *by the failure path itself* (exit 2 via
that message requires a clean import and a resolved pin) — a better standard than "it worked a
minute ago". Restored with one legitimate gateway read; runner re-exercised clean.

Then, assigned the DL's first question, I settled it at source and the layer mattered:
`server.py:15` validates the gateway Bearer **before any tool dispatch**, so every gateway-mediated
send inherits the dependency **by construction** — no per-tool test needed, no per-tool exception
possible. And the refresh is an interactive OAuth challenge (`:81-87`, "triggers Claude"), so a
scheduled task structurally cannot self-heal. Gateway is disqualified for the DL on criterion (1);
SES survives.

## Corrections — one of mine, twice

My proof instance claimed the water-test fire ran "with the Analyst seat DOWN … MEASURED, not
assumed". The seat was **alive**; I had measured a broker reading and inferred a seat state.
Corrected (`87775d2227`) — and the first correction was **itself defective**, because it explained
the false reading with a mechanism that was retracted in full forty minutes later. Re-corrected
(`d594fd705b`) to rest on observation-without-cause, which is all it ever needed. I deliberately
did not re-quote the retracted mechanism's memorable line inside the retraction: striking it in
place leaves the sentence propagating, and that sentence is precisely what propagated. Residual
sweep: zero surviving instances. Owned in the instance's surprises — I accepted it because it
arrived with the word GROUNDED on it and was well-phrased, three hours after correcting another
seat for exactly that.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `.tools/commit-gate.sh` | py_compile + ruff clean on the engine; retired-alias invariant PASS | PASS |
| `proof-of-spec-check.py` ×3 (positional, rc unpiped) | VALID rows=4 violations=0 after each correction | PASS |
| Path-form probe | Windows form OPENS the channels config; **/cygdrive form FAILS FileNotFoundError** — handed to BG as a warning and they confirmed it was load-bearing | PASS |
| Source reads (gateway) | `server.py:15,81-98`, `tools.py:214/228` — the transport-layer bearer finding | PASS |
| `safe-commit` ×4 + risk-reflex | 3e8de96ed1, ab4f76c878, 87775d2227, d594fd705b | PASS |

## Blockers

None I hold. A1 pending a real post at BG. Next: W-A (amended cut, WA-1..9), W-F staged behind
design, the DL transport question answered and returned to the gate. Runner live; note the
standing qualifier — **the intake is live while a session is warm**.
