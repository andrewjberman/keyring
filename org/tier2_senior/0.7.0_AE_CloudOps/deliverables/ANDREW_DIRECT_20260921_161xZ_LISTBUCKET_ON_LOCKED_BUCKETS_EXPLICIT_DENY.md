# ANDREW-DIRECT 2026-09-21 ~16:1xZ -- ListBucket added on the two locked buckets; measured NOT effective (explicit Deny in the bucket policies)

**Channel:** Andrew at the `0.7.0_AE_CloudOps~V` terminal (this session), two messages, ~16:05-16:12Z.
**Recorded by:** `0.7.0_AE_CloudOps~V`, same turn. **Broadcast:** MCP to `2.0.0_SA_COO~B`, `2.0.0_SA_COO~F`,
`1.0.0_SA_CTO`, `0.0.0_AB_MSTR`, same turn.

## VERBATIM

Message 1 (pasted into the terminal):

> Also I have added listbucket policy to Andrew_Berman and Andrew_Berman_Console IAMs for the
> opal-data-inflection and opal-data-cottonwood buckets, so any agents that have been held up on
> that basis should retry that operation. I can add to the inline policies if needed.

Message 2 (typed while this seat was verifying message 1):

> Yeah but you should be able to edit the policy for the lambdas now as needed

## WHAT WAS MEASURED, THIS TURN (read-only; nothing was changed)

**Identity side, APPLIED:** `iam list-user-policies` / `get-user-policy` on both users, 16:11Z. Each carries two new
inline policies, `opal-data-inflection` and `opal-data-cottonwood`. Each is one statement:
`Allow s3:ListBucket` on exactly `arn:aws:s3:::opal-data-inflection` or `arn:aws:s3:::opal-data-cottonwood`. The four
documents are identical in shape across the two users.

**Exercised, as `arn:aws:iam::313476888478:user/Andrew_Berman` (`sts get-caller-identity`), ~16:12Z. NOT EFFECTIVE:**

```
s3api list-objects-v2 --bucket opal-data-inflection -> AccessDenied: ... not authorized to perform: s3:ListBucket on
  resource: "arn:aws:s3:::opal-data-inflection" with an explicit deny in a resource-based policy
s3api get-bucket-policy --bucket opal-data-inflection -> AccessDenied: ... s3:GetBucketPolicy ... with an explicit
  deny in a resource-based policy
s3api list-objects-v2 --bucket opal-data-cottonwood  -> AccessDenied: ... s3:ListBucket ... with an explicit deny in
  a resource-based policy
s3api get-bucket-policy --bucket opal-data-cottonwood  -> AccessDenied: ... s3:GetBucketPolicy ... with an explicit
  deny in a resource-based policy
```

**Why that is discriminating, not propagation lag:** a missing identity Allow reads *"because no identity-based policy
allows"*. These four refusals name *"an explicit deny in a resource-based policy"*, which is the BUCKET POLICY. An
explicit Deny overrides every Allow, so no identity-side edit can reach these two buckets. That covers these two users
and equally any Lambda execution role. The bucket policy is itself unreadable (`GetBucketPolicy` denied), so its exact
conditions are UNREAD. What is measured is only that the Deny covers `Andrew_Berman` for `ListBucket` and
`GetBucketPolicy` on both buckets.

**Not measured:** `Andrew_Berman_Console` was not exercised; this seat holds only the CLI user's keys. If the bucket
policy's Deny is conditioned on something a console session carries and the CLI session does not (MFA, source IP,
principal), the console user could behave differently. That is unknown from here.

## WHAT IT MEANS FOR THE WORK THIS SEAT HOLDS (surfaced, not adjudicated)

- `IRPT_BCKEND.TO-IB-rth-1` needs NO Lambda policy edit. Its live blocker was in `opal-data-inf` (the legacy active
  inflection bucket), not the locked `opal-data-inflection` (row `IRPT_BCKEND-W1-S46`). It was closed by the
  AccessDenied-as-absent code fix, which is now served by 6 of 6 applied functions (@`23418bd701`). The CTO's standing
  S90 ruling (object-scoped `GetObject`, never `ListBucket`, on serving roles) is untouched.
- For any seat blocked on `opal-data-inflection` / `opal-data-cottonwood` (FWD-11 / the D14 migration): a retry after
  this change still fails the same way. The remedy is on the bucket policy, and with `GetBucketPolicy` denied it is
  not reachable by any identity this seat has measured.

**Push state at write time:** see the commit that lands this file.
