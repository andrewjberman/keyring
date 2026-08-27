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


### RULING LANDED — 76202 (1.0.0_SA_CTO): explicit `nna_headline SUM pre == post` assert folded into the c01 acceptance harness (durability-rule landing)

3.0.0_SA_CVO, 2026-08-27 ~17:0xZ, same-turn landing. CTO CONCUR on 0.4.0_DS_ClientPlatform~U's
76195 instrument swap (comp-blast NOT-FOUND on a stale snapshot is not an absence verdict; source
enumeration governs; backfill set UNCHANGED), with ONE SHARPENING that AMENDS THE ACCEPTANCE:
**THREE of four d-plane readers consume c01's OUTPUT** (d01:43+50, d02:33+41, d04:40+52 read
`nna_canonical` and sum `nna_headline`; d11 does not) — their invariance under the c01 fix rests on
the measured headline-unchanged claim (0 of 267 legs, @e8ccd8eb7), NOT on field-disjointness.
**RULED: the acceptance harness ~U is building carries an EXPLICIT assert — `nna_headline` SUM
pre == post on the produced partition — beside the four controls.** A failing assert STOPS the
field-landed report; that is what an acceptance control is for.

CERT LINKAGE, noted as CTO offered: the cert step-zero record @958dbfc carried a P2 observation
(headline-unchanged rode the delta-table instrument rather than an explicit assert on c01's face).
**This assert, when it lands in the harness, DISCHARGES that P2's remedy path** — the observation
converted into a mechanism. Discharge is recorded here at the assert's LANDING evidence (~U's
harness commit), not at this ruling; until then the P2 stands as written.

### AMENDMENT LANDED -- 76253 (2.0.0_SA_COO): RPS-CUSTODY expected_criteria widened 5 -> 7 (RPS-1b, RPS-1c), issuer-authored post-cert; CVO DELTA-CERT PASS

3.0.0_SA_CVO, 2026-08-27 ~17:3xZ, same-turn landing. Issuer ruling 76210 s.5 split the materiality print into three measured rows after the wrong-account finding; the executing seat implemented the element to match the issuer prose (implementing, not adjudicating -- stated in their own comment). DELTA-CERT at this seat: element reads the 7 ids; RPS-1b (measure the TRUE successor at opal-data-assets/schwab/08242234/silver/fact_rps/) and RPS-1c (re-print materiality on the true pair, legacy@2026-07-23 vs the 0824 successor) are real criteria on the face (:111, :114) tracing to the ruling. The step-zero cert @958dbfc certified the 5-id face; THIS ENTRY is the cert record for the widened set -- acceptance reads on this TO expect 7 positional ids.

### ACCEPTANCE READ -- ADVI_49F.RPS-CUSTODY: PASS (CVO independent run). TO COMPLETE stands.

3.0.0_SA_CVO, 2026-08-27 ~17:5xZ. Run at this seat, not accepted on report: `python .tools/proof-of-spec-check.py <instance> "RPS-1,RPS-1b,RPS-1c,RPS-2,RPS-3,RPS-4,RPS-5"` -> `VALID`, TRUE_RC=0 taken bare, acceptance rows=7, violations=0, alignment frame resolves the governing TO by declared id (scanned 2126) and correctly ANNOUNCES the pre-pipeline basis (no decomp_ref required, CTO ruling 66492). Completion chain: seat flip (76272) -> COO RAVC-4 (76274, APPLIED-layer read on a different instrument, mutant control both-arms, failed validator pass recorded INSIDE the instance) -> this read. Face attribution swap corrected by its author @dab6eda3b3. RESIDUALS AT THEIR OWNERS: Rule-25 marker instrument (COO, round-close queue, WS-E miss as fixture); the 23 served July-23-basis partitions re-emit question = a PRODUCT CALL AT ANDREW, surfaced by COO, not authorized anywhere below him.
