# /self-drive D11 — ticks 25-26 · FIVE MORE REWORKS, A CVO VERDICT THAT UNBLOCKED L3, AND A 42x4 GAP THE FIVE-STEP SEQUENCE WAS SILENT ABOUT

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP (guard PASS, basis: workspace path) · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 08:50Z–09:30Z

---

## SCOPE

```
D11 "Substrate Analysis"   denominator: 1 of 12 live directives   flags: []
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 2
  claimed-not-member sweep: 1 claim over 337 project JSONs -- already a register member. No lag.
```

## 1. CALLS + VERDICT — THE LOOP'S OWN CYCLE, CLOSED IN FOUR MINUTES

| | |
|---|---|
| PITCHED | 1 ADJUDICABLE to `3.0.0_SA_CVO~X` (msg 75226) · **0 RESERVED** |
| VERDICT | **75229 — (a): D11 AUTHORIZES declaring the bridge relations, as L3's own deliverable** |
| RECORDED | PRD §7/§7a + project JSON `phase`+`blocking` `@604f0a1a0c`, on origin |

**Operative sentence, quoted not paraphrased:** *"The PRD defines L3 AS the fusion, L1 measured the
bridges absent, so declining to declare them is declining to DO L3 — which would contradict the
sovereign arc word while wearing restraint's costume."*

⛔ **THEIR REASONING ON *WHY NOT RESERVED* IS BETTER THAN MY PITCH'S.** Andrew's arc word `74754`
already settles AUTHORITY; only the build-vs-repair LINE needed a second seat. **Sending the
authority question to Andrew would have been re-asking a settled thing** — the shape I have spent
the night correcting in other seats.

**Four conditions bind any L3 decomp**, and two of them do work I did not do:
- **Condition 1 (D11-owned registry only) is what keeps my `#9` NAMED-GAP ruling STANDING rather
  than silently overturned.** A careless (a) would have made qualify-do-not-fix depend on which
  finding was more interesting.
- **Condition 4 preserves the (b) answer's true half**, which I had not seen: a bridge that cannot
  be declared without store-side changes is a named gap for the store's owner. **The arc proceeds on
  the declarable bridges and names the rest — rather than stalling whole or building wide.**

## 2. ⛔ FIVE REWORKS. THE ADVERSARY FOUND SOMETHING ON EVERY COMMIT I MADE

| pass | what my validator ACCEPTED | commit |
|---|---|---|
| 5 | `pattern_source_home = "p.py\n"` — **`$` matches BEFORE a final newline**, so `^\S+$` accepted whitespace | `6702f0f4f1` |
| 5 | the `basis` enum had **no definitions**, so its MECE claim was uncheckable | `6702f0f4f1` |
| 6 | `https://`, `file://`, `ftp://` as a **repo path** | `7407a41ed3` |
| 6 | the three DECLARED branches held **inline enums, not the vocabulary** | `7407a41ed3` |
| pre-commit | I fixed a local-copy defect by **writing the same guard three times** | `f5f94d63a3` |

>> **THE PRE-COMMIT FINDING IS THE SHARPEST.** rework8 replaced three inline `basis` enums with
`$ref`s *because a rule applied by copy cannot move when the rule moves* — **and in the same edit I
added an identical URI-scheme guard at three sites by copy. The lesson and the violation shipped
together.** <<

**Two things I did right and will keep doing:**
- **Reproduced CRO~A's finding as a BASELINE before editing.** Removing `held` from `basis_present`
  left grain/key/failure_mode **unmoved at 0 errors** and moved only `member_set` — 3 of 4 sites did
  not follow the vocabulary, inside a field whose `x-rule24` asserts *"one estate vocabulary, not a
  local copy."* **My claim was in the artifact, in my words, and it was false.**
- **Proved the fix by mutation, not assertion.** Deleting the scheme rule from `$defs/repo_relative_path`
  makes BOTH bound sites accept `https://`. A copy could not have done that.

**And my own control harness typed its denominator** — printed "26 of 27" when 26 tests ran, inside
the commit that refuses stored derivable values in three schema fields. Harness now derives it.

## 3. FOUR POLICY CALLS RULED — AND ONE ENUM VALUE WAS A SECOND AXIS

```
  Q1 absolute / traversal paths      REJECTED — a manifest is read on BOTH fabrics
  Q2 fixed literal family pattern    NO — the PLACEHOLDER IS THE NON-ENUMERABILITY
  Q3 iceberg triple as db_path       MOOT, dissolved by Q4
  Q4 one file as BOTH repo_path
     and db_path                     ⛔ IT CAN, AND THAT IS THE DEFECT
```

⛔ **`db_path` IS SYNTACTICALLY IDENTICAL TO `repo_path`.** It distinguished what the artifact IS
from how its address PARSES — a **second axis inside a one-axis enum**, in a field whose own
`x-rule24` says the axis is *"HOW to parse and normalise `home`."* `part_class` already carries role.
**REMOVED.** `4.0.0_SA_CRO~A` found it by asking whether one file could be both. **I had enumerated
the address shapes I had seen, and one of them was not an address shape.**

**Residual ruled, not hidden:** `a.b.c` is indistinguishable from an iceberg triple. **The producer
DECLARES `home_space`; the schema checks COHERENCE and does not INFER.** A pattern claiming to
discriminate them would guess, and guess silently.

## 4. ⛔ ACCEPTING THE STEP-4 ADDENDUM EXPOSED A GAP NOBODY HAD SCOPED

```
  DENOMINATOR: 42 parts
    grain / key / failure_mode / home_space   present on   0 of 42   EACH
    parts step 4 would REJECT today                       42 of 42
    rows step 2 as scoped touches                          3
```

**Step 2 moves three rows. Step 4 requires forty-two rows to carry four receivers each. Nothing in
the five-step sequence produces the other 39 × 4.** It is the window defect a **third** time, one
artifact further along: step 4's `required` would reject the very manifest the rerun was run to make.

**RULED (contract owner):** step 4 is conditional on a **measured gate — `42 of 42` read off the
EMITTED manifest, denominator printed** — not on the rerun having happened. Short of that, the
compatibility wording stays with a **new named expiry** rather than quietly persisting.

⚠ **AND THE HONEST READ:** the receivers exist because the PRD said L1 needs the manifest to NAME
the grains, keys and failure modes. **They are named on 0 of 42.** L1 delivered anyway by measuring
the substrates directly — **the consumer routed around the contract, so the contract's emptiness
never fired.**

## 5. DOCTRINE LANDED — principle 17 / instance I-15 `@125a0b0774`

`INSTRUMENTS_AND_AXES.md` principle 17 (+17a/b/c) and CHECK item 8; instance **I-15**. No new file —
that file already carries the axis principles. Cost and non-application both stated in the file.

⛔ **I NEARLY MIS-ID'D IT: numbered `I-17` to match principle 17.** The instance ids run
**sequentially 1..14** and the `(doctrine §n)` tags are a **stale pre-split numbering** — I-14 maps
to §8. Corrected by reading the id column instead of inferring it from the number I had just
written. **A name is not an identity — inside the commit whose subject is that instruments must be
opened rather than assumed.** `4.0.0_SA_CRO~A` validated it at the bytes, not the message.

## 6. WHAT OTHER LANES FOUND, RECORDED BECAUSE IT IS BETTER THAN MINE

- **`0.4.0_DT_ClientPlatform~X`, falsifier 2 HIT:** `PLANE` was never defined, and the reading a
  reader would take (`layer`) **REFUTES the declaration** — found by running a falsifier they had
  declared and could have left declared, after a verification that legitimately could not reach it.
  **A declared-but-unrun falsifier is a promise, not a control.**
- **Same lane, F3:** reproduced *my own* zero-join mechanism from the other end, different
  instrument, different question. **That is corroboration rather than repetition** — the POSITIVE
  case of principle 17.
- **Same lane, the withdrawn 6:** *"A comment calling 6 withdrawn does not stop the generator from
  publishing it."* And `_objects` DELETED — **a total spanning a family of undefined cardinality is
  a number the estate does not have.**
- **`0.0.0_AB_MSTR`:** third wrong-population instrument, twice against the same lane. *"Outbound
  messages"* read as *outbound TO ME* — **a seat routing findings to the seat that needs them goes
  silent in the observer's inbox while working at full rate.** They withdrew an uncalibrated CPU
  instrument rather than leave a plausible number in the record.

## COMPLETION TEST

**NOT DONE — 0 of 1 projects complete.** **REACHABLE 1 / UNREACHABLE 0.**

**HOLDS, both named, NEITHER MINE TO LIFT:** the L0 generator rerun (`4.0.0_SA_CRO~A`), and behind
it step 4 — `part.basis` → `basis_present`, `parts_registered` removed, four fields added to
`required`, compatibility wording retired — **ONE atomic commit AFTER the rerun**.

## RESERVED — AT ANDREW: **ZERO**

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; the `org/XXX.md` edit is a
law-file edit held under Andrew's standing instruction.

## Compiler Tools

`jsonschema` Draft202012 `check_schema` + the live 42-part manifest as a positive control on every
pass · hand-built mutant sets written **against the defect an adversary named, never the one I
imagined** (12 / 26 / 24 / 29 cases, **denominators DERIVED after the harness typed one**) ·
**schema mutation** (delete a `$defs` rule, re-validate both sites) as the binding-vs-copy oracle ·
**empirical terminator sweep** (LF/CRLF/CR/TAB/SPACE against each anchored pattern) after a
text-predicate sweep missed 1 of 5 · `git show <ref>:<path> | grep -c '"field":'` as the
write-vs-comment discriminator with the parent commit as a firing negative control ·
`git ls-remote` + `merge-base --is-ancestor` for push state, never a default ·
`.tools/directives-check.py --json` · `.tools/safe-commit.sh -F` with Write-authored message files ·
`ack_messages` for the READ clock (**62 recorded across this window**).

**state: ARMED** · next tick :17
