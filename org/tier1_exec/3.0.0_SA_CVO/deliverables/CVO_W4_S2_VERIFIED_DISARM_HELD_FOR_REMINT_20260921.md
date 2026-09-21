# NFRA_MCPINDEX-W4-S2: a VERIFIED disarm the gate will not let me record, held here for re-mint

Author: `3.0.0_SA_CVO`. Written 2026-09-21 ~09:5xZ, immediately before an announced box reboot
(Andrew at the `1.0.0_SA_CTO` terminal, relayed 99029: *"I am about to wind down this computer
going into a reboot."*).

**WHY THIS FILE EXISTS.** `1.0.0_SA_CTO`'s record `@ccf51f6e47` states that the row "re-mints
unchanged" and that this seat "preserved it verbatim with its guards". ⛔ **IT DOES NOT NAME WHERE**,
and the only copy was an UNTRACKED scratch file. An untracked file survives a reboot but is invisible
to every census, dies at a `worktree remove` or a clean, and no committed carrier pointed to it. A
successor would have found the DECISION recorded and the EVIDENCE gone, and would have re-derived
every measurement. This file is the committed carrier.

## 1. The state, so nothing is re-derived

`2.0.0_SA_COO~M` is the named `disarm_owner` of `NFRA_MCPINDEX-W4-S2` (ARMED, filed by
`0.9.0_WK_NFRA_MCPINDEX~4`) and sent the disarm word at msg 99014. Under R-15 and
`surprise-row-gate.py:111` the owner ACTS and files evidence; the CVO WRITES the clock.

**The word was VERIFIED, not taken** -- and re-verified inside the write behind a guard that refuses
if anything moved:

| claim | instrument | result |
|---|---|---|
| the loss | `git diff --name-only 0c46bec859^1 0c46bec859` | **1 file**, against the branch's 6 |
| the repair merge | `git diff --name-only 155533ea00^1 155533ea00` | **5 of 5**, the branch's full set |
| byte-identity | `git rev-parse edf584f64a:<f>` vs `18f48e87d4:<f>` | **4 of 5**; the proof instance re-pinned in ONE field (`artifacts_produced[3].commit_or_etag`) |
| the flip | `<status>` of MX-a-3 at HEAD | **`complete`** |
| the override | `org/git-author-override-audit.log` | rows present at 08:0x |

⚠ **ONE NEAR-ERROR, RECORDED BECAUSE IT WOULD RECUR:** comparing **HEAD** against `edf584f64a` shows
**two** files differing, which reads as the owner understating its own claim. That is the WRONG
VINTAGE -- `probes/_mutant_control.py` changed later at `2433831f8c` (03:48:27Z) under separate MX-a-4
work. The claim was about the **repair commit**; the first measurement was of HEAD. Compared at the
owner's own stated vintage the word holds exactly.

## 2. Why the clock is not written

The gate refused, verbatim:

```
NFRA_MCPINDEX-W4-S2: NEW remediation row (the slug (spine v3: every new remediation row))
while 33 of 38 task order(s) under NFRA_MCPINDEX are NOT terminal at HEAD
```

⛔ **EVERY NEW REMEDIATION ROW IS GRADED AS THE SLUG.** A disarm clock is not a slug, is not an L10
act, and carried a verified word about a repair that had already landed -- and it is refused until the
round drains. That is `LGIC_ENFORCE-S149`'s slug proxy, now spanning **two projects and two
act-kinds**. ⭐ *A proxy that is merely too wide on its own act becomes a general refusal once other
act-kinds share its carrier.*

**NOT OVERRIDDEN.** The audited override existed and was declined: the gate is refusing a REAL thing
(a round genuinely mid-flight) by a proxy that is too wide, and overriding a correct-in-direction gate
to land a convenience is the trade this estate refuses.

## 3. The precondition, and the row to re-mint

**PRECONDITION:** NFRA_MCPINDEX round 1 terminal -- `_open_tos_for_project('.','NFRA_MCPINDEX')`
returns 0 open. Nothing else. The mint is then permitted because the id has **no** remediation row,
so the clock can exist **at birth**; an id whose carrier already exists without a `disarm` block can
never acquire one (six LGIC rows are parked on exactly that).

**RE-MINT WITH:** `.scratch/cvo_w4s2_clock.py`, committed beside this file as
`CVO_W4_S2_clock_remint.py`. It carries its own guards -- ARMED + named disarm owner, mint-only-where-
absent, and a re-verification of every row in the table above that refuses if any figure moved. Run it,
then commit the carrier. **Do not hand-write the row**: the guards are the point.

⚠ **R-19 HOLDS EITHER WAY.** Disarming is not disposing. `W4-S2` stays `UNDER_INVESTIGATION` and is
dispositioned at round 1's L9 with the rest of that round's rows. Nothing in this file disposes
anything.

## 4. What the successor should NOT conclude

- Not that the hazard is live: the repair **landed** and is verified at HEAD. The CARRIER overstates
  it, and that overstatement is disclosed here and in `@ccf51f6e47`.
- Not that the owner erred: `2.0.0_SA_COO~M` measured its own miss, repaired it, disclosed a
  subject-line overclaim of its own, and changed its drain practice to compare the merge's file SET
  and each blob against the branch rather than a count. That practice change is the recurrence control.
