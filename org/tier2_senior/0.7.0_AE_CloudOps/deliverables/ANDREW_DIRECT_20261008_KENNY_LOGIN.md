# Kenny Cusick login recovery - Andrew direct

Recorded 2026-10-08, US Eastern, in Codex thread 01a11c3f-a479-79b0-8007-b279b330b7c6.
Channel: direct user message. Receiving seat: 0.7.0_AE_CloudOps.

Verbatim instruction:

> I need you to read the following email from kenny.cusick@cottonwood.mail. He is a new employee at Cottonwood Capital Advisors, our client at Opal Capital. Yesterday, I built a new account for him to access the opalinvest.dev dashboard. I need to understand why he is getting an internal error, likely a 500 from his login. I would recommend checking his user entry, if it differs from other users (missing fields for example) that other opal-users-v2 entries have. I would also recommend checking for similar issues on the opal-partners-cottonwood table. We need to make sure he is able to get online cleanly. Below is his attached email: [<Good morning Andrew,
>
>  
>
> I am having issues logging in. I even tried resetting the password and once I input the new password it just says internal error and does change anything. I tried the password I created, tried resetting and it gives the same message. Can you help me on this? Thanks
>
>  
>
> Kenny>]

## Measured diagnosis

- Actual identity is kenny.cusick@cottonwoodmail.com (Kenneth Cusick), created October 7 at 12:15:42 PM Eastern. No account exists for the literal cottonwood.mail address. Actual partner table is opal-partner-cottonwood (singular).
- Exactly one email-index profile. PROFILE, FIRM/MEMBER and partner row exist. Compared with all three other real Cottonwood member profiles: required fields and types match. Kenny has a valid bcrypt-shaped hash, active status, advisor tier, user role, MFA disabled explicitly, and mustChangePassword=true. No data repair indicated.
- Last successful login October 7 at 12:47:48 PM Eastern. Password remains unchanged since provisioning.
- Auth Lambda errors at 12:48:07, 12:48:17 and 12:48:42 PM Eastern October 7, and 11:52:04 AM Eastern October 8, say the password must have at least 12 characters. Logs omit identity, so attribution is temporal and supported by the account state, not a request-level identity proof.
- password.ts validates 12 characters; auth.ts throws a generic Error; index.ts maps it to HTTP 500. ChangePasswordPage.tsx and ResetPasswordPage.tsx still advertise and locally accept 8. This explains the reported misleading error.
- Separate confirmed defect: resetPassword searches listUsers(), which queries firmId-index only for opal-capital. Cottonwood reset links cannot complete through that path even with a compliant password.
- Downloaded live bundle SHA256 matches source map: h1tnQVRpRA52eWyfAia6CfBsJmn6xKwHa8IUC0zBSsQ=. Read-only IAM simulation permits dynamodb:Scan on opal-users-v2 for opalinvest-auth-lambda-role.

## Repair scope

Return a clear HTTP 400 for rejected new passwords; resolve reset tokens across all firms with pagination and ambiguity rejection; retain expiry and email uniqueness checks. Do not rewrite Kenny's user records or passwords. Backend regression cases cover the actual defects. Frontend eight-character copy remains separately identified in the incident record.

Push state: LOCAL. Origin CLOUD measured before changes: 37a4a9454cc928cd3d672ec788159290301d77f9. No push by this seat.
