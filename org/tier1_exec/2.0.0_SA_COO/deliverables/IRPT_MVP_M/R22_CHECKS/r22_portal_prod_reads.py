"""Round 22 (~M) served-bundle after-read: does the SERVED portal PROD bundle admit `account_masks` (AD-10 release
step 2; CTO condition @ee4bc93257) and read `CATEGORY` (L0 release step 2; TO-IB-m22-222 step 0)?

Reads the served bundle from its origin bucket (s3://opalinvest-portal, the CloudFront S3 origin), starting at the
served index.html, following every script asset it references, and searching the served JS bytes. Prints
PROD-READS account_masks=<y/n> CATEGORY=<y/n> <index ETag> <assets n>, rc 0 only when both are present.
Read-only; no write.
"""
import re
import sys

import boto3

BUCKET = "opalinvest-portal"


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    idx = s3.get_object(Bucket=BUCKET, Key="index.html")
    html = idx["Body"].read().decode("utf-8", "replace")
    assets = sorted(set(re.findall(r'(?:src|href)="/?([^"]+\.js)"', html)))
    if not assets:
        print("NOT-READ: index.html (ETag %s) references no .js asset" % idx.get("ETag"))
        return 1
    seen, queue, blob = set(), list(assets), []
    while queue:
        key = queue.pop()
        if key in seen:
            continue
        seen.add(key)
        try:
            body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 -- a missing chunk is reported, never skipped silently
            print("NOT-READ: asset %s unreadable (%s)" % (key, type(exc).__name__))
            return 1
        blob.append(body)
        for chunk in re.findall(r'["\'](?:\./|/)?(assets/[A-Za-z0-9_.-]+\.js)["\']', body):
            if chunk not in seen:
                queue.append(chunk)
    text = "\n".join(blob)
    masks = "account_masks" in text
    cat = bool(re.search(r"""["']CATEGORY["']""", text))
    print("PROD-READS account_masks=%s CATEGORY=%s index=%s assets=%d"
          % ("y" if masks else "n", "y" if cat else "n", idx.get("ETag"), len(seen)))
    return 0 if (masks and cat) else 1


if __name__ == "__main__":
    sys.exit(main())
