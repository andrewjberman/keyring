# 0.4.0_DE_ClientPlatform~Z -- 2026-08-28 21:30-22:30Z -- D1_CATVIEWS D-3 + D-4 RENDER DEFECTS

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Fresh seat (predecessor's session ended; no orphan watcher existed, registration was absent). Seated
on Andrew's singular-priority D1_CATVIEWS directive. Rule 27 project: `D1_CATVIEWS`, one project.
**Scope was re-cut TWICE by the issuer while I worked** -- MEASURE -> FIX(D-1,D-3,D-4) ->
FIX(D-3,D-4) -- and the second re-cut was caused by a measurement I made.

---

## Commits

| hash | repo/branch | what |
|---|---|---|
| `db3df0b2` | portal / DEV | feat(D1_CATVIEWS.D-3/D-4): canonical L2 member colour + delete the fee-split panel |

PUSH STATE, MEASURED by `git ls-remote origin DEV` at ~22:1xZ: **LOCAL**. origin/DEV reads
`4dde6df344`; exactly **1 unpushed commit**; clean fast-forward (the tree was measured identical to
origin/DEV before I started, so the overlap set is empty). Push routed to `0.0.0_AB_MSTR~Z`
(LD-0367). **That ls-remote read is perishable -- re-measure at the act.**

---

## OK: THE MEASUREMENT THAT RE-CUT MY OWN TO -- D-1 WAS NEVER RENDER-SIDE

I was dispatched (14112) to FIX D-1 (L2 rows showing `--`), with the diagnosis handed to me as
settled: *"THE PRODUCER IS CORRECT AND COMPLETE. D-1 IS RENDER-SIDE. DO NOT TOUCH THE PRODUCER."*
That diagnosis rested on a conservation check over the `qa_return_bodies` capture -- sound
arithmetic, real control, and **about a different object than the one on screen.**

```
  git show bc9d11dd8e:<CVO edge-captured baseline>/category-views.<scope>.json
  scope         L2 members   VALUE  NULL  ZERO  ABSENT-KEY   any_mapped
  49financial       15         0     0     0        15         False
  global            15         0     0     0        15         False
  cottonwood        15         0     0     0        15         False
  inflection        15         0     0     0        15         False
  TOTAL             60         0     0     0        60         False
```

**Not one served member carries an `aum` key at any scope.** `L2Members:224` tests
`m.aum !== undefined`, gets `undefined`, and prints `--` correctly. The QA capture is the FIXED
code's output; the page reads the SERVED object written earlier by the PREVIOUS code.
**A correct measurement of the wrong artifact** -- the same "deployed bytes has two referents" class
that had already bitten twice tonight, one rung further out.

`2.0.0_SA_COO~Z` reached the same conclusion independently and in parallel (14164, measured `global`,
9 members). Mine covered 60 members over 4 scopes off a *different* artifact, so I routed it as
**corroboration rather than repetition** and said which was which. D-1 moved to the reland lane.

---

## WARN: THE CATCH THAT MATTERED MORE -- AN ACCEPTANCE CRITERION THAT COULD ONLY BE MET BY A REGRESSION

After D-1 was reclassified, the issuer kept a criterion (`CATV-TOF1-AC2`) asserting *"exactly one is a
genuine `None` ... **that one must still render `--`**. The renderer already does this correctly."*
**It does not, and that is the code being RIGHT.**

```
  L2Members:198   const members = visibleConstituents(row.members ?? [])   <- THE GATE, runs FIRST
  :135-139        anyMapped = items.some(aum != null)   TODAY false -> nothing suppressed -> all dash
                  return items.filter(aum != null && aum !== 0)
                  POST-RELAND anyMapped TRUE (8 of 9) -> members[0] IS REMOVED, NOT DASHED
```

`:224`'s dash is only ever reached by members that already survived `:198`. **Today's dashes look
like the null convention but are the suppressor lying dormant.** And the deletion is Andrew's own
overrule, quoted verbatim in the file at `:112-113` (*"A null is a 0 in this case"*).

EXERCISED, not argued -- my lane's scorer, `--self-test` rc=0, ARM 3:
`subject NULL not 0 (overrule) -> ABSENT@G5, expected ABSENT@G5, OK`.

>> **So the criterion could only have been satisfied by REVERSING A SOVEREIGN RULING.** I surfaced
   with two coherent repairs and a recommendation, adjudicated neither, and touched neither `:224`
   (forbidden, and not the gate anyway) nor `:135-139` (reversing Andrew is not mine).
   `1.0.0_SA_CTO~Z` ruled (a) in 14177; `2.0.0_SA_COO~Z` re-cut in 14185. **An instrument built two
   hours earlier for a different question is what falsified the criterion.**

---

## What shipped

**D-3 -- the defect was an OPT-OUT, not an inconsistency.** `getModelColor` is the estate's model
colour system; 11 files call it, including the Portfolio Analytics panels Andrew was comparing
against. `CategoryViewTree` called it **zero** times and indexed a local 5-colour palette, so an L2
member's colour was decided by its POSITION. The fix is a call, not a palette:
`getModelColor(getCanonicalModelName(name))`.

**L1 BUCKET rows left positional, deliberately.** `Primary`/`Custom`/`ETF|ALT Strategies` are buckets,
not model portfolios; no canonical colour for them exists, so name-keying them would mean *inventing*
a palette -- barred by 14112 s.3. Refusing the wider fix was confirmed correct (14282 s.1).

**The pin, and why the hash was not left alone.** `Fixed Income` is now a declared entry at `#8b5cf6`
with `Opal Fixed Income` aliased to it. Before, it fell through to `EXTENDED_MODEL_COLORS[hash % 6]`
= index 0 = the identical `#8b5cf6` -- so **the pin preserves rather than repaints, measured on both
sides.** Pinning was still required because the hash keys on the STRING: `'Opal Fixed Income'` hashes
to index 4 (`#d946ef`) and **collides with `'Opal Global All Equity Total Return'` in the SAME card**,
so a producer rename would silently repaint a canonical model into a collision.

**D-4 -- the fee-split panel is gone from the DOM.** `PredicateUnavailable` and its render site
deleted. **The diagnostic it carried is preserved**: that component did two jobs -- advisor copy
(deleted, Andrew's call) and a `predicate_reason` console.warn (kept, moved into `CategoryCard`).

**The D-4 second-order effect, measured not guessed.** The issuer flagged "at least one scope" would
render an empty titled card. It is **exactly 2 of 4**: `global` and `cottonwood` Client
(predicate unavailable, $290.4M / $294.9M, `children: {}`); 49financial and inflection are untouched.
The `!unavailable` guard came off the observational line so those cards say something true instead of
nothing. **The headline-figure decision I did NOT take and routed instead** -- see Blockers.

---

## Compiler Tools

- `comp-find 'CATVP-d-1' --corpus raw` -> the decomp rectangle; `comp-find 'L1Bar' --corpus raw
  --files` -> the single render surface (2 DEF hits, one a `.runtmp` promote snapshot -- I read the
  live tree, not the snapshot). `comp-find 'categoryChildrenForDisplay'`, `'SMA_BUCKETS'`,
  `'Fixed Income'`, `'ASSET_CLASS'`, `'CATV-TOF1'` for the accessor, producer, palette and TO face.
  Denominators printed by the tool on every run (~273k files scanned).
- `comp-find 'bc9d11dd8e' --band DEF` to recover the scorer's `BASELINE_DIR` **after my first guess
  at that path returned `git rc=128`**. Worth recording: rc=128 is "path absent in that commit", NOT
  a clean zero -- had it come back empty I would have read absence and moved my search.
- Rule 21 note: the new T1 (raw `grep`/`find` in Bash denied, relayed as law in 13973) landed
  mid-session. **The enforcing hook is not on this device**, so nothing refused me; I complied with
  the rule rather than the gate from the point I read it, and routed searches through `comp-find`.

---

## Blockers

**None blocking this lane's landing.** One decision is ROUTED AND OPEN, and it is the only thing
between `CATV-TOF1-AC5` and PASS:

- [`2.0.0_SA_COO~Z`] **The Client headline figure on a predicate-unavailable node.** Deleting the fee
  box removes the headline gate's ONLY stated rationale (`:287-301` -- the contradiction between a
  figure and a panel calling it unavailable). So (A) restore the figure is now coherent; (B) keep it
  suppressed is what shipped; (C) drop the card is rejected (hides ~$290M from an advisor).
  **My rec is (A), CONDITIONAL on that office confirming the held-node residual (its own 13544 s.4
  item) is trustworthy** -- turning an unverified residual into a client-facing dollar figure is not
  a renderer's call. **One word lands it; (A) is a one-line change.**
  `3.0.0_SA_CVO~Z` 14283 s.3 confirmed it scores the routing-and-answer, never the merits.

---

## Current State (written for zero prior context)

`D1_CATVIEWS.TO-F1-DE` carried 5 criteria. **AC3 (D-3) and AC4 (D-4) are PASS**, both read on the
rendered page, and AC3 was independently scored PASS by `3.0.0_SA_CVO~Z` (14283 s.1). **AC1 is
N/A** -- struck by the issuer on my own measurement. **AC2 is UNCOMPUTABLE by its own terms**
("score AFTER the reland") and belongs to the post-refire verification pass. **AC5 is UNCOMPUTABLE
pending the routed answer above.** Proof-of-spec instance filed and `proof-of-spec-check` returns
**VALID, 0 violations**, coverage 5/5, alignment closed in both directions.

Verification actually performed: `bun run typecheck` (`tsc -b --noEmit`) rc=0, and **proven failable
first** -- injected mutant returned rc=2 `TS2322` at the exact line, restore returned rc=0 with the
file byte-identical (33750 both sides). Two scopes rendered via `ui-smoke` against the committed
fixture and **the screenshots were READ**, then **re-rendered from the committed state** as the
determinism control. `.tools/commit-gate.sh` printed `checked 0 of 2 file(s) -- NOTHING WAS CHECKED`
and says outright not to cite it for a frontend artifact; **I am not citing it.**

`1.0.0_SA_CTO~Z` 14282 declared Andrew's gate (*"yes reland once all fixes are in"*) DISCHARGED on
this commit, and the chain is running: push -> reland -> floor -> publisher -> promote -> verify.

---

## Next Steps

- [`0.0.0_AB_MSTR~Z`] Push `db3df0b2` to `origin/DEV`. Integrator-only; DT cannot.
- [`2.0.0_SA_COO~Z`] The AC5 headline decision above -- the one item that flips AC5 to PASS.
- [`1.0.0_SA_CTO~Z`] **Surprise S1, ARMED, owner accepted:** `IDVZ` and `PFDE` both resolve to
  `#f43f5e` inside `SMA > ETF Strategies`. Invisible today only because both carry `0.0` and the
  suppressor removes them -- **and the SMA reland is exactly what puts values into that subtree**
  (`3.0.0_SA_CVO~Z` 14283 s.4). Same remedy shape as the Fixed Income pin. I offered to land it; not
  taken unilaterally because that seat owns the class.
- [post-reland] `CATV-TOF1-AC2` scored with the self-test-gated scorer. **Zero dashes must remain**
  and the 9th member must be proven ABSENT **at gate G5** -- an absence proven by naming its cause,
  not an absence observed.
- [banked, INERT] Surprise S2: `getModelColor`'s partial match resolves `'Ultra Short-Term (UST)'` to
  `Short-Term`'s amber. Served names are clean, so production is unaffected; a producer rename is
  what would make it live.
