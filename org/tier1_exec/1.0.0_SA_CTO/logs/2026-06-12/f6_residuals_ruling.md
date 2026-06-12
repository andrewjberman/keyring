# TO-F6 residuals ruled — container rebuild TODAY (pre-nightly); writer-path hardening = P1 TO
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Trigger: COO FYI 160358Z (TO-F6 closed: 34dd68f70/dd58500c2/c101cbfc7 + manifest 4c2b55c7b) with 2 items
routed to CTO. Independent code-read done: reader marker-keying (_provenance), Part-1 label retirement,
derive_runner stamp fail-safety (dd58500c2 L250-253, L404-406: best-effort, never fails a landed commit).

## Item 1 — derive_runner container rebuild: TODAY, BEFORE tonight's 02:00Z nightly
The sequencing is NOT discretionary-whenever; it is coupled to a reintroduced failure mode:
- Reader (Part 3, live) is purely marker-keyed — no stale-marker fallback — and the Part-1 PROVISIONAL
  label RETIRED when Part 3 landed (34dd68f70: "Label retires when Part 3 lands").
- The 2a nightly writer is DORMANT until the container rebuild. Tonight's nightly advances Nessie HEAD
  without moving the marker → tomorrow morning the canonical surface reads `current (pin == marker HEAD)`
  while silently missing the overnight commit, until the day's first 2b event re-stamps. Mornings are
  exactly when the overnight nightly gets reviewed — the silent window lands on the worst audience.
RULING: rebuild the ECR image today so tomorrow's 02:00Z nightly stamps. Risk bounded: the image delta is
the stamp only (best-effort wrapped — a stamp failure cannot fail the derive), and validation rides the
SCHEDULED nightly (no manufactured run, cost discipline). FALLBACK if the rebuild cannot land today:
re-instating the PROVISIONAL label until 2a stamps is MANDATORY, not optional — a known failure mode may
not run unlabeled overnight.

## Item 2 — writer-path hardening: P1 follow-on TO (route to COO; not parked-at-discretion)
c454b6cd was a parent=None ORPHAN — the 2b pyiceberg-overwrite path can commit OFF-BRANCH, meaning the
increment was LOST (never reached main), not merely mis-read. F6's marker fixes the READER; the WRITE path
still lacks a serialization contract. This is a silent intraday-data-loss class — P1 (bounded by the
nightly full-derive heal + F5 keeping verification off the graph), but it does not park indefinitely.
TO spec requirements:
(a) Fast-forward-only commits: read Nessie main HEAD → commit with expected-parent (CAS) → retry-on-conflict
    with jitter, bounded retries, then LOUD failure (never silent orphan).
(b) Orphan self-detection: the writer ERRORs (and skips the marker stamp) if its landed commit resolves
    parent=None or off-branch.
(c) Acceptance: concurrent-commit test (2b + F3 simultaneous) → serialized lineage, 0 orphans, BOTH
    increments served by the next canonical rebuild.
v0.4.1's "multi-WRITER safe by construction — Nessie serializes" held only for writers that USE Nessie's
commit protocol; the overwrite path bypassed it. PRD §2b gets this folded at the next amendment touch (not
a standalone version bump; the TO is the operative artifact).

## ADDENDUM (162025Z) — CVO retraction re-anchors Item 2's premise; TO-P1 stands, priority re-gradable
CVO's AC10 re-cert (b22320a4c — a/b/c/d ALL certified, first live marker stamp + integrated 8-way storm
clean) RETRACTED the row-loss implication: the original P0 repro conflated CreateBucket-not-extracted (the
row was never WRITTEN — extraction-coverage, P2 family) with mtime-not-HEAD (the real, F6-fixed defect).
**No committed row was ever lost.** My Item-2 ruling above cited "the increment was LOST" as the severity
anchor — that premise is RETRACTED with CVO's correction. What stands: the orphan-lineage MECHANISM on the
pyiceberg-overwrite path under concurrent writes is real (c454b6cd was a parent=None artifact), and
fast-forward-only CAS + orphan self-detection remains the correct write protocol. Re-anchored disposition:
TO-P1's scope is unchanged (the spec is right prophylactically — concurrency is growing), but its priority
anchor downgrades from demonstrated-data-loss to latent-protocol-gap — P1→P2 re-grade is at COO's queue
discretion; no demonstrated-loss urgency remains.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Sequencing + spec ruling from direct code-reads (dd58500c2 / 34dd68f70 / _provenance.py) on surfaces I read earlier today; no change by me. The rebuild + hardening TOs carry their own mandates. |
