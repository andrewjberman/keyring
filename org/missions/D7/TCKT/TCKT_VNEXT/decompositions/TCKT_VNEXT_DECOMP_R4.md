# TCKT_VNEXT decomposition -- ROUND 4, 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_4_20261011.md`
@8d93c41f11 (msg 5101), section 4, answering the round-3 slug `ledger/L10_SLUG_R3.md` @8e1ff5192a; and CTO msg 5094 (the package
door's env-list firm bound). No PRD addendum. FWD-1 is NOT REALIZED; its break is the resident host's vendor session, outside this
project's files, so round 4's thread cell cannot be cut yet.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R4-pk-1` | the ticket service: for the package principal the package door binds the body firm to an env list `PACKAGE_ALLOWED_FIRMS` (unset or empty admits nothing; `ALL` is not a wildcard) instead of the caller's users row; and the creator branch's two uncoded refusals gain codes. Code and tests only | 1, 2 | FWD-1 | cut | dell2 worker, slot 15 | WORLD (path floor; nothing is applied) | worker | none |
| `R4-pk-2` | the apply of `R4-pk-1`'s build, under its own never-widen pair; the env list's value is the pair's to name | 1, 2 | FWD-1 | NOT-EVALUATED | ISSUER + applier seat | WORLD | -- | `R4-pk-1` |
| `R4-la-1` | the runner gains an arms-only mode: the identity, the census, hops (a)-(c), the report route's malformed-id arm and the package door's denial of the filer; NO submission is sent. Code and tests only | 3 | FWD-1 (instrument) | cut | dell2 worker, slot 16 | LOCAL by act; WORLD by path floor if a path under `infra/` is named (none is) | worker | none |
| `R4-la-2` | ONE arms-only run on DEV as the one-firm synthetic filer, under a new pair of the runner's existing shape | 3 | FWD-1 | NOT-EVALUATED | ISSUER + applier seat | WORLD | -- | `R4-la-1`; after `R4-pk-2` so the two acts never overlap on the ticket function |
| `R4-tr-1` | the FIFTH run, filed through the form's one-step path; it is also the vendor-session diagnostic request | 4 | FWD-1 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat | WORLD | -- | resident st32 installed; the CTO's word; a new pair |
| `R4-id-1` | run 4's request id and job state written into this project's result file; run 3's when IRPT_YCDGEN's reconciliation packet returns it | 5 | FWD-1 (record) | run 4's half done at this issuance; run 3's NOT-EVALUATED | ISSUER | LOCAL | -- | that packet |

**Item 6** (carried from round 1) is cut when the thread has run once, by the analysis's own words. **Section 5** (the fourteen
stale rows) is a file to `3.0.0_SA_CVO`, not a cell.

**Chains (M = 4):** {`R4-pk-1` -> `R4-pk-2`}; {`R4-la-1` -> `R4-la-2`}; {`R4-tr-1`}; {`R4-id-1`}. One ordering edge that is not a
data dependency: `R4-pk-2` before `R4-la-2` (two WORLD acts on one function). **Fan-out now: 2 workers of 4 chains, cap 8.**

**Write sets (disjoint):** `R4-pk-1`: `infra/aws/lambda/ticket_center/lambda_function.py`, its `tests/` folder. `R4-la-1`: the slot-8
runner folder `deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/`. Both grant `R4_CHECKS/r4_checks.py` for reading only in practice.

## Rule 24 record

- **MECE over the analysis's section 4.** Domain: its six numbered items. By subtraction: 1 and 2 -> `R4-pk-1` + `R4-pk-2` (the
  analysis says one build, one deploy); 3 -> `R4-la-1` + `R4-la-2`; 4 -> `R4-tr-1`, not cut; 5 -> `R4-id-1`; 6 -> not this
  issuance. Nothing of section 4 is uncovered.
- **Where item 3 cannot be met as written, stated before the cut.** The analysis asks for "the package route's codes, as the
  one-firm synthetic filer". Read by this seat (`lambda_function.py` at handler blob `dc0cd973`, `package_ticket`): the door
  denies every caller that is not the package principal BEFORE any coded 409, so the filer can only receive the denial. `R4-la-1`
  therefore exercises the door's denial of the filer, and the five codes stay unexercised until the packager's first real attach.
  Put to the CTO with the issuance.
- **Same grain:** each cell is one build or one act. **Intent:** FWD-1 and its instruments only. **State:** the vendor session is
  not moved by any cell here.

## Battery

comp-schedule, comp-iam: DECLARED-NOT-APPLICABLE for both cut cells (no schedule; no IAM; the new env key is read with a default
and is not set by the build). comp-adversary: the adversarial arms of `R4-pk-1` are its tests (a firm outside the list; an unset
list; `ALL`; a packager with a users row but no list). `R4-la-1`'s are the unexpected-answer test and the no-submission test.

Dry-run at the base (box/dell2, 2026-10-11 ~14:3xZ): pk-env FAIL absent, pk-regress FAIL (169 below 175), la-arms FAIL (missing
tests), la-regress FAIL (56 below 61), all as expected.

## Issuer record `R4-id-1`, run 4's half

Run 4: request `REQ-59aa6803901f371b27ffa176`, accepted 2026-10-11T11:19:00Z under `49financial`, job ATTENTION
`SESSION_REFRESH_ALREADY_USED` at 11:34:05Z (the host journal read by `2.0.0_SA_COO~G2`, msg 4898; not re-read by this seat).
Run 3's id: not held by this project.

## AMENDMENT 1 (2026-10-11 ~14:5xZ) -- by CTO msg 5176 (halves @0135c6f2c8)

- `R4-pk-2`: the CTO half is SIGNED for Branch E. The applier adds `PACKAGE_ALLOWED_FIRMS = ""` and nothing else; the list's value
  is named in the pair that mints the packager (IRPT_YCDGEN's). Cut as TO-APPLY-R4-pk2.
- `R4-la-2`: **NOT CUT, CLOSED BY RULING.** The CTO did not sign the run and withdrew it: with the five package codes out of
  reach it buys a 400 and a 403 that tests already cover, for an identity, a token and more leftovers under `49financial`. Both
  arms ride the fifth run (`R4-tr-1`). `R4-la-1`'s build stays merged (@bd97cf87e7) and unused by any live run; the fifth run's
  order decides whether it calls the two arms through that code or as part of the full journey.
- The analysis's item 3 reads CLOSED BY RULING. Chains now: {`R4-pk-1` -> `R4-pk-2`}; {`R4-tr-1`}; {`R4-id-1`}.

## AMENDMENT 2 (2026-10-11 ~16:0xZ) -- by CTO msg 5283 (the packager mint's CTO half @65622fbcdc, IRPT_ANLREQ's pair)

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R4-pk-3` | the SECOND apply of `opal-ticket-api`: env only, `PACKAGE_ALLOWED_FIRMS = "49financial,cottonwood,inflection"`, the value the CTO accepted in the mint's pair; no code change | 1 (its authorisation half) | FWD-1 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat, under the mint's pair | WORLD | -- | the laptop's return showing both simulates of that pair as expected (owner `2.0.0_SA_COO~G2`) |

Edge: `R4-pk-2` -> `R4-pk-3`. Rollback of `R4-pk-3` is the env key back to empty; of the build, two changes (the applier's carry).

## AMENDMENT 3 (2026-10-11 ~16:4xZ) -- by CTO msg 5327 (st32 is installed; write the fifth run's pair now)

`R4-tr-1`'s pair is written: `deliverables/2.0.0_SA_COO~V2/R4_RUN/R4_TR1_FIFTH_RUN_PAIR.md`, COO half signed ahead of its conditions.
Writing it showed the runner cannot file the form's one-step path (it claims the ticket and submits without `ticket_id`), so the
run needs one more build cell:

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R4-rn-2` | the runner gains a one-step mode: the form's four calls (upload; ticket with source `ticketcenter:i1`, no claim; ONE submission with `ticket_id` and the `tckt-` request id; the creator's record and its repeat), the two arms before the submission, at most one submission per process | 4 (its instrument) | FWD-1 (instrument) | cut | dell2 worker, slot 17, workstream RN | LOCAL | worker | none |

Edge: `R4-rn-2` -> `R4-tr-1`. `R4-tr-1` also still waits on the CTO half and on `2.0.0_SA_COO~G2`'s two reads at the GO.
Dry-run at the base: os-mode FAIL (missing tests) and os-regress FAIL (61 below 68), as expected.
