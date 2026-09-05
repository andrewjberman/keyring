# 3.0.0_SA_CVO~Z -- work log 2026-09-03 15:55-17:05Z: two rows held then landed, and a probe of mine that was wrong

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_1300-1555Z_*`. **Push state as read:** local HEAD
f3897425ee, origin/SITEZ 001709c96e at 17:04Z -- this seat's commits since the stamp are LOCAL and travel in the
integrator's window. **Loops:** none armed here.

## 1. Z-S41 discharged, and the discharge verified rather than assumed

`0.7.0_AE_CloudOps~S` committed the declaration at f570d3981e as its first act on respawn, and `2.0.0_SA_COO~Z`
filed the disarm record at Z-S43. **Verified at this seat:** the committed bytes hash to `5c19df6ab8715341...`,
BYTE-IDENTICAL to the hash Z-S41 pinned from the untracked worktree file at 15:48Z. So the file that landed is
the file that was at risk and the rescue copy was never needed. Pinning the hash on the row is what made that a
check rather than a matter of trust, and it is worth doing on every row that names a file at risk.

The severity correction held on both planes: `1.0.0_SA_CTO~Z` ran the live `describe-table` this seat had named
as the discharging read (DeletionProtectionEnabled True, positive control on 49financial), and
`0.0.0_AB_MSTR~Z` added the NEGATIVE control the positive-only pair lacked (`opal-pii-lookup` reads False). Both
Tier-1 seats retracted the data-loss wording they had passed on.

## 2. Row Z-S47 -- the contract gap behind those three armed hours

NEVER-2 governs an entry left OPEN, and Z-S42 is that instance: the apply the ledger said never ran had run,
pinned by PITR's own EarliestRestorableDateTime at 13:21:50Z, about seventy seconds after the import leg closed.
**Nothing governs the other direction.** Leg L1 of the same ledger closed at 13:11:25Z against a target reading
"dynamodb.tf flip + demo import declaration committed", citing 464c58b859 -- a commit carrying `opsec/dynamodb.tf`
and the ledger entry, and not the declaration. It could not have: L1 closed NINE MINUTES before the import at L4
produced the file. So a closed leg certified an artifact that did not yet exist, no seat then held an open
obligation to commit it, and the gap was found three hours later by a peer reading the WORLD, never by the record.

The mismatch is permanent: 464c58b859 still shows `demo.tf` zero times while the declaration lives at f570d3981e.
**One ledger, wrong in both directions at once, and neither error was a lie** -- `proof: null` honestly records
that nobody wrote a proof, and L1 honestly records a hash. The reader supplies the false part. Filed
OBSERVATION/INERT at 9c3a46b9ae after the discharge, scoped to what survives it. Two shapes would close it and
both are the contract owner's call: one artifact per leg, or a close-time check that the proof names every
artifact the target names.

## 3. Row Z-S48 -- a worker's armed finding confirmed, and its class bounded

`0.7.0_AE_CloudOps~Z` found that S2-AC3 offers three interchangeable instruments for the vendor-call count and
one of them is silently dead: `opal-portal-data-proxy` cannot emit custom metrics, so that arm returns zero for
the wrong reason and reads exactly like a clean result. It disarmed same-turn by using the log-line arm with an
existing-record control.

**Confirmed here on the DECLARED plane, which the live log line could not show:**
`shared-infra/opal-portal-lambda-role.tf` grants `cloudwatch:GetMetricData`, `GetMetricStatistics` and
`ListMetrics` -- the READ verbs -- and NOT `PutMetricData`, which is absent from all 13 tracked `.tf` naming that
role. Positive controls: `inf-pipeline/iam.tf` and `yang-pipeline/iam.tf` both carry it, 28 files estate-wide do.
So the role is shaped read-only on CloudWatch by declaration; the denial is what that shape predicts, not a
dropped grant. That bears on the remedy, since adding the verb widens a live role's identity policy.

## 4. My own probe was wrong, and I caught it by reading

Z-S46 states it did not survey the class's REACH, so this seat measured it. A regex for an alternation near an
instrument word over all 55 criteria in the project's 9 faces returned **THREE** hits. Reading each in full,
**all three are false positives**: `S1-AC3` alternates a DENOMINATOR on one instrument (39 of 39 methods or 20 of
20 non-OPTIONS with both counts printed -- the AMEND D shape from this seat's own tick-8 verdict), and
`S16178-AC3` and `S17R28-AC3` each alternate an OUTCOME ("0/0/0, or the row that says otherwise"), which is the
standard STOP-and-file clause. **True reach: 1 of 55, and it is S2-AC3 itself.** Both STAGED faces are clear.

The wrong probe is recorded in the row beside the right count, because the obvious probe for this shape returns
3 and is wrong about all 3, and the next seat will otherwise re-run it. This is the class the project has caught
all day, applied to my own working note before it left this seat.

## 5. The guard fired three times in five minutes, and each refusal was correct

The Z-S47 row was built and HELD while the channel file was contended: twice on a peer's transient write, once
because a peer had the file STAGED mid-commit. Committing through any of those would have swept a peer's work
under this seat's author line -- the class four seats closed this afternoon. The row's id recomputes at write, so
holding costs nothing. It landed at 9c3a46b9ae when the file went quiet; Z-S48 landed at f3897425ee the same way.

**One instrument note, banked to memory rather than filed as a row:** the notifier's `ROW MUTATED in place` WARN
fired three times today on rows whose DATA was byte-identical, with the hash CYCLING BACK. The innocent causes are
a peer's whole-file re-serialisation and staging transitions. But one of today's WARNs was a REAL in-place edit
that the row gate refused, and it produced the identical signature -- so the warning cannot discriminate, and this
seat called the first one a notifier defect and was wrong. Measure the row data before saying anything.

## 6. State at close of this window

L8 intake current through Z-S48. Round 2, per the issuer's 19861: FIVE faces, THREE terminal
(TO-OP-S-25-26-27 @71f74091d0 and TO-OP-S-16-17-8R2 @976e405a89 both ACCEPTED on the issuer's own
coverage-checked runs), TO-OP-S-17R-28 GO'd at 17:03Z, TO-OP-S-2 open at ~Z, TO-OP-S-1 staged. Decomp v0.1.7
carries the two-bucket split as cells. **This seat's tick-8 ruling is being applied downstream correctly:**
S17-AC5 and S17-AC6 file UNCOMPUTABLE by the v0.9 ruling with nothing attempted, and the worker additionally
refused a PASS on AC6 from observed delivery on the ground that continuing delivery is equally consistent with
success and with never having been tested -- which is the right reading of a criterion whose subject was retired.

**Still owed and still blocked:** the four round-1 closure rows for `REMEDIATION_v1.Z.md`. The gate here reads
`c3ef3a2530` with zero occurrences of `REMEDIATED`; the ruled arm has not arrived because the integrate leg is
assess-only with the site not quiet and the push declined at Andrew's terminal. Script ready, refuses over a dirty
file. Round 2's L9 is not reachable with two faces open and one staged.
