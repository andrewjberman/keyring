# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 23:1xZ - 2026-10-04 00:2xZ (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 23:2xZ-23:3xZ | DSGN_IRPTV1 (FAST) | does the Analysis tab show REQ-51d9daac's ATTENTION | read-only walk `20261003T232315Z`: the row reads its status after a 7-8 s read (the driver's flat 3 s wait read "loading"); the opened request read a bare "Job status: Unavailable" (route: UNAVAILABLE / ANALYSIS_REQUIRES_ATTENTION) | DRIVE FORWARD (defect found) |
| 23:4xZ-00:1xZ | DSGN_IRPTV1 (FAST) | the opened request's status words | the dialog words its reason code as the row does; pin request-dialog-attention, DEV fails (a); walk `20261004T001153Z` reads "Job status: Unavailable — needs attention"; LANDED portal DEV `37765a14` (ls-remote); pin handed to the CVO | DRIVE FORWARD |
| 00:1xZ | DSGN_IRPTV1 Y-H driver | yh-submit-case.mjs | waits up to 30 s for the row's status read; stops on ATTENTION and on a refused row read; CLOUD `4112d1ab8d` | DRIVE FORWARD |
| 00:2xZ | DSGN_IRPTV1 | the receipt poll's bound | 40 reads at 1.5 s, about 90 s measured, against a 49 s render: no change; closed in STATUS | NO-OP (measured) |
| 00:2xZ | DSGN_REBRND W3-S5 | IR-REQUEST-FAILED on /investor-reporting | the named render now draws one designed error panel (ui-smoke `--fail directory/resolve`, looked at); the residue (StatusPanel's verbatim code) is CTO ruling T: parked with the CTO | NO-OP (narrowed, parked) |

## Notes

- Site Z holds the UI-walker account from 00:18Z (0.0.0_AB_MSTR 104823); this seat does not arm until DISARMED is
  relayed. Every walk this hour sent ARM and DISARMED.

## Open

- The print's bundle reference on the face: put to Andrew.
- Aproxy re-fires on 2.0.0_SA_COO~Y's served pin (104811).
- W3-S5: bare spinners and "Loading..." lines; /data-refresh's amber band; the demo page's silver copy.
