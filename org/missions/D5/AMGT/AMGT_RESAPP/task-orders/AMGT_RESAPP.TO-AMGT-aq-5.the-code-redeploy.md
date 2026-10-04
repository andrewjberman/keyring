# AMGT_RESAPP task order -- `AMGT-aq-5` -- THE CODE REDEPLOY CARRYING aq-1..aq-4 (FWD-39 REPAIR, FWD-36 TONE, FWD-38 (d), Z-S86)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aq-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- 0 new actions: the act carries code only, so the plan must show NO IAM change.
BLIND: no IAM simulation was run for this act (0 new actions); the criteria read served fields off the deployed function, so a denied read shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- on deployed FcVBPafw, r67_served c23, c24, c25 and c26 FAIL.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-aq-5` (round 67, decomposition s.75)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying aq-1 to
aq-4. Build and upload ONE artifact, then ONE code-only `safe-apply`. `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed. Then:
- Re-read the base CodeSha256 the halves name live before the build. A moved base is a STOP.
- Build from a detached checkout at the build commit. Any CHANGED/ADDED/REMOVED file not on the halves' list is a STOP.
- Any destroy, IAM, route or gateway change in a plan is a STOP.
- The package is at 96.8% of the 262,144,000 B ceiling: print the build's size, and a build over the ceiling is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No memory change, no store write, no S3 delete, no vendor call, no push of shared branches, no portal
   promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aq-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c23 --where deployed; echo "exit=$?"</invocation><expect>run from a checkout at the build commit: C1, C2 and C3 PASS over every served payload; R67 C23 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aq-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c24 --where deployed; echo "exit=$?"</invocation><expect>on each of days=30, 90 and 365 C1 prints mismatches 0, old-reason 0 and a no-table-row count equal to a local read of the same check run beside it (21 at the pin; row AMGT_RESAPP-Z-W220-S1), so R67 C24 SERVED: NO comes from that one clause alone</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aq-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c25 c26; do PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R67 C25 and C26 SERVED: YES on the deployed function; and exit=0</expect></criterion>
</proof_of_spec>

The following are run with them and reported (no regression), and the issuer re-reads them:
- `r64_served.py --cell c9 / c10 / c11 / c12 / c13 / c14 --where deployed`;
- `r65_served.py --cell c17` and `r66_served.py --cell c18 / c19 / c22 --where deployed`;
- `r64_served.py --cell c15 --where deployed`, cold, on the day route;
- the RANGE route's cold read (BA `/security/BA_US_Equity/timeline?from=2026-09-01&to=<today>`). Over 5 s is reported, not rolled
  back.

## 4a. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-04 ~20:3xZ) -- the pin, a grant leg, and AC2's expectation

**The build commit is `d8bafe6896`,** or a descendant whose CONTENT-DIFF equals CHANGED 5 + ADDED 1:
- `scoped_amgt.py`, `monthly_chatter.py`, `rolling_windows.py`;
- `infra/logic/registry/reporting_policies.json`, `infra/logic/registry/systems.json`;
- ADDED `lib/research/coverage/covered_no_block.py`.

**THE ACT IS NOW TWO LEGS, in this order (row `AMGT_RESAPP-Z-S345`).** aq-4 reads
`s3://opal-data-portal-v2/json/security_scanner/latest/universes/sp500/universe_data.json` at request time. The role reads it as
implicitDeny today, so without the grant every unknown `_US_Equity` key turns from 404 into 502.
1. **Grant leg first.**
   - Add exactly this statement to `scoped_amgt_api_grants` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`:
     `Sid = "ReadTheScannerSp500UniverseForCoveredNoBlock"`, `Action = ["s3:GetObject"]`,
     `Resource = ["arn:aws:s3:::opal-data-portal-v2/json/security_scanner/latest/universes/sp500/universe_data.json"]`.
   - `safe-apply` targeted at that role policy. The plan shows ONE in-place update of `opal-amgt-scoped-api-grants` and
     nothing else, or it is a STOP.
   - Then `simulate-principal-policy` on the role for that key must read `allowed`.
2. **Code leg.** As in section 1, at the pin above. Section 1's "any IAM change in a plan is a STOP" binds this leg.

**AC2** expects c24's one known clause, the producer gap of row `AMGT_RESAPP-Z-W220-S1`. Any mismatch, any old reason, or a
no-table-row count that differs from the local read is the rollback trigger.

**Also a rollback:** a 502 on any key.

Halves:
- COO: `deliverables/2.0.0_SA_COO~Z/round67/NEVER_WIDEN_HALF_COO_AQ5.md`;
- CTO: `ledger/NEVER_WIDEN_ROUND67_AQ5_CTO_HALF.md` (owed).

Gate limb that graded this modification: none. LIMB 6 fires only on a newly-added order, and GATE (viii) does not apply
(`<placeholders>NONE</placeholders>`).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-aq-5.the-code-redeploy.proof_of_spec.json`.
Report once:
- the prior and new CodeSha256 and artifact VersionId
- the CONTENT-DIFF summary and the package size
- every criterion's output lines
- the regression reads and both cold reads

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.75; staged until aq-1..aq-4 drain and the pair is signed.

<status>staged</status>
<round>67</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-04 ~21:0xZ):** both halves committed -- COO `round67/NEVER_WIDEN_HALF_COO_AQ5.md` @0e415a64d9,
CTO `ledger/NEVER_WIDEN_ROUND67_AQ5_CTO_HALF.md` @786d5e992e (SIGNED under conditions 1-5). Build commit `d8bafe6896`. Executor
`0.7.0_AE_CloudOps~A`, spawned with this GO.

<status>pending</status>
