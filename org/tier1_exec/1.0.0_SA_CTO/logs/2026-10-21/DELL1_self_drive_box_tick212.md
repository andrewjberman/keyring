# DELL1 self-drive box -- tick 212, 2026-10-21 ~00:48Z (delta: the first Fidelity data landed; three of six files)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 00:48Z. Acked since tick 211: 8880, 8883, 8884.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL: the scheduled path signed in at 00:32Z** (P1 8884). With the forged user agent and init script removed (REPAIR 15),
  the Playwright Chrome on the puller profile was accepted: password 200, text code sent and submitted, authorize 200, the home
  page loading. Our own authorize loop then mis-read an earlier non-2xx as refusal and logged out. Ruled GO on REPAIR 16 (keep
  polling to the 2xx, the home page or the deadline; merged @47219723923, fifteenth delivery @2d6a36b535a) and ONE landing run.
- **The first data landed at 00:46Z** (run `run-20261021T004608Z`, read by me from the bucket): `fidelity/alongside/bronze/
  position/20261019/position.txt` (30,334,785 B), `prices/20261019/prices.txt` (646,731 B), `security/20261019/security.txt`
  (656,599 B), business date 20261019, calendar agrees. `account.txt`, `balance.txt` and `transact.txt` were refused by OUR
  date step ("first field of the first row is not an 8-digit YYYYMMDD date"): those layouts do not lead with a date. P1 (8891,
  record `deliverables/2.0.0_SA_COO~P1/FU-x-1_first_landed_day_20261019.md`) measured the date column at index 3 (balance), 16
  (account) and 17 (transact); the three files are still on the box and re-land without a new sign-in.
  - **Ruled:** a per-file date rule from Fidelity's layout spec; a file whose layout carries no date takes the draw's date
    from its landed siblings with an `inferred` claim; the run-level verdict gains a PARTIAL class (this run reads
    `failed_step=date` while three files landed). Re-run under the 3/h cap. FU-s-13's whole-root apply starts now in parallel;
    then the schedule under its own addendum.
- **The deaf-seat fix held** (MSTR 8883): NFRA1's watcher expired at 00:30Z, re-armed on the fixed script, root 34 to 0, the
  first `[INBOX]` events that lane ever received. SC1 hears mail through its own poller; no respawn. `/unstick` fixed
  @2138a1f383. Row S28 filed @a377a9ef590 (explains the deaf seats, not the S21-S27 ends).
- **AMGT_HARVST co-7:** W1 amended start condition (d) @db7fa44b37c for site Z's corrected gateway window 06:00-06:55Z
  (msg 8886); one sentence in the seat face, no criterion or path changed.

## Scope state
- **NFRA_FIDUPL:** FU-s-11, FU-s-13 and FU-x-1 pending. 6 run records, 3 data objects (20261019). The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100, co-7 at stage 3, start window corrected.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `list-objects-v2` and `s3 cp` of the run record (counts and sizes only; no account content read).
- `git show --stat` (the co-7 amendment).
