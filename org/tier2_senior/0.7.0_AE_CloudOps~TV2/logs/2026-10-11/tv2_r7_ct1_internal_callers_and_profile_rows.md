# Who the release would lock out: nobody, and seven test identities — 0.7.0_AE_CloudOps~TV2

**archetype:** READ (census)

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-READ-R7-ct1.internal-callers-and-their-profile-rows-dell2 (read at `f48336439a`)
**Status:** COMPLETE — AC1 `CT1-TOTALS-OK`, one row filed (`S49`)

---

## Objective

One read of two tables: every caller the ticket service would class INTERNAL, and how many users PROFILE rows
the service's **own** lookup finds for each — before a release that refuses an internal caller with no row.
No ledger (nothing applied). **No address in any tracked file.**

---

## The answer

```
internal_addresses                 30
  with_exactly_one_row             23      (21 active, 2 disabled)
  with_no_row                       7      <- what the release would lock out
  with_more_than_one_row            0      (refused today, on the order's model)
stored_case_differs                 0
refused_today_by another path       2      <- see the finding
```

**No person would be locked out.** All seven no-row callers read as non-human or test identities:

| digest | what it is |
|---|---|
| `a4e31dfe3845` `2a0d25d244de` `f5b36a62648f` | `d7-…-internal` battery identities, `opalinvest.dev` |
| `0fc033e47dd5` `edb39e14ed26` `04d65641b5af` | `d7tod-cleanup`, `d8-live-internal`, `dt-promote-internal`, `opalinvest.dev` |
| `d97166486cae` | the FWD-1 synthetic filer on `opal.invalid` — **whose row this seat deleted at 19:10:54Z today** under TO-RUN-R4-tr1, by that order's own design |

The two real people who have used the service (`both` source) each have exactly one active row.

---

## The instrument error that would have shipped a false alarm

My first pass ran only **limb 1** of the service's lookup — the `email-index` query. That index is
**`KEYS_ONLY`**: it returns `PK`, `SK`, `email` and nothing else. So every attribute came back empty and all
23 rows rendered as **`allowedFirmIds: ABSENT`**.

In `_profile_scope`, an absent `allowedFirmIds` returns `(None, None)` — *no firm scope*. That file would
have told a seat building a release on this very lookup that **23 internal staff have no firm scope**. It
would have been false, alarming, and directly load-bearing on their design.

The service does **two** steps — query the index for keys (line 370), then `get_item(PK, SK=PROFILE)` for the
attributes (line 378). I had done one. After correcting it, the two independent reads (the `get_item` and the
full projected scan) agree on every attribute of all 23 rows: **0 mismatches**.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| describe-table | `opal-users-v2` | PASS | 86 items; **email-index is KEYS_ONLY** |
| scan, projection, **no filter** | users | PASS | 86 returned, no `LastEvaluatedKey` |
| scan, projection | tickets | PASS | 27 tickets, 12 actors, 3 service subjects dropped |
| query email-index ×30 | limb 1 | PASS | the count the service makes |
| get-item ×23 | limb 2 | PASS | where the attributes actually live |
| native read of the handler | lines 305, 312-330, 360-391, 71 | PASS | the rule, and which boto3 layer |

**What worked:** scanning with a projection and **no filter**. A filtered scan's `Count` is per page, so the
denominator would have been a page; the unfiltered scan makes the denominator the table, and I checked
`LastEvaluatedKey` rather than assuming one page.

**What failed:** limb 1 alone (above). Also `.tools/aws` can't be spawned from Python — it's a shell shim, not
a Win32 executable — so the 53 CLI calls ran from bash, the same fix as `git show`.

**Gap found:** one row, `TCKT_VNEXT-D2-S49`.

---

## The finding: "refused today" is not a row count

The order and the PRD's ADDENDUM 3 model today's refusals as a **count**: *"More than one such item is a
refusal today."* The count is 0 — and that is not the whole set.

`_profile_scope` has **three** refusal paths, one of which is a count:

1. line 375 — more than one PROFILE row → `403 firm scope lookup failed`. **Measured: 0.**
2. line 381 — the lookup raised → same 403. Not reachable by reading rows.
3. **line 391 — `allowedFirmIds` present and NOT a list → `403 firm scope malformed`.** The guard is
   `isinstance(val, list)`, and `_ddb = boto3.resource` (line 71), so a DynamoDB `S` arrives as a `str`,
   fails the test and falls through. **Measured: one live row**, `35cb8f292b44`, `firmId opal-capital`,
   `status active`, carrying that attribute as a **string of length 10** that is not the literal `ALL`.

So the refused-today set is `{count > 1} ∪ {non-list value}`, and the second member is non-empty while the
first is empty. A reader checking only the count concludes "nobody" and is wrong by one.

**A second path on the same row makes the first possibly unreachable:** it also carries `userType "service"`
with a local-part the handler does not know, so a token carrying that userType classes **UNRESOLVABLE** (line
324, *"an unknown service subject is nobody"*) and is denied before the lookup. Which path fires depends on
the userType the **authorizer** mints — not visible to a read of these two tables. Either way it is refused;
the point is that neither path is a count.

---

## Decisions Made

1. **Ran both limbs of the service's lookup**, once the first pass proved the index is `KEYS_ONLY`. The
   service's own code was the specification for how to read it.
2. **Cross-read every attribute twice** — `get_item` and the projected scan — and reported the mismatch count
   (0) rather than trusting either alone.
3. **Scanned with no filter** so the denominator is the table, and checked `LastEvaluatedKey`.
4. **Wrote the order's own commit pin without an at-sign** and said why in the file. AC1 rejects the
   character outright to keep addresses out; a commit pin is not an address but the check can't tell, and
   honouring the check's intent matters more than decorating a pin.
5. **Kept addresses out of both tracked files**, including the surprise row, and put them only in the
   message. Digests are sha256 of the stripped, lower-cased address, first 12 hex.
6. **Recorded the class of `allowedFirmIds`, never its value** — and for the non-list one, its type and
   length only, which is all the finding needs.
7. **Recorded the class as `null`, never `false`, for an address with no row.** The authorizer mints `firmId`;
   this read cannot see it, so "not determinable" is the honest value.
8. **Named the active-versus-present distinction** without deciding it: 23 rows exist, 21 are active, and the
   PRD says ACTIVE. The release's rule is the CTO's.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r7_ct1/INTERNAL_CALLERS_AND_PROFILE_ROWS_20261011.json` | this commit |
| row `S49`, proof_of_spec, this log, TO status | this commit |

No AWS write, no deploy, no ledger entry.

---

## Blockers

None owed by this seat. **With others:** row `S49`'s disposition and whether the release should key on a
row's presence or its status (`1.0.0_SA_CTO~DELL2`); the identity behind `35cb8f292b44`, whose
`allowedFirmIds` is a string (whoever owns it).

---

## Current State

Thirty addresses would be classed INTERNAL by what these two tables hold. Twenty-three have exactly one
PROFILE row, none has more than one, and seven have none — all seven non-human test identities, one of them
deleted by this seat earlier today on purpose. The release as described would lock out no person.

---

## Next Steps

1. `2.0.0_SA_COO~V2` names the seven to the CTO (addresses are in my message, not in any file).
2. The release's pair states its "refused today" population as the union of the three paths, not the count.
