"""SC-e-66 verify leg (CTO condition 3): the first nightly's silver/bd_assets_dim.parquet against the prior VersionId.

Needs pandas + pyarrow (a laptop seat). Reads two versions of one key in opal-data-bd; writes nothing.
  python e66_nightly_check.py [--prior yHxeKSnXyTZuiSb0Sl0buG9bAMJ_6ju0]
Prints  E66-NIGHTLY ok=<bool> cols=<n> new_nulls=<n> gld=.. phys=.. vxx=.. old_cols_equal=<n>/<n> date_dtypes_same=<bool> ...
"""
import argparse
import io

import boto3
import pandas as pd

BUCKET, KEY = "opal-data-bd", "silver/bd_assets_dim.parquet"
NEW_COLS = ("asset_class_canonical", "sub_asset_class_canonical", "class_source")
EXPECT = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}

ap = argparse.ArgumentParser()
ap.add_argument("--prior", default="yHxeKSnXyTZuiSb0Sl0buG9bAMJ_6ju0")
a = ap.parse_args()
s3 = boto3.client("s3", region_name="us-east-1")
head = s3.head_object(Bucket=BUCKET, Key=KEY)
cur = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=KEY)["Body"].read()))
old = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=KEY, VersionId=a.prior)["Body"].read()))
added = [c for c in cur.columns if c not in old.columns]
new_nulls = int(sum(cur[c].isna().sum() for c in NEW_COLS if c in cur.columns))
missing_new = [c for c in NEW_COLS if c not in cur.columns]
tick = "ticker"
picks = {}
for t, want in EXPECT.items():
    rows = cur[cur[tick].astype(str).str.upper() == t] if tick in cur.columns else cur.iloc[0:0]
    got = sorted({(r["asset_class_canonical"], r["sub_asset_class_canonical"]) for _i, r in rows.iterrows()}) if not missing_new else []
    picks[t] = got == [want]
shared = sorted(set(cur["asset_id"]) & set(old["asset_id"]))
c2 = cur.set_index("asset_id").loc[shared]
o2 = old.set_index("asset_id").loc[shared]
old_cols = [c for c in old.columns if c != "asset_id"]
equal = sum(1 for c in old_cols if c2[c].reset_index(drop=True).equals(o2[c].reset_index(drop=True)))
dates = [c for c in old.columns if "date" in c.lower()]
dtypes_same = all(str(cur[c].dtype) == str(old[c].dtype) for c in dates)
ok = (len(cur.columns) == 25 and not missing_new and new_nulls == 0 and all(picks.values()) and equal == len(old_cols)
      and dtypes_same and len(dates) == 4)
print(f"E66-NIGHTLY ok={ok} version={head.get('VersionId')} modified={head['LastModified'].isoformat()} cols={len(cur.columns)} "
      f"added={added} new_nulls={new_nulls} picks={picks} old_cols_equal={equal}/{len(old_cols)} shared_ids={len(shared)} "
      f"date_cols={dates} date_dtypes_same={dtypes_same}")
