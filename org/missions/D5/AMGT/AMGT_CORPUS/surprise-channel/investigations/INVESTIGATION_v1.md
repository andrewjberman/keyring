# AMGT_CORPUS -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Opened by:** `3.0.0_SA_CVO~Z`, 2026-09-23, at L4-R. **Home:** the project tree's channel. Lane `ANY`;
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Why this file is opened before any issuance.** This project has no seat, no decomposition and no order, and
its PRD has been blocked all night by a fabric defect outside it. The finding needs a carrier that survives the
seat that made it, and a broker message is never that carrier. The first row is the reviewer's own.

**Id grammar on this fabric:** a seat's row is `AMGT_CORPUS-Z-S<k>`; a worker's row is `AMGT_CORPUS-Z-W<n>-S<k>`
with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_CORPUS"` and `"fabric": "site-z"` on
every new row. The CVO's adjudication rows live in `adjudications/`, never here.

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-S1",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:20Z",
    "one_line": "The spine's overdue-brief-half RE-ROUTE consults LIVENESS, which cannot see CONSUMPTION, so it could never fire for a seat that heartbeats and reads nothing: 4.0.0_SA_CRO~G shows LIVE seconds old while its read/ is EMPTY and 13 messages sit unread, and this PRD was blocked all night behind it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured by this seat 2026-09-23 ~01:1xZ: org/mcp/inbox/4.0.0_SA_CRO/~G/ top level carries unread messages while .../~G/read/ contains 0 entries -- nothing has ever been consumed.",
        "1.0.0_SA_CTO~Z msg 24492: liveness LIVE at 01:10:38Z (seconds old); last commit by that serial d5e870fed2 at 15:43, ~9.5h earlier, on an unrelated subject; the L4 notifier delivered this PRD's review nine times (20:00, 20:01, 20:41, 21:15, 21:55, 22:30, 23:09, 00:18, 00:51) plus two direct messages and two broadcasts -- 13 items, 0 read.",
        "The spine's provision re-routes an overdue brief half to a live COO when the CRO is 'not online'; the condition reads liveness, and liveness reports this seat as fine."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An overdue half re-routes to a live alternate reviewer, so a PRD cannot stall on one unavailable seat.",
    "world_is": "The trigger's instrument answers a question adjacent to the one asked -- is the process alive, not is anyone reading -- so a heartbeating, non-consuming seat holds a half indefinitely and nothing fires.",
    "notes": "THE DISCRIMINATOR IS CHEAP AND NOBODY WAS RUNNING IT: read/ EMPTY with a NON-EMPTY top level. Liveness is a heartbeat; read/ is consumption. A staleness trigger reads the second. ⚠ A row records the defect; it does not build the fix -- the trigger is fabric machinery outside this project and outside any AMGT lane, so its owner is the fabric's, not this project's, and no gate is built here. The immediate block was cleared by hand (1.0.0_SA_CTO~Z re-routed the brief half to 2.0.0_SA_COO~Z under the spine's own 'or a live COO in their stead'), which closes THIS instance and leaves the mechanism open. Seating of 4.0.0_SA_CRO~G is 0.0.0_AB_MSTR~Z's."
  }
]
```
