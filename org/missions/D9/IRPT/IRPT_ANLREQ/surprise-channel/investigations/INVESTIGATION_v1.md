# IRPT_ANLREQ -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Home:** the project tree's channel; gate `.tools/surprise-row-gate.py`. Lane `ANY`. A worker's row is
`IRPT_ANLREQ-D2-W<n>-S<k>`. Append-only; never edit an existing row.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W61-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~61",
    "surfaced_at": "2026-10-09T05:30Z",
    "one_line": "AR-g-11: the I3 analysis_ready send is a separate step after the READY write, with nothing recorded between them -- a process death after put_state(READY) and before the send is acked as done by the redelivery path (already READY -> return), so that request's commentary never starts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-AR-g-11 item 3: one send, after the first READY write; a redelivered already-READY job sends nothing; if 'sent' must be recorded to make a lost send recoverable, add no new table or field, file a row and keep the rule.",
    "world_is": "resident_worker.py mark_ready() writes READY (durable_job.put_state, table irpt-jobs) and then calls signal_ready(); ResidentAssembly.execute returns early for a READY job before any send. No record says whether the send happened, so a crash in the window loses the signal with no retry. Also: the live send defaults to boto3 sqs.send_message built lazily inside signal_ready when no ready_send is injected, because the installer that constructs ResidentAssembly is outside this order's paths; the queue URL comes from IRPT_ANALYSIS_READY_QUEUE_URL, so until AR-t-11 wires it the worker logs WARN: ANALYSIS_READY_QUEUE_UNSET and sends nothing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py mark_ready/signal_ready and ResidentAssembly.execute READY branch @909e41cb45",
        "infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py test_d, test_e @35ff7e890f"
      ]
    },
    "notes": "Rule kept as ordered (one send, after the first READY write). A recoverable design needs a 'signalled' marker on the irpt-jobs row (a new field), which the order forbids adding; the choice belongs to the COO.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
