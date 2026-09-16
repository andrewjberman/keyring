# PRD REVIEW -- ADVI_FIRMBKTS v1.0 @ecac007bf3 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96558.

**Read, UTC 2026-09-14, 09:40Z to 09:55Z:**
- The PRD `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` @`ecac007bf3`. The working copy is identical to the pin.
- The endpoint `ENDPOINT_FWD_D8_LEGACY_FIRM_BUCKETS_MIGRATION_20260913.md` @`e2210bf34c`, past its outcome block: the amendment record, "FOUR THINGS THE CUT SURFACED", and the ~18:4xZ ruling stamp.
- `org/standards/NAMING_SCHEMA.json` v1.2 @`d6e0c3b74a`.
- `LGIC_NAMING` S1 (`LGIC_NAMING_PRD.md:125`) and its channel row S6.
- `LGIC_ENFORCE` v1.1 @`78128f29ea`: `key()` and `address()` (`:152`, `:180-182`).
- `MDPF_CANON`'s counterpart row (`MDPF_CANON_PRD.md:180` @`6ab0a19bd4`).
- The bucket template `infra/aws/terraform/shared-infra/s3-49financial.tf` @`37931439cf`.
- The portal's ADVI callers @portal `3ade1aba`: `advisor-intelligence.ts` and `adviKeyRepoint.ts`.
- `shared-advisor-router/index.mjs` @`40697fe79d`.
- DEC-3, DEC-14, F4 and the SURFACE MANIFEST (brief half), read only for what the CONTRACTS rows rest on.
- `sequence-check.py --project ADVI_FIRMBKTS`: stage 2; HELD at DECOMP by design; no new flag.

**Half hash reviewed:** ratified-text `d4258a7d01a36218cbd0a93fbcfe8fb82529b0c6de36c328bc3a67b09a5ebfa9`. It matches the
notifier's `d4258a7d01a3`.

## VERDICT: REFUSE -- three changes, each on one CONTRACTS row. The ENDPOINT holds.

## ENDPOINT -- 8 of 8 outcomes carried verbatim; every constraint outside the block is carried

**The instrument:** a parser over both documents' FWD blocks, field by field, against the endpoint @`e2210bf34c`.
- **Title and ACCEPT:** EQUAL for FWD-1 through FWD-8.
- **DONE WHEN:** EQUAL for 7 of 8. FWD-6 differs only by the endpoint's inline *"⚠ CARRIES THE ONE GENUINE WAIT ..."*. That is an annotation, and the spine keeps it out of the section (`CANONICAL_FABRIC_WORKFLOW_20260901.md:165`).

**The constraints outside the outcome block, each carried:**

| endpoint item | where this half carries it |
|---|---|
| Amendment 1: FWD-3 depends on the D14 registry | the identity-registry row: consumed, produced by `LGIC_ENFORCE` |
| Amendment 2: two acts at mint (template read logging, and the trail selector) | the firm-buckets row: "born with ... read logging". The template now carries it as a born-with control (`s3-49financial.tf:17-29`) |
| Amendment 3: the quiet window rests on CloudTrail data events, not FIRMSEP | the decommission row: "a named instrument" |
| Things 1 and 2: FWD-6's wait; the 45-day window from read logging going live (card 2; its parking with `0.7.0_AE_CloudOps`, card 3) | the decommission row: 45 CONSECUTIVE days, no earlier than the instrument's observed-live stamp, counted after cutover; any other event restarts it. This agrees with 96488 and with `MDPF_CANON`'s FWD-8, which inherits it |
| Thing 2: FWD-4 driven, the organic case demoted | FWD-4's ACCEPT, verbatim |
| Thing 3: FWD-3 cut at APPLIED | FWD-3's DONE WHEN, verbatim |
| Thing 4: the string, since ruled source-first | the key-string row |
| Card 1: the fence on three conditions | the separation-rule row, consumed from `LGIC_ENFORCE` (E5, the sequence's manual gate) |

## CONTRACTS

### R1 (blocking) -- the platinum vector keeps a snake_case served name, and the schema it cites says served names are kebab

**The row:** `key("advi", "49financial", "platinum", "firm", "header_metrics.json")`, *"with the served file in the
partition slot the schema calls 'a named leaf'"*.

**The schema it consumes:**
- `NAMING_SCHEMA.json:35`: *"a platinum leaf is a kebab-case .json file (the served names)"*.
- `LGIC_NAMING` S1 (`:125`): *"a platinum leaf is a kebab `.json`"*.

**The world:**
- The portal asks for `/api/scoped/advisor-intelligence/platinum/firm/header_metrics.json` (`advisor-intelligence.ts:302`).
- Of the 15 served leaves `adviKeyRepoint.ts` lists, **12 are snake_case**, 1 is kebab-case and 2 are one word. The denominator is that file's entries, not the buckets.

**The sibling PRD reads the rule the other way.** `MDPF_CANON` v2.1 puts a KEBAB served file in the same slot
(`aum-metrics.json`). So two PRDs on one schema disagree about whether the rule binds a served file sitting in the
partition slot. The schema uses "leaf" for both the `{object}` (`:27`) and a partition form (`:36`), and its `:35`
parenthetical ties the rule to served names either way.

**Why it blocks.** These are the migration's served keys. As written, either:
- the builders or the naming gate refuse 12 of 15 names; or
- the ratified row violates the ratified schema on its own worked example.

This is the class `LGIC_NAMING`-S6 was filed for: an address the schema does not admit.

**Fix, touching only this row.** Say which rule governs a legacy served name:
- **(a)** it is kept byte-for-byte, as FWD-4 and the frozen portal's URLs imply, and the row names `LGIC_NAMING`'s admission of that exception as a dependency. This review files the row at `LGIC_NAMING`. Or:
- **(b)** the object is renamed to kebab-case, and the row names the edge's per-leaf name mapping.

The vector then follows whichever is chosen. REC: (a). Option (b) writes 12 names into an edge table, and FWD-3
exists to remove exactly that kind of hand-written list.

### R2 (blocking) -- the tenant assertion is the bare test the router rejects, so it refuses Opal's staff and aliases

**The row:** *"a scoped request is served only when BOTH the bucket AND the key's `{scope}` segment equal the session's
firm."*

**The row never defines "the session's firm" for the two identities the router admits today:**
- **Internal staff** (firmId `opal-capital`) reach a firm through `?firm=` (`advisor-intelligence.ts:81`, `:303`), and the router's opal-capital branch serves them (`index.mjs:227-241`).
- **Aliases:** `mockadv` maps to 49 Financial. DEC-14 calls it "a registry alias, never a scope segment", but the row does not say that the session's firm is resolved through the registry.

**The router's own comment** (`index.mjs:367-373` @`40697fe79d`): *"no narrower (the mockadv->bd alias and opal-capital
?firm= proxy keep working). A bare pathFirm === firmId test would instead REFUSE both of those legitimate identities."*
Read literally, the row is that test with a bucket check added.

**What is right in the row:** adding the scope check (DEC-3) closes LD-0442's latent hazard.

**Fix, touching only this row.** Define the session's firm:
- for a partner tenant, its firm as the registry resolves it, so aliases resolve there;
- for internal staff, the firm their `?firm=` names.

Then run both checks against that resolved firm. This is the same change 3.0.0_SA_CVO asked of `MDPF_CANON` v2.1's
route row (R2 @`e6462c2f67`).

### R3 (blocking) -- the serving grant is written tier-first, so it covers none of the keys this half rules

**The row:** *"Every firm bucket ... carries the CloudFront serving grants on `platinum/**` before its router row flips."*

**Under the key string two rows above,** the tier is the THIRD segment. Served objects live at:
- `advi/{firm}/platinum/...`;
- `mdpf/{firm}/platinum/...`, which is `MDPF_CANON`'s firm slice.

A grant on the key prefix `platinum/` covers neither.

**It breaks the counterpart.** `MDPF_CANON` consumes this row as *"the bucket ... carries its serving grants"*
(`:180`).

**Nothing else specifies the grant.** The template grants nothing today: its only policy is the cross-firm Deny
(`s3-49financial.tf` @`37931439cf`). So this row is the grant's only specification.

**Fix, touching only this row:** write the pattern in the key's own grammar, for example `*/{firm}/platinum/*`. An
S3 resource-ARN wildcard spans `/`. One grant per source also works. The same `platinum/**` appears in F4 and the
SURFACE MANIFEST (`:377`) in the brief half, for that half's reviewer to align.

### Also checked -- these rows hold

- **The gold vector:** `advi/49financial/gold/fact_account_gains/date=2026-09-11` with object `data.parquet`. That is five segments, and it agrees with `key()`.
- **The bucket rule:** `address()` takes the bucket from the tier home rule and the scope's tenancy (`LGIC_ENFORCE` `:152`); `data_bucket` is `opal-data-{scope}`, LONG form.
- **The firm-bucket tiers:** `{tier}` in a firm bucket is only gold, platinum, state or code, because bronze and silver go home (R4). That agrees with `MDPF_CANON`'s bronze in `opal-data-assets`.
- **The mapping table:** one destination or RETIRE per key class. An unplaceable key is a table fault (FWD-2). The two decision rows at Andrew are FWD-7 and FWD-8.
- **The registry and the separation rule:** both agree with `LGIC_ENFORCE` v1.1.
- **The served bytes:** they agree with FWD-4.
- **The decommission standard:** as in the table above; its terms match `MDPF_CANON`'s inheriting row.

## NOTES (non-blocking)

- **N1:** the entity-keyed family waits on `LGIC_NAMING`-S6, which is ARMED with `1.0.0_SA_CTO` as disarm owner. Until S6 disarms, FWD-2's *"nothing is left unplaced"* cannot be met for a firm holding that family. The row names the dependency, which is enough.
- **N2:** parity with `IRPT_BCKEND`, a named consumer, is NOT EVALUATED, because it has no PRD.

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s.
- **That either vector runs.** `lib/opal_naming.py` does not exist yet.
- **How many objects in the buckets carry snake_case leaves.** The 12 of 15 is the portal's served-leaf list, not a bucket census.
- **That the edge can build the tenant rule.** F6 reads the router at L5.
