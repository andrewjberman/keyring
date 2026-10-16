# TO TCKT_MTADTA.TO-MD-r2 -- the release, part 2: Andrew's consent, the secret values, the three subscriptions, two scheduled fires, Andrew's live read

<to_id>TCKT_MTADTA.TO-MD-r2</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.7.0_AE_CloudOps~TM1</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-r-2` (`decompositions/TCKT_MTADTA_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-7, FWD-9 | **depends_on:** `MD-r-1` complete. **STAGED: the issuer flips it to `pending` after MD-r-1 closes and its probe (item 7d) read AccessDenied.**

---

## WORKER FACE

### THE CELL

`MD-r-2`: the thread goes live. The root is applied (MD-r-1). Now the Microsoft side and the secret values: the single-purpose Entra app holding `ActivityFeed.Read` on the
Office 365 Management APIs, consented by ANDREW (his act, Cloud Application Administrator), the two secret values, the three subscriptions, and two scheduled fires of the hourly
collector. Then Andrew reads one of the eight's real day (FWD-1). Read first: `data/m365_metadata/scripts/app/RUNBOOK.md`, `register_app.py`, `start_subscriptions.py`
(both dry-run by default), `infra/aws/terraform/trino/identity.tf`, PRD rows C-APP, C-SECRET, C-FIELDS, C-COLLECT.

**THE PART THAT IS ANDREW'S.** You cannot consent to the app and must not try. Item 2 is the issuer's card to Andrew. You prepare everything, then STOP and report
`WAITING ON ANDREW: consent` to `2.0.0_SA_COO~S1` by the broker; record the wait with the issuer's `unblock.py tick --owed-call` form if it gives you an id; do not poll and do not loop. The issuer
messages you when he has acted.

### ITEMS, in this order

1. **Preconditions.** MD-r-1 is complete and its three checks still print their OK tokens. The credential secret container `m365-metadata/trino/api-credentials` exists with no value.
2. **Prepare Andrew's act.** Run `python data/m365_metadata/scripts/app/register_app.py` (the DRY RUN) and `python data/m365_metadata/scripts/app/start_subscriptions.py` (dry run), read both plans, and write into your
   report the exact commands Andrew runs: he sets `M365_DELEGATED_TOKEN` (his own Graph token, the way the RUNBOOK says) and `M365_TENANT_ID`, runs `register_app.py --apply`, and grants the admin consent at the URL it
   prints. The script stores the app credential as JSON `{tenant_id, client_id, client_secret}` in the secret container (it needs AWS credentials able to `PutSecretValue` on that one secret: say in the report which
   identity Andrew should run it under, from what you measured). Then STOP (see above).
3. **After Andrew's word (the issuer will message you):** confirm `python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r2.py app` is OK for the credential. Put the SECOND secret's value, the
   subject-hash key, without ever printing it: `python -c "import secrets, boto3; boto3.client('secretsmanager').put_secret_value(SecretId='m365-metadata/trino/subject-key', SecretString=secrets.token_urlsafe(48))"`
   (the value exists only inside that process).
4. **Start the three subscriptions.** Obtain a Management API token with the app credential (a client-credentials call to the tenant's token endpoint, scope `https://manage.office.com/.default`), keep it in the process
   environment only, and run `python data/m365_metadata/scripts/app/start_subscriptions.py --apply` with `M365_TENANT_ID` and `M365_ACCESS_TOKEN` set. Print HTTP statuses only. Write the UTC time in ISO form to
   `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/subs_started_at.txt` and commit it. The Entra sign-in feed `Audit.AzureActiveDirectory` is NOT subscribed (PRD C-FIELDS (a)).
5a. **AMENDED 2026-10-16 ~13:5xZ -- the first live fire timed out (row D1-S12).** The 13:31Z fire, and its two retries, hit the 300-second limit (`Status: timeout`); the cause is a 7-day cold-start backlog fetched one blob at a time with nothing saved before the limit. `TO-MD-x2` is reopened with a time budget,
   parallel fetch and `timeout = 900`. The issuer messages you when that repair is MERGED. Then: `bash infra/aws/lambda/m365-metadata-collector/build.sh`; `terraform plan` must show an in-place update of the collector function only (code hash and timeout), nothing destroyed or replaced; one
   `bash .tools/safe-apply.sh ... apply <plan>` under a ledger entry of its own; and write the UTC time of that apply, ISO form, to `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/fires_since.txt` and commit it. The earlier failed invocations then do not count against AC3. You write no code in the collector.
   Do NOT invoke the collector by hand for the criterion; the scheduled fires are the acceptance. A fire after the repair may stop early with `complete=False` while the 7-day backlog is worked off (it saves what it did); that is not a failure. Report the log line each fire prints (counts only).
5. **Two scheduled fires.** The collector fires hourly on its own clock. Do NOT invoke it by hand for the criterion (an ad-hoc run is QA only; the scheduled fire is the acceptance). Wait for two fires after the start time
   (about two hours), then run the three checks from the repository root. **The first content may take up to 12 hours to appear (the vendor's word); the criteria below do not need content, only two clean fires.**
6. **The admin GetObject probe (the CTO's FWD-8 criterion, deferred from MD-r-1).** Once the first clean fire has written the cursor, run `r2_check_r1.py getobject` from the repository root: an admin `GetObject` on the EXISTING
   cursor key must read AccessDenied (a missing key reads NoSuchKey, which proves nothing).
7. **Hand over.** Report to the issuer: the check lines, the HTTP statuses of the starts, the time the subscriptions started. State in the report how Andrew runs the door scripts with his MFA session (the group's invoke now
   requires `aws:MultiFactorAuthPresent`): the exact commands to obtain a session token with his MFA device and the environment variables boto3 reads, without any secret. The issuer cards Andrew for his live read of FWD-1 and the first-content read.

### ACCEPTANCE

<criterion id="MD2-r2-AC1" cell_refs="MD-r-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r2.py app</invocation><expect>R2-APP-OK</expect></criterion>
`MD2-r2-AC1` -- the credential secret holds a JSON value with `tenant_id`, `client_id` and `client_secret`, and the subject-key secret holds a value of 32 characters or more (only the key names are printed).

<criterion id="MD2-r2-AC2" cell_refs="MD-r-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r2.py subs</invocation><expect>R2-SUBS-OK</expect></criterion>
`MD2-r2-AC2` -- the Management API lists exactly the three subscriptions enabled: `Audit.Exchange`, `Audit.General`, `Audit.SharePoint`.

<criterion id="MD2-r2-AC3" cell_refs="MD-r-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r2.py fires org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/fires_since.txt</invocation><expect>R2-FIRES-OK</expect></criterion>
`MD2-r2-AC3` -- at least two scheduled collector invocations since the time in `fires_since.txt` (the redeploy of item 5a), none of them a timeout or an error.

<criterion id="MD2-r2-AC4" cell_refs="MD-r-2" judgment="true"/>
`MD2-r2-AC4` -- JUDGMENT, graded by the CVO at L9, never by you: Andrew names one of the eight and a trading day and reads that person's Microsoft 365 day in order from collection that is actually running, and recognises it as that person's day (PRD FWD-1). You do not run, grade or claim this one.

<criterion id="MD2-r2-AC5" cell_refs="MD-r-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py getobject</invocation><expect>R1-GETOBJECT-OK</expect></criterion>
`MD2-r2-AC5` -- (a fourth mechanical criterion, with this reason: the CTO's ruling, msg 6614, moved the admin GetObject probe here because it needs an object that exists) an admin `GetObject` on the existing cursor key reads AccessDenied.

<expected_criteria>MD2-r2-AC1,MD2-r2-AC2,MD2-r2-AC3,MD2-r2-AC4,MD2-r2-AC5</expected_criteria>

Dry-run at the base 2026-10-16 ~08:5xZ: AC1 `R2-APP-REFUSED the credential secret has no readable JSON value`, AC2 `R2-SUBS-REFUSED no credential`, AC3 `R2-FIRES-REFUSED ...` -- each FAIL as expected. All three are reads; they print no value.
(AC4 is the judgment criterion: FWD-1's live read is the round's exercised outcome and only Andrew can give it.)

## BOUNDS

- **Grant.** AWS: `secretsmanager:PutSecretValue` on the subject-key secret only; get of the two secrets for the checks; CloudWatch Logs reads. Microsoft: the Management API subscription starts and the token call, with the app's own credential; NOTHING else.
  Repo: `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`, the `deliverables/0.7.0_AE_CloudOps~TM1/` folder, the investigation file, and this order's file.
- **You never perform or fake Andrew's consent**, never run `register_app.py --apply` yourself, never read the Entra tenant with any other credential, and never read stored objects or invoke the door.
- **NEVER** print, log, echo, write to a file or put in a message any secret value, token, tenant id or client id. The sign-in feed is not subscribed. No alarm, SNS or notification resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in the ledger and file a NEW surprise row (id `TCKT_MTADTA-D1-WTM1-S<k>`). Do not weaken the test.
- Commit only through `.tools/safe-commit.sh` with your own `--author`, `-F` a message file written with the Write tool, and `-- <paths>`.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/subs_started_at.txt
org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/fires_since.txt
infra/aws/terraform/trino/collector.tf
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP_R2.md</decomp_doc> (round 2), cell `MD-r-2`.
<owned_cells>MD-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD2-r2-AC1, MD2-r2-AC2, MD2-r2-AC3, MD2-r2-AC4, MD2-r2-AC5. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/TCKT_MTADTA.TO-MD-r2.identity-and-fires.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD2-r2-AC1,MD2-r2-AC2,MD2-r2-AC3,MD2-r2-AC4,MD2-r2-AC5` BEFORE the flip. AC1-AC3 and AC5 mechanical; AC4 judgment (UNVERIFIABLE-BY-INSTRUMENT, graded by the CVO).
</proof_of_spec>

**PER-STEP LINES (AMENDED 2026-10-16 ~13:2xZ, Andrew's ask relayed by the CTO, msg 6698):** send `2.0.0_SA_COO~S1` ONE line by the broker as each of these lands, never a value: (1) the `r2_check_r2.py app` result; (2) the subject key written (yes/no, length only);
(3) each of the three subscription starts with its HTTP status, or the API's refusal VERBATIM (the unified audit-log check was never run, so a refusal is the measure; send it once and make no retry loop); (4) each of the two fires as it reads clean. The issuer relays them.

**REPORT:** the commands Andrew runs (as in item 2); the three check lines; the subscription HTTP statuses; the start time; every refusal and denial verbatim. No secret, tenant or client value.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the hourly rule read back by two consecutive scheduled fires (AC3). BLIND: a fire that lands content is not required by the criterion; the first content may take up to 12 hours (vendor).
comp-iam: DECLARED-NOT-APPLICABLE for this order -- no principal is created; Andrew's group membership is his word and the issuer's message.
comp-adversary: DECLARED-NOT-APPLICABLE -- the credential never leaves the process; AC1 prints key names only.
lane: WORLD, a CloudOps seat under the change-management entry of MD-r-1; the consent is Andrew's act (PRD OPEN AT ANDREW), qualified as an essential wait with its owner.
</preflight>

**ISSUER NOTES:** Source: CTO round-1 analysis items 1(b)-(d) and 4; PRD v0.4. The first-content read is `data/m365_metadata/scripts/silver/first_content.py` (MD-x-3), run by a group member; its output is counts only.
