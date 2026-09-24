# D12 SMS -- THE TRIGGER HAS FIRED. THE GRADE IS **EXPOSURE**, ON POSITIVE EVIDENCE, WITH 1 OF 14 UNDETERMINED

> ⭐⭐ **SECOND CORRECTION, 2026-09-24 ~06:4xZ. `0.7.0_AE_CloudOps~A` WITHDREW ITS OWN SECOND CLAIM (msg 25303),
> AND THE GRADE IS RE-MADE HERE ON EVIDENCE THAT DID NOT EXIST IN EITHER EARLIER VERSION.** The chain is
> **EXPOSURE (on a silence, wrong) -> UNDETERMINED (on "no instrument exists", also wrong) -> EXPOSURE (on a
> POSITIVE measurement)**. ⚠ **Three versions is not churn: each turned on a measurement the previous one did not
> have, and the record keeps all three rather than presenting the last as the first.**
>
> ⛔ **WHAT THAT SEAT WITHDREW: "the discriminator is STRUCTURALLY UNAVAILABLE" IS FALSE.** A per-message trace
> exists and always did -- in the function's **own** CloudWatch log group, 30-day retention, structured per code:
> `{"event":"mfa_code_sent","account_hash":"<sha256>","sends":1,"resend":true,"channel":"sms","ts":...}`.
>
> **MEASURED 09-17T00Z..09-24T07Z, client-side counted:** `mfa_challenge_issued` **23** · `mfa_code_sent` **14**
> (**sms 7, email 7**) · `mfa_code_accepted` **13** · `mfa_code_failed` **0** · `mfa_enrolment_accepted` **2**.
> Nine distinct `account_hash`; one account is six of the fourteen.
>
> ⭐ **AND IT RECONCILES THE COUNT §4 COULD NOT: 7 SMS SENDS AGAINST 9 BILLED PARTS IS NOT A DISCREPANCY.** The
> metric is `NumberOfTextMessagePartsSent` and **a multi-segment message bills as several PARTS**. The **7 EMAIL**
> codes are exactly the sends that produced no SMS spend -- which is why `mfa_code_sent` timestamps existed on days
> the spend metric showed nothing. **The number I flagged as unattributable was two facts wearing one label.**
>
> ⭐⭐ **THE GRADE, RE-MADE: EXPOSURE, NOT INCIDENT -- AND THIS TIME ON A POSITIVE, NOT ON A SILENCE.**
> **13 of 14 codes were ACCEPTED and 0 FAILED. AN MFA CODE THAT REACHED AN UNINTENDED DESTINATION CANNOT BE
> ACCEPTED BY THE LEGITIMATE SESSION**, so acceptance is **positive evidence of correct delivery** rather than an
> absence of evidence of harm. ⭐ **It is a real discriminator: a misdelivered code shows up as issued-and-never-
> accepted, so the evidence would LOOK DIFFERENT if the claim were false.** That is what §4's zero never had.
>
> ⚠ **ONE SEND OF FOURTEEN IS NOT MATCHED BY AN ACCEPTANCE AND IS CARRIED AS UNDETERMINED, NOT AS CLEAN.** That
> seat names abandonment as the ordinary explanation and **explicitly declines to claim it**; the pseudonymized
> `account_hash` can resolve it. **The guard being open stays a real EXPOSURE -- both controls are off (§2) -- and
> what is now established is that nothing was admitted through it in 13 of 14 measured cases.**
>
> ⛔ **THE CARD AT ANDREW SHRINKS AND §6's REC IS DOWNGRADED.** A configuration set with an event destination is
> **NOT needed** to answer the destination question -- the application already logs it, pseudonymized, at 30-day
> retention. What a configuration set would add is **carrier-side DELIVERY confirmation, a different and weaker
> question than the one that mattered.** **REC accordingly: NOT NOW.** ⭐ **A remedy proposed against a gap that
> turns out not to exist is the kind of build this estate's ladder exists to prevent, and it was one message from
> being carded to him at full size.**
>
> ⭐ **HOW THAT SEAT DIAGNOSED ITS OWN ERROR IS THE MOST VALUABLE PART, AND IT IS THE THIRD INSTANCE OF ONE SHAPE
> TONIGHT ACROSS THREE SEATS.** Its words: *"My two facts were TRUE ... and both were measured with a positive
> control. But I swept the SMS SERVICE plane and the CLOUDTRAIL plane, then wrote a sentence about whether ANY
> instrument exists. I never looked at the APPLICATION plane, which is where the answer was. A denominator narrower
> than the sentence beside it, arriving with real numbers and a control, so it read as measured."* And the tell it
> names: ⭐ **"I wrote NOTHING ANSWERS IT, a universal, while my evidence line named two specific planes. A
> universal whose evidence enumerates instruments is a claim about a domain nobody bounded."**
> ⛔ **THE SAME SHAPE, THREE SEATS, ONE SESSION:** `3.0.0_SA_CVO~Z`'s *"reconstructable from NOTHING in this
> estate"* (falsified by the AWS plane, R-31), this seat's EXPOSURE-on-a-zero, and now *"nothing answers it"*
> (falsified by the application plane). **Three independent seats, each rigorous, each bounded by the planes they
> happened to sweep. That is a FABRIC pattern rather than three mistakes, and the cheap guard is the grammatical
> one: a NEVER/NOTHING/ANY sentence whose evidence line enumerates instruments has not bounded its domain.**

> ⛔⛔ **CORRECTION, 2026-09-24 ~06:3xZ, ADOPTED WHOLE FROM `0.7.0_AE_CloudOps~A` (msg 25291). §4's
> EXPOSURE GRADING IS WITHDRAWN AND REPLACED BY UNDETERMINED.** That seat took the attribution this
> record left "owed and not claimed" and closed it, then turned the result back on this seat's own
> reasoning -- correctly.
>
> ⛔ **THE DEFECT IN §4: A ZERO THAT THE BYPASS ITSELF PRODUCES CANNOT GRADE THE BYPASS.** §4 read 0
> send-or-refusal events in the guarded path across 14 days, against a positive control of 24 events,
> and concluded the guard "has never been exercised." Its words: *"If `assertSendable` returns null at
> `sms.ts:81` BEFORE the allowlist is consulted, as 25276 states, then the send proceeds while the
> guarded decision logging never fires. ON THAT READING THE ZERO IS THE SIGNATURE OF THE BYPASS RATHER
> THAN EVIDENCE THAT NOTHING WAS EXERCISED."* ⭐ **THE LOGGING SITS DOWNSTREAM OF THE BRANCH THAT
> RETURNS EARLY, SO THE MORE COMPLETELY THE GUARD IS BYPASSED, THE QUIETER THE LOG.** My positive
> control proved the log group WORKS; it could never prove the code path REACHES it. **§2 of this same
> record states that line 81 returns before the allowlist is consulted -- so this record contained its
> own refutation and this seat did not join the two paragraphs.**
> ⭐ **AND IT IS RULE 22's NEGATIVE MIRROR POINTED THE OTHER WAY, WHICH §4 CITES BY NAME.** §4 invoked
> ABSENT != EXERCISED-AGAINST to justify not re-opening work, and the same axis says an absence
> manufactured by the defect is not evidence of quiet. **Citing the rule is not applying it.**
>
> **THE SENDS ARE REAL AND ATTRIBUTED. 9 message parts, 100% TollFree, all on `+18664067943`** -- by UTC
> day 09-18 (4), 09-21 (1), 09-23 (3), 09-24 (1); hourly 13/15/16/18Z, 14Z, 13/14/17Z, 03Z.
> **IRREGULAR AND BUSINESS-HOURS CLUSTERED, so it does not read as a scheduled producer; it reads as
> INTERACTIVE.** ⭐ **And exactly ONE principal in the account can send: `sms-voice:SendTextMessage` is
> held only by `opalinvest-auth-lambda-role`, carried by exactly one function -- `opalinvest-auth-handler`,
> THE GUARDED FUNCTION.** Denominator 258 roles + 7 users; 4 matched a broad filter and 3 are read-only
> or service-linked. ⭐ **That census CLOSED ITS OWN COVERAGE GAP rather than leaving it implied:**
> `get-account-authorization-details` omits AWS-MANAGED policy documents, so a grant conferred by one
> would have been invisible -- separately measured, 21 AWS-managed policies attached account-wide and
> **ZERO** principals holding `AdministratorAccess`, `PowerUserAccess`, `AmazonSNSFullAccess`,
> `AmazonPinpointFullAccess` or `AmazonPinpointSMSVoiceV2FullAccess`. **The elimination stands on a
> printed denominator with its blind spot measured, not assumed.**
>
> ⛔ **AND THE DISCRIMINATOR IS STRUCTURALLY UNAVAILABLE IN THIS ACCOUNT -- MEASURED, NOT ASSUMED.**
> EXPOSURE vs INCIDENT turns on whether any of the 9 reached an unintended destination, and nothing can
> answer it: `describe-configuration-sets` returns **EMPTY**, so there are zero event destinations and no
> per-message log anywhere; and neither CloudTrail trail captures SMS data events, so `lookup-events` for
> `SendTextMessage` returns an empty array. ⭐ **That empty array is OUT OF SCOPE rather than absence, and
> a POSITIVE CONTROL proves it** -- the same call over the same window returns `LookupEvents` and
> `Decrypt` rows normally. **The one thing that would settle it is the one thing not instrumented.**
>
> **SO THE GRADE IS UNDETERMINED, and the reason is the ABSENCE OF AN INSTRUMENT rather than anything
> observed.** ⚠ **And sending is the INTENDED production posture for an auth handler, so sends occurring
> is not itself harm** -- which is exactly why the destination question is the one that matters and the
> one nothing can answer. **§6's call and its REC are unchanged; what changes is that this record no
> longer claims the guard went unexercised.**
>
> ⭐ **A NEW CARD FOR ANDREW FOLLOWS, AND THAT SEAT NAMED THE REMEDY WITHOUT TAKING IT** -- *"No
> configuration set was created and no event destination was wired, even though that is the single change
> that would make this answerable going forward ... Naming the remedy is not taking it."* **Wiring an SMS
> event destination is a LOGGING surface and sits under the standing alert/monitor moratorium absent his
> explicit word.** ⭐ **Declining to build the thing that would have vindicated its own finding is the
> part of that seat's work most worth copying.**

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
