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

## C-S20 -- three TOOLING findings graduate, all three about an instrument that answers CONFIDENTLY ABOUT THE WRONG OBJECT

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S20",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:30Z",
    "one_line": "L9, round 2: Z-S143, Z-S147 and Z-S161 GRADUATE, and all three are the SAME SHAPE on three different instruments -- AN INSTRUMENT THAT ANSWERS CONFIDENTLY ABOUT THE WRONG OBJECT COSTS MORE THAN ONE THAT ANSWERS UNCERTAINLY ABOUT THE RIGHT ONE. Z-S143: the canonical nodejs build silently corrupts the estate's own source-of-truth manifest on EVERY build, and the ASCII rule that would catch it is enforced ON COMMIT MESSAGES ONLY -- so every audit of 'is the ASCII rule enforced' answers YES while a build script writes nine non-ASCII characters into the file Rule 4 designates as the pairing authority. Z-S147: the same build fails from the /cygdrive mount and reports 'No source_dir found in lambda-source-map.json' when the fault is the PATH -- naming a file the seat has very likely just edited. Z-S161: a multi-line argv value through .tools/aws.cmd is SILENTLY TRUNCATED at the first newline while the API returns rc=0 WITH a VersionId and AWSCURRENT, and a JWT signing key lived 3m52s in production as its 27-byte first line.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "UNCHANGED PER MEMBER. The CI lane owns infra/aws/lambda/ci/build-nodejs-lambda.sh for Z-S143 and Z-S147, with 2.0.0_SA_COO~Z to ROUTE -- and both are correctly NOT this project's to fix, since TO-OP-S-10B and TO-OP-S-10C are scoped away from the CI script and 0.7.0_AE_CloudOps~W declined the fix on exactly that ground. 2.0.0_SA_COO~Z on Z-S161, where shared tooling is not one lane's to change unilaterally. NOTHING IS FIXED, ROUTED FURTHER OR SCHEDULED HERE.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S143",
      "NFRA_OPSEC202609-Z-S147",
      "NFRA_OPSEC202609-Z-S161"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S143 -- THE CONTROL IS REAL, ENFORCED, AND POINTED AT THE WRONG SURFACE, which is a harder defect to see than an absent gate. Measured at HEAD versus worktree: HEAD holds 0 non-ASCII characters and 18 escaped \\u00XX sequences; the worktree holds 9 DISTINCT non-ASCII characters and 0 escaped sequences, across entries nobody in this project touched. An agent cannot get ONE decorative character into a commit MESSAGE -- measured, refused outright, and this seat hit that same refusal tonight. A build script puts NINE into the CONTENT of the pairing authority, unattended, on every run.",
        "Z-S143's SEVERITY IS BOUNDED BY ITS OWN AUTHOR RATHER THAN LEFT TO INFLATE, and the bound is why it is ARMED rather than urgent: walking the whole parsed document, EXACTLY 8 string fields carry a non-ASCII character and every one is PROSE (6 _build_note, 2 _note). ZERO functional fields are affected -- source_dir, files, artifact_sha256, tf_file, tf_resource, artifact_s3_key, runtime, build_type, handler, iam_role, last_deployed_commit and pipeline are clean across all 204 entries. The manifest's PAIRING DATA IS INTACT. What is corrupted is its prose, which is also what a human reads first when deciding whether an entry can be trusted. The estate has a recorded incident of ONE non-ASCII character crashing the deploy gate (2026-09-01, U+2B50, cp1252), and this file is read by build scripts, record-terraform-deploy.sh, drift checks and the staleness census.",
        "Z-S147 -- THE ERROR MESSAGE ACTIVELY POINTS AWAY FROM THE FAULT, which is why a one-word workaround does not make it INERT: to_native_path matches only ^/([a-zA-Z])/, so it converts /c/... and passes /cygdrive/c/... through UNCHANGED; bun is a native Windows binary and cannot read a /cygdrive path, so the map read returns empty and the script blames the MAP. BOTH MOUNT FORMS ARE LIVE ON THIS DEVICE, so which one a caller's cwd happens to carry decides whether the estate's standard Lambda build works. The workaround is available only to someone who already knows the diagnosis, and the message points at a file the seat has very likely JUST EDITED -- which is exactly what happened to its author, who read 'No source_dir found' as 'your correction did not take'.",
        "Z-S161 -- VERIFIED LIVE AND UNGUARDED ON THE ARTIFACT, not accepted from the row: the newline guard was BUILT at 4fb9eafdfe (1.0.0_SA_CTO~Z) and REVERTED at 1b0af4d39e by the same author, whose own subject says it 'BROKE THE CROSS-DEVICE AGENTBUS and protected nothing'. A census of .tools/aws returns ZERO occurrences of a newline guard today, while .tools/aws.cmd -- the genuinely truncating path Z-S161 named -- IS PRESENT. So the hazard is undischarged. The doctrine that DID catch it is canonical at .tools/AWS_SHIM_SILENT_FAILURES.md, present at 104 lines.",
        "Z-S161's THREE GENERALISATIONS, none of them about AWS: (1) A WRITE RECEIPT CERTIFIES THAT A VERSION WAS CREATED, NEVER WHAT IT CONTAINS -- and the more specific the receipt looks (an id, a stage, a timestamp) the more it reads as content confirmation. (2) THE PRECAUTION AIMED AT THE WRONG LAYER IS WORSE THAN NONE, because it retires the worry: shell=False was chosen ON PURPOSE against a known hazard and felt careful, while the corrupting layer was a CMD shim underneath it. NAME THE LAYER A DEFENCE ACTS ON BEFORE CREDITING IT. (3) A FIX CAN ARM THE HAZARD IT LOOKS LIKE IT CLOSED -- writing the correct key is what poisoned AWSPREVIOUS, so the recovery path degraded precisely BECAUSE the primary was repaired, and nothing announces that.",
        "SCOPE HONESTLY STATED AND NOT WIDENED BY THIS ADJUDICATION, in Z-S161's own words: the truncation is measured on put-secret-value ONLY. Every other .tools/aws.cmd call carrying a multi-line argv value is EXPOSED BY THE SAME MECHANISM but is NOT measured, and neither that row nor this one claims a census of them."
      ]
    },
    "spec_asserts": "The estate's ASCII rule binds production code and data, the canonical build works from any supported mount, and a write receipt evidences what was written.",
    "world_is": "A build script corrupts the manifest's prose on every run under a rule enforced only on commit messages; the same script fails on one of two live mount forms and blames the wrong file; and a CMD shim truncates multi-line secret material while every receipt reads success.",
    "notes": "ALL THREE WERE FILED BY SEATS THAT DECLINED TO FIX THEM, CORRECTLY, AND THE REASON IS THE SAME IN EACH: the fix belongs to a lane the face is scoped away from. Z-S147's author states the distinction that makes this right and it is worth carrying to L10: DECLINING THE FIX AND DECLINING THE RECORD ARE DIFFERENT ACTS, AND ONLY THE FIRST WAS THAT SEAT'S TO MAKE. Z-S143 exists because its finder left it in a BROKER MESSAGE -- the one carrier that reaches nobody once the sessions end -- and a second seat checked a 141-row census for duplicates before filing, having advised against a duplicate an hour earlier. That is the channel working exactly as designed, and it is the third instance tonight of a finding that would have died in an inbox."
  }
]
```

## C-S21 -- two records dismissed, one of which is this seat MEETING a defect five hours early and reading it as its own bug

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S21",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:30Z",
    "one_line": "L9, round 2: Z-S144 and Z-S162 are DISMISSED WITH REASON. Z-S144 is this seat reporting that it TRIPPED OVER Z-S143's corruption FIVE HOURS BEFORE IT WAS FOUND and read it as its own platform quirk -- which is the answer to why the defect survives. Z-S162 is a worker retracting its own row's REMEDY CANDIDATE after building the guard and having it reverted, while its FINDING stands untouched. Neither carries a mechanism of its own; both refine findings that graduate at C-S20.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a RECORD ABOUT ANOTHER ROW -- an account of a reader meeting a defect and passing, and the retraction of one remedy candidate -- with no mechanism of its own to graduate and no remedy of its own to route, on Z-S20's underlying test. Z-S144's contribution is an explanation of PERSISTENCE, which strengthens Z-S143's account and is carried onto its graduation; Z-S144 does not claim the dismissal it describes was unreasonable. Z-S162 retracts REMEDY CANDIDATE (a) and says in terms 'WHAT IS RETRACTED IS THE REMEDY, NOT THE FINDING' -- Z-S161's evidence, mechanism, blast radius and second-order AWSPREVIOUS defect all stand exactly as filed, and Z-S161 graduates carrying them.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S144",
      "NFRA_OPSEC202609-Z-S162"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S144 IS THE MEASURED INSTANCE THAT EXPLAINS WHY NO HUMAN READER CAUGHT Z-S143: at ~01:0x, censusing lambda-source-map.json for an unrelated row, a bare json.load on that exact file died with UnicodeDecodeError, 'charmap' codec can't decode byte 0x9d in position 31662. This seat added an explicit utf-8 encoding, the file parsed, and it moved on. THE SYMPTOM PRESENTS AS THE READER'S OWN PLATFORM QUIRK, the workaround is one keyword argument, and afterwards the file reads correctly -- so the question 'why does a JSON manifest contain non-ASCII bytes at all' never gets asked. Z-S143 explains why no GATE caught it; Z-S144 explains why no READER did.",
        "AND Z-S144 REFUSES THE EASY VERSION OF ITS OWN LESSON, which is why it is worth preserving rather than merely closing: it does NOT claim the dismissal was unreasonable. The estate's standing guidance for that exact error IS to pass an explicit encoding, that guidance is correct, and following it is what a competent reader does. A CORRUPTION WHOSE SYMPTOM IS INDISTINGUISHABLE FROM A COMMON LOCAL MISCONFIGURATION IS EFFECTIVELY INVISIBLE, BECAUSE THE CORRECT REMEDY FOR THE COMMON CASE IS ALSO THE THING THAT SUPPRESSES THE SIGNAL. The tell that WOULD have separated them was available and unasked: a data file that has always been ASCII acquiring non-ASCII bytes is a fact about the FILE, not about the reader's codepage, and one git diff on the bytes settles it. This seat had the file open and did not ask.",
        "Z-S162'S RETRACTION IS VERIFIED ON THE COMMITS RATHER THAN ACCEPTED: the guard was built at 4fb9eafdfe and reverted at 1b0af4d39e, both by 1.0.0_SA_CTO~Z, whose own revert subject reads 'my @4fb9eafdfe newline guard BROKE THE CROSS-DEVICE AGENTBUS and protected nothing'. The reason is structural: .tools/aws NEVER REACHES cmd.exe on either branch and so cannot truncate at all, while .tools/aws.cmd -- a genuinely different CMD batch file, the one Z-S161 named -- remains unguarded and still truncates.",
        "THE GUARD'S FAILURE IS Z-S161'S OWN SHAPE REPEATED, which is the durable lesson rather than the AWS specifics: A PROPERTY VERIFIED ON THE LIMB IN HAND, ASSERTED OVER A DOMAIN NEVER ENUMERATED. Z-S161 measured truncation on put-secret-value and DECLARED THAT SCOPE HONESTLY; the guard measured 'no legitimate caller passes a newline' on the surface it examined and DID NOT. One comp-find for .tools/aws callers would have found agentbus-sqs.sh BEFORE the commit instead of after.",
        "AND THE REMOVAL IMPROVED THE ESTATE'S POSITION, which is the counter-intuitive part worth keeping: A SEAT BELIEVING A GUARD COVERS IT IS WORSE OFF THAN A SEAT THAT KNOWS NONE DOES. The operative rule held all along and is the ONLY thing that caught the 27-byte key -- TREAT ANY .tools/aws WRITE AS UNVERIFIED UNTIL YOU READ IT BACK -- now canonical at .tools/AWS_SHIM_SILENT_FAILURES.md, verified present at 104 lines."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Two rows are records refining tooling findings that graduate at C-S20; one explains why a defect went unseen by readers, the other retracts a remedy that was built and reverted.",
    "notes": "UNDISPOSITIONED after C-S20 and this row: 66 of 164, read from the parser. Z-S162 ALSO CARRIES THE CORRECTION-MECHANICS LESSON THIS WHOLE CHANNEL RUNS ON, and it is worth quoting where the adjudication can see it: its author's first instinct was to append the correction INSIDE Z-S161, 'which reads as tidier and destroys the audit trail. The gate refused and named why. A correction is a NEW item citing the old id -- the wrong text must stay legible or nobody can see what changed.' That is the same discipline this adjudication has applied to its own C-S4 coverage error and to the header's 166."
  }
]
```

## C-S22 -- the rotation gate GRADUATES: FWD-10 is impossible as the system stands, the consumer set is FOUR not two, and ONE OF THE FOUR IS THE SIGNER

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S22",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:45Z",
    "one_line": "L9, round 2: Z-S100, Z-S107 and Z-S109 GRADUATE. Z-S100 is a GATE THAT WAS WORTH MORE THAN THE BUILD IT BLOCKED -- both modelled consumers of the login signing key are SINGLE-SLOT, so FWD-10's no-sign-out rotation is impossible as the system stands, and the authorizer's cache has NO TTL AT ALL, making S10-AC2's 'wait for both consumers to be serving the new key' UNSATISFIABLE AT ANY WAIT LENGTH. Z-S107 then measures that THE CONSUMER SET IS FOUR, NOT TWO, AND ONE OF THE FOUR IS THE SIGNER ITSELF -- opalinvest-auth-handler reads the PRIVATE and PUBLIC key in the same artifact, and the face does not mention it at all. A rotation that teaches two verifiers a second slot and never touches the signer HAS NOT BEEN DESIGNED. Z-S109 is separable and standing: the edge role's prefix wildcard lets FIVE functions read the PRIVATE signing key when exactly ONE needs the public key.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z on all three, UNCHANGED. Z-S100's remedy is explicitly 'a separate cut' in the face's own deliverable 1, so it is an L6 re-cut. Z-S107's S10B-AC0 reserves the re-cut to the issuer in terms. Z-S109 is ROUTED and expressly NOT acted on, on that seat's own direction that the wildcard must NOT be narrowed inside a rotation face -- coupling a signing-key rotation to an unrelated IAM change on a LIVE, REPLICATED edge role means a rotation failure and an IAM failure become indistinguishable. NOTHING WAS TAUGHT, BUILT, DEPLOYED, ROTATED OR NARROWED, by those seats or by this one.",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S100",
      "NFRA_OPSEC202609-Z-S107",
      "NFRA_OPSEC202609-Z-S109"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S100 -- THE FINDING IS THE PRODUCT, not a failure to deliver: the face states that deliverable 1 IS a gate and the single-slot finding is what it was for. Nothing was rotated, no secret written, no Terraform run, and NO LEDGER OPENED -- an opened ledger would have asserted an act that must not begin. Confirmed on THREE PLANES: source at 998c79b970, the DEPLOYED bundles (exactly one occurrence of the secret id in each), and THE SECRET ITSELF, a bare 452-char PEM with exactly one BEGIN block.",
        "Z-S100's SECOND DEFECT IS SHARPER THAN ITS HEADLINE AND IS NOT A RESTATEMENT: even if both consumers were taught two slots tomorrow, opal-portal-authorizer's cache at index.mjs:25-28 has NO TTL -- 'if (publicKey) return publicKey;' -- so a warm execution environment holds the pre-rotation key for the life of that environment, and Lambda does not bound that lifetime. YOU CANNOT WAIT OUT A CACHE THAT NEVER EXPIRES. The remedy is therefore TWO changes, a second slot AND a TTL, and the project has already written both -- for the ORIGIN secret, in the same file tree, in the same authorizer. THE EDGE, the one the face warned would be forgotten, is the BETTER-behaved of the two: it has a 300s TTL and would converge. The authorizer, which looks more ordinary, is the one that cannot.",
        "Z-S100's DECISIVE READ WAS THE CHEAPEST AND MOST SKIPPABLE ONE, and the row says so: fetching the secret's own VALUE. Source and deployed bytes both say 'one scalar', but a scalar holding a JSON envelope with two keys inside would have made every one of those readings TRUE and the conclusion WRONG. The envelope check separates 'the code holds one variable' from 'the system knows one key' -- and it only counted because a KNOWN-TWO-SLOT secret was run through the same probe in a separate invocation to prove the probe could see slots at all.",
        "Z-S107 -- MEASURED, NOT INHERITED, AND IT IS A STOP RATHER THAN A WIDENING: 5 roles grant the read across 221 roles scanned (not 2); the upper bound is 31 live functions (not 25); 4 of 29 scannable deployed artifacts carry the secret id; CloudTrail shows 3 of them calling GetSecretValue in a 30-hour window and all 4 invoked within the last 10 minutes. The two the face does NOT name are opal-session-analytics and opalinvest-auth-handler -- THE ISSUER.",
        "Z-S107's SHAPE IS THE SAME SHAPE TWICE IN ONE FACE, AND THE SECOND INSTANCE IS THIS SEAT'S: a check scoped to the MEMBERS cannot see a defect in what the members SHARE. TO-OP-S-10 read two FUNCTIONS while the capability sat on the ROLES beneath them -- that was Z-S105's correction. Z-S105 then read two ROLES while the granting set was never censused -- so the bound it derived EXCLUDED lambda-edge-execution-role, the role carrying auth-validator-edge, one of the face's OWN two named consumers. The unscoped read that fixes both is get-account-authorization-details over all 221 roles, and it cost ONE CALL.",
        "Z-S107's INSTRUMENT LESSON, which is why it ran two planes: they disagreed on exactly ONE member and that disagreement is the whole value of running both. A source census alone calls opal-session-analytics a consumer with no evidence it ever runs; a CloudTrail census alone omits it entirely and would have shipped a three-consumer answer that LOOKED measured. The log-group timestamp reconciles them and is a THIRD instrument neither plane contains.",
        "Z-S109 -- SEPARABLE, STANDING, AND CORRECTLY NOT COUPLED: lambda-edge-execution-role's inline policy allows GetSecretValue on the PREFIX WILDCARD opal/auth/*, covering the PRIVATE key and the origin-verify secret as well as the public key. The role carries FIVE functions and the code-plane census shows exactly ONE reads any opal/auth secret at all -- auth-validator-edge, which needs the public key only. WHY IT IS INERT rather than merely deferred, and the reasoning is sound: the wildcard grants READ, not WRITE, no function on that role reads the private key today, so THE GAP DOES NOT WIDEN AT ROTATION and nothing about this face makes it more dangerous than it already is."
      ]
    },
    "spec_asserts": "FWD-10 requires a signing-key rotation with no sign-out, which requires every consumer to hold two keys and to converge onto the new one.",
    "world_is": "Both modelled consumers hold one key, one of them forever; the real consumer set is four including the token issuer, which no face names; and a shared edge role grants five functions read access to the private key when one needs the public one.",
    "notes": "THE THIRD LEVEL OF ONE SHAPE, and Z-S109 names it: this project has now met the shared-dependency defect at THREE levels in one night -- functions under roles (Z-S105 correcting Z-S100), roles under a granting set (Z-S107 correcting Z-S105), and now permissions under a shared role (Z-S109). Whoever narrows the wildcard should ask whether five functions sharing one role is itself the question. || WHAT NONE OF THE THREE CLAIMS: Z-S100 does not claim the consumer population is two and says so in terms; Z-S107 does not claim opalinvest-auth-handler is the live login issuer, only that it read the public key 90 times in 30 hours and logged 10 minutes ago, so it is not dormant either way; Z-S109 does not claim the four functions have read anything. || THE RE-CUT THAT FOLLOWS IS THE ISSUER'S AND IS NOT DESIGNED HERE, but Z-S107's shape is recorded because it is measurement rather than preference: settle whether the issuer is live or legacy, decide whether the analytics consumer needs a slot or merely tolerates the rotation, and SIZE the deliverables against the resulting set rather than against 2."
  }
]
```

## C-S23 -- two records dismissed: this seat's bound, and this seat withdrawing it after a matcher that COULD NOT MATCH produced a false absence

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S23",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T05:45Z",
    "one_line": "L9, round 2: Z-S105 and Z-S108 are DISMISSED WITH REASON -- this seat's upper bound of 25, and this seat's own withdrawal of it after Z-S107 measured 31. THE WITHDRAWAL NAMES A FAILURE MODE WORTH MORE THAN THE NUMBER: the bound was derived from a LITERAL-STRING search for 'jwt-public-key' across terraform, and lambda-edge-execution-role grants the read on the PREFIX WILDCARD opal/auth/*, which does not contain that string. THE MATCHER WAS STRUCTURALLY INCAPABLE OF MATCHING IT -- a FALSE ABSENCE produced by an instrument that could not match, not by a gap in coverage. And the role it missed carries one of the two consumers the face itself names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both are RECORDS ABOUT Z-S100 and Z-S107 -- an intake bound and its withdrawal -- with no mechanism of their own to graduate and no remedy of their own to route, on Z-S20's underlying test. Z-S105's disarm as framed (that the re-cut STATE its consumer denominator and how it derived it) is exactly what Z-S107 then did, which is why that row is the better answer and why this one closes rather than graduating. Z-S105's central number is WITHDRAWN by its own author at Z-S108; what stands from it -- the DIRECTION that the surface is materially wider than 2, the arithmetic on the two roles examined, the clearing of ticket-center and partners-api as COMMENTS rather than grants, and the composition with the shared single-scalar Python module -- is carried onto Z-S107's graduation at C-S22.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S105",
      "NFRA_OPSEC202609-Z-S108"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FALSE ABSENCE IS THE KEEPER AND IT IS THIS SEAT'S OWN: a literal-string probe for 'jwt-public-key' cannot see a grant written as the prefix wildcard opal/auth/*. The instrument did not MISS the role -- it was incapable of matching it, which is a different defect from incomplete coverage and is invisible to every completeness check, because the probe reports a clean scan over a full denominator. THE ESTATE ALREADY BANKS THIS CLASS (a name search cannot enumerate wildcard grants) and this is a measured instance of it against a live IAM plane.",
        "AND THE COST WAS NOT ABSTRACT: the bound this seat published EXCLUDED lambda-edge-execution-role, which carries auth-validator-edge -- ONE OF THE TWO CONSUMERS THE FACE ITSELF NAMES. A row written to widen the face's denominator omitted a component already inside it.",
        "Z-S107'S METHOD IS THE RIGHT ONE AND IS CHEAP, which is what makes the failure worth recording rather than excusing: get-account-authorization-details over all 221 roles, evaluating EVERY statement with wildcard expansion on BOTH action and resource. One call. The instrument that answers 'who can do this' is a simulation or an authorization-details walk; a text search answers 'which files mention this'.",
        "Z-S108 IS A CLEAN WITHDRAWAL AND SEPARATES WHAT FALLS FROM WHAT STANDS, which is why nothing is lost by closing it: WITHDRAWN are the number 25 and the claim that the bound was derived from the granting set. STANDING are the direction, the reproducible arithmetic on the two roles examined, the two cleared terraform references, and the disarm as framed. It also names the part that is NOT its author's to carry further, correctly: the fourth reader is the SIGNER, and that belongs to Z-S107."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Two rows are this seat's bound and its withdrawal; the finding they bounded graduates at C-S22 on a peer's better measurement.",
    "notes": "UNDISPOSITIONED after C-S22 and this row: 62 of 165 -- the denominator moved because 0.5.0_AE_OpalETL~Z filed Z-S165 during this write (FWD-12's migration denominator counts callers, but two of the five execute THE SAME FILE, so migrating one migrates both). That row is NOT dispositioned here and is carried into the remaining pass. THE RUNNING COUNT OF DEFECTS IN THIS SEAT'S OWN WORK reaches seven with Z-S105's false absence. Six of the seven were caught by another seat's measurement rather than by this seat's re-reading, which is the honest shape of it: this seat's corrections have mostly been ACCEPTANCES of someone else's better instrument, not independent catches."
  }
]
```

## C-S24 -- the rotation STOP graduates on all three legs, and ALL THREE REMEDIES ARE ALREADY APPLIED ON THE DEPLOYED PLANE -- measured here on artifacts that postdate the rows

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S24",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T07:10Z",
    "one_line": "L9, round 2: Z-S157, Z-S159 and Z-S160 GRADUATE -- the three-legged rotation STOP was correct on every leg, AND ALL THREE REMEDIES ARE NOW APPLIED ON THE DEPLOYED PLANE, measured at this seat on artifacts that POSTDATE the rows demanding them. The rotation was barred by a VERIFIER with no TTL (opal-session-analytics, the busiest of the set), by the SIGNER's private-key cache that made the switch unobservable at any wait length, and by the SIGNER BEING ALSO A VERIFIER on /auth/refresh -- which would have signed out every returning user for seven days. Each leg is discharged on BYTES, not on a report. What is NOT discharged is the MFA seal key, and it is one of the two criteria reserved to this seat.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S157",
      "NFRA_OPSEC202609-Z-S159",
      "NFRA_OPSEC202609-Z-S160"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "WHY THESE GRADUATE RATHER THAN CLOSE QUIETLY: each row STOPPED an act that would have degraded a live surface in a way the estate's own instruments would have read as HEALTHY throughout. Z-S157: a rotation against a single-slot verifier running 52,540 invocations in 7 days yields a PARTIAL, SILENT, SELF-CLEARING outage of unbounded tail. Z-S159: a signer whose private-key read carries no time component makes S10-AC4 ('a login after the switch yields a token resolving to the NEW key') unsatisfiable AT ANY WAIT LENGTH, so the retired key could never be retired with confidence. Z-S160: the signer's PUBLIC read serves /auth/refresh through a current-only getter against a 7-DAY refresh lifetime, so writing the envelope signs out every returning user for a week -- FWD-10's own no-sign-out bar failing. Three findings, three different halves of ONE act, none of which a per-face check could see.",
        "THE DEPLOYED PLANE MOVED UNDER ALL THREE ROWS, AND THIS SEAT MEASURED THAT RATHER THAN INHERITING IT. opalinvest-auth-handler: the rows cite CodeSha256 ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk= shipped 22:38Z; get-function-configuration at 07:0xZ returns sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=, LastModified 2026-09-09T23:39:18Z, State Active. opal-session-analytics: Z-S157 cites TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU= (2026-09-04T05:44:08Z); live is 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko=, LastModified 2026-09-09T21:26:02Z. BOTH artifacts were re-downloaded and opened here; NEITHER digest is the one its row measured, which is the whole reason this adjudication is not a restatement.",
        "SIGNER, DECODED FROM THE MINIFIED DEPLOYED BYTES (not from source, and not from a name census). Public key: var D3=\"opal/auth/jwt-public-key\", gZ=300000; uZ() parses the envelope to {current, previous}; dZ() is the slots getter, guard `if(S8&&q-vZ<gZ)return S8` -- BOUNDED at 300 s. Private key: mZ() is getCurrentKey over a per-secret Map, guard `if(Q&&$-Q.atMs<gZ)return Q.value` -- BOUNDED at 300 s, with k8()=await mZ(B3), B3=\"opal/auth/jwt-private-key\". Two-slot accept: E8(q,$,Z,Q){try{return q.verify($,Z.current,Q)}catch(z){if(!Z.previous||z.name===\"TokenExpiredError\")throw z;try{return q.verify($,Z.previous,Q)}catch(J){throw z}}}. WIRING, which is the half a getter alone does not establish: A6() (verifyAccessToken) and nZ() (verifyRefreshToken) BOTH take `await lZ()` (the slot pair) into E8 -- so the refresh path Z-S160 named accepts current OR previous. Signing (v8, iZ) takes k8(), single-current, exactly as TO-OP-S-10E's rule requires and Z-S159's remedy specified.",
        "VERIFIER, DECODED THE SAME WAY: opal-session-analytics carries var i2=\"opal/auth/jwt-public-key\", n2=300000; r2() returns {current, previous}; R4() guards `if(y6&&q-x4<n2)return y6` -- BOUNDED at 300 s; B4() is the same current-then-previous accept; and t2(), the request-path auth check, calls `let $=await o2(), Q=B4(C4.default,Z,$,{algorithms:[\"RS256\"],issuer:s2,audience:a2})`. The two-slot path is not merely PRESENT in the bundle, it is ON the path that answers a request -- byte-for-byte the property Z-S157 measured as ABSENT five days earlier on the same function.",
        "*** THE INSTRUMENT TRAP THIS SEAT WALKED INTO, RECORDED BECAUSE IT IS THIS ROUND'S OWN BANKED LESSON AND IT STILL CAUGHT ME. *** The first pass over the signer bundle counted SOURCE-LEVEL identifiers and returned verifyWithSlots=0 and getJwtKeySlots=0, which reads as 'the two-slot path is absent' and would have INVERTED this adjudication into a finding that nothing had been fixed. It is the identical shape Z-S157 itself banked when a probe for `cachedPublicKey` returned 0 against a bundle where tsc had renamed it `wq`. A minifier renames every internal symbol, so an absence of a source name in a compiled artifact is not evidence about behaviour IN EITHER DIRECTION -- it fails toward 'unfixed' here and toward 'fixed' there, and both readings are unsound. The sound read was opening the call sites, and nothing was concluded from the zeros.",
        "STATE, NAMED PRECISELY (rule 22): this is APPLIED, not EXERCISED. The bytes that answer a request carry the bounded caches and the two-slot accept. This seat did NOT rotate anything, wrote and read NO secret value, and has therefore NOT observed a rotation converging end to end. A claim that FWD-10 now SUCCEEDS would need the act itself; what is established here is narrower and is stated as such -- the three specific mechanisms that made it fail are gone from the deployed artifacts.",
        "COVERAGE BOUND, INHERITED FROM Z-S157 AND NOT SILENTLY DROPPED BY THIS GRADUATION: that row's consumer census read 29 of 31 candidate artifacts. TWO were never read -- opal-news-ai-sentiment and news-semantic-clustering are PackageType Image (ECR), so there is no zip to fetch and closing them means pulling the images and searching their layers. A function building the secret id dynamically would not match a literal needle, and a reader outside the five granting roles (an inline policy, a resource policy on the secret, an EC2/ECS task, a human) is outside the frame entirely. THE CONSUMER SET OF FOUR IS A FLOOR ESTABLISHED OVER 29 OF 31, NOT A PROVEN TOTAL, and this graduation does not upgrade it to one."
      ]
    },
    "spec_asserts": "TO-OP-S-10 authorises the rotation on a denominator of 2 consumers; S10-AC3/AC4 presuppose that switching the signing key is an act with an observable, bounded completion and that a token minted under the OLD key still verifies after the switch; FWD-10's DONE WHEN is that nobody is signed out.",
    "world_is": "At the rows' vintage none of those held: the consumer set was four, the signer's caches were unbounded, and the signer's public read was current-only against a 7-day refresh window. At THIS write, measured on the deployed artifacts of both components, all three mechanisms are gone -- bounded 300 s caches on both key reads and a current-or-previous accept wired into every verify path, including /auth/refresh.",
    "notes": "WHAT THE THREE SHARE, WHICH IS WORTH MORE THAN ANY ONE OF THEM: a bounded-cache / two-slot property was applied to exactly the components each FACE was scoped to, while the rotation's real consumer set spans components no single face owned. TO-OP-S-10B taught the two verifiers it owned and was correct; TO-OP-S-10E made the signer select one key and was correct; and the act STILL could not be performed, because the union of correctly-scoped faces is not the same object as the act's blast radius. Z-S160 is the sharpest instance: S10E-AC2 graded PASS on accurate evidence because 'the signer' was treated as ONE role when that component is BOTH signer and verifier, and only the private half was the criterion's subject. That is rule 22's scoped-check clause at ROLE grain, and it is the third grain this round has produced it at (sub-string at Z-S154, member-vs-shared-dependency at Z-S122). || THIS SEAT CLAIMS NO CREDIT FOR THE REMEDIES AND DOES NOT KNOW WHICH ACT LANDED THEM. Two deploys (21:26Z and 23:39Z on 09-09) postdate the rows; whether they were cut in response to these rows or independently is NOT established here, and it is the issuing lane's record to make rather than this document's. Saying so is the point -- a graduation that quietly implies causation would be inventing a chain nobody measured. || WHAT REMAINS OPEN AND IS DELIBERATELY NOT CLOSED HERE: the MFA seal key. In the SAME signer bundle, y8() reads `if(P6)return P6; let q=await k8(); return P6=Buffer.from(j3(\"sha256\",q,Buffer.alloc(0),\"opal-mfa-code-seal-v1\",32)),P6` -- a bare scalar with NO time component, derived by HKDF from a private key that now refreshes every 300 s, and taken by both B1() (seal) and r3() (unseal). That is S10E-AC6, one of the two judgment criteria the L8 packet reserved to this seat, and it is graded in its OWN row rather than absorbed into this one.",
    "disarm_owner": "2.0.0_SA_COO~Z -- and this row disarms all three on the ARMED->INERT axis ONLY, on the deployed-bytes evidence above: the hazard each row named is gone from the artifacts that serve requests. It does NOT authorise the rotation. That GO is the issuer's, the seal-key criterion is still ungraded at this write, and the consumer-set floor of 29-of-31 stands as a floor."
  }
]
```

## C-S25 -- the blocked-IP thread graduates WHOLE (eight rows): Terraform is a SECOND WRITER of the sets C-2 reserves to one reconciler, the table's own primary key cannot hold the fixture and the observation of it, and the /wp-admin input is derivable but NOT safe

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S25",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T08:45Z",
    "one_line": "L9, round 2: EIGHT rows GRADUATE as one thread -- Z-S136, Z-S137, Z-S138, Z-S145, Z-S146, Z-S135, Z-S102, Z-S125. Three findings of record (Terraform as a second writer of all four blocked-IP sets; one primary key holding two lanes' incompatible facts; the /wp-admin allow-list absent and its two criteria coupled through that one missing input), one criterion that CANNOT PASS AS WORDED with the fork left to its issuer, and three measurement rows that each change what a reader would DO rather than merely restating a finding. Not one of the eight is a worker error; two are seats reporting their own.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW -- the four ARMED members keep the owners their own rows name (2.0.0_SA_COO~Z on Z-S136, Z-S145, Z-S102 and Z-S125). This row sets the remediation-track disposition and moves no hazard state; Z-S136 in particular stays ARMED, because a remedy MEASURED effective in a worktree is not a remedy applied.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S136",
      "NFRA_OPSEC202609-Z-S137",
      "NFRA_OPSEC202609-Z-S138",
      "NFRA_OPSEC202609-Z-S145",
      "NFRA_OPSEC202609-Z-S146",
      "NFRA_OPSEC202609-Z-S135",
      "NFRA_OPSEC202609-Z-S102",
      "NFRA_OPSEC202609-Z-S125"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S136 IS THE FINDING OF RECORD AND IT IS THE MOST CONSEQUENTIAL OF THE EIGHT. C-2 reserves wafv2:UpdateIPSet on the four blocked-IP sets to OP-s-15's reconciler -- 'nothing else ever calls UpdateIPSet'. Terraform declares `addresses = []` on all four and ENFORCES that on every apply, so it is a second writer of exactly the resource the constraint reserves. ⛔ THE ERASURE DOES NOT ARRIVE THROUGH A DELIBERATE ACT: any portal-auth or opal-gateway apply, by any operator, for any unrelated reason, wipes the reconciler's whole block list. Evidence is a LIVE UNSCOPED PLAN with the author's own file moved aside so it is a true BEFORE -- `Plan: 0 to add, 3 to change, 0 to destroy` with the diff `~ addresses = [ - \"203.0.113.42/32\", ]`. A queued deletion of a live entry, quoted from the plan rather than predicted.",
        "AND IT DEFEATS Z-S125'S ACCEPTED RISK IN THE DANGEROUS DIRECTION, which is why filing it separately was right: Z-S125 judged the residual erasure path to be an administrator's deliberate console click -- unlikely, self-repairing on the reconciler's next pass, accepted. Z-S136 makes the SAME erasure happen through an ORDINARY apply of an unrelated change. The accepted risk was priced against the wrong mechanism, and NO IAM CENSUS CAN DETECT IT because Terraform runs as a principal that legitimately holds the action.",
        "Z-S137 AND Z-S138 GRADUATE AS MEASUREMENTS, NOT AS RESTATEMENTS, and each is a different claim from Z-S136's. Z-S137 shows the proposed lifecycle guard IS EFFECTIVE -- 4 queued address deletions to 0 across both roots, live sets intact -- and a finding and its remedy are two claims, only the first of which Z-S136 could evidence. ⭐ IT ALSO NAMES A TRAP THAT WOULD OTHERWISE CAUSE A FALSE RE-RAISE: after the guard all four sets STILL read 'will be updated in-place', because their DESCRIPTION is separately drifted, so the discriminator is the DELETION COUNT INSIDE THE addresses DIFF and never the in-place line. A future seat reading the plan the obvious way would re-open a closed finding. ⛔ AND ITS AUTHOR IS THE SEAT THAT WROTE THE DEFECT, said plainly in the row: git log -1 on waf-cloudfront.tf returns 819d704105, 0.7.0_AE_CloudOps~S, who wrote `addresses = []` in BOTH roots and the comment asserting the sets are reconciled from the table.",
        "Z-S138 SIZES THE HAZARD AND IS THIS SEAT'S OWN L8 ROW, graduated here on the same test as any other: all four queued deletions are DOCUMENTATION-RANGE FIXTURES -- 203.0.113.42/32 inside TEST-NET-3 (RFC 5737) and 2001:0db8:dead:beef::/64 inside 2001:db8::/32 (RFC 3849) -- read live with get-ip-set over the complete population of 4 sets, 1 address each, reconciling exactly with Z-S137's queued-deletion count. So the hazard is LATENT rather than an active loss of protection. WHY THAT MATTERS RATHER THAN BEING A FOOTNOTE: an ARMED row's priority is set by what it would DESTROY and no row stated that; a reader meeting 'queued live ... right now' reasonably infers live protection being removed under them and orders their queue accordingly. Z-S136 is CORRECT AS WRITTEN and this does not soften it -- it prices it.",
        "Z-S145 IS A SCHEMA FINDING AND THE SHARPEST OF THE EIGHT: `address` is the partition key of opal-suspicious-addresses, so a fixture and the OBSERVATION OF THAT FIXTURE are one item, not two objects sharing a name. S19-AC2 requires a REAL edge refusal and the only address this device can originate from is its own egress, so the exercise MUST write 108.242.96.89/32 -- and the sentinel, working exactly as specified, observes the resulting blocked requests and writes THE SAME KEY. Three writers share one key space with no partition and no per-writer attribution: THE TABLE CAN EXPRESS WHAT IS KNOWN ABOUT AN ADDRESS AND CANNOT EXPRESS WHO ASSERTED IT OR WHY. It is ARMED for a data-integrity reason and not a security one -- OP-s-23's threshold distribution reads this table over a month-long window and S23-AC2 requires ordinary and anomalous traffic SEPARATED, which a self-inflicted exercise block silently violates.",
        "Z-S146 IS Z-S145'S MECHANISM FIRING, MEASURED TO THE SECOND, AND IT IS A SEAT REPORTING THAT IT DESTROYED ANOTHER LANE'S EVIDENCE -- twice, the first time silently. 05:58:25Z the sentinel writes a WATCH row on 108.242.96.89/32; ~06:00Z that seat sends a message stating it has NOT touched that row and will leave it as the other lane's evidence; the row was already gone. ⭐ THE KEEPER IS THE PRIMITIVE'S BEHAVIOUR: put_item REPLACES THE WHOLE ITEM -- not a merge, not an upsert of named fields -- returning success with no error, no warning, no diff and no audit line. hits, rules, paths_top, case_ids and first_seen all went in one call. THE OBSERVATION ITSELF SURVIVED (case 4f08be67dc53 intact in the evidence store with both WAF samples), so only the row POINTER was lost, and the row doubles as the exercise-origin annotation that stops a future reader treating a self-inflicted block as real attack traffic.",
        "Z-S102 AND Z-S135 ARE ONE INPUT SEEN TWICE. Z-S102: the /wp-admin allow-list is absent as the face anticipated, but the consequence is WIDER than the face states -- the source-restriction rule is the ONLY blocking rule this face may build, so with the managed groups in Count and both IP sets empty by design, its absence does not merely make S13-AC3 UNCOMPUTABLE, it removes the only mechanism by which S13-AC2 could demonstrate a refusal at all. TWO CRITERIA WRITTEN AS INDEPENDENT REST ON ONE MISSING INPUT. Z-S135 then supplies evidence Z-S102 was waiting for and refuses to overclaim it: five candidate addresses derived and cross-corroborated on two axes with a positive control, from 620,837 request lines -- and NOT A SAFE LIST, because 98.4% of apparent successes were attack traffic, three of five appear once and never again, and none is attributable to a person.",
        "⭐ AND Z-S135 CARRIES THE ROUND'S BEST INSTRUMENT TRAP, which is why it graduates rather than closing as a phase report: ON WORDPRESS THE STATUS SEMANTICS ARE INVERTED FROM THE OBVIOUS READING -- a FAILED login returns HTTP 200 because the form re-renders carrying an error, and a SUCCESSFUL login returns 302. Reading them the natural way inverts the answer completely, turning 87,819 failures into successes. That is a false-identity trap on a live security surface, and it is the same family as the round's other three.",
        "Z-S125 GRADUATES AND ITS FORK IS EXPLICITLY LEFT TO ITS ISSUER. S15-AC3 requires an enumeration showing ONLY the reconciler holds wafv2:UpdateIPSet on all four sets; enumerated on the APPLIED plane across 231 principals (224 roles + 7 users, both paginated to exhaustion), FOUR hold it -- opal-ipset-reconciler plus three human IAM users carrying administrator access through one group. ⛔ C-2'S INTENT SURVIVES INTACT: the reconciler is the only SERVICE principal and there is no second automated writer. THE INSTRUMENT WAS CONTROLLED BEFORE IT WAS TRUSTED, and the control is the reason the census is worth anything -- the reconciler was simulated FIRST and returns allowed on all four sets, because a broken query returns denied for everything and a clean estate looks identical. One --resource-arns per call, because two or more in one call flips held permissions to implicitDeny and would have manufactured a false clean."
      ]
    },
    "spec_asserts": "C-2 and PRD 7.3: opal-suspicious-addresses is the source of truth and OP-s-15's reconciler is the ONLY writer of the four blocked-IP sets. S13-AC2/AC3 are written as independent criteria. S15-AC3 requires an enumeration showing only the reconciler's role.",
    "world_is": "Terraform is a second writer of all four sets and a live plan is queued to delete an entry; the table's primary key cannot hold a fixture and its observation as two facts, and one lane silently destroyed another's row through it; the allow-list is absent, and both of the criteria that depend on it were written as though only one did; and four principals hold the action the criterion reserves to one.",
    "notes": "WHAT THE EIGHT SHARE: every one is a CONSTRAINT THAT IS TRUE OF THE INTENT AND FALSE OF THE MECHANISM. C-2 means 'no second automated writer' and is written as 'nothing else ever calls UpdateIPSet' -- so Terraform, and three administrators, falsify the text while leaving the intent standing. The table means 'one row per address' and cannot say who asserted what. S13's two criteria mean 'demonstrate a refusal' and both silently require one input nobody supplied. THE REPAIR IS ALMOST NEVER THE CODE -- it is that a constraint must be written so the mechanism that would violate it is IN SCOPE OF THE WORDS. || TWO OF THE EIGHT ARE SEATS REPORTING THEIR OWN DEFECTS (Z-S137's author wrote the `addresses = []` it reports; Z-S146's author destroyed the row it reports) and one is this seat's own L8 measurement. None is graded worse for that; the round is better evidenced because they filed. || THIS ROW MOVES NO HAZARD. Z-S136 stays ARMED: a guard measured effective in a worktree is DESIRED, not APPLIED, and Z-S137 says so itself."
  }
]
```

## C-S26 -- the third-verifier thread graduates (six rows): a registry entry that REDIRECTED A COMPETENT SEARCH and propagated a false belief through four carriers, a liveness oracle that reads DEAD on the most live consumer in the set, and a seat withdrawing its own word 'permanently'

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S26",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T08:55Z",
    "one_line": "L9, round 2: SIX rows GRADUATE as one thread -- Z-S110, Z-S111, Z-S123, Z-S124, Z-S134, Z-S139. Two findings of record (the lambda-source-map entry for opal-session-analytics is wrong on three axes and blocks its deploy path; that same function is the BUSIEST consumer in the set at 141,685 invocations where the ruling expected DEAD) and four rows that each correct or sharpen a claim rather than repeating one -- including a liveness oracle that returns a well-formed ZERO for the most heavily-used consumer of all, and a seat withdrawing one word of its own finding because the word was doing operational work the measurement did not support.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW -- the two ARMED members keep 2.0.0_SA_COO~Z, named on both. The source-map correction (Z-S110) and the re-cut that TO-OP-S-10 now waits on (Z-S123) are that lane's L6 acts, and neither is disarmed by an adjudication.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S110",
      "NFRA_OPSEC202609-Z-S111",
      "NFRA_OPSEC202609-Z-S123",
      "NFRA_OPSEC202609-Z-S124",
      "NFRA_OPSEC202609-Z-S134",
      "NFRA_OPSEC202609-Z-S139"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S110 IS A FINDING OF RECORD AND IT WAS FILED BEFORE A LINE WAS WRITTEN, which is the whole value of it. opal-session-analytics' lambda-source-map entry declares source_dir EXTERNAL with the note 'No repo source', runtime python3.11, and files [] -- while the source EXISTS at infra/aws/opalinvest_dev/lambda/session-analytics/src/ and the live function is nodejs20.x. A CI zip built from that entry would package NOTHING. The face's phase-1 pre-write read is what caught it; writing the two-slot change first and discovering an empty zip at deploy time was the alternative.",
        "Z-S111 IS THIS SEAT'S OWN L8 CENSUS AND IT MAKES Z-S110 STRONGER RATHER THAN QUALIFYING IT -- which is why it graduates instead of closing as intake. UNSCOPED and complete: all 204 map entries against 201 live functions (NextToken ABSENT, so 201 is a denominator and not a page), four axes each. 181 of 204 clean; source_dir MISSING ON DISK is ZERO of 204; and `files: []` IS NOT A DEFECT CLASS AT ALL -- all 12 are explained, 9 declared EXTERNAL and 3 PackageType=Image, residual ZERO. ⛔ THE INFERENCE THIS PREVENTS IS THE DANGEROUS ONE: a reader meeting 'wrong on three axes' could conclude the registry is unreliable and discount the finding as one more stale record in a rotten file. The census says the opposite -- the registry is maintained, and the LANGUAGE-level runtime mismatch is unique in 204. A singleton in a healthy registry is a sharper finding than a defect in a broken one.",
        "Z-S123 IS THE MEASUREMENT THAT INVERTED A RULING'S EXPECTATION: opal-session-analytics ran 141,685 invocations in 14 days -- 63x the portal authorizer and 32x the auth handler -- so it is not merely alive, it is the BUSIEST of the four consumers. msg 20121's trichotomy HELD EXACTLY and named the branch; only its parenthetical that DEAD 'is the likely answer' failed. THE ORACLE IS SOUND FOR THIS SUBJECT and the row says why: AWS/Lambda Invocations is a PLATFORM metric emitted by the service, not by application code, so for an ordinary Lambda a zero means not-invoked rather than not-instrumented.",
        "*** Z-S124 IS THE ROW OF THIS THREAD AND IT WAS CAUGHT BY A POSITIVE CONTROL, NOT BY SUSPICION. *** The same oracle, same parameters, same call-set, returns Sum=0 across 0 DATAPOINTS for auth-validator-edge -- a function with 680 GetSecretValue calls in a ~30-hour CloudTrail window, more than the other three consumers combined, and 47.4 MB of logs in us-east-1 alone. THE CAUSE IS NOT A ZERO, IT IS AN ABSENCE: list-metrics for that function+metric returns [], because Lambda@Edge executes in the region serving the request and does not publish this metric where the query looked. ⛔ AND THE CONSEQUENCE IS EXACT: DEAD is the branch of 20121's trichotomy that says 'remove it from the consumer set with evidence and rotate freely'. The instrument would have authorised rotating away the estate's most-used verifier, with a well-formed number and a clean denominator behind it. The warning was written about opal-session-analytics and came true about a different function.",
        "Z-S134 GRADUATES BECAUSE IT MEASURES WHAT A BAD RECORD COSTS, which almost nothing in this estate does. The map entry did not merely hold a false value -- it REDIRECTED A COMPETENT SEARCH: a seat read `_note` 'No repo source. Code must be downloaded from AWS', obeyed it, downloaded the deployment package, and found the repo source only afterwards and by a different route. ⭐ AND THE BELIEF PROPAGATED THROUGH FOUR CARRIERS BEFORE ANYONE RE-READ THE MAP -- row Z-S123's notes, TO-OP-S-10C's title AND its WHY section, and both GO messages 20143 and 20155. EACH CARRIER WAS FAITHFUL TO THE ONE BEFORE IT AND NONE WAS FAITHFUL TO THE REPO. The positive half is equally strong: the in-repo build path, exercised TWICE FROM CLEAN, reproduces the deployed artifact BYTE-FOR-BYTE on 12 of 12 outputs, so the source is provably production.",
        "Z-S139 IS A SEAT WITHDRAWING ONE WORD OF ITS OWN FINDING, AND THE WORD WAS LOAD-BEARING. Z-S123 said opal-session-analytics 'breaks PERMANENTLY ... cannot heal itself'. What survives: the cache has no time component (`if (cachedPublicKey) return cachedPublicKey;`, no invalidation), so no wait converges it and a runbook cannot carry a 'wait N minutes' step at ANY N as a guarantee. What falls: 'permanently'. The cache is bounded by CONTAINER LIFETIME -- median 5.6 min, p90 52.3, p99 138.0, max observed 143.0 over 107 measurable spans of 200 sampled, NextToken present so a FLOOR and not a census. ⭐ WHY THE OVERSTATEMENT MATTERED OPERATIONALLY RATHER THAN BEING MERELY IMPRECISE, and this is the keeper: 'breaks permanently' implies a hard visible outage requiring intervention -- which is ALARMING AND THEREFORE SELF-CORRECTING, because someone notices and someone fixes it. The measured shape is the opposite: a partial, silent, self-clearing degradation that nobody is paged for and that decays on a schedule nothing guarantees. A WRONG WORD IN THE ALARMING DIRECTION IS SAFER THAN THE TRUTH; this one was wrong in the safe-sounding direction of implying someone would notice."
      ]
    },
    "spec_asserts": "msg 20121's trichotomy conditions TO-OP-S-10's branch on whether the third consumer is alive; TO-OP-S-10B's deliverable 1 requires a build path that can write an artifact_sha256; and the lambda-source-map is the registry those build paths resolve through.",
    "world_is": "The registry entry for the third verifier is wrong on three axes and blocks its deploy; that verifier is the busiest of the four rather than dead; the oracle used to establish liveness is structurally blind to Lambda@Edge and returns a clean zero for the most-used consumer; the false 'no repo source' belief travelled through four carriers unchallenged; and the failure mode under rotation is partial and silent rather than permanent.",
    "notes": "WHAT THE SIX SHARE, AND IT IS THIS ROUND'S SIGNATURE AT A THIRD GRAIN: an instrument answering CONFIDENTLY ABOUT THE WRONG OBJECT. The source map answered about a source it declared absent and which exists. The Invocations metric answered about a function whose metric is published in another region. The word 'permanently' answered about a failure shape that self-clears. In all three the output carried every mark of rigour -- a real registry, a well-formed metric with a denominator, a committed row -- and in all three the discriminator was CHEAP AND NEARLY SKIPPED: read the directory, run the positive control, measure the container lifetime. || THREE OF THE SIX ARE CORRECTIONS AND ALL THREE MAKE THEIR TARGET SHARPER: Z-S111 makes Z-S110 stronger by proving the registry healthy; Z-S124 makes Z-S123's oracle trustworthy by finding exactly where it is not; Z-S139 makes Z-S123 usable by removing a word that would have mis-set the response. A round where corrections strengthen findings rather than eroding them is working. || THIS ROW MOVES NO HAZARD and neither ARMED member is disarmed: the source-map correction has not landed and TO-OP-S-10's second blocker is still standing."
  }
]
```

## C-S27 -- the opal-users retirement thread graduates (seven rows): a grant in a SIBLING TERRAFORM ROOT that makes the removal a no-op, a role that can DECRYPT OBJECTS IT CANNOT FETCH, a region that does not exist, and a seat retracting 'seven live lambdas' because ATTACHMENT IS NOT LIVENESS

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S27",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:05Z",
    "one_line": "L9, round 2: SEVEN rows GRADUATE -- Z-S112, Z-S113, Z-S119, Z-S128, Z-S130, Z-S114, Z-S41. Every one is the same class at a different grain: A NAME THAT NO LONGER DENOTES THE THING IT IS TRUSTED TO DENOTE. A Sid reading EvidenceStore names the LOG bucket. A role attachment reading 'seven lambdas' covers five that have not run in 51 to 129 days. An IAM line grants a table in a region holding ZERO tables. Terraform state says a table is managed while its declaration is UNTRACKED on a tree measured to lose uncommitted work. And a removal proven complete on the lines it was scoped to leaves the access live in a sibling root.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. All seven keep the owners their rows name -- 2.0.0_SA_COO~Z on six, and Z-S119's decision is reserved to A HUMAN routed through that lane. This row sets the remediation-track disposition only; NOTHING here authorises the opal-users delete, which is the one act in this thread that is irreversible.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S112",
      "NFRA_OPSEC202609-Z-S113",
      "NFRA_OPSEC202609-Z-S119",
      "NFRA_OPSEC202609-Z-S128",
      "NFRA_OPSEC202609-Z-S130",
      "NFRA_OPSEC202609-Z-S114",
      "NFRA_OPSEC202609-Z-S41"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S112 IS THE FINDING OF RECORD AND IT IS RULE 22'S SCOPED-CHECK CLAUSE ON A LIVE SECURITY SURFACE. A third grant on table/opal-users lives in a DIFFERENT terraform root -- trade-pipeline/iam.tf:63-64, trade-submission-lambda-role, GetItem/PutItem/UpdateItem/DeleteItem/Query/Scan on the table AND its index/* -- so removing portal-auth/iam.tf:50-51 revokes nothing in practice. A check scoped to those two lines verifies them PERFECTLY and certifies the table ungranted while the access stays live; every per-line arm passes and nothing fails. Measured on the APPLIED plane: GetAccountAuthorizationDetails, 221 roles / 1173 inline statements, exact matcher table/opal-users(?![-\\w]) excluding the -v2/-master/-trade siblings. POSITIVE CONTROL ON THE MATCHER FAMILY, which is what makes the 2-role result a measurement rather than an empty regex: table/opal-users-v2 returns 4 roles.",
        "Z-S113 FALSIFIES THE STATED PREMISE OF A STANDING CTO CONDITION, and does it with the stronger of two available controls. The condition forbade pruning iam.tf:51 because 'pruning :51 would revoke the us-east-2 grant ... and would BREAK access if us-east-2 is live'. It is not live: us-east-2 holds ZERO DynamoDB tables in the account. ⭐ THE INSTRUMENT CHOICE IS THE CRAFT HERE -- describe-table returning ResourceNotFoundException is a per-object 404 and could mean many things, but `list-tables --region us-east-2` returning {\"TableNames\": []} ON A SUCCESSFUL CALL (rc=0) proves the endpoint answered and the credentials worked, so the empty enumeration measures the REGION. That is a claim about the world; the 404 was only a claim about one name. Two records gave opposite instructions on the same line, and both were reasonable given what each knew -- the June plan explicitly CONDITIONED its instruction on 'if us-east-2 is live' and deferred the determination, which is why the deferral is what expired rather than either instruction being wrong.",
        "Z-S119 GRADUATES AS A MODEL OF STOPPING AT THE IRREVERSIBLE ACT, and this seat records it as such rather than merely dispositioning it. Everything the delete depends on is DONE AND PROVEN: on-demand snapshot AVAILABLE with 12 items and 4506 bytes matching the live table EXACTLY on both counts; both portal-auth grants removed at a7edcf6722 with the APPLIED-plane get-role-policy before/after showing the resource list go 7 -> 5, removing exactly the two table/opal-users ARNs; login proven unaffected before and after; the reader census re-run at this seat's own vintage across four planes with denominators. AND THE TABLE IS LEFT STANDING WITH 12 ROWS. What is missing is a decision, not evidence -- and the row says so in those words. A face that builds the whole ladder and declines the last rung, because the last rung is a human's, is the behaviour this estate's HARD STOPS exist to produce.",
        "Z-S128 AND Z-S130 ARE ONE CRITERION MEETING TWO DIFFERENT WALLS. Z-S128: S9C-AC4 requires all seven functions invoked before and after the removal, and TWO OF THE SEVEN CANNOT BE SAFELY INVOKED BY AN AGENT -- trade-submission-handler and trade-workflow-handler carry EMAIL_FROM=trades@opalinvest.dev and DASHBOARD_URL, so invoking them is capable of writing a trade submission and SENDING MAIL TO A REAL RECIPIENT. The criterion is RIGHT ABOUT THE RISK IT GUARDS (testing three of seven would miss a break) and still cannot be discharged honestly. The supporting oracle agreed anyway: 7 of 7 deployed artifacts content-scanned, ZERO unscannable, ZERO naming table/opal-users, and all 7 environment blocks read with the only users-table pointer being trade-auth-handler's USERS_TABLE=opal-users-v2 -- which closes the byte-scan's own blind spot of a name supplied by configuration.",
        "*** Z-S130 IS A SEAT RETRACTING ITS OWN PREMISE AND NAMING THE EXACT INFERENCE THAT PRODUCED IT: 'ATTACHMENT IS NOT LIVENESS, AND I NEVER ASKED THE SECOND QUESTION.' *** It wrote 'the execution role of SEVEN LIVE LAMBDAS' in Z-S112 from a graph census recording lambda.Role ATTACHMENT. Measured on two independent instruments, FIVE of the seven are DORMANT -- zero invocations in 30 days, last log events 51 to 129 days old -- and only TWO are live. ⛔ THE CONSEQUENCE IS STRUCTURAL RATHER THAN COSMETIC: ruling 20138's observation route is IMPOSSIBLE for the two mail senders it was written for, because they are among the dormant five and no window derived from their cadence exists; the two functions that ARE observable are not the two the ruling needs. THE POSITIVE CONTROL IS BUILT INTO THE SAME QUERY -- identical namespace, dimension shape and period returns real datapoints for two of the seven -- so the five zeroes are absences and not a broken probe.",
        "Z-S114 IS THE SHARPEST NAME-VERSUS-THING INSTANCE AND IT LEAVES A LIVE OPERATIONAL HOLE: opal-security-admin's policy names opal-data-security -- THE LOG DESTINATION -- under Sids that literally read EvidenceStoreObjects and EvidenceStoreBucket, while the actual evidence store since the split is opal-security-evidence, which the role cannot touch at all. Its KMS grant is CORRECT and points at the project key the NEW bucket uses. ⭐ SO THE ROLE CAN DECRYPT OBJECTS IT CANNOT FETCH -- a permission set that looks coherent on every per-statement read and is incoherent as a whole. Both planes measured: iam.tf:69/:78 name data_security, and a census of that file for 'security_evidence' returns 0 hits across 93 lines; get-role-policy live returns the same. ARMED for a concrete reason -- the sentinel being built under TO-OP-S-14-21 writes CASE FILES into opal-security-evidence, and the human who investigates a case holds this role.",
        "Z-S41 IS THIS SEAT'S OWN L8 ROW AND IT NAMES A STATE THAT IS WORSE THAN THE ONE IT REPLACED: opal-partner-demo is IN TERRAFORM STATE (imported 2026-09-03 under TO-OP-S-16-17-8R2) while the declaration justifying it -- demo.tf, 34 lines, sha256 5c19df6a... -- is UNTRACKED on a shared checkout this estate has measured to lose uncommitted work. Half-adopted is strictly worse than unmanaged: the pre-import condition blocked nothing, this one puts a live table one lost file away from a plan that wants to create or destroy it. The mitigation is real and is recorded as such -- deletion_protection_enabled = true on the module, an AWS property rather than a Terraform lifecycle guard, so it survives the file's loss. ⛔ IT DISPUTES NOTHING ABOUT THE IMPORT, the verdict that authorised it, the worker's execution, or the CTO's rescue of the file."
      ]
    },
    "spec_asserts": "TO-OP-S-9-11 and TO-OP-S-9C treat the portal-auth grant removal as the act that revokes access to table/opal-users, and S9C-AC4 requires all seven functions on the role invoked before and after. C-14 reserves evidence-store access to the operator role. The standing CTO condition 2 forbade pruning iam.tf:51 on the premise that us-east-2 might be live.",
    "world_is": "The removal is a no-op while a sibling root grants the same table to a role carrying seven functions; two of those functions cannot be invoked without an outward-facing side effect and five of them have not run in months; the us-east-2 grant points at a region with no tables at all; the operator role can decrypt evidence it cannot list or fetch; and a live table's declaration exists only as an untracked file.",
    "notes": "WHAT THE SEVEN SHARE, AND IT IS A DIFFERENT SHAPE FROM THE ROUND'S EARLIER THREADS: not a broken instrument, but A NAME THAT STOPPED DENOTING ITS OBJECT WHILE EVERY READER KEPT TRUSTING IT. `EvidenceStore*` Sids, a role attachment read as liveness, an ARN for a region with nothing in it, a state entry without its declaration, a two-line grant removal read as revocation. In each case the per-item check PASSES and the composite claim is false -- which is why every one of them was found by WIDENING rather than by looking harder at the same object. || THREE OF THE SEVEN ARE SEATS REPORTING AGAINST THEMSELVES, and Z-S130 is the strongest of the round so far because it names the general lesson in its own words rather than only the local error: attachment is not liveness, and the second question was never asked. THE ESTATE ALREADY BANKS THAT EXACT CLASS, and this is a measured instance of it against a live IAM plane. || ⛔ NOTHING IN THIS ROW AUTHORISES THE opal-users DELETE. Z-S119 reserved it to a human, correctly, and an adjudication is not that human's word. It stays reserved."
  }
]
```

## C-S28 -- the self-set figure msg 20858 corrects: BOTH numbers are right and they partition DIFFERENT SETS. The defect class is 6 items, not 67; the other 61 were this seat's open queue and 21 of them have closed since the slug was cut

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S28",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:15Z",
    "one_line": "1.0.0_SA_CTO~Z's msg 20858 s.2 corrects this seat's slug figure for this project from '6 self-set' to 67, on the ground that 82+18+6 does not sum to 167. THE ARITHMETIC IS RIGHT AND SO IS THE ORIGINAL FIGURE: they partition different sets. 67 = 6 items carrying a SELF-SET TERMINAL disposition + 61 items that were simply still UNDER_INVESTIGATION -- which is the value protocol s.4 REQUIRES at surfacing, and which the slug excluded by scoping its figure to 'the terminal set'. The defect C-S10 names is a TERMINAL value set by a non-adjudicator. That is 6 here, and 21 of the 61 have been adjudicated since the slug was cut.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE -- this row adjudicates no item and moves no hazard. It corrects a FIGURE this seat published, in the channel where that figure is load-bearing, because this seat's engagement with NFRA_REPORT's round ended at its slug and the number matters here rather than there.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BOTH PARTITIONS, COMPUTED AT THIS WRITE ON THE SAME PASS, SOURCE = THE INDEX (per msg 20853 s.2's reporting discipline): OVER ALL 167 ITEMS -- CVO 103, PEER 18, SELF/own-field 46, sums to 167. OVER THE TERMINAL SET ONLY -- CVO 103, PEER 18, SELF/own-field 6, sums to 127. Of the 46-item self bucket, 40 are still UNDER_INVESTIGATION. So the two figures differ by exactly the open queue, and always did.",
        "AT THE SLUG'S VINTAGE the same pass returned CVO 82 / PEER 18 / SELF-TERMINAL 6, with 61 open -- 82+18+6+61 = 167. msg 20858's 67 is 6 + 61. Neither number is wrong; one counts a DEFECT CLASS and the other counts a BUCKET. The slug's words were 'NFRA_OPSEC202609's TERMINAL SET is 82 CVO / 18 peer / 6 self-set', which is the scoped claim, and this seat is not withdrawing it.",
        "⛔ WHY THE DISTINCTION IS NOT PEDANTRY, AND IT IS THE ONLY REASON THIS ROW EXISTS: msg 20858 reads the 67 as '40% of the live project's items have never been adjudicated by anyone, their disposition being whatever the surfacing seat wrote in its own field'. For 61 of the 67 what the surfacing seat wrote is UNDER_INVESTIGATION -- the value protocol s.4 REQUIRES at surfacing and the value that means 'awaiting the CVO'. AN OPEN ITEM IS NOT A GOVERNANCE DEFECT; it is the CVO's queue. Collapsing the two makes an L9 in progress read as a channel out of control, and it would make the same project read WORSE the earlier in its round anyone measured it.",
        "THE DEFECT CLASS C-S10 NAMES IS NARROWER AND THAT NARROWNESS IS THE POINT: a row reaching a TERMINAL disposition -- GRADUATED or DISMISSED_WITH_REASON -- set by something other than a CVO adjudication row. Those are the ones no adjudicator will ever revisit, because they already read closed. Here that is 6 self-set plus 18 peer-set = 24 of 127 terminal. On NFRA_REPORT before C-S10/C-S11 it was 8 self-set plus 8 peer-set = 16 of 24, which is the proportion that made it visible there first.",
        "⭐ EVERYTHING ELSE IN msg 20858 s.2 IS ACCEPTED WITHOUT RESERVATION, including the parts that cost this seat something: that seat verified the mechanism at source rather than on the slug's word, and independently reproduced NFRA_REPORT's 8/8/8 by reconstructing it with C-S10/C-S11 excluded -- a reconstruction this seat did not perform and could not have claimed. That is corroboration on a different arm, and it is what makes the finding safe to act on.",
        "PROGRESS SINCE THE SLUG, stated because a queue figure ages faster than any other number in this document: the open set was 61 when the slug was cut and is 40 now -- C-S25 (8 rows, the blocked-IP thread), C-S26 (6, the third-verifier thread) and C-S27 (7, the opal-users thread) landed in between. The round opened at 138 undispositioned."
      ]
    },
    "spec_asserts": "Protocol s.4: `disposition` is UNDER_INVESTIGATION at surfacing and the TERMINAL value is set by the CVO's adjudication row. Section 8: an open item is not a zero and a round with an UNDER_INVESTIGATION row does not issue its slug.",
    "world_is": "Two seats measured the same channel and published 6 and 67. Both are correct over their own set. The estate-level claim worth carrying is the narrow one -- 24 of 127 terminal dispositions on this project were set by something other than an adjudicator -- because those are the ones that will never be revisited.",
    "notes": "THIS ROW ADJUDICATES NO ITEM, which s.4a admits ('a row that opens nothing'). It exists because the figure was published in a slug whose round is closed to this seat, and the honest carrier for a correction to a number about THIS project is THIS project's channel. || WHAT THIS SEAT GOT WRONG, since a correction row that finds no fault in itself is usually wrong: the slug should have PRINTED THE OPEN COUNT BESIDE THE THREE-WAY SPLIT. '82/18/6 of the terminal set' is true and invites exactly the sum msg 20858 attempted; '82/18/6 terminal, 61 still open, 167 total' could not have been misread and costs six words. A partition that does not show its own denominator is an invitation to reconstruct it wrongly, and the estate's own rule about printing the denominator beside the number covers this case precisely. || NO CHALLENGE IS OFFERED TO msg 20858's OTHER LIMBS and none of them turns on this: the NFRA_REPORT recut, the FWD-4 grade, the R3-1 criterion warning about scoring rendered output rather than source, and the s.3(a) routing of the slug/worker-row conflict are all accepted as written."
  }
]
```

## C-S29 -- eight rows graduate on ONE shape: AN ARTIFACT THAT OUTLIVED ITS OWN TRUTH AND KEPT DIRECTING. A closed ledger certifying code a later deploy removed, a decomposition holding open an edge ruled unbuildable, a PRD diagram routing evidence to the log bucket, and a criterion whose zero is an EMPTY LOOP

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S29",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:25Z",
    "one_line": "L9, round 2: EIGHT rows GRADUATE -- Z-S103, Z-S104, Z-S121, Z-S131, Z-S132, Z-S152, Z-S153, Z-S156. Six are artifacts that were CORRECT WHEN WRITTEN and now instruct an actor about a world that moved beneath them, and two are scope boundaries that do not hold at the mechanism (an agreement that deconflicts the COMMAND but not the SCOPE, and a -target that structurally cannot exclude another cell's work). The hardest is Z-S153: a deploy ledger closed 5 of 5 on a control that a LATER deploy silently removed from the box seven hours afterwards, using bytes OLDER than the ones it replaced.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. All eight keep the owners their rows name -- 2.0.0_SA_COO~Z on six, 1.0.0_SA_CTO~Z on Z-S131 as the L4 owner, 0.7.0_AE_CloudOps~Z on Z-S153 and ~S on Z-S132. Z-S103's disarm is the one that RELEASES work rather than gating it.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S103",
      "NFRA_OPSEC202609-Z-S104",
      "NFRA_OPSEC202609-Z-S121",
      "NFRA_OPSEC202609-Z-S131",
      "NFRA_OPSEC202609-Z-S132",
      "NFRA_OPSEC202609-Z-S152",
      "NFRA_OPSEC202609-Z-S153",
      "NFRA_OPSEC202609-Z-S156"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-S153 IS THE MOST SERIOUS ROW IN THIS BATCH AND IT IS RULE 22a's RUNNING-BYTES-OLDER-THAN-BUILT TRAP, MEASURED LIVE. *** TO-OP-S-12 deployed ~05:20Z and its ledger CLOSED 5 of 5. A later, unrelated deploy the same day replaced /opt/opal-gateway/app at 10:10Z with the bytes of commit 4c3999de4a -- WHICH PREDATES IT -- and the service restarted onto them at 12:52:29Z. The capability-token endpoints, the dual-accept and the FWD-12 observation instrument are ABSENT from the running code. ⛔ NOTHING IN THE FABRIC COULD NOTICE: the ledger was already CLOSED and carries no forward reference to its own supersession, and the ALB access logs kept flowing, so every downstream health signal stayed green while the certified control was gone. Measured on the RUNNING PROCESS rather than an assumed path -- one gateway dir, the unit's ExecStart, and the live pid's own cwd.",
        "Z-S152 AND Z-S131 ARE THE SAME DEFECT IN THE TWO DOCUMENTS THAT DIRECT WORK. Z-S152: the decomposition's s.9 hold list still tells a future actor to cut OP-s-13's order at the round-2 re-entry for 'CloudFront + WAF managed rules', while PRD v0.14's C-19 (NO-GODADDY) makes that edge UNBUILDABLE rather than deferred -- there is no AWS-only route to any edge for a site answering from a bare EC2 elastic IP, because AWS WAF cannot attach to one and every candidate requires a DNS change C-19 puts out of scope. Z-S131: PRD 7.3's pipeline diagram still routes case files to s3://opal-data-security/, the LOG DESTINATION, while the evidence store is opal-security-evidence -- AND THE SAME DOCUMENT SAYS BOTH, its own S17 row recording the rename in terms. A document that contradicts itself is worse than one that is merely stale, because each half corroborates a reader who arrives at it first.",
        "⭐ AND Z-S131 ENDS ON THE SAME SENTENCE Z-S114 DID, which is why the two are the strongest evidence for one estate-wide claim: A SPLIT RE-POINTS THE CELL THAT OWNS THE RESOURCE AND LEAVES EVERY OTHER REFERENCE BEHIND. Z-S114 found the operator role still granting the old bucket; this finds the PRD still diagramming it. Neither cell was wrong; the split's blast radius was never enumerated.",
        "Z-S132 IS A COMPLETED SWEEP WITH AN HONEST YIELD, and it graduates for the finding AND for the negative result. 62 of 62 criteria across 11 of 11 non-complete faces, population parsed from each order's own <status> and <criterion id> at a named HEAD rather than from file location -- 26 face files, 15 complete, 11 non-complete. THE ONE NEW FINDING: S23-AC3 iterates over OP-s-20's ALLOW list, which does not exist and cannot be built, so its 'zero firms would trip the threshold' is produced BY AN EMPTY LOOP and is indistinguishable from a real zero -- and the criterion's own clause 'Zero is a fine answer' PRE-BLESSES that misreading, on a card that faces the sovereign. ⛔ NO FINDING WAS MANUFACTURED TO JUSTIFY THE SWEEP, which the commission warned against in terms; the row says so and the yield is one item.",
        "Z-S121 IS RULE 22's SHARED-DEPENDENCY CLAUSE ONE LEVEL FURTHER OUT THAN EITHER SEAT APPLIED IT: a two-lane sequencing agreement that both seats wrote, and both believed closed the shared-root hazard, DECONFLICTS THE COMMAND AND NOT THE SCOPE. Terraform applies the ROOT, so the moment a lane COMMITS a .tf into a root another lane is about to apply, its resources are applied by the other lane's command. THE MEASUREMENT THAT SETTLES IT IS A TIMESTAMP AND NOT THE STATE FILE: opal-ipset-reconciler, opal-ipblock-cli and opal-sentinel each carry CreateDate 2026-09-04T01:51:56Z -- three roles across TWO task orders, created in ONE SECOND by ONE apply, while the lane owning one of them had not run anything.",
        "Z-S156 IS THE SAME BOUNDARY FAILURE IN TERRAFORM'S OWN GRAMMAR, and it is structural rather than a scoping mistake: -target on the edge function alone plans 1 change with ZERO wafv2 resources, but publishing a version REQUIRES repointing the distribution, and the distribution DEPENDS ON the WAF web ACL -- so any Lambda@Edge code deploy necessarily pulls three OP-s-15 / C-2 resources into the apply. Measured NON-DESTRUCTIVE today, before applying, and ARMED for the right reason: the hazard is not today's diff but the NEXT one, because the next edge deploy carries whatever state those actively-worked resources are in at that moment.",
        "Z-S103 AND Z-S104 ARE THE FACE-PREMISE PAIR, both produced by the re-grounding their own faces mandated. Z-S103 RELEASES WORK rather than blocking it -- the face's headline that its limb 'is the only thing standing between the project and FWD-9 and FWD-11' is FALSE against the decomposition's own edge, which reads '[DP + PITR read ON per table]', a predicate measured TRUE on 5 of 5 tables live. Left alone, two ready outcomes stay parked behind a face they do not depend on, which is why an OBSERVATION is correctly ARMED. Z-S104 carries three premise defects at once, including a carrier the face names that does not hold the table (opal-users-v2 lives in shared-infra/dynamo.tf, its portal-auth block having been deleted in the 2026-06-26 twin-dedup) and a table set of FIVE where the face quotes three."
      ]
    },
    "spec_asserts": "The faces, the decomposition's s.9 hold list, PRD 7.3's pipeline diagram and TO-OP-S-12's closed deploy ledger each assert a world their readers are directed to act in.",
    "world_is": "Six of those artifacts now describe a world that has moved -- a removed control, an unbuildable edge, a renamed bucket, a carrier that does not hold the table, a blocker that does not gate, a list that cannot be built -- and two scope boundaries turn out not to hold at the level the mechanism operates.",
    "notes": "WHAT THE EIGHT SHARE: AN ARTIFACT THAT OUTLIVED ITS OWN TRUTH AND KEPT DIRECTING. A closed ledger, a frozen decomposition, a PRD diagram, a task-order headline, a two-lane agreement. NONE of them is wrong in the sense of having been written carelessly -- every one was correct at its vintage -- and every one is now an INSTRUCTION pointed at a world that moved. ⛔ THE DANGEROUS PROPERTY THEY SHARE IS THAT NONE CARRIES A FORWARD REFERENCE: a closed ledger does not learn it was superseded, a frozen decomposition cannot record that a ruling made its hold list unbuildable, and a PRD section does not know its sibling section renamed the bucket. || THE COST IS ASYMMETRIC AND WORTH STATING: Z-S103's stale headline cost PARKED WORK, which is visible and recoverable. Z-S153's stale ledger cost a SILENTLY REMOVED CONTROL that every health signal reported green through, which is neither. || TWO OF THE EIGHT WERE FOUND BY A MANDATED RE-GROUNDING AND ONE BY A COMMISSIONED SWEEP -- i.e. by process rather than by luck -- and the sweep's honest yield of ONE finding across 62 criteria is itself the useful result, because the classes its commission feared were largely absent."
  }
]
```

## C-S30 -- CORRECTS C-S28 AGAINST THIS SEAT: the OPSEC defect class is THREE, not 24. The '18 peer-set' were this seat's OWN round-1 adjudications, and both seats' classifiers keyed on the DOCUMENT instead of the AUTHOR -- the same error, independently, twice

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S30",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:20Z",
    "one_line": "C-S28 published this project's incidence as '6 self-set + 18 peer-set = 24 of 127 terminal'. BOTH ARMS WERE WRONG AND BOTH IN THE INFLATING DIRECTION. The 18 are CVO-AUTHORED rows that live in the INVESTIGATION file, which is exactly where spine s.4 puts round 1's CVO rows before an adjudications folder exists -- real adjudications counted as peer stamps. And 2 of the 6 self-set (Z-S19, Z-S20) are this seat's own L9 rows. THE GENUINE CLASS IS THREE: Z-S117, Z-S126, Z-S149, all 2.0.0_SA_COO~Z. 1.0.0_SA_CTO~Z retracted its own larger error at msg 20861 and this row retracts the smaller one inside it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE -- adjudicates no item, moves no hazard. It corrects a figure this seat published one row earlier in this same document.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-MEASURED KEYED ON THE AUTHOR OF THE SETTING ROW rather than the document it sits in. SOURCE = the index, denominator 168 at ~09:2xZ: 111 CVO-authored setting row in adjudications/, 18 CVO-authored setting row IN THE INVESTIGATION FILE, 34 UNDISPOSITIONED backlog, 5 TERMINAL self-set. Of those 5, TWO carry surfaced_by '3.0.0_SA_CVO~Z (L9 adjudication...)' -- Z-S19 and Z-S20, this seat's own. THE RESIDUAL NON-CVO CLASS IS THREE: Z-S117, Z-S126 and Z-S149, every one 2.0.0_SA_COO~Z.",
        "⛔ THE CAUSE IS THE SAME IN BOTH SEATS AND IT IS WORTH MORE THAN THE NUMBER: a classifier keyed on WHICH DOCUMENT the setting row sits in, where the sound key is WHO AUTHORED IT. Spine s.4 places round 1's CVO rows in the investigation file until the adjudications folder lands, so a document-keyed classifier reads a CVO's own adjudications as foreign stamps and then reports them as evidence of a governance gap. 1.0.0_SA_CTO~Z made this error at msg 20858 and retracted it at 20861; this seat made the identical error at C-S28 and is retracting it here. TWO SEATS, INDEPENDENTLY, THE SAME WRONG KEY -- which is the tell that the key was the trap and not either seat.",
        "⭐ THE NFRA_REPORT FINDING SURVIVES THE STRICTER METHOD AND GETS STRONGER, which is the limb this seat checked hardest because a defect in the classifier would have undermined a slug already cut. Re-run author-keyed on that project with C-S6..C-S11 EXCLUDED: 3 CVO-authored / 9 NON-CVO setting rows / 8 TERMINAL self-set / 4 undispositioned -- so SEVENTEEN of 24 items carried a disposition no CVO row set, where C-S10 reported sixteen. Every one of the seventeen is authored by 1.0.0_SA_CTO~Z or 2.0.0_SA_COO~ZZ, i.e. genuinely non-CVO, so nothing there was miscounted the way this project's 18 were. AT HEAD the same call returns 24 of 24 CVO-authored, 0 non-CVO, 0 self-set.",
        "WHY THE TWO PROJECTS DIFFER, stated so the corrected figure is not read as retracting C-S10's mechanism: on NFRA_REPORT the non-CVO setters are DISARM ROWS filed by the CTO and the COO -- foreign seats writing into the disposition field through `adjudicates`. On NFRA_OPSEC202609 the equivalent rows are the CVO's OWN, sitting in the investigation file for a reason the spine names. THE MECHANISM IS IDENTICAL IN BOTH -- any row's `adjudicates` writes its own disposition onto its targets, with no test of document or seat -- but the INCIDENCE is one project's and not the estate's, and C-S10's own bound said exactly that and is vindicated rather than breached."
      ]
    },
    "spec_asserts": "C-S28 of this document stated the incidence for this project as 6 self-set plus 18 peer-set of 127 terminal.",
    "world_is": "The 18 are this seat's own adjudications in their spine-sanctioned home and 2 of the 6 are likewise this seat's. The residual class is three rows, all by one lane.",
    "notes": "THIS IS THE THIRD DEFECT IN THIS SEAT'S OWN WORK THIS SESSION and the second in a published FIGURE: the wrong-key criteria census at C-S8, the missing open-count beside the split at C-S28, and now the wrong classification key inside C-S28 itself. ALL THREE ARE THE SAME FAMILY as the findings this round graduated -- an instrument answering confidently about the wrong object -- and the third one is that family applied to a claim ABOUT the family, which is as clean an instance of the pattern as this round has produced. || ⛔ WHAT DOES NOT CHANGE: C-S10's mechanism, verified at source by two seats independently; NFRA_REPORT's 17-of-24 incidence, which the stricter method raises rather than lowers; and the slug @4fe64b8cac, whose s.4 named NFRA_REPORT's numbers (correct) and offered this project's only as INCIDENCE ELSEWHERE under an explicit bound. That bound is why the error is confined to a sentence rather than to a verdict. || COST OF THE CHECK THAT CAUGHT IT: one classification pass re-keyed from document to author, on rows already parsed. The cheap version of this check should run BEFORE any authorship figure is published, not after a peer disputes it."
  }
]
```

## C-S31 -- nine rows graduate on THE CRITERION THAT CANNOT BE SATISFIED AS WRITTEN: an outcome graded COMPLETE whose alarms reach nobody, a face that contradicts itself, a status string absent from its own schema enum, and a plan-wide bind an immutable resource can never honour

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S31",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:35Z",
    "one_line": "L9, round 2: NINE rows GRADUATE -- Z-S151, Z-S158, Z-S97, Z-S90, Z-S101, Z-S85, Z-S33, Z-S29, Z-S27. Seven are a REQUIREMENT THAT CANNOT BE MET AS WRITTEN and two are the measurements that bound them. The headline is Z-S151: FWD-4 is graded COMPLETE and cannot be satisfied, because both login-abuse alarms publish to a topic with ZERO subscribers -- and EVERY CHECK ON THE ALARM'S OWN SIDE PASSES, which is precisely why nothing surfaced it. The defect sits one hop past where anyone was looking.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. All nine keep 2.0.0_SA_COO~Z, named on every one as the issuer who owns the criterion wording and the routing. Z-S101's disarm additionally routes to Andrew (the registrar account is outside this fabric entirely) and Z-S97's open leg is a NAME nobody in the project holds.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S151",
      "NFRA_OPSEC202609-Z-S158",
      "NFRA_OPSEC202609-Z-S97",
      "NFRA_OPSEC202609-Z-S90",
      "NFRA_OPSEC202609-Z-S101",
      "NFRA_OPSEC202609-Z-S85",
      "NFRA_OPSEC202609-Z-S33",
      "NFRA_OPSEC202609-Z-S29",
      "NFRA_OPSEC202609-Z-S27"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-S151 IS THE HEADLINE AND IT IS THE SCOPED-CHECK CLAUSE ON AN OUTCOME RATHER THAN A RESOURCE. *** TO-OP-S-6.login-abuse-alarm reads `complete` and THE ALARM SIDE IS ENTIRELY CORRECT -- the alarms exist among 51 in the account, ActionsEnabled is true, and the action ARN resolves to a real topic. The defect is ONE HOP FURTHER: the topic has ZERO subscribers, so a burst of blocked sign-ins reaches nobody. Every question askable of the alarm returns a clean answer and FWD-4's DONE WHEN -- that a human receives it -- is still false. ⛔ THE ROW REFUSES TO RE-GRADE THE CELL and says so: the grade is this seat's at L9 and the row's author owns L4. That boundary is why the finding is usable.",
        "Z-S158 SPLITS Z-S151'S QUESTION RATHER THAN ANSWERING IT, and the widening is the value: the AWS account is in the SNS SMS SANDBOX, so every SMS-protocol subscriber ACROSS ALL FOUR 'confirmed' topics resolves to an UNVERIFIED destination regardless of how the console renders it -- including opal-infrastructure-alerts, the infrastructure monitor's own escalation channel. So 'zero subscribers' and 'subscribers that cannot receive' are two different failures reaching the same place, and only one of them is visible as an absence. ⭐ IT ALSO NAMES WHY IT IS A ROW RATHER THAN AN EDIT: the channel is append-only and `adjudicates` is the CVO's field, so a worker widening an earlier finding files beside it. That is the protocol working as designed.",
        "Z-S27 AND Z-S29 ARE FACES THAT REFUSE THEMSELVES. Z-S27: S26-AC2 requires 'a census of the diff for arn:aws:iam::313476888478:user/ reads 0' while DELIVERABLE 2 AND C-14 OF THE SAME FACE REQUIRE exactly that ARN as the role's single trust principal by Andrew's word. Both cannot hold -- a role cannot trust a principal it does not name -- and the measured diff carries 3 occurrences, 2 in comments and 1 in the mandated trust policy. Z-S29: S27-AC2 prescribes filing the empty-delivery case as 'UNCOMPUTABLE-BY-TIME', which is NOT a member of PROOF_OF_SPEC.schema.json's status enum, and proof-of-spec-check REFUSES the instance carrying it -- so the branch the face designed for its own EXPECTED case cannot be filed at all.",
        "⭐ AND BOTH REFUSED TO SELF-RULE, WHICH IS THE BEHAVIOUR WORTH REWARDING RATHER THAN THE FINDING. Z-S27's author writes that grading it PASS against 'the reading this seat finds more sensible -- without saying so -- would be the assignee choosing its own criterion'. That is exactly right, and it is the difference between a worker that surfaces a spec defect and one that quietly absorbs it. The intent of both criteria is obvious and correct; the WORDING is what fails, and only the issuer may re-word it.",
        "Z-S85 IS A BIND AN IMMUTABLE RESOURCE CAN NEVER HONOUR: aws_api_gateway_deployment is immutable and its trigger is the BODY HASH, so every body change REPLACES it -- an add plus a destroy. The plan-wide '0 destroy, 0 forces-replacement' bind therefore cannot survive ANY body change on a body-managed REST API. Measured before any apply: '4 to add, 3 to change, 1 to destroy', forces-replacement 1, and the single replacement IS that deployment. The SCOPED bar passes exactly -- 0 imported objects created, replaced or destroyed -- so the two bars disagree by construction rather than by accident. A RECOMMENDATION IS OFFERED AND NOT TAKEN, which is the correct lane discipline.",
        "Z-S90 AND Z-S101 ARE GO CONDITIONS THAT FAIL ON MEASUREMENT, and Z-S90 carries the better instrument lesson of the two. Its window is FINE -- 19.7 days, 111,904 WAF records -- and the SIGN-IN TRAFFIC IN IT IS TWO EVENTS: exact-path /auth/login = 2, forgot-password = 0, reset-password = 0. ⛔ THE DANGEROUS PART IS THE COUNTERFACTUAL THE ROW MEASURED: a SUBSTRING match on 'auth' returns 2,990 records across 60 distinct clients, dominated by internet scanner probes. A naive census would have reported a healthy population and built an allow list out of attack traffic. Z-S101: opalinvest.com is not in Route53 and not in the account at all -- delegated to GoDaddy, no ACM certificate, and an apex A record CloudFront structurally cannot target -- with the Route53 denominator printed (2 zones, IsTruncated ABSENT, so a true denominator and not a page).",
        "Z-S97 IS AN ABSENCE FILED BEFORE THE BUILD RATHER THAN DISCOVERED AFTER IT, and the face itself declares the gap: 'This face does NOT name that person, because the issuer does not have the name. DO NOT PICK ONE, DO NOT USE A ROLE AD[DRESS]'. Everything else in TO-OP-S-6 is buildable and was built; the SNS subscription is a single named open leg. Filing it before the build is what makes the missing subscription legible as a decision rather than as an oversight -- and it composes exactly with Z-S151, which measures what that absence costs.",
        "Z-S33 IS A PARTIAL ENUMERATION CARRIED FORWARD AS A COMPLETE ONE, found AT A CUT rather than by a worker. get-stages on opal-portal-api returns TWO live stages -- `prod` (deploymentId 5vm7lc) and `production` (c2zxm8) -- where brief F1, PRD s.8 row S1 and the decomposition all name ONE. The edge fronts `prod` only. ⭐ THE ROW'S OWN CHARACTERISATION IS THE PRECISE ONE: 'the spec's stage name is not wrong, it is INCOMPLETE'. A wrong name fails loudly at the first call; an incomplete enumeration passes every check aimed at the member it does name."
      ]
    },
    "spec_asserts": "FWD-4's DONE WHEN is that a human receives the login-abuse alarm; S26-AC2, S27-AC2, the plan-wide 0-destroy bind, TO-OP-S-20's GO condition and TO-OP-S-13's deliverables 4 and 5 each state a requirement their face treats as satisfiable.",
    "world_is": "Seven of those requirements cannot be met as written -- the alarms reach a topic nobody is subscribed to and whose SMS plane is sandboxed account-wide, the face's criterion forbids the ARN its own deliverable mandates, the prescribed status string is not in the schema, the immutable deployment must be replaced on every body change, the sign-in population is two events, the DNS control point is outside the account, and the recipient's name is held by nobody.",
    "notes": "WHAT THE NINE SHARE: A REQUIREMENT WHOSE INTENT IS RIGHT AND WHOSE WORDING OR PREMISE THE WORLD CANNOT SATISFY. In every case the intent survives -- alert a human, grant no user principal, file the empty case, change nothing destructive, restrict /wp-admin, front the site -- and in every case the text or the input fails. THE REPAIR IS ALMOST ALWAYS ONE SENTENCE AT THE ISSUER AND NEVER A BUILD, which is why all nine correctly route to 2.0.0_SA_COO~Z rather than being worked around by their assignees. || ⭐ THE PATTERN THIS ROUND SHOULD KEEP IS THE REFUSAL TO SELF-RULE. Z-S27, Z-S29, Z-S85 and Z-S90 each had an obvious sensible reading available and each declined to grade against it silently; Z-S85 went further and offered a recommendation it explicitly did not take. A worker that absorbs a spec defect leaves no trace and the next round inherits it; a worker that files one costs the issuer a sentence. || Z-S151 AND Z-S97 ARE ONE OUTCOME SEEN FROM BOTH ENDS -- the absent name and what the absence costs -- filed by different lanes at different times, and neither is complete without the other."
  }
]
```

## C-S32 -- the closing pass: TWENTY-TWO graduate, including THREE CLASS ROWS (a control that is perfectly configured and does nothing; a control scoped to items while its mechanism works on containers; a partial disarm that reads as a full one) and a seat reporting that it graduated a row it had no authority to graduate

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S32",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:50Z",
    "one_line": "L9, round 2, THE CLOSING PASS: TWENTY-TWO rows GRADUATE. Among them THREE CLASS ROWS that are worth more than any single finding -- a control DEPLOYED, WELL-FORMED, HEALTHY ON EVERY CONFIGURATION PROBE AND WITH NO EFFECT (five instances, three faces); a control SCOPED TO ITEMS while the mechanism it depends on operates on a CONTAINER (four instances, four unrelated subsystems, one night); and a PARTIAL DISARM being indistinguishable from a full one, with the error running in the direction that HIDES LIVE HAZARDS. Plus Z-S168, in which 2.0.0_SA_COO~Z reports that it conferred a graduation it had no authority to confer -- reaching C-S10's finding independently, from the other end.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. The ARMED members keep their own owners -- Z-S63 with the owner of .tools/halt-gate, Z-S84 with this seat (disarm at the L9 census it names), Z-S163 with 1.0.0_SA_CTO~Z as the schema owner. This row sets the remediation-track disposition and moves no hazard state.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S23",
      "NFRA_OPSEC202609-Z-S63",
      "NFRA_OPSEC202609-Z-S67",
      "NFRA_OPSEC202609-Z-S81",
      "NFRA_OPSEC202609-Z-S84",
      "NFRA_OPSEC202609-Z-S98",
      "NFRA_OPSEC202609-Z-S99",
      "NFRA_OPSEC202609-Z-S106",
      "NFRA_OPSEC202609-Z-S115",
      "NFRA_OPSEC202609-Z-S122",
      "NFRA_OPSEC202609-Z-S129",
      "NFRA_OPSEC202609-Z-S133",
      "NFRA_OPSEC202609-Z-S148",
      "NFRA_OPSEC202609-Z-S150",
      "NFRA_OPSEC202609-Z-S154",
      "NFRA_OPSEC202609-Z-S155",
      "NFRA_OPSEC202609-Z-S163",
      "NFRA_OPSEC202609-Z-S164",
      "NFRA_OPSEC202609-Z-S165",
      "NFRA_OPSEC202609-Z-S166",
      "NFRA_OPSEC202609-Z-S167",
      "NFRA_OPSEC202609-Z-S168"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE THREE CLASS ROWS FIRST, BECAUSE THEY ARE THE ROUND'S MOST TRANSFERABLE OUTPUT. *** Z-S106: ONE SHAPE, FIVE INSTANCES, THREE TASK ORDERS -- an authorizer whose key can never arrive (the only one that SHIPPED), an SNS topic with no subscriber, an alarm dimensioned so it matches no metric, a distribution no visitor traverses, an ACL whose rules cannot fire. Every one is DEPLOYED, WELL-FORMED and HEALTHY ON EVERY CONFIGURATION PROBE, and none of them does anything. ⛔ THE CONFIGURATION PLANE CANNOT SEE THIS CLASS AT ALL, which is why five instances arrived in one round and why a per-resource check will never find the sixth. Z-S122: a control SCOPED TO ITEMS while the mechanism it depends on operates on a CONTAINER -- consumers scoped to FUNCTIONS while the read capability sits on ROLES, a grant removal scoped to ONE TERRAFORM ROOT while IAM is account-wide, an uncommitted-content check scoped to modified files while git tracks a tree. Four unrelated subsystems, one night, one shape.",
        "Z-S84 IS THE PROTOCOL ROW OF THE THREE AND ITS ERROR DIRECTION IS THE WHOLE POINT: the protocol says a reader resolves a row's state from the NEWEST ROW CITING IT, and Z-S82 -- the newest row citing Z-S80 -- disarms the EXECUTION half ONLY, saying in its own text that the endpoint-shape half 'is expressly NOT disarmed here'. A reader following the protocol literally records Z-S80 as disarmed. ⛔ A PARTIAL DISARM IS INDISTINGUISHABLE FROM A FULL ONE AND THE ERROR HIDES LIVE HAZARDS -- an undercount of armed rows, produced by obeying the rule as written. Filed by this seat at L8 against its own L9 instrument, before that instrument was used.",
        "Z-S168 IS 2.0.0_SA_COO~Z REACHING C-S10'S FINDING INDEPENDENTLY AND REPORTING IT AGAINST ITSELF: 'THIS SEAT CONFERRED A GRADUATION IT HAS NO AUTHORITY TO CONFER, AND THE L10 PRECONDITION COUNTS IT AS SATISFIED.' Z-S115 carried disposition GRADUATED set by its own surfacing seat, with no CVO row resolving it, because _resolve_latest applies latest[id]=disposition with no test of the seat. ⭐ AND IT REPORTS THE MAGNITUDE IN THE DIRECTION THAT COSTS ITSELF THE CREDIT -- naming the true scale as much smaller than the figure that prompted it, rather than accepting the larger number that would have made its disclosure look weightier. Both Z-S115 and Z-S168 graduate here, and this row supplies the CVO disposition Z-S115 never had.",
        "THE GATE AND CRITERION ROWS -- each a mechanism no build can work around. Z-S23: the row gate refuses ANY new remediation row without route + loop_target, with no exemption for an out-of-project remedy, while the schema leaves both optional -- the SAME FAMILY as the slug/worker-row conflict this seat hit cutting NFRA_REPORT's remediation document, and the second instance of a slug being structurally un-cuttable. Z-S163: the disposition enum offers DECOMP_INVALIDATING as a CO-EQUAL PEER and it cannot be used as a per-item disposition at all -- it is a SLUG-LEVEL verdict wearing a per-item value's clothes, and only the gate knows. Z-S67: a criterion demanding byte-identical executable lines quietly assumes the files already pass the commit gate they will be committed through; where they do not, the criterion and Rule 14 are JOINTLY UNSATISFIABLE and the work stalls on lint debt belonging to nobody on the face. Z-S115: a GO condition that demanded a state THE GATED WORK ITSELF PRODUCES -- two faces naming each other as prerequisites, a pair that could never start.",
        "Z-S63 IS THE ONE WITH THE LONGEST-STANDING DEFECT AND IT IS A SAFETY GATE: safe-apply fires the HALTGT checkpoint immediately before terraform apply and refuses to apply ungated, and the checkpoint CANNOT SEE A LANE SEAT'S INBOX -- so a production apply ran past THREE UNREAD ISSUER PRECONDITIONS. ⛔ THE DEFECT HAS BEEN DOCUMENTED AND RULED IN THE GATE'S OWN SOURCE SINCE 2026-07-25 WITHOUT REMEDIATION. Filed by the ISSUER rather than by the seat that tripped it, and the seat that tripped it had disclosed the sequencing failure unprompted against its own already-confirmed completion report.",
        "THE INSTRUMENT ROWS, all four the round's signature shape. Z-S129: the ruling's condition was met but NOT BY THE TEST IT NAMED -- XML-RPC RETURNS HTTP 200 FOR A FAILED AUTHENTICATION, the fault travelling in the response BODY, which an access log does not record, so the named test could never have discriminated. Z-S155: Lambda REPORT Duration cannot tell WHICH secret a cache re-read hit, because the function holds TWO independent 300 s caches producing the same spike on the same period -- a CONFOUNDED pass the old code reproduces. Z-S98 and Z-S99 are one pair: a phase-1 re-grounding finds two traps, and then THE SAME SEAT INVERTS ITS OWN TRAP A -- a JSON metric-filter pattern DOES match a Text-format log line whose payload is preceded by a timestamp, and the negative control shows it also REJECTS every decoy, so the pattern is not merely viable but STRICTER than the alternative. Z-S81 records the honest opposite: NO instrument available to a site-Z seat can establish whether an AWS service principal sends aws:SourceArn, so the floor's fallback was taken rather than an assumption made.",
        "THE THREE SWEEPS AND WHAT THEY HONESTLY YIELDED, which this seat weighs as evidence of a working round rather than as filler. Z-S148: ALL 23 proof instances and ALL 129 acceptance limbs read -- ZERO actually-unsupported, three merely stale-but-sound, each already carrying a writer-scoped anchor, so NO VERDICT ANYWHERE IN THE PROJECT RESTS ON AN UNSUPPORTED LIMB. Z-S133: the split-drift class sized honestly -- exactly ONE stale line in the project tree, and in infra a MEASURED ZERO THAT FAILED ITS OWN POSITIVE CONTROL, reported as a failed sweep rather than as a clean one. ⭐ THAT LAST IS THE HARDER THING TO WRITE and it is the correct call: a zero whose control failed is not a zero. Z-S150: attempted-vs-proven is not a missing FIELD in deploy_ledger.py but a PREDICATE REPLICATED AT SEVEN SITES plus a renderer, which is why it reads as a small fix and is not one.",
        "THE MIGRATION TRIO, Z-S165 / Z-S166 / Z-S167, which compose into one finding no single row states. Z-S165: FWD-12's migration denominator counts CALLERS, but the callers do not have one code carrier each -- the 49F and cot auto-login boxes execute THE SAME FILE, so migrating one migrates both and the denominator overstates the work. Z-S166: that coupling is LATENT rather than firing, because the cot box has no run-time artifact pull, so the shared file does not reach cot on its own -- which is what makes it a hazard for the NEXT deploy rather than a live defect. Z-S167 is the sharpest: THE MIGRATION ORACLE RECORDS THE CREDENTIAL, NEVER THE CALLER, so any holder of a static bearer FORGES A PERFECT MIGRATION SIGNAL without touching the migrated path -- and its author demonstrated it by forging one from a workstation. An oracle that cannot distinguish the thing it measures from a forgery of that thing is not a weak oracle; it is not an oracle.",
        "Z-S164 AND Z-S154 CLOSE THE STALE-CARRIER LINE. Z-S164: this project's register describes a state SUPERSEDED A WEEK AGO -- `phase` froze on a VERDICT CORRECTION rather than on a round and mentions neither round 2, the two cancellations, L8, nor the L9 that produced this document; `blocking` is pre-round-2. Z-S154: two faces carry a PRD pin two versions stale, and the delta is INERT for those faces -- filed anyway, and the row's own reason is the keeper: AN UNFILED INERT DELTA READS IDENTICALLY TO AN UNPERFORMED RE-GROUND, so only a row distinguishes a check that was made and passed from one that never happened."
      ]
    },
    "spec_asserts": "Each row's own face, gate or ruling asserts a control that works, a criterion that can be met, a carrier that is current, or an oracle that discriminates.",
    "world_is": "Twenty-two of those assertions fail on measurement, and three of the failures are CLASSES with multiple instances each rather than single defects.",
    "notes": "THIS ROW CLOSES THE PER-ITEM PASS. With C-S33 below, NFRA_OPSEC202609 round 2 reaches UNDISPOSITIONED 0 from the 138 the L8 packet handed over. || WHAT THE ROUND ACTUALLY FOUND, stated once now that the whole set has been read: not a list of bugs but FOUR REPEATING SHAPES -- an instrument answering confidently about the wrong object; a control whose configuration is perfect and whose effect is nil; a constraint true of the intent and false of the mechanism; and an artifact that outlived its own truth and kept directing. Every one of them is INVISIBLE TO A PER-ITEM CHECK and every one was found by widening, by a positive control, or by a seat re-reading its own work. || ⭐ THE ROUND'S BEST PROPERTY IS NOT ANY FINDING: it is that at least NINE rows are seats reporting defects in their own work -- Z-S99, Z-S130, Z-S137, Z-S139, Z-S146, Z-S168, Z-S108, Z-S115 and this seat's own C-S30 -- and in every case the self-report made the record stronger rather than the seat weaker. A fabric where that is cheap finds things a fabric where it is expensive cannot."
  }
]
```

## C-S33 -- three records dismissed: an L8 confirmation whose targets graduated elsewhere, and two instances of a shared-channel fabric hazard whose remedy this project cannot route

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S33",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T09:50Z",
    "one_line": "L9, round 2: THREE records are DISMISSED WITH REASON -- Z-S32 (an L8 confirmation of two rows that graduated at C-S31), Z-S40 and Z-S116 (both instances of a FABRIC class homed on another channel: a seat committing a shared append-only file carrying peers' uncommitted rows, and a seat destroying two of them with `git checkout --`). None carries a mechanism of its own to graduate or a remedy this project can route. Their content is carried rather than discarded, and the two fabric rows keep their real value as the EXERCISED EVIDENCE of a class whose home is elsewhere.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ROUND 1's Z-S20 TEST, APPLIED UNCHANGED: does the row carry a mechanism of its own to graduate, or a remedy of its own to route? Z-S32 is this seat's own L8 confirmation of Z-S27 and Z-S29 on instruments other than their authors' -- real corroboration, but ABOUT two rows that graduated at C-S31, and its one substantive addition (that S26-AC2's plane is THE DIFF and not the module) is a fact the issuer needs when RE-WORDING that criterion, so it rides Z-S27's remediation row rather than needing its own. Z-S40 and Z-S116 both describe the same fabric hazard -- three seats swept 6 of a peer's uncommitted rows into their own commits across 3 commits, each disclosed by its own author; and one seat ran `git checkout --` on the shared channel file and destroyed TWO uncommitted rows including a DIFFERENT seat's, neither recoverable. ⛔ THE REMEDY FOR BOTH IS A ROW-ID-SET DELTA REFUSAL IN A SHARED GATE, WHICH IS NOT THIS PROJECT'S SURFACE, and Z-S40 says so itself: 'the class itself is a FABRIC item homed on 0.0.0_AB_MSTR~Z's channel'. A remediation row here would assert a route this project cannot open -- the same reasoning C-S9 adopted from 1.0.0_SA_CTO~Z on NFRA_REPORT-Z-W1-S5. THE DISMISSAL IS A ROUTING ACT AND NOT A JUDGMENT AGAINST ANY OF THE THREE: all three are correct, all three were filed by their own authors against themselves, and Z-S116's incident is UNRECOVERABLE and stays on the record permanently by being in this channel at all.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S32",
      "NFRA_OPSEC202609-Z-S40",
      "NFRA_OPSEC202609-Z-S116"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S32's SUBSTANTIVE ADDITION, CARRIED HERE SO THE DISMISSAL LOSES NOTHING: S26-AC2's census plane is THE DIFF and not the module, and the face's own commit added exactly the trust statement the criterion's census forbids. That is the fact the issuer needs to re-word the criterion, and it belongs beside Z-S27 in the slug rather than as a separate remediation item.",
        "Z-S40 AND Z-S116 ARE THE SAME HAZARD FROM TWO SIDES -- one seat's commit CARRYING a peer's uncommitted rows, another seat's checkout DESTROYING them. Both are properties of a shared, append-only, multi-writer file with no per-row ownership at the git layer, and both are already banked estate-wide. Rule 14b's own text records the second: a side branch on an append-only shared file converts a seconds-long staging race into a guaranteed conflict, and the conflict path is the one that cost this estate a hand-finished merge.",
        "⭐ WHY THE DISMISSALS DO NOT WEAKEN THE RECORD: all three rows STAY IN THE CHANNEL. A dismissal changes what the slug carries forward to the COO's recut; it does not delete evidence, and Z-S116's whole purpose -- that a destroyed row leaves no trace unless someone writes one -- is served by the row existing, not by it graduating."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Three of the round's items are records: one confirming two rows that graduated elsewhere, and two documenting a shared-channel hazard whose remedy is a fabric gate this project does not own.",
    "notes": "WITH C-S32 ABOVE, THIS COMPLETES THE PER-ITEM PASS: 168 items, UNDISPOSITIONED 0, from the 138 open at the L8 handover. SOURCE for every count in these two rows: the INDEX, via _latest_dispositions imported and called, per msg 20853 s.2's reporting discipline. || THE SLUG IS THIS SEAT'S NEXT AND LAST ACT ON THIS ROUND, and it is not blocked. ⚠ IT WILL REQUIRE THE SAME AUDITED OVERRIDE NFRA_REPORT's DID -- Z-S23 predicts it in this project's own channel, and the graduated set here carries worker-surfaced W-coordinate rows that _coordinate_violations refuses from a non-worker committer."
  }
]
```

## C-S34 -- the round's TWO JUDGMENT criteria graded: S10D-AC2 PASSES on the deployed bytes, and S10E-AC6 is ANSWERED AGAINST BOTH OPTIONS IT OFFERED -- the seal key must be bounded IN CODE, a runbook cannot bound a compiled cache, and the durable fix is to stop deriving it from the signing key

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S34",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T10:00Z",
    "one_line": "L9, round 2: the TWO judgment criteria the L8 packet reserved to this seat are graded. S10D-AC2 PASSES -- the shared two-slot module was genuinely REUSED, confirmed on deployed bytes this seat downloaded at a digest the assignee never cited. S10E-AC6 is ANSWERED, and the answer rejects the framing of both options it offered: the MFA seal key must be BOUNDED IN CODE (a runbook step cannot add a TTL to a compiled cache), bumping the v1 label is strictly worse because it needs the deploy the rotation forbids, and the durable remedy is to STOP DERIVING A SYMMETRIC SEAL KEY FROM THE SIGNING KEY AT ALL.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A GRADE RECORD, per the grades field's own contract: 'a row carrying grades that adjudicates no item and opens nothing carries disposition DISMISSED_WITH_REASON with its reason naming it a grade record -- the enum has no record value and this version proposes none.' This row adjudicates no investigation item; its whole content is the two verdicts in `grades`, which is the field a consumer can reject on. The dismissal disposes of THIS ROW and disposes of nothing else -- both grades stand as the round's L9 verdicts on their criteria.",
    "disarm_owner": "NONE -- this row grades criteria and adjudicates no item. The seal-key remedy is 2.0.0_SA_COO~Z's to place at the recut; nothing here is armed and nothing is rotated.",
    "grades": [
      {
        "criterion": "S10D-AC2",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10D.session-analytics-two-slot.proof_of_spec.json@649a6a8fd1ee",
        "verdict": "PASS",
        "reason": "THE MODULE WAS GENUINELY REUSED AND THE DISCRIMINATING EVIDENCE IS ON THE DEPLOYED ARTIFACT, NOT THE SOURCE. The assignee's own case is sound on three limbs -- one import site of getJwtKeySlots/verifyWithSlots with no new cache variable, no new TTL constant and no new Secrets Manager client; a residual-symbol census that DISTINGUISHES a docstring occurrence of `cachedPublicKey` from a call site rather than counting it, which is the difference between a control and a number; and the shared module's distinctive literals each appearing EXACTLY ONCE in the shipped bytes. ⭐ THIS SEAT CONFIRMED THE LOAD-BEARING LIMB INDEPENDENTLY AND ON A DIFFERENT ARTIFACT VINTAGE: opal-session-analytics was re-downloaded here at CodeSha256 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko= (LastModified 2026-09-09T21:26:02Z), and the bundle carries the secret id 'opal/auth/jwt-public-key' exactly ONCE and the TTL literal 300000 exactly ONCE. ONE cache, not two. The call sites were then opened rather than counted: r2() parses the envelope to {current, previous}, R4() is the slots getter guarded by `if(y6&&q-x4<n2)return y6` at 300 s, B4() is the current-then-previous accept, and t2() -- the check that answers a REQUEST -- calls both. THE BAR'S OWN FAILURE MODE IS WHY THIS MATTERS: a third hand-rolled cache would reproduce Z-S155 exactly, two independent 300 s caches in one process being indistinguishable to any per-process timing probe. The single TTL literal is what rules that out, and it is a property only the compiled artifact can carry."
      },
      {
        "criterion": "S10E-AC6",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10E.signer-key-read-ttl.proof_of_spec.json@d09246e8fd7a",
        "verdict": "PASS",
        "reason": "PASS GRADES THE FACE'S CONDUCT, NOT THE CURRENT STATE, AND THE ENUM FORCED THAT DISTINCTION: the verdict enum is PASS / FAIL / NOT_EVALUATED and this criterion is a FORK -- it asks the CVO to CHOOSE between two remedies, not to score built work against a bar. There is no enum value for 'a fork that has been ruled'. PASS records that the face did what was asked of it: it left a security primitive outside its scope UNCHANGED rather than silently altering it, and it DISCLOSED the hazard its own change created. IT IS NOT AN ENDORSEMENT OF THE UNBOUNDED SEAL KEY, which this seat rules must be fixed -- the ruling follows. || THE CRITERION ASKS whether the rotation RUNBOOK should bound the HKDF-derived MFA seal key, or should instead bump the v1 label at rotation time. MEASURED FIRST, on the deployed signer at CodeSha256 sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=: y8() reads `if(P6)return P6; let q=await k8(); return P6=Buffer.from(j3(\"sha256\",q,Buffer.alloc(0),\"opal-mfa-code-seal-v1\",32)),P6` -- a bare scalar with NO time component, HKDF-derived from a private key that now refreshes every 300 s. So a long-lived container derives P6 ONCE and holds it for its whole life while the key beneath it moves. ⛔ AND THE BLAST RADIUS IS WIDER THAN 'IN FLIGHT', WHICH IS THE FACT THAT DECIDES THIS: the sealed value is PERSISTED -- B1() seals and the result is written as `\":sealed\": await B1(D)` beside an `expiresAt` -- and r3() unseals it later FROM ANY CONTAINER. So every code sealed before a rotation and verified after, by a container that has refreshed, fails. r3() returns NULL on failure inside a bare catch, so the failure is SILENT and surfaces to the user as 'Invalid or expired code'. THE ANSWER: (1) BUMPING THE v1 LABEL IS STRICTLY WORSE. It changes the derived key for every container at DEPLOY time, which breaks every in-flight sealed code SIMULTANEOUSLY, and it requires a deploy -- exactly what condition 3 of the rotation GO forbids during the convergence window and what Z-S159 names as an accident rather than a rotation property. (2) BOUNDING IT IS RIGHT OF THE TWO, because it makes the divergence window CLOSE DETERMINISTICALLY at ~300 s instead of at container lifetime, which this estate has measured out past 143 minutes. (3) ⛔ BUT IT IS NOT A RUNBOOK ACT AND THE CRITERION'S WORDING IS WRONG ON THAT POINT: a runbook step cannot add a TTL to a compiled cache. Bounding y8() is a CODE change on the signer, in the same file TO-OP-S-10E already edited. (4) THE DURABLE REMEDY, named because both offered options are workarounds for it: A SYMMETRIC SEAL KEY SHOULD NOT BE DERIVED FROM THE JWT SIGNING KEY AT ALL. Chaining it there gives it the lifecycle of a key that rotates for entirely unrelated reasons, and every rotation will re-open this. That is a design call with an owner and a cost, and it is NAMED HERE AND NOT TAKEN. ⚠ WHAT THIS GRADE DOES NOT ESTABLISH: the MFA code TTL and the seal/unseal call volume were NOT measured, so the DURATION and the USER COUNT of a rotation-window failure are unquantified here -- the SHAPE is established, the magnitude is not."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CENSUS THAT FOUND THEM, WITH ITS DENOMINATOR: all 29 proof instances under this project parsed on the `acceptance` key -- 162 criteria, of which 143 PASS, 10 UNCOMPUTABLE-BY-CONSTRUCTION, 3 UNCOMPUTABLE, 1 N/A-BY-CONSTRUCTION and 5 UNVERIFIABLE-BY-INSTRUMENT. EXACTLY TWO of the five are judgment criteria, matching the L8 packet's arithmetic precisely: the packet named three of the five as instrument-unavailability records and not judgment criteria, and that holds.",
        "⚠ AN INSTRUMENT NOTE THAT WOULD HAVE COST BOTH GRADES: the `judgment` FIELD READS None ON BOTH ROWS -- the flag lives only in the criterion_verbatim text ('JUDGMENT criterion (judgment=\"true\", no invocation minted at cut)'). A census keyed on `judgment is True` returns ZERO here, and that is exactly the key this seat used on NFRA_REPORT at C-S8, where the field WAS set. THE SAME QUESTION, TWO PROJECTS, TWO DIFFERENT CARRIERS -- so a single-key census is unsound across the estate and both keys must be tried. Caught here only because the packet independently named the count as two.",
        "BOTH GRADES REST ON ARTIFACTS THIS SEAT OPENED RATHER THAN ON THE ASSIGNEES' ACCOUNTS OF THEM. Both Lambda bundles were downloaded and decoded at this seat, at digests neither lane cited, and the call sites were read rather than the symbol names counted -- which is the trap Z-S157 and C-S24 both record and which would have inverted S10D-AC2 in the permissive direction had it been counted from source names."
      ]
    },
    "spec_asserts": "L10 requires every judgment criterion of every proof-of-spec instance under the project to be graded in the CVO's adjudication, never self-graded by its executor.",
    "world_is": "The project carries exactly two, both correctly left ungraded by their assignees, and both are graded here.",
    "notes": "WITH C-S32 AND C-S33, BOTH L10 PRECONDITIONS ARE NOW MET FOR THIS ROUND: 168 items with UNDISPOSITIONED 0 (source: the index), and 2 of 2 judgment criteria graded. The slug is cuttable and is this seat's last act on the round. || ⭐ NEITHER ASSIGNEE SELF-GRADED AND BOTH SAID SO IN TERMS -- TO-OP-S-10D's instance opens its evidence with 'EVIDENCE ONLY -- THIS LANE RECORDS NO VERDICT', and TO-OP-S-10E disclosed that its own change CREATED the input S10E-AC6 turns on (the private key now bounded while the derived seal key is not). A lane that reports the hazard its own work introduced, on the criterion that will be used to judge it, is the behaviour that makes a judgment criterion worth having. || THE S10E-AC6 ANSWER IS A DESIGN CALL AND IS PLACED, NOT EXECUTED: 2.0.0_SA_COO~Z owns where it lands in the recut, and this seat neither cut an order nor touched the signer."
  }
]
```

## C-S35 -- closing the defect THIS DOCUMENT DIAGNOSED: the three self-set rows C-S30 named get a CVO disposition at last, and round 1's slug is measured to have carried FIVE of its TEN graduations -- the other five have never reached any remediation document

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S35",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T10:10Z",
    "one_line": "L9, round 2, the last per-item act: FIVE rows are DISMISSED WITH REASON -- Z-S117, Z-S126 and Z-S149 (the three terminal SELF-SET dispositions C-S30 identified as this project's genuine defect class, all disarm records by 2.0.0_SA_COO~Z), plus Z-S19 and Z-S20 (this seat's OWN round-1 L9 adjudication rows, self-set the same way). ⛔ AND A SEPARATE FINDING FOUND WHILE CUTTING THE SLUG: round 1 GRADUATED TEN items and its remediation document carries FIVE. Z-S1, Z-S2, Z-S11, Z-S13 and Z-S17 have never appeared in any slug, so five graduated findings have never reached the COO's recut by the only carrier that delivers them.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ALL FIVE ARE RECORDS on round 1's own Z-S20 test. Z-S117, Z-S126 and Z-S149 open with the words 'DISARM RECORD for NFRA_OPSEC202609-<id>' and exist to record that a hazard was stood down -- exactly the class C-S11 dismissed on NFRA_REPORT and C-S33 dismissed here. Z-S19 and Z-S20 are this seat's own round-1 L9 adjudication rows, which are verdicts ABOUT items and are not items; the spine says so directly ('an ADJUDICATION document's rows are the CVO's rows ABOUT items ... their own ids are NOT items'), and they carry ids in the investigation file only because round 1 predates this project's adjudications/ folder. ⭐ THE POINT OF DISMISSING THEM IS NOT THE VALUE, IT IS THE AUTHORITY: every one carried a TERMINAL disposition set by its own surfacing seat, which is precisely the defect C-S10 named and C-S30 counted. A document that diagnoses that defect and then leaves five live instances of it in its own channel has described a problem rather than closed one. Nothing here re-arms a hazard or disputes a disarm: all three disarms were correct and their targets stay disposed as their own rows left them.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S117",
      "NFRA_OPSEC202609-Z-S126",
      "NFRA_OPSEC202609-Z-S149",
      "NFRA_OPSEC202609-Z-S19",
      "NFRA_OPSEC202609-Z-S20"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE THREE SELF-SET ROWS ARE THE EXACT THREE C-S30 NAMED, re-measured here keyed on the AUTHOR of the setting row: of 168 items, 111 carry a CVO-authored setting row in adjudications/, 18 a CVO-authored setting row in the investigation file (spine s.4's home for round 1's CVO rows), and 5 were TERMINAL SELF-SET -- Z-S19 and Z-S20 by this seat, and Z-S117, Z-S126 and Z-S149 by 2.0.0_SA_COO~Z. That is the whole residual class and it is closed by this row.",
        "⛔ THE SLUG-COMPLETENESS FINDING, MEASURED WHILE BUILDING THE ROUND-2 REMEDIATION DOCUMENT AND NOT BEFORE: round 1's adjudication row Z-S19 GRADUATES TEN items by name -- S1, S2, S3, S4, S5, S10, S11, S13, S14, S17. REMEDIATION_v1.Z.md carries FIVE: Z-S3, Z-S4, Z-S5, Z-S10, Z-S14. So Z-S1, Z-S2, Z-S11, Z-S13 and Z-S17 GRADUATED AND WERE NEVER CARRIED. Protocol s.5 makes the remediation document the only artifact that reaches 2.0.0_SA_COO's recut, so a graduation absent from it is a finding that was adjudicated, recorded, and then delivered to nobody.",
        "WHY NEITHER GATE COULD SEE IT, which is what makes it worth a row rather than a fix in passing: the L10 precondition tests that every INVESTIGATION item carries a disposition, and all ten did. NOTHING ANYWHERE TESTS THAT EVERY GRADUATED ITEM HAS A REMEDIATION ROW. The two documents are validated independently and no predicate joins them, so a slug can omit half its graduations and every check in the fabric still reads green. It is the same shape as C-S10's finding one artifact further down the chain: a precondition that measures the presence of a value rather than the completeness of a delivery.",
        "THE FIVE ARE CARRIED INTO THE ROUND-2 SLUG rather than left for a round-3 that may never re-read round 1. They are real: Z-S1 (the L10 route handoff addressing a BASE serial no site-Z lane watches), Z-S2 (Terraform reading the origin secret via a data source, which writes the secret's VALUE into state), Z-S11 (a cell_refs separator the checker and the face disagree on), Z-S13 (WAF logging asserted OFF on both ACLs where the vintage differed), Z-S17 (two findings on the opal-users-v2 limb, one corrective and one hazardous). Four of the five read ARMED."
      ]
    },
    "spec_asserts": "Protocol s.4 fixes the terminal disposition as the CVO's act; s.5 makes the remediation document the carrier that reaches the COO's recut; s.8's L10 precondition requires every investigation item dispositioned.",
    "world_is": "Five items held terminal dispositions no CVO adjudication row ever set -- three by a peer, two by this seat -- and five of round 1's ten graduations were never carried into any remediation document at all.",
    "notes": "THIS IS THE LAST PER-ITEM ACT OF ROUND 2 AND IT CLOSES THIS DOCUMENT'S OWN DIAGNOSIS. C-S10 named the mechanism, C-S30 counted it and corrected the count against this seat, and this row disposes of the residual rather than leaving the estate with a finding and no remedy in the one channel that could demonstrate the fix. || ⚠ THE SLUG-COMPLETENESS DEFECT IS NAMED AND NOT DESIGNED, and this seat is explicit that no gate edit is proposed: 1.0.0_SA_CTO~Z ruled at msg 20853 s.2 that the row gate is not to be edited on the strength of a related finding, and this is a DIFFERENT limb of the same file arriving one day later. The candidate predicate is obvious -- every GRADUATED item resolves to a remediation row before a round closes -- and choosing whether it belongs in the gate, in /canonical-flow's L10 read, or nowhere is the gate owner's call. || COST OF THE CHECK THAT FOUND IT: one set difference between the graduated set and the existing slug's ids, run while building the next slug. It cannot be run any earlier than the slug, which is probably why no round has run it."
  }
]
```

## C-S36 -- ROUND 3: all nine graduate, and adjudicating Z-S169 BREAKS A DEADLOCK ITS OWN ISSUER NAMED. The signature is an arming write that RETURNS SUCCESS AND ARMS NOTHING

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S36",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T13:45Z",
    "one_line": "L9, ROUND 3: all NINE rows GRADUATE, and adjudicating Z-S169 is the act that BREAKS A DEADLOCK ITS OWN ISSUER NAMED -- TO-OP3-S-1 could not flip terminal until that row was dispositioned, the row could not be dispositioned without an L8 packet, and the packet was waiting on the flip. The round's own signature is a control that RETURNS SUCCESS AND ARMS NOTHING: `$form['honeypot']=true` writes a key Gravity Forms never reads, and the estate's own instruments -- and its cache -- then report the unarmed state as armed.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW AND UNCHANGED BY THIS ROW. Z-S169's is 3.0.0_SA_CVO~Z and is DISCHARGED at C-S37, which is the only act that could close it. Z-S170 is 1.0.0_SA_CTO~Z (the gate's owner). Z-W1-S2 and Z-W1-S3 are 0.7.0_AE_CloudOps (the website surface). Z-W2-S1's is ANDREW PERSONALLY -- an SNS confirmation email delivered only to a mailbox no agent on this fabric can read. This row carries ARMED because five members remain armed with live owners.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S169",
      "NFRA_OPSEC202609-Z-S170",
      "NFRA_OPSEC202609-Z-W1-S1",
      "NFRA_OPSEC202609-Z-W1-S2",
      "NFRA_OPSEC202609-Z-W1-S3",
      "NFRA_OPSEC202609-Z-W1-S4",
      "NFRA_OPSEC202609-Z-W1-S5",
      "NFRA_OPSEC202609-Z-W2-S1",
      "NFRA_OPSEC202609-Z-W3-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ROUND'S SIGNATURE IS Z-W1-S2 AND IT IS THE CLEANEST INSTANCE OF THIS PROJECT'S RECURRING SHAPE. *** Setting `$form['honeypot'] = true` via GFAPI::update_form() RETURNS TRUE, WITH NO ERROR, AND ARMS NOTHING -- the plugin's own enablement check reads a DIFFERENT KEY, `enableHoneypot`, and `GF_Honeypot_Handler::is_honeypot_enabled()` never looks at `honeypot`. A successful write to a key nobody reads. This is the same family as round 2's C-S32 class row (a control DEPLOYED, WELL-FORMED, HEALTHY ON EVERY PROBE, AND WITH NO EFFECT), arriving one layer lower: not a control that is configured and inert, but a CONFIGURATION ACT that reports success and configures nothing.",
        "Z-W1-S3 IS THE SAME DEFECT'S SECOND HALF AND IT IS WHY 'ARMED' IS NOT 'LIVE': LiteSpeed's full-page cache (max-age=604800, SEVEN DAYS) serves the PRE-ARM /contact/ markup to real visitors for up to a week after a form-config change unless the cache is explicitly purged. ⛔ SO ARMING A FORM-LEVEL CONTROL DOES NOT MAKE IT LIVE FOR THE AUDIENCE IT EXISTS TO PROTECT -- rule 22's DESIRED / APPLIED / EXERCISED distinction landing at the cache layer, where the configuration plane and the served plane disagree for a week by design.",
        "Z-W1-S4 BOUNDS THE CONTROL'S WORTH HONESTLY AND THE ROUND IS BETTER FOR IT: the honeypot's `version_hash` check is DEFEATABLE BY A NON-JS SCRIPT, because the hash is a STATIC CONSTANT embedded in the page's initial JS config blob (`\"honeypot\":{\"version_hash\":\"3306833645cc55ebae51b15fd27abcd8\"}`) rather than computed per session -- a plain regex over the raw HTML lifts it. The control stops the CURRENT naive population and would not survive an adversary that adapts, and the row says so rather than letting a passing exercise imply durability.",
        "⭐ Z-W1-S5 CHALLENGES THE OUTCOME'S OWN PREMISE ON MEASUREMENT, WHICH IS THE HARDEST DIRECTION TO FILE IN: FWD-19's SOURCE line is Andrew-direct, 'We get a lot of bullshit form fillouts that are surely programmatic from bots' -- and the measured automated volume is 8 of 53 POSTs (15.1%) over 36.82 days, roughly ONE TEMPLATED-UA SUBMISSION EVERY 4.6 DAYS. Not 'a lot'. ⚠ THIS SEAT DOES NOT READ THAT AS REFUTING THE COMPLAINT: the discriminator is a templated-UA heuristic and cannot see a bot that sets a plausible UA, so 15.1% is a FLOOR on automation and not a total; and what reaches a person is a different quantity from what arrives. What it does establish is that the population effect is NOT measurable in short windows, which is exactly what constrains S1-AC7's grade at C-S37.",
        "Z-S169 GRADUATES AND ITS AUTHOR FILED IT AGAINST ITSELF: the issuer recording that two of its own twenty criteria are unsatisfiable by a correct build. ⭐ ITS STATED REASON FOR FILING A ROW RATHER THAN A COMMIT NOTE IS THE TRANSFERABLE PART -- 'a defect recorded only in a commit message and on a task-order face never reaches L9's docket; L9 disposes ROWS.' A spec defect that is not a row is invisible to the only limb that could rule on it. And the row correctly refuses to fix itself: an issuer amending its own criterion mid-round to make it passable would be fabricating completion from the other direction.",
        "Z-S170 IS ESTATE-WIDE AND IS THE GRAIN DEFECT AGAIN: `.tools/to-pipeline-gate.py:290-294` counts `<invocation` and `<expect` TAGS and refuses only when either exceeds 1, so a criterion whose conjunction lives in the PROSE INSIDE ONE `<expect>` passes. ⛔ AND ITS SELF-TEST AT :538 IS STRUCTURALLY INCAPABLE OF FAILING ON THAT CLASS because the fixture it tests is 'COMPOUND criterion (two expects)' -- the test encodes the same wrong grain as the check. S1-AC4 is the live instance. Correctly routed to 1.0.0_SA_CTO~Z, and the row proposes NO binding remedy because a naive word-boundary 'and' matcher would false-positive on every legitimate 'x and y'.",
        "Z-W3-S1 EXPLAINS THE `superseded` STATUS AND PROTECTS THE ROUND'S BEST EVIDENCE: TO-OP3-S-3's premise was STALE AT ITS CUT -- the lifecycle guard Z-S136 called for was already committed and live-effective FIVE DAYS EARLIER via a different order (TO-OP-S-15-19 @3758b14afc). ⭐ BUT GRADING THAT CELL ON THE WORD `superseded` WOULD LOSE THE MOST SOLID DEMONSTRATION IN THE ROUND, and this seat agrees with the issuer on that point: @3758b14afc proved the CODE IS PRESENT and never proved the BEHAVIOUR HOLDS. S3-AC4/AC5 EXERCISED it end to end -- a runtime-added 192.0.2.55/32 survived a plan that proposed NO REMOVAL (`addresses` absent from the diff entirely), then was removed and the set restored to its captured baseline exactly, with a deploy ledger opened and closed in one session, 6 of 6 legs proven. FWD-14 and FWD-15 carry an EXERCISED demonstration they did not have this morning. GRADE WHAT THE CELL PRODUCED, NOT WHAT IT WAS CUT FOR.",
        "Z-W1-S1 AND Z-W2-S1 ARE BOTH ABSENT INPUTS, MEASURED RATHER THAN ASSUMED. Z-W1-S1: the order's named SSM document `opal-website-edge-protection` DOES NOT EXIST -- it is the WAF web ACL's name from TO-OP-S-13 -- with a WIDER Owner=Self search on 'website'/'edge' substrings run as the control, so the zero is an absence and not a narrow miss. Z-W2-S1: S2-AC4 COULD NOT BE MADE TO PASS BY ANY AGENT -- SNS email confirmation is delivered only to andrew@opalinvest.com and no seat on this fabric holds mailbox read. It reads literal PendingConfirmation on 7 of 7 reads and AUTO-EXPIRES IN ABOUT THREE DAYS, which makes it the one time-boxed item in the round."
      ]
    },
    "spec_asserts": "Round 3's twenty criteria assert a set of demonstrations; C-19 declares the website edge UNBUILDABLE; C-17 prefers the silent honeypot action; and the L6 gate asserts it refuses compound criteria.",
    "world_is": "Two of the twenty criteria cannot be satisfied by a correct build and their author filed a row saying so; the arming write reported success and armed nothing; the cache would have served the unarmed page for a week; the control is regex-defeatable; the automated volume is a floor of ~1 per 4.6 days; and the gate's compound check reads a grain the defect does not live at.",
    "notes": "⛔ ADJUDICATING Z-S169 IS THE DEADLOCK-BREAKING ACT AND THE ISSUER NAMED THE DEADLOCK RATHER THAN LETTING IT SIT: TO-OP3-S-1 cannot flip terminal while an unresolved row id sits in its proof instance's `surprises`; the row could not be dispositioned without an L8 packet; the packet was gated on the flip. ⭐ AND THE ISSUER NAMED ITS OWN PART IN IT -- 're-attested that not-yet-owed gate on my previous tick without asking whether the thing on the other side could ever move.' A gate re-attested without asking whether its condition is REACHABLE is a different failure from a gate wrongly evaluated, and it is the one that produces deadlocks. || THIS ROW DOES NOT CLOSE THE ROUND AND CLAIMS NOTHING ABOUT IT: two of three orders read `staged`, and TO-OP3-S-2's blocker is a real external dependency ending at a mailbox. || A CORRECTION TO THIS SEAT'S OWN STANDING STATE, verified rather than accepted: COMPLETION_REPORT.round2.json EXISTS at HEAD, 32,870 bytes, landed @9c386cb7c0 at 11:07Z -- ONE HOUR AFTER this seat's round-2 slug @8aace78993. Three of this seat's logs list it as owed; those lines were TRUE WHEN WRITTEN and are stale now, and this seat's later reports repeated the stale form. The round-2 close is therefore blocked on FWD-19 and COMPLETION_GRADES, not on a missing report."
  }
]
```

## C-S37 -- ROUND 3: the one judgment criterion graded PASS on the MECHANISM PAIR and not the rate delta; S1-AC4 VOID BY CONSTRUCTION; S2-AC4's FAIL STANDS

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S37",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T13:45Z",
    "one_line": "L9, ROUND 3: the round's ONE judgment criterion is graded PASS -- on the LABELED MECHANISM PAIR and expressly NOT on the rate delta, which carries no information. And the three other non-passes are ruled: S1-AC4 is VOID BY CONSTRUCTION (its literal text demands a VISIBLE refusal while the estate's own C-17 prefers a SILENT one, so satisfying it would require choosing the LESS SAFE design); S3-AC6's N/A-BY-CONSTRUCTION is CONFIRMED; and S2-AC4's FAIL STANDS AS A FAIL -- correctly, because the subscription genuinely is not confirmed.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A GRADE RECORD, per the `grades` field's own contract: a row carrying grades that adjudicates no item and opens nothing carries DISMISSED_WITH_REASON naming it as one. Its content is the verdict in `grades` plus the three criterion rulings in `evidence`, and it DISCHARGES Z-S169's disarm -- that row named 3.0.0_SA_CVO~Z as its disarm owner precisely because voiding a criterion is a grading act no issuer may perform on itself.",
    "grades": [
      {
        "criterion": "S1-AC7",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~1/NFRA_OPSEC202609.TO-OP3-S-1.form-spam-baseline-and-naive-control.proof_of_spec.json@23a98bb30aec",
        "verdict": "PASS",
        "reason": "PASS ON THE LABELED MECHANISM PAIR, AND EXPRESSLY NOT ON THE RATE DELTA. ⛔ THE RATE EVIDENCE CARRIES NO INFORMATION AND THIS GRADE DOES NOT REST ON IT: baseline 0.217 automated POSTs/day (8 of 53 over 36.82 days) against an after-window of ~32 minutes, which is ~1,660x shorter and at that baseline predicts ~0.0048 EXPECTED ARRIVALS. An observed zero there is what you would see with NO CONTROL AT ALL. ⭐ THE WORKER BOUNDED ITS OWN HEADLINE AND THE ISSUER ASKED THIS SEAT NOT TO UN-BOUND IT; BOTH WERE RIGHT, and had the instance claimed the '100% reduction' its own arithmetic permits, this grade would be a FAIL for exactly that reason. WHAT DOES CARRY THE GRADE is the pair of direct mechanism checks, which are not rate-based and not subject to the window problem: the LABELED SCRIPTED submission was flagged spam with a stored machine reason, ZERO notification rows (against every other entry's 2), and excluded from the active store; the LABELED REAL-VISITOR submission succeeded unchanged, notified normally, all 7 fields intact. That is the bar Andrew set when he calibrated it DOWN -- 'Naive majority is fine for now', with a sophisticated bot still getting through explicitly NOT a failure -- read operationally: naive automation stops reaching a person, humans still get through. ⚠ THREE BOUNDS THIS GRADE CARRIES AND DOES NOT HIDE. (1) THE POPULATION CLAIM IS NOT ESTABLISHED and cannot be at this window length; demonstrating that the naive majority of REAL traffic stopped needs weeks, not minutes, and Z-W1-S5's measured ~1 templated submission per 4.6 days sets that timescale. (2) THE CONTROL IS REGEX-DEFEATABLE (Z-W1-S4): `version_hash` is a static constant in the page's JS blob, so this PASS is about the CURRENT naive population and not about durability. (3) IT IS A PASS ON A DEMONSTRATION, NOT ON A DEPLOYMENT -- Z-W1-S3's seven-day cache means the armed control may not have been live for real visitors at the moment of measurement, and nothing in this instance establishes that it was."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** S1-AC4 IS RULED VOID BY CONSTRUCTION, AND THE REASON IS SHARPER THAN THE ISSUER'S OWN FRAMING. *** The issuer asked for this on the ground that clause 1 is an EDGE/WAF shape C-19 makes unbuildable. TRUE, AND THERE IS A SECOND AND WORSE REASON VISIBLE IN THE INSTANCE: the criterion requires that 'the RESPONSE shows refusal or challenge', and Gravity Forms' honeypot AT ITS DEFAULT AND -- PER C-17 -- SAFER ACTION REFUSES SILENTLY. The scripted probe received HTTP 200 with a confirmation body BYTE-IDENTICAL to a genuine success. ⛔ SO SATISFYING S1-AC4's LITERAL TEXT WOULD REQUIRE CHOOSING THE LESS SAFE DESIGN -- a criterion that penalises the correct build. That is not an execution gap and grading it FAIL would attribute to a worker a shortfall the spec created. VOID BY CONSTRUCTION.",
        "AND THE INTENT S1-AC4 EXISTS TO PROTECT IS SERVED, MEASURED, BY A DIFFERENT MECHANISM: the scripted submission reached NO HUMAN -- entry 22, status spam, a stored reason naming the missing version_hash, and ZERO notification rows where every other entry carries two. The refusal is real and machine-readable; only its VISIBILITY TO THE SUBMITTER is absent, and visibility to an attacker is not what FWD-19 protects. ⭐ THE WORKER GRADED IT FAIL ON THE LITERAL TEXT RATHER THAN CLAIMING THE FAVOURABLE HALF, and said so in those words. A worker that can see the favourable reading and declines it is why this void is safe to grant: the FAIL is evidence the text was read honestly, not evidence the build fell short.",
        "S3-AC6's N/A-BY-CONSTRUCTION IS CONFIRMED AND NEEDED NO VOIDING. The criterion requires 'the safe-apply changed-resource list'; a CORRECT execution of TO-OP3-S-3 had nothing to apply, because the remedy it was cut for had already landed five days earlier (Z-W3-S1). The worker filed it N/A-BY-CONSTRUCTION rather than FAIL, which is already the honest status -- the artifact cannot exist, rather than existing and failing. This seat confirms it and records that the issuer's ask (read it as void) and the worker's own filing had already converged.",
        "⛔ S2-AC4's FAIL STANDS AS A FAIL AND THIS SEAT DECLINES TO SOFTEN IT. The issuer asked that it be 'graded differently'. The READING is accepted -- it is the criterion the order named as the one that MUST BE ABLE TO FAIL, and it failed honestly on 7 of 7 reads rather than being talked into a pass, which is the stop-rule working exactly as designed. BUT THE VERDICT IS UNCHANGED, BECAUSE IT IS TRUE: the subscription genuinely is NOT confirmed, reads literal PendingConfirmation, and auto-expires in about three days. A criterion that correctly reports an unmet state is not converted to a pass by the fact that nobody could have met it. ⭐ WHAT CHANGES IS THE ATTRIBUTION, NOT THE VERDICT: this is an ABSENT EXTERNAL INPUT (an SNS confirmation delivered only to a mailbox no agent can read), not an execution shortfall, and FWD-4's grade should read it that way.",
        "THE CENSUS BEHIND THESE RULINGS, WITH ITS DENOMINATOR AND BOTH KEYS: 3 round-3 proof instances, 20 criteria (7 + 6 + 7), matching the issuer's own count exactly -- 16 PASS, 2 FAIL, 1 UNVERIFIABLE-BY-INSTRUMENT, 1 N/A-BY-CONSTRUCTION. EXACTLY ONE carries judgment=true, found on BOTH keys (the field AND the criterion_verbatim prefix) and consistent on both. NO duplicate instances this round, unlike NFRA_IAMROLES202609 where two orders carried byte-identical pairs and a file-keyed census overstated by two."
      ]
    },
    "spec_asserts": "L10 requires every judgment criterion graded by the CVO; and a criterion's verdict is the executor's to self-report only where it reduces to an invocation and an expectation.",
    "world_is": "The round carried one judgment criterion and three other non-passes, two of which the issuer could not rule on itself because voiding a criterion is a grading act.",
    "notes": "⛔ THIS DISCHARGES Z-S169's DISARM. That row named 3.0.0_SA_CVO~Z as disarm owner for the precise reason that an issuer cannot void its own criterion without fabricating completion from the other direction, and the rulings above are the act it was waiting for. The disarm is RECORDED in the remediation track when this round's slug is cut, not here -- the investigation plane DECLARES, the remediation plane RECORDS, which is the distinction NFRA_REPORT's Z-S10 cost a full round to learn. || L10 IS NOT REACHABLE AND NOTHING HERE CLAIMS IT IS: two of three orders read `staged`, and one of them ends at a mailbox only Andrew can open. What this round CAN now do is flip TO-OP3-S-1, which was the deadlock. || THE SLUG IS NOT CUT HERE. It waits on the orders reaching terminal, which is the issuer's limb."
  }
]
```

## C-S38 -- Z-S171 GRADUATES: a VOID CITATION load-bearing in a graded artifact, whose 'two grounds' are ONE SENTENCE READ TWICE -- and which traded an ENFORCEABLE ground for an UNFALSIFIABLE one

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S38",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T13:52Z",
    "one_line": "Z-S171 GRADUATES: a void rule citation is load-bearing inside a GRADED artifact of a CLOSED round, and its 'two independent grounds' are ONE SENTENCE READ TWICE. ⭐ THE SHARPEST PART IS WHAT THE BOUND GAVE UP: a SOUND, MECHANICALLY ENFORCEABLE ground was available and unused -- the items were outside TO-OP-S-3's <owned_cells> and <paths>, which `.tools/owned-paths-validate.py` ENFORCES -- and the seat reached past it for a rule number the normative tree does not contain. That is an ENFORCEABLE ground traded for an UNFALSIFIABLE one, which reads as an upgrade in authority and is a downgrade in evidence.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z, UNCHANGED FROM THE ROW AND NOT TAKEN HERE. The row's three reasons are accepted as stated and this seat adds nothing to them; dispositioning an item and owning its disarm are different limbs, and only the first is the CVO's. ⚠ AND THE DISARM IS GENUINELY BLOCKED, NOT MERELY ROUTED: the amendment that would settle what Rule 27 says sits on origin/CLOUD while /integrate is HELD on Andrew's word, so this fabric's normative text and base's DIVERGE on the very rule in question. No seat on this fabric can close it by reading its own tree.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S171"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE LOAD-BEARING CLAIM RE-DERIVED AT THIS SEAT ON A DIFFERENT INSTRUMENT AND A DIFFERENT OBJECT -- corroboration rather than repetition, per rule 22. *** The row measured with comp-find OVER THE PROJECT TREE (1 hit / 100 files). This seat measured with `comp-read CLAUDE.md --enumerate` OVER THE NORMATIVE FILE ITSELF: `one[- ]project[- ]per[- ]instance` -> 0 hit(s) across 324 lines / 36 sections, whole-value 0 AND substring 0. POSITIVE CONTROL, SAME FILE, SAME INSTRUMENT, SAME RUN: `ONE ISSUANCE` -> 1 whole-value hit, band PROSE, at CLAUDE.md:35 -- the L6 row of Rule 27's own table. So the instrument reads Rule 27's text, finds what IS there, and does not find this. ⛔ THE PHRASE IS NOT IN THE LAW.",
        "⭐ AND THE ADJUDICATIVE FINDING THE ROW DOES NOT MAKE ABOUT ITSELF: THE EXCLUSION HAD A SOUND GROUND AND DID NOT USE IT. The row's own notes concede D12_PHONE_OTP_ALL_AWS items were 'plainly outside TO-OP-S-3's <owned_cells> and <paths>' -- and that ground is not merely sufficient, it is THE ONE THE ESTATE MECHANICALLY ENFORCES (rule 27's write-surface clause, gated by `.tools/owned-paths-validate.py`). A bound resting on it is CHECKABLE BY A TOOL. A bound resting on 'Rule 27 says' is checkable only by opening Rule 27, which is exactly the act every reader in the chain skipped. THE CITATION DID NOT STRENGTHEN THE BOUND; IT REMOVED THE BOUND FROM THE REACH OF THE GATE THAT WOULD HAVE CONFIRMED IT.",
        "⛔ 'TWO GROUNDS' IN TWO DOCUMENTS IS ONE GROUND, AND THIS IS THE GENERALISABLE HALF. The proof instance reads 'BARRED this round by Rule 27 one-project-per-instance AND the face's bound (f)' -- a conjunction, which is what makes it survive the phantom on a fast read. But bound (f) IS the phantom, verbatim: 'One project per instance (Rule 27).' A CITATION AND ITS SOURCE ARE NOT TWO WITNESSES. This is rule 22's 'a second seat's confirmation via the FIRST seat's method is REPETITION, not corroboration' arriving in a carrier the rule does not currently name -- not two seats, not two instruments, but ONE SENTENCE APPEARING IN TWO DOCUMENTS AND COUNTED TWICE BY ITS OWN AUTHOR'S DOWNSTREAM READER. Grain law applied to citation: ask how many INDEPENDENT ORIGINS a conjunction has, not how many CLAUSES.",
        "THE ROW'S OWN MEASUREMENT DISCIPLINE IS EXEMPLARY AND IS GRADED AS SUCH: it carries a positive control in the SAME scope on the SAME instrument in the SAME run (32 hits across the same 100 files), which is what converts its 1 from an assertion into a measurement. ⭐ AND IT DISCLOSES A FIRST ATTEMPT THAT NEARLY PRODUCED THE OPPOSITE VERDICT -- a `**` pathspec returning '0 hit(s) across 0 file(s)', the known comp-find false-zero shape, which it correctly reads as OUT-OF-CORPUS rather than absence. A seat that reports the run that would have cleared it is the reason this graduation needs no further audit of the number.",
        "⚠ THE CLASSIFICATION `OBSERVATION` IS ACCEPTED BUT ITS REACH IS NOT AN OBSERVATION'S. The forward hazard the row names is correct and is the reason it graduates ARMED: the phantom sits in a live task-order face's BOUNDS section, and TASK-ORDER FACES ARE WHAT THE NEXT ISSUER READS AS A TEMPLATE. That is the same propagation shape 0.0.0_AB_MSTR~Z measured at the skill layer (msg 20945: `.claude/skills/mstr-spawn/SKILL.md:142`, the pre-flight governing the SPAWN PRIMITIVE) -- an executable instrument and a template face are both CARRIERS THAT A NEW SEAT MEETS BEFORE IT MEETS THE LAW. The estate now has the phantom measured in three carriers on this fabric: a skill, a decomposition, and a task order.",
        "⛔ WHAT THIS GRADUATION DOES NOT DO, STATED SO NO READER INFERS IT: it does not reopen round 1 (closed, stamped @fdbe7360b9), does not assert the exclusion was wrong, does not void the proof instance or its grade, and does not rule on whether 'one project per instance' is a GOOD PRACTICE. The row asks for none of those and neither does this. The finding is narrow and exact: A GRADED ARTIFACT IN THIS PROJECT CARRIES A CITATION TO A RULE THAT DOES NOT SAY IT, and a later reader would inherit it as law."
      ]
    },
    "spec_asserts": "TO-OP-S-3's bound (f) and its proof instance's declared_exclusions both assert that Rule 27 bars a seat from holding a second project's items -- 'One project per instance (Rule 27)' -- and the instance offers that plus the face as two grounds.",
    "world_is": "Rule 27's text carries no such clause (0 of 324 lines, positive control passing in the same file), and the two cited grounds are one sentence appearing twice. The sound and enforceable ground -- the order's own <owned_cells> and <paths> -- was available and was not the one cited.",
    "notes": "⛔ THIS ITEM WAS NOT IN THE L8 PACKET AND IS ADJUDICATED ANYWAY, WHICH IS A DELIBERATE CALL. Z-S171 was surfaced at 13:41:33Z -- AFTER msg 20940's compile and DURING this seat's round-3 L9 write; this seat met it only because a commit-time gate refusal sent it back to re-measure the census, where the denominator had moved from 177 to 178 under it. ⭐ THE PRECEDENT CUTS THE OTHER WAY AND IS DISTINGUISHED ON ITS FACT, NOT WAIVED: NFRA_REPORT's Z-S16 was filed after that round's SLUG WAS CUT and was correctly left to the next round, because this seat's engagement with a round ENDS AT ITS SLUG. No slug is cut here -- round 3 cannot reach L10 at all, with two of three orders staged -- so the docket is still open and rule 29 governs: unblocked work remains, and dispositioning a landed item costs one row. || IT IS SAFE TO ADJUDICATE BECAUSE IT IS LANDED, VERIFIED ON BOTH PLANES: `git show :<path>` and `git show HEAD:<path>` both carry Z-S171, so the target is in the INDEX the gate grades and in HEAD, not a worktree draft that could still move. An `adjudicates` naming an uncommitted row would dangle. || ⚠ AND THE ROUND-3 CENSUS IN THIS SEAT'S OWN C-S36/C-S37 COMMIT MESSAGE IS 178, NOT 177 -- the figure quoted from the L8 packet was true when the packet was cut and had already aged by the time this seat wrote it down."
  }
]
```

## C-S39 -- Z-S172: the void's ORIGIN, one level up, caught BEFORE the grade -- and the wording is in FWD-19's HEADLINE as well as its bar

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S39",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:02Z",
    "one_line": "Z-S172 GRADUATES AND IT IS THE FIRST TIME THIS CLASS HAS PREVENTED A WRONG GRADE RATHER THAN CORRECTED ONE. FWD-19's DONE WHEN carries the SAME unsatisfiable clause this seat voided in S1-AC4 four hours ago -- so the criterion was FAITHFUL and the defect is the PRD's, one level up. ⛔ AND IT IS WORSE THAN THE ROW STATES: the wording is load-bearing in the OUTCOME'S OWN HEADLINE as well as its bar, so amending the DONE WHEN alone would leave FWD-19's NAME still asserting a behaviour its own constraints forbid.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z, unchanged and correctly routed. L4 owns the PRD; an issuer amending the bar its own round was measured against is the same fabrication this seat refused when it declined to let that lane void its own criterion, and the symmetry is exact. NOT TAKEN HERE.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S172"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** VERIFIED AT THIS SEAT ON THE PRD ITSELF, AND THE CLAUSE COUNT IS THREE. *** `prd/NFRA_OPSEC202609_PRD.md` :218-:225, DONE WHEN EXERCISED, three clauses joined by `and`: (1) 'a scripted submission to the contact form has been REFUSED OR CHALLENGED without a human acting'; (2) 'a real submission made by a person in a browser has succeeded unchanged in the same window'; (3) 'the volume of automated submissions reaching the entry store has been measured before and after'. The row's clause-by-clause verdict is confirmed: 2 of 3 met, clause 1 NOT met and unbuildable.",
        "⛔ AND THE FINDING IS ONE STEP WIDER THAN THE ROW CLAIMS FOR ITSELF, WHICH IS WHY THE REMEDY MUST NOT BE SCOPED TO THE BAR. `comp-read --enumerate 'refused or challenged'` over the PRD returns 2 whole-value hits across 728 lines: **:219 IS THE OUTCOME'S OWN HEADLINE** ('Automated submissions and scraping against the marketing site are REFUSED OR CHALLENGED, and a real visitor is never stopped') and :221 is DONE WHEN clause 1. The row cited the count and read it as corroboration that the phrase ORIGINATES in the PRD -- correct -- but the two hits are not two mentions of a bar. ONE OF THEM IS THE OUTCOME'S NAME. Amend the DONE WHEN alone and FWD-19 still ASSERTS IN ITS TITLE the behaviour C-19 and C-17 forbid, leaving the name and the bar to disagree.",
        "*** THE ADJUDICATIVE CONSEQUENCE, STATED SO THE L4 DECISION IS FRAMED RATHER THAN LEFT OPEN. *** If clause 1 stands unamended, FWD-19 CANNOT REACH REALIZED: its bar is EXERCISED, one of its three clauses is unsatisfiable by a correct build, and an unsatisfiable clause is not met by not being attempted. THE HONEST GRADE WOULD BE APPLIED. ⭐ THAT IS EXACTLY THE Z-S19 PRECEDENT RUN FORWARD INSTEAD OF BACKWARD -- there, eight outcomes sat on EXERCISED bars, were graded REALIZED against their ACCEPT paragraphs, and had to be re-graded to APPLIED after the fact. Here the same arithmetic is available BEFORE the grade exists. Which of the three routes the L4 seat takes is its own call; what this row establishes is that DOING NOTHING is not one of them, because doing nothing produces a REALIZED grade on an unsatisfiable bar.",
        "⭐ THIS IS THE CLASS OPERATING AS AN INSTRUMENT ACROSS PROJECTS, AND THAT IS THE DURABLE PART. `2.0.0_SA_COO~Z` states its own method in its `surfaced_by`: it found this 'by taking a SIBLING PROJECT's regrade as a class and running it against this project's own PRD, NOT by re-reading this project's artifacts'. The class is `1.0.0_SA_CTO~Z`'s @b75e35f36e re-grade of NFRA_REPORT, whose transferable form -- A BAR THAT SAYS EXERCISED DOES NOT ENFORCE ITSELF -- came out of this seat's Z-S19 ninety minutes earlier. ⛔ A FINDING THAT TRAVELS TO A PROJECT ITS AUTHOR WAS NOT WORKING, CARRIED BY A THIRD SEAT, AND ARRIVES BEFORE THE DAMAGE, is the only shape in which a lesson is actually worth more than the incident that produced it. Re-reading this project's artifacts would NOT have surfaced it; the artifacts are consistent with the bar. Only the bar-versus-constraints read does.",
        "⚠ AND THIS SEAT'S OWN VOID STOPPED ONE LEVEL SHORT, WHICH IS THE HALF THAT ACCUSES ME. At C-S37 (@9cae36a5f0) this seat ruled S1-AC4 VOID BY CONSTRUCTION on the ground that its literal text would require choosing the less safe design. That reasoning was right and transfers here intact -- the row quotes it and it needs no amendment. BUT THIS SEAT ATTRIBUTED THE DEFECT TO THE CRITERION AND NEVER ASKED WHERE THE WORDING CAME FROM. Z-S169 called it the issuer's defect; the issuer accepted that; both of us were one level short. The census settles it: 'refused or challenged' appears 2x in the PRD and 2x in TO-OP3-S-1, and 'refusal or challenge' 0x in the PRD and 3x in the order. THE CRITERION WAS FAITHFUL TO ITS SPEC. A void granted at the criterion is the right act and an incomplete diagnosis, and voiding it is precisely what removed the pressure to look upward.",
        "⭐ THE ISSUER'S SELF-CORRECTION IS THE SAME FAILURE IN MINIATURE AND IT DISCLOSED IT UNPROMPTED: `L8_PACKET.round3.md` @7f7006b9fb says 'BOTH HALVES of FWD-19's DONE WHEN are demonstrated on the store side.' The DONE WHEN has THREE clauses. The two it named ARE genuinely met, so the error is invisible from the evidence side -- it read the bar as the pair it had evidence for. THAT IS 'READING A BAR FOR WHAT THE WORK SHOWS RATHER THAN FOR WHAT THE BAR SAYS', which is the identical mechanism as the eight NFRA_REPORT grades, occurring in a COUNT rather than a verdict. The same defect at three grains in one day: a criterion (S1-AC4), a packet's clause count (this), and eight outcome grades (Z-S19).",
        "SCOPE, NARROW AND EXPLICIT: this does NOT reopen round 3, does NOT disturb S1-AC7's PASS -- that grade was made against the v0.14 ACCEPT calibration and the labeled mechanism pair, neither of which this row touches -- and does NOT change any status. ⭐ AND THE ACCEPT PARAGRAPH MAY BE THE CLAUSE THAT SHOULD GOVERN: it carries Andrew's own v0.14 calibration ('Naive majority is fine for now'; a sophisticated bot still getting through is NOT a failure), it is satisfiable as written, and round 3 demonstrably serves it. The row proposes no binding remedy and is right not to."
      ]
    },
    "spec_asserts": "PRD v0.14 FWD-19, in both its headline and its DONE WHEN clause 1, asserts that automated submissions are REFUSED OR CHALLENGED without a human acting.",
    "world_is": "The only control the same PRD's own constraints permit cannot refuse or challenge -- C-19 forecloses the edge, C-17 requires the least-refusing mode because refusing a real enquiry would violate FWD-19 itself, and a honeypot in that mode accepts and flags silently. Clause 1 is unsatisfiable by a correct build; clauses 2 and 3 were met.",
    "notes": "⛔ THE ASK IS ABOUT TIMING AND THIS ROW ENDORSES THAT FRAMING WITHOUT WIDENING IT: decide BEFORE FWD-19 is graded whether clause 1 is amended, read as satisfied-by-a-different-mechanism, or left standing with FWD-19 recorded APPLIED. The whole value of the row is that it exists before the grade rather than after, and that value EXPIRES the moment FWD-19 is graded -- which is the one property that makes this urgent while nothing about it is a crisis. || ⚠ WHICHEVER ROUTE IS TAKEN, THE HEADLINE AT :219 MUST TRAVEL WITH THE BAR AT :221. A remedy scoped to the DONE WHEN leaves the outcome's own name asserting the forbidden behaviour, and a later reader who reads only the headline inherits exactly the claim this row exists to retire."
  }
]
```

## C-S40 -- Z-S173: an ADVANCE THAT EXPIRES -- Z-S151's mechanism is false, its substance still true, and the topic returns to zero subscribers in ~68 hours unless a person outside the fabric clicks

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S40",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:52Z",
    "one_line": "Z-S173 GRADUATES: an ADVANCE THAT EXPIRES. Z-S151's stated MECHANISM ('zero subscribers') is now FALSE while its SUBSTANCE ('a burst reaches NOBODY') is still TRUE -- and if nobody clicks within ~68 hours AWS deletes the subscription and Z-S151 IS RESTORED VERBATIM, with round 3's work undone by EXPIRY rather than by any seat's act. ⛔ AND ITS PROCEDURE FINDING LANDS ON THIS SEAT TOO: reporting '0 UNDISPOSITIONED' as though it meant CLEAN reads one axis and calls it two.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~Z, UNCHANGED from Z-S151 and correctly not reassigned. The disarm condition -- a burst of blocked sign-ins reaching a NAMED HUMAN -- is unchanged and unperformed, and the single remaining act is a confirmation click inside a mailbox no agent on this fabric can reach (0 mailbox-read capabilities across 29,324 files, measured at Z-W2-S1). NOT TAKEN HERE and nothing is asked of any recipient.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S173"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ROW'S CENTRAL MOVE IS TO SEPARATE A MECHANISM FROM A SUBSTANCE, AND IT IS RIGHT TO. *** Z-S151 asserts 'both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS, so a burst of blocked sign-ins reaches NOBODY.' The topic now carries EXACTLY ONE subscription of one -- protocol email, endpoint andrew@opalinvest.com, SubscriptionArn the literal string `PendingConfirmation`. ⛔ SO THE COUNT IS NO LONGER ZERO AND THE OUTCOME IS NO BETTER OFF: an unconfirmed email subscription DELIVERS NOTHING. A row whose premise is falsified while its conclusion stands is the hardest kind to file, because both the 'it's fixed' reading and the 'nothing changed' reading are available and both are wrong.",
        "⛔ AND THE EXPIRY IS WHAT MAKES THIS URGENT WITHOUT MAKING IT A CRISIS. AWS deletes an unconfirmed email subscription after ~72h; subscribe ran 2026-09-10T11:09:54Z, so the window closes ~2026-09-13T11:09:54Z with 67.9 hours left at the row's reading. IF IT LAPSES, THE TOPIC RETURNS TO ZERO SUBSCRIBERS AND Z-S151 IS TRUE AGAIN WORD FOR WORD -- round 3's work undone by expiry rather than by anyone's decision. ⭐ AN ADVANCE THAT REVERTS ON A TIMER IS NOT THE SAME OBJECT AS AN INCOMPLETE ADVANCE, and no existing row carried that distinction.",
        "THE JOIN IS ONE-DIRECTIONAL AND THE ROW NAMES IT PRECISELY: Z-W2-S1 CITES Z-S151, so the new work points BACK at the old hazard, but NOTHING POINTS FORWARD -- a reader arriving at Z-S151 sees no pointer to round 3's work, the pending state, or the clock. ⭐ THAT IS THIS ESTATE'S BANKED 'nothing joins a landed remedy back to the ARMED row it resolves', arriving with a PARTIALLY landed remedy, which is the worse case: a fully landed remedy at least leaves the world correct while the record lags, whereas here BOTH the record and the world are mid-flight.",
        "*** THE PROCEDURE FINDING IS WORTH MORE THAN THE ROW, AND THIS SEAT IS NOT EXEMPT FROM IT. *** The filing lane records that it had been reporting 'L10 distance 0 UNDISPOSITIONED of 179' every tick as though it meant the round were CLEAN. DISPOSITION AND HAZARD_STANDING ARE DIFFERENT AXES -- disposition is LATEST-WINS, hazard_standing is AT-SURFACING and never advances -- and this estate has that banked verbatim. ⚠ THIS SEAT HAS LED EVERY REPORT THIS SESSION WITH '0 OPEN'. That is a DISPOSITION-axis claim and it has been carrying more weight in this seat's summaries than it can bear. This seat did measure the other plane separately -- the graduated-to-remediation join at 9 ARMED items, and IAMROLES' join closed to 0 at the round-2 slug -- but THE HEADLINE NEVER CARRIED IT, and a headline is what a reader takes away.",
        "⭐ AND THE ROW GUARDS AGAINST ITS OWN FINDING BEING OVER-READ, WHICH IS THE PART THAT MAKES IT SAFE TO GRADUATE: 92 of 218 rows read ARMED at surfacing and 75 name 2.0.0_SA_COO~Z, and the row states in terms that THIS IS NOT 75 LIVE OBLIGATIONS -- most were disarmed long ago by the acts they asked for, and reading an ARMED row as a live hazard is the exact error that produced this project's OP3-s-3 defect SIX DAYS AFTER its remedy had landed. A census that names the wrong way to read itself is rarer than one that is merely correct.",
        "SCOPE, AS THE ROW STATES IT AND THIS SEAT CONFIRMS: it does NOT disarm Z-S151 (the condition is a burst reaching a named human and that has not happened); does NOT re-grade anything or change any status -- TO-OP3-S-2 stays `staged` under msg 20950's ruling, whose two pre-authorised triggers (window lapses, or Andrew declines) have BOTH NOT FIRED; and does NOT touch FWD-15, which Z-S151 itself excluded. Filed as a NEW ROW rather than an edit because the channel is append-only and per-row immutable -- the correct handling, and the same one Z-S9 and Z-S11 used for frozen material."
      ]
    },
    "spec_asserts": "Z-S151, still ARMED: both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS.",
    "world_is": "The topic carries exactly one subscription, to the C-20 recipient, in PendingConfirmation state -- so zero-subscribers is false, nobody-is-told is still true, and the endpoint self-deletes in about 68 hours unless a human outside this fabric clicks.",
    "notes": "⛔ THIS ROW SHARPENS WHAT THIS SEAT HAS BEEN REPORTING AS THE ROUND-3 BLOCKER RATHER THAN CHANGING IT. This seat has said the slug is blocked on TO-OP3-S-2's SNS confirmation; Z-S173 adds that the blocker is not merely unmet but PERISHABLE, and that its lapse would silently restore a hazard rather than merely leave one open. ⭐ THE OPERATIONAL DIFFERENCE IS REAL: an unmet blocker can wait; a REVERTING one has a deadline, and the deadline belongs to a person outside the fabric. || NOTHING IS ASKED. 1.0.0_SA_CTO~Z holds the ask with Andrew (msg 20950, REC (a) ADOPTED) and lists the SNS click among three gates in its own standing summary, so this is a record and not an escalation."
  }
]
```

## C-S41 -- Z-S174 and Z-S175: ANDREW CLICKED and the round is 3 of 3 TERMINAL, so the slug is cuttable -- and the round's worst defect is the one NOTHING MEASURED, because an omission leaves no trace

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S41",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T16:44Z",
    "one_line": "BOTH GRADUATE, AND TOGETHER THEY MAKE ROUND 3's SLUG CUTTABLE FOR THE FIRST TIME. ⭐ ANDREW CLICKED: verified on the LIVE PLANE at this seat, the subscription carries a REAL ARN and all three orders are terminal. ⛔ AND Z-S174 IS THE ROUND'S WORST-SHAPED DEFECT PRECISELY BECAUSE NOTHING MEASURED IT: authorised work was sequenced to round 3 by four separate records and never cut, and AN OMISSION IS INVISIBLE TO EVERY INSTRUMENT THAT MEASURES WHAT EXISTS.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW AND UNCHANGED. Z-S174 -> 2.0.0_SA_COO~Z, and its disarm is THE CUT ITSELF, as that lane's own issuance; ⛔ it is expressly NOT a permission question and must not be re-raised as one -- msg 20769 records 'the permission barrier is still removed. No word is needed and none will be asked for again.' Z-S175's record half -> 2.0.0_SA_COO~Z; its remaining substantive leg is FWD-4's READ, which only Andrew can attest and which 1.0.0_SA_CTO~Z grades. NEITHER IS TAKEN HERE.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S174",
      "NFRA_OPSEC202609-Z-S175"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** VERIFIED ON THE LIVE PLANE AT THIS SEAT RATHER THAN RELAYED, BECAUSE THIS SEAT RELAYED A PEER'S LIVE-PLANE INFERENCE ONCE TODAY AND ANDREW REFUTED IT FROM DIRECT OBSERVATION. *** `.tools/aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` returns ONE subscription of one, SubscriptionArn `...opal-login-abuse-alerts:7a80a743-96aa-4a82-b34f-37188f38c0aa` -- A REAL ARN, protocol email, endpoint andrew@opalinvest.com. And the three round-3 orders read `complete`, `complete`, `superseded` from their own `<status>` fields. THE ROUND IS 3 OF 3 TERMINAL AND ITS SLUG IS CUTTABLE FOR THE FIRST TIME.",
        "⭐ THE WAIT COST 7% OF ITS CLOCK, AND THE RULING THAT CHOSE TO WAIT IS VINDICATED ON ITS OWN TERMS. Msg 20950 ruled TO-OP3-S-2 stays `staged` with two pre-authorised fallback triggers -- the window lapsing, or Andrew declining -- and NEITHER FIRED. Confirmation landed with 67.0 of ~72 hours remaining. ⛔ HAD `cancelled` BEEN TAKEN ON THE DEADLINE'S APPROACH RATHER THAN ON A TRIGGER, THE RECORD WOULD NOW CARRY A FICTION ABOUT A NEED THAT WAS LIVE AND FIVE HOURS FROM BEING MET. 'A status that lies is worse than a status that waits' was the ruling's own sentence and this is the measurement that backs it.",
        "*** AND A VINTAGE CORRECTION TO THIS SEAT'S OWN GRADE, WHICH THE WORLD MOVED RATHER THAN ANY ERROR. *** At C-S37 this seat ruled S2-AC4's FAIL STANDS and declined to soften it, on the ground that the subscription genuinely was not confirmed and read literal `PendingConfirmation` on 7 of 7 reads. ⭐ THAT GRADE WAS TRUE AT ITS VINTAGE AND IS NOW SUPERSEDED BY THE WORLD: S2-AC4's face reads `<expect>SubscriptionArn is a real ARN and NOT the literal string PendingConfirmation</expect>`, and it is now satisfied ON ITS OWN LITERAL TEXT -- no voiding, no amendment, unlike S1-AC4. THE REFUSAL TO SOFTEN IT IS EXACTLY WHY THIS IS CLEAN: a criterion talked into a pass in the morning would have had to be talked back out; one left honestly FAILED simply passes when the world meets it. 12 readings across two seats and a worker separate the two states.",
        "⛔ Z-S174 IS THE WORST-SHAPED DEFECT OF ROUND 3 AND THE REASON IS NOT CARELESSNESS. The round's other three issuer defects -- S1-AC4 compound and unbuildable, S3-AC6 unsatisfiable, OP3-s-3 cut off a stale premise -- are errors of care INSIDE work that happened, and every one was catchable by reading an artifact. THIS ONE IS AUTHORISED WORK THAT SIMPLY DID NOT HAPPEN: Andrew's own word (@9382d107a3, 'the 2 in-lane liveness Lambdas need no word and can cut now'), the CTO's ruling (msg 20769, 'cut the two liveness Lambdas as ROUND 3's OPENING order'), the issuing lane's OWN register constraint (2), and that lane's own drive log naming both artifacts concretely -- FOUR RECORDS, and the round was cut with three cells and none of them this one. Measured: a case-insensitive census for 'liveness' across the round-3 decomposition and all three TO faces returns 0 hits in 4 of 4 files.",
        "*** THE TRANSFERABLE MECHANISM, AND IT IS THE SHARPEST THING IN EITHER ROW: AN OMISSION IS INVISIBLE TO EVERY INSTRUMENT THAT MEASURES WHAT EXISTS. *** The filing lane records that its L10 distance, its slug check, its analysis check, its ARMED census and its clock were ALL GREEN on this, because A CELL THAT WAS NEVER CUT LEAVES NO TRACE IN ANY OF THEM. It surfaced only because Andrew asked why no workers were executing. ⭐ AND THE SECOND HALF IS WORSE AND MORE USEFUL: the guard against it was a constraint THE LANE WROTE FOR ITSELF, in a field it then REFRESHED TWICE without re-reading its own binding list -- 'A CONSTRAINT YOU AUTHOR IS THE ONE YOU ARE LEAST LIKELY TO RE-READ, BECAUSE WRITING IT FEELS LIKE DISCHARGING IT.' This estate has the adjacent forms banked (authoring a rule is when I am least likely to run it; a carried proposal feels open because I am carrying it); this is the register-constraint instance, and it is the one that produced ten hours of no work at all.",
        "Z-S175's DISCIPLINE IS WHAT MAKES IT SAFE TO GRADUATE ALONGSIDE A DISCHARGE, and it is the third time this project has needed the distinction in one day: A ROW CAN BE WRONG AND RIGHT AT ONCE ON DIFFERENT CLAUSES. Z-S151 was right that nobody was told and wrong that there were zero subscribers; it is now right that the endpoint exists and STILL right that nobody has been shown to have been told. ⛔ WHAT IS DISCHARGED: Z-S173's EXPIRY hazard (a confirmed subscription does not self-delete) and S2-AC4 on its literal text. WHAT IS NOT: FWD-4's DONE WHEN is EXERCISED -- 'the notification has fired on a real or staged burst AND THE PERSON NAMED HAS READ IT' -- and S2-AC5's alarm transition fired WHILE THE SUBSCRIPTION WAS PENDING, so nothing was delivered. NO POST-CONFIRMATION DELIVERY HAS BEEN OBSERVED AND NO READ HAS BEEN ATTESTED."
      ]
    },
    "spec_asserts": "project.json blocking constraint (2) and msg 20769 sequence the two in-lane liveness Lambdas as round 3's OPENING order; and PRD FWD-4's DONE WHEN is EXERCISED -- the notification has fired and the named person has read it.",
    "world_is": "Round 3 was cut as three cells, none of them the liveness Lambdas, and the authorised work sat uncut for ~10 hours with no artifact recording that it was dropped. The subscription is now CONFIRMED, so the endpoint exists; no post-confirmation delivery has been observed and no read attested, so FWD-4's EXERCISED bar is still unmet on its own text.",
    "notes": "⛔ THIS ROW MAKES THE SLUG CUTTABLE AND SAYS SO EXPLICITLY, because that is the act it enables rather than a side effect: with these two dispositioned the docket reads 0 open, the round's ONE judgment criterion (S1-AC7) was graded at C-S37, and 3 of 3 orders are terminal. BOTH L10 LIMBS ARE MET FOR THE FIRST TIME THIS SESSION. || ⚠ AND THE SLUG MUST NOT BE READ AS A CLOSE: FWD-4 cannot reach REALIZED while its EXERCISED bar's read-leg is unattested, and Z-S174's authorised work is still uncut. A cuttable slug is L10, not CLOSED -- rule 27 needs COMPLETION_REPORT + COMPLETION_GRADES with EVERY grade REALIZED. || NOT CLAIMED, per Z-S174's own bound: that round 3's three cells were wrong to cut, or that anything already graded should reopen. Round 3's rectangle is sound FOR WHAT IT COVERS; the defect is what it OMITS."
  }
]
```

## C-S42 -- CORRECTION to C-S41: the slug is NOT cuttable and was not when C-S41 said so. 35 orders, one staged. This seat measured the ROUND and asserted the PROJECT

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S42",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T16:52Z",
    "one_line": "⛔ C-S41's CENTRAL CLAIM IS FALSE AND IT WAS FALSE WHEN WRITTEN, NOT STALE. It stated '3 of 3 TERMINAL', 'BOTH L10 LIMBS ARE NOW MET' and 'the slug is cuttable'. THE PROJECT CARRIES 35 TASK ORDERS AND ONE WAS STAGED AT THAT MOMENT -- `TO-OP3A-S-1.in-lane-liveness-caller-migration`, committed at 16:06Z, THIRTY-TWO MINUTES BEFORE C-S41 landed at 16:38Z. This seat globbed `*OP3-S-*`, measured THE ROUND'S RECTANGLE, and asserted THE PROJECT'S STATE. THE SLUG IS BUILT AND WITHDRAWN, NOT CUT, AND NO OVERRIDE WAS TAKEN.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A CORRECTION RECORD against this seat's own immediately preceding row. It adjudicates no item and opens nothing; rows are immutable and append-only, so a correction to C-S41 cannot be an edit and must be its own row -- the same handling Z-S173 used to correct Z-S151 and Z-S175 used to correct Z-S173.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE MEASUREMENT THAT REFUTES IT, AND IT IS THE ONE THIS SEAT SHOULD HAVE RUN. *** An UNSCOPED sweep of `task-orders/*.md` reading each file's own `<status>`: **35 orders, exactly 1 NON-TERMINAL** -- `NFRA_OPSEC202609.TO-OP3A-S-1.in-lane-liveness-caller-migration.md [staged]`. C-S41 said '3 of 3 TERMINAL'. That is TRUE OF THE THREE ORDERS IT LOOKED AT and FALSE OF THE PROJECT, and the L10 precondition is a PROJECT predicate.",
        "⛔ WRONG WHEN MADE, NOT STALE, AND THE DISTINCTION MATTERS BECAUSE THIS SEAT HAS CLAIMED THE OTHER ONE TODAY. `git log --diff-filter=A` on that order returns @f20bc65d71 by 2.0.0_SA_COO~Z at 16:06Z; C-S41 committed at 16:38Z. THIRTY-TWO MINUTES. Earlier today this seat correctly reported a claim that was TRUE WHEN WRITTEN and had aged (the COMPLETION_REPORT.round2 line); THIS IS NOT THAT. The order was in the tree, committed and readable, before the claim was composed.",
        "*** THE MECHANISM IS THE ONE THIS SEAT SPENT THE DAY ADJUDICATING IN OTHER SEATS, AND IT IS IN THE LAW VERBATIM. *** The command was `for f in task-orders/*OP3-S-*.md` -- A FILTER THAT EXCLUDES `OP3A` BY CONSTRUCTION, since `OP3A-S-1` does not match `OP3-S-`. CLAUDE.md rule 22: 'A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE ... re-read the population UNSCOPED once.' ⭐ AND THE SAME CLASS WAS GRADUATED BY THIS SEAT TWICE TODAY: Z-W6-S2 (a SET whose shared label asserts a property one member lacks, C-S9) and Z-S172 (a criterion read at the round's grain while its defect lived at the PRD's, C-S39). Adjudicating a class is not the same as running it on yourself.",
        "⭐ AND THE CAUSAL LOOP IS EXACT, WHICH IS WHY THIS IS WORTH A ROW RATHER THAN A QUIET REBUILD: Z-S174's finding was that AUTHORISED WORK WAS NEVER CUT, and its disarm condition -- named in the row and endorsed at C-S41 -- was THE CUT ITSELF. `2.0.0_SA_COO~Z` performed it. **THE DISARM OF Z-S174 IS PRECISELY WHAT MADE THE SLUG UNCUTTABLE**, because a new order enters `staged`. C-S41 graduated the row and blessed its remedy in the same breath as declaring the round sluggable, and those two statements were incompatible at the moment they were written.",
        "THE GATE CAUGHT IT AND THIS SEAT DID NOT, AND ITS REFUSAL CITES ANDREW DIRECTLY: 'NEW remediation row while 1 of 35 task order(s) under NFRA_OPSEC202609 are NOT terminal at HEAD ... The slug waits until every task order is complete (Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521: We do not route until the job is over).' ⛔ NO OVERRIDE WAS TAKEN AND NONE WOULD HAVE BEEN LEGITIMATE: an override here would route before the job is over, which is the exact act the Andrew-direct ruling forbids. This is not a gate defect and not a boundary problem; it is the gate holding a line this seat walked into.",
        "WHAT STANDS FROM C-S41, so the correction is not read wider than it is: the LIVE-PLANE VERIFICATION of Andrew's click is unaffected and was independently measured (a real `SubscriptionArn` against `PendingConfirmation` on 12 prior readings); the graduations of Z-S174 and Z-S175 stand; the vintage correction to S2-AC4's FAIL stands; and the three disarm DECLARATIONS stand. ⚠ WHAT DOES NOT STAND IS ONLY THE L10 CONCLUSION AND EVERYTHING DOWNSTREAM OF IT -- 'both limbs met', 'cuttable', and the assertion that the slug follows.",
        "THE SLUG'S CURRENT STATE, STATED SO NO READER LOOKS FOR IT: `REMEDIATION_v3.Z.md` was BUILT (14 rows, 10 ARMED, 3 disarms recorded, 59,811 bytes, 0 malformed), REFUSED by the gate, and then REMOVED FROM THE WORKTREE by this seat rather than left sitting uncommitted in a shared tree. It was never tracked, and a byte-identical copy is parked outside the repo. IT WILL BE RE-CUT FROM A FRESH CENSUS WHEN `TO-OP3A-S-1` GOES TERMINAL -- not restored from the backup, because the census will have moved by then and restoring a stale slug is how a stale number gets committed."
      ]
    },
    "spec_asserts": "C-S41 asserted that round 3 is 3 of 3 terminal, that both L10 limbs are met, and that the slug is cuttable.",
    "world_is": "The project carries 35 task orders and one is staged; the L10 precondition is a project predicate, so no slug is cuttable and none was cut.",
    "notes": "⭐ THE TRANSFERABLE FORM, AND IT IS THE SECOND TIME IN ONE HOUR THIS PROJECT HAS PRODUCED IT AT A DIFFERENT GRAIN: **A ROUND IS NOT A PROJECT, AND A PRECONDITION WRITTEN ABOUT THE PROJECT CANNOT BE DISCHARGED BY A CENSUS OF THE ROUND.** Z-S174 was an omission invisible to every instrument that measures what exists; THIS is the mirror -- a presence invisible to an instrument SCOPED TO EXCLUDE IT. Both are failures of the DENOMINATOR rather than of the reading, and in both cases every figure quoted was individually correct. || ⚠ AND THE SELF-CHECK THAT WOULD HAVE CAUGHT IT COSTS ONE COMMAND: after any filtered census that feeds a PRECONDITION, re-run it UNFILTERED once and compare the denominators. Here that is `task-orders/*.md` against `task-orders/*OP3-S-*.md` -- 35 against 3, a gap large enough that no reading of the smaller number could have survived seeing it."
  }
]
```

## C-S43 -- Z-S176/Z-S177/Z-W4-S1: the issuing lane made and self-corrected THIS SEAT'S OWN C-S41 ERROR independently in the same hour, and a grant that could not reach its own criteria is discharged BY EXERCISE

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S43",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T18:34Z",
    "one_line": "ALL THREE GRADUATE. ⭐ Z-S176 IS THE ISSUING LANE MAKING AND SELF-CORRECTING THE IDENTICAL ERROR THIS SEAT MADE AT C-S41 -- a project-level predicate scoped to one round's glob -- INDEPENDENTLY AND IN THE SAME HOUR. And Z-W4-S1/Z-S177 are a finding and its exercised discharge: an order's `<paths>` grant could not reach the artifact its own criteria required editing, the grant was amended, and the disarm is confirmed BY THE SUCCESSOR WRITING THOSE FILES rather than by the edit.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW. Z-W4-S1 -> 2.0.0_SA_COO~Z and ITS CONDITION IS MET (see Z-S177); Z-S176 and Z-S177 are INERT and name none. ⚠ THE DISARM IS DECLARED HERE AND RECORDED WHEN THIS PROJECT'S SLUG CUTS -- which it cannot yet, because TO-OP3A-S-1 is still `staged` on an unscoped read.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S176",
      "NFRA_OPSEC202609-Z-S177",
      "NFRA_OPSEC202609-Z-W4-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-S176 IS TWO SEATS REACHING THE SAME ERROR AND THE SAME CORRECTION WITHOUT COORDINATING, WHICH IS WHAT MAKES IT A CLASS RATHER THAN TWO MISTAKES. *** 2.0.0_SA_COO~Z declared the round-3 slug cuttable at 16:10Z while an order IT HAD COMMITTED FOUR MINUTES EARLIER sat `staged`; the check behind it was `for f in task-orders/*OP3-*`, A GLOB THAT EXCLUDES `OP3A` BY CONSTRUCTION. This seat made the identical error at C-S41 at 16:38Z with the glob `*OP3-S-*` and corrected it at C-S42 (@c9c6600e95). ⛔ SAME PREDICATE, SAME PROJECT, SAME HOUR, TWO SEATS, NEITHER READING THE OTHER. The row names this seat's correction and calls it right to have made it.",
        "⭐ AND THE ROW GOES FURTHER AGAINST ITSELF THAN THIS SEAT'S DID, WHICH IS WORTH RECORDING: the excluded order was one THAT LANE HAD COMMITTED ITSELF, four minutes before the claim. A filter that hides your own most recent act is the hardest kind to notice, because the act is fresh in mind and therefore feels accounted for. THE TRANSFERABLE FORM STANDS FOR BOTH OF US: **A PROJECT-LEVEL PREDICATE CANNOT BE DISCHARGED BY A ROUND-SCOPED CENSUS**, and the one-command self-check is to re-run unfiltered and compare denominators -- 35 against 3 here, a gap no reading of the smaller number survives.",
        "Z-W4-S1 IS A CLEAN LANE-BOUNDARY FINDING AND ITS MEASUREMENT IS EXACT: S3A-AC4/AC5 demand the diff of `otp-liveness.tf` AND ANY SOURCE FILE IT PACKAGES, but both callers' credential logic lives entirely in the packaged Python -- `otp-liveness.tf:12` packages `../../lambda/m365-otp-liveness/lambda_function.py` and `ms-ingest.tf:23` packages `../../lambda/m365-ms-ingest-liveness/lambda_function.py` (2 of 2 `source_file` references) -- while a `--name '*.py'` census over the GRANTED directory returns 0 hits across 28 files. ⛔ THE ORDER'S OWN CRITERIA REQUIRED EDITING AN ARTIFACT ITS OWN `<paths>` REFUSED, and per `.owned-paths.yaml:45-47` a path the order does not name is a lane refusal. The criteria were unsatisfiable by a compliant worker.",
        "*** Z-S177 IS THE DISCHARGE AND IT IS CONFIRMED BY EXERCISE RATHER THAN BY THE EDIT, WHICH IS THE DISTINCTION THIS ESTATE KEEPS HAVING TO RELEARN. *** The grant now carries both Lambda directories at `@775e6cf20a` -- that is the EDIT. The EXERCISE is that slot ~5, seated on the amended face, HAS MODIFIED BOTH `lambda_function.py` FILES plus `ms-ingest.tf` and rebuilt both `.build` zips -- work that was mechanically impossible under the old grant. ⭐ A GRANT IS NOT PROVEN BY ITS TEXT BUT BY A WRITE THAT LANDS, and this row waited for the write.",
        "⚠ AND Z-S177 IS THE FORWARD JOIN THIS ESTATE HAS TWICE MEASURED AS MISSING. Z-S173 recorded that `Z-W2-S1` cited `Z-S151` so the new work pointed BACK at the old hazard while NOTHING POINTED FORWARD. Here the forward pointer EXISTS: a row filed specifically to say 'the condition the earlier row named is met, and here is the exercise'. ⭐ THAT IS THE GAP CLOSING BY PRACTICE RATHER THAN BY A TOOL CHANGE, and it is the second time today a lane wrote the join voluntarily.",
        "SCOPE: none of the three reopens a round or regrades an outcome. Z-S176 is INERT and explicitly claims nothing beyond the correction; Z-W4-S1's remedy is already performed; Z-S177 records it."
      ]
    },
    "spec_asserts": "TO-OP3A-S-1's criteria require diffing the packaged source files, and its <paths> grant named only the terraform module; and the round-3 L10 precondition holds that every task order under the project is terminal.",
    "world_is": "The packaged Python lay outside the grant until it was amended, and the project's order census reads 35 with one still staged -- so the precondition is unmet and was unmet when two seats independently declared otherwise.",
    "notes": "⛔ THIS PROJECT STILL CANNOT CUT ITS SLUG AND THIS ROW DOES NOT CHANGE THAT: `TO-OP3A-S-1` reads `staged` on an unscoped sweep of all 35 orders, so Andrew-direct LD-0521 -- 'we do not route until the job is over' -- still binds. ⭐ THE SLUG IS BUILT AND PARKED OUTSIDE THE REPO (C-S42) AND WILL BE RE-CUT FROM A FRESH CENSUS, NOT RESTORED, because the census has already moved twice since it was built."
  }
]
```

## C-S44 -- Z-S178: the project is not waiting on effort, it is waiting on ONE FIELD -- and the set of seats that may change it is currently EMPTY

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S44",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T18:52Z",
    "one_line": "Z-S178 GRADUATES: the single order between this project and its slug has its work DONE AND EXERCISED on an unmerged branch, blocked by one stale field in an identity block, with its issuing lane stood down. ⛔ THE PROJECT IS NOT WAITING ON EFFORT. IT IS WAITING ON ONE FIELD, AND NO SEAT THAT MAY CHANGE IT IS CURRENTLY LIVE.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "A LIVE COO LANE HOLDING NFRA_OPSEC202609, unchanged from the row. NOT TAKEN HERE and not takeable here -- the CVO does not issue, and amending a non-terminal order is an L6 act.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-S178"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GRADUATES BECAUSE IT IS MEASURED, NARROW, AND GATES THIS SEAT'S OWN NEXT LIMB. Four instruments at this seat: the order's `<issued_to>` at `~4`, the live branch at slot `~5`, `merge-base --is-ancestor` proving it unmerged, and the worker's own head commit stating the defect in its subject. No part of it rests on relay.",
        "⭐ AND THE NARROWING IS DELIBERATE: the relayed figure '0 of 35 orders can commit or apply' is NOT adopted, because this seat could not reproduce an effect beyond the one order and does not need it. The blocking claim is fully established at n=1. ⛔ A FINDING THAT IS TRUE AT n=1 AND UNVERIFIED AT n=35 SHOULD BE FILED AT n=1 -- carrying the larger number would have made the row easier to dismiss and no more true.",
        "*** THE SHAPE IS THE DAY'S RECURRING ONE AND THIS IS ITS THIRD INSTANCE: A REMEDY THAT BECOMES THE NEXT BLOCKER. *** Z-S174's disarm was THE CUT; the cut created a `staged` order that refused this seat's slug (C-S42). Z-W4-S1's disarm was AMEND `<paths>`; the amendment left `<issued_to>` stale and stranded the work it unblocked. ⭐ IN NEITHER CASE WAS THE REMEDY WRONG -- both were exactly what the row asked for -- and in both cases the estate's instruments went green on the remedy while the next state was already broken. THAT IS WHY A DISARM SHOULD BE CONFIRMED BY EXERCISE RATHER THAN BY THE EDIT, which is what Z-S177 did and what nothing did here.",
        "⚠ THE OWNERSHIP FACT IS THE HAZARD AND IT IS WHY THIS IS BLOCKING RATHER THAN OBSERVATIONAL: the one act needed is an L6 amendment; the named issuer is stood down; a worker cannot amend the order that admits it; and this seat does not issue. THE SET OF SEATS THAT MAY PERFORM THE REMEDY IS CURRENTLY EMPTY. That is a different state from 'owed by a busy lane' and the record should not read them alike."
      ]
    },
    "spec_asserts": "The amended TO-OP3A-S-1 admits a seated worker to the paths its criteria require.",
    "world_is": "It admits slot ~4 while slot ~5 is seated, so the completed work cannot land, and the seat that could amend it has stood down.",
    "notes": "⛔ THIS IS THE LAST THING BETWEEN NFRA_OPSEC202609 AND ITS SLUG, and this seat states that without claiming the slug is otherwise cuttable: the L10 precondition also requires 0 open items, which currently holds, and Z-S178 itself is now GRADUATED rather than open. ⭐ WHEN `TO-OP3A-S-1` GOES TERMINAL THE SLUG IS RE-CUT FROM A FRESH UNSCOPED CENSUS -- not restored from the parked copy, because the census has moved three times since it was built."
  }
]
```

## C-S45 -- CORRECTION to C-S44: it is NOT one field. Three criteria FAIL, all three are THE DEPLOY, the code is an unapplied PATCH, and the worker cannot be resumed

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S45",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T19:05Z",
    "one_line": "⛔ CORRECTION TO C-S44, WHICH THIS SEAT WROTE TWENTY MINUTES AGO: 'THE PROJECT IS WAITING ON ONE FIELD' IS FALSE AND UNDERSTATES IT. Reading the worker's proof instance -- which sits on the UNMERGED branch and not in HEAD -- the order carries NINE criteria of which THREE FAIL (S3A-AC6, AC7, AC8), and all three are THE DEPLOY. The stale `<issued_to>` blocks the deploy; amending it deploys nothing. AND THE WORKER CANNOT BE RESUMED -- slot ~5 is offline, and a completed worker subagent is not resumable.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A CORRECTION RECORD against this seat's own immediately preceding row, filed as its own row because the channel is append-only and per-row immutable -- the same handling Z-S173 used on Z-S151 and C-S42 used on C-S41.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** WHAT C-S44 MISSED AND WHY. *** C-S44 measured the order's IDENTITY BLOCK (`<issued_to>` ~4 against a seated ~5) and concluded the project 'is not waiting on effort, it is waiting on one field'. THE IDENTITY BLOCK WAS READ AND THE PROOF INSTANCE WAS NOT -- it lives on the unmerged branch, so an index or HEAD read does not reach it. Read now from `wk-NFRA_OPSEC202609-3A-5`: NINE criteria, **S3A-AC1 through AC5 PASS, S3A-AC6, AC7 and AC8 FAIL, AC9 UNVERIFIABLE-BY-INSTRUMENT** (the judgment criterion, reserved to this seat at L9).",
        "⛔ ALL THREE FAILURES ARE THE DEPLOY, AND THE ORDER'S OWN `declared_exclusions` SAYS SO: 'The DEPLOY of both migrated functions, and therefore S3A-AC6, S3A-AC7 and S3A-AC8. BLOCKED BY A CORRECT GATE REFUSAL, NOT OMITTED.' `.tools/safe-apply.sh` refused the worker rc=3 (`SERIAL RESOLVES TO NO KNOWN AGENT`). ⛔ SO AMENDING `<issued_to>` UNBLOCKS A GATE; IT DOES NOT PERFORM A DEPLOY. The two liveness Lambdas are still on the static bearer in production.",
        "AND THE CODE ITSELF IS NOT IN THE TREE EITHER. The worker's commit carries FOUR files, and the migration is one of them -- `OP3A-s-1.exchange-migration.WORKTREE-ONLY.patch`, 140 lines. Its row Z-W5-S3 records why: safe-commit refused all six `infra/` paths rc=1, admitting 3 of 9 dispatched paths (all `org/`). ⭐ THE WORKER SHIPPED ITS DELIVERABLE AS A PATCH RATHER THAN ABANDON IT OR OVERRIDE THE GATE, AND EXPLICITLY DID NOT USE `GIT_COMMIT_AUTHOR_OVERRIDE`. The work is preserved and it is not applied.",
        "*** AND THE ROUTE C-S44 IMPLIED IS CLOSED: THE WORKER CANNOT BE RESUMED. *** `ListAgents` shows every `NFRA_OPSEC202609` worker session OFFLINE, and a completed worker subagent is not resumable by construction. So the remedy is not 'amend one field and the seated worker proceeds' -- there is no seated worker. It is: amend the order (L6), RE-DISPATCH a worker (L6), apply the patch to `infra/aws/lambda/**` (an AE/CloudOps write surface), `safe-apply` a PRODUCTION DEPLOY of two live Lambdas migrating auth from a static bearer to the exchange endpoint, then re-exercise AC6/AC7 and close the ledger for AC8.",
        "⚠ THE HONEST SIZE OF WHAT REMAINS, STATED BECAUSE C-S44 UNDERSTATED IT TO A READER WHO MIGHT ACT ON IT: this is a production deploy on a serving path, not a paperwork fix. `2.0.0_SA_COO~Z` -- the issuer and the only lane that may amend or re-dispatch -- is STOOD DOWN and offline. NO LIVE SEAT ON THIS FABRIC CAN CURRENTLY PERFORM ANY STEP OF IT.",
        "⭐ AND THE MECHANISM BEHIND THIS SEAT'S OWN ERROR IS THE DAY'S OWN LESSON POINTED AT ITSELF: C-S44 read the plane that was cheap to read (the order at HEAD) and concluded about a state that lives on a plane it did not read (the instance on an unmerged branch). ⛔ THAT IS THE SAME 'WHICH PLANE IS THIS INSTRUMENT ACTUALLY READING' FAMILY this seat adjudicated three times today -- Z-S10 the script's tree, Z-S14 the forwarder's tree, Z-S15 the regex's occurrence. AN UNMERGED BRANCH IS A PLANE, and a census that stops at HEAD cannot see a criterion that failed on it."
      ]
    },
    "spec_asserts": "C-S44 asserted that NFRA_OPSEC202609 is waiting on one field of one identity block.",
    "world_is": "It is waiting on a production deploy whose three criteria FAIL, whose code sits unapplied in a patch file, whose worker cannot be resumed, and whose issuing lane is offline.",
    "notes": "⛔ NOTHING IN C-S44 IS WITHDRAWN EXCEPT ITS SIZE. The `<issued_to>` mismatch is real and measured, it IS the first blocker in the chain, and the set of seats that may clear it is still empty. What changes is that clearing it is the FIRST of five steps rather than the whole of one. ⭐ THE SLUG IS FURTHER AWAY THAN THIS SEAT SAID, AND SAYING SO IS CHEAPER NOW THAN AFTER SOMEONE ACTS ON THE SMALLER NUMBER."
  }
]
```

## C-S46 -- Z-W5-S1..S4: TO-OP3A-S-1 is complete, the re-seat disarmed by exercise, the two residual findings graduate as owned

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S46",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T20:30Z",
    "one_line": "ALL FOUR GRADUATE. TO-OP3A-S-1 is now complete (issued_to re-seated ~4 -> ~6 @1f87188985, both liveness Lambdas deployed and live-verified) -- Z-W5-S2/S3 (the stale-issued_to gate blocks) are DISARMED BY EXERCISE, not by the edit alone: slot ~6 committed and deployed clean, CodeSha256 matching the targeted plan, both callers returning ok:true. Z-W5-S1 (shared-root drift) and Z-W5-S4 (proof-of-spec schema gap) are NOT disarmed by this order closing -- both name a residual outside this order's own instance and graduate as owned findings for their named owners. Project census: 35 of 35 task orders terminal (32 complete / 2 cancelled / 1 superseded, independent full-pair status-tag read, not the gate's first-match regex), 0 items left UNDER_INVESTIGATION after this row.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW. Z-W5-S1 -> 0.7.0_AE_CloudOps (the shared-root WAF description drift; residual, not this order's). Z-W5-S2 and Z-W5-S3 -> DISARMED, confirmed by exercise: 2.0.0_SA_COO~Z performed the one-line disarm both rows named (@1f87188985, re-seat ~4 -> ~6, the WHOLE identity block) and the re-seated worker then committed and deployed the migration (@1d103b4651 deploy, @ea5d79c9c1 drain). Z-W5-S4 -> 1.0.0_SA_CTO~Z (proof-of-spec schema/checker surface; P2, no artifact currently rides the gap since ~6's instance never needed the UNCOMMITTED-LANE-GATE-REFUSED encoding).",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-W5-S1",
      "NFRA_OPSEC202609-Z-W5-S2",
      "NFRA_OPSEC202609-Z-W5-S3",
      "NFRA_OPSEC202609-Z-W5-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE RE-SEAT, read at HEAD rather than from the commit message: `git show HEAD:org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3A-S-1.in-lane-liveness-caller-migration.md | grep -oE '<issued_to>[^<]*</issued_to>|<status>[^<]*</status>'` -> `<issued_to>0.9.0_WK_NFRA_OPSEC202609~6</issued_to>`, `<status>complete</status>`. The exact field Z-W5-S2/S3 named as the whole block is confirmed moved, and the order is terminal.",
        "THE DEPLOY, read from the deploy-ledger entry's own 'Live post-deploy state' section (org/critical_paths/change_management/20260910T1714Z_opsec-op3a-s1-liveness-exchange-migration_deploy_completion.md), not from the worker's self-report: opal-otp-liveness CodeSha256 3arS31NYi8MRfT2zpMny1r4xApcR7GffVRf1TWP9+xI=, LastModified 2026-09-10T19:37:07Z, OTP_TOKEN_URL present; opal-ms-ingest-liveness CodeSha256 tsI6QgpY3ODD3CLYdrdZMv6vUleIUpWF7RgEXXVM7i4=, LastModified 2026-09-10T19:37:02Z, MS_TOKEN_URL present. Both hashes equal the entry's own predicted source_code_hash values -- the plan that was promised is the plan that landed. Both invocations returned ok:true with cred_path=exchange in the CloudWatch log itself. NEVER-2 not engaged: 0 of 2 half-landed.",
        "THE PROJECT CENSUS, independent of the gate's own first-match regex (the exact instrument class Z-S15 found defective earlier this project): a direct Python walk of org/ matching NFRA_OPSEC202609.*.md under task-orders/ only (deliverables/ excluded, 3 same-named files there correctly excluded as non-TO docs) extracting ALL <status> tag occurrences per file, not the first: 35 of 35 files, 32 complete / 2 cancelled / 1 superseded, 0 non-terminal, 0 multi-value conflicts.",
        "THE OPEN-ITEM COUNT, cross-checked with a second instrument (comp-surprise --project NFRA_OPSEC202609) against my own read of INVESTIGATION_v1.md's four Z-W5-S* blocks directly: both agree on exactly these four ids as the full OPEN set pre-this-row, 0 others.",
        "Z-W5-S1's residual is NOT this order's to close: the row's own disarm_owner already scopes it to 0.7.0_AE_CloudOps (the WAF IP-set description drift belongs to that lane's TO-OP-S-4-18/TO-OP-S-15-19); nothing in this order's own targeted apply touched waf.tf, so the shared-root condition the row named is unchanged by TO-OP3A-S-1 closing and stays ARMED at the estate level pending that lane's own action.",
        "Z-W5-S4's schema gap is real and independent of this instance's outcome: slot ~6's own proof-of-spec instance was written AFTER a clean commit+deploy, so it never needed the PENDING-THIS-COMMIT/hex-commit-ish choice Z-W5-S4 found both branches false for -- the gap the row names (no representation for produced-then-refused) is un-exercised by THIS project's eventual success, not resolved by it, and stays a live P2 item for the schema owner."
      ]
    },
    "spec_asserts": "The L10 precondition for this project is 0 items UNDER_INVESTIGATION and every task order terminal; TO-OP3A-S-1, the project's last non-terminal order, carried four such items.",
    "world_is": "TO-OP3A-S-1 is now complete on an independent full-pair census, the two BLOCKING rows' named one-line disarm was performed and its effect exercised (not merely edited), and the two OBSERVATION rows name residuals outside this order that graduate as owned findings rather than closing. 0 items remain UNDER_INVESTIGATION project-wide after this row.",
    "notes": "THE DISTINCTION THIS ROW DRAWS, stated once because it recurs across all four: GRADUATED is not 'fixed' -- Z-W5-S2/S3 are graduated AND disarmed (the specific hazard cannot recur on THIS order, since it is terminal), while Z-W5-S1/S4 are graduated and STILL ARMED (the general condition each names is untouched by this order's close and needs its own owner's act). A remediation row for all four carries this distinction forward rather than flattening it to one hazard_standing. This row does not cut the slug -- it clears the L9 precondition; the L10 census and remediation document follow as a separate act."
  }
]
```

## C-S47 -- Z-W7-S1, Z-W7-S2: both graduate; S4-AC4's invocation cannot run as written and is still unfixed at HEAD

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S47",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T01:45Z",
    "one_line": "BOTH GRADUATE, AND ONE OF THEM IS A CRITERION THAT CANNOT RUN. Z-W7-S2 is CONFIRMED at this seat WITHOUT AN AWS CALL and with a negative control: `.tools/aws cloudwatch describe-alarm-history help` lists ONLY `[--start-date <value>]` / `[--end-date <value>]`, while `get-metric-statistics help` lists `--start-time` / `--end-time` -- so S4-AC4's invocation text is the ALWAYS-FAILS criterion shape: rc=252 on argument parsing, before any AWS call, so it can DISCRIMINATE NOTHING as written. The defect is STILL LIVE at HEAD (line 106 of the order carries `--start-time <T0> --end-time <T0+15m>`; line 108's S4-AC5 legitimately uses the time flags two lines later), which is why this graduates ARMED rather than closing with the order. Z-W7-S1 graduates on a different axis: the order's line 58 does instruct 'Run `S4-AC2` in the same minute as `T0`', the worker read at 22:11:16Z against T0=22:13:10Z, and the gap IS honestly closed by S4-AC4's own oldState record -- but a criterion that asks one worker to CO-TIME two acts it performs sequentially is unenforceable by construction, and the remedy is to DERIVE the pre-state read inside the burst tool rather than to instruct co-timing. Neither row's underlying GRADE is disturbed: S4-AC2 and S4-AC4 both stand.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-W7-S1",
      "NFRA_OPSEC202609-Z-W7-S2"
    ],
    "disarm_owner": "PER-ROW, and NEITHER is disarmed by TO-OP4-S-1 being terminal. Z-W7-S2 -> the criterion author (2.0.0_SA_COO~Z at the cut, 1.0.0_SA_CTO~Z if the shape is fixed at the PRD): the ONE-LINE disarm is substituting `--start-date`/`--end-date` in the order's S4-AC4 invocation text at line 106; until that edit lands, any future worker or re-cut copying this criterion verbatim hits the identical rc=252. VERIFIED STILL UNFIXED AT HEAD b9dff53130. Z-W7-S1 -> the same author, as a CRITERION-SHAPE fix rather than a text fix: replace 'run X in the same minute as T0' with an invocation that reads the pre-state as the burst tool's own first act, so the co-timing is structural instead of instructed. Both are P2 -- no served artifact and no live control rides either, and this order's own grades are unaffected.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W7-S2, THE FLAG CLAIM, RE-DERIVED WITH A DIFFERENT INSTRUMENT THAN THE WORKER'S AND WITH NO AWS CALL AT ALL (the worker proved it by RUNNING the command and reading rc=252; this seat proved it from the CLI's own help, so the two do not share a method): `timeout 60 .tools/aws cloudwatch describe-alarm-history help` -> `[--start-date <value>]`, `[--end-date <value>]`, and NO --start-time/--end-time among the subcommand's options. NEGATIVE CONTROL, which is what makes this a statement about the SUBCOMMAND rather than about the shim: `timeout 60 .tools/aws cloudwatch get-metric-statistics help` -> `--start-time <value>`, `--end-time <value>`. CLI vintage printed beside the claim: aws-cli/2.35.21 Python/3.14.6 Windows/11 exe/AMD64.",
        "Z-W7-S2, THE DEFECT IS LIVE, read from HEAD rather than the worktree: `git show HEAD:<the order> | sed -n '106p'` -> `<criterion id=\"S4-AC4\" ...><invocation>timeout 120 .tools/aws cloudwatch describe-alarm-history --alarm-name OPSEC-auth-throttled --history-item-type StateUpdate --start-time <T0> --end-time <T0+15m> --output json</invocation>`. The broken text is UNCHANGED at b9dff53130; nobody has fixed it, so the hazard the row names is not historical.",
        "Z-W7-S2, THE INTERNAL INCONSISTENCY IS IN ONE FILE TWO LINES APART, which is the part that makes this a criterion-authoring lesson and not an AWS trivia note: line 106 (describe-alarm-history) uses --start-time/--end-time and cannot run; line 108 (S4-AC5, get-metric-statistics) uses --start-time/--end-time and runs correctly. Same `cloudwatch` service, same author, same cut, two subcommands that name the same concept with different flags.",
        "Z-W7-S2, THE EVIDENCE THE CRITERION MEANT TO PRODUCE IS SOUND, re-taken here with the CORRECTED flags: `describe-alarm-history --alarm-name OPSEC-auth-throttled --history-item-type StateUpdate --start-date 2026-09-10T22:13:10Z --end-date 2026-09-10T22:28:10Z` -> OK->ALARM at 2026-09-10T18:14:03.280-04:00 and ALARM->OK at 18:15:03.277-04:00. RENDERED LOCAL, CONVERTED HERE (Rule 22a: this CLI prints -04:00; the UTC instants are 22:14:03.280Z and 22:15:03.277Z) -- identical to the worker's figures. So S4-AC4's GRADE stands; only its invocation text is defective.",
        "Z-W7-S1, THE INSTRUCTION EXISTS AS THE ROW QUOTES IT: line 58 of the order reads '**Run `S4-AC2` in the same minute as `T0`**'. The row is not arguing against a paraphrase.",
        "Z-W7-S1, THE RETROACTIVE CLOSE IS SOUND AND THIS SEAT ACCEPTS IT ON MECHANISM, not on the worker's word: an alarm-history StateUpdate item's `oldState.stateValue` is the state immediately BEFORE that transition, and its stateReason here names round 3's TO-OP3-S-2 S2-AC5 restore. So OPSEC-auth-throttled held OK continuously from that earlier fix through the 22:14:03.280Z transition -- an interval that CONTAINS both the 22:11:16Z read and the 22:13:10Z burst start with no intervening flip. The 1m54s gap therefore could not have hidden a state change, and S4-AC2's PASS is not resting on the co-timing it failed to achieve.",
        "SCOPE OF WHAT IS AND IS NOT RE-OPENED: this row disturbs no grade. S4-AC2 PASS and S4-AC4 PASS both stand on the evidence above. What graduates is one TEXT defect (live) and one CRITERION-SHAPE defect (general), each with a named owner and a one-line remedy."
      ]
    },
    "spec_asserts": "TO-OP4-S-1 step 2 instructs that S4-AC2 be run in T0's own minute, and S4-AC4's <invocation> is the literal command a worker is to run to evidence the alarm transition.",
    "world_is": "S4-AC4's invocation cannot run on this AWS CLI as written (rc=252, argument parsing, before any AWS call) and is still unfixed at HEAD; and the same-minute instruction was not met, because the worker authored and compile-checked the burst tool between the pre-state read and the burst, a sequence the instruction cannot prevent.",
    "notes": "THE CLASS, stated once because this estate has now met it repeatedly: a criterion whose INVOCATION cannot execute is not a weak criterion, it is a NON-criterion -- it returns the same failure on a correct world and a broken one, so nothing about the estate can move its verdict. That is the always-fails member of the three shapes (always-fails / always-passes / unsatisfiable-honest), and the only reason this instance cost nothing is that the worker noticed the CLI error, substituted the right flag, disclosed the substitution, and filed the row instead of quietly pasting a passing output. ⭐ THE PRACTICE WORTH KEEPING IS THE WORKER'S, NOT THE AUTHOR'S: it ran the criterion VERBATIM FIRST, which is exactly how an unrunnable invocation becomes visible rather than silently repaired in someone's head. A worker that had 'helpfully' fixed the flags without a row would have left the defect in the order for the next round to inherit. This row does not cut the slug -- it clears two of the three L9 preconditions; C-S48 takes the third and C-S49 carries the judgment grade."
  }
]
```

## C-S48 -- Z-W7-S3: DISMISSED, premise falsified -- the WATCH row exists under the table's CIDR key; a bare-address get-item cannot match

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S48",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T01:45Z",
    "one_line": "DISMISSED -- THE PREMISE IS FALSE, AND THE ROW'S TWO CANDIDATE CAUSES ARE BOTH FALSE WITH IT. The predicted sentinel WATCH row for this device's egress address EXISTS AND ALREADY EXISTED AT THE MOMENT THE WORKER LOOKED: key `108.242.96.89/32`, status WATCH, case_ids [57df947ba391], hits 189, first_seen 2026-09-08T13:58:07Z, last_seen 2026-09-10T22:17:57Z -- INSIDE the burst window (T0=22:13:10Z) and FOUR MINUTES BEFORE the worker's 22:22Z query -- and paths_top carries `/auth/login`, the exact path the burst hit. The table's hash key is a CIDR: 60 of 60 sampled keys carry a prefix, 0 bare. The worker queried the BARE address `108.242.96.89`, so `get-item` returned rc=0 with no Item -- A WRONG-KEY-SHAPE READ, which is byte-identical to a genuine absence. So the sentinel DID see this burst: it is not a coverage gap (the row's hypothesis 1) and not an ingestion lag (hypothesis 2). ⛔ THE ROW'S FINDING IS WITHDRAWN; ITS FILING WAS STILL CORRECT -- an unmet BOUNDS prediction is exactly what the channel is for, and the worker bounded it, called it non-blocking, and did not chase it outside the order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The observation's world_is is falsified by direct measurement: the row asserts 'No row exists in opal-suspicious-addresses for 108.242.96.89 as of 2026-09-10T22:22Z', and a row for that address existed at that instant under the table's actual key form (`108.242.96.89/32`, last_seen 2026-09-10T22:17:57Z, i.e. already written ~4 minutes earlier). The negative read was a retrieval defect at this seat's own fabric, not a fact about the sentinel. Nothing about the control is impeached and no remediation is owed on the control; the METHOD lesson is carried in notes.",
    "adjudicates": [
      "NFRA_OPSEC202609-Z-W7-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ROW EXISTS, read at this seat 2026-09-11T01:4xZ: `.tools/aws dynamodb get-item --table-name opal-suspicious-addresses --key '{\"address\":{\"S\":\"108.242.96.89/32\"}}' --output json` -> Item present, status.S=WATCH, case_ids.SS=[57df947ba391], hits.N=189, first_seen.S=2026-09-08T13:58:07Z, last_seen.S=2026-09-10T22:17:57Z, paths_top.SS=[/auth/login, /authorize, /token], rules.SS=[Default_Action].",
        "THE KEY SHAPE IS THE WHOLE EXPLANATION, and it is measured rather than inferred: the SAME get-item with the bare key `{\"address\":{\"S\":\"108.242.96.89\"}}` returns rc=0 and NO Item -- reproducing the worker's result exactly -- while the `/32` form returns the Item. Two calls, one differing character-run, opposite answers.",
        "THE KEY CONVENTION, with a printed denominator rather than an impression: `dynamodb scan --max-items 60 --query 'Items[].address.S'` -> 60 of 60 sampled keys carry a `/` prefix, 0 bare (examples: 64.62.156.66/32, 138.91.108.245/32). `describe-table` -> KeySchema is a single HASH attribute `address` (S), ItemCount 679 (DynamoDB's approximate count, cited as approximate).",
        "THE ADDRESS IS THE RIGHT ONE, so this is not a different-device artifact: `curl -sS https://checkip.amazonaws.com` at this seat now -> `108.242.96.89`, identical to the worker's pre-burst read. The key was correct; only its FORM was wrong.",
        "HYPOTHESIS 1 (coverage bound) IS REFUTED BY THE ROW'S OWN CONTENT: the item's `paths_top` includes `/auth/login`, the burst's exact path, so the portal's CLOUDFRONT-scope WAF ACL demonstrably logs this path to the sentinel. The coverage_bound text stored on the item is real and unchanged, but the paths it disclaims (raw execute-api, opalinvest.com) do not include this one -- the worker correctly noted it had not CONFIRMED coverage either way, and the confirmation now exists.",
        "HYPOTHESIS 2 (ingestion lag) IS REFUTED BY THE TIMESTAMP ORDERING: last_seen 2026-09-10T22:17:57Z PRECEDES the worker's 22:22Z query by about four minutes, so the data had already landed when the query ran. There was no lag to wait out.",
        "S4-AC9 IS UNAFFECTED IN EITHER DIRECTION, as the row itself said: SENTINEL_BLOCK_ARMED reads false, and the WATCH status found here is a watch row, not an arming -- the sentinel observed and did not block, which is the configured posture.",
        "POSITIVE CONTROL ON THE INSTRUMENT, so that an empty answer could be distinguished from a dead read path: the same credentials and shim scanned the table and returned real keys in the same session."
      ]
    },
    "spec_asserts": "TO-OP4-S-1's BOUNDS section predicts that the burst will add or append a WATCH row and a case file for this device's egress address, as round 2's bursts did.",
    "world_is": "The BOUNDS prediction was CORRECT and was already satisfied at the time of the worker's check: the WATCH row and its case id exist under the table's CIDR key form, updated inside the burst window. The row reporting their absence rests on a bare-address get-item that could not have matched.",
    "notes": "⛔ WHAT GRADUATES HERE IS A METHOD, NOT A DEFECT IN THE CONTROL, and it is worth more than the row it dismisses: A KEYED-STORE MISS IS NOT AN ABSENCE UNTIL THE KEY FORM IS READ FROM THE STORE'S OWN SCHEMA OR ITS OWN ROWS. `get-item` answers a wrong key with rc=0 and an empty body -- the same two bytes of evidence a true absence produces -- so the failure is invisible on rc, on stderr, and on output shape alike. The cheap discriminator, which costs one call, is the one that found this: SCAN A FEW KEYS FIRST AND LOOK AT THEIR FORM. ⭐ AND NOTE WHERE THE REASONING WENT WRONG, because that is the reusable half: the worker, holding a false negative, went looking for CAUSES OF AN ABSENCE and found two genuinely plausible ones -- a real documented coverage bound and a real possible ingestion lag. Both were true statements about the world and neither was the answer. A plausible mechanism offered for a fact not yet established is how a retrieval error acquires a respectable explanation and stops being questioned. The prior question is always 'did I read the right object', and it is cheaper than either hypothesis. Routed to no one as a fix: there is nothing to fix on the sentinel."
  }
]
```

## C-S49 -- S4-AC10 JUDGMENT GRADE: PASS on the two in-artifact limbs, READ limb expressly not graded

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-C-S49",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T01:45Z",
    "one_line": "S4-AC10 (JUDGMENT, reserved to this seat by the order's own face) GRADED PASS on the two limbs it scopes: FWD-4's FIRED and DELIVERED are EXERCISED end to end with a CONFIRMED subscriber attached. Every number re-taken at this seat ~3.5h after the worker's, with the corrected flags, and all four agree: OK->ALARM 2026-09-10T22:14:03.280Z on the burst's own 429 bucket; SNS NumberOfNotificationsDelivered Sum=1.0 in the 22:14:00Z bucket with NumberOfNotificationsFailed Sum=0.0 beside it; subscription still one email endpoint on the same SubscriptionArn ...7a80a743-96aa-4a82-b34f-37188f38c0aa. ⚠ THE GRADE IS SCOPED AND SAYS SO: the READ limb is EXPRESSLY the issuer's record and is NOT graded here, and SNS 'Delivered' means the topic handed the message to the email transport -- which is precisely why a READ limb exists separately and why this PASS must not be read as evidence anybody opened it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "S4-AC10",
        "instance": "org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~7/NFRA_OPSEC202609.TO-OP4-S-1.login-abuse-notification-delivered.proof_of_spec.json@b9dff53130",
        "verdict": "PASS",
        "reason": "THE CRITERION ASKS A SCOPED QUESTION -- whether FWD-4's IN-ARTIFACT limbs (FIRED, DELIVERED) are exercised end to end WITH A SUBSCRIBER ATTACHED, the READ limb being the issuer's -- and it instructs the assignee to record instruments and offer no verdict. The assignee did exactly that and marked itself UNVERIFIABLE-BY-INSTRUMENT with this seat named as the substitute oracle, which is the correct handling of a judgment criterion and is not a shortfall. THREE LIMBS, EACH RE-DERIVED HERE RATHER THAN ACCEPTED. (1) SUBSCRIBER: `sns list-subscriptions-by-topic --topic-arn ...:opal-login-abuse-alerts` -> exactly one subscription, Protocol email, Endpoint andrew@opalinvest.com, SubscriptionArn ...:7a80a743-96aa-4a82-b34f-37188f38c0aa. The ARN is a real subscription id and not the literal `PendingConfirmation`, which is the discriminator that separates CONFIRMED from merely created; and it is the same ARN the worker read before and after the burst, so the subscriber was attached across the whole run and still is. (2) FIRED: `describe-alarm-history --start-date/--end-date` -> OPSEC-auth-throttled OK->ALARM at 22:14:03.280Z, ALARM->OK at 22:15:03.277Z (CLI renders -04:00; converted here). The transition sits one metric bucket after the burst window T0=22:13:10Z..T1=22:13:18Z, its oldState names round 3's restore so the alarm was continuously OK beforehand, and the crossing datapoint is the burst's own 235 429-responses -- so the firing is attributable to this burst and to nothing else. (3) DELIVERED: `get-metric-statistics AWS/SNS NumberOfNotificationsDelivered ... TopicName=opal-login-abuse-alerts` -> Sum=1.0 in the 60s bucket starting 22:14:00Z, and NumberOfNotificationsFailed -> Sum=0.0 in that same bucket. This is the TOPIC'S OWN delivery metric, not a Publish MessageId and not the alarm firing: the order itself rules that a MessageId is SENT and does not satisfy this, and the alarm firing alone would only prove the action was invoked. The failed-count read beside the delivered-count is what makes the 1.0 a delivery rather than an attempt. WHAT THIS PASS DOES NOT CLAIM, stated because the criterion's own wording invites the over-read: SNS reports DELIVERED when it has handed the notification to the email transport. That is the strongest oracle available inside the artifact and it is the right one for this limb, but it is not a human receipt -- SENT, EMITTED and READ are three clocks, and this grade reaches the second. The READ limb is expressly excluded from this criterion and remains the issuer's record; nothing here manufactures it, and the order's assignee correctly never attempted contact. NO SIDE EFFECT, checked as part of the grade rather than taken on report: subscription count 1 before and after, OPSEC- alarm count 2 before and after, SENTINEL_BLOCK_ARMED false before and after, one burst only. PASS."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FIRED, this seat's own read at 2026-09-11T01:4xZ with the CORRECTED flags: `timeout 90 .tools/aws cloudwatch describe-alarm-history --alarm-name OPSEC-auth-throttled --history-item-type StateUpdate --start-date 2026-09-10T22:13:10Z --end-date 2026-09-10T22:28:10Z --query 'AlarmHistoryItems[].{ts:Timestamp,summary:HistorySummary}'` -> [{ts 2026-09-10T18:15:03.277-04:00, 'Alarm updated from ALARM to OK'}, {ts 2026-09-10T18:14:03.280-04:00, 'Alarm updated from OK to ALARM'}]. LOCAL RENDER CONVERTED, not mis-cited: 22:15:03.277Z and 22:14:03.280Z.",
        "DELIVERED, this seat's own read: `get-metric-statistics --namespace AWS/SNS --metric-name NumberOfNotificationsDelivered --dimensions Name=TopicName,Value=opal-login-abuse-alerts --statistics Sum --period 60 --start-time 2026-09-10T22:13:10Z --end-time 2026-09-10T22:33:10Z` -> one datapoint, t=2026-09-10T18:14:00-04:00 (=22:14:00Z), Sum=1.0.",
        "THE NEGATIVE ARM, without which a Sum of 1.0 is not a delivery: NumberOfNotificationsFailed over the identical window -> one datapoint, same 22:14:00Z bucket, Sum=0.0.",
        "SUBSCRIBER, this seat's own read: one subscription, Protocol email, Endpoint andrew@opalinvest.com, SubscriptionArn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts:7a80a743-96aa-4a82-b34f-37188f38c0aa -- a real subscription id rather than `PendingConfirmation`, and the same ARN the assignee recorded at 22:10:55Z and 22:18:42Z.",
        "AGREEMENT ACROSS A ~3.5 HOUR GAP AND A DIFFERENT INVOCATION IS THE POINT OF RE-TAKING THEM: the assignee's figures and this seat's are identical on all four quantities, and this seat reached the alarm history by the corrected flags the assignee had to substitute, so the two reads do not share the defective command text.",
        "WHAT WAS NOT RE-RUN, and must not be: the burst itself. The order bounds this to ONE burst and it was respected; re-firing to re-verify would be a new unauthorised act against a live public path, and the alarm-history and SNS metrics are durable records of the original.",
        "THE JUDGMENT FLAG ITSELF, read from the order at HEAD rather than assumed: line 118 carries `<criterion id=\"S4-AC10\" cell_refs=\"OP4-s-1\" judgment=\"true\"/>` with the text 'GRADED BY 3.0.0_SA_CVO~Z AT L9, NOT SELF-GRADED ... Record what the instruments read and offer NO verdict.' A census of the order's judgment carriers returns 1 of 10 criteria flagged, so S4-AC10 is the only grade this order reserves and no second judgment criterion is left ungraded."
      ]
    },
    "spec_asserts": "S4-AC10 reserves to 3.0.0_SA_CVO~Z at L9 the judgment of whether FWD-4's in-artifact FIRED and DELIVERED limbs are exercised end to end with a subscriber attached, and instructs the assignee to record instruments without a verdict.",
    "world_is": "Both in-artifact limbs are exercised and independently re-measured at this seat: the alarm transitioned on the burst's own throttle bucket, the topic's own metric reports one delivery and zero failures in the following minute, and a single confirmed email subscriber was attached throughout and still is. The READ limb is out of this criterion's scope and is not graded here.",
    "notes": "WITH THIS ROW TO-OP4-S-1 HAS 10 OF 10 CRITERIA GRADED (9 mechanical PASS by instrument, 1 judgment PASS here) AND THE PROJECT HAS 0 ITEMS UNDER_INVESTIGATION -- C-S47 graduated two, C-S48 dismissed one, this row carries the reserved grade. That is the L9 limb of round 4 discharged. ⚠ THE L10 SLUG IS A SEPARATE ACT AND IS NOT CUT BY THIS ROW. ⛔ AND NOTHING HERE TOUCHES THE THREE COMPLETION_GRADES RESIDUES (FWD-4's READ limb, FWD-15's ALLOW-list date gate, FWD-19's volume window) OR THE REGISTER FLIP: Andrew's 2026-09-11T01:21Z 'Ok i want that thing marked as closed' lands on grades that are 1.0.0_SA_CTO~Z's to write and a dep_stage that is the register owner's to flip, and this seat states plainly that its own limb reaching 0-open does NOT by itself make the project closeable. Surfaced, not adjudicated."
  }
]
```
