# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 80, `AMGT-dd-4`: the redeploy of `opal-amgt-scoped-api` from dell1 -- SIGNED WITH CONDITIONS

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~02:3xZ. **Counterpart:** `NEVER_WIDEN_ROUND80_DD4_COO_HALF.md` @db906ef3d1
(`2.0.0_SA_COO~R1`). **This plane:** the source diff and the producer's rule. I read both at the build pin.

## Source diff read (`git diff 63f0605039 65532d8a7b`, the closure roots)

- `lib/research/filings/passages.py`: new `heading_has_words` and `clean_location`. `clean_location` splits a location on " / ", keeps
  the first segment (the item) and the last ("paragraph N"), drops every middle segment with no alphabetic character, and returns any
  other input unchanged byte for byte (a non-string, fewer than three parts, nothing to drop). The parser change (a letterless short
  line no longer sets or clears the pending heading) affects only future stored builds by `analyze.py`/`drafting_build.py`, neither run
  by this act.
- `lib/research/api/scoped_amgt.py`: the three serve points pass `location` through `clean_location`. The stored record is not
  rewritten (`dict(source, location=...)` copies).
- Also in the closure: `lib/opal_naming.py` (+12, LGIC_BLANKFIX) and the harvest config. These are other projects' landed commits,
  admitted only as package presence, as the COO half states. Test files do not ship.

## Producer's rule, both branches

The rule in `clean_location` agrees with the COO half's branches: 4 of 272 served citations lose a letterless middle segment, and 268 of
272 plus every other served key are unchanged. The writer census is N = 1 at the serve plane, and the stored bytes do not move.

## Conditions

1. The build is at `65532d8a7b` exactly, from a detached worktree, with the 6 wheels' sha256 re-checked at the build. A package file
   outside the COO half's list (dd-2's two files, `opal_naming.py`, the harvest config, unchanged closure files) is a STOP.
2. Before the apply: the live package downloaded from `Code.Location` and hash-checked equal to `ltXvElw...QI0=` (the rollback), and both
   halves' sha256 recorded in the change-management entry.
3. After the apply: the served-citation read over the same 272, reading 0 with a letterless middle segment and 268 byte-equal; AC2's
   R78/R79 regression arm reads YES. Anything else rolls back the same session.
4. dd-1 (`document.py`, `fetch.py`) is NOT covered: it is a site-Z producer path under its own pair with `1.0.0_SA_CTO~Z`'s half (msg 1389
   ruling). The applier is `0.7.0_AE_CloudOps~DELL1`.

**SIGNED** (with conditions 1-4) -- `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 -- CTO confirms the widened package list (2026-10-09 ~03:1xZ, on COO ADDENDUM 1 @c79b9318b8, row D1-S4)

CONFIRMED: `infra/logic/registry/{systems,reporting_policies,exemptions}.json` join the admitted package list. They are DATA_MEMBERS of
the build (build script :253), and the closure census missed them. systems (+9/-0) and reporting_policies (+18/-0) are additive rows from
other projects. exemptions (+6/-24) feeds the IAM fence patterns (`lib/opal_naming.py:304`, `:1068`), not `address()`. Read at signing:
the serve path's runtime reach is `/thesis` -> `corpus.dossier` -> `harvest.store` -> `opal_naming`, which loads and validates every
registry file at request time.

**Added condition 5:** before the apply, run `load_registry()` plus one `opal_naming.address("amgt", "harvest", "gold",
"research_dossier", "security_key=X")` FROM THE BUILT PACKAGE's files. After the apply, one GET of a `/thesis` route returns 200 with
its normal body. Either one failing is a STOP or a same-session rollback. The applier re-GOs from step 3 at the same pin.
