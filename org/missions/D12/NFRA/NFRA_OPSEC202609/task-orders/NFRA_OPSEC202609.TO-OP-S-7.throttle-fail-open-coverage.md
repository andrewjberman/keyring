# TO NFRA_OPSEC202609.TO-OP-S-7 -- LOSING THE THROTTLE'S BOOKKEEPING MUST NOT OPEN THE DOOR WIDER: prove what actually holds the login path when `throttle.ts` fails open, and close the gap that read finds -- **the fail-open is DELIBERATE and is NOT to be removed** (OP-s-7, FWD-7)

<to_id>NFRA_OPSEC202609.TO-OP-S-7</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT **FWD-7**; s.8 row S7; the `PORTAL_AUTHHARD` note at :233) - **Decomp cell:** `OP-s-7` (v0.1.10 @2fd3843047, s.1a) - **Lane:** `infra/aws/opalinvest_dev/lambda/auth-handler/src/throttle.ts` (AE lane, per the 09-02 OTP deploy precedent) - **Round:** 3 of NFRA_OPSEC202609. **Dispatch:** GO after `TO-OP-S-1` goes terminal -- one task order at a time.

---

## ⛔ READ THIS BEFORE ANYTHING ELSE: THE FAIL-OPEN IS NOT THE BUG

**FWD-7's DONE WHEN, verbatim from the endpoint at :109: *"Losing the login throttle's bookkeeping never opens the door wider."*** It does **not** say the throttle must fail closed. And PRD :233 says in terms that `PORTAL_AUTHHARD`'s throttle design *"is the starting point of FWD-7, not something to replace."*

**The source defends the fail-open explicitly and the defence is sound.** Read at this cut:
- `:103` -- *"a rate-limiter must never take down login."*
- `:11` -- *"Progressive delay / temporary cooldown -- NEVER a hard lockout."*
- `:42` -- *"maximum cooldown -- never a permanent lockout."*
- `:59` -- *"KEYED ON THE ACCOUNT, NEVER ON THE DESTINATION NUMBER, AND THAT IS THE WHOLE DESIGN."*
- `:24` -- the response *"must never reveal whether the account exists (enumeration-safety)."*

>> **SO: MAKING `throttle.ts` FAIL CLOSED IS A STOP AND A ROW, NOT A DELIVERABLE.** A rate limiter that takes down login on a DynamoDB blip converts a bookkeeping failure into an outage, and that is a wider door than the one FWD-7 is about. **If your reading of this face ever points at `return; // fail-open`, re-read this section: it is pointing at the wrong thing.** <<

**THE QUESTION THIS FACE ACTUALLY ANSWERS: while the throttle is failing open, WHAT ELSE is holding the login path, and is it enough?** That is a measurement first and a build only if the measurement finds a gap.

## READ LIVE AT THIS CUT BY THE ISSUER (2026-09-03 19:2xZ; re-ground in phase 1 and STOP on any difference)

- **Three fail-open sites, not one.** `:112` GetItem failed, `:147` UpdateItem failed, `:164` set-block failed -- each logs `WARN: throttle ... (fail-open)` with a `key_type`. **The cell names `:112-114`; there are THREE. Grade all three.**
- **The IP-blindness has a CAUSE and it is upstream, not in this file.** `:14` -- *"the Lambda cannot see the real client IP -- `/auth/*` forwards no `CloudFront-*` headers."* **So "IP-blind by design" is a consequence of the forwarding configuration, and that is a different surface from this one.**
- **A second control already exists on the same path:** `opal-cloudfront-protection` carries `AuthLoginRateLimit` at **priority 2, action `Block`** (read live). **That rule is IP-based and is NOT affected by a DynamoDB failure**, which makes it the obvious candidate for what holds the door while the throttle is blind.

## DELIVERABLE

1. **MEASURE THE COVERAGE, and this is the substance of the face.** With the throttle failing open, determine what still limits repeated login attempts. At minimum: does `AuthLoginRateLimit` fire on the `/auth/login` path, at what threshold, on what key, and does its scope actually cover the requests the throttle would have counted? **Name the threshold and the evaluation window as READ values, never as recalled ones.**
2. **EXERCISE IT, do not infer it, under the `OP-x-1` probe verdict.** Drive the login path against the fixture identity hard enough to trip the WAF rule while the throttle's table is untouched, and capture the block. **Then the discriminating half: exercise the SAME burst in a condition where the throttle's bookkeeping is unavailable and show the WAF rule still blocks.** How you produce the second condition is yours to design and to state -- a temporary IAM deny on the throttle table's `GetItem` for the handler role is the obvious shape and is reversible; **if you choose it, it goes in the ledger with its rollback and it is reverted in the same window.** ⛔ **Never make the table itself unavailable** -- that is a live dependency of a live login path.
3. **REPORT THE GAP, do not silently close it.** If the WAF rule covers the fail-open window, FWD-7 is served by evidence and this face builds nothing. **If it does not** -- wrong path, wrong scope, threshold too high to matter, or it keys on something the burst does not vary -- **that is the finding, it goes in a ROW, and the remedy is a separate cut.** Do not invent a remedy inside this face.
4. **THE ENUMERATION-SAFETY PROPERTY IS A BOUND ON YOUR PROBE, not a target:** `:24` says the response must never reveal whether an account exists. **Your burst must not use a real partner human's address**, and any response bodies you paste must be checked so the proof itself does not become the disclosure.
5. **A deploy-ledger entry ONLY IF you make a change** (including a temporary IAM deny), opened before and closed after, with the rollback named and REVERTED in the same window. **If the face ends as a pure measurement, say so and open no ledger.**
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-7.throttle-fail-open-coverage.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S7-AC1" cell_refs="OP-s-7"/> `S7-AC1` -- THE THREE FAIL-OPEN SITES ARE ENUMERATED AT SOURCE WITH A VINTAGE: `:112`, `:147`, `:164` quoted with `file:line @ <commit-ish>`, each with the operation that fails and the `key_type` it logs. Denominator: fail-open sites found of sites in the file, printed. **A count of one is a FAIL** -- the cell's own `:112-114` was the incomplete read this criterion exists to correct.
<criterion id="S7-AC2" cell_refs="OP-s-7"/> `S7-AC2` -- THE SECOND CONTROL IS IDENTIFIED AND ITS PARAMETERS ARE READ, NOT RECALLED: the rule holding the login path named, with its live threshold, evaluation window, key and scope pasted from `get-web-acl`, plus the explicit statement of whether its scope covers the `/auth/login` requests the throttle counts. **"It exists" is not the criterion; "it covers these requests at this threshold" is.**
<criterion id="S7-AC3" cell_refs="OP-s-7"/> `S7-AC3` -- THE COVERAGE IS EXERCISED IN BOTH CONDITIONS AND THEY DIFFER: a burst with the throttle healthy (captured: what blocked, and which control blocked it) and a burst with the throttle's bookkeeping unavailable (captured: same). **The discriminator is that the second condition still blocks.** State the method used to create the second condition, its ledger entry and that it was reverted. **If the two conditions cannot be distinguished by the evidence, this files `UNCOMPUTABLE` with the reason** -- an undifferentiated pair proves nothing about the fail-open window.
<criterion id="S7-AC4" cell_refs="OP-s-7"/> `S7-AC4` -- THE VERDICT IS STATED AS A VERDICT: either **FWD-7 IS SERVED** by the measured coverage, with the reasoning and the numbers, or **A GAP EXISTS**, named precisely, with a row id, and explicitly NOT remediated in this face. **Both are PASS outcomes for this criterion; the FAIL is an unstated verdict or a silently-closed gap.**
<criterion id="S7-AC5" cell_refs="OP-s-7"/> `S7-AC5` -- NOTHING WAS MADE FAIL-CLOSED AND NOTHING PERMANENT CHANGED: a diff census of `throttle.ts` against HEAD showing **0 changes to its fail-open behaviour**, and a census of any temporary change made for AC3 showing it is REVERTED, read on the APPLIED plane after the revert with a positive control. The login path is left exactly as found.

<expected_criteria>S7-AC1, S7-AC2, S7-AC3, S7-AC4, S7-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @2fd3843047 (v0.1.10), cell `OP-s-7` (manifest S7; FWD-7; value EXERCISED).
<owned_cells>OP-s-7</owned_cells>
Read-dependencies, NOT claimed: `OP-s-4` (the CloudFront ACL whose `AuthLoginRateLimit` rule is the likely second control -- read it, do not edit it; its managed-group work is `TO-OP-S-4-18`'s), `OP-x-1` (the probe verdict authorising the burst).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). This face builds no monitor and carries no moratorium exception; a gap it finds is a ROW, never an alarm.
comp-iam: DECLARED-NOT-APPLICABLE at cut -- this face creates no role and attaches no standing policy. IF the assignee uses a temporary IAM deny to produce AC3's second condition, that is a live-plane act verified by its own before/after reads and its ledger revert, not by a DESIRED-plane lens.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S7-AC1), which is where the vintage discipline actually binds.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S7-AC1`, `S7-AC2`, `S7-AC3`, `S7-AC4`, `S7-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-7.throttle-fail-open-coverage.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S7-AC1,S7-AC2,S7-AC3,S7-AC4,S7-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S7-AC3`'s second condition: if the burst blocks identically whether or not the throttle can read its table, the evidence does not discriminate and the criterion must say so rather than claim coverage.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-read `throttle.ts` at HEAD and re-count the fail-open sites; re-read the CloudFront ACL's rule set. STOP on any difference from the reads quoted above.</phase>
  <phase id="2" when="before any probe">A broker drain, and the OP-x-1 verdict's bounds re-read rather than recalled.</phase>
  <phase id="3" when="after the probe">The revert verified on the APPLIED plane with a positive control, before the instance is written.</phase>
</compiler_tools_mandate>
