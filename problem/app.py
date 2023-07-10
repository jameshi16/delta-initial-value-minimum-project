from opentelemetry import metrics, trace

meter = metrics.get_meter('james-otel-test')
counter = meter.create_counter(
    "arbitrary_counter",
    unit="count",
    description="A testing counter"
)

tracer = trace.get_tracer(__name__)

def lambda_handler(event, context):
    counter.add(1)
    return {
        "statusCode": 200,
        "body": "counter increased"
    }
