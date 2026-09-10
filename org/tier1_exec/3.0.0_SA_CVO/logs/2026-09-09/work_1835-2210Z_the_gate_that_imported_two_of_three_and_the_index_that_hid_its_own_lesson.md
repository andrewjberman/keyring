# 3.0.0_SA_CVO~Z -- work log 2026-09-09 18:35Z-22:10Z: the gate that imported two of three, and the index that hid its own lesson

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Seat:** `3.0.0_SA_CVO~Z`, site Z, PID 41724. **Prior log:** `work_1817-1835Z_*` @aed00f93d8 (merged @cc1748e24e).
**Loops:** zero crons; `/watcher` Monitor bmz64p2ig live and PROVEN CONSUMING -- it delivered six messages this
window. **Push state:** local ahead of `origin/SITEZ` `3054872f2b` (ls-remote); this seat does not push.

## Summary

The LD-0319 parity finding was accepted by `1.0.0_SA_CTO~Z`, WIDENED to both fabrics, and routed to Andrew as a
P1 open call. A law landed mid-window (`prd-manifest-gate.py`) and this seat verified it rather than reading it,
which produced a real defect and a same-window fix. Two corrections landed AGAINST this seat and both were
accepted in full. The memory index was found to be silently dropping ~70% of itself and was curated on the
operator's word.

## 1. The parity finding: accepted, widened, and validated back

`1.0.0_SA_CTO~Z` (msg 20565) accepted the finding, elevated REC 2 above REC 1, refused to self-assign into the
unseated `0.8.0_AE_CloudComp` lane, and routed ownership to Andrew. It also WIDENED it: CLOUD carries the
identical drift.

⭐ **THE WIDENING WAS RE-DERIVED HERE RATHER THAN TAKEN** -- `git show`/`git grep` against the `origin/CLOUD` ref,
a different instrument from the site-Z census (comp-find is worktree-scoped by ruling and structurally cannot
read a foreign ref). head v1.8; 8 files at v1.2; **0 at v1.8 (negative control)**. **POSITIVE CONTROL: 109,632
bytes fetched** -- a mangled ref-path returns CLEAN-EMPTY on this platform, so the v1.8 zero needed proving.

⛔ **AND THE RE-DERIVATION FOUND A GRAIN ERROR THAT CHANGES THE REMEDIATION.** Both seats read "8 files". **The
EIGHTH on both refs is `infra/system/system_parity.py` ITSELF** -- the harness, whose three hits are its own
fixtures, self-excluded by name, one of them a DELIBERATE NEGATIVE CONTROL (`"rb_stale.yaml": "adapter pinned at
rule-bank v1.1"`). The remediable surface is **7 files / 8 sites**. A remediation keyed on "8 files" rewrites the
harness's fixtures and **destroys the control that detects this drift** -- the check would then pass by having
lost its ability to fail. Sent as the RAVC close; it is the reason REC 1 must be "derive the version" and not
"search and replace".

## 2. The manifest-gate law: verified, defect found, fixed same window

`17c153a1cb` made a SURFACE MANIFEST mandatory at COMMIT time for step-4 PRDs. The message invited re-derivation.
Verified rather than accepted: census reproduced exactly (205 tracked / 8 step-4 / **0 of 8 refused**); wiring
confirmed at `safe-commit.sh:793`/`:802`; refusal exercised; import confirmed at `:103`.

⛔ **THE FINDING: the claim "the L4 and L6 refusals CANNOT DRIFT APART" held for the two IMPORTED symbols and NOT
for the third thing the gates share.** The emptiness floor was a **duplicated literal** -- `< 40` at
`prd-manifest-gate.py:107` and `to-pipeline-gate.py:1140`. Both read 40, so nothing had diverged; but the property
ASSERTED was structural and that limb did not have it. **The pieces imported cannot drift; the piece copied could.**
Two smaller limbs, both fail-CLOSED: the floor is an unmeasured constant untested at its boundary by any of the 5
controls, and the message said **EMPTY** for a real two-row table, routing a reader to "add a heading" when the
repair is "add rows".

⭐ **IT IS WS-4's AC-2 TWELVE HOURS LATER IN A DIFFERENT COSTUME** -- a property verified on the limbs it names,
with an untested limb inside the same claim. The author named the tell this seat had not: *"THE CLAIM WAS WRITTEN
FROM THE IMPLEMENTATION IT HAD JUST AUTHORED"* -- having deliberately imported two symbols, "cannot drift" felt
measured because two thirds of it was.

FIXED at `736306797e` and verified here: literal gone from BOTH (0 and 0), `MANIFEST_MIN_BODY_CHARS` named in the
PRIMARY and imported, message reworded to UNDER-POPULATED, and **two boundary controls built BY CONSTRUCTION off
the imported value** rather than hardcoding 39/41. ⭐ **The control this seat could not obtain before the fix:** a
fixture ONE ROW OVER the floor now PASSES rc=0 through the real gate. Previously I could show it refuses near the
boundary and only that it passes FAR from it -- **which is not distinguishable from a guard that refuses
everything near the boundary.**

## 3. Two corrections against this seat, both accepted in full

**(a) The law-file claim.** MSTR's CLOSE frame told five seats CLAUDE.md and XXX.md changed in the merge.
Measured false here (blob-identical; positive control 443 files / 69,847 insertions). ⛔ **But my CAUSAL
diagnosis was wrong and was declined:** I offered "a merge diff against the foreign parent reports convergent
edits as changes" -- a real trap I had hit minutes earlier -- as the explanation. **That seat ran no diff at all.**
I HAD RUN THAT DIFF MYSELF and attributed my own instrument path to another seat with no evidence any reading was
taken. A mechanism that CAN produce an observation is not evidence that it DID; the cheaper rival (no measurement)
was never tested and was true. The tell was in the frame -- it talked in PERIODS throughout. The mechanism stands,
re-homed one link upstream to explain the LAPTOP's list.

**(b) `GRADUATED`.** Asked whether the disposition implies a CVO remediation row. Measured at
`investigation_item.schema.json`: enum is 4 values; GRADUATED's only coupling is a grounding bar at `:163`; and
**`REMEDIAT` is ABSENT from the whole schema (0 hits / 226 lines)**. Answered NO -- two rows were NOT superseded.
CLAUDE.md's reserved term governs a DIFFERENT artifact's schema; two artifacts, one word, they do not touch.

## 4. The memory index was hiding its own lessons

`MEMORY.md` measured **520 entries / 111KB against a 24.4KB load cap** -- ~70% invisible, and WHICH 70% set by
insertion ORDER. ⛔ **Demonstrated live at my own cost: `cvoz-reports-to-ctoz-never-mstr` sat at line 292, in the
dead zone, and I made exactly that error this session** (the L8 send guard refused a send to `0.0.0_AB_MSTR~Z`).
A memory can be written, correct, indexed and unreachable.

Curated on the operator's explicit word: **113 lines / 17,434 bytes / 153 memories, 0 broken links** (verified),
with a header stating the full ~520 files are grep-able in the directory and that new entries must go NEAR THE
TOP. Nothing deleted from disk. ⚠ The file was CONCURRENTLY MODIFIED mid-edit -- a Write was correctly refused as
stale, and the peer's new entry (`hazard_standing is AT-SURFACING`) was folded in rather than clobbered.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `--enumerate` on comp-schedule, prd-manifest-gate, to-pipeline-gate, safe-commit, WS-4 TO, the schema | PASS | every source citation this window; found the `_fenced_lines` helper and the absent `REMEDIAT` |
| `comp-schedule` | bare + `--self-test` | 6/6 | C1 component 20->4; total 22 (the msg-20365 trap firing as predicted) |
| `prd-manifest-gate.py` | `--census`, `--self-test`, 3 hand-built fixtures | 0/8; 7/7 | the boundary pass fixture is the control the census could not give |
| `comp-find` | `'rule-bank v[0-9]' -- infra/system`; `--name 'NFRA_SYSPARITY*'` both pages | 11/173; 26/54,602 | the drift census; established SYSPARITY has no channel |
| `git` | `show`/`grep` on `origin/CLOUD`, `merge-base --is-ancestor` with negative controls, `ls-remote` | PASS | the two-fabric widening; every push-state claim |
| `safe-commit` / `safe-merge` | 1 commit in an isolated worktree, 1 drain | PASS | the guard correctly refused on a foreign MERGE_HEAD first |

**What worked:** verifying an inbound law instead of reading it -- the census reproduced, and the ONE claim that
did not was structural. Re-deriving a peer's widening on a different instrument, which is what surfaced the
eighth-file grain error. **What failed:** the causal diagnosis in §3(a), invented rather than measured. **Gap
found:** a shared constant duplicated across two files while the claim of non-divergence rested on two imported
symbols.

## Blockers

None. The parity remediation is EVENT-GATED on Andrew's open call and an unseated lane; L8/L9 is event-gated.

## Current State

- LD-0319 DRIFTED, estate-wide, accepted, with Andrew as a P1 open call. Remediable surface 7 files / 8 sites,
  `system_parity.py` NAMED AS EXCLUDED.
- prd-manifest-gate: verified, one defect found and fixed at `736306797e`, re-verified end to end.
- Inbox: 27 messages read and acked this session, every Msg-ID from its own header.
- NFRA_REPORT L9 items recorded: FWD-4's ACCEPT line is RE-CUT (grade the new text); section 7's residual is
  STRUCK and must not be graded open; RP-s-1's LEGIBILITY limb is L9's; `hazard_standing` stays ARMED on
  W2-S2/Z-S1 by append-only design -- **disposition + resolving row id is the discriminator, not hazard_standing.**

## Next Steps

- [`0.8.0_AE_CloudComp`] the 8 v1.2 sites -- DERIVE the version, do not re-copy it.
- [Andrew] the parity open call; NFRA_REPORT's naming call (Gateway / Graph / both).
- [`3.0.0_SA_CVO~Z`] L8/L9 on NFRA_OPSEC202609 and NFRA_REPORT when their rounds reach L8. Nothing before.

-- 3.0.0_SA_CVO
