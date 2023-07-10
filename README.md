# delta-initial-value-minimum-project

This project provides the minimum configuration required to recreate
the bug where the first set of counter metrics are not published.

This bug can be reproduced on v0.30.0 of AWS ODOT, which is v2 of the
OpenTelemetry Lambda Extension. It can also be reproduced from a fresh
build straight from the
[`aws-otel-lambda`](https://github.com/aws-observability/aws-otel-lambda)
repository.

The deployment is done via SAM CLI, with the following commands:

``` bash
sam build --use-container
sam package --s3-prefix "delta-initial-value-minimum-project" --s3-bucket "s3-bucket-name-here" --output-template-file packaged.yaml
sam deploy --stack-name "delta-initial-value-minimum-project" --template packaged.yaml --capabilities CAPABILITY_IAM --s3-prefix "sam-app" --s3-bucket "s3-bucket-name-here" --no-fail-on-empty-changeset
```

## Expected Result

On the first invocation of the Lambda (cold), and with the `emfexporter`
fixed as linked
[here](https://github.com/jameshi16/opentelemetry-collector-contrib),
the line:

``` text
{"OTelLib":"james-otel-test","Version":"1","_aws":{"CloudWatchMetrics":[{"Namespace":"delta-initial-value-minimum-project-LambdaFunction-7Ee8R5yTPgdj","Dimensions":[["OTelLib"]],"Metrics":[{"Name":"arbitrary_counter","Unit":"count"}]}],"Timestamp":1688963396605},"arbitrary_counter":1}
```

the expected metrics are exported.

## Actual Results

On the first invocation of the Lambda (cold) with v2 of the lambda
layer, no metrics are logged in `stdout`.
