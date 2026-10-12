# IRPT_BCKEND: remediations, round 165 (workstream ~P)

<sweep_watermark>2026-10-12T19:05Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T19:05:00Z. Follows ADJUDICATION_v66. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_165_P_DRAIN_END_20261012.md` (blob b78a9d04c9, msg 6495). No judgment criterion.
Graduated, round label v166: 2 rows, OPEN, owner `2.0.0_SA_COO~P2`. ARMED: 1 (D2-W328-S1: a challenged stored-bundle probe signs in again; no
released byte carries it; no resident release before the round-166 repair merges).
Two REMEDIATION_v41 rows stay OPEN and are now MEASURED (IB-pr-475, read from code): D2-W309-S2 -- `commentary_ref` is still written beside
the record and read from inside it at HEAD, so by the code a live packager raises COMMENTARY_REF_ABSENT, and no test crosses the write and
the read; D2-W315-S3 -- the prices store's writer exists (`build_canonical_prices_v2.py:907`) and nothing schedules it, so it is
WRITER_UNSCHEDULED, which is neither of v0.49's two branches. Both are the CTO's to rule. D2-W321-S1 stays OPEN on the C-VALUEFACTS pair
(this seat's condition: the portal reader moves before bd_adapter renames).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W328-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A stored-bundle probe that is now classified WAF_CHALLENGE still falls into refreshSession, i.e. a fresh sign-in submission, in withAuthenticatedPage (the path mainCli runs); the new challenge ending covers acquireSession's own probe only.",
  "evidence": [
   "investigation row D2-W328-S1",
   "row D2-S109 (the disarm owner's ruling)"
  ],
  "remedy": "In withAuthenticatedPage, a stored-bundle probe classified WAF_CHALLENGE ends the run with acquireSession's challenge ending and never calls refreshSession; an arm in probe_challenge_and_pair.js proves it. Round 166 cell. Until it merges, no resident release carrying ycharts_session.js is cut (the disarm owner's ruling, row D2-S109). Disarmed when that cell reads merged.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v166",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v166"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W328-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The pair is requested once per run on the first probe after the submission (pairControl: filled && !record.probe_pair); with the new rule a token-less first probe records discriminating=false and no later probe, even one holding a token, runs the pair.",
  "evidence": [
   "investigation row D2-W328-S2"
  ],
  "remedy": "The probe pair is decided by the first probe after the submission, so a token minted later is never paired. Decide in the round-166 cell beside D2-W328-S1 whether the gate is `discriminating !== true`, or state that once per run is the design.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v166",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v166"
  },
  "closed": false
 }
]
```
