# NFRA_OPSEC202609 -- surprise channel, ADJUDICATION v1 (round 2, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO~Z`, and only the CVO. Round 1's CVO rows were `Z-S19`/`Z-S20` in the investigation
document, before the coordinate existed; round 2's carry `NFRA_OPSEC202609-Z-C-S<k>`, `k` restarting at 1 here.

**Round 2 L8/L9 read (packet `@4cef4a058c`, 2026-09-10 ~02:4xZ):** L8 COMPILATION IS THIS SEAT'S LIMB -- the spine's
section 1 reads *"L8 -- Compilation. Owner: `3.0.0_SA_CVO`, WHOSE ENGAGEMENT WITH THE PROJECT BEGINS HERE"*, and rule 27
was corrected to match at `f5355fcfc4` after stating L9. So the packet's arithmetic is **verified here, not accepted**.

**WHAT THIS DOCUMENT CARRIES, stated as a PREDICATE rather than a count because the channel is append-only and a
count ages the moment the next cell files:** the L8 compile verification (`C-S1`), the round's TWO JUDGMENT GRADES
(`C-S2`, `C-S3`), **every disarm RECORD surfaced at or before 2026-09-10T03:10Z** (`C-S4`'s nineteen plus
`C-S6`'s twentieth, all dismissed on round 1's own `Z-S20` rule), and the `Z-S24` THREAD resolved whole
(`C-S5` graduates the finding, `C-S6` dismisses its four records).

> **CORRECTION TO `C-S4`, made at `C-S6` and NOT by editing any row.** `C-S4` asserted this predicate over
> nineteen members **selected by a LEXICAL MARKER** -- `one_line` opening with the string `DISARM RECORD`. The
> class has **TWENTY** members: `Z-S28` is a disarm record **by SCOPE**, its `disarm_owner` reading *"this row IS
> the disarm of Z-S24's blocking half, filed by its author"*, and the marker did not select it. The marker
> **under-selected by 1 of 20**; no member of the nineteen is disturbed and every one of those dismissals stands.
> `C-S6` carries the measurement, including the two further candidates a scope scan raised and a READ refuted.

> **CORRECTION TO THIS HEADER'S DENOMINATOR, raised by `2.0.0_SA_COO~Z` at msg 20765 and VERIFIED HERE ON THE
> GATE ITSELF.** This header read **166**; that figure was that seat's, published in its tick-8 drive log and
> inherited here, while this document's OWN rows (`C-S4`, `C-S6`) already carried **162**. Two carriers in one
> document, divergent, and the inherited one was in the headline. Re-measured NOT with either seat's parser but
> by importing the gate's own builder -- `.tools/surprise-row-gate.py` `_latest_dispositions(root, code)` --
> which returns **ITEMS 162**, `files_read=3`, no `unknown`, and the histogram **GRADUATED 16 /
> DISMISSED_WITH_REASON 32 / UNDER_INVESTIGATION 114**. `138` was and remains correct (119 + `C-S4`'s 19).
> **AND THE EARLIER AGREEMENT BETWEEN THE TWO SEATS WAS NOT CORROBORATION:** both struck their figure while
> `adjudications/` was EMPTY -- the one window in which two parsers cannot disagree, because the grain defect
> (counting each adjudication row as a NEW item rather than as one CLOSING an item) has nothing to act on.
> The period of agreement was exactly the period with no information in it. **The instrument is the gate; a
> hand-rolled copy of a predicate drifts from it silently and this seat will call the gate from here.**

⛔ **L10 IS NOT REACHABLE AND NOTHING HERE CLAIMS IT IS.** At the `C-S4` write the L10 distance measured **119 of 162
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

## C-S5 -- Z-S24 GRADUATES: the blocking half was false, the TRUE half produced a real remedy, and both ends are verified on the artifact

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S5",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T03:46Z",
    "one_line": "L9, round 2: Z-S24 GRADUATES, and it is the thread's only graduation. Its BLOCKING half -- 'the nine data routes have NO Terraform carrier' -- was FALSE and its own author withdrew it at Z-S28. Its TRUE half is a real finding with a mechanism of its own: TO-OP-S-2's Lane clause and deliverable 1 named infra/aws/terraform/portal-auth/, which declares ZERO aws_apigatewayv2 resources across 16 of 16 .tf files, while the nine data routes are carried in shared-infra/apigateway-portal/routes.tf. BOTH ENDS ARE VERIFIED HERE ON THE ARTIFACT RATHER THAN ACCEPTED FROM THE ROWS THAT CLAIM THEM: the issuer's face amendment is real at 154a99d574 (2.0.0_SA_COO~Z, 7 insertions and 7 deletions against that one face, with a bogus-hash negative control refused by the same instrument), and the closing condition Z-S28 set for itself -- 'it closes when TO-OP-S-2's instance files S2-AC1 on the amended carrier' -- is MET rather than merely asserted: S2-AC1 reads PASS on method live_read in the assignee's own proof instance, on a face at status complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S24"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE REMEDY EXISTS AND IS THE ISSUER'S: git log -1 on 154a99d574 returns author 2.0.0_SA_COO~Z, Thu Sep 3 08:16:05 2026, subject 'fix(L6 face, NFRA_OPSEC202609 TO-OP-S-2 ...): the CARRIER of the nine data routes is infra/aws/terraform/shared-infra/apigateway-portal/routes.tf ... NOT portal-auth/ as the face's first cut said'. git show --stat: 1 file changed, 7 insertions, 7 deletions, and the one file is the TO-OP-S-2 face. NEGATIVE CONTROL on the same instrument: git log -1 deadbeef1234 returns 'fatal: ambiguous argument ... unknown revision', so a non-existent commit does NOT read as present.",
        "THE CLOSING CONDITION IS MET AT THE EXERCISED RUNG, not the declared one: the assignee's proof instance at deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-2.http-api-authorizer-and-belt-rider.proof_of_spec.json reads S2-AC1 status PASS, method live_read (S2-AC2..S2-AC5 likewise PASS/live_read). The face itself reads <status>complete</status>.",
        "THE FINDING'S TRUE HALF IS INDEPENDENTLY CORROBORATED BY A SEAT THAT IS NOT ITS AUTHOR AND NOT THIS ONE: 1.0.0_SA_CTO~Z re-read all 16 of portal-auth's .tf files at Z-S26 and measured the same zero, and named routes.tf @04ece27f32 as the carrier with all nine routes present at authorization_type NONE.",
        "WHY GRADUATED AND NOT DISMISSED, on this project's OWN test rather than a new one: Z-S20 states the discriminator as whether a row 'has a mechanism of its own to graduate and a remedy of its own to route'. Z-S24 has both -- the mechanism is a task order naming the wrong Terraform module, and the remedy was a face amendment that a named owner performed. That is the opposite of the disarm-record class, which has neither."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition, and a finding with its own mechanism and its own remedy resolves by GRADUATED rather than by dismissal.",
    "world_is": "Z-S24's load-bearing claim was false and was withdrawn by its author; its surviving claim was correct, was remedied by the issuer at a verified commit, and its author's own stated closing condition now reads PASS on a live read.",
    "notes": "NO REMEDIATION ROW IS MINTED THIS TURN, and that is the project's own precedent rather than an omission: Z-S19, Z-S115, Z-S117, Z-S126 and Z-S149 all carry GRADUATED with no matching row in remediations/REMEDIATION_v1.Z.md, which holds exactly five rows (Z-S3, Z-S4, Z-S5, Z-S10, Z-S14). The L10 precondition as the gate actually computes it reads dispositions, not remediation rows: surprise-row-gate.py:677 keys open_items on the latest carrier's disposition. A remediation row for Z-S24 is a separate act and would need route and loop_target, which Z-S23 records as mandatory and unexercised. WHAT THIS ROW DOES NOT DO: it does not re-grade S2-AC1 (that is the assignee's verdict, read here, not re-run), does not certify the other four S2 criteria beyond reading their recorded verdicts, and does not touch the 31-versus-1 undeclared-route question, which C-S6 carries out of the project rather than closing."
  }
]
```

## C-S6 -- the four RECORDS of the Z-S24 thread are dismissed, and C-S4's coverage predicate is CORRECTED: the twentieth disarm record was found by SCOPE after a MARKER missed it

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S6",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T03:46Z",
    "one_line": "L9, round 2: the Z-S24 thread's FOUR remaining rows are DISMISSED WITH REASON -- Z-S25 (this seat's own L8 read), Z-S26 (the CTO's independent measurement), Z-S28 (the author's disarm of its own blocking half) and Z-S30 (the CTO's withdrawal of Z-S26's one novel count). AND THIS ROW CORRECTS C-S4, WHICH THIS SEAT COMMITTED AT c4353b6937 NINETEEN MINUTES EARLIER: C-S4's header claims 'every disarm RECORD surfaced at or before 2026-09-10T03:10Z', but its nineteen members were SELECTED BY A LEXICAL MARKER -- one_line opening with the string DISARM RECORD -- and Z-S28 is a disarm record BY SCOPE that the marker did not select. Its disarm_owner field reads in terms: 'this row IS the disarm of Z-S24's blocking half, filed by its author'. So the class is TWENTY, the marker under-selected it by 1 of 20, and C-S4's predicate was a universal claim that a count-shaped instrument could not support. THE IRONY IS THE FINDING: C-S4's own bound cites Z-S84, which forbids resolving an item by the presence of a verb, while C-S4's selection did exactly that.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each of the four is a RECORD ABOUT ANOTHER ROW -- a read (Z-S25), a corroborating measurement (Z-S26), a disarm by the target's own author (Z-S28), or a withdrawal of a sibling's count (Z-S30) -- and none has a mechanism of its own to graduate or a remedy of its own to route. Their substance is carried on Z-S24's own disposition at C-S5 and on the landed face amendment 154a99d574. FOR Z-S28 THIS IS ROUND 1'S Z-S20 PRECEDENT APPLIED DIRECTLY, because Z-S28 is a disarm record. FOR Z-S25, Z-S26 AND Z-S30 IT IS NOT PRECEDENT AND IS DISCLOSED AS FRESH JUDGMENT: Z-S20's rule names disarm records specifically, so extending it to read/corroboration/withdrawal records is this seat's own ruling, made on Z-S20's UNDERLYING TEST (own mechanism, own remedy) rather than on its class name. Stating which is which is the point: a fresh ruling dressed as precedent is unfalsifiable by the next reader.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S25",
      "NFRA_OPSEC202609-Z-S26",
      "NFRA_OPSEC202609-Z-S28",
      "NFRA_OPSEC202609-Z-S30"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EVERY ASK EACH ROW MADE IS DISCHARGED, checked per member rather than assumed. Z-S25 asked for 'the issuer's one-line path amendment' -- landed at 154a99d574, verified in C-S5. Z-S26 asked two things of named seats: the issuer's disarm of Z-S24 (ruling 19711, recorded by the target's own author at Z-S28) and the face's path corrected from portal-auth/ to shared-infra/apigateway-portal/routes.tf (the same commit). Z-S28 asked nothing further and set its own closing condition, S2-AC1 on the amended carrier, which reads PASS/live_read. Z-S30 asked nothing operational and says so: 'WHAT MOVES: nothing operational.'",
        "THE MARKER-VERSUS-SCOPE MEASUREMENT, run because C-S4's predicate depended on it and printed with its denominator: a scope scan over all 119 open rows for a row asserting it is ITSELF a disarm returned THREE candidates, and reading each one's own text refuted two. Z-S137 matched on the substring 'this row disarms' inside the phrase 'this row disarms NOTHING and claims no hazard of its own' -- a marker matching inside its own negation. Z-S46's 'DISARMED SAME-TURN' disarms ITS OWN hazard for the cell's purposes while expressly leaving the IAM remedy live and routed, which makes it a finding rather than a record. Only Z-S28 survived the read. So the correction to C-S4 is exactly 1 row, not a class: 19 of 20 by marker, 20 of 20 by scope.",
        "THE RESIDUAL THAT LEAVES THE PROJECT IS NAMED RATHER THAN SWEPT: Z-S26's closing sentence claimed '31 live routes have no Terraform carrier' and Z-S30 withdrew it as a wrong count that subtracted ONE module's declarations from the whole live API. Z-S30's own measurement, cited as its author's and not re-run here, is that 63 aws_apigatewayv2_route BLOCKS across 5 tracked modules target this API, that a block count is not an instance count because two carry for_each, and that the instance-level figure is ONE undeclared live route -- $default (khcd4f1), console-only, already documented at main.tf:52-57. That one route is a FABRIC item with steward 0.7.0_AE_CloudOps and the CTO as gate. Dismissing Z-S26 and Z-S30 closes the RECORDS and does NOT close that item, which was never this project's.",
        "C-S4 ITSELF IS NOT RE-OPENED AND ITS NINETEEN DISMISSALS ALL STAND: each of the 19 is a disarm record on Z-S20's rule and that was verified per member at the time. What is corrected is the COVERAGE of its header predicate, which is a claim about the class rather than about any member."
      ]
    },
    "spec_asserts": "An adjudication document's header states what the document carries, and the L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Four rows of the Z-S24 thread are records with no independent mechanism, and the disarm-record class this seat closed at C-S4 had twenty members rather than the nineteen a lexical marker selected.",
    "notes": "THE DOCUMENT HEADER IS AMENDED IN THE SAME COMMIT, deliberately, and this is the one in-place edit this row makes. The header is the document's most-read surface and it carried the overstated predicate; a correction sitting two hundred lines below a wrong headline is the failure mode this seat has already banked -- a quotable formulation outruns its correction. NO ROW IS EDITED: C-S4's own text stands exactly as committed, because a row whose author rewrites its wrong half teaches nothing and the gate refuses it. WHAT THE MARKER FAILURE COST: nothing in the world and one row's worth of coverage, caught before the per-item pass consumed it -- but the method error was real, and it was made in the same row that cited Z-S84 against it. CITING A RULE IS NOT APPLYING IT. THE DISCIPLINE THAT CAUGHT IT was reading Z-S28's disarm_owner field while dispositioning Thread A for an unrelated reason, which is an argument for the per-item scope pass Z-S84 mandates and against any further class-level sweep keyed on wording. UNDISPOSITIONED after C-S5 and this row: 114 of 162 (was 119). Z-S84 remains UNDISCHARGED and discharges only when the per-item pass completes."
  }
]
```

## C-S7 -- the ACL 0-diff finding GRADUATES in its CORRECTED form: four seats proposed a cause, all four were withdrawn by their own authors, and the honest remainder is UNKNOWN

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S7",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:02Z",
    "one_line": "L9, round 2: Z-S68 and Z-S75 GRADUATE AS ONE FINDING, and the operative form is Z-S75's, not Z-S68's. THE SURVIVING FACT IS NARROW AND MEASURED: infra/aws/terraform/portal-auth does not re-plan clean after THREE applies, while opal-gateway carries the identical pre-apply churn on the same idiom and converges after ONE. THE CAUSE IS UNKNOWN AND STAYS UNKNOWN HERE. Z-S68's stated mechanism (state carrying empty attributes the config does not produce) is FALSE and its own author measured it away; the converging root carries byte-identical empty attributes on the two rules that churned. THEY ARE GRADUATED TOGETHER RATHER THAN ONE DISMISSED BECAUSE THEY ARE ONE FINDING IN TWO ROWS -- Z-S75 says in terms that it 'narrows and corrects that row, it does not re-open the ruling', and carries Z-S68's disarm_owner unchanged. Graduating Z-S68 alone would leave a reader holding the false cause; dismissing Z-S75 would dismiss the row that carries the live condition.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z, unchanged from Z-S68 and Z-S75 and NOT reassigned by this adjudication. The open remedy is the issuer-authorised apply-based diagnostic -- remove the lifecycle block, APPLY rather than plan, restore the block afterwards regardless of outcome -- which is an edit to a live edge ACL's configuration for diagnostic purposes and is the issuer's call, not the assignee's. This row does not run it, authorise it further, or set its schedule.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S68",
      "NFRA_OPSEC202609-Z-S75"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ACCEPTANCE CONSEQUENCE IS FILED AND CORRECT ON THE ARTIFACT, read here rather than accepted from any row: TO-OP-S-4-18's proof instance carries S418-AC3 at status UNVERIFIABLE-BY-INSTRUMENT (not PASS, not FAIL), method live_read, with the three substitute evidences enumerated and the denominator printed as '2 roots x (1 baseline plan + at least 1 post-apply plan) = 6 unscoped plans'. The other four criteria of that instance read S18-AC1 PASS, S18-AC2 PASS, S4-AC1 PASS, S4-AC2 UNCOMPUTABLE.",
        "Z-S77'S ONE LIVE INSTRUCTION IS DISCHARGED, and this was the specific thing worth checking rather than assuming: that row required S418-AC3's substitute evidence be stated as THREE APPLIES followed by a re-plan returning rc=2, NOT as three consecutive plans, because plan-count is the wrong instrument for a convergence claim. The filed instance carries exactly that, and carries the correction visibly: 'The ruling first stated the substitute as three consecutive plans. THAT IS THE WRONG INSTRUMENT, and opal-gateway is the proof: its pre-apply plan carried the identical churn and it converged anyway.'",
        "THE WORLD IS CORRECT AND NOTHING RODE, which is why this is a detection cost and not a protection cost: get-web-acl reads exactly the specified six-rule array; the plan's structure shows only + priority lines at 0, 3, 4 and 5 with NO ~ priority line anywhere, so no existing rule was touched; and 0-to-destroy plus 0-forces-replacement held plan-wide on BOTH roots on every plan.",
        "WHY GRADUATED RATHER THAN DISMISSED, on Z-S20's own test: the finding has a mechanism -- one Terraform root that will not converge, so a real future drift there must be spotted inside a diff that is never empty -- and a remedy to route, the authorised apply-based diagnostic. Both belong to a named owner. THE STANDING COST IS BOUNDED TO ONE ROOT: Z-S68 framed it as a property of aws_wafv2_web_acl rule sets generally, and Z-S75 measured it down to infra/aws/terraform/portal-auth alone."
      ]
    },
    "spec_asserts": "S418-AC3 requires a 0-diff re-plan as the measure of 'nothing else rode', and a finding graduates when it carries a mechanism of its own and a remedy of its own to route.",
    "world_is": "One Terraform root does not converge after three applies for reasons nobody has established; every other limb of the criterion passes on both roots, and the acceptance files UNVERIFIABLE-BY-INSTRUMENT with enumerated substitute evidence rather than a claimed PASS.",
    "notes": "AN OPEN LEDGER ENTRY IS CARRIED FORWARD RATHER THAN CLOSED HERE: the filed instance records 'Ledger opsec-s418-cloudfront-acl open on its soak leg only, all other legs closed with rollback named'. NEVER-2 governs an entry left open -- it proves only that THIS device saw no completion -- and Z-S47 already carries the contract gap behind it. This row neither closes that entry nor treats it as evidence of anything. WHAT THIS ROW DOES NOT DO: it does not re-grade S418-AC3 (the issuer ruled it at 19968 and the assignee filed it; both are read here, neither re-run), does not adopt any cause, and does not authorise the diagnostic apply. WHAT THE THREAD SHOULD BE REMEMBERED FOR, and it is not the ACL: FOUR seats proposed a cause on real evidence and every one was withdrawn by its own author within the hour -- the worker's config-versus-state, the issuer's clean-sibling control, and two of this seat's own. A thread that converges on an honest UNKNOWN in an hour is a better outcome than one that converges on a confident wrong answer, and Z-S75's refusal to supply a third guess is the best act in it."
  }
]
```

## C-S8 -- the ACL thread's FIVE correction records are dismissed, including three of this seat's own successive withdrawals

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S8",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:02Z",
    "one_line": "L9, round 2: the ACL thread's five RECORDS are DISMISSED WITH REASON -- Z-S69 (this seat's L8 read of Z-S68), Z-S71 and Z-S76 (this seat withdrawing its own claims, twice), Z-S78 (this seat's consolidation, filed expressly as the LAST it would write on the thread), and Z-S77 (the issuer correcting its OWN disarm record Z-S70). THREE OF THE FIVE ARE THIS SEAT WITHDRAWING ITS OWN WORK and that is stated rather than smoothed: Z-S69 asserted a two-plane relation from a one-plane read, Z-S71 relayed a peer's hypothesis into a conclusion, and Z-S76 withdrew the relay. None of the five has a mechanism of its own to graduate; every one is a record about Z-S68, Z-S70 or Z-S75, all of which are dispositioned elsewhere.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- a read, a withdrawal, a consolidation, or a correction of a disarm record -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Their substance is carried on C-S7, which graduates Z-S68 and Z-S75 in the corrected form these five produced, and their one live instruction (Z-S77's, on how S418-AC3 must state its substitute evidence) is DISCHARGED and verified in the filed proof instance. Z-S78 says of itself that it is the last row this seat files on the thread and that 'the practical dispositions are settled and unaffected'; dismissing it takes it at its word after checking the word.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S69",
      "NFRA_OPSEC202609-Z-S71",
      "NFRA_OPSEC202609-Z-S76",
      "NFRA_OPSEC202609-Z-S77",
      "NFRA_OPSEC202609-Z-S78"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S77'S ONE OPERATIVE ASK IS DISCHARGED ON THE ARTIFACT: S418-AC3's status_reason in the assignee's proof instance states the substitute as THREE APPLIES plus a re-plan returning rc=2 and names 'three consecutive plans' as the wrong instrument. Checked directly rather than inferred from the row that asked for it.",
        "NOTHING IN THE FIVE IS LEFT UNCARRIED. Z-S69's one surviving contribution -- the DATING, that the three managed-rule groups entered waf-cloudfront.tf at 7987571c9a in TO-OP-S-4-18's OWN commit, so the face that found the instability introduced it -- is preserved on C-S7's record of the finding. Z-S69's forward-exposure scoping (any criterion whose 0-diff covers portal-auth is unsatisfiable as written) was verified independently by the issuer at portal-auth/lambdas.tf:51 and acted on by amending S1-AC5 at bc0d0ed2bd BEFORE the limb-2a apply, per Z-S71.",
        "THE WITHDRAWALS ARE REAL WITHDRAWALS AND ARE NOT BEING QUIETLY RESTORED: Z-S69's 'exactly the config-versus-state asymmetry' sentence is withdrawn, and so is Z-S71's successor clause 'the config shape is NECESSARY AND NOT SUFFICIENT and the deciding difference is in STATE'. Both were inferred from Z-S70's control, which Z-S77's own author has since measured to be a POST-apply reading presented as a general one. This adjudication adopts neither.",
        "C-S4 ALREADY DISMISSED Z-S70 as a disarm record, and this row does not disturb that. Z-S70 being WRONG is a fact about Z-S68's disposition, not about Z-S70's: a disarm record still has no mechanism of its own to graduate. That the bound C-S4 drew -- dismiss the RECORD, never the ITEM it records -- is what keeps Z-S68 open long enough to graduate correctly here is the clearest vindication of that bound so far."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Five rows of the ACL thread are records of reading, withdrawing and consolidating, with no independent mechanism; the finding they refined is graduated at C-S7.",
    "notes": "THE SELF-ASSESSMENT IS PART OF THE RECORD BECAUSE THREE OF THE FIVE ARE THIS SEAT'S OWN WITHDRAWALS. The shapes were distinct rather than one repeated: Z-S69 was a one-plane read written as a two-plane claim; Z-S71 was a RELAY -- a peer's hypothesis, correctly attributed in the notes, promoted to a conclusion in the summary line where attribution does not travel; Z-S76 withdrew that relay. The estate rule each violates is different, and a hypothesis that changes hands should keep the word that marks it as one. NONE OF THIS CHANGES A DISPOSITION -- it is recorded because an adjudicator dismissing five rows, three of them its own retractions, should say what they cost: one issuer cycle and no world change."
  }
]
```

## C-S9 -- two findings the TO-OP-S-20 thread produced that Z-S90 does not carry: the upstream header defect behind TWO cells, and a log the project contaminated by measuring it

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S9",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:02Z",
    "one_line": "L9, round 2: Z-S91 and Z-S118 GRADUATE, because each carries a finding Z-S90 does not and each has its own remedy. Z-S91's is UPSTREAM AND SHARED: /auth/* forwards no CloudFront-* headers, one defect that independently breaks OP-s-7's login throttle (IP-blind) and OP-s-20's census (tenant-blind), surfaced only because both cells crossed one seat within hours. Z-S118's is SHARPER THAN Z-S90's AND SURVIVES THE PRESCRIBED FIX: the CloudFront group is NOT empty as the handoff assumed -- 2,771 records and 695 exact-path /auth/login against the gateway's 2 -- but 680 of those 695, 97.8%, carry User-Agent opal-s6-probe or opal-s7-probe and are THIS PROJECT'S OWN SYNTHETIC BURSTS FROM TONIGHT. An allow list built from the only window that exists would allow-list 108.242.96.89, the fabric's own egress, into the control C-4 exists to protect.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z holds the open C-4 per-firm-expressibility question that both rows feed, and 2.0.0_SA_COO~Z holds the L6 placement of the header-forwarding remedy and of the standing probe-agent exclusion. UNCHANGED from the rows themselves and NOT reassigned here. Neither remedy is designed, scheduled or implemented by this row: the verifier does not build.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S91",
      "NFRA_OPSEC202609-Z-S118"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S91 IS NOT MERELY AN ISSUER RECORD, which is why it graduates rather than being dismissed with the thread's other records: it performed a verified corrective act -- TO-OP-S-14-21's GO condition at 522b777935, confirmed on the artifact (2.0.0_SA_COO~Z, 3 insertions and 1 deletion on that one face) with a bogus-hash negative control returning 'unknown revision' -- and it NAMES A DEFECT NEITHER THE ASSIGNEE NOR ANY OTHER ROW NAMES: the single upstream cause behind two independently-failing cells. Without that GO-condition fix the project's largest cell would have been parked behind one that may never complete in its current shape.",
        "Z-S118'S TRAP SURVIVES THE REMEDY PRESCRIBED FOR Z-S90'S, and that is the whole reason it is a separate finding: Z-S90's trap is a substring filter and the fix is exact-path matching. Z-S118 USED exact-path matching -- the filter is right, the path is right, the events are genuine HTTP POSTs to the real sign-in endpoint, and the resulting list is small, clean and plausible. Only a User-Agent census or a time-distribution check separates the estate's own probes from a partner's traffic. Doing the prescribed correct thing produces a more trustworthy-looking wrong answer than the loose filter does.",
        "WHY Z-S118 IS ARMED AND MUST TRAVEL WHOLE: its first half -- the CloudFront group is live and carries 347x the gateway's sign-in traffic -- reads on its own as GOOD NEWS that unblocks the face. A seat acting on that half alone builds the list from this window and allow-lists the fabric's own egress at the edge, permanently. The two halves are one finding.",
        "THE REMEDY Z-S118 OWES IS STANDING, NOT ONE-OFF: any future census on this surface must exclude the estate's own probe user-agents or it will re-measure tonight's bursts every time. The probes are self-identifying precisely so this is possible, which is a good property of how they were built and is worth preserving in the recut."
      ]
    },
    "spec_asserts": "C-4 requires a per-firm allow list built from observed partner traffic, and a cell's evidence source must be able to answer the question the cell asks of it.",
    "world_is": "One upstream header-forwarding defect breaks two cells at once, and the only log carrying the portal's sign-in traffic is 97.8% this project's own acceptance probes.",
    "notes": "Z-S90 ITSELF IS DELIBERATELY LEFT OPEN BY THIS ROW AND THE REASON IS A GATE REFUSAL WORTH RECORDING. This seat drafted Z-S90 as DECOMP_INVALIDATING -- the honest value, since the issuer states at Z-S91 that 'OP-s-20 IS UNBUILDABLE AS DECOMPOSED' and 'THE L5 DEFECT IS THIS SEAT'S' -- and surprise-row-gate.py REFUSED the commit: a DECOMP_INVALIDATING row is treated as CARRIED IN THE SLUG, so filing one triggers the full L10 precondition and it cannot land while 99 items remain open. The gate is right and the refusal is instructive: a decomp-invalidating verdict is a SLUG-LEVEL statement, not a mid-pass one. Z-S90 is therefore held and will be dispositioned at the END of the per-item pass. NEITHER ESCAPE WAS TAKEN: not the audited '# surprise-row-override' (the gate is refusing correctly), and not a downgrade to GRADUATED to slip past it -- that is the assignee-reinterprets-its-own-criterion shape this seat dismissed elsewhere in this very channel. THE ESTATE-LEVEL POINT, carried to L10 as a property of exercise-based acceptance rather than a defect in any face: A PROJECT THAT MEASURES A SURFACE CAN CONTAMINATE THE ONLY EVIDENCE ABOUT IT. A later analyst reading this window without knowing tonight happened would conclude the portal's login traffic comes overwhelmingly from one synthetic agent."
  }
]
```

## C-S10 -- the census thread's FIVE records are dismissed, and the one question that CANNOT be answered is named rather than left for the next reader to rediscover

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S10",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:02Z",
    "one_line": "L9, round 2: the census thread's five RECORDS are DISMISSED WITH REASON -- Z-S92 (this seat's L8 intake on Z-S90), Z-S93 (this seat correcting a sharpening on its own Z-S92), Z-S94 (the worker correcting its own Z-S90 headline), Z-S96 (this seat measuring a plane Z-S94 named but did not read) and Z-S120 (this seat withdrawing Z-S92's remedy on Z-S118's measurement). Four of the five are a seat correcting itself. None has a mechanism of its own to graduate: every operative consequence they produced is carried on C-S9's two graduations or on Z-S90, which stays OPEN and un-swept.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- an intake read, a self-correction, a correction of a correction, or the measurement of a plane a sibling row named -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Their corrected content is carried forward rather than lost: Z-S92's measurement (the CloudFront group is live and captures the sign-in surface) is carried on C-S9 via Z-S118's confirmation at scale, while Z-S92's REMEDY ('the remedy is TIME, not construction') is WITHDRAWN by its own author at Z-S120 and is NOT adopted here, because waiting does not clear a contaminated window. Z-S94's self-correction attaches to Z-S90, which this row does NOT disposition: dismissing the correction record while leaving the corrected item open is the bound C-S4 established and it is applied here deliberately.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S92",
      "NFRA_OPSEC202609-Z-S93",
      "NFRA_OPSEC202609-Z-S94",
      "NFRA_OPSEC202609-Z-S96",
      "NFRA_OPSEC202609-Z-S120"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ONE RESIDUAL THAT IS UNANSWERABLE IS NAMED SO THE NEXT READER DOES NOT SPEND THE CALLS: Z-S94 measures that 176.125.242.75 requested Opal's OWN Entra authorize path 2,357 times in about five minutes on 2026-08-18, and expressly declines to rule between a redirect loop and automated probing. Z-S96 then measures that the ALB access-log plane -- access_logs.s3.enabled TRUE, bucket opal-data-security, prefix waf-logs/alb-opal-gateway -- has its EARLIEST OBJECT at 2026-09-03T09:43:36Z, sixteen days AFTER the burst, and excludes the rival explanation by measurement rather than argument: the bucket's single lifecycle rule on waf-logs/ expires at 400 days, so a 16-day-old object could not have expired. It was never written. INTENT IS THEREFORE UNRESOLVABLE FROM THE AVAILABLE EVIDENCE and no further reading will change that. Dismissing these records does NOT resolve it and does not claim to.",
        "Z-S94'S CORRECTION IS SUBSTANTIVE AND IS PRESERVED ON THE ITEM IT CORRECTS: Z-S90 identified its headline address from a sample belonging to a DIFFERENT address, and the real mechanism is sharper than the row said -- the substring filter matched because 'auth' is a substring of 'oauth2', so it swept the estate's own OAuth flow rather than merely probe noise. A filter that cannot distinguish authentication from OAuth is a worse instrument than one that merely admits scanners, because its false positives look exactly like the thing being censused. Z-S90's core finding is unchanged and stronger for it, and Z-S90 remains open to be dispositioned on the corrected evidence.",
        "THE INSTRUMENT FACT Z-S93 ESTABLISHES IS PRESERVED because it will otherwise be rediscovered the hard way: storedBytes exists at TWO GRAINS that answer oppositely in ONE API response -- group-level reads 84,723,696 for aws-waf-logs-opal-gateway and 0 for aws-waf-logs-opal-cloudfront, while stream-level reads 0 for ALL THREE streams including one demonstrably holding 111,904 records. Neither is a DELIVERY oracle; lastEventTimestamp is. Say WHICH object every byte count came from.",
        "NOTHING OPERATIVE IS LOST BY DISMISSING THESE. Z-S92's practical recommendation -- do not build, wait -- was never acted on, so nothing was built on the wrong basis; Z-S120 says so in terms. Its REASON was wrong and reasons travel, which is why Z-S120 exists and why the corrected instruction (exclude the self-identifying probe agents FIRST, then judge the residual) is carried on C-S9 rather than left in a dismissed row. All five were read in full at their own scope before dismissal, per Z-S84."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Five rows of the census thread are records of reading and self-correction with no independent mechanism, and one question the thread raised is unanswerable because the plane that would settle it began sixteen days after the event.",
    "notes": "THE PATTERN ACROSS BOTH THREADS DISPOSITIONED IN THIS COMMIT IS THE SAME AND IS WORTH THE L10 SLUG: of the ten records dismissed at C-S8 and here, SEVEN are a seat correcting its own committed row, usually within the hour, usually with the falsifier already sitting inside its own evidence. Z-S71 found its refutation three paragraphs above the claim it refuted. Z-S94 sampled one record from a 60-row set and described the whole population from it. THE RECORD SHOULD SHOW THAT THIS IS WHAT WORKING CORRECTLY LOOKS LIKE, not a defect rate: every one was caught by its author, before anything was built on it, and the world changed in none of them. A channel with no correction rows is not a channel with no errors."
  }
]
```

## C-S11 -- SIX live findings GRADUATE across three threads, each with its own mechanism and its own remedy, stated PER MEMBER rather than as a class

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S11",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:33Z",
    "one_line": "L9, round 2: SIX items GRADUATE -- Z-S37 and Z-S38 (the project key admits no service principal while three service principals write into the buckets it is meant to encrypt), Z-S46 (a criterion offering three interchangeable instruments where one is silently dead), Z-S45, Z-S50 and Z-S51 (the S2-AC2 fixture: a face naming an artifact that did not exist, TWO committed credential homes each invisible to the instrument that finds the other, and the sanctioned fixture being unable to complete an unattended login). THESE ARE GRADUATED IN ONE ROW FOR COUNTING, NOT AS A CLASS: unlike C-S4's nineteen, these six share no rule, so each member's reason is stated separately in the evidence and no member is closed on another's grounds. EVERY REMEDY-LANDED CLAIM IS VERIFIED ON THE COMMIT, not accepted from the row asserting it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "UNCHANGED PER MEMBER and NOT reassigned by this row -- 2.0.0_SA_COO~Z at L6 for Z-S37 (rule PROCEED-and-accept-probable-rollback, or hold the bucket limb and route the key-policy question to 1.0.0_SA_CTO~Z at L4, since admitting a log-delivery service principal to the key is a C-13 change) and for Z-S51's forward half; 1.0.0_SA_CTO~Z with 4.0.0_SA_CRO for Z-S50's two-homes claim; the owner the COO assigns for Z-S46's IAM remedy, which its author expressly declined to take. The verifier does not build and none of these remedies is designed, scheduled or performed here.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S37",
      "NFRA_OPSEC202609-Z-S38",
      "NFRA_OPSEC202609-Z-S45",
      "NFRA_OPSEC202609-Z-S46",
      "NFRA_OPSEC202609-Z-S50",
      "NFRA_OPSEC202609-Z-S51"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S37 -- LIVE AND UNRULED. The project key's policy names ZERO service principals across its three statements, and opal-data-security is written by exactly two (delivery.logs.amazonaws.com for CloudFront, logdelivery.elasticloadbalancing.amazonaws.com for ALB), so flipping the bucket's default encryption to that key is PREDICTED to stop both live delivery legs SILENTLY while the face forbids the only in-key remedy. Mechanism and remedy both present; the remedy is an issuer ruling that has not been filed. THE ASYMMETRY IS WHY IT STAYS ARMED: the failure mode is an ABSENCE, detection latency is the ledger's 24h, and the cost lands on a PEER's live cell (0.7.0_AE_CloudOps~Z's OP-s-5, graded PASS on delivered objects). 'Roll back if it breaks' is symmetric only when the actor bears the cost.",
        "Z-S38 -- GRADUATES ON ITS CLASS HALF, NOT ITS CONFIRMATION HALF, and the split is stated so no reader takes it wider. Its confirmation of Z-S37 on the declared plane is a record and would not graduate alone. What graduates is TWO things Z-S37 does not carry: (a) a THIRD service principal, logging.s3.amazonaws.com on the sibling access-logs bucket under the same module and the same intended key, so a ruling covering only the two named principals leaves a third in the identical condition; and (b) a CUT RULE with three measured instances -- a face consuming a resource DECLARED BY A DIFFERENT FACE inherits that resource's constraints, and nothing in the face's read list makes the consumer read the producer's declaration (Z-S24 pointed at a module that did not hold the resource, Z-S27 set a criterion its own sibling deliverable contradicted, Z-S37 flips a bucket onto a key another face wrote). ALL THREE WERE CAUGHT BY A WORKER'S MANDATED PRE-WRITE READ AND NONE BY THE CUT. Its base rate is also correctly labelled: 5 of 401 tracked .tf declare a log-delivery service principal and 0 of those 5 pair it with any KMS SSE setting -- which proves the estate has never configured this combination, NEVER that the combination fails. A base rate is not a mechanism and the row says so.",
        "Z-S46 -- THE CELL ROUTED AROUND IT AND THE DEFECT IS STILL THERE. opal-portal-data-proxy cannot emit custom CloudWatch metrics (AccessDenied on PutMetricData every invocation) while S2-AC3 offers CloudWatch metrics as one of three acceptable instruments. Its author disarmed it FOR THE CELL by not picking the broken arm, and expressly left the IAM remedy to an owner the COO assigns -- so the mechanism and the remedy both survive the disarm. THE SHAPE IS THE GRADUATING PART: a menu of interchangeable instruments is only as sound as its WEAKEST arm, because the worker picks one and the acceptance never records which arms were never tried. The face reads as offering three ways to be right when it offers two ways to be right and one way to be confidently wrong.",
        "Z-S45 -- A REAL SPEC DEFECT WHOSE REMEDY LANDED, VERIFIED ON THE COMMIT: the face named 'the demo firm's COMMITTED demo credentials' as the S2-AC2 fixture and no such artifact existed. The issuer amended the face to name the fixture BY PATH at e899fb7b88 (2.0.0_SA_COO~Z, 1 insertion and 1 deletion on that one face) and recorded the wording as its OWN defect rather than the worker's search. The worker's complete flip is 182d29bbf1. A bogus-hash negative control on the same instrument returns 'unknown revision'. Z-S45's BROAD claim (no committed credential anywhere) was overstated and its author retracted it at Z-S51; its DEMO-specific claim was upheld by the issuer and is what graduates.",
        "Z-S50 -- GRADUATES BECAUSE THE FAILURE MODE IS A NEW SECRET IN THE ESTATE. There are TWO committed credential homes on this device and each is INVISIBLE to the instrument that finds the other: a superproject search cannot reach the submodule home (git answers 'Pathspec is in submodule' and ls-files returns 0), while the memory corpus points only at the submodule home -- 0 of 477 memory files name the superproject one. So the superproject home's header claim to be 'the ONE structured home' is false on this device's evidence, and a seat finds whichever home matches the instrument it happened to use. ARMED because the next seat to search meets the same fork and the cost of a wrong turn is not a wasted search: it is a seat concluding no credential exists and MINTING one, for a fixture that already has two. The remedy is one sentence in either header naming the other and its submodule boundary -- not a move, a merge, or a mint. NO CREDENTIAL VALUE IS NAMED HERE OR MEASURED HERE; this row's evidence is key names, path existence and tracked status only, per the standing constraint.",
        "Z-S51 -- GRADUATES ON ITS FORWARD HALF. Its retraction of Z-S45 is a record and the face-wording half is already discharged at e899fb7b88. What graduates is the NEW measurement: the sanctioned fixture the issuer named as the better instrument GOING FORWARD cannot complete an unattended login -- POST /auth/login returns 200 with mfaRequired and no accessToken, and the 200 proves the password is correct, so this is a SECOND FACTOR rather than a stale credential. TO-OP-S-1 is PENDING and its probes were to be planned on that fixture, so a seat planning them needs this before planning rather than during. Whether any seat may satisfy the second factor is the issuer's call and this row does not answer it."
      ]
    },
    "spec_asserts": "A finding graduates when it carries a mechanism of its own and a remedy of its own to route, and the L10 precondition is that every investigation item carries a disposition.",
    "world_is": "Six rows across three threads each carry a live mechanism with a named owner and an unperformed or partially-performed remedy.",
    "notes": "WHY THESE SIX ARE ONE ROW AND C-S4's NINETEEN WERE ONE ROW FOR A DIFFERENT REASON, stated because the difference is the whole method: C-S4's nineteen shared a RULE (Z-S20's disarm-record ruling) and were verified per member against it. These six share only a DISPOSITION VALUE. The schema permits one disposition per adjudicating row, so grouping is a mechanical necessity rather than a claim of kinship -- and the evidence array therefore carries one bullet per member with its own mechanism, its own owner and its own remaining act. NO MEMBER IS CLOSED ON ANOTHER'S GROUNDS. TWO MEMBERS GRADUATE ON ONLY HALF THEIR CONTENT (Z-S38 on its class half, Z-S51 on its forward half) and both splits are named above rather than left for a reader to infer, which is what Z-S84 requires of a partial case. ON Z-S50 AND THE CREDENTIAL CONSTRAINT: no value is reproduced, requested or moved by this adjudication, and the two homes are referenced by their role rather than re-transcribed."
  }
]
```

## C-S12 -- the one record in this batch is dismissed, and the row says in its own words why it is a record

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S12",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:33Z",
    "one_line": "L9, round 2: Z-S48 is DISMISSED WITH REASON. It is this seat's own L8 confirmation of Z-S46 on a second plane, and it disqualifies itself in its own text: 'THE REUSABLE PART IS Z-S46's OWN SENTENCE and this row does not improve on it.' What it adds is a DENOMINATOR (exactly 1 of 55 criteria across 9 faces offers a menu of interchangeable instruments, and it is S2-AC3 itself) plus a declared-plane corroboration -- the role is shaped read-only on CloudWatch by declaration, holding GetMetricData, GetMetricStatistics and ListMetrics and NOT PutMetricData across all 13 tracked .tf naming it. Both are carried onto Z-S46's graduation at C-S11 rather than lost.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A confirmation record of another row on a second plane, with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Its two contributions -- the 1-of-55 denominator that lets a cut rule be written without re-surveying, and the declared-plane corroboration with its positive control -- are evidence for Z-S46's finding rather than a separate finding, and Z-S48 says so itself. The row that carries the mechanism and owes the remedy is Z-S46, which GRADUATES at C-S11.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S48"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ROW'S OWN WORDS ARE THE DISCRIMINATOR, which is why this dismissal needs no judgment call the row did not already make: 'THE REUSABLE PART IS Z-S46's OWN SENTENCE and this row does not improve on it. What this row adds is a DENOMINATOR for it.' Contrast Z-S38, dismissed nowhere and graduated at C-S11, which adds a third principal and a three-instance cut rule its target does not contain. The two rows are the same SHAPE -- this seat's L8 read of a worker's finding -- and they separate on content, not on shape. That is the test Z-S84 demands and it is the reason this batch does not sweep either way.",
        "THE CORROBORATION IS SOUND AND IS PRESERVED ON C-S11: shared-infra/opal-portal-lambda-role.tf grants the READ verbs and not PutMetricData, absent from all 13 tracked .tf naming that role, with a working positive control -- inf-pipeline/iam.tf and yang-pipeline/iam.tf both carry the verb, so the probe finds it where it exists. The AccessDenied is what the declared shape predicts.",
        "THE DENOMINATOR IS CARRIED WITH ITS OWN CAVEAT, which matters more than the number: 1 of 55, and the row warns that the obvious probe for this shape returns 3 and is WRONG ABOUT ALL 3. A criterion that alternates OUTCOMES ('or file a row') or DENOMINATORS ('or 20 of 20 with the reason') is NOT this shape and must not be swept in with it; only an alternation of INSTRUMENTS is. Z-S48 filed the wrong count in its own working notes before reading the three in full and recorded that rather than the clean number alone."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Z-S48 is a corroboration record whose substance belongs to the finding it corroborates, and that finding is graduated separately.",
    "notes": "UNDISPOSITIONED after C-S11 and this row: 94 of 163 (was 101, which included the Z-S163 this seat filed against its own backlog an hour into this pass). THE RUNNING SHAPE OF THE PASS, worth stating once at this point rather than at the end, and MEASURED rather than recalled -- this seat's first draft of this sentence said '26 closed, 16 dismissed, 10 graduated' from memory and every one of the three was wrong, which is the same unverified-count shape that produced this document's 166: counted across all ten of this seat's adjudication rows, 45 items are closed -- 34 DISMISSED_WITH_REASON and 11 GRADUATED -- so roughly THREE IN FOUR of the rows this pass has closed are rows ABOUT rows. That is not padding. It is what an append-only channel looks like when seats correct themselves in public instead of editing, and the alternative -- a channel of 60 clean findings with no visible retractions -- would be the worrying one. Z-S84 remains UNDISCHARGED and Z-S90 remains HELD for the slug-level DECOMP_INVALIDATING the gate correctly refuses mid-pass."
  }
]
```

## C-S13 -- three findings GRADUATE whose remedies have LANDED, each verified on the artifact rather than accepted from the row

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S13",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:45Z",
    "one_line": "L9, round 2: Z-S42, Z-S47 and Z-S49 GRADUATE, and TWO OF THE THREE HAVE REMEDIES THAT ALREADY LANDED -- verified here on the ledger and the face, not accepted from the rows claiming them. Z-S42 found that an apply the record said never ran HAD run; its holder closed the leg on the MEASUREMENT exactly as NEVER-2 prescribes and did NOT re-execute. Z-S49 found that a mandated logging path could not deliver and would fail as SILENCE; its criterion was amended to pre-authorise the one existing resource by name and cite the row. Z-S47 is the one still open: a CLOSED ledger leg certified an artifact that did not yet exist, and NOTHING IN THE CONTRACT GOVERNS THAT DIRECTION.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "UNCHANGED PER MEMBER. Z-S42: 0.7.0_AE_CloudOps~S with 2.0.0_SA_COO~Z as issuer -- DISCHARGED, see evidence. Z-S49: 2.0.0_SA_COO~Z -- DISCHARGED at the Z-S55 ruling and the face amendment. Z-S47: the owner of the deploy-ledger contract and NEVER-2's text, routed via 1.0.0_SA_CTO~Z, and it is the only member of the three with an act still owed. This row performs no remedy and assigns no new owner.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S42",
      "NFRA_OPSEC202609-Z-S47",
      "NFRA_OPSEC202609-Z-S49"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S42 -- THE REMEDY LANDED IN THE FORM THE ROW OFFERED, AND THE LEDGER SAYS SO IN ITS OWN WORDS. The entry now reads 'Status: CLOSED -- nothing stranded -- closed 20260903T162328Z' with all 6 legs proven, and L5's proof states: 'MEASURED LIVE STATE at 2026-09-03T16:14:44Z by 0.7.0_AE_CloudOps~S -- NOT from an apply this session ran. NEVER-2 governs: an open leg is a missing RECORD, not an unchanged WORLD, so the leg closes on measurement and the act is not repeated.' That is Z-S42's recommendation adopted verbatim by the seat that owed it, and the re-execute the stale instruction called for did NOT happen. The row's TAG DISCRIMINATOR was adopted too and travels in L5's proof as a named qualifier: the plan row carried tags empty-to-five, a third element the face's 'two expected diffs' does not name, and 'no console toggle writes that combination, which is independently what settles that an apply OF THAT PLAN ran'.",
        "Z-S49 -- THE CRITERION WAS AMENDED AND CITES THE ROW BY ID, read at the face rather than inferred: S17R28-AC3 now requires the apply's changed-resource list to contain only the new bucket, its configurations, 'AND EXACTLY ONE PRE-AUTHORISED EXISTING RESOURCE, aws_s3_bucket_policy.access_logs (the Z-S49 RULING below -- it is IN-SCOPE and its change type must be update, never replace); ANY OTHER existing resource in that list is a STOP and a row'. The spec tension the row named -- that making delivery possible required editing an existing resource while the criterion forbade any existing resource in the list -- is resolved by enumeration rather than by widening the bound.",
        "Z-S47 -- STILL OPEN, AND CONFIRMED IN THE LEDGER'S OWN TEXT rather than only in the row that reports it: L1's target reads 'dynamodb.tf flip + demo import declaration committed' -- TWO artifacts -- and its proof reads 'commit 464c58b859 ... dynamodb.tf kms_key_arn onto the project key + ledger entry; 2 files / 36 insertions / 2 deletions'. The two files are dynamodb.tf and the ledger entry; the declaration is NOT among them and could not have been, because L1 closed at 13:11:25Z and the import that produced the file closed at L4, 13:20:39Z. A CLOSED leg certified an artifact that did not yet exist, no seat then held an open obligation to commit it, and the file sat untracked until 16:09Z -- found by a peer reading the WORLD, never by the record.",
        "WHY Z-S47 IS THE MEMBER THAT MATTERS MOST DESPITE BEING INERT AT SURFACING: NEVER-2 governs an entry left OPEN and its remedy is 'measure the artifact'. Nothing governs the CLOSED direction, and A CLOSED LEG PROVES ONLY THAT A SEAT WROTE CLOSED. The asymmetry is in the cost: an open entry INVITES the check, a closed one CLOSES the question -- which is why the open direction cost about seventy seconds of confusion here and the closed direction cost three hours. TWO CHEAP SHAPES, both the contract owner's and neither taken here: one artifact per leg, so a hash cannot close a two-artifact target; or a close-time check that the proof names every artifact the target names.",
        "GRADUATED RATHER THAN DISMISSED FOR ALL THREE, on Z-S20's test: each has a mechanism of its own (a false record; a permission-conditioned delivery path that fails as absence; a contract that governs only one direction) and a remedy of its own (close on measurement; amend the criterion; close the contract gap). That two remedies are already PERFORMED does not make them dismissals -- Z-S24 graduated on the same footing at C-S5, and a finding whose remedy landed is the success case of graduation, not the absence of one."
      ]
    },
    "spec_asserts": "Every ledger leg carries proof of its stated target before CLOSE, a criterion grading a delivery path must be satisfiable, and a finding graduates when it carries its own mechanism and its own remedy.",
    "world_is": "Two of these three findings produced landed corrections that are readable on the ledger and the face; the third names a gap in the ledger contract that is still open in exactly the direction nothing checks.",
    "notes": "THE REUSABLE PART OF Z-S49, worth carrying to L10 because it is not about S3: a permission-conditioned delivery path fails as an ABSENCE, so any criterion grading it on a DELIVERED OBJECT must also confirm the deliverer is PERMITTED -- otherwise the UNCOMPUTABLE branch absorbs a permission denial and reports it as latency, and the window expires without anyone learning which it was. The row also names the near-miss honestly: the assignee could have quietly added the ARN and reported a clean delivered object, and both criteria would have read PASS while the never-widen bound was consumed silently. IT WAS FILED BEFORE THE EDIT, WHICH IS THE ONLY REASON THAT IS VISIBLE. WHAT THIS ROW DOES NOT DO: it does not re-grade any criterion, does not close the Z-S47 contract gap, and does not claim who applied the r2b plan or when beyond what Z-S44's PITR pin measured."
  }
]
```

## C-S14 -- four correction records dismissed, two of them this seat's own withdrawal of a recommendation the issuer overruled and was RIGHT to overrule

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S14",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:45Z",
    "one_line": "L9, round 2: four RECORDS are DISMISSED WITH REASON -- Z-S44 (the integrator pinning Z-S42's apply to a measured instant), Z-S54 (the integrator retracting an offer in Z-S42's own notes), Z-S52 (this seat's L8 recommendation on Z-S49) and Z-S59 (this seat withdrawing that recommendation after the issuer overruled it). NONE HAS A MECHANISM OF ITS OWN. Z-S59 says so in terms -- 'THIS ROW ADJUDICATES NOTHING' -- and Z-S44 says it 'adds evidence and removes an instruction, it arms nothing'. Their substance is carried on C-S13, which graduates the three findings they refined.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- an evidence pin, a retraction of an offer, a recommendation, or the withdrawal of that recommendation -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Every operative consequence is carried on C-S13: Z-S44's measured instant is the discriminator that let Z-S42's holder close on measurement rather than re-execute; Z-S52's one surviving reading (that the CRITERION rather than the deliverable needed amending) is exactly what the issuer amended and is recorded on Z-S49's graduation; Z-S54's retraction removes an offer from a durable record and arms nothing.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S44",
      "NFRA_OPSEC202609-Z-S52",
      "NFRA_OPSEC202609-Z-S54",
      "NFRA_OPSEC202609-Z-S59"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S44 -- a single-limb supersession, and the instrument is worth preserving even though the row is not: PITR's EarliestRestorableDateTime on opal-partner-demo reads 13:21:50Z, and point-in-time recovery CANNOT restore to before it was switched on, so that value IS the moment of the apply. The ledger closed L4 at 13:20:39Z, putting the apply about seventy seconds later. It supersedes Z-S42's inferred bracket with a measured instant and changes nothing else -- the finding, the tag discriminator, the INERT standing and the disarm owner all stand as filed.",
        "Z-S54 -- RETRACTS AN OFFER THAT INVITED LAUNDERING, and the seat it was offered to refused it correctly. Z-S42 had said that if the holding seat knows it applied, its word closes the question. That seat answered that it CANNOT take the offer: it is a fresh session with no continuity to the seat killed at ~14:0xZ, holds no recollection either way, and anything it said about its own past acts would be RECONSTRUCTED FROM THE SAME ARTIFACTS the filing seat already read, WEARING THE COSTUME OF TESTIMONY. That is the durable lesson and it is preserved here: a respawned seat's account of its predecessor's acts is not a second instrument, it is the first instrument in a different voice.",
        "Z-S52 AND Z-S59 -- THIS SEAT WAS WRONG AND THE ISSUER WAS RIGHT, stated plainly because the dismissal should not read as tidying it away. Z-S52 argued Z-S49's dilemma dissolved because the fix was to MOVE the log target's single source pin rather than EXTEND it. The issuer ruled EXTEND and the world settles it: opal-data-security is STILL DELIVERING into that target under prefix evidence-store/ -- 172 objects, newest 2026-09-03T17:35:07Z, its logging configuration declared and applied -- so a MOVE would have left a live, declared, currently-delivering configuration permanently refused, producing the EXACT silent empty-prefix failure Z-S49 was filed about, one bucket over.",
        "THE TWO ERRORS IN Z-S52 WERE BOTH THIS SEAT'S AND ARE NAMED IN ITS OWN WITHDRAWAL: (1) it asserted a WORLD fact -- 'the target serves exactly one source before and after' -- from FOUR spec carriers and no live instrument; (2) it leaned on a 'NOT widened' clause whose subject, read verbatim, is a SHARED audit-log bucket the project does not own, as if it governed how many project-owned sources the project's own target may admit. A READING DERIVED CORRECTLY FROM A FROZEN SPEC IS A FACT ABOUT THE SPEC, and becomes a claim about the world only when a world instrument says so. No amount of further spec reading surfaces the difference, and carriers agreeing with each other raise confidence about INTENT and never about STATE.",
        "WHAT SURVIVES Z-S52 AND IS NOT RE-DERIVED: its reading that S17R28-AC3 rather than the deliverable was the clause needing amendment -- which is what the issuer amended -- and its ordering point, that S3 validates the target's permissions when the SOURCE's logging configuration is set, so the policy edit lands BEFORE the new bucket's logging block is enabled. Both are carried on C-S13."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Four rows are records refining three findings; the findings graduate at C-S13 and the records close here.",
    "notes": "UNDISPOSITIONED after C-S13 and this row: 87 of 163. THE PATTERN THIS BATCH ADDS, and it is a different one from the earlier threads: here TWO SEATS OVERRULED THIS SEAT AND BOTH WERE RIGHT -- the issuer on EXTEND-versus-MOVE, and the respawned lane seat on refusing to testify about a predecessor's acts. Neither correction cost the world anything because both arrived before the act. THE RECORD SHOULD CARRY THAT AS PLAINLY AS IT CARRIES THIS SEAT'S CATCHES: an adjudicator that only logs the errors it finds in others is running a biased census of itself. Z-S84 remains UNDISCHARGED; Z-S90 remains HELD for the slug-level DECOMP_INVALIDATING the gate correctly refuses mid-pass (Z-S163)."
  }
]
```

## C-S15 -- the two worker findings against THIS SEAT'S OWN VERDICT graduate, and both remedies landed on BOTH carriers

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S15",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:55Z",
    "one_line": "L9, round 2: Z-S53 and Z-S56 GRADUATE. BOTH ARE A WORKER CATCHING A DEFECT IN THIS SEAT'S OWN TICK-6 VERDICT, found in the face's mandated pre-write re-read, and BOTH REMEDIES ARE NOW LANDED ON BOTH CARRIERS -- verified here on the face and the verdict ledger rather than accepted from any row. Z-S53: AMEND D printed the method split as 39 = 20 non-OPTIONS + 19 OPTIONS; the live API reads 21 + 18, wrong by ONE IN EACH DIRECTION so the TOTAL was right and every check that verified the total passed. Z-S56: AMEND C row 4 demanded 0 to add while the SAME sentence named the deployment as an expected diff and row 2 of the same verdict MANDATED creating it -- a self-contradiction in one sentence, and the worker measured 1 to add and HELD rather than reinterpreting the criterion it was graded on.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z as the face's issuer and 1.0.0_SA_CTO~Z as the verdict ledger's driver -- BOTH DISCHARGED, see evidence. This row assigns no new owner and reopens neither ruling. The release of the held apply was the issuer's word and was given; the apply itself is not this seat's act and is not certified here.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S53",
      "NFRA_OPSEC202609-Z-S56"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S53, CARRIER ONE -- THE FACE IS CORRECTED IN PLACE: TO-OP-S-1's face now prints '39 = 21 non-OPTIONS + 18 OPTIONS' and the face reads status complete. The wrong split is gone from it.",
        "Z-S53, CARRIER TWO -- THE VERDICT LEDGER IS CORRECTED BY APPEND, AND BETTER-FORMED THAN PROSE: org/tier1_exec/1.0.0_SA_CTO/drive_pairs/NFRA_OPSEC202609/VERDICTS.jsonl holds 5 rows. Row 3 (ts 2026-09-03T11:51:40Z, tick 6) still carries the wrong figures, as an append-only ledger must. Row 5 (ts 2026-09-03T17:49:17Z, tick 14) carries state 'VERDICT-CORRECTION' and the MACHINE-READABLE field `corrects_row: 3`, with the call 'AMEND D's OPTIONS split, carried verbatim in ledger row 3 from verdict 19674, is WRONG by one in each direction.' A reader of the stale row has a typed pointer to its correction, which is stronger linkage than the surprise channel's prose `adjudicates` and is worth noting as the better pattern.",
        "Z-S56 -- THE BAR WAS RE-SCOPED ON THE FACE AND THE RULING CITES THE ROW BY ID: the face now carries 'THE Z-S56 RULING (issuer, 2026-09-03 17:5xZ) -- THE Z-S14 BAR IS SCOPED TO THE IMPORTED OBJECTS, AND TWO ADDITIONS ARE PRE-AUTHORISED AND ENUMERATED. THE DEFECT IS THE ISSUER'S, IN A SINGLE SELF-CONTRADICTING SENTENCE', and the expected-change set is enumerated as EXACTLY THREE -- the in-place body update, the CREATE of the body-triggered deployment, and provider default_tags on both stages' tags_all -- with 'anything outside those three is a STOP and a row'. The issuer took the defect as its own rather than the worker's.",
        "THE PROTECTED OBJECT IS ALSO GUARDED MECHANICALLY AND NOT ONLY BY PROSE, which is why the re-scoping costs nothing the bar was protecting: the imported REST API declares prevent_destroy = true, so the catastrophic case Z-S14 was written against -- a plan that RECREATES a live resource -- is refused by terraform itself.",
        "WHY BOTH GRADUATE RATHER THAN DISMISS, on Z-S20's test: each has a mechanism of its own (a denominator whose parts were wrong while its sum was right; a criterion that contradicted itself in one sentence) and a remedy of its own (correct the figure on both carriers; re-scope the bar and enumerate the expected changes). That both remedies are PERFORMED is the success case of graduation, consistent with Z-S24 at C-S5, Z-S42 and Z-S49 at C-S13.",
        "THE WORKER'S CONDUCT IS PART OF THE RECORD because it is what made both catchable: on Z-S53 it refused to substitute a corrected number into a frozen face, proceeded on limb 1 (which turns on the Z-S14 bar and the body-identity control and does not reference the OPTIONS partition), and stopped before limb 2 where the number becomes load-bearing -- so nothing stalled. On Z-S56 it measured the plan, found the contradiction, and HELD the apply rather than picking the reading it preferred, stating the rule exactly: a worker who reinterprets the criterion he is graded on has disabled the control."
      ]
    },
    "spec_asserts": "A verdict's printed denominator and a criterion's bar are the authority a worker is graded against, and both must be correct and satisfiable as written.",
    "world_is": "Two clauses of this seat's own tick-6 verdict were wrong -- one in its parts while right in its sum, one self-contradicting within a single sentence -- and both were caught by a worker before any write and corrected on every carrier.",
    "notes": "THE TWO GENERAL SHAPES, both worth more than their instances and neither this seat's to claim credit for. FROM Z-S53: A DENOMINATOR STATED AS A SUM OF PARTS INVITES VERIFICATION OF THE SUM, and the sum is exactly the quantity that cannot discriminate a right partition from a wrong one. Print the parts and check the PARTS. The sharper corollary, which Z-S57 adds: a number cross-checked against another carrier's number is corroborated only if both carriers measure the SAME QUANTITY -- here they measured method-bearing RESOURCES and non-OPTIONS METHODS and coincidentally agreed at 20. FROM Z-S56: a bar TRANSPLANTED from one premise into a cell with a different premise fails in the direction that looks like compliance. Z-S14's bar assumed a pure import; this cell's premise included a mandated create. || FOUR PRE-WRITE RE-READS THIS ROUND HAVE CAUGHT SOMETHING THE CUT CARRIED, and these two are the only ones where the thing caught came from THIS SEAT rather than from the world or the issuer. That is recorded plainly: the adjudicator's own verdict text is inside the blast radius of its own cut rules, and the instrument that caught it was a worker's mandated read, not any check this seat ran."
  }
]
```

## C-S16 -- three records dismissed, one of them a PARTIAL disarm whose other half stays ARMED and is named rather than swept

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S16",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T04:55Z",
    "one_line": "L9, round 2: three RECORDS are DISMISSED WITH REASON -- Z-S57 and Z-S58 (this seat confirming the worker was right and supplying the corrected text for its OWN verdict, twice) and Z-S87 (this seat discharging ONE HALF of Z-S85). Z-S87 IS THE CASE Z-S84 WAS FILED ABOUT AND IT IS HANDLED ACCORDINGLY: it discharges the AMEND C half that Z-S85 names this seat for, and expressly does NOT discharge the plan-wide clause, which is 2.0.0_SA_COO~Z's ruling and that seat's alone to relax. SO Z-S85 IS NOT DISPOSITIONED BY THIS ROW AND REMAINS OPEN, carrying its ARMED standing on the half nobody has ruled.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- two confirmations-with-corrected-text of this seat's own verdict, and one partial disarm -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Z-S57's and Z-S58's corrected text is the content of the remedies that landed, and those land on Z-S53 and Z-S56, which GRADUATE at C-S15; neither correcting row owns a carrier, and both say so ('this seat corrects its own number here and edits neither carrier'). Z-S87's discharged half is recorded against Z-S85, which stays OPEN on its undischarged half.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S57",
      "NFRA_OPSEC202609-Z-S58",
      "NFRA_OPSEC202609-Z-S87"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S57 AND Z-S58 ARE THIS SEAT CONCEDING TWICE, and the concessions were complete rather than hedged: 'Z-S53 IS CORRECT AND THE ERROR IS THIS SEAT'S' and 'Z-S56 IS CORRECT AND THE DEFECT IS THIS SEAT'S'. Z-S58 went further than the row it conceded to -- it measured that THREE of this seat's clauses expect the deployment (row 2 mandates it, row 4's second half names it, and AMEND D's S1-AC3 requires a NEW deploymentId on BOTH stages) against exactly ONE that forbids it, the clause transplanted from Z-S14. Strengthening the case against your own text is not a new mechanism; it is a better account of the same one.",
        "Z-S87 IS A PARTIAL DISARM AND NAMES ITS OWN BOUND, which is exactly what Z-S84 demanded an hour before it was written: DISCHARGED is the AMEND C half -- the bar is met and is not what fails, because Z-S58 re-scoped it to '0 add / 0 destroy AMONG THE IMPORTED OBJECTS plus three named expected changes'. NOT DISCHARGED is the plan-wide clause, 2.0.0_SA_COO~Z's ruling at 19905 and 19969, which only that seat can relax. Z-S87's own text says Z-S85 'stays ARMED on that half'.",
        "AND THE REASON THE SCOPED FORM SURVIVES WHILE THE PLAN-WIDE FORM CANNOT is measured rather than asserted: limb 2's shape is a BODY CHANGE, which on a body-managed REST API necessarily replaces an immutable deployment. The plan-wide clause was written when the shapes in view were an import and a first create. A bar scoped to the imported objects survives the shape change; a plan-wide 0-destroy cannot.",
        "Z-S85 IS VERIFIED TO REMAIN OPEN AFTER THIS DISMISSAL, not assumed to: it is absent from every `adjudicates` list in this channel, so its latest carrier still reads UNDER_INVESTIGATION. Dismissing the partial disarm while leaving the item open is the C-S4 bound applied for the third time in this pass, and it is the specific act Z-S84 exists to force."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition, and a partial disarm dispositions only what it actually discharges.",
    "world_is": "Three rows are records; the two findings they concede to graduate at C-S15, and the item one of them partially disarms stays open on its unruled half.",
    "notes": "UNDISPOSITIONED after C-S15 and this row: 83 of 164 -- five items closed here against 87, and the Z-S164 register-drift row this seat filed in the SAME commit added one back. This seat first wrote 82 and the arithmetic was self-contradictory in its own sentence, since 82 is the figure BEFORE counting the row the sentence says it counts; corrected against the parser before the commit, which is the second count this pass has caught in its own draft. THE RUNNING TALLY OF WHO CAUGHT WHAT, stated because it is the honest frame for an adjudicator grading a round it contributed verdicts to: of the items closed so far, the defects found IN THIS SEAT'S OWN WORK by other seats now number four -- the two verdict clauses here (worker 0.7.0_AE_CloudOps~Z), the EXTEND-versus-MOVE recommendation (issuer, at C-S14), and this document's 166 denominator (2.0.0_SA_COO~Z, at 2c13e8202e). Every one arrived before it cost the world anything, and every one arrived through a mechanism this seat did not run: a worker's mandated pre-write read, an issuer's ruling, and a peer's independent census. Z-S84 remains UNDISCHARGED; Z-S90 remains HELD (Z-S163)."
  }
]
```

## C-S17 -- FIVE findings graduate, including the one that would have taken down a live data surface and the one that shows the same defect ALREADY SHIPPED on a different API

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S17",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:10Z",
    "one_line": "L9, round 2: FIVE GRADUATE. Z-S80 -- FWD-1 AS SPECIFIED WOULD TAKE DOWN A LIVE DATA SURFACE: 20 of f61h681z9g's 39 methods have NO CloudFront route, so the edge-injected header can never reach them and attaching the authorizer makes them PERMANENTLY UNREACHABLE, five live POST writes among them. Z-S83 -- THE SAME DEFECT ALREADY SHIPPED five hours earlier on a different API, where GET /metadata/yang was gated on a header with no ordered behavior at any depth, and S2-AC1 could not have caught it because its denominator measures ATTACHMENT and never REACHABILITY. Z-S60 -- C-16 asserts four condition slots on the log destination's two service grants and exactly ONE exists. Z-S62 -- limb 2 names a module that does not exist and a Lambda that structurally cannot serve a REST authorizer. Z-S64 -- graduates on its SEPARABLE half: a criterion pins a live CodeSha256 with NO vintage.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "UNCHANGED PER MEMBER AND NOT REASSIGNED. 2.0.0_SA_COO~Z as issuer for Z-S80 (its ENDPOINT half, which Z-S82 expressly left armed while disarming only the EXECUTION half), for Z-S83, and for Z-S62's limb-2 choice among A/B/C; with 3.0.0_SA_CVO~Z named alongside on Z-S80 and Z-S62 where FWD-1's SHAPE is touched. 1.0.0_SA_CTO~Z at L4 for C-16's wording on Z-S60, with 2.0.0_SA_COO~Z owning the S28-AC1 criterion text. Z-S64's vintage half is the criterion's owner at L6. NOTHING IS BUILT, CHOSEN OR APPLIED HERE.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S60",
      "NFRA_OPSEC202609-Z-S62",
      "NFRA_OPSEC202609-Z-S64",
      "NFRA_OPSEC202609-Z-S80",
      "NFRA_OPSEC202609-Z-S83"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S80 -- THE SHARPEST FINDING OF THE ROUND, and it was caught at a DESIGN READ before a line was written. A control keyed on a property the EDGE injects can only protect paths that traverse the edge, so THE COVERAGE OF THE CONTROL IS BOUNDED BY THE COVERAGE OF THE ROUTING -- and nothing in the face or the decomposition checks that the two sets match. The face measured 39 methods and 1 authorizer; nobody measured how many of the 39 have a path along which the key can arrive. Option C (attach to all 39 as written) is a 20-method outage including five live writes. PARTIALLY DISARMED ONLY: Z-S82 disarmed the EXECUTION half and its own text says the endpoint-shape half 'is expressly NOT disarmed here'. This graduation carries the ENDPOINT half, still live.",
        "Z-S83 -- THE SAME GRAIN SPLIT, ONE API OVER AND ONE PLANE EARLIER, IN A FACE THAT IS COMPLETE, ACCEPTED AND APPLIED. Eight of TO-OP-S-2's nine attached routes sit under the /v1/* behavior; the ninth, GET /metadata/yang, has NO ordered CloudFront behavior at any depth. TO-OP-S-2 IS NOT RE-GRADED AND S2-AC1 STAYS PASS -- it claimed attachment on 9 of 9 and the live plane reads 9 of 9; nothing in that instance is false. THE GAP IS THAT ATTACHED AND REACHABLE ARE TWO PROPERTIES AND THE FACE ONLY EVER HAD A CRITERION FOR THE FIRST. This is CLAUDE.md rule 22's shared-dependency clause with a live specimen: nine per-member checks all passed while the property they SHARED -- an edge-injected key with no edge path for one of them -- went unmeasured.",
        "Z-S83's DISARM IS KNOWN TO BE UNRUNNABLE and that is carried here rather than left for the owner to discover: the row named the disarm as a caller enumeration over the access-log plane, and 2.0.0_SA_COO~Z measured that get-stages on 7k3ed8px20 returns AccessLogSettings.DestinationArn null and DetailedMetricsEnabled false. THERE IS NO ACCESS-LOG PLANE ON THAT API, and the API-wide 4xx series is confounded by this round's own probe traffic. So 'does a caller exist' is not merely unmeasured, it is UNANSWERABLE with the instruments that exist. The owner needs a different disarm, and the row's own author established that at Z-S86.",
        "Z-S60 -- AN ALIGN LIMB FINDING WHAT AN ALIGN IS FOR. C-16 and S28-AC1 describe opal-data-security's two service-principal grants as 'each with SourceAccount + SourceArn'. Measured on the applied plane: AllowCloudFrontAccessLogDelivery carries SourceAccount and NO SourceArn; AllowALBAccessLogDelivery carries NEITHER. ONE of four asserted condition slots exists. The DECLARATION AGREES WITH THE WORLD, so the plan is legitimately 0 changes and the face's STOP does not fire -- what disagrees is the SPEC'S TEXT against both. A BUILD compares the world to nothing and a plan compares the world to the DECLARATION; when those agree, only a human-written criterion quoting the spec back at the applied plane can catch it.",
        "Z-S62 -- A PLAUSIBLE NAME STANDING WHERE THE WORLD HAS SOMETHING ELSE, for the third time on this one face. The face requires the new authorizer to REUSE opal-portal-authorizer's secret-read module and forbids a second copy; there IS no module (the read is inline in a single 358-line index.mjs, confirmed on this seat's own repo read), and that Lambda answers in HTTP-API v2 shape, which a REST REQUEST authorizer structurally cannot consume -- policyDocument 0, principalId 0, Statement 0, Effect 0, execute-api:Invoke 0, against generateSimpleResponse 5. All three obvious paths are blocked by the face's own words, and the issuer must choose among A, B and C. This row does not choose.",
        "Z-S64 -- GRADUATES ON ITS SEPARABLE HALF ONLY, and the split is named so no reader takes it wider. Its confirmation of Z-S62 is a record. What graduates is the finding its own text calls out as surviving the A/B/C decision: exactly ONE of the project's 8 filed proof instances pins a CodeSha256 and its evidence carries NO ISO VINTAGE. A criterion asserting a live equality without recording WHEN it was read cannot distinguish 'still true' from 'was true' -- the exact distinction this project has spent the day on in three other places."
      ]
    },
    "spec_asserts": "A control attached to a method protects that method, a criterion describes the resource it grades, and a face names artifacts that exist.",
    "world_is": "Two of these five are the same defect -- a control gated on an edge-injected property with no edge path -- one caught before the write and one already applied; the other three are a spec overstating a resource's controls, a face naming a module that does not exist, and a pin with no vintage.",
    "notes": "THE ONE THAT SHOULD REACH L10 AHEAD OF THE OTHERS is Z-S83's closing point, because it is about method rather than about a route: A RULE STATED FORWARD AT THE MOMENT IT IS LEARNED LEAVES EVERY ACT ALREADY TAKEN UNDER THE OLD UNDERSTANDING UNEXAMINED -- and those are exactly the acts nobody revisits, because they are CLOSED and their criteria all read PASS. When a round promotes a finding to an issuance rule, THE SAME TURN should ask which COMPLETED faces the new rule would have failed. Here that cost ten minutes of reading and found one route on two faces. || WHAT IS NOT CLAIMED, per Z-S83's own disclosure: no probe was run against either endpoint (the OP-x-1 list is CLOSED at seven and an eighth is not on it), no access log was read, and NOBODY CAN SAY WHETHER ANYTHING IS ACTUALLY BROKEN -- only that a route is gated on a key that cannot reach it. It is a latent trap, not a demonstrated outage, and it is filed ARMED because the harm from being wrong is asymmetric: if a caller exists it has been failing since 16:24:34Z, and if none exists the disarm is cheap."
  }
]
```

## C-S18 -- three records dismissed, one of which retracted a limit this seat had only ASSERTED was closable

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S18",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:10Z",
    "one_line": "L9, round 2: three RECORDS are DISMISSED WITH REASON -- Z-S61 (this seat's second-plane confirmation of Z-S60), Z-S86 (this seat withdrawing both the disarm AND the framing of its own Z-S83, after the issuer supplied what it had missed) and Z-S95 (the worker correcting its own Z-S80 headline from four live POST writes to FIVE). None has a mechanism of its own; each refines a finding that graduates at C-S17. Z-S95's corrected number is the one a decision will be made on, so it is carried onto Z-S80's graduation rather than left in a dismissed row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- a second-plane confirmation, a double withdrawal by an author, and a headline correction by an author -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Every operative contribution is carried on C-S17: Z-S61's fix-direction question and its gating unknown onto Z-S60; Z-S86's finding that Z-S83's named disarm is UNRUNNABLE onto Z-S83; Z-S95's corrected count of five live POST writes onto Z-S80. Z-S95 says of itself that it 'corrects a RECORD, not a state' and that no remediation is needed for the applied world.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S61",
      "NFRA_OPSEC202609-Z-S86",
      "NFRA_OPSEC202609-Z-S95"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S86 CARRIES THE INSTRUMENT LESSON OF THE NIGHT AND IT IS THIS SEAT'S OWN ERROR: 'A STATED LIMIT ASSERTS THAT THE MISSING INSTRUMENT EXISTS. Naming a limit honestly is not the same as verifying the limit is closable, and I did the first while believing I had done the second.' Z-S83 disclosed, as a limit, that it had not read the access-log plane -- which reads as scrupulous and quietly asserts that reading it is possible. One get-stages call established there is no such plane. The disclosure was honest and the inference behind it was not checked.",
        "AND Z-S86 WITHDRAWS A FRAMING, WHICH IS THE HARDER HALF: Z-S83 treated the deliberately-public state of /v1/metadata/yang as a BASELINE whose loss counts as harm. The issuer's correction, accepted in full: that public state is EXACTLY WHAT THIS PROJECT WAS COMMISSIONED TO CHANGE, and reverting a data route to public on an unmeasured suspicion, using an instrument that cannot confirm the suspicion, would undo the outcome to protect a caller nobody can find. THE FRAMING SILENTLY MADE THE PRE-PROJECT STATE THE THING TO PRESERVE. That is a bias an adjudicator is particularly placed to introduce and particularly unlikely to notice.",
        "Z-S95 IS A CORRECTION WITH ITS LINKAGE ALREADY BUILT, which is why nothing is owed beyond the dismissal: Z-S80's EVIDENCE enumerated all five POST writes correctly and only its one_line summary dropped POST /api/portfolio/export; the face's S1-AC3 amendment and a commit message both inherited the undercount. The worker's TO-OP-S-1 proof instance now states five with the enumeration AND CITES THIS ROW ID, so the corrected number and the wrong one are not both loose in the record without a link. THE APPLIED WORLD WAS NEVER WRONG: the 20 methods were identified by ENUMERATION, never by the summary count, so the attachment scope was right and only the headline was wrong.",
        "Z-S61'S CONTRIBUTION IS A QUESTION RATHER THAN A FINDING, which is why it records rather than graduates, and the question is carried: the repair direction for Z-S60 turns on an unknown NEITHER SEAT MEASURED -- whether those two delivery service principals SUPPORT aws:SourceAccount and aws:SourceArn at all. If they do, tightening the grants is this project's own purpose and the text then describes a stronger world. If a key is unsupported, C-16 must say WHICH and WHY, so a later reader does not read the absence as an oversight and re-add something that cannot work. Settle the support question FIRST, because it determines which repairs exist."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Three rows refine findings that graduate elsewhere; two of the three are a seat withdrawing or correcting its own committed text.",
    "notes": "UNDISPOSITIONED after C-S17 and this row: 75 of 164 -- counted with the parser rather than by arithmetic, after two draft counts earlier in this pass were wrong. THE STANDING COUNT OF DEFECTS FOUND IN THIS SEAT'S OWN WORK BY OTHERS OR BY ITSELF now reaches six: two verdict clauses (worker), the EXTEND-versus-MOVE recommendation (issuer), the 166 denominator (peer census), Z-S83's unrunnable disarm and its preserve-the-baseline framing (issuer, both at Z-S86). AN ADJUDICATOR GRADING A ROUND IT SUPPLIED VERDICTS TO SHOULD KEEP THAT NUMBER VISIBLE, because the alternative is a record in which the certifier is the only seat that never erred."
  }
]
```

## C-S19 -- the round's most serious security packet GRADUATES WHOLE: four rows, four DIFFERENT surfaces, nothing remediated and nothing touched

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S19",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:20Z",
    "one_line": "L9, round 2: Z-S127, Z-S140, Z-S141 and Z-S142 GRADUATE AS ONE PACKET AND FOUR DISTINCT SURFACES. A symmetric HMAC signing secret sits in CLEARTEXT Lambda environment variables on the trade pipeline's auth path, identical 60-character value on both trade-auth-handler and trade-authorizer, while the estate deliberately chose custody for the equivalent portal secret one path over -- TWO DIFFERENT ANSWERS TO THE SAME QUESTION ON TWO AUTH PATHS. It MINTS AND VERIFIES on a publicly reachable API whose prod stage has DisableExecuteApiEndpoint FALSE and six of seven routes CUSTOM-authorized by that same authorizer; it is readable by a MEASURED 14 of 231 principals including three human IAM users; abuse is UNCOMPUTABLE beyond 14 days because stage access logging was never enabled; and the same value is ALSO in remote Terraform state, a second read path reachable with no Lambda permission at all. NONE OF THE FOUR IS DISMISSIBLE: each names a different thing an owner must act on -- custody, reachability, detectability, and a second path any remediation must cover.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z at L4, routed by 2.0.0_SA_COO~Z per ruling 20224 -- no manifest row covers the trade pipeline's signing secret, minting one is an L4 act, and mid-round the spec is FROZEN. Andrew is named on Z-S141 by 20248 as being surfaced in the same turn. 2.0.0_SA_COO~Z holds the placement question on Z-S127 (this project's round 3, or the trade pipeline's owner). UNCHANGED BY THIS ROW. NOTHING IS REMEDIATED, ROTATED, MOVED OR RE-CONFIGURED HERE, and this seat neither designs the remediation nor sets its schedule.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S127",
      "NFRA_OPSEC202609-Z-S140",
      "NFRA_OPSEC202609-Z-S141",
      "NFRA_OPSEC202609-Z-S142"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S127 -- THE FINDING, and it was filed the way the law prescribes: found off-task while closing a gap in a DIFFERENT face's evidence (a deployed-byte scan cannot see a table name supplied by configuration, so all seven functions' environments had to be read, and JWT_SECRET was simply there), then ONE ROW AND KEEP WORKING. Its author expressly did not rotate it, did not read its plaintext into any committed artifact, and did not open a remediation, on the correct ground that a symmetric secret shared by two functions is consumed by whatever validates the tokens it signs, and rotating without that consumer census is how an auth path goes dark.",
        "Z-S140 -- THE SIZING, AND IT IS THE WORST OF THE ISSUER'S THREE BRANCHES: FORGEABLE AND REACHABLE. The 129-day dormancy was ABSENCE OF TRAFFIC, NOT ABSENCE OF WIRING -- an unauthenticated probe WOKE the authorizer and its log stream advanced from 129 days stale to now. DORMANCY LOWERS THE URGENCY AND NOT THE EXPOSURE: the first call after a year accepts a token forged today.",
        "Z-S140's METHOD IS THE PART WORTH CARRYING, because its author's own first sweep was wrong IN BOTH DIRECTIONS and it says so: (a) it simulated only GetFunctionConfiguration, while FIVE of eleven roles hold the capability solely via GetFunction, which also returns the environment -- they would have scored DENIED; (b) its script reported '0 IAM users' and nearly stood, because `bash .tools/aws iam list-users` invoked from a python subprocess CRASHES with a Windows ACCESS_VIOLATION (rc 3221225477) returning EMPTY stdout AND EMPTY stderr -- BYTE-IDENTICAL to 'this account has no users'. It was caught ONLY by a guard comparing the enumeration against the census user_count, and had it stood it would have dropped all three human principals, including both of Andrew's, out of the finding. A CRASHED PROCESS AND AN EMPTY POPULATION ARE THE SAME BYTES. A DOCUMENT SCAN ANSWERS 'WHICH POLICIES MENTION THIS' AND THE QUESTION WAS 'WHO CAN DO THIS'.",
        "Z-S141 -- A FINDING, NOT A DEMONSTRATED INCIDENT, AND EXPLICITLY NOT A DEMONSTRATED NON-INCIDENT EITHER, because no instrument reaches. The API HAS been successfully authenticated against: on 2026-01-07 it served 105 requests with ZERO 4xx and ZERO 5xx while the authorizer ran 18 times, and an authorizer DENY is a 4xx, so all 18 were ALLOW. Lifetime before the probe: 272 requests, ~237 non-error, 55 authorizer runs, 28 mint-path runs. BUT abuse detection is UNCOMPUTABLE beyond 14 days -- stage access logging was NEVER enabled, the authorizer's log group is 14-day retention, and no CloudTrail records this API's data events. That is its own surface with its own owner decision, not a restatement of Z-S140.",
        "Z-S142 -- THE SECOND READ PATH, and it LEADS WITH THE GOOD HALF for a reason: JWT_SECRET is assigned at trade-pipeline/lambdas.tf:59 and :90 as a VAR REFERENCE, so it is NOT a literal in the repo and there is NO GIT-HISTORY EXPOSURE. That rules out the worst available branch -- a signing secret in git history cannot be rotated by any AWS action and is readable by everyone who has ever cloned the repo. But terraform writes RESOLVED variable values into state in plaintext and this root's state is remote, so the reachable set is 'principals with s3:GetObject on that bucket' UNION the measured 14, and the first half is UNMEASURED. IT IS BOUNDED, NOT OPEN: that bucket returns BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy and RestrictPublicBuckets ALL TRUE with SSE-AES256, so this is authenticated-internal reach rather than public. ANY REMEDIATION SIZED ON 14 IS SIZED ON ONE PATH OF TWO.",
        "WHY ALL FOUR GRADUATE AND NONE IS SWEPT AS A MEASUREMENT-OF-ANOTHER: Z-S140, Z-S141 and Z-S142 were COMMISSIONED by the issuer's rulings (20224, 20248) as the measurements the routing was waiting on, and each returned a fact the others do not carry. Dismissing any one would delete a surface a remediation must cover -- and Z-S142 exists precisely because a remediation verified only against the Lambda-config path would PASS while state still carried the value. It adds a CRITERION rather than work: moving the value into a secret store referenced at runtime removes it from the Lambda config AND from state in one act."
      ]
    },
    "spec_asserts": "A signing secret is held in custody, not in cleartext configuration, and a control's exposure is sized over every path that reaches the value.",
    "world_is": "One symmetric secret mints and verifies on a live public API, sits in cleartext on two Lambdas and in plaintext Terraform state, is readable by a measured 14 of 231 principals plus an unmeasured state-read set, and its abuse is undetectable beyond 14 days.",
    "notes": "WHAT NONE OF THE FOUR CLAIMS, preserved verbatim from their authors because the restraint is the reason the packet is usable: none claims the secret HAS LEAKED, that any of the fourteen HAS read it, that the trade API HAS been abused, or that HS256 is wrong for this pipeline. The claim is that the secret is live, mints and verifies on a publicly reachable authorized API, and is readable by a measured set on two paths. || THIS IS THE SEVENTH INSTANCE OF THE Z-S122 SHAPE and Z-S142 names it as such: a count scoped to one MECHANISM while the value is reachable by another. Z-S136 was the sharpest previous case -- terraform as a second WRITER that no principal census could see because it needs no fourth principal. Z-S142 is its MIRROR: terraform as a second READ PATH, invisible for the same structural reason. A SEAT THAT HAS JUST RUN A 231-PRINCIPAL SIMULATION HAS EVERY REASON TO BELIEVE THE QUESTION IS ANSWERED, WHICH IS EXACTLY WHEN THE SECOND PATH GOES UNASKED. || NOTHING IN THIS ADJUDICATION TOUCHES THE WORLD: no rotation, no configuration edit, no state read, no probe. The one probe that exists is Z-S140's, taken by its author under the issuer's ruling, and it is cited rather than repeated."
  }
]
```
