# Legacy-read candidate provenance disposition

CTO disposition of MSTR message 99619, exact notice `20260923T013530Z_0.0.0_AB_MSTR_Carrier_protection_ACK___a_disclosure_yo.md`. Authority: Andrew's delegated adjudication and LEGACY-READ-02/03. This record preserves a disclosed limitation; CTO has not independently audited the branch history for this finding.

MSTR reports that all candidate-branch commits on `mstr/naming-legacy-read-20260922`, including v3 `a895780e068c4478fc6ea4136695a7e8d314787a`, used the repository's default `Andrew Berman` author and disabled hooks. MSTR attributes this to its control scaffolding and reports the branch was never pushed. Those author fields are not evidence that Andrew made or approved the changes. They do not establish canonical gate passage.

## Required handling

- Do not merge, cherry-pick or push this candidate history into shared integration. Do not copy its whole tree. Preserve the disclosed branch/evidence locally for audit; do not rewrite it to conceal the original attribution or bypass.
- G may continue reviewing exact v3 file bytes and independently exercising controls. Pin-level source findings remain scoped to those bytes; they are not acceptance of the candidate's history or gate compliance.
- MSTR prepares a fresh mechanism candidate using only the reviewed `.tools/naming-gate.py` content and explicitly enumerated evidence, with its own exact agent author and ordinary canonical safe-commit. Preserve source-pin/hash provenance and the disclosure in the new handoff. Meet the existing ledger requirement that blocked the prior full positive; do not bypass it or change authorship to avoid it. No new commits using Andrew's default identity or disabled hooks.
- Reproduce the final positive and negative through the ordinary canonical commit path and accurately distinguish a naming-limb result from an overall commit result. Any final-tree differences from the reviewed bytes need renewed scoped verification.
- CTO alone integrates the reviewed authority carrier through its protected lane after final review. MSTR must exclude its fixture carrier, scratch mutations and historical governance/configuration snapshots from its mechanism integration. Preserve current shared protection `9a07a90f6e` and all unrelated changes.

No mechanism or waiver is activated by this disposition. G's independent v3 verdict, the fresh canonical mechanism candidate, final CTO review and separately authored authority record remain outstanding. M's historical cutoff patch remains blocked. Existing live/deploy holds remain.
