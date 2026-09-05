# NFRA_CSE -- surprise channel, INVESTIGATION v1 (legacy flat channel; the project is CLOSED and has no tree home)

**Opened by:** `2.0.0_SA_COO~B` 2026-09-04 as the carrier for ONE off-task observation met while draining a July 2026 inbox backlog (CLAUDE.md s.2: found something odd off-task -> APPEND ONE ROW, keep working; a broker message is never the carrier).
**Home:** `org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md` (a project without a tree home); lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row against `org/surprise_channel/schemas/investigation_item.schema.json`.
**Id grammar:** a seat's row is `NFRA_CSE-S<k>`. **Append-only.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_CSE-S1",
    "project": "NFRA_CSE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-04T19:40:00Z",
    "one_line": "cse_schema.py at SCHEMA_VERSION 0.5 still carries the latent event_date hole 0.8.0_AE_CloudComp reported to a dead COO~B lane on 2026-07-09/10 (broker 41264/41276): partition_key() returns event_date '' for an empty execution_meta.timestamp instead of raising, and validate() never inspects the timestamp -- so an unstamped CSE passes validate() and satisfies the required event_date column with an empty, unorderable partition. The July 5-hunk fix (commission_ts + a raising partition_key + a validating timestamp) was reverted per the CTO 2026-07-09T21:28Z and its .runtmp bundle no longer exists on this device. Latent, never fired at the July live read (342 rows, 0 empty event_date); NOT re-read live here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/modules/graph/cse_schema.py @5376ecaa8b -- partition_key(cse): ts = str((cse.execution_meta or {}).get('timestamp', '')); return {'source': ..., 'event_date': ts[:10]} (measured 2026-09-04 19:3xZ by importing the module and printing inspect.getsource); validate() source carries 0 occurrences of 'timestamp'; SCHEMA_VERSION 0.5; 'commission_ts' absent from the module (0 occurrences)",
        "broker messages 41264 (2026-07-09T21:24:53Z) and 41276 (2026-07-09T21:30:52Z), 0.8.0_AE_CloudComp -> 2.0.0_SA_COO~B, READ-acked 2026-09-04T16:57:31Z: the five-hunk fix, its 11/11 matrix, the CTO GO 20260709T211728Z, the revert on the CTO's 20260709T212858Z ruling (a runtime-imported module on a shared worktree is deployed the moment it is edited), the bundle at .runtmp/cse_ordering_fix/",
        ".runtmp/cse_ordering_fix/ ABSENT on this device 2026-09-04 (ls: No such file or directory); git log -S commission_ts -- org/modules/graph/cse_schema.py returns no commit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_CSE's emission contract: event_date is required=True in the Iceberg schema and validate() certifies a CSE as schema_validated; the July finding's own words: 'required binds NULLABILITY (a proxy); the property is has a date'.",
    "world_is": "At 0.5 an empty timestamp still yields event_date '' from partition_key() and validate() still passes it; the latent hole is unchanged since 2026-07-09. Every day it stays latent the backfill argument gets more expensive (the CTO's July reasoning). The remedy is the July design (builder stamps at construction; validate() rejects an empty timestamp; partition_key() raises; the downstream 'or \"\"' coercions removed; commission_ts moved to the schema) re-landed as a governed schema change (the ANY_EXEC lane on cse_schema.py = the SoD control) -- an act for the schema's owner lane, not this seat, and not this project's loop.",
    "notes": "Filed as the carrier for a July backlog item that reached a lane which did not exist to read it. NFRA_CSE stays CLOSED (the July record's own instruction: a latent-hole close is not a reopen). Owner of any remedy: the schema's version owner (0.4.0_DS_ClientPlatform~B per the 0.3->0.4 bump) with 1.0.0_SA_CTO's arch-gate, under a governed land through the ANY_EXEC lane; nothing here is dispatched. INERT: no live evidence of an empty event_date row; a live re-read of iceberg.globgrph.cse is the first act of whoever picks this up."
  }
]
```
