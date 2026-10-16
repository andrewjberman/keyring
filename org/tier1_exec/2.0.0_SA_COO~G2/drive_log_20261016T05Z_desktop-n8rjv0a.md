# Drive log 2026-10-16 05Z -- 2.0.0_SA_COO~G2 (IRPT_YCDGEN and IRPT_ANLREQ workstream G)

Lease: FULL on both. Keep-driving empty_tick=on. Cadence 30m (:23 and :53).

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_ANLREQ ~G | L6/L7 and the two release legs | 31 to 33 | R31 AR-g-113 merged, AR-g-114 read done; R32 AR-g-115 merged, apply AR-g-117 with AQ2; R33 AR-g-116 merged | R31 2/2, R32 2/2, R33 1/1 | n (run 3 waits on the library and the re-applied r34) | DRIVE FORWARD |
| IRPT_YCDGEN | engine release train (see ANLREQ ~G) | -- | -- | -- | n | none own |

Acts this window (05Z):
1. r34 rolled back (CTO msg 9070): AQ2 ran step 9, read r32 back green twice (msg 9085), ledger ROLLED-BACK; order marked superseded. AQ2's read-only host facts (msg 9090): x86_64, CPython 3.12.14, glibc 2.34, pip 23.2.1, 22 pydeps distributions.
2. Library delivery (CTO msgs 9070, 9075): cross-box call XB-20261016T052534Z-983c to `~C` (committed and sent by MSTR~DELL2, acked); the laptop CTO accepted (yes, wheels only, no S3 upload, Taildrop to dell2); MSTR~DELL2 collects into C:/opal-intake/inbound/yfinance-linux-cp312/. Nothing requested or fetched yet.
3. irpt-status failure-code release (r35L): AR-g-113 (map re-pin) and AR-g-115 (build, worker 255, 49 members, delta exactly durable_job.py/owned_status.py/status.py) merged and re-verified; packet R35L signed by the CTO (msg 9106); AQ2 order TO-APPLY-R35L sent with GO (not yet reported).
4. r34 re-apply plan: tooling folds the hop_failure resident writers in (pin c43f8fc13a, new ledger name r34b), AR-g-116 (worker 256) merged and re-verified, packet R34C (blob db596c0725) sent to the CTO for re-sign; it requires the library first.

Waiting on: AQ2 (r35L), CTO (r34C re-sign), `~C` (closure list), MSTR (Taildrop). Next: library packet and AQ2 install order when the list is approved; AQ2 order for the re-applied r34 after the library; tell `~Y2` at each timing change.
Messages acked: 9102, 9106, 9109 and earlier.
