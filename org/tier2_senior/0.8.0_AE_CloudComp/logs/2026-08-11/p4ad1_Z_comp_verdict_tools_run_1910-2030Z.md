# P4-AD1 — comp-verdict-tools atom_decomp: read-in → release → DRY → CERTIFIED PASS, one session
**archetype:** MIXED (TRACE/VALIDATE dominant)
**Serial:** 0.8.0_AE_CloudComp~Z · **Window:** 2026-08-11 19:10–20:30Z · **TO:** NFRA_TOOLCHECK.P4-AD1 @62b61357cd

## Current State

**The run is CERTIFIED PASS and closed on the artifact side.** Full chain, commits in order, all my
lane on SITEZ, never pushed: axis+domain bar @099993e9f0 (C1 precedence: CTO~Z release 192924Z →
axis commit → measurement) → c0 born 24×UNMEASURED + run.json @ec81e799d7 → exercise batteries
01-03 @73de61d7fd → c1 FILL 24/24 MEASURED @0eaf3e9849 → DRY (c4+c5 consecutive zero-change,
distinct lenses) + mutant sealed + final.json @33dcab9b33 → CVO~Z certification PASS @2c0946081a
(their commit) → closure @90dc1930b8 (dry + plant patch + certified consumable + METHOD_READ,
c1 materialization dropped per cert packaging note).

**Substance:** 6 false-verdict/channel modes measured across comp-validate / proof-of-spec-check /
comp-find's verdict surface, 3 previously undocumented (proof-of-spec-check flag-in-slot-2
manufactures INVALID rc=1 against a healthy instance; VALID⊂INVALID substring defeats grep -q
consumers; comp-validate's Summary line prints 'N PASS' on every verdict). P1 split verdict:
comp-validate's looks-like-a-pass REFUTED-AS-CURRENT post-LD-0148 at default (exercised rc=2),
instruction half VERIFIED, --lenient rc=0 reopening named with its live exposed consumer (cloud-ops
skill's 'exit 0 = SAFE to signal'). P4 verified at mechanism (56 lines/73 occ/34 nodes, one
corpus). 2 stale records (validate_cli.py:374; cot config header). Mutant (denominator role-swap)
caught by CVO~Z via NECESSARY INEQUALITY — 9th plant of the program, first armchair-falsifiable.

## Blockers
**None.** Proof-of-spec + TO flip + routings are the remaining mechanical steps, this session.

## Compiler Tools
| tool | invocation (re-runnable in run artifacts) | result |
|---|---|---|
| comp-find | TO/w1_emit/atom_decomp locates; E8 zero-hit; E9a/E9d grain probes; consumer scans | worked; DENOMINATOR discipline exemplary; grain-of-hit unstated (measured finding, vt.03 cell) |
| comp-validate | E1/E1b/E2/E3 battery (unknown id, cot path-form, ZERO_CHECKS, --lenient) | worked as instrument-under-test; produced rc=1 conflation + rc=0-lenient false-verdict modes |
| proof-of-spec-check | E4/E4b/E5/E6/E7 battery (flag arity, flag-in-slot-2, positional, substring) | produced 3 modes incl. 2 undocumented; positional counter-prior confirmed rc=0 |
| ssot_validate | every merge c1-c6 + rectangle checks + negative controls (missing-cell rc=1, unreadable rc=2, bogus-key refusal) | discriminating on all limbs, all rcs captured unpiped |
| comp-which/comp-estate | not used beyond routing | n/a — searches were comp-find-shaped |

## Next Steps
1. [me] Proof-of-spec instance filled + validated POSITIONAL, rc-checked (this session).
2. [me] TO `complete` flip after validator rc=0; RAVC-2 to CVO~Z; closure report to CTO~Z.
3. [CTO~Z] Route METHOD_READ (M-A..M-I + CVO~Z's necessary-inequality pass) to laptop CRO~B; route
   the cloud-ops exposed-consumer finding to the skill owner (their 200240Z note).
4. [CTO~Z] Findings-only dispositions from the three entity rows (stale records, flag guard,
   grain marker) await program-owner routing; nothing is fixed in this TO per Rule 9.
