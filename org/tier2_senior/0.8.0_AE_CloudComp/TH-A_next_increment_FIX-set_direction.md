# TH-A EFFECTIVE-probe — next-increment direction (CAPTURED, HELD)

**Status:** HELD — CTO stand-down 2026-07-12T~16:19Z. The keystone dispatch ("complete
the keystone") is DONE (last landed item: vendored sovereign_held mirror `c49144301`).
This is the CTO-pre-approved design-gated direction for the NEXT increment, to **resume
on an Andrew re-dispatch or a deliberate capacity decision** — NOT an open-ended auto-extend.

## Where TH-A stands (grounded 2026-07-12, live comp-tool-health Phase-B)
- EFFECTIVE bools produced for **4 tools**: comp-which=no (FIX), comp-freshness=no (FIX),
  comp-iam=yes (KEEP), comp-aws=yes (KEEP). Committed regression guards:
  `60c6dca97` (comp-aws garbage-reject), `729adfe5a` (comp-iam resource-discrimination),
  `08be45523` (D2 partition-key), `3e5fad954` (probe A+B, off-bd re-point + tristate feed).
- **57 tools pending_effective.** verdict counts `{FIX:2, FIX?:6, RETIRE?:5, KEEP:2, KEEP?:51}`.
- **RETIRE?-PREVENTIVE subset is EMPTY** (finding): `_PREVENTIVE_RX` matches only
  `-check|gate|validate|guard|audit|lint` gates, and every such gate is heavily USED
  (comp-surface-check 5869, comp-validate 264, comp-manifest-check 136, comp-coverage-check 73).
  CVO~B's asymmetry fix `24a4a0822` is a correct **LATENT** guard — it fires the instant a
  preventive gate goes not-used; no live row exercises the RETIRE?-PREVENTIVE render today.

## Next-increment TARGET (CTO pre-approved)
The populated highest-value target now = the **FIX? value-grounded-low set**:
`comp-drift, comp-constants, comp-tooltip, comp-denytest, comp-registry, comp-deadgrant`
(all mean OUTCOME value < 0.6). An EFFECTIVE bool there **corroborates or refutes the value-FIX**:
- effective=False + low value  -> confirmed FIX (value-low AND not effective).
- effective=True  + low value  -> effective-but-low-observed — re-examine the value anchor / a routing-HUD issue.

Framing (REFINED by CVO~B handshake 20260712T162037Z -- supersedes "corroborates/refutes the
value-FIX"): the EFFECTIVE axis is ORTHOGONAL to VALUE, so an effective bool does NOT refute the
value verdict -- it DISAMBIGUATES the FIX? MECHANISM:
- effective="no"  => FUNCTIONAL-FIX (the tool doesn't even reach an answer -- a real defect, the
  high-value catch, like comp-freshness). 
- effective="yes" => WORKS-but-low-value (reaches an answer; the concern is value/adoption, not
  function -> a DIFFERENT remedy than a functional fix).
Each probe case is individually CTO-design-gated (same discipline as the comp-aws/comp-iam cases).

INTERFACE CONTRACT -- CONFIRMED by CVO~B (probe owner) + the ONE load-bearing invariant:
- not-used tool: same reach x usability oracle (run on a representative ws scenario; effective=True
  iff it reaches a usable answer). Usage-independent -- a not-used tool CAN be effective (-> PROMOTE).
- The probe emits a TRISTATE STRING "yes"|"no"|"unknown". The seam MUST map "yes"->True->PROMOTE /
  "no"->False->RETIRE / **"unknown"->None->HOLD (NEVER False)**. Absent-from-feed == None == HOLD.
  This is the CANNOT-EVALUATE-vs-FAIL law: "no"=MEASURED-not-effective (may retire); "unknown"=
  COULD-NOT-MEASURE (must hold). unknown->False would silently RETIRE an unmeasured tool.
- VERIFIED at HEAD (2026-07-12): _effective_to_bool + load_effective_feed implement this exactly
  (exercised across 15 inputs). LOCKED by a non-vacuous regression test
  `org/modules/graph/tests/test_effective_feed_unknown_never_false.py` (commit 4646ee3cd) so it
  cannot silently regress. Each not-used tool needs a CORPUS PROBE (blind Q + sealed A); no
  authorable scenario => emit "unknown", never a silent False. CVO~B offered to author the corpus
  probes for the FIX?-value-low set at resume (probe side = theirs; seam side = mine).

## Resume trigger
Andrew re-dispatch OR a deliberate COO/CTO capacity decision. Do NOT auto-arm.
