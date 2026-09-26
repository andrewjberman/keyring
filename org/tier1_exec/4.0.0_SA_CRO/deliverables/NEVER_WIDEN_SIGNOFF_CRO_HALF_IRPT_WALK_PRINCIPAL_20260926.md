# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the bounded Opal-class walk principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_WALK_PRINCIPAL_20260926.md`
blob `fe8e8d8979727c07cf6bbf469640314cc9045d7b` @`87c1396686`. The blob is the same at HEAD, at the pin and on disk
(read 2026-09-26 ~02:4xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_WALK_PRINCIPAL_20260926.md` @`ba29004a1b`.
**Routed by:** 1.0.0_SA_CTO msg 101083. This seat is not in the act.
**Signed:** 4.0.0_SA_CRO, 2026-09-26 ~02:5xZ.

## VERDICT: SIGNED, on the blob above, with the 1.0.0_SA_CTO half's two additions, and the three items named below.

## What this seat measured (a different instrument from the packet's source reading)

1. **The rollback holds on the SERVED bytes, not only the source.**
   - This seat downloaded `opalinvest-auth-handler` (LastModified 2026-09-17T19:08:48Z, CodeSha256 `h1tnQVRp...`) and
     read `dist/index.mjs`.
   - The served bundle holds all three status guards (`status!=="active"` -> `Account disabled`), matching the three in
     source:
     - login, `auth.ts:105`;
     - MFA verify;
     - refresh, `auth.ts:537`.
   - The served refresh path re-reads the row and throws `User not found` when it is absent. So a refresh token dies
     with K1, which is the property the packet's "token life <= 60 min" rests on.
   - The served token mint sets tier `internal` only when `firmId` is `opal-capital`.
   - This closes the packet's own named gap for the auth-handler ("served bytes were NOT compared"). It stays open for
     the authorizer and the edge, which bound REACH, not rollback.
2. **No other writer or trigger fires on K1.**
   - `opal-users-v2` has `StreamSpecification: null` and no event-source mapping (`list-event-source-mappings`, 0
     rows).
   - The item put reaches no second system, so the `DeleteItem` is the whole K1 rollback.
   - The table held 79 items at this read.
3. **No source drift since the packet's pin.** `git diff 2df913f644 HEAD` over the auth-handler source, the portal
   authorizer and the edge validator is empty.

## Named items the signature carries

1. **The authority reading widens the record's own words.**
   - Andrew's verbatim delegation is "have an agent do those walks and record HAR". It names the Inflection Orion call
     and the first live Analysis upload among the acts.
   - The CTO's record of that word (@`37025a10e9`, "What it binds" item 4) adds that the agent "signs in as
     IRPT_BCKEND's approved bounded test principal (IB-rtf-3...)". That principal is a 49financial advisor, and it
     cannot reach two of the delegated acts (packet, "Why not the IB-rtf-3 principal").
   - This seat signs on the verbatim word, which delegates acts only an internal-class login reaches. The record's
     gloss is not Andrew's word.
   - This seat is putting the widening to Andrew in the same turn. If he vetoes before the create, the act does not
     run.
2. **The HAR is the one key with no rollback.**
   - The committed HAR keeps client data from two firms (49financial and Inflection), per the packet's step 5.
   - Once the commit is on origin, it cannot be withdrawn.
   - It is in scope ("The HAR and the screenshots are committed as the drain artifacts", same record). It is named
     here because the packet's key list (K1, K1-CRED, K2) does not carry it.
3. **Reach is bound by script, not mechanism** (packet, "THE BLAST RADIUS"). This seat accepts it on the same terms as
   the CTO half. The committed HAR is the proof, and 1.0.0_SA_CTO grades it at the drain.

## Not measured by this seat

- The served bytes of `opal-portal-authorizer` and `auth-validator-edge`.
- The one-use Orion plan gate's `PERFORMANCE_USE#` refusal.
- The `db.ts` line citations.
