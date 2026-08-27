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

**DELTA-CERT -- c02-CFINPUT widened 5 -> 6 (CF-3b) @03975fd4c5: PASS** (the RPS form). CF-3b traces verbatim to ruling 76331: the pair-scan instrument, graduation through EXISTING pair-match provenance (zero new principle), unestablished rows refused-BY-REASON, and the P1.5 residual-dollar clause carried INTO the criterion. NON-GATING stated on its face (beside/after CF-3, never blocks). Element matches the 6 ids; CF-5 additionally sharpened -- the instance must CITE the expected-id set the checker ran against, a bare rc=0 does not establish positional coverage (the coverage-unchecked fallback closed one layer deeper). Acceptance reads on this TO expect 6 positional ids. Keeper #10 banked at the round queue per 76335: c00 signing code-rule INTERNAL cash legs, value unrecoverable from the ledger as it stands -- named, not built.

**CF-3b MEASURED + ACCEPTED (76346/76350) -- landed for the round record:** the pair-scan ran; CONTROLLED subset (10 legs / $292k, instrument PROVEN live 7/7 + 75/75 on the known-pair control) -> ZERO graduate; UNCONTROLLED (29 legs / $636k, 69% of refused value) -> NOT EVIDENCE, stays REFUSED-BY-REASON and travels to the P1.5 re-grade with its per-day dollar size. The reporting form is the value: a pooled "0 of 39, $0" was available and would have read as clean coverage from a dead instrument -- the controlled/uncontrolled split IS the finding.

**KEEPER #12 BANKED (routed to this seat for the cut): cusip DOES NOT SURVIVE INTO flow_ledger** (absent from c00 out_cols, measured on the emitted 25-column partition) -- the ruled pair-scan cannot run against the ledger as emitted; this measurement worked only through a txn_ref positional-suffix recovery, AND NEEDING THE WORKAROUND IS THE FINDING. Production CF-3b needs cusip carried additively (c00 1.2 -> 1.3) or an explicit tested fact_trn join; NEITHER is built mid-round; the round names an owner or declines the build, with the controlled-zero as the sizing input. Also per 76350: CF-2 harness runs NOW at the ~U seat (built artifact, not another seat's gate); the ONE sanctioned CRO~A cc fires at harness-verified, harness-owner role only.

### CHANNEL -- 76367/76375: THE THIRD INPUT-WALL HAZARD (a00 attestation tie-guard) | ROUTED TO CTO FOR ARCHITECTURE RULING; CF-2 FALLBACK WENT LIVE AS PRE-REGISTERED

3.0.0_SA_CVO, 2026-08-27 ~18:4xZ. THE FINDING (0.4.0_DS_ClientPlatform~U 76367, exercised + enumerated, both controls): a00_runner's attestation tie-guard (:83-100, denominator from the CONVERTER never a self-count -- correct BY DESIGN, nobody proposes relaxing it) requires a conversion record attesting fact_acc at the date; 32 of 533 backfill dates are attested (2026-07-14..08-26), so the ruled P14 full-chain pass REFUSES LOUDLY at stage 1 of 15 on 506 of 533 dates. Exercised by a real 2026-03-24 abort; enumerated from the converter's own 456 records. RULING AT 1.0.0_SA_CTO (gates P1.4 -> the P1.5 arm-(a) evidence): remedy space = back-fill conversion records / a documented backfill-mode path / another shape -- the guard's principle survives whichever. THIRD independent input-wall hazard on the same pass (D-1 pull; absent A/B planes; attestation) -- fires FIRST and FRIENDLIEST (loud stage-1 refusal, not 16 wasted hours, not silent greens); COO's synthesis framing stands: the three probably want ONE ruled answer about what re-mint-history MEANS for this chain, not three patches. 0.7.0_AE_CloudOps~L independently re-derives the 27/506 split (a denominator this consequential does not travel on one read); V14-3 hold unchanged.

**AND THE PRE-REGISTRATION SYSTEM PAID OUT AGAIN:** the CF-2 fallback conditions went LIVE BY EXECUTION (2026-03-24 UNMEASURED-PRE-BACKFILL; the substitute carries the magnitude half, the BD-tie half explicitly bound to the original) -- executed exactly as pre-approved, NO NEW WORD NEEDED. That is what pre-registration is for.

### RULING LANDED -- 76380 (1.0.0_SA_CTO): DECLARED-HISTORICAL MODE; back-filled attestations BANNED (durability-rule landing)

3.0.0_SA_CVO, ~18:4xZ, same-turn. THE GUARD STANDS UNMODIFIED. (1) Back-filled conversion records BANNED -- attesting conversions nobody witnessed is the self-count the guard forbids in the record format's clothing. (2) RULED SHAPE: a00 gains an EXPLICIT historical branch -- driver-selected flag, NEVER auto-fallback; the mode itself REFUSES dates >= the attestation epoch (its own negative control, exercised at acceptance); the EPOCH IS MEASURED from the converter's record set at run time, never typed; every emitted partition + manifest carries attestation_basis {converter-attested | declared-historical-pre-epoch} WITH ITS CONSUMERS NAMED -- the P1.5 re-grade and the parity harness READ the field and state the N-attested/M-declared split beside their denominators (the consuming half is the enforcement). (3) SYNTHESIS over all three input-wall hazards: RE-MINT HISTORY = THE FULL CHAIN, WITH CONTROL-REGIME BOUNDARIES DECLARED AND STAMPED, NEVER FAKED. No stage trimming. (4) Execution: DS-class a00 change + driver flag, COO cuts as a P1.4 precondition sized small; V14 execution report carries the attested/declared split. (CVO P1.5 bar updated AGAIN: the re-grade now carries BOTH the residual dollar figure AND the attestation split.)

### CERT STEP-ZERO -- ADVI_49F.P14-PRECOND @3982ab3a43: **PASS, AND THE DISCLOSED OVERRIDE IS BLESSED WITH A BOUNDARY**

3.0.0_SA_CVO, ~18:5xZ. THE FACE: ids DH-1..DH-5 execute ruling 76377/76380 verbatim with "the ruling wins on any divergence" on its own face -- DH-1 exercises the no-auto-fallback arm FROM THE REAL FAILING STATE (the 2026-03-24 abort must reproduce flagless); DH-2 exercises the mode's own epoch-refusal ("run it; do not assert it"); DH-3 epoch measured at runtime with a planted-record control; DH-4 basis stamped AND CONSUMED with the consumers named; DH-5 the rc discipline. Element matches; single-group instance_path in the assignee folder. PASS.

THE OVERRIDE (TO_DECOMP_OVERRIDE, audited, disclosed for blessing per 76396): **BLESSED, scoped.** The lint fired CORRECTLY (the R-4 exercise's gate doing its job on its author) and the audited escape is its designed relief valve. The decomp requirement exists so criteria trace to enumerated surfaces; here the contract IS a same-window Tier-1 ruling restated verbatim, ruling-wins-on-divergence -- a one-cell decomp would restate the ruling and change nothing (the speed governor: a check that cannot change what you do is cost, not control). **THE BOUNDARY, so this blesses an instance and not a habit: the override is acceptable ONLY for a single-surface TO executing a same-window Tier-1 ruling VERBATIM, ruling cited as authority and winning on divergence. Anything multi-surface, interpretive, or ruling-adjacent mints the cell first.** A second override citing this one as precedent without meeting that test is a channel finding.

### RULING LANDED -- 76422 (1.0.0_SA_CTO): CF-4 DEPLOY GATE PASS ON FOUR CONDITIONS; serve stays behind arm-(a) (durability-rule landing)

3.0.0_SA_CVO, ~19:0xZ, same-turn. On c02 harness-verified @6523480924 + implemented @cab1f8bff9. THE FOUR CONDITIONS, all verifiable: (1) one file (c02_twr_engine.py), DS QA-deploy lane, nothing rides; per-key enumeration = future twr_daily partitions only, no historical partition touched by the deploy act. (2) **THE SERVED-DELTA-0 BASIS IS RE-VERIFIED AT DEPLOY TIME, NOT INHERITED** -- the fail-closed publisher state (@bfb74b20c2) is re-read as part of the deploy act; changed state = STOP, gate re-opens. A 24-hour-old measurement of the thing that makes an act safe is not the thing that makes it safe. (3) Post-deploy verify by LF-NORMALISED CONTENT -- c02 is CRLF in tree, so a comp-pipescript STALE is an instrument signature, not deploy evidence; MATCH stays trustworthy one-directionally. (4) NO serve, NO flip, NO backfill -- served values move only at Andrew's arm-(a); V14-3 additionally waits on the a00 declared-historical build even after c02 completes; CF-2 clause 2 stays OPEN as recorded. On deployed-verified: CF-4 row updates from UNCOMPUTABLE to evidence, CF-5 finalizes, flip = COO + CVO ground. (CVO acceptance-read note: my c02 read will check condition (2)'s re-verification and condition (3)'s normalised compare as evidence rows, not trust them.)

### CF-4 DEPLOYED + ACCEPTED AT BOTH GATE HALVES (76470 CTO, 76472 COO) -- flip pending ONE act + the CVO completion read

3.0.0_SA_CVO, ~19:1xZ. All four conditions met WITH evidence: condition 2 done on the merits (three-plane publisher re-read, per-plane positive controls, fail-closed UNCHANGED -- which also keeps the arm-(a) context current for Andrew); **condition 3 fired FOR REAL and is the session's cleanest live specimen of the banked CRLF class:** raw compare DIFFERENT by exactly 355 carriage returns on a GOOD deploy; comp-pipescript MATCH true of a DIFFERENT SUBJECT (working-tree CRLF vs S3 CRLF); the LF-normalised digest with the parent-blob vintage discrimination is the verdict that binds. MATCH/STALE without its BASIS is not evidence -- to the round verbatim.

PENDING BEFORE THE FLIP: (1) the c02 face :8 token append ("DEPLOYED-THROUGH-CF-4 @21170203c5") -- measured ABSENT at HEAD by both Tier-1 seats (sound predicate reads 0); AE~L's pinned unlock read correctly refuses leg 2 until it lands -- the restrictive-stale-face arm, now one line from firing on the fabric that just banked it. (2) CVO independent completion read on the token's landing; on PASS, COO flips. FLIP FORM ruled: c02 flips WITH CF-2 clause 2 OPEN-AND-CARRIED -- a TRANSFERRED obligation with named carrier (post-backfill acceptance -> P1.5 re-grade, which the CVO bar independently requires), not an incomplete TO; the status text carries the attribution. Also pre-confirmed for P14-PRECOND: the tie check is DECLARED-NOT-RUN in historical mode -- feeding it len(acc) would be the self-count in the mode's clothing.
