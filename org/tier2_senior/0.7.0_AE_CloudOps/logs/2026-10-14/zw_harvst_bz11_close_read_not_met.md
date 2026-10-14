# HVST-bz-11: the close read prints CLOSE=NOT_MET -- one refresh per publisher, reported done, and the next job was refused expired again

**archetype:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~ZW` (respawned after a silent death; no kill on record) | **Box:** site Z | **Order:** `AMGT_HARVST.TO-HVST-bz-11.the-refresh-is-read-closed-for-wsj-and-barrons` (round 85, workstream REFRESH-SITEZ, `<risk>LOCAL</risk>`) | **Issuer:** `2.0.0_SA_COO~W1`

## Objective

Read, about hourly and read-only, whether the `--refresh-once` registration of `HVST-bz-10` closed row `Z-S119` for `wsj` and `barrons`, until `bz11_close_read.py` prints `CLOSE=MET` or `CLOSE=NOT_MET`.

## Current State

**The read is closed: `CLOSE=NOT_MET`, `wsj` NOT_CURED and `barrons` NOT_CURED**, at 2026-10-14T12:33:33Z. The previous twelve reads (00:40Z to 11:58Z, written by the seat before the respawn) all read `CLOSE=WAITING`; the 12:33Z read was the first taken by this instance.

Both verdicts were then checked against the two checkpoint files directly, not through the instrument:

| publisher | cycle | refresh | refusals | checkpoint |
|---|---|---|---|---|
| wsj | `20261014T121845Z` | `done` 12:28:08Z (17 s) | 2, both `class=expired` | `state/cycles/wsj/20261014T121845Z.checkpoint.json` |
| barrons | `20261014T122950Z` | `done` 12:30:24Z (16 s) | 2, both `class=expired` | `state/cycles/barrons/20261014T122950Z.checkpoint.json` |

`state` is `C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/state`. `cycle_runner.log` agrees: after each refresh the same publisher's retried job was refused `class=expired` again (wsj 12:29:46Z, barrons 12:30:43Z) with `SignInRefused: 401 under --no-sign-in: no refresh`, then `STOP <publisher>: sign_in_refused`.

The runner is untouched and healthy: it began its next bbg cycle at 12:30:43Z and a `JOB bbg` line landed at 12:34:00Z.

Filed: `bz11_reads.out` (13th entry), `bz11_AC1.out`, `bz11_AC2.out`, the proof-of-spec instance (AC1 **FAIL** recorded as the order directs, AC2 PASS; checker **VALID rc=0**, invocation-alignment 2/2, surprises 1/1 resolves under ENFORCE), and row `AMGT_HARVST-Z-S121`.

## Decisions Made

- **Stopped reading at the first closing verdict.** The order (section 2 step 3) ends the reading at `MET` or `NOT_MET`; the issuer note routes NOT_CURED to the CTO's round-85 analysis, not a re-try. No second read to see whether it recovers.
- **Re-derived the verdict from the checkpoint files** because a closing result worth filing should not rest on the one instrument that produced it. The instrument and the files agree.
- **Did not diagnose.** The log does not say what the refresh did in its 16-17 s and this seat read no session, credential or producer source. The error text is recorded verbatim in `Z-S121` and not interpreted.
- **Filed one row, OBSERVATION / INERT**, because the order says anything odd is a row; its `disarm_owner` is the issuer.

## Blockers

**None for this seat.** The cell is complete. Three items sit with the issuer:

- Route `HVST-bz-11` as NOT_MET to the CTO's round-85 analysis and disposition `Z-S119` from `Z-S121`.
- Flip `HVST-bz-10`'s and `HVST-bz-11`'s `<status>` (the issuer's, per both orders).
- `Z-S120` (the stop-file parent directory) is still undispositioned and carries forward.

## Next Steps

1. `[2.0.0_SA_COO~W1]` Disposition `Z-S121` and `Z-S119`; flip both statuses; carry `NOT_MET` into the round-85 analysis.
2. `[1.0.0_SA_CTO]` Round-85 analysis: the first question in `Z-S121`'s notes is whether the retried job can use whatever the refresh produced at all.
3. `[0.7.0_AE_CloudOps~ZW]` Nothing further on the line. Any new order arrives by the inbox watcher.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `bz11_close_read.py` | AC1's literal invocation | `CLOSE=NOT_MET`; wsj NOT_CURED, barrons NOT_CURED |
| `pytest` (`test_bz11_close_read.py`) | AC2's literal invocation | 10 passed in 1.30s |
| `proof-of-spec-check` | `<instance> AC1,AC2 --governing-order <TO>` | **VALID rc=0**, 0 violations |
| `get_agent_status` / `register_agent` / `/watcher` | respawn self-heal | lane was NOT REGISTERED; registered; one script row (pid 30148) after arming |
| `comp-schedule` / `comp-iam` / `comp-adversary` | not run | all three are L5 (the issuer) in this order's preflight; this cell made no AWS call and no write under the state dir |
| `comp-find` | not needed | every path was named in the order or read from the live log |

## Corrections made in this session

The session's first instinct on seeing `NOT_MET` thirty-five minutes after a `WAITING` read was that the instrument might be reading pre-pin records. The cut (`T0=2026-10-14T00:08:31Z`) and both cycle ids (`20261014T121845Z`, `20261014T122950Z`) are after it, so that was checked and ruled out before the result was filed.
