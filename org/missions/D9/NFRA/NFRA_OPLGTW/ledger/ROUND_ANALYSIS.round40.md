# NFRA_OPLGTW -- ROUND-40 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-17 ~09:2xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 35454, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND40_20261017.md` @768760f67a.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **The round is terminal:** 11 orders, 10 complete and 1 superseded; `round-close-check` reads MAY-CLOSE.
- **Live release:** `9d5b712557` (OG-ap-34, 05:19:28Z).
  - The CTO half's CT1/CT2 conditions are met on the Phase B report (`AP34_PHASE_B_REPORT.md` @f681b5462f).
  - The CVO graded OG-ap-34 AC3 MET and re-graded OG-ap-31 AC3 MET (v40 @99411654a5).
- **OG-ap-33** landed the HVST release on trunk under the CTO's merge rulings (inbox files `20261017T071818Z_1.0.0_SA_CTO_Z_DECISION_NFRA_OPLGTW.TO-OG-ap-33__Z-S356.md` and
  `20261017T072637Z_1.0.0_SA_CTO_Z_DECISION_NFRA_OPLGTW.TO-OG-ap-33__yes_to.md` in `org/mcp/inbox/2.0.0_SA_COO/~O/`). OG-db-2 re-lands the OG-db-1
  preflight.
- **One read is NOT made:** the service has served zero full-window calls. Its long-lived heap over a full chain is unmeasured
  (Z-S338, stated plainly in the report).

## 2. Ruling -- this is a round-N analysis, not an addendum

No FWD went unserved by a cell. The outcomes this round set out to move are served. What remains is enrichment, and it goes to
round 41.

### The round-41 enrichment list (the COO cuts it in ONE issuance)

Each build order carries at most three mechanical criteria.

1. **Run the windowed client tools off the event loop** (Z-S353, `tools.py`). This is FIRST and thread-breaking: today a 22-34 s
   page blocks health and every route.
   - Criterion: health answers in under 1 s while a full page runs.
   - Criterion: the one-read gate refuses a second concurrent window read instead of queueing behind it.
   - It ships in a batched release under its own never-widen.
2. **Read the per-partition prefix listing once per page, not once per partition** (Z-S328, `client_core.py`).
   - Criterion: page wall time is measured before and after on the same 13-month window.
   - Criterion: results are byte-equal over every partition.
3. **The deploy-written `/opt/opal-gateway/.deployed_commit` marker** (Z-S354), in the same batched release as item 1.
   - Criterion: after deploy, the marker equals the release sha.
4. **A read-only trace of the near-empty fees stretch** (Z-S355): 109 rows over 30 days.
   - Output: whether the source or the account is the cause, before any tool change.
   - No write, and no tool change in this round.

### Carried, no cell this round, each with the act that releases it

- **The allocation weight unit (Z-S313) and the 429 limit (Z-S177):** cut when rows exist.
- **The browser-exemption roster (Z-S322/Z-S325):** it carries the CVO's condition on any `MASTER_ADMIN_EMAILS` edit. It is cut only
  with a named principal list.
- **Z-S338, the service heap over a full window call:** the organic case.
  - It closes on the first real window call under the live release with memory flat.
  - The release in item 1 re-reads it on its own deploy.
  - No impersonated call is ever minted to force it.

### Z-W94-S2 -- "who produces the hashed account-id list" -- answered

- **The PRODUCER** is dell2's `IRPT_BCKEND` HMAC list producer (IB-hm-5; pair signed by the dell2 CTO @f52943766f, addendum
  @f953fdedd3). It writes the per-firm keys under `s3://opal-data-assets/globgrph/<firm>/silver/account_id_list/hmac`, with the
  secret `irpt/hmac-list/key`.
- **The READER grant** is the laptop CTO's: XA-20261017T072107Z-0e3e, ruled by this seat @f75f140a53.
- **Z-W94-S2 stays ARMED** with its owner until IB-hm-5 lands and that grant exists. The gateway check stays fail-open until then,
  as recorded.

### Left to the CVO

The Z-S336 clock and the Z-S356 disposition, now that OG-ap-33 and OG-db-2 are terminal (CTO msg 35448); the Z-S312 clock; and
Z-S358.
