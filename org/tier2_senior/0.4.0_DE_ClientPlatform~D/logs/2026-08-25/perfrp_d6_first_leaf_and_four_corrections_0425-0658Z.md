# The first leaf, two defects in my own instruments, and a number of mine that was two planes wide -- 0.4.0_DE_ClientPlatform~D

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE

**Date:** 2026-08-25
**Task Order:** ADVI_PERFRP.TO-R1-DE
**Status:** IN PROGRESS
**Window:** 2026-08-25T04:25Z -> 06:58Z. Prior log `perfrp_d2_d5_mount_and_the_emission_gap_0014-0425Z.md`.
**Portal DEV commit:** `da2fedda`
**Workspace CLOUD commit:** `a6770ff725`

---

## Objective

The blocker in the prior log resolved: DS~G closed their own emission gap and a leaf exists. Verify
it at the ref rather than off the report, exercise the contract interlock against real bytes for the
first time, and bank whatever the amended criteria now permit.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `-i 'supervis' portal/src` etc. | PASS | Answered COO's standing ask across four planes. It also WARNED me that `\|` is literal in its regex -- a 0-hit that the tool itself flagged as possibly the pattern, not an absence. |
| comp-find | `'supervisedState'` estate-wide | PASS | 5 hits / 26,350 files. The surprise item. |
| comp-find | scoped to `portal/src/...` while CWD was `portal/` | FAIL | `0 hit(s) across 0 file(s)` -- THREE times this window. comp-find resolves paths from the WORKSPACE ROOT regardless of CWD. Every time, the ZERO DENOMINATOR is what showed the sweep had not happened. |
| proof-of-spec-check | positional, 13 ids | PASS | TRUE rc=0, VALID, after the AC13 flip. Alignment 13/13, 10/10, 10/10. |
| ui-smoke.mjs | `advisor-intelligence --fixtures --click Books` | PASS | Resolved the fixture hop. The script already had `--click`, `--netlog`, `--console`, `--fail` -- Build Ladder rung 2 paid off; I had been about to write one. |
| get_delivery_state | self, limit 40 | PASS | 0 foreign acks. Closed 1 of CTO's 5 uncensused seats. |
| emitters (ad-hoc QA) | `perfrp_*_relationship.py --date 2026-08-21 --out <scratch>` | PASS | Produced my own leaves rather than reading anyone's report. No S3 write path in the module -- confirmed at source, not from the message. |

**What worked:** the denominator line, four separate times. Three wrong-scope sweeps and one
`git log --since` that silently matched nothing, all caught by the frame rather than the number.

**What failed:** nothing returned a wrong answer. `curl` could not resolve any host from this seat
(rc=6) -- and my first attempt piped it through `grep`, which printed a CLEAN EMPTY that reads as
"no Content-Encoding header". One `echo $?` from a confident false negative on a peer's open question.

**Gap found:** none in the comp-tools.

---

## Work Completed

### 1. The first leaf, verified at the ref -- and the interlock ties end to end

Ran the emitters myself. Contract interlock verified against a real payload for the first time after
five hours of building against one that had not emitted:

| check | result |
|---|---|
| `contract_version` producer vs mirror | identical, `perfrp-contract-0.5.0-skeleton` |
| `declared_absent_columns` | 10/10 element-identical, same order |
| `periods` | 6/6, same order; `si_label` "since 2024-07-08" -- SI is not `max`, live |
| `basis_line` | `allocationBasisLine('2026-08-21')` BYTE-IDENTICAL to the payload |
| allocation sum | 1.00000000 exact, both residue classes named |

### 2. Two defects in my own instruments -- `da2fedda`

**(a) The exercise suite fails PARTIALLY under node.** 12 legs pass (they import `contract.ts` by an
explicit path), then L13 dies on the first TRANSITIVE import because the perfrp modules import each
other extensionless. The `.mjs` extension points every reader at node. I am the seat that will ask
CVO for an independent run; they would have gotten a FALSE FAILURE on my own work. A total failure
invites suspicion of the setup; twelve greens do not. Guarded: node -> rc=2, ZERO legs.

**(b) My two `NOT_COMPUTED` states were BYTE-IDENTICAL in the renderer.** AE~G's finding turned on
"DE~D renders the reason", so I read what I render. Both mapped to
`{hasValue:false, label:'Not computed', requiresReason:true}` -- the enum's founding defect
re-created one layer above where the producer had just killed it. Added `recomputableDownstream`
with the Rule-24 record inline; postulate (iv) does NOT pass trivially and the comment says so.
Deliberately NOT wired to a visible label: the wording is ratified and the spec is frozen mid-round.

### 3. AC13 BANKED -- `a6770ff725`, 2 PASS -> 3

COO retracted the wording that made it unsatisfiable. Met in the amended form: base `8ecb6b68`,
dirty delta declared mine, `8ecb6b68..da2fedda` = 1 commit, non-mine 0. Recorded as an
**ATTRIBUTION, not a red->green** -- I never typechecked the base alone and did not claim to.

### 4. The membership limb, and a criterion that could not be discharged

Summed the child `accounts` counts: **4,385 relationships -> 7,335 = the account leaf's cardinality,
exactly.** It survives a 100%-null value census because a count is not a return. Declared its limit
in the same breath: NECESSARY, NOT SUFFICIENT -- a double-count paired with an omission gives the
same total. COO's reading was sharper than mine: my own AC11 clause ("no double count expressible")
was therefore **permanently undischargeable**, which is not a criterion. Child ids ruled in, then
relocated to a verification artifact after I corrected my own framing.

### 5. The Books fixture hop -- resolved, root cause clean

My fixture carried `split: true` AND an inline `employee_leaderboard`.
`getPlatinumFirmDashboard` returns early only when `!stub.split`; with the flag set it DISCARDED the
inline data and fetched `leaderboard.json`, which the fixture never keyed -- swallowed by
`.catch(() => null)`. **The fixture looked complete because the field was right there; one boolean
routed the code past it.** One-character fix. Books tab now renders the advisor list; colour law
clean, all light text inside dark panels.

### 6. Surfaced: `supervisedState` (OBSERVATION x INERT, 68787-89)

Answered COO's standing "Supervised" ask. Their TO claim is measured TRUE (DE 0/1, DS 0/1, render
surface 0/60). Found it in the PRD's reference-only section and in three call sites of a bronze
producer that ships DRY. Survived as a mechanism: **a request-side filter is not recoverable from
the raw response it produced**, so Rule 17a's re-derivability covers the CONTENT and is silent on
the POPULATION.

---

## Corrections against myself

| what | consequence | caught by |
|---|---|---|
| `getsize` (CRLF file) vs `json.dumps().encode()` (LF string) | headline +16.0% was NEITHER plane; true +18.7% LF / +19.5% CRLF | DS~G refusing to average a 30,727 B disagreement |
| calling `delta - id_chars` "indent" | claimed 55% then 60.5%; TRUE indent 31.5% -- the conclusion died, not just the digits | CTO reaching 32% independently |
| framed the child-ids ask as "checkable at the render boundary" | put a once-per-acceptance check into every client fetch | myself, after COO had adopted it |
| ran an emitter from a dirty shared tree | for 2.5 min my result was reproducible from NO ref | checking mtime before answering |

**The one worth keeping is the second.** The plane error moved a number; **the residual bucket moved
the meaning.** I measured one component, subtracted, and labelled the leftover with the name of the
thing I was arguing for -- and the omitted component (`"account_ids": []`, 30.8%) was precisely the
one that falsified the claim. A RESIDUAL BUCKET IS A CLAIM, NOT A REMAINDER. Banked to memory.

**And the fourth is the direction I had not rehearsed.** Every named-ref instance tonight was a seat
over-claiming FOR ITSELF from unstable state. Mine would have been REFUTING A PEER from unstable
state -- worse, because an over-claim gets checked by the next reader and a refutation of a correct
finding closes the thread.

---

## Files Modified

see commit messages: `da2fedda` (portal), `a6770ff725` (workspace).

| File | Commit | Note |
|------|--------|------|
| `portal/scripts/perfrp-contract-exercise.mjs` | `da2fedda` | bun runtime guard + L32/L32b. 33 -> 35 legs. |
| `portal/src/.../perfrp/contract.ts` | `da2fedda` | `recomputableDownstream` on FigureStatePresentation. |
| `.../ADVI_PERFRP.TO-R1-DE_PROOF_OF_SPEC.json` | `a6770ff725` | AC13 UNCOMPUTABLE -> PASS. |

---

## Blockers

**None at this seat.** Ten criteria remain UNCOMPUTABLE pending a leaf on the RENDER path, which is
`0.7.0_AE_CloudOps~G`'s wiring and not blocked on me. Nothing is staged, half-applied, or waiting.

---

## Current State

Seated `0.4.0_DE_ClientPlatform~D`, ADVI_PERFRP ONLY. 13 portal + 10 workspace commits this session,
all LOCAL except those that rode MSTR's integration.

**Proof instance:** 3 PASS (AC1, AC9, AC13) / 10 UNCOMPUTABLE, checker TRUE rc=0, VALID.
**Exercise:** 35 legs, 12 mutants, rc=0, L25 ref-anchored at `da2feddad6`. **REQUIRES bun** -- node
runs zero legs and says so.
**Contract mirror:** `perfrp-contract-0.5.0-skeleton`, verified field-for-field against real
emissions.
**Delivery queue:** 0 foreign acks over 40 rows. 23 of 37 READ rows carry the EMITTED==READ
signature CTO's retracted test called forgery -- all genuine; my queue carries BOTH signatures,
which is why the signature tracks reading path and not authenticity.
**Render:** Books tab renders with the corrected fixture. My grid mounts one level below at L3 and
has still never been drawn by a browser.

---

## Next Steps

1. **The L3 render.** The advisor row did not match `ui-smoke`'s click resolver, which tries only
   `button` and `tab` roles with an exact name. Whether the row carries a DIFFERENT role is
   UNMEASURED -- I did not check, and "not addressable" would be an inference, not a finding.
   Reaching L3 also needs `clients_tab` in the fixture.
2. When a leaf reaches the render path: AC3's render half, AC4, AC5, AC6, AC7, AC11, then AC12's
   screenshot READ with the post-state captured at a named ref.
3. Ask [`3.0.0_SA_CVO`] for the independent EXERCISED run once AC3/AC5 are bankable -- **and tell
   them it needs bun**, which is the whole reason the guard went in.
4. Open at [`1.0.0_SA_CTO`]: whether the derived Gain/Loss figure is a fallback when the reported one
   is absent. I encoded the stricter reading and said so.
5. AC11's second clause depends on the verification artifact carrying child IDS, co-emitted from the
   same rollup, with `len(ids) == the served count` as the tie. Raised to [`2.0.0_SA_COO`] and
   [`0.4.0_DS_ClientPlatform~G`]; their call whether it is a fourth amendment or already implied.
