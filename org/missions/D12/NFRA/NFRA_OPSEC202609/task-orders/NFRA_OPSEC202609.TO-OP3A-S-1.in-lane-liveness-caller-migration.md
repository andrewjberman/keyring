# TO NFRA_OPSEC202609.TO-OP3A-S-1 -- FWD-12: the two IN-LANE liveness callers still present a STATIC BEARER. Move them onto the gateway's exchange endpoint and show it happened (OP3A-s-1, FWD-12)

<to_id>NFRA_OPSEC202609.TO-OP3A-S-1</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.9.0_WK_NFRA_OPSEC202609~4</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged</status>

**Directive:** D12 · **Fabric:** site-z · **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14** (FWD-12) ·
**Decomp cell:** `OP3A-s-1` (issuance 3A, v0.1.0) · **Issuance:** 3A.

---

## THE CELL

Two Lambdas probe the gateway every 6 hours and each presents a **static bearer** read from Secrets
Manager. FWD-12's migration moves callers onto the gateway's **exchange endpoint** so a credential is
obtained per-call rather than held. **Five holdings exist across three secrets; three are other lanes'.
These two are THIS LANE'S and they are your whole scope.**

| caller | declared at | probe URL | credential TODAY |
|---|---|---|---|
| `opal-otp-liveness` | `infra/aws/terraform/opal-gateway/otp-liveness.tf:83-84` | `https://mcp.opalinvest.dev/otp/health` | `OTP_BEARER_SECRET_ID = "blackdiamond/49f/otp-gateway-token"` |
| `opal-ms-ingest-liveness` | `infra/aws/terraform/opal-gateway/ms-ingest.tf:86-87` | `https://mcp.opalinvest.dev/ms/health` | `MS_INGEST_BEARER_SECRET_ID = "opal/mcp/ms-ingest-token"` |

Both are stdlib-only (`urllib` + `boto3`, `archive_file` zip, no layer), both on ENABLED 6h EventBridge
rules.

## GROUNDING -- and PHASE 1 IS TO RE-TAKE IT, NOT TO TRUST IT

⛔ **THE SAFETY MEASUREMENT IN THIS FACE IS FROM THE PREVIOUS EVENING. RE-MEASURE IT BEFORE YOU CHANGE
ANYTHING.** It says dual-accept is intact -- the static bearer returned 200 on `/otp/fetch` (3 of 3 at
19:22:33/34/36Z) while no-auth and junk-auth both 401 -- and that `/otp/token` (`class=exchange`) has been
reachable through the ALB since 2026-09-09T19:14Z, before which it answered a Microsoft OIDC 302 to
everything.

**A premise older than a day is exactly what produced this project's `OP3-s-3` defect: a cell cut from a
row whose remedy had landed six days earlier.** `S3A-AC1` and `S3A-AC2` exist so that cannot repeat here.

## BOUNDS

- **THE THREE CROSS-LANE CALLERS ARE NOT YOURS.** `bd-49f-auto-login` (OpalETL), `bd-cot-auto-login`
  (PartnerETL) and the globgrph `NFRA_MSGRAPH` derive (CloudComp) are migrated **through their owning
  lanes** by Andrew's own ruling `@9382d107a3` s.1, which states it *"does NOT move the three callers into
  OPSEC's territory; PRD s.3's boundary stands."* **Do not touch their code and do not migrate them.**
- ⛔ **DO NOT RETIRE THE STATIC BEARER OR REVOKE EITHER SECRET.** Dual-accept must stay intact -- three
  other callers still depend on it. Retiring is a separate decision once all five have migrated.
- **NO ALARM, NO MONITOR, NO NOTIFICATION IS AUTHORISED BY THIS ORDER.** The standing moratorium is
  untouched, and the ruling that authorised this cut says so in terms.
- **`safe-apply` only, never bare `terraform apply`.** A deploy-ledger entry under
  `org/critical_paths/change_management/` is OPENED before any apply and CLOSED at completion.
- **If the change turns out to need a gateway-side edit, STOP and file a ROW.** The gateway app is
  `0.7.0_AE_CloudOps`'s lane, not this order's write surface.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md`
  (lane ANY; site-Z ids are `NFRA_OPSEC202609-Z-W4-S<n>`; carry `project`, `fabric`, `spec_asserts`,
  `world_is`, `class`, `hazard_standing`, `disposition`) -- then keep working. Never a message.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSEC202609~4
  <0.9.0_WK_NFRA_OPSEC202609~4@opal.agent>" -F <msgfile>` (msgfile written by a NON-SHELL writer).
  **No non-ASCII in a commit message** -- the gate refuses it.
- **Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE**, using the worktree's own copy.

## ACCEPTANCE CRITERIA

<criterion id="S3A-AC1" cell_refs="OP3A-s-1"><invocation>`git show HEAD:infra/aws/terraform/opal-gateway/otp-liveness.tf` and the same for `ms-ingest.tf`, with the credential and URL lines pasted.</invocation><expect>the four values this face names are quoted back from source, each with its file and line; any that differ from this face are stated as differences rather than silently adopted.</expect></criterion> `S3A-AC1` -- THE FACE'S GROUNDING IS RE-TAKEN FROM SOURCE.

<criterion id="S3A-AC2" cell_refs="OP3A-s-1"><invocation>a request to `https://mcp.opalinvest.dev/otp/health` presenting the CURRENT static bearer, with the request and the observed status code pasted.</invocation><expect>the status code is recorded verbatim, whatever it is.</expect></criterion> `S3A-AC2` -- DUAL-ACCEPT IS RE-MEASURED TODAY, NOT INHERITED. **This is the criterion that must be able to fail: if it is not 200, dual-accept has changed since last night, and that is a STOP and a ROW before any edit.**

<criterion id="S3A-AC3" cell_refs="OP3A-s-1"><invocation>a request to `https://mcp.opalinvest.dev/otp/token`, with the request and the observed response pasted.</invocation><expect>the response is recorded verbatim and it is stated whether it is a Microsoft OIDC 302 or something else.</expect></criterion> `S3A-AC3` -- THE EXCHANGE ENDPOINT'S ACTUAL CONTRACT IS READ FROM THE ENDPOINT. **This face deliberately does NOT specify the exchange's shape -- read it, do not assume it.**

<criterion id="S3A-AC4" cell_refs="OP3A-s-1"><invocation>the diff of `otp-liveness.tf` and any source file it packages, after the change.</invocation><expect>the diff shows `opal-otp-liveness` obtaining its credential through the exchange endpoint rather than presenting the static bearer directly.</expect></criterion> `S3A-AC4` -- CALLER 3 IS MIGRATED IN THE DECLARATION.

<criterion id="S3A-AC5" cell_refs="OP3A-s-1"><invocation>the diff of `ms-ingest.tf` and any source file it packages, after the change.</invocation><expect>the diff shows `opal-ms-ingest-liveness` obtaining its credential through the exchange endpoint rather than presenting the static bearer directly.</expect></criterion> `S3A-AC5` -- CALLER 5 IS MIGRATED IN THE DECLARATION.

<criterion id="S3A-AC6" cell_refs="OP3A-s-1"><invocation>a manual invocation of `opal-otp-liveness` after the change, with the invocation result and the function's own log output pasted.</invocation><expect>the probe reports the gateway healthy, and the log shows which credential path it took.</expect></criterion> `S3A-AC6` -- CALLER 3 STILL WORKS, EXERCISED RATHER THAN PLANNED.

<criterion id="S3A-AC7" cell_refs="OP3A-s-1"><invocation>a manual invocation of `opal-ms-ingest-liveness` after the change, with the invocation result and the function's own log output pasted.</invocation><expect>the probe reports the gateway healthy, and the log shows which credential path it took.</expect></criterion> `S3A-AC7` -- CALLER 5 STILL WORKS, EXERCISED RATHER THAN PLANNED.

<criterion id="S3A-AC8" cell_refs="OP3A-s-1"><invocation>the deploy-ledger entry under `org/critical_paths/change_management/`, read after closure.</invocation><expect>the entry is CLOSED, names its rollback, and states its push state as a MEASURED value.</expect></criterion> `S3A-AC8` -- THE LEDGER CLOSES ON THE ARTIFACT.

<criterion id="S3A-AC9" cell_refs="OP3A-s-1" judgment="true"/> `S3A-AC9` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9, NOT SELF-GRADED.** Whether FWD-12's IN-LANE half is now EXERCISED. **Record what the two probes did and offer NO verdict.**

<expected_criteria>S3A-AC1, S3A-AC2, S3A-AC3, S3A-AC4, S3A-AC5, S3A-AC6, S3A-AC7, S3A-AC8, S3A-AC9</expected_criteria>

<paths>
infra/aws/terraform/opal-gateway/
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3A-S-1.in-lane-liveness-caller-migration.md
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~4/
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3A.md</decomp_doc> v0.1.0, cell `OP3A-s-1`, issuance 3A.
<owned_cells>OP3A-s-1</owned_cells>
Read-dependencies, NOT claimed: the three CROSS-LANE callers (OpalETL, PartnerETL, CloudComp), which are migrated through their owning lanes and are out of this order's scope by Andrew's ruling.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell builds no scheduled job and no monitor; the two EventBridge rules already exist and are ENABLED, and this order does not change their cadence, their targets or their alerting.
comp-iam: RUN -- 2 of 2 roles resolved at the cut: `opal-otp-liveness-role` (tf_resource `otp_liveness`, source `infra/aws/terraform/opal-gateway/otp-liveness.tf`, 4 statements) and `opal-ms-ingest-liveness-role` (tf_resource `ms_ingest_liveness`, source `infra/aws/terraform/opal-gateway/ms-ingest.tf`, 4 statements); statement 1 on BOTH is `secretsmanager:GetSecretValue`. BLIND ON THIS SUBJECT, stated rather than implied: comp-iam reads the DECLARED (Terraform) plane, not the live one, and it did not resolve statement 1's RESOURCE ARNs on either role (they are interpolated), so this lens CANNOT say whether the existing grant's scope reaches a secret the exchange path may need. That is UNMEASURED at the cut and is the worker's to establish LIVE via `simulate-principal-policy`, one `--resource-arns` per call with the positive control as a separate invocation, BEFORE any apply.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- this issuance cites two source files and one ruling, all re-read at HEAD by the issuer at cut time and all re-taken by `S3A-AC1`.
</preflight>

<proof_of_spec>
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~4/NFRA_OPSEC202609.TO-OP3A-S-1.in-lane-liveness-caller-migration.proof_of_spec.json
</proof_of_spec>

---

## ISSUER'S NOTE, ON THE RECORD RATHER THAN BEHIND IT

**This order is TEN HOURS LATE and the delay is the issuer's.** Andrew authorised it at `@9382d107a3` s.1
(*"need no word and can cut now"*), `1.0.0_SA_CTO~Z` ruled it as round 3's OPENING order at msg 20769, and
this seat wrote it into the register as binding constraint (2) -- **then cut round 3 without it.** Recorded
as row `Z-S174` @`09c10ed9a5`.

⭐ **AND THE REASON IT STAYED INVISIBLE IS WORTH KNOWING IF YOU FILE A ROW HERE: an omission leaves no trace
in any instrument that measures what EXISTS.** The L10 distance, the slug check, the analysis check, the
ARMED census and the expiry clock were all green on it for ten hours. It surfaced because a human asked why
nothing was running.
