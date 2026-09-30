# IRPT_BCKEND decomposition -- ROUND 22, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on the CTO's sweep-1 analysis)

Cut on `ledger/ROUND_ANALYSIS.sweep1.md` (@eaefb76322, msg 102708) section 4 item 3, and CTO msg 102702 (CRO finding
102699 = brief item AD-10). Item 3 names three acts for ~M. TO-IB-m21-212 Part 2 (the cot login deploy) is already in
flight in round 21 under the issuer's GO and the CTO's read (@76a44392fd), so it is not re-cut here. The other two
are this round's rectangle.

| cell | item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-221` | AD-10: every directory entry carries each ACCOUNT's own mask (its own last-4 and its own UIC-16 registration name), additive to `DirectoryEntry`, beside today's head-row `masked_discriminator` | brief AD-10 ("each account shows its own tail everywhere"); CTO 102702 | FWD-2 (the directory: picker + identity list) | LOCAL build + half (serves at the directory bundle's next signed re-mint, with ~D's picker reading it) | none |
| `IB-mr-222` | The Holdings L0 re-mint on its signed release order: re-mint `irpt_holdings_{49f,inf,cot}` from CLOUD (IB-mr-202 CATEGORY, IB-mr-203 vendor keys + assigned strategy, IB-mr-213 registration labels), then read every reader on the served page at the next scheduled publication | CTO signoffs SIGNOFF_HOLDINGS_L0_CATEGORIES_AND_VENDOR_KEYS_20260929.md and SIGNOFF_HOLDINGS_UIC16_49F_20260929.md; release order step 3 | FWD-5 (Holdings) | WORLD (S3 mint + served publication) | release step 2 (portal PROD reads CATEGORY -- Andrew's word on the hotfix); IB-mr-204 drained (the first scheduled fire read on today's packages) |

Chains: A = 221, worker slot `0.9.0_WK_IRPT_BCKEND~75` (S197: 1 + max(authors 73, issued_to 74, branches 74) = 75).
B = 222, worker slot `0.9.0_WK_IRPT_BCKEND~76`, spawned only when both dependencies hold. Its order states them as a
refusal: a worker that finds either unmet stops before the ledger opens.
Rule carried (round-19 analysis s.2): an order that changes a served figure names every reader in its criteria.
