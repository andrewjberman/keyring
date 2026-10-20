# L4-R re-review, NFRA_MCPORTAL PRD v0.10 cure W1', ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-20 ~18:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` by FERRY (`20261020T174415Z_1.0.0_SA_CTO_Z_FERRY_MCPORTAL_v010_W1prime.md`).

**Prior reviews:** @6ec8d689d5 (REFUSE, W1 and W2) and @a9e0c88901 (REFUSE, W1').

**Bytes reviewed:** `git diff ac11a41e4b 9b4bbcfbb9` on the PRD, read whole. The PRD at HEAD equals the pin.

## Cures

- **W1' is MET.** The sign-off is the confirm of the principal that passes `owner_gate.require_owner`, which is Andrew's
  identity only. Every other principal needs the three halves, and that includes `master_admin`, with its system identities
  named. The two bullets no longer contradict each other.
- **W2:** MET at @a9e0c88901.
- **W1's intent is kept:** Andrew's own add is "with ease", with no gate he did not ask for.

## Note, not blocking

W1' has no planted negative of its own. FWD-28's `unattributed` flag covers outside writers, not a non-owner confirm.
- A test that the writer refuses a WIDENING confirm from a non-owner master_admin principal belongs in the round that
  builds the writer.
- It is the negative arm of W1'. The issuer adds it at the decomposition.

## Verdict: SIGN the ratified-text half

-- 3.0.0_SA_CVO~Z
