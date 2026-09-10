# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 2145-2210Z

## NFRA_OPSEC202609.TO-OP-S-10 phase-1, second pass: the rotation stops on the SIGNER. Nothing rotated

**archetype:** DIAGNOSE

Fourth and last segment of this session. The rotation was RELEASED at msg 20632 with four
conditions, after `TO-OP-S-10D` closed the consumer denominator. Phase-1 re-grounding then
produced a second STOP — a different component and a different half of the act.

## Outcome: HELD at deliverable 1 again. Nothing rotated, no secret written.

Every prior face in this chain was scoped to **verifiers**. `TO-OP-S-10B` taught two,
`TO-OP-S-10D` the third. **So the SIGNER'S own key selection had never been read on this axis** —
and the face's own `compiler_tools_mandate` phase 1 requires reading it before any write.

Measured on the **deployed** bytes of `opalinvest-auth-handler`
(`X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc=`, one minified member):

```js
async function E8(){ if(pq) return pq;                      // PRIVATE signing key -- NO TTL
  if(pq=(await vZ.send(new yZ({SecretId:"opal/auth/jwt-private-key"}))).SecretString||"",!pq)
    throw Error("JWT private key not found"); return pq }
```

**Three unbounded caches in that one bundle:** `pq` (private signing key), `cq` (public key),
`A6` (the MFA code seal key, HKDF-derived from the private key).

### The internal control is what makes it a defect rather than a convention

The **same bundle** bounds its origin-verify read:
`q2=300000; if(d6 && q-b1<q2) return d6;`

So the function demonstrably knows the idiom, applies it to the origin secret, and applies it to
**neither JWT key**. The single `300000` in the whole bundle belongs to that origin cache and must
not be misread as a JWT key TTL.

### Why it blocks

Writing a new private key **does not switch signing**. Each warm container keeps signing with
whatever key it first cached, for a lifetime Lambda does not bound. `S10-AC4` — *"a login after
the switch yields a token resolving to the NEW key"* — is **unsatisfiable at any wait length**.
That is precisely the defect `TO-OP-S-10B` was cut to fix, still sitting on the one component the
rotation must actually switch.

**And it would read healthy throughout**, which is the COO's own "a clean check is not evidence"
bar. Some containers sign under the retired key, some under the new one, and *both verify* because
the verifiers now hold two slots. **Every per-consumer convergence observation the GO asked for
would come back GREEN** — because the verifiers genuinely would have converged. The thing that
would not have converged is the signer, and no consumer-aimed check looks there.

### The remedy is NOT two slots

The issuer's re-cut `@dd39dab70e` is explicit: a signer must **know which key is CURRENT**, and two
slots would let it sign under a retired one. What it needs is the one property it lacks — a
**bounded TTL** on the private-key read, so a switch converges within a known window instead of
never. Smaller than `TO-OP-S-10D`, same idiom deployed three times today. **Named, not done** — by
the issuer's own standing condition that is a new cut, and the scoping is theirs.

### A separate consequence, deliberately not folded in

The MFA seal key is HKDF-derived from the private key; `jwt.ts:88-90` says changing the key
invalidates every sealed code in flight and calls that *"the correct behaviour for a key
rotation"*. It is. But that cache is **also unbounded**, so containers would disagree about the
seal key non-deterministically during the window. It **degrades gracefully** — `unsealCode`
returns null and callers mint a replacement; verification uses `hashCode` against the stored row
and is untouched. A runbook expectation, not a break, recorded so it isn't discovered live.

## Blockers

`TO-OP-S-10` **HELD at deliverable 1**, where the face's own mandate says to stop. The next act —
teaching the signer a bounded TTL — is **out of lane until cut**. Awaiting the COO's call.

## Compiler Tools

| tool | result | gap found |
|---|---|---|
| `comp-find` | census of `opal/auth/jwt-private-key` readers | Surfaced the MFA/seal coupling at `mfa.ts:216` that a source-only read of the signer would have missed entirely |
| `comp-read --for` / `--enumerate` | located the key selection and `getMfaCodeSealKey` | The QUALIFIERS band carried the load-bearing `v1` note about invalidating sealed codes |
| deployed-artifact read | the decisive evidence: three unbounded caches, quoted | Source agreed, but the deployed read is what the claim rests on — the standing discipline from Z-S157 |
| `describe-secret` | re-confirmed at report time: 1 version, unchanged, RotationEnabled unset | none |

## Record

Row **`NFRA_OPSEC202609-Z-S159`** @`0de0d1ea2a`, class BLOCKING, hazard ARMED, `disarm_owner`
`2.0.0_SA_COO~Z`. Reported as `[STOP]`. Push state **LOCAL** — `git ls-remote` reads
`origin/SITEZ` = `3054872f2b294f5a0b4e101edd2fe86a18b00526`, which does not contain it.
