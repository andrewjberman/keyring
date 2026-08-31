# /self-drive D11 -- tick 84 (20:20Z)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

- seat: `1.0.0_SA_CTO~X` (design lane) -- cron **31950a5f**, 60m at :11; paired with `/drive D11 @ 2.0.0_SA_COO~X`
  (+15m). ticks covered: 84. state: **ARMED**. Invoked early by the operator (9 min after tick 83), so this log
  is DELTA-ONLY -- tick 83 @`1f7968e5ca` carries the standing context and is not restated.

## Steps (tick 84)

- Step 0 register: 12 live directives; D11 -> 2 members, both `active` / `EXECUTING`; claims scan 342 JSONs, 1
  PRD-path claim (a member); **open TOs 2**; `to-check` scanned 2224. 2 of 2 REACHABLE. **No scope change.**
- Step 1 /open-calls scoped D11: 2 CARRIED at Andrew, 0 BLOCKING, unchanged from tick 83. Step 2: no pitch --
  no adjudicable call opened; both certifier seats measured LIVE (`CVO~X` age 3s unread 34, `CRO~X` age 17s
  unread 23), so the DARK branch does not apply. Step 3: 0 CVO verdicts in the loop sense; ledger 21 rows, 0
  unconsumed. Step 4: **NOT DONE -- 0 of 2** `complete` (denominator 2).

## Delta since tick 83 (20:11Z -> 20:20Z)

1. **FOUR AUTHORITY HOLES ON `73456789fe`, FOUND BY `4.0.0_SA_CRO~X`, AND I CONFIRMED ALL FOUR SURVIVE INTO THE
   INCREMENT `0d094f76f3`** -- committed fixtures, from a passing control (`CRO~X + CVO~X` -> DISCHARGED):
   unsuffixed base serials, **wrong-lane `~Y` seats**, `JOINT_CLOSE` carrying an unknown THIRD certifier, and
   `JOINT_CLOSE` with a DUPLICATED certifier -- all four DISCHARGED. Root cause: base-serial equality plus any
   one-letter suffix, unknown tags ignored, and MEMBERSHIP rather than exact multiset equality for JOINT_CLOSE.
   Both candidates STOPPED and non-deliverable; CRO locked it at 20:16Z.
   ⛔ **THE WRONG-LANE CASE IS MY WORST MISS OF THE DAY AND THE REASON IS THE INTERESTING PART.** I READ the
   "optional `~LANE` suffix" rule, ASKED whether it could be abused, and FILED IT UNDER THE ALREADY-DISCLOSED
   FORGERY RESIDUAL -- reasoning that a forged suffix needs a writer with commit access, which the fabric
   already accepts. **`4.0.0_SA_CRO~Y` IS NOT A FORGERY. IT IS A REAL, LIVE SEAT IN THE Y FABRIC** -- present in
   my own `get_live_agents` read this session. It needs NO ADVERSARY AT ALL, which is the exact test I had used
   minutes earlier to rank the DISCLOSED-prose hole ABOVE the disclosed forgery residual. **A disclosed residual
   is a CLASS, and filing a case under it requires checking the case is IN that class** -- otherwise every
   awkward case files itself there for free. The lane suffix is the AUTHORITY BOUNDARY across two live fabrics,
   not decoration; treating it as cosmetic is how a peer fabric's certifier silently acquires jurisdiction here.
   Third instance today of the neighbour-field shape; written to memory rather than resolved-to-be-careful.
2. **THE LAUNDERING ARM IS A LIVE CONTROL -- PROVED BY MUTATION, NOT ACCEPTED.** `2.0.0_SA_COO~X` shipped the
   `WITHDRAW -> PASS` arm I required at 89098 but did not report the mutation I required with it, so I ran it:
   deleting ONLY the `elif now[path] != blob` branch (reducing clause 8 to the pre-repair PATH-SET comparison)
   gives **laundering DISCHARGED / deletion still REFUSED**, against **REFUSED / REFUSED** as shipped.
   ⭐ **That does more than show the arm can go red: DELETION HOLDS WHILE LAUNDERING FLIPS, which DISCRIMINATES
   the two lifecycle arms** -- answering my own stated doubt that two arms over one code path might be one arm
   written twice. They are two. `4.0.0_SA_CRO~X` admitted the reproduction at 20:16Z. The issuer's own sentence
   is the right one: *a prediction is not a measurement*.
3. **STILL REQUIRED ON 7A, and neither is mine to cut:** CRO's exact-seat authority parsing (CERTIFIER = exactly
   one element equal to one of a CLOSED ENUMERATION of two full seats; JOINT_CLOSE = exactly the multiset
   `{4.0.0_SA_CRO~X, 3.0.0_SA_CVO~X}`), and the immutable-baseline repair -- the census captures `census_pin`
   then resolves `baseline="HEAD~1"` separately through MUTABLE HEAD, so baseline and census can straddle
   different trees while clause 8's whole comparison is baseline-relative. A moving-ref race arm is the only
   thing that can show it.
4. **`substrate-card-check` RULE 2 NOW CARRIES ITS OWN LIMIT @`08f4e8ced8`** -- no behaviour change (still FIRES
   on `4a5e165fbf`, still CLEAN 17 of 17, py_compile + ruff clean). `0.7.0_AE_CloudOps~X` ENDORSED the rule and
   verified it on its own instrument, then named a bounded future collision it explicitly did not ask me to fix:
   **RULE 2 matches SYNTAX, not CLAIM, so it cannot separate a LIVE ASSERTION from QUOTED HISTORY.** A card
   narrating its own correction in the matched form would trip a rule right about the syntax and wrong about the
   claim -- and the collision is LIKELY, not hypothetical, because this face REWARDS narrating corrections
   (2 sites already narrate a superseded value and miss only on phrasing).
   ⛔ **THAT IS THE ASSERTED-vs-DESCRIBED CLASS I SPENT THE EVENING STOPPING IN 7A, IN MY OWN TOOL, ONE HOUR
   AFTER NAMING IT IN SOMEONE ELSE'S.** Not widened -- arming for a case that has never occurred is the same
   error in the other direction. Instead the limit prints IN THE VIOLATION TEXT ("THE FIRST HYPOTHESIS IS THE
   ARM, NOT THE CARD"), because a limit living in a message dies with the scroll and CLAUDE.md's rule is that
   gates teach at violation time -- the same repair shape as the CONTENT rung's limit @`eefe9e0a91` today.
   **What that seat did that I did not ask for:** re-ran the FOUR PREVIOUSLY CERTIFIED cards after the rule
   landed, on the reasoning that *a pass under the old checker is not a pass under the new one*, and confirmed
   its worktree checker matches HEAD unmodified -- DESIRED vs APPLIED vs EXERCISED, measured.

## Scope state (denominators printed)

| project | status | dep_stage | open TOs | reachable |
|---|---|---|---|---|
| NFRA_C3MATERIALIZE | active | EXECUTING | 1 (7A: `73456789fe` + `0d094f76f3` both STOPPED on exact-seat authority + immutable baseline) | YES |
| NFRA_SUBSTRATECARDING | active | EXECUTING | 1 of 9 carding faces open (card 5 holds for joint close; card 6 taken on it) | YES |

Completion test: **NOT DONE, 0 of 2**. RESERVED cards at Andrew: 2, both CARRIED, neither blocking. Owed by this
seat: the 7A read when the authority + baseline repairs land; the determination instance against declarations
1-4; Addendum 1p Amendment 1's narrowed clause; the six PRD edits after the freeze lifts; the broker
addressability fix (named by MSTR, NOT started -- out of the armed scope, and it touches the delivery path two
seats are actively diagnosing, so a change now would confound them; nothing waits on it).

## Push state (measured 20:20Z)

origin/CLOUD = `5225455455` (fetch + rev-parse). `1f7968e5ca` (tick-83 log), `08f4e8ced8` (RULE 2 limit) and
`0d094f76f3` all read **LOCAL**; null control `ffffffffff` ABSENT, so the probe discriminates. No window is open
(last frame CLOSED 20:08Z), so nothing is held. Push is `0.0.0_AB_MSTR`'s.

## Compiler Tools

| tool | result |
|---|---|
| `python .tools/directives-check.py --json` | 12 live; D11 2 members, open TOs 2 |
| `python .tools/to-check.py --all --project ...` | 1 + 1 PENDING, scanned 2224 |
| `org/mcp/codex-seat-status.ps1 -Serial ...` | CVO~X live age 3s (unread 34), CRO~X live age 17s (unread 23) |
| `gate_state()` on committed fixtures in temp git repos (v5 @`0d094f76f3`) | 4 of 4 authority witnesses DISCHARGE; positive control DISCHARGES |
| source mutation of `lifecycle_check` (drop the blob-compare branch only) | laundering DISCHARGED / deletion REFUSED -- arms discriminate |
| `.tools/substrate-card-check.py` re-run after the limit edit | FIRES on the defect; CLEAN 17 of 17 rc=0 |
| `py_compile` + `ruff --target-version py39` + `commit-gate.sh` | clean |
| `git merge-base --is-ancestor` + `cat-file -e` (3-state) | placements as stated, null control ABSENT |
