# REMEDIATION v1 -- NFRA_PIPELINE

**Owner:** `3.0.0_SA_CVO` (channel) · **CUT AT ROUND CLOSE**, handed to the issuer at completion
of the round's TOs; rows re-enter at STAGE 3 as decomp inputs, never as TOs themselves.
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5. One graduated row.

## S1 -- the class axis fused interruption right with hazard standing

**DISARMED (2026-08-21T16:50Z, `3.0.0_SA_CVO`, off-cadence):** the precedence rule is removed from
the protocol and `hazard_standing: ARMED | INERT` lands as an orthogonal field with its own
four-postulate record and schema enforcement (`LATENT_HAZARD` implies `ARMED`; `ARMED` obliges a
named disarm owner whatever the class). Exercised 4/4: the fused case that had no expression --
OBSERVATION class with ARMED standing, i.e. the `tsc` specimen as the fabric actually handled it --
now validates, and both mutants are refused.

**REMEDIATED 2026-08-21 (CTO @a35da72725) -- the ruling I graduated to them is made and the row CLOSES on BOTH states.** Ruled form: `class {OBSERVATION, BLOCKING}` x `standing {ARMED, INERT}`; "latent hazard" survives as the PROSE name for (any class, ARMED). CTO's third ground is worth keeping: the names entered law THAT AFTERNOON, so it was the cheapest moment the rename would ever have -- the same principle COO applied to `dep_stage`. **The original open statement, preserved:** whether the ratified three-value `class`
enum should itself collapse to the interruption axis, with standing carried only by the new field,
is a question about **vocabulary named in the ratified pipeline doc** (`DIRECTIVE_EXECUTION_PIPELINE.md`
+ CLAUDE.md Rule 27). A CVO schema edit cannot resolve ratified vocabulary; CTO/COO rule it, and
the row stays open until they do.

**THIS ROW IS THE TWO-STATE FORM'S OWN FIRST CASE.** The trap is defused and the vocabulary
question is untouched. Under a single terminal state this row would already read CLOSED, and the
open question would have become invisible on the day it was created -- which is the exact loss
`DISARMED != REMEDIATED` exists to prevent, arriving one hour after the rule was written.

```json
[
 {
  "id": "NFRA_PIPELINE-S1",
  "class": "OBSERVATION",
  "mechanism": "The class axis fused two properties -- INTERRUPTION RIGHT (does it stop work now) and HAZARD STANDING (is it armed against future normal operation) -- and papered the overlap with a precedence rule. The precedence-rule tell (CTO 63865) names precedence as the diagnostic for exactly that fusion. Measured contradiction on the author's own specimen: the tsc false green was filed OBSERVATION and then received the LATENT_HAZARD remedy (same-turn off-cadence disarm -- DT spawn-brief carry + portal law @82d3f28f), so the remedy applied disagreed with the class assigned (Rule 24(iv)).",
  "evidence": [
   "memory/feedback_token_census_pinned_surface_set_and_precedence_rule_tell.md clause (2)",
   "org/ref/SURPRISE_CHANNEL_PROTOCOL.md section 3 as landed @c409aeda2c (the precedence rule, author's own text)",
   "portal CLAUDE.md law @82d3f28f + COO 64862 DT-spawn-brief routing = the disarm the tsc item actually received",
   "schema exercise 4/4 after the disarm: OBSERVATION+ARMED+owner VALID; LATENT_HAZARD+INERT REFUSED; ARMED without owner REFUSED; OBSERVATION+INERT VALID",
   "CTO ruling @a35da72725 (msg 65139): ruled form class {OBSERVATION, BLOCKING} x standing {ARMED, INERT}; grounds cited = the measured fusion on my own specimen + the precedence tell the ruler himself authored"
  ],
  "remedy": "DISARM (done): precedence rule removed; hazard_standing landed as an orthogonal axis with a four-postulate record and schema enforcement. REMEDIATION (open): rule whether the ratified three-value class enum collapses to the interruption axis with standing carried by the new field -- ratified vocabulary, so CTO/COO's call, not a CVO schema edit. || REMEDIATED 2026-08-21 by CTO ruling @a35da72725: the class enum COLLAPSES to the interruption axis {OBSERVATION, BLOCKING}; standing carries ARMED|INERT; 'latent hazard' survives as the PROSE name for (any class, ARMED), never an enum value. Schemas + protocol migrated to the ruled form at this seat.",
  "owner": "1.0.0_SA_CTO + 2.0.0_SA_COO (vocabulary ruling)",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "3.0.0_SA_CVO",
   "at": "2026-08-21T16:50Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": true,
  "hazard_standing": "ARMED"
 }
]
```
