# NFRA_OPLGTW v0.2 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~20:13Z · request: `1.0.0_SA_CTO~A` message 96738.

**VERDICT: SIGNED, brief half.** R1, R2 and R3 from the v0.1 refusal are closed. Each item named there now appears
in its coverage row and in a consuming surface or acceptance row. ENDPOINT, CONTRACTS and the contract data are
byte-unchanged.

## Exact inputs and scope

- PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@059526828b2d0393c181b1294f64bb6e5205333f`, v0.2,
  295 lines, 52,943 bytes. The file's latest commit is the pin, and the worktree matched HEAD at review.
- brief_ref, the commission: `…/ANDREW_DIRECT_20260914_1511ET_NFRA_OPLGTW_D9_REGISTRATION_AND_PRD.md@45ce4e5b73`
  (4 headings). The supplied SPEC: `…/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/SPEC.md@39a8c5eeca` (10 level-2
  headings, none deeper).
- Reviewed brief-half SHA-256: `04461a4925dc40dcbe06c85962f6cd200dd819bacdf1a6c2251885281c798dc1`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `04461a4925dc`.
- Ratified-text half: `908c9e9460c1cdbb3cf4fa111d5946461c1dfc074963022b3b5e43d6c00233f9`. It is identical to v0.1's
  and still SIGNED current by `3.0.0_SA_CVO`.
- `org/standards/NFRA_OPLGTW_CONTRACT.json`: `git diff 2af252cb39 HEAD` is empty.
- Prior review: `docs/briefs/sources/NFRA_OPLGTW_L4_BRIEF_REVIEW_v0_1_20260914.md@51c7fc7f51b69a711118770077e1f8ec93f303fb`,
  which REFUSED v0.1 (stamp `f348c0a537`).

## Correction closure

`git diff 2af252cb39 059526828b` on the PRD: 18 insertions and 14 deletions. The changes are the version header, the
authority line, S9, coverage rows for four sections, the matrix preamble, A6, A15, A16, A19, A20, and two new
paragraphs in the operator journey. All of these are in the brief half.

| v0.1 finding | Where v0.2 carries it | Verdict |
|---|---|---|
| R1(a) the IPv4, DNS, global-routing, no-cross-host-redirect and WAF/proxy checks from the actual Claude connection (SPEC 123) | Coverage row "Network and front-door contract" (v0.2:239); A16 (v0.2:268); S9 (v0.2:209); the operator verification paragraph (v0.2:278) | CLOSED |
| R1(b) the Anthropic egress range 160.79.104.0/21 where filters apply (SPEC 123) | v0.2:239, A16 and v0.2:278. It is reverified against current published egress at rollout, and "The IP range is never user identity" is kept. | CLOSED |
| R1(c) the measured 60-second ALB idle timeout (SPEC 125) | v0.2:239 ("constrains query/export preparation and streaming gaps, despite Claude's longer timeout"); A19 (v0.2:271); S9; v0.2:278 | CLOSED |
| R1(d) Host/Origin verification, clientInfo as telemetry only (SPEC 125) | v0.2:239, A16 and v0.2:278 | CLOSED |
| R2 A6 caching (SPEC item 6) | A6 (v0.2:258): "precedes queries, aggregates, caching and export". Its proof deliberately warms caches under another or a broader grant, then checks filtered reads and writes under the narrower grant and denial after revocation. | CLOSED |
| R2 A16 network checks (SPEC item 16 plus R1) | A16 (v0.2:268) | CLOSED |
| R2 A19 ALB idle behavior (SPEC item 19) | A19 (v0.2:271), with slow preparation, streaming and cancellation deliberately exercised through the ALB | CLOSED |
| R2 A20 tool and connector-URL records (SPEC item 20) | A20 (v0.2:272) and the matrix preamble (v0.2:249). The connector URL is defined as the public endpoint, without credentials, ticket fragments or private query parameters. | CLOSED |
| R3 Claude chat retention disclosure (SPEC 161) | Coverage row "Downloads and revocation" (v0.2:241); onboarding (v0.2:276: "the operator tells Menachem …"); A20 | CLOSED |
| R3 preserving the source-bucket settings (SPEC 38) | Coverage row "Observations and gaps" (v0.2:235); A15 (v0.2:267) records before/after readbacks; S9; v0.2:280 names the four controls and treats a mismatch as a failed preservation check | CLOSED |

**What was re-checked beyond the named lines:**
- The coverage row "Implementation and acceptance" (v0.2:243) now names the restored clauses.
- The version line (v0.2:27) cites the v0.1 review by path and pin.
- No A-row outside A6, A15, A16, A19 and A20 changed, and no coverage row outside the five named changed. No new
  claim of execution was introduced: v0.2:278 and v0.2:280 each say the authoring clauses do not claim the tests ran
  and are "not a fresh cloud measurement".

## Coverage

Apart from the lines above, the brief half is byte-identical to v0.1. So the v0.1 review's section-by-section check
of both coverage maps stands, now with those rows amended: the commission map's 4 headings and the SPEC map's 10 of
10. So does its verification that the contract's field lists and limits equal the SPEC.

## Limits

This is requirements acceptance only. No deployment, IAM, network, Claude journey or bucket readback was exercised.
The 60-second idle timeout and the Anthropic range are the SPEC's recorded values, and v0.2 itself marks the range
for reverification at rollout. The ratified-text half and the pending ground-truth certification are
`3.0.0_SA_CVO`'s. The header remains DRAFT by the PRD's own rule until that certification. Admission is measured by
the canonical status read after the stamp.

The delivered notice 96738 was opened and READ-acked. This seat performs no push, deploy or cloud mutation. Push
state is measured and stated in the completion message to `1.0.0_SA_CTO~A`.
