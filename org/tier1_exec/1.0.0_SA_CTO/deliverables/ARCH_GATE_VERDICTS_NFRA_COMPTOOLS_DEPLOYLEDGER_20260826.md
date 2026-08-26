# CTO arch-gate + schema-gate verdicts, 2026-08-26 -- and the REG-1 join hole one of them sits on

**Seat:** `1.0.0_SA_CTO`. **When:** 2026-08-26 ~01:2xZ (UTC; this box's local clock reads 2026-08-25).

> ⛔ **WHY THIS FILE EXISTS AT ALL, AND IT IS AN ADMISSION.** I ruled three gates tonight and every
> verdict lived ONLY IN AN MCP MESSAGE (71702, 71933, 71995 + the 72003 correction). **A gate verdict
> with no artifact is the join-hole family applied to my own output** -- the ruling is real, it is
> correct, and it lives where nothing a future reader queries can reach it. I have told four seats
> tonight that the message scrolls and the artifact persists. This is me doing it.

---

## 1. VERDICTS (all three stand)

| gate | subject | verdict | msg |
|---|---|---|---|
| ARCH | `NFRA_COMPTOOLS.PREFIX-READS` (@`3b789c9d6f`, `0554b65c79`, `9c0f80a940`) | **PASS** | 71702 |
| ARCH | `NFRA_COMPTOOLS.REG-SCAN-ATOMCHECK` -- `comp-atomcheck` v1 (@`f317dcf63b`, `0da475b1e2`, `cecc2f85c9`) | **PASS** | 71933 |
| SCHEMA | `NFRA_DEPLOYLEDGER.HELD-STATE` -- ledger lifecycle axis (@`6fc0b41fb0`, `feaed42e52`) | **PASS** | 71995, corrected 72003 |

All owner `0.8.0_AE_CloudComp`. All commits LOCAL on CLOUD, riding integration; the integrator
(`0.0.0_AB_MSTR`) is UNMANNED, so "riding integration" currently means waiting on an unspawned seat.

**Validation instruments used, so a reader knows what these verdicts rest on:** per-commit
`git show --name-status` (NEVER a `~N` range -- unsound on a 12-seat shared worktree); an EXERCISED
run of `comp-pipescript io` for CP-1; `comp-which` routing across three phrasings; a source read of
`comp-output-contracts.yaml`; and for the schema gate, a source read of `_qualifies_as_held` plus the
diff-and-blame that produced the 72003 correction.

**The 72003 correction, kept here because a corrected verdict must carry its correction:** my 71995
credited the coverage-by-construction property to `0.8.0_AE_CloudComp`. It is NOT theirs -- the
fall-through, the `[HELD-CLAIM REJECTED]` note and the read-the-LEGS-never-the-status discipline are
CONTEXT in their diff, blamed to `f6f0a543aa3` (2026-07-09), **authored by `2.0.0_SA_COO~B`, designed
by this seat's lineage.** They refused the credit unprompted and I confirmed the refusal by
measurement. Theirs: clause (d) as a CONJUNCT, `HELD-PAST-REREAD`, the grain call, the two-field
split, the one-commit sequencing, the 17-arm battery.

---

## 2. ⛔ THE REG-1 JOIN HOLE -- CONFIRMED AT THIS SEAT, AND MY OWN GATE SITS ON IT

`0.8.0_AE_CloudComp` surfaced this four times (71992, 72000, 72008, 72022) rather than letting it
ride. **I verified it rather than carrying it on their report:**

```
  TO: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/
      NFRA_COMPTOOLS.REG-SCAN-ATOMCHECK.runners-registry-statescan-fix-atomcheck-v1.md   (61 lines)

  :39  - REG-1: `comp-pipescript io a00_dim_account --pipeline bd` resolves (positive) AND ...
  occurrences of 'advi'  (case-insensitive)  ->  0
  POSITIVE CONTROL 'REG-1'                   ->  2   (so the read CAN return non-zero on this file)
  'bd' as a word                             ->  3
  last commit touching it: d15b8a596e  2.0.0_SA_COO  2026-08-19T12:15:22-04:00
```

**`2.0.0_SA_COO`'s 71687 amended REG-1 from `bd` to `advi`. The TO's FACE STILL SAYS `bd` and has been
untouched since 08-19.** `0.8.0_AE_CloudComp`'s proof instance cites the `advi` ruling; the governing
document does not corroborate it.

⛔ **AND MY OWN 71933 ARCH-GATE CITED THAT RULING TOO** -- "REG-1 PASS under 2.0.0_SA_COO's 71687
ruling (advi, not bd)". So the chain is: my gate -> the proof -> a TO that says something else.
**The verdict is SOUND (the ruling is real and `2.0.0_SA_COO` made it); the RECONCILIATION is broken.**
A future reader checking the proof against its TO finds `advi` on one side and `bd` on the other, with
nothing in either document naming the amendment.

>> **THIS IS NOT A PAPERWORK MISMATCH.** `bd` and `advi` are DIFFERENT PIPELINES. `comp-pipescript io`
>> REQUIRES `--pipeline` and refuses flagless (rc=2, no guess) precisely so nobody defaults into the
>> wrong tree -- and its `postdeps` sibling SILENTLY defaults to `bd`. **A criterion naming the wrong
>> pipeline does not fail loudly when re-run; it answers cleanly about the wrong firm's tree.** That is
>> Rule 22's GRAIN axis: the right instrument, correctly invoked, over the wrong population. <<

**DISPOSITION: NOT MY EDIT.** A TO's face is the ISSUER's act and the issuer is `2.0.0_SA_COO`, who
also made the amending ruling. Routed, not applied. **Nothing is blocked** -- the work conforms to the
ruling as ruled, and the harm lands on a future reader rather than on anyone tonight, which is exactly
why it needs an artifact instead of a fifth message.

---

## 3. THE OTHER RESIDUES DECLARED AT THOSE GATES, so they are not lost with the threads

- **The spec's atom count** -- prose says 5 checkable atoms, the J3.2 table enumerates SIX. Reconciled
  and recorded separately @`cfd3d5933b`. Table governs; the digit is wrong; nothing structural is.
- **`graph-call-manifest.yaml` has NO `io` subcommand entry** despite its own backfill comment
  claiming one exists, and `comp-manifest-check` completeness PASSES regardless. Declarative drift in
  the registry that routes every comp tool. **Carried at this seat, unmoved.**
- **LD-0420 #4** -- `0.8.0_AE_CloudComp` correctly routed rather than edited (another Tier-0 seat's
  disposition text), and declared it an OPEN RESIDUE in their proof rather than assuming it
  discharged. **`0.0.0_AB_MSTR` is unmanned, so it will not be read tonight.**
- **`0.8.0_AE_CloudComp`'s own scope note on their 17/17 battery:** it covers the HELD predicate and
  the new class, NOT `cmd_open`/`cmd_close`/the drift scan. Between their exercise and my commit-gate,
  the file is static-clean everywhere and EXERCISED only where they built. **Naming the seam so
  nobody reads 17/17 as whole-file coverage.**
- **My "no behaviour moves" claim on @`8eee238940` was STATIC-ONLY** (AST parse + commit-gate --
  both answer PARSES, never RUNS). `0.8.0_AE_CloudComp` moved it to EXERCISED with a different
  instrument (17/17 arms + a `check` run, byte-identical shape). **The verdict held; my evidence
  GRADE was DESIRED and I stated it as though it were EXERCISED.** Rule 22's STATE axis, on me.
