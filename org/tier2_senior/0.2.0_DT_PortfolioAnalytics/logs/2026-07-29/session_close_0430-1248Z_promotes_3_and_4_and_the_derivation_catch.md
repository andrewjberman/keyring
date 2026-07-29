# 2026-07-29 — Session 0430-1248Z: promotes #3 and #4, the count-derivation catch, and two instruments that lied

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

Delta since `session_close_2343-0430Z`. Two more PROD promotes landed, closing the night at
**four promotes + the WO-3 edge flip, zero rollbacks, zero stranded legs.** The substantive
finding was not a deploy: a **third live client-side derivation on a client-facing count**,
surfaced only because two agents reported different numbers and neither folded.

---

## Deployment Sequence + Verification (DT role requirement — actual output)

```
                    PROMOTE #3                          PROMOTE #4
DEV head            42b0f524                            70166741 (carries cfc1e879)
PROD merge          763d58c2                            83afea3f
tag (PEELED)        portal-v2.1.151                     portal-v2.1.152
CI run              30423754792 success                 30425645382 success
parity gate         0 bytes (EMPTY)                     0 bytes (EMPTY)
pointer             e64d0024cb -> 42b0f524              4648327add -> 70166741
base / rollback     80e21674                            763d58c2
commits             1                                   2
held-language scan  0 hits                              0 hits
main tree after     DEV                                 DEV
```
Both: typecheck `tsc -b --noEmit` 0 errors · Step-3 PROD re-assert · FOREGROUND `bun install`
(420 pkgs; 311s / 232s) · VALGATE D-1 PASS · pre-push typecheck PASS · `worktree remove` failed
"Filename too long" (documented-acceptable) -> `worktree prune` clean.

**END STATE, measured:** `origin/PROD` = `83afea3f`, `origin/DEV` = `70166741`,
`git log origin/PROD..origin/DEV` = **EMPTY**. DEV and PROD level. CLOUD sync 0/0.
**CTO confirmed formally (124133Z) that DE's shipped queue is empty** — the two nominally-open
DE items are future work gated on a producer deploy (quarterly cells post-16:15Z) or expected to
self-clear at today's fire (carried-label text).

---

## THE CATCH: a third client-side derivation, live in PROD

**Sequence, because the sequence IS the finding:**
1. DE's announce published the promote-#3 render oracle as **"Total Holdings 7,780 / 257 unfunded"**.
2. My acceptance leg (b) says *read the count FROM THE ARTIFACT, never from the announce*. The
   served object said **`total.account_count` 7,597 · `active_accounts_count` 7,646 ·
   `excluded_unfunded_count` 49** — internally coherent (7,646 − 49 = 7,597; the 7 by_model
   cohorts sum to 7,597). **Neither announce figure appeared in the artifact.** I raised it as a
   discrepancy, explicitly NOT as a promote blocker (the deploy's own gates all passed).
3. COO measured independently, agreed with the artifact, and **corrected me**: *"the page
   field-reads the object, so whatever the object says IS what renders"* — therefore I had never
   needed the pixel I said I needed. **I accepted that without checking the code path.**
4. **COO then RETRACTED it.** DE was right: the numbers were true RENDER facts. The tile derived.
5. **I verified the retraction at source rather than accepting it on authority** (having just made
   the opposite mistake). `ModelPortfolios.tsx` @ `42b0f524` — the build I had promoted:
```js
const totalHoldingsSleeveLevel = activeDistribution?.total
  ? (activeDistribution.total.account_count ?? 0) +
    Object.entries(activeDistribution.by_model ?? {}).reduce((sum, [key, stats]) =>
      sum + (getCanonicalModelName(key) in BLEND_ARCHETYPES ? (stats.account_count ?? 0) : 0), 0)
  : 0
```
   **7,597 + 183 blend sleeve-adds = 7,780.** The unfunded footnote was a cross-artifact
   subtraction (7,854 − 7,597 = 257). @ `70166741` both become
   `const totalHoldingsDisplayed = activeDistribution?.total?.account_count ?? 0` — pure field reads.

**MY ERROR, which sits underneath both of theirs: I accepted a MECHANISM claim on authority when
I had the source in hand.** One `git show 42b0f524:src/pages/ModelPortfolios.tsx` would have
refuted COO in seconds. I wrote "accepting the correction without hedging" and called my own
reasoning wrong — in the same message where I thanked COO for catching that I trust announces
over artifacts. **The tell I ignored: COO asserted a mechanism and I treated it as a measurement.**
Rule 22 exactly: a causal claim is a hypothesis until source-confirmed, and authority does not
convert one into the other. **Standing correction for me: do not un-hedge a self-correction
without checking the claim that prompted it.**

**COO's framing, kept:** *the disagreement was the instrument.* Had DE announced 7,597 we would
all have agreed, nobody would have looked, and the derivation would still be in PROD.
**A number nobody contradicts is not a verified number.**

**Not quietly deleted:** the sleeve-level semantic (+183) is Andrew's own 2026-06-05 business
ruling. Routed to CTO for producer-side statement (e.g. `total.sleeve_level_count`), which the
page would then field-read. A business semantic implemented in the wrong layer is still a
business semantic.

---

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `git show <ref>:<path>` (source read at the promoted ref) | yes | **PASS — the authoritative instrument of this window.** Settled the derivation question that two artifact-reads and one authority-claim could not. |
| raw `curl` + `md5sum` on served URLs | yes (x8) | **PASS** — byte-identity legs held on both promotes (`31e64570` unmoved across all four; control `9bae4b42` unmoved). |
| minified-bundle marker grep | yes | **FAIL — INVALID INSTRUMENT, see below.** |
| `gh run view --json conclusion` | yes (x4) | **PASS** — never `run watch` (banked hang). |
| `git diff origin/DEV HEAD` (parity gate) | yes (x2) | **PASS** — 0 bytes both promotes. |
| comp-* tools | no | This window was deploy-execution + source reads on a known file at known refs. No estate traversal, no new resource, no IAM change — the comp-rail's own HUD did not nudge, and the questions (plan diffs, CF pins, byte-identity, a code path at a specific ref) are ones no comp-tool answers. |

**What worked:** **leg (b) — read the artifact, never the announce.** It is the entire reason the
derivation surfaced. And **pre-stating the acceptance values before the build landed**, so they
could not drift afterward.

**What failed — and this is the instrument note:** my **minified-bundle marker probe is INVALID
for local variables.** I probed the deployed chunk for `totalHoldingsSleeveLevel` (the derivation)
and `totalHoldingsDisplayed` (the field read). **BOTH returned 0 — including the one that SHOULD
have been present**, because minification renames local `const`s. Reading "derivation marker: 0"
as "derivation gone" would have been a **false PASS**; I caught it only because a positive control
rode in the same run. **The technique is VALID for object-property names and imported identifiers
(they survive minification) and INVALID for local consts.** My promote-#2/#3 probes
(`opal_aggregate_aua`, `getNonModelAumForDate`) were **accidentally** sound for exactly that
reason — property name and imported function name. Those results stand; **the technique does not
generalise.** CTO banked it verbatim ("the instrument-note of the night").

Also failed: **the verify JWT expired twice mid-promote**, each time returning 401 on every URL.
Both times the tell was **identical 36-byte bodies across two unrelated URLs** — an auth wall, not
two independent data faults. Diagnosed in seconds rather than escalated as a serve failure.

**Gap found:** the commit-message execution-vector gate (LD-0276) fired correctly on my first
promote-#3 pointer commit because the same compound command line carried a `$(` from an earlier
`curl`. Correct behavior — the gate text-matches the raw command by design. I split the command
and used `-F`. Worth knowing: **any compound line mixing a command substitution with a
`safe-commit -m` will trip it**, and the fix is to separate the steps, not to fight the gate.

---

## Current State

- **LIVE PROD:** `83afea3f`, tag `portal-v2.1.152`. Workspace pointer `4648327add` -> `70166741`.
  Portal main tree on **DEV**; CLOUD sync 0/0. **DEV == PROD, zero unpromoted commits.**
- **The Global surface now states what the artifact states**, end to end: headline
  `opal_aggregate_aua`, trend full-series field read, donut/counts field reads, Total Holdings
  `total.account_count` (**7,597**), unfunded footnote `excluded_unfunded_count` (**49**).
  **No derivation sits between artifact and render on this surface** — confirmed by source read
  at the promoted ref, not inferred.
- **Served artifact byte-unmoved across all four promotes:** `mdpf/global` md5
  `31e64570d3090eff4df3baab91d2a1dd`, 200,059 B. Non-mdpf control `9bae4b42...`, 7,234 B.
- **Distribution artifact vintage:** `period` 2026-07-28, `generated_at` 2026-07-29T00:33:16Z,
  `_provenance.written_at` 2026-07-29T00:35:21Z — current publisher batch (CTO's
  reachable-is-not-current leg, which earned its place).
- **Night's ledger:** WO-3 edge flip (router v6, ledger `20260729T0101Z` CLOSED) +
  v2.1.149 `1f363956` · v2.1.150 `80e21674` · v2.1.151 `763d58c2` · v2.1.152 `83afea3f`.
- **Standing rule now in force (CTO 052600Z):** a commit that is purely an MDPF read re-point onto
  the platinum contract keys carries a standing GO on green CI + full DT gates; anything that ADDS
  logic or touches a non-MDPF surface needs CTO's fresh word.
- **The corrected doctrine (COO, replacing its own retracted claim):** *an artifact value equals a
  rendered value ONLY where someone has read the code path and confirmed no derivation sits
  between them.* Everywhere else it is a hypothesis.

## Next Steps

- **[2.0.0_SA_COO]** D4 pixel read — still the only unread leg across all four promotes (my Edge
  automation stayed down; Andrew's own visual smoke of $1.95B + July 27th is the working oracle).
- **[1.0.0_SA_CTO]** sleeve-level `+183` producer disposition; the `platinum/` **active legacy
  writer** (underscore twins rewritten 23:47Z) as a teardown line item; the owned-paths
  merge-awareness + audit-misattribution gap from the prior window.
- **[0.4.0_DE_ClientPlatform]** quarterly-cells re-point — NEW commit + promote, gated on DS~A's
  `aum-metrics` x3 reaching platinum (post-16:15Z, CTO's word). Carried-label text expected to
  self-clear at today's fire.
- **[unowned / morning]** dangling `hotfix/global-monthly-axis-key` worktree at
  `C:/Users/AndrewBerman/Desktop/_portal_hotfix_wt` (`8fd61dbf` is in PROD, not an ancestor of DEV;
  its CONTENT is in DEV, positive-controlled — nothing was reverted).
- **[me]** IDLE, available, holding promote authority. Next promote expected post-16:15Z if the
  producer work lands.

## Blockers

**None.** Every open item is dispositioned to a named owner with evidence. The one leg I could not
close myself — the rendered pixel — is routed to COO and was labelled an inference, never a claim,
on every promote.
