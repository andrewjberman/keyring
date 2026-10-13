# L4-R review, NFRA_OPLGTW PRD v2.7, ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-13 ~21:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 33762 and 33765 (both acked). **Bytes reviewed:**
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @27ba6b6191. The working tree equals the pin.
`git diff 713305ee56 27ba6b6191` was read whole: the version bump, one clause of FWD-21's ACCEPT, and the v2.7 addendum.
Half hash at review: `e5d56318afab`. Prior: v2.6 SIGNED, review @e2e0025bf0.

## What changed

FWD-21's ACCEPT changes in three ways:
- "Grants go through the existing grant writer (one writer)" is replaced. V1 now admits by IDENTITY through OG-tg-1's
  Opal-user predicate: the opalinvest domain, and no `#ext#` guest.
- A non-Opal principal, or a prefix outside the list, is refused before any S3 call. The grant writer writes nothing
  for V1.
- A per-person harvest grant comes with NFRA_MCPORTAL's control outcome, through the one existing writer.

## Sources read

- **Andrew's call 8** (`ANDREW_DIRECT_20261013_200xZ_..._HARVEST.md:5`): "available for opal users only for now, which
  will be managed via opalgateway entitlements. There should be no undue holds on that in the interim, those policies
  merely need to be designed ...". Identity admission now and per-person entitlements once designed is that sentence
  in order. It is neither wider (the predicate is "Opal users") nor narrower (no grant build stands in front of V1).
- **The predicate exists at HEAD:** `infra/aws/ec2/opal-gateway/app/tools.py:1042` returns
  `"#ext#" not in low and low.rsplit("@", 1)[1] == identity_scope.OPAL_USERS_DOMAIN`. It is OG-tg-1's code, which is
  NOT on the live ref: it is part of the unreleased r30 (Z-S101). v2.6 item 3 already orders FWD-21 after that release,
  so the dependency is stated.

## Verdict: SIGN

The clause resolves a real internal conflict. v2.6 said both "Opal principals" and "the existing grant writer", and that
writer has no harvest scope. The resolution follows Andrew's words. The one-writer rule is deferred to when a second
grant writer would actually appear; it is not dropped.

## Carried (not grounds)

1. **The census source no longer matches the admission.** PROOF asks for "a census of the asset-manager principals", and
   ACCEPT names them "from the grant store". Under identity admission, the grant store holds no harvest record, so the
   census should name the store it reads, for example the gateway's principal records or Entra. Otherwise a zero from the
   grant store would read as "no asset managers".
2. **The gateway role's own S3 reach is a separate widening.** "Refused before any S3 call" is the app-level gate. Serving
   the bucket also needs the gateway role to hold `s3:GetObject` on `opal-data-harvest`. This seat did NOT read whether it holds that
   today. If it does not, that role-policy change is a served-reach widening. Its release carries never-widen halves, and its name is builder
   output (rule 30). This text does not need to say so; the release pair does.
3. Item 3 of the v2.6 review stands: "refused on every prefix" is proved on two prefixes. A simulate or a refusal over all
   24 closes the quantifier.

-- 3.0.0_SA_CVO~Z
