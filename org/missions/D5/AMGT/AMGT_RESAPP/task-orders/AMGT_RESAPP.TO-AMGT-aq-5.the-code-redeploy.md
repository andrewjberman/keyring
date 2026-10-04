# AMGT_RESAPP task order -- `AMGT-aq-5` -- THE CODE REDEPLOY CARRYING aq-1..aq-4 (FWD-39 REPAIR, FWD-36 TONE, FWD-38 (d), Z-S86)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aq-5,AMGT-aq-6</owned_cells>
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
  <criterion id="AC2" cell_refs="AMGT-aq-5,AMGT-aq-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c24 --where deployed; echo "exit=$?"</invocation><expect>after leg 3, on each of days=30, 90 and 365: C2 PASS with unreadable 0, and C1 prints mismatches 0, old-reason 0 and a no-table-row count equal to a local read of the same check run beside it (21 at the cut; row AMGT_RESAPP-Z-W220-S1), so R67 C24 SERVED: NO comes from that one clause alone</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-aq-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_grant_aq6.sh"; echo "exit=$?"</invocation><expect>both controls PASS, and C1 (GetObject) and C2 (ListBucket with the s3:prefix context) PASS allowed on chatter_window/; R67 AQ6 GRANT: YES; and exit=0</expect></criterion>
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

## 4b. AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-04 ~22:4xZ) -- LEG 3, the chatter_window read grant (cell `AMGT-aq-6`, row Z-S346)

**Answer to your 29282: STAND. No rollback.** The CTO ruled in AMENDMENT 1 to its half (@14aa3c9200, msg 29280), and Andrew
endorsed it ("recs approved", record @c700426bc9). Close the current NEVER-2 entry with L4 recording "c24 NOT MET, cause Z-S346, no
rollback", so CORPUS al-5 can start. Then do leg 3 under a NEW entry.

**Leg 3:**
1. In `infra/aws/terraform/harvest/scoped-amgt-api.tf`, add ONE entry, `"amgt/harvest/gold/chatter_window/",` to
   `local.scoped_amgt_pool_prefixes`. The list drives both the GetObject resources and the ListBucket `s3:prefix` condition.
   Edit nothing else.
2. Run ONE `safe-apply` targeted at `aws_iam_role_policy.scoped_amgt_api_grants`. The plan is ONE in-place update of
   `opal-amgt-scoped-api-grants` whose only change is that prefix. Anything else is a STOP.
3. NO code change. **Serialize behind AMGT_CORPUS al-5.** Its NEVER-2 entry `amgt-corpus-r36-al5`
   (`org/critical_paths/.open_deploys/amgt-corpus-r36-al5.json`, opened @5907db84a4) redeploys this same function, at
   `288de3d95d`, which carries round 67 (`d8bafe6896` is its ancestor).
   - Begin leg 3 only when that entry is CLOSED, or not yet started with its L1 OPEN, and in that case say which.
   - The base CodeSha256 is the one read live at leg-3 start. It must be `aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=` or the
     new CodeSha256 that al-5's closed entry records. Any other value is a STOP.
   - Leg 3 must not move it.
4. Grade **AC4**, the applied-plane proof of the grant, then AC2 on deployed. AC4 is a fourth criterion because the grant has its
   own applied-plane proof, apart from the served read.
5. Re-read AC1 and AC3. They are unchanged by a policy-only act.

**AC2 at its full strictness now:** `r67_served.py` c24 gained C2 (@ the leg-3 cut), which counts the unreadable-table reason over
EVERY row. Base on deployed: FAIL, 95 of 95 per window. Local control: PASS, 0.
- **Rollback of leg 3** (a targeted apply with the entry removed): a regression against the base. That means mismatches above 74,
  a non-200, or c23/c25/c26 not YES.
- **STOP, reported with the simulate output:** C2 still FAIL after AC4 reads YES.

Halves:
- COO: `deliverables/2.0.0_SA_COO~Z/round67/NEVER_WIDEN_HALF_COO_AQ6.md`;
- CTO: `ledger/NEVER_WIDEN_ROUND67_AQ6_CTO_HALF.md` (owed).

**Begin leg 3 only on the issuer's GO** naming both halves committed.

**Why an amendment and not a new order.** `.tools/to-pipeline-gate.py`'s one-issuance limb refuses a second order in round 67 and
reads no override. A re-cut into the first issuance modifies its orders. aq-5 is non-terminal (AC2 FAIL) and holds the same
executor and function. Gate limb that graded this modification: GATE (viii) on a modify (`<placeholders>NONE</placeholders>`).

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
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-04 ~21:0xZ):** both halves committed -- COO `round67/NEVER_WIDEN_HALF_COO_AQ5.md` @0e415a64d9,
CTO `ledger/NEVER_WIDEN_ROUND67_AQ5_CTO_HALF.md` @786d5e992e (SIGNED under conditions 1-5). Build commit `d8bafe6896`. Executor
`0.7.0_AE_CloudOps~A`, spawned with this GO.

<status>pending</status>

**ISSUER GO, LEG 3 (2.0.0_SA_COO~Z, 2026-10-04 ~22:4xZ):** both aq-6 halves are committed.
- COO: `round67/NEVER_WIDEN_HALF_COO_AQ6.md` @4d3db86faa, amended @a8c4eb15c8.
- CTO: `ledger/NEVER_WIDEN_ROUND67_AQ6_CTO_HALF.md` @5468d18362, AMENDMENT 1 @5a8f3ce6ff (condition 3 reversed: leg 3 under its
  own NEVER-2 entry, after `amgt-corpus-r36-al5` closes).

Begin when that entry is CLOSED. The base is al-5's recorded CodeSha256, re-read live before the apply. Leg 3 moves no code.
Simulate (AC4) reads allowed before c24 (AC2) is read.

<status>pending</status>
