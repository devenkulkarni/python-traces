from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("table-tracer")

number = [ 2, 5 , "ten"]

with tracer.start_as_current_span("Generate Table") as span1: 
    try:
        print("Hello, This is a Table generation python app!")
        for num in number: 
            span1.set_attribute("table.number",int(num))
            for i in range(1, 11):
               print(f"{num} x {i} = {num * i}")
    except ValueError as e:
        #print(f"Error in printing table for {number}", number, f"Error: {e}")
        #pass
        raise
