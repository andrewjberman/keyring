# Hop-3 proof window -- interim findings, reported first (packet outcome table rows 2 and 5)

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~06:3xZ. Packet `HOP3_PROOF/WINDOW_PACKET_HOP3_PROOF_20261002.md` (blob `3b3d4bc0c3`),
CTO half batch 119. Ledger `irpt-hop3-proof-20261002`. Leg A's job is NOT terminal at this writing; nothing further is
posted, signed in or redriven by this seat. Journal: `JOURNAL_LEG_B_20261002.txt` (SSM `75762749`, read-only).

## Timeline (resident journal, st10 root `b1db201025-st10`, UTC)

| time | line | whose |
|---|---|---|
| 06:24:58 | leg P: `PROBE_VERDICT=LIVE` (one GET, status 200 JSON, `set_cookie_count` 1) | probe |
| 06:26:02 | `IRPT_RESIDENT_RESOLVE state=READY` | A's upload |
| 06:26:09 | `IRPT_RESIDENT_EVICTION verdict=EVICTED job=REQ-93441e4e201b40e3b119c46b` | A's job, first request |
| 06:26:18 | `IRPT_RESIDENT_VENDOR_REQUESTS kept=1` | A's job (item 16, first live line) |
| 06:26:18 | `IRPT_RESIDENT_POLL retained_for_retry class=OperationRefused code=CAPTURE_FAILED:UNEXPECTED_CHALLENGE:CHALLENGE_CAPTCHA_UNSUPPORTED` | A's job: the resident's one refresh |
| 06:27:01-04 | leg B's gate: A's job reads `SUBMITTING` | runner |
| 06:27:14 | leg B K4 POST 200, `RESOLVING`, upload `UP-d3b01928..` | B |
| 06:27:16, 06:28:16, 06:29:16 | `IRPT_RESIDENT_RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY` | B |
| 06:30:17 | `IRPT_RESIDENT_RESOLVE state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED` | B |
| 06:30:22 | after leg B: A's job reads `SUBMITTING` | runner |

B's normalization row: `NEEDS_CORRECTION`, reason `RESOLVE_RETRY_EXHAUSTED`, dispatched 1790922436, resolved 1790922617
(181 s), one ERROR finding with actions `[REPLACE_FILE]`.

## Finding 1 -- hop 3 is NOT closed on st10, and the mechanism is now named

The upload resolved while A's job was live and exhausted its four receives, each refused
`PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY`. The sessionless lookup (batch 72 item 12, st7) removed the SESSION from the
lookup but not the provider OPERATION LEASE: while A's job holds the lease, each receive is refused busy, 60 s apart, and the
fourth ends the upload. Rows S206 and S215 measured the effect; this is its cause by the journal's own class. The file is
exonerated again (the same CSV resolved READY at 06:26:02 with nothing in flight), and `REPLACE_FILE` is again the wrong
remedy shown to the user.

Remedy candidates, for `1.0.0_SA_CTO` (S215's open P2): (a) a receive refused `OPERATION_BUSY` does not count against the
four-receive bound, and is released for the lease's own retry-after; (b) the sessionless lookup does not take the account
operation lease (it reaches no account state); (c) the resolve is held until no job is non-terminal. Recommendation: (a),
since it keeps the lease's spacing, with (b) only if the lease's purpose is read as account mutation alone.

## Finding 2 -- leg A was EVICTED 71 s after leg P read LIVE, and the resident's own sign-in met a CAPTCHA (row S230)

The session leg P read LIVE at 06:24:58 was displaced by 06:26:09 (A's first request). The resident took its one refresh and
the capture failed `CHALLENGE_CAPTCHA_UNSUPPORTED`: st7's reason token names row S230's cause for the first time (the vendor
answers the resident's own sign-in with a CAPTCHA). NOT MEASURED, a hypothesis only: leg P's GET drew `set_cookie_count` 1,
and if that reply rotated the session the stored copy was stale for A. The job's message is retained for retry with its one
refresh used; under the packet no sign-in is made and nothing is redriven. Its next receive is the job's own.

## What stands

- Item 16 ran live: `VENDOR_REQUESTS kept=1` on A's first receive (its record is compared with the requests made at A's end).
- Item 15's `WAF_READ` line did not occur (no read was challenged; the challenge was at sign-in).
- Leg A's runner waits for the job to be terminal or its 60-minute deadline (stop 5).
