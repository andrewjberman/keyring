# NFRA_TRNSPT -- ROUND ANALYSIS, round 3 (the FAST round of 2026-10-01/02)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~14:4xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. The project was placed on dell2 whole
(laptop `1.0.0_SA_CTO` msgs 106273/106287, relayed by `0.0.0_AB_MSTR~DELL2` msg 669); the COO lane is `2.0.0_SA_COO~T2`.

**Input:** the FAST round's record `org/missions/D9/NFRA/NFRA_TRNSPT/STATUS.md` (seat `2.0.0_SA_COO~D`, wound down
2026-10-02T04:0xZ), and `~T2`'s measurement (msg 678). There is no CVO slug: in FAST mode `3.0.0_SA_CVO` grades landed pins after
the fact, and that grade has not been written. It rides round 4's compile and does not hold this analysis.

## 1. Accepted from the FAST round

Eight landings (STATUS.md "Landed this round", items 1-8). In short:
- the laptop caller and bronze;
- the real run;
- the listing route's order, released by site Z and checked 4 of 4;
- the wipe's stated limits inside the silver file (row W4-S8's remedy, review Q2);
- the unattended pull over the listing;
- admitted-only landing;
- the positive arm by a seat's command;
- the daily schedule, applied 9/0/0 and closed 3 of 3.

Rows S13 and S14 are met as STATUS.md reads them. S9 and W4-S8 are graded by the CVO at round 4's compile.

## 2. FWD-7 -- the schedule fires; it has filed nothing new

Measured this session from dell2, function `outlook-global-transcripts-pull-lambda`:
- **CloudWatch Lambda metrics:** 6 invocations from 2026-10-02 to 10-06 (the 04:04Z QA invoke plus 5 scheduled fires), 0 errors.
- **REPORT lines:** 6, durations 12.0 to 20.9 s.
- **`~T2`'s key census:** 0 `outlook` objects landed since 10-02 (24 in total).

The ordinary daily run therefore starts with no person, five times out of five, and every one of those days landed nothing. That is the
**negative arm**, proven five times. DONE WHEN (a real feedback email filed by the ordinary daily run, no person starting it) is NOT
met.

**No FWD is a wait** (rule 27 L2). The CRO measured roughly 6 to 18 admitted emails in eleven months, so the organic case may take
weeks. The positive arm is therefore DRIVEN:
- The named admitted message (2026-08-11, row S9) is still outside bronze.
- The scheduled function, on its own clock, is given a window that reaches it ONCE.
- That fire lands it with no seat starting it.
- The window then returns to 7 days.

An organic arrival grades the same outcome again whenever it happens. Neither arm is a person sending mail.

## 3. The store is not read from dell2 (laptop ruling A, msg 669)

`cloudops-dell2-agent-user` is refused `kms:Decrypt` on the transcripts key (`~T2` msg 678), and the laptop rules it stays that way.
- Every read of `run.json`, `silver.json` or silver parquet is a FILE from the laptop, through the fenced-read path:
  1. a row;
  2. a committed read-only script that prints counts only;
  3. a relay through `0.0.0_AB_MSTR~DELL2`;
  4. the FILE back.
- Item C2 below removes most of that traffic: a fire is graded from its own log, which holds counts and nothing else.

## 4. ENRICHMENT -- round 4, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| C1 | **The scheduled function reaches past 31 days by spans.** `mail_handler.py` accepts a window of up to 120 days and lists it as spans of at most 31 days, as `pull.py --gateway` already does. Default unchanged at 7 | (1) a fake-route test: a 120-day window issues spans of at most 31 days covering every day once, and a message already in bronze is skipped (the existing sidecar rule); (2) a window over 120 or under 1 raises, as today; (3) the bundle import check passes on the deployed layout | LOCAL |
| C2 | **The fire states what it did, in its own log.** The handler prints ONE line per fire: `MAIL-PULL-FIRE run=<id> window_days=<n> listed=<n> admitted=<n> landed=<n> skipped_known=<n> list_refusals=<n> silver_rows=<n> held_out=<n>`. No sender, address, subject, name or id beyond `run=` | (1) a fake-route test asserts the line's exact field set, and a control that a planted sender address in the fake never appears in captured stdout; (2) the suite passes | LOCAL |
| C3 | **The driven positive arm (FWD-7)**, after C1 and C2 are applied under the project's ledger: the function's window is set by configuration to reach 2026-08-11 for ONE scheduled fire, then returned to 7 | (1) that fire's log line reads `landed>=1` and the invocation is the schedule's (EventBridge), not a manual invoke; (2) a laptop FILE (fenced read) shows the bronze objects' hashes equal their sidecar's and the silver row's `held_out` state, counts only; (3) the window reads 7 at the next fire's log line | SERVED |
| T1 | **The transcripts route, measured (FWD-1 hops 1-2).** From NFRA_OPLGTW's release record and gate G-TEAMS-TX: is `/hx/transcripts` released, and does Andrew's tenant setting allow attributed transcripts | (1) one record naming route state (released at a commit, or not) and G-TEAMS-TX state, each with its source line; no gateway call from dell2 | LOCAL |

The apply in C3 is a served move with the CTO and COO halves. Each half names:
- the function's environment as the one key;
- a rollback to `WINDOW_DAYS=7`;
- both branches: the fire lands the message, or it lands nothing, and then the criterion is listed. Bronze already holding it is
  not this branch, because it is not there today.

Which machine applies the change is the COO's L6 call, under the rule that a Dell writes no Lambda permission.

## 5. Placed with others (one line each, owner and condition)

- **The placement record:** `project.json` and the four-box record still read SITEZ / laptop. The laptop holds placement (C-ROLES),
  so its carrier is the laptop's; asked through `0.0.0_AB_MSTR~DELL2`.
- **The 14 flagged words of the first real row:** Andrew, as a named reader. The row stays held out, which is the safe side.
- **Row S11, the fourth meeting type:** a calendar invitation, already ruled in NFRA_OPLGTW (reached by invitation).
- **FWD-8's second named reader:** has no AWS principal. Andrew names it.
- **Kimi K3 (FWD-10):** Andrew's word travels with the project, scope unchanged (laptop ruling B). No call before C-WIPE-GATE.

## 6. Outcome read

FWD-2 and FWD-5 are realized for three of four meeting types. FWD-7 is applied and its negative arm exercised 5 times, but it is
not realized. FWD-1 waits on T1's answer. FWD-3, 4, 6 and 8 to 11 have not been started. The project is REACHABLE.

-- 1.0.0_SA_CTO~DELL2
