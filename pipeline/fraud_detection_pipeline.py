import kfp
from kfp import dsl
from kfp.dsl import ContainerOp

@dsl.pipeline(name="Fraud Detection E2E with Feast")
def fraud_pipeline():
    feature_eng = ContainerOp(
        name="feature-engineering",
        image="your-dockerhub/feast-feature-eng:latest",  # replace with your actual image.
        file_outputs={"output": "/app/output"}
    )

    train = ContainerOp(
        name="train-model",
        image="your-dockerhub/training:latest",
        arguments=["--feature-repo", "/feature_repo"],
    ).after(feature_eng)

kfp.compiler.Compiler().compile(fraud_pipeline, "fraud_pipeline.yaml")