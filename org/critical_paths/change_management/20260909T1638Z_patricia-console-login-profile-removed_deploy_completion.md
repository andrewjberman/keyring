# CHANGE COMPLETION — patricia@thewhitelabelcreative.com console login profile REMOVED

**Actor:** `4.0.0_SA_CRO~Z` · **Opened AND closed:** 2026-09-09 16:38Z (single-call change, verified
in-session) · **Status: COMPLETE — VERIFIED LIVE**
**Authority:** Andrew-direct at the `4.0.0_SA_CRO~Z` terminal 2026-09-09 ~16:3xZ, VERBATIM AND
ENTIRE: *"Rec approved, remediate now"* — approving this seat's recommendation to *"remove console
access rather than MFA-gating it."*

---

## THE ACT, exactly one call

```
aws iam delete-login-profile --user-name patricia@thewhitelabelcreative.com     rc=0
```

**NOTHING ELSE CHANGED.** The IAM user, its path, its tags and its
`website-estate-admin` policy attachment are untouched.

## VERIFICATION — live, with a positive control (rc=0 is not evidence)

| Check | Result |
|---|---|
| `get-login-profile patricia@…` | **`NoSuchEntity`** — profile gone |
| **POSITIVE CONTROL** `get-login-profile Andrew_Berman_Console` | returns a real profile → the call works, so the NoSuchEntity is a TRUE absence and not a broken call |
| `get-user patricia@…` | still `arn:aws:iam::313476888478:user/website/patricia@thewhitelabelcreative.com` |
| `list-attached-user-policies` | still `["website-estate-admin"]` |

**NO TERRAFORM DRIFT INTRODUCED.** `infra/aws/terraform/website/iam_patricia.tf` declares the USER
and the POLICY only; it has never declared a login profile. See below.

---

## WHY THIS IS NOT AN OUT-OF-BAND VIOLATION

`iam_patricia.tf:163-176` documents the login profile as **deliberately** out-of-band, with the
technical reason, verbatim:

> *"the AWS Terraform provider's `aws_iam_user_login_profile` can only GENERATE a random password (its
> `password` attribute is provider-computed, not settable), so a SPECIFIC password (Andrew-direct
> 2026-07-08: console login using this email, initial password chosen by Andrew) cannot be expressed
> in TF. Per the estate credential-value convention (passwords/secrets are set out-of-band, never in
> repo or TF state …), the login profile is created with the AWS CLI once the user exists."*

**Deleting it by CLI is therefore SYMMETRIC with how it was created, not a violation of the
Terraform-only rule.** The access-defining infrastructure (user + permissions) remains fully
Terraform-declared and unmodified. This is deliberately distinct from the `deployed-ahead` class
Andrew ruled enforceable earlier the same day — that ruling concerns Lambda CODE deployed outside
Terraform, not a credential VALUE the provider structurally cannot express.

## REVERSIBLE — the runbook already exists, in the same file

```
aws iam create-login-profile --user-name patricia@thewhitelabelcreative.com \
  --password '<chosen-password>' --password-reset-required
```

`iam_patricia.tf:172-174`. Re-provisioning is a documented, one-command act whenever Andrew lifts
the delivery hold and actually onboards TWLC.

---

## WHAT THE FINDING ACTUALLY WAS — corrected

The 2026-09-09 infrastructure report's AI briefing ranked this **#1 urgent**:
*"IAM - patricia@thewhitelabelcreative.com: Console access with NO MFA. External vendor account.
Enforce MFA or suspend immediately."*

**True, and materially misleading without context that the report has no way to carry:**

1. **The blast radius is small and was measured, not assumed.** `website-estate-admin`
   (`iam_patricia.tf`, 7 statements) is tag-scoped to `Project=NFRA_WEBSITE` for EC2/SSM, ONE exact
   backups-bucket ARN, and the website box's own log group. Its header states: *"ZERO data-estate
   reach, ZERO other bucket, ZERO Secrets Manager, ZERO IAM-modify, ZERO SG/perimeter rewrite, ZERO
   instance-terminate."* Operational admin over ONE EC2 box, not the account.
2. **The policy already granted self-service MFA enrolment** (SID `SelfManageCredsMfa` +
   `ViewAccountInfoForConsoleSelfService`), scoped to her own identity. MFA was designed in.
3. **She had no MFA because she had never logged in.** `PasswordLastUsed` was ABSENT.
   Andrew held delivery on 2026-07-08 (*"dont send anything to Patricia yet"*) and **the hold was
   honoured** — the measurement is the evidence.

**So the real exposure was never "an unprotected admin." It was a ONE-TIME BOOTSTRAP PASSWORD
created 2026-07-08 19:07:43Z and never delivered** — small, but nonzero for 63 days. Deleting the
profile retires it at zero operational cost, because nothing was using it.

## THE REPORTING LESSON, carried to the infrastructure-reporting brief

**Posture without context reads as breach.** Every fact the scanner reported was correct; the
conclusion a reader draws from it was wrong, because the scanner cannot see a sovereign hold, a
delivery state, or a `PasswordLastUsed` absence. Under the two-axis model Andrew ratified this same
day, this row is `CHECKED` on Axis 1 and `DEGRADED` — not `BREACH` — on Axis 2.

This is recorded as evidence for brief finding F10/F11
(`docs/briefs/global-infrastructure-reporting-brief-20260909.md`), which stated the blast radius as
UNREAD. **It is now read, and this record supersedes that non-claim.**

## RESIDUAL — named, not chased

- **The bootstrap password's disposition is unknown to this seat.** It was chosen by Andrew on
  2026-07-08 and may still exist in a note or a password manager. Deleting the login profile makes
  it non-authenticating, so the residual is hygiene, not access.
- **`website-estate-admin`'s 7 statements were read; they were not exercised.** No
  `simulate-principal-policy` battery was run by this seat, so the scope is asserted from the policy
  DOCUMENT, not from EXERCISED behaviour. The TF header cites a live simulate battery at
  clearance-time 2026-07-08, which this seat did not re-run.
- **The delivery hold is NOT lifted by this act**, and this record does not lift it.
