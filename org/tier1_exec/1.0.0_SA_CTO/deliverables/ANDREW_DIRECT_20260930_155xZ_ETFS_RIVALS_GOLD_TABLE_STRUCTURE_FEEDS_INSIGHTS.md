# ANDREW-DIRECT 2026-09-30 ~15:5xZ -- ETFS_RIVALS: establish in detail the gold table structure, and how it feeds the served insights

**Terminal:** `1.0.0_SA_CTO~Z`, site Z, after this seat's endpoint Addendum A (@`bd6effc4f3`).

## VERBATIM

> youre goingto get a message from CRO on the subject. I just want to make some points that we should establish in detail what
> the gold table structure is, and how that table structure feeds these served insight deliverables.

## HOW IT BINDS (read narrowly: the PRD's content, no new gate)

The ETFS_RIVALS PRD addendum that follows Addendum A carries a **GOLD MODEL** section, written in detail before any round-2 build
cell is cut. It has two parts.

1. **One entry per gold table**, stating:
   - its grain (one row per what);
   - its key;
   - every column with its type and meaning;
   - which columns are MEASURED, and which are INFERRED with a confidence;
   - its producer and trigger;
   - its builder address (`lib/opal_naming.py address()`, never typed).
2. **A lineage matrix, one row per served insight.** The insights are:
   - the trade schedule (FWD-5);
   - performance by sector and security (FWD-6);
   - projections and the wildcard (FWD-7);
   - the style read (FWD-10);
   - home vs rivals (FWD-11);
   - the page and archive (FWD-1, FWD-9).
   Each row names the exact gold tables and columns it reads, which parts are deterministic computation and which are AI, and what
   the AI system prompt may read. **The AI reads only what the matrix lists.**

The PRD's existing `C-ONE-SIGNAL` clause ("tables beyond `canonical_shape` and `trade_schedule` enter only when a cell names their
consumer") is satisfied by the matrix: every table has a named consumer, or it is not built.

**Input awaited:** `4.0.0_SA_CRO~Z`'s message on the subject, which the model is written against.
