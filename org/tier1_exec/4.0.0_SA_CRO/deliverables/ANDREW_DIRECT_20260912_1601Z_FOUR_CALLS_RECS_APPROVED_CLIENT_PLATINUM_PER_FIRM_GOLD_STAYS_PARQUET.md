# ANDREW-DIRECT 2026-09-12 ~16:0xZ -- four `/open-calls` recs approved: client platinum goes PER-FIRM, gold STAYS parquet

**archetype:** SCRIBE (record)
**Channel:** the `4.0.0_SA_CRO~D` terminal, direct to this seat. **Recorded by:** `4.0.0_SA_CRO~D`.
**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Status:** DIRECTION RULED. ⛔ **NOTHING MOVES. NOT A MIGRATION AUTHORIZATION.** NEVER#3 unchanged.

---

## 1. THE WORDS, VERBATIM AND COMPLETE

> **"Recs approved"**

⛔ **THAT IS THE WHOLE OF WHAT HE SAID.** Nothing paraphrased, nothing omitted. It answers the
four-card `/open-calls` set this seat put to him minutes earlier in the same terminal, at
2026-09-12 ~15:2xZ.

---

## 2. WHAT IT RULES, CARD BY CARD

| card | the call | ruling |
|---|---|---|
| 1 | client PLATINUM home: (a) per-firm bucket or (b) `opal-data-portal-v2` | **REC APPROVED -- (a) PER-FIRM.** |
| 2 | client GOLD format: keep parquet or move to JSON | **REC APPROVED -- GOLD STAYS PARQUET;** platinum is the JSON tier; both live in the firm bucket. |
| 3 | D10-1 residual: the rule for scopes he has NOT named | **REC APPROVED -- DEFAULT: firm-shaped where the served data is client-confidential, product-shaped otherwise.** Plus the mechanism: the CRO enumerates every unnamed scope with evidence; Andrew ticks. |
| 4 | D10-2: legacy `opal-data-bd` / `-inf` / `-cot` disposition | **REC APPROVED -- DO NOT RULE IT NOW.** Formally deferred to the canon pass (the data-engineering bible). |

### The resulting target pattern for CLIENT data

```
INGEST     opal-data-assets/{vendor}/{firm}/bronze/     raw, byte-for-byte     (UNCHANGED)
SILVER     opal-data-assets/.../silver/                 typed parquet, deduped (UNCHANGED)
GOLD       opal-data-{firm}/gold/                       PARQUET. computed, complete, AUDITABLE.
                                                        the gold code lives in that bucket too.
PLATINUM   opal-data-{firm}/platinum/                   JSON. served, shaped for the screen.
                                                        <<< THIS IS THE CHANGE >>>
```

**The amendment in one clause: PLATINUM'S HOME IS PER-TENANCY, NOT ABSOLUTE.** For client data it is
the firm's own bucket; `opal-data-portal-v2` remains platinum's home for GENERAL (non-client) data.

---

## 3. WHAT THIS RESOLVES -- a live collision between two ratified laws

Card 1 existed because two laws could not both hold for client data:

- **Andrew-direct 2026-08-25 ~17:55Z** (`ANDREW_DIRECT_20260825_1755Z_GOLD_CONSOLIDATION_ONE_BUCKET_PER_PRODUCT_OR_FIRM.md`),
  verbatim: *"Then there is a platinum publisher that picks those files up and brings them in json
  format to the portal, opal-data-portal-v2."*
- **`docs/architecture/ADVI_APISCP_PRD.md` s.2, labelled NON-NEGOTIABLE:** *"Partner data is never
  copied to `opal-data-portal-v2` or any shared bucket. Each partner's data lives exclusively in
  `opal-data-{firmId}`. All portal reads go directly to the partner's origin bucket."*

**Card 1 resolves it in favour of firm separation.** The live scoped route already behaves this way
(`/api/scoped/advisor-intelligence/*` -> `/gold/*` -> `s3://opal-data-{firmId}/gold/`), so the ruling
ratifies observed behaviour rather than ordering a move.

⚠ **CAVEAT ON THE ADVI CITATION, STATED BECAUSE IT IS LOAD-BEARING:** `ADVI_APISCP_PRD.md` is dated
2026-03-10. Its compliance rule was read from the document, **NOT** re-derived against live CloudFront
behaviours or bucket policy. The bible's census re-derives it before it is quoted as current law.

---

## 4. ⛔ WHAT THIS DOES **NOT** RULE -- scope guards

**SURFACE, DO NOT ADJUDICATE (org/XXX.md). This record does not widen his four sentences.**

1. ⛔ **NO MIGRATION IS AUTHORIZED.** Nothing moves, no key is rewritten, no lifecycle rule, no
   bucket-policy edit. Several named surfaces are LIVE and written daily, and two feed
   `IRPT_BCKEND`'s open round. Moving a served key is NEVER#3 and is untouched by this.
2. ⛔ **D10-1 IS NOT FULLY CLOSED.** The approval rules the **DEFAULT RULE** and the **MECHANISM**.
   Per-scope assignment for the scopes he has not named **still returns to him** as a tick-list. A
   seat may NOT derive an unnamed scope's shape from the default and treat it as ruled.
3. ⛔ **D10-2 IS DEFERRED, NOT DECIDED.** Approving *"do not rule it now"* defers the call; it does
   not choose a disposition. The legacy-bucket disposition remains OPEN and is now formally waiting
   on the bible's census. *(Precedent for this exact distinction:
   `ANDREW_DIRECT_20260910_211xZ_OPEN_CALLS_ALL_RECS_APPROVED_EXCEPT_NO_ALARM.md` s.3 -- a blanket
   approval closes the calls whose RECs were answers; it cannot close one whose REC was that there
   is no answer yet.)*
4. ⛔ **NON-CLIENT PIPELINES ARE UNTOUCHED.** Andrew-direct, same session, verbatim: the four-tier
   discipline is *"mandatory"* for client data and a *"general rule of thumb ... recommended to be
   followed"* elsewhere. Pathfinder / TrueShares serving raw with no gold or platinum tier is
   **CORRECT, not debt**, and a conformance sweep must not flag it.

---

## 5. OWED ACTS

| # | act | owner |
|---|---|---|
| 1 | **Rule 17b amendment** -- the per-tenancy platinum clause. Rule 17b (`docs/doctrine/CLAUDE_ANNEX.md:411`) currently reads *"`platinum` serving under `opal-data-portal-v2/platinum/`"* with no tenancy split. **NOT landed by this seat** -- CLAUDE.md/annex is a law surface and the CRO does not write its own grant (SoD). | `1.0.0_SA_CTO` (authored the prior 17b/D10 amendment records) |
| 2 | The data-engineering bible: census the WHOLE estate, doctrine the CLIENT half. Decided in the CRO's own lane; needs none of the four calls. | `4.0.0_SA_CRO~D` (in flight) |
| 3 | Unnamed-scope enumeration -> back to Andrew as a tick-list (card 3's mechanism). | `4.0.0_SA_CRO~D` |
| 4 | Register defect, surfaced not chased: the Global Pipeline Consolidation work has a PRD at `docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md`, was assigned to D8 by Andrew's word, and is a member of NEITHER row (D10 members empty; D8 members are five other projects). Rule 17b cites `docs/architecture/D8_GLOBAL_PIPELINE_STRUCTURE_PRD.md`, which **does not exist on disk** (measured). | `0.0.0_AB_MSTR` (register owner) / `1.0.0_SA_CTO` |

---

## 6. PROVENANCE

**Prior art this ruling sits on, all read at HEAD this session:**
`docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md` v1.6.0 (the grand consolidation; s.2b END-STATE
HORIZON) . `docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md` . `org/missions/DIRECTIVES.yaml`
D8/D10 rows . `docs/doctrine/CLAUDE_ANNEX.md` Rule 17/17a/17b .
`ANDREW_DIRECT_20260825_1755Z_GOLD_CONSOLIDATION_ONE_BUCKET_PER_PRODUCT_OR_FIRM.md` .
`ANDREW_DIRECT_20260826_1810Z_ALL_RECS_APPROVED_SIX_CALL_SET.md` (D10-2 folded, D10-3 DEFERRED) .
`ANDREW_DIRECT_20260910_211xZ_OPEN_CALLS_ALL_RECS_APPROVED_EXCEPT_NO_ALARM.md` (D10-1 still open) .
`docs/architecture/ADVI_APISCP_PRD.md` .
`1.0.0_SA_CTO` msg-id 96116 (the D10 bucket/plane-hygiene measurement brief to this seat).

**Live AWS census run this session** (`comp-find --corpus aws`, vintage 2026-09-12T12:21:46Z,
denominator 21 of 37 S3_BUCKET nodes): 49 Financial resolves to FOUR identities -- `opal-data-bd`
(live) . `opal-data-49financial` (live) . `blackdiamond/49f/` and `blackdiamond/49financial/` inside
`opal-data-assets` -- and the scoped router keys on `X-Firm-Id`. The partner-firm module declares
four firms; only `opal-data-49financial` and `opal-data-demo` appear as new-pattern buckets.
**Carried, NOT re-derived by this seat:** the seven S3 disparities in CTO msg-id 96116.
