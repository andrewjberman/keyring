# NFRA_OPLGTW v0.1 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~19:58Z · request: `1.0.0_SA_CTO~A` message 96730.

**VERDICT: REFUSED, brief half.** Most of the supplied SPEC is carried. The contract's field lists equal the SPEC's
proposed columns exactly, its limits equal the SPEC's numbers, and 17 of the SPEC's 20 acceptance items map to A-rows
without loss (A11's narrowing is a stated departure).

Three grounds remain, all of one kind: SPEC content that appears nowhere in the PRD, in either half, while the
coverage table reports its section as carried.
- **R1:** the network and front-door checks, including the measured 60-second ALB idle timeout.
- **R2:** four acceptance items narrowed without a stated departure: A6, A16, A19 and A20.
- **R3:** two SPEC disclosures, Claude chat retention and the source-bucket settings to preserve.

Every fix is a line in a coverage row, an A-row or the operator journey.

## Exact inputs and scope

- PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@2af252cb3961c0c7d9529af3d6f5e754faff4c43`, v0.1,
  291 lines, 48,555 bytes. At review, HEAD and worktree both matched the pinned bytes.
- brief_ref, the commission: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_1511ET_NFRA_OPLGTW_D9_REGISTRATION_AND_PRD.md@45ce4e5b73`,
  25 lines, **4 headings**: the title plus three sections.
- The supplied brief it names: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/SPEC.md@39a8c5eeca03666d3ef81dbccce6859506b572af`,
  218 lines. It has **1 level-1 and 10 level-2 headings, and no deeper headings**, so the level-2 grain is the whole
  section set. Its worktree matched the pin.
- Reviewed brief-half SHA-256: `999a3219dcea83c1a5a2119d069868c1025a000f504c28e938913e44962450b7`, computed by
  `prd_signoff_lib.half_hashes` on the pinned bytes. It matches the notifier's `999a3219dcea`.
- Ratified-text half (ENDPOINT, CONTRACTS C1–C6), identified but not signed here:
  `908c9e9460c1cdbb3cf4fa111d5946461c1dfc074963022b3b5e43d6c00233f9`.
- Contract data: `org/standards/NFRA_OPLGTW_CONTRACT.json@2af252cb39`. The SPEC's proposed entitlement:
  `menachem-entitlement.proposed.json@39a8c5eeca`.

This seat reviews the brief half: authority and arc, scope, surface manifest, ground truth, BRIEF COVERAGE, the
acceptance matrix, the operator journey and the handoff. It checks both coverage maps.

## What is carried, with the checks behind it

- **The commission map (v0.1:228).** All three sections are carried: the D9/NFRA identity and CTO ownership; the SPEC
  pin; and the singular `/endpoint --forward`, the UNCHECKED receiving-check and the registration/PRD-only scope. The
  denominator is 4 headings, of which the title is identity context.
- **The SPEC map (v0.1:232–243), 10 of 10 headings.** Checked against the SPEC text section by section:
  - Recommended experience: the "Confirmed by Andrew" table (SPEC 23–30) is honoured in Scope (v0.1:37).
  - Architecture and authorization: the immutable tid/oid principal, default deny, and a tombstone rather than
    deletion.
  - Proposed first entitlement:
    - The contract's `fields` equal the proposed JSON's column lists exactly: dim_position 11, dim_balance 9,
      dim_asset 9.
    - `forbidden_field_classes` covers raw account ID, account title, tax identifier and mailing address (SPEC 93).
    - The window is 30 days, anchored on the latest complete business date (SPEC 91; contract `calendar_days: 30`).
  - Claude application login: SPEC 109's in-memory state is replaced by durable state, and SPEC 111's refresh
    correction is carried.
  - Tool and query contract: the contract limits equal SPEC 145: 30 s; 12 objects / 67,108,864 bytes; 500 rows,
    100,000 codepoints and 131,072 bytes; 250,000 rows / 52,428,800 bytes.
  - Downloads: SPEC 151's five-minute ticket is `limits.ticket_seconds: 300`.
  - AWS permissions: the reader role, the dedicated ExternalId and the 41-simulation limit are carried.
- **A11's departure (v0.1:245)** is sourced in the SPEC itself: "Filtered CSVs initially; originals later" (SPEC 27)
  and "Keep it disabled in v1" (SPEC 157). It is stated, not silent.
- **S4's completion-metadata extension (v0.1:212)** is stated as a bounded departure from SPEC 139's reuse
  preference, and justified by SPEC 139's own fail-closed clause.

## R1 — the network and front-door checks are lost

SPEC "Network and front-door contract", lines 117–125:
- (a) "Validate public IPv4 DNS, globally routable answers, no cross-host redirect, and WAF/proxy preservation from
  the actual Claude connection" (123).
- (b) "permit the current Anthropic outbound range, 160.79.104.0/21, on required MCP/OAuth paths" where network
  filters apply (123).
- (c) "The measured ALB idle timeout is 60 seconds. Keep the 30-second query deadline; bound export preparation and
  avoid idle streaming gaps. Do not assume Claude's longer tool timeout overrides the load balancer" (125).
- (d) "Verify Host/Origin behavior with Claude while retaining origin validation where applicable; clientInfo names
  and versions are telemetry only" (125).

**Census of the pinned PRD, all 291 lines and both halves:**
- **0 hits:** `IPv4`, `DNS`, `WAF`, `160.79`, `Anthropic`, `\b60[- ]?s(econd)?`, `Host`, `clientInfo`.
- **`idle`:** its one hit is the 7-day refresh expiry in C1.
- **`Origin`:** the only substantive hit is C5's download POST check.
- **The contract** has no ALB field; its only "idle" is `refresh_idle_seconds`.

**The coverage row "Network and front-door contract" (v0.1:239)** lists "Existing public MCP endpoint and ALB,
explicit auth routes, preserved stream headers/transport/cancellation and browser default, no private tunnel". It
omits (a) through (d). The limits in C4 and C5 happen to fit under 60 seconds, but nothing records the ALB timeout
as a constraint. So a later limit change would not see it.

**Fix, returned by pinned line:**
- v0.1:239: carry (a) through (d) into the row.
- Name a consuming surface for them: S9 (v0.1:209) and A16 (v0.1:268) for (a), (b) and (d); A19 for (c), see R2.
- Whether any of them also becomes a clause in C1 or C6 is the author's call. That half is `3.0.0_SA_CVO`'s.

## R2 — four acceptance items narrowed without a stated departure

The coverage row "Implementation and acceptance" (v0.1:243) claims the SPEC's "20 acceptance criteria", and the
matrix preamble (v0.1:249) says the expected set is A1–A20. Compared item by item with SPEC 195–214, four A-rows lose
a clause the SPEC's item carries. Only A11 has a stated departure.

| SPEC item | Clause lost | PRD row |
|---|---|---|
| 6 (200): "Account/column filtering precedes queries, aggregation, **caching** and export" | caching | A6 (v0.1:258): "precedes aggregates and export". C2 requires policy before "cache lookup", but no A-row proves it. A5 proves only that caches do not mix masters. |
| 16 (210): "Actual Claude web/desktop handshake preserves the Bearer challenge, headers, negotiated protocol and transport through the deployed edge" | none by itself | A16 (v0.1:268) carries item 16, but it is the natural home for R1's (a), (b) and (d), and it names none of them. |
| 19 (213): "Auth endpoint latency meets its separate deadlines; **query/export traffic respects ALB idle behavior** and cancellation" | ALB idle behavior | A19 (v0.1:271): "Auth endpoints meet 10s/refresh30s deadlines under load; cancel disconnects terminate jobs; denied grants do not produce an OAuth loop" |
| 20 (214): "Record **tool**, UTC timestamp, **connector URL** and sanitized server correlation; collect an ofid_ reference" | tool and connector URL | A20 (v0.1:272) keeps "sanitized correlation/ofid_". The matrix preamble (v0.1:249) records UTC time and the request but neither the tool nor the connector URL. |

**Fix, returned by pinned line:**
- A6: restore caching.
- A16: add R1's network checks.
- A19: restore ALB idle behavior, at the measured 60 s.
- A20 or the preamble: restore the tool and connector-URL record fields.

## R3 — two SPEC disclosures dropped

| SPEC | Text | PRD |
|---|---|---|
| Downloads and revocation, 161 | "Selected results enter the organization's Claude chat environment and retention settings. Commercial training defaults do not mean zero transfer." | 0 hits for `retention` or `training`. The coverage row (v0.1:241) carries "already delivered bytes unrecalled" but not where the returned Schwab client data then resides. The operator journey (v0.1:276) onboards Menachem without it. |
| Observations and gaps, 38 | "Versioning enabled, AES256 encryption, all four public-access blocks enabled, bucket policy status non-public → **Preserve these settings**" | 0 hits for `versioning` or `public-access`. C3 depends on VersionIds and C6 on AES256, but the requirement to preserve the four public-access blocks and the non-public bucket policy is nowhere stated. The coverage row (v0.1:235) omits it. |

The first is the brief's only statement of where the product sends client data once it answers, which bears on what
the operator tells the user and Andrew at onboarding.

**Fix, returned by pinned line:**
- v0.1:241 and the operator journey (v0.1:276): carry the retention disclosure as an onboarding statement.
- v0.1:235: carry "preserve these settings", and name its consuming surface (S9's release invariants, or the rollback
  invariants).

## Not grounds

- The SPEC's 240-second published tool deadline is carried in substance by C4's "stay within Claude's published
  runtime limits".
- The one-time forced reconnect departs from SPEC item 2's "retain their working flows", but it is stated in C1 and
  A2 and justified by SPEC 111's refresh correction. The half says so.
- The capacity target (t4g.small) is labelled a design target with a benchmark gate (v0.1:284). No move is asserted.

## Limits

This is requirements review only. No deployment, IAM, network or Claude journey was exercised. The SPEC's own
measured facts, the 60-second idle timeout and the 18:43:46Z probe, are cited as the SPEC states them, not
re-measured. The ratified-text half and the pending ground-truth certification are `3.0.0_SA_CVO`'s. A v0.2 that
changes only the lines named above needs no re-audit beyond them, unless the author also moves CONTRACTS, which
re-opens only that half.

The delivered notice 96730 was opened and READ-acked. This seat performs no push, deploy or cloud mutation. Push
state is measured and stated in the completion message to `1.0.0_SA_CTO~A`.
