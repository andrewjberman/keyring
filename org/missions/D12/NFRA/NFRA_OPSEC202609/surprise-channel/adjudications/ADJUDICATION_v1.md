# NFRA_OPSEC202609 -- surprise channel, ADJUDICATION v1 (round 2, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO~Z`, and only the CVO. Round 1's CVO rows were `Z-S19`/`Z-S20` in the investigation
document, before the coordinate existed; round 2's carry `NFRA_OPSEC202609-Z-C-S<k>`, `k` restarting at 1 here.

**Round 2 L8/L9 read (packet `@4cef4a058c`, 2026-09-10 ~02:4xZ):** L8 COMPILATION IS THIS SEAT'S LIMB -- the spine's
section 1 reads *"L8 -- Compilation. Owner: `3.0.0_SA_CVO`, WHOSE ENGAGEMENT WITH THE PROJECT BEGINS HERE"*, and rule 27
was corrected to match at `f5355fcfc4` after stating L9. So the packet's arithmetic is **verified here, not accepted**.

**WHAT THIS DOCUMENT CARRIES, stated as a PREDICATE rather than a count because the channel is append-only and a
count ages the moment the next cell files:** the L8 compile verification (`C-S1`), the round's TWO JUDGMENT GRADES
(`C-S2`, `C-S3`), and **every disarm RECORD surfaced at or before 2026-09-10T03:10Z** (`C-S4`, nineteen of them,
dismissed on round 1's own `Z-S20` rule).

⛔ **L10 IS NOT REACHABLE AND NOTHING HERE CLAIMS IT IS.** At the `C-S4` write the L10 distance measured **119 of 166
undispositioned**, down from 138. The remainder is the per-item pass: 37 standalone observations and 60 ARMED items --
**including the 19 targets of the records `C-S4` dismissed, which that row explicitly does NOT disposition.** Sizing
note carried from this seat's own correction: a partition on `hazard_standing` answers whether a row is a hazard, not
whether one row can close it; the groupable share is ~41, not 78.

---

## C-S1 -- the L8 COMPILE, verified on this seat's own instruments, including a limb the packet did not claim

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T02:45Z",
    "one_line": "L8 COMPILE VERIFIED, three limbs, none taken from the packet. (1) TERMINAL: 31 of 31 read from the FACES -- 29 complete + 2 cancelled, 0 non-terminal. (2) ROW QUALITY: 29 of 29 instances VALID, proof-of-spec-check.py run per instance, 0 INVALID. (3) ROW COVERAGE -- THE LIMB THE PACKET DID NOT CLAIM: every instance carries exactly the criterion set its face declares, 0 mismatches across 29, measured on the AUTHORITATIVE `<criterion id=...>` tag. That third limb is the checker's own documented split -- an instance valid on every row it carries can still silently OMIT a criterion -- and a VALID verdict without the criterion-id argument does not cover it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "31 task-order faces parsed for <status>: complete 29, cancelled 2, non-terminal 0. The 2 cancelled carry their re-entry pointers on the face per the CTO ruling @affef41b63.",
        "proof-of-spec-check.py run once per instance over 29 instances: rc=0 on 29, rc!=0 on 0.",
        "Coverage: criterion ids extracted from each face's `<criterion id=\"...\"/>` tags (31 of 31 faces carry a structured set) and compared to each instance's acceptance criterion_ids -- 29 compared, 0 MISSING, 0 EXTRA.",
        "DISCLOSED AGAINST THIS SEAT'S OWN FIRST PROBE: a prose-regex over each face's proof_of_spec block reported FIVE mismatches. Every one was an artifact -- the block MENTIONS sibling criteria (TO-OP-S-2's text names TO-OP-S-3's S3-AC5 because the worker must amend that row), and a string census cannot separate a citation from a criterion. The structured tag is the authoritative instrument and reports 0."
      ]
    },
    "spec_asserts": "The L8 packet reports 31 of 31 terminal and 29 of 29 instances VALID at HEAD.",
    "world_is": "Both reproduce exactly at this seat, and a third limb the packet did not claim -- row coverage -- is also clean.",
    "notes": "NOT VERIFIED HERE and stated so no silence reads as a pass: this seat did NOT re-execute any criterion's own invocation, did not re-read the deliverables other than the two judgment artifacts below, and does not certify the 3m52s production window as harmless (the packet correctly refuses that too -- one invocation, denominator of 1). L10 remains unreachable: the 138 undispositioned items are this seat's at L9 and are not dispositioned on this write."
  }
]
```

## C-S2 -- S10D-AC2 GRADED PASS, on the deployed bytes rather than on source or self-report

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S2",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T02:45Z",
    "one_line": "S10D-AC2 (JUDGMENT, reserved to this seat) GRADED PASS. The shared two-slot module is GENUINELY REUSED, not a third cache hand-rolled beside it, and the discriminating evidence is on the DEPLOYED ARTIFACT: the module's distinctive literals each appear EXACTLY ONCE in the shipped bundle. A hand-rolled copy would put them there twice. The lane assembled this evidence and correctly wrote no verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "S10D-AC2",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10D.session-analytics-two-slot.proof_of_spec.json@4cef4a058c",
        "verdict": "PASS",
        "reason": "Three limbs, each re-derived at this seat. IMPORT SITE: src/auth.ts:13 imports getJwtKeySlots and verifyWithSlots from ./lib/authkeys/jwtPublicKeys.mjs, used at :60 and :85 -- the same module TO-OP-S-10B deployed to the other two verifiers. RESIDUAL CENSUS, with the comment-vs-code split the lane claimed and this seat re-ran: getJwtPublicKey 0, GetSecretValueCommand 0, SecretsManagerClient 0, secretsClient 0; cachedPublicKey total 1, CODE 0, COMMENT 1 -- the single occurrence is at :43 inside a docstring quoting the retired line, so it is distinguished rather than counted. THE DISCRIMINATING LIMB, and the lane was right that it cannot be argued from source: the DEPLOYED bundle of opal-session-analytics (CodeSha256 66qB33r/6QF+jkb/lcrSbRD+, LastModified 2026-09-09T21:26:02Z, 22,584 bytes, ONE member dist/index.mjs, 70,108 chars scanned) carries 'JWT public key secret is empty' ONCE, 'JWT public key envelope has no usable' ONCE, and the TTL literal 300000 ONCE. A second hand-rolled cache would reproduce Z-S155 and would show these literals twice. It shows them once. PASS. Probing the bundle on LITERALS rather than identifiers is also the correct instrument here -- a bun-bundled artifact mangles identifiers, so an identifier probe would have proved nothing either way."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/opalinvest_dev/lambda/session-analytics/src/auth.ts read at HEAD: import at :13, call sites :60 and :85.",
        "Residual-symbol census re-run at this seat with a code/comment classifier, not a bare count.",
        "aws lambda get-function opal-session-analytics; bundle fetched from the returned Code.Location and its single .mjs member scanned; literal counts as stated."
      ]
    },
    "spec_asserts": "S10D-AC2 asks whether the shared module was genuinely REUSED rather than a third cache hand-rolled beside it.",
    "world_is": "One copy of the module's literals in the deployed bytes; zero residual symbols of the retired path in live code.",
    "notes": "BOUND: this grades REUSE, which is what the criterion asks. It does NOT certify the module's own correctness, the two-slot verification logic, or the TTL's value -- those are other criteria's and are not re-graded here."
  }
]
```

## C-S3 -- S10E-AC6 GRADED PASS, and the design fork it reserves is RULED

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S3",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T02:45Z",
    "one_line": "S10E-AC6 (JUDGMENT, reserved to this seat) GRADED PASS, and its fork is RULED: BOUND THE SEAL CACHE as the routine mechanism, and KEEP the v1 label bump as the deliberate immediate-invalidation lever. The two are NOT alternatives -- the criterion's wording offers them as a choice and they answer different questions. The deciding argument is the failure DIRECTION: a bounded cache fails toward MORE invalidation, which the system already absorbs; a runbook step fails SILENTLY toward retaining a key that should have been invalidated, which is the exact state a rotation exists to eliminate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "S10E-AC6",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10E.mfa-seal-key-rotation.proof_of_spec.json@4cef4a058c",
        "verdict": "PASS",
        "reason": "THE CELL PASSES ON WHAT A JUDGMENT CRITERION REQUIRES OF AN ASSIGNEE: it assembled the evidence, created no functional regression, recorded the consequence in a docstring ON THE FUNCTION where the next reader meets it, and declined to make the design call mid-face. Verified at source (jwt.ts:145-156): getMfaCodeSealKey caches with no time component; the docstring states the consequence, the non-regression and what is weakened. THE RULING THE CRITERION RESERVES: BOUND THE CACHE, to a window no longer than the private key's. Reasoning -- (a) the divergence exists ONLY because the derived value is cached forever: getMfaCodeSealKey already calls getJwtPrivateKey(), which IS now bounded, so a cache miss already yields the current key and bounding converges automatically. (b) THE FAILURE DIRECTIONS ARE NOT SYMMETRIC. A bounded cache that refreshes spuriously at a TTL boundary costs a lapsed resend-idempotency, and the cell's own limb 5 establishes that path is already graceful -- unsealCode returns null, mfa.ts mints a replacement code, hashCode verification is untouched. A missed runbook step retains a seal key derived from a rotated-away private key, silently, with nothing observable distinguishing 'step performed' from 'step forgotten'. This estate's own doctrine settles that: a missed gate is worse than a phantom one, and only one of the two errors announces itself. (c) THE LABEL BUMP IS NOT THEREBY RETIRED -- it remains the correct lever when invalidation must be IMMEDIATE and TOTAL rather than within one TTL (a suspected compromise), which bounding cannot deliver. RULING THE FORK AS EXCLUSIVE WOULD HAVE DISCARDED A CAPABILITY: 'bound OR bump' is a false dichotomy the criterion's wording invites, and naming that is part of the answer."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:145-156 read at HEAD: `if (cachedMfaSealKey) return cachedMfaSealKey;` then hkdfSync over getJwtPrivateKey() with label 'opal-mfa-code-seal-v1'.",
        "The v1 note at :115-117 records the invalidation intent the cell says is weakened: 'Changing it invalidates every sealed code in flight -- which is the correct behaviour for a key rotation.'",
        "The consequence docstring at :119-144 states the new divergence, the absence of functional regression, and routes the call to L9 -- the cell did not fix it mid-face and said why."
      ]
    },
    "spec_asserts": "S10E-AC6 asks whether the rotation runbook should ALSO bound the seal cache, or should instead bump the v1 label at rotation time.",
    "world_is": "The derived key is cached unbounded while its input is now bounded; both remedies are available and they address different failure modes.",
    "notes": "VERIFIER-NOT-DOER: this rules the fork the criterion reserves and does NOT implement it. Bounding the cache is an edit to jwt.ts and belongs to the owning lane at the recut, and the runbook line belongs to whoever owns the rotation runbook. IMPLEMENTATION IS NOT PART OF THIS GRADE. Also NOT ruled: the TTL's numeric value, which is a separate call and should be measured rather than inherited from the 300000 used elsewhere."
  }
]
```

## C-S4 -- the NINETEEN DISARM RECORDS dismissed as a class, and why their TARGETS are NOT thereby dispositioned

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S4",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T03:10Z",
    "one_line": "L9, round 2: NINETEEN DISARM RECORDS are DISMISSED WITH REASON as a class, on this project's OWN round-1 precedent -- Z-S20 ruled that a disarm record is the record of a disarm act by its named owner, NOT a finding, and its content is carried on the item it disarms. Verified per member rather than assumed: all 19 name a target that EXISTS in this channel, 19 of 19, none orphaned. ⛔ AND THEIR NINETEEN TARGETS ARE NOT DISPOSITIONED BY THIS ROW -- every one is still ARMED and UNDER_INVESTIGATION, and dispositioning them requires reading the SCOPE each disarm claims, which is exactly what this seat's own Z-S84 instructed and what at least one member (Z-S82, which disarms Z-S80's EXECUTION half ONLY and says the endpoint-shape half is expressly NOT disarmed) proves is necessary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each of the nineteen is the RECORD of a disarm act performed by the named disarm_owner of another item, not an independent finding. Its substance lives on the item it disarms and in that item's remediation row (disarm.state, owner, at), so it seeds no remediation row of its own and needs no separate remedy. This is the identical rule round 1 applied at Z-S20 to eight records of the same shape; applying it to a later cohort is precedent, not fresh judgment.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S21","NFRA_OPSEC202609-Z-S22","NFRA_OPSEC202609-Z-S31",
      "NFRA_OPSEC202609-Z-S34","NFRA_OPSEC202609-Z-S35","NFRA_OPSEC202609-Z-S36",
      "NFRA_OPSEC202609-Z-S39","NFRA_OPSEC202609-Z-S43","NFRA_OPSEC202609-Z-S55",
      "NFRA_OPSEC202609-Z-S65","NFRA_OPSEC202609-Z-S66","NFRA_OPSEC202609-Z-S70",
      "NFRA_OPSEC202609-Z-S72","NFRA_OPSEC202609-Z-S73","NFRA_OPSEC202609-Z-S74",
      "NFRA_OPSEC202609-Z-S79","NFRA_OPSEC202609-Z-S82","NFRA_OPSEC202609-Z-S88",
      "NFRA_OPSEC202609-Z-S89"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "All 19 parsed from the channel at HEAD and each one's target extracted from its own one_line: 19 of 19 name a target present in this channel, 0 orphaned. Targets: Z-S10, Z-S1, Z-S24, Z-S33, Z-S27, Z-S29, Z-S37, Z-S41, Z-S49, Z-S58, Z-S62, Z-S68, Z-S53, Z-S56, Z-S57, Z-S75, Z-S80, Z-S83, Z-S85.",
        "Every one of those 19 targets currently reads hazard_standing ARMED and disposition UNDER_INVESTIGATION -- measured, not inferred -- so none is dispositioned by the existence of its record.",
        "PRECEDENT: round 1's Z-S20 dismissed eight disarm records with this reason. That row is in this same channel and its rule is quoted rather than restated.",
        "THE PARTIAL CASE THAT PROVES THE BOUND: Z-S82 disarms Z-S80's EXECUTION half only and its own text says the endpoint-shape half 'is expressly NOT disarmed here', routing it to 1.0.0_SA_CTO~Z. A sweep keyed on the presence of a disarm would have closed Z-S80 whole."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Nineteen of the open items are records rather than findings and close on an existing rule; their nineteen targets remain open and require individual scope reads.",
    "notes": "⛔ THE BOUND IS THE POINT OF THIS ROW AND IS STATED SO NO READER TAKES IT WIDER: this dispositions the RECORDS, never the ITEMS THEY RECORD. This seat's own NFRA_OPSEC202609-Z-S84 -- filed by a prior session of this seat, naming this seat as disarm_owner, expressly as an instruction to this adjudication -- requires that an item's state be resolved by reading the SCOPE each citing row claims for itself and never by the presence of a disarm verb, carrying partial cases explicitly. Z-S82/Z-S80 is a measured instance of exactly that partial case. The nineteen targets are therefore carried into the per-item pass with the rest of the ARMED set. UNDISPOSITIONED after this row: 119 of 162 (was 138). Z-S84 itself is NOT discharged here; it discharges when the per-item pass it governs is complete."
  }
]
```
