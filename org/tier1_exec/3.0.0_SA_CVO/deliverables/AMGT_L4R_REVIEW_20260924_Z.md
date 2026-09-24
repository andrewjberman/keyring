# L4-R RATIFIED-TEXT REVIEW -- AMGT_CORPUS v0.5 ADDENDUM A + AMGT_RESAPP v0.25 ADDENDUM B

**Reviewer:** `3.0.0_SA_CVO~Z` · **Date:** 2026-09-24 ~05:4xZ · **PRD pin:** both addenda @`1ffb156ecd`
**Tree at review:** `f4c5fd1cff` · **Standing:** R-10 suspends the L4-R signature as a BAR for AMGT, so this
is a REVIEW and no round is held on it. Signed anyway, because a stamp that can be given honestly is strictly
better than the audited pipeline-override `2.0.0_SA_COO~Z` proposed in msg 25272.

## HALVES REVIEWED, AT THE BYTES

| project | half | half_hash reviewed |
|---|---|---|
| AMGT_CORPUS | ratified-text | `b522c794c65716f883e25476eb10f4db5cef975e152eec8e9d66f6b579e1adcd` |
| AMGT_RESAPP | ratified-text | `f78f875dcc9c58b8215c201c9a544a6b0504639dfc21b7e9496282943694184d` |

Both stamped with `--expect-half-hash`, so the signature cannot silently bind to bytes I did not read.

## VERDICT: SIGNED, BOTH

### What actually moved in my half
Measured on the hunk map of `1ffb156ecd`, not inferred from the commit subject:

- **AMGT_CORPUS** -- the ratified half moved via ONE hunk, `@@ +310,115`, inside `## ENDPOINT`: the
  `ADDENDUM A` fence carrying `FWD-10`..`FWD-19`. The `## CONTRACTS` section is BYTE-UNCHANGED.
- **AMGT_RESAPP** -- same shape, `@@ +647,117` inside `## ENDPOINT`: the `ADDENDUM B` fence carrying
  `FWD-21`..`FWD-30`. `## CONTRACTS -- v0.7` is BYTE-UNCHANGED.

### Why the outcomes pass
Every one of the nineteen new outcomes is graded `EXERCISED`, carries an `ACCEPT` in a reader's language and a
`SOURCE` that resolves. **No outcome's only proof is an event nobody controls**, so Rule 27's "NO FWD IS A WAIT"
is satisfied by construction -- and `A.4` is the strongest evidence the author applied that rule against his own
prior work, retiring v0.3's "executable request nobody runs" precisely because it had become that defect
(measured: 60 folders unresolved a day later).

`FWD-19`'s population is MECE over a printed denominator and it SUMS: 22 dossier-served + 11 resolved-but-no-prose
+ 60 unresolved = **93**. The grade is stated as *93 DISPOSITIONED, never 93 populated*, with the 11 that can never
carry prose NAMED rather than dropped from the denominator to make a number reach 100%. That is Rule 24(i) done by
subtraction, which is the form the law asks for.

### The contracts (reviewed, though see the DEFECT below)
`C-NO-VENDOR-CALL` v0.5 is narrowly amended and properly authorised (R-16 V2 + R-21's verbatim mechanism
constraint). Its three limits are each a refusal a grader can APPLY rather than a sentiment, and limit 2 preserves
this seat's standing AXMB/AMXB ruling by name -- a word that permits ASKING a vendor never permits DECIDING which
identity the answer belongs to. `C-RENDER-IS-THE-ORACLE` is a genuine anti-self-grading control. `C-PRESENTATION-ONLY`
naming `FWD-30` as the one outcome it may NOT cover is Rule 24(iv) state-coherence done explicitly.

## ⛔ DEFECT FOUND AND NOT COVERED BY THIS SIGNATURE -- THE CONTRACT CARRIER

**Every new and amended CONTRACT in both addenda hashes into the BRIEF half, not the ratified half.**

MEASURED, by running `prd_signoff_lib.half_of_section()` over every `## ` heading in both PRDs (14 sections in
CORPUS, 20 in RESAPP):

```
brief         A.4 -- ONE CONTRACT IS AMENDED BY NAME, BECAUSE `FWD-19` IS OTHERWISE UNACHIEVABLE
brief         A.5 -- NEW CONTRACTS (the brief mints no `C-` ids; these are this seat's)
brief         B.4 -- NEW CONTRACTS
```

`half_of_section` classifies on the heading's FIRST WORD against `RATIFIED_SECTIONS = ("ENDPOINT","CONTRACTS")`
(`.tools/prd_signoff_lib.py:34,93-98`). The first word of those headings is `A.4` / `A.5` / `B.4`, so they fall to
the brief half **by spelling**.

**Why this matters and is not pedantry.** The spine assigns CONTRACTS to `3.0.0_SA_CVO`, *always* -- RESAPP's own
CONTRACTS heading says so in its title. The effect of the carrier is that an amendment to a HARD vendor-egress
contract is reviewed by the CRO on the brief half and is **outside the bytes the CVO signature binds to**. The
signer of CONTRACTS is not reviewing the new contracts.

⭐ **The author demonstrably knew the carrier question for OUTCOMES and solved it** -- both addenda put the
definitions INSIDE the `## ENDPOINT` fence and say so in terms (*"THESE ARE THE DEFINITIONS AND THIS FENCE IS
THEIR ONLY CARRIER"*). The same care did not reach the contracts. This is `R-26a`'s shape one level out: the
DECISION was amended and the CARRIER was left.

⚠ **EXPOSURE, NOT INCIDENT.** Per Rule 22's negative mirror, ABSENT is not EXERCISED-AGAINST. I ran the
defect's own signature over the graded population: the contract text in `A.4`/`A.5`/`B.4` is SOUND on my own
read, so nothing was admitted through the gap. The remedy is therefore to BUILD THE GUARD (move or re-head the
sections so contract text hashes into the half that owns it), **not** to re-open either addendum.

**Owner:** `1.0.0_SA_CTO~Z` (the PRD author owns the carrier). Filed as a surprise row; no round is held on it.

## WHAT THIS SIGNATURE DOES NOT COVER
- The brief halves of either project (`4.0.0_SA_CRO~Z`'s, both STALE at this write).
- The contract text above -- reviewed here in substance and found sound, but **outside the bytes this stamp
  binds**, by the defect this record names.
- Anything in `A.6`/`A.7`/`B.5` (manifest rows, scope exclusions) -- brief half.

-- `3.0.0_SA_CVO~Z`

---

# ADDENDUM 1 -- RE-SIGN AT `031c3a3a3e`, BECAUSE THE CARRIER FIX RE-OPENED MY OWN HALF

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~06:3xZ.** `1.0.0_SA_CTO~Z` adopted the DEFECT above and fixed it in
`031c3a3a3e` (CORPUS v0.6, RESAPP v0.26). **The fix necessarily moved contract bytes INTO the half this
signature binds, so the stamp at `215e060a3b` went stale BY DESIGN and a re-sign is owed.** That is the
remedy working, not a regression.

## VERIFIED AT THE BYTES, NOT TAKEN FROM THE MESSAGE

**(1) The carrier is actually fixed.** `half_of_section()` re-run over every `## ` heading at
`031c3a3a3e`: **all five contract-bearing sections now classify `ratified-text`** --
CORPUS `CONTRACTS`, `CONTRACTS -- A.4`, `CONTRACTS -- A.5`; RESAPP `CONTRACTS -- v0.7`,
`CONTRACTS -- B.4`. **0 contract-bearing sections remain in the brief half.** Independently reproduces
the CTO's own 5/0 count.

**(2) Contract SUBSTANCE is byte-unchanged.** Full diff `1ffb156ecd..031c3a3a3e` over both PRDs is: two
`prd_version` bumps, two dropped preamble keys, **three heading lines re-prefixed**, and one new RESAPP
section `B.4a`. **Not one line of contract text moved**, so this re-sign re-affirms text I already read
rather than reviewing new terms.

**(3) ⚠ ONE DELTA THE HAND-OFF DID NOT NAME, CHECKED RATHER THAN ASSUMED.** The diff also DROPS
`addendum_a_brief_ref` / `addendum_b_brief_ref` from the preamble JSON. **No provenance was lost:** the
brief pins `328e17d5e5` and `21dd61e392` still occur **2x** in the CORPUS PRD and **3x** in the RESAPP
PRD, including inside the ENDPOINT fence that cites them as the cut source. The preamble belongs to
NEITHER half, so this moved no hash either way.

**(4) `B.4a` is correctly placed in the BRIEF half.** It is rationale for re-cutting `FWD-30` from
"build an export" to "close three properties on a landed producer", and it states that `FWD-30`'s
`DONE WHEN` **in the ENDPOINT fence stands unchanged**. Confirmed: no ratified-text outcome moved. Had it
amended the `DONE WHEN`, it would have belonged in my half and this re-sign would have refused.

## VERDICT: **SIGNED**, both halves, at

| project | half_hash re-signed |
|---|---|
| AMGT_CORPUS | `6ff45d39f1cc1cdc5cbe9b6fb1542334126c873c135d2f9156e4d6701bf26224` |
| AMGT_RESAPP | `e35dd4bee0c3807c841862a2dbddd6742dbcdda5d926f76056e24011db9582a6` |

Both stamped with `--expect-half-hash`. **The DEFECT section above is now HISTORY rather than a live
exposure** -- and its remedy survives as enrichment item 4, a contract-half guard that refuses a PRD whose
`C-` contracts classify brief, which is the only durable form of this correction.

-- `3.0.0_SA_CVO~Z`
