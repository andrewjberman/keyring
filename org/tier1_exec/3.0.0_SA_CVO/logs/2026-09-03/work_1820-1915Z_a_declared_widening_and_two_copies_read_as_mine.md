# 3.0.0_SA_CVO~Z -- work log 2026-09-03 18:20-19:15Z: a declared widening, a pin in the wrong place, and two sends that read as mine

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake + the standing tie-break. **Prior log:** `work_1800-1820Z_*`.
**Push state as read:** local HEAD dd54b46735; origin/SITEZ 001709c96e at 19:11Z. **Loops:** none.

## 1. Z-S62 read (my Z-S64) -- option C is impossible, and one cost was overstated

`0.7.0_AE_CloudOps~Z` found TO-OP-S-1 limb 2 naming a secret-read module that does not exist and a Lambda that
cannot serve a REST authorizer. **Confirmed on the repo plane at this seat:** the authorizer directory holds
exactly one source file (index.mjs, 358 lines) beside package files and deploy.sh, and a repo-wide search finds
no shared secret-read module.

**Added (1) -- option C is STRUCTURALLY impossible, not merely forbidden.** Token census over index.mjs:
`policyDocument` 0, `principalId` 0, `Statement` 0, `Effect` 0, `execute-api:Invoke` 0, against
`generateSimpleResponse` 5 and `EnableSimpleResponses` 2. The file emits ONE shape and contains no code that
emits another. This is stronger than the row's framing because it needs no claim about what the service accepts:
whatever REST would take, this Lambda cannot produce it without being edited, which collapses C into A's cost.

**Added (2) -- option A's proof-invalidation cost is overstated and points at a different defect.** Of the
project's 8 filed proof instances, exactly ONE pins a `CodeSha256` and **its evidence carries no ISO vintage**.
So a redeploy makes that claim STALE, not false. That is a defect in the evidence's FORM, and it will recur on
every future redeploy whatever is decided here. **The A-versus-B trade therefore rests on the rotation-control
argument -- whether the two-slot overlap and TTL live in one place or two -- and not on proof invalidation.**

## 2. The issuer DECLARED a bounds widening and invited objection. NO OBJECTION.

`2.0.0_SA_COO~Z` ruled EXTRACT and declared same-turn that TO-OP-S-1 now admits `opal-portal-authorizer` **for an
extraction only** -- OP-s-2's surface, accepted and closed, which this seat grades at L9. Declaring it rather than
letting me meet it in a diff is the right act independent of the answer.

**Answered promptly because a seat was holding.** The structure already contains what I would have specified: its
own limb 2a with its own ledger entry, a diff bounded to the import line and the deleted function with any other
line a STOP, and the nine routes re-probed on the 403-direct / 200-through-CloudFront discriminator. And the
distinction it draws is the one that matters at L9 and is correct: **a later, separately-ledgered change to an
artifact an accepted TO produced is not a re-execution of accepted work.** TO-OP-S-2's acceptance recorded what
was true at its vintage and stands; nothing is re-graded, nothing rewound.

**Its remedy fixes the defect s.1 measured:** recording the supersession with BOTH values converts a vintage-less
pin into a superseded one with a trail. Worth doing on its own terms.

**ONE CORRECTION THE RECORD NEEDED:** the issuer named TO-OP-S-2's filed pin. **Measured: the pin is in
TO-OP-S-3's instance -- 6 mentions of `CodeSha256`, the only instance with any -- and TO-OP-S-2's has 0.** If the
supersession is written against TO-OP-S-2, the pin that actually goes stale sits in TO-OP-S-3 and stays
unsuperseded, which is the failure the supersession exists to prevent. Scope stated in the send: proof instances
under this project's deliverables only.

**Taken from that seat rather than the reverse:** its Z-S60 severity framing is better than my Z-S61's -- both
grants are `s3:PutObject` scoped to a prefix, so the exposure is foreign WRITES into two `waf-logs/` prefixes and
never reads, an INTEGRITY risk on an evidence bucket rather than a confidentiality one. And its sentence for why
a sound comment left a gap intact -- *"a correct defence of a neighbouring question is why it survived"* -- is
sharper than anything I wrote today. Its halt-gate finding I corroborated from this seat's own earlier
measurement: the lane inbox is `inbox/<BASE>/~<LANE>/` and an EMPTY DECOY exists at the suffixed path, so a
reader building the flat path gets a clean zero rather than an error. Previously measured here at a cost of two
failed reads; this is the first time it cost a CONTROL rather than a search.

## 3. Two sends that read as mine and were not

19930/31/32 and 19939/40/41 opened with second person across three recipients. Both resolved to
`4.0.0_SA_CRO~Z`; I opened my replies with "read as a copy" and verified that seat held them rather than only me,
so nothing was stranded. `0.0.0_AB_MSTR~Z` disclosed the defect against itself, correctly: **not a misroute -- a
mis-addressing.** All three recipients were deliberate; the pronoun was the fault, and the second occurrence put
it in a SUBJECT LINE, which no body qualifier can repair because the subject binds before the body is read. Two
seats spent a message each proving a negative about their own outboxes. **The rule is banked at this seat already
and it is why my cost was one clause rather than a census** -- I did not extend that memory item, which is
already 54.9 KB and carries the subject-line variant explicitly.

**What was substantively mine in those sends, and it strengthens my own condition:** `attempted_at` is not an
added field. It is EIGHT sites -- seven predicates that each define an open leg as one with no proof, plus the
RENDERER at :211 that decides what the markdown a human reads prints. Move the seven and leave the renderer and
the entry still prints OPEN for an attempted-unproven leg, making the exact state the stamp exists to reveal
invisible in the one artifact people look at. **That raises the cost honestly and makes WRITE-AHEAD more
load-bearing, not less:** a stamp written after the act AND applied to only some sites leaves a record that is
populated and still means the old thing, which is worse than not having it.

## 4. Z-S47 confirmed as the carrier, and what it does not carry

`0.0.0_AB_MSTR~Z` confirmed Z-S47 exists and stands as the closed-direction carrier, and disclosed that it had
cited that row in an INSTRUCTION without verifying it -- right by luck, and the same shape as this seat's own
third error today with the direction reversed: a claim that travels loses the check that made it safe.

**Measured what Z-S47 does and does not carry, so the appending row complements rather than repeats:** it holds
the instance, the timeline, the verified discharge with its byte-identical hash, the symmetry statement, and two
remedy shapes named as the contract owner's call. It contains "fabric item", "fabric", "register" and "would not
close" **zero times** -- so the advice to state that the CLASS is a fabric item on the deploy-ledger contract
while the INSTANCE is this project's is exactly the sentence it lacks, and Z-S40 on the same file is the pattern
to copy. The eight sites are genuinely new to the thread: Z-S47 established the record can be wrong in the closed
direction and says nothing about how many places define "open leg".

**The line from that exchange worth more than the exchange:** *a positive control proves the ENGINE and the FILE,
it never proves the PATTERN* -- a control firing on ids shares none of the risk of a probe whose risk lives in
its SUBJECT terms.

## 5. State at close

Channel 66 rows, 19 this seat's. Task orders **7 of 9 complete**, TO-OP-S-1 PENDING, TO-OP-S-17R-28 STAGED.
Resolved-live ARMED 6. Both of this seat's self-corrections are DISARMED by the issuer's rulings (Z-S65, Z-S66)
and the scoped bar landed in the form proposed. Inbox empty, everything acked.

**The one blocked item, stated in full because it has been carried across five logs:** the four round-1 closure
rows for S2, S11, S13 and S17 -- items remediated INSIDE round 1, which need no route because a route answers
"what does the remedy need that does not exist yet" and the answer is nothing. The gate here refuses any NEW
remediation row without a route; the base RULED an exemption for exactly this case and landed it, and those
commits reach this device on the CLOUD -> SITEZ leg, which is ASSESS-ONLY because the site is not quiet and the
push was DECLINED at Andrew's terminal. Measured this window: the gate still reads `c3ef3a2530` with **0**
occurrences of `REMEDIATED`. The append script is written, validated and refuses over a dirty file. **Cost of the
block: nothing live -- those four items' closure sits in prose on Z-S19 rather than in a machine-readable field.**
This seat does not route around it: the gate's own override cannot fire for tree paths on this device, measured
twice, and forcing a shared control would be the wrong act.
