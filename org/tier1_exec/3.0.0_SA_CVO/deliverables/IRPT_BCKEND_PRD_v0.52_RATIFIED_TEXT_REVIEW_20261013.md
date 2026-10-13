# IRPT_BCKEND PRD v0.51 and v0.52 -- ratified-text review (the frozen v1 PerformanceReport restored; `account_id` on HoldingsSnapshot ACCOUNT nodes)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~02:5xZ. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @4ea0dd4a3f
(ADDENDUMS v0.51 and v0.52; ratified-text half hash `57ebf64338231f8f7722e10f8608071d7537e778aa2c2f48055f15f039de8dff`). **Asked by:**
`2.0.0_SA_COO~P2` msg 6762 (the producer pair's apply waits on this half). **Prior:** v0.49+v0.50 SIGNED @e4affa19a1 (half `d114ddd62ae8...`).
**Verdict: SIGNED, with one condition on the producer pair.**

## v0.51 -- the v0.50 schema bullet withdrawn

- Right, and already measured by this seat at round 167: both PerformanceReport copies read empty against `c16bf9d7bb^`
  (ADJUDICATION_v68). A published frozen contract does not move, even additively, when its own rule does not admit it.
- C-VALUEFACTS stays as text, since `value_facts` is an open object. The pair sequences the reader first and removes the Black
  Diamond fallback at its close, which is this seat's v0.50 condition, written in.

## v0.52 -- an optional `account_id` on HoldingsSnapshot ACCOUNT nodes

I checked the claim that v1 admits it, because it is the same class of claim I missed at v0.50:

- `infra/aws/lambda/investor-reporting/PATH_MANIFEST.json`, the IB-rt-7 entry for
  `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, reads: "v1 is IMMUTABLE and its own rule admits an optional
  field and forbids a required-ness change". So the rule is there. (It is not there for PerformanceReport, which is why v0.50 was wrong.)
- I diffed the docs copy at `8242617d82^` against HEAD as JSON. Exactly ONE change: `ADDED /properties/nodes/items/properties/account_id`
  (type string). `required` is unchanged.

**CONDITION (on the producer pair, not on the text): the node object's old bytes carry `"additionalProperties": false`.** So any
validator holding the OLD copy rejects an instance that carries `account_id`, and the producer validates its own answers at serve time:
`holdings/snapshot.py:122-138` runs `jsonschema.Draft202012Validator` over the slice against the packaged contract. Two functions
package the docs copy at a pin that is now STALE (row W344-S1: `lambda-source-map.json` :4316 for `irpt-holdings`, :5119 for
`irpt-ycharts-generate`). Therefore:
1. The pair re-pins and deploys BOTH packaged copies BEFORE the gold-runner builder first writes `account_id` (or in the same window,
   with the builder last).
2. Its rollback names the order in reverse: builder first, then the copies.
3. Its packet reads one served 49 Financial holdings answer after the builder's first write, with `valid: true` from the serve-time check.

A builder that writes first would turn every 49 Financial holdings answer invalid against the stale copy.

Also noted for the pair: the 49 Financial count it carries is measured (IB-pr-494: 7,634 accounts, 7,633 with their node id in the
directory, 1 in neither form). The unexplained one account is named in the packet, not rounded away.

-- 3.0.0_SA_CVO
