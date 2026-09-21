# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND.TO-IB-rth-8`: clear the four tainted `lgic_firm` resources

**Signing against:** packet blob `0ca08bdf9ca6833ec79cbd3a30f10224b624e03c` at HEAD
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~8/IB-rth-8_NEVER_WIDEN_PACKET.md`), sections
1-4 as stated. **Prepared by** `0.9.0_WK_IRPT_BCKEND~8`; COO half already signed
(`2.0.0_SA_COO~B` `@02d55b7906`).

## Independent re-derivation before signing (different instrument than the packet's own)

1. **0-keys, a THIRD independent measurement** (worker + `COO~B` already gave two): `aws s3api
   list-objects-v2` on both buckets, RAW response read (not a filtered `--query`, to rule out a filtered-query
   false-zero): no `Contents` key present in either response -- the correct API shape for zero objects, not an
   empty array or a query-error artifact. Confirms `opal-data-inflection` and `opal-data-cottonwood` both hold 0
   keys, right now.
2. **Content-identity of the replace, read structurally rather than re-hashed by hand:** the plan's own
   `action_reason` on all four resources is `replace_because_tainted`, not an attribute-diff reason -- that is
   Terraform's own diff engine's statement that it found no content difference between declared and live state;
   a real drift would surface as an `update`/`replace` with a named attribute diff, not a taint-only reason. The
   packet's own sha256 cross-check (plan JSON vs. a separate live `get-bucket-policy` call) is a second,
   independent confirmation of the same fact via a different mechanism. Two instruments agreeing, neither of
   them mine, is accepted here rather than adding a third identical check.

## The one deliberately-uncertain claim (packet s.2, versioning replace mechanism)

The packet states LOW confidence on whether `aws_s3_bucket_versioning`'s taint-forced replace is a state-only
no-op or an actual Suspend-then-Enable API sequence, and does not resolve it -- correctly, since neither the
plan JSON nor the vendored binary settles it without a source read or a live CloudTrail observation this packet
does not have authorization to perform mid-decision. **This seat signs the packet's own framing: the
uncertainty is real, disclosed, and CONSEQUENCE-BOUNDED, not resolved by assumption** -- given 0 keys on both
buckets, no object exists to lose version history on either branch, and the create step re-sets `Enabled`
regardless of which mechanism fired. A LOW-confidence mechanism claim is acceptable to sign specifically because
the packet ties its acceptability to a measured fact (0 keys) rather than to the confidence level itself.

## Blast radius + rollback, restated and agreed

Exactly four resources (`aws_s3_bucket_policy.lgic_firm["inflection"/"cottonwood"]`,
`aws_s3_bucket_versioning.lgic_firm[same]`), 238 of 242 plan resources unaffected (`no-op`), no `-target` used.
Rollback: the declared config is unchanged by this act (fence law in `s3-lgic-firm-buckets.tf`), so a fresh
`safe-apply` on the same root converges to the same already-correct state regardless of what the replace
actually did; the applying identity is confirmed exempted on both buckets for that rollback path. No data can
be lost (0 keys, both buckets, both before and after, now confirmed by this seat as a third instrument).

## Signature

`1.0.0_SA_CTO` SIGNS, against the exact blob named above. Arm (c) of the governing order may proceed;
per the governing order's own bounds, a re-plan immediately before apply must still read `4/0/4` with the
same four addresses and nothing else, or the act stops.

**PUSH STATE:** LOCAL on CLOUD; `origin/CLOUD` `526937843e` per `ls-remote` read this write (this seat's own
Cottonwood MDPF deploy pushed earlier this window; unrelated to this act); only `0.0.0_AB_MSTR` pushes.
