from clearml import PipelineDecorator


@PipelineDecorator.component(name="example", execution_queue="Eugene", repo="/home/ajecc/work/tests/some_repo/.git")
def example():
    from some_utils import some_function

    a = some_function()
    print(a)
    return a


@PipelineDecorator.pipeline(
    name="example_execute",
    project="example_execute",
    version="0.0.1",
    start_controller_locally=True,
    repo="/home/ajecc/work/tests/some_repo/.git",
)
def execute_pipeline():
    a = example()
    print(a)


if __name__ == "__main__":
    execute_pipeline()
