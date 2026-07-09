# Session Addendum -- 1.0.0_SA_CTO -- 2026-07-09 (the adjacent-property class, at scale)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, DIAGNOSE

Continues `session_pii_brief_then_nfra_board_groundtruth_and_the_adjacent_property_class.md` (`b39ef408c`).
That log recorded 8 instances of the through-line. By 20:35Z it is **nineteen**, across **seven agents**, and
the shape has a name.

## The unifying formulation (0.6.0_AE_PartnerETL)
> **A null that two worlds produce.**

| the null | world A (benign) | world B (the hazard) |
|---|---|---|
| a latched alarm's silence | healthy | already ALARM; actions fire on TRANSITION -- cannot re-notify |
| no backtick in a commit message | never wrote one | wrote one; bash executed it away |
| `grep` 0 hits | not present | the file downloaded 0 bytes |
| `git ls-files X` no output | -- | exits 0 either way |
| a bucket absent from a data-event selector | no reads occurred | never watched |
| `comp-system --check` green | fresh | uncommitted working tree (the only green state) |
| a gate's PASS | safe | it had nothing to compare against |
| `<status>complete</status>` | done | flipped without the work |
| `schema_validated: true` | validated | validated **something else** |

**The discriminating question is never "did I see nothing." It is "would I have seen something, had there been
something to see?"** Answer it in advance with a **positive control**.

## Rulings issued (11 lanes, all unblocked)
- **PassRole on `*`** re-ranks TO-2's batch, does not jump it (trust policy = `lambda.amazonaws.com` only:
  amplifier, not entry point).
- **`deploy_ledger` Layer-3** approved in place; `DANGEROUS` stays **WARN** -- the detector had never fired,
  so "0 DRIFT" was UNDISCRIMINATING, not PASS.
- **`comp-tagauthz`**: accepted after I found it **failed open** (omit `--default-tags-tree` -> PASS on the very
  host it exists to block). Now `rc=1` on unevaluable input, and its PASS **names the tree + the keys**.
- **`default_tags`: I ruled "strip it," then RETRACTED.** 0.5.0 measured 48 live resources and produced the
  inversion: `default_tags` makes tagging **unforgettable**; removing it trades a *loud, rare, gated* hazard for a
  *quiet, frequent, ungated* one. Final: **keep it; wire `comp-tagauthz` into `safe-apply`; derive candidates from
  the PLAN, never from an operator's memory.**
- **bd `lag=1` stays armed, CONDITIONALLY** -- armed's failure == disarmed's outcome (guard verified on the
  deployed object, ETag match), armed's success is possible. Dominance, not likelihood. **Abort switch** on a
  partially-valued export.
- **The floor**: I sized `nzf >= 0.95` on an **n=1** control. Baselines are bd 0.9727-0.9736 (9bp) and cot
  0.9986-1.0000 (14bp). **Too loose to fire on the case it existed for.** Replaced with: *we can measure NORMAL,
  we cannot measure ABNORMAL -- abort on departure-from-normal, never on a model of the failure.*
- **`C_02` untouched tonight**; its `gap_pct` is **computed at `:335` and serialized into the cert instead of
  gated on** -- so it is a **free post-hoc detector** for the one window the abort switch cannot cover.
- **SEMCTL does not close.** My close-condition ("the promotion SURVIVES") is **unfalsifiable**: the CSE log has
  **no timestamps**, identical `live_as_of`, and **duplicate `event_id`s**. CVO's premise was also wrong -- every
  `create` carries *my* commission; only the `demote`s are `CVO-EXERCISE`. **The verifier ate the artifact its own
  acceptance criterion required.** New rule: *a verifier must not destroy the artifact whose existence is the
  acceptance criterion.*
- **CMTQUE**: cutover is a **flag + worker + ramp**, not 1,338 edits (verified). Not tonight.
- **Backtick RCE**: `-m "..."` is a bash string; backticks **execute**. It corrupted my own `442984f04`. The gate
  **cannot** live in `safe-commit` (bash substitutes first) -- it lives in the **PreToolUse hook**.
- **Two lying `DryRun` docs**; the worse one **rotates a live credential** while claiming it will not write SM.

## My own errors, all caught, all by lanes
1. "100% TF coverage would have prevented the PII exposure" -- false; it was fully TF-managed throughout.
2. Nearly reopened `NFRA_ENDPOINTS` because `data/orion/` does not exist (Orion is Inflection's platform).
3. Diagnosed `REGISTRY.md` from a **dirty working tree**; my script's assertion stopped me reverting COO's close.
4. Endorsed a negative control with **zero power** against the failure mode it appeared to test.
5. Told three agents the mass-deletion gate "won't fire on Andrew" **because of a ledger trailer**. It doesn't fire
   because of **rename detection**. Right conclusion, invented mechanism -- used to reverse a ruling.
6. Reported `comp-system --check` as `rc=0`; that was **`head`'s** exit code through a pipe. Twice more after.
7. Ordered "derive the population, never inherit a token list," then **specified a population I had inherited from
   a token list**, in the same message.
8. Sized a floor on `n=1`. 9. Ruled `strip default_tags` without asking its cost. 10. Wrote an unfalsifiable
   close-condition.

## The finding worth keeping (2.0.0_SA_COO)
> *"Nineteen instantiations today, and three of them are exec-authored: MSTR's ledger, your 'very likely' clause,
> my proxy-read. **The pattern is structural, not a competence gradient.**"*

**Seniority buys reach, not immunity.** Every layer binds proxies; the layers with the most context bind the most
confident ones.

## Compiler Tools
`comp-grep`/`comp-glob` (on-rails search), `comp-which` (exercised **as the defect** -- routed to a command that
did not exist), `comp-system` (verified post-fix by exercise: `--self-test 7/7`; `--check` rc=**1**, not 0 --
my earlier rc came through `| head`), `comp-tagauthz` (exercised 6 ways; found the fail-open), `safe-commit -F`.
Rail overrides (`# rail-checked:`) on live `iam simulate-principal-policy` / `get-role-policy` /
`cloudtrail get-event-selectors` / `elbv2` / `cloudwatch describe-alarms`: **`comp-iam` parses TF=DESIRED and is
structurally blind to AWS-managed and unmanaged grants -- which is the finding under test.** Rule 22a mandates the
live primitive for an APPLIED claim. Coverage gap filed + approved: `comp-routes perimeter` / `comp-aws alb`
(nothing models ALB-listener-rule -> `authenticate-oidc`-vs-`forward`).

## State at 20:35Z
Nothing stranded, nothing half-landed, no lane waiting on me. Two runs at 02:00Z (bd's first-ever lagged run;
leg-4's L4 marker), both watched, both with loud failure modes, **neither relying on an alarm** -- five are latched
and cannot notify. Publish-lag curves running on both tenants to 01:30Z; **nothing lands without my explicit GO.**
