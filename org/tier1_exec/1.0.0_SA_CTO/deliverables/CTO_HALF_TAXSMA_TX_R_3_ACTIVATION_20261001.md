# CTO half -- MDPF_TAXSMA TX-r-3, Tax SMA activation, and the HEALGAP hookup's condition 3

**Request:** `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/NEVER_WIDEN_REQUEST_TX-r-3.md`, **blob `d2598ef965`** at the
commit that carries its 17:3xZ addendum (the message 103921 cites @e7d87da7b0; this half binds the file as it stands with the
addendum). Andrew's word: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_170xZ_TAXSMA_APPLY_AND_DEPLOY_NOW_WITH_EGRESS.md`
@28e5589af0, which authorizes the applies, deploys and egress and leaves the two halves in place.

## SIGNED, 2026-10-01 ~17:2xZ, by 1.0.0_SA_CTO

On the blast radius the request measures: turning Tax on moves 9 of the Gold function's 16 documents as its table states
(49 Financial total 1,743,965,549.58 to 1,762,733,661.93; Global total 2,066,937,285.42 to 2,091,754,766.55; Cottonwood's SMA
line 0.00 to 6,049,368.78 with its total unchanged; Inflection gains null extension fields only); 7 documents are identical.
All five of its branches are covered: complete on the frontier date; activation day (no dollar moves, extension fields and a
null `tax` member only); a day Tax cannot be read (`CARRIED_LAST_COMPLETE`, dated); a Cottonwood Tax account gaining a model
(withheld, last complete carried); Tax off (nothing moves). The first dollars are expected on the 2026-10-05 13:30Z run.

**Writers counted: 2.** The Gold function writes the dated documents under `portal/gold/mdpf/` in `opal-data-assets`; the
publisher copies each to the served plane and adds two stamp fields to category-views. The Gold function's rule was read by
the request's probe (two full builds in one process, zero S3 writes); the publisher's rule is taken from the request and was
NOT read by this seat.

**Read by this seat (17:17Z):** `mdpf-gold-lambda` runs CodeSha256 `eZ6Rtm+2XOKm4UFWgdYhFpNYxCjiKDVtRONV6Ewt21s=`, modified
15:00:26Z, environment `MDPF_GOLD_COMMIT` = `8ade880fad` and no other key; no Tax-named key is set. So activation adds
environment and a secret value only, as the addendum says. The request's last line ("the deployed functions run e8994f23af")
is superseded by its own addendum and by this read.

**Rollback per key, accepted as follows:** capability off and switch OFF, effective from the next run. Whether a dated
document already written with Tax can be rewritten the same day is UNMEASURED, so a rollback is read as next-run, not same-day.
On activation day no dollar moves, so that gap carries extension fields only.

## Condition 3 of the HEALGAP hookup signature -- RULED: AMENDED, activation does not wait

The 2026-10-02 13:30Z run is that deploy's leg V2, whose rollback trigger is "any served change outside the five Cottonwood
dates and Global's same five". It is amended to admit EXACTLY branch 2 of this request and nothing else: on the four
`aggregate-aua-timeseries` documents, the four extension fields named in the request (null values, basis NOT_APPLICABLE where
the request says so), and at 49 Financial and Global a `tax` member with a null value. Every Tax-off value outside the ten
dates must be unchanged. A Tax DOLLAR on 2026-10-02 is outside the amendment and still triggers the rollback, because branch 2
says none should land that day. `4.0.0_SA_CRO` writes the amended trigger into the leg before the run and reads both changes
apart in its V2 record.

## Named in addition

1. Annex rule 26a: Andrew's word makes this seat-run Gateway release a one-time departure; it does not change the rule.
2. Portal PROD promotion is NOT covered by this half; the request itself puts it to Andrew by name.
3. Not verified by this seat: the probe's run, the publisher's code, the Gateway release's contents, the Graph read's scope.

-- 1.0.0_SA_CTO


## ADDENDUM 2026-10-01T18:06Z -- condition 3 RE-AMENDED on Andrew's 17:4xZ word (record @39f9ce95c0; CRO msg 103940)

Andrew ruled that an account's first observation also covers the prior trading day, approved one ad-hoc Gold run and one
ad-hoc publisher run today after activation, and named DEV. So today's ad-hoc run serves Tax at 2026-09-30 and tomorrow's
13:30Z run carries it: that is the request's BRANCH 1, which both halves already signed. The 17:2xZ amendment admitted branch 2
only and would roll back the HEALGAP catch-up for it.

RE-AMENDED: leg V2 of `mdpf-gold-healgap-hookup-20261001` admits, beyond the ten dates, EXACTLY the Tax changes the request
names, each checked by an identity, not by a range:
(a) at 49 Financial and Global, every total that moves equals its Tax-off value plus the served `tax` member at that date,
    to the cent;
(b) at Cottonwood, the SMA line rises and the Client line falls by the same amount at each date, and the total does not move;
(c) the four extension fields and the `tax` member, and `tax_additive_aum` and the `taxsma` fee-basis component where the
    request names them;
(d) every other value outside the ten dates is unchanged.
A change that fails (a) to (d) still rolls the catch-up back. `4.0.0_SA_CRO` writes this trigger into the leg before the
ad-hoc run and reads the ten dates and the Tax identities apart in its V2 record. The 18:03Z deploy of the first-day rule is
DELTA=0 with Tax disabled (16 of 16 equal), so it needed no half.
