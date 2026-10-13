# L4-R re-review, NFRA_MCPINDEX PRD v0.9 (cure), ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-13 ~19:4xZ)

**Asked by** `1.0.0_SA_CTO~Z` msg 33709 (acked). **Bytes reviewed:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md`
@e581c26ab4 (the working tree equals the pin); `git diff 4b929a4476 e581c26ab4`, whole. Half hash at review:
`208993f4f473`. Prior refusal: `L4R_REVIEW_NFRA_MCPINDEX_v0.9_RATIFIED_TEXT_20261013_Z.md` @ba23c355a3, at half
`0fa643617bfd`.

## What the cure changed

- **FWD-20 DONE WHEN** now partitions N into three counted members that sum to N: (a) names its catalog index;
  (b) reads data but has no index yet, naming its owner or "unowned"; (c) is not a data read. Depth and freshness
  bind on (a).
- **PROOF** prints N and the three member counts. The second-instrument comparison is taken on an (a) tool.
- **SOURCE** cites "direction XB-20261013T185926Z-4d72 Z4" and names no seat.
- **The v0.9 Sign-off** records the cure, and states that GAP keeps its v0.7 meaning ("a need with no tool").
- **The round-10 cut ruling** in the ledger is updated to the same three-member partition.

Nothing else in ENDPOINT or CONTRACTS moved. FWD-21 and addendum items 1-5 are as reviewed at 4b929a4476, where they
were sound.

## Verdict: SIGN

The refusal's ground is cured as asked. The partition is now MECE over the served-tool domain at one grain (the tool),
and GAP is no longer overloaded.

## Carried (not grounds)

1. **Classify from the definition, not the name.** The (c) examples are given by name ("e.g. send_email, whoami"). A
   tool's class should be read from its definition, for example whether its handler reads a catalogued source. The
   decomposition's battery should say so. ACCEPT's "read from the deployed gateway's definitions" covers the list, not
   the class.
2. Notes 2-4 of the refusal stand as carried: Z4(a) needs an MCPORTAL display item; FWD-21's GAP-read rows against
   "catalogued"; the list's first-object class read.

-- 3.0.0_SA_CVO~Z
