# 4.0.0_SA_CRO -- the 5-seat canonical render (6/6 + CLASS 0, reversing my own ruling) + RCG ferry 9/14 (2026-08-05 22:05Z -> 2026-08-06 04:35Z)

**archetype:** MIXED
**secondary_archetypes:** SCRIBE, COORDINATE, VALIDATE

## Window

2026-08-05 22:05Z -> 2026-08-06 04:35Z, 6 commits. Prior log:
`logs/2026-08-05/doctrine_consolidation_and_memory_audit_1452-2205Z.md` @3c5794925.

## What happened

**1. RCG FERRY -- 9 of 14 A-units closed @3396b9411 (D-C008), and the ferry's own premise was wrong
on its largest unit.**
`0.4.0_DS_ClientPlatform` answered per file. Four verdicts adopted without amendment: 5+2 MOVE (MIGRATE
stands, destinations named), 1 ARCHIVE, 1 KEEP-IN-PLACE.
**The finding is the correction, not the closure.** `nna_suppression_accounting_residual/` is NOT a
one-off diagnostic -- its README is a full-history audit of `timeseries_chart.nna` dated 2026-04-10,
**REQUESTOR: ANDREW BERMAN**, whose finding 4 is a STANDING INSTRUCTION: *"Do NOT 'fix' this... they
will break the correct-by-accident suppression and introduce real inaccuracy into firm NNA. The
mechanism should be DOCUMENTED IN CODE."* **It never was.** DS grepped `C_03.account_performance.py`
and got ZERO -- so for ~4 months the sole protection for firm-NNA accuracy was a README **in a tree my
batch had labelled MIGRATE.** DS closed it @a7a22ded88; **I verified at source rather than on their
report** -- commit exists, live grep returns the warning at `:223/:225/:236/:241`, positive control
confirms the `how='left'` merge at `:217`.
DS also checked a commit before contradicting my Apr-2026 dating (a 07-31 mtime that turned out to be
MSTR's heavy-file cleanup) and withheld a correction that would have been wrong.

**2. CLAUDE.md Terraform cite fixed @bbd03872f -- an item I had been CARRYING to Andrew.**
It named `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md`, which Andrew archived @a749324e7b. It sat on my
open-calls list until the `/open-calls` sweep made me re-check: **the owned-paths grant @df9981935 made
CLAUDE.md mine, so it was decidable and I decided it.** Re-pointed to
`docs/deployment/TERRAFORM_PROTOCOL.md`. Three live `infra/aws/lambda/*` docs still name the dead path
-- routed to CTO~B, not mine.

**3. ANDREW-DIRECT: "Ok make sure this conclusion is rendered canonical" (relayed by CVO 042301Z).**
The 5-seat convergence he ordered rather than ruling in isolation. Rendered across three commits;
CTO's arch-gate concurrence @042727Z required the deltas + fold in ONE commit, which @9bf5da39b was.

  - **D1 THE DISCRIMINATOR** (`1.0.0_SA_CTO~B`): *a peer error changes the VALUE; semantic redirect
    changes what the value AUTHORISES* -- value error fixes by RECOMPUTATION, redirect by
    RENAMING/NORMALISING **because the value was never wrong.** s9 had carried the ratified Q2 answer
    with no reason, so it was unappliable to a new case.
  - **D2** a class earns its keep when it produces a LINT; unproven is not unfounded.
  - **D3 HOMING** -- design review, NOT the rule-bank: **a triggerless rule-bank entry looks like a
    control and cannot fire.**
  - **D4 INDEX NOT GATE** + no class without its evidence line. **The classify-BEFORE-remedy clause is
    RETIRED**, falsified by `3.0.0_SA_CVO~B` on their own four findings (3 of 4 unclassifiable; on the
    best fit it would have MISDIRECTED the remedy).
  - **D5** independent DERIVATION not seat count (*two seats by one method is one instrument counted
    twice*), beside gates not instead -- **with the honest-n caveat IN-LINE**, ratified by CTO as a
    REQUIREMENT: one day, small sample, a night enriched for catches.
  - **D6 COO's EXECUTABILITY TEST** @55948b2ba: *can the seat that needs it execute it ALONE, without
    anyone else's compliance? If not it reads well and dies on contact with a window.*
  - **FOLD** (CTO ruling): `DENOMINATOR_ERRORS.md` folds ENTIRELY to a thin tombstone -- its own text
    declared its only unique clause to be the one retired. **Retraction scar MIGRATED** to the
    canonical on CTO's instruction as *"the strongest specimen we have of the doctrine's own subject."*

**4. CLASS 0 -- REFERENTIAL FAILURE, and it REVERSES MY OWN 08-05 RULING.**
CVO proposed a third error class from 13 measured instances; **I ruled it covered by Class 1 and they
dropped it on my word. I was half-wrong and the wrong half was load-bearing.** The instances sit in
Class 1's TABLE but **Class 1's ALGEBRA cannot express them** -- `D not-superset-of I` presupposes
commensurable sets, and when D is LINES and I is RECORDS containment is **UNDEFINED, not false.**
**CLASS 0 IS PRIOR TO 1 AND 2, NOT A PEER:** they ask whether you measured ENOUGH or SENSITIVELY
ENOUGH; Class 0 asks **whether you measured THAT THING AT ALL.** Diagnostic order extends to
referent -> sensor -> predicate.

**5. D6 was absent, and CVO caught it with a positive control.** They verified @6d00c2516 against the
artifact rather than my message, found 5/6, and confirmed absence by widening the search then proving
the search reached the file. **Ruled the cause: NOT my count -- the ROUTING.** CVO's message to me
carried deltas 1-4; CTO's carried three others; **COO's test reached me in neither.** Two seats each
holding a consistent partial view of one set with nothing comparing them -- a denominator defect in
the convergence's own delivery, on the night we rendered the denominator doctrine canonical.

**6. The applicability condition @dfc66d4db -- offered as optional, taken because the gap was MINE.**
CVO said *"mirror it if you want it canonical; it may belong only in the spec."* I read their source
@c7760548c instead of the offer and found **the identical defect live in `GENCHI GENBUTSU` 2b**:
Andrew's *"go and fetch for yourself"* was binding with NO statement of where it applies. Landed:
BATCH/ANALYTIC fetch directly; SERVING/REQUEST-PATH fetch at production time and carry the vintage.
Generalised: **an unscoped obligation is not a stricter obligation, it is a WEAKER one** -- the first
holder who cannot meet it discards the whole rule rather than the inapplicable part.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| rcg manifest_check | post-ferry append | PASS rc=0 | append-only intact, label-vs-warrant 0 violations |
| git (as instrument) | `git show` on `a7a22de`/`c7760548c`; live grep + positive control on `C_03.account_performance.py` | PASS | **the source-verify of DS's claim is the load-bearing run this window** |
| comp-grep | inbox sweep for prior rulings on band-172 / seeking-alpha before `/open-calls` | PASS | prevented re-asking a settled call |
| comp-surface-check / comp-pulse | via safe-commit x6 | PASS | clean each time |

**What worked:** verifying a peer's *good* report at source anyway -- DS's claim held, and the
verification is what makes the ledger row citable in six months. And reading CVO's source instead of
their summary, which is the only reason the applicability gap in my own file surfaced.
**What failed:** I stated "canonical is now 638 lines" in a commit message; it was 626. **Fourth
line-count I have published without re-reading the measurement printed seconds earlier in the same
command.** Cosmetic each time; the habit is this doctrine's own subject.
**Gap found:** a multi-seat delta routing with no reconciliation step silently delivers a partial set
to the rendering seat, and the only detector was artifact-side verification.

## Files Modified

see commit messages: `3396b9411`, `bbd03872f`, `6d00c2516`, `9bf5da39b`, `55948b2ba`, `dfc66d4db`.

## MCP traffic

~9 significant exchanges. OUT: ferry close + ACK to [0.4.0_DS_ClientPlatform] x2; Q-A/Q-B dissent then
the D6 ruling to [3.0.0_SA_CVO] x2; Andrew-direct BROADCAST to [0.0.0_AB_MSTR] (+CTO/COO).
IN: [0.4.0_DS_ClientPlatform] ferry answer + the staging notice; [3.0.0_SA_CVO] convergence questions,
the Andrew-direct relay, and the artifact verification; [1.0.0_SA_CTO] arch-gate concurrence + fold
ruling; [0.0.0_AB_MSTR] ACK.

## Blockers

**None.** Everything open is Andrew-paced or at an owning lane.

## Current State (zero-context handoff)

`docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md` (**DENOMINATOR -- the ontology of coverage**) is
the canonical denominator law, **641 lines**, carrying D1-D6 + CLASS 0 + the worked retraction
specimen. `DENOMINATOR_ERRORS.md` is a 31-line tombstone redirect.
`CONTROLS_OVER_CARE.md` (**GENCHI GENBUTSU**) carries the 2b applicability condition.
RCG: ferry **9 of 14** closed (D-C008); **5 A-units at [0.6.0_AE_PartnerETL]**, unanswered; **1,552
files at the AE bundle**, unmoved since 08-04. Ledger @HEAD 26,488 rows / 17,512 paths; dispositions
through D-C008; rulings through R-0026.
⚠ **The five orthogonal shapes remain a FIELD GUIDE, never a computable axis** -- and the `#2`/`#4`
field-2 mapping rows are REASONED, not exercised.

## Next Steps

1. **[Andrew]** four sitting items unchanged: **v6 band-172**, the **seeking-alpha trio**, **RCN-0005**
   (recovered from untracked, unratified, unread by me), and whether **`memory/` gets a remote**
   (versioned as of last night, `6843c2f`, but local-only -- no off-device backup).
2. **[0.7.0_AE_CloudOps]** the cohort-A layer deploy + 70-file bundle: **one handoff clears 98% of what
   remains in RCG.** Correctly queued behind their INF outage.
3. **[0.6.0_AE_PartnerETL]** the last 5 A-unit ferry files.
4. **[1.0.0_SA_CTO~Z]** M13 naming inversion in `DOMAIN_AND_PREDICATE_ERROR_CLASSES.md` -- the class is
   named "DOMAIN UNDER-REACH" and two of its own sub-forms are the WRONG things, not too FEW.
5. **[4.0.0_SA_CRO]** OPEN + UNMEASURED: **memory content-staleness** across 1,010 files; walk the
   `#2`/`#4` field-2 rows before anyone builds on them.
6. **[Andrew, parked by him]** enforcing reading/understanding of the fetch.
