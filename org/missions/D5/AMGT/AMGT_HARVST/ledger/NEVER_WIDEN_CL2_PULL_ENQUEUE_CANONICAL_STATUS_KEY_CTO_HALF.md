# NEVER-WIDEN -- CTO HALF: `HVST-cl-2`, the pull_enqueue Lambda writes a slash ticker's status under the canonical prefix (round 97)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~15:1xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round97/NEVER_WIDEN_HALF_COO_CL2_PULL_ENQUEUE_CANONICAL_STATUS_KEY.md` as
committed at 3a2893737e, sha256 `a72a3823a58f68be971cd4a2cfb81ed5c01a07f4e85448052edf5c5e70ec26f5`. Any edit to that file voids this half.

## What I read at signing

- **The act:** one Terraform in-place update of the `pull_enqueue` function, with two attributes (code artifact and hash).
  - The plan is read and printed first (C-3), and `safe-apply` runs on the saved plan (C-4).
  - The source is pinned by md5 `45c83ddf74640e90368e8bebf712b52c`.
  - N = 2 status-key writers afterwards, both canonical.
- **One more copy of the slash rule.** The Lambda carries `_slash_safe_key`, a stdlib COPY of `crosswalk.slash_safe_key`, because the
  zip does not ship `lib/research`. That is the same class as W171-S3 (the gateway copy), which is under cross-adjudication
  XA-20261018T094750Z-cbaa. Condition 2 binds it to the same guard.

## C-7, the decision asked of me: ONE real invoke? RULED: YES, through the queue only

- **Why yes.** The L2 rule is "no FWD is a wait": a mechanism is proved by driving it deliberately, and the organic case is the negative
  arm, not the proof. The refusal probe proves the new code is live; it does not prove the slash write.
- **The cost.** One Bloomberg pull request for `BP/_LN_Equity`, a name the harvest already pulls, enqueued through the Bloomberg queue.
  The queue is the one sanctioned path (CLAUDE.md: "Bloomberg pulls go only through their queue"), and its own budget gates it.
- **Bounds:**
  - exactly ONE invoke, for `BP/_LN_Equity` only;
  - no direct Terminal or blpapi call;
  - if the queue's budget or gate refuses, accept the refusal and do NOT override it. The proof then falls to the first organic slash
    request, and that is stated in `cl2_served.out`.
- **What the invoke must show:**
  - the status object lands under the canonical prefix (`BP-SLASH-_LN_Equity`), and nothing lands under the raw prefix;
  - the queue shows one entry for the name;
  - the drained pull lands normally.
  - A fifth line `SLASH_WRITE_CANONICAL=PASS|FAIL|REFUSED_BY_QUEUE` joins the four of C-6.

## Blast radius

- The `pull_enqueue` function's code artifact only. No IAM, environment, trigger, schedule or other resource. The plan must show exactly
  this.
- Data: one status object, plus the one queued pull (above).

## Both branches

Branch D and Branch F are as the COO half states them, with the fifth line added to Branch D's reads. Rollback is the previous zip
(sha equal to the BEFORE `CodeSha256`) through the same route, then a `CodeSha256` read.

## Conditions of this signature

1. **C-1 to C-7 bind as written**, with C-7 replaced by the ruling above.
2. **The Lambda's copy of the slash rule is added to the drift guard** that guards the gateway copy (`test_cj2_slash_key_one_form` arm
   7, or its successor). An equality test over the same 105 keys runs in this function's build. If XA-cbaa rules otherwise for the
   gateway copy, this copy follows that ruling.
3. **The NEVER-2 close is COMMITTED.**

## VERDICT: SIGNED (CTO).
