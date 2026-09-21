# AMGT_RESAPP task order -- `AMGT-rk-82` -- H0-iam: ADD read grants on the new-grammar harvest prefixes to the two served roles (opal-amgt-scoped-api-role +8 prefixes, amgt-resapp-chatter-axis-lambda-role +4), both limbs (GetObject ARN + ListBucket s3:prefix), by ONE targeted safe-apply under a never-widen pair; no existing grant removed, no reader switched

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-82</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~82</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits two Terraform locals lists and applies two IAM role
  policies; it arms no cron, alarm, monitor or cadence, and the chatter-axis schedule (chatter-axis-schedule.tf's
  scheduler resources) is neither read for change nor written (scope checked: the targeted apply names exactly
  aws_iam_role_policy.scoped_amgt_api_grants and aws_iam_role_policy.chatter_axis_lambda). It OPENS one deploy-ledger
  entry before the apply and CLOSES it on the post-apply policy read.
comp-iam: RUN -- `comp-iam stats` @b832f7b03e: 214 Terraform IAM roles parsed, 190 services scanned, 1139 operations,
  330 permission gaps estate-wide (none on either role below); `comp-iam role opal-amgt-scoped-api-role`: 5
  statements (4 in the inline policy opal-amgt-scoped-api-grants + the attached logs policy), the two pool statements drawing on local.scoped_amgt_pool_prefixes (13 prefixes); `comp-iam role
  amgt-resapp-chatter-axis-lambda-role`: 4 statements, the two pool statements drawing on
  local.chatter_axis_pool_prefixes (4 prefixes); `comp-iam live`: 248 live roles from the graph, full-derive vintage
  2026-09-21T02:00:23Z (the graph is BLIND to any change after that vintage -- the worker's AC3 read of the live
  policy documents is the authority, not the graph). A targeted `terraform plan` on both policies at the cut read "No
  changes" (Terraform == live, 2 of 2).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~82`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/`, `infra/aws/terraform/harvest/scoped-amgt-api.tf` and `chatter-axis-schedule.tf` exist; if any is
absent, STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~82;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-82` (H0-iam, round 21 wave 1)

**The acceptance of record (`1.0.0_SA_CTO~Z`, msg 24090), verbatim:** *"ROUND 21 (2.0.0_SA_COO~Z): waves 1 + 2
(H0-store, H0-iam, H1-H6) = 8 cells is ACCEPTED ... only when (i) both v0.17 halves are signed (LIMB 6), (ii) Z-S203
has disarmed so the builder prints harvest, and (iii) rk-79 has drained, for H4/H5."*

**The contract, `prd/AMGT_RESAPP_PRD.md` v0.17 @`6f39881c3c`:**
- `:856-857` C-HARVEST-HOME, verbatim: *"AMGT_RESAPP's bronze, silver, gold, platinum, state and code live exactly
  where the builder prints them."*
- `:897-903` C-FORMAT-SEQUENCE, verbatim: *"Each move of served objects carries its own never-widen pair, and the
  source path's readers switch and the source path retires in the SAME window ... 'Retire' means that in the move's
  window the old path's readers are switched, its writers are stopped, and its read grant is removed."*
- **So this cell ONLY ADDS grants.** Removing an old prefix's grant is the job of each MOVE cell (M1-M4, a later
  round), inside that move's window. A reader reading a new prefix before its move is harmless, because nothing is
  there yet.

**THE MEASURED STATE (issuer, HEAD `b832f7b03e`, builder re-read at `ec4e000709` after Z-S203's fix @`10bace8916`; RE-READ at your branch HEAD before editing):**
- `infra/aws/terraform/harvest/scoped-amgt-api.tf`: `local.scoped_amgt_pool_prefixes` has 13 entries:
  `publication-links/v1/`, `publications/v1/`, `universe/v1/`, `crosswalk/v1/`, `filings/v1/`, `drafting/v1/`,
  `peers/v1/`, `management/v1/`, `posture/v1/`, `derived/model_block/`, `packs/`, `raw/` and `scores/v1/`.
  - The list feeds TWO statements of `aws_iam_role_policy.scoped_amgt_api_grants`:
    - `ReadThePoolPrefixesTheAdapterReads`: `s3:GetObject` on `${aws_s3_bucket.harvest.arn}/${p}*`.
    - `ListOnlyThePoolPrefixesTheAdapterReads`: `s3:ListBucket`, `StringLike s3:prefix ${p}*`.
  - The file's own law, stated in its comments: *"THE TRAILING SLASH IS MANDATORY"*.
- `infra/aws/terraform/harvest/chatter-axis-schedule.tf`: `local.chatter_axis_pool_prefixes` has 4 entries:
  `publication-links/v1/`, `publications/v1/`, `crosswalk/v1/` and `universe/v1/`.
  - The list feeds `aws_iam_role_policy.chatter_axis_lambda`: `ReadThePoolPrefixesTheProducerReads` and
    `ListOnlyThePoolPrefixesTheProducerReads`.
- A targeted plan on both policies read "No changes" at the cut. The LIVE inline policies, read by the issuer with
  `iam.get_role_policy` (AC3's own invocation, dry-run, output discarded): opal-amgt-scoped-api-grants 4 statements,
  13 GetObject resources, sha256 `f85199f9b5a08635...`; amgt-resapp-chatter-axis-lambda-policy 4 statements, 4
  resources, sha256 `d60b058257b60bfb...`.
- **The new prefixes are BUILDER output:** `key(src, "harvest", tier, ...)` up to the tier segment, measured on this
  registry.
  - **For the scoped role (8):**
    - `bloomberg/harvest/bronze/`, `bloomberg/harvest/silver/`: they replace `raw/` and `derived/model_block/` at M1.
    - `seeking-alpha/harvest/bronze/`, `seeking-alpha/harvest/silver/`: `raw/seekingalpha` plus the SA article
      silver, at M3.
    - `sec/harvest/silver/`: the `filings/v1` derived records become silver `filing_section`, at M2.
    - `barrons/harvest/silver/`, `wsj/harvest/silver/`, `ft/harvest/silver/`: the publication bodies, at M4.
  - **For the chatter role (4):** `barrons/harvest/silver/`, `wsj/harvest/silver/`, `ft/harvest/silver/` and
    `seeking-alpha/harvest/silver/`, the publications it reads, at M4.
  - Sibling-stem overlap with the existing 13 entries is 0; each new entry carries its trailing slash.

**RULED, what you do:**
1. **Append** the 8 prefixes to `scoped_amgt_pool_prefixes` and the 4 to `chatter_axis_pool_prefixes`.
   - Each appended entry sits under one comment block naming this cell, the pair, and "added by H0-iam; the OLD
     prefix's grant is removed by its MOVE cell, never here".
   - Existing entries are unchanged, in order.
   - No statement, Sid, action, condition or other resource changes.
2. **ONE targeted apply:**
   `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -auto-approve -lock-timeout=60s -target=aws_iam_role_policy.scoped_amgt_api_grants -target=aws_iam_role_policy.chatter_axis_lambda`
   - It runs only after AC3's pre-act read.
   - Its plan must read `0 to add, 2 to change, 0 to destroy`. Anything else is a STOP with no apply.
3. **Deploy ledger:** `python .tools/deploy_ledger.py open --slug amgt-rk82-harvest-iam-grants ...` BEFORE the apply,
   and `close-leg` + `close` on AC5's proof.
4. **Rollback, if AC5 fails:**
   - Restore the two locals lists to their pre-act bytes, which are AC3's snapshot in `.scratch/r82/`.
   - Re-run the same targeted apply.
   - Re-read both policy documents: their sha256 must equal AC3's pre-act hashes.
   - Nothing is deleted.

## 2. WHERE THIS CAME FROM

- **Round 21**, decomposition s.29, cut by `2.0.0_SA_COO~Z`.
- The proposal it comes from: `HARVEST_CHAIN_DECOMP_PROPOSAL`, cell "H0 iam", which reads *"ADD read grants on the
  new `{vendor}/harvest/{bronze,silver}/` prefixes (both limbs: GetObject ARN + ListBucket `s3:prefix`)"*.
- The CTO's rulings: msg 24090 (the shape) and msg 24086 (the builder binds).
- PRD v0.17 @`6f39881c3c`.
- **The pair:** `ledger/NEVER_WIDEN_ROUND21_RK82_{COO,CTO}_HALF.md`.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
infra/aws/terraform/harvest/chatter-axis-schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~82/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-82.harvest-iam-grants.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch goes in `<your worktree>/.scratch/r82/` only.
- **Collision check, done at the cut:** rk-81 writes `lib/research/harvest/`, the wave-2 channel cells write their
  channels' `lib/`/`integrations/` files, and round-20 rk-79 writes `lib/research/management/`. NONE writes
  `infra/aws/terraform/harvest/`. The shared file `INVESTIGATION_v1.md` is append-only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~82 <0.9.0_WK_AMGT_RESAPP~82@opal.agent>" -F <msgfile> -- <paths>`.
  Commit the `.tf` edit BEFORE the apply, so the applied bytes are committed bytes. Never push, merge, rebase,
  `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **THE ONE LIVE ACT is the targeted apply of the two role policies, under the pair.**
  - Before it: AC0's builder gate, AC2's plan and AC3's pre-act read.
  - It never runs a bare `terraform apply`, never an apply without `-target`, and never touches any other resource
    (Lambda, bucket, route, table, scheduler).
- **AC0 IS A GATE:** if the REAL registry's builder still prints `opal-data-assets` for harvest bronze or silver, Z-S203
  has not disarmed. STOP, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and apply nothing.
- **REMOVE NOTHING:** no existing prefix and no existing statement. Retiring old grants is each move cell's job.
- **Standing prohibitions:**
  - No S3 read or write of objects.
  - No secret.
  - **NO alarm, monitor, SNS/SES-send, notification or freshness checker.**
  - No non-ASCII.
  - **PUSH: never** (LD-0522).
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row. It is
  never widened: never by a broader prefix, never by a wildcard, never by an extra statement.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W82-S<k>`, with disarm_owner never a worker serial (name `2.0.0_SA_COO~Z`). Append
  only.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; AC2 and AC4 run under timeout 600, the rest under timeout 120)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("validate_refusals", len(r[0])); print("builder_bronze", n.address("bloomberg", "harvest", "bronze", "refdata", "date=2026-09-21")); print("builder_silver", n.address("barrons", "harvest", "silver", "article", "date=2026-09-21")); new = [n.key(s, "harvest", t, "x", "date=1970-01-01").rsplit("/", 2)[0] + "/" for s, t in (("bloomberg", "bronze"), ("bloomberg", "silver"), ("seeking-alpha", "bronze"), ("seeking-alpha", "silver"), ("sec", "silver"), ("barrons", "silver"), ("wsj", "silver"), ("ft", "silver"))]; print("scoped_new", new)'</invocation><expect>validate_refusals 0; builder_bronze and builder_silver both begin s3://opal-data-harvest/ (measured so at HEAD ec4e000709, after 4.0.0_SA_CRO's Z-S203 fix @10bace8916 deleted the stale PRODUCT harvest row; at b832f7b03e, before it, both began s3://opal-data-assets/ -- any opal-data-assets output here is a STOP: no edit, no apply); scoped_new prints exactly ['bloomberg/harvest/bronze/', 'bloomberg/harvest/silver/', 'seeking-alpha/harvest/bronze/', 'seeking-alpha/harvest/silver/', 'sec/harvest/silver/', 'barrons/harvest/silver/', 'wsj/harvest/silver/', 'ft/harvest/silver/'] -- the 8 entries this order appends are builder output, not typed</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, re
def lst(path, name):
    t = io.open(path, encoding="utf-8").read(); body = re.search(name + r"\s*=\s*\[(.*?)\n\s*\]", t, re.S).group(1)
    return re.findall(r"^\s*\"([^\"]+)\"", body, re.M)
s = lst("infra/aws/terraform/harvest/scoped-amgt-api.tf", "scoped_amgt_pool_prefixes"); c = lst("infra/aws/terraform/harvest/chatter-axis-schedule.tf", "chatter_axis_pool_prefixes")
print("scoped", len(s), s[13:]); print("chatter", len(c), c[4:]); print("scoped_head_unchanged", s[:13] == ["publication-links/v1/", "publications/v1/", "universe/v1/", "crosswalk/v1/", "filings/v1/", "drafting/v1/", "peers/v1/", "management/v1/", "posture/v1/", "derived/model_block/", "packs/", "raw/", "scores/v1/"]); print("chatter_head_unchanged", c[:4] == ["publication-links/v1/", "publications/v1/", "crosswalk/v1/", "universe/v1/"]); print("all_slash", all(x.endswith("/") for x in s + c)); print("dupes", len(s) - len(set(s)), len(c) - len(set(c)))'</invocation><expect>scoped 21 with the tail exactly AC0's scoped_new list; chatter 8 with the tail exactly ['barrons/harvest/silver/', 'wsj/harvest/silver/', 'ft/harvest/silver/', 'seeking-alpha/harvest/silver/']; scoped_head_unchanged True; chatter_head_unchanged True; all_slash True; dupes 0 0 -- measured at the cut the lists held 13 and 4</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/harvest plan -input=false -lock=false -no-color -target=aws_iam_role_policy.scoped_amgt_api_grants -target=aws_iam_role_policy.chatter_axis_lambda 2>&1 | grep -E "Plan:|will be updated|No changes|Error"</invocation><expect>exactly two "will be updated in-place" lines (aws_iam_role_policy.scoped_amgt_api_grants and aws_iam_role_policy.chatter_axis_lambda) and "Plan: 0 to add, 2 to change, 0 to destroy." with no Error line -- read-only plan (at the cut the same plan on the unedited files read "No changes"); any other count is a STOP, no apply</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r82 && python -c 'import boto3, hashlib, json; iam = boto3.client("iam")
out = {}
for role, pol in (("opal-amgt-scoped-api-role", "opal-amgt-scoped-api-grants"), ("amgt-resapp-chatter-axis-lambda-role", "amgt-resapp-chatter-axis-lambda-policy")):
    doc = iam.get_role_policy(RoleName=role, PolicyName=pol)["PolicyDocument"]; b = json.dumps(doc, sort_keys=True).encode(); get = [s for s in doc["Statement"] if s.get("Action") in (["s3:GetObject"], "s3:GetObject")][0]; res = get["Resource"] if isinstance(get["Resource"], list) else [get["Resource"]]
    out[role] = {"sha256": hashlib.sha256(b).hexdigest(), "statements": len(doc["Statement"]), "getobject_resources": len(res)}; print(role, "sha256", out[role]["sha256"], "statements", out[role]["statements"], "getobject_resources", len(res))
json.dump(out, open(".scratch/r82/pre_act.json", "w"), indent=2)'</invocation><expect>the PRE-ACT read, run BEFORE the apply: opal-amgt-scoped-api-role statements 4 getobject_resources 13; amgt-resapp-chatter-axis-lambda-role statements 4 getobject_resources 4; each with a 64-hex sha256 saved to .scratch/r82/pre_act.json -- the rollback target. Any other count means the live policy moved since the cut: STOP, row, no apply</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -auto-approve -lock-timeout=60s -target=aws_iam_role_policy.scoped_amgt_api_grants -target=aws_iam_role_policy.chatter_axis_lambda 2>&1 | grep -E "Apply complete|Error|to add"</invocation><expect>"Apply complete! Resources: 0 added, 2 changed, 0 destroyed." and no Error line -- run only after AC0-AC3 print as expected and the deploy-ledger entry is OPEN; if the tool's time bound kills it with nothing written, verify both policies unchanged against AC3 and no state lock before ONE retry</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, hashlib, json; iam = boto3.client("iam"); pre = json.load(open(".scratch/r82/pre_act.json"))
want = {"opal-amgt-scoped-api-role": ("opal-amgt-scoped-api-grants", 21), "amgt-resapp-chatter-axis-lambda-role": ("amgt-resapp-chatter-axis-lambda-policy", 8)}
for role, (pol, n) in want.items():
    doc = iam.get_role_policy(RoleName=role, PolicyName=pol)["PolicyDocument"]; st = doc["Statement"]; get = [s for s in st if s.get("Action") in (["s3:GetObject"], "s3:GetObject")][0]; lst = [s for s in st if s.get("Action") in (["s3:ListBucket"], "s3:ListBucket")][0]; res = get["Resource"] if isinstance(get["Resource"], list) else [get["Resource"]]; pfx = lst["Condition"]["StringLike"]["s3:prefix"]; pfx = pfx if isinstance(pfx, list) else [pfx]
    print(role, "statements", len(st), "(pre", pre[role]["statements"], ") getobject", len(res), "listprefix", len(pfx), "want", n, "arn_prefix_pairs_agree", sorted(r.split(":::opal-data-harvest/", 1)[1] for r in res) == sorted(pfx), "sha_moved", hashlib.sha256(json.dumps(doc, sort_keys=True).encode()).hexdigest() != pre[role]["sha256"])'</invocation><expect>opal-amgt-scoped-api-role statements 4 (pre 4) getobject 21 listprefix 21 want 21 arn_prefix_pairs_agree True sha_moved True; amgt-resapp-chatter-axis-lambda-role statements 4 (pre 4) getobject 8 listprefix 8 want 8 arn_prefix_pairs_agree True sha_moved True -- both limbs carry the same prefix set (an S3 grant has two limbs), statement counts unchanged, nothing removed; any other value is the ROLLBACK branch (section 1 item 4)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-82"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/harvest plan -input=false -lock=false -no-color -target=aws_iam_role_policy.scoped_amgt_api_grants -target=aws_iam_role_policy.chatter_axis_lambda 2>&1 | grep -E "No changes|Plan:" ; python -c 'import io; [print(f, "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in ("infra/aws/terraform/harvest/scoped-amgt-api.tf", "infra/aws/terraform/harvest/chatter-axis-schedule.tf")]'</invocation><expect>the re-plan reads "No changes" (applied == committed); both .tf files crlf 0 and non_ascii_bytes equal to their base figures (measure the base with git show on the merge-base before editing; do not introduce any)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~82/AMGT_RESAPP.TO-AMGT-rk-82.harvest-iam-grants.proof_of_spec.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`;
   rc 0 is the verdict.
3. Close the ledger leg with AC5's output, then close the entry.
4. Flip the order's status tag to `complete` and commit.
5. Report once, naming the pre and post policy sha256 values, the prefix counts, and whether rollback fired.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES of both `.tf` files to `.scratch/r82/` before editing.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:**
- **The pair:** COO half `ledger/NEVER_WIDEN_ROUND21_RK82_COO_HALF.md` (signed at issuance) and CTO half
  `ledger/NEVER_WIDEN_ROUND21_RK82_CTO_HALF.md` (owed). Spawn only when both are on file.
- **Open question for the CTO at issuance (named in the COO half):** H0-iam grants the scoped role SILVER only for
  filings (`sec/harvest/silver/`), not `issuer-site/` or `filings-xbrl/` silver, and NOT `amgt/harvest/state/` (where
  the 180 `UNRESOLVED-SOURCE` markers become `filing_attempt`). The H2 filings cell and the M2 move decide those
  homes; their grants are added by M2 inside its own window rather than pre-granted here on a guess.

<status>complete</status>
<round>21</round>
<slot>~82</slot>
<fabric>site-z</fabric>
