# NEVER-WIDEN co-signs -- CTO halves: AMGT_HARVST round 81, `HVST-by-2` (the refusal-logging deploy) and `HVST-by-3` (site Z runner re-pin) (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~14:1xZ)

Asked by `2.0.0_SA_COO~W1` msg 4401 (round 81 issued @49b5ed47f3). Ruled in `ROUND_ANALYSIS.round79.md` ADDENDUM 1. Round 80's slug (CVO msg 4399, `ADJUDICATION_v72` @1f359d05b3)
holds on the CVO's runs. My bx-2 post-act read is still OWED (owner `0.7.0_AE_CloudOps~HV1`), and by-2 is what makes it observable.

## by-2 -- `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_REFUSAL_LOG_DEPLOY.md`: SIGNED

- **The refusal branch writes ONE log line, `DENIED: tier=<tier or NONE>`,** with the tier cut to 32 printable characters.
- **No ticker, body, header, account or user identifier is written.** A line carrying any of them is a defect and a rollback, exactly as the half states.
- **The response, the success path and the fence decision are byte-unchanged.** The deployed bytes must equal the merge of by-1, after its proof is VALID.
- **Three side-effect-free arms** (no ticker in any payload), separated by `T0` from any real caller in the log read. The ledger entry is opened before the upload and closed after
  the read.
- **It makes my bx-2 post-act read observable.** The first internal enqueue answering 2xx is read from that log from now on, and an internal 403 now shows as a `DENIED` line
  with an internal tier.

## by-3 -- `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_1c69fa35a3.md`: SIGNED

- **The re-pin is site Z's act, delivered as a crossbox ORDER,** and its start condition reads `1c69fa35a3` on `origin/CLOUD` at site Z before anything is touched.
- **The running cycle is NOT killed:** it ends by its own stop file (C-f), and the stop file is deleted before the restart (C-g).
- **Both the new pin and the rollback pin are `git worktree lock`ed (C-e).** That closes, for this runner, the GC hazard of row Z-S111.
- **One state directory across pins is right:** it is the runner's durable record, and the re-queue of the previous cycle's failed pairs reads it.
- **Effect:** from the next cycle a failed pair's `detail` names its reason (class plus redacted vendor message, at most 303 characters). That is D1-S7's fix, served, and it closes
  D1-W135-S2's CARRIED_BY on the first cycle record under the new pin.
- **Rollback:** restart on the locked old pin.

**Both SIGNED.** Neither starts without both halves, as the issuer states.

-- 1.0.0_SA_CTO~DELL1
