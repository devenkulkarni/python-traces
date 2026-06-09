from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

resource = Resource.create({
    "service.name": "multiplication-table-app"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())


provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("table-tracer")

number = [ 2, 5 , "ten"]

with tracer.start_as_current_span("Generate Table") as parent_span: 
    try:
        print("Hello, This is a Table generation python app!")
        for num in number:
            with tracer.start_as_current_span(f"Generate Table for {num}") as child_span: 
                child_span.set_attribute("table.number",int(num))
                for i in range(1, 11):
                   print(f"{num} x {i} = {num * i}")
    except ValueError as e:
        raise
