# MDPF_COTREMEDIATION -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive
Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25T16:4xZ on three items routed to this seat while it was dark, both
issuers filing correctly rather than writing this tree themselves (executing seats are barred from
it -- COO ruling 2026-08-24). **All three are OBSERVATION x INERT** -- no BLOCKING item, no ARMED
item, no disarm owner required. The live client-facing hazard (cottonwood + global served payloads
frozen at 2026-08-19, four trading days, NEVER#1 discharged) is **already owned under D8** and is
not a channel item; nothing here adds exposure to it.

**Issuer messages:** `1.0.0_SA_CTO` 70743 (16:09Z) · `2.0.0_SA_COO` 70753 (16:30Z). Both ACKed by
this seat 16:3xZ.

**Verifier note on S1:** the relay was re-derived at source by this seat before graduation, and the
re-derivation **widened it** -- see the item's `notes`. A relay carries its grounding or its caveat
(XXX.md relayer half); this one carried its grounding and was still narrower than the truth.

```json
[
 {
  "id": "MDPF_COTREMEDIATION-S1",
  "surfaced_by": "1.0.0_SA_CTO (msg 70743), routed explicitly as class OBSERVATION / standing INERT while re-verifying the root cause under Andrew's order to check it first",
  "surfaced_at": "2026-08-25T16:09Z",
  "one_line": "The exception class is called VendorDriftError -- IT NAMES AN ATTRIBUTION, NOT A CONDITION. The condition it detects is 'observed header != declared header', which is agnostic about who moved; by calling that VENDOR drift it hands every reader a causal story for free, and the story was wrong here.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "class VendorDriftError(ValueError) at data/assets/scripts/silver/mirror_conversion.py:133 -- DEF band, re-derived by 3.0.0_SA_CVO 2026-08-25T16:4xZ, not taken on relay",
    "comp-find 'VendorDriftError' DENOMINATOR: 111 hit(s) across 26575 file(s) scanned; BANDS DEF=5 SURFACED=66 CONFIG=5 TEST=16 DOC=19",
    "the falsifying fact: commit 17c38a26f2, author 0.6.2_AE_PartnerETL, 2026-08-20T17:56:24Z -- 'daily holdings template 226355 amended IN PLACE per CTO pin (B) -- {Holding Supervised, Account Supervised} added'. AN OPAL AGENT CHANGED THE VENDOR EXPORT TEMPLATE; THE VENDOR CHANGED NOTHING",
    "CTO grounded the overturn at three independent layers with no shared instrument: the vendor xlsx read directly with openpyxl (19 cols vs 21), live CloudWatch filter-log-events on opal-assets-silver-blackdiamond (observed=21 / declared=19), and our own git history",
    "the superseded record is 079b1b770e, 'ROOT CAUSE CONFIRMED ... THE LAMBDA CODE DID NOT CHANGE. THE VENDOR DID.'"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ VERIFIER ADDITION -- THE RENAME IS FIVE DEFINITION HOMES, NOT ONE, AND THE ISSUER DID NOT HAVE THIS. class VendorDriftError is DEFINED at FIVE sites: data/assets/scripts/silver/mirror_conversion.py:133 · opal-assets-silver-blackdiamond/mirror_conversion.py:133 · opal-assets-silver-eclipse/mirror_conversion.py:99 · opal-assets-silver-etf/mirror_conversion.py:101 · opal-assets-silver-orion/mirror_conversion.py:101. So the misnaming is estate-wide across FOUR converter families, not a cottonwood artifact, and 66 SURFACED raise-sites carry it. || THE FIRST TWO OF THOSE FIVE ARE THE SAME LOGICAL FILE IN TWO INDEPENDENTLY-EDITABLE HOMES -- the identical Rule-22a two-homes pair CTO named for mirror_schemas.py:460. A rename that moves one and not the other reads CLEAN and diverges silently. || THE RENAME IS NOT COSMETIC AND THAT IS THE WHOLE ITEM: the guard FIRED CORRECTLY and refused bad data. What failed was the NAME, which pre-encoded an attribution into a detection -- and the seat that misread it was the same CTO seat that had issued the pin authorising the amendment. A false attribution of a GOOD act (a working guard) is the class that survives unchallenged, because credit is never contested. Rename candidate carried from the issuer: HeaderContractMismatch. || SCOPE FENCE: this graduates as a NAMING act, and naming acts are Andrew's to ratify. It does NOT authorise touching the detection logic, and it must not ride the outage repair."
 },
 {
  "id": "MDPF_COTREMEDIATION-S2",
  "surfaced_by": "2.0.0_SA_COO (msg 70753), from the stage-3 atom-decomp of MDPF_COTREMEDIATION",
  "surfaced_at": "2026-08-25T16:30Z",
  "one_line": "The two payload leads carried in MDPF_COTREMEDIATION_PRD.md s.3 DO NOT REPRODUCE against the served platinum keys -- L1 ('cottonwood dates array almost entirely None, hundreds of nulls') measures 0 nulls of 458, unique 458, sorted True; L2 ('global tail repeats 2026-07-22 ~15x') measures a consecutive 08-10..08-19 tail with zero repeats.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured by 2.0.0_SA_COO against the SERVED platinum keys at 16:2xZ: cottonwood nulls = 0 of 458, unique = 458, sorted = True",
    "global tail measured as 2026-08-10 ... 2026-08-19 consecutive, zero repeats",
    "the leads' origin is 1.0.0_SA_CTO msg 70736 (14:36Z), where they were surfaced explicitly as signatures to hand to the TO holder, not as diagnoses",
    "DENOMINATOR NOTE: both measurements are on the SERVED plane; the original observation's plane is UNNAMED, which is the item"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "⛔ RECORDED AS RELOCATED, NOT REFUTED -- and that framing IS the item, carried verbatim from the issuer. Whoever observed a null-filled array observed it on SOME artifact: the gold object, D_05, a per-model series, or a different field. AN UNREPRODUCED OBSERVATION IS AN OPEN QUESTION ABOUT THE INSTRUMENT, NOT A CLOSED ONE ABOUT THE WORLD. || THE GUARDED FAILURE MODE, named by the issuer and endorsed here: a downstream seat reads 'L1 did not reproduce' as 'L1 was imaginary' and drops AC5. The PRD's own trap already binds -- a clean re-run does not establish cause, and AC5 stays UNMET if the null-fill is never explained. || THIS IS THE WRONG-PLANE CLASS IN ITS EXACT CANONICAL FORM (CLAUDE.md Git section, designed half): a sweep answers the question ITS PLANE can answer, and NO CONTROL INSIDE THE WRONG PLANE CAN CATCH A WRONG-PLANE ERROR. Both COO's measurement and the original observation are individually well-formed; they are about different planes, and neither output carries its plane. RESOLUTION PATH: name the plane of the ORIGINAL observation before adjudicating either reading. It stays UNDER_INVESTIGATION -- an open item blocks the zero-graduation round by design, which is correct here."
 },
 {
  "id": "MDPF_COTREMEDIATION-S3",
  "surfaced_by": "2.0.0_SA_COO (msg 70753), found while confirming S2 -- a second, older defect surfaced by running the set difference in BOTH directions",
  "surfaced_at": "2026-08-25T16:30Z",
  "one_line": "cottonwood and global carry NINE NON-TRADING DAYS that 49financial and inflection exclude -- 8 weekend days plus 2026-06-19 (Juneteenth) -- a data-quality defect that PREDATES the freeze, SURVIVES it, and that a re-run will not touch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "9 of 9 confirmed against lib/trading_calendar.is_trading_day -- the ONE frontier definition named by CLAUDE.md NEVER#1, not a hand-rolled weekday test",
    "POSITIVE CONTROL FIRING on the same predicate: is_trading_day('2026-08-19') = True, is_trading_day('2026-08-24') = True -- so the nine Falses are discriminated, not a uniformly-False instrument",
    "the contrast set is the discriminator: 49financial and inflection exclude all nine, cottonwood and global include them -- a two-partner difference on one predicate",
    "independent of the freeze by construction: predates it, survives it, unaffected by re-running the three frozen partitions"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ EXPLICITLY BARRED FROM RIDING THE OUTAGE REPAIR, and the reason is the item's operative half: folding a data-quality investigation into a P0 makes the P0 wait on it. Routed to D8 as 'in pattern' work per Andrew's own two-part instruction ('fixed immediately' AND 'take this as an opportunity'). || INERT is the correct standing and it is a real defect at the same time: wrong dates in a client-facing series is a genuine quality problem, but nothing about it is armed or time-critical -- no future ordinary act encounters it and is harmed. Standing is not severity. || METHOD NOTE WORTH KEEPING PAST THIS ITEM, carried from the issuer: both S2 and S3 came out of running ONE set difference in BOTH directions. The other direction returned the tightest confirmation of the outage on the page. AN ASYMMETRIC CHECK WOULD HAVE PRODUCED A CLEAN, CORRECT, COMPLETE-LOOKING CONFIRMATION AND REVEALED NEITHER ITEM."
 }
]
```

## Open at this seat, NOT a channel item

`2.0.0_SA_COO` disclosed (msg 70753 item 3) that the stage-3 decomp at
`workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/` (38 cells, @7807a52e75,
LOCAL -- rides integration) is **SOLO and UNCERTIFIED** because no Tier-2 cohort and no CVO were
live at authoring, and that **every TO cut from it carries "UNCERTIFIED DECOMP" stated by the
issuer**. That is a disclosure done correctly, not a surprise: COO did not queue behind a dark seat
on a live client-facing outage, which is what the pipeline's degraded-state clause asks for.

**The cert is owed and it is this seat's.** It is tracked as CVO work, not as an item in this round;
if the certification invalidates cells, the re-decomp is COO's and re-certification routes to an
independent signer (base CTO -- CRO is off-limits per Andrew).
