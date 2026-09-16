# PRD REVIEW -- MDPF_CANON v2.1 @6ab0a19bd4 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96552. `1.0.0_SA_CTO`'s note 96555 says which rows changed.

**Prior:** v2.0 was REFUSED on R1, in the review @`e57ea8b980`. The v2.0 stamp was never applied, because v2.1 landed
before it. v2.0's half (`aa9f1414...`) is superseded, and a stamp pinned to it would record a verdict on stale
bytes. That committed review stays the record of the v2.0 verdict.

**Read, UTC 2026-09-14, after 09:07:58Z:**
- The PRD @`6ab0a19bd4`. The working copy is identical to the pin.
- A section-by-section diff against v2.0 @`3514843a12`, through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- `LGIC_ENFORCE` v1.1 @`78128f29ea`: `key()`, `address()` and `lib/opal_naming.py` (`:152`, `:180-182`).
- `org/standards/NAMING_SCHEMA.json` v1.2 @`d6e0c3b74a`.
- `infra/logic/06_CONFORMANCE_LEDGER.md` @`6dab0d76a7`: X2 and section 4.
- The portal's callers @portal `ca8524a1`: `ModelPortfolios.tsx`, `aum.ts` and `portal-proxy.ts`.
- `infra/aws/lambda-edge/shared-advisor-router/index.mjs` @`40697fe79d`.
- This PRD's DEC-5 (brief half), read only for the assertion the route row inherits.
- `4.0.0_SA_CRO`'s v2.1 brief review @`f44f70c069`, read as a prior-record check.

**Half hash reviewed:** ratified-text `b5caa547cd1557238912a8dd083f8d1a464381e0aa7d99c245208036023b9d60`. It matches the
notifier's `b5caa547cd15`.

## VERDICT: REFUSE -- one change, R2, in the CONTRACTS route row. R1 is closed.

## THE DIFF OF THIS HALF, v2.0 -> v2.1

- **ENDPOINT is byte-unchanged,** so v2.0's finding carries: 8 of 8 outcomes verbatim, and every removed constraint is carried in CONTRACTS.
- **CONTRACTS changed on two rows, and only those:** the key-string row and the route row.

## R1 -- CLOSED

| check | v2.1 | against |
|---|---|---|
| five key segments | the vector `key("mdpf", "49financial", "platinum", "aum_metrics", "aum-metrics.json")` returns `mdpf/49financial/platinum/aum_metrics/aum-metrics.json`, which has five segments | `key()` returns exactly `{source}/{scope}/{tier}/{table}/{partition}` (`LGIC_ENFORCE` `:152`) |
| table and leaf case | `aum_metrics` is snake_case; `aum-metrics.json` is kebab-case | `NAMING_SCHEMA` `:35` |
| the partition slot | the served file, in the "named leaf" form | `NAMING_SCHEMA` `:36` |
| the bucket | `s3://opal-data-49financial/` | `address()` takes the bucket from the tier home rule and the scope's tenancy, never from an argument (`:152`, `:180-182`); `data_bucket` is `opal-data-{scope}`, LONG form (`NAMING_SCHEMA` `:39-40`) |
| the claim | "Every NEW address comes from `key()` and `address()`" | the combined slice is named as the one exception: historical, tier-first, not produced by a builder, and unmoved. The contradiction R1 named is gone |

**What this does not claim:** the vector was read against the written contract. It was not run, because
`lib/opal_naming.py` does not exist yet (N3).

## R2 (blocking) -- the route row refuses identities that the router it inherits from admits

**The row:** *"any firm segment is served ONLY when the viewer's asserted tenant equals that segment ... another firm's
session is refused"*. It also says *"the portal is frozen, so no caller changes"*.

**What the frozen caller does** (`portal/src/pages/ModelPortfolios.tsx` @`ca8524a1`):
- An internal viewer is `isInternal() || isDev()` (`:352-353`). Internal means firmId `opal-capital` (`:534`).
- Internal viewers keep the firm selector, under Andrew's MDPF_SCOPED.S5 *"Internal users keep the selector ... (no regression)"* (`:357-358`).
- For internal viewers, `effectiveFirmId` is the selected firm (`:371-372`).
- Every per-firm fetch is keyed by `effectiveFirmId` (`:410-411`, `:477-483`, `:512-519`).
- Those fetches request `/api/general/mdpf/${firmId}/...` with no `?firm=` parameter (`aum.ts:534`, `:614`, `:882`; `portal-proxy.ts:532`).

So an `opal-capital` session asking for `/api/general/mdpf/49financial/aum-metrics.json` asserts tenant `opal-capital`,
which is not `49financial`. Under the row as written, that session is refused, for every firm, as each firm's origin
flips.

**What DEC-5 says the row inherits:** *"The assertion is the one the scoped router already applies to
`/api/scoped/*`"*. That router compares resolved BUCKETS, not segments, and its comment says why
(`shared-advisor-router/index.mjs:367-373` @`40697fe79d`): *"no narrower (the mockadv->bd alias and opal-capital ?firm=
proxy keep working). A bare pathFirm === firmId test would instead REFUSE both of those legitimate identities."*

The route row writes the exact test that router rejected. So the half this seat signs disagrees with the brief half
beside it.

**The ENDPOINT does not ask for the narrower rule.** FWD-2 is *"another firm's advisors cannot reach them even with
the address"*. Opal's own staff are not another firm's advisors.

**Why it blocks.** This row is the access rule on served firm data, and it will be ratified. Either:
- the literal text is built, and Opal's staff lose per-firm Model Portfolios on a frozen portal, against S5; or
- L5 builds the router's rule, and the ratified text does not say what was built.

**Fix, touching only this row:**
- Replace segment equality with the tenancy boundary the router already enforces. A firm segment is served to that firm's tenant (including its aliases) and to internal Opal staff; any OTHER firm's session is refused.
- Say that for internal staff the path segment carries the selection, because the frozen portal sends no `?firm=` on these requests.
- If the intent is to refuse staff instead, the row must say so and name the selector regression. The portal is frozen and S5 is Andrew's word, so that choice is his.

### The rest of the route row holds

- **The URLs are real:** the portal calls exactly `/api/general/mdpf/{firmId}/...` (`aum.ts:534`, `:614`, `:882`; `portal-proxy.ts:532`).
- **The firm ids match:** they are LONG form (`ModelPortfolios.tsx:247-249`), the same as the key-string row's `{scope}`.
- **`global` is unchanged:** it keeps its general handling, which agrees with the key-string row's one exception.
- **Separation holds:** refusing another firm's session agrees with FWD-2.
- **The finding is new:** `4.0.0_SA_CRO`'s review @`f44f70c069` closed R3 on this same mapping. It has 0 hits for internal, opal-capital, staff or selector across 74 lines; the positive control, tenant|route|R3, has 7 hits.

## NOTES (non-blocking)

- **N1:** carries from v2.0, unchanged.
- **N2:** carries from v2.0, with one addition. Ledger section 4 still names the firm slices' migration target tier-first, `opal-data-{firm}/platinum/mdpf/...` (`06_CONFORMANCE_LEDGER.md:110`). v2.1's five-segment key now contradicts it. That is the ledger's to reconcile, not this PRD's.
- **N3 -- the vector is not exercised yet.**
  - `NAMING_SCHEMA` uses "leaf" for two things: the `{object}` (`:27`) and a partition form, "a named leaf" (`:36`).
  - v2.1 fixes one reading with one vector: the served file goes in the partition slot, with `object=None`.
  - Nothing yet binds `LGIC_ENFORCE`'s builder to that reading. If this vector goes into the shared vector file its builder is tested against, the two agree by test, not only by text.
- **N4 -- X2 covers the home, not the key order.**
  - The combined slice stands "(X2)". Ledger X2 (`:131`) covers the R7 composite branch and the portal-v2 home, not the tier-first key order.
  - The v2.0 review put that widening inside its fix (ii). It is a change to the ledger, which this PRD does not own, so it is carried here as a note to the ledger's owner.
  - The row itself now names the key as historical and tier-first, so the exception is visible in the ratified text.

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s, and SIGNED.
- **That the compatibility mapping can be built.** M9 reads the live behaviours at L5.
- **The builder's actual output.** It has not been run.
- **How a refused per-firm fetch renders on the page.** Not measured.
