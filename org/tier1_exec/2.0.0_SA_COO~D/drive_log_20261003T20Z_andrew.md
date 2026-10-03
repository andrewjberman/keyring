# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 19:4xZ-20Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 19:4xZ-19:5xZ | DSGN_IRPTV1 (FAST) | V walk defect 4 | PATH A skip for an account PATH B already serves, LANDED portal `557862f1` | DRIVE FORWARD |
| 19:5xZ | IRPT_BCKEND S307 (~P 104713) | stop check | one tab load: ****0090's reporting GETs 200 (19:55:57.885Z, 19:55:58.431Z); ~P cleared the stop | DRIVE FORWARD |
| 19:5xZ-20:0xZ | DSGN_IRPTV1 (FAST) | defect 4 real run | send times measured: both PATH A GETs leave before the PATH B answer (first-load race) | DRIVE FORWARD (limit recorded) |
| 20:0xZ | P-2 window leg V, P1 (~P 104718) | the export re-walk | export ACCEPTED, receipt exr_07fe19290b7846e39a6afa0a, still RENDERING through 20:04:11Z; ~P asked for the final state | DRIVE FORWARD |
| 20:0xZ-20:1xZ | DSGN_IRPTV1 (FAST) | defect 5, found by P1 | the receipt poll counts every read, LANDED portal `49d0a98a` | DRIVE FORWARD |

## Notes

- Defect 4's first report claimed a fix the live walk did not show. The netlog stamps an ANSWER's arrival, so a request
  sent earlier reads as later. With send times logged, the race is measured. The CVO was handed the pin with that limit
  named.
- The UI-walker was armed and disarmed four times this hour. Each time 0.0.0_AB_MSTR was sent ARM before and DISARMED
  after, and each disarm proved the login refused.
- The V driver gained `--tab-only`, `--no-export`, request send times, and the export id and frozen as_of read from the
  answers (ids and dates only, never a body).

## Open

- P1's receipt: final state and frozen as_of. ~P reads it server-side; it closes leg V and S307.
- The receipt poll's bound (about 90 s) against the measured render time.
- The print face: the bundle reference on the face (put to Andrew) and the "not supplied" chip (to trace).
