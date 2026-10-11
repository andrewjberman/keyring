# TCKT_VNEXT round 2, cell R2-tr-1 -- L9 grade of TO-RUN-R2-tr1 AC2 (the FWD-1 thread re-run)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:15:51Z, on `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_TR1.md @4387ede65a (msg 4548)`. Row TCKT_VNEXT-D2-S33.

| criterion | verdict | evidence |
|---|---|---|
| AC2: FWD-1's ACCEPT, "the report is made from the filed file, and the finished report opens from the same ticket", shown by hops (e) and (g) reading the finished report for the id the service issued and the ticket holds; one firm only; the row removed after `exp` | **NOT MET** | In run 3's trace hops (e), (f) and (g) each read UNREACHABLE with 0 calls, and hop (d) records `request_id: None`. No run read a finished report, and no ticket holds an id the service issued. The issuer's own reading is the same |

## Run 3's submission, read from the service's side

The runner called hop (d) refused: HTTP 200 with the public reason NOT_READY. This seat read the generate function's log across
the run's 30-minute token window:

- 12 invocations and 2 refusals logged. Both refusals are other calls (an upload refused NOT_AUTHORIZED, a request with a missing
  field). Neither carries NOT_READY.
- The last invocation, at 08:14:32Z, ran 5.6 seconds and logged no refusal. Round 1's accepted submission had the same shape
  (6.0 seconds, no refusal).
- So the service did not refuse it. That agrees with the issuer's code read: an accepted submission answers QUEUED with the reason
  NOT_READY, and the runner reads any reason as a refusal.
- **It is still not a measurement of acceptance.** No log line names the run's token or a request id, and the answer's body was not
  kept. The request record is unreadable from this box (the table's key denies decrypt). grounding: INFERRED.

## What is established

One firm only (82 routes armed, 0 off-list admits in run 2), the identity row deleted after `exp` and read absent twice, and zero
data-refresh calls in run 3: these are the applier's measured limbs and this seat did not re-run them.

## Three rounds, three different stops at the same hop

- Round 1: the runner polled its own token, not the issued id.
- Round 2, run 2: the runner re-sent round 1's token and was refused for it.
- Round 2, run 3: the runner misread an accepted answer as a refusal and never took the issued id.

Each stop is the runner's, at hop (d). Before a fourth run, the runner's reading of the submission's answer needs a test against
a recorded real answer, with the body kept in the trace. The CTO has ruled the fourth run into round 3.
