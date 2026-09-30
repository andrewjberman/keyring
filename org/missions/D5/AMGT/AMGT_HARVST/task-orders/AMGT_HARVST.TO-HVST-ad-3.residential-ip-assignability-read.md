# AMGT_HARVST task order -- `HVST-ad-3` -- ROUND 31 chain 3: THE RESIDENTIAL-IP ASSIGNABILITY READ -- CAN OPAL's EXISTING BRIGHT DATA RESIDENTIAL EGRESS BE BOUND TO AN EC2 HARVESTER HOST, READ FROM THE ASTN AND BD BOXES' OWN CONFIGURATION (FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ad-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~89</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY: repo files, and AWS describe/list reads of the named EC2 hosts and their security groups and Secrets NAMES. NO vendor call (no Bright Data API, no proxy request, no publisher), NO write anywhere except this cell's deliverables.
comp-adversary: RUN at L5 -- the adversary is a "yes" read from a document or a comment rather than from the configuration that actually routes traffic. AC1 requires every verdict line to cite the file and line (or the AWS resource and field) it read, and to class each as MEASURED (configuration) or INFERRED (prose).
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL.** No Bright Data API or proxy request, and no publisher request. Reads only.
2. **No secret VALUE** is printed or written. Name secrets and zones by name only.
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~89/scripts/`; outputs named `ad3_*`.
4. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~89/AMGT_HARVST.TO-HVST-ad-3.residential-ip-assignability-read.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-ad-3.residential-ip-assignability-read`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~89/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE QUESTION (cloud ruling section 0, cell 4; Andrew: "If we can assign our existing bright data residential IP to an EC2 box to do this, then great")

Read the configuration that ACTUALLY routes the existing Bright Data traffic.
- **Where to look:** `infra/aws/ec2/EC2_MANIFEST.json`, `infra/aws/ec2/astn-wsjft/`, `infra/aws/ec2/bd-*-auto-login/`, and
  `infra/logic/registry/{systems,resources}.json`. Plus AWS describe reads of the hosts they name.
- **What to answer**, each with its source:
  1. **Which Bright Data product and zone:** residential, ISP, datacenter, or Web Unlocker. Is it a fixed IP or a rotating
     pool? Is the proxy endpoint a superproxy host and port?
  2. **How the existing hosts reach it:** is the EC2 host a proxy CLIENT of the Bright Data superproxy, or is the IP bound to
     the host? Name the file and line where the proxy URL or credential name is set.
  3. **Whether a second EC2 host can use the same egress:** zone allowlists, IP whitelisting of the caller, per-host
     credentials. Only as the configuration shows it, and anything not shown is INFERRED.
  4. **The verdict:** `ASSIGNABILITY: ASSIGNABLE | NOT-ASSIGNABLE | UNDETERMINED`, with the one-line reason and its class
     (MEASURED / INFERRED).

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ad-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~89/scripts/ad3_ac1_assignability.py</invocation><expect>VENDOR CALLS: 0</expect></criterion>
</proof_of_spec>

**What AC1 must print:**
- each of the four answers, with its source (file:line, or AWS resource.field) and its class (MEASURED / INFERRED);
- the line `ASSIGNABILITY: <verdict>`;
- the line `VENDOR CALLS: 0` (sockets to non-AWS hosts blocked and counted).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round30.md` @`6adebef352` section 4 item 3; cloud ruling section 0 cell 4 (Andrew's answer 1).
- **Measured at the cut:** the Bright Data / residential tokens appear in `infra/aws/ec2/EC2_MANIFEST.json`,
  `infra/aws/ec2/astn-wsjft/*`, `infra/aws/ec2/bd-cot-auto-login/*` and `bd-49f-auto-login/*`, and in
  `infra/logic/registry/{systems,resources}.json`, among 15+ files. The worker reads them to their configuration lines.
- **A LOCAL read with no pair.** The verdict is input to phase 2 (the cloud host), which waits until phase 1 matures.
- **Cross-firm note (CLAUDE.md NEVER):** `bd-*` hosts may belong to another firm's pipeline. The read quotes configuration only,
  and nothing here references another firm's data.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>31</round>
<slot>~89</slot>
<fabric>site-z</fabric>
