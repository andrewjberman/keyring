# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 2210-2255Z

## NFRA_OPSEC202609.TO-OP-S-10E: the SIGNER's two key reads are now BOUNDED. The rotation's write side is fixed

**archetype:** DEPLOY

Fifth segment. Follows the second STOP (`..._2145-2210Z_..._SIGNER_STOP`), which the issuer
accepted and turned into this cut — noting the STOP landed on a blind spot in the issuer's own
four conditions, all of which were consumer-side.

## Outcome

`opalinvest-auth-handler` read **both** JWT keys into bare scalars with no time component. Both
now resolve through one bounded, single-CURRENT read. **Nothing rotated.** Proof-of-spec **VALID
rc=0**, six of six; ledger CLOSED 5/5; TO flipped `complete`.

```
BEFORE  if(pq) return pq;                       // private -- unbounded
        if(cq) return cq;                       // public  -- unbounded
AFTER   let Q=yZ.get(q); if(Q && $-Q.atMs<F3) return Q.value;   // bounded, per secret id
        ... {current:J}=Y3(z.SecretString); return yZ.set(...),J   // CURRENT only, a STRING
```

| criterion | verdict |
|---|---|
| S10E-AC1 | PASS — baseline unmoved; both reads re-confirmed unbounded before any change |
| S10E-AC2 | PASS — both bounded, each single-key, on the deployed bytes |
| S10E-AC3 | PASS — origin cache unchanged; TTL constants separated on structure |
| S10E-AC4 | PASS — a **real login** exercised the changed path end to end |
| S10E-AC5 | PASS — 0 add / 1 change / 0 destroy, **0 wafv2**, measured |
| S10E-AC6 | **UNVERIFIABLE-BY-INSTRUMENT** — judgment, reserved to `3.0.0_SA_CVO~Z` |

## A TTL, explicitly not two slots

The remedy shape was the thing to get right. A verifier accepts current-or-previous; **a signer
must know which key is CURRENT**, and a second slot would let it sign under a retired key. So
`getCurrentKey` returns a **string**, not a slot pair — it destructures `current` and discards
`previous`. It reuses `parseKeySlots` deliberately, so the signer survives the shape change the
rotation itself introduces (bare PEM today, `{current, previous}` envelope after). Keyed **per
secret id**, because this consumer reads two secrets through one function and a shared scalar
would have handed the private key back for a public-key read — the defect being fixed, wearing a
different mask.

## Three things worth carrying

**1. `previous` appears in the bundle, and it is not a two-slot path.** A careless read would have
called that a FAIL. All seven occurrences were enumerated with context: five inside
`parseKeySlots`'s own return shape, two inside the **origin secret's** pre-existing overlap
(TO-OP-S-3's, correct). **The decisive test was the ABSENCE of `verifyWithSlots`, not the presence
of a word.**

**2. The mutant showed which assertions actually work.** Planting a mutant that hands the signer
`previous` gave 3 passed / 6 failed — and **the two cache-mechanics assertions still passed**. A
timing-shaped test cannot see a wrong-VALUE defect; only the identity assertions caught it. Worth
knowing for anyone testing a cache.

**3. Both terraform patterns now exist in one root, and the difference decides whether a code
upload is a deploy or a no-op.** `session-analytics` hardcodes `source_code_hash` (upload alone →
"No changes"); `auth_handler` resolves it through a `data` lookup (upload alone → a real plan). I
checked which one applied here rather than carrying yesterday's lesson across.

## AC3's real content: separating two identical numbers

`300000` went 1 → 2 in the bundle. The origin window is `z2`, beside the origin secret id, read
only by `J2`. The JWT window is `F3`, the shared module's constant, read only by `T8` and adjacent
to the two JWT secret ids. **The discriminator is structural, not a value difference** — the two
windows are deliberately the same number so a runbook reasons about one convergence window, which
is precisely why the number alone can never tell them apart and why Z-S159's conflation was
possible.

## What I did not grade, and one consequence I created

`S10E-AC6` (the MFA seal key) is judgment — evidence assembled, **no verdict**. But my change
creates something new there: the private key now refreshes on a bounded window and the
HKDF-derived seal key does not, so a long-lived container holds a seal key derived from a key it
no longer holds. **No functional regression** — seal/unseal within a container still agree, and
failure stays graceful (`unsealCode` → null → callers mint a replacement). What is *weakened* is
the invalidation intent the source itself records at the `v1` note. Documented in a docstring on
the function so the next reader meets it at the file, and routed to L9 rather than fixed mid-face.

## Blockers

**None.** `TO-OP-S-10`'s write side is now fixed; all three verifiers hold two slots and the signer
has a bounded window. The rotation remains barred pending the issuer's GO.

## Compiler Tools

| tool | result | gap found |
|---|---|---|
| `deploy_ledger.py` | CLOSED 5/5 | None — and this face **applied** TO-OP-S-10D's lesson: every leg closed through argv with no shell, then the stored proofs **read back** to confirm lengths rather than trusting the OK line |
| `build-nodejs-lambda.sh` | deterministic zip, independently re-verified | Its footer again prints three things wrong on this estate; ignored |
| `terraform plan` | 0/1/0, three attributes, 0 wafv2 | The data-lookup pattern moved the plan here, unlike session-analytics — verified rather than inferred |
| `node` local exercise + mutant | 9/9 clean, 3/9 mutated | The cache-mechanics assertions survive a wrong-value mutant |
| deployed-artifact read | both bounded, single-key; origin control unchanged | `previous` present but not an accept path — settled by enumerating all seven occurrences |
