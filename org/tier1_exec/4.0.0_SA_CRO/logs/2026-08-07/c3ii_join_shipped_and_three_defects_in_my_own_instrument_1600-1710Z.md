# 4.0.0_SA_CRO -- C3.ii declared-plane join shipped, and three defects in my OWN instrument, one of which passed the very control I had just argued for (2026-08-07 16:00Z -> 17:10Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

## Window

16:00Z -> 17:10Z. Prior log: `to0_column_denominator_delivered_and_the_resolver_finding_1343-1600Z.md`.

## What happened

**1. Rule 21 repointed -- I verified the fix to my own finding and it was HALF closed.** MSTR's
broadcast credited my TO-0 misroute as the hole `comp-find` closes. Ran the exact failing intent: the
FOOTER is fixed (names `comp-find`), the ROUTING half is unchanged (`comp-blast` still top at 2.00
for a call-site search it cannot serve). Reported as LOW SEVERITY with the reasons it may not be a
defect at all, and owned that I had filed two halves as one finding. **COO then found the mechanism
in their own verification**: they grepped for `comp-find|comp-grep|comp-glob` and their pattern did
not contain `comp-blast`, so their scan was structurally incapable of seeing the unfixed half -- a
conclusion about ROUTING from an instrument whose domain was MENTIONS.

**2. Reviewed base CTO's C3.ii grounding as asked rather than inheriting it.** Agreed join-not-union
and sharpened why (an absence oracle passes for many reasons; a position oracle fails for one), then
found two holes: their CENG control was **undischargeable** (a dead applied plane satisfies it most
cleanly), and their 2x2's NOT-APPLIED cell failed Rule 24 postulate (iii) by pooling RETIRED with
ASPIRATIONAL. Also ran postulate **(iv)**, which they had not, and named which values do not move
together. **COO had independently found the same control defect within ten minutes** and amended the
TO mid-execution; both halves went in.

**3. C3.ii SHIPPED @c4d354d714.** 26 DECLARED x APPLIED / 9 NOT-APPLIED / 0 NOT-MEASURED of **35**
codes (not the grounding's "~30" -- that was a file read). 187 candidates of 400 measured resources.
Control PAIR passes, and passes for the *right* reason: CENG MEASURED-EMPTY / kind=RETIRED / not
matcher-limited, ADVI APPLIED in the same pass, ground-truthed independently at 0/0/0 for
`causality|ceng` against a positive control of 3 for `advisor` on the same pipes.

**4. >> THREE DEFECTS IN MY OWN INSTRUMENT, AND THE FIRST ONE PASSED MY OWN CONTROL. <<**
- **`shell=True` -> a page count wearing a total's clothes.** Quotes survived the shell, `aws` read
  the JMESPath as a RAW STRING LITERAL, returned that constant once **per page**: three limbs
  reported `measured` with n=**4/2/1** against true **197/139/30**, rc=0 throughout. **And my
  code-level control pair PASSED**, because ADVI was satisfied by a healthy LOCAL limb while three
  REMOTE limbs were dead. **A control at the wrong granularity reports the health of whichever limb
  happens to be alive.** I proposed that pair at code level and argued to COO that it catches
  silent-zero failures; it needed to be per-limb. Now every limb carries its own must-contain control.
- **Partial measurement read as complete** -- 16 codes said MEASURED-EMPTY including CENG, so the
  negative control passed on missing data. Fixed: *absence is only meaningful under complete
  measurement.*
- **Token bleed** -- CENG declares `pipeline = "causality, news-pipeline"` and inherited `news`,
  NPPL's own SURFACE, matching all 34 `news-*` resources byte-identically to NPPL and FAILING the
  negative control. I stopped and diagnosed per criterion 2 instead of shipping. Fixed by the
  registry's own rule 4: **surface area is IDENTITY, pipeline is only USAGE.**

**5. Rule-24 verdict shipped alongside, not gating.** Sharpened (i): a residual bucket makes
collective-exhaustiveness true BY CONSTRUCTION, so `ADHC` renders MECE **unfalsifiable**, which is
worse than failing it. Added (iv) with its three non-converging remedies. `MACRO_CODES.md` read-only
throughout -- editing it mid-harvest would move the declared plane under my own measurement.

**6. `4.0.0_SA_CRO~A` spawned; coordinated as base.** Gave it the authorization caveat, the
provenance split (four of the files it audits are MINE from this morning), the filename trap
(`06_..._v0.1.md` holds v0.4 content), the five already-settled findings, and one high-value unrun
target. Told it explicitly to **audit my files harder, not softer**, and not to route findings about
my work through me for softening.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-estate --definitions` | Phase 1, C3/C3.i/C3.ii/vertical/substrate | all reserved_ratified | adopted, not re-coined |
| `comp-estate --layers` | Phase 1 orientation | C3 is VIEW-COMPILED | carries my predecessor's own derive-don't-quote correction |
| `comp-which` | Phase 2, "what consumes the C3.ii candidate list" | near-tie, orientation only | no producer modified, so no blast radius |
| `comp-which` | re-ran my TO-0 failing intent post-repoint | **HALF FIXED** | footer -> comp-find; routing still comp-blast. Reported |
| `aws` (argv, auto-paginated) | lambdas / rules / buckets | 197 / 139 / 30 | counted client-side; **no `--no-paginate` anywhere** |
| `commit-gate.sh` | join script | BLOCKED then PASS | flagged `any_limb_ok` as dead -- **the leftover of the wrong completeness logic**, so the gate confirmed the old rule was gone |
| `safe-commit.sh` | 1 commit, `-F` | PASS @c4d354d714 | |
| join `--self-test` | 19 assertions | 19/19 | includes a regression for **every** defect in item 4 |

**What worked:** stopping on the failed control instead of shipping, and ground-truthing the CENG
zero with a positive control on the same pipes rather than trusting my own matcher. **What failed:**
my paired control was at the wrong granularity and passed through a dead measurement -- the exact
failure mode I had described to COO an hour earlier, in my own implementation of the fix.
**Gap found:** `comp-which` routing half still open (recorded, low severity, routed).

## Blockers

**None at me.** At **Andrew**: whether my atom_decomp proceed-condition reading stands -- now
materially relevant, because `~A` is auditing the corpus that rests on it.

## Current State (zero-context handoff)

- **NFRA_PYFIELD TO-0: CLOSED** (COO re-derived 3/3 exact). **C3.ii: COMPLETE** @c4d354d714.
- **4 commits unpushed** (lanes commit, integrators push).
- **`~A` is LIVE** on the ATOM_DECOMP audit, briefed, writing outside ATOM_DECOMP and pinning.
- **Named residues on C3.ii, none blocking:** 187 is an UPPER BOUND (5 matcher-limited codes put
  `bd-*`/`yang*` families in the candidate pile); matcher precision UNMEASURED (control codes
  hand-checked, not all 400 decisions); applied plane excludes IAM/DynamoDB/CloudFront/Step
  Functions/portal `json/*`, so it is larger than 400. The cheapest real fix is a registry column
  naming each surface's resource prefix -- **Andrew's file, his act; proposed, not performed.**
