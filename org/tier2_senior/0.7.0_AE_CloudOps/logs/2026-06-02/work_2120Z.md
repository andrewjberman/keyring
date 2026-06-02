# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2120Z

## Joe-loop resolved (Joe holds session) + Andrew RULING-b reframes W4f -> edge untier (CTO co-design)

### Loop: RESOLVED for Joe (decoded-token proven, see work_2117Z)
Joe's pre-fix JWT lacked advisorId -> :312 forbid -> 403 -> /login loop. Post my 210210Z
opal-partner-inflection entry, a fresh Joe JWT carries advisorId=joe_brandenburg + firmId ->
:312 passes -> session holds. Joe unblocked for the immediate re-smoke.

### Andrew RULING-b (COO 211320Z 2nd msg) — supersedes my W4f rec-(a) + CTO RULING-a
"No tiering on Distribution; nothing on the Distribution tab is PII/blocked from non-admins."
So: (1) non-admins HOLD A SESSION regardless of advisorId (valid firmId JWT not edge-forbidden
at bootstrap), (2) UNTIERED Distribution incl cross-advisor drills for non-admins, (3) KEEP Books
admin-gated. This = an EDGE change (relax .004 for non-admins on Distribution paths, scoped so
Books stays gated).

### The seam (why CTO co-design, not a quick tweak)
Distribution drill + Books BOTH fetch platinum/advisors/{advisorId}/book.json via the SAME .004a
pattern. Relaxing .004a for non-admins opens BOTH -> breaks "Books admin-gated." Options routed to
CTO: (i) [my lean] Distribution consumes a SEPARATE no-PII advisor-summary artifact on a
non-.004a-gated path; Books keeps the PII book.json .004a-gated -- clean boundary, needs DS no-PII
artifact + FE re-point. (ii) edge PII-strip projection -- fragile (can't distinguish intent from URL).

### Actions
- RAVC2 to COO (212042Z): loop root-cause + ACK ruling-b + edge-change plan (co-design w/ CTO before landing).
- CONSULT to CTO (212104Z): the seam analysis + I own the edge impl once CTO sets the artifact/path
  boundary + the session-hold scope. Won't land a .004 loosening unilaterally.
- Task #11 opened: edge untier Distribution (CTO co-design).

Standing by for CTO's seam scoping. Joe is unblocked for the immediate re-smoke meanwhile.
