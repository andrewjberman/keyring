# NFRA_OPSWKF PRD v0.11 -- ratified-text review (ENDPOINT: FWD-10's proof names the probe that discriminates)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T00:10:38Z. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @17edabd1df.
**Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6184. **Prior:** v0.10 SIGNED with this point as its note.
**Verdict: SIGNED.**

The change, read as a diff against v0.10: FWD-10's DONE WHEN now puts the setting read back from the API's own configuration
FIRST, and names a probe that can tell open from closed: a request with no credential to a route behind the API's authorizer,
answered 401 by the API before the act and refused by the endpoint after, the two answers written out and shown different. The
invocation counts are struck from the proof and kept only as the check that the probe invoked nothing. Both domain planes and
the distributions are read with their counts.

That is the note on v0.10, taken whole, and it is now measured: the applier's report shows the missing-route request answering
404 before and 404 after, and the behind-the-authorizer request answering 401 before and 404 after. v0.10's probe could never
have shown the closure. The applier stopped correctly when the first probes did not behave as the pair said, and the pair was
re-cut before the write.

The CTO's ruling on the stage's deployment id (it moved five seconds after the write, by the stage's own auto-deploy, with no
stage setting or route changed) is accepted as stated; this seat did not read the stage.

Still open and correctly kept out of FWD-10: deleting the API, its functions and their key, which is Andrew's; and who may invoke
the trade functions directly.
