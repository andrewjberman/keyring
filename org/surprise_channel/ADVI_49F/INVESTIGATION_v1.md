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


### ACCEPTANCE READ — ADVI_49F.c01-SIGNFIELD: PASS (CVO independent run). CERT P2: **DISCHARGED** on witnessed evidence @0412a8d6d8.

3.0.0_SA_CVO, 2026-08-27 ~17:5xZ. Validator run at this seat: ids C01-1..C01-6 -> `VALID`,
TRUE_RC=0 bare, rows=6, violations=0. Chain: seat flip + report (76283) -> COO RAVC-4 (76284,
"strongest of the launch set") -> this read.

**P2 DISCHARGED, act witnessed not expected:** the explicit `nna_headline SUM pre == post` assert is
IN the harness at @0412a8d6d8 (`ADVI_49F.c01-SIGNFIELD_ACCEPTANCE_HARNESS.py:236-242`, citing CTO
76200 + the three d-readers by line) and EXERCISED (result JSON `nna_headline_sum` entries; delta
0.0000 on both dates; COO corroborates). The 76202 landing's condition is met; the cert record
@958dbfc's P2 observation is closed by mechanism.

**TWO SELF-FOUND INSTRUMENT DEFECTS recorded with the completion (the seat filed them against
itself; COO banked #5 as a round keeper):** (a) the pre-registered table @e8ccd8eb77 carried ONE
wrong row (64,841.33 vs measured 87,054.14) with a wrong stated mechanism — both alternative causes
measured out, originals kept beside corrections; (b) **THE MOVING-BASELINE HARNESS** — the committed
acceptance artifact pinned its PRE arm to `git show HEAD:` (a moving symbol) while its own docstring
cited the content-pin rule; the moment the fix landed, both arms read post-fix code and the harness
could not reproduce its own committed result. Found ONLY because the determinism control ran AFTER
the commit. Corrective shape @bb48c4ee4c: explicit content pin + a guard REFUSING a baseline already
carrying the field (exercised rc=1). Keeper class: *a committed acceptance artifact must pin its
baseline by CONTENT, and its determinism control must run post-commit.*

**SCOPE NOTE carried:** history re-valuation deliberately NOT done — historical partitions keep the
old sign until P14-VEHICLE runs; c01's loud pre-1.2 refusal makes the gap non-silent in code.
c02-CFINPUT proceeds per the sequenced GO; P14's gate now waits on c02 alone.

### RULING LANDED -- 76331 (1.0.0_SA_CTO): the c02 provenance fork RULED; INTER_ACCOUNT_PROVENANCE = {pair-match, text-counterpart} STANDS; code-rule INTERNAL rows NOT admitted on the code alone (durability-rule landing)

3.0.0_SA_CVO, 2026-08-27 ~18:2xZ, same-turn per the drive-open rule and the ruling's own instruction.

THE RULING: 74122's class-grain sentence binds transfers whose inter-account character is ESTABLISHED -- a transaction code is not a counterparty (a-name-is-not-an-identity, applied to rows). Route (a) measurably never crosses; route (b) is UNKNOWN, and a filter must not encode a guess as a measurement. The 8-of-8 all-ten pass under this exact reading is the supporting evidence.

THE (b) IN-KIND HALF GETS AN INSTRUMENT, NOT A FIAT: a cross-account pair-scan (same day, same CUSIP, opposite-direction quantity in another account's ledger); rows where the scan ESTABLISHES a counterparty graduate through the EXISTING pair-match provenance -- zero new principle. 2.0.0_SA_COO cuts the bounded pair-scan measurement where judged right; it does NOT gate CF-3, which proceeds NOW on the ruled population.

THE RESIDUE IS NAMED ALL THE WAY UP: unestablished code-rule in-kind legs stay EXCLUDED, refused-BY-REASON in the census, and THE P1.5 RE-GRADE REPORT CARRIES THE RESIDUAL'S PER-DAY DOLLAR SIZE WITH ITS DENOMINATOR so the arm-(a) serve read is made with it in view -- materiality at the serve gate is Andrew's judgment and he gets the number, never a silent drop. (This binds the CVO P1.5 acceptance read: the re-grade is NOT complete without that figure.)

Also ruled in 76331: CF-4 deploy routes through the CTO seat when CF-2/3/5 close; the c00-signs-code-rule-cash item banks to the round queue (COO); the CRLF post-deploy STALE caveat banks for the post-CF-4 verifier.
