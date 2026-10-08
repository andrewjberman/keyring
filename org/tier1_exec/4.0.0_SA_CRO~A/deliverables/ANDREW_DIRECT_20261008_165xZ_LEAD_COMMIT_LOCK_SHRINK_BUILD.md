# ANDREW_DIRECT 2026-10-08 ~16:5xZ -- 4.0.0_SA_CRO~A leads the build of the commit-lock shrink directly

**Channel:** laptop terminal, to `4.0.0_SA_CRO~A`, in the GitOps session, after
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/CMTQUE_LONG_TERM_ASSESSMENT_20261008.md` (@`65a1defac0`, corrected
@`a477ba49fb`) recommended its option B.
**Recorded by:** `4.0.0_SA_CRO~A`, same turn.

## Andrew's words, verbatim

> "I need you to lead the development of this function as we dont have time to really hand it off to a whole
> canonical-flow project registration, this should be fairly fast to get through, lets get through it, ask me any
> questions you need in /open-calls format as you go and we'll figure out how to integrate it across the fabric as we go."

## Reading

"This function" = the assessment's option B: run the commit gates that read only a commit's own files on a private
index before the commit lock, so the lock covers only writing the commit. `4.0.0_SA_CRO~A` builds it directly, with no
L1-L10 project registration. Questions go to Andrew as /open-calls cards as they arise. How it spreads across the
fabric is worked out along the way, not decided here.

## Ruling, 2026-10-08 ~17:0xZ, same channel

Retry-storm question, verbatim: "How would retries not create a retry storm?" Answered with the two-phase design:
validate (all gates and hooks on a private index, no lock), then land (a short lock that writes the validated content
onto the current tip). A commit that loses the race waits for the land lock and never re-runs its validation, unless
another commit changed one of the same files.

Open call put (CALL 1 of 1): may the hooks run in the validate phase, with the land step writing the commit through
git's low-level commands instead of `git commit`? REC (a) yes. Andrew, verbatim: "Yes go ahead"
