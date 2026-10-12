# NFRA_OPSWKF workstream S -- L9 grade of the FWD-8 and FWD-9 releases

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:59:53Z. Row NFRA_OPSWKF-D2-S10.
**Input:** `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_DEPLOY/WORKSTREAM_S_L8_PACKET_AND_FWD9_GRADE_20261011.md @4daa06ebad (msg 5930)` and the issuer's FWD-8 grade file beside it.

| criterion | what it covers | verdict |
|---|---|---|
| OW-sd1-AC2 | FWD-8: the plan branch, the deployed bytes, the unchanged environment | **MET** |
| OW-sr1-AC1 | FWD-8: the live reads on the deployed service | **MET** |
| OW-sd2-AC2 | FWD-9: the plan branch, the deployed bytes, the unchanged environment | **MET** |
| OW-sr2-AC1 | FWD-9: the live reads on the deployed service | **MET for the refusal. The admitted arm of the DONE WHEN was not run** |

**FWD-8: REALIZED. FWD-9: REALIZED for the refusal; one read of its DONE WHEN is still owed.**

## This seat's own read: the deployed bytes

Both issuer grades say the member-by-member diff was the applier's and was not repeated. This seat repeated it, from the live
functions, in memory.

| | trade-dashboard-api | trade-submission-handler |
|---|---|---|
| downloaded package's hash equals the function's code hash | yes | yes |
| members | 3 | 3 |
| byte-equal to the tree at the release pin | 3 of 3 (abf78fcb7f) | 3 of 3 (234c3b4b10) |
| environment keys | 1 | 4 |
| last modified | 19:30:58Z | 21:27:29Z |

So what runs is what was built, on both. The plan lines and the replans are the applier's and were not re-run.

## FWD-8: REALIZED

The DONE WHEN asks for both arms on the deployed service, before and after. The applier made them: the same outside caller read
200 before and 403 after, and an Opal-internal caller read 200 after. That caller was advisor-tier with the Opal firm id, which is
the branch PRD v0.5 would have broken and the one this seat's note on v0.6 asked to see.

Not exercised on the deployed service: a caller admitted by tier `internal`. It is one of two comparisons in a function whose
deployed bytes equal the tested bytes. It closes the first time such a staff member opens the page.

## FWD-9: the refusal is proven; the admitted read was not made

The refusal is proven in the form PRD v0.8 asked for: one body that cannot be stored, by an outside caller WITH a verified email;
400 before, 403 after with the new check's own message; no row stored, read with a non-zero control.

**The same DONE WHEN has a third read: after the release, an Opal-internal caller with an email is answered 400.** It was never
made. The CTO's half of the pair refused to mint such an identity. So an Opal staff member being ADMITTED to submit rests on tests
at the pin, the byte equality above, and FWD-8's live read through the same authorizer. None of those is a read of this route.

What that leaves: if the check refuses staff, nobody learns it until a real person's trade submission fails. The CTO has ruled
that a staff 403 is an immediate rollback, and the rollback version is named. That is a sound control for a small, known group. It
is not the outcome's proof, and the ratified text asks for the proof.

Two ways to close it, either enough: the first real staff submission, read from the function's log as admitted; or the one
synthetic read the DONE WHEN names. Until then FWD-9 should be carried as realized for the refusal with one read owed.

**"No mail from any of the three reads"** is in the DONE WHEN. The packet shows no row stored; it shows no read of the mail side.
The malformed body returns before the mail call in the bytes this seat read at the v0.7 review, so no mail is the expected
result; it was not measured.

## What the release recorded that is not a pass

Taken from the packet and repeated because a grade should not hide it: the cross-box gate read STOP in warn mode on four open
deploys of other projects; the commit gate checked 0 of 2 files on the deploy-record commit; the client-data check had no hash
list on this box; the FWD-8 applier read the two halves whole only after the act. None changed an outcome.

---

## ADDENDUM, 2026-10-11T22:48:30Z: the four direct invokes (OW-sr2-AC2 and OW-sr1-AC2)

**Input:** `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/S3_FINAL_REPORT_FOUR_DIRECT_INVOKES.md @891dfaf600 (msg 6007)`. Row NFRA_OPSWKF-D2-S13.

| criterion | what it covers | verdict |
|---|---|---|
| OW-sr2-AC2 | FWD-9: the admitted arm on the deployed bytes, with its refusing twin | **MET** |
| OW-sr1-AC2 | FWD-8: the tier arm on the deployed bytes | **MET** |

**FWD-9: REALIZED, as PRD v0.9's DONE WHEN defines it.** The one read owed above is made.

The applier's four invokes, in the order made:

| invoke | constructed context | answer |
|---|---|---|
| the refusing twin, FIRST | advisor tier, a firm id that is not Opal's | 403, the new check's own message |
| the admitted arm | advisor tier, the Opal firm id | 400, the unstorable body's message |
| the other comparison | tier internal, a firm id that is not Opal's | 400, the same |
| the dashboard's tier arm | tier internal, a firm id that is not Opal's | 200, count 12 |

The refusal was read from the instrument before either admission, so the two 400s mean the caller was admitted and not that the
check never ran. Both comparisons of the submit check are exercised, including the one this seat suggested at the v0.9 review.
No row was stored for any of the three addresses, read as a whole partition with a control of 18.

**This seat's own read:** both functions' code hashes are unchanged since it downloaded the packages, and equal the digests the
applier read before its first invoke. The invokes ran against bytes this seat has read member by member.

### What is still not shown, and it is two different things

1. **That the portal's authorizer hands these functions the context a real staff session carries.** The applier's own words are
   exact: the tier shape has been shown through no door. The first real staff session closes each. This is the residual v0.9 named.
2. **That "Opal staff only" holds on every path to these functions.** Row D2-S11, filed after the releases: a second live API
   reaches the dashboard, submit and workflow functions under an authorizer nobody has read. FWD-8 and FWD-9 are proven on the
   functions' own check, which runs whatever door the request came through, so that check still refuses a caller it does not
   recognise. What is unknown is what context that other authorizer sets, and the workflow function is covered by neither release (the CTO's statement, msg 5960; not read by this seat).
   This is outside both DONE WHENs as written; it is the outcome the CTO said it will write on that read's record.

The mail side stays as v0.9 states it: claimed from the handler's order and the row count, not from the mail service's log.
