# ADVI_49F — Surprise-channel investigation doc v1

Opened 2026-08-27 ~16:5xZ by 3.0.0_SA_CVO (channel owner) at the project's first channel item.
ADVI_49F registered @67ee4a4485 (Andrew 15:42Z word @8a89bef0b7); D2 member (DIRECTIVES.yaml
@12b28fc831). Append-only during a round.

---

## D2 DRIVE-OPEN DECLARATION — 3.0.0_SA_CVO (channel owner)

Binding for this project's D2 round, per the Andrew-direct lock-in
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260827_D2_TIGHTENING_LOCKIN_BEFORE_FLOOD.md`
@ff94ca9971):

1. **DURABILITY RULE:** any mid-round ruling that amends a spec, remedy, or acceptance for this
   project LANDS IN THIS DOCUMENT SAME-TURN, landed by 3.0.0_SA_CVO. Executing seats rule on the
   wire at full speed; the landing is CVO's act.
2. **ROUND-CLOSE MODE:** the round terminates through a REAL remediation cut — REMEDIATION_v1 cut
   at round close, closing only at ZERO graduated items; graduated rows re-enter at stage 3.
3. **Rule 27 standing:** 3.0.0_SA_CVO mans this channel for the whole D2 drive. Class
   {OBSERVATION, BLOCKING} x standing {ARMED, INERT}; ARMED names its disarm owner at surfacing;
   OBSERVATION never interrupts.

---

## CHANNEL ITEM — 76196 (0.4.0_DS_ClientPlatform, S6, RPS-CUSTODY) | OBSERVATION / INERT / RECORDED

**Filed:** 2026-08-27T16:55:15Z, found discharging RIDER 1 (full print @a53fcf6459). Seat continued
RPS-CUSTODY; nothing halted; no control built (moratorium honored).

**FINDING:** WS-E's runtime backstop `SCHWAB_NON_MODEL_SANE = (50M, 500M)` is a MAGNITUDE band on
the derived residual `non_model_aua`, and it is structurally blind to the defect that was actually
running: the custody minuend froze 2026-07-23 while the model subtrahend kept advancing, so the
residual walks DOWNWARD through the band at ~-1.9M/day — "sane" for ~49 more days before tripping.
It has ALREADY left the design's own stated observed range (~180M–203M, same file line 166) without
firing, because the stated range is prose in a comment and the coded band is ten times wider.

**THE PATTERN, banked as the seat offered it:** *A BAND ON A DERIVED VALUE CANNOT DISCRIMINATE A
FROZEN INPUT FROM A MOVING ONE* — both inputs live inside one number and the band sees only the
number. The check that discriminates costs one comparison: does the input partition date ADVANCE
between runs — a STATE check on the input, not a magnitude check on the output. (Kin to the banked
one-axis-sweep and prose-vs-code lessons; distinct in mechanism.) Second defect inside the same
specimen: the honest range lived in a COMMENT while the enforced range was 10x wider — a
prose-vs-mechanism split inside one file.

**DISPOSITION:** RECORDED, INERT (the frozen-basis defect itself is already known subject matter of
this project's remediation; this item is about the CONTROL SHAPE). Candidate remediation row at
round close: input-advance state check beside any derived-value band on this chain — remedy-holder
named at the cut; NOT built mid-round (alert/monitor moratorium + frozen spec both stand).

— 3.0.0_SA_CVO
