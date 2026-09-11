# ANDREW-DIRECT 2026-09-11 ~14:5xZ -- THE YCHARTS RUNNER MAY BE STARTED (the export render host, IRPT_BCKEND W4-S14)

**Terminal:** `1.0.0_SA_CTO`, in answer to the RESERVED card put to him at 14:47Z (option (a): start `irpt-ycharts-runner`
for an export RENDER; the CVO's classification 14:51Z: the render is outside the vendor class, the lifecycle stayed reserved
on the EC2 stop clause). **Recorded by:** `1.0.0_SA_CTO`, same turn.

## VERBATIM AND ENTIRE

> Yes ycharts runner may be started

## WHAT IT SETTLES

- **Option (a) is taken.** `irpt-ycharts-runner` (`i-0167fd745ad906a66`, held stopped by `aws_ec2_instance_state.runner` in
  `infra/aws/terraform/investor-reporting/ycharts/`) MAY BE STARTED for the export render -- IB-rt-8 arm (a), FWD-8's served
  PDF -- by `2.0.0_SA_COO~B`'s order as the README at `infra/aws/ec2/investor-reporting-export/README.md` writes it: start,
  `ssm send-command irpt-export-render-run`, and return to the declared state.
- **No vendor act rides on it.** The render performs no YCharts sign-in, request or cookie use; the sign-in gate on that host
  is untouched by this word (the CVO's reading: a purely internal render is outside the sign-in decision class).
- **The ycharts root header** (`instance.tf:9-17`, and the output description at `:124` that calls a bare start a vendor
  call) is amended by the lane in the same act to say that a start FOR A RENDER is not the gated sign-in, so the next actor
  does not re-derive this.
- **Returning the host to STOPPED** after the render is the root's DECLARED state (`aws_ec2_instance_state.runner`), so
  the render cycle ends where Terraform already holds it; the CTO reads his word as authorizing the cycle that ends there,
  not a host left running. Stated here rather than assumed; one word from him changes it.
- Option (b) (a Chromium AMI build) is not taken and is not needed.

## WHAT IT DOES NOT SETTLE

- The authenticated print-route session the host needs (IB-rtb-1's territory) -- a build item, not a word.
- Any other start of that host, for any other purpose; the sign-in gate stands.
