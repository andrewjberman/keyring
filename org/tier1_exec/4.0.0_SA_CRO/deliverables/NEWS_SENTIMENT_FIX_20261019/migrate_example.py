"""Bounded migration of the reported coal topic through the deployed batch and publisher.

prepare captures exact DynamoDB wire before-images; apply runs deployed enrichment,
conditionally patches only the reported topic's evidence fields, then republishes.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys

import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from botocore.config import Config

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/finbert_batch_processor'))
from news_contract import canonical_url, deduplicate_articles, public_context  # noqa: E402

SCRATCH = ROOT / '.runtime/news-sentiment-fix-20261019'
DDB = boto3.client('dynamodb', region_name='us-east-1')
LAM = boto3.client('lambda', region_name='us-east-1',
                   config=Config(read_timeout=850, retries={'total_max_attempts': 1}))
SERIALIZER, DESERIALIZER = TypeSerializer(), TypeDeserializer()


def unpack(item):
    return {k: DESERIALIZER.deserialize(v) for k, v in item.items()}


def query(table, field, value):
    args = {'TableName': table, 'KeyConditionExpression': '#pk = :pk',
            'ExpressionAttributeNames': {'#pk': field}, 'ExpressionAttributeValues': {':pk': {'S': value}},
            'ConsistentRead': True}
    rows = []
    while True:
        response = DDB.query(**args)
        rows.extend(response['Items'])
        if 'LastEvaluatedKey' not in response:
            return rows
        args['ExclusiveStartKey'] = response['LastEvaluatedKey']


def invoke(name, event):
    response = LAM.invoke(FunctionName=name, Payload=json.dumps(event).encode())
    output = json.loads(response['Payload'].read())
    if response.get('FunctionError') or output.get('statusCode') != 200:
        raise ValueError('invoke_failed: ' + name)
    return json.loads(output['body'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'apply'])
    args = parser.parse_args()
    path = SCRATCH / 'backup/example-before-wire.json'
    if args.mode == 'prepare':
        if path.exists():
            print('BEFORE-IMAGE ALREADY CAPTURED; preserved')
            return
        date = datetime.now(timezone.utc).date()
        topics = query('opal-news-trending-daily', 'date', str(date))
        topic = next(t for t in topics if 'South Korea Returns to Coal' in unpack(t).get('headline', ''))
        urls = {canonical_url(a['url']) for a in unpack(topic)['top_articles']}
        rows = []
        for offset in range(7):
            rows.extend(r for r in query('opal-news-articles', 'article_date', str(date - timedelta(days=offset)))
                        if canonical_url(unpack(r).get('url')) in urls)
        path.write_text(json.dumps({'topic': topic, 'articles': rows, 'urls': sorted(urls)}, indent=2))
        print('CAPTURED', len(rows), 'article rows;', len(urls), 'distinct URLs; one topic')
        return
    before = json.loads(path.read_text())
    result = invoke('finbert-batch-processor', {'context_only': True, 'max_articles': 10, 'urls': before['urls']})
    (SCRATCH / 'example-invoke.json').write_text(json.dumps(result, indent=2))
    journal = []
    lookup = {}
    for old in before['articles']:
        key = {k: old[k] for k in ('article_date', 'url_hash')}
        new = DDB.get_item(TableName='opal-news-articles', Key=key, ConsistentRead=True)['Item']
        for field in ('sentiment_finbert', 'sentiment_finbert_label', 'sentiment_finbert_confidence'):
            if old.get(field) != new.get(field):
                raise ValueError('raw_sentiment_changed')
        if new.get('news_context') != old.get('news_context'):
            journal.append({'table': 'opal-news-articles', 'key': key, 'attribute': 'news_context',
                            'before': old.get('news_context'), 'after': new['news_context']})
        item = unpack(new)
        lookup[canonical_url(item['url'])] = item
    folder = SCRATCH / 'journals'
    folder.mkdir(exist_ok=True)
    # Persist after-images before evaluating acceptance, so partial enrichment is reversible.
    (folder / 'example-articles.json').write_text(json.dumps(journal, indent=2))
    if result.get('failures') or any('news_context' not in a for a in lookup.values()):
        raise ValueError('incomplete_enrichment: inspect example-invoke.json')
    old = before['topic']
    topic = unpack(old)
    articles = [dict(a, **public_context(lookup[canonical_url(a['url'])])) for a in topic['top_articles']]
    unique = deduplicate_articles(articles)
    fields = {'top_articles': unique,
              'article_count': max(len(unique), int(topic.get('article_count', len(articles))) - len(articles) + len(unique)),
              'market_direction': topic['topic_rank'].split('-')[0],
              'direction_reason': topic.get('direction_reason') or topic.get('rationale') or
               'Rising energy costs and LNG supply disruption pressure broad markets; coal producers can benefit.'}
    key = {k: old[k] for k in ('date', 'topic_rank')}
    entries = [{'table': 'opal-news-trending-daily', 'key': key, 'attribute': k,
                'before': old.get(k), 'after': SERIALIZER.serialize(v)} for k, v in fields.items()]
    (folder / 'example-topic.json').write_text(json.dumps(entries, indent=2))
    names = {f'#f{i}': k for i, k in enumerate(fields)}
    values = {f':v{i}': e['after'] for i, e in enumerate(entries)}
    values.update({':old_articles': old['top_articles'], ':old_headline': old['headline']})
    DDB.update_item(TableName='opal-news-trending-daily', Key=key,
        UpdateExpression='SET ' + ', '.join(f'#f{i} = :v{i}' for i in range(len(fields))),
        ConditionExpression='top_articles = :old_articles AND headline = :old_headline',
        ExpressionAttributeNames=names, ExpressionAttributeValues=values)
    published = invoke('opal-trending-topics-portal-publisher', {})
    print(json.dumps({'enrichment': result, 'publisher': published, 'unique_articles': len(unique)}, default=str))


if __name__ == '__main__':
    main()
