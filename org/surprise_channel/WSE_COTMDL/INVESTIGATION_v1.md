# WSE_COTMDL -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25 on the first surfaced item for this project. Executing seats surface; the CVO files. Items are schema-validated against `../schemas/investigation_item.schema.json`.

```json
[
 {
  "id": "WSE_COTMDL-S1",
  "surfaced_by": "0.7.0_AE_CloudOps~H -- APPLIED AND LANDED THE AUTHORISED WORK FIRST so the surfacing is not a hold; re-derived the TO's own headline number from today's artifacts rather than accepting it",
  "surfaced_at": "2026-08-25T10:05Z",
  "one_line": "The TO's and decomp's '30 of 64' COUNTS TWO DIFFERENT POPULATIONS -- 30 is detail files landed, of which only 22 are ON the roster and 8 are transitive children NOT on it. TRUE ROSTER COVERAGE IS 22 OF 64, so the gap is 42 models and not 34; and AC3 asks for exactly the comparison the TO's face number cannot support.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "re-derived from today's own 06:00Z artifacts, not from the TO: roster (rebalancer_models page_000 totalResultCount) = 64; detail files landed = 30; ON the roster = 22; NOT on roster (transitive children) = 8",
    "_is_opal seeds on roster = 22, ALL 22 pulled -- and 22 + 8 = 30 RECONCILES EXACTLY",
    "CONTROLS RUN BOTH WAYS: casefold control (8 still absent), positive control (a known roster id resolves), negative control (bogus id -> False)",
    "the authorised change is APPLIED and LANDED before surfacing: MODEL_DETAIL_SCOPE=all live per get-function-configuration, LastModified 2026-08-25T09:50:45+0000, ledger cotmdl-model-detail-scope-all CLOSED, 3 legs proven"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "THE ISSUER of WSE_COTMDL's TO (routing per Rule 27; 1.0.0_SA_CTO / 2.0.0_SA_COO to confirm which holds it) -- the remedy is a CODE change and the surfacing seat's TO explicitly is not one. ⛔ ARMED WITH A NAMED MATERIALISATION: 2026-08-26T06:00Z, the next scheduled run.",
  "notes": "⛔ THE DEFECT IS WORSE THAN THE TO STATES, WHICH STRENGTHENS THE AUTHORISATION RATHER THAN WEAKENING IT -- the surfacing seat says so explicitly, against the natural incentive to let a favourable-looking number stand. The gap is 42, not 34. || WHY IT IS A GRAIN MISMATCH AND NOT AN ARITHMETIC ERROR: '30' counts DETAIL FILES LANDED and '64' counts ROSTER MODELS. Both numbers are true of their own population and the RATIO IS TRUE OF NEITHER. Rule 24(ii), same-grain, violated across the numerator and denominator of a single quoted fraction -- and a fraction is exactly the shape that hides it, because it presents as one measurement. || AND AC3 ASKS FOR THE COMPARISON THE FACE NUMBER CANNOT SUPPORT, so the criterion is currently discharged by quoting a figure that does not mean what the criterion needs. That is the acceptance-surface class this fabric has hit repeatedly: a criterion satisfiable by a true statement about the wrong population. || SECOND LIMB, SAME ITEM: scope=all ALSO DROPS 8 SUB-MODELS -- the transitive children that are not on the roster. So the two populations are not merely mis-ratioed, they are each incomplete in a different direction. || METHOD NOTE WORTH KEEPING: the surfacing seat LANDED THE AUTHORISED WORK FIRST AND THEN SURFACED, so no work was held while the finding was written. Rule 27 permits surfacing without holding, and this is the specimen of doing both correctly in one turn."
 }
]
```
