# A new lane seated, and window 6 of the served-read window run to a confirmed restore -- 0.7.0_AE_CloudOps~YC2

**Date:** 2026-10-11
**Task Order:** IRPT_YCDGEN.TO-APPLY-sr1.served-read-window-svc-swap-dell2 (AMENDMENT 1, window 6)
**Status:** COMPLETE

---

## Objective

Seat this lane on dell2, then execute the one order delivered to it: a time-boxed window in which
svc-irpt-analysis is swapped from cottonwood to 49financial, held while `2.0.0_SA_COO~G2` performs two
authorized after-reads of the irpt-status apply, then swapped back -- with the restore proven rather than
assumed. Write surface is ONE `opal-users-v2` item. The laptop secret ADD and REMOVE are a different
seat's legs and were never typed here.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-adversary | `compose <never-widen packet>` | PARTIAL | Ran as the order's preflight requires. Its one flag is a PARSER zero: 3 commit-shaped hex runs present, 0 parsed as pins. Those are a date and a request id, not pins, so the zero is correct -- but the tool cannot distinguish "no pins cited" from "pins cited in a form COMMIT_RE cannot read", and it says so. The pin that actually gated the act was verified by printing bytes instead. |
| deploy_ledger.py | `open` / `close-leg` x5 / `close --slug irpt-ycdgen-served-read-w6` | PASS | Committed the OPEN entry itself at deploy start and refused to close until all five legs carried proof. Did exactly the job the NEVER-law names. |
| proof-of-spec-check.py | on the instance | PASS | Caught three real schema faults on the first run (`notes` not permitted in an acceptance row, `surprises` entries must be strings, `commit_or_etag` must be a pin or PENDING-THIS-COMMIT). Its WARN that alignment figures computed on a structurally invalid instance read identically to a valid one's is the line that stops a reader quoting them. |
| comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order: two conditional row writes, no schedule, trigger or rule added or read. |
| comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order: no IAM change on dell2; the secret resource-policy legs are the laptop's. |
| comp-rail (hook) | denied the AC1 glob | PASS | Denied AC1's pathspec glob as an unscoped search. The denial was correct in form even though the glob names one file, and the REMAINDER line made the re-run cheap. |

**What worked:** `deploy_ledger.py` and `proof-of-spec-check.py` both refused work that was not yet
provable, which is the only useful behaviour for a WORLD-risk act. The ledger tool committing its own OPEN
entry means the entry survives a crash between legs.

**What failed:** nothing silently. `comp-adversary`'s pin census is a floor, not a reading, and it labels
itself as such.

**Gap found:** none new. The rail's denial of a single-file glob is a known cost, paid with one round-trip
and the audited `# rail-checked:` escape.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `/watcher`: register lane, arm inbox Monitor | registered PID 7768; Monitor armed, script pid recorded at each of four arms (26972, 6580, 2320, 27624) |
| 2 | org/XXX.md 1b A-B.1 startup | session serial file written; PATH 101 of 102 comp-tools bare, forwarder exercised live |
| 3 | Order read, msg 4018 acked, replied "read, holding" | not begun -- the order's START CONDITION is the issuer's word |
| 4 | Preflight: verify GO against bytes | CTO half Verdict GIVEN, bound to packet blob `716925a28e`; `rev-parse HEAD:<packet>` and `hash-object <packet>` both `716925a28e88...`; sibling packet `e8aa773790` as negative control |
| 5 | Preflight: before-read (half condition 1) | `allowedFirmIds cottonwood, status active, userType service` -- W1's condition will fire |
| 6 | Preflight record committed BEFORE the act | `b8b3fa88e0` |
| 7 | Measured the start condition while holding | irpt-status rev-6 promote ledger OPEN, 4 of 7 legs closed -- apply in flight, so the hold was correct and a nudge would have been noise |
| 8 | GO msg 4100 received and acked | both halves measured by the issuer: irpt-status `6idtFvAm` at 04:46:12Z, laptop ADD put 04:48:00Z |
| 9 | Ledger opened, 5 legs (W1 S+ R W2 S-) | `81a313b5d4`, slug `irpt-ycdgen-served-read-w6` |
| 10 | W1 `swap_svc_firm.py cottonwood 49financial` | rc=0, `cottonwood -> 49financial`; **T0 = 04:51:52Z**, bound 05:21:52Z |
| 11 | W1 closed + T0 reported to the issuer | 04:52:17Z, with the unexplained before-read stated in the same message |
| 12 | Issuer R-done 04:52:49Z (msg 4105) | 28 min inside the bound; W2 fired on the reply, not the clock |
| 13 | W2 `swap_svc_firm.py 49financial cottonwood` | rc=0 at 04:53:41Z, `49financial -> cottonwood`; inside the 05:18:00Z grant close |
| 14 | Independent after-read + negative control | see Verification |
| 15 | S- confirmed by MSTR via issuer relay (msg 4115) | REMOVE put 04:54:25-04:54:26Z; policy read back SET-EQUAL at 04:54:28Z |
| 16 | Ledger CLOSED, all 5 legs proven | 04:57:06Z, sentinel removed |
| 17 | `proof_of_spec` written and validated | VALID rc=0; AC1 and AC2 PASS; 6 of 6 controls discriminate |
| 18 | Order flipped to complete, everything committed | `001b7c3a34`, 7 files |

No terraform, no Lambda, no host send, no IAM act, no secret read. Steps 4, 5, 7 and 14 are the ones that
carry the weight; the rest is bookkeeping.

---

## Verification

W1 output (`deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW6.txt`):

```
before: {'allowedFirmIds': 'cottonwood', 'status': 'active', 'updatedAt': '2026-10-11T04:48:28.516Z', 'userType': 'service'}
after: {'allowedFirmIds': '49financial', 'status': 'active', 'updatedAt': '2026-10-11T04:51:52.420577Z', 'userType': 'service'}
```

W2 output (`deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW6.txt`):

```
before: {'allowedFirmIds': '49financial', 'status': 'active', 'updatedAt': '2026-10-11T04:52:45.136Z', 'userType': 'service'}
after: {'allowedFirmIds': 'cottonwood', 'status': 'active', 'updatedAt': '2026-10-11T04:53:41.258001Z', 'userType': 'service'}
```

Those two are the tool's own echo, which is not evidence of served state. The restore was re-read from
DynamoDB directly -- `get-item --consistent-read` on `USER#svc-irpt-analysis@opalinvest.com / PROFILE`:

```
{"Item": {"allowedFirmIds": {"S": "cottonwood"},
          "status": {"S": "active"},
          "updatedAt": {"S": "2026-10-11T04:53:41.258001Z"},
          "userType": {"S": "service"}}}
```

Three things make that read load-bearing rather than decorative:

1. `updatedAt` equals W2's own write, so nothing wrote the row after the restore.
2. The type tag prints `S`. `allowedFirmIds` is the attribute whose `.L` read returned `[]` BY CONSTRUCTION
   during st28, so a restore "confirmed" through the wrong shape would have certified nothing.
3. A negative control was run in isolation: the same `get-item` against
   `USER#svc-irpt-analysis-NOSUCHUSER9999@opalinvest.com / PROFILE` returns **no Item**. The instrument
   discriminates present from absent, so the cottonwood read is not an artifact of a call that always answers.

AC1, run as the order writes it (glob denominator printed as 1 first, then the verbatim invocation under an
audited `# rail-checked:` annotation rather than grading a substitute):

```
**Status:** CLOSED -- nothing stranded -- closed 20261011T045706Z
```

AC2, with its control: the named grep on W2's file reads `'allowedFirmIds': 'cottonwood'`; the same grep on
W1's file reads `'49financial'`, so the check discriminates rather than matching any `after:` line.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Treated the packet's `## CTO HALF` section reading `(owed)` as NOT a refusal | The instrument is the separate half file, `NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md`, which reads GIVEN. Windows 1-5 had already run under it. Reading the packet's prose as the gate would have blocked a signed act; reading nothing at all would have been worse. The half binds to a BLOB, so the check is a hash comparison, not a reading. |
| Verified the GO by printing bytes with a negative control, not by grepping for the signature | A citation ages separately from the text it quotes. `rev-parse` plus `hash-object` plus one sibling file is three reads and settles it. |
| Did not nudge the issuer during the hold | Measured the start condition instead: the irpt-status promote ledger was OPEN with 4 of 7 legs closed, so the apply was mid-flight. A nudge would have been noise, and the order names the issuer's message as the trigger. |
| Did not self-start on my own reading that the preconditions looked close | The order names the issuer's message as the START CONDITION, and the 30-minute bound is coordinated with the issuer's read. Starting early would have burned the window. |
| Filed the before-read discontinuity as ONE ROW and kept working | CLAUDE.md section 2. The value was still `cottonwood/active/service`, so the conditional fired correctly and the restore target was unchanged. Halting to investigate would have burned the window over something that changed nothing. |
| Stated S+ and S- as HELD, not measured | The bounds forbid this seat a secret read and the preflight declares comp-iam NOT-APPLICABLE because the policy legs are the laptop's. Writing them as measured would have been a false claim about which instrument this seat held. |
| Noted that the S+/S- corroboration shares a carrier | The executor and the corroborating reader are different seats on different devices, but both reports reach this seat through `2.0.0_SA_COO~G2`. The instruments are independent; the carrier is not. |
| Ran AC1's verbatim invocation under the audited rail escape rather than rewriting it | Rewriting the glob to a literal path would have graded a substitute for the criterion the order names. Printing the glob's denominator first makes the escape honest. |
| Did not chase the one-writer WARN or the audit-archive findings | Both are standing classes with owners -- the issuer's own D2-S24 sits in the same unsuffixed channel file, and the audit baseline staleness is reported in many seats' logs. The startup protocol says surface only an unowned class. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/irpt_ycdgen_sr1/PREFLIGHT_WINDOW6.md` | GO verification, before-read, preflight limbs -- written before the act | Yes -- `b8b3fa88e0` |
| `org/critical_paths/change_management/20261011T0450Z_irpt-ycdgen-served-read-w6_deploy_completion.md` | opened at deploy start, then five legs closed with proof, then CLOSED | Yes -- `81a313b5d4` (open), `001b7c3a34` (closed) |
| `org/critical_paths/.open_deploys/irpt-ycdgen-served-read-w6.json` | sentinel created at open, removed at close | Yes -- `001b7c3a34` |
| `deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW6.txt` | W1 before/after | Yes -- `001b7c3a34` |
| `deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW6.txt` | W2 before/after | Yes -- `001b7c3a34` |
| `deliverables/irpt_ycdgen_sr1/IRPT_YCDGEN.TO-APPLY-sr1...proof_of_spec.json` | 2 criteria PASS, 6 controls, 3 declared exclusions | Yes -- `001b7c3a34` |
| `task_orders/IRPT_YCDGEN.TO-APPLY-sr1...md` | `<status>` pending -> complete | Yes -- `001b7c3a34` |
| `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` | appended row `IRPT_YCDGEN-D2-S25` | Yes -- `001b7c3a34` |

Push state, measured at close: `001b7c3a34` LOCAL on `box/dell2`; origin `box/dell2` read `01cc38c2ac`
(`git ls-remote`). The box's scheduled `box-sync` carries it; this seat does not push a shared branch.

---

## Surprise Rows

`IRPT_YCDGEN-D2-S25` -- OBSERVATION, INERT, `disarm_owner 2.0.0_SA_COO~G2`, UNDER_INVESTIGATION.

`updatedAt` on svc's PROFILE row has a SECOND writer: `/auth/login` stamps it (issuer msg 4105). The
window's standing inference -- "the before-`updatedAt` is exactly my own last write, so no third party
touched this row" -- is therefore not a sound no-third-party oracle. The discriminating tell is PRECISION,
not value: `swap_svc_firm.py` builds its stamp with `strftime('%f')` and writes 6-decimal microseconds
(`04:51:52.420577Z`), while the login writes 3-decimal milliseconds (`04:48:28.516Z`, `04:52:45.136Z`).

Scope of the claim, stated precisely: this does NOT falsify `N = 1` for `allowedFirmIds` -- no login wrote
that property, and both conditional UpdateItems fired on a correct read. What it falsifies is the ORACLE the
ledger prose leans on. It fails in BOTH directions: here it manufactured a discontinuity that the order's
STOP branch could have been read onto, and in a window where no login happens to land it would silently
certify a continuity it never established.

---

## Blockers

None. The order is complete and nothing is owed from this seat.

---

## Current State

This lane (`0.7.0_AE_CloudOps~YC2`, MSTR-seated on dell2 per `0.0.0_AB_MSTR~DELL2` msg 4012) holds ONE
order and it is complete: `IRPT_YCDGEN.TO-APPLY-sr1` window 6, flipped to `complete` at `001b7c3a34` on
`box/dell2` (LOCAL; origin `01cc38c2ac`). `svc-irpt-analysis` is back on `allowedFirmIds cottonwood`,
confirmed by a consistent read with a negative control, and the laptop's secret grant on
`irpt/svc-irpt-analysis/password` was removed at 04:54:26Z per MSTR. Ledger
`irpt-ycdgen-served-read-w6` is CLOSED with all five legs proven and its sentinel removed, so nothing is
stranded in `org/critical_paths/.open_deploys/`. The inbox watcher is armed (script pid 27624) and all four
delivered messages read 4 of 4 ACKABLE as READ.

---

## Next Steps

1. **[2.0.0_SA_COO~G2] Disposition row `IRPT_YCDGEN-D2-S25`** -- it is this seat's `disarm_owner` and the
   remedy is a wording fix for the next window's packet, not code: state the continuity claim on
   `allowedFirmIds`, the property the bounds actually name, or name which writers can move `updatedAt` and
   use the decimal precision as the discriminator.
2. **[2.0.0_SA_COO~G2] Sign the packet's own `## CTO HALF` section or point it at the half file** -- it
   still reads `(owed)` while the half is GIVEN, which costs every future operator the same re-derivation
   this session paid.
3. **[0.7.0_AE_CloudOps~YC2] Hold for the next task order** -- event-driven, watcher armed, no loop.
