# ANDREW-DIRECT: lambda backfill requires row-level chunking, else auto-start/stop EC2 (~20:3xZ)

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

**Date:** 2026-07-14
**Task Orders:** delta-6 commission (CTO 200541Z) -- this ruling binds its design fork

---

## The instruction (VERBATIM -- the phrasing IS the ruling)

Channel: Andrew direct to 0.4.0_DS, chat, 2026-07-14 ~20:3xZ (~4:3x PM ET):

> "for backfill you cannot get away with doing this stuff with a lambda, unless you have
> row-level chunking ability. THe question then becomes if it is efficient/possible to develop
> row-level chunking solutions then that could work, otherwise need auto-startup/auto-shutdown
> ec2 machines"

Broadcast same turn: CTO 203857Z, COO 203903Z, MSTR 203908Z. Scope surfaced, not adjudicated.

## How it lands on my board (delta-6, tomorrow)

The fork, as ruled: (a) row-level chunking in Lambda IF efficient/possible; (b) otherwise
auto-startup/auto-shutdown EC2. The CTO delta-6 commission is branch (a) for the current heavy
class; Andrew has now named branch (b) as the mandated alternative, not merely an option.

Design consequences carried into tomorrow:
1. **Delta-6 acceptance gains a MEASURED Lambda-envelope go/no-go**: streamed peak-RSS +
   wall-time on THE failing unit (orion fact_transactions 07-10, 1.39M rows) must land well
   inside memory AND the 900s wall -- measured with 0.6.2's peak-RSS method, stamped in the
   pin-verify report. Miss -> pivot to branch (b), no second Lambda attempt.
2. **Branch (a) is live for the current class on its merits**: orion jsonl.gz and schwab CRS
   are line-delimited -- genuinely row-streamable (gzip line iterator -> bounded chunks ->
   RecordBatch -> incremental ParquetWriter; peak = O(chunk) not O(partition)).
3. **Branch (b) has estate precedent** (bd-gold-trigger boots an EC2 runner on demand;
   auto-shutdown pattern exists) -- if invoked, it is 0.7.0/CTO infra lane, my converter code
   rides either substrate.
4. **Non-streamable whole-file formats at scale** (future multi-GB xlsx/binary) are branch (b)
   by construction -- named now so the next heavy class does not re-litigate.
