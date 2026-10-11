# ADVI_FIRMBKTS task order -- `FB-g-29` -- THE INVOCATION CENSUS FOR ACT 4'S WIDENED SAMPLE (EIGHT IRPT CONSUMERS AND THE VALIDATOR)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-29</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~51</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census of repository files; nothing is changed or applied.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant: you read files only. Do not invoke any function.
comp-adversary: RUN by the issuer -- at base the census file does not exist and `r4_invoke.py` reads 0 of 4 (V1 to V4 FAIL by construction). Blindness: the check proves that the cited lines exist and carry the chain token; it cannot prove an event runs. The act-4 actor invokes each event once and records the result.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-29` (round 4, workstream `INVOKE`; the CTO's act 3b CTO half and act 4 ADDENDUM 2)

After the flip, act 4's sample is WIDENED: each of the eight IRPT consumers and the edge validator must make ONE real
invocation that exercises its read of the ownership map at the canonical home (an IAM simulation cannot see an organization
SCP). The actor needs, per function, the smallest event that reaches the ownership read WITHOUT a side effect. You write that
census from the repository. You invoke nothing.

### 1a. What to produce (the whole spec)

One JSON file `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/IRPT_INVOCATION_CENSUS.json`: an object `{"entries": [ ... ]}` of exactly NINE entries, each once, in this order of `function`:
`irpt-49f-reporting-read-lambda`, `irpt-directory-search`, `irpt-export-render`, `irpt-holdings`, `irpt-narrative`,
`irpt-performance-adapter`, `irpt-status`, `irpt-ycharts-generate`, and `auth-validator-edge`. Each entry has these keys:
- `function`: the name above; `kind`: `"irpt-consumer"` or `"edge-validator"`;
- `handler`: the handler's `module.function` as the function's configuration names it (read the function's Terraform root
  under `infra/aws/terraform/investor-reporting/<root>/` or, for the validator, `infra/aws/terraform/` and
  `infra/aws/lambda-edge/`; the source folder of each IRPT function is in `infra/aws/lambda/ci/lambda-source-map.json`);
- `event`: a JSON OBJECT, the smallest event that reaches the ownership read (an API-gateway-shaped object for an HTTP
  function, the direct-invoke shape for a service function; build it from a test fixture in that function's own tests where
  one exists, else from the fields the handler's entry reads);
- `reads_ownership`: `true` if that event reaches `load_ownership` (IRPT, `_authz/loaders.py:241`) or the validator's
  ownership read; `false` otherwise, with the reason in `side_effects`;
- `call_chain`: a list of `"path:line"` strings from the handler's `lambda_handler` line to the line that calls the
  ownership read, each line verified by you in the file at the tree;
- `side_effects`: `"none"` or one sentence naming each write, email, queue send or table put the event would cause;
  `invoke_recommended`: `true` when `side_effects` is `"none"`, else `false`;
- `source_of_event`: `"path:line"` of the fixture or the entry code the event was built from;
- `before_flip`: the S3 bucket and key the ownership read addresses BEFORE act 4 (the routed bucket's legacy key), and
  `after_flip`: the canonical bucket and key AFTER (`advi/49financial/platinum/49financial/ownership_map.json` for the IRPT
  consumers' read, `_authz/loaders.py:75-76`), each as `"bucket/key"` read from the code and the generated lists
  (`firm-config.mjs` for the validator), never typed from memory.

### 1b. Rules

1. Read only. Do not call AWS, invoke a function, run a test that writes, or edit any repository file.
2. If a function's event cannot reach the ownership read without a side effect, say so: `reads_ownership` true,
   `side_effects` naming the write, `invoke_recommended` false. Do not invent an event you could not build from the tree.
3. Seven or more of the nine entries must read `"none"`. If fewer can, file a surprise row naming each and stop.

## 2. BOUNDS

1. The only file you write is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/IRPT_INVOCATION_CENSUS.json`, plus your surprise rows and proof instance under your own deliverables folder.
2. No keys or ids of clients appear in the census: a firm token is fine, a client or advisor identifier is not.
3. ASCII only. If something cannot be met, file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/ADVI_FIRMBKTS.TO-FB-g-29.irpt-invocation-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-29"><invocation>cd /c/dev/wk-firmbkts-51 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_invoke.py --arms census --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51/IRPT_INVOCATION_CENSUS.json --root /c/dev/wk-firmbkts-51; echo "exit=$?"</invocation><expect>ROUND 4 INVOKE CENSUS: 4 of 4 arms</expect></criterion>
</proof_of_spec>

AC1 reads the file against the tree: nine entries each with every key; every call-chain line exists and carries its token;
every event is a non-empty object whose source exists; at least seven entries have no side effect. The invocation terminates
inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-29.irpt-invocation-census.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~51`.
Commit the census, your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it). Row
ids: `ADVI_FIRMBKTS-D1-W51-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1's output, the count of
entries with `side_effects` none, any entry with `invoke_recommended` false and its reason, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's act 3b CTO half (msg 3932: simulation closes 3b; act 4's sample is widened to one real
invocation per admitted principal because a simulation cannot see an SCP). The act-4 actor (`0.7.0_AE_CloudOps~FB1` for the
eight IRPT roots; the laptop lane for the validator) invokes each event once after the flip. Workstream `INVOKE`. Class LOCAL
(a census; no paths outside the deliverables folder).

<status>pending</status>
<round>4</round>
<workstream>INVOKE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-29</to_id>
<slot>~51</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
