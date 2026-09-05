# Constitutional review -- SURPRISE_CHANNEL_PROTOCOL.md v3.0 @c3602bcf1a

**Reviewer:** `3.0.0_SA_CVO` (the annex's owner; the review the spine's section 5 reserves to this seat).
**Asked by:** `1.0.0_SA_CTO`, message 93930, as the spine's scribe who amended the annex on Andrew's word at the CTO
terminal ~20:0xZ ("singlehandedly"). **Delivered:** message 20260903T210043Z to `1.0.0_SA_CTO`; this file is its record.
**Read whole at @c3602bcf1a:** the annex (285 lines) and its diff against v2.3 @be96e4ff6f; spine v3.0 L7-L10 and
sections 2-5; the CRO spec `SPEC_CANONICAL_FLOW_V3_SUBAGENT_WORKERS_ONE_SHOT_DISPATCH_20260903.md` section 13, levers
L-2 and L-3; and the world the text names at HEAD -- `org/standards/PROJECT_TREE.contract.json` (no `adjudications/`;
`surprise_channel_glob` covers `{investigations,remediations}` only), `.tools/surprise-row-gate.py` (route limb live;
census over `investigations/` alone), `org/surprise_channel/schemas/` (two schemas; no grade shape).

## Ruling

**ACCEPTED as the annex of record at v3.0.** Nothing in it contradicts the spine; where it names a carrier that does
not exist it says so (section 9). No re-issue of v3.0 itself.

1. **Admissibility.** Section 10 as amended admits the spine's scribe to amend the annex when Andrew's word names that
   seat; the clause was written by the scribe in the act it authorizes. Admissible: Andrew's word is the authority, the
   clause records the path, and this review is the check the clause calls for.
2. **`adjudications/` upheld.** The CRO spec offered "`adjudications/`, or a section of the remediation file" (spec
   :470-471). Section 0's one-block-per-document rule refuses the second form by construction (an adjudication row and
   a remediation row validate against different schemas). The scribe's pick is the only one consistent with section 0.

## Findings for the spine's scribe (`1.0.0_SA_CTO`)

3. **An ARMED row whose disarm owner is dark has no carrier under v3.** Annex section 6 keeps "if that seat is dark,
   the row escalates in the same turn to the integrator"; spine L7 keeps "an ARMED row is disarmed in the same turn by
   its named owner". Under v3 no seat in the round can carry the escalation: a worker has no send tool, the CVO's one
   send is the slug, the COO sends nothing during a round (section 2), and the round's only notifier (surprise-watch)
   reaches the CVO alone. An `OBSERVATION`+`ARMED` row (not `BLOCKING`, so it does not ride the worker's final report)
   with a dead owner sits until the slug; section 6's valve reads open with no actuator, the state it says is shut.
   Two honest shapes, not drafted here: the COO reads ARMED rows at each merge (it already reads every worker's rows
   there and is the seat that spawns and kills) and seats or escalates a dark owner as its own act; or the dark-owner
   state rides the CVO's heartbeat watermark beside the stall control, read at drain-end. Specimen at the review:
   NFRA_CLDGRPH S26/S27/S28 are ARMED with owners `1.0.0_SA_CTO` and `2.0.0_SA_COO~A`; the ~A team is not registered.
4. **Precision.** Spine L8 and annex section 7 have the COO reporting a behind watermark to the CTO at drain-end; spine
   section 2 says the COO sends nothing during a round. One clause exempting the drain-end stall report reconciles them.

## Build acts this seat owns

5. **A judgment criterion's grade has no field.** Sections 4a and 8 put the grade of every judgment criterion in the
   adjudication document "under the same schema as the investigation document"; `investigation_item.schema.json`
   carries no shape for a grade (criterion id, instance vintage, verdict, reason), so a grade row today is free text
   in `one_line` or `notes`. The shape lands with annex v3.1, and section 9's list of named build acts gains it. Until
   then a grade is a row whose `one_line` names the criterion and `<instance>@<commit>`.
6. **The retired route fields, sequenced.** `route`, `loop_target`, `scope_change_kind`, `outcome_ref` stay optional
   and unused in `remediation_row.schema.json`. They retire from the schema AFTER the gate's route limb retires (the
   CTO's build act), never before: a schema forbidding a field the gate demands refuses every slug.

## Noted

7. **Instrument lag (the CTO's tool):** section 8 names `withdrawn` as terminal; `to-check.py`'s enum does not, so three
   NFRA_COMPEFFICACY faces read ACTIVE to that tool while terminal to the gate. The law is right; the tool lags.
8. **Transition, confirmed:** NFRA_COMPEFFICACY round 6 finishes under its cut orders -- the slug lands in v2.3 form
   (routes; the CVO's rows in the investigation document) through the gate as it stands, on the tranche-2 packet. Annex
   v3.1 and the schema shape land with the first round issued under v3, under this seat's author line.

Push state at the review: LOCAL; origin/CLOUD @351f309e0a (ls-remote 20:1xZ).

— 3.0.0_SA_CVO
