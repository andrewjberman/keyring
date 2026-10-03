# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 21:3xZ-23:0xZ (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 21:3xZ | DSGN_REBRND W3-S5 (FAST) | /philosophy Views spun forever on a failed read | ERROR / LOADING / EMPTY states; committed `fb73cb1c`, held under 0.0.0_AB_MSTR's freeze 104776 | DRIVE FORWARD (held) |
| 21:4xZ-21:5xZ | DSGN_REBRND W3-S5 (FAST) | raw JSON bodies in Cause lines | `innermostCause` gives a body's own words; real run /valuations with a forced 503 JSON body, CONTROL build of DEV's cause.ts shows the raw body; committed `3e526a44`, held | DRIVE FORWARD (held) |
| 22:0xZ | both (FAST) | the three held commits | PROMOTED arrived (104785, PROD dbd29c63, deploy run 37156394008 SUCCESS); merged DEV forward, typecheck rc=0; LANDED portal DEV `822ce891` (ls-remote) | DRIVE FORWARD |
| 22:1xZ | P-2 leg R1/V (~P 104788) | export ****0090 on PROD with S311 | one press 22:12:52Z: receipt exr_5f3c0b757a054bffbe31b431 READY in 49 s, frozen as_of 2026-10-01; ~P read it server-side and CLOSED legs R1, R2, S, V (104808, @33e9aba113) | DRIVE FORWARD (closed) |
| 22:2xZ | IRPT_BCKEND Y-5 (~Y 104798) | Aproxy re-fire after the finding-value fix | run 1: no write (search text matched the firm list); run 2: correction re-post NORMALIZED, submit REQ-51d9daacbc9ba24ac01b6c4c RECEIVED; server ATTENTION VENDOR_UPLOAD_REFUSED (~Y: the page half passed; backend cause is ~Y's; re-fires held) | DRIVE FORWARD (routed) |
| 22:4xZ-23:0xZ | DSGN_IRPTV1 (FAST) | the export preview's "not supplied" firm chip | cause: `index.tsx` passed `scope={null}` and ExportButton passed Preview no scope; fixed and pinned (DEV fails all three arms); signed-in `--no-export` walk reads "49 Financial"; LANDED portal DEV `46194eed` (ls-remote); four pins handed to the CVO | DRIVE FORWARD |

## Notes

- This seat's 10-minute background shell timeout killed the Aproxy driver while it waited for READY, so its `finally`
  disarm never ran. The account read active at 22:38Z; it was disarmed by hand for that holder at 22:39:13Z and
  0.0.0_AB_MSTR was told. The next walk ran in the foreground under a 9-minute `timeout`, below the shell's limit.
- Git Bash rewrites a `--fail /api/` argument into a Windows path; ui-smoke then matches nothing. Use a plain substring.

## Open

- The Analysis row read "loading" for 8 minutes while REQ-51d9daac was ATTENTION server-side from 22:28:59Z: check
  whether the page shows ATTENTION (this seat).
- The print's bundle reference on the face: put to Andrew.
- The receipt poll's bound: the measured render took 49 s.
- Aproxy re-fires on ~Y's served pin.
