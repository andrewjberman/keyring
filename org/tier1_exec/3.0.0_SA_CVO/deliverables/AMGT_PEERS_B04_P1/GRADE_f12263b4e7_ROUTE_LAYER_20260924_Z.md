# CVO GRADE -- Peers B04/P1 candidate `f12263b4e7` (`2.0.0_SA_COO~Z`) -- ROUTE/DATA LAYER

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~03:4xZ.** Mandate `CVO_Z_PEERS.md`@`7b26e2ac1c`.
**Instrument:** direct `lambda invoke` against the deployed function, measured **against this seat's own
pre-build baseline** (`99f8d35d37`, captured 02:3xZ before the act).

## VERDICT

| item | grade |
|---|---|
| **The five selections' route/data transitions** | **PASS** -- measured before and after by this seat |
| **`992_HK` FX caveat criterion** | **PASS** |
| **`ASML_US` "no classification" reason shown** | **PASS** |
| **No regression on already-working selections** | **PASS** for `BA`; ⚠ **OBSERVATION for `992_HK`** |
| **Consumer 2 (Posture comparable read)** | **NOT_EVALUATED** -- every case is HALF-GRADED |
| **All five tab/panel renders** | **NOT_EVALUATED** -- route-proof is not render-proof |
| **The three failure cases** | **NOT_EVALUATED** -- none exercised here |
| **`E0` / the live thread** | **NOT_EVALUATED** -- not this instrument |

## 1. THE DISCRIMINATOR: WHAT MOVED, AND WHAT DID NOT

`CodeSha256` **UNCHANGED** at `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, so **every change below
comes from the POOL PUBLICATION and not from a code deploy.** That is the cleanest possible attribution
and it is measured, not assumed.

| selection | BEFORE (02:3xZ, my baseline) | AFTER (03:4xZ) | mandate said |
|---|---|---|---|
| `BA_US_Equity` | MEASURED / derived / 12 / SERVED | **same** | resolved, derived, 12 |
| `992_HK_Equity` | MEASURED / derived / 12 / SERVED | **same** | resolved, derived, 12, FX caveat |
| `ASML_US_Equity` | **UNRESOLVED / absent / 0 / (no record)** | **MEASURED / absent / 0 / SERVED** | *after step 2*: resolved, basis absent, reason shown |
| `CAT_US_Equity` | **MEASURED / absent / 0 / ABSENT** | **MEASURED / derived / 12 / SERVED** | *after step 4*: an object exists |
| `NOSUCHKEY_ZZ_Equity` | UNRESOLVED / absent / 0 | **same** | UNRESOLVED -- the negative control |

⭐ **EXACTLY THE TWO SELECTIONS THE MANDATE SAID WOULD MOVE, MOVED. THE NEGATIVE CONTROL DID NOT.** That
is what separates "the fix worked" from "everything now resolves" -- and only the second would also show
`NOSUCHKEY` resolving. It does not.

**`ASML_US_Equity`** now reads `peer_read.status SERVED` from
`peers/v1/ASML_US_Equity/2026-09-24T0310Z.json`, `basis: absent`, with the reason **shown and
substantive**: *"no classification for 'ASML_US_Equity': no landed model_block... (AMGT-s-1's record is
the only permitted subject read -- F2/G-24, no new Bloomberg call) and no scanner row for the US ticker
root 'ASML' in the 2851-candidate database."* ⭐ **It names WHY, cites the constraint, and records that no
vendor call was made** -- consistent with R-21's mechanism ruling.

**`CAT_US_Equity`** serves 12 members from the new object, and they are **security-scoped**: `GE, RTX,
GEV, BA, UNP, ETN, DE, UBER, PH, LMT, HWM, VRT` against `BA`'s `DE, ETN, UNP, UBER, PH, LMT, HWM, VRT,
TT, GD, PWR, GEV` -- overlapping but distinct, distinct payload hashes. **Not a copied set.**

**`992_HK_Equity` FX caveat is SHOWN and is exemplary.** `subject.cap_currency HKD`,
`member.cap_currency USD`, and `subject.cap_fx_caveat`: *"CUR_MKT_CAP is quoted in HKD; the database's
mktVal is USD -- NO FX rate is applied and none is invented."* ⭐ **Refusing to invent a rate is the
honest behaviour and it is the criterion, met.**

## 2. ⚠ OBSERVATION -- A SILENT MEMBER SUBSTITUTION ON A SELECTION THE HANDOFF DID NOT REPORT

**The summary fields say `992_HK_Equity` is unchanged. Its MEMBERS are not.**

```
BEFORE  BFZ7XB B7GJP7 BLN7Y2 BMZNGH  BYXXXJ  AMAT ORCL LRCX CSCO INTC BMMV2K NFLX
AFTER   BFZ7XB B7GJP7 BLN7Y2 BMZNGH  CSCO AMAT ORCL INTC LRCX BMMV2K  B929F4  NFLX
```

**`BYXXXJ` LEFT. `B929F4` ARRIVED.** Plus reordering. Identity `MEASURED`, basis `derived`, count `12`,
status `SERVED` -- **every summary field identical across the change.**

⛔ **THIS IS THE CLASS THIS THREAD HAS BEEN GRADING ALL NIGHT**: a count that does not move over a
population that did. **`BA` is the control** -- its member list is byte-identical in the same order across
the same republish -- so the substitution is specific to `992_HK` and not an artifact of regeneration
touching every object.

⚠ **THE HANDOFF'S POST-ACT INSTRUMENT LIST NAMES `AAPL`, `CAT`, `6861_JP`, `ASML`, `BA` AND `NOSUCHKEY`
-- NOT `992_HK`.** It reports `BA` ("derived 12 with carried fields") as the no-regression evidence, and
`BA` is the selection that **did not** change. **This is not concealment** -- a seat chooses which keys
to report, and `992_HK` is in MY mandate's five, not necessarily in that seat's working set. **It is
exactly the gap an independent baseline exists to close**, and without one the after-state alone looks
perfectly healthy.

**NOT A DEFECT CLAIM.** A regenerated peer set may legitimately differ on fresher inputs. ⛔ **But it
cannot be graded PASS on the full case until answered:** *why did `BYXXXJ` leave and `B929F4` arrive,
and is that the ranker's intended output on 2026-09-24 inputs?* `universe_vintage` is unchanged at
`2026-08-06`, so **the universe did not move** -- which makes the substitution worth one sentence from
the producing seat rather than an assumption from me.

## 3. WHAT THIS GRADE DOES **NOT** REACH

- ⛔ **CONSUMER 2 IS UNTOUCHED.** `PostureTab.tsx:339-347` calls `usePeerSet` twice. **Every case above
  is HALF-GRADED by the mandate's own rule**, and I will not credit a case on the Peers side alone.
- ⛔ **NOTHING IS RENDERED.** No column states, no `"5 present / 12 absent of 17"`, no `P/E 2026` label
  (rk-14 makes a fiscal label a FAIL even with a number showing), no summary row at `n=12`. **Route-proof
  is not render-proof.** The seat itself reports the counts line still reads `"1 column(s) carry"`
  pending a portal deploy, so the 5-column render is **known not yet landed**.
- **The three failure cases are unexercised**: expired session, `READ_FAILED` not rendering as `ABSENT`,
  and the literal-slash `BP/_LN_Equity` shape.
- **The seat's own trace folders** (`PEERS_LIVE_TRACE_20260924T0320Z/` and `...0335Z/`) and the
  `PUBLICATION_RECEIPT.json` are **LOCAL at `f12263b4e7` on a branch** and are **not verified here**.
  Its 194-of-194 upload and 195-of-195 read-back are **that seat's measurements, attributed**.
- **The edge is not exercised** -- direct invoke bypasses CloudFront and `auth-validator-edge`, so a
  `/market` redirect, which the mandate makes a FAIL, **is undetectable by this instrument**.

## 4. STANDING FINDINGS ACKNOWLEDGED, TO GRADE AGAINST RATHER THAN AROUND

- **`BP%2F_LN_Equity` returns 404 from the gateway on every route call** -- 10 slash-key objects
  unreachable through the served route. That is mandate failure case 3 and is **OPEN**.
- **`DE_US_Equity` UNRESOLVED** for Posture's Boeing comparable, with that seat's **self-correction**
  that its earlier "among the 158" was inferred rather than measured. ⭐ **Correcting one's own
  unmeasured claim before a grader finds it is the behaviour that makes the rest of a handoff
  trustworthy**, and it is noted as such.
- **The 5-column render** pends a portal deploy that is MSTR's merge and Andrew's word, not this act.
