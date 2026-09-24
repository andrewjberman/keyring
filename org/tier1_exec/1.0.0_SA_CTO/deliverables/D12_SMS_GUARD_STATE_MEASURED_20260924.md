# D12 SMS -- THE SANDBOX-EXIT HAZARD'S TRIGGER HAS FIRED. MEASURED, AND IT IS AN EXPOSURE, NOT AN INCIDENT

**Author** `1.0.0_SA_CTO~Z`, 2026-09-24 ~05:5xZ, site Z. **Class** a measurement owed by this seat's own hold entry,
now performed. **Nothing was changed on any deployed surface by this seat; every line below is a READ.**

## 1. WHY THIS CHECK WAS OWED, AND BY WHOM

`org/critical_paths/.open_deploys/d12-sms-origination-identity-activation.json` is **HELD-STALE at 21.6 days,
author `1.0.0_SA_CTO~Z`** -- this seat. Its own warning, verbatim:

> *"sms.ts:38-44 states that the day sandbox exit happens, every guard that lived only in the sandbox evaporates at
> once and this Lambda would begin texting arbitrary enrolled numbers WITH NOTHING IN THE REPO HAVING CHANGED.
> **Nothing in this estate can observe that transition; it must be checked against AWS deliberately.** That is why
> this entry exists rather than a note in a project blocking field, which comp-schedule classes NOT-DECIDABLE and
> never counts."*

⭐ **THE ENTRY WAS RIGHT ON EVERY POINT, INCLUDING THAT NOTHING WOULD OBSERVE IT.** It sat 21.6 days precisely
because its re-read condition is an out-of-band AWS event with no repo signal. **This is that deliberate check.**

## 2. THE STATE, MEASURED ON THE LIVE PLANE

| what | value | instrument |
|---|---|---|
| account tier | ⛔ **`PRODUCTION`** (sole attribute returned) | `pinpoint-sms-voice-v2 describe-account-attributes` |
| text spend limit | `EnforcedLimit=50 MaxLimit=50 Overridden=false` | `describe-spend-limits` |
| origination identity | ⛔ **SET** -- `arn:...:phone-number/phone-0e98f7739a16415c83d951336a7da12a` | `lambda get-function-configuration opalinvest-auth-handler` |
| `SMS_ALLOW_UNVERIFIED` | ⛔ **`'true'`** | same read |
| `SMS_VERIFIED_DESTINATIONS` | **ABSENT** (not empty -- absent) | same read |
| the number | `+18664067943` **ACTIVE / TOLL_FREE / TRANSACTIONAL** | `describe-phone-numbers` |

**THE GUARD, READ AT SOURCE** (`infra/aws/opalinvest_dev/lambda/auth-handler/src/sms.ts:78-83`):

```
if (!ORIGINATION_IDENTITY) return 'no_origination_identity';   // SET   -> passes
if (!E164.test(phoneE164))  return 'malformed_destination';
if (ALLOW_UNVERIFIED)       return null;                        // TRUE  -> RETURNS HERE
return VERIFIED_DESTINATIONS.includes(phoneE164) ? null : 'destination_not_verified';
```

⛔ **`ALLOW_UNVERIFIED` IS TRUE, SO LINE 81 RETURNS BEFORE THE ALLOWLIST IS EVER CONSULTED.** The absent
`SMS_VERIFIED_DESTINATIONS` is therefore irrelevant rather than protective. ⛔ **AND AWS'S OWN SANDBOX REFUSAL IS
GONE TOO, BECAUSE THE TIER IS `PRODUCTION`. BOTH CONTROLS ARE OFF AT THE SAME TIME.** The file's comment at `:55-58`
says that flag exists *"so that leaving the sandbox requires TWO acts -- the AWS-side exit AND a reviewable change
here -- rather than one silent one."* **Both acts have occurred.**

## 3. ⭐ IT WAS DELIBERATE AND REVIEWABLE. THE CONTROL WORKED EXACTLY AS DESIGNED

⛔ **THIS IS NOT AN UNAUTHORIZED FLIP AND MUST NOT BE REPORTED AS ONE.** `SMS_ALLOW_UNVERIFIED = "true"` sits in
**`infra/aws/terraform/portal-auth/lambdas.tf:40`**, and it arrived through a dated, attributed artifact:
`org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D12_PHONE_OTP_SMS_LIVE_portal-auth_terraform_20260917.patch:25`.

⭐ **SO SB-1's WHOLE VALUE PROPOSITION HELD.** Its claim was *"the value is that flipping it is visible in a diff
and in Terraform, which sandbox exit is not."* **The flip IS in a diff, IS in Terraform, and IS attributable to a
lane and a date.** The design did the one thing it promised: it converted an invisible account-level event into a
reviewable change. **The control is the reason this record can be written at all.**

⚠ **AND ANDREW'S 2026-09-09 WORD PLAUSIBLY AUTHORIZES IT** -- *"Whatever must be done to initiate SMS registrations
and proceedings to make this operational should be pursued now."* **"Operational" is not obviously narrower than
this.** That reading is NOT adopted here as his word, because `sms.ts:55` asks for something more specific
(*"SET THIS ONLY WHEN SP-2 IS DONE AND ANDREW HAS SAID GO"*), and stretching a general word onto a specific gate is
the widening §2 forbids. **It is put to him in §6 rather than assumed in either direction.**

## 4. EXPOSURE OR INCIDENT -- Rule 22's NEGATIVE MIRROR, RUN RATHER THAN ASSERTED

**ABSENT != EXERCISED-AGAINST.** A missing guard is an EXPOSURE until someone measures whether it FIRED, and the
two carry different remedies -- an exposure is closed by building the guard, an incident **also** requires
re-opening whatever the gap admitted.

**THE SIGNATURE, RUN OVER THE GUARDED PATH:** `/aws/lambda/opalinvest-auth-handler`, 14 days, filtered for
`mfa_sms` / `SendTextMessage` / `destination_not_verified` / `no_origination_identity` -> **0 events.**
⭐ **POSITIVE CONTROL, BECAUSE A ZERO FROM A FILTER I WROTE IS NOT AN ABSENCE:** the same log group over the same
window holds **24 events**, and 3.16 MB stored at 30-day retention. **So the zero is a REAL absence: the SMS path in
the guarded Lambda has not run.**

**VERDICT: EXPOSURE, NOT INCIDENT. The open guard has never been exercised through the path it guards, so nothing
is re-opened.**

⚠ **ONE LIMIT, STATED BECAUSE IT IS THE UNCOMFORTABLE HALF AND OMITTING IT WOULD MAKE THIS RECORD LOOK CLEANER
THAN THE EVIDENCE:** **`TextMessageMonthlySpend` IS NON-ZERO AND RISING** -- month-to-date `$0.0478` (09-18, 09-19,
09-20) -> `$0.05975` (09-21, 09-22) -> **`$0.10755` (09-23)**. ⛔ **So messages HAVE been sent from this account.**
They are **not attributable to `opalinvest-auth-handler`**, whose log is silent against a passing positive control.
**This seat cannot attribute them further and does not guess** -- plausible sources include the toll-free
verification exchange itself and console tests, and `+17862617679` sits as a verified destination in `PENDING`,
whose verification sends an SMS. **Attribution of that spend is OWED and is not claimed here.**

## 5. THE LEDGER REPAIRS MADE ALONGSIDE, AND THE ONE LEG LEFT OPEN

`d12-sms-tfn-registration-and-production-access` (author `0.0.0_AB_MSTR`, age 350h, **window 504h -- IN-WINDOW, not
past it**): legs **`V2`** closed on its own clause measured verbatim, and **`A`** and **`V1`** closed by
**TRANSCRIBING** the proof MSTR had already written into the markdown table on 09-13 but which never reached the
JSON index the tool reads -- so those two had been falsely stranded for 11 days. Stranded set
`['A','V1','V2','V3']` -> **`['V3']`**, verify-after run.

⛔ **`V3` STAYS OPEN AND ITS CLAUSE IS DEFECTIVE TWICE.** It wants *"`SMS_VERIFIED_DESTINATIONS` +
`SMS_ALLOW_UNVERIFIED` re-read in a reviewed commit BEFORE or WHEN V2 lands"*, proven by *"commit hash under
`0.7.0_AE_CloudOps` author line"*. **(i) the re-read landed in `0.4.0_DT_ClientPlatform`'s 09-17 patch -- a
different lane; (ii) "BEFORE or WHEN V2 lands" is already past.** The clause is re-cut by its owner, not stretched
to fit, and ⭐ **the substance it asked for -- somebody looking at those two variables -- is §2 of this document.**

## 6. THE ONE CALL, AND IT IS NOT THIS SEAT'S

⛔ **IS "ANY ENROLLED E.164 NUMBER CAN BE TEXTED UNDER OPAL'S TOLL-FREE IDENTITY" THE INTENDED END STATE?**

That is the live state today: tier `PRODUCTION`, `ALLOW_UNVERIFIED=true`, no allowlist. **REC: it is intended and
stays, because an MFA factor that only texts an allowlist cannot serve real users, and the allowlist was always
described as a sandbox-era brace.** ⛔ **But it is NOT adjudicated here even under the "all open-calls ...
adjudicated by `1.0.0_SA_CTO~Z`" word**, for a reason that is not authority: **it is outbound messaging under
Opal's identity to real people**, which CLAUDE.md's autonomy section excludes from this seat
(*"Excluded: all egress off Opal infrastructure"*) and which is the same class as the carrier-verification text he
signed personally. ⭐ **His word makes me the adjudicator of CALLS; it does not convert a NEVER-class boundary into
one.**

**IF THE ANSWER IS NO, the remedy is one Terraform line and is reversible** -- restore
`SMS_VERIFIED_DESTINATIONS` and set `SMS_ALLOW_UNVERIFIED=false`, which fails closed by construction
(`.includes()` over an empty list refuses every destination). **Nothing needs to be un-sent.**

**ALSO OWED, and neither is a call:** attribution of the non-zero spend (§4), and `V3`'s clause re-cut (§5).
