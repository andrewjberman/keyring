# Never-widen CTO half, `1.0.0_SA_CTO~DELL1` -- CN-s-6: Global's axis drops the enumerated date 2026-10-16 (gold deploy for the 2026-10-18 13:30Z fire)

**Signed 2026-10-17 ~15:0xZ.** This half binds the COO half
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/NEVER_WIDEN_PAIR_R11_CN_S_6.md` as committed at f39392914a, sha256
`9e7b1930e0536e6a0eef0209b91c6add44f6005ec9d002d8a2806e5f310cad61`. The COO signature is the line in commit 370cd85823. Any edit to that
file voids this half; a correction travels in an addendum file.

## What I read at signing

- **Code commit 128fce3524** (one commit on the deployed pin d2f734fbac). It touches one file, `dim_mdpf_aggregate_aua_timeseries.py`, and the
  diff is exactly two changes:
  - the constant `GLOBAL_AXIS_DROP_DATES = frozenset({"2026-10-16"})`;
  - the subtraction from the union of the three legs at `dates =` inside `build_global_artifact`.
  `GLOBAL_CROSS_AXIS_EXEMPT_DATES` is unchanged at 20 dates. It also adds one test with a non-enumerated control.
- **Rules behind the outcome**, read from the producer's code (my rulings 7594 and 7600, PRD v2.29):
  - Global's axis is the union of the three legs (`:2368` at the pin);
  - `as_of_last` is `dates[-1]` (`:2860`);
  - gate (v) checks every date (`:1791-1815`);
  - dated gold keys are write-once (A8).
- **Writers:** N = 1 for Global's axis (the single `dates =` assignment) and N = 1 for Global's `as_of_last`. The per-firm `as_of_last` (L1316)
  is a different property and is untouched.

## Blast radius

- **Deploy:** the `mdpf-gold-lambda` code package and `MDPF_GOLD_COMMIT` only, by ONE targeted `safe-apply`.
- **At the fire:** only Global's four objects under `portal/gold/mdpf/global/`, and the manifest's `run.code.commit`.
- **Cannot move:**
  - any 49 Financial, Inflection or Cottonwood object (D4 gate (v): the 12 bodies are byte-equal to the reference);
  - any served dated key (write-once);
  - the emitter, the publisher, the portal and the edge.
- **One gold change per fire:** nothing else rides the 2026-10-18 13:30Z fire. That excludes S34's silver fix and the 7-day re-pull.

## Both branches, as the COO half states them (section 2)

- **Branch 1.** 49F and Inflection carry a value date after 2026-10-15 at the fire. Global emits under a NEW dated key with `as_of_last` set to
  that date, and CN-s-1's V2 leaf set reaches Global.
- **Branch 2, the likely one.** 10-16 is never filled (msg 6986), and the next 49F trading date is Monday 10-19, so the legs still end at
  2026-10-15. Global emits with no error, and the 2026-10-15 key write is a `conflict`. Nothing served at Global moves, and the served Global
  stays the 10-16 fire's 2026-10-15 object. CN-s-1's Global grade waits for the first fire whose Global `as_of` is a new date.
- **Either branch:** `errors` empty and `a4_objects_built` 16 are the floor. The manifest's per-key Global write statuses name the branch.

## Conditions of this signature

1. **D4 is the go/no-go.** Its six gates (COO half section 3, (i) to (vi)) must all pass on the DEPLOYED function, with no write.
   - The D4 dry run, not the offline build, grades the headline.
   - If any gate fails, the result is D4-STOP: D2 is rolled back at once, and the live function stays at d2f734fbac.
2. **Window:** D2 and D4-new finish by 2026-10-18 12:44Z. If they do not, the pair takes the next fire.
3. **Rollback:** `MDPF_GOLD_COMMIT` goes back to d2f734fbac, the package goes back to the VersionId recorded in (a), and `CodeSha256` goes
   back to `fAXZ4gdLPspZepxmR9J8l3BfJROkppYOyf3qC2dAd40=`, by a targeted `safe-apply`, read back. A bad object is never answered by a delete.
4. **NEVER-2:** the ledger entry is opened before (a). Its close is COMMITTED. Every live worktree is read at the drain.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
