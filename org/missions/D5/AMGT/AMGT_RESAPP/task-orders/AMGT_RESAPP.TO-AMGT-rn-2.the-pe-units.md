# AMGT_RESAPP task order -- `AMGT-rn-2` -- THE P/E UNITS: the producer states them, the consumer applies them, and a magnitude criterion makes the class visible

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~147</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS; the lib change reaches the Lambda only on a deploy no cell cuts this round.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-rn-2` (round 39, decomposition s.47, 47b)

The Peers tab renders `P/E (trailing)` and `P/E (NTM)` 100x too small on 12 of 12 members (row `AMGT_RESAPP-Z-S265`). The
reciprocal EXISTS: `portal/src/pages/SecurityAnalysis/cscTable.ts:90-93` computes `1 / value` for codes `ey` and `ey_ntm`. The
defect is UNITS: the peers document the page renders carries `ey` as a PERCENT (`__harness__/tests/uiContractFixtures.json`, route
`/api/scoped/amgt/security/BA_US_Equity/peers`: DE `ey` 2.88, `factors.ey_ntm` 3.42), the package's own tests carry fractions
(`lib/research/peers/tests/test_csc_carry.py:17`), and the consumer assumes a fraction, so 1/2.88 = 0.35 renders where 34.7 is
the number. **Build, in this order:** (1) the producer STATES its semantics -- every `build_csc_map()` present entry whose
`relation` begins `RECIPROCAL` carries `transform: "reciprocal"` and `units: "percent"` or `"fraction"`, read from the factor
registry's own unit for the code (`factor_metadata.json`; if the registry names none, state `"percent"` on the measured fixture
values and say so in the report), with a test in `lib/research/peers/tests/`; (2) the consumer APPLIES it -- `cscTable.ts` reads the
entry's `transform` and `units` (`types.ts` gains the two optional fields) and computes `100 / x` for percent, `1 / x` for fraction,
`null` when the entry carries no `transform`; the code-name switch at `:90` goes; (3) the captured fixtures' map entries for `ey`
and `ey_ntm` are patched to carry the two fields (`uiContractFixtures.json` and every `tabsFixture.*.json`), nothing else in them
touched. Report the LIVE unit the registry names, verbatim.

## 2. BOUNDS

1. **No server.** The render is graded by the issuer after the merge; your criteria are the files below.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-147-portal` at DEV `5e339ffd`. Python from the
   repo root with `PYTHONPATH="$(pwd)"`.
3. No other column, route, DTO or served figure moves. Standing: no install, no push, no promote. REFUSE, do not rescue.

## 3. SURFACES

<paths>
lib/research/peers/csc.py
lib/research/peers/tests/**
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BABA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.COST_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.HD_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.SAP_GY_Equity.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~147/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-2.AC1.py; echo "exit=$?"</invocation><expect>RECIPROCAL entries carrying transform+units: 2 of 2 (present columns: 5) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-2.AC2.cjs; echo "exit=$?"</invocation><expect>THE MAGNITUDE CRITERION: members: 12; P/E values in [0.5,200]: 24 of 24 (null: 0); out-of-band samples: none -- and exit=0 (a null count above 0 is reported with which member and column)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-2.AC3.sh; echo "exit=$?"</invocation><expect>the peers package's tests all pass, the cell's new units test among them (N passed, 0 failed), exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~147/AMGT_RESAPP.TO-AMGT-rn-2.the-pe-units.proof_of_spec.json`.
Report names the registry's unit for `ey`/`ey_ntm` verbatim, the before/after value for one member, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 3, the highest consequence. Sized at 47b: the reciprocal exists (the CVO's "no locatable implementation"
is corrected there), the unit is the fault. Worker class `worker` (three surfaces, tests). The magnitude criterion is the class
remedy the analysis owes (s.4).

**ISSUER CLOSE, 2.0.0_SA_COO~Z, 2026-09-24 ~19:0xZ, carried on the worker's branch so the chain-end merge carries it.**
Checker's match: proof-of-spec-check VALID rc=0 on the worker's instance (3 of 3 PASS-by-output); not re-run by the issuer.
AC1: RECIPROCAL entries carrying transform+units 2 of 2. AC2, THE MAGNITUDE CRITERION: P/E values in [0.5,200] 24 of 24, null 0
(base read 5 of 24). AC3: peers package 34 passed. The registry names NO unit: the scanner's factor registry
(`infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json` @18f7a03a63, 289 factors) carries no `unit`
field on any factor, so `units="percent"` is stated on the measured served-fixture scale under the face's own fallback clause.
BA before/after: ey 2.88187 rendered 0.35, now 34.7. No rows. **Carried, not closed:** the live producer's unit is INFERRED from
the captured fixture's magnitude, never declared by the source; a registry `unit` field is the source-side fix and goes to the
next list. The render grade (the Peers tab showing P/E in plausible magnitudes) is the issuer's real run on 5174 after the
round's last merge. Portal merged 9b246d3f -> DEV 4501c543.

<status>complete</status>
<round>39</round>
<slot>~147</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
