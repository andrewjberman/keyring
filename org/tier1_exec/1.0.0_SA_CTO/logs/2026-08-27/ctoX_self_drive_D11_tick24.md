# /self-drive D11 — ticks 23-24 · FOUR ADVERSARIAL REWORKS IN ONE WINDOW, AND L1 CLOSED AT 6 OF 7 BY REFUSING AN ESCAPE CLAUSE THAT DID NOT FIT

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 07:20Z–08:50Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)   denominator: 1 of 12 live
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 2
  L1: TO-L1-DTX COMPLETE — 29/29 cells, 26 MEASURED / 3 UNMEASURED, 0 UNMEASURED without a reason
```

**Open calls in scope: 0 adjudicable · 0 RESERVED.** Nothing gated on Andrew, nothing gated on me.

## 1. ⛔ FOUR REWORKS ON MY OWN CONTRACT, EIGHTEEN ACCEPTED MUTANTS, ZERO FOUND BY ME

`4.0.0_SA_CRO~A` ran independent CRO Base matrices against every commit I landed. Every single pass
found something my controls accepted.

| pass | what my validator ACCEPTED | commit |
|---|---|---|
| 3 | whitespace-only `evidence`/`owner`; empty-string degrade path; a declared key CROSSING id spaces with NO mapping | `618c6fbe15` |
| 4 | a one-member `member_set`; `basis=absent` beside concrete members | `3aef865b30` |
| 5 (mine) | prose in `home`; one string carrying four address spaces | `51bd214d42` |
| 6 | `pattern_source` promising `file:line`, accepting `p.py`, `source-token`, `p.py:`, `:1`, `p.py:0` | `59570a9098` |

⛔ **MY `minLength: 1` WAS SATISFIED BY A SINGLE SPACE.** The rule I wrote was *"NEVER null, say the
literal NONE"* — and a space defeats it while looking populated to every consumer downstream.

⛔ **AND THE SHAPE RULING IN PASS 3 CLOSED A REAL HOLE, NOT A TYPO.** A declared key could say
`crosses_spaces: true` and name NO mapping — **precisely the unjoinable-id-space defect this whole
layer exists to surface, expressible as a valid card.**

## 2. THE ONE DEFECT WITH THREE FACES, AND ALL THREE WERE MINE

```
  prose in `home`          "NOWHERE -- unbuilt; no code, no store, no artifact"   3 of 42 parts
  a stored cardinality     a number no validator can check against its array
  `file:line` as ONE STRING  a locator nothing parses
```

>> **A VALUE THE CONSUMER MUST RE-DERIVE AT THE CALL SITE IS A VALUE THE CONTRACT NEVER
   CONSTRAINED.** Three surfaces, one defect, all three inside a schema whose entire subject is
   machine-checkable claims. I refused the typed derivable number in one property and shipped an
   unparsed compound string in the next. <<

⚠ **AND THE PROSE `home` IS THE HARDER HALF OF THE WHITESPACE DEFECT.** It passed every control
including rework 3's non-whitespace pattern **because it is not whitespace.** `0.0.0_AB_MSTR` put it
best back to me: *whitespace looks wrong the moment anyone prints it; a sentence looks RIGHT.* The
value is HONEST about the world — it is the FIELD that is wrong for it, and `population_status`
already says `unknown` in a value a consumer can branch on.

## 3. ⛔ MSTR ROUTED ME A "SEVEN-INSTANCE CONTRACT-COVERAGE" FINDING. MEASURED, IT IS FOUR ARTIFACTS AND 7 OF 9 WERE ALREADY CLOSED

```
  1 joinable_ref            SUBSTRATE_CARD.v2       PRESENT     5 key/failure_mode   L0    @101304be51
  2 the ack instrument      THE BROKER (no schema)  CLOSED      6 all-null receiver  L0    @d630687669
  3 forward_disposition     SUBSTRATE_CARD.v2       PRESENT     7 cardinality        L0    @3aef865b30
  4 artifact.location.home  SUBSTRATE_CARD.v2       PRESENT     8 identity TRIPLE    L0    OPEN -> MINE, taken
                                                                9 scan scope         stores OPEN -> seated
```

**The tally names a NEED, and a need has no grain.** It read as one contract's coverage gap; it is a
Rule 24(ii) SAME-GRAIN failure in the tally itself, and the routing inherited it.

>> **"PATCH-AT-A-TIME IS NOT CONVERGING" IS REFUTED BY THE COUNT. THE DISCRIMINATOR IS NOT
   PATCH-VS-ROADMAP — IT IS WHETHER THE HOST ARTIFACT HAS AN OWNER.** Both open instances are open
   for that reason and no other. `0.0.0_AB_MSTR` upheld the correction against their own routing and
   seated #9 the same turn, off the manifest's own `owner` field — **7 of 42 parts, measured, not
   inferred from a name.** <<

**RULED on #9: NAMED GAP, not a build under D11.** The deciding reason is not the directive's scope —
it is that `0.7.0_AE_CloudOps~X` named the `snap_store.py:415` remedy tonight and correctly did not
apply it. **Ruling the opposite here would make qualify-do-not-fix depend on WHICH SEAT FOUND THE
DEFECT.** Cost stated rather than deferred: **3 of 4 L1 coverage rows stay UNMEASURED** until the
field exists. Non-application stated: binds D11 only, does not bind Andrew.

## 4. L1 CLOSED AT 6 OF 7 — AND THE SEVENTH WAS REFUSED ON PRINCIPLE

`0.4.0_DT_ClientPlatform~X` delivered 29/29 cells and declined AC7's escape clause:

> *"4.0.0_SA_CRO~A ruled the contract PROPOSED, then separately HELD the generator re-run on
> RECEIVER-MUTANT grounds. That is a different blocker from the one AC7 anticipated, so the escape
> clause does not cover it and I am not claiming it does."*

⛔ **A CRITERION SATISFIED BY AN ESCAPE WRITTEN FOR A DIFFERENT BLOCKER IS A PASS THAT READS CLEAN
AND IS NOT.** That lane also nominated three attack targets against its own result and listed seven
self-caught defects of one class.

**Row 6 is the night's transferable and it arrived at four grains:** `file` is the only id space whose
discrimination gate passes, **because its second arm is a DIFFERENT PLANE — the filesystem — not
another projection of the same producer.** A gate needs an oracle OUTSIDE the pipeline that produced
the data. Rule 22's repetition clause, at INSTRUMENT, PARSER, SUBSTRATE, and then at PROPOSAL when
that lane's own interim-safety check validated a shape it had constructed in memory instead of the
committed artifact.

## 5. SEQUENCE 1: STEP 2 IS HELD BY ME, AND THE HOLE WAS IN THE GUARANTEE BOTH OF US GAVE

```
  51c851e8b9 on origin                                      YES (is-ancestor rc=0)
  l0_compile_w3.py / build_manifest.py  write sites         0 and 0
  NEGATIVE CONTROL at 51c851e8b9^                           1 and 1   <- the check CAN fail
  graph_object_manifest.json  denominator.parts_registered  1         <- STILL THERE
```

⛔ **THE ZERO-WINDOW GUARANTEE COVERED THE GENERATOR AND NOT THE ARTIFACT.** Removing the property
now makes the COMMITTED manifest invalid under `additionalProperties: false`, and the only act that
drops the field is the rerun `4.0.0_SA_CRO~A` is holding — **so the window would be exactly as long
as the hold.** Correct order: Base PASS → rerun → artifact loses the field → property removed. Both
seats now hold this; the lane claimed the authorship of the error and it is theirs, but I gave the GO.

⚠ **MY OWN INSTRUMENT FAILED TWICE INSIDE THAT ONE CHECK.** `merge-base --is-ancestor` printed
nothing and I read its rc as *"does not resolve"* when it means *"not an ancestor."* Then
`grep -n parts_registered` hit at `:263` **of the very commit that removed it** — matching the
lane's COMMENT recording the removal. **A grep cannot tell a write from a sentence about the write.**
The discriminating predicate is the write form `"parts_registered":`, and with it the answer inverted.

## COMPLETION TEST

**NOT DONE — 0 of 1 complete.** **REACHABLE 1 / UNREACHABLE 0.** `NFRA_SUBSTRATECARDING` is `active`
/ `EXECUTING`, 2 open TOs. L1 lane closed and routed to `3.0.0_SA_CVO~X` for certification.

## RESERVED — AT ANDREW: **ZERO**

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; this loop dies with the
session. The XXX.md edit is a law-file edit and stays held under Andrew's standing instruction.

## Compiler Tools

`jsonschema` Draft202012 `check_schema` + the live 42-part manifest as a **positive control on every
pass** + hand-built mutants as negative controls (9, then 6, then 12, then 14, then 15 — **each set
written against the defect an adversary named, never against the one I imagined**) ·
`git show <ref>:<path> | grep -c '"field":'` as the **write-vs-comment discriminator**, with the
parent commit as a firing negative control · `git ls-remote` for push state (never a default) ·
`.tools/directives-check.py --json` · `.tools/safe-commit.sh -F` with a Write-authored message file ·
`ack_messages` for the READ clock (49 recorded this window).

**state: ARMED** · next tick :17
