# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND` IB-rte-2: the bounded test advisor principal

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-18 ~23:0xZ.
**Pairs with:** the COO half, `org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rte-2_TEST_PRINCIPAL.md` @`a0f05dda0c` (msg 98066).
**Authority for the act:** Andrew-direct 2026-09-18 ~17:3xZ *"Approved"* (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @`af794c77e3`); CTO round-4 analysis s.6/s.8 @`561d6e1cc9`.

## BOUND TO CONTENT, NOT TO A NAME OR A VERSION

This half signs the packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md` **at blob `3d9f57335b9893753973132ba5c4958b2622e24f`** (11,585 bytes).

Resolved by CONTENT at signing, on this seat's own instrument: `git rev-parse HEAD:<path>` and `git rev-parse f08295cc8f:<path>` **both** return that blob, and `f08295cc8f` is an ancestor of HEAD. ⛔ **IF THE PACKET'S BYTES CHANGE, THIS HALF DOES NOT TRAVEL TO THE NEW BYTES.** A re-cut packet needs a re-signature; that is the whole reason the binding is a hash and not `IB-rte-1`.

---

## 1. WHAT THIS HALF SIGNS -- the blast radius, key by key

I sign **K1** and **K2** exactly as the packet's key table shapes them, and no wider.

- **K1 -- ONE item in `opal-users-v2`**, `PK = USER#usr_irptrte_<epoch>`, `firmId = 49financial`, `advisorKey`/`advisorId = abby_horton`, e-mail under the reserved `.test` TLD, **no phone, no MFA enrolment**. **May touch:** that one PK and nothing else in the table. **Rollback:** `DeleteItem` on the same PK, **verified by a consistent-read `GetItem` on that PK returning no `Item` key at all** -- the verification is part of the rollback, not a follow-up to it.
- **K2 -- the session token** from `generateAccessToken()` on a normal login through the real portal auth route. **May touch:** nothing persistent. **Rollback:** none needed; it expires on its own TTL. ⛔ **The token, the `Authorization` header and any `get-secret-value` output are NEVER recorded anywhere** -- not in evidence, not in a log, not in a commit (bound 6). The private key is read BY NAME (`opal/auth/jwt-private-key`), never read out.

⛔ **K3 AND K4 ARE NOT AUTHORIZED BY THIS HALF, AND THEIR ABSENCE IS THE ACT'S SHAPE, NOT AN OVERSIGHT.** No `ownership_map.json` row for `abby_horton`; no annotation in 49financial's `directory.json`. The packet names them as NOT NEEDED precisely so a half cannot silently assume them, and I sign that reading: **if IB-rte-2 discovers it needs K3 or K4 to proceed, that is a STOP and a new packet, not a widening of this one.**

**The entitlement claim I am signing** is narrow and I restate it in my own words so it cannot be read wider: a token minted against K1 carries **exactly `abby_horton`'s already-live entitlement in 49financial** -- no broader and no narrower -- **because no new grant is minted anywhere.** The act adds an authentication row; it adds no authorization.

## 2. ⛔ THE CONDITION THIS HALF ADDS -- THE ENTITLEMENT PROPERTY HAS A SECOND WRITER

The blast radius above rests on a property (*"`abby_horton`'s existing entitlement"*) that **K1 is not the writer of.** K1 writes the auth row; the entitlement is written by the **ownership map**. CLAUDE.md's never-widen line: *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N writers needs N rules read, and N is a number the half PRINTS."*

The packet's census is excellent and I rely on it -- **6 of 263** principals can write `opal-users-v2`, no resource policy, 0 UNKNOWN. ⚠ **BUT THAT CENSUS COUNTS THE WRITERS OF THE TABLE, NOT THE WRITERS OF THE ENTITLEMENT.** Those are two different properties, and this is the exact shape that cost `NFRA_CLDGRPH` W2-S67/S98: both halves read the one producer's rule on a surface a second writer also set.

**So this half signs CONDITIONALLY on a guard IB-rte-2 runs AT EXECUTION TIME, not on a fact measured now** (the fact is perishable; a measurement taken at signing is stale by the act):

1. **Immediately before creating K1**, re-read 49financial's live ownership map and confirm `abby_horton` is **present** with a grant set. **If `abby_horton` is absent, the act mints a NEW entitlement rather than reusing one, the blast radius in s.1 is FALSE, and this half does not cover it -- STOP.**
2. **Record the grant counts at that moment** (the packet measured 43 accounts / 18 relationships this run). They are the blast radius' actual magnitude; a materially different number at execution is not a blocker but **is** a row, because the half's radius was signed against that shape.
3. **The principal's lifetime is this order's ledger interval only.** Deletion is IB-rte-2's own last arm, or earlier on any STOP.

## 3. BOTH BRANCHES ARE COVERED -- THIS HALF PREDICTS NO OUTCOME

CLAUDE.md: *"Where a half names an EXPECTED OUTCOME ... the half covers BOTH branches or it is not signed."*

The packet measures, live and against the REAL production wiring, that a genuine `abby_horton`/`49financial` request is refused **`UNPROJECTED_GRANT`** before the served branch is reached (0 of 22,646 grants join; 0 of 13 live modules pass `id_projection`). ⛔ **I DO NOT SIGN THAT AS AN EXPECTED OUTCOME AND THIS HALF DOES NOT DEPEND ON IT.** Whether IB-rte-2's arms read REFUSED or SERVED, **the keys, the radius and the rollbacks above are unchanged** -- K1 is one row and K2 is one ephemeral token either way. The half covers the act, not the verdict.

⭐ **And it is INDIFFERENT to the id-space ruling.** If this seat's L4 ruling on the id space lands as (b) -- re-key the ownership map's producer -- the principal's shape does not change, so this half still stands. The COO half says the same; we agree, independently.

## 4. MY OWN VERIFICATION -- a DIFFERENT instrument, not a re-read of the packet

⛔ *"A second seat's confirmation via the FIRST seat's method is REPETITION, not corroboration."* The COO half read the packet. I checked a citation the packet's advisor-id reasoning rests on, **by printing the bytes** rather than by reading the prose about them:

`git cat-file -p HEAD:infra/aws/lambda/investor-reporting/_ids/ids.py`, lines 69-74:
```
KINDS = {
    "account": "acc_",
    "relationship": "rel_",
    "client": "cli_",
    "firm": "fir_",
}
```
**Four members; no `advisor` kind.** Negative control: `advisor` occurs exactly ONCE in the whole file, at `:307`, inside a docstring naming the `_scope.advisor_grant` callable -- **not** a kind. **So the packet's substantive claim (W1-S21: the advisor id is a raw identity-plane string, not an issued typed id) is CORRECT**, and using `abby_horton` as `advisorKey`/`advisorId` is the right shape rather than a shortcut.

⚠ **ONE NOTATIONAL CORRECTION, RECORDED BECAUSE A LATER READER WILL GREP IT:** the packet renders this as `KINDS = {"account", "relationship", "client", "firm"}` -- a **set** literal. It is a **dict**; those four are its KEYS and each carries a prefix value (`acc_`, `rel_`, `cli_`, `fir_`). **The conclusion is unaffected** -- the membership is identical and there is still no advisor kind -- but a reader who copied the set form would mis-handle `KINDS.items()` at `:77` and `KINDS[kind]` at `:218`/`:278`. Not a defect in the act; a defect in the quote.

## 5. ⛔ WHAT THIS HALF DOES **NOT** COVER -- named so nothing is read into the silence

1. **FWD-11's SSM parameter.** `/opal/irpt/opal-principal-roster` does not exist (`ParameterNotFound`, measured live in the packet's run). **Creating it is a SEPARATE infrastructure act with its OWN sign-off.** This half does not authorize it, and IB-rte-2 must not create it as a convenience.
2. **The identity provider's own admin surface.** The writer census is IAM-shaped; an admin/signup flow inside `opalinvest-auth-lambda-role`'s Lambda could admit a wider population than the six IAM principals, and no census here can see it. The packet names this blind spot itself -- I am ratifying that it stays NAMED and UNCLOSED, not signing it away.
3. **The already-issued-JWT-after-deletion question** (the packet's negative control 4): deleting K1 does not necessarily invalidate a token already minted against it before its own TTL expires, because the row's existence is not itself an input to `_scope.resolve`. **This is an EXPOSURE, not an incident** -- nothing has been admitted by it, because nothing has been created yet. It is IB-rte-2's to measure and file, and it is a reason the TTL and the ledger interval both matter.
4. **Any second principal.** One principal, one firm, one order.

## 6. WHO MAY EXECUTE

⛔ **NOT A WORKER.** This is a write to the production authentication plane, outside every `<paths>` grant on this project, and the alternative path (a hand-signed token) is forbidden by bound 6. **The operator is `0.7.0_AE_CloudOps` or Andrew**, exactly as `RT2_test_principal_human_gated.md` names and the packet restates. A ledger entry in `org/critical_paths/change_management/` is opened before the act and closed at completion, per CLAUDE.md's half-landed rule.

---

## VERDICT

**CTO HALF: SIGNED**, bound to blob `3d9f57335b9893753973132ba5c4958b2622e24f`, subject to the s.2 execution-time guard (ownership-map presence of `abby_horton` re-read immediately before K1; absent -> STOP) and the s.5 exclusions.

With the COO half @`a0f05dda0c` at HEAD, **both halves required by CLAUDE.md's never-widen line are now on file for IB-rte-2's act.** ⚠ This clears the SIGN-OFF gate ONLY -- IB-rte-2 remains gated on IB-rte-6 by `2.0.0_SA_COO~B`'s own measurement (W1-S22: the served path refuses every live advisor `UNPROJECTED_GRANT` today), and that gate is the COO's, not this half's.
