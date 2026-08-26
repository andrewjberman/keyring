# /spot-check 1725Z — 3.0.0_SA_CVO

**Cycle:** ad-hoc, one pass, NO cron armed (LD-0164; prompt.md BASE lane "arm ZERO crons, NO exception").
**Checkpoint in:** `bb1c1899a6` @2026-07-28T09:10:19-04:00 — **29 days stale, 7,876 commits.**
**Checkpoint out:** `2682f60044`.

---

## SCOPE BOUNDARY — read this before treating the checkpoint advance as coverage

The 7,876-commit delta was **NOT** ground per-commit. Precedent is this file's own history:
`bdfbe944d4` (2026-07-06) ruled a 3,130-commit gap a **checkpoint-hygiene artifact, not un-verified
backlog** — interim CVO sessions had covered the period and a per-commit grind was disproportionate.
Same reasoning, higher magnitude.

**What was actually swept:** today's 149 commits on `origin/CLOUD` (since 2026-08-26T00:00Z),
filtered per SKILL 2c to alignment-metadata surfaces → **5 commits**.
**The other 7,727 commits are NOT claimed as verified by this cycle.** Stated because a bare
checkpoint advance otherwise silently asserts coverage that was not performed.

---

## FINDING 1 (P1, routed) — REGISTRY.md is missing 5 of 20 ACTIVE projects

Entered from `944ca89492` (`register(D11 SUBSTRATE ANALYSIS + NFRA_SUBSTRATECARDING)`) and nearly
filed as a one-off registration miss. **The positive control killed that reading.**

| | |
|---|---|
| ACTIVE project JSONs | **20** |
| ACTIVE but ABSENT from `org/projects/REGISTRY.md` | **5** |
| Absent | `MDPF_COTREMEDIATION` · `NFRA_COMPTOOLS` · `NFRA_DEPLOYLEDGER` · `NFRA_SUBSTRATECARDING` · `OPAL_ADVIPOINTERS` |
| Positive control (present by the same test) | `D1_CATVIEWS` · `ADVI_PERFRP` · `ETFS_POSITIONING` |

`NFRA_SUBSTRATECARDING` is `status: active` and claimed by `D11` in `org/missions/DIRECTIVES.yaml:440`,
so it is live by the Rule 25 membership test and still has no row.

**The reading that matters:** not "the D11 registration skipped a step." `MDPF_COTREMEDIATION` is the
most-worked project in the fabric today and `NFRA_COMPTOOLS` had a lane on it all afternoon — both
absent. A 25% coverage gap in the registry, with the day's hottest project among the omissions.

**WHY unmeasured:** whether these were never added, added-and-removed, or deliberately tracked
elsewhere is **NOT established** and is not guessed at here.

**NOT FIXED — routed.** REGISTRY.md row drift is nominally in the /spot-check fix scope, but five rows
across five projects this seat does not own is a content act, not alignment-metadata hygiene. The
owned-paths lane has refused non-owner author lines on the register before (`590eab4fa7` records the
gate refusing even MSTR's). Routed to `2.0.0_SA_COO` + `0.0.0_AB_MSTR` per the charter's
owned-paths-block pattern rather than reaching for `--force`. Msg 72712/72713.

---

## FINDING 2 (skill-record defect, no owner action needed from others)

`.claude/skills/spot-check/SKILL.md` **contradicts itself on the default invocation.** Its Step-1
table says bare `/spot-check` arms a 20m cron; its own description field says bare = one cycle, no
cron, per **LD-0164**. `prompt.md` BASE lane and the XXX.md Step 1b-F CVO row both say **zero crons,
no exception**.

Resolved in favour of LD-0164 + prompt + XXX row (three carriers against one stale table): **one cycle
run, no cron armed.** Recorded so the next CVO session reading the table alone does not arm a cron
that three ratified carriers forbid.

---

## VERIFICATION DISCHARGED THIS SESSION (not /spot-check scope, logged for continuity)

- **`ec3639cad5`** (`0.4.0_DT_ClientPlatform~C`, deploy_ledger population fix) — **VERIFIED both
  directions.** The author's controls all ran the WIDENING direction; the **narrowing** direction was
  untested and was the only one that could have made the fix a regression. Measured: old glob
  `*_deploy_completion.md` = **429**; dropped by the new content filter = **2**; both explicitly
  `CLOSED` and skipped as terminal under the old reader too → outcome byte-identical, **no
  regression**, 427 unchanged. `551 → 122` and `483/68` reproduced exactly on an independent
  instrument. Msg 72655/72656/72657.
- **`74 → 2 → 1`** — all five "closed in substance" entries read in full, not counted; COO's
  further correction confirmed at its named target (`20260622T1650Z_cotetl-c00snapshot-servedaua_deploy_completion.md`
  = `CLOSED — nothing stranded — closed 20260622T165318Z`, 5/5 legs each carrying its own proof).
  Nothing in the estate is half-deployed on this axis.
- **Grain flag:** the `74` recomputes to **65** under the FIXED predicates. **Not drift** — 74 was
  measured with the pre-fix reader and the fixes exist to recognise closure it could not parse.
- **Own finding, adopted:** 3 of 6 record defects are ONE missing-vocabulary shape (apply-complete +
  verify-leg-pending under a different owner). `2.0.0_SA_COO` ruled it `HELD-VERIFY-PENDING`
  @`be7d73eb2a` and the census found **six** independent coinages, not three — a wider result than
  this seat's.
- **Push-state convention:** 4 of 4 commits reported "landed LOCAL (ls-remote not read)" were measured
  **ON ORIGIN** against the true tip `4e8aa3b5f9`. The honest caveat was carrying a wrong default.
  Msg 72664–72667.
- **A9 / MDPF bundle:** `0.4.0_DS_ClientPlatform~T`'s blocker CONFIRMED independently at source
  (`build_package.py` bakes the pair script) and on the applied plane (lambda LastModified
  **15:29:34Z** vs commit **17:12:28Z**, gap 1h42m54s). **Widened:** the running bundle sits at
  ephemeral minimal pin `48c473caa1` and **four** commits across **two** lanes are outside it; the
  bake list carries **18 .py, 16 from gold/silver trees**, so sixteen files share the dual-artifact
  property. Option (c)'s predicted failure mode is priced on the cottonwood limb only. Msg 72705–72708.

---

## Instrument note

`comp-pipescript deployed` = MATCH is **TRUE and SILENT about the lambda** — it reads the S3 code
tree; the lambda executes the bundle; different artifacts. Rule 22a's DESIGNED half: no way of calling
the instrument differently fixes it. Blast radius = the 16 baked gold/silver scripts.

**Compiler tools this cycle:** `comp-which` exercised at startup (A.3 probe — a forwarder RAN, not
merely resolved; 105 of 105 resolve bare). The census work used direct filesystem/git probes
deliberately: Rule 22 requires re-deriving with a DIFFERENT instrument than the one under test, and
`deploy_ledger.py`'s own predicates were the subject.
